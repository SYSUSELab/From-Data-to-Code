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

<div class="img-container">
  <img src="{{ site.baseurl }}/images/generated_code_issues_detection.png" alt="Taxonomy of Code Issue Detection Methods" width="100%">
  <p><em>Fig. 6. Taxonomy of Code Issue Detection Techniques</em></p>
</div>

## 2. Data-Level Detection

Targets the integrity, provenance, and representativeness of the underlying training data:

- **Dynamic Analysis**: Execution-based validation (checking if scraped code compiles) and metric drift monitoring (detecting data leakage or contamination through training loss curves).
- **Static Analysis**: Rule-based detection, human review, and provenance tracing (using file hashes to identify duplicate or benchmark-contaminated data).
- **Model-based Detection**: High-throughput semantic screening using LLMs or lightweight classifiers to evaluate sample readability, information entropy, and potential hazards.

<div class="img-container">
  <img src="{{ site.baseurl }}/images/data_quality_issues_detection.png" alt="Taxonomy of Dataset Issue Detection Methods" width="100%">
  <p><em>Fig. 7. Taxonomy of Training Data Issue Detection Techniques</em></p>
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
    <span class="paper-title">Syntactic Robustness</span>
    <div class="paper-meta">
      <span class="paper-year">2024-04</span>
      <a class="paper-link" href="https://arxiv.org/abs/2404.01535" target="_blank">📄 View Paper</a>
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
    <span class="paper-title">Every Sample Matters</span>
    <div class="paper-meta">
      <span class="paper-year">2025-03</span>
      <a class="paper-link" href="https://arxiv.org/abs/2503.17793" target="_blank">📄 View Paper</a>
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
    <span class="paper-title">DataComp-LM</span>
    <div class="paper-meta">
      <span class="paper-year">2024-06</span>
      <a class="paper-link" href="https://arxiv.org/abs/2406.11794" target="_blank">📄 View Paper</a>
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
    <span class="paper-title">ClassEval</span>
    <div class="paper-meta">
      <span class="paper-year">2024-6</span>
      <a class="paper-link" href="https://ieeexplore.ieee.org/document/10549472" target="_blank">📄 View Paper</a>
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
