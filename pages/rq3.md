---
layout: default
title: "RQ3: Mapping mechanisms"
parent: Home
nav_order: 4
---

# 🔗 RQ3: Mapping: Data to Code

How do data defects cause code generation failures? We summarize **18 propagation mechanisms** bridging the gap between dataset flaws and generated code defects:

1. **Direct Mappings (10 types)**: The classic "garbage in, garbage out" replication. The model explicitly memorizes dataset flaws and replicates them.
2. **Indirect Mappings (8 types)**: Insidious propagation. Non-code defects do not inject explicit errors but disrupt the model's internal representations via mechanisms such as _entropy collapse_, _representation bias_, or _semantic drift_.

<div align="center">
  <img src="{{ site.baseurl }}/images/sankey.png" alt="Sankey Diagram of Mapping from Data Issues to Code Issues" width="100%">
  <p><em>Fig. 5. Mapping mechanisms from Training Data Issues to Generated Code Issues.</em></p>
</div>

## 📄 Papers Referenced

1. LLMs Meet Library Evolution [2024-06] [[paper](https://arxiv.org/abs/2406.09834)]
2. SStuBs [2023-03] [[paper](https://arxiv.org/abs/2303.11455)]
3. AutoAPIEval [2024-09] [[paper](https://arxiv.org/abs/2409.15228)]
4. CodeIP [2024-04] [[paper](https://arxiv.org/abs/2404.15639)]
5. CIDRe [2025-05] [[paper](https://arxiv.org/abs/2505.19757)]
6. Infinite-Instruct [2025-05] [[paper](https://arxiv.org/abs/2505.23177)]
7. Quality In, Quality Out [2025-03] [[paper](https://arxiv.org/abs/2503.11402)]
8. SwallowCode [2025-05] [[paper](https://arxiv.org/abs/2505.02881)]
9. Refining ChatGPT-Generated Code [2023-07] [[paper](https://arxiv.org/abs/2307.12596)]
10. CRPE [2025-05] [[paper](https://arxiv.org/abs/2505.10594)]
11. StarCoder 2 and The Stack v2 [2024-02] [[paper](https://arxiv.org/abs/2402.19173)]
12. CodeSmellEval [2024-12] [[paper](https://arxiv.org/abs/2412.18989)]
13. RPG [2025-05] [[paper](https://arxiv.org/abs/2505.10402)]
14. Repetition In Repetition Out [2023-10] [[paper](https://arxiv.org/abs/2310.10226)]
15. CodeMI [2024-04] [[paper](https://arxiv.org/abs/2404.14296)]
16. CodeCipher [2024-10] [[paper](https://arxiv.org/abs/2410.05797)]
17. DataComp-LM [2024-06] [[paper](https://arxiv.org/abs/2406.11794)]
18. Code Llama [2023-08] [[paper](https://arxiv.org/abs/2308.12950)]
19. Path Planning Evaluation [2025-04] [[paper](https://arxiv.org/abs/2504.21276)]
20. Datasets for Large Language Models [2024-02] [[paper](https://arxiv.org/abs/2402.18041)]
21. Synthetic Data Generation [2025-01] [[paper](https://ieeexplore.ieee.org/document/11080380)]
22. Cracks in The Stack [2025-05] [[paper](https://ieeexplore.ieee.org/document/11028470)]
23. Unseen Horizons [2025-04] [[paper](https://ieeexplore.ieee.org/document/11029836)]
24. DataRecipe [2024-10] [[paper](https://dl.acm.org/doi/10.1145/3691620.3695593)]
25. LLM-ProS [2025-05] [[paper](https://ieeexplore.ieee.org/document/11028406)]
