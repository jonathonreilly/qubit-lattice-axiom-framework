#!/usr/bin/env python3
"""Cycle 151: physical symplectic decision and commuting multiplication atoms."""

from __future__ import annotations

from collections import Counter
from itertools import product
from pathlib import Path

import physical_commuting_row_multiplication_probe_2026_07_15 as p


c150 = p.c150
commute = c150.p
alu = commute.alu
compact = alu.compact
u = compact.unified
d = alu.d
c53 = alu.c53
ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "work_history" / "repo" / "review_feedback" / "PHYSICAL_COMMUTATION_MULTIPLICATION_ATOMS_CYCLE151_NOTE_2026-07-15.md"
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


def enabled(records):
    return {
        target: p.MERGED_RAW[local]
        for target in c53.open_candidates(records)
        if (local := c53.local_signature(records, target)) in p.MERGED_RAW
    }


def unified_run(state_id, events):
    source, expected = u.apparatus(state_id, events)
    records = dict(source)
    for target, output in expected.items():
        actual = enabled(records)
        wanted = {target: frozenset((output,))}
        if actual != wanted:
            return False, (actual, wanted)
        records[target] = output
    return (not enabled(records), enabled(records))


def deletion_controls():
    attempts = 0
    failures = []
    for local, output in p.CANONICAL_TABLE.items():
        for index in range(len(local)):
            attempts += 1
            mutated = local[:index] + local[index + 1:]
            if output in p.MERGED_RAW.get(mutated, frozenset()):
                failures.append((local, index, output))
    return attempts, tuple(failures)


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0

    print("AUTHORITY AND PREDECESSOR")
    check("review note exists", NOTE.is_file())
    check(
        "literal commutation atom remains exact and conflict-free",
        len(commute.PARITY_TABLE) == 6
        and len(commute.PARITY_RAW) == 48
        and not commute.RAW_CONFLICTS,
    )
    check(
        "row alphabet covers all 32 signed Paulis",
        len(p.five.ROW_ROLE) == len(p.five.ROLE_ROW) == 32,
    )

    print("\nCOMMUTING MULTIPLICATION TABLE")
    rows = tuple(product((0, 1), repeat=5))
    commuting = tuple(
        (left, right)
        for left in rows
        for right in rows
        if not p.algebra.symplectic(left, right)
    )
    check("exact ordered commuting-pair census is 544", len(commuting) == 544, len(commuting))
    check(
        "commutativity quotient gives 288 five-parent canonical rows",
        len(p.CANONICAL_TABLE) == 288
        and Counter(map(len, p.CANONICAL_TABLE)) == {5: 288},
        Counter(map(len, p.CANONICAL_TABLE)),
    )
    check(
        "6,528 raw multiplication rows merge without conflict",
        len(p.MULTIPLY_RAW) == 6_528
        and len(p.MERGED_RAW) == 77_420
        and not p.RAW_CONFLICTS
        and all(len(values) == 1 for values in p.MERGED_RAW.values()),
        (len(commute.MERGED_RAW), len(p.MULTIPLY_RAW), len(p.MERGED_RAW)),
    )
    check(
        "canonical outputs equal signed commuting multiplication",
        all(
            p.CANONICAL_TABLE[p.local(left, right)]
            == p.five.ROW_ROLE[p.algebra.multiply_commuting(left, right)]
            for left, right in commuting
        ),
    )

    print("\nALL PAIRS AND ROTATIONS")
    failures = []
    sizes = set()
    for rotation_index, rotation in enumerate(c53.ROTATIONS):
        for left, right in commuting:
            ok, detail = p.run(left, right, rotation)
            if not ok:
                failures.append((rotation_index, left, right, detail))
            else:
                sizes.add(detail)
    check(
        "all 13,056 rotated commuting products form exactly once",
        not failures and sizes == {29},
        (sizes, failures[:1]),
    )
    attempts, deletion_failures = deletion_controls()
    check(
        "deleting any direct multiplication parent suppresses its output",
        attempts == 1_440 and not deletion_failures,
        (attempts, deletion_failures[:1]),
    )

    print("\nALGEBRAIC PIVOT SUFFICIENCY")
    branch_failures = []
    for state_id in range(60):
        generators = p.algebra.STATE_GENERATORS[state_id]
        for measurement_id in range(15):
            for outcome_bit in (0, 1):
                observed = p.algebra.tableau_measure(generators, measurement_id, outcome_bit)
                probability, target = p.algebra.compiled.BRANCH[(state_id, measurement_id, outcome_bit)]
                if observed != (float(probability), target):
                    branch_failures.append((state_id, measurement_id, outcome_bit, observed, probability, target))
    check(
        "commutation/multiply/pivot algebra reconstructs all 1,800 branches",
        not branch_failures,
        branch_failures[:1],
    )

    print("\nMIXED-DEVICE CLOSURE")
    mixed_failures = []
    for state_id in range(60):
        for events in product(u.EVENTS, repeat=2):
            ok, detail = unified_run(state_id, events)
            if not ok:
                mixed_failures.append((state_id, events, detail))
    check(
        "multiplication rows preserve all 86,640 unified histories",
        not mixed_failures,
        mixed_failures[:1],
    )
    check(
        "Cycle-144 terminal retains exactly its two priced fronts",
        enabled(d.BOUND_TERMINAL) == d.BOUND_IGNORED,
        enabled(d.BOUND_TERMINAL),
    )

    print("\nSCOPE")
    note = " ".join(NOTE.read_text(encoding="utf-8").lower().split()) if NOTE.is_file() else ""
    for phrase in (
        "physical commutation and multiplication atoms",
        "pivot controller remains open",
        "multiplication is still role-level",
        "does not derive occurrence or equal weights",
        "no axiom addition follows",
        "n1 — alternative routes",
        "n8 — cross-cycle echo",
    ):
        check("note contains: " + phrase, phrase in note)

    print("\nTOTAL")
    print("PASS", PASS, "FAIL", FAIL)
    print("RESULT", "PHYSICAL_COMMUTATION_AND_MULTIPLICATION_ATOMS" if FAIL == 0 else "FAIL")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
