---
layout: default
title: Home
nav_order: 1
description: "A Systematic Review of Quality Issues in LLMs for Code"
permalink: /
---

# Bridging Generation and Training: A Systematic Review of Quality Issues in LLMs for Code

<div class="abstract-box">
  <strong>📖 Abstract:</strong> Large language models (LLMs) frequently generate defective outputs in code generation tasks, ranging from logical bugs to security vulnerabilities. While these generation failures are often treated as model-level limitations, empirical evidence increasingly traces their root causes to imperfections within the training corpora. Yet, the specific mechanisms linking training data quality issues to generated code quality issues remain largely unmapped. This paper presents a systematic literature review of 114 primary studies to investigate how training data quality issues propagate into code generation. We establish a unified taxonomy that categorizes generated code quality issues across nine dimensions and training data quality issues into code and non-code attributes. Based on this taxonomy, we formalize a causal framework detailing 18 typical propagation mapping mechanisms. Furthermore, we synthesize state-of-the-art detection and mitigation techniques across the data, model, and generation lifecycles. 
</div>

<div class="img-container">
  <img src="{{ site.baseurl }}/images/lifecycle.png" alt="Lifecycle of Detection and Governance" width="80%">
  <p><em>Fig. 1. Conceptual Framework of Quality Issues and Mitigation in the LLM Lifecycle.</em></p>
</div>

---


## 📢 News

- **[2026-04]** 🚀 The `From-Data-to-Code` repository is officially launched.

---

## 📚 Overview of Findings

Our review is structured around five key Research Questions:

1.  **[RQ1: Generated Code Quality Issues]({% link pages/rq1.md %})**: A taxonomy of 9 core dimensions of quality issues in LLM-generated code.
2.  **[RQ2: Training Data Quality Issues]({% link pages/rq2.md %})**: Categorization of intrinsic flaws within pre-training and fine-tuning corpora.
3.  **[RQ3: Mapping: Data to Code]({% link pages/rq3.md %})**: 18 propagation mechanisms bridging dataset flaws and generated code defects.
4.  **[RQ4: Detection Methods]({% link pages/rq4.md %})**: Evolution of techniques from static analysis to model-driven evaluation.
5.  **[RQ5: Governance Strategies]({% link pages/rq5.md %})**: Multi-layered framework for addressing quality defects throughout the lifecycle.

<div class="img-container">
  <img src="{{ site.baseurl }}/images/paper_collection.png" alt="Overview of the process of paper collection and filtering" width="80%">
  <p><em>Fig. 2. Overview of the paper collection and filtering process.</em></p>
</div>

---

## 🔗 Resources

- **GitHub Repository:** [SYSUSELab/From-Data-to-Code](https://github.com/SYSUSELab/From-Data-to-Code)
- **Paper (PDF):** [Download]({{ site.baseurl }}/paper.pdf)

