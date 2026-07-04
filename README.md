# AgriTinyGPT — ~1M Parameter Agriculture Language Model

## Author
Shiva

A GPT-style transformer built entirely from scratch in PyTorch, trained on an original
agriculture corpus. No pretrained weights, no fine-tuning — trained from random
initialization, same approach as the earlier tiny-llm scale-up series.

## What This Is
A ~1.07M-parameter GPT-style model trained on original text covering six agriculture
domains: hydroponics, aeroponics, aquaponics, aquaculture, dairy farming, and
microgreens. Built on the same architecture family proven at the ~990,200-parameter
scale in the earlier tiny-llm-jetson reference build (2 layers, multi-head attention,
weight-tied output head).

## Architecture
- Type: Decoder-only transformer (GPT architecture)
- Parameters: 1,071,840
- Layers: 3
- Embedding dim: 160
- Attention heads: 8
- Context length (block_size): 64
- Vocabulary: ~861 (word-level tokenizer, not character-level)
- Weight tying: yes (output head shares weights with token embedding)
- Biases: none

## Why word-level instead of character-level
The earlier reference models used character-level tokenization on a single repeated
placeholder sentence. That doesn't scale to real vocabulary, so this build uses a
simple word-level tokenizer instead, sized appropriately for a real (if small)
agriculture text corpus.

## Training
- Corpus: original agriculture text (paragraphs + Q&A), generated fresh, not copied
  from any external source, covering hydroponics, aeroponics, aquaponics, aquaculture,
  dairy farming, and microgreens
- Optimizer: AdamW, lr=3e-3
- Steps: 4000, batch size 32
- Framework: PyTorch, trained on Google Colab

## Results
- Initial loss: ~108
- Final loss: ~0.10-0.13
- Independently verified by reloading the saved checkpoint in a separate script and
  generating answers to 4 unseen agriculture questions — all 4 answered correctly
  and on-topic after the v2 corpus/tokenizer fixes (see model-card.md for full
  before/after comparison)

## Files
- `train_agri.py` — dataset generation + tokenizer + model + training script
- `test_agri.py` — independent load-and-generate verification script
- `agri_tiny_llm.pt` — trained checkpoint (model weights + tokenizer + config)
- `model-card.md` — full architecture, training, and results details
- `AgriTinyGPT_Colab.ipynb` — the notebook version, runnable end-to-end on Google Colab

## How to Run
```
pip install torch
python train_agri.py
```
Or open `AgriTinyGPT_Colab.ipynb` in Google Colab and run all cells.

## Next Steps
- Expand corpus coverage per domain (more edge cases, especially dairy and aquaculture)
- Parameter ablation study at this vocabulary size
- Evaluate on a held-out question set not seen during training
