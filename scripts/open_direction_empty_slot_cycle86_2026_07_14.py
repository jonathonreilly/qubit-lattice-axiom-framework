#!/usr/bin/env python3
"""Cycle 86: physical open-direction encoding into the eight-bit EMPTY slot.

One seed-frame port is genuinely open.  A caged sensor has four recorded
transverse neighbours and two axial openings: the monitored port behind it
and an EMPTY candidate slot ahead.  Only while both are open can the sensor
append H1.  That record grows the reserved word 11111111 along the candidate
spine.  Cycle 81's existing comparator certificates follow the grown bits
against a supplied all-H1 reference word.

Every asynchronous schedule, all proper-cubic images, and one-extra-neighbour
controls over the complete 134-role bounded alphabet are exhausted.  The
59-record frame/reference/isolation source is supplied, not seed-grown.

Authority: none.  No foundation, queue, audit, or git authority is exercised.
"""

from __future__ import annotations

from collections import Counter, deque
from pathlib import Path

import directional_multiword_rule_port_output_cycle82_2026_07_14 as c82
import eight_bit_physical_role_comparator_cycle81_2026_07_14 as c81
import four_open_reservation_comb_cycle59_2026_07_14 as c59
import official_seed_to_rail_nucleation_cycle53_2026_07_14 as c53


ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / "docs" / "work_history" / "repo" / "review_feedback"
NOTE = REVIEW / "OPEN_DIRECTION_EMPTY_SLOT_CYCLE86_NOTE_2026-07-14.md"

Coord = tuple[int, int, int]
Signature = c53.Signature
H0 = "H0"
H1 = "H1"
EMPTY_WORD: c81.Word = (1, 1, 1, 1, 1, 1, 1, 1)

SENSOR: Coord = (-1, 0, 0)
MONITORED_PORT: Coord = (-2, 0, 0)
COMPARATOR_START: Coord = (-1, 1, 0)
CANDIDATE: tuple[Coord, ...] = tuple((index, 0, 0) for index in range(8))
REFERENCE: tuple[Coord, ...] = tuple((index, 2, 0) for index in range(8))
CERTIFICATE: tuple[Coord, ...] = tuple((index, 1, 0) for index in range(8))

# Sensor neighbours in -y,+y,-z,+z order.  +y is also comparator START.
SENSOR_MARKERS = (H0, H1, H0, H1)
# Candidate wire markers in -y,-z,+z order.
WIRE_MARKERS = (H0, H0, H0)
# Monitored-port isolation cage in -x,-y,+y,-z,+z order.
PORT_MARKERS = (H0, H0, H1, H1, H1)
# These two sites were the exact parasites in the unblocked geometry.
START_BLOCKERS = {
    (-1, 1, -1): H1,
    (-1, 1, 1): H1,
}

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


def source(extra: str | None = None) -> dict[Coord, str]:
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


def signature(records: dict[Coord, str], target: Coord) -> Signature:
    return c53.local_signature(records, target)


def build_table() -> dict[Signature, str]:
    records = source()
    table = {c53.canonical_signature(signature(records, SENSOR)): H1}
    records[SENSOR] = H1
    table[c53.canonical_signature(signature(records, CANDIDATE[0]))] = H1
    return table


CANONICAL_TABLE = build_table()
RAW_OUTPUTS = c59.raw_rule_outputs(CANONICAL_TABLE)


def merge_raw() -> dict[Signature, frozenset[str]]:
    outputs = {local: set(values) for local, values in c82.COMBINED_RAW.items()}
    for local, values in RAW_OUTPUTS.items():
        outputs.setdefault(local, set()).update(values)
    return {local: frozenset(values) for local, values in outputs.items()}


COMBINED_RAW = merge_raw()
ALLOWED: dict[Coord, str] = {
    SENSOR: H1,
    **{site: H1 for site in CANDIDATE},
    **{site: H1 for site in CERTIFICATE},
}


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


def records_for(state: frozenset[Coord], extra: str | None = None) -> dict[Coord, str]:
    records = source(extra)
    records.update({site: ALLOWED[site] for site in state})
    return records


def graph() -> tuple[frozenset[frozenset[Coord]], int, tuple[frozenset[Coord], ...], tuple[tuple, ...], int]:
    initial: frozenset[Coord] = frozenset()
    queue = deque((initial,))
    seen = {initial}
    terminals: list[frozenset[Coord]] = []
    parasites: list[tuple] = []
    edges = 0
    maximum = 0
    while queue:
        state = queue.popleft()
        outputs = enabled_outputs(records_for(state))
        maximum = max(maximum, len(outputs))
        if not outputs:
            terminals.append(state)
        for target, values in outputs.items():
            if len(values) != 1 or ALLOWED.get(target) != next(iter(values)):
                parasites.append((state, target, values))
                continue
            future = state | {target}
            edges += 1
            if future not in seen:
                seen.add(future)
                queue.append(future)
    return frozenset(seen), edges, tuple(terminals), tuple(parasites), maximum


def canonical_records(records: dict[Coord, str]) -> tuple[tuple[Coord, str], ...]:
    minima = tuple(min(site[axis] for site in records) for axis in range(3))
    return tuple(sorted((tuple(site[axis] - minima[axis] for axis in range(3)), content) for site, content in records.items()))


def transform(records: dict[Coord, str], rotation: c53.Matrix, shift: Coord) -> dict[Coord, str]:
    return {c53.add(c53.matvec(rotation, site), shift): content for site, content in records.items()}


def row_program(local: Signature) -> tuple[int, ...]:
    contents = dict(local)
    return tuple(
        bit
        for direction in c82.DIRECTION_ORDER
        for bit in (c81.ROLE_TO_WORD[contents[direction]] if direction in contents else EMPTY_WORD)
    )


ROW_PROGRAMS = {local: row_program(local) for local in c81.SELECTED_TABLE}


def table_and_geometry_contract() -> None:
    section("A - Physical sensor, reserved EMPTY word, and exact table")
    check("A01 all-H1 EMPTY word is reserved", EMPTY_WORD in c81.RESERVED_WORDS and EMPTY_WORD not in c81.WORD_TO_ROLE)
    check("A02 source has exactly 59 supplied H0/H1 records", len(source()) == 59 and set(source().values()) == {H0, H1})
    check("A03 monitored port and all seventeen additions start open", MONITORED_PORT not in source() and set(ALLOWED).isdisjoint(source()))
    check("A04 sensor has four recorded transverse neighbours and two axial openings", len(signature(source(), SENSOR)) == 4 and {c53.add(SENSOR, (-1, 0, 0)), c53.add(SENSOR, (1, 0, 0))} == {MONITORED_PORT, CANDIDATE[0]})
    check("A05 table has exactly openness and H1-wire rows", len(CANONICAL_TABLE) == 2 and set(CANONICAL_TABLE.values()) == {H1} and set(map(len, CANONICAL_TABLE)) == {4})
    check("A06 two rows have 36 proper-cubic raw images", len(RAW_OUTPUTS) == 36)
    check("A07 new raw domain is disjoint from Cycle-82", set(RAW_OUTPUTS).isdisjoint(c82.COMBINED_RAW))
    check("A08 physical union has 4,624 single-valued raw rows", len(COMBINED_RAW) == 4_624 and all(len(values) == 1 for values in COMBINED_RAW.values()))
    canonical = canonical_records(source())
    stabilizer = sum(canonical_records({c53.matvec(rotation, site): content for site, content in source().items()}) == canonical for rotation in c53.ROTATIONS)
    check("A09 supplied source has trivial proper-cubic stabilizer", stabilizer == 1)


def asynchronous_contract() -> frozenset[frozenset[Coord]]:
    section("B - Exhaustive asynchronous openness-to-EMPTY graph")
    states, edges, terminals, parasites, maximum = graph()
    check("B01 graph has exactly 46 reachable states", len(states) == 46)
    check("B02 graph has exactly 73 append edges", edges == 73)
    check("B03 graph has one complete seventeen-record terminal", len(terminals) == 1 and terminals[0] == frozenset(ALLOWED))
    check("B04 graph has no parasite or output conflict", not parasites, str(parasites[:1]))
    check("B05 no state enables more than candidate plus comparator", maximum == 2)
    profiles = Counter((SENSOR in state, sum(site in state for site in CANDIDATE), sum(site in state for site in CERTIFICATE)) for state in states)
    expected = Counter({(False, 0, 0): 1})
    expected.update({(True, candidate_count, certificate_count): 1 for candidate_count in range(9) for certificate_count in range(candidate_count + 1)})
    check("B06 states are exactly sensor then 0<=certificate<=candidate<=8", profiles == expected, str(profiles - expected))
    check("B07 terminal candidate is physical 11111111", all(dict(records_for(terminals[0]))[site] == H1 for site in CANDIDATE))
    check("B08 terminal comparator certificates form the physical slot MATCH", all(site in terminals[0] for site in CERTIFICATE))
    check("B09 monitored port is never naturally writable", all(MONITORED_PORT not in enabled_outputs(records_for(state)) for state in states))
    return states


def extra_and_covariance_contract(states: frozenset[frozenset[Coord]]) -> None:
    section("C - Extra-neighbour sensitivity and all proper-cubic images")
    extra_contents = tuple(sorted(c81.FULL_ROLES)) + ("FOREIGN_CONTROL",)
    failures = []
    shift = (47, -29, 13)
    for extra in extra_contents:
        records = source(extra)
        if assignments(records):
            failures.append(("base", extra, assignments(records)))
        for rotation_index, rotation in enumerate(c53.ROTATIONS):
            transformed = transform(records, rotation, shift)
            if assignments(transformed):
                failures.append((rotation_index, extra, assignments(transformed)))
    check("C01 all 3,375 pre-existing one-extra-neighbour controls are quiet", len(extra_contents) * 25 == 3_375 and not failures, str(failures[:1]))
    check("C02 every one of the 134 bounded physical contents blocks EMPTY", all(not assignments(source(extra)) for extra in c81.FULL_ROLES))
    check("C03 an otherwise unknown content also blocks EMPTY", not assignments(source("FOREIGN_CONTROL")))

    covariance_failures = []
    for rotation_index, rotation in enumerate(c53.ROTATIONS):
        for state in states:
            records = records_for(state)
            expected = assignments(records)
            transformed = transform(records, rotation, shift)
            transformed_expected = transform(expected, rotation, shift)
            actual = assignments(transformed)
            if actual != transformed_expected:
                covariance_failures.append((rotation_index, state, transformed_expected, actual))
    check("C04 all 1,104 rotated reachable states have exact frontier", len(states) * 24 == 1_104 and not covariance_failures, str(covariance_failures[:1]))


def program_composition_and_scope_contract() -> None:
    section("D - All 198 programs and exact remaining physical boundary")
    check("D01 all 198 programs remain distinct with EMPTY=11111111", len(ROW_PROGRAMS) == len(set(ROW_PROGRAMS.values())) == 198)
    empty_slots = sum(1 for local in c81.SELECTED_TABLE for direction in c82.DIRECTION_ORDER if direction not in dict(local))
    check("D02 exact program bank has 613 open-direction slots", empty_slots == sum(6 - len(local) for local in c81.SELECTED_TABLE) == 613)
    check("D03 exactly 195 programs consume at least one EMPTY slot", sum(EMPTY_WORD in tuple(program[index:index + 8] for index in range(0, 48, 8)) for program in ROW_PROGRAMS.values()) == 195)
    distances = [sum(left != right for left, right in zip(a, b)) for index, a in enumerate(ROW_PROGRAMS.values()) for b in tuple(ROW_PROGRAMS.values())[:index]]
    check("D04 program minimum Hamming distance remains one", min(distances) == 1)

    note = NOTE.read_text(encoding="utf-8").lower() if NOTE.is_file() else ""
    for marker in ("*", "`", ">"):
        note = note.replace(marker, "")
    note = " ".join(note.split())
    check("D05 note exists and carries authority none", NOTE.is_file() and "authority: none" in note)
    check("D06 note states the 59-record source is supplied", "59-record source is supplied" in note)
    check("D07 note names the slot-placement residual", "empty_slot_to_six_slot_candidate_geometry" in note)
    check("D08 note names late-composition scope", "multi-front reservation remains untested" in note)
    check("D09 note denies foundation and axiom effects", "no foundation edit" in note and "no axiom addition follows" in note)


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    table_and_geometry_contract()
    states = asynchronous_contract()
    extra_and_covariance_contract(states)
    program_composition_and_scope_contract()
    print("\nSOURCE=59 CANONICAL=2 RAW=36 PHYSICAL_UNION_RAW=4624")
    print("STATES=46 EDGES=73 TERMINALS=1 EXTRA_CONTROLS=3375 ROTATED_STATES=1104")
    print("EMPTY_PROGRAM_SLOTS=613 PROGRAMS=198")
    print(f"SUMMARY: {PASS} PASS / {FAIL} FAIL")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
