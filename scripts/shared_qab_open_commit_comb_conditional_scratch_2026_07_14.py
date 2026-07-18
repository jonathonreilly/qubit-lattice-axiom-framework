#!/usr/bin/env python3
"""Conditional shared q/a/b OPEN--COMMIT comb scratch certificate.

This is intentionally not a state-zero construction.  Its source is the
completed Cycle-57 builder plus eight completed Cycle-52 rail slices.  From
that bounded source, one static proper-cubic exact-nearest-neighbour table
forms role-distinct OPEN and COMMIT records at q, a, and b, then performs the
three designated writes.  Every asynchronous order is exhausted.

The final block keeps the important negative control explicit: installing the
same table at Cycle-57 state zero lets its H0-only START rule hit two official
future-support sites.  A completion gate is therefore still required before
this conditional object can be composed into the live state-zero law.
"""

from __future__ import annotations

from collections import Counter, deque
from dataclasses import dataclass
from pathlib import Path

import auxiliary_pair_completion_gate_cycle54_2026_07_14 as c54
import full_a_boundary_launcher_last_cycle57_2026_07_14 as c57
import official_seed_to_rail_nucleation_cycle53_2026_07_14 as c53
import self_extending_frame_cage_rail_cycle52_2026_07_14 as c52
import strict_nn_record_law_compiler_cycle43_2026_07_14 as c43


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs/work_history/repo/review_feedback/SHARED_QAB_OPEN_COMMIT_COMB_CONDITIONAL_SCRATCH_NOTE_2026-07-14.md"

Coord = tuple[int, int, int]
Signature = c53.Signature
Mask = int
PASS = 0
FAIL = 0

Q: Coord = (0, -1, 0)
A: Coord = (1, 0, 0)
B: Coord = (2, 0, 0)
C: Coord = (3, 0, 0)

OPEN_Q: Coord = (0, -2, 0)
COMMIT_Q: Coord = (0, -1, -1)
OPEN_A: Coord = (1, -1, 0)
COMMIT_A: Coord = (1, 0, -1)
OPEN_B: Coord = (2, -1, 0)
COMMIT_B: Coord = (2, 0, -1)


def section(title: str) -> None:
    print("\n" + "=" * 79 + "\n" + title + "\n" + "=" * 79)


def check(label: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"PASS {label}" + (f" :: {detail}" if detail else ""))
    else:
        FAIL += 1
        print(f"FAIL {label}" + (f" :: {detail}" if detail else ""))


def key(records: dict[Coord, str], target: Coord) -> Signature:
    return c53.canonical_signature(c53.local_signature(records, target))


def source_records() -> dict[Coord, str]:
    records = dict(c57.BUILDER.completed)
    records.update(dict(c57.natural_rail_sequence(8)[:96]))
    return records


@dataclass(frozen=True)
class Construction:
    table: dict[Signature, str]
    allowed: dict[Coord, str]
    completed: dict[Coord, str]


def construction() -> Construction:
    records = source_records()
    table: dict[Signature, str] = {}
    allowed: dict[Coord, str] = {}

    def orbit(target: Coord, output: str) -> None:
        signature = key(records, target)
        aliases = c53.signature_classes(records)[signature]
        table[signature] = output
        for site in aliases:
            records[site] = output
            allowed[site] = output

    def one(target: Coord, output: str) -> None:
        signature = key(records, target)
        aliases = c53.signature_classes(records)[signature]
        if aliases != [target]:
            raise RuntimeError(f"{output} is not singleton: {aliases}")
        table[signature] = output
        records[target] = output
        allowed[target] = output

    # Common late orbits, reached only in the conditional eight-slice source.
    orbit((0, -1, 2), "START")
    orbit((0, -1, 1), "QARM")
    orbit((0, -2, 1), "TIER")

    # q OPEN arm.  Every two-parent step has its alternate common target
    # already occupied, so no coordinate selector is used.
    one((-1, -1, 1), "ASYM")
    one((-1, -2, 1), "LEFT")
    one((-1, -1, 0), "SIDE")
    one((-1, -2, 0), "LOWLEFT")
    one(OPEN_Q, "OPEN_Q")

    # The TIER+TIER completion orbit includes seven harmless common joins.
    orbit((1, -2, 1), "JOINT_QA")
    one((1, -2, 0), "LOWER_A")
    one(OPEN_A, "OPEN_A")

    # Mirrored lower zipper produces q COMMIT and then the a cage.
    one((-1, 1, -1), "ASYM_Z")
    one((-1, 0, -1), "ZSIDE")
    one((-1, -1, -1), "MID")
    one((-1, -2, -1), "N1")
    one((0, -2, -1), "CAGE_Q")
    one(COMMIT_Q, "COMMIT_Q")
    one((1, -2, -1), "N1_A")
    one((1, -1, -1), "CAGE_A")

    # COMMIT_A must precede M0.  The opposite order creates a real race in
    # which the later CAP0 input can mistype COMMIT_A.  This dependency is the
    # schedule-safe repaired order.
    one(COMMIT_A, "COMMIT_A")
    one((0, 0, -1), "M0")

    # Designated writes: each exact input contains its corresponding COMMIT.
    one(Q, "VALUE_Q")
    one(A, "VALUE_A")

    # A lower cap and one common two-site shell advance the shared comb to b.
    one((0, 0, -2), "CAP0")
    one((0, -1, -2), "CAP_Q")
    one((1, -1, -2), "CAP_A")
    orbit((2, -1, -2), "SHELL_A")
    orbit((2, -1, -1), "CAGE_B")
    one((2, -2, -1), "N1_B")
    one((2, -2, 0), "LOWER_B")
    one((2, -2, 1), "JOINT_B")
    one((2, -1, 1), "TIER_B")
    one(COMMIT_B, "COMMIT_B")
    one(OPEN_B, "OPEN_B")
    one(B, "VALUE_B")

    return Construction(table, allowed, records)


CONSTRUCTION = construction()


def raw_outputs(table: dict[Signature, str]) -> dict[Signature, set[str]]:
    outputs: dict[Signature, set[str]] = {}
    for signature, output in table.items():
        for rotation in c53.ROTATIONS:
            raw = c53.rotate_signature(signature, rotation)
            outputs.setdefault(raw, set()).add(output)
    return outputs


@dataclass(frozen=True)
class Graph:
    states: frozenset[Mask]
    edges: int
    terminals: tuple[Mask, ...]
    parasites: frozenset[tuple[Coord, str]]
    conflicts: frozenset[tuple[Mask, Coord, tuple[str, ...]]]
    sites: tuple[Coord, ...]


def exhaustive_graph() -> Graph:
    """Compile exact local inputs to masks and exhaust every append order."""

    base = source_records()
    table = CONSTRUCTION.table
    allowed = CONSTRUCTION.allowed
    sites = tuple(sorted(allowed))
    site_index = {site: index for index, site in enumerate(sites)}
    occupied_universe = set(base) | set(allowed)
    candidates = {
        c53.add(site, direction)
        for site in occupied_universe
        for direction in c53.DIRECTIONS
        if c53.add(site, direction) not in base
    }
    raw_rules = {
        (c53.rotate_signature(signature, rotation), output)
        for signature, output in table.items()
        for rotation in c53.ROTATIONS
    }

    conditions: set[tuple[int, int, int, str, Coord]] = set()
    for target in candidates:
        for signature, output in raw_rules:
            expected = dict(signature)
            present = 0
            absent = 0
            viable = True
            for direction in c53.DIRECTIONS:
                neighbor = c53.add(target, direction)
                wanted = expected.get(direction)
                if neighbor in base:
                    if wanted != base[neighbor]:
                        viable = False
                        break
                elif neighbor in allowed:
                    bit = 1 << site_index[neighbor]
                    if wanted is None:
                        absent |= bit
                    elif wanted == allowed[neighbor]:
                        present |= bit
                    else:
                        viable = False
                        break
                elif wanted is not None:
                    viable = False
                    break
            if not viable:
                continue
            target_bit = 1 << site_index[target] if target in allowed else 0
            if target_bit:
                absent |= target_bit
            conditions.add((present, absent, target_bit, output, target))

    queue = deque((0,))
    seen = {0}
    terminals: list[Mask] = []
    parasites: set[tuple[Coord, str]] = set()
    conflicts: set[tuple[Mask, Coord, tuple[str, ...]]] = set()
    edges = 0
    ordered = tuple(conditions)
    while queue:
        mask = queue.popleft()
        writes: dict[Coord, set[tuple[int, str]]] = {}
        for present, absent, target_bit, output, target in ordered:
            if mask & present == present and not mask & absent:
                writes.setdefault(target, set()).add((target_bit, output))
        if not writes:
            terminals.append(mask)
        for target, choices in writes.items():
            outputs = tuple(sorted({output for _, output in choices}))
            if len(outputs) != 1:
                conflicts.add((mask, target, outputs))
                continue
            target_bit, output = next(iter(choices))
            edges += 1
            if not target_bit or allowed.get(target) != output:
                parasites.add((target, output))
                continue
            future = mask | target_bit
            if future not in seen:
                seen.add(future)
                queue.append(future)

    return Graph(
        frozenset(seen), edges, tuple(terminals), frozenset(parasites),
        frozenset(conflicts), sites,
    )


def main() -> int:
    section("A - Conditional boundary and exact static table")
    check("A note exists", NOTE.is_file())
    check("A source is completed Cycle57 plus exactly eight rail slices", len(source_records()) == len(c57.BUILDER.completed) + 96)
    check("A static table has thirty-five canonical inputs", len(CONSTRUCTION.table) == 35)
    check("A declared conditional footprint has fifty-two additions", len(CONSTRUCTION.allowed) == 52)
    check("A q/a/b OPEN records are role-distinct", {CONSTRUCTION.allowed[site] for site in (OPEN_Q, OPEN_A, OPEN_B)} == {"OPEN_Q", "OPEN_A", "OPEN_B"})
    check("A q/a/b COMMIT records are role-distinct", {CONSTRUCTION.allowed[site] for site in (COMMIT_Q, COMMIT_A, COMMIT_B)} == {"COMMIT_Q", "COMMIT_A", "COMMIT_B"})

    raw = raw_outputs(CONSTRUCTION.table)
    check("A every proper-cubic raw input is single-valued", all(len(outputs) == 1 for outputs in raw.values()))
    check("A table has no raw Cycle52 input collision", not (set(raw) & set(c52.RULE_OUTPUTS)))
    check("A table has no raw Cycle57-builder input collision", not (set(raw) & set(c57.raw_builder_outputs())))

    section("B - Support, target, and commit geometry")
    program = c43.Program((0, 0, 0), (1, 0, 0), (0, 1, 0))
    official = set(c43.official_block_support(program))
    check("B only designated q/a/b writes occupy official support", set(CONSTRUCTION.allowed) & official == {Q, A, B})
    check("B c remains open", C not in CONSTRUCTION.allowed and C not in source_records())
    rail32 = {site for site, _ in c57.natural_rail_sequence(32)}
    check("B auxiliary footprint avoids thirty-two rail slices", not ((set(CONSTRUCTION.allowed) - {Q, A, B}) & rail32))
    for name, target, opened, committed in (
        ("q", Q, OPEN_Q, COMMIT_Q),
        ("a", A, OPEN_A, COMMIT_A),
        ("b", B, OPEN_B, COMMIT_B),
    ):
        check(f"B {name} OPEN is adjacent to target", opened in c52.neighbors(target))
        check(f"B {name} COMMIT is adjacent to target", committed in c52.neighbors(target))
        local = c53.local_signature(CONSTRUCTION.completed, target)
        contents = {content for _, content in local}
        check(f"B {name} target input contains its OPEN", f"OPEN_{name.upper()}" in contents)
        check(f"B {name} target input contains its COMMIT", f"COMMIT_{name.upper()}" in contents)

    section("C - Exhaustive asynchronous graph")
    graph = exhaustive_graph()
    all_mask = (1 << len(graph.sites)) - 1
    check("C graph has exact reachable-state census", len(graph.states) == 71425, str(len(graph.states)))
    check("C graph has exact directed-edge census", graph.edges == 405708, str(graph.edges))
    check("C every schedule joins one complete terminal", graph.terminals == (all_mask,), str(Counter(mask.bit_count() for mask in graph.terminals)))
    check("C graph has no parasite write", not graph.parasites, str(sorted(graph.parasites)))
    check("C graph has no output conflict", not graph.conflicts)
    index = {site: bit for bit, site in enumerate(graph.sites)}
    for name, target, opened, committed in (
        ("q", Q, OPEN_Q, COMMIT_Q),
        ("a", A, OPEN_A, COMMIT_A),
        ("b", B, OPEN_B, COMMIT_B),
    ):
        value_bit = 1 << index[target]
        open_bit = 1 << index[opened]
        commit_bit = 1 << index[committed]
        check(
            f"C {name} VALUE never precedes OPEN or COMMIT",
            all(not mask & value_bit or mask & open_bit and mask & commit_bit for mask in graph.states),
        )

    section("D - Quiescence, recurrence, and the state-zero blocker")
    completed = dict(CONSTRUCTION.completed)
    check("D conditional terminal is quiescent under its own table", c54.enabled(completed, CONSTRUCTION.table) == {})
    recurrence = []
    for step in range(108):
        if c54.enabled(completed, CONSTRUCTION.table):
            recurrence.append(step)
            break
        enabled = c52.enabled_assignments(completed)
        if len(enabled) != 1:
            recurrence.append(step)
            break
        target, output = next(iter(enabled.items()))
        completed[target] = output
    check("D no reservation-rule recurrence through 108 more rail writes", not recurrence)

    initial = c54.enabled(c57.source_records(), CONSTRUCTION.table)
    leaks = {(site, output) for site, output in initial.items() if site in official}
    check("D state-zero installation has the exact two known support leaks", leaks == {((1, 0, 2), "START"), ((1, 2, 0), "START")}, str(sorted(leaks)))
    check("D conditional table is therefore not a live state-zero closure", bool(leaks))

    section("TOTAL")
    print(f"PASS={PASS} FAIL={FAIL}")
    print("RESULT: " + ("PASS" if FAIL == 0 else "FAIL"))
    print(
        "BOUNDARY: q/a/b OPEN--COMMIT--VALUE is schedule-safe only after "
        "Cycle57 plus eight rail slices; a state-zero completion gate and c remain open"
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
