---
layout: default
title: Sensitivity Analyses
parent: Data and Reproducibility
nav_order: 2
permalink: /data/sensitivity/
---

# Publication and author-overlap sensitivity

This is a **2026-08-29 publication-status snapshot** for the 114 included papers. It does not reconstruct status at inclusion: per-paper inclusion/acceptance dates are unavailable. Coding is filtered from the included copies rather than fully re-extracted from every version of record.

## Released results

| File | Rows | Content |
|:---|---:|:---|
| [publication_status.csv](publication_status.csv) | 114 | Verified status, public evidence URLs, overlap identities, and adjudication notes |
| [claim_dependency.csv](claim_dependency.csv) | 44 | Review-level and local claim changes under removal scenarios |
| [method_leaf_sensitivity.csv](method_leaf_sensitivity.csv) | 32 | Method-leaf support under reviewed-only and archival-only definitions |
| [peer_reviewed_automation_replacements.csv](peer_reviewed_automation_replacements.csv) | 10 | Targeted replacement exemplars with direct source links and scope limits |
| [summary.json](summary.json) | — | Compact frozen counts, definitions, and limitations |

The status classification contains 74 formal archival publications, three accepted non-archival workshop papers, 22 preprint-only papers, 14 technical/model reports, and one unconfirmed formal-successor link. Of the workshops, two have verified peer review; the third has an unclear review process. S074's possible formal successor remains unconfirmed.

## Main comparisons

The primary reviewed-only scenario retains **76 papers**: 74 verified archival publications and two reviewed workshops. The archival-only boundary retains **74**. Both retain the eight RQ1 dimensions, 13 RQ2 headings, 12 RQ3 families, Correctness dominance, and all high-level detection/mitigation families. Fine-grained support changes: only 28 of 32 detailed method leaves remain. A targeted full-text audit supplies reviewed automation exemplars for affected broad headings.

An author-overlapping paper has at least one author who is also a manuscript author after identity disambiguation. **18/114 papers (15.8%)** meet the definition: 11 formal publications and seven currently preprint-only papers. Removing the seven leaves **94 RQ3 assignments from 62 papers**, all 12 families, Correctness at **58/94 (61.7%)**, and the same four leading families at **64/94 (68.1%)**.

Local findings are sensitive: one redundancy-to-derailment branch loses all support, and the small Clarity family loses its primary experiment. The original one-exemplar generated-code automation crosswalk drops from 8/8 to 6/8 under that removal; targeted non-overlapping reviewed replacements restore narrow broad-heading existence. The replacement table does not establish exhaustive subtype coverage or deployment maturity.

A separate upper-bound check removes all 18 overlapping papers, including 11 currently formally published papers. It is a deliberately broader removal scenario. “Mainly dependent” means strictly more than 50% of direct support is lost; exactly 50% is a boundary. “Pivotal” identifies exact, ranking, or evidence-type statements that fail even if a majority of support remains. Consult the claim-level rows rather than interpreting preserved high-level structures as unchanged fine-grained evidence.
