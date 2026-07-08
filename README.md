# AgriTinyGPT — Progressive Scale-Up Agriculture Language Model

A series of GPT-style transformers built entirely from scratch in PyTorch, trained
on original agriculture text, scaling up in size rung by rung. No pretrained
weights, no fine-tuning — every rung is trained from random initialization.

## Author
Shiva

## Rungs So Far

| Rung | Parameters | Scope | Result |
|---|---|---|---|
| 1 | 1,066,400 (~1.07M) | All 6 domains, basics | 4/4 |
| 2 | 5,283,200 (~5.28M) | All 6 domains, +deeper interactions/troubleshooting | 7/7 |
| 3 | 9,919,360 (~9.92M) | All 6 domains, hydroponics expanded to A-Z | 9/9 |
| 4 | 51,699,480 (~51.7M) | Hydroponics only, full A-Z completion | 9/9 |
| 5 | 96,678,000 (~96.7M) | Aeroponics only, full A-Z completion | 9/9 |

Domains: hydroponics, aeroponics, aquaponics, aquaculture, dairy farming, microgreens.

From Rung 4 onward, each rung focuses on completing one domain fully before moving
to the next, rather than mixing all six domains together.

**Domain completion status:** Hydroponics (Rung 4) and Aeroponics (Rung 5) are
fully complete. Aquaponics, Aquaculture, Dairy farming, and Microgreens are still
at basic coverage (Rungs 1-3 level) and await their own dedicated rung.

## Why word-level instead of character-level
The earlier reference models (990,200-parameter Jetson Orin build) used
character-level tokenization on a single repeated placeholder sentence. That doesn't
scale to real vocabulary, so this build uses a simple word-level tokenizer instead,
sized appropriately for real (if still small) agriculture text corpora.

## A Real Bug Found and Fixed (Rung 3)
At the ~10M parameter scale, a fixed learning rate that worked fine at 1M and 5M
became unstable — loss dropped well early, then climbed back up and destabilized
for the rest of training, producing incoherent output despite training running to
completion. Fixed with a lower learning rate, cosine decay, gradient clipping, and
saving the best checkpoint seen during training rather than just the last step. Full
details in `model-card-10m.md`. This fix has held reliably through Rungs 4 and 5,
including at nearly 100M parameters.

## Files Per Rung
- `train_agri_<size>.py` — dataset loading + tokenizer + model + training script
- `agri_corpus_<size>.txt` — exact training corpus used for that rung
- `agri_tiny_llm_<size>.pt` — trained checkpoint
- `model-card-<size>.md` — full architecture, training, and results details

Rung 1 uses `train_agri.py`, `agri_corpus.txt`, `agri_tiny_llm.pt`, and `model-card.md`
(already in this repo from the first push).

## How to Run
