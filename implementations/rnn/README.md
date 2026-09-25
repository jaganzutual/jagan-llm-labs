# RNN primer

Built BEFORE Paper #1 so the *"drop the recurrence"* claim actually
lands. Not part of the official 26-paper list — it's a foundation
exercise.

## Why an RNN first?

Paper #1's whole thesis is: *attention is enough, you don't need
recurrence*. To feel that claim, you have to feel the recurrence
first.

## Files

- `rnn_cell.py`     — single time-step cell (Step 1)
- `rnn_unrolled.py` — unroll across a sequence (Step 2)
- `train_char.py`   — tiny char-level LM training (Step 4)
- Tests: `../../tests/test_rnn.py`

## Build it in 4 steps

### Step 1 — single cell
Implement `RNNCell(input_size, hidden_size)` so that:

```
h_t = tanh(x_t @ W_xh + h_{t-1} @ W_hh + b)
```

Shapes:
- `x_t`         : (batch, input_size)
- `h_{t-1}`, `h_t` : (batch, hidden_size)
- `W_xh`        : (input_size, hidden_size)
- `W_hh`        : (hidden_size, hidden_size)
- `b`           : (hidden_size,)

Run: `pytest tests/test_rnn.py -v` — must pass before Step 2.

### Step 2 — unroll
Loop over a sequence in `rnn_unrolled.py` and return all hidden
states. Add a test with T=5 time steps.

### Step 3 — compare with `nn.RNN`
Use `torch.nn.RNN` on the same input. Your outputs should match.

### Step 4 — train a tiny char-LM
Take ~100 lines of text (a Shakespeare paragraph is fine). Predict
the next character. **Watch how slow it gets on long sequences** —
that's the bottleneck Paper #1 attacks.

## Rules

- Write the code yourself. Don't peek at reference implementations
  until yours works.
- Each step ends with a passing test before the next.
- After Step 4, write `notes.md`: *"what did the recurrence feel
  like? why is it slow on long sequences?"* That sets up Paper #1.
