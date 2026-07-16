#!/usr/bin/env python3
"""Cycle 157: verify one physical bit feeding two cable branches."""

from __future__ import annotations

from collections import Counter
from pathlib import Path

import physical_literal_bit_fork_probe_2026_07_15 as p


d = p.d
c53 = p.c53
ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "PHYSICAL_LITERAL_BIT_FORK_CYCLE157_NOTE_2026-07-15.md"
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

    print("AUTHORITY AND GEOMETRY")
    check("review note exists", NOTE.is_file())
    check(
        "Cycle 157 adds no transition row",
        p.MERGED_RAW is p.cable.MERGED_RAW and len(p.MERGED_RAW) == 83_372,
        len(p.MERGED_RAW),
    )
    check(
        "two three-write branches share exactly one source",
        len(p.PATHS) == 2
        and all(len(path) == 4 for path in p.PATHS)
        and set(p.PATHS[0]) & set(p.PATHS[1]) == {p.SOURCE},
        p.PATHS,
    )

    print("\nCAUSAL PRODUCT")
    failures = []
    source_sizes = set()
    endpoint_failures = []
    for value in (d.H0, d.H1):
        initial, expected, ports = p.apparatus(value)
        source_sizes.add(len(initial))
        if (
            len(expected) != 6
            or set(expected.values()) != {value}
            or len(ports) != 2
            or set(ports) & (set(initial) | set(expected))
        ):
            endpoint_failures.append((value, expected, ports))
        for rotation_index, rotation in enumerate(c53.ROTATIONS):
            result = p.graph(value, rotation)
            if result[:5] != (16, 24, 1, 2, ()):
                failures.append((value, rotation_index, result))
    check(
        "all 48 value-orientation fork graphs are exact",
        not failures and source_sizes == {81},
        (source_sizes, failures[:1]),
    )
    check(
        "both endpoints retain the source value and remain open",
        not endpoint_failures,
        endpoint_failures[:1],
    )
    check(
        "one literal source and no supplied branch value drive six writes",
        all(
            Counter(p.apparatus(value)[0].values())[value] == 1
            and not (set(p.apparatus(value)[1]) & set(p.apparatus(value)[0]))
            for value in (d.H0, d.H1)
        ),
    )

    print("\nCONTROLS")
    deletion_failures = []
    for value in (d.H0, d.H1):
        initial, _expected, _ports = p.apparatus(value)
        initial.pop(p.SOURCE)
        actual = p.enabled(initial)
        if actual:
            deletion_failures.append((value, actual))
    check(
        "deleting the shared source suppresses both branches",
        not deletion_failures,
        deletion_failures[:1],
    )
    check(
        "the joint fixture uses only existing frame and guide roles",
        all(
            set(p.apparatus(value)[0].values())
            <= {value, p.FRAME, p.cable.GUIDE_ROLE}
            for value in (d.H0, d.H1)
        ),
    )

    print("\nSCOPE")
    note = " ".join(NOTE.read_text(encoding="utf-8").lower().split()) if NOTE.is_file() else ""
    for phrase in (
        "one physical bit to two cable branches",
        "no transition row is added",
        "measured-row reuse",
        "supplied guide/frame harness",
        "does not derive occurrence or equal weights",
        "no axiom addition follows",
        "n1 — alternative routes",
        "n8 — cross-cycle echo",
    ):
        check("note contains: " + phrase, phrase in note)

    print("\nTOTAL")
    print("PASS", PASS, "FAIL", FAIL)
    print("RESULT", "PHYSICAL_LITERAL_BIT_FORK" if FAIL == 0 else "FAIL")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
