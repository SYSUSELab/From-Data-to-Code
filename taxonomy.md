---
layout: default
title: Quality Taxonomies
description: "Eight generated-code dimensions and thirteen training-data headings, with definitions and paper-level memberships."
nav_order: 2
---

# Quality taxonomies

RQ1 describes generated-code outcomes. RQ2 describes properties of training samples and corpora. Coding is multi-label: a paper can support several headings, once per heading. Counts indicate research attention and do not measure defect prevalence.

## {% include rq_icon.html rq=1 %} RQ1: Generated-code quality
{: #rq1-generated-code-quality }

| Dimension | Immediate failure condition |
|:---|:---|
| Correctness | Syntax, logic, API, or dependency failures under task-required conditions |
| Security | Weaknesses permitting unauthorized access, disclosure, alteration, or unsafe execution |
| Compliance | Licensing, privacy, harmful-content, or other rights-related problems |
| Robustness | Failure to tolerate abnormal inputs, boundary cases, or runtime disruption |
| Maintainability | Structure or coupling that makes modification and extension difficult |
| Understandability | Naming, comments, or expressions that obscure intent |
| Efficiency | Excessive execution time or memory for the required behavior |
| Generation Derailment | Repetition, truncation, verbosity, or deviation from generation instructions |

The immediate failure condition determines the heading when manifestations overlap. A redundant structure that impedes modification concerns Maintainability; repetitive or instruction-divergent output concerns Generation Derailment.

![Eight generated-code quality dimensions, with paper counts and definitions]({{ '/images/generated_code_issues.svg' | relative_url }})

The [195 paper–dimension memberships]({{ '/data/rq1_code_quality.csv' | relative_url }}) involve 98 papers. Correctness has the largest literature coverage. The [codebook]({{ '/data/rq3/taxonomy_codebook.csv' | relative_url }}) gives operational definitions and inclusion/exclusion boundaries.

## {% include rq_icon.html rq=2 %} RQ2: Training-data quality
{: #rq2-training-data-quality }

**Code attributes** comprise Correctness, Security, Compliance, Robustness, Maintainability, Understandability, and Efficiency. They concern the code sample itself.

**Non-code and corpus attributes** comprise textual Compliance and Security Risks, Distribution Imbalance, Redundancy, Inadequate Diversity, Data Contamination Risks, and Low-Value Data. They concern surrounding content, supervision, composition, or training–evaluation overlap.

![Thirteen training-data quality headings grouped into code attributes and non-code or corpus attributes]({{ '/images/data_quality_issues.svg' | relative_url }})

The [165 paper–heading memberships]({{ '/data/rq2_data_quality.csv' | relative_url }}) involve 78 papers. Distribution imbalance concerns relative frequency among represented strata; inadequate diversity concerns absent or effectively uncovered strata. Redundancy concerns repetition within training data; contamination concerns overlap with evaluation material.

## Supporting papers

The complete [114-paper register]({{ '/data/included_studies.csv' | relative_url }}) records stable IDs, paper links, included-copy metadata, and consensus quality scores. Download the membership tables above to recover the exact supporting set for each heading.

{% assign rq1_ids = site.data.rq1_code_quality | map: 'study_id' %}
{% assign rq2_ids = site.data.rq2_data_quality | map: 'study_id' %}
{% assign taxonomy_ids = rq1_ids | concat: rq2_ids | uniq %}
{% include study_list.html study_ids=taxonomy_ids %}
