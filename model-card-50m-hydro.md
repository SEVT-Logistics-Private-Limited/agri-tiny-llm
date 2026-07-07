# Model Card: agri-tiny-llm-50m-hydro (Rung 4)

## Overview
Fourth rung, and the first rung to focus on a single domain rather than mixing all
six. This rung is hydroponics only, completing full A-Z coverage of the topic:
all 6 system types (wick, DWC, NFT, ebb & flow, drip, Kratky), all growing media,
complete macro/micronutrient deficiency list, ~19 crop types spanning leafy greens,
fruiting vegetables, herbs, vine crops, and root vegetables, 3 flowers (marigolds,
petunias, orchids), light/CO2/water treatment/pests, and guidance on which system
suits which plant type. All content original, written fresh rather than copied from
any source.

## Why single-domain from this rung onward
Earlier rungs mixed all 6 agriculture domains together in one corpus. From this rung
forward, each rung covers one domain completely before moving to the next, keeping
scope, evaluation, and corpus growth easier to track and verify per topic.

## Architecture
- Parameters: 51,699,480
- Layers: 6
- Embedding dim: 840
- Attention heads: 8
- Context length (block_size): 64
- Vocabulary: 977 (word-level tokenizer, hydroponics-only corpus)
- Weight tying: yes
- Biases: none

## Training
- Corpus: ~181KB, hydroponics only, full A-Z coverage
- Optimizer: AdamW, lr=1e-3 with cosine decay (eta_min = 5% of peak lr)
- Gradient clipping: max norm 1.0
- Steps: 5000, batch size 32
- Framework: PyTorch, trained on Google Colab (T4 GPU)
- Checkpoint selection: best loss seen during training is saved, not just the final step

## Results
- Loss trajectory: 548.8 -> 2.18 -> 0.84 -> 0.50 -> 0.25 -> 0.14 -> 0.10 (smooth,
  monotonic decrease throughout, no instability at any point)
- Final loss (last step): 0.101
- Best loss during training: 0.080
- Independently verified against 9 seed questions

## Test Results
| Seed Question | Result |
|---|---|
| What is the ideal TDS for hydroponic lettuce? | Correct |
| What causes tipburn in hydroponic lettuce? | Correct |
| What EC should I use for hydroponic bell peppers during fruiting? | Correct |
| Why does my hydroponic spinach stop producing leaves and flower instead? | Correct |
| Can orchids be grown in a standing hydroponic nutrient solution? | Correct |
| Which hydroponic system is best for tomatoes and peppers? | Correct |
| What growing medium depth do hydroponic carrots need? | Correct |
| Why does mint need to be grown separately from other hydroponic crops? | Correct |
| What conditions do hydroponic peas need? | Correct |

9 out of 9 seed questions answered correctly. This is the cleanest result across
all 4 rungs so far: fully stable training and perfect test accuracy, including on
the newest, least-repeated content (orchids, mint, carrot medium depth).

## Files
- `train_agri_50m_hydro.py` - dataset loading + tokenizer + model + training script
- `agri_corpus_50m_hydro.txt` - exact training corpus used for this rung (hydroponics only)
- `agri_tiny_llm_50m_hydro.pt` - trained checkpoint

## Next Steps
Hydroponics is now considered complete. Rung 5 will pick one new domain (aquaculture,
dairy farming, aeroponics, aquaponics, or microgreens) and bring it to the same
completeness, following the single-domain-per-rung approach established here.
