# Contributing

This is primarily a personal learning-in-public lab, but reproductions,
corrections, and discussion are welcome and genuinely useful.

## Setup

```bash
git clone <this-repo>
cd jagan-llm-lab
python3 -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"   # once pyproject.toml dependencies are defined
```

Python 3.11+ and PyTorch are required. Individual `papers/` and
`experiments/` folders may have their own `requirements.txt` for
paper-specific dependencies.

## Code style

- `ruff` for linting/formatting.
- `pytest` for tests.
- Type hints where they add clarity.
- Config files (YAML) instead of hardcoded hyperparameters — see
  [configs/experiment_config.yaml](configs/experiment_config.yaml).
- Deterministic seeds where practical.
- No giant notebooks: core implementations live in `.py` modules; notebooks
  are for visualization, exploration, and analysis only.

## Issues

Use issues for:
- Reporting a bug or incorrect implementation
- Pointing out a broken or outdated paper link
- Suggesting a paper for a future phase
- Proposing an experiment

## Pull requests

- Keep PRs scoped to a single paper, experiment, or fix.
- Explain what changed and why in the description.
- If you change results, include how you obtained them (hardware, seed,
  config) so they can be checked.

## Reproduction reports

If you reproduce an experiment from this repo, please open an issue or PR
with:
- What you reproduced
- Your hardware and config
- Your results vs. the ones recorded here
- Any differences and your hypothesis for why

Reporting a *difference* is just as valuable as confirming a result —
please don't just confirm blindly.

## Experiment contributions

New experiments should follow [experiments/_template](experiments/_template/README.md):
Research Question → Hypothesis → Controlled Variables → Results → Analysis.
