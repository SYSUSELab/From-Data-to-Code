---
layout: default
title: Overview
nav_order: 1
description: "Bridging Generation and Training: A Systematic Review of Quality Issues in LLMs for Code"
permalink: /
---

# 📖 Bridging Generation and Training

## A Systematic Review of Quality Issues in LLMs for Code

<div style="margin: 20px 0;">
  <a href="{{ '/paper/From-Data-to-Code.pdf' | relative_url }}" class="btn btn-primary">📄 View Paper</a>
  <a href="https://github.com/SYSUSELab/From-Data-to-Code" class="btn btn-outline">💻 GitHub Repo</a>
</div>

Large language models (LLMs) frequently generate defective outputs in code generation tasks, ranging from logical bugs to security vulnerabilities.
 While these generation failures are often treated as model-level limitations, empirical evidence increasingly traces their root causes to imperfections within the training corpora.

---

## 📢 News

- **[2026-04]** 🚀 The `From-Data-to-Code` repository is officially launched.

---

<div class="stats-bento">
  <div class="paper-card" style="margin-bottom: 0; text-align: center;">
    <div style="font-size: 2rem; font-weight: 800; color: var(--accent-blue);">114</div>
    <div style="font-size: 0.8rem; color: var(--text-muted);">Primary Studies Reviewed</div>
  </div>
  <div class="paper-card" style="margin-bottom: 0; text-align: center;">
    <div style="font-size: 2rem; font-weight: 800; color: #3fb950;">9</div>
    <div style="font-size: 0.8rem; color: var(--text-muted);">Quality Dimensions</div>
  </div>
  <div class="paper-card" style="margin-bottom: 0; text-align: center;">
    <div style="font-size: 2rem; font-weight: 800; color: var(--accent-purple);">18</div>
    <div style="font-size: 0.8rem; color: var(--text-muted);">Propagation Mechanisms</div>
  </div>
</div>

## 📖 Abstract

<div class="abstract-box">
This paper presents a systematic literature review of 114 primary studies to investigate how training data quality issues propagate into code generation. We establish a unified taxonomy that categorizes generated code quality issues across nine dimensions and training data quality issues into code and non-code attributes. 

Based on this taxonomy, we formalize a causal framework detailing 18 typical propagation mapping mechanisms. Furthermore, we synthesize state-of-the-art detection and mitigation techniques across the data, model, and generation lifecycles. 
</div>

---

<div align="center">
  <img src="{{ '/images/paper_collection.png' | relative_url }}" alt="Overview of the process of paper collection and filtering" width="80%" style="border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.2);">
  <p><em>Fig. 1. Overview of the paper collection and filtering process.</em></p>
</div>

<br>

<div align="center">
  <img src="{{ '/images/lifecycle.png' | relative_url }}" alt="Lifecycle of Detection and Governance" width="80%" style="border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.2);">
  <p><em>Fig. 2. Conceptual Framework of Quality Issues and Mitigation in the LLM Lifecycle.</em></p>
</div>

---

## 🤝 Contribution

We warmly welcome contributions from the community! If you have new research or have discovered missing classic papers, please follow these steps:

1. Fork this repository.
2. Add your paper to the corresponding RQ section.
3. Submit a Pull Request.
