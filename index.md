---
layout: default
title: "From Data to Code: Quality Issues in LLMs for Code"
nav_order: 1
nav_title: Overview
description: "Evidence, taxonomies, and reproducible results from a systematic review of 114 papers on training-data and generated-code quality."
permalink: /
---

<section class="site-hero">
  <div class="site-hero__content">
    <div class="site-hero__eyebrow">Systematic Literature Review</div>
    <h1>From Data to Code</h1>
    <h2>Bridging Generation and Training: A Systematic Review of Quality Issues in LLMs for Code</h2>
    <p class="site-hero__summary">Trace the evidence connecting training-data quality with generated-code outcomes, and explore detection and mitigation across the LLM lifecycle.</p>
    <div class="hero-actions">
      <a href="{{ '/data/' | relative_url }}" class="btn btn-primary">Explore the Data</a>
      <a href="https://arxiv.org/abs/2605.05267" class="btn btn-outline">Original Preprint</a>
      <a href="https://github.com/SYSUSELab/From-Data-to-Code" class="btn btn-outline">GitHub</a>
    </div>
  </div>
  <div class="hero-visual">
    <img class="hero-visual__image hero-visual__image--light" src="{{ '/images/from-data-to-code-hero-light.png' | relative_url }}" alt="A blue-to-violet bridge connects 13 training-data quality headings through 12 relationship families with eight generated-code dimensions. The review includes 114 papers; 67 contribute 101 relationship assignments. Detection and mitigation act at the data, model, and generation levels." width="1672" height="941" loading="eager" decoding="async" fetchpriority="high">
    <img class="hero-visual__image hero-visual__image--dark" src="{{ '/images/from-data-to-code-hero-dark.png' | relative_url }}" alt="" width="1672" height="941" decoding="async" aria-hidden="true">
  </div>
</section>

<div class="stats-bento" aria-label="Review summary">
  <div class="stat-card"><span class="stat-card__value">114</span><span class="stat-card__label">Included Papers</span></div>
  <div class="stat-card"><span class="stat-card__value">8</span><span class="stat-card__label">Code Quality Dimensions</span></div>
  <div class="stat-card"><span class="stat-card__value">12</span><span class="stat-card__label">Relationship Families</span></div>
</div>

## About the review

Large language models frequently generate defective code, ranging from logical bugs to security vulnerabilities. Training-data quality contributes to these outcomes alongside model architecture, optimization and alignment, prompting and inference context, and decoding.

We review **114 included papers**, synthesize **eight generated-code quality dimensions** and **13 training-data headings**, and organize reported data-to-code relationships into **12 families**. We also compare detection and mitigation methods by their prerequisites, outcomes, costs, and limitations. Data curation forms one layer of quality assurance coordinated with model, inference, and software-development controls.

The **101 paper-level relationship assignments from 67 papers** describe literature coverage. Their counts and Sankey widths do not measure effect size or causal strength. Each assignment links to its supporting evidence and scope limitations.

## Explore the findings

| Research question | Resource |
|:---|:---|
| {% include rq_icon.html rq=1 %} RQ1: What generated-code quality issues occur? | [Code quality taxonomy]({{ '/taxonomy.html#rq1-generated-code-quality' | relative_url }}) |
| {% include rq_icon.html rq=2 %} RQ2: What training-data quality issues occur? | [Training-data taxonomy]({{ '/taxonomy.html#rq2-training-data-quality' | relative_url }}) |
| {% include rq_icon.html rq=3 %} RQ3: What data-to-code relationships are reported? | [Relationship families and evidence]({{ '/mapping.html' | relative_url }}) |
| {% include rq_icon.html rq=4 %} RQ4: How are issues detected? | [Detection methods and trade-offs]({{ '/detection.html' | relative_url }}) |
| {% include rq_icon.html rq=5 %} RQ5: How are issues mitigated? | [Mitigation and practitioner workflow]({{ '/governance.html' | relative_url }}) |
| How can the findings be checked? | [Result data and reproduction guide]({{ '/data/' | relative_url }}) |

## Study collection

Database searches cover publications through **December 31, 2025**. After deduplication, 2,114 records yielded 122 eligible papers. Snowballing, completed in February 2026, added 12 candidates. Quality assessment retained 114 of 134 candidates at a consensus threshold of 10/16. Three independent pre-consensus total scores per candidate yield interval Krippendorff's **alpha = 0.717**.

<div class="figure-block">
  <div class="figure-frame"><img src="{{ '/images/paper_collection.png' | relative_url }}" alt="Study selection: 2,298 retrieved records, 184 duplicates removed, 2,114 unique records, 122 eligible papers, 12 snowballing additions, 134 quality-assessment candidates, and 114 included papers." width="1100" loading="lazy" decoding="async"></div>
  <p class="figure-caption">Paper collection and filtering. See the <a href="{{ '/data/search_summary.csv' | relative_url }}">search summary</a> and <a href="{{ '/data/quality_scores_for_included_papers.csv' | relative_url }}">consensus scores</a>.</p>
</div>

## Quality assurance across the lifecycle

<div class="figure-block">
  <div class="figure-frame figure-frame--narrow"><img src="{{ '/images/lifecycle.png' | relative_url }}" alt="Detection and mitigation controls act at the data, model, and generation stages." width="860" loading="lazy" decoding="async"></div>
  <p class="figure-caption">A lifecycle view of quality issues and interventions. Individual controls have been evaluated in different settings; the integrated workflow is an author synthesis.</p>
</div>

## Versions and contributions

This website and its result package reflect the major-revision synthesis. The [May 2026 preprint](https://arxiv.org/abs/2605.05267) and [archived PDF]({{ '/paper/From-Data-to-Code.pdf' | relative_url }}) document the original version; its taxonomy and mapping counts differ. Publication-status sensitivity results are a snapshot verified on **August 29, 2026**.

Contributions should identify the relevant research question, primary source, supporting passage, and scope limitation. Open an issue or a pull request in the [project repository](https://github.com/SYSUSELab/From-Data-to-Code).
