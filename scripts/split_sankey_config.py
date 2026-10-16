"""Shared geometry for the two stitchable RQ3 Sankey panels.

The left and right renderers must import this module rather than solve their
layouts independently.  In particular, the mapping bars use the same unit,
gap, order, and vertical chart extent in both panels.
"""

from __future__ import annotations


DENOMINATOR = 101
PANEL_WIDTH = 1100
PANEL_HEIGHT = 2000
COMPOSITE_WIDTH = PANEL_WIDTH * 2
PRINT_COMPOSITE_WIDTH_IN = 7.43
PRINT_PANEL_WIDTH_IN = PRINT_COMPOSITE_WIDTH_IN / 2
PRINT_HEIGHT_IN = PRINT_COMPOSITE_WIDTH_IN * PANEL_HEIGHT / COMPOSITE_WIDTH

CHART_TOP = 120.0
CHART_BOTTOM = 1930.0
CHART_HEIGHT = CHART_BOTTOM - CHART_TOP
NODE_WIDTH = 18.0
NODE_GAP = 90.0

MAPPING_ORDER = [
    "F01",
    "F02",
    "F03",
    "F12",
    "F04",
    "F05",
    "F06",
    "F09",
    "F08",
    "F10",
    "F11",
    "F07",
]

SOURCE_ORDER = [
    "RQ2_CA_COR",
    "RQ2_CA_SEC",
    "RQ2_CA_COM",
    "RQ2_CA_ROB",
    "RQ2_CA_MAI",
    "RQ2_CA_UND",
    "RQ2_CA_EFF",
    "RQ2_NC_CSR",
    "RQ2_NC_DIS",
    "RQ2_NC_RED",
    "RQ2_NC_DIV",
    "RQ2_NC_CON",
    "RQ2_NC_LOW",
]

TARGET_ORDER = [
    "RQ1_SEC",
    "RQ1_COM",
    "RQ1_ROB",
    "RQ1_MAI",
    "RQ1_UND",
    "RQ1_EFF",
    "RQ1_COR",
    "RQ1_DER",
]

PARENT_ORDER = ["RQ2_CA", "RQ2_NC"]

LAYER_X = {
    "left": {
        "rq2_parent": 45.0,
        "rq2_leaf": 330.0,
        "mapping_left": 630.0,
    },
    "right": {
        "mapping_right": 470.0,
        "rq1_target": 820.0,
    },
}

# These are the fixed endpoints for the later horizontal family-pair arrows.
# The right value is panel-local; add PANEL_WIDTH in a side-by-side assembly.
LEFT_ARROW_ANCHOR_X = 1040.0
RIGHT_ARROW_ANCHOR_X = 60.0


def shared_unit() -> float:
    """Return the common pixels-per-path scale for every split-panel node."""

    largest_layer_size = max(len(SOURCE_ORDER), len(MAPPING_ORDER), len(TARGET_ORDER))
    return (CHART_HEIGHT - NODE_GAP * (largest_layer_size - 1)) / DENOMINATOR
