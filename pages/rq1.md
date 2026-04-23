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

<div class="img-container">
  <img src="{{ site.baseurl }}/images/generated_code_issues.png" alt="Taxonomy of Generated Code Quality Issues" width="100%">
  <p><em>Fig. 3. Taxonomy of Generated Code Quality Issues</em></p>
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
    <span class="paper-title">Copilot Security</span>
    <div class="paper-meta">
      <span class="paper-year">2022-04</span>
      <a class="paper-link" href="https://arxiv.org/abs/2204.04741" target="_blank">📄 View Paper</a>
    </div>
  </div>
  <div class="paper-card">
    <span class="paper-title">Copilot Evaluation</span>
    <div class="paper-meta">
      <span class="paper-year">2025-01</span>
      <a class="paper-link" href="https://doi.org/10.1145/3524842.3528470" target="_blank">📄 View Paper</a>
    </div>
  </div>
  <div class="paper-card">
    <span class="paper-title">HalluCode</span>
    <div class="paper-meta">
      <span class="paper-year">2024-04</span>
      <a class="paper-link" href="https://arxiv.org/abs/2404.00971" target="_blank">📄 View Paper</a>
    </div>
  </div>
  <div class="paper-card">
    <span class="paper-title">CodeHalu</span>
    <div class="paper-meta">
      <span class="paper-year">2024-05</span>
      <a class="paper-link" href="https://arxiv.org/abs/2405.00253" target="_blank">📄 View Paper</a>
    </div>
  </div>
  <div class="paper-card">
    <span class="paper-title">EffiBench</span>
    <div class="paper-meta">
      <span class="paper-year">2024-02</span>
      <a class="paper-link" href="https://arxiv.org/abs/2402.02037" target="_blank">📄 View Paper</a>
    </div>
  </div>
  <div class="paper-card">
    <span class="paper-title">Mercury</span>
    <div class="paper-meta">
      <span class="paper-year">2024-02</span>
      <a class="paper-link" href="https://arxiv.org/abs/2402.07844" target="_blank">📄 View Paper</a>
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
    <span class="paper-title">HallTrigger</span>
    <div class="paper-meta">
      <span class="paper-year">2024-07</span>
      <a class="paper-link" href="https://arxiv.org/abs/2407.04831" target="_blank">📄 View Paper</a>
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
    <span class="paper-title">Purple Llama CYBERSECEVAL</span>
    <div class="paper-meta">
      <span class="paper-year">2023-12</span>
      <a class="paper-link" href="https://arxiv.org/abs/2312.04724" target="_blank">📄 View Paper</a>
    </div>
  </div>
  <div class="paper-card">
    <span class="paper-title">Lost at C</span>
    <div class="paper-meta">
      <span class="paper-year">2022-08</span>
      <a class="paper-link" href="https://arxiv.org/abs/2208.09727" target="_blank">📄 View Paper</a>
    </div>
  </div>
  <div class="paper-card">
    <span class="paper-title">AI Assistants Security</span>
    <div class="paper-meta">
      <span class="paper-year">2022-11</span>
      <a class="paper-link" href="https://arxiv.org/abs/2211.03622" target="_blank">📄 View Paper</a>
    </div>
  </div>
  <div class="paper-card">
    <span class="paper-title">The Counterfeit Conundrum</span>
    <div class="paper-meta">
      <span class="paper-year">2024-02</span>
      <a class="paper-link" href="https://arxiv.org/abs/2402.19475" target="_blank">📄 View Paper</a>
    </div>
  </div>
  <div class="paper-card">
    <span class="paper-title">Bugs in LLM-generated Code</span>
    <div class="paper-meta">
      <span class="paper-year">2024-03</span>
      <a class="paper-link" href="https://arxiv.org/abs/2403.08937" target="_blank">📄 View Paper</a>
    </div>
  </div>
  <div class="paper-card">
    <span class="paper-title">GitHub Copilot, Amazon CodeWhisperer, ChatGPT</span>
    <div class="paper-meta">
      <span class="paper-year">2023-04</span>
      <a class="paper-link" href="https://arxiv.org/abs/2304.10778" target="_blank">📄 View Paper</a>
    </div>
  </div>
  <div class="paper-card">
    <span class="paper-title">ChatGPT Code Quality</span>
    <div class="paper-meta">
      <span class="paper-year">2023-08</span>
      <a class="paper-link" href="https://arxiv.org/abs/2308.04838" target="_blank">📄 View Paper</a>
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
    <span class="paper-title">CodeMirage</span>
    <div class="paper-meta">
      <span class="paper-year">2024-08</span>
      <a class="paper-link" href="https://arxiv.org/abs/2408.08333" target="_blank">📄 View Paper</a>
    </div>
  </div>
  <div class="paper-card">
    <span class="paper-title">LLM-generated Code Efficiency</span>
    <div class="paper-meta">
      <span class="paper-year">2024-04</span>
      <a class="paper-link" href="https://arxiv.org/abs/2404.06041" target="_blank">📄 View Paper</a>
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
    <span class="paper-title">DeSec</span>
    <div class="paper-meta">
      <span class="paper-year">2024-10</span>
      <a class="paper-link" href="https://arxiv.org/abs/2410.08858" target="_blank">📄 View Paper</a>
    </div>
  </div>
  <div class="paper-card">
    <span class="paper-title">When Fine-Tuning LLMs Meets Data Privacy</span>
    <div class="paper-meta">
      <span class="paper-year">2024-12</span>
      <a class="paper-link" href="https://arxiv.org/abs/2412.01072" target="_blank">📄 View Paper</a>
    </div>
  </div>
  <div class="paper-card">
    <span class="paper-title">Bias Unveiled</span>
    <div class="paper-meta">
      <span class="paper-year">2024-11</span>
      <a class="paper-link" href="https://arxiv.org/abs/2411.10351" target="_blank">📄 View Paper</a>
    </div>
  </div>
  <div class="paper-card">
    <span class="paper-title">FairCoder</span>
    <div class="paper-meta">
      <span class="paper-year">2025-01</span>
      <a class="paper-link" href="https://arxiv.org/abs/2501.05396" target="_blank">📄 View Paper</a>
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
    <span class="paper-title">From Effectiveness to Efficiency</span>
    <div class="paper-meta">
      <span class="paper-year">2024-06</span>
      <a class="paper-link" href="https://arxiv.org/abs/2406.00602" target="_blank">📄 View Paper</a>
    </div>
  </div>
  <div class="paper-card">
    <span class="paper-title">ENAMEL</span>
    <div class="paper-meta">
      <span class="paper-year">2024-06</span>
      <a class="paper-link" href="https://arxiv.org/abs/2406.06647" target="_blank">📄 View Paper</a>
    </div>
  </div>
  <div class="paper-card">
    <span class="paper-title">DeVAIC</span>
    <div class="paper-meta">
      <span class="paper-year">2024-04</span>
      <a class="paper-link" href="https://arxiv.org/abs/2404.07548" target="_blank">📄 View Paper</a>
    </div>
  </div>
  <div class="paper-card">
    <span class="paper-title">PTMs</span>
    <div class="paper-meta">
      <span class="paper-year">2024-11</span>
      <a class="paper-link" href="https://arxiv.org/abs/2411.10565" target="_blank">📄 View Paper</a>
    </div>
  </div>
  <div class="paper-card">
    <span class="paper-title">Software Librarian</span>
    <div class="paper-meta">
      <span class="paper-year">2024-08</span>
      <a class="paper-link" href="https://arxiv.org/abs/2408.05128" target="_blank">📄 View Paper</a>
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
    <span class="paper-title">Artificial-Intelligence Generated Code Considered Harmful</span>
    <div class="paper-meta">
      <span class="paper-year">2024-09</span>
      <a class="paper-link" href="https://arxiv.org/abs/2409.19182" target="_blank">📄 View Paper</a>
    </div>
  </div>
  <div class="paper-card">
    <span class="paper-title">Unveiling Inefficiencies in LLM-Generated Code</span>
    <div class="paper-meta">
      <span class="paper-year">2025-03</span>
      <a class="paper-link" href="https://arxiv.org/abs/2503.06327" target="_blank">📄 View Paper</a>
    </div>
  </div>
  <div class="paper-card">
    <span class="paper-title">Python Tests Quality</span>
    <div class="paper-meta">
      <span class="paper-year">2025-06</span>
      <a class="paper-link" href="https://arxiv.org/abs/2506.14297" target="_blank">📄 View Paper</a>
    </div>
  </div>
  <div class="paper-card">
    <span class="paper-title">CoQuIR</span>
    <div class="paper-meta">
      <span class="paper-year">2025-06</span>
      <a class="paper-link" href="https://arxiv.org/abs/2506.11066" target="_blank">📄 View Paper</a>
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
    <span class="paper-title">Security and Quality in LLM-Generated Code</span>
    <div class="paper-meta">
      <span class="paper-year">2025-02</span>
      <a class="paper-link" href="https://arxiv.org/abs/2502.01853" target="_blank">📄 View Paper</a>
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
    <span class="paper-title">ROSE</span>
    <div class="paper-meta">
      <span class="paper-year">2025-07</span>
      <a class="paper-link" href="https://arxiv.org/abs/2507.12561" target="_blank">📄 View Paper</a>
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
    <span class="paper-title">Beyond Correctness</span>
    <div class="paper-meta">
      <span class="paper-year">2024-07</span>
      <a class="paper-link" href="https://arxiv.org/abs/2407.11470" target="_blank">📄 View Paper</a>
    </div>
  </div>
  <div class="paper-card">
    <span class="paper-title">Generated Code Diversity</span>
    <div class="paper-meta">
      <span class="paper-year">2024-08</span>
      <a class="paper-link" href="https://arxiv.org/abs/2408.14504" target="_blank">📄 View Paper</a>
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
    <span class="paper-title">Unseen Horizons</span>
    <div class="paper-meta">
      <span class="paper-year">2025-04</span>
      <a class="paper-link" href="https://ieeexplore.ieee.org/document/11029836" target="_blank">📄 View Paper</a>
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
    <span class="paper-title">ClassEval</span>
    <div class="paper-meta">
      <span class="paper-year">2024-6</span>
      <a class="paper-link" href="https://ieeexplore.ieee.org/document/10549472" target="_blank">📄 View Paper</a>
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
    <span class="paper-title">DRAINCODE</span>
    <div class="paper-meta">
      <span class="paper-year">2026-01</span>
      <a class="paper-link" href="https://arxiv.org/abs/2601.20615" target="_blank">📄 View Paper</a>
    </div>
  </div>
  <div class="paper-card">
    <span class="paper-title">RealSec-Bench</span>
    <div class="paper-meta">
      <span class="paper-year">2026-01</span>
      <a class="paper-link" href="https://arxiv.org/abs/2601.22706" target="_blank">📄 View Paper</a>
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
  <div class="paper-card">
    <span class="paper-title">AATK Benchmark</span>
    <div class="paper-meta">
      <span class="paper-year">2021-08</span>
      <a class="paper-link" href="https://dl.acm.org/doi/10.1145/3610721" target="_blank">📄 View Paper</a>
    </div>
  </div>
</div>
