#!/usr/bin/env python3
"""Cycle 150: literal-bit ALU and physical symplectic commutation."""

from __future__ import annotations

from collections import Counter
from itertools import product
from pathlib import Path

import physical_symplectic_commutation_circuit_probe_2026_07_15 as p


alu = p.alu
compact = alu.compact
u = compact.unified
d = alu.d
c53 = alu.c53
ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "work_history" / "repo" / "review_feedback" / "LITERAL_BIT_ALU_SYMPLECTIC_COMMUTATION_CYCLE150_NOTE_2026-07-15.md"
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


def deletion_controls(table, raw):
    attempts = 0
    failures = []
    for local, output in table.items():
        for index in range(len(local)):
            attempts += 1
            mutated = local[:index] + local[index + 1:]
            if output in raw.get(mutated, frozenset()):
                failures.append((local, index, output))
    return attempts, tuple(failures)


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0

    print("AUTHORITY AND BOOLEAN BASIS")
    check("review note exists", NOTE.is_file())
    truth_failures = []
    for left, right, operation in product((0, 1), repeat=3):
        expected = (left ^ right) if operation == 0 else (left & right)
        if alu.output(left, right, operation) != expected:
            truth_failures.append((left, right, operation))
    check("XOR/AND truth tables are exact", not truth_failures, truth_failures)
    check(
        "XOR, AND, and recorded one express NOT and OR",
        all((value ^ 1) == (1 - value) for value in (0, 1))
        and all(((left ^ right) ^ (left & right)) == (left | right) for left, right in product((0, 1), repeat=2)),
    )

    print("\nRECURRENT LITERAL-BIT ALU")
    check(
        "eight five-parent rows implement both binary operations",
        len(alu.CANONICAL_TABLE) == 8
        and Counter(map(len, alu.CANONICAL_TABLE)) == {5: 8},
        Counter(map(len, alu.CANONICAL_TABLE)),
    )
    check(
        "192 covariant ALU rows merge conflict-free with Cycle 149",
        len(alu.ALU_RAW) == 192
        and not alu.RAW_CONFLICTS
        and len(alu.MERGED_RAW) == 70_844,
        (len(compact.MERGED_RAW), len(alu.ALU_RAW), len(alu.MERGED_RAW)),
    )
    instructions = tuple(product((0, 1), repeat=2))
    alu_failures = []
    states = edges = 0
    for rotation_index, rotation in enumerate(c53.ROTATIONS):
        for initial in (0, 1):
            for program in product(instructions, repeat=3):
                ok, detail = alu.run(initial, program, rotation)
                if not ok:
                    alu_failures.append((rotation_index, initial, program, detail))
                else:
                    local_states, local_edges, _size, _result = detail
                    states += local_states
                    edges += local_edges
    check(
        "all 3,072 rotated three-instruction programs are exact",
        not alu_failures and states == 12_288 and edges == 9_216,
        (states, edges, alu_failures[:1]),
    )
    alu_deletions, alu_deletion_failures = deletion_controls(alu.CANONICAL_TABLE, p.MERGED_RAW)
    check(
        "deleting any ALU parent suppresses its output",
        alu_deletions == 40 and not alu_deletion_failures,
        (alu_deletions, alu_deletion_failures[:1]),
    )

    print("\nPHYSICAL SYMPLECTIC COMMUTATION")
    check(
        "rotational parity quotient collapses sixteen words to six rows",
        len(p.PARITY_TABLE) == 6
        and Counter(map(len, p.PARITY_TABLE)) == {6: 6},
        Counter(map(len, p.PARITY_TABLE)),
    )
    check(
        "48 parity rows yield a 70,892-row single-valued union",
        len(p.PARITY_RAW) == 48
        and len(p.MERGED_RAW) == 70_892
        and not p.RAW_CONFLICTS
        and all(len(values) == 1 for values in p.MERGED_RAW.values()),
        (len(p.PARITY_RAW), len(p.MERGED_RAW)),
    )
    graph_failures = []
    total_states = total_edges = 0
    rows = tuple(product((0, 1), repeat=5))
    for rotation_index, rotation in enumerate(c53.ROTATIONS):
        for left in rows:
            for right in rows:
                result = p.graph(left, right, rotation)
                if result != (17, 33, 1, 4, ()):
                    graph_failures.append((rotation_index, left, right, result))
                total_states += result[0]
                total_edges += result[1]
    check(
        "all 24,576 signed-row graphs are exact four-AND/parity diamonds",
        not graph_failures
        and total_states == 417_792
        and total_edges == 811_008,
        (total_states, total_edges, graph_failures[:1]),
    )
    check(
        "every output equals the signed-tableau symplectic parity",
        all(
            (p.outputs(left, right)[p.CENTER] == alu.bit(compact.algebra.symplectic(left, right)))
            for left in rows
            for right in rows
        ),
    )
    parity_deletions, parity_deletion_failures = deletion_controls(p.PARITY_TABLE, p.MERGED_RAW)
    check(
        "deleting any parity parent suppresses its output",
        parity_deletions == 36 and not parity_deletion_failures,
        (parity_deletions, parity_deletion_failures[:1]),
    )

    print("\nMIXED-DEVICE CLOSURE")
    mixed_failures = []
    for state_id in range(60):
        for events in product(u.EVENTS, repeat=2):
            ok, detail = unified_run(state_id, events)
            if not ok:
                mixed_failures.append((state_id, events, detail))
    check(
        "ALU/parity rows preserve all 86,640 unified event histories",
        not mixed_failures,
        mixed_failures[:1],
    )
    check(
        "Cycle-144 terminal remains at exactly two priced fronts",
        enabled(d.BOUND_TERMINAL) == d.BOUND_IGNORED,
        enabled(d.BOUND_TERMINAL),
    )

    print("\nSCOPE")
    note = " ".join(NOTE.read_text(encoding="utf-8").lower().split()) if NOTE.is_file() else ""
    for phrase in (
        "literal-bit alu",
        "physical symplectic commutation",
        "commuting multiplication and pivot remain open",
        "does not derive equal outcome weights",
        "no axiom addition follows",
        "n1 — alternative routes",
        "n8 — cross-cycle echo",
    ):
        check("note contains: " + phrase, phrase in note)

    print("\nTOTAL")
    print("PASS", PASS, "FAIL", FAIL)
    print("RESULT", "LITERAL_BIT_ALU_AND_SYMPLECTIC_COMMUTATION" if FAIL == 0 else "FAIL")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
