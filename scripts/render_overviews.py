#!/usr/bin/env python3
"""Render English web-overview SVGs from the released final result tables."""
from __future__ import annotations

import csv
from collections import Counter, defaultdict
from html import escape
from pathlib import Path
import textwrap

ROOT = Path(__file__).resolve().parents[1]
IMAGES = ROOT / 'images'
FONT = 'DejaVu Sans, sans-serif'


def read(name):
    with (ROOT / 'data' / name).open(encoding='utf-8', newline='') as handle:
        return list(csv.DictReader(handle))


def text(x, y, label, size=18, fill='#334155', weight=400, family=FONT):
    return f'<text x="{x}" y="{y}" fill="{fill}" font-family="{family}" font-size="{size}" font-weight="{weight}">{escape(str(label))}</text>'


def multiline(x, y, label, width=68, size=17, fill='#475569', line_height=24):
    return ''.join(text(x, y + i * line_height, line, size, fill) for i, line in enumerate(textwrap.wrap(label, width=width)))


def rect(x, y, w, h, fill='#ffffff', stroke='#d9e2e8', radius=10):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}" fill="{fill}" stroke="{stroke}"/>'


def save(name, width, height, title, body, desc):
    svg = f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc"><title id="title">{escape(title)}</title><desc id="desc">{escape(desc)}</desc>{body}</svg>\n'
    (IMAGES / (name + '.svg')).write_text(svg, encoding='utf-8')


def heading(title, subtitle, width=1200):
    return rect(0, 0, width, 120, '#f7f9fa', '#f7f9fa', 0) + text(32, 48, title, 30, '#102d3b', 700) + text(32, 86, subtitle, 17, '#475569')


def code_taxonomy():
    nodes = [r for r in read('rq3/taxonomy_codebook.csv') if r['taxonomy'] == 'RQ1' and r['parent_id'] == 'RQ1_ROOT']
    counts = Counter(r['category'] for r in read('rq1_code_quality.csv'))
    assert len(nodes) == 8 and sum(counts.values()) == 195
    descriptions = {
        'Correctness': 'Syntax, logic, API, and dependency failures.',
        'Security': 'Weaknesses permitting exploitation or unsafe execution.',
        'Compliance': 'Licensing, privacy, harmful-content, and rights concerns.',
        'Robustness': 'Failures under abnormal inputs or runtime disruptions.',
        'Maintainability': 'Structure and coupling that impede modification.',
        'Understandability': 'Naming, comments, or expressions that obscure intent.',
        'Efficiency': 'Excessive runtime or memory for the required behavior.',
        'Generation Derailment': 'Repetition, truncation, verbosity, and instruction deviation.',
    }
    body = rect(0, 0, 1200, 770, '#f7f9fa', '#f7f9fa', 0)
    body += heading('Generated-code quality: eight dimensions', 'RQ1 / 195 paper–dimension memberships from 98 papers')
    for i, row in enumerate(nodes):
        x, y = 32 + (i % 2) * 584, 134 + (i // 2) * 143
        label = row['label']
        body += rect(x, y, 552, 125)
        body += text(x + 20, y + 35, label, 23, '#153e50', 700)
        body += text(x + 458, y + 35, str(counts[label]), 23, '#176b78', 700)
        body += multiline(x + 20, y + 70, descriptions[label], width=51)
    body += text(32, 742, 'Counts show supporting papers per dimension; papers can appear in several dimensions.', 16)
    save('generated_code_issues', 1200, 770, 'Generated-code quality dimensions', body, 'Eight final dimensions and their paper counts. Counts measure literature coverage, not defect prevalence.')


def data_taxonomy():
    nodes = [r for r in read('rq3/taxonomy_codebook.csv') if r['taxonomy'] == 'RQ2' and r['parent_id'] in {'RQ2_CA', 'RQ2_NC'}]
    counts = Counter(r['category'] for r in read('rq2_data_quality.csv'))
    category_map = {'RQ2_NC_CSR': 'Compliance and Security Risks (Textual)', 'RQ2_NC_DIS': 'Distribution Imbalance Issues', 'RQ2_NC_RED': 'Redundancy Issues', 'RQ2_NC_DIV': 'Inadequate Diversity', 'RQ2_NC_CON': 'Data Contamination Risks', 'RQ2_NC_LOW': 'Low-Value Data'}
    assert len(nodes) == 13 and sum(counts.values()) == 165
    body = rect(0, 0, 1200, 980, '#f7f9fa', '#f7f9fa', 0)
    body += heading('Training-data quality: thirteen headings', 'RQ2 / 165 paper–heading memberships from 78 papers')
    for col, (parent, label) in enumerate([('RQ2_CA', 'CODE ATTRIBUTES'), ('RQ2_NC', 'NON-CODE AND CORPUS ATTRIBUTES')]):
        x = 32 + col * 584
        color = '#176b78' if col == 0 else '#94501f'
        body += text(x, 148, label, 18, color, 700)
        for i, row in enumerate(r for r in nodes if r['parent_id'] == parent):
            y = 168 + i * 104
            key = category_map.get(row['node_id'], row['label'])
            assert key in counts, key
            body += rect(x, y, 552, 88)
            lines = textwrap.wrap(row['label'], 35)
            for j, line in enumerate(lines):
                body += text(x + 18, y + 33 + j * 25, line, 21, '#153e50', 600)
            body += text(x + 470, y + 36, counts[key], 23, color, 700)
    body += text(32, 935, 'Counts show supporting papers per heading; the operational codebook defines the boundaries.', 16)
    save('data_quality_issues', 1200, 980, 'Training-data quality headings', body, 'Seven code-attribute headings and six non-code/corpus headings. Multi-label counts measure literature coverage.')


def method_overview(scope, stem, title):
    groups = defaultdict(list)
    rows = [r for r in read('method_taxonomy.csv') if r['taxonomy_scope'] == scope]
    for row in rows:
        groups[row['method_path'].split(' > ')[0]].append(row)
    total_height = 165 + sum(72 + sum(34 + len(textwrap.wrap(r['method_leaf'], 84)) * 24 for r in items) for items in groups.values())
    body = rect(0, 0, 1200, total_height, '#f7f9fa', '#f7f9fa', 0)
    body += heading(title, 'Web overview / final manuscript method names and multi-label paper counts')
    y = 134
    for group, items in groups.items():
        h = 56 + sum(34 + len(textwrap.wrap(r['method_leaf'], 84)) * 24 for r in items)
        body += rect(32, y, 1136, h)
        body += text(54, y + 36, group, 22, '#153e50', 700)
        cy = y + 73
        for row in items:
            lines = textwrap.wrap(row['method_leaf'], 84)
            for j, line in enumerate(lines):
                body += text(64, cy + j * 24, line, 19)
            body += text(1050, cy, row['n_studies'], 21, '#176b78', 700)
            cy += 34 + len(lines) * 24
        y += h + 18
    body += text(32, total_height - 17, 'Numbers identify supporting papers, not effectiveness or complete issue coverage.', 16)
    save(stem, 1200, total_height, title, body, 'Method groups and paper counts from the final released method taxonomy. The accompanying CSV tables identify every membership.')


def main():
    IMAGES.mkdir(exist_ok=True)
    code_taxonomy()
    data_taxonomy()
    for args in [
        ('generated_code_detection', 'generated_code_issues_detection', 'Detecting generated-code quality issues'),
        ('training_data_detection', 'data_quality_issues_detection', 'Detecting training-data quality issues'),
        ('generated_code_mitigation', 'generated_code_issues_mitigation', 'Mitigating generated-code quality issues'),
        ('training_data_mitigation', 'data_quality_issues_mitigation', 'Mitigating training-data quality issues'),
    ]:
        method_overview(*args)
    print('Rendered six taxonomy and method SVGs from the final released tables. Hero PNGs are maintained separately.')


if __name__ == '__main__':
    main()
