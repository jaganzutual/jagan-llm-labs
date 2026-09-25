# Stage 6 — PyTorch nn API

How to build models using PyTorch's layers.

## Must-know before Paper #1

- [ ] `nn.Module`:
  - subclass it
  - `__init__` registers layers
  - `forward(x)` computes output
- [ ] `nn.Parameter` (or layers that create them)
- [ ] `nn.Linear` (you've seen this in `rnn_cell.py`)
- [ ] `nn.Embedding` (lookup table)
- [ ] `nn.LayerNorm` (smooths tokens)
- [ ] `nn.Dropout` (regularization)
- [ ] `model.to(device)` moves weights to GPU
- [ ] `model.parameters()` for the optimizer

## Concrete practice

1. Tiny `nn.Module` with one `nn.Linear`
2. Use `nn.Embedding(100, 16)` and inspect `.weight` shape
3. Apply `nn.LayerNorm(16)` to a `(2, 16)` tensor, check mean≈0 std≈1
4. **MLP here** (moved from architectures): 2× `nn.Linear` + ReLU,
   train on XOR until loss < 0.05 — this is the first "real" model

## After this stage

You should be able to read `class MultiHeadAttention(nn.Module)`
and recognize every line.

## Done when

- write a tiny `nn.Module` with one `nn.Linear` from memory
- say what `nn.Embedding(10,4).weight` shape is and what it holds
- apply `nn.LayerNorm(16)` and verify mean≈0, std≈1 yourself
- read `class RNNCell(nn.Module)` and name every line's job

## Reference

- PyTorch tutorial: pytorch.org/tutorials/beginner/blitz/neural_networks_tutorial.html
