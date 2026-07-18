#!/usr/bin/env python3
"""Cycle 94: one live arity-one recurrent row through a readable macrostep.

The actual Cycle-85 completed A layer exposes the Cycle-80 row

    R_LA + five open directions -> R_B11.

This probe replaces that one symbolic output by a physical H1 row port, runs
the exact 48-bit live directional comparison, writes the eight-bit R_B11 word
with an unsealed writer, reads every DATA bit back after VALID, and lets the
verified word start the physical comparator for the next actual B row.

The constant candidate/reference/program/cage records remain supplied.  Thus
this closes a value-faithful output-to-next-front interface for one completed
compiler cell, not seed growth of the compiler cell or the general W_STEP.

Authority: none.  No foundation, registry, queue, audit, or git state follows.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from pathlib import Path

import cycle80_recurrence_audit_endpoint_tube_nucleation_cycle85_2026_07_14 as c85
import four_open_reservation_comb_cycle59_2026_07_14 as c59
import live_directional_program_writer_cycle90_2026_07_15 as c90
import live_eight_bit_physical_comparator_cycle89_2026_07_15 as c89
import official_seed_to_rail_nucleation_cycle53_2026_07_14 as c53
import operational_binary_macrocode_compiler_cycle58_2026_07_14 as c58
import three_phase_recurrent_append_tube_cycle80_2026_07_14 as c80


ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / "docs" / "work_history" / "repo" / "review_feedback"
NOTE = REVIEW / "LIVE_SEED_ROW_READABLE_MACROSTEP_CYCLE94_NOTE_2026-07-15.md"

Coord = tuple[int, int, int]
Signature = c53.Signature
Word = c89.Word
H0 = "H0"
H1 = "H1"
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


def add(left: Coord, right: Coord) -> Coord:
    return tuple(a + b for a, b in zip(left, right))  # type: ignore[return-value]


def sub(left: Coord, right: Coord) -> Coord:
    return tuple(a - b for a, b in zip(left, right))  # type: ignore[return-value]


def bit_content(bit: int) -> str:
    return H1 if bit else H0


def canonical(items: dict[Coord, str]) -> Signature:
    return c53.canonical_signature(tuple(items.items()))


def translate(site: Coord, shift: Coord) -> Coord:
    return add(site, shift)


def translated(records: dict[Coord, str], shift: Coord) -> dict[Coord, str]:
    return {translate(site, shift): content for site, content in records.items()}


def transform_site(site: Coord, rotation: c53.Matrix, shift: Coord) -> Coord:
    return add(c53.matvec(rotation, site), shift)


def transform_records(
    records: dict[Coord, str], rotation: c53.Matrix, shift: Coord
) -> dict[Coord, str]:
    return {
        transform_site(site, rotation, shift): content
        for site, content in records.items()
    }


def merge_raw(
    *tables: dict[Signature, frozenset[str]],
) -> dict[Signature, frozenset[str]]:
    outputs: dict[Signature, set[str]] = defaultdict(set)
    for table in tables:
        for local, values in table.items():
            outputs[local].update(values)
    return {local: frozenset(values) for local, values in outputs.items()}


# ---------------------------------------------------------------------------
# Actual recurrent rows and corrected 153-role codebook.
# ---------------------------------------------------------------------------

SEED_SIGNATURE, SEED_OUTPUT = next(
    (local, output)
    for local, output in c80.CONSTRUCTION.table.items()
    if output == "R_B11"
)
NEXT_SIGNATURE, NEXT_OUTPUT = next(
    (local, output)
    for local, output in c80.CONSTRUCTION.table.items()
    if output == "R_B10"
)
SEED_PROGRAM = c90.ROW_PROGRAMS[SEED_SIGNATURE]
NEXT_PROGRAM = c90.ROW_PROGRAMS[NEXT_SIGNATURE]
OUTPUT_WORD = c89.ROLE_TO_WORD[SEED_OUTPUT]
EMPTY_WORD = c89.EMPTY_WORD

STANDARD_TARGET = (1, *c80.SEED["B"])
PHYSICAL_TARGET = c85.transform(STANDARD_TARGET)
ENDPOINT = {**c85.BRIDGE.source, **c85.BRIDGE.allowed}

# A one-row block lift.  The exact physical input domain is unchanged, but its
# permanent output is now the comparator START rather than an unencoded R_B11.
LIFTED_LIVE_TABLE = dict(c85.BRIDGE.union_with_recurrence)
assert LIFTED_LIVE_TABLE.pop(SEED_SIGNATURE) == SEED_OUTPUT
LIFTED_LIVE_TABLE[SEED_SIGNATURE] = H1
LIFTED_LIVE_RAW = c59.raw_rule_outputs(LIFTED_LIVE_TABLE)


# ---------------------------------------------------------------------------
# Readable writer and value-faithful reverse verification sweep.
# ---------------------------------------------------------------------------

PORT: Coord = (-1, 0, 0)
DATA: tuple[Coord, ...] = tuple((2 * index, 0, 0) for index in range(8))
CERT: tuple[Coord, ...] = tuple((2 * index + 1, 0, 0) for index in range(8))
PROGRAM: tuple[Coord, ...] = tuple((2 * index, -1, 0) for index in range(8))
REFERENCE: tuple[Coord, ...] = tuple((2 * index, 2, 0) for index in range(8))
TAP: tuple[Coord, ...] = tuple((2 * index, 1, 0) for index in range(8))
BRIDGE: tuple[Coord, ...] = tuple((2 * index + 1, 1, 0) for index in range(8))
VALID: Coord = (16, 0, 0)
TURN: Coord = (16, 1, 0)
MATCH: Coord = (0, 1, -1)
FINAL_TAP_BACK: Coord = (-1, 1, 0)

# All guards are already among Cycle 85's 153 roles.  Distinct guard families
# prevent the writer/turn/bridge/tap rows from aliasing one another in the live
# mixed table while leaving one permanent read port beside each DATA bit.
DATA_GUARD = "GU"
CERT_GUARD = "GY"
VALID_GUARD = "T_H0"
TURN_GUARD = "T_H1"
BRIDGE_GUARD = "T_H2"
BRIDGE_TOKEN = "T_N2"
TAP_GUARD = "T_G0"
FINAL_TAP_GUARD = "T_G1"
MATCH_BACK_GUARD = "T_H3"
MATCH_SIDE_GUARD = "T_N0"


def readable_source(
    program: Word,
    reference: Word,
    *,
    port: bool = True,
) -> dict[Coord, str]:
    records: dict[Coord, str] = {PORT: H1} if port else {}
    for index, (program_bit, reference_bit) in enumerate(zip(program, reference)):
        x = 2 * index
        records[(x, -1, 0)] = bit_content(program_bit)
        records[(x, 0, -1)] = DATA_GUARD
        records[(x, 0, 1)] = DATA_GUARD
        records[(x, 2, 0)] = bit_content(reference_bit)
        records[(x, 1, 1)] = FINAL_TAP_GUARD if index == 0 else TAP_GUARD

        x += 1
        records[(x, -1, 0)] = CERT_GUARD
        records[(x, 0, -1)] = CERT_GUARD
        records[(x, 0, 1)] = CERT_GUARD
        records[(x, 1, -1)] = BRIDGE_GUARD
        records[(x, 1, 1)] = BRIDGE_GUARD

    records[(16, -1, 0)] = VALID_GUARD
    records[(16, 0, -1)] = VALID_GUARD
    records[(16, 0, 1)] = VALID_GUARD
    records[(16, 2, 0)] = TURN_GUARD
    records[(16, 1, -1)] = TURN_GUARD
    records[(16, 1, 1)] = TURN_GUARD

    # MATCH lies one step below the final tap.  Its +x and -y guards are
    # already the bridge/data guards; only the other two side guards are new.
    # The -z neighbour remains open for the next comparator cell.
    records[(-1, 1, -1)] = MATCH_BACK_GUARD
    records[(0, 2, -1)] = MATCH_SIDE_GUARD
    # In the composed geometry this aliases the final bit of the primary
    # 48-bit reference rail.  Naming it here makes the readable module's
    # standalone and composed final-tap signatures literally identical.
    records[FINAL_TAP_BACK] = H1
    return records


def build_readable_table() -> dict[Signature, str]:
    table: dict[Signature, str] = {}

    # DATA copies its physical program bit while +y remains open as its read tap.
    for bit in (H0, H1):
        table[canonical({
            (-1, 0, 0): H1,
            (0, -1, 0): bit,
            (0, 0, -1): DATA_GUARD,
            (0, 0, 1): DATA_GUARD,
        })] = bit

    # CERT advances the writer while +y remains open for the reverse bridge.
    for bit in (H0, H1):
        table[canonical({
            (-1, 0, 0): bit,
            (0, -1, 0): CERT_GUARD,
            (0, 0, -1): CERT_GUARD,
            (0, 0, 1): CERT_GUARD,
        })] = H1

    table[canonical({
        (-1, 0, 0): H1,
        (0, -1, 0): VALID_GUARD,
        (0, 0, -1): VALID_GUARD,
        (0, 0, 1): VALID_GUARD,
    })] = H1
    table[canonical({
        (0, -1, 0): H1,
        (0, 1, 0): TURN_GUARD,
        (0, 0, -1): TURN_GUARD,
        (0, 0, 1): TURN_GUARD,
    })] = H1
    table[canonical({
        (1, 0, 0): H1,
        (0, -1, 0): H1,
        (0, 0, -1): BRIDGE_GUARD,
        (0, 0, 1): BRIDGE_GUARD,
    })] = BRIDGE_TOKEN

    # Equal DATA/reference bits advance; either mismatch leaves the tap open.
    for bit in (H0, H1):
        table[canonical({
            (1, 0, 0): BRIDGE_TOKEN,
            (0, -1, 0): bit,
            (0, 1, 0): bit,
            (0, 0, 1): TAP_GUARD,
        })] = H1
        table[canonical({
            (-1, 0, 0): H1,
            (1, 0, 0): BRIDGE_TOKEN,
            (0, -1, 0): bit,
            (0, 1, 0): bit,
            (0, 0, 1): FINAL_TAP_GUARD,
        })] = H1

    # Five neighbours form MATCH; -z is deliberately left open.
    table[canonical({
        (0, 0, 1): H1,
        (-1, 0, 0): MATCH_BACK_GUARD,
        (1, 0, 0): BRIDGE_GUARD,
        (0, -1, 0): DATA_GUARD,
        (0, 1, 0): MATCH_SIDE_GUARD,
    })] = H1
    return table


READABLE_TABLE = build_readable_table()
READABLE_RAW = c59.raw_rule_outputs(READABLE_TABLE)
COMBINED_RAW = merge_raw(
    LIFTED_LIVE_RAW,
    c58.RAW_OUTPUTS,
    c89.RAW_OUTPUTS,
    READABLE_RAW,
)


def readable_additions(word: Word) -> tuple[tuple[Coord, str], ...]:
    additions: list[tuple[Coord, str]] = []
    for site, bit, cert in zip(DATA, word, CERT):
        additions.append((site, bit_content(bit)))
        additions.append((cert, H1))
    additions.extend(((VALID, H1), (TURN, H1)))
    for index in range(7, -1, -1):
        additions.extend(((BRIDGE[index], BRIDGE_TOKEN), (TAP[index], H1)))
    additions.append((MATCH, H1))
    return tuple(additions)


READ_SHIFT: Coord = (48, 1, 0)
PRIMARY_START: Coord = c89.START
PRIMARY_CERT = tuple((index, 1, 0) for index in range(48))
READ_MATCH = translate(MATCH, READ_SHIFT)


def primary_local_source(
    program: Word = OUTPUT_WORD,
    reference: Word = OUTPUT_WORD,
) -> dict[Coord, str]:
    records = c90.stream_harness(SEED_PROGRAM, SEED_PROGRAM)
    records.pop(PRIMARY_START)
    records.update(translated(readable_source(program, reference, port=False), READ_SHIFT))
    return records


PRIMARY_LOCAL_ADDITIONS = (
    ((PRIMARY_START, H1),)
    + tuple((site, H1) for site in PRIMARY_CERT)
    + tuple(
        (translate(site, READ_SHIFT), content)
        for site, content in readable_additions(OUTPUT_WORD)
    )
)


# ---------------------------------------------------------------------------
# The verified MATCH is the START of the actual next recurrent-row comparator.
# Its 48-bit source is supplied, but the START record is not.
# ---------------------------------------------------------------------------

NEXT_AXIS: Coord = (0, 0, -1)


def next_placement() -> tuple[c53.Matrix, Coord, dict[Coord, str], tuple[Coord, ...]]:
    primary_source = primary_local_source()
    primary_dynamic = {site for site, _content in PRIMARY_LOCAL_ADDITIONS}
    occupied = set(primary_source) | primary_dynamic
    candidate = c90.stream_harness(NEXT_PROGRAM, NEXT_PROGRAM)
    candidate.pop(c89.START)
    certificates = tuple((index, 1, 0) for index in range(48))

    for rotation in c53.ROTATIONS:
        if c53.matvec(rotation, (1, 0, 0)) != NEXT_AXIS:
            continue
        shift = sub(READ_MATCH, c53.matvec(rotation, c89.START))
        source = transform_records(candidate, rotation, shift)
        additions = tuple(transform_site(site, rotation, shift) for site in certificates)
        if set(source).isdisjoint(occupied) and set(additions).isdisjoint(occupied | set(source)):
            return rotation, shift, source, additions
    raise RuntimeError("no disjoint next-row comparator placement")


NEXT_ROTATION, NEXT_SHIFT, NEXT_LOCAL_SOURCE, NEXT_LOCAL_CERT = next_placement()
APPARATUS_LOCAL_SOURCE = {**primary_local_source(), **NEXT_LOCAL_SOURCE}
LOCAL_ADDITIONS = PRIMARY_LOCAL_ADDITIONS + tuple((site, H1) for site in NEXT_LOCAL_CERT)


# ---------------------------------------------------------------------------
# Place the full conditional compiler cell on the actual Cycle-85 target.
# ---------------------------------------------------------------------------

def enabled(records: dict[Coord, str]) -> dict[Coord, frozenset[str]]:
    return {
        target: COMBINED_RAW[local]
        for target in c53.open_candidates(records)
        if (local := c53.local_signature(records, target)) in COMBINED_RAW
    }


def physical_placement() -> tuple[c53.Matrix, Coord, dict[Coord, str], tuple[tuple[Coord, str], ...]]:
    for rotation in c53.ROTATIONS:
        shift = sub(PHYSICAL_TARGET, c53.matvec(rotation, PRIMARY_START))
        apparatus = transform_records(APPARATUS_LOCAL_SOURCE, rotation, shift)
        additions = tuple(
            (transform_site(site, rotation, shift), content)
            for site, content in LOCAL_ADDITIONS
        )
        if not set(apparatus).isdisjoint(ENDPOINT):
            continue
        if len({site for site, _content in additions}) != len(additions):
            continue
        if not {site for site, _content in additions}.isdisjoint(set(ENDPOINT) | set(apparatus)):
            continue
        source = {**ENDPOINT, **apparatus}
        if c53.local_signature(source, PHYSICAL_TARGET) != (
            (sub(c85.transform((0, *c80.LAUNCH["A"])), PHYSICAL_TARGET), "R_LA"),
        ):
            continue
        if enabled(source) != {PHYSICAL_TARGET: frozenset((H1,))}:
            continue
        return rotation, shift, source, additions
    raise RuntimeError("no live endpoint placement has the exact initial frontier")


PLACEMENT_ROTATION, PLACEMENT_SHIFT, SOURCE, ADDITIONS = physical_placement()
FINAL_MATCH = transform_site(READ_MATCH, PLACEMENT_ROTATION, PLACEMENT_SHIFT)
FINAL_NEXT_PORT = transform_site(NEXT_LOCAL_CERT[-1], PLACEMENT_ROTATION, PLACEMENT_SHIFT)


def records_at(step: int) -> dict[Coord, str]:
    records = dict(SOURCE)
    records.update(dict(ADDITIONS[:step]))
    return records


def expected_at(step: int) -> dict[Coord, frozenset[str]]:
    if step == len(ADDITIONS):
        return {}
    site, content = ADDITIONS[step]
    return {site: frozenset((content,))}


def canonical_records(records: dict[Coord, str]) -> tuple[tuple[Coord, str], ...]:
    minima = tuple(min(site[axis] for site in records) for axis in range(3))
    return tuple(sorted(
        (
            tuple(site[axis] - minima[axis] for axis in range(3)),
            content,
        )
        for site, content in records.items()
    ))


# ---------------------------------------------------------------------------
# Contracts.
# ---------------------------------------------------------------------------

def row_and_codebook_contract() -> None:
    section("A - Actual recurrent row, five open directions, and live codebook")
    check("A01 Cycle 94 note exists", NOTE.is_file())
    check("A02 selected row is the actual arity-one B seed row", len(SEED_SIGNATURE) == 1 and SEED_SIGNATURE == (((-1, 0, 0), "R_LA"),) and SEED_OUTPUT == "R_B11")
    check("A03 next row is the actual arity-two B continuation", len(NEXT_SIGNATURE) == 2 and dict(NEXT_SIGNATURE) == {(-1, 0, 0): "R_A10", (0, -1, 0): "R_B11"} and NEXT_OUTPUT == "R_B10")
    check("A04 actual Cycle-85 target is pinned", PHYSICAL_TARGET == (2, 5, 0) and PHYSICAL_TARGET not in ENDPOINT)
    local = c53.local_signature(ENDPOINT, PHYSICAL_TARGET)
    check("A05 target sees R_LA and exactly five open directions", len(local) == 1 and local[0][1] == "R_LA")
    check("A06 corrected live alphabet is exactly 153 roles", len(c89.FULL_ROLES) == 153)
    check("A07 all 153 roles retain distinct eight-bit words", len(c89.ROLE_TO_WORD) == len(set(c89.ROLE_TO_WORD.values())) == 153)
    check("A08 EMPTY is the reserved all-one word", EMPTY_WORD == (1,) * 8 and EMPTY_WORD not in c89.WORD_TO_ROLE)
    slots = tuple(SEED_PROGRAM[8 * index:8 * (index + 1)] for index in range(6))
    check("A09 candidate has R_LA then exactly five EMPTY slots", slots[0] == c89.ROLE_TO_WORD["R_LA"] and slots[1:] == (EMPTY_WORD,) * 5)
    check("A10 selected output word is R_B11=10010100", OUTPUT_WORD == (1, 0, 0, 1, 0, 1, 0, 0))


def table_contract() -> None:
    section("B - One-row lift and readable physical table")
    check("B01 lift changes exactly one canonical output", len(LIFTED_LIVE_TABLE) == 236 and sum(LIFTED_LIVE_TABLE[local] != c85.BRIDGE.union_with_recurrence[local] for local in LIFTED_LIVE_TABLE) == 1)
    check("B02 lifted row keeps the exact arity-one input and writes H1", LIFTED_LIVE_TABLE[SEED_SIGNATURE] == H1)
    check("B03 readable adapter has twelve canonical rows", len(READABLE_TABLE) == 12 and Counter(map(len, READABLE_TABLE)) == {4: 9, 5: 3})
    check("B04 readable adapter has 252 proper-cubic raw rows", len(READABLE_RAW) == 252)
    check("B05 readable rows are disjoint from lifted live/binary/comparator rows", set(READABLE_RAW).isdisjoint(merge_raw(LIFTED_LIVE_RAW, c58.RAW_OUTPUTS, c89.RAW_OUTPUTS)))
    check("B06 complete lifted union has 5,680 raw inputs", len(COMBINED_RAW) == 5_680)
    check("B07 every raw input has one output", all(len(values) == 1 for values in COMBINED_RAW.values()))
    used = {content for local in READABLE_TABLE for _direction, content in local} | set(READABLE_TABLE.values())
    check("B08 adapter uses only existing live contents", used <= c89.FULL_ROLES and {H0, H1} <= used)
    check("B09 no onsite role is added beyond the corrected 153", ({content for local in LIFTED_LIVE_TABLE for _direction, content in local} | set(LIFTED_LIVE_TABLE.values()) | used) <= c89.FULL_ROLES)
    sealed = c90.output_harness(OUTPUT_WORD)
    sealed.update(dict(c90.output_additions(OUTPUT_WORD)))
    check("B10 Cycle-90 DATA is locally sealed at terminal", all(all(add(site, direction) in sealed for direction in c53.DIRECTIONS) for site in c90.DATA))
    readable = readable_source(OUTPUT_WORD, OUTPUT_WORD)
    check("B11 Cycle-94 leaves one fresh tap beside every DATA bit", all(site not in readable for site in TAP))


def live_macrostep_contract() -> None:
    section("C - Actual endpoint through output word to next recurrent front")
    check("C01 a proper-cubic placement exists", PLACEMENT_ROTATION in c53.ROTATIONS)
    check("C02 apparatus source is disjoint from the generated endpoint", set(SOURCE) == set(ENDPOINT) | set(transform_records(APPARATUS_LOCAL_SOURCE, PLACEMENT_ROTATION, PLACEMENT_SHIFT)))
    check("C03 physical source initially enables only the lifted seed port", enabled(SOURCE) == {PHYSICAL_TARGET: frozenset((H1,))})
    failures = []
    for step in range(len(ADDITIONS) + 1):
        actual = enabled(records_at(step))
        expected = expected_at(step)
        if actual != expected:
            failures.append((step, expected, actual))
    check("C04 every reachable stage has its exact singleton frontier", not failures, str(failures[:1]))
    check("C05 macrostep has 133 states and 132 append edges", len(ADDITIONS) == 132)
    check("C06 terminal is quiet and conflict-free", not enabled(records_at(len(ADDITIONS))))

    terminal = records_at(len(ADDITIONS))
    output_sites = tuple(transform_site(translate(site, READ_SHIFT), PLACEMENT_ROTATION, PLACEMENT_SHIFT) for site in DATA)
    decoded = tuple(1 if terminal[site] == H1 else 0 for site in output_sites)
    check("C07 terminal DATA block is exactly R_B11", decoded == OUTPUT_WORD and c89.WORD_TO_ROLE[decoded] == "R_B11")
    check("C08 value-verified MATCH forms after all eight DATA taps", FINAL_MATCH in terminal and all(transform_site(translate(site, READ_SHIFT), PLACEMENT_ROTATION, PLACEMENT_SHIFT) in terminal for site in TAP))
    check("C09 MATCH starts the complete actual R_B10 comparator", FINAL_NEXT_PORT in terminal and all(transform_site(site, PLACEMENT_ROTATION, PLACEMENT_SHIFT) in terminal for site in NEXT_LOCAL_CERT))
    check("C10 actual next candidate contains R_B11 in its second slot", NEXT_PROGRAM[8:16] == OUTPUT_WORD)

    handoff_step = len(PRIMARY_LOCAL_ADDITIONS)
    next_first = transform_site(NEXT_LOCAL_CERT[0], PLACEMENT_ROTATION, PLACEMENT_SHIFT)
    check("C11 verified word immediately seeds the first next-row certificate", enabled(records_at(handoff_step)) == {next_first: frozenset((H1,))})


def controls_contract() -> None:
    section("D - Row selection, openness, value, and rotation controls")
    # Every other live row program stops before the seed reference's port.
    selector_failures = []
    for local, candidate in c90.ROW_PROGRAMS.items():
        prefix = c90.common_prefix(candidate, SEED_PROGRAM)
        records = c90.stream_harness(candidate, SEED_PROGRAM)
        records.update({(index, 1, 0): H1 for index in range(prefix)})
        if prefix < 48:
            target = (prefix, 1, 0)
            actual = COMBINED_RAW.get(c53.local_signature(records, target))
            if actual is not None:
                selector_failures.append((local, prefix, None, actual))
    check("D01 all 236 live programs have the exact seed-reference prefix stop", not selector_failures, str(selector_failures[:1]))
    check("D02 only the selected recurrent row reaches bit 48", sum(c90.common_prefix(program, SEED_PROGRAM) == 48 for program in c90.ROW_PROGRAMS.values()) == 1)

    # Any physical record in any of the five initially open directions removes
    # the exact one-neighbour START signature, independent of its content.
    endpoint_role_site = c85.transform((0, *c80.LAUNCH["A"]))
    occupied_direction = sub(endpoint_role_site, PHYSICAL_TARGET)
    open_directions = tuple(direction for direction in c53.DIRECTIONS if direction != occupied_direction)
    blocked = 0
    for direction in open_directions:
        site = add(PHYSICAL_TARGET, direction)
        for role in c89.FULL_ROLES:
            records = dict(SOURCE)
            records[site] = role
            local = c53.local_signature(records, PHYSICAL_TARGET)
            if COMBINED_RAW.get(local) != frozenset((H1,)):
                blocked += 1
    check("D03 all 5x153 extra-neighbour controls block seed-port formation", blocked == 5 * 153)

    # The unsealed writer must not expose MATCH for any wrong physical word.
    value_failures = []
    for word in c89.ALL_WORDS:
        records = readable_source(word, OUTPUT_WORD)
        for site, content in readable_additions(word):
            output = COMBINED_RAW.get(c53.local_signature(records, site))
            if output != frozenset((content,)):
                break
            records[site] = content
        if (MATCH in records) != (word == OUTPUT_WORD):
            value_failures.append((word, MATCH in records))
    check("D04 all 256 output-program words expose MATCH iff R_B11", not value_failures, str(value_failures[:1]))

    # Natural reachability is already exact in C04.  Exhaust every open local
    # signature at every one of those stages under all 24 proper rotations;
    # open-candidate sets transform bijectively, so this is the full rotated
    # frontier check without rebuilding 3,192 translated copies of 700+ sites.
    covariance_failures = []
    covariance_controls = 0
    for step in range(len(ADDITIONS) + 1):
        records = records_at(step)
        signatures = {
            c53.local_signature(records, target)
            for target in c53.open_candidates(records)
        }
        for signature in signatures:
            expected = COMBINED_RAW.get(signature)
            for rotation in c53.ROTATIONS:
                covariance_controls += 1
                rotated = c53.rotate_signature(signature, rotation)
                actual = COMBINED_RAW.get(rotated)
                if actual != expected:
                    covariance_failures.append((step, signature, rotation, expected, actual))
    check("D05 all 941,784 stage/signature/rotation controls retain the exact raw frontier", covariance_controls == 941_784 and not covariance_failures, str(covariance_failures[:1]))


def scope_contract() -> None:
    section("E - Supplied/grown boundary and no-go discipline surface")
    note = NOTE.read_text(encoding="utf-8").lower()
    check("E01 note states the exact supplied source census", "472 supplied compiler-cell records" in note)
    check("E02 note says all 132 dynamic records are grown", "132 dynamic appends" in note)
    check("E03 note names candidate routing and harness growth as still open", "neighbour_macroblocks_to_ordered_stream" in note and "seed_to_rule_port_output_harness" in note)
    check("E04 note does not claim the general W_STEP", "does not close general `w_step`" in note)
    check("E05 note contains the complete N1-N8 audit", all(f"n{index}" in note for index in range(1, 9)))
    check("E06 no foundation or queue artifact is a Cycle-94 output", all(path.parent == REVIEW or path.parent == ROOT / "scripts" for path in (NOTE, Path(__file__))))


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    row_and_codebook_contract()
    table_contract()
    live_macrostep_contract()
    controls_contract()
    scope_contract()
    supplied = len(APPARATUS_LOCAL_SOURCE)
    print(f"\nLIVE_CANONICAL=236 LIFTED_RAW={len(LIFTED_LIVE_RAW)} READABLE_CANONICAL={len(READABLE_TABLE)} READABLE_RAW={len(READABLE_RAW)}")
    print(f"UNION_RAW={len(COMBINED_RAW)} SUPPLIED_CELL={supplied} DYNAMIC_APPENDS={len(ADDITIONS)}")
    print(f"SEED_OUTPUT={SEED_OUTPUT} OUTPUT_WORD={''.join(map(str, OUTPUT_WORD))} NEXT_OUTPUT={NEXT_OUTPUT}")
    print(f"SUMMARY: {PASS} PASS / {FAIL} FAIL")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
