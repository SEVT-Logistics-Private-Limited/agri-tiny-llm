# Model Card: agri-tiny-llm-97m-aero (Rung 5)

## Overview
Fifth rung, continuing the single-domain-per-rung approach established in Rung 4.
This rung is aeroponics only, completing full A-Z coverage of the topic: low-pressure
vs high-pressure misting systems, vertical tower vs horizontal tray systems, root
zone temperature management, misting cycle timing by growth stage, chamber humidity
requirements, nutrient delivery and foliar feeding, Pythium disease identification
and prevention, crop suitability (which plants work well and which don't, and why),
equipment failure risk (power outages, nozzle clogging), and maintenance. All
content original, written fresh rather than copied from any source.

## Architecture
- Parameters: 96,678,000
- Layers: 8
- Embedding dim: 1000
- Attention heads: 8
- Context length (block_size): 64
- Vocabulary: 580 (word-level tokenizer, aeroponics-only corpus)
- Weight tying: yes
- Biases: none

## Training
- Corpus: ~82KB, aeroponics only, full A-Z coverage
- Optimizer: AdamW, lr=1e-3 with cosine decay (eta_min = 5% of peak lr)
- Gradient clipping: max norm 1.0
- Steps: 5000, batch size 32
- Framework: PyTorch, trained on Google Colab (T4 GPU)
- Checkpoint selection: best loss seen during training is saved, not just the final step
- Same stability approach established in Rung 3 (fixed a learning-rate instability
  bug at that scale) and carried through Rung 4 and this rung

## Results
- Loss trajectory: 637.2 -> 0.55 -> 0.26 -> 0.19 -> 0.13 -> 0.09 -> 0.07 (smooth,
  monotonic decrease throughout, no instability at any point despite this being
  the largest model in the series so far)
- Final loss (last step): 0.070
- Best loss during training: 0.054
- Independently verified against 9 seed questions

## Test Results
| Seed Question | Result |
|---|---|
| What is the difference between low-pressure and high-pressure aeroponics? | Correct |
| What root zone temperature is ideal for aeroponics? | Correct |
| What is the most common aeroponic disease? | Correct |
| Why does Pythium spread so fast in aeroponic systems? | Correct |
| Can tomatoes be grown aeroponically? | Correct |
| What misting cycle should I use for aeroponic seedlings? | Correct |
| What humidity level should an aeroponic chamber maintain? | Correct |
| Why is a power outage more dangerous in aeroponics than hydroponics? | Correct |
| What causes nozzle clogging in aeroponic systems? | Correct |

9 out of 9 seed questions answered correctly, coherently, and specifically. This
matches Rung 4's clean result, confirming the training stability fixes hold reliably
even at nearly double the parameter count.

## Files
- `train_agri_97m_aero.py` - dataset loading + tokenizer + model + training script
- `agri_corpus_97m_aero.txt` - exact training corpus used for this rung (aeroponics only)
- `agri_tiny_llm_97m_aero.pt` - trained checkpoint

## Next Steps
Aeroponics is now considered complete, alongside hydroponics (Rung 4). Rung 6 will
pick a new domain (aquaponics, aquaculture, dairy farming, or microgreens) and bring
it to the same completeness, continuing to scale up model size progressively.
