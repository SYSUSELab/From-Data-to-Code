---
layout: default
title: "RQ5: Governance Strategies"
parent: Home
nav_order: 6
---

# 🛠️ RQ5: Governance Strategies

We synthesize a **Multi-layered Governance Framework** spanning the entire data lifecycle and model inference stages to address quality defects:

## 1. Code-Level Mitigation

- **Model-level**: SFT, RLHF/DPO, Reward-based optimization (combining execution correctness with static metrics), and Regularization-based stabilization to prevent mode collapse.
- **Generation-level**:
  - _Pre-generation_: Prompt Engineering, RAG, and Agent-based workflows.
  - _In-generation_: Adaptive decoding constraints and Iterative Self-reflection.
  - _Post-generation_: Automated AST-level repairs and sandbox execution filtering.

<div align="center">
  <img src="{{ site.baseurl }}/images/generated_code_issues_detection.png" alt="Taxonomy of Code Issue Mitigation Strategies" width="100%">
  <p><em>Fig. 8. Taxonomy of Code Issue Mitigation Strategies</em></p>
</div>

## 2. Data-Level Mitigation

- **Cleaning & Filtering**: Execution-feedback elimination, static rule sanitization, and LLM-driven semantic cleaning to remove noise and vulnerabilities.
- **Data Balancing**: Stratified resampling across programming languages, domains, and difficulty levels to mitigate representation bias.
- **Data Enhancement**: Using LLMs or formatting tools to refactor, add docstrings, and standardize existing low-quality code.
- **Data Augmentation**: Expanding datasets via high-quality synthetic generation (rule/LLM-based) and integration of curated open-source repositories.

<div align="center">
  <img src="{{ site.baseurl }}/images/data_quality_issues_mitigation.png" alt="Taxonomy of Dataset Issue Mitigation Strategies" width="100%">
  <p><em>Fig. 9. Taxonomy of Training Data Issue Mitigation Strategies</em></p>
</div>

## 📄 Papers Referenced

1. LLMs Meet Library Evolution [2024-06] [[paper](https://arxiv.org/abs/2406.09834)]
2. Less is More [2025-02] [[paper](https://arxiv.org/abs/2502.14212)]
3. Qwen [2023-09] [[paper](https://arxiv.org/abs/2309.16609)]
4. Qwen2 [2024-07] [[paper](https://arxiv.org/abs/2407.10671)]
5. DataMan [2025-02] [[paper](https://arxiv.org/abs/2502.19363)]
6. Phi-4 [2024-12] [[paper](https://arxiv.org/abs/2412.08905)]
7. SStuBs [2023-03] [[paper](https://arxiv.org/abs/2303.11455)]
8. package hallucinations [2024-06] [[paper](https://arxiv.org/abs/2406.10279)]
9. Large Language Models for Code [2023-02] [[paper](https://arxiv.org/abs/2302.05319)]
10. CloudAPIBench [2024-07] [[paper](https://arxiv.org/abs/2407.09726)]
11. AutoAPIEval [2024-09] [[paper](https://arxiv.org/abs/2409.15228)]
12. Codequal Analyzer [2025-06] [[paper](https://arxiv.org/abs/2506.02211)]
13. REAL [2025-05] [[paper](https://arxiv.org/abs/2505.22704)]
14. CIDRe [2025-05] [[paper](https://arxiv.org/abs/2505.19757)]
15. Infinite-Instruct [2025-05] [[paper](https://arxiv.org/abs/2505.23177)]
16. Quality In, Quality Out [2025-03] [[paper](https://arxiv.org/abs/2503.11402)]
17. SwallowCode [2025-05] [[paper](https://arxiv.org/abs/2505.02881)]
18. Refining ChatGPT-Generated Code [2023-07] [[paper](https://arxiv.org/abs/2307.12596)]
19. Qwen3 [2025-05] [[paper](https://arxiv.org/abs/2505.09388)]
20. Qwen2.5 [2024-12] [[paper](https://arxiv.org/abs/2412.15115)]
21. TeleChat [2025-07] [[paper](https://arxiv.org/abs/2507.18013)]
22. Kimi K2 [2025-07] [[paper](https://arxiv.org/abs/2507.20534)]
23. ReCode [2025-06] [[paper](https://arxiv.org/abs/2506.20495)]
24. Seed-Coder [2025-06] [[paper](https://arxiv.org/abs/2506.03524)]
25. Data-efficient Fine-tuning [2025-04] [[paper](https://arxiv.org/abs/2504.12687)]
26. CRPE [2025-05] [[paper](https://arxiv.org/abs/2505.10594)]
27. DeepSeek-Coder [2024-01] [[paper](https://arxiv.org/abs/2401.14196)]
28. Code Pretraining [2024-09] [[paper](https://arxiv.org/abs/2409.04556)]
29. StarCoder 2 and The Stack v2 [2024-02] [[paper](https://arxiv.org/abs/2402.19173)]
30. CodeSmellEval [2024-12] [[paper](https://arxiv.org/abs/2412.18989)]
31. RPG [2025-05] [[paper](https://arxiv.org/abs/2505.10402)]
32. Repetition In Repetition Out [2023-10] [[paper](https://arxiv.org/abs/2310.10226)]
33. Brevity is the soul of wit [2024-07] [[paper](https://arxiv.org/abs/2407.00434)]
34. Benchmark Builders [2025-04] [[paper](https://arxiv.org/abs/2504.19444)]
35. CodeCipher [2024-10] [[paper](https://arxiv.org/abs/2410.05797)]
36. DataComp-LM [2024-06] [[paper](https://arxiv.org/abs/2406.11794)]
37. RedStone [2024-12] [[paper](https://arxiv.org/abs/2412.03398)]
38. Code Llama [2023-08] [[paper](https://arxiv.org/abs/2308.12950)]
39. Codex [2021-07] [[paper](https://arxiv.org/abs/2107.03374)]
40. Path Planning Evaluation [2025-04] [[paper](https://arxiv.org/abs/2504.21276)]
41. CODEJUDGE [2024-01] [[paper](https://aclanthology.org/2024.emnlp-main.1118.pdf?utm_source=chatgpt.com)]
42. Synthetic Data Generation [2025-01] [[paper](https://ieeexplore.ieee.org/document/11080380)]
43. Cracks in The Stack [2025-05] [[paper](https://ieeexplore.ieee.org/document/11028470)]
44. MG-Verilog [2024-06] [[paper](https://ieeexplore.ieee.org/document/10691738)]
45. Code Generation Survey [2024-08] [[paper](https://dl.acm.org/doi/10.1145/3747588)]
46. DataRecipe [2024-10] [[paper](https://dl.acm.org/doi/10.1145/3691620.3695593)]
47. aiXcoder-7B [2025-04] [[paper](https://ieeexplore.ieee.org/document/11121702)]
48. Imperfect Code Generation [2024-05] [[paper](https://ieeexplore.ieee.org/document/10554837)]
49. Inter-Dataset Code Duplication [2025-01] [[paper](https://ieeexplore.ieee.org/document/10759822)]
50. LLM-ProS [2025-05] [[paper](https://ieeexplore.ieee.org/document/11028406)]
51. UCD-Training [2026-02] [[paper](https://arxiv.org/abs/2602.20799)]
52. ShortCoder [2026-01] [[paper](https://arxiv.org/abs/2601.09703)]
53. APIKG4SYN [2025-11] [[paper](https://arxiv.org/abs/2512.00380)]
54. MultiCodeIF [2025-07] [[paper](https://arxiv.org/abs/2507.00699)]
55. Beyond Functional Correctness [2024-06] [[paper](https://arxiv.org/abs/2407.00456)]
56. Adadec [2025-06] [[paper](https://arxiv.org/html/2506.08980v1)]
57. Code Copycat Conundrum [2025-04] [[paper](https://arxiv.org/abs/2504.12608)]
58. AllianceCoder [2025-03] [[paper](https://arxiv.org/abs/2503.20589)]
59. RustEvo^ 2 [2025-03] [[paper](https://arxiv.org/abs/2503.16922)]
60. RobGen [2025-03] [[paper](https://arxiv.org/abs/2503.20197)]
61. Llm Hallucinations in Practical Code Generation [2024-09] [[paper](https://arxiv.org/abs/2409.20550)]
62. COFFE [2025-02] [[paper](https://arxiv.org/abs/2502.02827)]
