"""
Independent verification script — reloads the trained checkpoint fresh
(same pattern as test_tiny_llm_1m.py) and generates answers to agriculture
seed questions.
"""
import torch, torch.nn as nn, re
from torch.nn import functional as F

device = "cuda" if torch.cuda.is_available() else "cpu"

ckpt = torch.load("agri_tiny_llm.pt", map_location=device)
stoi = ckpt["stoi"]
itos = ckpt["itos"]
cfg = ckpt["config"]
block_size = cfg["block_size"]
n_embd     = cfg["n_embd"]
n_head     = cfg["n_head"]
n_layer    = cfg["n_layer"]
vocab_size = cfg["vocab_size"]

def tokenize(s):
    return re.findall(r"\d+\.\d+|\w+|[^\w\s]", s.lower())

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
model.load_state_dict(ckpt["model"])
model.eval()

print("Reloaded parameter count:", sum(p.numel() for p in model.parameters()))

seeds = [
    "Q: What is aeroponics?",
    "Q: My aquaculture pond pH is 4.2, what should I do?",
    "Q: How do I grow microgreens on cocopeat?",
    "Q: What is the ideal TDS for hydroponic lettuce?",
]
for s in seeds:
    idx = torch.tensor([encode(s)], dtype=torch.long, device=device)
    out = model.generate(idx, 40)
    print(f"\nSEED: {s}\n-> {decode(out[0].tolist())}")
