#!/usr/bin/env python3
"""Cycle 100: zero-binary-source R_B11 macroblock bind at Cycle-85 endpoint.

The actual lifted R_LA + five OPEN row writes the first H1 bit at its physical
target.  Nine further exact local rows walk the already-generated endpoint
surface, append the remaining seven R_B11 bits, then append VALID and READY.
No candidate word, reference word, bit rail, comparator, writer, or new cage
record is supplied.

Authority: none.
"""

from __future__ import annotations

from collections import defaultdict
from pathlib import Path

import four_open_reservation_comb_cycle59_2026_07_14 as c59
import live_eight_bit_physical_comparator_cycle89_2026_07_15 as c89
import live_seed_row_readable_macrostep_cycle94_2026_07_15 as c94
import official_seed_to_rail_nucleation_cycle53_2026_07_14 as c53


ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / "docs" / "work_history" / "repo" / "review_feedback"
NOTE = REVIEW / "ZERO_BINARY_SOURCE_ENDPOINT_MACROBLOCK_BIND_CYCLE100_NOTE_2026-07-15.md"

Coord = tuple[int, int, int]
Signature = c53.Signature
H0 = "H0"
H1 = "H1"
PASS = 0
FAIL = 0


def section(title: str) -> None:
    print("\n" + "=" * 79)
    print(title)
    print("=" * 79)


def check(label: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"PASS {label}" + (f" :: {detail}" if detail else ""))
    else:
        FAIL += 1
        print(f"FAIL {label}" + (f" :: {detail}" if detail else ""))


def add(left: Coord, right: Coord) -> Coord:
    return tuple(left[index] + right[index] for index in range(3))  # type: ignore[return-value]


def transform_site(site: Coord, rotation: c53.Matrix, shift: Coord) -> Coord:
    return add(c53.matvec(rotation, site), shift)


def transform_records(
    records: dict[Coord, str], rotation: c53.Matrix, shift: Coord
) -> dict[Coord, str]:
    return {
        transform_site(site, rotation, shift): content
        for site, content in records.items()
    }


def canonical(records: dict[Coord, str], target: Coord) -> Signature:
    return c53.canonical_signature(c53.local_signature(records, target))


def merge_raw(
    *tables: dict[Signature, frozenset[str]],
) -> dict[Signature, frozenset[str]]:
    outputs: dict[Signature, set[str]] = defaultdict(set)
    for table in tables:
        for local, values in table.items():
            outputs[local].update(values)
    return {local: frozenset(values) for local, values in outputs.items()}


SOURCE = dict(c94.ENDPOINT)
TARGET = c94.PHYSICAL_TARGET
CODE_SITES: tuple[Coord, ...] = (
    TARGET,
    (1, 5, 0),
    (1, 5, 1),
    (0, 5, 1),
    (0, 5, 2),
    (1, 5, 2),
    (1, 4, 2),
    (2, 4, 2),
)
VALID: Coord = (3, 4, 2)
READY: Coord = (3, 3, 2)
R_B11_WORD = c89.ROLE_TO_WORD["R_B11"]
ADDITIONS: tuple[tuple[Coord, str], ...] = tuple(
    (site, H1 if bit else H0)
    for site, bit in zip(CODE_SITES, R_B11_WORD)
) + ((VALID, H1), (READY, H1))


def build_encoder_table() -> dict[Signature, str]:
    records = dict(SOURCE)
    # The lifted live row supplies the first physical bit at TARGET.
    records[ADDITIONS[0][0]] = ADDITIONS[0][1]
    table: dict[Signature, str] = {}
    for target, output in ADDITIONS[1:]:
        local = canonical(records, target)
        prior = table.get(local)
        if prior is not None and prior != output:
            raise ValueError((local, prior, output))
        table[local] = output
        records[target] = output
    return table


ENCODER_TABLE = build_encoder_table()
ENCODER_RAW = c59.raw_rule_outputs(ENCODER_TABLE)
COMBINED_RAW = merge_raw(c94.LIFTED_LIVE_RAW, ENCODER_RAW)


def enabled(records: dict[Coord, str]) -> dict[Coord, frozenset[str]]:
    return {
        target: COMBINED_RAW[local]
        for target in c53.open_candidates(records)
        if (local := c53.local_signature(records, target)) in COMBINED_RAW
    }


def records_at(step: int) -> dict[Coord, str]:
    records = dict(SOURCE)
    records.update(dict(ADDITIONS[:step]))
    return records


def expected_at(step: int) -> dict[Coord, frozenset[str]]:
    if step == len(ADDITIONS):
        return {}
    site, content = ADDITIONS[step]
    return {site: frozenset((content,))}


def contracts() -> None:
    section("A - Exact generated endpoint and zero binary compiler source")
    check("A01 source is exactly the generated Cycle-85 endpoint", SOURCE == c94.ENDPOINT and len(SOURCE) == 254)
    check("A02 all eight code, VALID, and READY sites start open", set(CODE_SITES + (VALID, READY)).isdisjoint(SOURCE))
    check("A03 source adds no compiler candidate/reference/rail/cage", all(site not in SOURCE for site in CODE_SITES + (VALID, READY)))
    check("A04 target sees exactly R_LA with five open directions", c53.local_signature(SOURCE, TARGET) == (((0, -1, 0), "R_LA"),))
    check("A05 lifted live law initially enables only first R_B11 bit", enabled(SOURCE) == {TARGET: frozenset((H1,))})
    check("A06 first physical bit agrees with R_B11", ADDITIONS[0] == (TARGET, H1) and R_B11_WORD == (1, 0, 0, 1, 0, 1, 0, 0))

    section("B - Surface encoder table and exact append trajectory")
    check("B01 encoder has seven data plus VALID plus READY rows", len(ENCODER_TABLE) == 9)
    check("B02 encoder uses only existing endpoint contents and H0/H1", {content for local in ENCODER_TABLE for _direction, content in local} | set(ENCODER_TABLE.values()) <= c89.FULL_ROLES)
    check("B03 every encoder raw input is single-valued", all(len(values) == 1 for values in ENCODER_RAW.values()))
    overlap = set(ENCODER_RAW) & set(c94.LIFTED_LIVE_RAW)
    check("B04 encoder has no exact raw-input overlap with lifted live law", not overlap, str(tuple(overlap)[:1]))
    check("B05 complete lifted union is output-single-valued", all(len(values) == 1 for values in COMBINED_RAW.values()))
    failures = []
    for step in range(len(ADDITIONS) + 1):
        actual = enabled(records_at(step))
        expected = expected_at(step)
        if actual != expected:
            failures.append((step, expected, actual))
    check("B06 all eleven states have the exact singleton/quiet frontier", not failures, str(failures[:1]))
    check("B07 execution is ten forced permanent appends", len(ADDITIONS) == 10 and not enabled(records_at(10)))

    section("C - Decoder, causal validation, blockers, and covariance")
    word_state = records_at(8)
    decoded = tuple(1 if word_state[site] == H1 else 0 for site in CODE_SITES)
    check("C01 first eight records decode exactly to R_B11", decoded == R_B11_WORD and c89.WORD_TO_ROLE[decoded] == "R_B11")
    check("C02 word completes before VALID and READY", VALID not in word_state and READY not in word_state)
    check("C03 VALID forms ninth and READY tenth", ADDITIONS[8:] == ((VALID, H1), (READY, H1)))

    corruption_failures = []
    for index, (site, content) in enumerate(ADDITIONS[:8]):
        records = records_at(index + 1)
        records[site] = H0 if content == H1 else H1
        if enabled(records):
            corruption_failures.append((index, enabled(records)))
    check("C04 every one-bit causal corruption stops before the next certificate", not corruption_failures, str(corruption_failures[:1]))

    blocker_failures = []
    blocker_count = 0
    for step, (target, _content) in enumerate(ADDITIONS):
        records = records_at(step)
        occupied = set(records)
        for direction in c53.DIRECTIONS:
            neighbour = add(target, direction)
            if neighbour in occupied:
                continue
            for role in c89.FULL_ROLES:
                altered = dict(records)
                altered[neighbour] = role
                blocker_count += 1
                if target in enabled(altered):
                    blocker_failures.append((step, direction, role))
                    break
    check("C05 every tested extra-neighbour record blocks the exact next write", not blocker_failures and blocker_count > 0, str(blocker_failures[:1]))

    covariance_failures = []
    shift = (71, -53, 37)
    for rotation in c53.ROTATIONS:
        for step in range(len(ADDITIONS) + 1):
            records = transform_records(records_at(step), rotation, shift)
            expected = transform_records(
                {site: next(iter(values)) for site, values in expected_at(step).items()},
                rotation,
                shift,
            )
            actual = {site: next(iter(values)) for site, values in enabled(records).items()}
            if actual != expected:
                covariance_failures.append((rotation, step, expected, actual))
                break
    check("C06 all 264 rotated stages have the exact transformed frontier", not covariance_failures, str(covariance_failures[:1]))

    section("D - Scope, N1-N8, and constitutional disposition")
    note = NOTE.read_text(encoding="utf-8").lower() if NOTE.is_file() else ""
    check("D01 note exists and carries authority none", NOTE.is_file() and "authority: none" in note)
    check("D02 note pins zero added binary source records", "zero added binary source records" in note)
    check("D03 note names exact next residual", "macroblock_ready_to_self_grown_first_harness" in note)
    check("D04 note contains N1-N8", all(f"n{index}" in note for index in range(1, 9)))
    check("D05 note denies foundation and axiom effects", "no foundation edit" in note and "no axiom addition follows" in note)


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    contracts()
    print(f"\nSOURCE={len(SOURCE)} CODE_BITS=8 VALID=1 READY=1 APPENDS={len(ADDITIONS)}")
    print(f"ENCODER_CANONICAL={len(ENCODER_TABLE)} ENCODER_RAW={len(ENCODER_RAW)} UNION_RAW={len(COMBINED_RAW)}")
    print(f"WORD={''.join(map(str, R_B11_WORD))} ROLE=R_B11")
    print(f"SUMMARY: {PASS} PASS / {FAIL} FAIL")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
