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

<div class="img-container">
  <img src="{{ site.baseurl }}/images/sankey.png" alt="Sankey Diagram of Mapping from Data Issues to Code Issues" width="100%">
  <p><em>Fig. 5. Mapping mechanisms from Training Data Issues to Generated Code Issues.</em></p>
</div>

## 📄 Papers Referenced

<div class="paper-list">
  <div class="paper-card">
    <span class="paper-title">LLMs Meet Library Evolution</span>
    <div class="paper-meta">
      <span class="paper-year">2024-06</span>
      <a class="paper-link" href="https://arxiv.org/abs/2406.09834" target="_blank">📄 View Paper</a>
    </div>
  </div>
  <div class="paper-card">
    <span class="paper-title">SStuBs</span>
    <div class="paper-meta">
      <span class="paper-year">2023-03</span>
      <a class="paper-link" href="https://arxiv.org/abs/2303.11455" target="_blank">📄 View Paper</a>
    </div>
  </div>
  <div class="paper-card">
    <span class="paper-title">AutoAPIEval</span>
    <div class="paper-meta">
      <span class="paper-year">2024-09</span>
      <a class="paper-link" href="https://arxiv.org/abs/2409.15228" target="_blank">📄 View Paper</a>
    </div>
  </div>
  <div class="paper-card">
    <span class="paper-title">CodeIP</span>
    <div class="paper-meta">
      <span class="paper-year">2024-04</span>
      <a class="paper-link" href="https://arxiv.org/abs/2404.15639" target="_blank">📄 View Paper</a>
    </div>
  </div>
  <div class="paper-card">
    <span class="paper-title">CIDRe</span>
    <div class="paper-meta">
      <span class="paper-year">2025-05</span>
      <a class="paper-link" href="https://arxiv.org/abs/2505.19757" target="_blank">📄 View Paper</a>
    </div>
  </div>
  <div class="paper-card">
    <span class="paper-title">Infinite-Instruct</span>
    <div class="paper-meta">
      <span class="paper-year">2025-05</span>
      <a class="paper-link" href="https://arxiv.org/abs/2505.23177" target="_blank">📄 View Paper</a>
    </div>
  </div>
  <div class="paper-card">
    <span class="paper-title">Quality In, Quality Out</span>
    <div class="paper-meta">
      <span class="paper-year">2025-03</span>
      <a class="paper-link" href="https://arxiv.org/abs/2503.11402" target="_blank">📄 View Paper</a>
    </div>
  </div>
  <div class="paper-card">
    <span class="paper-title">SwallowCode</span>
    <div class="paper-meta">
      <span class="paper-year">2025-05</span>
      <a class="paper-link" href="https://arxiv.org/abs/2505.02881" target="_blank">📄 View Paper</a>
    </div>
  </div>
  <div class="paper-card">
    <span class="paper-title">Refining ChatGPT-Generated Code</span>
    <div class="paper-meta">
      <span class="paper-year">2023-07</span>
      <a class="paper-link" href="https://arxiv.org/abs/2307.12596" target="_blank">📄 View Paper</a>
    </div>
  </div>
  <div class="paper-card">
    <span class="paper-title">CRPE</span>
    <div class="paper-meta">
      <span class="paper-year">2025-05</span>
      <a class="paper-link" href="https://arxiv.org/abs/2505.10594" target="_blank">📄 View Paper</a>
    </div>
  </div>
  <div class="paper-card">
    <span class="paper-title">StarCoder 2 and The Stack v2</span>
    <div class="paper-meta">
      <span class="paper-year">2024-02</span>
      <a class="paper-link" href="https://arxiv.org/abs/2402.19173" target="_blank">📄 View Paper</a>
    </div>
  </div>
  <div class="paper-card">
    <span class="paper-title">CodeSmellEval</span>
    <div class="paper-meta">
      <span class="paper-year">2024-12</span>
      <a class="paper-link" href="https://arxiv.org/abs/2412.18989" target="_blank">📄 View Paper</a>
    </div>
  </div>
  <div class="paper-card">
    <span class="paper-title">RPG</span>
    <div class="paper-meta">
      <span class="paper-year">2025-05</span>
      <a class="paper-link" href="https://arxiv.org/abs/2505.10402" target="_blank">📄 View Paper</a>
    </div>
  </div>
  <div class="paper-card">
    <span class="paper-title">Repetition In Repetition Out</span>
    <div class="paper-meta">
      <span class="paper-year">2023-10</span>
      <a class="paper-link" href="https://arxiv.org/abs/2310.10226" target="_blank">📄 View Paper</a>
    </div>
  </div>
  <div class="paper-card">
    <span class="paper-title">CodeMI</span>
    <div class="paper-meta">
      <span class="paper-year">2024-04</span>
      <a class="paper-link" href="https://arxiv.org/abs/2404.14296" target="_blank">📄 View Paper</a>
    </div>
  </div>
  <div class="paper-card">
    <span class="paper-title">CodeCipher</span>
    <div class="paper-meta">
      <span class="paper-year">2024-10</span>
      <a class="paper-link" href="https://arxiv.org/abs/2410.05797" target="_blank">📄 View Paper</a>
    </div>
  </div>
  <div class="paper-card">
    <span class="paper-title">DataComp-LM</span>
    <div class="paper-meta">
      <span class="paper-year">2024-06</span>
      <a class="paper-link" href="https://arxiv.org/abs/2406.11794" target="_blank">📄 View Paper</a>
    </div>
  </div>
  <div class="paper-card">
    <span class="paper-title">Code Llama</span>
    <div class="paper-meta">
      <span class="paper-year">2023-08</span>
      <a class="paper-link" href="https://arxiv.org/abs/2308.12950" target="_blank">📄 View Paper</a>
    </div>
  </div>
  <div class="paper-card">
    <span class="paper-title">Path Planning Evaluation</span>
    <div class="paper-meta">
      <span class="paper-year">2025-04</span>
      <a class="paper-link" href="https://arxiv.org/abs/2504.21276" target="_blank">📄 View Paper</a>
    </div>
  </div>
  <div class="paper-card">
    <span class="paper-title">Datasets for Large Language Models</span>
    <div class="paper-meta">
      <span class="paper-year">2024-02</span>
      <a class="paper-link" href="https://arxiv.org/abs/2402.18041" target="_blank">📄 View Paper</a>
    </div>
  </div>
  <div class="paper-card">
    <span class="paper-title">Synthetic Data Generation</span>
    <div class="paper-meta">
      <span class="paper-year">2025-01</span>
      <a class="paper-link" href="https://ieeexplore.ieee.org/document/11080380" target="_blank">📄 View Paper</a>
    </div>
  </div>
  <div class="paper-card">
    <span class="paper-title">Cracks in The Stack</span>
    <div class="paper-meta">
      <span class="paper-year">2025-05</span>
      <a class="paper-link" href="https://ieeexplore.ieee.org/document/11028470" target="_blank">📄 View Paper</a>
    </div>
  </div>
  <div class="paper-card">
    <span class="paper-title">Unseen Horizons</span>
    <div class="paper-meta">
      <span class="paper-year">2025-04</span>
      <a class="paper-link" href="https://ieeexplore.ieee.org/document/11029836" target="_blank">📄 View Paper</a>
    </div>
  </div>
  <div class="paper-card">
    <span class="paper-title">DataRecipe</span>
    <div class="paper-meta">
      <span class="paper-year">2024-10</span>
      <a class="paper-link" href="https://dl.acm.org/doi/10.1145/3691620.3695593" target="_blank">📄 View Paper</a>
    </div>
  </div>
  <div class="paper-card">
    <span class="paper-title">LLM-ProS</span>
    <div class="paper-meta">
      <span class="paper-year">2025-05</span>
      <a class="paper-link" href="https://ieeexplore.ieee.org/document/11028406" target="_blank">📄 View Paper</a>
    </div>
  </div>
</div>
