---
layout: default
title: Detection Methods
description: "Detection methods for quality issues in LLM-generated code and training data, including static analysis, dynamic analysis, model-based detection, and data-level quality assessment."
nav_order: 4
---

# 🔍 RQ4: Detection Methods

Detection techniques are evolving from rigid static analysis to dynamic, model-driven, and hybrid evaluation frameworks. They form the diagnostic foundation of LLM quality governance.

---

## 💻 1. Code-Level Detection

Identifies defects in generated code using three main paradigms:

- **Dynamic Analysis**: Test-based execution and runtime monitoring to assess accuracy and efficiency.
- **Static Analysis**: Rule-based detection (SonarQube, Semgrep) for syntax errors and vulnerabilities.
- **Model-based Detection**: "LLM-as-a-judge" techniques and ML classifiers for semantic filtering.

<div class="figure-block">
  <div class="figure-frame">
    <img src="{{ '/images/generated_code_issues_detection.png' | relative_url }}" alt="Taxonomy of Code Issue Detection Methods" width="1100" loading="lazy" decoding="async">
  </div>
  <p class="figure-caption"><em>Fig. 6. Taxonomy of Code Issue Detection Techniques</em></p>
</div>

---

## 📊 2. Data-Level Detection

Targets the integrity, provenance, and representativeness of training data:

- **Dynamic Analysis**: Execution-based validation and metric drift monitoring (detecting data leakage).
- **Static Analysis**: Rule-based detection and provenance tracing using file hashes.
- **Model-based Detection**: Semantic screening using LLMs to evaluate readability and hazards.

<div class="figure-block">
  <div class="figure-frame">
    <img src="{{ '/images/data_quality_issues_detection.png' | relative_url }}" alt="Taxonomy of Dataset Issue Detection Methods" width="1100" loading="lazy" decoding="async">
  </div>
  <p class="figure-caption"><em>Fig. 7. Taxonomy of Training Data Issue Detection Techniques</em></p>
</div>




---

## 📄 Referenced Papers

<div class="paper-card">
    <div class="paper-title">LLMs Meet Library Evolution</div>
    <div class="paper-subtitle">LLMs Meet Library Evolution: Evaluating Deprecated API Usage in LLM-based Code Completion</div>
    <div class="paper-meta">
        <span class="paper-tag">2024-06</span>
        <a href="https://arxiv.org/abs/2406.09834" class="paper-link" target="_blank">View Paper ↗</a>
    </div>
</div>

<div class="paper-card">
    <div class="paper-title">Less is More</div>
    <div class="paper-subtitle">Less is More: On the Importance of Data Quality for Unit Test Generation</div>
    <div class="paper-meta">
        <span class="paper-tag">2025-02</span>
        <a href="https://arxiv.org/abs/2502.14212" class="paper-link" target="_blank">View Paper ↗</a>
    </div>
</div>

<div class="paper-card">
    <div class="paper-title">Qwen</div>
    <div class="paper-subtitle">Qwen Technical Report</div>
    <div class="paper-meta">
        <span class="paper-tag">2023-09</span>
        <a href="https://arxiv.org/abs/2309.16609" class="paper-link" target="_blank">View Paper ↗</a>
    </div>
</div>

<div class="paper-card">
    <div class="paper-title">Qwen2</div>
    <div class="paper-subtitle">Qwen2 Technical Report</div>
    <div class="paper-meta">
        <span class="paper-tag">2024-07</span>
        <a href="https://arxiv.org/abs/2407.10671" class="paper-link" target="_blank">View Paper ↗</a>
    </div>
</div>

<div class="paper-card">
    <div class="paper-title">DataMan</div>
    <div class="paper-subtitle">DataMan: Data Manager for Pre-training Large Language Models</div>
    <div class="paper-meta">
        <span class="paper-tag">2025-02</span>
        <a href="https://arxiv.org/abs/2502.19363" class="paper-link" target="_blank">View Paper ↗</a>
    </div>
</div>

<div class="paper-card">
    <div class="paper-title">Phi-4</div>
    <div class="paper-subtitle">Phi-4 Technical Report</div>
    <div class="paper-meta">
        <span class="paper-tag">2024-12</span>
        <a href="https://arxiv.org/abs/2412.08905" class="paper-link" target="_blank">View Paper ↗</a>
    </div>
</div>

<div class="paper-card">
    <div class="paper-title">Copilot Security</div>
    <div class="paper-subtitle">Is GitHub’s Copilot as Bad as Humans at Introducing Vulnerabilities in Code?</div>
    <div class="paper-meta">
        <span class="paper-tag">2022-04</span>
        <a href="https://arxiv.org/abs/2204.04741" class="paper-link" target="_blank">View Paper ↗</a>
    </div>
</div>

<div class="paper-card">
    <div class="paper-title">Copilot Evaluation</div>
    <div class="paper-subtitle">An Empirical Evaluation of GitHub Copilot’s Code Suggestions</div>
    <div class="paper-meta">
        <span class="paper-tag">2025-01</span>
        <a href="https://doi.org/10.1145/3524842.3528470" class="paper-link" target="_blank">View Paper ↗</a>
    </div>
</div>

<div class="paper-card">
    <div class="paper-title">HalluCode</div>
    <div class="paper-subtitle">Exploring and Evaluating Hallucinations in LLM-Powered Code Generation</div>
    <div class="paper-meta">
        <span class="paper-tag">2024-04</span>
        <a href="https://arxiv.org/abs/2404.00971" class="paper-link" target="_blank">View Paper ↗</a>
    </div>
</div>

<div class="paper-card">
    <div class="paper-title">CodeHalu</div>
    <div class="paper-subtitle">CodeHalu: Investigating Code Hallucinations in LLMs via Execution-based Verification</div>
    <div class="paper-meta">
        <span class="paper-tag">2024-05</span>
        <a href="https://arxiv.org/abs/2405.00253" class="paper-link" target="_blank">View Paper ↗</a>
    </div>
</div>

<div class="paper-card">
    <div class="paper-title">EffiBench</div>
    <div class="paper-subtitle">EffiBench: Benchmarking the Efficiency of Automatically Generated Code</div>
    <div class="paper-meta">
        <span class="paper-tag">2024-02</span>
        <a href="https://arxiv.org/abs/2402.02037" class="paper-link" target="_blank">View Paper ↗</a>
    </div>
</div>

<div class="paper-card">
    <div class="paper-title">Mercury</div>
    <div class="paper-subtitle">Mercury: A Code Efficiency Benchmark for Code Large Language Models</div>
    <div class="paper-meta">
        <span class="paper-tag">2024-02</span>
        <a href="https://arxiv.org/abs/2402.07844" class="paper-link" target="_blank">View Paper ↗</a>
    </div>
</div>

<div class="paper-card">
    <div class="paper-title">SStuBs</div>
    <div class="paper-subtitle">Large Language Models and Simple, Stupid Bugs</div>
    <div class="paper-meta">
        <span class="paper-tag">2023-03</span>
        <a href="https://arxiv.org/abs/2303.11455" class="paper-link" target="_blank">View Paper ↗</a>
    </div>
</div>

<div class="paper-card">
    <div class="paper-title">package hallucinations</div>
    <div class="paper-subtitle">We Have a Package for You! A Comprehensive Analysis of Package Hallucinations by Code Generating LLMs</div>
    <div class="paper-meta">
        <span class="paper-tag">2024-06</span>
        <a href="https://arxiv.org/abs/2406.10279" class="paper-link" target="_blank">View Paper ↗</a>
    </div>
</div>

<div class="paper-card">
    <div class="paper-title">HallTrigger</div>
    <div class="paper-subtitle">Code Hallucination</div>
    <div class="paper-meta">
        <span class="paper-tag">2024-07</span>
        <a href="https://arxiv.org/abs/2407.04831" class="paper-link" target="_blank">View Paper ↗</a>
    </div>
</div>

<div class="paper-card">
    <div class="paper-title">Large Language Models for Code</div>
    <div class="paper-subtitle">Large Language Models for Code: Security Hardening and Adversarial Testing</div>
    <div class="paper-meta">
        <span class="paper-tag">2023-02</span>
        <a href="https://arxiv.org/abs/2302.05319" class="paper-link" target="_blank">View Paper ↗</a>
    </div>
</div>

<div class="paper-card">
    <div class="paper-title">Purple Llama CYBERSECEVAL</div>
    <div class="paper-subtitle">Purple Llama CYBERSECEVAL: A Secure Coding Benchmark for Language Models</div>
    <div class="paper-meta">
        <span class="paper-tag">2023-12</span>
        <a href="https://arxiv.org/abs/2312.04724" class="paper-link" target="_blank">View Paper ↗</a>
    </div>
</div>

<div class="paper-card">
    <div class="paper-title">Lost at C</div>
    <div class="paper-subtitle">Lost at C: A User Study on the Security Implications of Large Language Model Code Assistants</div>
    <div class="paper-meta">
        <span class="paper-tag">2022-08</span>
        <a href="https://arxiv.org/abs/2208.09727" class="paper-link" target="_blank">View Paper ↗</a>
    </div>
</div>

<div class="paper-card">
    <div class="paper-title">AI Assistants Security</div>
    <div class="paper-subtitle">Do Users Write More Insecure Code with AI Assistants?</div>
    <div class="paper-meta">
        <span class="paper-tag">2022-11</span>
        <a href="https://arxiv.org/abs/2211.03622" class="paper-link" target="_blank">View Paper ↗</a>
    </div>
</div>

<div class="paper-card">
    <div class="paper-title">The Counterfeit Conundrum</div>
    <div class="paper-subtitle">The Counterfeit Conundrum: Can Code Language Models Grasp the Nuances of Their Incorrect Generations?</div>
    <div class="paper-meta">
        <span class="paper-tag">2024-02</span>
        <a href="https://arxiv.org/abs/2402.19475" class="paper-link" target="_blank">View Paper ↗</a>
    </div>
</div>

<div class="paper-card">
    <div class="paper-title">Bugs in LLM-generated Code</div>
    <div class="paper-subtitle">Bugs in Large Language Models Generated Code: An Empirical Stud</div>
    <div class="paper-meta">
        <span class="paper-tag">2024-03</span>
        <a href="https://arxiv.org/abs/2403.08937" class="paper-link" target="_blank">View Paper ↗</a>
    </div>
</div>

<div class="paper-card">
    <div class="paper-title">GitHub Copilot, Amazon CodeWhisperer, ChatGPT</div>
    <div class="paper-subtitle">Evaluating the Code Quality of AI-Assisted Code Generation Tools: An Empirical Study on GitHub Copilot, Amazon CodeWhisperer, and ChatGPT</div>
    <div class="paper-meta">
        <span class="paper-tag">2023-04</span>
        <a href="https://arxiv.org/abs/2304.10778" class="paper-link" target="_blank">View Paper ↗</a>
    </div>
</div>

<div class="paper-card">
    <div class="paper-title">ChatGPT Code Quality</div>
    <div class="paper-subtitle">No Need to Lift a Finger Anymore? Assessing the Quality of Code Generation by ChatGPT</div>
    <div class="paper-meta">
        <span class="paper-tag">2023-08</span>
        <a href="https://arxiv.org/abs/2308.04838" class="paper-link" target="_blank">View Paper ↗</a>
    </div>
</div>

<div class="paper-card">
    <div class="paper-title">CloudAPIBench</div>
    <div class="paper-subtitle">On Mitigating Code LLM Hallucinations with API Documentation</div>
    <div class="paper-meta">
        <span class="paper-tag">2024-07</span>
        <a href="https://arxiv.org/abs/2407.09726" class="paper-link" target="_blank">View Paper ↗</a>
    </div>
</div>

<div class="paper-card">
    <div class="paper-title">CodeMirage</div>
    <div class="paper-subtitle">CodeMirage: Hallucinations in Code Generated by Large Language Models</div>
    <div class="paper-meta">
        <span class="paper-tag">2024-08</span>
        <a href="https://arxiv.org/abs/2408.08333" class="paper-link" target="_blank">View Paper ↗</a>
    </div>
</div>

<div class="paper-card">
    <div class="paper-title">LLM-generated Code Efficiency</div>
    <div class="paper-subtitle">On Evaluating the Efficiency of Source Code Generated by LLMs</div>
    <div class="paper-meta">
        <span class="paper-tag">2024-04</span>
        <a href="https://arxiv.org/abs/2404.06041" class="paper-link" target="_blank">View Paper ↗</a>
    </div>
</div>

<div class="paper-card">
    <div class="paper-title">Syntactic Robustness</div>
    <div class="paper-subtitle">Syntactic Robustness for LLM-based Code Generation</div>
    <div class="paper-meta">
        <span class="paper-tag">2024-04</span>
        <a href="https://arxiv.org/abs/2404.01535" class="paper-link" target="_blank">View Paper ↗</a>
    </div>
</div>

<div class="paper-card">
    <div class="paper-title">DeSec</div>
    <div class="paper-subtitle">Decoding Secret Memorization in Code LLMs Through Token-Level Characterization</div>
    <div class="paper-meta">
        <span class="paper-tag">2024-10</span>
        <a href="https://arxiv.org/abs/2410.08858" class="paper-link" target="_blank">View Paper ↗</a>
    </div>
</div>

<div class="paper-card">
    <div class="paper-title">Bias Unveiled</div>
    <div class="paper-subtitle">Bias Unveiled: Investigating Social Bias in LLM-Generated Code</div>
    <div class="paper-meta">
        <span class="paper-tag">2024-11</span>
        <a href="https://arxiv.org/abs/2411.10351" class="paper-link" target="_blank">View Paper ↗</a>
    </div>
</div>

<div class="paper-card">
    <div class="paper-title">FairCoder</div>
    <div class="paper-subtitle">FairCoder: Evaluating Social Bias of LLMs in Code Generation</div>
    <div class="paper-meta">
        <span class="paper-tag">2025-01</span>
        <a href="https://arxiv.org/abs/2501.05396" class="paper-link" target="_blank">View Paper ↗</a>
    </div>
</div>

<div class="paper-card">
    <div class="paper-title">From Effectiveness to Efficiency</div>
    <div class="paper-subtitle">From Effectiveness to Efficiency: Comparative Evaluation of Code Generated by LCGMs for Bilingual Programming Questions</div>
    <div class="paper-meta">
        <span class="paper-tag">2024-06</span>
        <a href="https://arxiv.org/abs/2406.00602" class="paper-link" target="_blank">View Paper ↗</a>
    </div>
</div>

<div class="paper-card">
    <div class="paper-title">ENAMEL</div>
    <div class="paper-subtitle">How Efficient is LLM-Generated Code? A Rigorous & High-Standard Benchmark</div>
    <div class="paper-meta">
        <span class="paper-tag">2024-06</span>
        <a href="https://arxiv.org/abs/2406.06647" class="paper-link" target="_blank">View Paper ↗</a>
    </div>
</div>

<div class="paper-card">
    <div class="paper-title">DeVAIC</div>
    <div class="paper-subtitle">DeVAIC: A Tool for Security Assessment of AI-generated Code</div>
    <div class="paper-meta">
        <span class="paper-tag">2024-04</span>
        <a href="https://arxiv.org/abs/2404.07548" class="paper-link" target="_blank">View Paper ↗</a>
    </div>
</div>

<div class="paper-card">
    <div class="paper-title">PTMs</div>
    <div class="paper-subtitle">Comparing Robustness Against Adversarial Attacks in Code Generation: LLM-Generated vs. Human-Written</div>
    <div class="paper-meta">
        <span class="paper-tag">2024-11</span>
        <a href="https://arxiv.org/abs/2411.10565" class="paper-link" target="_blank">View Paper ↗</a>
    </div>
</div>

<div class="paper-card">
    <div class="paper-title">Codequal Analyzer</div>
    <div class="paper-subtitle">Improving LLM-Generated Code Quality with GRPO</div>
    <div class="paper-meta">
        <span class="paper-tag">2025-06</span>
        <a href="https://arxiv.org/abs/2506.02211" class="paper-link" target="_blank">View Paper ↗</a>
    </div>
</div>

<div class="paper-card">
    <div class="paper-title">Artificial-Intelligence Generated Code Considered Harmful</div>
    <div class="paper-subtitle">Artificial-Intelligence Generated Code Considered Harmful: A Road Map for Secure and High-Quality Code Generation</div>
    <div class="paper-meta">
        <span class="paper-tag">2024-09</span>
        <a href="https://arxiv.org/abs/2409.19182" class="paper-link" target="_blank">View Paper ↗</a>
    </div>
</div>

<div class="paper-card">
    <div class="paper-title">Unveiling Inefficiencies in LLM-Generated Code</div>
    <div class="paper-subtitle">Unveiling Inefficiencies in LLM-Generated Code: Toward a Comprehensive Taxonomy</div>
    <div class="paper-meta">
        <span class="paper-tag">2025-03</span>
        <a href="https://arxiv.org/abs/2503.06327" class="paper-link" target="_blank">View Paper ↗</a>
    </div>
</div>

<div class="paper-card">
    <div class="paper-title">Python Tests Quality</div>
    <div class="paper-subtitle">Quality Assessment of Python Tests Generated by Large Language Models</div>
    <div class="paper-meta">
        <span class="paper-tag">2025-06</span>
        <a href="https://arxiv.org/abs/2506.14297" class="paper-link" target="_blank">View Paper ↗</a>
    </div>
</div>

<div class="paper-card">
    <div class="paper-title">CoQuIR</div>
    <div class="paper-subtitle">CoQuIR: A Comprehensive Benchmark for Code Quality-Aware Information Retrieval</div>
    <div class="paper-meta">
        <span class="paper-tag">2025-06</span>
        <a href="https://arxiv.org/abs/2506.11066" class="paper-link" target="_blank">View Paper ↗</a>
    </div>
</div>

<div class="paper-card">
    <div class="paper-title">REAL</div>
    <div class="paper-subtitle">Training Language Models to Generate Quality Code with Program Analysis Feedback</div>
    <div class="paper-meta">
        <span class="paper-tag">2025-05</span>
        <a href="https://arxiv.org/abs/2505.22704" class="paper-link" target="_blank">View Paper ↗</a>
    </div>
</div>

<div class="paper-card">
    <div class="paper-title">CIDRe</div>
    <div class="paper-subtitle">CIDRe: A Reference-Free Multi-Aspect Criterion for Code Comment Quality Measurement</div>
    <div class="paper-meta">
        <span class="paper-tag">2025-05</span>
        <a href="https://arxiv.org/abs/2505.19757" class="paper-link" target="_blank">View Paper ↗</a>
    </div>
</div>

<div class="paper-card">
    <div class="paper-title">Infinite-Instruct</div>
    <div class="paper-subtitle">Infinite-Instruct: Synthesizing Scaling Code instruction Data with Bidirectional Synthesis and Static Verification</div>
    <div class="paper-meta">
        <span class="paper-tag">2025-05</span>
        <a href="https://arxiv.org/abs/2505.23177" class="paper-link" target="_blank">View Paper ↗</a>
    </div>
</div>

<div class="paper-card">
    <div class="paper-title">Quality In, Quality Out</div>
    <div class="paper-subtitle">Quality In, Quality Out: Investigating Training Data's Role in AI Code Generation</div>
    <div class="paper-meta">
        <span class="paper-tag">2025-03</span>
        <a href="https://arxiv.org/abs/2503.11402" class="paper-link" target="_blank">View Paper ↗</a>
    </div>
</div>

<div class="paper-card">
    <div class="paper-title">Security and Quality in LLM-Generated Code</div>
    <div class="paper-subtitle">Security and Quality in LLM-Generated Code: A Multi-Language, Multi-Model Analysis</div>
    <div class="paper-meta">
        <span class="paper-tag">2025-02</span>
        <a href="https://arxiv.org/abs/2502.01853" class="paper-link" target="_blank">View Paper ↗</a>
    </div>
</div>

<div class="paper-card">
    <div class="paper-title">SwallowCode</div>
    <div class="paper-subtitle">Rewriting Pre-Training Data Boosts LLM Performance in Math and Code</div>
    <div class="paper-meta">
        <span class="paper-tag">2025-05</span>
        <a href="https://arxiv.org/abs/2505.02881" class="paper-link" target="_blank">View Paper ↗</a>
    </div>
</div>

<div class="paper-card">
    <div class="paper-title">ROSE</div>
    <div class="paper-subtitle">ROSE: Transformer-Based Refactoring Recommendation for Architectural Smells</div>
    <div class="paper-meta">
        <span class="paper-tag">2025-07</span>
        <a href="https://arxiv.org/abs/2507.12561" class="paper-link" target="_blank">View Paper ↗</a>
    </div>
</div>

<div class="paper-card">
    <div class="paper-title">Refining ChatGPT-Generated Code</div>
    <div class="paper-subtitle">Refining ChatGPT-Generated Code: Characterizing and Mitigating Code Quality Issues</div>
    <div class="paper-meta">
        <span class="paper-tag">2023-07</span>
        <a href="https://arxiv.org/abs/2307.12596" class="paper-link" target="_blank">View Paper ↗</a>
    </div>
</div>

<div class="paper-card">
    <div class="paper-title">Qwen3</div>
    <div class="paper-subtitle">Qwen3 Technical Report</div>
    <div class="paper-meta">
        <span class="paper-tag">2025-05</span>
        <a href="https://arxiv.org/abs/2505.09388" class="paper-link" target="_blank">View Paper ↗</a>
    </div>
</div>

<div class="paper-card">
    <div class="paper-title">Qwen2.5</div>
    <div class="paper-subtitle">Qwen2.5 Technical Report</div>
    <div class="paper-meta">
        <span class="paper-tag">2024-12</span>
        <a href="https://arxiv.org/abs/2412.15115" class="paper-link" target="_blank">View Paper ↗</a>
    </div>
</div>

<div class="paper-card">
    <div class="paper-title">TeleChat</div>
    <div class="paper-subtitle">Technical Report of TeleChat2, TeleChat2.5 and T1</div>
    <div class="paper-meta">
        <span class="paper-tag">2025-07</span>
        <a href="https://arxiv.org/abs/2507.18013" class="paper-link" target="_blank">View Paper ↗</a>
    </div>
</div>

<div class="paper-card">
    <div class="paper-title">Kimi K2</div>
    <div class="paper-subtitle">Kimi K2: Open Agentic Intelligence</div>
    <div class="paper-meta">
        <span class="paper-tag">2025-07</span>
        <a href="https://arxiv.org/abs/2507.20534" class="paper-link" target="_blank">View Paper ↗</a>
    </div>
</div>

<div class="paper-card">
    <div class="paper-title">ReCode</div>
    <div class="paper-subtitle">ReCode: Updating Code API Knowledge with Reinforcement Learning</div>
    <div class="paper-meta">
        <span class="paper-tag">2025-06</span>
        <a href="https://arxiv.org/abs/2506.20495" class="paper-link" target="_blank">View Paper ↗</a>
    </div>
</div>

<div class="paper-card">
    <div class="paper-title">Seed-Coder</div>
    <div class="paper-subtitle">Seed-Coder: Let the Code Model Curate Data for Itself</div>
    <div class="paper-meta">
        <span class="paper-tag">2025-06</span>
        <a href="https://arxiv.org/abs/2506.03524" class="paper-link" target="_blank">View Paper ↗</a>
    </div>
</div>

<div class="paper-card">
    <div class="paper-title">Data-efficient Fine-tuning</div>
    <div class="paper-subtitle">Data-efficient LLM Fine-tuning for Code Generation</div>
    <div class="paper-meta">
        <span class="paper-tag">2025-04</span>
        <a href="https://arxiv.org/abs/2504.12687" class="paper-link" target="_blank">View Paper ↗</a>
    </div>
</div>

<div class="paper-card">
    <div class="paper-title">CRPE</div>
    <div class="paper-subtitle">CRPE: Expanding The Reasoning Capability of Large Language Model for Code Generation</div>
    <div class="paper-meta">
        <span class="paper-tag">2025-05</span>
        <a href="https://arxiv.org/abs/2505.10594" class="paper-link" target="_blank">View Paper ↗</a>
    </div>
</div>

<div class="paper-card">
    <div class="paper-title">DeepSeek-Coder</div>
    <div class="paper-subtitle">DeepSeek-Coder: When the Large Language Model Meets Programming -- The Rise of Code Intelligence</div>
    <div class="paper-meta">
        <span class="paper-tag">2024-01</span>
        <a href="https://arxiv.org/abs/2401.14196" class="paper-link" target="_blank">View Paper ↗</a>
    </div>
</div>

<div class="paper-card">
    <div class="paper-title">StarCoder 2 and The Stack v2</div>
    <div class="paper-subtitle">StarCoder 2 and The Stack v2: The Next Generation</div>
    <div class="paper-meta">
        <span class="paper-tag">2024-02</span>
        <a href="https://arxiv.org/abs/2402.19173" class="paper-link" target="_blank">View Paper ↗</a>
    </div>
</div>

<div class="paper-card">
    <div class="paper-title">CodeSmellEval</div>
    <div class="paper-subtitle">How Propense Are Large Language Models at Producing Code Smells? A Benchmarking Study</div>
    <div class="paper-meta">
        <span class="paper-tag">2024-12</span>
        <a href="https://arxiv.org/abs/2412.18989" class="paper-link" target="_blank">View Paper ↗</a>
    </div>
</div>

<div class="paper-card">
    <div class="paper-title">RPG</div>
    <div class="paper-subtitle">Rethinking Repetition Problems of LLMs in Code Generation</div>
    <div class="paper-meta">
        <span class="paper-tag">2025-05</span>
        <a href="https://arxiv.org/abs/2505.10402" class="paper-link" target="_blank">View Paper ↗</a>
    </div>
</div>

<div class="paper-card">
    <div class="paper-title">Repetition In Repetition Out</div>
    <div class="paper-subtitle">Repetition In Repetition Out: Towards Understanding Neural Text Degeneration from the Data Perspective</div>
    <div class="paper-meta">
        <span class="paper-tag">2023-10</span>
        <a href="https://arxiv.org/abs/2310.10226" class="paper-link" target="_blank">View Paper ↗</a>
    </div>
</div>

<div class="paper-card">
    <div class="paper-title">Every Sample Matters</div>
    <div class="paper-subtitle">Every Sample Matters: Leveraging Mixture-of-Experts and High-Quality Data for Efficient and Accurate Code LLM</div>
    <div class="paper-meta">
        <span class="paper-tag">2025-03</span>
        <a href="https://arxiv.org/abs/2503.17793" class="paper-link" target="_blank">View Paper ↗</a>
    </div>
</div>

<div class="paper-card">
    <div class="paper-title">WaveCoder</div>
    <div class="paper-subtitle">WaveCoder: Widespread And Versatile Enhancement For Code Large Language Models By Instruction Tuning</div>
    <div class="paper-meta">
        <span class="paper-tag">2023-12</span>
        <a href="https://arxiv.org/abs/2312.14187" class="paper-link" target="_blank">View Paper ↗</a>
    </div>
</div>

<div class="paper-card">
    <div class="paper-title">Brevity is the soul of wit</div>
    <div class="paper-subtitle">Brevity is the soul of wit: Pruning long files for code generation</div>
    <div class="paper-meta">
        <span class="paper-tag">2024-07</span>
        <a href="https://arxiv.org/abs/2407.00434" class="paper-link" target="_blank">View Paper ↗</a>
    </div>
</div>

<div class="paper-card">
    <div class="paper-title">Benchmark Builders</div>
    <div class="paper-subtitle">Large Language Models are Qualified Benchmark Builders: Rebuilding Pre-Training Datasets for Advancing Code Intelligence Tasks</div>
    <div class="paper-meta">
        <span class="paper-tag">2025-04</span>
        <a href="https://arxiv.org/abs/2504.19444" class="paper-link" target="_blank">View Paper ↗</a>
    </div>
</div>

<div class="paper-card">
    <div class="paper-title">Beyond Correctness</div>
    <div class="paper-subtitle">Beyond Correctness: Benchmarking Multi-dimensional Code Generation for Large Language Models</div>
    <div class="paper-meta">
        <span class="paper-tag">2024-07</span>
        <a href="https://arxiv.org/abs/2407.11470" class="paper-link" target="_blank">View Paper ↗</a>
    </div>
</div>

<div class="paper-card">
    <div class="paper-title">Generated Code Diversity</div>
    <div class="paper-subtitle">Is Functional Correctness Enough to Evaluate Code Language Models? Exploring Diversity of Generated Codes</div>
    <div class="paper-meta">
        <span class="paper-tag">2024-08</span>
        <a href="https://arxiv.org/abs/2408.14504" class="paper-link" target="_blank">View Paper ↗</a>
    </div>
</div>

<div class="paper-card">
    <div class="paper-title">CodeMI</div>
    <div class="paper-subtitle">Does Your Neural Code Completion Model Use My Code? A Membership Inference Approach</div>
    <div class="paper-meta">
        <span class="paper-tag">2024-04</span>
        <a href="https://arxiv.org/abs/2404.14296" class="paper-link" target="_blank">View Paper ↗</a>
    </div>
</div>

<div class="paper-card">
    <div class="paper-title">DataComp-LM</div>
    <div class="paper-subtitle">DataComp-LM: In search of the next generation of training sets for language models</div>
    <div class="paper-meta">
        <span class="paper-tag">2024-06</span>
        <a href="https://arxiv.org/abs/2406.11794" class="paper-link" target="_blank">View Paper ↗</a>
    </div>
</div>

<div class="paper-card">
    <div class="paper-title">Codex</div>
    <div class="paper-subtitle">Evaluating Large Language Models Trained on Code</div>
    <div class="paper-meta">
        <span class="paper-tag">2021-07</span>
        <a href="https://arxiv.org/abs/2107.03374" class="paper-link" target="_blank">View Paper ↗</a>
    </div>
</div>

<div class="paper-card">
    <div class="paper-title">Path Planning Evaluation</div>
    <div class="paper-subtitle">Assessing LLM code generation quality through path planning tasks</div>
    <div class="paper-meta">
        <span class="paper-tag">2025-04</span>
        <a href="https://arxiv.org/abs/2504.21276" class="paper-link" target="_blank">View Paper ↗</a>
    </div>
</div>

<div class="paper-card">
    <div class="paper-title">CODEJUDGE</div>
    <div class="paper-subtitle">CODEJUDGE : Evaluating Code Generation with Large Language Models</div>
    <div class="paper-meta">
        <span class="paper-tag">2024-01</span>
        <a href="https://aclanthology.org/2024.emnlp-main.1118.pdf?utm_source=chatgpt.com" class="paper-link" target="_blank">View Paper ↗</a>
    </div>
</div>

<div class="paper-card">
    <div class="paper-title">Datasets for Large Language Models</div>
    <div class="paper-subtitle">Datasets for Large Language Models: A Comprehensive Survey</div>
    <div class="paper-meta">
        <span class="paper-tag">2024-02</span>
        <a href="https://arxiv.org/abs/2402.18041" class="paper-link" target="_blank">View Paper ↗</a>
    </div>
</div>

<div class="paper-card">
    <div class="paper-title">Synthetic Data Generation</div>
    <div class="paper-subtitle">Synthetic Data Generation Using Large Language Models: Advances in Text and Code</div>
    <div class="paper-meta">
        <span class="paper-tag">2025-01</span>
        <a href="https://ieeexplore.ieee.org/document/11080380" class="paper-link" target="_blank">View Paper ↗</a>
    </div>
</div>

<div class="paper-card">
    <div class="paper-title">Cracks in The Stack</div>
    <div class="paper-subtitle">Cracks in The Stack: Hidden Vulnerabilities and Licensing Risks in LLM Pre-Training Datasets</div>
    <div class="paper-meta">
        <span class="paper-tag">2025-05</span>
        <a href="https://ieeexplore.ieee.org/document/11028470" class="paper-link" target="_blank">View Paper ↗</a>
    </div>
</div>

<div class="paper-card">
    <div class="paper-title">Unseen Horizons</div>
    <div class="paper-subtitle">Unseen Horizons: Unveiling the Real Capability of LLM Code Generation Beyond the Familiar</div>
    <div class="paper-meta">
        <span class="paper-tag">2025-04</span>
        <a href="https://ieeexplore.ieee.org/document/11029836" class="paper-link" target="_blank">View Paper ↗</a>
    </div>
</div>

<div class="paper-card">
    <div class="paper-title">MG-Verilog</div>
    <div class="paper-subtitle">MG-Verilog: Multi-grained Dataset Towards Enhanced LLM-assisted Verilog Generation</div>
    <div class="paper-meta">
        <span class="paper-tag">2024-06</span>
        <a href="https://ieeexplore.ieee.org/document/10691738" class="paper-link" target="_blank">View Paper ↗</a>
    </div>
</div>

<div class="paper-card">
    <div class="paper-title">Code Generation Survey</div>
    <div class="paper-subtitle">A Survey on Large Language Models for Code Generation</div>
    <div class="paper-meta">
        <span class="paper-tag">2024-08</span>
        <a href="https://dl.acm.org/doi/10.1145/3747588" class="paper-link" target="_blank">View Paper ↗</a>
    </div>
</div>

<div class="paper-card">
    <div class="paper-title">DataRecipe</div>
    <div class="paper-subtitle">DataRecipe --- How to Cook the Data for CodeLLM?</div>
    <div class="paper-meta">
        <span class="paper-tag">2024-10</span>
        <a href="https://dl.acm.org/doi/10.1145/3691620.3695593" class="paper-link" target="_blank">View Paper ↗</a>
    </div>
</div>

<div class="paper-card">
    <div class="paper-title">Training Data Extraction</div>
    <div class="paper-subtitle">Understanding Privacy Risks of Large Language Models in Japanese Based on Training Data Extraction Attacks</div>
    <div class="paper-meta">
        <span class="paper-tag">2025-08</span>
        <a href="https://dl.acm.org/doi/10.1145/3709018.3736331" class="paper-link" target="_blank">View Paper ↗</a>
    </div>
</div>

<div class="paper-card">
    <div class="paper-title">aiXcoder-7B</div>
    <div class="paper-subtitle">aiXcoder-7B: A Lightweight and Effective Large Language Model for Code Processing</div>
    <div class="paper-meta">
        <span class="paper-tag">2025-04</span>
        <a href="https://ieeexplore.ieee.org/document/11121702" class="paper-link" target="_blank">View Paper ↗</a>
    </div>
</div>

<div class="paper-card">
    <div class="paper-title">Imperfect Code Generation</div>
    <div class="paper-subtitle">Imperfect Code Generation: Uncovering Weaknesses in Automatic Code Generation by Large Language Models</div>
    <div class="paper-meta">
        <span class="paper-tag">2024-05</span>
        <a href="https://ieeexplore.ieee.org/document/10554837" class="paper-link" target="_blank">View Paper ↗</a>
    </div>
</div>

<div class="paper-card">
    <div class="paper-title">Inter-Dataset Code Duplication</div>
    <div class="paper-subtitle">On Inter-Dataset Code Duplication and Data Leakage in Large Language Models</div>
    <div class="paper-meta">
        <span class="paper-tag">2025-01</span>
        <a href="https://ieeexplore.ieee.org/document/10759822" class="paper-link" target="_blank">View Paper ↗</a>
    </div>
</div>

<div class="paper-card">
    <div class="paper-title">LLM-ProS</div>
    <div class="paper-subtitle">LLM-ProS: Analyzing Large Language Models’ Performance in Competitive Problem Solving</div>
    <div class="paper-meta">
        <span class="paper-tag">2025-05</span>
        <a href="https://ieeexplore.ieee.org/document/11028406" class="paper-link" target="_blank">View Paper ↗</a>
    </div>
</div>

<div class="paper-card">
    <div class="paper-title">ClassEval</div>
    <div class="paper-subtitle">Evaluating Large Language Models in Class-Level Code Generation</div>
    <div class="paper-meta">
        <span class="paper-tag">2024-6</span>
        <a href="https://ieeexplore.ieee.org/document/10549472" class="paper-link" target="_blank">View Paper ↗</a>
    </div>
</div>

<div class="paper-card">
    <div class="paper-title">Uncovering Pretraining Code in LLMs</div>
    <div class="paper-subtitle">Uncovering Pretraining Code in LLMs: A Syntax-Aware Attribution Approach</div>
    <div class="paper-meta">
        <span class="paper-tag">2025-11</span>
        <a href="https://arxiv.org/abs/2511.07033" class="paper-link" target="_blank">View Paper ↗</a>
    </div>
</div>

<div class="paper-card">
    <div class="paper-title">RealSec-Bench</div>
    <div class="paper-subtitle">RealSec-bench: A Benchmark for Evaluating Secure Code Generation in Real-World Repositories</div>
    <div class="paper-meta">
        <span class="paper-tag">2026-01</span>
        <a href="https://arxiv.org/abs/2601.22706" class="paper-link" target="_blank">View Paper ↗</a>
    </div>
</div>

<div class="paper-card">
    <div class="paper-title">ShortCoder</div>
    <div class="paper-subtitle">ShortCoder: Knowledge-Augmented Syntax Optimization for Token-Efficient Code GenerationPreprint</div>
    <div class="paper-meta">
        <span class="paper-tag">2026-01</span>
        <a href="https://arxiv.org/abs/2601.09703" class="paper-link" target="_blank">View Paper ↗</a>
    </div>
</div>

<div class="paper-card">
    <div class="paper-title">APIKG4SYN</div>
    <div class="paper-subtitle">Framework-Aware Code Generation with API Knowledge Graph-Constructed Data: A Study on HarmonyOS</div>
    <div class="paper-meta">
        <span class="paper-tag">2025-11</span>
        <a href="https://arxiv.org/abs/2512.00380" class="paper-link" target="_blank">View Paper ↗</a>
    </div>
</div>

<div class="paper-card">
    <div class="paper-title">MultiCodeIF</div>
    <div class="paper-subtitle">A hierarchical and evolvable benchmark for fine-grained code instruction following with multi-turn feedback</div>
    <div class="paper-meta">
        <span class="paper-tag">2025-07</span>
        <a href="https://arxiv.org/abs/2507.00699" class="paper-link" target="_blank">View Paper ↗</a>
    </div>
</div>

<div class="paper-card">
    <div class="paper-title">Beyond Functional Correctness</div>
    <div class="paper-subtitle">Beyond functional correctness: Investigating coding style inconsistencies in large language models</div>
    <div class="paper-meta">
        <span class="paper-tag">2024-06</span>
        <a href="https://arxiv.org/abs/2407.00456" class="paper-link" target="_blank">View Paper ↗</a>
    </div>
</div>

<div class="paper-card">
    <div class="paper-title">Adadec</div>
    <div class="paper-subtitle">Adadec: Uncertainty-guided adaptive decoding for llm-based code generation</div>
    <div class="paper-meta">
        <span class="paper-tag">2025-06</span>
        <a href="https://arxiv.org/html/2506.08980v1" class="paper-link" target="_blank">View Paper ↗</a>
    </div>
</div>

<div class="paper-card">
    <div class="paper-title">Code Copycat Conundrum</div>
    <div class="paper-subtitle">Code Copycat Conundrum: Demystifying Repetition in LLM-based Code Generation</div>
    <div class="paper-meta">
        <span class="paper-tag">2025-04</span>
        <a href="https://arxiv.org/abs/2504.12608" class="paper-link" target="_blank">View Paper ↗</a>
    </div>
</div>

<div class="paper-card">
    <div class="paper-title">AllianceCoder</div>
    <div class="paper-subtitle">What to retrieve for effective retrieval-augmented code generation? an empirical study and beyond</div>
    <div class="paper-meta">
        <span class="paper-tag">2025-03</span>
        <a href="https://arxiv.org/abs/2503.20589" class="paper-link" target="_blank">View Paper ↗</a>
    </div>
</div>

<div class="paper-card">
    <div class="paper-title">RustEvo^ 2</div>
    <div class="paper-subtitle">RustEvo^ 2: An Evolving Benchmark for API Evolution in LLM-based Rust Code Generation</div>
    <div class="paper-meta">
        <span class="paper-tag">2025-03</span>
        <a href="https://arxiv.org/abs/2503.16922" class="paper-link" target="_blank">View Paper ↗</a>
    </div>
</div>

<div class="paper-card">
    <div class="paper-title">RobGen</div>
    <div class="paper-subtitle">A Preliminary Study on the Robustness of Code Generation by Large Language Models</div>
    <div class="paper-meta">
        <span class="paper-tag">2025-03</span>
        <a href="https://arxiv.org/abs/2503.20197" class="paper-link" target="_blank">View Paper ↗</a>
    </div>
</div>

<div class="paper-card">
    <div class="paper-title">Llm Hallucinations in Practical Code Generation</div>
    <div class="paper-subtitle">Llm hallucinations in practical code generation: Phenomena, mechanism, and mitigation</div>
    <div class="paper-meta">
        <span class="paper-tag">2024-09</span>
        <a href="https://arxiv.org/abs/2409.20550" class="paper-link" target="_blank">View Paper ↗</a>
    </div>
</div>

<div class="paper-card">
    <div class="paper-title">COFFE</div>
    <div class="paper-subtitle">COFFE: A Code Efficiency Benchmark for Code Generation</div>
    <div class="paper-meta">
        <span class="paper-tag">2025-02</span>
        <a href="https://arxiv.org/abs/2502.02827" class="paper-link" target="_blank">View Paper ↗</a>
    </div>
</div>

<div class="paper-card">
    <div class="paper-title">AATK Benchmark</div>
    <div class="paper-subtitle">Asleep at the keyboard? assessing the security of github copilot's code contributions</div>
    <div class="paper-meta">
        <span class="paper-tag">2021-08</span>
        <a href="https://dl.acm.org/doi/10.1145/3610721" class="paper-link" target="_blank">View Paper ↗</a>
    </div>
</div>
