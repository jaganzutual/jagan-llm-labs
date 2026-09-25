# Stage 8 — Terminal, Git, Experiments

Not ML, but you need it every single session.

## Terminal / Linux

- [ ] `cd`, `ls`, `pwd`, `mkdir`
- [ ] `python file.py`, running scripts
- [ ] pip + venv from terminal
- [ ] reading stack traces top-down
- [ ] `grep`, `find` basics

## Git

- [ ] `git status`, `git log --oneline`
- [ ] `git add` / `git commit`
- [ ] `git diff` to review changes
- [ ] branches: `git switch -c name`
- [ ] `.gitignore` (never commit venv, checkpoints)

## Experiment hygiene

- [ ] one experiment = one folder with its own `README.md`
- [ ] always `torch.manual_seed(0)` before comparing runs
- [ ] log: config used, loss curve, result
- [ ] commit after each working step

## Done when

- from terminal alone: branch, run experiment, commit results
- a `.gitignore` exists that excludes venv + checkpoints
- you can read a Python traceback top-down and point at the real
  error line

## Concrete practice

1. Create a branch for your tiny char-LM experiment
2. Run it, save the checkpoint
3. Commit with message "experiment: char-LM first run"
