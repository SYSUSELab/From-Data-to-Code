---
layout: default
title: "RQ2: Data Quality Issues"
parent: Home
nav_order: 3
---

# 📊 RQ2: Training Data Quality Issues

We categorize intrinsic flaws within pre-training and fine-tuning corpora into **two core dimensions**:

1. **Code Attribute Quality Issues**: Inherent defects within individual code samples that models explicitly learn, categorized into correctness, security, compliance, robustness, maintainability, understandability, and efficiency flaws.
2. **Non-Code Attribute Quality Issues**: Non-code textual noise and macro-level dataset flaws. Categorized into:
   - **Compliance and Security Risks (Textual)**: Hazards inherent in textual data, categorized into illegal/harmful, copyright-infringing, and privacy-leaking text.
   - **Distribution Imbalance Issues**: Skewed dataset proportions, manifesting as imbalances across programming languages, domains, data types, or difficulty levels.
   - **Redundancy Issues**: Excessive repetition, manifesting as duplicate samples or synthetic data degradation.
   - **Inadequate Diversity**: Insufficient coverage of real-world scenarios, manifesting as underrepresented edge cases or niche business logic.
   - **Data Contamination Risks**: Leakage of evaluation data, primarily manifesting as benchmark test sets embedded in training corpora.
   - **Low-Value Data**: Data contributing little or negatively to learning, categorized into meaningless text, format noise, low-information-density text, erroneous text, and incomplete data.

<div align="center">
  <img src="{{ site.baseurl }}/images/data_quality_issues.png" alt="Taxonomy of Dataset Quality Issues" width="100%">
  <p><em>Fig. 4. Taxonomy of Training Data Quality Issues</em></p>
</div>

## 📄 Papers Referenced

1. LLMs Meet Library Evolution [2024-06] [[paper](https://arxiv.org/abs/2406.09834)]
2. Less is More [2025-02] [[paper](https://arxiv.org/abs/2502.14212)]
3. DataMan [2025-02] [[paper](https://arxiv.org/abs/2502.19363)]
4. Phi-4 [2024-12] [[paper](https://arxiv.org/abs/2412.08905)]
5. SStuBs [2023-03] [[paper](https://arxiv.org/abs/2303.11455)]
6. DeSec [2024-10] [[paper](https://arxiv.org/abs/2410.08858)]
7. CIDRe [2025-05] [[paper](https://arxiv.org/abs/2505.19757)]
8. Infinite-Instruct [2025-05] [[paper](https://arxiv.org/abs/2505.23177)]
9. Quality In, Quality Out [2025-03] [[paper](https://arxiv.org/abs/2503.11402)]
10. SwallowCode [2025-05] [[paper](https://arxiv.org/abs/2505.02881)]
11. Seed-Coder [2025-06] [[paper](https://arxiv.org/abs/2506.03524)]
12. CRPE [2025-05] [[paper](https://arxiv.org/abs/2505.10594)]
13. Code Pretraining [2024-09] [[paper](https://arxiv.org/abs/2409.04556)]
14. StarCoder 2 and The Stack v2 [2024-02] [[paper](https://arxiv.org/abs/2402.19173)]
15. Repetition In Repetition Out [2023-10] [[paper](https://arxiv.org/abs/2310.10226)]
16. Every Sample Matters [2025-03] [[paper](https://arxiv.org/abs/2503.17793)]
17. Code Data Training Stage [2023-09] [[paper](https://arxiv.org/abs/2309.16298)]
18. WaveCoder [2023-12] [[paper](https://arxiv.org/abs/2312.14187)]
19. Brevity is the soul of wit [2024-07] [[paper](https://arxiv.org/abs/2407.00434)]
20. Benchmark Builders [2025-04] [[paper](https://arxiv.org/abs/2504.19444)]
21. CodeMI [2024-04] [[paper](https://arxiv.org/abs/2404.14296)]
22. CodeCipher [2024-10] [[paper](https://arxiv.org/abs/2410.05797)]
23. Code Pre-training Impact [2024-08] [[paper](https://arxiv.org/abs/2408.10914)]
24. DataComp-LM [2024-06] [[paper](https://arxiv.org/abs/2406.11794)]
25. Logical Inference Pre-training [2024-10] [[paper](https://arxiv.org/abs/2410.06735)]
26. Code Llama [2023-08] [[paper](https://arxiv.org/abs/2308.12950)]
27. Codex [2021-07] [[paper](https://arxiv.org/abs/2107.03374)]
28. Path Planning Evaluation [2025-04] [[paper](https://arxiv.org/abs/2504.21276)]
29. Datasets for Large Language Models [2024-02] [[paper](https://arxiv.org/abs/2402.18041)]
30. Synthetic Data Generation [2025-01] [[paper](https://ieeexplore.ieee.org/document/11080380)]
31. Cracks in The Stack [2025-05] [[paper](https://ieeexplore.ieee.org/document/11028470)]
32. Unseen Horizons [2025-04] [[paper](https://ieeexplore.ieee.org/document/11029836)]
33. RTL-Breaker [2025-03] [[paper](https://ieeexplore.ieee.org/document/10993260)]
34. MG-Verilog [2024-06] [[paper](https://ieeexplore.ieee.org/document/10691738)]
35. Code Generation Survey [2024-08] [[paper](https://dl.acm.org/doi/10.1145/3747588)]
36. DataRecipe [2024-10] [[paper](https://dl.acm.org/doi/10.1145/3691620.3695593)]
37. Training Data Extraction [2025-08] [[paper](https://dl.acm.org/doi/10.1145/3709018.3736331)]
38. aiXcoder-7B [2025-04] [[paper](https://ieeexplore.ieee.org/document/11121702)]
39. Imperfect Code Generation [2024-05] [[paper](https://ieeexplore.ieee.org/document/10554837)]
40. LLM-ProS [2025-05] [[paper](https://ieeexplore.ieee.org/document/11028406)]
41. Uncovering Pretraining Code in LLMs [2025-11] [[paper](https://arxiv.org/abs/2511.07033)]
42. APIKG4SYN [2025-11] [[paper](https://arxiv.org/abs/2512.00380)]
43. MultiCodeIF [2025-07] [[paper](https://arxiv.org/abs/2507.00699)]
44. RustEvo^ 2 [2025-03] [[paper](https://arxiv.org/abs/2503.16922)]
45. AATK Benchmark [2021-08] [[paper](https://dl.acm.org/doi/10.1145/3610721)]
