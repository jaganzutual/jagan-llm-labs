# Roadmap — Building LLMs From First Principles

6 phases, no fixed deadline. Each phase pairs a set of papers with concrete
implementation and experiment goals. Nothing here is fixed in stone — the
roadmap will be adjusted and extended as I learn, but the structure and
honesty requirements stay the same.

Progress legend: ⬜ Not started · 🟨 In progress · 🟩 Complete

---

## Phase 1 — Transformer Foundations

**Status:** ⬜

**Papers**
1. [Attention Is All You Need](https://arxiv.org/abs/1706.03762)
2. [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/)
3. [BERT: Pre-training of Deep Bidirectional Transformers](https://arxiv.org/abs/1810.04805)
4. [Language Models are Few-Shot Learners (GPT-3)](https://arxiv.org/abs/2005.14165)

**Goals**
- Understand tokenization
- Understand embeddings
- Understand self-attention
- Implement multi-head attention
- Implement Transformer blocks
- Understand encoder vs. decoder
- Build a decoder-only Transformer

**Build**
- Mini Transformer
- Mini GPT

---

## Phase 2 — Modern LLM Architectures

**Status:** ⬜

**Papers**
1. [Scaling Laws for Neural Language Models](https://arxiv.org/abs/2001.08361)
2. [Training Compute-Optimal Large Language Models](https://arxiv.org/abs/2203.15556)
3. [LLaMA: Open and Efficient Foundation Language Models](https://arxiv.org/abs/2302.13971)
4. [RoFormer: Enhanced Transformer with Rotary Position Embedding](https://arxiv.org/abs/2104.09864)
5. [FlashAttention: Fast and Memory-Efficient Exact Attention](https://arxiv.org/abs/2205.14135)

**Goals**
- Understand scaling
- Understand compute-optimal training
- Understand RoPE
- Understand RMSNorm
- Understand SwiGLU
- Understand efficient attention
- Understand GPU memory movement

**Build**
- Mini-GPT v2
- Scaling Lab
- FlashAttention benchmark

---

## Phase 3 — Knowledge + Post-Training

**Status:** ⬜

**Papers**
1. [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401)
2. [Training language models to follow instructions with human feedback (InstructGPT)](https://arxiv.org/abs/2203.02155)
3. [Direct Preference Optimization](https://arxiv.org/abs/2305.18290)

**Goals**
- Understand retrieval augmentation
- Understand supervised fine-tuning
- Understand preference optimization
- Understand LoRA/QLoRA as supporting techniques

**Build**
- RAG system
- SFT pipeline
- LoRA fine-tuning
- DPO experiment

---

## Phase 4 — Reasoning + Agents

**Status:** ⬜

**Papers**
1. [Chain-of-Thought Prompting Elicits Reasoning in Large Language Models](https://arxiv.org/abs/2201.11903)
2. [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629)
3. [DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via RL](https://arxiv.org/abs/2501.12948)
4. [Qwen3 Technical Report](https://arxiv.org/abs/2505.09388)

**Goals**
- Understand reasoning prompting
- Understand tool use
- Understand RL for reasoning
- Understand test-time compute
- Understand modern reasoning models

**Build**
- Reasoning benchmark
- Tiny tool-using agent
- Small reasoning experiment

---

## Phase 5 — Mixture of Experts

**Status:** ⬜

**Papers**
1. [Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer](https://arxiv.org/abs/1701.06538)
2. [Switch Transformers: Scaling to Trillion Parameter Models](https://arxiv.org/abs/2101.03961)
3. [Mixtral of Experts](https://arxiv.org/abs/2401.04088)
4. [Sparse Upcycling: Training Mixture-of-Experts from Dense Checkpoints](https://arxiv.org/abs/2212.05055)

**Goals**
- Understand conditional computation
- Routing
- Expert capacity
- Load balancing
- Sparse activation
- Dense → MoE conversion

**Build**
- MoE Transformer
- Router
- Expert system
- Dense → MoE sparse upcycling experiment

---

## Phase 6 — Deeper Research + Original Work

**Status:** ⬜

**Papers**
1. [The Platonic Representation Hypothesis](https://arxiv.org/abs/2405.07987)
2. [Textbooks Are All You Need](https://arxiv.org/abs/2306.11644)
3. [Scaling Monosemanticity: Extracting Interpretable Features from Claude 3 Sonnet](https://transformer-circuits.pub/2024/scaling-monosemanticity/)
4. [PaLM: Scaling Language Modeling with Pathways](https://arxiv.org/abs/2204.02311)
5. [GLaM: Efficient Scaling of Language Models with Mixture-of-Experts](https://arxiv.org/abs/2112.06919)
6. [The Smol Training Playbook](https://huggingface.co/spaces/HuggingFaceTB/smol-training-playbook)

**Goals**
- Understand representation learning
- Understand synthetic data
- Understand interpretability
- Understand large-scale training
- Understand MoE scaling
- Understand practical training workflows

**Final goal:** an original LLM research project.

---

## Full paper database

| #   | Paper                                                                                                                                             | Authors                                                               | Year | Category                | Level        | Difficulty   | Read | Implemented | Experiment | Link                                                                          |
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

## Learning levels

🟢 **IMPLEMENT** — core idea implemented from scratch
🟡 **EXPERIMENT** — concept reproduced at small scale
🔵 **STUDY** — methodology and results understood without full reproduction

