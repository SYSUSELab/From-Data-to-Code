---
layout: default
title: Data and Reproducibility
nav_order: 6
has_children: true
permalink: /data/
description: "Compact final results, evidence links, quality scores, and reproducible figures for the review."
---

# Data and reproducibility

This package contains final results from the 114-paper major-revision synthesis. Stable `S001`–`S114` identifiers connect tables; `bib_key` identifies the manuscript's bibliography key, not its typeset reference number. Publication-status analyses are frozen at **2026-08-29**.

## Start here

| File | Rows | Content |
|:---|---:|:---|
| [included_studies.csv](included_studies.csv) | 114 | Stable IDs, titles, links, included-copy dates/venues, and consensus scores |
| [quality_scores_for_included_papers.csv](quality_scores_for_included_papers.csv) | 114 | Final consensus quality totals, 10–16 |
| [rater_scores.csv](rater_scores.csv) | 134 | Three independent pre-consensus totals per quality-assessment candidate |
| [search_summary.csv](search_summary.csv) | 13 | Database counts, selection totals, and search/snowballing scope |
| [rq1_code_quality.csv](rq1_code_quality.csv) | 195 | Paper–dimension memberships across eight generated-code dimensions |
| [rq2_data_quality.csv](rq2_data_quality.csv) | 165 | Paper–heading memberships across thirteen training-data headings |
| [method_taxonomy.csv](method_taxonomy.csv) | 32 | Final RQ4/RQ5 method leaves, hierarchy paths, and study counts |
| [method_assignments.csv](method_assignments.csv) | 249 | Paper–method memberships linked by `method_id` |
| [automation_examples.csv](automation_examples.csv) | 21 | Direct detection/mitigation exemplars, primary-source links, locators, and limits |
| [rq3/](rq3/) | 101 assignments | Final relationship evidence and graph tables |
| [sensitivity/](sensitivity/) | 114 status records | Publication and author-overlap results, dependence checks, and replacement exemplars |

The independent rating totals are included to reproduce the reported interval alpha of 0.717. Consensus totals reflect subsequent discussion. These are total scores on the 0–16 rubric; criterion-level scores are not present. The threshold of 10 was set after initial scoring and serves minimum-quality screening.

The paper register preserves included-copy metadata, with one documented correction: S008 has its DOI and May 2022 publication date restored from the included ACM paper. Its two RQ1 temporal labels are corrected consistently; category memberships and counts are unchanged. See `provenance.json`. Use `sensitivity/publication_status.csv` for the independently audited publication snapshot; later publication does not change the paper's stable ID or silently replace the evaluated copy.

## Evidence and counting

RQ1, RQ2, and method memberships are multi-label: one paper can contribute to several categories. RQ3 has a different unit: a unique paper–family–source–outcome assignment. Its **101 assignments from 67 papers** link to **105 used evidence records through 107 links**. Detailed definitions and counting rules appear in the [RQ3 guide](rq3/).

An automation row establishes one detection example and one mitigation example for a broad heading. They need not concern the same subtype. The 8/8 and 13/13 results are existence tests, not exhaustive subtype coverage or effectiveness estimates.

Primary-paper links and reported pages/sections are retained. Some locators also record line ranges in the extracted text used during the source audit. Those line numbers identify that source extraction and are not links to bundled files; this release contains no third-party paper PDFs or text copies.

## Reproduction

From the repository root:

```bash
python3 scripts/validate_release.py
python3 scripts/render_sankey.py --no-static-export
python3 scripts/render_sankey_panels.py --no-static-export
python3 scripts/check_english.py
```

The data validator uses the Python standard library. The language check additionally uses PyMuPDF for PDF text. See [the script guide](https://github.com/SYSUSELab/From-Data-to-Code/blob/main/scripts/README.md) for optional static figure export and site preview.

[validation_report.md](validation_report.md) records the arithmetic and structural checks. [checksums.json](checksums.json) fixes the delivered CSV/JSON bytes. [provenance.json](provenance.json) identifies the source revision, source hashes, and release transformations. The validation report is an integrity check, not a re-evaluation of each paper's empirical claims.

The result package excludes raw retrieval exports, intermediate candidate mappings, batch adjudication work, API response snapshots, reviewer correspondence, and the full-text paper collection.
