#!/usr/bin/env python3
"""Cycle 102: generated endpoint to autonomous frame/cage rail composition.

The exact Cycle-100 source already contains the transformed Cycle-52 A slice
and its occupied backstop.  This runner composes the current zero-source
macroblock table with Cycle 52's autonomous rail rows, then checks the exact
mixed asynchronous product of codeword formation and one complete rail slice,
longer rail renewal, proper-cubic covariance, and the bounded scope claim.

Authority: none.
"""

from __future__ import annotations

from collections import defaultdict
from pathlib import Path

import self_extending_frame_cage_rail_cycle52_2026_07_14 as c52
import zero_binary_source_endpoint_macroblock_bind_cycle100_2026_07_15 as c100


ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / "docs" / "work_history" / "repo" / "review_feedback"
NOTE = REVIEW / "GENERATED_ENDPOINT_AUTONOMOUS_FRAME_RAIL_CYCLE102_NOTE_2026-07-15.md"

Coord = tuple[int, int, int]
Signature = c100.Signature
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


def merge_raw(
    *tables: dict[Signature, frozenset[str]],
) -> dict[Signature, frozenset[str]]:
    outputs: dict[Signature, set[str]] = defaultdict(set)
    for table in tables:
        for local, values in table.items():
            outputs[local].update(values)
    return {local: frozenset(values) for local, values in outputs.items()}


def add(left: Coord, right: Coord) -> Coord:
    return tuple(left[index] + right[index] for index in range(3))  # type: ignore[return-value]


def transform_records(
    records: dict[Coord, str], rotation: c52.Rotation, shift: Coord
) -> dict[Coord, str]:
    return {
        add(c52.matvec(rotation, site), shift): content
        for site, content in records.items()
    }


# Standard Cycle-52 (x,y,z) maps to the generated physical endpoint as
# (-x-1,z,y).  The initial rail therefore grows toward physical -x.
SEED_ROTATION: c52.Rotation = ((-1, 0, 0), (0, 0, 1), (0, 1, 0))
SEED_SHIFT: Coord = (-1, 0, 0)
STANDARD_SEED = c52.seed_records()
PHYSICAL_SEED = transform_records(STANDARD_SEED, SEED_ROTATION, SEED_SHIFT)
RAIL_SEQUENCE = c52.transform_sequence(
    c52.bounded_sequence(8), SEED_ROTATION, SEED_SHIFT
)
FIRST_SLICE = RAIL_SEQUENCE[:12]
MIXED_RAW = merge_raw(c100.COMBINED_RAW, c52.RULE_OUTPUTS)


def enabled(records: dict[Coord, str]) -> dict[Coord, frozenset[str]]:
    return {
        target: MIXED_RAW[local]
        for target in c100.c53.open_candidates(records)
        if (local := c100.c53.local_signature(records, target)) in MIXED_RAW
    }


def product_state(code_prefix: int, rail_prefix: int) -> dict[Coord, str]:
    records = c100.records_at(code_prefix)
    records.update(dict(FIRST_SLICE[:rail_prefix]))
    return records


def product_expected(
    code_prefix: int, rail_prefix: int
) -> dict[Coord, frozenset[str]]:
    answer: dict[Coord, frozenset[str]] = {}
    if code_prefix < len(c100.ADDITIONS):
        site, content = c100.ADDITIONS[code_prefix]
        answer[site] = frozenset((content,))
    # At prefix 12 the autonomous rail does not stop: its exact lawful
    # frontier is the first record of the following slice.
    if rail_prefix < len(RAIL_SEQUENCE):
        site, content = RAIL_SEQUENCE[rail_prefix]
        answer[site] = frozenset((content,))
    return answer


def contracts() -> None:
    section("A - Exact generated rail seed and mixed table")
    check("A01 source is the exact 254-record generated endpoint", len(c100.SOURCE) == 254)
    check(
        "A02 transformed Cycle-52 seed is literally present",
        all(c100.SOURCE.get(site) == content for site, content in PHYSICAL_SEED.items()),
    )
    check("A03 transformed seed has twelve slice roles and one backstop", len(PHYSICAL_SEED) == 13)
    check("A04 seed transform is a proper cubic rotation", c52.determinant(SEED_ROTATION) == 1)
    overlap = set(c100.COMBINED_RAW) & set(c52.RULE_OUTPUTS)
    check("A05 macroblock and rail raw domains are disjoint", not overlap, str(tuple(overlap)[:1]))
    check("A06 mixed raw table has the exact union size", len(MIXED_RAW) == 6524)
    check("A07 every mixed raw input is single-valued", all(len(values) == 1 for values in MIXED_RAW.values()))

    section("B - Complete asynchronous code/rail product")
    failures = []
    for code_prefix in range(len(c100.ADDITIONS) + 1):
        for rail_prefix in range(len(FIRST_SLICE) + 1):
            actual = enabled(product_state(code_prefix, rail_prefix))
            expected = product_expected(code_prefix, rail_prefix)
            if actual != expected:
                failures.append((code_prefix, rail_prefix, expected, actual))
    check("B01 all 143 product states have exactly the two lawful fronts", not failures, str(failures[:1]))
    check("B02 product contains every code/rail interleaving prefix", 11 * 13 == 143)
    check("B03 code front remains the exact R_B11 to VALID to READY sequence", c100.ADDITIONS[-2:] == ((c100.VALID, c100.H1), (c100.READY, c100.H1)))
    check("B04 first rail slice remains the exact twelve-write Cycle-52 sweep", len(FIRST_SLICE) == 12)
    terminal = product_state(10, 12)
    next_site, next_content = RAIL_SEQUENCE[12]
    check("B05 bounded product exposes only the next lawful rail write", enabled(terminal) == {next_site: frozenset((next_content,))})

    section("C - Longer renewal, old debris, and covariance")
    records = c100.records_at(10)
    renewal_failures = []
    for index, (site, content) in enumerate(RAIL_SEQUENCE):
        actual = enabled(records)
        expected = {site: frozenset((content,))}
        if actual != expected:
            renewal_failures.append((index, expected, actual))
            break
        records[site] = content
    check("C01 all 96 rail appends have a singleton mixed frontier", not renewal_failures, str(renewal_failures[:1]))
    next_long = c52.transform_sequence(c52.bounded_sequence(9), SEED_ROTATION, SEED_SHIFT)[96]
    check("C02 eight complete slices expose exactly the ninth-slice start", enabled(records) == {next_long[0]: frozenset((next_long[1],))})
    check("C03 old endpoint, code, and seven prior slices stay permanently present", all(records.get(site) == content for site, content in c100.records_at(10).items()))

    covariance_failures = []
    shift = (101, -73, 59)
    base_states = (
        product_state(0, 0),
        product_state(5, 0),
        product_state(0, 7),
        product_state(10, 12),
    )
    for rotation in c52.ROTATIONS:
        for base in base_states:
            transformed = transform_records(base, rotation, shift)
            expected = transform_records(
                {site: next(iter(values)) for site, values in enabled(base).items()},
                rotation,
                shift,
            )
            actual = {
                site: next(iter(values))
                for site, values in enabled(transformed).items()
            }
            if actual != expected:
                covariance_failures.append((rotation, len(base), expected, actual))
                break
    check("C04 all 96 mixed checkpoint rotations preserve the frontier", not covariance_failures, str(covariance_failures[:1]))
    check("C05 Cycle-52 supplies an exact period-four unbounded renewal induction", len(c52.BASE_RULES) == 48 and len(c52.ROTATIONS) == 24)

    section("D - Exact scope and constitutional disposition")
    note = NOTE.read_text(encoding="utf-8").lower() if NOTE.is_file() else ""
    check("D01 note exists and carries authority none", NOTE.is_file() and "authority: none" in note)
    check("D02 note names the closed bounded interface", "boot_relational_frame_existence_and_renewal" in note)
    check("D03 note names the exact remaining bind", "ready_row_to_rail_payload_bind" in note)
    check("D04 note contains N1-N8", all(f"n{index}" in note for index in range(1, 9)))
    check("D05 note denies foundation and axiom effects", "no foundation edit" in note and "no axiom addition follows" in note)


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    contracts()
    print(f"\nSOURCE={len(c100.SOURCE)} CODE_APPENDS={len(c100.ADDITIONS)} RAIL_APPENDS={len(RAIL_SEQUENCE)}")
    print(f"MACROBLOCK_RAW={len(c100.COMBINED_RAW)} RAIL_RAW={len(c52.RULE_OUTPUTS)} MIXED_RAW={len(MIXED_RAW)}")
    print(f"PRODUCT_STATES={(len(c100.ADDITIONS) + 1) * (len(FIRST_SLICE) + 1)}")
    print(f"SUMMARY: {PASS} PASS / {FAIL} FAIL")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
