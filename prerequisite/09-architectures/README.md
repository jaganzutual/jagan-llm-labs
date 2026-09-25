# Stage 4 Architectures — MLP → CNN → RNN → LSTM → Attention → Transformer

For each architecture, the rule is the same:
**first ask — what problem was this trying to solve?**
Implement the tiny version yourself. Not the paper version.

## Order and status

- [ ] 1. **MLP** — stack of Linear + activation
  - solves: patterns beyond linear (e.g. XOR)
  - **implemented in 06-nn practice 4** — return here only to
    explain why MLP cannot handle sequences (no position, no order)

- [x] 2. **RNN** — recurrence for sequences
  - solves: variable-length inputs, state across time
  - done in the lab (`implementations/rnn/`, tests passing)
  - you already know its 3 problems: sequential bottleneck,
    vanishing gradients, information bottleneck

- [ ] 3. **CNN** — sliding filters for local patterns
  - solves: translation-invariant local features (images)
  - implement: `nn.Conv1d` over a toy signal; count params vs MLP
  - done when: you can say why conv beats MLP on shifted patterns

- [ ] 4. **LSTM** — gated RNN
  - solves: vanishing gradients in long sequences
  - implement: read + explain the 4 gates; use `nn.LSTM` in a
    tiny char-LM, compare loss vs plain RNN
  - done when: you can explain forget gate in one sentence
  - note: conceptual stop — modern LLMs don't use LSTM; the
    lesson is *why attention replaced it*

- [ ] 5. **Attention** — direct connections between any two positions
  - solves: LSTM's sequential bottleneck + long-range forgetting
  - = Paper #1 §3.2, the whole point of the lab
  - done when: dot-product scores + softmax weights computed by
    hand for a 3-token sentence

- [ ] 6. **Transformer** — attention stacked, no recurrence
  - solves: full parallelism + long-range access
  - = Paper #1 §3.1 (already read: 6 layers, 2+3 sub-layers,
    residual + LayerNorm)
  - done when: decoder-only GPT implemented in
    `implementations/gpt/` with passing tests

## Why this order

Every step exists because the previous one hit a wall:

```
MLP        no notion of sequence or position
CNN        local patterns only, fixed window
RNN        sequences, but sequential + vanishing grads
LSTM       patches gradients, still sequential
Attention  parallel + direct long-range access
Transformer attention stacked = the LLM backbone
```

Each "done when" is small on purpose. Small wins, no blockers.
