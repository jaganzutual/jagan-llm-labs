# Stage 2 — NumPy

NumPy is the parent of PyTorch tensors. Learn it before PyTorch.

## Must-know before Paper #1

- [ ] Create arrays: `np.array`, `np.zeros`, `np.ones`, `np.arange`, `np.random.randn`
- [ ] Shapes: `x.shape`, `x.dtype`, `x.ndim`
- [ ] Indexing / slicing: `x[0]`, `x[0, 1]`, `x[:, 0]`
- [ ] Reshape: `x.reshape((a, b))`, `x.flatten()`
- [ ] Transpose: `x.T`, `x.transpose(0, 1)`
- [ ] Matrix multiplication: `x @ y`, `np.dot(x, y)`
- [ ] Elementwise ops: `+ - * /`
- [ ] Reductions: `x.sum`, `x.mean`, `x.max`
- [ ] Broadcasting (basic idea: shapes align from right)

## Concrete practice

1. shape `(3, 4)` ones, reshape to `(12,)`, back to `(2, 6)`
2. matrix `(2, 3)` @ `(3, 4)` -> shape `(2, 4)`
3. softmax by hand with `np.exp` and `x / x.sum`

## After this stage

You should be able to translate any NumPy to PyTorch tensor code
almost line-by-line.

## Done when

- given `(2,3) @ (3,4)`, you say the output shape instantly
- write softmax with `np.exp` + `x / x.sum()` from memory
- explain broadcasting in one sentence with an example

## Reference

- NumPy quickstart: numpy.org/doc/stable/user/quickstart.html
