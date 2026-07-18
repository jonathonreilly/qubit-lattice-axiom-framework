#!/usr/bin/env python3
"""Cycle 164: verify physical row transport through commuting multiplication."""

from __future__ import annotations

from collections import Counter
from itertools import product
from pathlib import Path

import physical_transport_bound_commuting_multiplier_probe_2026_07_15 as p


ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "PHYSICAL_TRANSPORT_BOUND_COMMUTING_MULTIPLIER_CYCLE164_NOTE_2026-07-15.md"
)
ROWS = tuple(product((0, 1), repeat=5))
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


def manhattan(left, right):
    return sum(abs(a - b) for a, b in zip(left, right))


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0

    print("AUTHORITY AND LAW")
    check("Cycle-164 review note exists", NOTE.is_file())
    check(
        "Cycle 164 adds no row and uses the deterministic Cycle-163 law",
        p.MERGED_RAW is p.prior.MERGED_RAW
        and len(p.MERGED_RAW) == 96_620
        and not p.prior.RAW_CONFLICTS
        and all(len(outputs) == 1 for outputs in p.MERGED_RAW.values()),
        len(p.MERGED_RAW),
    )
    paths = (p.LEFT_PATH, p.RIGHT_PATH, p.OUTPUT_PATH)
    nonlocal_steps = [
        (left, right)
        for path in paths
        for left, right in zip(path, path[1:])
        if manhattan(left, right) != 1
    ]
    check(
        "all three transport paths are strictly nearest-neighbor",
        not nonlocal_steps
        and p.cable.terminal_direction(p.LEFT_PATH) == (0, 0, -1)
        and p.cable.terminal_direction(p.RIGHT_PATH) == (0, 0, 1)
        and p.cable.terminal_direction(p.OUTPUT_PATH) == (1, 0, 0),
        nonlocal_steps[:1],
    )

    print("\nALL COMMUTING ROW PAIRS")
    pairs = tuple(
        (left, right)
        for left in ROWS
        for right in ROWS
        if not p.m.algebra.symplectic(left, right)
    )
    failures = []
    shapes = Counter()
    product_failures = []
    for left, right in pairs:
        result = p.graph(left, right)
        shapes[result[:6]] += 1
        wanted_role = p.m.five.ROW_ROLE[p.m.algebra.multiply_commuting(left, right)]
        if result[:5] != (42, 66, 1, 2, ()):
            failures.append((left, right, result))
        if result[6] != wanted_role:
            product_failures.append((left, right, result[6], wanted_role))
    check(
        "all 544 commuting pairs have one exact schedule graph",
        len(pairs) == 544
        and not failures
        and shapes == {(42, 66, 1, 2, (), 187): 544},
        (len(pairs), shapes, failures[:1]),
    )
    check(
        "every terminal output is the exact signed commuting product",
        not product_failures,
        product_failures[:1],
    )

    print("\nCUBIC COVARIANCE AND CAUSAL CONTROL")
    representative = ((1, 0, 0, 1, 0), (0, 1, 1, 0, 1))
    rotation_failures = []
    rotation_shapes = Counter()
    for rotation_index, rotation in enumerate(p.c53.ROTATIONS):
        result = p.graph(*representative, rotation=rotation)
        rotation_shapes[result[:6]] += 1
        if result[:5] != (42, 66, 1, 2, ()):
            rotation_failures.append((rotation_index, result))
    check(
        "all 24 proper-cubic orientations preserve exact closure",
        not rotation_failures
        and rotation_shapes == {(42, 66, 1, 2, (), 187): 24},
        (rotation_shapes, rotation_failures[:1]),
    )
    deletion_failures = []
    for label, source, surviving, role in (
        ("left", p.LEFT_PATH[0], p.RIGHT_PATH[1], p.m.five.ROW_ROLE[representative[1]]),
        ("right", p.RIGHT_PATH[0], p.LEFT_PATH[1], p.m.five.ROW_ROLE[representative[0]]),
    ):
        initial, expected, _dependencies, product_role = p.apparatus(*representative)
        if p.m.TARGET in initial or product_role in {
            initial.get(p.m.TARGET), initial.get(p.OUTPUT_PATH[1])
        }:
            deletion_failures.append((label, "product-supplied"))
            continue
        initial.pop(source)
        actual = p.enabled(initial)
        wanted = {surviving: frozenset((role,))}
        if actual != wanted:
            deletion_failures.append((label, actual, wanted, len(expected)))
    check(
        "source deletion suppresses product formation without harming the other input",
        not deletion_failures,
        deletion_failures[:1],
    )

    print("\nPROBE AND SCOPE")
    check("the companion composition probe is green", p.main() == 0)
    note = " ".join(NOTE.read_text(encoding="utf-8").lower().split()) if NOTE.is_file() else ""
    for phrase in (
        "all 544 ordered commuting pairs",
        "cycle 164 adds no canonical or raw row",
        "the product is not a host calculation",
        "joint placement rather than a newly identified operation",
        "does not claim the full physical pivot is complete",
        "no axiom, primitive, registry, policy, or audit edit follows",
    ):
        check("note contains: " + phrase, phrase in note)

    print("\nTOTAL")
    print("PASS", PASS, "FAIL", FAIL)
    print("RESULT", "PHYSICAL_TRANSPORT_BOUND_COMMUTING_MULTIPLIER" if FAIL == 0 else "FAIL")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
