#!/usr/bin/env python3
"""Cycle 87: physical one-bit router and Patricia selector reduction.

This is a positive next step toward replacing 198 parallel full comparators.
A supplied strict-NN H0/H1 gate consumes an active H1 token and one physical
H0/H1 candidate bit, then appends exactly one of two H1 branch tokens.  The
gate is composed with the complete Cycle-86 physical raw union and exhausted
under both inputs and all proper-cubic images.

Separately, the exact 198 Cycle-86 row programs are reduced to their binary
prefix and compressed Patricia tries.  This proves a unique serial decision
structure exists, but does not claim that candidate bits have been routed to
all physical trie nodes.  All gate cages and input records are supplied.

Authority: none.  No foundation, queue, audit, or git authority is exercised.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from pathlib import Path

import four_open_reservation_comb_cycle59_2026_07_14 as c59
import official_seed_to_rail_nucleation_cycle53_2026_07_14 as c53
import open_direction_empty_slot_cycle86_2026_07_14 as c86


ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / "docs" / "work_history" / "repo" / "review_feedback"
NOTE = REVIEW / "PHYSICAL_BIT_ROUTER_PATRICIA_SELECTOR_CYCLE87_NOTE_2026-07-14.md"

Coord = tuple[int, int, int]
Signature = c53.Signature
Program = tuple[int, ...]
H0 = "H0"
H1 = "H1"

GATE: Coord = (0, 0, 0)
TOKEN: Coord = (-1, 0, 0)
BIT: Coord = (1, 0, 0)
BRANCH_0: Coord = (0, -1, 0)
BRANCH_1: Coord = (0, 1, 0)
GATE_MARKERS = (H1, H1)  # -z,+z
BRANCH_0_MARKERS = (H0, H0, H1, H1)  # -x,+x,-z,+z
BRANCH_1_MARKERS = (H0, H0, H0, H1)

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


def section(title: str) -> None:
    print("\n" + "=" * 79)
    print(title)
    print("=" * 79)


def source(bit: str) -> dict[Coord, str]:
    assert bit in (H0, H1)
    return {
        TOKEN: H1,
        BIT: bit,
        (0, 0, -1): GATE_MARKERS[0],
        (0, 0, 1): GATE_MARKERS[1],
        (-1, -1, 0): BRANCH_0_MARKERS[0],
        (1, -1, 0): BRANCH_0_MARKERS[1],
        (0, -1, -1): BRANCH_0_MARKERS[2],
        (0, -1, 1): BRANCH_0_MARKERS[3],
        (-1, 1, 0): BRANCH_1_MARKERS[0],
        (1, 1, 0): BRANCH_1_MARKERS[1],
        (0, 1, -1): BRANCH_1_MARKERS[2],
        (0, 1, 1): BRANCH_1_MARKERS[3],
    }


def signature(records: dict[Coord, str], target: Coord) -> Signature:
    return c53.local_signature(records, target)


def build_table() -> dict[Signature, str]:
    table: dict[Signature, str] = {}
    for bit in (H0, H1):
        records = source(bit)
        table[c53.canonical_signature(signature(records, GATE))] = bit
        records[GATE] = bit
        target = BRANCH_0 if bit == H0 else BRANCH_1
        table[c53.canonical_signature(signature(records, target))] = H1
    return table


CANONICAL_TABLE = build_table()
RAW_OUTPUTS = c59.raw_rule_outputs(CANONICAL_TABLE)


def merge_raw() -> dict[Signature, frozenset[str]]:
    outputs: dict[Signature, set[str]] = defaultdict(set)
    for table in (c86.COMBINED_RAW, RAW_OUTPUTS):
        for local, values in table.items():
            outputs[local].update(values)
    return {local: frozenset(values) for local, values in outputs.items()}


COMBINED_RAW = merge_raw()


def enabled_outputs(records: dict[Coord, str]) -> dict[Coord, frozenset[str]]:
    return {
        target: COMBINED_RAW[local]
        for target in c53.open_candidates(records)
        if (local := signature(records, target)) in COMBINED_RAW
    }


def assignments(records: dict[Coord, str]) -> dict[Coord, str]:
    return {
        target: next(iter(values)) if len(values) == 1 else "CONFLICT"
        for target, values in enabled_outputs(records).items()
    }


def canonical_records(records: dict[Coord, str]) -> tuple[tuple[Coord, str], ...]:
    minima = tuple(min(site[axis] for site in records) for axis in range(3))
    return tuple(sorted((tuple(site[axis] - minima[axis] for axis in range(3)), content) for site, content in records.items()))


PROGRAM_TO_ROW = {program: local for local, program in c86.ROW_PROGRAMS.items()}
PROGRAMS = tuple(PROGRAM_TO_ROW)
PREFIXES = frozenset(program[:depth] for program in PROGRAMS for depth in range(49))
CHILD_COUNT = {
    prefix: sum(prefix + (bit,) in PREFIXES for bit in (0, 1))
    for prefix in PREFIXES if len(prefix) < 48
}
BRANCH_PREFIXES = frozenset(prefix for prefix, count in CHILD_COUNT.items() if count == 2)
SIGNIFICANT_PREFIXES = frozenset({()}) | BRANCH_PREFIXES | frozenset(PROGRAMS)


def patricia_edges() -> tuple[tuple[Program, Program], ...]:
    edges = []
    for node in SIGNIFICANT_PREFIXES - {()}:
        parent = max(
            (
                prefix for prefix in SIGNIFICANT_PREFIXES
                if len(prefix) < len(node) and node[:len(prefix)] == prefix
            ),
            key=len,
        )
        edges.append((parent, node))
    return tuple(edges)


PATRICIA_EDGES = patricia_edges()


def classify(program: Program) -> Signature | None:
    return PROGRAM_TO_ROW.get(program)


def gate_contract() -> None:
    section("A - Strict-NN physical one-bit branch gate")
    check("A01 each supplied gate source has twelve H0/H1 records", all(len(source(bit)) == 12 and set(source(bit).values()) == {H0, H1} for bit in (H0, H1)))
    check("A02 gate table has exactly four canonical rows", len(CANONICAL_TABLE) == 4 and sorted(map(len, CANONICAL_TABLE)) == [4, 4, 5, 5])
    check("A03 gate has 51 proper-cubic raw rows", len(RAW_OUTPUTS) == 51)
    overlap = set(RAW_OUTPUTS) & set(c86.COMBINED_RAW)
    check("A04 24 overlaps are safe identical-H1 aliases", len(overlap) == 24 and all(RAW_OUTPUTS[local] == c86.COMBINED_RAW[local] == frozenset((H1,)) for local in overlap))
    check("A05 complete physical union has 4,651 raw rows", len(COMBINED_RAW) == 4_651)
    check("A06 complete physical union is output-single-valued", all(len(values) == 1 for values in COMBINED_RAW.values()))
    check("A07 gate rows consume and write only H0/H1", {content for local in CANONICAL_TABLE for _offset, content in local} | set(CANONICAL_TABLE.values()) == {H0, H1})

    failures = []
    shift = (19, -13, 7)
    for bit in (H0, H1):
        records = source(bit)
        target = BRANCH_0 if bit == H0 else BRANCH_1
        stages = (
            (records, {GATE: bit}),
            ({**records, GATE: bit}, {target: H1}),
            ({**records, GATE: bit, target: H1}, {}),
        )
        canonical = canonical_records(records)
        stabilizer = sum(canonical_records({c53.matvec(rotation, site): content for site, content in records.items()}) == canonical for rotation in c53.ROTATIONS)
        if stabilizer != 1:
            failures.append((bit, "stabilizer", stabilizer))
        for stage_index, (state, expected) in enumerate(stages):
            if assignments(state) != expected:
                failures.append((bit, stage_index, expected, assignments(state)))
            for rotation_index, rotation in enumerate(c53.ROTATIONS):
                transformed = {c53.add(c53.matvec(rotation, site), shift): content for site, content in state.items()}
                transformed_expected = {c53.add(c53.matvec(rotation, site), shift): content for site, content in expected.items()}
                if assignments(transformed) != transformed_expected:
                    failures.append((bit, stage_index, rotation_index, transformed_expected, assignments(transformed)))
    check("A08 both branches have exact three-state/two-edge graphs", not failures, str(failures[:1]))
    check("A09 all 144 transformed stage controls are exact", not failures)


def trie_contract() -> None:
    section("B - Exact 198-program prefix and Patricia selectors")
    check("B01 program bank contains 198 distinct 48-bit leaves", len(PROGRAMS) == len(set(PROGRAMS)) == 198 and all(len(program) == 48 for program in PROGRAMS))
    check("B02 explicit prefix trie has 6,785 nodes and 6,784 edges", len(PREFIXES) == 6_785)
    child_census = Counter(CHILD_COUNT.values())
    check("B03 explicit trie has 197 branch and 6,390 unary nodes", child_census == {1: 6_390, 2: 197}, str(child_census))
    width = Counter(map(len, PREFIXES))
    check("B04 exact maximum trie width is 198 at depths 46-48", max(width.values()) == 198 and {depth for depth, count in width.items() if count == 198} == {46, 47, 48})
    check("B05 compressed Patricia trie has 395 nodes and 394 edges", len(SIGNIFICANT_PREFIXES) == 395 and len(PATRICIA_EDGES) == 394)
    edge_lengths = tuple(len(child) - len(parent) for parent, child in PATRICIA_EDGES)
    check("B06 compressed edge labels total 6,784 bits", sum(edge_lengths) == 6_784)
    check("B07 longest compressed edge label is 42 bits", max(edge_lengths) == 42)
    check("B08 every exact program classifies to its unique selected row", all(classify(program) == local for local, program in c86.ROW_PROGRAMS.items()))
    check("B09 every selected leaf retains its exact output association", all(c86.ROW_PROGRAMS[classify(program)] == program and c86.c81.SELECTED_TABLE[classify(program)] in c86.c81.ROLE_TO_WORD for program in PROGRAMS))

    accepted_flips = 0
    failures = []
    for program in PROGRAMS:
        for index in range(48):
            altered = program[:index] + (1 - program[index],) + program[index + 1:]
            selected = classify(altered)
            if selected is not None:
                accepted_flips += 1
                if c86.ROW_PROGRAMS[selected] != altered:
                    failures.append((program, index, altered, selected))
    check("B10 all 9,504 one-bit perturbations classify exactly or reject", not failures)
    check("B11 exactly 30 directed one-bit flips land on another valid row", accepted_flips == 30)


def disposition_contract() -> None:
    section("C - Positive partial selector and exact physical residual")
    note = NOTE.read_text(encoding="utf-8").lower() if NOTE.is_file() else ""
    for marker in ("*", "`", ">"):
        note = note.replace(marker, "")
    note = " ".join(note.split())
    check("C01 note exists and carries authority none", NOTE.is_file() and "authority: none" in note)
    check("C02 note states every gate input/cage is supplied", "twelve-record gate source is supplied" in note)
    check("C03 note names candidate-bit bus residual", "candidate_bit_bus_to_active_trie_node" in note)
    check("C04 note names physical trie embedding residual", "proper_cubic_patricia_embedding" in note)
    check("C05 note does not call the selector seed-grown", "no seed-grown selector is claimed" in note)
    check("C06 note denies foundation and axiom effects", "no foundation edit" in note and "no axiom addition follows" in note)


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    gate_contract()
    trie_contract()
    disposition_contract()
    print("\nGATE_SOURCE=12 GATE_CANONICAL=4 GATE_RAW=51 PHYSICAL_UNION_RAW=4651")
    print("PREFIX_NODES=6785 PATRICIA_NODES=395 PATRICIA_EDGES=394 LABEL_BITS=6784")
    print(f"SUMMARY: {PASS} PASS / {FAIL} FAIL")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
