# Prerequisites — Before Touching the LLM Papers

Everything here exists for one reason: make Paper #1
(*Attention Is All You Need*) readable, and make "how does an
LLM learn?" concrete.

Rule: a stage is **completed** only when its "Done when" test
passes. Not when you read about it — when you can *do* it.

## No-blocker rule (protects motivation)

Never do a stage "because it's next". Do it **right before the
paper needs it**. Every item below says which paper piece it
unlocks. If a stage unlocks nothing you're reading — skip it for
now, guilt-free.

## Just-in-time path for Paper #1

| step | learn (small) | unlocks in paper | status |
|------|---------------|------------------|--------|
| 1 | word → id → vector | §3.1 input embeddings | done (word_to_vector.py) |
| 2 | dot product = similarity | §3.2.1 attention scores | **next** |
| 3 | softmax to weights | §3.2.1 attention weights | after 2 |
| 4 | matmul shapes `(m,k)@(k,n)` | Q,K,V projections | after 3 |
| 5 | tensor shapes `(b,s,d)` | everywhere | mostly done |
| 6 | autograd 3-line loop | "how does it learn" | after model exists |
| 7 | tiny char-LM training loop | §3.4 + §4 end-to-end | capstone |
| 8 | git/terminal hygiene | every experiment | ongoing, parallel |

Everything else in the stage folders = optional, learn when a
paper actually needs it.

## Stage folders (reference, not a queue)

| # | Stage | Why it matters |
|---|-------|----------------|
| 1 | [01-python](01-python/) | read + write small model code |
| 2 | [02-numpy](02-numpy/) | shapes and arrays, parent of PyTorch |
| 3 | [03-tensors](03-tensors/) | same as NumPy + GPU + gradients |
| 4 | [04-math](04-math/) | dot products, softmax, cross-entropy |
| 5 | [05-autograd](05-autograd/) | how learning actually happens |
| 6 | [06-nn](06-nn/) | nn.Module, Linear, Embedding, LayerNorm |
| 7 | [07-training](07-training/) | the full learn loop end-to-end |
| 8 | [08-git-linux](08-git-linux/) | run, track, commit — **parallel, from day 1**, not a queue step |
| 9 | [09-architectures](09-architectures/) | MLP → CNN → RNN → LSTM → Attention → Transformer |

Folder numbers = learning order. Do 1 → 9 in sequence; folder 4
(math) is just-enough for now, deep math gets added when a paper
needs it.

## Definition of done (per stage)

1. **python-basics** — write a function, a class with `__init__`
   + method, and a dict lookup with missing-key handling, without
   googling syntax.
2. **numpy** — given shapes `(2,3)` and `(3,4)`, predict the
   output shape of `a @ b`; write softmax with `np.exp` by hand.
3. **pytorch-tensors** — explain what every dim means in
   `(batch, seq_len, d_model)`; slice, reshape, transpose, and
   softmax a tensor without errors.
4. **math** — compute `softmax([1,2,3])` and cross-entropy for a
   correct class with prob 0.7, on paper.
5. **pytorch-autograd** — write the 3-line optimizer loop
   (`zero_grad / backward / step`) from memory; explain what
   `.grad` holds.
6. **pytorch-nn** — write a tiny `nn.Module` with one `nn.Linear`
   from memory; explain what `nn.Embedding(10,4).weight` holds;
   train an MLP on XOR to loss < 0.05.
7. **training-loop** — train a tiny char-level LM until loss
   drops; explain every line of your loop in your own words.
8. **terminal-git** — create a branch, run an experiment, commit
   results, all from the terminal without help.

## How to work a stage

1. Read the checklist in the stage's README.
2. Do the "Concrete practice" items — write the code yourself.
3. Prove the "Done when" test to yourself (or to the tutor).
4. Tick the boxes.

## Status

- [x] step 1 — word → id → vector
- [ ] step 2 — dot product  ← NEXT
- [ ] step 3 — softmax
- [ ] step 4 — matmul shapes
- [ ] step 5 — tensor shapes (mostly done)
- [ ] step 6 — autograd loop
- [ ] step 7 — char-LM capstone

## Not in scope (deliberately)

Classical ML (SVM, trees, k-means), CNNs, advanced linear algebra
(SVD, eigen), distributed training. These come later, when a paper
actually needs them.
