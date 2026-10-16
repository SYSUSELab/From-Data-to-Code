#!/usr/bin/env python3
"""Check the public result package without access to the revision workspace."""
from __future__ import annotations

import csv
import hashlib
import json
from collections import Counter, defaultdict
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'data'


def read(name):
    with (DATA / name).open(encoding='utf-8', newline='') as handle:
        reader = csv.DictReader(handle)
        assert reader.fieldnames and len(reader.fieldnames) == len(set(reader.fieldnames)), name
        rows = list(reader)
        assert all(None not in row and None not in row.values() for row in rows), name
        return rows


def ids(value):
    return {part.strip() for part in value.split(';') if part.strip()}


def unique(rows, field):
    result = {row[field]: row for row in rows}
    assert len(result) == len(rows), f'Duplicate {field}'
    return result


def percent(count, denominator=101):
    return str((Decimal(count) * 100 / denominator).quantize(Decimal('.01'), rounding=ROUND_HALF_UP))


def main():
    studies = unique(read('included_studies.csv'), 'study_id')
    assert len(studies) == 114
    assert len({r['bib_key'] for r in studies.values()}) == 114
    scores = read('quality_scores_for_included_papers.csv')
    scores_by_title = {r['Paper']: int(r['Quality Score (Consensus After Discussion)']) for r in scores}
    assert len(scores) == len(scores_by_title) == 114
    assert {r['title'] for r in studies.values()} == set(scores_by_title)
    assert all(10 <= score <= 16 for score in scores_by_title.values())
    assert all(int(r['consensus_quality_score']) == scores_by_title[r['title']] for r in studies.values())
    assert Counter(scores_by_title.values()) == {10: 23, 11: 6, 12: 47, 13: 7, 14: 20, 15: 1, 16: 10}
    raters = read('rater_scores.csv')
    assert len(raters) == len({r['Title'] for r in raters}) == 134
    triples = [[int(r[key]) for key in ('Rater1', 'Rater2', 'Rater3')] for r in raters]
    assert all(0 <= value <= 16 for triple in triples for value in triple)
    observed = sum((a - b) ** 2 for triple in triples for i, a in enumerate(triple) for j, b in enumerate(triple) if i != j) / (len(triples) * 6)
    flattened = [v for triple in triples for v in triple]
    expected = sum((a - b) ** 2 for a in flattened for b in flattened) / (len(flattened) * (len(flattened) - 1))
    alpha = 1 - observed / expected
    assert round(alpha, 3) == .717, alpha
    search = read('search_summary.csv')
    stages = {r['stage']: int(r['records']) for r in search if r['stage'] != 'database_search'}
    assert sum(int(r['records']) for r in search if r['stage'] == 'database_search') == stages['retrieved_total'] == 2298
    assert stages['retrieved_total'] - stages['duplicates_removed'] == stages['unique_records'] == 2114
    assert stages['eligible_after_screening'] + stages['snowballing_added'] == stages['quality_assessment_candidates'] == 134
    assert stages['quality_assessment_candidates'] - stages['excluded_by_quality_threshold'] == stages['included_papers'] == 114
    for name, expected_rows, expected_categories in [('rq1_code_quality.csv', 195, 8), ('rq2_data_quality.csv', 165, 13)]:
        rows = read(name)
        assert len(rows) == expected_rows
        assert len({r['category'] for r in rows}) == expected_categories
        assert len({(r['study_id'], r['category']) for r in rows}) == len(rows)
        assert all(r['study_id'] in studies and r['bib_key'] == studies[r['study_id']]['bib_key'] for r in rows)

    assignments = unique(read('rq3/study_mapping_assignments.csv'), 'path_assignment_id')
    definitions = unique(read('rq3/mapping_definitions.csv'), 'mapping_id')
    taxonomy = unique(read('rq3/taxonomy_codebook.csv'), 'node_id')
    evidence = unique(read('rq3/relationship_evidence.csv'), 'evidence_id')
    links = read('rq3/path_evidence_links.csv')
    summaries = unique(read('rq3/mapping_summary.csv'), 'mapping_id')
    assert len(assignments) == 101 and len(definitions) == 12 and len(taxonomy) == 25
    assert len(evidence) == 105 and len(links) == 107
    assert len({r['study_id'] for r in assignments.values()}) == 67
    fact_keys = {(r['study_id'], r['mapping_id'], r['rq2_source_id'], r['rq1_target_id']) for r in assignments.values()}
    assert len(fact_keys) == 101
    linked = defaultdict(set)
    assert len({(r['path_assignment_id'], r['evidence_id']) for r in links}) == 107
    for link in links:
        fact = assignments[link['path_assignment_id']]
        ev = evidence[link['evidence_id']]
        assert all(link[key] == fact[key] for key in ('study_id', 'mapping_id', 'rq2_source_id', 'rq1_target_id'))
        assert ev['study_id'] == fact['study_id']
        assert link['source_evidence_id'] == ev['source_evidence_id']
        assert link['relation_subtype_id'] in ids(fact['relation_subtype_ids'])
        linked[link['path_assignment_id']].add(link['evidence_id'])
    assert set(evidence) == {r['evidence_id'] for r in links}
    for pid, fact in assignments.items():
        assert fact['study_id'] in studies and fact['bib_key'] == studies[fact['study_id']]['bib_key']
        assert fact['mapping_id'] in definitions
        assert fact['rq2_source_id'] in taxonomy and fact['rq1_target_id'] in taxonomy
        assert linked[pid] == ids(fact['supporting_evidence_ids'])
    for mid, summary in summaries.items():
        facts = {pid: r for pid, r in assignments.items() if r['mapping_id'] == mid}
        supporting_evidence = set().union(*(linked[pid] for pid in facts))
        assert int(summary['n_path_assignments']) == len(facts)
        assert summary['percentage_of_path_assignments'] == percent(len(facts))
        assert int(summary['assignment_denominator']) == 101
        assert ids(summary['supporting_study_ids']) == {r['study_id'] for r in facts.values()}
        assert int(summary['n_distinct_studies']) == len(ids(summary['supporting_study_ids']))
        assert ids(summary['supporting_evidence_ids']) == supporting_evidence
        assert int(summary['n_distinct_evidence_rows']) == len(supporting_evidence)
        assert int(summary['n_evidence_links']) == sum(r['mapping_id'] == mid for r in links)
    screening = unique(read('rq3/study_screening.csv'), 'study_id')
    assert set(screening) == set(studies)
    for sid, row in screening.items():
        n = sum(r['study_id'] == sid for r in assignments.values())
        assert int(row['n_final_assignments']) == n
        assert row['final_graph_status'] == ('contributes_final_assignment' if n else 'no_final_assignment')

    branches = read('rq3/sankey_atomic_branches.csv')
    assert len(branches) == 25 and sum(int(r['value']) for r in branches) == 101
    for branch in branches:
        expected_paths = {pid for pid, r in assignments.items() if all(r[k] == branch[k] for k in ('mapping_id', 'rq2_source_id', 'rq1_target_id'))}
        assert ids(branch['supporting_path_assignment_ids']) == expected_paths
        assert int(branch['value']) == len(expected_paths)

    for stem, n_nodes, n_edges in [('sankey', 33, 37), ('sankey_left', 27, 27), ('sankey_right', 20, 23)]:
        nodes = unique(read(f'rq3/{stem}_nodes.csv'), 'node_id')
        edges = read(f'rq3/{stem}_edges.csv')
        assert len(nodes) == n_nodes and len(edges) == n_edges
        incoming, outgoing = Counter(), Counter()
        layers = Counter()
        for edge in edges:
            assert edge['source_node_id'] in nodes and edge['target_node_id'] in nodes
            value = int(edge['value'])
            assert value > 0 and int(edge['assignment_denominator']) == 101
            assert edge['percentage_of_path_assignments'] == percent(value)
            path_ids = ids(edge['supporting_path_assignment_ids'])
            assert len(path_ids) == value and path_ids <= set(assignments)
            source = nodes[edge['source_node_id']]
            target = nodes[edge['target_node_id']]
            for pid in path_ids:
                fact = assignments[pid]
                for node in (source, target):
                    logical = node['logical_id']
                    expected_logical = fact['mapping_id'] if logical.startswith('F') else fact['rq1_target_id'] if logical.startswith('RQ1_') else taxonomy[fact['rq2_source_id']]['parent_id'] if logical in {'RQ2_CA', 'RQ2_NC'} else fact['rq2_source_id']
                    assert logical == expected_logical, (stem, pid, logical)
            incoming[edge['target_node_id']] += value
            outgoing[edge['source_node_id']] += value
            layers[edge['edge_layer']] += value
        assert all(total == 101 for total in layers.values())
        for nid, node in nodes.items():
            n = int(node['n_path_assignments'])
            assert node['percentage_of_path_assignments'] == percent(n)
            if nid in incoming:
                assert incoming[nid] == n
            if nid in outgoing:
                assert outgoing[nid] == n
            if nid in incoming and nid in outgoing:
                assert incoming[nid] == outgoing[nid]
    alignment = unique(read('rq3/mapping_panel_alignment.csv'), 'mapping_id')
    arrows = unique(read('rq3/mapping_arrow_labels.csv'), 'mapping_id')
    assert set(alignment) == set(arrows) == set(definitions)
    for side in ('left', 'right'):
        nodes = read(f'rq3/sankey_{side}_nodes.csv')
        for mid, row in alignment.items():
            node = next(r for r in nodes if r['logical_id'] == mid)
            assert all(node[k] == row[k] for k in ('y_top', 'y_center', 'node_height', 'n_path_assignments', 'percentage_of_path_assignments'))

    methods = unique(read('method_taxonomy.csv'), 'method_id')
    memberships = read('method_assignments.csv')
    assert len(methods) == 32 and len(memberships) == 249
    assert len({(r['study_id'], r['method_id']) for r in memberships}) == 249
    for row in memberships:
        assert row['study_id'] in studies and row['method_id'] in methods
        assert row['taxonomy_scope'] == methods[row['method_id']]['taxonomy_scope']
    assert all(int(m['n_studies']) == sum(r['method_id'] == mid for r in memberships) for mid, m in methods.items())
    audit_methods = read('sensitivity/method_leaf_sensitivity.csv')
    for row in audit_methods:
        method = next(m for m in methods.values() if m['taxonomy_scope'] == row['taxonomy_scope'] and m['method_leaf'] == row['method_leaf'])
        assert int(row['baseline_study_count']) == int(method['n_studies'])
        assert ids(row['baseline_study_ids']) == {r['study_id'] for r in memberships if r['method_id'] == method['method_id']}
    automation = read('automation_examples.csv')
    assert len(automation) == len({(r['layer'], r['issue']) for r in automation}) == 21
    assert Counter(r['layer'] for r in automation) == {'Generated code': 8, 'Training data': 13}
    for row in automation + read('sensitivity/peer_reviewed_automation_replacements.csv'):
        for phase in ('detection', 'mitigation'):
            study = studies[row[f'{phase}_study_id']]
            assert row[f'{phase}_study_key'] == study['bib_key']
            assert row[f'{phase}_source_url'] == study['url']
            assert row[f'{phase}_evidence_location'] and row['scope_limit']
    status = unique(read('sensitivity/publication_status.csv'), 'study_id')
    assert set(status) == set(studies)
    assert {r['status_as_of'] for r in status.values()} == {'2026-08-29'}
    assert sum(r['author_overlap'] == 'yes' for r in status.values()) == 18
    assert sum(r['peer_review_current'] in {'peer_reviewed', 'workshop_reviewed'} for r in status.values()) == 76
    assert sum(r['status_current'] == 'formally_published' for r in status.values()) == 74
    removed = {sid for sid, r in status.items() if r['overlap_current_non_peer_reviewed'] == 'yes'}
    assert len(removed) == 7
    retained = [r for r in assignments.values() if r['study_id'] not in removed]
    assert len(retained) == 94 and len({r['mapping_id'] for r in retained}) == 12
    assert sum(r['rq1_target_id'] == 'RQ1_COR' for r in retained) == 58

    published_files = sorted(p for p in DATA.rglob('*') if p.is_file() and p.suffix in {'.csv', '.json'} and p.name != 'checksums.json')
    hashes = {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest() for p in published_files}
    checksum_path = DATA / 'checksums.json'
    if checksum_path.exists():
        assert json.loads(checksum_path.read_text()) == hashes, 'Released data checksum mismatch'
    lines = [
        '# Release validation', '',
        'All checks passed using `python3 scripts/validate_release.py`.', '',
        '| Check | Result |', '|:---|:---|',
        '| Included papers and consensus scores | 114; threshold 10/16 |',
        f'| Independent total scores | 134 candidates; three raters; interval alpha {alpha:.6f} |',
        '| RQ1 / RQ2 memberships | 195 / 165; 8 / 13 headings |',
        '| Final RQ3 graph | 101 unique assignments; 67 papers; 12 families |',
        '| Used evidence and normalized links | 105 / 107 |',
        '| Atomic branches / combined nodes / edges | 25 / 33 / 37 |',
        '| Split panels | 27 nodes / 27 edges; 20 nodes / 23 edges; matching family geometry |',
        '| Flow conservation | 101 per layer; matching inflow and outflow |',
        '| RQ4 / RQ5 method taxonomy | 32 leaves; 249 paper memberships |',
        '| Automation existence crosswalk | 21 rows; 8 code / 13 data headings |',
        '| Publication snapshot | 2026-08-29; 76 verified reviewed / 74 archival papers |',
        '| Author-overlap sensitivity | 18 overlapping papers; removing 7 preprints leaves 94 assignments |',
        '| Source identities, links, and data checksums | Passed |', '',
        'The checks establish structural and arithmetic consistency. They do not establish the correctness of every substantive interpretation or external paper claim.', '',
    ]
    (DATA / 'validation_report.md').write_text('\n'.join(lines), encoding='utf-8')
    print(f'Validated 114 papers, 101 assignments, 105 evidence rows, 107 links; interval alpha={alpha:.6f}.')


if __name__ == '__main__':
    main()
