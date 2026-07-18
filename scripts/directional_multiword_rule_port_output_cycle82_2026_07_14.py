#!/usr/bin/env python3
"""Cycle 82: directional multiword rule port and eight-bit output writer.

Six seed-frame neighbour slots are serialized into one 48-bit candidate
stream.  A matching 48-bit law-program stream uses Cycle 81's physical H0/H1
equality row at every bit; the forty-eighth certificate is the physical rule
port.  It starts an alternating DATA/CERT writer which copies an associated
eight-bit H0/H1 output program and writes VALID last.

The full end-to-end geometry is executed for all three six-neighbour rows in
the selected Cycle-60/67/72/80 table.  The output writer is independently
exhausted on all 256 output words.  Harnesses, ordered streams, and programs
remain supplied; no seed-grown or 198-way bank claim is made.

Authority: none.  No foundation, registry, queue, or audit state is edited.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from pathlib import Path

import eight_bit_physical_role_comparator_cycle81_2026_07_14 as c81
import four_open_reservation_comb_cycle59_2026_07_14 as c59
import official_seed_to_rail_nucleation_cycle53_2026_07_14 as c53


ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / "docs" / "work_history" / "repo" / "review_feedback"
NOTE = REVIEW / "DIRECTIONAL_MULTIWORD_RULE_PORT_OUTPUT_CYCLE82_NOTE_2026-07-14.md"

Coord = tuple[int, int, int]
Word = c81.Word
BitStream = tuple[int, ...]
Signature = c53.Signature
H0 = "H0"
H1 = "H1"
PASS = 0
FAIL = 0

DIRECTION_ORDER: tuple[Coord, ...] = tuple(sorted(c53.DIRECTIONS))
EMPTY_WORD: Word = c81.RESERVED_WORDS[0]

# Output-writer presentation.  DATA and CERT alternate along x.  The incoming
# physical rule port occupies (-1,1,0); no symbolic role is read there.
PORT: Coord = (-1, 1, 0)
DATA: tuple[Coord, ...] = tuple((2 * index, 1, 0) for index in range(8))
CERT: tuple[Coord, ...] = tuple((2 * index + 1, 1, 0) for index in range(8))
PROGRAM: tuple[Coord, ...] = tuple((2 * index, 2, 0) for index in range(8))
VALID: Coord = (16, 1, 0)

# DATA sees previous H1, the program bit, and these three fixed markers.
DATA_MARKERS = (H0, H0, H0)  # -y, +z, -z
# CERT sees previous DATA H0/H1 and four fixed markers.
CERT_MARKERS = (H1, H1, H1, H1)  # +y, -y, +z, -z
# VALID sees final CERT plus these five fixed neighbours.
VALID_MARKERS = (H0, H0, H0, H0, H0)  # +x, -y, +y, -z, +z


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


def bit_content(bit: int) -> str:
    return H1 if bit else H0


def translate(site: Coord, shift_x: int) -> Coord:
    return (site[0] + shift_x, site[1], site[2])


def output_harness(word: Word, *, port: bool = True, shift_x: int = 0) -> dict[Coord, str]:
    records: dict[Coord, str] = {}
    if port:
        records[translate(PORT, shift_x)] = H1
    for index, bit in enumerate(word):
        x = shift_x + 2 * index
        records[(x, 2, 0)] = bit_content(bit)
        records[(x, 0, 0)] = DATA_MARKERS[0]
        records[(x, 1, 1)] = DATA_MARKERS[1]
        records[(x, 1, -1)] = DATA_MARKERS[2]
        x += 1
        records[(x, 2, 0)] = CERT_MARKERS[0]
        records[(x, 0, 0)] = CERT_MARKERS[1]
        records[(x, 1, 1)] = CERT_MARKERS[2]
        records[(x, 1, -1)] = CERT_MARKERS[3]
    records[(shift_x + 17, 1, 0)] = VALID_MARKERS[0]
    records[(shift_x + 16, 0, 0)] = VALID_MARKERS[1]
    records[(shift_x + 16, 2, 0)] = VALID_MARKERS[2]
    records[(shift_x + 16, 1, -1)] = VALID_MARKERS[3]
    records[(shift_x + 16, 1, 1)] = VALID_MARKERS[4]
    return records


def output_additions(word: Word, shift_x: int = 0) -> tuple[tuple[Coord, str], ...]:
    additions: list[tuple[Coord, str]] = []
    for index, bit in enumerate(word):
        additions.append(((shift_x + 2 * index, 1, 0), bit_content(bit)))
        additions.append(((shift_x + 2 * index + 1, 1, 0), H1))
    additions.append(((shift_x + 16, 1, 0), H1))
    return tuple(additions)


def signature(records: dict[Coord, str], target: Coord) -> Signature:
    return c53.local_signature(records, target)


def build_output_table() -> dict[Signature, str]:
    table: dict[Signature, str] = {}
    for word in ((0,) * 8, (1,) * 8):
        records = output_harness(word)  # type: ignore[arg-type]
        table[c53.canonical_signature(signature(records, DATA[0]))] = bit_content(word[0])
        records[DATA[0]] = bit_content(word[0])
        table[c53.canonical_signature(signature(records, CERT[0]))] = H1
    records = output_harness((0,) * 8)  # type: ignore[arg-type]
    records.update(dict(output_additions((0,) * 8)[:-1]))  # type: ignore[arg-type]
    table[c53.canonical_signature(signature(records, VALID))] = H1
    return table


OUTPUT_TABLE = build_output_table()
OUTPUT_RAW = c59.raw_rule_outputs(OUTPUT_TABLE)


def merge_raw() -> dict[Signature, frozenset[str]]:
    outputs: dict[Signature, set[str]] = defaultdict(set)
    for table in (c81.COMBINED_RAW_OUTPUTS, OUTPUT_RAW):
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
        site: next(iter(values)) if len(values) == 1 else "CONFLICT"
        for site, values in enabled_outputs(records).items()
    }


def canonical_records(records: dict[Coord, str]) -> tuple[tuple[Coord, str], ...]:
    minima = tuple(min(site[axis] for site in records) for axis in range(3))
    return tuple(sorted((tuple(site[axis] - minima[axis] for axis in range(3)), content) for site, content in records.items()))


def decode_output(records: dict[Coord, str], shift_x: int = 0) -> Word | None:
    if translate(VALID, shift_x) not in records:
        return None
    contents = tuple(records.get(translate(site, shift_x)) for site in DATA)
    if any(content not in (H0, H1) for content in contents):
        return None
    return tuple(1 if content == H1 else 0 for content in contents)  # type: ignore[return-value]


def flatten(words: list[Word] | tuple[Word, ...]) -> BitStream:
    return tuple(bit for word in words for bit in word)


def row_program(local: Signature) -> BitStream:
    contents = dict(local)
    return flatten(tuple(c81.ROLE_TO_WORD[contents[direction]] if direction in contents else EMPTY_WORD for direction in DIRECTION_ORDER))


ROW_PROGRAMS = {local: row_program(local) for local in c81.SELECTED_TABLE}
SIX_ROWS = tuple((local, output) for local, output in c81.SELECTED_TABLE.items() if len(local) == 6)


def stream_harness(candidate: BitStream, reference: BitStream) -> dict[Coord, str]:
    assert len(candidate) == len(reference) == 48
    records: dict[Coord, str] = {(-1, 1, 0): H1}
    for index, (left, right) in enumerate(zip(candidate, reference)):
        records[(index, 0, 0)] = bit_content(left)
        records[(index, 2, 0)] = bit_content(right)
        records[(index, 1, 1)] = H0
        records[(index, 1, -1)] = H1
    return records


def common_prefix(left: BitStream, right: BitStream) -> int:
    return next((index for index, pair in enumerate(zip(left, right)) if pair[0] != pair[1]), len(left))


def pipeline_records(
    candidate: BitStream,
    reference: BitStream,
    output_word: Word,
    certificate_count: int,
    output_step: int = 0,
) -> dict[Coord, str]:
    records = stream_harness(candidate, reference)
    # No supplied output port: comparator certificate 47 becomes that port.
    records.update(output_harness(output_word, port=False, shift_x=48))
    records.update({(index, 1, 0): H1 for index in range(certificate_count)})
    records.update(dict(output_additions(output_word, 48)[:output_step]))
    return records


def program_bank_contract() -> None:
    section("A - Six-slot directional program bank")
    check("A01 direction order is exactly all six nearest neighbours", len(DIRECTION_ORDER) == len(set(DIRECTION_ORDER)) == 6 and set(DIRECTION_ORDER) == set(c53.DIRECTIONS))
    check("A02 EMPTY is a genuinely reserved eight-bit word", EMPTY_WORD in c81.RESERVED_WORDS and EMPTY_WORD not in c81.WORD_TO_ROLE)
    check("A03 all 198 row programs are exactly 48 bits", len(ROW_PROGRAMS) == 198 and all(len(program) == 48 for program in ROW_PROGRAMS.values()))
    check("A04 all 198 directional programs are distinct", len(set(ROW_PROGRAMS.values())) == 198)
    distances = [sum(left != right for left, right in zip(a, b)) for index, a in enumerate(ROW_PROGRAMS.values()) for b in tuple(ROW_PROGRAMS.values())[:index]]
    check("A05 exact minimum program Hamming distance is one", min(distances) == 1)
    check("A06 row arity census is preserved", Counter(map(len, ROW_PROGRAMS)) == {1: 13, 2: 70, 3: 62, 4: 32, 5: 18, 6: 3})
    check("A07 exactly three programs need no EMPTY slot", len(SIX_ROWS) == 3 and all(EMPTY_WORD not in tuple(program[index:index + 8] for index in range(0, 48, 8)) for local, program in ROW_PROGRAMS.items() if len(local) == 6))
    check("A08 every programmed output has an assigned eight-bit word", all(output in c81.ROLE_TO_WORD for output in c81.SELECTED_TABLE.values()))


def output_writer_contract() -> None:
    section("B - Physical rule-port to arbitrary eight-bit output")
    check("B01 output table has five canonical rows", len(OUTPUT_TABLE) == 5 and sorted(map(len, OUTPUT_TABLE)) == [5, 5, 5, 5, 6])
    check("B02 output table has 48 proper-cubic raw rows", len(OUTPUT_RAW) == 48)
    check("B03 exactly 24 raw rows safely alias prior H1 rows", len(set(OUTPUT_RAW) & set(c81.COMBINED_RAW_OUTPUTS)) == 24 and all(OUTPUT_RAW[local] == c81.COMBINED_RAW_OUTPUTS[local] == frozenset((H1,)) for local in set(OUTPUT_RAW) & set(c81.COMBINED_RAW_OUTPUTS)))
    check("B04 provisional physical union has 4,588 rows", len(COMBINED_RAW) == 4_588)
    check("B05 provisional physical union is single-valued", all(len(values) == 1 for values in COMBINED_RAW.values()))
    check("B06 writer rule input/output contents are only H0/H1", {content for local in OUTPUT_TABLE for _offset, content in local} | set(OUTPUT_TABLE.values()) == {H0, H1})
    check("B07 writer source is 69 supplied records plus incoming port", all(len(output_harness(word)) == 70 and len(output_harness(word, port=False)) == 69 for word in (c81.ALL_WORDS[0], c81.ALL_WORDS[-1])))
    fixed = output_harness(c81.ALL_WORDS[0])
    for site in PROGRAM:
        del fixed[site]
    canonical = canonical_records(fixed)
    stabilizer = sum(canonical_records({c53.matvec(rotation, site): content for site, content in fixed.items()}) == canonical for rotation in c53.ROTATIONS)
    check("B08 fixed 62-record writer cage has trivial stabilizer", len(fixed) == 62 and stabilizer == 1)

    failures = []
    states = edges = terminals = 0
    for word in c81.ALL_WORDS:
        source = output_harness(word)
        additions = output_additions(word)
        for step in range(len(additions) + 1):
            records = dict(source)
            records.update(dict(additions[:step]))
            expected = {additions[step][0]: additions[step][1]} if step < len(additions) else {}
            actual = assignments(records)
            states += 1
            edges += len(actual)
            terminals += int(not expected)
            if actual != expected:
                failures.append((word, step, expected, actual))
            if (decode_output(records) is not None) != (step == len(additions)):
                failures.append((word, step, "decode timing", decode_output(records)))
            if step == len(additions) and decode_output(records) != word:
                failures.append((word, step, "wrong output", decode_output(records)))
    check("B09 all 4,608 writer states have exact serial frontier", states == 4_608 and not failures, str(failures[:1]))
    check("B10 all word writers have 4,352 edges and 256 terminals", (edges, terminals) == (4_352, 256), str((edges, terminals)))


def multiword_match_contract() -> None:
    section("C - Directional multiword match to physical rule port")
    check("C01 48-bit stream uses six ordered eight-bit slots", all(row_program(local)[8 * index:8 * (index + 1)] == (c81.ROLE_TO_WORD[dict(local)[direction]] if direction in dict(local) else EMPTY_WORD) for local in c81.SELECTED_TABLE for index, direction in enumerate(DIRECTION_ORDER)))
    check("C02 stream comparator source has 193 supplied H0/H1 records", all(len(stream_harness(program, program)) == 193 and set(stream_harness(program, program).values()) == {H0, H1} for program in tuple(ROW_PROGRAMS.values())[:3]))
    # The local equality row is exactly Cycle 81's five-neighbour pair; chain
    # length changes no physical rule.
    sample = next(iter(ROW_PROGRAMS.values()))
    start_signature = c53.canonical_signature(signature(stream_harness(sample, sample), (0, 1, 0)))
    check("C03 stream uses an existing Cycle-81 equality row", start_signature in c81.CANONICAL_TABLE and len(start_signature) == 5)

    substitution_failures = []
    substitution_count = 0
    for local, output in SIX_ROWS:
        expected_stream = ROW_PROGRAMS[local]
        contents = dict(local)
        output_word = c81.ROLE_TO_WORD[output]
        for slot, direction in enumerate(DIRECTION_ORDER):
            original = contents[direction]
            for replacement, replacement_word in c81.ROLE_TO_WORD.items():
                if replacement == original:
                    continue
                words = [c81.ROLE_TO_WORD[contents[item]] for item in DIRECTION_ORDER]
                words[slot] = replacement_word
                candidate = flatten(tuple(words))
                prefix = common_prefix(candidate, expected_stream)
                records = pipeline_records(candidate, expected_stream, output_word, prefix)
                actual = assignments(records)
                substitution_count += 1
                if actual:
                    substitution_failures.append((output, slot, original, replacement, prefix, actual))
    check("C04 every one-role substitution in every full row stops quietly", substitution_count == 2_394 and not substitution_failures, str(substitution_failures[:1]))
    check("C05 no substituted full row reaches the output writer", not substitution_failures)


def end_to_end_contract() -> None:
    section("D - Three hardest rows: six words to exact output word")
    failures = []
    states = edges = terminals = 0
    outputs_seen = set()
    for local, output in SIX_ROWS:
        reference = ROW_PROGRAMS[local]
        output_word = c81.ROLE_TO_WORD[output]
        additions = output_additions(output_word, 48)
        for certificate_count in range(49):
            records = pipeline_records(reference, reference, output_word, certificate_count)
            expected = {(certificate_count, 1, 0): H1} if certificate_count < 48 else {additions[0][0]: additions[0][1]}
            actual = assignments(records)
            states += 1
            edges += len(actual)
            if actual != expected:
                failures.append((output, "compare", certificate_count, expected, actual))
        for output_step in range(1, len(additions) + 1):
            records = pipeline_records(reference, reference, output_word, 48, output_step)
            expected = {additions[output_step][0]: additions[output_step][1]} if output_step < len(additions) else {}
            actual = assignments(records)
            states += 1
            edges += len(actual)
            terminals += int(not expected)
            if actual != expected:
                failures.append((output, "write", output_step, expected, actual))
            if output_step == len(additions):
                decoded = decode_output(records, 48)
                outputs_seen.add(decoded)
                if decoded != output_word:
                    failures.append((output, "decode", output_word, decoded))
    check("D01 each full row has exactly 66 states and 65 edges", (states, edges, terminals) == (198, 195, 3), str((states, edges, terminals)))
    check("D02 all three end-to-end physical frontiers are exact", not failures, str(failures[:1]))
    check("D03 terminal words are exactly the three selected outputs", outputs_seen == {c81.ROLE_TO_WORD[output] for _local, output in SIX_ROWS})
    check("D04 each pipeline has 262 supplied source records", all(len(pipeline_records(ROW_PROGRAMS[local], ROW_PROGRAMS[local], c81.ROLE_TO_WORD[output], 0)) == 262 for local, output in SIX_ROWS))
    check("D05 each pipeline appends 48 rule-port certificates plus 17 output records", 48 + len(output_additions(c81.ALL_WORDS[0], 48)) == 65)


def covariance_and_residual_contract() -> None:
    section("E - Covariance, achieved boundary, and exact residuals")
    local, output = SIX_ROWS[0]
    program = ROW_PROGRAMS[local]
    output_word = c81.ROLE_TO_WORD[output]
    additions = output_additions(output_word, 48)
    samples = (
        (pipeline_records(program, program, output_word, 0), {(0, 1, 0): H1}),
        (pipeline_records(program, program, output_word, 48), {additions[0][0]: additions[0][1]}),
        (pipeline_records(program, program, output_word, 48, 16), {additions[16][0]: additions[16][1]}),
        (pipeline_records(program, program, output_word, 48, 17), {}),
    )
    failures = []
    shift = (83, -41, 29)
    for rotation_index, rotation in enumerate(c53.ROTATIONS):
        for records, expected in samples:
            transformed = {c53.add(c53.matvec(rotation, site), shift): content for site, content in records.items()}
            transformed_expected = {c53.add(c53.matvec(rotation, site), shift): content for site, content in expected.items()}
            if set(assignments(transformed)) != set(transformed_expected):
                failures.append((rotation_index, transformed_expected, assignments(transformed)))
    check("E01 all 96 transformed pipeline controls have exact frontier", not failures, str(failures[:1]))

    note = NOTE.read_text(encoding="utf-8").lower() if NOTE.is_file() else ""
    for marker in ("*", "`", ">"):
        note = note.replace(marker, "")
    note = " ".join(note.split())
    check("E02 note exists and carries authority none", NOTE.is_file() and "authority: none" in note)
    check("E03 note says every harness and program is supplied", "all cycle-82 harnesses and program rails are supplied" in note)
    check("E04 note names open-direction residual", "open_direction_to_empty_word" in note)
    check("E05 note names stream-routing residual", "neighbour_macroblocks_to_ordered_stream" in note)
    check("E06 note names program-bank residual", "candidate_fanout_to_198_programs" in note)
    check("E07 note names seed-growth residual", "seed_to_rule_port_output_harness" in note)
    check("E08 note scopes the output result to an incoming physical port", "conditional on an incoming physical h1 rule port" in note)
    check("E09 note denies foundation and axiom effects", "no foundation edit" in note and "no axiom addition follows" in note)


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    program_bank_contract()
    output_writer_contract()
    multiword_match_contract()
    end_to_end_contract()
    covariance_and_residual_contract()
    print("\nPROGRAMS=198 SLOT_BITS=48 EMPTY_WORDS=1 SIX_ROWS=3")
    print("OUTPUT_CANONICAL=5 OUTPUT_RAW=48 PHYSICAL_UNION_RAW=4588")
    print("PIPELINE_SOURCE=262 PIPELINE_ADDITIONS=65")
    print(f"SUMMARY: {PASS} PASS / {FAIL} FAIL")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
