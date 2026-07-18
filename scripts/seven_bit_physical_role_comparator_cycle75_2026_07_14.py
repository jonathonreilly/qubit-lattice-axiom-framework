#!/usr/bin/env python3
"""Cycle 75: seven-bit physical role inventory and local comparator.

The selected Cycle-60/Cycle-67/Cycle-72 exact-NN compiler is inventoried at
its actual boundary.  Its 62 output labels fit in six bits, but the exact
input/output alphabet contains 69 labels, so any injective operational
replacement needs seven binary records.  Including every otherwise inert
content in the concrete Cycle-72 source raises the inventory to 83 and does
not raise that bound.

The constructive probe then compares two supplied seven-record words without
reading a symbolic role.  Candidate and reference bits are H0/H1 records.  A
five-neighbour equality cage advances an H1 certificate chain exactly through
their common prefix; a six-neighbour H1 MATCH record can form only after all
seven equalities.  The table is tested on all 128^2 ordered word pairs, every
reachable chain state, and in union with the Cycle-58 and selected extensional
raw tables.

Authority: none.  The finite binary harness is supplied, not seed-grown.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass
from hashlib import sha256
from itertools import product
from math import ceil, log2
from pathlib import Path

import cycle67_terminal_bdh_rebind_cycle72_2026_07_14 as c72
import four_open_reservation_comb_cycle59_2026_07_14 as c59
import official_seed_to_rail_nucleation_cycle53_2026_07_14 as c53
import operational_binary_macrocode_compiler_cycle58_2026_07_14 as c58


ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / "docs" / "work_history" / "repo" / "review_feedback"
NOTE = REVIEW / "SEVEN_BIT_PHYSICAL_ROLE_COMPARATOR_CYCLE75_NOTE_2026-07-14.md"

Coord = tuple[int, int, int]
Word = tuple[int, int, int, int, int, int, int]
Signature = c53.Signature

H0 = "H0"
H1 = "H1"
BITS = (H0, H1)

EXPECTED_OUTPUT_DIGEST = "43de3d0275d001640b9a5c9e150828f890d66973d81402d66abbb06223d34e10"
EXPECTED_ACTIVE_DIGEST = "78d0fbf07bf904eacc87156d3464c1fa82de9c845d896f8598151b5aff4bbefa"
EXPECTED_SOURCE_DIGEST = "2b83cb0745b542f96852c8fa8763af97196bcda29440a1da9399c1bfa3786619"
EXPECTED_FULL_DIGEST = "7fd38947ef276e298736d54b55c27b79c75807120911b8f7603d70f8c8738248"

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


def digest(values: set[str] | frozenset[str]) -> str:
    return sha256("\n".join(sorted(values)).encode("utf-8")).hexdigest()


UNION_TABLE = c72.CONSTRUCTION.union_table
OUTPUT_ROLES = frozenset(UNION_TABLE.values())
INPUT_ROLES = frozenset(content for signature in UNION_TABLE for _offset, content in signature)
ACTIVE_ROLES = OUTPUT_ROLES | INPUT_ROLES
SOURCE_ROLES = frozenset(c72.CONSTRUCTION.source.values())
FULL_ROLES = ACTIVE_ROLES | SOURCE_ROLES
INPUT_ONLY_ROLES = INPUT_ROLES - OUTPUT_ROLES
SOURCE_ONLY_ROLES = SOURCE_ROLES - ACTIVE_ROLES


def int_word(value: int) -> Word:
    assert 0 <= value < 128
    return tuple((value >> shift) & 1 for shift in range(6, -1, -1))  # type: ignore[return-value]


ALL_WORDS: tuple[Word, ...] = tuple(product((0, 1), repeat=7))  # type: ignore[assignment]
ROLE_TO_WORD: dict[str, Word] = {
    role: int_word(index) for index, role in enumerate(sorted(FULL_ROLES))
}
WORD_TO_ROLE = {word: role for role, word in ROLE_TO_WORD.items()}
RESERVED_WORDS = tuple(word for word in ALL_WORDS if word not in WORD_TO_ROLE)


# Seed-frame presentation only.  The raw table is closed under all 24 proper
# cubic rotations, so no coordinate congruence or preferred global axis is a
# rule input.
CANDIDATE: tuple[Coord, ...] = tuple((index, 0, 0) for index in range(7))
REFERENCE: tuple[Coord, ...] = tuple((index, 2, 0) for index in range(7))
CERTIFICATE: tuple[Coord, ...] = tuple((index, 1, 0) for index in range(7))
CAGE_H0: tuple[Coord, ...] = tuple((index, 1, 1) for index in range(7))
CAGE_H1: tuple[Coord, ...] = tuple((index, 1, -1) for index in range(7))
START: Coord = (-1, 1, 0)
MATCH: Coord = (7, 1, 0)

# Together with CERTIFICATE[6], these five records completely surround MATCH.
MATCH_CAGE: dict[Coord, str] = {
    (7, 0, 0): H0,
    (7, 2, 0): H1,
    (7, 1, -1): H0,
    (7, 1, 1): H1,
    (8, 1, 0): H0,
}


def bit_content(bit: int) -> str:
    return H1 if bit else H0


def harness(candidate: Word, reference: Word) -> dict[Coord, str]:
    """Thirty-four supplied physical H0/H1 records; no role label occurs."""

    records: dict[Coord, str] = {START: H1, **MATCH_CAGE}
    records.update({site: bit_content(bit) for site, bit in zip(CANDIDATE, candidate)})
    records.update({site: bit_content(bit) for site, bit in zip(REFERENCE, reference)})
    records.update({site: H0 for site in CAGE_H0})
    records.update({site: H1 for site in CAGE_H1})
    return records


def common_prefix(candidate: Word, reference: Word) -> int:
    return next(
        (index for index, pair in enumerate(zip(candidate, reference)) if pair[0] != pair[1]),
        7,
    )


@dataclass(frozen=True)
class Stage:
    certificate_count: int
    match: bool = False


def stages(candidate: Word, reference: Word) -> tuple[Stage, ...]:
    prefix = common_prefix(candidate, reference)
    answer = [Stage(count) for count in range(prefix + 1)]
    if prefix == 7:
        answer.append(Stage(7, match=True))
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
    if prefix == 7 and not stage.match:
        return {MATCH: H1}
    return {}


def local_signature(records: dict[Coord, str], target: Coord) -> Signature:
    return c53.local_signature(records, target)


def build_new_canonical_table() -> dict[Signature, str]:
    table: dict[Signature, str] = {}

    def install(records: dict[Coord, str], target: Coord) -> None:
        signature = c53.canonical_signature(local_signature(records, target))
        prior = table.get(signature)
        if prior is not None and prior != H1:
            raise ValueError(f"comparator output conflict: {prior}/H1")
        table[signature] = H1

    zero = int_word(0)
    one = int_word(127)
    install(stage_records(zero, zero, Stage(0)), CERTIFICATE[0])
    install(stage_records(one, one, Stage(0)), CERTIFICATE[0])
    install(stage_records(zero, zero, Stage(7)), MATCH)
    return table


NEW_CANONICAL_TABLE = build_new_canonical_table()
NEW_RAW_OUTPUTS = c59.raw_rule_outputs(NEW_CANONICAL_TABLE)
SELECTED_RAW_OUTPUTS = c59.raw_rule_outputs(UNION_TABLE)


def merged_raw_outputs() -> dict[Signature, frozenset[str]]:
    outputs: dict[Signature, set[str]] = defaultdict(set)
    for table in (c58.RAW_OUTPUTS, SELECTED_RAW_OUTPUTS, NEW_RAW_OUTPUTS):
        for signature, values in table.items():
            outputs[signature].update(values)
    return {signature: frozenset(values) for signature, values in outputs.items()}


COMBINED_RAW_OUTPUTS = merged_raw_outputs()


def enabled_outputs(records: dict[Coord, str]) -> dict[Coord, frozenset[str]]:
    return {
        target: COMBINED_RAW_OUTPUTS[signature]
        for target in c53.open_candidates(records)
        if (signature := local_signature(records, target)) in COMBINED_RAW_OUTPUTS
    }


def canonical_records(records: dict[Coord, str]) -> tuple[tuple[Coord, str], ...]:
    minima = tuple(min(position[axis] for position in records) for axis in range(3))
    return tuple(sorted(
        (
            tuple(position[axis] - minima[axis] for axis in range(3)),
            content,
        )
        for position, content in records.items()
    ))


def transform_records(
    records: dict[Coord, str], rotation: c53.Matrix, shift: Coord
) -> dict[Coord, str]:
    return {
        c53.add(c53.matvec(rotation, position), shift): content
        for position, content in records.items()
    }


def inventory_contract() -> None:
    section("A - Exact selected-compiler role inventory and information bound")
    check("A01 selected union has 147 canonical rows", len(UNION_TABLE) == 147)
    check("A02 exact output inventory has 62 roles", len(OUTPUT_ROLES) == 62, str(sorted(OUTPUT_ROLES)))
    check("A03 output inventory digest is pinned", digest(OUTPUT_ROLES) == EXPECTED_OUTPUT_DIGEST)
    check("A04 output-only lower bound is six bits", ceil(log2(len(OUTPUT_ROLES))) == 6)
    check("A05 every output is also consumed as an input", OUTPUT_ROLES <= INPUT_ROLES)
    check("A06 active exact-law alphabet has 69 roles", len(ACTIVE_ROLES) == 69, str(sorted(ACTIVE_ROLES)))
    check("A07 active alphabet digest is pinned", digest(ACTIVE_ROLES) == EXPECTED_ACTIVE_DIGEST)
    check("A08 seven exact input-only roles close the 62-to-69 gap", INPUT_ONLY_ROLES == {
        "ARM", "A_0_2", "B_1_2", "COMPLETE", "JOIN", "RING", "Z0"
    })
    check("A09 six bits cannot injectively replace the active alphabet", 2 ** 6 < len(ACTIVE_ROLES) <= 2 ** 7)
    check("A10 concrete source has 66 contents and pinned digest", len(SOURCE_ROLES) == 66 and digest(SOURCE_ROLES) == EXPECTED_SOURCE_DIGEST)
    check("A11 fourteen source-only contents are exact", SOURCE_ONLY_ROLES == {
        "AUX", "A_0_0", "A_0_1", "A_1_0", "A_1_2", "A_2_0", "A_2_1",
        "A_2_2", "A_3_0", "A_3_1", "A_3_2", "BACKSTOP", "JOINT", "LAUNCH_A",
    })
    check("A12 full bounded replacement inventory has 83 roles", len(FULL_ROLES) == 83)
    check("A13 full replacement inventory digest is pinned", digest(FULL_ROLES) == EXPECTED_FULL_DIGEST)
    check("A14 seven bits are also sufficient and necessary for all 83", 2 ** 6 < len(FULL_ROLES) <= 2 ** 7)
    check("A15 union row arities are exact", Counter(map(len, UNION_TABLE)) == {1: 10, 2: 39, 3: 52, 4: 28, 5: 15, 6: 3})


def codebook_and_geometry_contract() -> None:
    section("B - Injective seven-bit words and seed-relative physical geometry")
    check("B01 all 83 roles have distinct seven-bit words", len(ROLE_TO_WORD) == len(set(ROLE_TO_WORD.values())) == 83)
    check("B02 exact capacity leaves 45 reserved words", len(RESERVED_WORDS) == 45)
    check("B03 assigned and reserved words partition all 128", set(ROLE_TO_WORD.values()).isdisjoint(RESERVED_WORDS) and set(ROLE_TO_WORD.values()) | set(RESERVED_WORDS) == set(ALL_WORDS))
    check("B04 diagnostic inverse is exact", all(WORD_TO_ROLE[word] == role for role, word in ROLE_TO_WORD.items()))
    check("B05 candidate/reference/certificate spines each contain seven sites", all(len(spine) == len(set(spine)) == 7 for spine in (CANDIDATE, REFERENCE, CERTIFICATE)))
    check("B06 each spine is nearest-neighbour connected", all(
        c53.subtract(spine[index + 1], spine[index]) in c53.DIRECTIONS
        for spine in (CANDIDATE, REFERENCE, CERTIFICATE)
        for index in range(6)
    ))
    check("B07 each certificate site touches its two bits and two cage rails", all(
        {c53.subtract(site, CERTIFICATE[index]) for site in (
            CANDIDATE[index], REFERENCE[index], CAGE_H0[index], CAGE_H1[index]
        )} <= set(c53.DIRECTIONS)
        for index in range(7)
    ))
    check("B08 every comparator harness has exactly 34 supplied records", all(
        len(harness(candidate, reference)) == 34
        for candidate, reference in ((ALL_WORDS[0], ALL_WORDS[0]), (ALL_WORDS[0], ALL_WORDS[-1]), (ALL_WORDS[-1], ALL_WORDS[-1]))
    ))
    check("B09 supplied harness contains only physical H0/H1", all(
        set(harness(candidate, reference).values()) <= set(BITS)
        for candidate, reference in ((ALL_WORDS[0], ALL_WORDS[0]), (ALL_WORDS[0], ALL_WORDS[-1]), (ALL_WORDS[-1], ALL_WORDS[-1]))
    ))
    fixed_cage = {START: H1, **MATCH_CAGE, **{site: H0 for site in CAGE_H0}, **{site: H1 for site in CAGE_H1}}
    canonical = canonical_records(fixed_cage)
    stabilizer = sum(
        canonical_records({c53.matvec(rotation, site): content for site, content in fixed_cage.items()}) == canonical
        for rotation in c53.ROTATIONS
    )
    check("B10 fixed cage has trivial proper-cubic stabilizer", stabilizer == 1)


def naive_collision_and_rule_contract() -> None:
    section("C - Naive collision rejected and five/six-neighbour repair")
    zero = int_word(0)
    one = int_word(127)

    # Delete the H1 cage rail from one mismatched bit.  The remaining
    # four-neighbour signature is already Cycle 58's physical copy-H1 row.
    naive = harness(zero, one)
    del naive[CAGE_H1[0]]
    naive_mismatch = local_signature(naive, CERTIFICATE[0])
    check("C01 one-rail 0/1 mismatch collides with Cycle-58", naive_mismatch in c58.RAW_OUTPUTS)
    check("C02 naive collision would append parasitic H0", c58.RAW_OUTPUTS.get(naive_mismatch) == frozenset((H0,)))
    false_pairs = sum(
        common_prefix(candidate, reference) < 7
        and candidate[common_prefix(candidate, reference)] == 0
        and reference[common_prefix(candidate, reference)] == 1
        for candidate in ALL_WORDS for reference in ALL_WORDS
    )
    check("C03 naive collision affects exactly 8,128 ordered pairs", false_pairs == 8_128)

    check("C04 repaired comparator has three canonical rows", len(NEW_CANONICAL_TABLE) == 3)
    check("C05 equality rows have five neighbours and MATCH has six", sorted(map(len, NEW_CANONICAL_TABLE)) == [5, 5, 6])
    check("C06 repaired proper-cubic table has 56 raw rows", len(NEW_RAW_OUTPUTS) == 56)
    check("C07 every repaired raw row writes physical H1", all(values == frozenset((H1,)) for values in NEW_RAW_OUTPUTS.values()))
    check("C08 repaired input and output alphabet is only H0/H1", {
        content for signature in NEW_CANONICAL_TABLE for _offset, content in signature
    } | set(NEW_CANONICAL_TABLE.values()) == {H0, H1})
    check("C09 repaired raw domain is disjoint from Cycle-58", set(NEW_RAW_OUTPUTS).isdisjoint(c58.RAW_OUTPUTS))
    check("C10 repaired raw domain is disjoint from selected extensional union", set(NEW_RAW_OUTPUTS).isdisjoint(SELECTED_RAW_OUTPUTS))
    check("C11 Cycle-58 and selected extensional domains are disjoint", set(c58.RAW_OUTPUTS).isdisjoint(SELECTED_RAW_OUTPUTS))
    check("C12 full provisional union has 3,394 raw rows", len(COMBINED_RAW_OUTPUTS) == 3_394)
    check("C13 full provisional union is output-single-valued", all(len(outputs) == 1 for outputs in COMBINED_RAW_OUTPUTS.values()))


def exhaustive_comparator_contract() -> None:
    section("D - Collision-complete all-pairs physical comparison")
    failures = []
    prefix_census: Counter[int] = Counter()
    state_count = 0
    edge_count = 0
    terminal_count = 0
    matched_terminals = 0
    maximum_enabled = 0

    for candidate in ALL_WORDS:
        for reference in ALL_WORDS:
            prefix = common_prefix(candidate, reference)
            prefix_census[prefix] += 1
            pair_stages = stages(candidate, reference)
            for stage in pair_stages:
                records = stage_records(candidate, reference, stage)
                expected = expected_writes(candidate, reference, stage)
                actual = enabled_outputs(records)
                maximum_enabled = max(maximum_enabled, len(actual))
                state_count += 1
                edge_count += len(actual)
                if set(actual) != set(expected) or any(values != frozenset((output,)) for (site, output), values in zip(sorted(expected.items()), (actual[site] for site in sorted(expected)))):
                    failures.append((candidate, reference, stage, expected, actual))
                if not expected:
                    terminal_count += 1
                    if MATCH in records:
                        matched_terminals += 1

    check("D01 first-difference census is exact", prefix_census == {
        0: 8_192, 1: 4_096, 2: 2_048, 3: 1_024,
        4: 512, 5: 256, 6: 128, 7: 128,
    }, str(prefix_census))
    check("D02 all 32,768 reachable states have exact frontier", not failures, str(failures[:1]))
    check("D03 all-pairs graph has 16,384 append edges", edge_count == 16_384, str(edge_count))
    check("D04 every ordered pair has exactly one terminal", terminal_count == 16_384)
    check("D05 exactly 128 equal pairs reach physical MATCH", matched_terminals == 128)
    check("D06 no unequal pair reaches MATCH", matched_terminals == len(ALL_WORDS))
    check("D07 no state exposes more than one comparator write", maximum_enabled == 1)
    check("D08 mismatch terminal retains exactly the common-prefix certificates", all(
        Stage(common_prefix(candidate, reference)) == stages(candidate, reference)[-1]
        for candidate in ALL_WORDS for reference in ALL_WORDS if candidate != reference
    ))


def covariance_and_residual_contract() -> None:
    section("E - Proper-cubic covariance and exact remaining obligations")
    samples = (
        (int_word(0), int_word(0), Stage(0)),
        (int_word(127), int_word(127), Stage(4)),
        (int_word(0), int_word(1), Stage(6)),
        (int_word(85), int_word(85), Stage(7)),
        (int_word(85), int_word(85), Stage(7, match=True)),
    )
    failures = []
    shift = (31, -19, 11)
    for rotation_index, rotation in enumerate(c53.ROTATIONS):
        for candidate, reference, stage in samples:
            records = stage_records(candidate, reference, stage)
            expected = expected_writes(candidate, reference, stage)
            transformed = transform_records(records, rotation, shift)
            transformed_expected = transform_records(expected, rotation, shift)
            actual = enabled_outputs(transformed)
            if set(actual) != set(transformed_expected):
                failures.append((rotation_index, candidate, reference, stage, transformed_expected, actual))
    check("E01 all 120 transformed sample states have exact transformed frontier", not failures, str(failures[:1]))

    note = NOTE.read_text(encoding="utf-8").lower() if NOTE.is_file() else ""
    for marker in ("*", "`", ">"):
        note = note.replace(marker, "")
    note = " ".join(note.split())
    check("E02 note exists", NOTE.is_file())
    check("E03 note states authority none", "authority: none" in note)
    check("E04 note names supplied-harness residual", "seed_to_seven_bit_comparator_harness" in note)
    check("E05 note names multiword rule-port residual", "directional_multiword_match_to_rule_port" in note)
    check("E06 note names output construction residual", "rule_port_to_seven_bit_output_word" in note)
    check("E07 note does not claim the harness is seed-grown", "the 34-record comparator harness is supplied" in note)
    check("E08 note denies symbolic role input to the comparator", "the comparator never receives a role label" in note)
    check("E09 note denies constitutional consequence", "no axiom addition follows" in note)


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    inventory_contract()
    codebook_and_geometry_contract()
    naive_collision_and_rule_contract()
    exhaustive_comparator_contract()
    covariance_and_residual_contract()
    print("\nOUTPUT_ROLES=62 ACTIVE_ROLES=69 FULL_ROLES=83 BITS=7 RESERVED=45")
    print("COMPARATOR_CANONICAL=3 COMPARATOR_RAW=56 ALL_PAIR_STATES=32768 ALL_PAIR_EDGES=16384")
    print(f"SUMMARY: {PASS} PASS / {FAIL} FAIL")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
