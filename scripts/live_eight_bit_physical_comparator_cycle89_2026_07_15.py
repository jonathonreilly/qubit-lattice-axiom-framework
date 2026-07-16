#!/usr/bin/env python3
"""Cycle 89: port the physical eight-bit comparator to the live Cycle-85 law.

Cycle 85 replaces the stale Cycle-72 composition used by Cycles 75/81/82/86/87
with the live Cycle-78 endpoint, its physical tube bridge, and Cycle-80
recurrence.  This runner rebuilds the exact role inventory and extends the old
eight-bit codebook only for genuinely new live roles.  The physical H0/H1
comparator is then exhausted over all 256^2 words against the corrected raw
union.

Authority: none.  The 38-record comparator harness is supplied, not grown.
Historical runners are imported only for their already-tested code assignment;
none of their stale selected-law unions is reused.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass
from hashlib import sha256
from itertools import product
from math import ceil, log2
from pathlib import Path

import cycle80_recurrence_audit_endpoint_tube_nucleation_cycle85_2026_07_14 as c85
import eight_bit_physical_role_comparator_cycle81_2026_07_14 as c81
import four_open_reservation_comb_cycle59_2026_07_14 as c59
import official_seed_to_rail_nucleation_cycle53_2026_07_14 as c53
import operational_binary_macrocode_compiler_cycle58_2026_07_14 as c58


ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / "docs" / "work_history" / "repo" / "review_feedback"
NOTE = REVIEW / "LIVE_EIGHT_BIT_PHYSICAL_COMPARATOR_CYCLE89_NOTE_2026-07-15.md"

Coord = tuple[int, int, int]
Word = tuple[int, int, int, int, int, int, int, int]
Signature = c53.Signature
H0 = "H0"
H1 = "H1"

EXPECTED_OUTPUT_DIGEST = "45cc68a8fffa4cbb1bbf1fc4dd7131cbfcd40a8d1198baa4e2827747733920e1"
EXPECTED_ACTIVE_DIGEST = "fcefe41c036199b4af8f5e6aaaa9d2cac4f373845a9bb27b0209b2655caf015d"
EXPECTED_SOURCE_DIGEST = "76d17e30efc9cbe31ab0f29f2673b08c92d51f790bcf484610703f760b8fd573"
EXPECTED_FULL_DIGEST = "2ca9ca3693fa35505a034fd716d41c104288a65bf13595307c9b1786d4828c0d"
EXPECTED_NEW_DIGEST = "a14ae29420e79ace969f99bd553611365926211fb1771ae2feb4a0b5673b6dc0"

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


LIVE_TABLE = dict(c85.BRIDGE.union_with_recurrence)
LIVE_RAW_OUTPUTS = c59.raw_rule_outputs(LIVE_TABLE)
OUTPUT_ROLES = frozenset(LIVE_TABLE.values())
INPUT_ROLES = frozenset(content for local in LIVE_TABLE for _offset, content in local)
ACTIVE_ROLES = OUTPUT_ROLES | INPUT_ROLES
SOURCE_ROLES = frozenset(c85.BRIDGE.source.values())
FULL_ROLES = ACTIVE_ROLES | SOURCE_ROLES

ALL_WORDS: tuple[Word, ...] = tuple(product((0, 1), repeat=8))  # type: ignore[assignment]
EMPTY_WORD: Word = (1,) * 8

# Preserve every Cycle-81 assignment whose role survives.  Cycle 85's full
# alphabet is a strict 19-role extension, so no old physical word must move.
OLD_ROLES = frozenset(c81.ROLE_TO_WORD)
NEW_ROLES = FULL_ROLES - OLD_ROLES
AVAILABLE_EXTENSION_WORDS = tuple(
    word for word in ALL_WORDS
    if word not in c81.WORD_TO_ROLE and word != EMPTY_WORD
)
ROLE_TO_WORD: dict[str, Word] = dict(c81.ROLE_TO_WORD)
ROLE_TO_WORD.update({
    role: word
    for role, word in zip(sorted(NEW_ROLES), AVAILABLE_EXTENSION_WORDS)
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
    return next((index for index, pair in enumerate(zip(candidate, reference)) if pair[0] != pair[1]), 8)


@dataclass(frozen=True)
class Stage:
    certificate_count: int
    match: bool = False


def stages(candidate: Word, reference: Word) -> tuple[Stage, ...]:
    prefix = common_prefix(candidate, reference)
    result = [Stage(count) for count in range(prefix + 1)]
    if prefix == 8:
        result.append(Stage(8, match=True))
    return tuple(result)


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


def merge_raw_outputs() -> dict[Signature, frozenset[str]]:
    outputs: dict[Signature, set[str]] = defaultdict(set)
    for table in (c58.RAW_OUTPUTS, LIVE_RAW_OUTPUTS, RAW_OUTPUTS):
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


def assignments(records: dict[Coord, str]) -> dict[Coord, str]:
    return {
        site: next(iter(values)) if len(values) == 1 else "CONFLICT"
        for site, values in enabled_outputs(records).items()
    }


def canonical_records(records: dict[Coord, str]) -> tuple[tuple[Coord, str], ...]:
    minima = tuple(min(site[axis] for site in records) for axis in range(3))
    return tuple(sorted(
        (tuple(site[axis] - minima[axis] for axis in range(3)), content)
        for site, content in records.items()
    ))


def inventory_contract() -> None:
    section("A - Corrected live inventory and exact eight-bit bound")
    check("A01 live table is exactly Cycle-85 bridge union", LIVE_TABLE == c85.BRIDGE.union_with_recurrence)
    check("A02 live table has 236 canonical and 5,240 raw rows", len(LIVE_TABLE) == 236 and len(LIVE_RAW_OUTPUTS) == 5_240)
    check("A03 live arity census is pinned", Counter(map(len, LIVE_TABLE)) == {1: 13, 2: 96, 3: 67, 4: 36, 5: 20, 6: 4})
    check("A04 exact output inventory has 132 roles", len(OUTPUT_ROLES) == 132 and digest(OUTPUT_ROLES) == EXPECTED_OUTPUT_DIGEST)
    check("A05 exact active inventory has 139 roles", len(ACTIVE_ROLES) == 139 and INPUT_ROLES == ACTIVE_ROLES and digest(ACTIVE_ROLES) == EXPECTED_ACTIVE_DIGEST)
    check("A06 completed live endpoint supplies 91 roles", len(SOURCE_ROLES) == 91 and digest(SOURCE_ROLES) == EXPECTED_SOURCE_DIGEST)
    check("A07 source-preserving alphabet has 153 roles", len(FULL_ROLES) == 153 and digest(FULL_ROLES) == EXPECTED_FULL_DIGEST)
    check("A08 eight bits are necessary and sufficient", ceil(log2(len(FULL_ROLES))) == 8 and 2 ** 7 < len(FULL_ROLES) <= 2 ** 8)


def codebook_and_table_contract() -> None:
    section("B - Minimal live codebook extension and physical comparator table")
    check("B01 old 134-role alphabet is an exact live subset", len(OLD_ROLES) == 134 and OLD_ROLES <= FULL_ROLES)
    check("B02 exactly nineteen new roles are pinned", len(NEW_ROLES) == 19 and digest(NEW_ROLES) == EXPECTED_NEW_DIGEST)
    check("B03 all old physical codewords are preserved", all(ROLE_TO_WORD[role] == word for role, word in c81.ROLE_TO_WORD.items()))
    check("B04 all 153 live roles have distinct words", set(ROLE_TO_WORD) == FULL_ROLES and len(set(ROLE_TO_WORD.values())) == 153)
    check("B05 EMPTY=11111111 remains reserved", EMPTY_WORD in RESERVED_WORDS and EMPTY_WORD not in WORD_TO_ROLE)
    check("B06 exactly 103 words remain reserved", len(RESERVED_WORDS) == 103 and len(set(RESERVED_WORDS)) == 103)
    check("B07 assigned and reserved words partition 256", set(ROLE_TO_WORD.values()).isdisjoint(RESERVED_WORDS) and set(ROLE_TO_WORD.values()) | set(RESERVED_WORDS) == set(ALL_WORDS))
    check("B08 every harness contains exactly 38 H0/H1 records", all(len(harness(left, right)) == 38 and set(harness(left, right).values()) == {H0, H1} for left, right in ((ALL_WORDS[0], ALL_WORDS[0]), (ALL_WORDS[0], ALL_WORDS[-1]), (ALL_WORDS[-1], ALL_WORDS[-1]))))
    fixed = {START: H1, **MATCH_CAGE, **{site: H0 for site in CAGE_H0}, **{site: H1 for site in CAGE_H1}}
    canonical = canonical_records(fixed)
    stabilizer = sum(canonical_records({c53.matvec(rotation, site): content for site, content in fixed.items()}) == canonical for rotation in c53.ROTATIONS)
    check("B09 fixed 22-record cage has trivial proper-cubic stabilizer", len(fixed) == 22 and stabilizer == 1)
    check("B10 comparator has three canonical and 56 raw rows", len(CANONICAL_TABLE) == 3 and sorted(map(len, CANONICAL_TABLE)) == [5, 5, 6] and len(RAW_OUTPUTS) == 56)
    check("B11 comparator consumes and writes only H0/H1", {content for local in CANONICAL_TABLE for _offset, content in local} | set(CANONICAL_TABLE.values()) == {H0, H1})
    check("B12 live, binary, and comparator raw domains are pairwise disjoint", set(LIVE_RAW_OUTPUTS).isdisjoint(c58.RAW_OUTPUTS) and set(LIVE_RAW_OUTPUTS).isdisjoint(RAW_OUTPUTS) and set(c58.RAW_OUTPUTS).isdisjoint(RAW_OUTPUTS))
    check("B13 corrected comparator union has 5,428 raw rows", len(COMBINED_RAW_OUTPUTS) == 5_428)
    check("B14 corrected comparator union is output-single-valued", all(len(values) == 1 for values in COMBINED_RAW_OUTPUTS.values()))


def exhaustive_contract() -> None:
    section("C - All 65,536 comparisons and every reachable stage")
    prefix_census: Counter[int] = Counter()
    failures = []
    state_count = edges = terminals = matches = maximum_enabled = 0
    for candidate in ALL_WORDS:
        for reference in ALL_WORDS:
            prefix_census[common_prefix(candidate, reference)] += 1
            for stage in stages(candidate, reference):
                records = stage_records(candidate, reference, stage)
                expected = expected_writes(candidate, reference, stage)
                actual = assignments(records)
                state_count += 1
                edges += len(actual)
                terminals += int(not expected)
                matches += int(not expected and MATCH in records)
                maximum_enabled = max(maximum_enabled, len(actual))
                if actual != expected:
                    failures.append((candidate, reference, stage, expected, actual))
    check("C01 first-difference census is exact", prefix_census == {0: 32_768, 1: 16_384, 2: 8_192, 3: 4_096, 4: 2_048, 5: 1_024, 6: 512, 7: 256, 8: 256}, str(prefix_census))
    check("C02 all 131,072 stages have exact frontier", state_count == 131_072 and not failures, str(failures[:1]))
    check("C03 all-pairs graph has 65,536 edges and terminals", edges == terminals == 65_536, str((edges, terminals)))
    check("C04 exactly 256 equal pairs reach MATCH", matches == 256)
    check("C05 no stage exposes more than one write", maximum_enabled == 1)
    check("C06 every assigned live role compares equal to itself", all(common_prefix(word, word) == 8 for word in ROLE_TO_WORD.values()))


def covariance_and_scope_contract() -> None:
    section("D - Proper-cubic covariance and historical boundary")
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
            actual = assignments(transformed)
            if actual != transformed_expected:
                failures.append((rotation_index, candidate, reference, stage, transformed_expected, actual))
    check("D01 all 120 transformed controls have exact frontier", not failures, str(failures[:1]))
    note = NOTE.read_text(encoding="utf-8").lower() if NOTE.is_file() else ""
    for marker in ("*", "`", ">"):
        note = note.replace(marker, "")
    note = " ".join(note.split())
    check("D02 note exists and carries authority none", NOTE.is_file() and "authority: none" in note)
    check("D03 note names Cycle 85 as the only selected base", "cycle 85 is the sole selected-law base" in note)
    check("D04 note preserves Cycles 81/82/86/87 as historical", "cycles 81, 82, 86, and 87 remain historical" in note)
    check("D05 note states the 38-record harness is supplied", "38-record comparator harness is supplied" in note)
    check("D06 note denies foundation and axiom effects", "no foundation edit" in note and "no axiom addition follows" in note)


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    inventory_contract()
    codebook_and_table_contract()
    exhaustive_contract()
    covariance_and_scope_contract()
    print("\nLIVE_CANONICAL=236 LIVE_RAW=5240 OUTPUT_ROLES=132 ACTIVE_ROLES=139 FULL_ROLES=153")
    print("BITS=8 OLD_WORDS=134 NEW_WORDS=19 RESERVED=103 EMPTY=11111111")
    print("COMPARATOR_CANONICAL=3 COMPARATOR_RAW=56 PHYSICAL_UNION_RAW=5428")
    print(f"SUMMARY: {PASS} PASS / {FAIL} FAIL")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
