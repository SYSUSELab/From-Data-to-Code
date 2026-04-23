---
layout: default
title: "RQ1: Code Quality Issues"
parent: Home
nav_order: 2
---

# 💻 RQ1: Generated Code Quality Issues

We discard vague concepts like generic "code hallucination" and establish a unified taxonomy encompassing **9 core dimensions** of quality issues in LLM-generated code:

1. **Correctness**: Functional accuracy and executability, categorized into syntax errors, logical flaws, and API misuse.
2. **Security**: Resilience against malicious exploitation, categorized into inherent design flaws and external vulnerabilities.
3. **Compliance**: Adherence to legal, ethical, and safety standards, categorized into copyright infringement, privacy leakage, and malicious code generation.
4. **Robustness**: Ability to handle abnormal inputs gracefully, manifesting as inadequate error handling and boundary condition failures.
5. **Maintainability**: Ease of long-term code modification, categorized into disorganized structure and low reusability.
6. **Understandability**: Human-readability and clarity, manifesting as poor naming conventions and lack of documentation.
7. **Efficiency**: Optimal system resource utilization, categorized into suboptimal time complexity and improper memory management.
8. **Parsimony of Output**: Conciseness of generated results, manifesting as redundant logic, useless loops, and extreme verbosity.
9. **Miscellaneous**: Anomalies outside the core eight dimensions, primarily manifesting as instruction-following failures.

<div align="center">
  <img src="{{ site.baseurl }}/images/generated_code_issues.png" alt="Taxonomy of Generated Code Quality Issues" width="100%">
  <p><em>Fig. 3. Taxonomy of Generated Code Quality Issues</em></p>
</div>

## 📄 Papers Referenced

1. LLMs Meet Library Evolution [2024-06] [[paper](https://arxiv.org/abs/2406.09834)]
2. Copilot Security [2022-04] [[paper](https://arxiv.org/abs/2204.04741)]
3. Copilot Evaluation [2025-01] [[paper](https://doi.org/10.1145/3524842.3528470)]
4. HalluCode [2024-04] [[paper](https://arxiv.org/abs/2404.00971)]
5. CodeHalu [2024-05] [[paper](https://arxiv.org/abs/2405.00253)]
6. EffiBench [2024-02] [[paper](https://arxiv.org/abs/2402.02037)]
7. Mercury [2024-02] [[paper](https://arxiv.org/abs/2402.07844)]
8. SStuBs [2023-03] [[paper](https://arxiv.org/abs/2303.11455)]
9. package hallucinations [2024-06] [[paper](https://arxiv.org/abs/2406.10279)]
10. HallTrigger [2024-07] [[paper](https://arxiv.org/abs/2407.04831)]
11. Large Language Models for Code [2023-02] [[paper](https://arxiv.org/abs/2302.05319)]
12. Purple Llama CYBERSECEVAL [2023-12] [[paper](https://arxiv.org/abs/2312.04724)]
13. Lost at C [2022-08] [[paper](https://arxiv.org/abs/2208.09727)]
14. AI Assistants Security [2022-11] [[paper](https://arxiv.org/abs/2211.03622)]
15. The Counterfeit Conundrum [2024-02] [[paper](https://arxiv.org/abs/2402.19475)]
16. Bugs in LLM-generated Code [2024-03] [[paper](https://arxiv.org/abs/2403.08937)]
17. GitHub Copilot, Amazon CodeWhisperer, ChatGPT [2023-04] [[paper](https://arxiv.org/abs/2304.10778)]
18. ChatGPT Code Quality [2023-08] [[paper](https://arxiv.org/abs/2308.04838)]
19. CloudAPIBench [2024-07] [[paper](https://arxiv.org/abs/2407.09726)]
20. CodeMirage [2024-08] [[paper](https://arxiv.org/abs/2408.08333)]
21. LLM-generated Code Efficiency [2024-04] [[paper](https://arxiv.org/abs/2404.06041)]
22. AutoAPIEval [2024-09] [[paper](https://arxiv.org/abs/2409.15228)]
23. DeSec [2024-10] [[paper](https://arxiv.org/abs/2410.08858)]
24. When Fine-Tuning LLMs Meets Data Privacy [2024-12] [[paper](https://arxiv.org/abs/2412.01072)]
25. Bias Unveiled [2024-11] [[paper](https://arxiv.org/abs/2411.10351)]
26. FairCoder [2025-01] [[paper](https://arxiv.org/abs/2501.05396)]
27. CodeIP [2024-04] [[paper](https://arxiv.org/abs/2404.15639)]
28. From Effectiveness to Efficiency [2024-06] [[paper](https://arxiv.org/abs/2406.00602)]
29. ENAMEL [2024-06] [[paper](https://arxiv.org/abs/2406.06647)]
30. DeVAIC [2024-04] [[paper](https://arxiv.org/abs/2404.07548)]
31. PTMs [2024-11] [[paper](https://arxiv.org/abs/2411.10565)]
32. Software Librarian [2024-08] [[paper](https://arxiv.org/abs/2408.05128)]
33. Codequal Analyzer [2025-06] [[paper](https://arxiv.org/abs/2506.02211)]
34. Artificial-Intelligence Generated Code Considered Harmful [2024-09] [[paper](https://arxiv.org/abs/2409.19182)]
35. Unveiling Inefficiencies in LLM-Generated Code [2025-03] [[paper](https://arxiv.org/abs/2503.06327)]
36. Python Tests Quality [2025-06] [[paper](https://arxiv.org/abs/2506.14297)]
37. CoQuIR [2025-06] [[paper](https://arxiv.org/abs/2506.11066)]
38. REAL [2025-05] [[paper](https://arxiv.org/abs/2505.22704)]
39. CIDRe [2025-05] [[paper](https://arxiv.org/abs/2505.19757)]
40. Infinite-Instruct [2025-05] [[paper](https://arxiv.org/abs/2505.23177)]
41. Quality In, Quality Out [2025-03] [[paper](https://arxiv.org/abs/2503.11402)]
42. Security and Quality in LLM-Generated Code [2025-02] [[paper](https://arxiv.org/abs/2502.01853)]
43. SwallowCode [2025-05] [[paper](https://arxiv.org/abs/2505.02881)]
44. ROSE [2025-07] [[paper](https://arxiv.org/abs/2507.12561)]
45. Refining ChatGPT-Generated Code [2023-07] [[paper](https://arxiv.org/abs/2307.12596)]
46. ReCode [2025-06] [[paper](https://arxiv.org/abs/2506.20495)]
47. Seed-Coder [2025-06] [[paper](https://arxiv.org/abs/2506.03524)]
48. Data-efficient Fine-tuning [2025-04] [[paper](https://arxiv.org/abs/2504.12687)]
49. CRPE [2025-05] [[paper](https://arxiv.org/abs/2505.10594)]
50. DeepSeek-Coder [2024-01] [[paper](https://arxiv.org/abs/2401.14196)]
51. CodeSmellEval [2024-12] [[paper](https://arxiv.org/abs/2412.18989)]
52. RPG [2025-05] [[paper](https://arxiv.org/abs/2505.10402)]
53. Repetition In Repetition Out [2023-10] [[paper](https://arxiv.org/abs/2310.10226)]
54. Beyond Correctness [2024-07] [[paper](https://arxiv.org/abs/2407.11470)]
55. Generated Code Diversity [2024-08] [[paper](https://arxiv.org/abs/2408.14504)]
56. CodeMI [2024-04] [[paper](https://arxiv.org/abs/2404.14296)]
57. CodeCipher [2024-10] [[paper](https://arxiv.org/abs/2410.05797)]
58. Code Llama [2023-08] [[paper](https://arxiv.org/abs/2308.12950)]
59. Codex [2021-07] [[paper](https://arxiv.org/abs/2107.03374)]
60. Path Planning Evaluation [2025-04] [[paper](https://arxiv.org/abs/2504.21276)]
61. CODEJUDGE [2024-01] [[paper](https://aclanthology.org/2024.emnlp-main.1118.pdf?utm_source=chatgpt.com)]
62. Synthetic Data Generation [2025-01] [[paper](https://ieeexplore.ieee.org/document/11080380)]
63. Unseen Horizons [2025-04] [[paper](https://ieeexplore.ieee.org/document/11029836)]
64. Code Generation Survey [2024-08] [[paper](https://dl.acm.org/doi/10.1145/3747588)]
65. DataRecipe [2024-10] [[paper](https://dl.acm.org/doi/10.1145/3691620.3695593)]
66. aiXcoder-7B [2025-04] [[paper](https://ieeexplore.ieee.org/document/11121702)]
67. Imperfect Code Generation [2024-05] [[paper](https://ieeexplore.ieee.org/document/10554837)]
68. ClassEval [2024-6] [[paper](https://ieeexplore.ieee.org/document/10549472)]
69. UCD-Training [2026-02] [[paper](https://arxiv.org/abs/2602.20799)]
70. DRAINCODE [2026-01] [[paper](https://arxiv.org/abs/2601.20615)]
71. RealSec-Bench [2026-01] [[paper](https://arxiv.org/abs/2601.22706)]
72. ShortCoder [2026-01] [[paper](https://arxiv.org/abs/2601.09703)]
73. APIKG4SYN [2025-11] [[paper](https://arxiv.org/abs/2512.00380)]
74. MultiCodeIF [2025-07] [[paper](https://arxiv.org/abs/2507.00699)]
75. Beyond Functional Correctness [2024-06] [[paper](https://arxiv.org/abs/2407.00456)]
76. Adadec [2025-06] [[paper](https://arxiv.org/html/2506.08980v1)]
77. Code Copycat Conundrum [2025-04] [[paper](https://arxiv.org/abs/2504.12608)]
78. AllianceCoder [2025-03] [[paper](https://arxiv.org/abs/2503.20589)]
79. RustEvo^ 2 [2025-03] [[paper](https://arxiv.org/abs/2503.16922)]
80. RobGen [2025-03] [[paper](https://arxiv.org/abs/2503.20197)]
81. Llm Hallucinations in Practical Code Generation [2024-09] [[paper](https://arxiv.org/abs/2409.20550)]
82. COFFE [2025-02] [[paper](https://arxiv.org/abs/2502.02827)]
83. AATK Benchmark [2021-08] [[paper](https://dl.acm.org/doi/10.1145/3610721)]
