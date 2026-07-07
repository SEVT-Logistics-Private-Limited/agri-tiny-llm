# Model Card: agri-tiny-llm-10m (Rung 3)

## Overview
Third rung in the progressive scale-up. Same 6 domains as Rung 2, with hydroponics
expanded to comprehensive A-Z coverage: all 6 system types (DWC, NFT, ebb & flow,
drip, wick, Kratky), all growing media, full macro/micronutrient deficiency list,
5 crop profiles (lettuce, tomato, cucumber, basil, strawberry), light/DLI/CO2
environmental management, water source treatment, and common pests. All content
original, written fresh rather than copied from any source.

## Architecture
- Parameters: 9,919,360
- Layers: 4
- Embedding dim: 440
- Attention heads: 8
- Context length (block_size): 64
- Vocabulary: 1,342 (word-level tokenizer)
- Weight tying: yes
- Biases: none

## Training
- Corpus: ~254KB, original text, all 6 domains with hydroponics fully expanded
- Optimizer: AdamW, lr=1e-3 with cosine decay (eta_min = 5% of peak lr)
- Gradient clipping: max norm 1.0
- Steps: 4000, batch size 32
- Framework: PyTorch, trained on Google Colab (T4 GPU)
- Checkpoint selection: best loss seen during training is saved, not just the final step

## Training Stability Issue Found and Fixed
An earlier version of this rung used a fixed learning rate of 3e-3 (same as smaller
rungs) with no decay or gradient clipping. Loss dropped well early (down to 2.73 at
step 600) but then climbed back up and destabilized for the rest of training (up to
4.5 by the final step), producing incoherent generated text despite a low-looking
final loss number. Root cause: a fixed high learning rate becomes unstable as model
size grows, causing the model to overshoot past good solutions instead of settling
into them. Fixed by lowering the learning rate, adding cosine decay so updates get
gentler over time, adding gradient clipping to cap any single destabilizing update,
and saving the best checkpoint seen during training rather than only the last step.
After the fix, loss decreased smoothly with no instability for the full run.

## Results
- Final loss: ~0.10-0.11 (smooth, monotonic decrease after the fix)
- Independently verified against 9 seed questions

## Test Results
| Seed Question | Result |
|---|---|
| What is aeroponics? | Correct |
| My aquaculture pond pH is 4.2, what should I do? | Correct |
| How do I grow microgreens on cocopeat? | Correct |
| What is the ideal TDS for hydroponic lettuce? | Correct |
| What causes tipburn in hydroponic lettuce? | Correct |
| What EC should I use for hydroponic tomatoes during fruiting? | Correct |
| What does boron deficiency look like in hydroponics? | Correct |
| What is DLI in hydroponics? | Correct |
| How do I remove chloramine from tap water? | Correct |

9 out of 9 seed questions answered correctly, coherently, and specifically.

## Files
- `train_agri_10m.py` - dataset loading + tokenizer + model + training script (includes stability fix)
- `agri_corpus_10m.txt` - exact training corpus used for this rung
- `agri_tiny_llm_10m.pt` - trained checkpoint

## Next Steps
See `model-card-50m-hydro.md` (Rung 4): hydroponics-only rung completing full
A-Z coverage of all common hydroponic crops, herbs, flowers, and system types.
Starting with Rung 4, each future rung covers one domain only rather than mixing
all six, to keep scope and evaluation clear per rung.
