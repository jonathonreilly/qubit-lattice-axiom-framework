#!/usr/bin/env python3
"""Cycle 81: exact eight-bit physical comparator for the selected recurrent law.

Cycle 80 adds 51 disjoint recurrent roles to Cycle 75's 83-role bounded
source alphabet.  This runner preserves the prior codebook under a leading
zero, assigns the recurrent roles under a leading one, and extends the
physical H0/H1 equality chain from seven to eight bits.  All 256^2 ordered
word pairs and every naturally reachable chain state are scanned in union
with Cycle 58 and the selected Cycle-60/67/72/80 extensional rows.

Authority: none.  The 38-record comparator harness is supplied, not grown.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass
from hashlib import sha256
from itertools import product
from math import ceil, log2
from pathlib import Path

import four_open_reservation_comb_cycle59_2026_07_14 as c59
import official_seed_to_rail_nucleation_cycle53_2026_07_14 as c53
import operational_binary_macrocode_compiler_cycle58_2026_07_14 as c58
import seven_bit_physical_role_comparator_cycle75_2026_07_14 as c75
import three_phase_recurrent_append_tube_cycle80_2026_07_14 as c80


ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / "docs" / "work_history" / "repo" / "review_feedback"
NOTE = REVIEW / "EIGHT_BIT_PHYSICAL_ROLE_COMPARATOR_CYCLE81_NOTE_2026-07-14.md"

Coord = tuple[int, int, int]
Word = tuple[int, int, int, int, int, int, int, int]
Signature = c53.Signature
H0 = "H0"
H1 = "H1"

EXPECTED_OUTPUT_DIGEST = "7a2af630282f0582b448a5a1ee6ef04cb7e49f425b7cfe3deb722687c11f330b"
EXPECTED_ACTIVE_DIGEST = "60d08f0409ab8852920e377478319ac19f178c801c94cd2d8cbd41e25405e721"
EXPECTED_FULL_DIGEST = "220f2f295e9e6d0f7e47fe4c68ca923559cd5b5989034641bd15e75af9a938dc"
EXPECTED_RECURRENT_DIGEST = "b3babaad33c8203036af079fe6ede7aa993ac1b4d1ca6a218f37339d4be196d7"

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


def digest(values: frozenset[str] | set[str]) -> str:
    return sha256("\n".join(sorted(values)).encode("utf-8")).hexdigest()


SELECTED_TABLE = dict(c75.UNION_TABLE)
SELECTED_TABLE.update(c80.CONSTRUCTION.table)
OUTPUT_ROLES = frozenset(SELECTED_TABLE.values())
INPUT_ROLES = frozenset(content for signature in SELECTED_TABLE for _offset, content in signature)
ACTIVE_ROLES = OUTPUT_ROLES | INPUT_ROLES
RECURRENT_ROLES = frozenset(c80.CONSTRUCTION.table.values()) | frozenset(
    content for signature in c80.CONSTRUCTION.table for _offset, content in signature
)
FULL_ROLES = c75.FULL_ROLES | RECURRENT_ROLES


def seven_bit_word(value: int) -> tuple[int, int, int, int, int, int, int]:
    assert 0 <= value < 128
    return tuple((value >> shift) & 1 for shift in range(6, -1, -1))  # type: ignore[return-value]


ALL_WORDS: tuple[Word, ...] = tuple(product((0, 1), repeat=8))  # type: ignore[assignment]
ROLE_TO_WORD: dict[str, Word] = {
    role: (0, *word) for role, word in c75.ROLE_TO_WORD.items()
}
ROLE_TO_WORD.update({
    role: (1, *seven_bit_word(index))
    for index, role in enumerate(sorted(RECURRENT_ROLES))
})
WORD_TO_ROLE = {word: role for role, word in ROLE_TO_WORD.items()}
RESERVED_WORDS = tuple(word for word in ALL_WORDS if word not in WORD_TO_ROLE)

CANDIDATE: tuple[Coord, ...] = tuple((index, 0, 0) for index in range(8))
REFERENCE: tuple[Coord, ...] = tuple((index, 2, 0) for index in range(8))
CERTIFICATE: tuple[Coord, ...] = tuple((index, 1, 0) for index in range(8))
CAGE_H0: tuple[Coord, ...] = tuple((index, 1, 1) for index in range(8))
CAGE_H1: tuple[Coord, ...] = tuple((index, 1, -1) for index in range(8))
START: Coord = (-1, 1, 0)
MATCH: Coord = (8, 1, 0)
MATCH_CAGE: dict[Coord, str] = {
    (8, 0, 0): H0,
    (8, 2, 0): H1,
    (8, 1, -1): H0,
    (8, 1, 1): H1,
    (9, 1, 0): H0,
}


def bit_content(bit: int) -> str:
    return H1 if bit else H0


def harness(candidate: Word, reference: Word) -> dict[Coord, str]:
    records: dict[Coord, str] = {START: H1, **MATCH_CAGE}
    records.update({site: bit_content(bit) for site, bit in zip(CANDIDATE, candidate)})
    records.update({site: bit_content(bit) for site, bit in zip(REFERENCE, reference)})
    records.update({site: H0 for site in CAGE_H0})
    records.update({site: H1 for site in CAGE_H1})
    return records


def common_prefix(candidate: Word, reference: Word) -> int:
    return next((i for i, pair in enumerate(zip(candidate, reference)) if pair[0] != pair[1]), 8)


@dataclass(frozen=True)
class Stage:
    certificate_count: int
    match: bool = False


def stages(candidate: Word, reference: Word) -> tuple[Stage, ...]:
    prefix = common_prefix(candidate, reference)
    answer = [Stage(count) for count in range(prefix + 1)]
    if prefix == 8:
        answer.append(Stage(8, match=True))
    return tuple(answer)


def stage_records(candidate: Word, reference: Word, stage: Stage) -> dict[Coord, str]:
    records = harness(candidate, reference)
    records.update({CERTIFICATE[index]: H1 for index in range(stage.certificate_count)})
    if stage.match:
        records[MATCH] = H1
    return records


def expected_writes(candidate: Word, reference: Word, stage: Stage) -> dict[Coord, str]:
    prefix = common_prefix(candidate, reference)
    if stage.certificate_count < prefix:
        return {CERTIFICATE[stage.certificate_count]: H1}
    if prefix == 8 and not stage.match:
        return {MATCH: H1}
    return {}


def signature(records: dict[Coord, str], target: Coord) -> Signature:
    return c53.local_signature(records, target)


def build_canonical_table() -> dict[Signature, str]:
    table: dict[Signature, str] = {}
    zero: Word = (0,) * 8
    one: Word = (1,) * 8
    examples = (
        (stage_records(zero, zero, Stage(0)), CERTIFICATE[0]),
        (stage_records(one, one, Stage(0)), CERTIFICATE[0]),
        (stage_records(zero, zero, Stage(8)), MATCH),
    )
    for records, target in examples:
        table[c53.canonical_signature(signature(records, target))] = H1
    return table


CANONICAL_TABLE = build_canonical_table()
RAW_OUTPUTS = c59.raw_rule_outputs(CANONICAL_TABLE)
SELECTED_RAW_OUTPUTS = c59.raw_rule_outputs(SELECTED_TABLE)


def merge_raw_outputs() -> dict[Signature, frozenset[str]]:
    outputs: dict[Signature, set[str]] = defaultdict(set)
    for table in (c58.RAW_OUTPUTS, SELECTED_RAW_OUTPUTS, RAW_OUTPUTS):
        for local, values in table.items():
            outputs[local].update(values)
    return {local: frozenset(values) for local, values in outputs.items()}


COMBINED_RAW_OUTPUTS = merge_raw_outputs()


def enabled_outputs(records: dict[Coord, str]) -> dict[Coord, frozenset[str]]:
    return {
        target: COMBINED_RAW_OUTPUTS[local]
        for target in c53.open_candidates(records)
        if (local := signature(records, target)) in COMBINED_RAW_OUTPUTS
    }


def canonical_records(records: dict[Coord, str]) -> tuple[tuple[Coord, str], ...]:
    minima = tuple(min(site[axis] for site in records) for axis in range(3))
    return tuple(sorted((tuple(site[axis] - minima[axis] for axis in range(3)), content) for site, content in records.items()))


def inventory_contract() -> None:
    section("A - Selected recurrent inventory and exact eight-bit bound")
    check("A01 selected table has 198 canonical rows", len(SELECTED_TABLE) == 198)
    check("A02 selected raw table has 4,376 rows", len(SELECTED_RAW_OUTPUTS) == 4_376)
    check("A03 exact output inventory has 113 roles", len(OUTPUT_ROLES) == 113 and digest(OUTPUT_ROLES) == EXPECTED_OUTPUT_DIGEST)
    check("A04 output-only information bound remains seven bits", ceil(log2(len(OUTPUT_ROLES))) == 7)
    check("A05 active matcher alphabet has 120 roles", len(ACTIVE_ROLES) == 120 and digest(ACTIVE_ROLES) == EXPECTED_ACTIVE_DIGEST)
    check("A06 active-only matcher could fit seven bits", ceil(log2(len(ACTIVE_ROLES))) == 7)
    check("A07 recurrence contributes exactly 51 disjoint roles", len(RECURRENT_ROLES) == 51 and RECURRENT_ROLES.isdisjoint(c75.FULL_ROLES) and digest(RECURRENT_ROLES) == EXPECTED_RECURRENT_DIGEST)
    check("A08 bounded source-preserving alphabet has 134 roles", len(FULL_ROLES) == 134 and digest(FULL_ROLES) == EXPECTED_FULL_DIGEST)
    check("A09 seven bits fail and eight bits suffice for 134", 2 ** 7 < len(FULL_ROLES) <= 2 ** 8)
    check("A10 exact selected arity census is pinned", Counter(map(len, SELECTED_TABLE)) == {1: 13, 2: 70, 3: 62, 4: 32, 5: 18, 6: 3})


def codebook_and_table_contract() -> None:
    section("B - Prefix-preserving codebook and physical comparator table")
    check("B01 all 134 roles have distinct eight-bit words", len(ROLE_TO_WORD) == len(set(ROLE_TO_WORD.values())) == 134)
    check("B02 all prior words are preserved below a leading zero", all(ROLE_TO_WORD[role] == (0, *word) for role, word in c75.ROLE_TO_WORD.items()))
    check("B03 all recurrent words occupy the leading-one half", all(ROLE_TO_WORD[role][0] == 1 for role in RECURRENT_ROLES))
    check("B04 exactly 122 words remain reserved", len(RESERVED_WORDS) == 122)
    check("B05 assigned and reserved words partition all 256", set(ROLE_TO_WORD.values()).isdisjoint(RESERVED_WORDS) and set(ROLE_TO_WORD.values()) | set(RESERVED_WORDS) == set(ALL_WORDS))
    check("B06 every harness contains exactly 38 H0/H1 records", all(len(harness(left, right)) == 38 and set(harness(left, right).values()) == {H0, H1} for left, right in ((ALL_WORDS[0], ALL_WORDS[0]), (ALL_WORDS[0], ALL_WORDS[-1]), (ALL_WORDS[-1], ALL_WORDS[-1]))))
    fixed = {START: H1, **MATCH_CAGE, **{site: H0 for site in CAGE_H0}, **{site: H1 for site in CAGE_H1}}
    canonical = canonical_records(fixed)
    stabilizer = sum(canonical_records({c53.matvec(rotation, site): content for site, content in fixed.items()}) == canonical for rotation in c53.ROTATIONS)
    check("B07 fixed 22-record cage has trivial proper-cubic stabilizer", len(fixed) == 22 and stabilizer == 1)
    check("B08 comparator still needs exactly three canonical rows", len(CANONICAL_TABLE) == 3 and sorted(map(len, CANONICAL_TABLE)) == [5, 5, 6])
    check("B09 comparator has 56 proper-cubic raw rows", len(RAW_OUTPUTS) == 56)
    check("B10 comparator uses and writes only H0/H1", {content for local in CANONICAL_TABLE for _offset, content in local} | set(CANONICAL_TABLE.values()) == {H0, H1})
    check("B11 comparator raw domain is disjoint from Cycle-58", set(RAW_OUTPUTS).isdisjoint(c58.RAW_OUTPUTS))
    check("B12 comparator raw domain is disjoint from selected recurrence union", set(RAW_OUTPUTS).isdisjoint(SELECTED_RAW_OUTPUTS))
    check("B13 provisional union has 4,564 raw rows", len(COMBINED_RAW_OUTPUTS) == 4_564)
    check("B14 provisional union is output-single-valued", all(len(values) == 1 for values in COMBINED_RAW_OUTPUTS.values()))


def exhaustive_contract() -> None:
    section("C - All 65,536 physical comparisons and reachable states")
    prefix_census: Counter[int] = Counter()
    failures = []
    states_count = edges = terminals = matches = maximum_enabled = 0
    for candidate in ALL_WORDS:
        for reference in ALL_WORDS:
            prefix_census[common_prefix(candidate, reference)] += 1
            for stage in stages(candidate, reference):
                records = stage_records(candidate, reference, stage)
                expected = expected_writes(candidate, reference, stage)
                actual = enabled_outputs(records)
                actual_assignments = {
                    site: next(iter(values)) if len(values) == 1 else "CONFLICT"
                    for site, values in actual.items()
                }
                states_count += 1
                edges += len(actual)
                maximum_enabled = max(maximum_enabled, len(actual))
                if actual_assignments != expected:
                    failures.append((candidate, reference, stage, expected, actual))
                if not expected:
                    terminals += 1
                    matches += int(MATCH in records)
    check("C01 first-difference census is exact", prefix_census == {
        0: 32_768, 1: 16_384, 2: 8_192, 3: 4_096, 4: 2_048,
        5: 1_024, 6: 512, 7: 256, 8: 256,
    }, str(prefix_census))
    check("C02 all 131,072 reachable states have exact frontier", states_count == 131_072 and not failures, str(failures[:1]))
    check("C03 all-pairs graph has exactly 65,536 edges", edges == 65_536, str(edges))
    check("C04 every pair has exactly one terminal", terminals == 65_536)
    check("C05 exactly the 256 equal pairs reach MATCH", matches == 256)
    check("C06 no state exposes more than one write", maximum_enabled == 1)
    false_naive = sum(common_prefix(left, right) < 8 and left[common_prefix(left, right)] == 0 and right[common_prefix(left, right)] == 1 for left in ALL_WORDS for right in ALL_WORDS)
    check("C07 rejected one-rail design would corrupt 32,640 pairs", false_naive == 32_640)


def covariance_and_scope_contract() -> None:
    section("D - Covariance and supplied-harness boundary")
    samples = (
        (ALL_WORDS[0], ALL_WORDS[0], Stage(0)),
        (ALL_WORDS[-1], ALL_WORDS[-1], Stage(5)),
        (ALL_WORDS[0], ALL_WORDS[1], Stage(7)),
        (ALL_WORDS[85], ALL_WORDS[85], Stage(8)),
        (ALL_WORDS[85], ALL_WORDS[85], Stage(8, match=True)),
    )
    failures = []
    shift = (41, -23, 17)
    for rotation_index, rotation in enumerate(c53.ROTATIONS):
        for candidate, reference, stage in samples:
            records = stage_records(candidate, reference, stage)
            expected = expected_writes(candidate, reference, stage)
            transformed = {c53.add(c53.matvec(rotation, site), shift): content for site, content in records.items()}
            transformed_expected = {c53.add(c53.matvec(rotation, site), shift): content for site, content in expected.items()}
            actual = enabled_outputs(transformed)
            if set(actual) != set(transformed_expected):
                failures.append((rotation_index, candidate, reference, stage, transformed_expected, actual))
    check("D01 all 120 transformed controls have exact frontier", not failures, str(failures[:1]))
    note = NOTE.read_text(encoding="utf-8").lower() if NOTE.is_file() else ""
    for marker in ("*", "`", ">"):
        note = note.replace(marker, "")
    note = " ".join(note.split())
    check("D02 note exists and carries no authority", NOTE.is_file() and "authority: none" in note)
    check("D03 note says the comparator harness is supplied", "38-record comparator harness is supplied" in note)
    check("D04 note names the surviving seed-growth residual", "seed_to_eight_bit_comparator_harness" in note)
    check("D05 note names the row-port next step", "directional_multiword_match_to_rule_port" in note)
    check("D06 note denies axiom consequence", "no axiom addition follows" in note)


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    inventory_contract()
    codebook_and_table_contract()
    exhaustive_contract()
    covariance_and_scope_contract()
    print("\nOUTPUT_ROLES=113 ACTIVE_ROLES=120 FULL_ROLES=134 BITS=8 RESERVED=122")
    print("COMPARATOR_CANONICAL=3 COMPARATOR_RAW=56 PAIR_STATES=131072 PAIR_EDGES=65536")
    print(f"SUMMARY: {PASS} PASS / {FAIL} FAIL")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
