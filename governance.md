---
layout: default
title: Mitigation and Workflow
description: "Conditional mitigation choices and an author-synthesized workflow spanning data intake, generation, review, CI/CD, and maintenance."
nav_order: 5
---

# {% include rq_icon.html rq=5 %} RQ5: Mitigation and software workflow
{: #rq5-mitigation-and-software-workflow }

Mitigation can act during dataset construction, model training, or generation. The intervention should match the diagnosed property and be evaluated against its intended output quality and possible regressions.

| Family | Useful conditions | Benefit | Cost, trade-off, and evidence limit |
|:---|:---|:---|:---|
| Deterministic validation and filtering | A checkable sample defect and another training run | Removes specified invalid, vulnerable, duplicate, or unsuitable material | Rules can discard useful samples; bundled pipelines rarely isolate each filter |
| Scoring, sampling, and expansion | Quality signals, a target mixture, or verified new sources | Selects graded quality and broadens relevant coverage | Labels and mixture targets require judgment; scoring and synthesis add cost and can repeat bias |
| Rewriting and transformation | Useful samples have recoverable presentation, alignment, or implementation defects | Retains information while changing a defined property | Requires validation; improvements can be task-dependent and can cause regressions |
| Model adaptation and reward-guided training | Weights or prefixes can be updated with relevant examples or rewards | Amortizes a target behavior across requests | Training and regression evaluation cost; reward proxies can conflict with functionality |
| Prompt, retrieval, and decoding control | Constraints or current context vary by request | Supplies targeted guidance or checker feedback at inference | Retrieval and decoding add latency; poor context can harm otherwise familiar tasks |
| Feedback-guided or deterministic repair | A compiler, test, analyzer, API map, or rule localizes a defect | Reuses development tools to repair candidates | Repeated calls and tests cost time; repairs can introduce defects or plateau |

## Generated-code mitigation

Data-level mitigation is detailed in the next section. Its effect on generated code requires training and held-out output evaluation.

{% include method_table.html scope='generated_code_mitigation' %}

## Training-data mitigation

{% include method_table.html scope='training_data_mitigation' %}

## Applying controls in a project

The following workflow is an **author synthesis of separately evaluated controls**. Included papers do not evaluate the complete arrangement as an integrated production system.

| Workflow point | Controls and retained evidence |
|:---|:---|
| Dataset intake | Record sources, licensing, provenance, versions, and coverage; check samples and training–evaluation overlap |
| Dependencies and build | Pin the environment; validate APIs and versions; compile or resolve packages |
| Local review | Run tests and static checks; examine intent, security, and maintainability in context |
| CI/CD and release | Apply project-specific gates; measure workloads and boundaries; return repaired candidates through applicable checks |
| Repository maintenance | Retain model, prompt, retrieval, artifact, and tool versions; investigate regressions as dependencies and requirements change |

Begin with deterministic checks, add execution and stress testing where an oracle exists, and use contextual triage and repair for residual cases. Projects set their own thresholds and escalation rules. The [automation crosswalk]({{ '/data/automation_examples.csv' | relative_url }}) records narrow exemplars and scope limits; it does not establish full issue coverage or production readiness.

## Supporting papers

{% assign code_methods = site.data.method_assignments | where: 'taxonomy_scope', 'generated_code_mitigation' %}
{% assign data_methods = site.data.method_assignments | where: 'taxonomy_scope', 'training_data_mitigation' %}
{% assign mitigation_rows = code_methods | concat: data_methods %}
{% assign mitigation_ids = mitigation_rows | map: 'study_id' | uniq %}

Browse **{{ mitigation_ids.size }} distinct papers** by mitigation method, separated by the artifact being changed. Expand a method to see its taxonomy path and supporting papers, or select its paper count in the tables above. Membership is multi-label: a paper can appear under several methods. The [paper–method memberships]({{ '/data/method_assignments.csv' | relative_url }}) retain the exact assignments.

### Generated-code mitigation

{% assign code_categories = site.data.method_taxonomy | where: 'taxonomy_scope', 'generated_code_mitigation' %}
{% include supporting_papers.html categories=code_categories memberships=code_methods match_key='method_id' membership_key='method_id' id_key='method_id' label_key='method_leaf' context_key='method_path' %}

### Training-data mitigation

{% assign data_categories = site.data.method_taxonomy | where: 'taxonomy_scope', 'training_data_mitigation' %}
{% include supporting_papers.html categories=data_categories memberships=data_methods match_key='method_id' membership_key='method_id' id_key='method_id' label_key='method_leaf' context_key='method_path' %}
