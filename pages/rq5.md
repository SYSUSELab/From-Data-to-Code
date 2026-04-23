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

<div class="img-container">
  <img src="{{ site.baseurl }}/images/generated_code_issues_detection.png" alt="Taxonomy of Code Issue Mitigation Strategies" width="100%">
  <p><em>Fig. 8. Taxonomy of Code Issue Mitigation Strategies</em></p>
</div>

## 2. Data-Level Mitigation

- **Cleaning & Filtering**: Execution-feedback elimination, static rule sanitization, and LLM-driven semantic cleaning to remove noise and vulnerabilities.
- **Data Balancing**: Stratified resampling across programming languages, domains, and difficulty levels to mitigate representation bias.
- **Data Enhancement**: Using LLMs or formatting tools to refactor, add docstrings, and standardize existing low-quality code.
- **Data Augmentation**: Expanding datasets via high-quality synthetic generation (rule/LLM-based) and integration of curated open-source repositories.

<div class="img-container">
  <img src="{{ site.baseurl }}/images/data_quality_issues_mitigation.png" alt="Taxonomy of Dataset Issue Mitigation Strategies" width="100%">
  <p><em>Fig. 9. Taxonomy of Training Data Issue Mitigation Strategies</em></p>
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
    <span class="paper-title">Less is More</span>
    <div class="paper-meta">
      <span class="paper-year">2025-02</span>
      <a class="paper-link" href="https://arxiv.org/abs/2502.14212" target="_blank">📄 View Paper</a>
    </div>
  </div>
  <div class="paper-card">
    <span class="paper-title">Qwen</span>
    <div class="paper-meta">
      <span class="paper-year">2023-09</span>
      <a class="paper-link" href="https://arxiv.org/abs/2309.16609" target="_blank">📄 View Paper</a>
    </div>
  </div>
  <div class="paper-card">
    <span class="paper-title">Qwen2</span>
    <div class="paper-meta">
      <span class="paper-year">2024-07</span>
      <a class="paper-link" href="https://arxiv.org/abs/2407.10671" target="_blank">📄 View Paper</a>
    </div>
  </div>
  <div class="paper-card">
    <span class="paper-title">DataMan</span>
    <div class="paper-meta">
      <span class="paper-year">2025-02</span>
      <a class="paper-link" href="https://arxiv.org/abs/2502.19363" target="_blank">📄 View Paper</a>
    </div>
  </div>
  <div class="paper-card">
    <span class="paper-title">Phi-4</span>
    <div class="paper-meta">
      <span class="paper-year">2024-12</span>
      <a class="paper-link" href="https://arxiv.org/abs/2412.08905" target="_blank">📄 View Paper</a>
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
    <span class="paper-title">package hallucinations</span>
    <div class="paper-meta">
      <span class="paper-year">2024-06</span>
      <a class="paper-link" href="https://arxiv.org/abs/2406.10279" target="_blank">📄 View Paper</a>
    </div>
  </div>
  <div class="paper-card">
    <span class="paper-title">Large Language Models for Code</span>
    <div class="paper-meta">
      <span class="paper-year">2023-02</span>
      <a class="paper-link" href="https://arxiv.org/abs/2302.05319" target="_blank">📄 View Paper</a>
    </div>
  </div>
  <div class="paper-card">
    <span class="paper-title">CloudAPIBench</span>
    <div class="paper-meta">
      <span class="paper-year">2024-07</span>
      <a class="paper-link" href="https://arxiv.org/abs/2407.09726" target="_blank">📄 View Paper</a>
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
    <span class="paper-title">Codequal Analyzer</span>
    <div class="paper-meta">
      <span class="paper-year">2025-06</span>
      <a class="paper-link" href="https://arxiv.org/abs/2506.02211" target="_blank">📄 View Paper</a>
    </div>
  </div>
  <div class="paper-card">
    <span class="paper-title">REAL</span>
    <div class="paper-meta">
      <span class="paper-year">2025-05</span>
      <a class="paper-link" href="https://arxiv.org/abs/2505.22704" target="_blank">📄 View Paper</a>
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
    <span class="paper-title">Qwen3</span>
    <div class="paper-meta">
      <span class="paper-year">2025-05</span>
      <a class="paper-link" href="https://arxiv.org/abs/2505.09388" target="_blank">📄 View Paper</a>
    </div>
  </div>
  <div class="paper-card">
    <span class="paper-title">Qwen2.5</span>
    <div class="paper-meta">
      <span class="paper-year">2024-12</span>
      <a class="paper-link" href="https://arxiv.org/abs/2412.15115" target="_blank">📄 View Paper</a>
    </div>
  </div>
  <div class="paper-card">
    <span class="paper-title">TeleChat</span>
    <div class="paper-meta">
      <span class="paper-year">2025-07</span>
      <a class="paper-link" href="https://arxiv.org/abs/2507.18013" target="_blank">📄 View Paper</a>
    </div>
  </div>
  <div class="paper-card">
    <span class="paper-title">Kimi K2</span>
    <div class="paper-meta">
      <span class="paper-year">2025-07</span>
      <a class="paper-link" href="https://arxiv.org/abs/2507.20534" target="_blank">📄 View Paper</a>
    </div>
  </div>
  <div class="paper-card">
    <span class="paper-title">ReCode</span>
    <div class="paper-meta">
      <span class="paper-year">2025-06</span>
      <a class="paper-link" href="https://arxiv.org/abs/2506.20495" target="_blank">📄 View Paper</a>
    </div>
  </div>
  <div class="paper-card">
    <span class="paper-title">Seed-Coder</span>
    <div class="paper-meta">
      <span class="paper-year">2025-06</span>
      <a class="paper-link" href="https://arxiv.org/abs/2506.03524" target="_blank">📄 View Paper</a>
    </div>
  </div>
  <div class="paper-card">
    <span class="paper-title">Data-efficient Fine-tuning</span>
    <div class="paper-meta">
      <span class="paper-year">2025-04</span>
      <a class="paper-link" href="https://arxiv.org/abs/2504.12687" target="_blank">📄 View Paper</a>
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
    <span class="paper-title">DeepSeek-Coder</span>
    <div class="paper-meta">
      <span class="paper-year">2024-01</span>
      <a class="paper-link" href="https://arxiv.org/abs/2401.14196" target="_blank">📄 View Paper</a>
    </div>
  </div>
  <div class="paper-card">
    <span class="paper-title">Code Pretraining</span>
    <div class="paper-meta">
      <span class="paper-year">2024-09</span>
      <a class="paper-link" href="https://arxiv.org/abs/2409.04556" target="_blank">📄 View Paper</a>
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
    <span class="paper-title">Brevity is the soul of wit</span>
    <div class="paper-meta">
      <span class="paper-year">2024-07</span>
      <a class="paper-link" href="https://arxiv.org/abs/2407.00434" target="_blank">📄 View Paper</a>
    </div>
  </div>
  <div class="paper-card">
    <span class="paper-title">Benchmark Builders</span>
    <div class="paper-meta">
      <span class="paper-year">2025-04</span>
      <a class="paper-link" href="https://arxiv.org/abs/2504.19444" target="_blank">📄 View Paper</a>
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
    <span class="paper-title">RedStone</span>
    <div class="paper-meta">
      <span class="paper-year">2024-12</span>
      <a class="paper-link" href="https://arxiv.org/abs/2412.03398" target="_blank">📄 View Paper</a>
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
    <span class="paper-title">Codex</span>
    <div class="paper-meta">
      <span class="paper-year">2021-07</span>
      <a class="paper-link" href="https://arxiv.org/abs/2107.03374" target="_blank">📄 View Paper</a>
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
    <span class="paper-title">CODEJUDGE</span>
    <div class="paper-meta">
      <span class="paper-year">2024-01</span>
      <a class="paper-link" href="https://aclanthology.org/2024.emnlp-main.1118.pdf?utm_source=chatgpt.com" target="_blank">📄 View Paper</a>
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
    <span class="paper-title">MG-Verilog</span>
    <div class="paper-meta">
      <span class="paper-year">2024-06</span>
      <a class="paper-link" href="https://ieeexplore.ieee.org/document/10691738" target="_blank">📄 View Paper</a>
    </div>
  </div>
  <div class="paper-card">
    <span class="paper-title">Code Generation Survey</span>
    <div class="paper-meta">
      <span class="paper-year">2024-08</span>
      <a class="paper-link" href="https://dl.acm.org/doi/10.1145/3747588" target="_blank">📄 View Paper</a>
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
    <span class="paper-title">aiXcoder-7B</span>
    <div class="paper-meta">
      <span class="paper-year">2025-04</span>
      <a class="paper-link" href="https://ieeexplore.ieee.org/document/11121702" target="_blank">📄 View Paper</a>
    </div>
  </div>
  <div class="paper-card">
    <span class="paper-title">Imperfect Code Generation</span>
    <div class="paper-meta">
      <span class="paper-year">2024-05</span>
      <a class="paper-link" href="https://ieeexplore.ieee.org/document/10554837" target="_blank">📄 View Paper</a>
    </div>
  </div>
  <div class="paper-card">
    <span class="paper-title">Inter-Dataset Code Duplication</span>
    <div class="paper-meta">
      <span class="paper-year">2025-01</span>
      <a class="paper-link" href="https://ieeexplore.ieee.org/document/10759822" target="_blank">📄 View Paper</a>
    </div>
  </div>
  <div class="paper-card">
    <span class="paper-title">LLM-ProS</span>
    <div class="paper-meta">
      <span class="paper-year">2025-05</span>
      <a class="paper-link" href="https://ieeexplore.ieee.org/document/11028406" target="_blank">📄 View Paper</a>
    </div>
  </div>
  <div class="paper-card">
    <span class="paper-title">UCD-Training</span>
    <div class="paper-meta">
      <span class="paper-year">2026-02</span>
      <a class="paper-link" href="https://arxiv.org/abs/2602.20799" target="_blank">📄 View Paper</a>
    </div>
  </div>
  <div class="paper-card">
    <span class="paper-title">ShortCoder</span>
    <div class="paper-meta">
      <span class="paper-year">2026-01</span>
      <a class="paper-link" href="https://arxiv.org/abs/2601.09703" target="_blank">📄 View Paper</a>
    </div>
  </div>
  <div class="paper-card">
    <span class="paper-title">APIKG4SYN</span>
    <div class="paper-meta">
      <span class="paper-year">2025-11</span>
      <a class="paper-link" href="https://arxiv.org/abs/2512.00380" target="_blank">📄 View Paper</a>
    </div>
  </div>
  <div class="paper-card">
    <span class="paper-title">MultiCodeIF</span>
    <div class="paper-meta">
      <span class="paper-year">2025-07</span>
      <a class="paper-link" href="https://arxiv.org/abs/2507.00699" target="_blank">📄 View Paper</a>
    </div>
  </div>
  <div class="paper-card">
    <span class="paper-title">Beyond Functional Correctness</span>
    <div class="paper-meta">
      <span class="paper-year">2024-06</span>
      <a class="paper-link" href="https://arxiv.org/abs/2407.00456" target="_blank">📄 View Paper</a>
    </div>
  </div>
  <div class="paper-card">
    <span class="paper-title">Adadec</span>
    <div class="paper-meta">
      <span class="paper-year">2025-06</span>
      <a class="paper-link" href="https://arxiv.org/html/2506.08980v1" target="_blank">📄 View Paper</a>
    </div>
  </div>
  <div class="paper-card">
    <span class="paper-title">Code Copycat Conundrum</span>
    <div class="paper-meta">
      <span class="paper-year">2025-04</span>
      <a class="paper-link" href="https://arxiv.org/abs/2504.12608" target="_blank">📄 View Paper</a>
    </div>
  </div>
  <div class="paper-card">
    <span class="paper-title">AllianceCoder</span>
    <div class="paper-meta">
      <span class="paper-year">2025-03</span>
      <a class="paper-link" href="https://arxiv.org/abs/2503.20589" target="_blank">📄 View Paper</a>
    </div>
  </div>
  <div class="paper-card">
    <span class="paper-title">RustEvo^ 2</span>
    <div class="paper-meta">
      <span class="paper-year">2025-03</span>
      <a class="paper-link" href="https://arxiv.org/abs/2503.16922" target="_blank">📄 View Paper</a>
    </div>
  </div>
  <div class="paper-card">
    <span class="paper-title">RobGen</span>
    <div class="paper-meta">
      <span class="paper-year">2025-03</span>
      <a class="paper-link" href="https://arxiv.org/abs/2503.20197" target="_blank">📄 View Paper</a>
    </div>
  </div>
  <div class="paper-card">
    <span class="paper-title">Llm Hallucinations in Practical Code Generation</span>
    <div class="paper-meta">
      <span class="paper-year">2024-09</span>
      <a class="paper-link" href="https://arxiv.org/abs/2409.20550" target="_blank">📄 View Paper</a>
    </div>
  </div>
  <div class="paper-card">
    <span class="paper-title">COFFE</span>
    <div class="paper-meta">
      <span class="paper-year">2025-02</span>
      <a class="paper-link" href="https://arxiv.org/abs/2502.02827" target="_blank">📄 View Paper</a>
    </div>
  </div>
</div>
