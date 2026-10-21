#!/usr/bin/env python3
"""Render supplied historical distance-law rows and untested causal hypotheses.

No distances, directions or exponents are recomputed. Architecture features
co-vary between rows; their causal roles require matched ablations.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class BreakpointRow:
    family: str
    retained_row: str
    architecture_feature: str
    alpha: str
    direction: str
    breakpoint_class: str


ROWS: list[BreakpointRow] = [
    BreakpointRow(
        family="Grown family 1",
        retained_row="drift=0.20, restore=0.70",
        architecture_feature="open directed grown transport",
        alpha="-0.962",
        direction="5/5 TOWARD",
        breakpoint_class="preserve",
    ),
    BreakpointRow(
        family="Grown family 2",
        retained_row="drift=0.05, restore=0.30",
        architecture_feature="independent open grown transport",
        alpha="-0.947",
        direction="5/5 TOWARD",
        breakpoint_class="preserve",
    ),
    BreakpointRow(
        family="Alt-connectivity",
        retained_row="drift=0.20, seed=0",
        architecture_feature="parity-tapered shell routing + dense fallback",
        alpha="-0.952",
        direction="0/5 TOWARD",
        breakpoint_class="break",
    ),
    BreakpointRow(
        family="Third family",
        retained_row="drift=0.20, seed=2",
        architecture_feature="deeper branch structure / cross-quadrant load balancing",
        alpha="-2.161",
        direction="0/5 TOWARD",
        breakpoint_class="break",
    ),
    BreakpointRow(
        family="Fourth family",
        retained_row="drift=0.00, seed=0",
        architecture_feature="quadrant-reflection symmetry",
        alpha="-1.190",
        direction="0/5 TOWARD",
        breakpoint_class="break",
    ),
    BreakpointRow(
        family="Fifth family radial",
        retained_row="drift=0.05, seed=0",
        architecture_feature="radial-shell confinement / over-locked transport",
        alpha="-0.313",
        direction="5/5 TOWARD",
        breakpoint_class="boundary",
    ),
]


def render_row(row: BreakpointRow) -> str:
    return (
        f"| {row.family} | {row.retained_row} | {row.architecture_feature} | "
        f"{row.alpha} | {row.direction} | {row.breakpoint_class} |"
    )


def main() -> int:
    print("# Distance Law Breakpoint Compare")
    print()
    print(
        "Historical finite-table rendering: supplied values are not recomputed; "
        "retention labels are historical, not current audit judgments."
    )
    print()
    print("| family | supplied row | architecture feature | alpha | direction | class |")
    print("| --- | --- | --- | ---: | --- | --- |")
    for row in ROWS:
        print(render_row(row))
    print()
    print("Conjectural feature interpretation (not tested by this renderer):")
    print(
        "The table motivates testing open directed transport against shell-locking, "
        "reflection closure and deep branch routing with matched ablations."
    )
    print()
    print("Historical causal hypotheses requiring ablations:")
    print(
        "- parity-tapered shell routing plus dense fallback rotates the response away"
    )
    print(
        "- deeper branch structure steepens the tail and kills the retained sign"
    )
    print(
        "- quadrant-reflection symmetry cancels the long-tail bias"
    )
    print(
        "- radial-shell confinement preserves direction but over-locks transport and flattens the exponent"
    )
    print()
    print("Scope:")
    print(
        "Only the supplied finite rows are rendered. Their association with features "
        "does not identify a causal mechanism or prove necessity across families."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
