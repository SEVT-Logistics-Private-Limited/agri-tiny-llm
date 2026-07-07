"""
AgriTinyGPT Rung 2 - ~5.28M parameters
6 domains (hydroponics, aeroponics, aquaponics, aquaculture, dairy, microgreens)
with deeper interaction/troubleshooting content added on top of Rung 1's basics.
"""
import torch, torch.nn as nn, re
from torch.nn import functional as F

torch.manual_seed(1337)
device = "cuda" if torch.cuda.is_available() else "cpu"

with open("agri_corpus_5m.txt", "r", encoding="utf-8") as f:
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
n_embd     = 320
n_head     = 8
n_layer    = 4
lr, steps, batch_size = 3e-3, 5000, 32

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
for step in range(steps):
    x, y = get_batch()
    _, loss = model(x, y)
    opt.zero_grad(); loss.backward(); opt.step()
    if step % 300 == 0:
        print(f"step {step:5d}  loss {loss.item():.3f}")

print("final loss:", loss.item())

torch.save({"model": model.state_dict(), "stoi": stoi, "itos": itos,
            "config": dict(block_size=block_size, n_embd=n_embd, n_head=n_head,
                            n_layer=n_layer, vocab_size=vocab_size)},
           "agri_tiny_llm_5m.pt")
print("saved agri_tiny_llm_5m.pt")
