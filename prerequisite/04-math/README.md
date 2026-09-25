# Stage 4 — Math for Transformers

This stage is *just enough* math to read Paper #1.
You don't need everything before starting — add as you go.

## Must-know before Paper #1

- [ ] Scalars vs vectors vs matrices
- [ ] Shapes as `(rows, cols)`
- [ ] Matrix multiply: `(m, k) @ (k, n) -> (m, n)`
- [ ] Dot product of two vectors: same-length, single number
- [ ] Softmax: convert raw scores to probabilities summing to 1
- [ ] Log: `log(softmax)` used in cross-entropy
- [ ] Cross-entropy: loss for "which class was correct"
- [ ] Mean: average of a vector

## Learn later (during/after Transformer)

- Transpose (already in NumPy stage)
- Norms (vector length)
- Eigenvalues / SVD (PCA)
- Partial derivatives, gradients, chain rule
- Probability: P(A|B), Bayes
- Entropy, KL divergence

## Concrete practice

1. `softmax([1.0, 2.0, 3.0])` by hand
2. cross-entropy of `[-log(0.7)]` when correct class had prob 0.7
3. mean of `[1, 2, 3, 4]`

## Done when

- `softmax([1,2,3])` computed on paper, sums to 1
- cross-entropy `-log(0.7)` computed and explained in words
- `(m,k) @ (k,n) -> (m,n)` rule stated from memory
- dot product explained as "similarity score" in one sentence

## Reference

- 3Blue1Brown: Essence of Linear Algebra (YouTube)
- StatQuest: Cross-entropy, softmax (YouTube)
