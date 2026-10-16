---
layout: default
title: Detection Methods
description: "Detection prerequisites, operational advantages, costs, and evidence limits across generated code and training data."
nav_order: 4
---

# {% include rq_icon.html rq=4 %} RQ4: Detecting quality issues
{: #rq4-detecting-quality-issues }

Detection depends on the artifact, available oracle, language, and deployment context. Outcomes from heterogeneous evaluations support conditional selection; they do not establish a universal method ranking.

| Family | Applicable when | Operational value | Cost and limitation |
|:---|:---|:---|:---|
| Execution and resource measurement | Code can run with tests, a reference behavior, or a representative workload | Reveals behavioral failures, runtime, or memory use | Requires dependencies, inputs, and an oracle; finite testing cannot prove equivalence |
| Static, rule, metadata, and overlap analysis | Parsers, rules, API maps, provenance, or comparison sets exist | Flags encoded patterns without running the artifact | Coverage depends on rules, language support, thresholds, and metadata |
| General LLM evaluation | A rubric and capable contextual evaluator are available | Supports qualitative judgment and triage where fixed oracles are absent | Sensitive to evaluator, prompt, order, and context; requires calibration and inference cost |
| Task-specific learned scoring | In-domain labels or a learnable proxy exist | Enables versioned batch scoring | Label construction and training cost; transfer can fail under domain shift |
| Human or hybrid review | Ambiguous findings require contextual judgment | Helps construct labels and validate automated flags | Expert effort and disagreement limit throughput; most reviewed evidence concerns research annotation |

## Generated-code detection

![Generated-code detection grouped into execution, static and human analysis, and model-based methods]({{ '/images/generated_code_issues_detection.svg' | relative_url }})

{% include method_table.html scope='generated_code_detection' %}

## Training-data detection

![Training-data detection grouped into execution, static and corpus audits, and model-based methods]({{ '/images/data_quality_issues_detection.svg' | relative_url }})

{% include method_table.html scope='training_data_detection' %}

## Automation evidence and residual gaps

The [21-row automation crosswalk]({{ '/data/automation_examples.csv' | relative_url }}) identifies a direct automated detection exemplar and a direct automated mitigation exemplar for each of **eight code headings and 13 data headings**. They can address different subtypes. The result establishes existence at a broad-heading level; it does not establish complete subtype coverage, paired detection and mitigation, or deployment readiness.

Human work remains in constructing rules, tests, labels, prompts, and thresholds, and in adjudicating context-sensitive findings. Important gaps include output-side copyright and privacy leakage, semantic contamination, repository-scale structural quality, and end-to-end CI/CD evaluation. RQ3 relationship families do not constitute an additional issue-detection denominator.

## Supporting papers

{% assign code_methods = site.data.method_assignments | where: 'taxonomy_scope', 'generated_code_detection' %}
{% assign data_methods = site.data.method_assignments | where: 'taxonomy_scope', 'training_data_detection' %}
{% assign detection_rows = code_methods | concat: data_methods %}
{% assign detection_ids = detection_rows | map: 'study_id' | uniq %}
{% include study_list.html study_ids=detection_ids %}
