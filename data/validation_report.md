# Release validation

All checks passed using `python3 scripts/validate_release.py`.

| Check | Result |
|:---|:---|
| Included papers and consensus scores | 114; threshold 10/16 |
| Independent total scores | 134 candidates; three raters; interval alpha 0.717134 |
| RQ1 / RQ2 memberships | 195 / 165; 8 / 13 headings |
| Final RQ3 graph | 101 unique assignments; 67 papers; 12 families |
| Used evidence and normalized links | 105 / 107 |
| Atomic branches / combined nodes / edges | 25 / 33 / 37 |
| Split panels | 27 nodes / 27 edges; 20 nodes / 23 edges; matching family geometry |
| Flow conservation | 101 per layer; matching inflow and outflow |
| RQ4 / RQ5 method taxonomy | 32 leaves; 249 paper memberships |
| Automation existence crosswalk | 21 rows; 8 code / 13 data headings |
| Publication snapshot | 2026-08-29; 76 verified reviewed / 74 archival papers |
| Author-overlap sensitivity | 18 overlapping papers; removing 7 preprints leaves 94 assignments |
| Source identities, links, and data checksums | Passed |

The checks establish structural and arithmetic consistency. They do not establish the correctness of every substantive interpretation or external paper claim.
