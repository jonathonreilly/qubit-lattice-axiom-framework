#!/usr/bin/env python3
"""Cycle 93: total-status comparator and physical serial-reject port.

The live 48-bit comparator is extended from quiet-on-mismatch equality to a
total H1/H0 status chain.  H1 means equal so far; H0 means a mismatch has
already occurred.  A guarded final cell sends terminal H1 into the existing
output writer and turns terminal H0 into a physical AUX reject record.

This closes the decision primitive for a serial row selector.  Candidate
transport from AUX to the next reference and seed-grown harness placement are
not constructed here.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from pathlib import Path

import four_open_reservation_comb_cycle59_2026_07_14 as c59
import live_directional_program_writer_cycle90_2026_07_15 as c90
import official_seed_to_rail_nucleation_cycle53_2026_07_14 as c53
import open_direction_empty_slot_cycle86_2026_07_14 as c86


ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / "docs" / "work_history" / "repo" / "review_feedback"
NOTE = REVIEW / "TOTAL_STATUS_SERIAL_REJECT_SELECTOR_CYCLE93_NOTE_2026-07-15.md"

Coord = tuple[int, int, int]
Signature = c53.Signature
Program = tuple[int, ...]
Word = c90.Word
H0 = "H0"
H1 = "H1"
ALL = "ALL"
REJECT = "AUX"
FINAL = (48, 1, 0)
FINAL_GUARD = (48, 0, 0)
FINAL_BLOCKER = (48, -1, 0)

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


def bit_content(bit: int) -> str:
    return H1 if bit else H0


def build_status_table() -> dict[Signature, str]:
    table: dict[Signature, str] = {}
    for previous in (H0, H1):
        for candidate in (H0, H1):
            for reference in (H0, H1):
                records = {
                    (-1, 1, 0): previous,
                    (0, 0, 0): candidate,
                    (0, 2, 0): reference,
                    (0, 1, 1): H0,
                    (0, 1, -1): H1,
                }
                local = c53.canonical_signature(
                    c53.local_signature(records, (0, 1, 0))
                )
                output = (
                    H1
                    if previous == H1 and candidate == reference
                    else H0
                )
                prior = table.get(local)
                if prior is not None and prior != output:
                    raise ValueError((local, prior, output))
                table[local] = output
    return table


def build_final_table() -> dict[Signature, str]:
    table: dict[Signature, str] = {}
    for status in (H0, H1):
        for program_bit in (0, 1):
            records = {
                (47, 1, 0): status,
                (48, 2, 0): bit_content(program_bit),
                FINAL_GUARD: ALL,
                (48, 1, 1): H0,
                (48, 1, -1): H0,
            }
            local = c53.canonical_signature(c53.local_signature(records, FINAL))
            output = bit_content(program_bit) if status == H1 else REJECT
            prior = table.get(local)
            if prior is not None and prior != output:
                raise ValueError((local, prior, output))
            table[local] = output
    return table


STATUS_TABLE = build_status_table()
FINAL_TABLE = build_final_table()
STATUS_RAW = c59.raw_rule_outputs(STATUS_TABLE)
FINAL_RAW = c59.raw_rule_outputs(FINAL_TABLE)


def merge_raw() -> dict[Signature, frozenset[str]]:
    outputs: dict[Signature, set[str]] = defaultdict(set)
    for table in (
        c90.COMBINED_RAW,
        c86.RAW_OUTPUTS,
        STATUS_RAW,
        FINAL_RAW,
    ):
        for local, values in table.items():
            outputs[local].update(values)
    return {local: frozenset(values) for local, values in outputs.items()}


COMBINED_RAW = merge_raw()


def status_prefix(candidate: Program, reference: Program, count: int) -> dict[Coord, str]:
    equal_so_far = True
    answer: dict[Coord, str] = {}
    for index in range(count):
        equal_so_far = (
            equal_so_far and candidate[index] == reference[index]
        )
        answer[(index, 1, 0)] = H1 if equal_so_far else H0
    return answer


def records(
    candidate: Program,
    reference: Program,
    output_word: Word,
    certificate_count: int,
    *,
    output_step: int = 0,
    reject: bool = False,
) -> dict[Coord, str]:
    assert len(candidate) == len(reference) == 48
    assert 0 <= certificate_count <= 48
    state = c90.stream_harness(candidate, reference)
    state.update(c90.output_harness(output_word, port=False, shift_x=48))
    state[FINAL_GUARD] = ALL
    state[FINAL_BLOCKER] = H0
    state.update(status_prefix(candidate, reference, certificate_count))
    if output_step:
        state.update(dict(c90.output_additions(output_word, 48)[:output_step]))
    if reject:
        state[FINAL] = REJECT
    return state


def assignments(state: dict[Coord, str]) -> dict[Coord, str]:
    answer: dict[Coord, str] = {}
    for target in c53.open_candidates(state):
        local = c53.local_signature(state, target)
        if local not in COMBINED_RAW:
            continue
        values = COMBINED_RAW[local]
        answer[target] = next(iter(values)) if len(values) == 1 else "CONFLICT"
    return answer


def expected_next_status(
    candidate: Program, reference: Program, count: int
) -> str:
    return H1 if candidate[: count + 1] == reference[: count + 1] else H0


def table_and_union_contract() -> None:
    section("A - Total status, guarded final cell, and live union")
    check("A01 note exists", NOTE.is_file())
    check("A02 live bank contains 236 programs", len(c90.ROW_PROGRAMS) == 236)
    check("A03 ALL and AUX are already in the live source alphabet", {ALL, REJECT} <= c90.c89.FULL_ROLES)
    check("A04 status truth table collapses to six canonical rows", len(STATUS_TABLE) == 6)
    check("A05 status table has 144 proper-cubic raw rows", len(STATUS_RAW) == 144)
    overlap = set(STATUS_RAW) & set(c90.COMBINED_RAW)
    check("A06 48 status overlaps are safe identical-H1 rows", len(overlap) == 48 and all(STATUS_RAW[local] == c90.COMBINED_RAW[local] == frozenset((H1,)) for local in overlap))
    check("A07 guarded final table has four canonical / 96 raw rows", len(FINAL_TABLE) == 4 and len(FINAL_RAW) == 96)
    check("A08 guarded final raw domain is disjoint from prior mechanisms", set(FINAL_RAW).isdisjoint(c90.COMBINED_RAW) and set(FINAL_RAW).isdisjoint(c86.RAW_OUTPUTS) and set(FINAL_RAW).isdisjoint(STATUS_RAW))
    check("A09 corrected total-selector union has 5,680 raw rows", len(COMBINED_RAW) == 5_680)
    check("A10 every raw input has one output", all(len(values) == 1 for values in COMBINED_RAW.values()))

    truth_failures = []
    for previous in (H0, H1):
        for candidate in (H0, H1):
            for reference in (H0, H1):
                state = {
                    (-1, 1, 0): previous,
                    (0, 0, 0): candidate,
                    (0, 2, 0): reference,
                    (0, 1, 1): H0,
                    (0, 1, -1): H1,
                }
                local = c53.canonical_signature(
                    c53.local_signature(state, (0, 1, 0))
                )
                expected = H1 if previous == H1 and candidate == reference else H0
                if STATUS_TABLE.get(local) != expected:
                    truth_failures.append((previous, candidate, reference, expected, STATUS_TABLE.get(local)))
    check("A11 all eight status truth assignments are exact", not truth_failures, str(truth_failures))


def exact_program_pipeline_contract() -> None:
    section("B - Every live row reaches its exact output word")
    failures = []
    states = edges = terminals = 0
    decoded = set()
    for local, output in c90.c89.LIVE_TABLE.items():
        program = c90.ROW_PROGRAMS[local]
        output_word = c90.c89.ROLE_TO_WORD[output]
        additions = c90.output_additions(output_word, 48)
        for count in range(49):
            state = records(program, program, output_word, count)
            expected = (
                {(count, 1, 0): H1}
                if count < 48
                else {additions[0][0]: additions[0][1]}
            )
            actual = assignments(state)
            states += 1
            edges += len(actual)
            if actual != expected:
                failures.append((output, "compare", count, expected, actual))
        for step in range(1, 18):
            state = records(
                program,
                program,
                output_word,
                48,
                output_step=step,
            )
            expected = (
                {additions[step][0]: additions[step][1]}
                if step < 17
                else {}
            )
            actual = assignments(state)
            states += 1
            edges += len(actual)
            terminals += int(not expected)
            if actual != expected:
                failures.append((output, "write", step, expected, actual))
            if step == 17:
                decoded.add(c90.decode_output(state, 48))
    check("B01 all 15,576 exact-row states have exact frontier", states == 15_576 and not failures, str(failures[:1]))
    check("B02 exact-row corpus has 15,340 edges / 236 terminals", (edges, terminals) == (15_340, 236), str((edges, terminals)))
    check("B03 every terminal decodes to its associated live output", decoded == {c90.c89.ROLE_TO_WORD[output] for output in c90.c89.LIVE_TABLE.values()})


def off_bank_one_bit_contract() -> None:
    section("C - All one-bit perturbations reject physically")
    failures = []
    perturbations = pre_edges = post_edges = 0
    exercised_flips: set[int] = set()
    for local, output in c90.c89.LIVE_TABLE.items():
        reference = c90.ROW_PROGRAMS[local]
        output_word = c90.c89.ROLE_TO_WORD[output]
        for flip in range(48):
            candidate = tuple(
                1 - bit if index == flip else bit
                for index, bit in enumerate(reference)
            )
            pre = records(candidate, reference, output_word, 48)
            actual_pre = assignments(pre)
            post = records(
                candidate,
                reference,
                output_word,
                48,
                reject=True,
            )
            actual_post = assignments(post)
            perturbations += 1
            exercised_flips.add(flip)
            pre_edges += len(actual_pre)
            post_edges += len(actual_post)
            if actual_pre != {FINAL: REJECT} or actual_post:
                failures.append((output, flip, actual_pre, actual_post))
    check("C01 all 11,328 one-bit perturbations reach AUX then stop", perturbations == 11_328 and not failures, str(failures[:1]))
    check("C02 perturbation corpus has one reject edge then zero", (pre_edges, post_edges) == (11_328, 0), str((pre_edges, post_edges)))
    check("C03 one-bit corpus exercises all 48 mismatch positions", exercised_flips == set(range(48)))


def all_selected_pair_contract() -> None:
    section("D - Every unequal selected-program pair rejects")
    items = tuple(c90.ROW_PROGRAMS.items())
    failures = []
    unequal = pre_edges = post_edges = 0
    first_difference: Counter[int] = Counter()
    for candidate_local, candidate in items:
        for reference_local, reference in items:
            if candidate_local == reference_local:
                continue
            output = c90.c89.LIVE_TABLE[reference_local]
            output_word = c90.c89.ROLE_TO_WORD[output]
            first = next(
                index
                for index, pair in enumerate(zip(candidate, reference))
                if pair[0] != pair[1]
            )
            first_difference[first] += 1
            pre = records(candidate, reference, output_word, 48)
            actual_pre = assignments(pre)
            post = records(
                candidate,
                reference,
                output_word,
                48,
                reject=True,
            )
            actual_post = assignments(post)
            unequal += 1
            pre_edges += len(actual_pre)
            post_edges += len(actual_post)
            if actual_pre != {FINAL: REJECT} or actual_post:
                failures.append((candidate_local, reference_local, actual_pre, actual_post))
                break
        if failures:
            break
    check("D01 all 55,460 unequal live-program pairs reach AUX then stop", unequal == 55_460 and not failures, str(failures[:1]))
    check("D02 selected-pair corpus has one reject edge then zero", (pre_edges, post_edges) == (55_460, 0), str((pre_edges, post_edges)))
    expected_positions = {
        0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
        16, 17, 19, 20, 24, 32, 35, 37, 40, 45,
    }
    check("D03 selected bank has the exact 26-position first-difference support", set(first_difference) == expected_positions, str(sorted(first_difference)))


def covariance_and_scope_contract() -> None:
    section("E - Covariance and exact residual")
    local, output = next(iter(c90.c89.LIVE_TABLE.items()))
    reference = c90.ROW_PROGRAMS[local]
    mismatch = tuple(1 - bit if index == 17 else bit for index, bit in enumerate(reference))
    output_word = c90.c89.ROLE_TO_WORD[output]
    additions = c90.output_additions(output_word, 48)
    samples = (
        (records(reference, reference, output_word, 0), {(0, 1, 0): H1}),
        (records(reference, reference, output_word, 48), {additions[0][0]: additions[0][1]}),
        (records(mismatch, reference, output_word, 48), {FINAL: REJECT}),
        (records(mismatch, reference, output_word, 48, reject=True), {}),
    )
    failures = []
    shift = (97, -53, 31)
    for rotation_index, rotation in enumerate(c53.ROTATIONS):
        for state, expected in samples:
            transformed = {
                c53.add(c53.matvec(rotation, site), shift): content
                for site, content in state.items()
            }
            transformed_expected = {
                c53.add(c53.matvec(rotation, site), shift): content
                for site, content in expected.items()
            }
            actual = assignments(transformed)
            if actual != transformed_expected:
                failures.append((rotation_index, transformed_expected, actual))
    check("E01 all 96 transformed controls have exact frontier", not failures, str(failures[:1]))

    note = NOTE.read_text(encoding="utf-8").lower() if NOTE.is_file() else ""
    for marker in ("*", "`", ">"):
        note = note.replace(marker, "")
    note = " ".join(note.split())
    check("E02 note exists and carries authority none", NOTE.is_file() and "authority: none" in note)
    check("E03 note names AUX-gated candidate transport residual", "aux_gated_candidate_transport" in note)
    check("E04 note says ALL/AUX cage is supplied", "all/aux final cage is supplied" in note)
    check("E05 note includes the N1-N8 discipline gate", all(f"n{i}" in note for i in range(1, 9)))
    check("E06 note denies foundation and axiom effects", "no foundation edit" in note and "no axiom addition follows" in note)


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    table_and_union_contract()
    exact_program_pipeline_contract()
    off_bank_one_bit_contract()
    all_selected_pair_contract()
    covariance_and_scope_contract()
    print("\nSTATUS_CANONICAL=6 STATUS_RAW=144 FINAL_CANONICAL=4 FINAL_RAW=96")
    print("PHYSICAL_UNION_RAW=5680 PROGRAMS=236 UNLIKE_PAIRS=55460 PERTURBATIONS=11328")
    print(f"SUMMARY: {PASS} PASS / {FAIL} FAIL")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
