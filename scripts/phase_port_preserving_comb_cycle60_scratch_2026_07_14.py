#!/usr/bin/env python3
"""Cycle 60 scratch: exact q/a/b/c comb with one fresh b phase port.

This authority-free probe replaces Cycle 59's broad one-E S8 fanout with a
write-once cube-completion marker.  The resulting homogeneous proper-cubic
nearest-neighbour table preserves the open site (2,-1,0), adjacent to b, while
retaining the q/a/b/c reservation order.  The graph follows every legal
asynchronous single-record append from the completed Cycle-57 builder.
"""

from __future__ import annotations

from pathlib import Path

import four_open_reservation_comb_cycle59_2026_07_14 as c59
import full_a_boundary_launcher_last_cycle57_2026_07_14 as c57
import official_seed_to_rail_nucleation_cycle53_2026_07_14 as c53
import strict_nn_record_law_compiler_cycle43_2026_07_14 as c43


ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / "docs" / "work_history" / "repo" / "review_feedback"
NOTE = REVIEW / "PHASE_PORT_PRESERVING_COMB_CYCLE60_SCRATCH_NOTE_2026-07-14.md"

Coord = tuple[int, int, int]
Signature = c53.Signature

EXPECTED_CANONICAL_RULES = 21
EXPECTED_ADDITIONS = 52
EXPECTED_CONDITIONS = 80
EXPECTED_STATES = 242_033
EXPECTED_EDGES = 1_650_121
PHASE_PORT: Coord = (2, -1, 0)

PASS = 0
FAIL = 0


def check(label: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"PASS {label}" + (f" :: {detail}" if detail else ""))
    else:
        FAIL += 1
        print(f"FAIL {label}" + (f" :: {detail}" if detail else ""))


def key(records: dict[Coord, str], site: Coord) -> Signature:
    return c53.canonical_signature(c53.local_signature(records, site))


def build_construction() -> c59.Construction:
    base = dict(c57.BUILDER.completed)
    records = dict(base)
    table: dict[Signature, str] = {}
    allowed: dict[Coord, str] = {}
    stage_aliases: dict[str, tuple[Coord, ...]] = {}

    def install(signature: Signature, output: str) -> None:
        canonical = c53.canonical_signature(signature)
        prior = table.get(canonical)
        if prior is not None and prior != output:
            raise ValueError(f"canonical output conflict: {prior} / {output}")
        table[canonical] = output

    def stage(label: str, representative: Coord) -> None:
        signature = key(records, representative)
        aliases = tuple(c53.signature_classes(records).get(signature, ()))
        if not aliases:
            raise ValueError(f"empty signature class for {label} at {representative}")
        install(signature, label)
        stage_aliases[label] = aliases
        for site in aliases:
            records[site] = label
            allowed[site] = label

    for label, representative in (
        ("START", (-1, 3, 0)),
        ("W1", (-1, 4, 0)),
        ("W2", (0, 3, -1)),
        ("W3", (0, 2, -1)),
        ("W4", (0, 1, -1)),
        ("W5", (0, 0, -1)),
        ("W6", (0, -1, -1)),
        ("J6", (0, -1, -2)),
        ("COMP6", (1, -1, -2)),
        ("S7", (2, -1, -2)),
        ("PAIR", (2, -2, -2)),
        ("ALL", (2, -2, -3)),
        ("R1", (3, -2, -3)),
        ("R2", (3, -2, -2)),
        ("MARK", (3, -1, -2)),
        ("E", (2, 0, -2)),
        ("OPEN_B", (2, 0, -1)),
        ("S8", (3, 0, -2)),
        ("OPEN_C", (3, 0, -1)),
    ):
        stage(label, representative)

    # The two commuting Cycle-59 state-zero/rail diamond rows are retained.
    install(
        (
            ((-1, 0, 0), "A_0_2"),
            ((0, -1, 0), "B_1_2"),
            ((0, 0, -1), "W1"),
        ),
        "B_0_2",
    )
    install(
        (
            ((-1, 0, 0), "B_0_2"),
            ((0, -1, 0), "START"),
        ),
        "W1",
    )

    return c59.Construction(base, table, allowed, stage_aliases, {})


CONSTRUCTION = build_construction()


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0

    table = CONSTRUCTION.table
    allowed = CONSTRUCTION.allowed
    aliases = CONSTRUCTION.stage_aliases
    terminal = dict(CONSTRUCTION.base)
    terminal.update(allowed)

    check("A01 note exists", NOTE.is_file())
    check("A02 base is completed Cycle 57", CONSTRUCTION.base == c57.BUILDER.completed)
    check("A03 table has 21 canonical rows", len(table) == EXPECTED_CANONICAL_RULES)
    check("A04 table is single-valued under all rotations", all(len(v) == 1 for v in c59.raw_rule_outputs(table).values()))
    check("A05 construction has 52 additions", len(allowed) == EXPECTED_ADDITIONS)

    expected_orbits = {
        "PAIR": {(1, -2, -3), (2, -2, -2), (2, -1, -3)},
        "ALL": {(2, -2, -3)},
        "R1": {(2, -3, -3), (2, -2, -4), (3, -2, -3)},
        "R2": {
            (1, -3, -3), (1, -2, -4), (2, -3, -2),
            (2, -1, -4), (3, -2, -2), (3, -1, -3),
        },
        "MARK": {(1, -3, -2), (1, -1, -4), (3, -1, -2)},
        "S8": {
            (0, -3, -2), (0, -1, -4), (1, -3, -1),
            (1, 0, -4), (3, -1, -1), (3, 0, -2),
        },
    }
    for label, expected in expected_orbits.items():
        check(f"B {label} orbit is exact", set(aliases[label]) == expected, str(aliases[label]))

    official = set(c43.official_block_support(c43.Program((0, 0, 0), (1, 0, 0), (0, 1, 0))))
    check("B phase port remains open", PHASE_PORT not in terminal)
    check("B phase port is adjacent to b", c43.manhattan(PHASE_PORT, c59.TARGETS["b"]) == 1)
    check("B additions avoid official support", set(allowed).isdisjoint(official))
    check("B q/a/b/c remain open", all(site not in terminal for site in c59.TARGETS.values()))
    check("B q/a/b/c certificates are exact", all(terminal.get(site) == c59.CERTIFICATE_CONTENTS[name] for name, site in c59.CERTIFICATES.items()))

    prior = c59.CONSTRUCTION
    c59.CONSTRUCTION = CONSTRUCTION
    try:
        conditions = c59.compile_conditions()
        graph = c59.exhaustive_comb_graph()
    finally:
        c59.CONSTRUCTION = prior

    check("C compiled condition count is exact", len(conditions) == EXPECTED_CONDITIONS, str(len(conditions)))
    check("C reachable-state count is exact", graph.states == EXPECTED_STATES, f"{graph.states:,}")
    check("C edge count is exact", graph.edges == EXPECTED_EDGES, f"{graph.edges:,}")
    check("C has one complete terminal", graph.terminals == graph.complete_terminals == 1)
    check("C has no incomplete terminal", graph.incomplete_terminals == 0)
    check("C has no output conflict", graph.conflicts == 0)
    check("C has no parasite", not graph.parasites, str(sorted(graph.parasites)))
    check("C OPEN_C never precedes q/a/b certificates", graph.commit_order_violations == 0)
    check("C OPEN_B never precedes q/a certificates", graph.b_order_violations == 0)

    print(f"\nSUMMARY: {PASS} PASS / {FAIL} FAIL")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
