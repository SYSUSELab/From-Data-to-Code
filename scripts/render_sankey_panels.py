#!/usr/bin/env python3
"""Render two independently usable but exactly aligned RQ3 Sankey panels.

The left panel is RQ2 parent -> observed RQ2 leaf -> mapping left half.  The
right panel is mapping right half -> observed RQ1 leaf.  A third preview places
the panels side by side and adds non-quantitative horizontal pairing arrows.
All values and coordinates are read from the split-panel CSV files.
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
import textwrap
import xml.etree.ElementTree as ET
from pathlib import Path

from split_sankey_config import (
    COMPOSITE_WIDTH,
    LEFT_ARROW_ANCHOR_X,
    NODE_WIDTH,
    PANEL_HEIGHT,
    PANEL_WIDTH,
    PRINT_COMPOSITE_WIDTH_IN,
    PRINT_HEIGHT_IN,
    PRINT_PANEL_WIDTH_IN,
    RIGHT_ARROW_ANCHOR_X,
    shared_unit,
)


ROOT = Path(__file__).resolve().parents[1] / "data" / "rq3"
OUTPUT = Path(__file__).resolve().parents[1] / ".local" / "rq3-panels"

STATIC_LABELS = {
    "RQ2_NC_DIS": "Distribution imbalance",
    "RQ2_NC_RED": "Redundancy",
    "RQ2_NC_DIV": "Inadequate diversity",
    "RQ2_NC_CON": "Contamination",
    "RQ2_NC_LOW": "Low-value data",
    "RQ1_DER": "Generation derailment",
}


def read_csv(name: str) -> list[dict[str, str]]:
    with (ROOT / name).open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def xml(value: object) -> str:
    return html.escape(str(value), quote=True)


def fmt(value: float) -> str:
    return f"{value:.2f}".rstrip("0").rstrip(".")


def display_percentage(value: str) -> str:
    return f"{float(value):.1f}%"


def short_label(node: dict[str, str]) -> str:
    return STATIC_LABELS.get(node["logical_id"], node["short_label"])


def wrap_label(value: str, width: int) -> list[str]:
    lines = textwrap.wrap(
        value,
        width=width,
        break_long_words=False,
        break_on_hyphens=False,
    )
    return lines or [value]


def positions(nodes: list[dict[str, str]]) -> dict[str, dict[str, float]]:
    return {
        row["node_id"]: {
            "x": float(row["x"]),
            "y": float(row["y_top"]),
            "center": float(row["y_center"]),
            "height": float(row["node_height"]),
        }
        for row in nodes
    }


def node_tooltip(node: dict[str, str]) -> str:
    layer_names = {
        "rq2_parent": "RQ2 training-data quality parent",
        "rq2_leaf": "RQ2 training-data quality leaf",
        "mapping_left": "RQ3 mapping family, source half",
        "mapping_right": "RQ3 mapping family, outcome half",
        "rq1_target": "RQ1 generated-code quality leaf",
    }
    lines = [
        f'{layer_names[node["layer"]]}: {node["label"]}',
        f'Share of path assignments: {display_percentage(node["percentage_of_path_assignments"])}',
        f'Distinct studies: {node["n_distinct_studies"]}',
    ]
    if node["paired_mapping_label"]:
        lines.append(f'Complete mapping: {node["paired_mapping_label"]}')
    lines.append(node["description"])
    return "\n".join(lines)


def edge_tooltip(
    edge: dict[str, str], node_by_id: dict[str, dict[str, str]]
) -> str:
    source = node_by_id[edge["source_node_id"]]
    target = node_by_id[edge["target_node_id"]]
    return "\n".join([
        f'{source["label"]} → {target["label"]}',
        f'Share of path assignments: {display_percentage(edge["percentage_of_path_assignments"])}',
        f'Distinct studies: {edge["n_distinct_studies"]}',
        f'Distinct evidence rows: {edge["n_distinct_evidence_rows"]}',
        f'Studies: {edge["supporting_study_ids"]}',
        f'Evidence: {edge["supporting_source_evidence_ids"]}',
    ])


def link_paths(
    nodes: list[dict[str, str]], edges: list[dict[str, str]]
) -> list[tuple[dict[str, str], str]]:
    position_by_id = positions(nodes)
    outgoing = {node_id: value["y"] for node_id, value in position_by_id.items()}
    incoming = {node_id: value["y"] for node_id, value in position_by_id.items()}
    result: list[tuple[dict[str, str], str]] = []
    unit = shared_unit()

    for edge in edges:
        source_id = edge["source_node_id"]
        target_id = edge["target_node_id"]
        source = position_by_id[source_id]
        target = position_by_id[target_id]
        thickness = int(edge["value"]) * unit
        x0 = source["x"] + NODE_WIDTH
        x1 = target["x"]
        y0_top = outgoing[source_id]
        y1_top = incoming[target_id]
        y0_bottom = y0_top + thickness
        y1_bottom = y1_top + thickness
        bend = (x1 - x0) * 0.48
        path = (
            f"M {fmt(x0)} {fmt(y0_top)} "
            f"C {fmt(x0 + bend)} {fmt(y0_top)}, {fmt(x1 - bend)} {fmt(y1_top)}, {fmt(x1)} {fmt(y1_top)} "
            f"L {fmt(x1)} {fmt(y1_bottom)} "
            f"C {fmt(x1 - bend)} {fmt(y1_bottom)}, {fmt(x0 + bend)} {fmt(y0_bottom)}, {fmt(x0)} {fmt(y0_bottom)} Z"
        )
        result.append((edge, path))
        outgoing[source_id] = y0_bottom
        incoming[target_id] = y1_bottom

    for node in nodes:
        node_id = node["node_id"]
        expected_bottom = position_by_id[node_id]["y"] + position_by_id[node_id]["height"]
        if node["layer"] in {"rq2_parent", "mapping_right"}:
            assert abs(outgoing[node_id] - expected_bottom) < 1e-4, node_id
        elif node["layer"] == "rq2_leaf":
            assert abs(incoming[node_id] - expected_bottom) < 1e-4, node_id
            assert abs(outgoing[node_id] - expected_bottom) < 1e-4, node_id
        elif node["layer"] in {"mapping_left", "rq1_target"}:
            assert abs(incoming[node_id] - expected_bottom) < 1e-4, node_id
    return result


def block_text(
    *,
    x: float,
    center_y: float,
    label_lines: list[str],
    metadata: str,
    anchor: str,
    data_layer: str,
    data_logical: str,
    data_mapping: str,
    mapping: bool,
) -> str:
    phrase_line_height = 29.0 if mapping else 28.0
    metadata_line_height = 24.0
    total_height = len(label_lines) * phrase_line_height + metadata_line_height
    first_baseline = center_y - total_height / 2.0 + phrase_line_height * 0.80
    base_class = "node-label mapping-label" if mapping else "node-label"
    parts = [
        (
            f'<text class="{base_class}" x="{fmt(x)}" y="{fmt(first_baseline)}" '
            f'text-anchor="{anchor}" data-layer="{xml(data_layer)}" '
            f'data-logical="{xml(data_logical)}" data-mapping="{xml(data_mapping)}">'
        )
    ]
    for index, line in enumerate(label_lines):
        y_attribute = f' y="{fmt(first_baseline)}"' if index == 0 else ""
        dy_attribute = "" if index == 0 else f' dy="{fmt(phrase_line_height)}"'
        parts.append(
            f'<tspan class="label-phrase" x="{fmt(x)}"{y_attribute}{dy_attribute}>{xml(line)}</tspan>'
        )
    parts.append(
        f'<tspan class="label-meta" x="{fmt(x)}" dy="{fmt(metadata_line_height)}">{xml(metadata)}</tspan>'
    )
    parts.append("</text>")
    return "".join(parts)


def panel_elements(
    panel: str,
    nodes: list[dict[str, str]],
    edges: list[dict[str, str]],
) -> str:
    assert panel in {"left", "right"}
    node_by_id = {row["node_id"]: row for row in nodes}
    position_by_id = positions(nodes)
    paths = link_paths(nodes, edges)

    if panel == "left":
        headings = [
            (45, "RQ2 CATEGORY", "start"),
            (330, "RQ2 LEAF", "start"),
            (650, "MAPPING · SOURCE HALF", "start"),
        ]
    else:
        headings = [
            (450, "MAPPING · OUTCOME HALF", "end"),
            (820, "RQ1 LEAF", "start"),
        ]

    parts = [f'<g id="{panel}-panel" class="panel">']
    parts.append(f'<rect width="{PANEL_WIDTH}" height="{PANEL_HEIGHT}" fill="#ffffff"/>')
    for x, label, anchor in headings:
        parts.append(
            f'<text class="column-heading" x="{x}" y="72" text-anchor="{anchor}">{xml(label)}</text>'
        )
    parts.append('<g class="links" aria-label="Sankey bands">')
    for edge, path in paths:
        tooltip = edge_tooltip(edge, node_by_id)
        parts.append(
            f'<path id="edge-{xml(edge["edge_id"])}" class="sankey-link" d="{path}" '
            f'fill="{xml(edge["color"])}" data-tooltip="{xml(tooltip)}" '
            f'data-mapping="{xml(edge["mapping_id"])}" '
            f'data-source-logical="{xml(edge["source_logical_id"])}" '
            f'data-target-logical="{xml(edge["target_logical_id"])}">'
            f'<title>{xml(tooltip)}</title></path>'
        )
    parts.append("</g><g class=\"nodes\" aria-label=\"Sankey nodes\">")
    for node in nodes:
        position = position_by_id[node["node_id"]]
        tooltip = node_tooltip(node)
        mapping_id = node["logical_id"] if node["layer"].startswith("mapping_") else ""
        parts.append(
            f'<rect id="node-{xml(node["node_id"].replace(":", "-"))}" class="sankey-node" '
            f'x="{fmt(position["x"])}" y="{fmt(position["y"])}" width="{fmt(NODE_WIDTH)}" '
            f'height="{fmt(position["height"])}" rx="3" fill="{xml(node["color"])}" '
            f'data-layer="{xml(node["layer"])}" data-logical="{xml(node["logical_id"])}" '
            f'data-mapping="{xml(mapping_id)}" data-tooltip="{xml(tooltip)}">'
            f'<title>{xml(tooltip)}</title></rect>'
        )
    parts.append("</g><g class=\"labels\" aria-label=\"Node labels\">")
    for node in nodes:
        position = position_by_id[node["node_id"]]
        layer = node["layer"]
        mapping = layer.startswith("mapping_")
        if layer == "rq2_parent":
            x, anchor, width = position["x"] + NODE_WIDTH + 10.0, "start", 19
        elif layer == "rq2_leaf":
            x, anchor, width = position["x"] + NODE_WIDTH + 9.0, "start", 20
        elif layer == "mapping_left":
            x, anchor, width = position["x"] + NODE_WIDTH + 12.0, "start", 28
        elif layer == "mapping_right":
            x, anchor, width = position["x"] - 12.0, "end", 28
        else:
            x, anchor, width = position["x"] + NODE_WIDTH + 10.0, "start", 16
        lines = wrap_label(node["label"] if mapping else short_label(node), width)
        metadata = f'({display_percentage(node["percentage_of_path_assignments"])})'
        parts.append(block_text(
            x=x,
            center_y=position["center"],
            label_lines=lines,
            metadata=metadata,
            anchor=anchor,
            data_layer=layer,
            data_logical=node["logical_id"],
            data_mapping=node["logical_id"] if mapping else "",
            mapping=mapping,
        ))
    parts.append("</g></g>")
    return "\n".join(parts)


def svg_style() -> str:
    return """<style>
    :root { color-scheme: light; }
    text { font-family: "Liberation Sans", Arial, sans-serif; fill: #20262d; }
    .column-heading { font-size: 24px; font-weight: 700; letter-spacing: .9px; fill: #46515b; }
    .sankey-link { transition: opacity 120ms ease; cursor: pointer; }
    .sankey-node { cursor: pointer; }
    .node-label { font-size: 25px; font-weight: 600; }
    .mapping-label { font-size: 27px; font-weight: 700; }
    .label-meta { font-size: 21px; font-weight: 500; fill: #4f5b65; }
    .mapping-label .label-meta { font-size: 22px; font-weight: 600; }
    .mapping-frame { fill: none; stroke: #4a5259; stroke-width: 2; stroke-dasharray: 10 7; }
    .mapping-title { font-size: 30px; font-weight: 700; }
    .pair-arrow { stroke: #20262d; stroke-width: 2.5; fill: none; }
    .sankey-link.is-dimmed, .sankey-node.is-dimmed, .node-label.is-dimmed { opacity: .10 !important; }
    .sankey-link.is-highlighted { opacity: .88 !important; stroke: rgba(30,35,40,.30); stroke-width: 1.1; }
    .sankey-node.is-highlighted { stroke: #17212b; stroke-width: 3; }
  </style>"""


def build_panel_svg(
    panel: str,
    nodes: list[dict[str, str]],
    edges: list[dict[str, str]],
) -> str:
    title = "RQ2 taxonomy to mapping source halves" if panel == "left" else "Mapping outcome halves to RQ1 taxonomy"
    description = (
        "Code-attribute and non-code-attribute RQ2 parents flow through twelve observed RQ2 leaves to twelve mapping source halves."
        if panel == "left"
        else "Twelve mapping outcome halves flow to eight observed RQ1 generated-code quality leaves."
    )
    return (
        f'<svg id="sankey-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {PANEL_WIDTH} {PANEL_HEIGHT}" '
        f'width="{PANEL_WIDTH}" height="{PANEL_HEIGHT}" role="img" aria-labelledby="figure-title figure-desc">\n'
        f'<title id="figure-title">{xml(title)}</title><desc id="figure-desc">{xml(description)}</desc>\n'
        f'{svg_style()}\n{panel_elements(panel, nodes, edges)}\n</svg>\n'
    )


def build_preview_svg(
    left_nodes: list[dict[str, str]],
    left_edges: list[dict[str, str]],
    right_nodes: list[dict[str, str]],
    right_edges: list[dict[str, str]],
    alignment: list[dict[str, str]],
) -> str:
    parts = [
        f'<svg id="sankey-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {COMPOSITE_WIDTH} {PANEL_HEIGHT}" '
        f'width="{COMPOSITE_WIDTH}" height="{PANEL_HEIGHT}" role="img" aria-labelledby="figure-title figure-desc">',
        '<title id="figure-title">Stitching preview of the split RQ3 Sankey diagram</title>',
        '<desc id="figure-desc">The two independently rendered panels share twelve exactly aligned mapping slots connected here by non-quantitative horizontal arrows.</desc>',
        svg_style(),
        '<defs><marker id="pair-arrowhead" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto" markerUnits="strokeWidth"><path d="M0,0 L8,4 L0,8 Z" fill="#20262d"/></marker></defs>',
        panel_elements("left", left_nodes, left_edges),
        f'<g transform="translate({PANEL_WIDTH},0)">{panel_elements("right", right_nodes, right_edges)}</g>',
        '<rect class="mapping-frame" x="610" y="88" width="980" height="1865" rx="24"/>',
        '<rect x="1010" y="24" width="180" height="52" fill="#ffffff"/>',
        '<text class="mapping-title" x="1100" y="61" text-anchor="middle">MAPPINGS</text>',
        '<g class="pair-arrows" aria-label="Non-quantitative mapping-pair arrows">',
    ]
    for row in alignment:
        y = float(row["y_center"])
        parts.append(
            f'<line id="pair-{xml(row["mapping_id"])}" class="pair-arrow" '
            f'x1="{fmt(LEFT_ARROW_ANCHOR_X + 4)}" y1="{fmt(y)}" '
            f'x2="{fmt(PANEL_WIDTH + RIGHT_ARROW_ANCHOR_X - 8)}" y2="{fmt(y)}" '
            f'marker-end="url(#pair-arrowhead)" data-mapping="{xml(row["mapping_id"])}">'
            f'<title>{xml(row["full_arrow_label"])}; pairing arrow only, not a flow value.</title></line>'
        )
    parts.extend(["</g>", "</svg>\n"])
    return "\n".join(parts)


def build_html(
    svg: str,
    *,
    width: int,
    height: int,
    print_width: float,
    print_height: float,
    note: str,
) -> str:
    # Points preserve the exact half-width relationship. Chromium rounds page
    # sizes expressed with three-decimal inch values to hundredths of an inch.
    print_width_pt = print_width * 72.0
    print_height_pt = print_height * 72.0
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>RQ3 split Sankey diagram</title>
  <style>
    html, body {{ margin: 0; padding: 0; overflow-x: hidden; background: #f4f6f8; color: #20262d; font-family: "Liberation Sans", Arial, sans-serif; }}
    #figure-frame {{ width: min({width}px, 100%); height: auto; aspect-ratio: {width} / {height}; margin: 0 auto; background: #fff; box-shadow: 0 2px 18px rgba(30,40,50,.12); }}
    #figure-frame svg {{ display: block; width: 100%; height: auto; }}
    .interactive-note {{ box-sizing: border-box; width: min({width}px, 100%); margin: 0 auto; padding: 12px 18px 16px; font-size: 15px; color: #52606c; background: #fff; }}
    #tooltip {{ position: fixed; z-index: 10; display: none; pointer-events: none; white-space: pre-wrap; max-width: 560px; padding: 12px 14px; border: 1px solid #bcc5cc; border-radius: 7px; background: rgba(255,255,255,.98); color: #18212a; box-shadow: 0 5px 22px rgba(20,30,40,.18); font-size: 15px; line-height: 1.42; }}
    @page {{ size: {print_width_pt:.2f}pt {print_height_pt:.2f}pt; margin: 0; }}
    @media print {{
      html, body {{ width: {print_width_pt:.2f}pt; height: {print_height_pt:.2f}pt; background: #fff; }}
      #figure-frame {{ width: {print_width_pt:.2f}pt; height: {print_height_pt:.2f}pt; aspect-ratio: auto; box-shadow: none; }}
      #figure-frame svg {{ width: {print_width_pt:.2f}pt; height: {print_height_pt:.2f}pt; }}
      .interactive-note, #tooltip {{ display: none !important; }}
    }}
  </style>
</head>
<body>
  <div id="figure-frame">{svg}</div>
  <div class="interactive-note">{xml(note)} Hover a band or node for counts and evidence coverage. The file is self-contained and makes no network requests.</div>
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
      if (mapping) return candidate.dataset.mapping === mapping || candidate.dataset.logical === mapping;
      const source = element.dataset.sourceLogical;
      const target = element.dataset.targetLogical;
      if (source || target) {{
        return candidate.dataset.logical === source || candidate.dataset.logical === target ||
          (candidate.dataset.sourceLogical === source && candidate.dataset.targetLogical === target);
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
    function clearHighlight() {{ [...links, ...nodes, ...labels].forEach(item => item.classList.remove('is-highlighted', 'is-dimmed')); }}
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
      element.addEventListener('mouseleave', () => {{ tooltip.style.display = 'none'; clearHighlight(); }});
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


def export_static(stem: str, width: int, height: int) -> None:
    from export_figure import export
    export(OUTPUT / stem, width, height)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--no-static-export",
        action="store_true",
        help="Generate SVG and HTML only; skip Playwright PDF/PNG export.",
    )
    args = parser.parse_args()

    subprocess.run([sys.executable, str(Path(__file__).with_name("validate_release.py"))], check=True)

    left_nodes = read_csv("sankey_left_nodes.csv")
    left_edges = read_csv("sankey_left_edges.csv")
    right_nodes = read_csv("sankey_right_nodes.csv")
    right_edges = read_csv("sankey_right_edges.csv")
    alignment = read_csv("mapping_panel_alignment.csv")
    assert len(left_nodes) == 27 and len(left_edges) == 27
    assert len(right_nodes) == 20 and len(right_edges) == 23
    assert len(alignment) == 12

    figures = {
        "sankey_left": (
            build_panel_svg("left", left_nodes, left_edges),
            PANEL_WIDTH,
            PANEL_HEIGHT,
            PRINT_PANEL_WIDTH_IN,
            PRINT_HEIGHT_IN,
            "Left panel: RQ2 parents → observed RQ2 leaves → mapping source halves.",
        ),
        "sankey_right": (
            build_panel_svg("right", right_nodes, right_edges),
            PANEL_WIDTH,
            PANEL_HEIGHT,
            PRINT_PANEL_WIDTH_IN,
            PRINT_HEIGHT_IN,
            "Right panel: mapping outcome halves → observed RQ1 leaves.",
        ),
        "sankey_split_preview": (
            build_preview_svg(left_nodes, left_edges, right_nodes, right_edges, alignment),
            COMPOSITE_WIDTH,
            PANEL_HEIGHT,
            PRINT_COMPOSITE_WIDTH_IN,
            PRINT_HEIGHT_IN,
            "Alignment preview: the middle arrows pair family halves and do not encode additional flow.",
        ),
    }

    OUTPUT.mkdir(parents=True, exist_ok=True)
    for stem, (svg, width, height, print_width, print_height, note) in figures.items():
        assert_compact_visible_labels(svg)
        (OUTPUT / f"{stem}.svg").write_text(svg, encoding="utf-8", newline="\n")
        (OUTPUT / f"{stem}.html").write_text(
            build_html(
                svg,
                width=width,
                height=height,
                print_width=print_width,
                print_height=print_height,
                note=note,
            ),
            encoding="utf-8",
            newline="\n",
        )
        if not args.no_static_export:
            export_static(stem, width, height)

    print("Rendered stitchable Sankey outputs:")
    for stem in figures:
        suffixes = ["svg", "html"] + ([] if args.no_static_export else ["pdf", "png"])
        print(f"  {stem}: " + ", ".join(str(OUTPUT / f"{stem}.{suffix}") for suffix in suffixes))


if __name__ == "__main__":
    main()
