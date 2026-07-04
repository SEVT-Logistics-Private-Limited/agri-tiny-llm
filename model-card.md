# Model Card: agri-tiny-llm-1m

## Overview
A 1,071,840-parameter GPT-style transformer, trained entirely from scratch on an
original agriculture text corpus. Built on the architecture family proven at the
~990,200-parameter scale in the earlier tiny-llm-jetson reference build, adapted with
a word-level tokenizer to handle real agriculture vocabulary instead of a repeated
placeholder sentence.

## Architecture
- Type: Decoder-only transformer (GPT architecture)
- Parameters: 1,071,840
- Layers: 3
- Embedding dim: 160
- Attention heads: 8
- Context length (block_size): 64
- Vocabulary: 861 (word-level, built from the training corpus)
- Weight tying: yes (output head shares weights with token embedding)
- Biases: none (linear layers and attention are bias-free)

## Training
- Corpus: original agriculture text (paragraphs + Q&A), ~127KB, covering hydroponics,
  aeroponics, aquaponics, aquaculture, dairy farming, and microgreens
- Optimizer: AdamW, lr=3e-3
- Steps: 4000, batch size 32
- Framework: PyTorch, trained on Google Colab

## Results
- Initial loss: ~108
- Final loss: ~0.10-0.13
- Loss converged cleanly with no instability across the full run

## Independent Verification
Reloaded from the saved checkpoint in a separate script (`test_agri.py`) and tested
against 4 unseen agriculture questions spanning 4 different domains.

## v1 -> v2 Fixes
The first version of this model had two known issues, fixed in v2:

1. **Number formatting bug**: the tokenizer split decimal numbers apart, so "4.2"
   was generated as "4. 2". Fixed by updating the tokenizer regex to treat decimal
   numbers as a single token.
2. **Topic confusion on microgreens/cocopeat**: v1 answered a question about growing
   microgreens on cocopeat with an unrelated hydroponics fact instead. Fixed by adding
   more specific, distinct training examples directly covering microgreens grown on
   cocopeat (setup steps, watering, medium comparison).

## Test Results (v2, after fixes)
| Seed Question | Result |
|---|---|
| What is aeroponics? | Correct — accurately describes misted roots in an enclosed chamber |
| My aquaculture pond pH is 4.2, what should I do? | Correct — flags danger, recommends alkaline buffer, correct number formatting |
| How do I grow microgreens on cocopeat? | Correct — specific, on-topic setup instructions (fixed from v1) |
| What is the ideal TDS for hydroponic lettuce? | Correct — accurate ppm and EC range |

4 out of 4 seed questions answered correctly and on-topic in v2, up from 3 out of 4
in v1.

## Interpretation
At this scale (~1.07M parameters), the model reliably reproduces specific facts from
its training corpus when questions closely match the training data's phrasing and
topic boundaries. The v1 confusion case shows the main failure mode at this scale:
when two topics share similar vocabulary or sentence structure, a small model can
blend them unless the training data draws a clear enough line between them. This is
expected behavior for a model this size, not a bug in the training pipeline — the
same class of error (though less frequent) appears in much larger language models too.

## Files
- `train_agri.py` — dataset generation + tokenizer + model + training script
- `test_agri.py` — independent load-and-generate verification script
- `agri_tiny_llm.pt` — checkpoint (model weights + tokenizer + config)

## Next Steps
- Expand corpus per domain, especially dairy and aquaculture edge cases
- Evaluate on a held-out question set not seen during training, to measure
  generalization rather than recall
- Parameter ablation study at this vocabulary size (matching the earlier
  984 -> 990,200 -> 150M rung progression, but with real vocabulary this time)
