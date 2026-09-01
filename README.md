# Building LLMs From First Principles

**This lab is hosted live here: [jaganzutual.github.io/jagan-llm-labs](https://jaganzutual.github.io/jagan-llm-labs/)**

**A growing lab. 26 papers. 26+ implementations. No fixed deadline.**
**One goal: become an LLM Engineer.**

> Learning how modern LLMs are built — in public.

---

## What this is

I'm a software engineer learning how modern large language models are built —
from Transformer fundamentals to reasoning, Mixture-of-Experts, inference, and
eventually my own research. This repository is a public, working lab notebook
for that journey: an ongoing, growing effort to go from **software engineer →
LLM Engineer → aspiring Research Engineer**, at whatever pace the work actually
takes.

I am **not** claiming to be an AI expert. I am documenting the process of
becoming one — in the open, with real code, real failures, and real results.

This is **learning in public**, connected to my journey on X/Twitter, where I
share what I learn, papers I read, things I build, experiments I run, what
fails, what works, and what I find interesting along the way.

**GitHub:** this repository
**X / Twitter:** [@Jagansivam](https://x.com/Jagansivam)

## How to read this repo

Everything here falls into one of five clearly labeled categories. They are
**not interchangeable** — mixing them up misrepresents the work:

| Label                 | Meaning                                                              |
| --------------------- | -------------------------------------------------------------------- |
| **Learning**          | Understanding an existing, published concept.                        |
| **Implementation**    | Building an existing, published idea from scratch.                   |
| **Reproduction**      | Attempting to reproduce published findings (usually at small scale). |
| **Experiment**        | Modifying or testing an idea under controlled conditions.            |
| **Original Research** | Investigating a question that goes beyond simply following a paper.  |

A small-scale experiment on a consumer GPU is never described as reproducing
a frontier model. Where relevant, results are labeled **"conceptual
small-scale reproduction."**

## Progress dashboard

_Updated as the project progresses. Everything starts at zero — no faked progress._

| Metric              | Progress |
| ------------------- | -------- |
| 📄 Papers read       | `0 / 26` |
| 🛠️ Implementations   | `0 / 26` |
| 🧪 Experiments       | `0 / 11` |
| 🔬 Research projects | `0 / 1`  |
| 📆 Weeks active      | `0`      |

This repo has no fixed end date — the paper list and phases will grow as the
project does.

## Roadmap

The full 6-phase roadmap lives in [ROADMAP.md](ROADMAP.md).

| Phase | Focus                           | Papers  |
| ----- | ------------------------------- | ------- |
| 1     | Transformer Foundations         | #1–#4   |
| 2     | Modern LLM Architectures        | #5–#9   |
| 3     | Knowledge + Post-Training       | #10–#12 |
| 4     | Reasoning + Agents              | #13–#16 |
| 5     | Mixture of Experts              | #17–#20 |
| 6     | Deeper Research + Original Work | #21–#26 |

## Learning levels

🟢 **IMPLEMENT** — core idea implemented from scratch
🟡 **EXPERIMENT** — concept reproduced at small scale
🔵 **STUDY** — methodology and results understood without full reproduction

## Paper tracker

Progress legend: ⬜ Not started · 🟨 In progress · 🟩 Complete

| #   | Paper                                                                                                                                             | Authors                                                               | Year | Category                | Level        | Difficulty   | Read | Implemented | Experiment | Notes                                                                         |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------- | ---- | ----------------------- | ------------ | ------------ | ---- | ----------- | ---------- | ----------------------------------------------------------------------------- |
| 1   | [Attention Is All You Need](https://arxiv.org/abs/1706.03762)                                                                                     | Vaswani, Shazeer, Parmar, Uszkoreit, Jones, Gomez, Kaiser, Polosukhin | 2017 | Foundations             | 🟢 IMPLEMENT  | Intermediate | ⬜    | ⬜           | ⬜          | [papers/01-attention-is-all-you-need](papers/01-attention-is-all-you-need/)   |
| 2   | [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/)                                                                | Jay Alammar                                                           | 2018 | Foundations             | 🔵 STUDY      | Beginner     | ⬜    | ⬜           | ⬜          | [papers/02-illustrated-transformer](papers/02-illustrated-transformer/)       |
| 3   | [BERT: Pre-training of Deep Bidirectional Transformers](https://arxiv.org/abs/1810.04805)                                                         | Devlin, Chang, Lee, Toutanova                                         | 2018 | Foundations             | 🟡 EXPERIMENT | Intermediate | ⬜    | ⬜           | ⬜          | [papers/03-bert](papers/03-bert/)                                             |
| 4   | [Language Models are Few-Shot Learners (GPT-3)](https://arxiv.org/abs/2005.14165)                                                                 | Brown, Mann, Ryder, Subbiah, Kaplan, et al.                           | 2020 | Foundations             | 🔵 STUDY      | Intermediate | ⬜    | ⬜           | ⬜          | [papers/04-gpt3](papers/04-gpt3/)                                             |
| 5   | [Scaling Laws for Neural Language Models](https://arxiv.org/abs/2001.08361)                                                                       | Kaplan, McCandlish, Henighan, Brown, et al.                           | 2020 | Scaling                 | 🔵 STUDY      | Intermediate | ⬜    | ⬜           | ⬜          | [papers/05-scaling-laws](papers/05-scaling-laws/)                             |
| 6   | [Training Compute-Optimal Large Language Models](https://arxiv.org/abs/2203.15556)                                                                | Hoffmann, Borgeaud, Mensch, Buchatskaya, et al.                       | 2022 | Scaling                 | 🔵 STUDY      | Intermediate | ⬜    | ⬜           | ⬜          | [papers/06-chinchilla](papers/06-chinchilla/)                                 |
| 7   | [LLaMA: Open and Efficient Foundation Language Models](https://arxiv.org/abs/2302.13971)                                                          | Touvron, Lavril, Izacard, Martinet, et al.                            | 2023 | Architecture            | 🟢 IMPLEMENT  | Advanced     | ⬜    | ⬜           | ⬜          | [papers/07-llama](papers/07-llama/)                                           |
| 8   | [RoFormer: Enhanced Transformer with Rotary Position Embedding](https://arxiv.org/abs/2104.09864)                                                 | Su, Lu, Pan, Murtadha, Wen, Liu                                       | 2021 | Architecture            | 🟢 IMPLEMENT  | Advanced     | ⬜    | ⬜           | ⬜          | [papers/08-roformer](papers/08-roformer/)                                     |
| 9   | [FlashAttention: Fast and Memory-Efficient Exact Attention](https://arxiv.org/abs/2205.14135)                                                     | Dao, Fu, Ermon, Rudra, Re                                             | 2022 | Systems                 | 🟡 EXPERIMENT | Advanced     | ⬜    | ⬜           | ⬜          | [papers/09-flash-attention](papers/09-flash-attention/)                       |
| 10  | [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401)                                              | Lewis, Perez, Piktus, Petroni, et al.                                 | 2020 | Knowledge               | 🟡 EXPERIMENT | Intermediate | ⬜    | ⬜           | ⬜          | [papers/10-rag](papers/10-rag/)                                               |
| 11  | [Training language models to follow instructions with human feedback (InstructGPT)](https://arxiv.org/abs/2203.02155)                             | Ouyang, Wu, Jiang, Almeida, et al.                                    | 2022 | Post-training           | 🟡 EXPERIMENT | Intermediate | ⬜    | ⬜           | ⬜          | [papers/11-instructgpt](papers/11-instructgpt/)                               |
| 12  | [Direct Preference Optimization](https://arxiv.org/abs/2305.18290)                                                                                | Rafailov, Sharma, Mitchell, Ermon, Manning, Finn                      | 2023 | Post-training           | 🟡 EXPERIMENT | Advanced     | ⬜    | ⬜           | ⬜          | [papers/12-dpo](papers/12-dpo/)                                               |
| 13  | [Chain-of-Thought Prompting Elicits Reasoning in Large Language Models](https://arxiv.org/abs/2201.11903)                                         | Wei, Wang, Schuurmans, Bosma, et al.                                  | 2022 | Reasoning               | 🔵 STUDY      | Beginner     | ⬜    | ⬜           | ⬜          | [papers/13-chain-of-thought](papers/13-chain-of-thought/)                     |
| 14  | [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629)                                                    | Yao, Zhao, Yu, Du, Shafran, Narasimhan, Cao                           | 2022 | Reasoning / Agents      | 🟡 EXPERIMENT | Intermediate | ⬜    | ⬜           | ⬜          | [papers/14-react](papers/14-react/)                                           |
| 15  | [DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via RL](https://arxiv.org/abs/2501.12948)                                                | DeepSeek-AI                                                           | 2025 | Reasoning               | 🔵 STUDY      | Advanced     | ⬜    | ⬜           | ⬜          | [papers/15-deepseek-r1](papers/15-deepseek-r1/)                               |
| 16  | [Qwen3 Technical Report](https://arxiv.org/abs/2505.09388)                                                                                        | Qwen Team, Alibaba                                                    | 2025 | Architecture            | 🔵 STUDY      | Advanced     | ⬜    | ⬜           | ⬜          | [papers/16-qwen3](papers/16-qwen3/)                                           |
| 17  | [Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer](https://arxiv.org/abs/1701.06538)                               | Shazeer, Mirhoseini, Maziarz, Davis, Le, Hinton, Dean                 | 2017 | MoE                     | 🟢 IMPLEMENT  | Advanced     | ⬜    | ⬜           | ⬜          | [papers/17-sparsely-gated-moe](papers/17-sparsely-gated-moe/)                 |
| 18  | [Switch Transformers: Scaling to Trillion Parameter Models](https://arxiv.org/abs/2101.03961)                                                     | Fedus, Zoph, Shazeer                                                  | 2021 | MoE                     | 🟡 EXPERIMENT | Advanced     | ⬜    | ⬜           | ⬜          | [papers/18-switch-transformer](papers/18-switch-transformer/)                 |
| 19  | [Mixtral of Experts](https://arxiv.org/abs/2401.04088)                                                                                            | Jiang, Sablayrolles, Roux, Mensch, et al. (Mistral AI)                | 2024 | MoE                     | 🔵 STUDY      | Advanced     | ⬜    | ⬜           | ⬜          | [papers/19-mixtral](papers/19-mixtral/)                                       |
| 20  | [Sparse Upcycling: Training Mixture-of-Experts from Dense Checkpoints](https://arxiv.org/abs/2212.05055)                                          | Komatsuzaki, Puigcerver, Lee-Thorp, Ruiz, et al.                      | 2022 | MoE                     | 🟡 EXPERIMENT | Advanced     | ⬜    | ⬜           | ⬜          | [papers/20-sparse-upcycling](papers/20-sparse-upcycling/)                     |
| 21  | [The Platonic Representation Hypothesis](https://arxiv.org/abs/2405.07987)                                                                        | Huh, Cheung, Wang, Isola                                              | 2024 | Representation Learning | 🔵 STUDY      | Advanced     | ⬜    | ⬜           | ⬜          | [papers/21-platonic-representation](papers/21-platonic-representation/)       |
| 22  | [Textbooks Are All You Need](https://arxiv.org/abs/2306.11644)                                                                                    | Gunasekar, Zhang, Aneja, Mendes, et al. (Microsoft)                   | 2023 | Data                    | 🔵 STUDY      | Intermediate | ⬜    | ⬜           | ⬜          | [papers/22-textbooks-are-all-you-need](papers/22-textbooks-are-all-you-need/) |
| 23  | [Scaling Monosemanticity: Extracting Interpretable Features from Claude 3 Sonnet](https://transformer-circuits.pub/2024/scaling-monosemanticity/) | Templeton, et al. (Anthropic)                                         | 2024 | Interpretability        | 🔵 STUDY      | Advanced     | ⬜    | ⬜           | ⬜          | [papers/23-scaling-monosemanticity](papers/23-scaling-monosemanticity/)       |
| 24  | [PaLM: Scaling Language Modeling with Pathways](https://arxiv.org/abs/2204.02311)                                                                 | Chowdhery, Narang, Devlin, Bosma, et al. (Google)                     | 2022 | Scaling                 | 🔵 STUDY      | Advanced     | ⬜    | ⬜           | ⬜          | [papers/24-palm](papers/24-palm/)                                             |
| 25  | [GLaM: Efficient Scaling of Language Models with Mixture-of-Experts](https://arxiv.org/abs/2112.06919)                                            | Du, Huang, Dai, Tong, et al. (Google)                                 | 2021 | MoE                     | 🔵 STUDY      | Advanced     | ⬜    | ⬜           | ⬜          | [papers/25-glam](papers/25-glam/)                                             |
| 26  | [The Smol Training Playbook](https://huggingface.co/spaces/HuggingFaceTB/smol-training-playbook)                                                  | Hugging Face (HuggingFaceTB)                                          | 2025 | Practical Training      | 🔵 STUDY      | Intermediate | ⬜    | ⬜           | ⬜          | [papers/26-smol-training-playbook](papers/26-smol-training-playbook/)         |

Paper links are verified against arXiv / official sources at the time of
writing. Entries marked `TBD` for official code have not been verified yet
and will be filled in before that paper is worked on — see
[CONTRIBUTING.md](CONTRIBUTING.md) if you spot a broken or outdated link.

## Repository structure

```
papers/            one folder per paper, using papers/_template
experiments/        controlled experiments, using experiments/_template
implementations/    reusable from-scratch components (tokenizer, attention, moe, ...)
notes/              running technical notes by topic
research/           work that goes beyond reproducing a paper
progress/           weekly and monthly progress reports
assets/             diagrams, plots, images
configs/            experiment configuration templates
scripts/, src/, tests/   shared tooling, source, and tests
```

## Engineering standards

- Python 3.11+, PyTorch as the primary framework.
- Core implementations (attention, tokenizer, Transformer blocks) are written
  from scratch when the goal is *understanding*. Libraries (PEFT, Accelerate,
  vLLM, FlashAttention, Hugging Face Transformers/Datasets) are used when the
  goal is *engineering* — every such use is documented explicitly.
- Assume a single consumer NVIDIA GPU. Every experiment has a small-scale
  mode, configurable model/batch sizes, and a CPU fallback where reasonable.
- Every experiment records its config, seed, dataset, and hardware — see
  [configs/experiment_config.yaml](configs/experiment_config.yaml).

## Learning philosophy

```
LEARN → IMPLEMENT → EXPERIMENT → ANALYZE → DOCUMENT → SHARE → REPEAT
```

Research progression for anything in [research/](research/):

```
Reimplement → Reproduce → Modify → Experiment → Find something interesting
→ Form a hypothesis → Run controlled experiments → Publish
```

## Community

See [COMMUNITY.md](COMMUNITY.md) and [CONTRIBUTING.md](CONTRIBUTING.md) for
how to reproduce an experiment, propose a paper, report a mistake, or
collaborate.

## The long-term goal

This started with *Attention Is All You Need*. The goal is to eventually
publish a first, honest, original LLM research project — whenever that
milestone is actually reached, not on a fixed schedule.

The real objective was never the checklist. It's becoming capable of:
reading an LLM paper, understanding the mathematics, implementing the core
idea, training a model, designing experiments, analyzing results,
communicating findings, collaborating with other researchers, and eventually
producing original research.

## License

Code is licensed under the [MIT License](LICENSE). Notes and writeups are
for educational/learning-in-public purposes; see individual paper folders
for citations to original work.
