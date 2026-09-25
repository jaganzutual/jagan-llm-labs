# Stage 5 — PyTorch Autograd

How PyTorch learns: compute loss, call `backward()`, update weights.

## Must-know before Paper #1

- [ ] `x.requires_grad = True`
- [ ] `loss.backward()` populates `.grad`
- [ ] `torch.no_grad()` for inference
- [ ] `tensor.detach()` to stop tracking
- [ ] Optimizer loop:
  ```
  optimizer.zero_grad()
  loss.backward()
  optimizer.step()
  ```
- [ ] `torch.optim.SGD` and `torch.optim.Adam`

## Concrete practice

1. `x = torch.tensor(2.0, requires_grad=True)`
   `y = x ** 2` -> `y.backward()` -> print `x.grad` (=4)
2. Linear regression end-to-end:
   - data
   - `nn.Linear`
   - MSE loss
   - SGD step
   - watch loss go down

## After this stage

You should be able to read a training loop and know which line
does what.

## Done when

- write the 3-line loop (`zero_grad / backward / step`) from memory
- explain what `.grad` holds after `backward()`
- explain why `zero_grad()` is needed at all
- linear regression practice reaches visibly lower loss than step 1

## Reference

- PyTorch tutorial: pytorch.org/tutorials/beginner/blitz/autograd_tutorial.html
