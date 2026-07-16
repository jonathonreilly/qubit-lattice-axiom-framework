#!/usr/bin/env python3
"""Cycle 162: verify covariant transport and forking of physical row roles."""

from __future__ import annotations

from pathlib import Path

import physical_row_role_fork_cable_probe_2026_07_15 as p
import physical_three_row_spacious_isolated_pivot_cycle161_2026_07_15 as prior


ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "PHYSICAL_ROW_ROLE_FORK_CABLE_CYCLE162_NOTE_2026-07-15.md"
)
PASS = 0
FAIL = 0


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0

    print("AUTHORITY AND LAW")
    check("Cycle-162 review note exists", NOTE.is_file())
    check("all 32 physical row roles are in scope", len(p.ROW_ROLES) == 32)
    check(
        "64 canonical row-cable rows produce 1,536 cubic raw rows",
        len(p.CANONICAL_TABLE) == 64 and len(p.ROW_CABLE_RAW) == 1_536,
        (len(p.CANONICAL_TABLE), len(p.ROW_CABLE_RAW)),
    )
    overlap = set(p.ROW_CABLE_RAW) & set(p.case.MERGED_RAW)
    check(
        "row transport is disjoint from and deterministic with the retained law",
        not overlap
        and not p.RAW_CONFLICTS
        and len(p.case.MERGED_RAW) == 89_708
        and len(p.MERGED_RAW) == 91_244
        and all(len(outputs) == 1 for outputs in p.MERGED_RAW.values()),
        (len(overlap), len(p.RAW_CONFLICTS), len(p.MERGED_RAW)),
    )

    print("\nEXHAUSTIVE ROW TRANSPORT")
    failures = []
    graph_shapes = set()
    first_frontiers = set()
    initial_sizes = set()
    for role in p.ROW_ROLES:
        for rotation_index, rotation in enumerate(p.c53.ROTATIONS):
            result = p.graph(role, rotation)
            graph_shapes.add(result[:5])
            initial_sizes.add(result[5])
            first_frontiers.update(map(len, result[6]))
            if result[:5] != (36, 60, 1, 2, ()):
                failures.append((role, rotation_index, result))
    check(
        "all 768 row/orientation graphs close under every schedule",
        not failures
        and graph_shapes == {(36, 60, 1, 2, ())}
        and initial_sizes == {121},
        (graph_shapes, initial_sizes, failures[:1]),
    )
    check(
        "each common source initially enables exactly two branch writes",
        first_frontiers == {2},
        first_frontiers,
    )

    print("\nCAUSAL CONTROL")
    deletion_failures = []
    for role in p.ROW_ROLES:
        initial, _expected, _ports = p.apparatus(role)
        initial.pop(p.SOURCE)
        if actual := p.enabled(initial):
            deletion_failures.append((role, actual))
    check(
        "deleting the row source suppresses both transport branches",
        not deletion_failures,
        deletion_failures[:1],
    )

    print("\nPREDECESSOR COEXISTENCE")
    check(
        "the complete Cycle-161 and predecessor suite remains green",
        prior.main() == 0,
    )

    print("\nSCOPE")
    note = " ".join(NOTE.read_text(encoding="utf-8").lower().split()) if NOTE.is_file() else ""
    for phrase in (
        "transport, not new foundation content",
        "768 apparatus graphs",
        "zero deterministic conflict",
        "does not by itself complete that pivot",
        "supplies no reason to edit admissibility, record, a primitive, the registry, or policy",
        "retained constructive routes remain",
    ):
        check("note contains: " + phrase, phrase in note)

    print("\nTOTAL")
    print("PASS", PASS, "FAIL", FAIL)
    print("RESULT", "PHYSICAL_ROW_ROLE_FORK_CABLE" if FAIL == 0 else "FAIL")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
