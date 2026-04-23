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

<div class="img-container">
  <img src="{{ site.baseurl }}/images/data_quality_issues.png" alt="Taxonomy of Dataset Quality Issues" width="100%">
  <p><em>Fig. 4. Taxonomy of Training Data Quality Issues</em></p>
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
    <span class="paper-title">DeSec</span>
    <div class="paper-meta">
      <span class="paper-year">2024-10</span>
      <a class="paper-link" href="https://arxiv.org/abs/2410.08858" target="_blank">📄 View Paper</a>
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
    <span class="paper-title">Seed-Coder</span>
    <div class="paper-meta">
      <span class="paper-year">2025-06</span>
      <a class="paper-link" href="https://arxiv.org/abs/2506.03524" target="_blank">📄 View Paper</a>
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
    <span class="paper-title">Repetition In Repetition Out</span>
    <div class="paper-meta">
      <span class="paper-year">2023-10</span>
      <a class="paper-link" href="https://arxiv.org/abs/2310.10226" target="_blank">📄 View Paper</a>
    </div>
  </div>
  <div class="paper-card">
    <span class="paper-title">Every Sample Matters</span>
    <div class="paper-meta">
      <span class="paper-year">2025-03</span>
      <a class="paper-link" href="https://arxiv.org/abs/2503.17793" target="_blank">📄 View Paper</a>
    </div>
  </div>
  <div class="paper-card">
    <span class="paper-title">Code Data Training Stage</span>
    <div class="paper-meta">
      <span class="paper-year">2023-09</span>
      <a class="paper-link" href="https://arxiv.org/abs/2309.16298" target="_blank">📄 View Paper</a>
    </div>
  </div>
  <div class="paper-card">
    <span class="paper-title">WaveCoder</span>
    <div class="paper-meta">
      <span class="paper-year">2023-12</span>
      <a class="paper-link" href="https://arxiv.org/abs/2312.14187" target="_blank">📄 View Paper</a>
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
    <span class="paper-title">Code Pre-training Impact</span>
    <div class="paper-meta">
      <span class="paper-year">2024-08</span>
      <a class="paper-link" href="https://arxiv.org/abs/2408.10914" target="_blank">📄 View Paper</a>
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
    <span class="paper-title">Logical Inference Pre-training</span>
    <div class="paper-meta">
      <span class="paper-year">2024-10</span>
      <a class="paper-link" href="https://arxiv.org/abs/2410.06735" target="_blank">📄 View Paper</a>
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
    <span class="paper-title">RTL-Breaker</span>
    <div class="paper-meta">
      <span class="paper-year">2025-03</span>
      <a class="paper-link" href="https://ieeexplore.ieee.org/document/10993260" target="_blank">📄 View Paper</a>
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
    <span class="paper-title">Training Data Extraction</span>
    <div class="paper-meta">
      <span class="paper-year">2025-08</span>
      <a class="paper-link" href="https://dl.acm.org/doi/10.1145/3709018.3736331" target="_blank">📄 View Paper</a>
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
    <span class="paper-title">LLM-ProS</span>
    <div class="paper-meta">
      <span class="paper-year">2025-05</span>
      <a class="paper-link" href="https://ieeexplore.ieee.org/document/11028406" target="_blank">📄 View Paper</a>
    </div>
  </div>
  <div class="paper-card">
    <span class="paper-title">Uncovering Pretraining Code in LLMs</span>
    <div class="paper-meta">
      <span class="paper-year">2025-11</span>
      <a class="paper-link" href="https://arxiv.org/abs/2511.07033" target="_blank">📄 View Paper</a>
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
    <span class="paper-title">RustEvo^ 2</span>
    <div class="paper-meta">
      <span class="paper-year">2025-03</span>
      <a class="paper-link" href="https://arxiv.org/abs/2503.16922" target="_blank">📄 View Paper</a>
    </div>
  </div>
  <div class="paper-card">
    <span class="paper-title">AATK Benchmark</span>
    <div class="paper-meta">
      <span class="paper-year">2021-08</span>
      <a class="paper-link" href="https://dl.acm.org/doi/10.1145/3610721" target="_blank">📄 View Paper</a>
    </div>
  </div>
</div>
