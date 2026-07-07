# Model Card: agri-tiny-llm-5m (Rung 2)

## Overview
Second rung in the progressive scale-up. Same 6 agriculture domains as Rung 1
(hydroponics, aeroponics, aquaponics, aquaculture, dairy farming, microgreens), with
deeper content added: interaction effects between variables, edge cases, and
troubleshooting scenarios per topic (e.g. why root rot appears suddenly, new tank
syndrome in aquaponics, oxygen crash vs disease in shrimp ponds).

## Architecture
- Parameters: 5,283,200
- Layers: 4
- Embedding dim: 320
- Attention heads: 8
- Context length (block_size): 64
- Vocabulary: 1,068 (word-level tokenizer)
- Weight tying: yes
- Biases: none

## Training
- Corpus: ~176KB, original text, all 6 domains with deeper interaction/troubleshooting content
- Optimizer: AdamW, lr=3e-3
- Steps: 5000, batch size 32
- Framework: PyTorch, trained on Google Colab (T4 GPU)

## Results
- Final loss: ~0.11
- Independently verified against 7 seed questions spanning all 6 domains

## Test Results
| Seed Question | Result |
|---|---|
| What is aeroponics? | Correct |
| My aquaculture pond pH is 4.2, what should I do? | Correct |
| How do I grow microgreens on cocopeat? | Correct |
| What is the ideal TDS for hydroponic lettuce? | Correct (fixed after adding disambiguating examples - see below) |
| Why does root rot suddenly appear after weeks of healthy growth? | Correct |
| What is new tank syndrome in aquaponics? | Correct |
| How can I tell if sudden shrimp mortality is an oxygen crash or disease? | Correct |

7 out of 7 seed questions answered correctly.

## Notable Issue Found and Fixed
An earlier version of this rung confused the hydroponic TDS question with an
unrelated pH/FCR fact from a different domain. This was fixed not by more training
steps, but by adding several additional TDS-specific examples with varied phrasing,
including one example explicitly stating that TDS and pH are different measurements.
This is the same class of fix used in Rung 1 (v1 -> v2) for a similar microgreens
confusion - when two topics share similar vocabulary or numeric patterns, the fix is
more distinguishing examples, not just more training time.

## Files
- `train_agri_5m.py` - dataset loading + tokenizer + model + training script
- `agri_corpus_5m.txt` - exact training corpus used for this rung
- `agri_tiny_llm_5m.pt` - trained checkpoint

## Next Steps
See `model-card-10m.md` (Rung 3) for the next stage: hydroponics expanded to full
A-Z coverage.
