# Stage 3 — PyTorch Tensors

PyTorch tensors behave like NumPy arrays but also:
- live on GPU
- track gradients
- plug into `nn.Module`

## Must-know before Paper #1

- [ ] Create: `torch.tensor`, `torch.zeros`, `torch.ones`, `torch.randn`
- [ ] Shapes: `x.shape`, `x.dtype`, `x.ndim`, `x.device`
- [ ] Indexing same as NumPy
- [ ] Reshape: `x.view`, `x.reshape`, `x.flatten`
- [ ] Transpose: `x.T`, `x.transpose`, `x.permute`
- [ ] Matmul: `x @ y`, `torch.matmul`
- [ ] Concatenate: `torch.cat`, `torch.stack`
- [ ] Masking: `x.masked_fill(mask, value)`
- [ ] Softmax: `torch.softmax(x, dim=-1)`
- [ ] Seed: `torch.manual_seed(0)` for reproducibility

## Concrete practice

1. Create `(1, 3, 512)` zeros and print shape
2. Slice last token: `x[:, -1, :]` -> shape `(1, 512)`
3. Softmax over last dim, check row sums to 1
4. Move tensor to GPU: `x.to('cuda')`

## Done when

- you can say what every dim means in `(1, 18, 512)` without thinking
- slice last token, transpose, reshape, softmax — all without errors
- you fix a real shape-mismatch bug yourself by reading the shapes

## After this stage

You should be able to:
- trace any tensor's shape through a model
- know what `(batch, seq_len, d_model)` means
