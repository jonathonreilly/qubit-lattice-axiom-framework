#!/usr/bin/env python3
"""Render a historical finite comparison table without recomputing its physics.

All rows are supplied historical descriptions. Retention words in those rows
are historical labels, not current audit judgments. The original grown-basin
signed-source half-row is outside the paired note's narrowed comparison.
No solver, causal ablation, physical verification or audit lookup is performed.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class SelectivityRow:
    family: str
    signed_source_surface: str
    signed_source_result: str
    weak_field_response: str
    complex_surface: str
    complex_result: str
    mismatch: str
    source_notes: str


ROWS: list[SelectivityRow] = [
    SelectivityRow(
        family="Original grown basin",
        signed_source_surface="exact zero-source / neutral same-point cancellation",
        signed_source_result="retained narrow basin positive",
        weak_field_response="F~M = 1.000",
        complex_surface="nearby grown-row complex-action surface",
        complex_result="retained narrow gamma=0 -> AWAY crossover on nearby rows",
        mismatch="selective basin, not family-wide closure",
        source_notes=(
            "docs/GROWN_TRANSFER_BASIN_NOTE.md; "
            "docs/CLAUDE_COMPLEX_ACTION_GROWN_COMPANION_NOTE.md"
        ),
    ),
    SelectivityRow(
        family="Second-family complex",
        signed_source_surface="adjacent only; not the active observable",
        signed_source_result="not the shared surface",
        weak_field_response="F~M = 1.000",
        complex_surface="exact gamma=0 baseline + Born proxy + crossover",
        complex_result="retained narrow anchor-row positive",
        mismatch="tiny basin, then a tighter AWAY-at-gamma=0 boundary",
        source_notes=(
            "docs/SECOND_GROWN_FAMILY_COMPLEX_NOTE.md; "
            "docs/SECOND_GROWN_FAMILY_COMPLEX_BOUNDARY_NOTE.md"
        ),
    ),
    SelectivityRow(
        family="Alternative connectivity family",
        signed_source_surface="exact zero / neutral signed-source controls",
        signed_source_result="retained bounded positive",
        weak_field_response="F~M = 0.999994",
        complex_surface="same no-restore slice, gamma sweep",
        complex_result="clean boundary failure; no TOWARD -> AWAY crossover",
        mismatch="sign-law survives, complex branch does not",
        source_notes=(
            "docs/ALT_CONNECTIVITY_FAMILY_BASIN_NOTE.md; "
            "docs/ALT_CONNECTIVITY_FAMILY_FM_TRANSFER_NOTE.md; "
            "docs/ALT_CONNECTIVITY_FAMILY_COMPLEX_FAILURE_NOTE.md"
        ),
    ),
    SelectivityRow(
        family="Third grown family",
        signed_source_surface="exact zero-source / exact neutral +1/-1 cancellation",
        signed_source_result="retained bounded basin positive",
        weak_field_response="charge exponent = 0.999842",
        complex_surface="not yet promoted on this slice",
        complex_result="not retained; boundary is sign-orientation reversal at drift edges",
        mismatch="signed-source basin survives in the interior only",
        source_notes=(
            "docs/THIRD_GROWN_FAMILY_SIGN_NOTE.md; "
            "docs/THIRD_GROWN_FAMILY_BOUNDARY_NOTE.md"
        ),
    ),
    SelectivityRow(
        family="Fourth family quadrant",
        signed_source_surface="exact zero-source / exact neutral cancellation",
        signed_source_result="retained narrow basin",
        weak_field_response="near-linear charge scaling",
        complex_surface="not yet promoted on this slice",
        complex_result="not retained; basin is seed-selective",
        mismatch="fresh family exists, but remains sign-law only",
        source_notes="docs/FOURTH_FAMILY_QUADRANT_NOTE.md",
    ),
]


def render_markdown(rows: list[SelectivityRow]) -> str:
    lines = [
        "# Complex Selectivity Compare Note",
        "",
        "**Date:** 2026-04-06",
        "**Status:** historical supplied-row rendering, not independent computation",
        "Original grown-basin signed-source half-row is out of scope; retention labels below are historical.",
        "",
        "## Question",
        "",
        "Why does signed-source transfer survive on multiple independent families while complex-action companions stay much more selective?",
        "",
        "## Comparison",
        "",
        "| family | signed-source surface | signed-source result | weak-field response | complex-action surface | complex-action result | mismatch |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    for row in rows:
        lines.append(
            f"| {row.family} | {row.signed_source_surface} | {row.signed_source_result} | {row.weak_field_response} | {row.complex_surface} | {row.complex_result} | {row.mismatch} |"
        )
    lines.extend(
        [
            "",
            "## Historical interpretation",
            "",
            "- historical table interpretation: signed-source transfer is the portable feature: exact zero / neutral controls survive on several distinct structured families",
            "- historical table interpretation: weak-field linearity survives with the signed-source package across the retained grown, alt, third, and fourth family slices",
            "- historical table interpretation: complex action is more selective: it needs the exact gamma=0 anchor / crossover structure and fails cleanly on the alt family and the tightened second-family window",
            "",
            "## Comparison boundary",
            "",
            "- the signed-source families share a common control surface",
            "- the complex-action branch does not share that same surface; it lives on a more constrained gamma baseline plus crossover test",
            "- the result is not a universal family theorem; it is a selectivity split between portable sign-law and basin-local complex action",
            "",
            "## Rendering scope",
            "",
            "**Historical finite-table rendering; source provenance and physical conclusions require separate verification.**",
        ]
    )
    return "\n".join(lines)


def render_text(rows: list[SelectivityRow]) -> str:
    lines = [
        "COMPLEX SELECTIVITY COMPARE NOTE",
        "Date: 2026-04-06",
        "Status: historical supplied-row rendering, not independent computation",
        "Original grown-basin signed-source half-row is out of scope; retention labels below are historical.",
        "",
        "Question:",
        "Why does signed-source transfer survive on multiple independent families while complex-action companions stay much more selective?",
        "",
    ]
    for row in rows:
        lines.extend(
            [
                f"- {row.family}",
                f"  signed-source: {row.signed_source_result}",
                f"  weak-field: {row.weak_field_response}",
                f"  complex-action: {row.complex_result}",
                f"  mismatch: {row.mismatch}",
            ]
        )
    lines.extend(
        [
            "",
            "Historical interpretation:",
            "- historical table interpretation: signed-source transfer is portable across several structured families",
            "- historical table interpretation: complex action is constrained to a smaller anchor-local basin",
            "- the comparison isolates a selectivity split rather than a universal identity",
            "",
            "Rendering scope:",
            "Historical finite-table rendering; source provenance and physical conclusions require separate verification.",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--format", choices=("markdown", "text", "json"), default="markdown")
    parser.add_argument("--write-log", help="optional path to write the rendered report")
    args = parser.parse_args()

    payload = {
        "rows": [row.__dict__ for row in ROWS],
        "summary": {
            "evidence_kind": "historical supplied-row rendering; no independent computation",
            "original_grown_signed_source_in_scope": False,
            "current_audit_status_checked": False,
            "historical_interpretation": "portable sign-law with anchor-local complex-action selectivity",
        },
    }

    if args.format == "json":
        rendered = json.dumps(payload, indent=2, sort_keys=True)
    elif args.format == "text":
        rendered = render_text(ROWS)
    else:
        rendered = render_markdown(ROWS)

    print(rendered)

    if args.write_log:
        path = Path(args.write_log)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(rendered + "\n", encoding="utf-8")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
