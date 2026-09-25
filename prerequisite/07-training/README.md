# Stage 7 — Training Loop End-to-End

The full loop that makes an LLM learn. This is the answer to
"how does the model actually learn?"

## Must-know before Paper #1

- [ ] `Dataset` (`__len__`, `__getitem__`)
- [ ] `DataLoader` (batching, shuffle)
- [ ] Flow:
  ```
  Dataset
    ↓
  DataLoader
    ↓
  Model (forward)
    ↓
  Loss (cross-entropy)
    ↓
  optimizer.zero_grad()
  loss.backward()
  optimizer.step()
  ```
- [ ] Cross-entropy for next-token prediction
- [ ] `.train()` vs `.eval()` mode
- [ ] Train/val split
- [ ] Checkpoint saving / loading (`torch.save` / `torch.load`)

## Concrete practice

1. Tiny char-level LM on a sentence like `"i love cats"`
   - vocab from unique chars
   - input = ids[:-1], target = ids[1:]
   - `nn.Embedding` → `nn.Linear` → cross-entropy
   - train 100 steps, watch loss drop
2. Print loss every 10 steps
3. Save / reload a checkpoint

## After this stage

"how does LLM learn" becomes concrete: loss → grad → nudge weights.

## Done when

- tiny char-LM trained, loss visibly drops across steps
- explain every loop line in your own words:
  data → forward → loss → zero_grad → backward → step
- predict what happens if you forget `zero_grad()` (then verify)

## Reference

- PyTorch quickstart: pytorch.org/tutorials/beginner/basics/quickstart_tutorial.html
