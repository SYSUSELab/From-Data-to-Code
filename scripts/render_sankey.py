#!/usr/bin/env python3
"""Render the validated RQ3 Sankey data as SVG, HTML, PDF, and PNG.

The SVG and self-contained HTML use only the Python standard library.  Static
PDF/PNG export is delegated to the optional Python Playwright and
Chromium through ``scripts/export_figure.py``.  No counts are embedded in this file: all
node and band values come from ``sankey_nodes.csv`` and ``sankey_edges.csv``.
"""

from __future__ import annotations

import argparse
import csv
import html
import os
import re
import shutil
import subprocess
import sys
import xml.etree.ElementTree as ET
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1] / "data" / "rq3"
OUTPUT = Path(__file__).resolve().parents[1] / "figures" / "rq3"
WIDTH = 2050
HEIGHT = 1370
PRINT_WIDTH_IN = 7.43
PRINT_HEIGHT_IN = PRINT_WIDTH_IN * HEIGHT / WIDTH
CHART_TOP = 180.0
CHART_BOTTOM = 1260.0
CHART_HEIGHT = CHART_BOTTOM - CHART_TOP
NODE_WIDTH = 18.0
NODE_GAP = 39.0
LAYER_X = {
    "rq2_source": 460.0,
    "mapping_family": 1070.0,
    "rq1_target": 1665.0,
}

STATIC_LABELS = {
    "RQ2_NC_DIS": "Distribution imbalance",
    "RQ2_NC_RED": "Redundancy",
    "RQ2_NC_DIV": "Inadequate diversity",
    "RQ2_NC_CON": "Contamination",
    "RQ2_NC_LOW": "Low-value data",
    "RQ1_DER": "Generation derailment",
}


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def xml(value: object) -> str:
    return html.escape(str(value), quote=True)


def fmt(value: float) -> str:
    return f"{value:.2f}".rstrip("0").rstrip(".")


def split_ids(value: str) -> list[str]:
    return [item.strip() for item in value.split(";") if item.strip()]


def display_percentage(value: str) -> str:
    return f"{float(value):.1f}%"


def static_label(node: dict[str, str]) -> str:
    return STATIC_LABELS.get(node["logical_id"], node["short_label"])


def layout_nodes(nodes: list[dict[str, str]]) -> dict[str, dict[str, float]]:
    layers: dict[str, list[dict[str, str]]] = defaultdict(list)
    for node in nodes:
        layers[node["layer"]].append(node)
    for rows in layers.values():
        rows.sort(key=lambda row: int(row["display_order"]))

    assert set(layers) == {"rq2_source", "mapping_family", "rq1_target"}
    denominators = {int(row["assignment_denominator"]) for row in nodes}
    assert denominators == {101}
    denominator = denominators.pop()
    assert sum(int(row["n_path_assignments"]) for row in layers["rq2_source"]) == denominator
    assert sum(int(row["n_path_assignments"]) for row in layers["mapping_family"]) == denominator
    assert sum(int(row["n_path_assignments"]) for row in layers["rq1_target"]) == denominator

    max_nodes = max(len(rows) for rows in layers.values())
    unit = (CHART_HEIGHT - NODE_GAP * (max_nodes - 1)) / denominator
    assert unit > 0

    result: dict[str, dict[str, float]] = {}
    for layer, rows in layers.items():
        occupied = denominator * unit + NODE_GAP * (len(rows) - 1)
        cursor = CHART_TOP + (CHART_HEIGHT - occupied) / 2.0
        for row in rows:
            height = int(row["n_path_assignments"]) * unit
            result[row["node_id"]] = {
                "x": LAYER_X[layer],
                "y": cursor,
                "height": height,
                "unit": unit,
            }
            cursor += height + NODE_GAP
    return result


def node_tooltip(node: dict[str, str]) -> str:
    layer_names = {
        "rq2_source": "RQ2 training-data quality leaf",
        "mapping_family": "RQ3 mapping family",
        "rq1_target": "RQ1 generated-code quality dimension",
    }
    return "\n".join([
        f'{layer_names[node["layer"]]}: {node["label"]}',
        f'Share of path assignments: {display_percentage(node["percentage_of_path_assignments"])}',
        f'Distinct studies: {node["n_distinct_studies"]}',
        node["description"],
    ])


def edge_tooltip(
    edge: dict[str, str], node_by_id: dict[str, dict[str, str]]
) -> str:
    source = node_by_id[edge["source_node_id"]]
    target = node_by_id[edge["target_node_id"]]
    study_ids = edge["supporting_study_ids"]
    evidence_ids = edge["supporting_source_evidence_ids"]
    return "\n".join([
        f'{source["label"]} → {target["label"]}',
        f'Share of path assignments: {display_percentage(edge["percentage_of_path_assignments"])}',
        f'Distinct studies: {edge["n_distinct_studies"]}',
        f'Distinct evidence rows: {edge["n_distinct_evidence_rows"]}',
        f'Studies: {study_ids}',
        f'Evidence: {evidence_ids}',
    ])


def link_paths(
    edges: list[dict[str, str]], positions: dict[str, dict[str, float]]
) -> list[tuple[dict[str, str], str]]:
    outgoing_offset = {node_id: position["y"] for node_id, position in positions.items()}
    incoming_offset = {node_id: position["y"] for node_id, position in positions.items()}
    result: list[tuple[dict[str, str], str]] = []

    # The CSV is already ordered so that segments follow the explicit node order
    # at both ends.  Separate offset maps preserve the mapping-node inflow and
    # outflow partitions independently.
    for edge in edges:
        source_id = edge["source_node_id"]
        target_id = edge["target_node_id"]
        source = positions[source_id]
        target = positions[target_id]
        thickness = int(edge["value"]) * source["unit"]
        assert abs(source["unit"] - target["unit"]) < 1e-9

        x0 = source["x"] + NODE_WIDTH
        x1 = target["x"]
        y0_top = outgoing_offset[source_id]
        y1_top = incoming_offset[target_id]
        y0_bottom = y0_top + thickness
        y1_bottom = y1_top + thickness
        bend = (x1 - x0) * 0.47
        path = (
            f"M {fmt(x0)} {fmt(y0_top)} "
            f"C {fmt(x0 + bend)} {fmt(y0_top)}, {fmt(x1 - bend)} {fmt(y1_top)}, {fmt(x1)} {fmt(y1_top)} "
            f"L {fmt(x1)} {fmt(y1_bottom)} "
            f"C {fmt(x1 - bend)} {fmt(y1_bottom)}, {fmt(x0 + bend)} {fmt(y0_bottom)}, {fmt(x0)} {fmt(y0_bottom)} Z"
        )
        result.append((edge, path))
        outgoing_offset[source_id] = y0_bottom
        incoming_offset[target_id] = y1_bottom

    for node_id, position in positions.items():
        if node_id.startswith("rq2:"):
            assert abs(outgoing_offset[node_id] - (position["y"] + position["height"])) < 1e-6
        elif node_id.startswith("mapping:"):
            assert abs(incoming_offset[node_id] - (position["y"] + position["height"])) < 1e-6
            assert abs(outgoing_offset[node_id] - (position["y"] + position["height"])) < 1e-6
        else:
            assert abs(incoming_offset[node_id] - (position["y"] + position["height"])) < 1e-6
    return result


def legend_svg() -> str:
    return """
  <g class="legend" aria-label="Color legend">
    <rect x="90" y="1305" width="18" height="18" rx="3" fill="#4C78A8"/>
    <text x="118" y="1321">RQ2 code-attribute leaf</text>
    <rect x="460" y="1305" width="18" height="18" rx="3" fill="#F28E2B"/>
    <text x="488" y="1321">RQ2 non-code/corpus leaf</text>
    <rect x="865" y="1305" width="18" height="18" rx="3" fill="#7B8792"/>
    <text x="893" y="1321">Band color identifies mapping family</text>
    <rect x="1395" y="1305" width="18" height="18" rx="3" fill="#5F6B76"/>
    <text x="1423" y="1321">RQ1 generated-code dimension</text>
  </g>
  <text class="footnote" x="1025" y="1353" text-anchor="middle">Band widths and percentages use path assignments; one study may support multiple paths.</text>
"""


def build_svg(
    nodes: list[dict[str, str]], edges: list[dict[str, str]]
) -> str:
    node_by_id = {row["node_id"]: row for row in nodes}
    assert len(node_by_id) == len(nodes) == 33
    positions = layout_nodes(nodes)
    paths = link_paths(edges, positions)

    parts = [f"""<svg id="sankey-svg" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 {WIDTH} {HEIGHT}" width="{WIDTH}" height="{HEIGHT}" role="img" aria-labelledby="figure-title figure-desc">
  <title id="figure-title">RQ3 training-data to generated-code quality Sankey diagram</title>
  <desc id="figure-desc">Study-family-source-target path assignments connect twelve observed RQ2 training-data quality leaves through twelve mapping families to eight RQ1 generated-code quality dimensions.</desc>
  <style>
    :root {{ color-scheme: light; }}
    text {{ font-family: "Liberation Sans", Arial, sans-serif; fill: #20262d; }}
    .title {{ font-size: 39px; font-weight: 700; }}
    .subtitle {{ font-size: 26px; fill: #56616c; }}
    .column-heading {{ font-size: 27px; font-weight: 700; letter-spacing: 1.1px; fill: #3e4852; }}
    .column-rule {{ stroke: #cfd5da; stroke-width: 1.5; }}
    .sankey-link {{ transition: opacity 120ms ease; cursor: pointer; }}
    .sankey-node {{ cursor: pointer; }}
    .node-label {{ font-size: 29px; font-weight: 600; }}
    .mapping-label {{ font-size: 28px; font-weight: 700; }}
    .long-target-label {{ font-size: 25px; }}
    .legend text {{ font-size: 25px; fill: #45515c; }}
    .footnote {{ font-size: 23px; fill: #59646e; }}
    .sankey-link.is-dimmed, .sankey-node.is-dimmed, .node-label.is-dimmed {{ opacity: 0.10 !important; }}
    .sankey-link.is-highlighted {{ opacity: 0.86 !important; stroke: rgba(30,35,40,0.28); stroke-width: 1.2; }}
    .sankey-node.is-highlighted {{ stroke: #17212b; stroke-width: 3; }}
  </style>
  <rect width="{WIDTH}" height="{HEIGHT}" fill="#ffffff"/>
  <text class="title" x="1025" y="48" text-anchor="middle">Training-data quality and generated-code quality relationships</text>
  <text class="subtitle" x="1025" y="84" text-anchor="middle">Band widths and percentages show literature coverage; one study may support multiple paths</text>
  <text class="column-heading" x="460" y="137" text-anchor="end">RQ2 DATA-QUALITY LEAF</text>
  <text class="column-heading" x="1079" y="137" text-anchor="start">MAPPING FAMILY</text>
  <text class="column-heading" x="1990" y="137" text-anchor="end">RQ1 GENERATED-CODE QUALITY</text>
  <line class="column-rule" x1="90" y1="153" x2="478" y2="153"/>
  <line class="column-rule" x1="1070" y1="153" x2="1460" y2="153"/>
  <line class="column-rule" x1="1665" y1="153" x2="1990" y2="153"/>
  <g class="links" aria-label="Sankey bands">"""]

    for edge, path in paths:
        tooltip = edge_tooltip(edge, node_by_id)
        parts.append(
            f'<path id="edge-{xml(edge["edge_id"])}" class="sankey-link" '
            f'd="{path}" fill="{xml(edge["color"])}" '
            f'data-tooltip="{xml(tooltip)}" data-mapping="{xml(edge["mapping_id"])}" '
            f'data-source-logical="{xml(edge["source_logical_id"])}" '
            f'data-target-logical="{xml(edge["target_logical_id"])}">'
            f'<title>{xml(tooltip)}</title></path>'
        )
    parts.append("  </g>\n  <g class=\"nodes\" aria-label=\"Sankey nodes\">")

    for node in nodes:
        position = positions[node["node_id"]]
        tooltip = node_tooltip(node)
        parts.append(
            f'<rect id="node-{xml(node["node_id"].replace(":", "-"))}" '
            f'class="sankey-node" x="{fmt(position["x"])}" y="{fmt(position["y"])}" '
            f'width="{fmt(NODE_WIDTH)}" height="{fmt(position["height"])}" rx="3" '
            f'fill="{xml(node["color"])}" data-layer="{xml(node["layer"])}" '
            f'data-logical="{xml(node["logical_id"])}" '
            f'data-mapping="{xml(node["logical_id"] if node["layer"] == "mapping_family" else "")}" '
            f'data-tooltip="{xml(tooltip)}"><title>{xml(tooltip)}</title></rect>'
        )
    parts.append("  </g>\n  <g class=\"labels\" aria-label=\"Node labels\">")

    for node in nodes:
        position = positions[node["node_id"]]
        center_y = position["y"] + position["height"] / 2.0 + 8.0
        if node["layer"] == "rq2_source":
            x = position["x"] - 15.0
            anchor = "end"
            label = f'{static_label(node)} ({display_percentage(node["percentage_of_path_assignments"])})'
            extra_class = ""
        elif node["layer"] == "mapping_family":
            x = position["x"] + NODE_WIDTH + 10.0
            anchor = "start"
            label = f'{node["short_label"]} ({display_percentage(node["percentage_of_path_assignments"])})'
            extra_class = " mapping-label"
        else:
            x = position["x"] + NODE_WIDTH + 15.0
            anchor = "start"
            label = f'{static_label(node)} ({display_percentage(node["percentage_of_path_assignments"])})'
            extra_class = " long-target-label" if node["logical_id"] == "RQ1_DER" else ""
        parts.append(
            f'<text class="node-label{extra_class}" x="{fmt(x)}" y="{fmt(center_y)}" '
            f'text-anchor="{anchor}" data-layer="{xml(node["layer"])}" '
            f'data-logical="{xml(node["logical_id"])}" '
            f'data-mapping="{xml(node["logical_id"] if node["layer"] == "mapping_family" else "")}">'
            f'{xml(label)}</text>'
        )
    parts.append("  </g>")
    parts.append(legend_svg())
    parts.append("</svg>\n")
    return "\n".join(parts)


def build_html(svg: str) -> str:
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>RQ3 Sankey diagram</title>
  <style>
    html, body {{ margin: 0; padding: 0; overflow-x: hidden; background: #f4f6f8; color: #20262d; font-family: "Liberation Sans", Arial, sans-serif; }}
    #figure-frame {{ width: min({WIDTH}px, 100%); height: auto; aspect-ratio: {WIDTH} / {HEIGHT}; margin: 0 auto; background: #fff; box-shadow: 0 2px 18px rgba(30,40,50,.12); }}
    #figure-frame svg {{ display: block; width: 100%; height: auto; }}
    .interactive-note {{ box-sizing: border-box; width: min({WIDTH}px, 100%); margin: 0 auto; padding: 12px 18px 16px; font-size: 15px; color: #52606c; background: #fff; }}
    #tooltip {{ position: fixed; z-index: 10; display: none; pointer-events: none; white-space: pre-wrap; max-width: 560px; padding: 12px 14px; border: 1px solid #bcc5cc; border-radius: 7px; background: rgba(255,255,255,.98); color: #18212a; box-shadow: 0 5px 22px rgba(20,30,40,.18); font-size: 15px; line-height: 1.42; }}
    @page {{ size: {PRINT_WIDTH_IN:.4f}in {PRINT_HEIGHT_IN:.4f}in; margin: 0; }}
    @media print {{
      html, body {{ width: {PRINT_WIDTH_IN:.4f}in; height: {PRINT_HEIGHT_IN:.4f}in; background: #fff; }}
      #figure-frame {{ width: {PRINT_WIDTH_IN:.4f}in; height: {PRINT_HEIGHT_IN:.4f}in; aspect-ratio: auto; box-shadow: none; }}
      #figure-frame svg {{ width: {PRINT_WIDTH_IN:.4f}in; height: {PRINT_HEIGHT_IN:.4f}in; }}
      .interactive-note, #tooltip {{ display: none !important; }}
    }}
  </style>
</head>
<body>
  <div id="figure-frame">{svg}</div>
  <div class="interactive-note">Hover a band or node to inspect counts, study coverage, evidence coverage, and definitions. Hovering also highlights the corresponding mapping family. This file is self-contained and makes no network requests.</div>
  <div id="tooltip" role="status" aria-live="polite"></div>
  <script>
  (() => {{
    const tooltip = document.getElementById('tooltip');
    const links = [...document.querySelectorAll('.sankey-link')];
    const nodes = [...document.querySelectorAll('.sankey-node')];
    const labels = [...document.querySelectorAll('.node-label')];
    const interactive = [...links, ...nodes];

    function related(element, candidate) {{
      const mapping = element.dataset.mapping;
      if (mapping) {{
        return candidate.dataset.mapping === mapping || candidate.dataset.logical === mapping;
      }}
      const logical = element.dataset.logical;
      if (!logical) return false;
      return candidate.dataset.sourceLogical === logical || candidate.dataset.targetLogical === logical || candidate.dataset.logical === logical;
    }}

    function highlight(element) {{
      [...links, ...nodes, ...labels].forEach(item => {{
        const isRelated = item === element || related(element, item);
        item.classList.toggle('is-highlighted', isRelated);
        item.classList.toggle('is-dimmed', !isRelated);
      }});
    }}

    function clearHighlight() {{
      [...links, ...nodes, ...labels].forEach(item => item.classList.remove('is-highlighted', 'is-dimmed'));
    }}

    function positionTooltip(event) {{
      const pad = 18;
      const rect = tooltip.getBoundingClientRect();
      let left = event.clientX + pad;
      let top = event.clientY + pad;
      if (left + rect.width > window.innerWidth - 8) left = event.clientX - rect.width - pad;
      if (top + rect.height > window.innerHeight - 8) top = event.clientY - rect.height - pad;
      tooltip.style.left = `${{Math.max(8, left)}}px`;
      tooltip.style.top = `${{Math.max(8, top)}}px`;
    }}

    interactive.forEach(element => {{
      element.addEventListener('mouseenter', event => {{
        tooltip.textContent = element.dataset.tooltip || '';
        tooltip.style.display = 'block';
        highlight(element);
        positionTooltip(event);
      }});
      element.addEventListener('mousemove', positionTooltip);
      element.addEventListener('mouseleave', () => {{
        tooltip.style.display = 'none';
        clearHighlight();
      }});
    }});
    window.__SANKEY_READY__ = true;
  }})();
  </script>
</body>
</html>
"""


def assert_compact_visible_labels(svg: str) -> None:
    """Keep audit IDs and integer counts out of the visible figure labels."""

    root = ET.fromstring(svg)
    visible = " ".join(
        "".join(element.itertext())
        for element in root.iter()
        if element.tag.rsplit("}", 1)[-1] == "text"
    )
    assert not re.search(r"\bF\d{2}\b|/101\b|\b101\b", visible), visible


def export_static() -> None:
    from export_figure import export
    export(OUTPUT / "sankey", WIDTH, HEIGHT)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--no-static-export",
        action="store_true",
        help="Generate SVG and HTML only; skip Playwright PDF/PNG export.",
    )
    args = parser.parse_args()

    subprocess.run([sys.executable, str(Path(__file__).with_name("validate_release.py"))], check=True)
    nodes = read_csv(ROOT / "sankey_nodes.csv")
    edges = read_csv(ROOT / "sankey_edges.csv")
    summaries = read_csv(ROOT / "mapping_summary.csv")
    assert len(nodes) == 33 and len(edges) == 37 and len(summaries) == 12
    assert sum(int(row["value"]) for row in edges if row["edge_layer"] == "source_to_mapping") == 101
    assert sum(int(row["value"]) for row in edges if row["edge_layer"] == "mapping_to_target") == 101

    OUTPUT.mkdir(parents=True, exist_ok=True)
    svg = build_svg(nodes, edges)
    assert_compact_visible_labels(svg)
    (OUTPUT / "sankey.svg").write_text(svg, encoding="utf-8", newline="\n")
    (OUTPUT / "sankey.html").write_text(build_html(svg), encoding="utf-8", newline="\n")
    if not args.no_static_export:
        export_static()

    print("Rendered Sankey outputs:")
    print(f"  {OUTPUT / 'sankey.svg'}")
    print(f"  {OUTPUT / 'sankey.html'}")
    if not args.no_static_export:
        print(f"  {OUTPUT / 'sankey.pdf'}")
        print(f"  {OUTPUT / 'sankey.png'}")


if __name__ == "__main__":
    main()
