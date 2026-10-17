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
| [Correctness](#papers-rq1_cor) | Syntax, logic, API, or dependency failures under task-required conditions |
| [Security](#papers-rq1_sec) | Weaknesses permitting unauthorized access, disclosure, alteration, or unsafe execution |
| [Compliance](#papers-rq1_com) | Licensing, privacy, harmful-content, or other rights-related problems |
| [Robustness](#papers-rq1_rob) | Failure to tolerate abnormal inputs, boundary cases, or runtime disruption |
| [Maintainability](#papers-rq1_mai) | Structure or coupling that makes modification and extension difficult |
| [Understandability](#papers-rq1_und) | Naming, comments, or expressions that obscure intent |
| [Efficiency](#papers-rq1_eff) | Excessive execution time or memory for the required behavior |
| [Generation Derailment](#papers-rq1_der) | Repetition, truncation, verbosity, or deviation from generation instructions |

The immediate failure condition determines the heading when manifestations overlap. A redundant structure that impedes modification concerns Maintainability; repetitive or instruction-divergent output concerns Generation Derailment.

{% include research_figure.html src='/images/generated_code_issues.svg' height=770 alt='Eight generated-code quality dimensions, with paper counts and definitions' caption='RQ1 overview. Paper counts indicate literature coverage.' %}

The [195 paper–dimension memberships]({{ '/data/rq1_code_quality.csv' | relative_url }}) involve 98 papers. Correctness has the largest literature coverage. The [codebook]({{ '/data/rq3/taxonomy_codebook.csv' | relative_url }}) gives operational definitions and inclusion/exclusion boundaries.

## {% include rq_icon.html rq=2 %} RQ2: Training-data quality
{: #rq2-training-data-quality }

**Code attributes** comprise [Correctness](#papers-rq2_ca_cor), [Security](#papers-rq2_ca_sec), [Compliance](#papers-rq2_ca_com), [Robustness](#papers-rq2_ca_rob), [Maintainability](#papers-rq2_ca_mai), [Understandability](#papers-rq2_ca_und), and [Efficiency](#papers-rq2_ca_eff). They concern the code sample itself.

**Non-code and corpus attributes** comprise textual [Compliance and Security Risks](#papers-rq2_nc_csr), [Distribution Imbalance](#papers-rq2_nc_dis), [Redundancy](#papers-rq2_nc_red), [Inadequate Diversity](#papers-rq2_nc_div), [Data Contamination Risks](#papers-rq2_nc_con), and [Low-Value Data](#papers-rq2_nc_low). They concern surrounding content, supervision, composition, or training–evaluation overlap.

{% include research_figure.html src='/images/data_quality_issues.svg' height=980 alt='Thirteen training-data quality headings grouped into code attributes and non-code or corpus attributes' caption='RQ2 overview. Code-sample attributes are separated from text and corpus attributes.' %}

The [165 paper–heading memberships]({{ '/data/rq2_data_quality.csv' | relative_url }}) involve 78 papers. Distribution imbalance concerns relative frequency among represented strata; inadequate diversity concerns absent or effectively uncovered strata. Redundancy concerns repetition within training data; contamination concerns overlap with evaluation material.

## Supporting papers

{% assign rq1_ids = site.data.rq1_code_quality | map: 'study_id' %}
{% assign rq2_ids = site.data.rq2_data_quality | map: 'study_id' %}
{% assign taxonomy_ids = rq1_ids | concat: rq2_ids | uniq %}

Browse **{{ taxonomy_ids.size }} distinct papers** by quality category. Expand a category to see its supporting papers, or select a linked category above to open it directly. Membership is multi-label: a paper appears in every category it supports, so category counts should not be added to obtain a distinct-paper total. Stable study IDs link each entry to the complete [114-paper register]({{ '/data/included_studies.csv' | relative_url }}).

### RQ1 · Generated-code quality

{% assign code_categories = site.data.rq3.taxonomy_codebook | where: 'parent_id', 'RQ1_ROOT' %}
{% include supporting_papers.html categories=code_categories memberships=site.data.rq1_code_quality match_key='label' membership_key='category' id_key='node_id' label_key='label' context_key='operational_definition' %}

### RQ2 · Training-data quality

#### Code attributes

{% assign sample_categories = site.data.rq3.taxonomy_codebook | where: 'parent_id', 'RQ2_CA' %}
{% include supporting_papers.html categories=sample_categories memberships=site.data.rq2_data_quality match_key='label' membership_key='category' id_key='node_id' label_key='label' context_key='operational_definition' %}

#### Non-code and corpus attributes

{% assign corpus_categories = site.data.rq3.taxonomy_codebook | where: 'parent_id', 'RQ2_NC' %}
{% include supporting_papers.html categories=corpus_categories memberships=site.data.rq2_data_quality match_key='label' membership_key='category' id_key='node_id' label_key='label' context_key='operational_definition' %}
