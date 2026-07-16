#!/usr/bin/env python3
"""Cycle 149: four-generator physical tableau-row machine and tournament."""

from __future__ import annotations

from collections import Counter
from itertools import combinations, product
from pathlib import Path

import cycle48_four_generator_tableau_row_machine_probe_2026_07_15 as p


five = p.five
algebra = p.algebra
u = p.unified
d = five.d
c53 = five.c53
ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "work_history" / "repo" / "review_feedback" / "FOUR_GENERATOR_PHYSICAL_TABLEAU_ROW_MACHINE_CYCLE149_NOTE_2026-07-15.md"
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


def rotated_row_run(record, gates, rotation):
    source, expected = five.apparatus(record, gates)
    shift = (47, -53, 59)
    source = c53.transform_records(source, rotation, shift)
    expected = c53.transform_records(expected, rotation, shift)
    records = dict(source)
    for target, output in expected.items():
        actual = enabled(records)
        wanted = {target: frozenset((output,))}
        if actual != wanted:
            return False, (actual, wanted)
        records[target] = output
    return (not enabled(records), enabled(records))


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


def parent_deletions():
    failures = []
    attempts = 0
    for local, intended in p.CANONICAL_TABLE.items():
        for index in range(len(local)):
            attempts += 1
            mutated = local[:index] + local[index + 1:]
            if intended in p.MERGED_RAW.get(mutated, frozenset()):
                failures.append((local, index, intended))
    return attempts, tuple(failures)


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0

    print("AUTHORITY AND ROW CODE")
    check("review note exists", NOTE.is_file())
    check(
        "thirty-two physical roles encode all signed two-qubit Pauli rows",
        len(five.ROW_ROLE) == len(five.ROLE_ROW) == 32
        and set(five.ROW_ROLE) == set(product((0, 1), repeat=5)),
    )
    check(
        "chosen primitive alphabet is H0,H1,S0,CX01",
        p.KEEP == (0, 1, 2, 4)
        and tuple(five.GATE_ROLE[index] for index in p.KEEP)
        == ("R_A22", "R_B01", "R_B21", "R_C23"),
    )

    print("\nLOCAL PHYSICAL COMPILER")
    check(
        "128 five-parent rows cover every signed row and primitive gate",
        len(p.CANONICAL_TABLE) == 128
        and Counter(map(len, p.CANONICAL_TABLE)) == {5: 128},
        Counter(map(len, p.CANONICAL_TABLE)),
    )
    check(
        "3,072 covariant rows merge conflict-free with the unified machine",
        len(p.ROW_GATE_RAW) == 3_072
        and len(p.MERGED_RAW) == 70_652
        and not p.RAW_CONFLICTS
        and all(len(values) == 1 for values in p.MERGED_RAW.values()),
        (len(u.MERGED_RAW), len(p.ROW_GATE_RAW), len(p.MERGED_RAW)),
    )
    primitive_failures = []
    for rotation_index, rotation in enumerate(c53.ROTATIONS):
        for record in five.ROWS:
            for gate_id in p.KEEP:
                ok, detail = rotated_row_run(record, (gate_id,), rotation)
                if not ok:
                    primitive_failures.append((rotation_index, record, gate_id, detail))
    check(
        "all 3,072 rotated primitive row histories are exact",
        not primitive_failures,
        primitive_failures[:1],
    )
    attempts, deletion_failures = parent_deletions()
    check(
        "deleting any row-gate parent suppresses that update",
        attempts == 640 and not deletion_failures,
        (attempts, deletion_failures[:1]),
    )

    print("\nDECLARED GATE RECONSTRUCTION")
    declared_failures = []
    states = edges = 0
    sizes = set()
    for record in five.ROWS:
        for gate_id in range(7):
            gates = p.DECLARED_WORD[gate_id]
            ok, detail = p.run(record, gates)
            observed = algebra.apply_sequence(record, gates)
            expected = algebra.apply_gate(record, gate_id)
            if not ok or observed != expected:
                declared_failures.append((record, gate_id, detail, observed, expected))
            else:
                local_states, local_edges, size = detail
                states += local_states
                edges += local_edges
                sizes.add(size)
    check(
        "four primitives physically reconstruct all 224 signed-row/gate cases",
        not declared_failures and states == 1_088 and edges == 864
        and sizes == {33, 81, 105, 153},
        (states, edges, sizes, declared_failures[:1]),
    )
    basis_failures = []
    for state_id in range(60):
        for basis in algebra.all_bases(state_id):
            for gate_id in range(7):
                transformed = tuple(
                    algebra.apply_sequence(record, p.DECLARED_WORD[gate_id])
                    for record in basis
                )
                observed = algebra.KEY_STATE[algebra.group_key(*transformed)]
                expected = algebra.clifford.GATE_IMAGE[(state_id, gate_id)]
                if observed != expected:
                    basis_failures.append((state_id, basis, gate_id, observed, expected))
    check(
        "all 2,520 state/basis/gate reconstructions agree",
        not basis_failures,
        basis_failures[:1],
    )

    print("\nBOUNDED GENERATOR TOURNAMENT")
    subset_sizes = {}
    for size in range(1, 6):
        for subset in combinations(range(5), size):
            subset_sizes[subset] = len(p.closure(subset))
    full = subset_sizes[(0, 1, 2, 3, 4)]
    minimal = tuple(
        subset for subset, group_size in subset_sizes.items()
        if group_size == full
        and not any(
            subset_sizes[proper] == full
            for length in range(1, len(subset))
            for proper in combinations(subset, length)
        )
    )
    check("five declared primitives generate the 11,520-element action", full == 11_520, full)
    check(
        "no tested three-generator subset reaches the full action",
        max(size for subset, size in subset_sizes.items() if len(subset) == 3) == 1_152,
        {tuple(p.GATE_NAMES[i] for i in subset): size for subset, size in subset_sizes.items() if len(subset) == 3},
    )
    check(
        "exactly three inclusion-minimal four-generator subsets survive",
        minimal == ((0, 1, 2, 4), (0, 1, 3, 4), (0, 2, 3, 4)),
        tuple(tuple(p.GATE_NAMES[i] for i in subset) for subset in minimal),
    )
    check(
        "S1 is explicitly reconstructed by the eleven-event retained word",
        len(p.S1_WORD) == 11
        and all(
            algebra.apply_sequence(record, p.S1_WORD) == algebra.apply_gate(record, 3)
            for record in five.ROWS
        ),
        p.S1_WORD,
    )

    print("\nMIXED-DEVICE COLLISION CLOSURE")
    mixed_failures = []
    for state_id in range(60):
        for events in product(u.EVENTS, repeat=2):
            ok, detail = unified_run(state_id, events)
            if not ok:
                mixed_failures.append((state_id, events, detail))
    check(
        "new row rows preserve all 86,640 unified event histories",
        not mixed_failures,
        mixed_failures[:1],
    )
    check(
        "Cycle-144 terminal remains at exactly its two priced fronts",
        enabled(d.BOUND_TERMINAL) == d.BOUND_IGNORED,
        enabled(d.BOUND_TERMINAL),
    )

    print("\nSCOPE")
    note = " ".join(NOTE.read_text(encoding="utf-8").lower().split()) if NOTE.is_file() else ""
    for phrase in (
        "four-generator physical tableau-row machine",
        "bounded to subsets of the five declared primitives",
        "not a universal generator minimum",
        "measurement pivot compiler remains open",
        "no axiom addition follows",
        "n1 — alternative routes",
        "n8 — cross-cycle echo",
    ):
        check("note contains: " + phrase, phrase in note)

    print("\nTOTAL")
    print("PASS", PASS, "FAIL", FAIL)
    print("RESULT", "FOUR_GENERATOR_PHYSICAL_TABLEAU_ROW_MACHINE" if FAIL == 0 else "FAIL")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
