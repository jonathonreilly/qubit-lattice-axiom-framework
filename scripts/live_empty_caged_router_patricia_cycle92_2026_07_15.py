#!/usr/bin/env python3
"""Cycle 92: corrected EMPTY encoder, caged bit router, and Patricia inventory.

The Cycle-86 open-port sensor is rebuilt against Cycle 90's live 5,452-row
compiler law.  Cycle 87's all-H branch gate is not reused: its rows parasitize
real pipeline geometry.  A two-guard cage repairs that leak.  The open sensor is exhausted
over every asynchronous schedule, every proper-cubic image, and one recorded
extra neighbour drawn from the complete 153-role live alphabet.  The physical
gate is exhausted on both bits and all proper-cubic images.  Finally the exact
236 live programs are reduced to their explicit and compressed binary tries,
including every one-bit perturbation.

Authority: none.  The 59-record EMPTY source and twelve-record gate sources
are supplied, not seed-grown.
"""

from __future__ import annotations

from collections import Counter, defaultdict, deque
from pathlib import Path

import four_open_reservation_comb_cycle59_2026_07_14 as c59
import live_directional_program_writer_cycle90_2026_07_15 as c90
import live_eight_bit_physical_comparator_cycle89_2026_07_15 as c89
import official_seed_to_rail_nucleation_cycle53_2026_07_14 as c53


ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / "docs" / "work_history" / "repo" / "review_feedback"
NOTE = REVIEW / "LIVE_EMPTY_CAGED_ROUTER_PATRICIA_CYCLE92_NOTE_2026-07-15.md"

Coord = tuple[int, int, int]
Signature = c53.Signature
Program = tuple[int, ...]
H0 = "H0"
H1 = "H1"
EMPTY_WORD: c89.Word = c89.EMPTY_WORD
PASS = 0
FAIL = 0

# Open-direction encoder geometry.
SENSOR: Coord = (-1, 0, 0)
MONITORED_PORT: Coord = (-2, 0, 0)
COMPARATOR_START: Coord = (-1, 1, 0)
CANDIDATE: tuple[Coord, ...] = tuple((index, 0, 0) for index in range(8))
REFERENCE: tuple[Coord, ...] = tuple((index, 2, 0) for index in range(8))
CERTIFICATE: tuple[Coord, ...] = tuple((index, 1, 0) for index in range(8))
SENSOR_MARKERS = (H0, H1, H0, H1)
WIRE_MARKERS = (H0, H0, H0)
PORT_MARKERS = (H0, H0, H1, H1, H1)
START_BLOCKERS = {(-1, 1, -1): H1, (-1, 1, 1): H1}

# One-bit branch gate geometry.  T_G0/T_G1/T_H0 are already-live Cycle-85
# bridge-guide roles.  One asymmetric guide in each target cage removes the
# Cycle-87 all-H parasite while retaining a trivial proper-cubic stabilizer.
# Every new gate row contains a guide, so it cannot fire in an all-H pipeline.
GATE: Coord = (0, 0, 0)
TOKEN: Coord = (-1, 0, 0)
BIT: Coord = (1, 0, 0)
BRANCH_0: Coord = (0, -1, 0)
BRANCH_1: Coord = (0, 1, 0)
GATE_GUARD = "T_G0"
BRANCH_0_GUARD = "T_G1"
BRANCH_1_GUARD = "T_H0"
GUARD_ROLES = frozenset((GATE_GUARD, BRANCH_0_GUARD, BRANCH_1_GUARD))
GATE_MARKERS = (GATE_GUARD, H1)
BRANCH_0_MARKERS = (BRANCH_0_GUARD, H0, H1, H1)
BRANCH_1_MARKERS = (BRANCH_1_GUARD, H0, H0, H1)
OLD_GATE_MARKERS = (H1, H1)
OLD_BRANCH_0_MARKERS = (H0, H0, H1, H1)
OLD_BRANCH_1_MARKERS = (H0, H0, H0, H1)


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


def signature(records: dict[Coord, str], target: Coord) -> Signature:
    return c53.local_signature(records, target)


def canonical_records(records: dict[Coord, str]) -> tuple[tuple[Coord, str], ...]:
    minima = tuple(min(site[axis] for site in records) for axis in range(3))
    return tuple(sorted(
        (tuple(site[axis] - minima[axis] for axis in range(3)), content)
        for site, content in records.items()
    ))


def transform(records: dict[Coord, str], rotation: c53.Matrix, shift: Coord) -> dict[Coord, str]:
    return {c53.add(c53.matvec(rotation, site), shift): content for site, content in records.items()}


def merge_raw(*tables: dict[Signature, frozenset[str]]) -> dict[Signature, frozenset[str]]:
    outputs: dict[Signature, set[str]] = defaultdict(set)
    for table in tables:
        for local, values in table.items():
            outputs[local].update(values)
    return {local: frozenset(values) for local, values in outputs.items()}


def enabled(records: dict[Coord, str], raw: dict[Signature, frozenset[str]]) -> dict[Coord, frozenset[str]]:
    return {
        target: raw[local]
        for target in c53.open_candidates(records)
        if (local := signature(records, target)) in raw
    }


def assignments(records: dict[Coord, str], raw: dict[Signature, frozenset[str]]) -> dict[Coord, str]:
    return {
        target: next(iter(values)) if len(values) == 1 else "CONFLICT"
        for target, values in enabled(records, raw).items()
    }


def empty_source(extra: str | None = None) -> dict[Coord, str]:
    records: dict[Coord, str] = {
        (-1, -1, 0): SENSOR_MARKERS[0],
        COMPARATOR_START: SENSOR_MARKERS[1],
        (-1, 0, -1): SENSOR_MARKERS[2],
        (-1, 0, 1): SENSOR_MARKERS[3],
        **START_BLOCKERS,
        (-3, 0, 0): PORT_MARKERS[0],
        (-2, -1, 0): PORT_MARKERS[1],
        (-2, 1, 0): PORT_MARKERS[2],
        (-2, 0, -1): PORT_MARKERS[3],
        (-2, 0, 1): PORT_MARKERS[4],
    }
    for index in range(8):
        records[REFERENCE[index]] = H1
        records[(index, 1, 1)] = H0
        records[(index, 1, -1)] = H1
        records[(index, -1, 0)] = WIRE_MARKERS[0]
        records[(index, 0, -1)] = WIRE_MARKERS[1]
        records[(index, 0, 1)] = WIRE_MARKERS[2]
    if extra is not None:
        records[MONITORED_PORT] = extra
    return records


def build_empty_table() -> dict[Signature, str]:
    records = empty_source()
    table = {c53.canonical_signature(signature(records, SENSOR)): H1}
    records[SENSOR] = H1
    table[c53.canonical_signature(signature(records, CANDIDATE[0]))] = H1
    return table


EMPTY_TABLE = build_empty_table()
EMPTY_RAW = c59.raw_rule_outputs(EMPTY_TABLE)
EMPTY_COMBINED_RAW = merge_raw(c90.COMBINED_RAW, EMPTY_RAW)
EMPTY_ALLOWED: dict[Coord, str] = {
    SENSOR: H1,
    **{site: H1 for site in CANDIDATE},
    **{site: H1 for site in CERTIFICATE},
}


def empty_records(state: frozenset[Coord], extra: str | None = None) -> dict[Coord, str]:
    records = empty_source(extra)
    records.update({site: EMPTY_ALLOWED[site] for site in state})
    return records


def empty_graph() -> tuple[frozenset[frozenset[Coord]], int, tuple[frozenset[Coord], ...], tuple[tuple, ...], int]:
    initial: frozenset[Coord] = frozenset()
    queue = deque((initial,))
    seen = {initial}
    terminals: list[frozenset[Coord]] = []
    parasites: list[tuple] = []
    edges = 0
    maximum = 0
    while queue:
        state = queue.popleft()
        outputs = enabled(empty_records(state), EMPTY_COMBINED_RAW)
        maximum = max(maximum, len(outputs))
        if not outputs:
            terminals.append(state)
        for target, values in outputs.items():
            if len(values) != 1 or EMPTY_ALLOWED.get(target) != next(iter(values)):
                parasites.append((state, target, values))
                continue
            future = state | {target}
            edges += 1
            if future not in seen:
                seen.add(future)
                queue.append(future)
    return frozenset(seen), edges, tuple(terminals), tuple(parasites), maximum


def gate_source(bit: str) -> dict[Coord, str]:
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


def old_gate_source(bit: str) -> dict[Coord, str]:
    """Exact historical Cycle-87 all-H cage, retained only as a regression."""

    assert bit in (H0, H1)
    return {
        TOKEN: H1,
        BIT: bit,
        (0, 0, -1): OLD_GATE_MARKERS[0],
        (0, 0, 1): OLD_GATE_MARKERS[1],
        (-1, -1, 0): OLD_BRANCH_0_MARKERS[0],
        (1, -1, 0): OLD_BRANCH_0_MARKERS[1],
        (0, -1, -1): OLD_BRANCH_0_MARKERS[2],
        (0, -1, 1): OLD_BRANCH_0_MARKERS[3],
        (-1, 1, 0): OLD_BRANCH_1_MARKERS[0],
        (1, 1, 0): OLD_BRANCH_1_MARKERS[1],
        (0, 1, -1): OLD_BRANCH_1_MARKERS[2],
        (0, 1, 1): OLD_BRANCH_1_MARKERS[3],
    }


def build_gate_table() -> dict[Signature, str]:
    table: dict[Signature, str] = {}
    for bit in (H0, H1):
        records = gate_source(bit)
        table[c53.canonical_signature(signature(records, GATE))] = bit
        records[GATE] = bit
        target = BRANCH_0 if bit == H0 else BRANCH_1
        table[c53.canonical_signature(signature(records, target))] = H1
    return table


def build_old_gate_table() -> dict[Signature, str]:
    table: dict[Signature, str] = {}
    for bit in (H0, H1):
        records = old_gate_source(bit)
        table[c53.canonical_signature(signature(records, GATE))] = bit
        records[GATE] = bit
        target = BRANCH_0 if bit == H0 else BRANCH_1
        table[c53.canonical_signature(signature(records, target))] = H1
    return table


GATE_TABLE = build_gate_table()
GATE_RAW = c59.raw_rule_outputs(GATE_TABLE)
COMBINED_RAW = merge_raw(EMPTY_COMBINED_RAW, GATE_RAW)
OLD_GATE_TABLE = build_old_gate_table()
OLD_GATE_RAW = c59.raw_rule_outputs(OLD_GATE_TABLE)
OLD_GATE_COMBINED_RAW = merge_raw(EMPTY_COMBINED_RAW, OLD_GATE_RAW)


PROGRAM_TO_ROW = {program: local for local, program in c90.ROW_PROGRAMS.items()}
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
            (prefix for prefix in SIGNIFICANT_PREFIXES if len(prefix) < len(node) and node[:len(prefix)] == prefix),
            key=len,
        )
        edges.append((parent, node))
    return tuple(edges)


PATRICIA_EDGES = patricia_edges()


def classify(program: Program) -> Signature | None:
    return PROGRAM_TO_ROW.get(program)


def empty_table_contract() -> None:
    section("A - Live open-direction to physical EMPTY word")
    check("A01 EMPTY remains reserved all-one word", EMPTY_WORD == (1,) * 8 and EMPTY_WORD in c89.RESERVED_WORDS and EMPTY_WORD not in c89.WORD_TO_ROLE)
    check("A02 source has exactly 59 supplied H0/H1 records", len(empty_source()) == 59 and set(empty_source().values()) == {H0, H1})
    check("A03 monitored port and all seventeen additions start open", MONITORED_PORT not in empty_source() and set(EMPTY_ALLOWED).isdisjoint(empty_source()))
    check("A04 sensor has four transverse records and two axial openings", len(signature(empty_source(), SENSOR)) == 4 and {c53.add(SENSOR, (-1, 0, 0)), c53.add(SENSOR, (1, 0, 0))} == {MONITORED_PORT, CANDIDATE[0]})
    check("A05 EMPTY table has two arity-four canonical rows and 36 raw rows", len(EMPTY_TABLE) == 2 and set(map(len, EMPTY_TABLE)) == {4} and set(EMPTY_TABLE.values()) == {H1} and len(EMPTY_RAW) == 36)
    check("A06 EMPTY rows are disjoint from corrected Cycle-90 union", set(EMPTY_RAW).isdisjoint(c90.COMBINED_RAW))
    check("A07 EMPTY union has 5,488 single-valued raw rows", len(EMPTY_COMBINED_RAW) == 5_488 and all(len(values) == 1 for values in EMPTY_COMBINED_RAW.values()))
    canonical = canonical_records(empty_source())
    stabilizer = sum(canonical_records({c53.matvec(rotation, site): content for site, content in empty_source().items()}) == canonical for rotation in c53.ROTATIONS)
    check("A08 supplied EMPTY source has trivial proper-cubic stabilizer", stabilizer == 1)


def empty_exhaustive_contract() -> frozenset[frozenset[Coord]]:
    section("B - Asynchronous, extra-neighbour, and covariance controls")
    states, edges, terminals, parasites, maximum = empty_graph()
    check("B01 graph has 46 states and 73 append edges", len(states) == 46 and edges == 73, str((len(states), edges)))
    check("B02 graph has one complete seventeen-record terminal", len(terminals) == 1 and terminals[0] == frozenset(EMPTY_ALLOWED))
    check("B03 graph has no parasite or output conflict", not parasites, str(parasites[:1]))
    check("B04 no state enables more than candidate plus comparator", maximum == 2)
    profiles = Counter((SENSOR in state, sum(site in state for site in CANDIDATE), sum(site in state for site in CERTIFICATE)) for state in states)
    expected = Counter({(False, 0, 0): 1})
    expected.update({(True, candidate_count, certificate_count): 1 for candidate_count in range(9) for certificate_count in range(candidate_count + 1)})
    check("B05 states are exactly sensor then 0<=certificate<=candidate<=8", profiles == expected, str(profiles - expected))
    check("B06 terminal candidate and certificate are physical all-one words", all(site in terminals[0] for site in CANDIDATE + CERTIFICATE))
    check("B07 monitored port is never naturally writable", all(MONITORED_PORT not in enabled(empty_records(state), EMPTY_COMBINED_RAW) for state in states))

    extra_contents = tuple(sorted(c89.FULL_ROLES)) + ("FOREIGN_CONTROL",)
    failures = []
    shift = (47, -29, 13)
    for extra in extra_contents:
        records = empty_source(extra)
        if assignments(records, EMPTY_COMBINED_RAW):
            failures.append(("base", extra, assignments(records, EMPTY_COMBINED_RAW)))
        for rotation_index, rotation in enumerate(c53.ROTATIONS):
            transformed = transform(records, rotation, shift)
            if assignments(transformed, EMPTY_COMBINED_RAW):
                failures.append((rotation_index, extra, assignments(transformed, EMPTY_COMBINED_RAW)))
    check("B08 all 3,850 one-extra-neighbour controls are quiet", len(extra_contents) * 25 == 3_850 and not failures, str(failures[:1]))
    check("B09 every one of 153 live roles blocks EMPTY formation", all(not assignments(empty_source(extra), EMPTY_COMBINED_RAW) for extra in c89.FULL_ROLES))

    covariance_failures = []
    for rotation_index, rotation in enumerate(c53.ROTATIONS):
        for state in states:
            records = empty_records(state)
            expected_outputs = assignments(records, EMPTY_COMBINED_RAW)
            transformed = transform(records, rotation, shift)
            transformed_expected = transform(expected_outputs, rotation, shift)
            actual = assignments(transformed, EMPTY_COMBINED_RAW)
            if actual != transformed_expected:
                covariance_failures.append((rotation_index, state, transformed_expected, actual))
    check("B10 all 1,104 rotated reachable states have exact frontier", len(states) * 24 == 1_104 and not covariance_failures, str(covariance_failures[:1]))
    return states


def gate_contract() -> None:
    section("C - Three-guide caged physical one-bit branch gate")
    check("C01 each gate source has twelve supplied records", all(len(gate_source(bit)) == 12 for bit in (H0, H1)))
    check("C02 all three guard roles already belong to the live alphabet", GUARD_ROLES <= c89.FULL_ROLES)
    check("C03 gate has four canonical and 84 raw rows", len(GATE_TABLE) == 4 and sorted(map(len, GATE_TABLE)) == [4, 4, 5, 5] and len(GATE_RAW) == 84)
    overlap = set(GATE_RAW) & set(EMPTY_COMBINED_RAW)
    check("C04 caged gate raw domain is disjoint from the prior union", not overlap)
    check("C05 complete live compiler union has 5,572 raw rows", len(COMBINED_RAW) == 5_572)
    check("C06 complete live compiler union is output-single-valued", all(len(values) == 1 for values in COMBINED_RAW.values()))
    check("C07 every gate row contains a non-H guide marker", all(any(content in GUARD_ROLES for _offset, content in local) for local in GATE_RAW))
    check("C08 gate outputs remain physical H0/H1", set(GATE_TABLE.values()) == {H0, H1})

    failures = []
    shift = (19, -13, 7)
    transformed_count = 0
    for bit in (H0, H1):
        records = gate_source(bit)
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
            if assignments(state, COMBINED_RAW) != expected:
                failures.append((bit, stage_index, expected, assignments(state, COMBINED_RAW)))
            for rotation_index, rotation in enumerate(c53.ROTATIONS):
                transformed_count += 1
                transformed = transform(state, rotation, shift)
                transformed_expected = transform(expected, rotation, shift)
                actual = assignments(transformed, COMBINED_RAW)
                if actual != transformed_expected:
                    failures.append((bit, stage_index, rotation_index, transformed_expected, actual))
    check("C09 both branch graphs and cage stabilizers are exact", not failures, str(failures[:1]))
    check("C10 all 144 transformed gate stages are exact", transformed_count == 144 and not failures)


def mixed_pipeline_contract() -> None:
    section("D - Mixed-pipeline parasite repair and exhaustive separation")
    content_failures = []
    equal_states = perturbation_states = 0
    for local, output in c89.LIVE_TABLE.items():
        program = c90.ROW_PROGRAMS[local]
        output_word = c89.ROLE_TO_WORD[output]
        for certificate_count in range(49):
            records = c90.pipeline_records(program, program, output_word, certificate_count)
            equal_states += 1
            if not set(records.values()) <= {H0, H1}:
                content_failures.append((output, "compare", certificate_count))
        for output_step in range(1, 18):
            records = c90.pipeline_records(program, program, output_word, 48, output_step)
            equal_states += 1
            if not set(records.values()) <= {H0, H1}:
                content_failures.append((output, "write", output_step))
        for index in range(48):
            altered = program[:index] + (1 - program[index],) + program[index + 1:]
            prefix = c90.common_prefix(altered, program)
            records = c90.pipeline_records(altered, program, output_word, prefix)
            perturbation_states += 1
            if not set(records.values()) <= {H0, H1}:
                content_failures.append((output, "perturb", index))
    check("D01 all 15,576 equal-program pipeline states are all-H", equal_states == 236 * 66 == 15_576 and not content_failures, str(content_failures[:1]))
    check("D02 all 11,328 one-bit stopped contexts are all-H", perturbation_states == 236 * 48 == 11_328 and not content_failures, str(content_failures[:1]))
    check("D03 caged rows are impossible in all 26,904 contexts", all(any(content in GUARD_ROLES for _offset, content in local) for local in GATE_RAW) and not content_failures)
    check("D04 content separation survives every proper-cubic image", all(GUARD_ROLES.isdisjoint({content for content in records.values()}) for records in (c90.pipeline_records(c90.ROW_PROGRAMS[local], c90.ROW_PROGRAMS[local], c89.ROLE_TO_WORD[output], 0) for local, output in c89.LIVE_TABLE.items())))

    # Directly re-run the concrete arity-five R_LB context which exposes the
    # historical all-H gate failure, then verify the caged replacement.
    r_lb_local = next(local for local, output in c89.LIVE_TABLE.items() if output == "R_LB")
    program = c90.ROW_PROGRAMS[r_lb_local]
    output_word = c89.ROLE_TO_WORD["R_LB"]
    initial = c90.pipeline_records(program, program, output_word, 0)
    baseline_initial = assignments(initial, EMPTY_COMBINED_RAW)
    old_initial = assignments(initial, OLD_GATE_COMBINED_RAW)
    old_extras = {site: output for site, output in old_initial.items() if site not in baseline_initial}
    check("D05 old all-H gate creates 32 immediate R_LB parasites", len(old_extras) == 32 and Counter(old_extras.values()) == {H0: 24, H1: 8}, str(Counter(old_extras.values())))

    old_failures = 0
    for certificate_count in range(49):
        records = c90.pipeline_records(program, program, output_word, certificate_count)
        old_failures += assignments(records, OLD_GATE_COMBINED_RAW) != assignments(records, EMPTY_COMBINED_RAW)
    for output_step in range(1, 18):
        records = c90.pipeline_records(program, program, output_word, 48, output_step)
        old_failures += assignments(records, OLD_GATE_COMBINED_RAW) != assignments(records, EMPTY_COMBINED_RAW)
    check("D06 old all-H gate corrupts exactly 63 of 66 R_LB states", old_failures == 63)

    failures = []
    states = 0
    for certificate_count in range(49):
        records = c90.pipeline_records(program, program, output_word, certificate_count)
        before = assignments(records, c90.COMBINED_RAW)
        after = assignments(records, COMBINED_RAW)
        states += 1
        if after != before:
            failures.append(("compare", certificate_count, before, after))
    for output_step in range(1, 18):
        records = c90.pipeline_records(program, program, output_word, 48, output_step)
        before = assignments(records, c90.COMBINED_RAW)
        after = assignments(records, COMBINED_RAW)
        states += 1
        if after != before:
            failures.append(("write", output_step, before, after))
    check("D07 repaired R_LB mixed pipeline preserves all 66 frontiers", states == 66 and not failures, str(failures[:1]))


def trie_and_perturbation_contract() -> None:
    section("E - Corrected 236-program serial/Patricia selector inventory")
    check("E01 bank has 236 distinct 48-bit leaves", len(PROGRAMS) == len(set(PROGRAMS)) == 236 and all(len(program) == 48 for program in PROGRAMS))
    check("E02 explicit prefix trie has 8,239 nodes and 8,238 edges", len(PREFIXES) == 8_239)
    child_census = Counter(CHILD_COUNT.values())
    check("E03 explicit trie has 235 branch and 7,768 unary nodes", child_census == {1: 7_768, 2: 235}, str(child_census))
    width = Counter(map(len, PREFIXES))
    check("E04 maximum width is 236 at depths 46-48", max(width.values()) == 236 and {depth for depth, count in width.items() if count == 236} == {46, 47, 48})
    check("E05 compressed Patricia trie has 471 nodes and 470 edges", len(SIGNIFICANT_PREFIXES) == 471 and len(PATRICIA_EDGES) == 470)
    edge_lengths = tuple(len(child) - len(parent) for parent, child in PATRICIA_EDGES)
    check("E06 compressed labels total 8,238 bits", sum(edge_lengths) == 8_238)
    check("E07 longest compressed edge is 43 bits", max(edge_lengths) == 43)
    check("E08 every live program classifies to its unique row", all(classify(program) == local for local, program in c90.ROW_PROGRAMS.items()))
    check("E09 every selected leaf retains its output association", all(c90.ROW_PROGRAMS[classify(program)] == program and c89.LIVE_TABLE[classify(program)] in c89.ROLE_TO_WORD for program in PROGRAMS))

    accepted_flips = 0
    failures = []
    for program in PROGRAMS:
        for index in range(48):
            altered = program[:index] + (1 - program[index],) + program[index + 1:]
            selected = classify(altered)
            if selected is not None:
                accepted_flips += 1
                if c90.ROW_PROGRAMS[selected] != altered:
                    failures.append((program, index, altered, selected))
    check("E10 all 11,328 one-bit perturbations classify exactly or reject", len(PROGRAMS) * 48 == 11_328 and not failures)
    check("E11 exactly 28 directed one-bit flips reach another live row", accepted_flips == 28)


def scope_contract() -> None:
    section("F - Bounded result and residual interfaces")
    note = NOTE.read_text(encoding="utf-8").lower() if NOTE.is_file() else ""
    for marker in ("*", "`", ">"):
        note = note.replace(marker, "")
    note = " ".join(note.split())
    check("F01 note exists and carries authority none", NOTE.is_file() and "authority: none" in note)
    check("F02 note states both supplied-source sizes", "59-record empty source" in note and "twelve-record gate source" in note)
    check("F03 note names candidate-bit bus residual", "candidate_bit_bus_to_active_trie_node" in note)
    check("F04 note names physical embedding residual", "proper_cubic_patricia_embedding" in note)
    check("F05 note denies a seed-grown selector", "no seed-grown selector is claimed" in note)
    check("F06 note preserves historical routes", "cycles 86 and 87 remain historical" in note)
    check("F07 note denies foundation and axiom effects", "no foundation edit" in note and "no axiom addition follows" in note)


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    empty_table_contract()
    empty_exhaustive_contract()
    gate_contract()
    mixed_pipeline_contract()
    trie_and_perturbation_contract()
    scope_contract()
    print("\nEMPTY_SOURCE=59 EMPTY_RAW=36 EMPTY_UNION_RAW=5488 EXTRA_CONTROLS=3850")
    print("GATE_SOURCE=12 GATE_RAW=84 COMPLETE_UNION_RAW=5572 MIXED_CONTEXTS=26904")
    print("PROGRAMS=236 PREFIX_NODES=8239 PATRICIA_NODES=471 PATRICIA_EDGES=470")
    print("PERTURBATIONS=11328 ACCEPTED_DIRECTED_FLIPS=28")
    print(f"SUMMARY: {PASS} PASS / {FAIL} FAIL")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
