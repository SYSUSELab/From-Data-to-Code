---
layout: default
title: "RQ4: Detection Methods"
parent: Home
nav_order: 5
---

# 🔍 RQ4: Detection Methods

Detection techniques are evolving from rigid static analysis to dynamic, model-driven, and hybrid evaluation frameworks. They form the diagnostic foundation of LLM quality governance and are classified into two categories:

## 1. Code-Level Detection

Identifies defects in generated code (e.g., runtime failures, hallucinations, security vulnerabilities) using three main paradigms:

- **Dynamic Analysis**: Test-based execution (unit tests, functional benchmarks) and runtime monitoring to assess execution accuracy and resource efficiency.
- **Static Analysis**: Rule-based detection (via tools like SonarQube, Semgrep) and manual inspection to find syntax errors, vulnerabilities, and code smells without executing the code.
- **Model-based Detection**: "LLM-as-a-judge" techniques (direct, prompt-engineered, or fine-tuned evaluation) and lightweight ML classifiers for scalable semantic filtering.

<div align="center">
  <img src="{{ site.baseurl }}/images/generated_code_issues_detection.png" alt="Taxonomy of Code Issue Detection Methods" width="100%">
  <p><em>Fig. 6. Taxonomy of Code Issue Detection Techniques</em></p>
</div>

## 2. Data-Level Detection

Targets the integrity, provenance, and representativeness of the underlying training data:

- **Dynamic Analysis**: Execution-based validation (checking if scraped code compiles) and metric drift monitoring (detecting data leakage or contamination through training loss curves).
- **Static Analysis**: Rule-based detection, human review, and provenance tracing (using file hashes to identify duplicate or benchmark-contaminated data).
- **Model-based Detection**: High-throughput semantic screening using LLMs or lightweight classifiers to evaluate sample readability, information entropy, and potential hazards.

<div align="center">
  <img src="{{ site.baseurl }}/images/data_quality_issues_detection.png" alt="Taxonomy of Dataset Issue Detection Methods" width="100%">
  <p><em>Fig. 7. Taxonomy of Training Data Issue Detection Techniques</em></p>
</div>

## 📄 Papers Referenced

1. LLMs Meet Library Evolution [2024-06] [[paper](https://arxiv.org/abs/2406.09834)]
2. Less is More [2025-02] [[paper](https://arxiv.org/abs/2502.14212)]
3. Qwen [2023-09] [[paper](https://arxiv.org/abs/2309.16609)]
4. Qwen2 [2024-07] [[paper](https://arxiv.org/abs/2407.10671)]
5. DataMan [2025-02] [[paper](https://arxiv.org/abs/2502.19363)]
6. Phi-4 [2024-12] [[paper](https://arxiv.org/abs/2412.08905)]
7. Copilot Security [2022-04] [[paper](https://arxiv.org/abs/2204.04741)]
8. Copilot Evaluation [2025-01] [[paper](https://doi.org/10.1145/3524842.3528470)]
9. HalluCode [2024-04] [[paper](https://arxiv.org/abs/2404.00971)]
10. CodeHalu [2024-05] [[paper](https://arxiv.org/abs/2405.00253)]
11. EffiBench [2024-02] [[paper](https://arxiv.org/abs/2402.02037)]
12. Mercury [2024-02] [[paper](https://arxiv.org/abs/2402.07844)]
13. SStuBs [2023-03] [[paper](https://arxiv.org/abs/2303.11455)]
14. package hallucinations [2024-06] [[paper](https://arxiv.org/abs/2406.10279)]
15. HallTrigger [2024-07] [[paper](https://arxiv.org/abs/2407.04831)]
16. Large Language Models for Code [2023-02] [[paper](https://arxiv.org/abs/2302.05319)]
17. Purple Llama CYBERSECEVAL [2023-12] [[paper](https://arxiv.org/abs/2312.04724)]
18. Lost at C [2022-08] [[paper](https://arxiv.org/abs/2208.09727)]
19. AI Assistants Security [2022-11] [[paper](https://arxiv.org/abs/2211.03622)]
20. The Counterfeit Conundrum [2024-02] [[paper](https://arxiv.org/abs/2402.19475)]
21. Bugs in LLM-generated Code [2024-03] [[paper](https://arxiv.org/abs/2403.08937)]
22. GitHub Copilot, Amazon CodeWhisperer, ChatGPT [2023-04] [[paper](https://arxiv.org/abs/2304.10778)]
23. ChatGPT Code Quality [2023-08] [[paper](https://arxiv.org/abs/2308.04838)]
24. CloudAPIBench [2024-07] [[paper](https://arxiv.org/abs/2407.09726)]
25. CodeMirage [2024-08] [[paper](https://arxiv.org/abs/2408.08333)]
26. LLM-generated Code Efficiency [2024-04] [[paper](https://arxiv.org/abs/2404.06041)]
27. Syntactic Robustness [2024-04] [[paper](https://arxiv.org/abs/2404.01535)]
28. DeSec [2024-10] [[paper](https://arxiv.org/abs/2410.08858)]
29. Bias Unveiled [2024-11] [[paper](https://arxiv.org/abs/2411.10351)]
30. FairCoder [2025-01] [[paper](https://arxiv.org/abs/2501.05396)]
31. From Effectiveness to Efficiency [2024-06] [[paper](https://arxiv.org/abs/2406.00602)]
32. ENAMEL [2024-06] [[paper](https://arxiv.org/abs/2406.06647)]
33. DeVAIC [2024-04] [[paper](https://arxiv.org/abs/2404.07548)]
34. PTMs [2024-11] [[paper](https://arxiv.org/abs/2411.10565)]
35. Codequal Analyzer [2025-06] [[paper](https://arxiv.org/abs/2506.02211)]
36. Artificial-Intelligence Generated Code Considered Harmful [2024-09] [[paper](https://arxiv.org/abs/2409.19182)]
37. Unveiling Inefficiencies in LLM-Generated Code [2025-03] [[paper](https://arxiv.org/abs/2503.06327)]
38. Python Tests Quality [2025-06] [[paper](https://arxiv.org/abs/2506.14297)]
39. CoQuIR [2025-06] [[paper](https://arxiv.org/abs/2506.11066)]
40. REAL [2025-05] [[paper](https://arxiv.org/abs/2505.22704)]
41. CIDRe [2025-05] [[paper](https://arxiv.org/abs/2505.19757)]
42. Infinite-Instruct [2025-05] [[paper](https://arxiv.org/abs/2505.23177)]
43. Quality In, Quality Out [2025-03] [[paper](https://arxiv.org/abs/2503.11402)]
44. Security and Quality in LLM-Generated Code [2025-02] [[paper](https://arxiv.org/abs/2502.01853)]
45. SwallowCode [2025-05] [[paper](https://arxiv.org/abs/2505.02881)]
46. ROSE [2025-07] [[paper](https://arxiv.org/abs/2507.12561)]
47. Refining ChatGPT-Generated Code [2023-07] [[paper](https://arxiv.org/abs/2307.12596)]
48. Qwen3 [2025-05] [[paper](https://arxiv.org/abs/2505.09388)]
49. Qwen2.5 [2024-12] [[paper](https://arxiv.org/abs/2412.15115)]
50. TeleChat [2025-07] [[paper](https://arxiv.org/abs/2507.18013)]
51. Kimi K2 [2025-07] [[paper](https://arxiv.org/abs/2507.20534)]
52. ReCode [2025-06] [[paper](https://arxiv.org/abs/2506.20495)]
53. Seed-Coder [2025-06] [[paper](https://arxiv.org/abs/2506.03524)]
54. Data-efficient Fine-tuning [2025-04] [[paper](https://arxiv.org/abs/2504.12687)]
55. CRPE [2025-05] [[paper](https://arxiv.org/abs/2505.10594)]
56. DeepSeek-Coder [2024-01] [[paper](https://arxiv.org/abs/2401.14196)]
57. StarCoder 2 and The Stack v2 [2024-02] [[paper](https://arxiv.org/abs/2402.19173)]
58. CodeSmellEval [2024-12] [[paper](https://arxiv.org/abs/2412.18989)]
59. RPG [2025-05] [[paper](https://arxiv.org/abs/2505.10402)]
60. Repetition In Repetition Out [2023-10] [[paper](https://arxiv.org/abs/2310.10226)]
61. Every Sample Matters [2025-03] [[paper](https://arxiv.org/abs/2503.17793)]
62. WaveCoder [2023-12] [[paper](https://arxiv.org/abs/2312.14187)]
63. Brevity is the soul of wit [2024-07] [[paper](https://arxiv.org/abs/2407.00434)]
64. Benchmark Builders [2025-04] [[paper](https://arxiv.org/abs/2504.19444)]
65. Beyond Correctness [2024-07] [[paper](https://arxiv.org/abs/2407.11470)]
66. Generated Code Diversity [2024-08] [[paper](https://arxiv.org/abs/2408.14504)]
67. CodeMI [2024-04] [[paper](https://arxiv.org/abs/2404.14296)]
68. DataComp-LM [2024-06] [[paper](https://arxiv.org/abs/2406.11794)]
69. Codex [2021-07] [[paper](https://arxiv.org/abs/2107.03374)]
70. Path Planning Evaluation [2025-04] [[paper](https://arxiv.org/abs/2504.21276)]
71. CODEJUDGE [2024-01] [[paper](https://aclanthology.org/2024.emnlp-main.1118.pdf?utm_source=chatgpt.com)]
72. Datasets for Large Language Models [2024-02] [[paper](https://arxiv.org/abs/2402.18041)]
73. Synthetic Data Generation [2025-01] [[paper](https://ieeexplore.ieee.org/document/11080380)]
74. Cracks in The Stack [2025-05] [[paper](https://ieeexplore.ieee.org/document/11028470)]
75. Unseen Horizons [2025-04] [[paper](https://ieeexplore.ieee.org/document/11029836)]
76. MG-Verilog [2024-06] [[paper](https://ieeexplore.ieee.org/document/10691738)]
77. Code Generation Survey [2024-08] [[paper](https://dl.acm.org/doi/10.1145/3747588)]
78. DataRecipe [2024-10] [[paper](https://dl.acm.org/doi/10.1145/3691620.3695593)]
79. Training Data Extraction [2025-08] [[paper](https://dl.acm.org/doi/10.1145/3709018.3736331)]
80. aiXcoder-7B [2025-04] [[paper](https://ieeexplore.ieee.org/document/11121702)]
81. Imperfect Code Generation [2024-05] [[paper](https://ieeexplore.ieee.org/document/10554837)]
82. Inter-Dataset Code Duplication [2025-01] [[paper](https://ieeexplore.ieee.org/document/10759822)]
83. LLM-ProS [2025-05] [[paper](https://ieeexplore.ieee.org/document/11028406)]
84. ClassEval [2024-6] [[paper](https://ieeexplore.ieee.org/document/10549472)]
85. Uncovering Pretraining Code in LLMs [2025-11] [[paper](https://arxiv.org/abs/2511.07033)]
86. RealSec-Bench [2026-01] [[paper](https://arxiv.org/abs/2601.22706)]
87. ShortCoder [2026-01] [[paper](https://arxiv.org/abs/2601.09703)]
88. APIKG4SYN [2025-11] [[paper](https://arxiv.org/abs/2512.00380)]
89. MultiCodeIF [2025-07] [[paper](https://arxiv.org/abs/2507.00699)]
90. Beyond Functional Correctness [2024-06] [[paper](https://arxiv.org/abs/2407.00456)]
91. Adadec [2025-06] [[paper](https://arxiv.org/html/2506.08980v1)]
92. Code Copycat Conundrum [2025-04] [[paper](https://arxiv.org/abs/2504.12608)]
93. AllianceCoder [2025-03] [[paper](https://arxiv.org/abs/2503.20589)]
94. RustEvo^ 2 [2025-03] [[paper](https://arxiv.org/abs/2503.16922)]
95. RobGen [2025-03] [[paper](https://arxiv.org/abs/2503.20197)]
96. Llm Hallucinations in Practical Code Generation [2024-09] [[paper](https://arxiv.org/abs/2409.20550)]
97. COFFE [2025-02] [[paper](https://arxiv.org/abs/2502.02827)]
98. AATK Benchmark [2021-08] [[paper](https://dl.acm.org/doi/10.1145/3610721)]
