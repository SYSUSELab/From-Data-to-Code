---
layout: default
title: "From Data to Code: A Systematic Review of Quality Issues in LLMs for Code"
nav_order: 1
description: "Project website for Bridging Generation and Training, a systematic literature review of training data quality issues, generated code quality issues, detection methods, and governance strategies for large language models for code."
permalink: /
---

<section class="site-hero">
  <div class="site-hero__content">
    <div class="site-hero__eyebrow">Systematic Literature Review</div>
    <h1>From Data to Code</h1>
    <h2>Bridging Generation and Training: A Systematic Review of Quality Issues in LLMs for Code</h2>
    <p class="site-hero__summary">A research map of how training data quality issues propagate into generated code defects, detection methods, and governance strategies across the LLM lifecycle.</p>
    <div class="hero-actions">
      <a href="https://arxiv.org/abs/2605.05267" class="btn btn-primary">View Paper</a>
      <a href="https://github.com/SYSUSELab/From-Data-to-Code" class="btn btn-outline">GitHub Repo</a>
    </div>
  </div>
  <div class="hero-visual">
    <img class="hero-visual__image hero-visual__image--light" src="{{ '/images/from-data-to-code-hero-light.png' | relative_url }}" alt="From Data to Code project overview" width="980" height="552" loading="eager" decoding="async" fetchpriority="high">
    <img class="hero-visual__image hero-visual__image--dark" src="{{ '/images/from-data-to-code-hero-dark.png' | relative_url }}" alt="" width="980" height="552" loading="eager" decoding="async" fetchpriority="high" aria-hidden="true">
  </div>
</section>

<div class="stats-bento" aria-label="Review summary">
  <div class="stat-card">
    <span class="stat-card__value">114</span>
    <span class="stat-card__label">Primary Studies Reviewed</span>
  </div>
  <div class="stat-card">
    <span class="stat-card__value">9</span>
    <span class="stat-card__label">Quality Dimensions</span>
  </div>
  <div class="stat-card">
    <span class="stat-card__value">18</span>
    <span class="stat-card__label">Propagation Mechanisms</span>
  </div>
</div>

From Data to Code is the project website for **Bridging Generation and Training: A Systematic Review of Quality Issues in LLMs for Code**. This systematic literature review studies how training data quality issues in large language models for code propagate into generated code quality issues, including correctness bugs, security vulnerabilities, compliance risks, robustness failures, maintainability problems, and efficiency defects.

The review connects data defects, code generation failures, detection methods, and governance strategies across the LLM lifecycle. It provides a taxonomy of quality issues in LLM-generated code, a taxonomy of training data quality issues, and a mapping from data problems to code defects.

---

## 📢 News

<ul class="news-list">
  <li><strong>[2026-05]</strong> Our paper is now available on <a href="https://arxiv.org/abs/2605.05267">arXiv</a>.</li>
  <li><strong>[2026-04]</strong> The <code>From-Data-to-Code</code> repository is officially launched.</li>
</ul>

---

## 📖 Abstract

<div class="abstract-box">
This paper presents a systematic literature review of 114 primary studies to investigate how training data quality issues propagate into code generation. We establish a unified taxonomy that categorizes generated code quality issues across nine dimensions and training data quality issues into code and non-code attributes.

Based on this taxonomy, we formalize a causal framework detailing 18 typical propagation mapping mechanisms. Furthermore, we synthesize state-of-the-art detection and mitigation techniques across the data, model, and generation lifecycles.
</div>

---

<div class="figure-block">
  <div class="figure-frame figure-frame--narrow">
    <img src="{{ '/images/paper_collection.png' | relative_url }}" alt="Overview of the process of paper collection and filtering" width="860" loading="lazy" decoding="async">
  </div>
  <p class="figure-caption"><em>Fig. 1. Overview of the paper collection and filtering process.</em></p>
</div>

<div class="figure-block">
  <div class="figure-frame figure-frame--narrow">
    <img src="{{ '/images/lifecycle.png' | relative_url }}" alt="Lifecycle of Detection and Governance" width="860" loading="lazy" decoding="async">
  </div>
  <p class="figure-caption"><em>Fig. 2. Conceptual Framework of Quality Issues and Mitigation in the LLM Lifecycle.</em></p>
</div>

---

## 🤝 Contribution

<div class="contribution-callout">
  <p>We welcome contributions from the community. If you have new research or have discovered missing classic papers, please follow these steps:</p>
  <ol>
    <li>Fork this repository.</li>
    <li>Add your paper to the corresponding RQ section.</li>
    <li>Submit a Pull Request.</li>
  </ol>
</div>



<div class="contributors-footer">
  <div class="contributors-footer__inner">
    <span><strong>Contributors</strong></span>
    <a href="https://github.com/kaifeng-he" target="_blank" class="contributor-link">
      <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"></path></svg>
      Kaifeng He
    </a>
    <a href="https://github.com/PeiliangCai" target="_blank" class="contributor-link">
      <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"></path></svg>
      Peiliang Cai
    </a>
  </div>
</div>
