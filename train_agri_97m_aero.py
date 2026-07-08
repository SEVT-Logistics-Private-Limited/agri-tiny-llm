"""
AgriTinyGPT Rung 5 - ~96.7M parameters
Aeroponics ONLY - full A-Z completion: low-pressure vs high-pressure misting
systems, vertical tower vs horizontal tray systems, root zone temperature,
misting cycle timing by growth stage, chamber humidity, nutrient delivery and
foliar feeding, Pythium disease prevention, crop suitability, equipment failure
modes, and nozzle maintenance. Continues the single-domain-per-rung approach and
training stability fixes (lower LR, cosine decay, gradient clipping, best
checkpoint saved) established in Rungs 3-4.
"""
import torch, torch.nn as nn, re
from torch.nn import functional as F

torch.manual_seed(1337)
device = "cuda" if torch.cuda.is_available() else "cpu"

with open("agri_corpus_97m_aero.txt", "r", encoding="utf-8") as f:
    text = f.read()

def tokenize(s):
    return re.findall(r"\d+\.\d+|\w+|[^\w\s]", s.lower())

tokens = tokenize(text)
vocab = sorted(set(tokens))
vocab_size = len(vocab)
stoi = {w: i for i, w in enumerate(vocab)}
itos = {i: w for w, i in stoi.items()}

def encode(s):
    return [stoi.get(w, 0) for w in tokenize(s)]

def decode(ids):
    words = [itos[i] for i in ids]
    out = ""
    for w in words:
        if re.match(r"^[^\w\s]$", w) and out:
            out += w
        else:
            out += (" " if out else "") + w
    return out

data = torch.tensor([stoi[w] for w in tokens], dtype=torch.long)
print("vocab_size:", vocab_size, "total tokens:", len(data))

block_size = 64
n_embd     = 1000
n_head     = 8
n_layer    = 8
lr, steps, batch_size = 1e-3, 5000, 32

def get_batch():
    ix = torch.randint(len(data) - block_size - 1, (batch_size,))
    x = torch.stack([data[i:i+block_size] for i in ix])
    y = torch.stack([data[i+1:i+block_size+1] for i in ix])
    return x.to(device), y.to(device)

class Block(nn.Module):
    def __init__(self):
        super().__init__()
        self.ln1 = nn.LayerNorm(n_embd)
        self.attn = nn.MultiheadAttention(n_embd, n_head, batch_first=True, bias=False)
        self.ln2 = nn.LayerNorm(n_embd)
        self.mlp = nn.Sequential(nn.Linear(n_embd, 4*n_embd, bias=False), nn.GELU(),
                                  nn.Linear(4*n_embd, n_embd, bias=False))
    def forward(self, x):
        T = x.size(1)
        mask = torch.triu(torch.ones(T, T, device=x.device), diagonal=1).bool()
        a = self.ln1(x)
        x = x + self.attn(a, a, a, attn_mask=mask, need_weights=False)[0]
        return x + self.mlp(self.ln2(x))

class TinyAgriGPT(nn.Module):
    def __init__(self):
        super().__init__()
        self.tok = nn.Embedding(vocab_size, n_embd)
        self.pos = nn.Embedding(block_size, n_embd)
        self.blocks = nn.ModuleList([Block() for _ in range(n_layer)])
        self.ln_f = nn.LayerNorm(n_embd)
        self.head = nn.Linear(n_embd, vocab_size, bias=False)
        self.head.weight = self.tok.weight
    def forward(self, idx, targets=None):
        pos = torch.arange(idx.size(1), device=idx.device)
        x = self.tok(idx) + self.pos(pos)
        for b in self.blocks: x = b(x)
        logits = self.head(self.ln_f(x))
        loss = None if targets is None else F.cross_entropy(
            logits.view(-1, vocab_size), targets.view(-1))
        return logits, loss
    @torch.no_grad()
    def generate(self, idx, n, temperature=0.8):
        for _ in range(n):
            logits, _ = self(idx[:, -block_size:])
            probs = F.softmax(logits[:, -1, :] / temperature, dim=-1)
            idx = torch.cat([idx, torch.multinomial(probs, 1)], dim=1)
        return idx

model = TinyAgriGPT().to(device)
n_params = sum(p.numel() for p in model.parameters())
print(f"device={device}  vocab={vocab_size}  parameters={n_params}")

opt = torch.optim.AdamW(model.parameters(), lr=lr)
sched = torch.optim.lr_scheduler.CosineAnnealingLR(opt, T_max=steps, eta_min=lr*0.05)
best_loss = float("inf")
best_state = None
for step in range(steps):
    x, y = get_batch()
    _, loss = model(x, y)
    opt.zero_grad()
    loss.backward()
    torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
    opt.step()
    sched.step()
    if loss.item() < best_loss:
        best_loss = loss.item()
        best_state = {k: v.clone() for k, v in model.state_dict().items()}
    if step % 300 == 0:
        print(f"step {step:5d}  loss {loss.item():.3f}  lr {sched.get_last_lr()[0]:.2e}")

print("final loss (last step):", loss.item())
print("best loss seen during training:", best_loss)
model.load_state_dict(best_state)

torch.save({"model": model.state_dict(), "stoi": stoi, "itos": itos,
            "config": dict(block_size=block_size, n_embd=n_embd, n_head=n_head,
                            n_layer=n_layer, vocab_size=vocab_size)},
           "agri_tiny_llm_97m_aero.pt")
print("saved agri_tiny_llm_97m_aero.pt")
