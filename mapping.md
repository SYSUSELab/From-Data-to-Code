---
layout: default
title: Data-to-Code Relationships
description: "Twelve relationship families, 101 paper-level assignments, and traceable evidence from 67 papers."
nav_order: 3
---

# {% include rq_icon.html rq=3 %} RQ3: Data-to-code relationships
{: #rq3-data-to-code-relationships }

We synthesize **12 recurring relationship families** between training-data conditions and observable generated-code outcomes. Evidence includes controlled interventions, corpus audits, output probes, cross-model comparisons, reviews, and authors' interpretations. Family definitions preserve these differences and their limitations.

## Read the relationship graph

<div class="figure-block">
  <div class="figure-frame"><a href="{{ '/images/sankey.pdf' | relative_url }}"><img src="{{ '/images/sankey.png' | relative_url }}" alt="Thirteen training-data headings connect through twelve relationship families to eight generated-code dimensions. The graph summarizes 101 assignments from 67 papers; correctness receives 61 assignments." width="1100" loading="lazy" decoding="async"></a></div>
  <p class="figure-caption">The manuscript graph. Width represents literature coverage. All percentages use 101 assignments as the denominator.</p>
</div>

[Explore the interactive graph]({{ '/figures/rq3/sankey.html' | relative_url }}) · [Download the manuscript figure (PDF)]({{ '/images/sankey.pdf' | relative_url }}) · [Read the data guide]({{ '/data/rq3/' | relative_url }})

One assignment is a unique **(paper, relationship family, RQ2 source, RQ1 outcome)** combination. Repeated passages supporting the same combination count once. A paper can contribute several assignments when the relationships differ. The graph contains **101 assignments from 67 papers**, linked to **105 evidence records through 107 normalized evidence links**. Width is not an effect-size or causal-strength estimate.

## Relationship families

| Family | Assignments | Share | Papers |
|:---|---:|---:|---:|
{% for row in site.data.rq3.mapping_summary %}| {{ row.mapping_id }}: {{ row.mapping_label }} | {{ row.n_path_assignments }} | {{ row.percentage_of_path_assignments }}% | {{ row.n_distinct_studies }} |
{% endfor %}

See the [operational definitions]({{ '/data/rq3/mapping_definitions.csv' | relative_url }}) for routing rules and boundaries, and the [assignment table]({{ '/data/rq3/study_mapping_assignments.csv' | relative_url }}) for individual paths. Rounded shares can sum to 99.99%.

## What the distribution supports

Correctness accounts for **61/101 assignments (60.4%)**. Underexposure, prevalence skew, defect carryover, and supervision-signal quality together account for **68/101 (67.3%)**. These concentrations describe the literature's attention. Robustness, Maintainability, and Understandability together receive six assignments.

The evidence supports examining example quality, input–target alignment, and coverage against deployment requirements. Interpretation remains study-specific: bundled cleaning may not isolate an individual filter's effect, hidden corpora limit attribution, and observed associations can have several explanations. The [evidence table]({{ '/data/rq3/relationship_evidence.csv' | relative_url }}) and [path links]({{ '/data/rq3/path_evidence_links.csv' | relative_url }}) retain source locations and qualifiers.

## Supporting papers

{% assign mapping_ids = site.data.rq3.study_mapping_assignments | map: 'study_id' | uniq %}
{% include study_list.html study_ids=mapping_ids %}
