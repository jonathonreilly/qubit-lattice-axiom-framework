#!/usr/bin/env python3
"""Cycle 90: port six-slot programs and the output writer to Cycle 85.

The corrected 236-row law is encoded as six direction-ordered eight-bit
slots using Cycle 89's minimally extended codebook and reserved all-one EMPTY
word.  The existing local equality mechanism serially checks 48 bits, then
drives the physical eight-bit output writer.  Every output word is exhausted;
all four arity-six rows are run end to end and under every one-role
substitution.

Authority: none.  Streams, program rails, and writer cages are supplied.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from pathlib import Path

import four_open_reservation_comb_cycle59_2026_07_14 as c59
import live_eight_bit_physical_comparator_cycle89_2026_07_15 as c89
import official_seed_to_rail_nucleation_cycle53_2026_07_14 as c53


ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / "docs" / "work_history" / "repo" / "review_feedback"
NOTE = REVIEW / "LIVE_DIRECTIONAL_PROGRAM_WRITER_CYCLE90_NOTE_2026-07-15.md"

Coord = tuple[int, int, int]
Word = c89.Word
BitStream = tuple[int, ...]
Signature = c53.Signature
H0 = "H0"
H1 = "H1"
PASS = 0
FAIL = 0

DIRECTION_ORDER: tuple[Coord, ...] = tuple(sorted(c53.DIRECTIONS))
EMPTY_WORD: Word = c89.EMPTY_WORD

# Output writer: DATA and CERT alternate along x.  Incoming comparator port is
# immediately behind DATA[0].
PORT: Coord = (-1, 1, 0)
DATA: tuple[Coord, ...] = tuple((2 * index, 1, 0) for index in range(8))
CERT: tuple[Coord, ...] = tuple((2 * index + 1, 1, 0) for index in range(8))
PROGRAM: tuple[Coord, ...] = tuple((2 * index, 2, 0) for index in range(8))
VALID: Coord = (16, 1, 0)
DATA_MARKERS = (H0, H0, H0)
CERT_MARKERS = (H1, H1, H1, H1)
VALID_MARKERS = (H0, H0, H0, H0, H0)


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


def signature(records: dict[Coord, str], target: Coord) -> Signature:
    return c53.local_signature(records, target)


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
    for table in (c89.COMBINED_RAW_OUTPUTS, OUTPUT_RAW):
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
    return tuple(sorted(
        (tuple(site[axis] - minima[axis] for axis in range(3)), content)
        for site, content in records.items()
    ))


def decode_output(records: dict[Coord, str], shift_x: int = 0) -> Word | None:
    if translate(VALID, shift_x) not in records:
        return None
    contents = tuple(records.get(translate(site, shift_x)) for site in DATA)
    if any(content not in (H0, H1) for content in contents):
        return None
    return tuple(1 if content == H1 else 0 for content in contents)  # type: ignore[return-value]


def flatten(words: tuple[Word, ...] | list[Word]) -> BitStream:
    return tuple(bit for word in words for bit in word)


def row_program(local: Signature) -> BitStream:
    contents = dict(local)
    return flatten(tuple(
        c89.ROLE_TO_WORD[contents[direction]] if direction in contents else EMPTY_WORD
        for direction in DIRECTION_ORDER
    ))


ROW_PROGRAMS = {local: row_program(local) for local in c89.LIVE_TABLE}
SIX_ROWS = tuple((local, output) for local, output in c89.LIVE_TABLE.items() if len(local) == 6)


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


def pipeline_records(candidate: BitStream, reference: BitStream, output_word: Word, certificate_count: int, output_step: int = 0) -> dict[Coord, str]:
    records = stream_harness(candidate, reference)
    records.update(output_harness(output_word, port=False, shift_x=48))
    records.update({(index, 1, 0): H1 for index in range(certificate_count)})
    records.update(dict(output_additions(output_word, 48)[:output_step]))
    return records


def program_bank_contract() -> None:
    section("A - Corrected six-slot directional program bank")
    check("A01 direction order is exactly all six nearest neighbours", len(DIRECTION_ORDER) == len(set(DIRECTION_ORDER)) == 6 and set(DIRECTION_ORDER) == set(c53.DIRECTIONS))
    check("A02 EMPTY=11111111 is genuinely reserved", EMPTY_WORD == (1,) * 8 and EMPTY_WORD in c89.RESERVED_WORDS and EMPTY_WORD not in c89.WORD_TO_ROLE)
    check("A03 all 236 programs are exactly 48 bits and distinct", len(ROW_PROGRAMS) == len(set(ROW_PROGRAMS.values())) == 236 and all(len(program) == 48 for program in ROW_PROGRAMS.values()))
    distances = [sum(left != right for left, right in zip(a, b)) for index, a in enumerate(ROW_PROGRAMS.values()) for b in tuple(ROW_PROGRAMS.values())[:index]]
    check("A04 exact minimum program Hamming distance is one", min(distances) == 1)
    check("A05 live row arity census is preserved", Counter(map(len, ROW_PROGRAMS)) == {1: 13, 2: 96, 3: 67, 4: 36, 5: 20, 6: 4})
    empty_slots = sum(6 - len(local) for local in c89.LIVE_TABLE)
    check("A06 bank contains exactly 742 EMPTY slots", empty_slots == 742)
    check("A07 exactly 232 programs use at least one EMPTY slot", sum(EMPTY_WORD in tuple(program[index:index + 8] for index in range(0, 48, 8)) for program in ROW_PROGRAMS.values()) == 232)
    check("A08 exactly four rows have all six physical slots", len(SIX_ROWS) == 4 and {output for _local, output in SIX_ROWS} == {"I2", "DONE", "P2", "B1"})
    check("A09 every live output has an assigned physical word", all(output in c89.ROLE_TO_WORD for output in c89.LIVE_TABLE.values()))


def writer_contract() -> None:
    section("B - Corrected-union physical output writer")
    check("B01 output table has five canonical and 48 raw rows", len(OUTPUT_TABLE) == 5 and sorted(map(len, OUTPUT_TABLE)) == [5, 5, 5, 5, 6] and len(OUTPUT_RAW) == 48)
    overlap = set(OUTPUT_RAW) & set(c89.COMBINED_RAW_OUTPUTS)
    check("B02 exactly 24 raw rows are identical-H1 aliases", len(overlap) == 24 and all(OUTPUT_RAW[local] == c89.COMBINED_RAW_OUTPUTS[local] == frozenset((H1,)) for local in overlap))
    check("B03 corrected writer union has 5,452 raw rows", len(COMBINED_RAW) == 5_452)
    check("B04 corrected writer union is output-single-valued", all(len(values) == 1 for values in COMBINED_RAW.values()))
    check("B05 writer rows consume and write only H0/H1", {content for local in OUTPUT_TABLE for _offset, content in local} | set(OUTPUT_TABLE.values()) == {H0, H1})
    check("B06 writer source is 69 supplied records plus port", all(len(output_harness(word)) == 70 and len(output_harness(word, port=False)) == 69 for word in (c89.ALL_WORDS[0], c89.ALL_WORDS[-1])))
    fixed = output_harness(c89.ALL_WORDS[0])
    for site in PROGRAM:
        del fixed[site]
    canonical = canonical_records(fixed)
    stabilizer = sum(canonical_records({c53.matvec(rotation, site): content for site, content in fixed.items()}) == canonical for rotation in c53.ROTATIONS)
    check("B07 fixed 62-record writer cage has trivial stabilizer", len(fixed) == 62 and stabilizer == 1)

    failures = []
    states = edges = terminals = 0
    for word in c89.ALL_WORDS:
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
            decoded = decode_output(records)
            if (decoded is not None) != (step == len(additions)) or (decoded is not None and decoded != word):
                failures.append((word, step, "decode", decoded))
    check("B08 all 4,608 writer stages have exact frontier", states == 4_608 and not failures, str(failures[:1]))
    check("B09 writer graph has 4,352 edges and 256 terminals", (edges, terminals) == (4_352, 256), str((edges, terminals)))


def substitution_and_pipeline_contract() -> None:
    section("C - Four full rows through 48-bit compare and output write")
    sample = next(iter(ROW_PROGRAMS.values()))
    start_signature = c53.canonical_signature(signature(stream_harness(sample, sample), (0, 1, 0)))
    check("C01 stream source has 193 supplied records", len(stream_harness(sample, sample)) == 193)
    check("C02 stream reuses Cycle-89 equality row", start_signature in c89.CANONICAL_TABLE and len(start_signature) == 5)

    substitution_failures = []
    substitution_count = 0
    for local, output in SIX_ROWS:
        reference = ROW_PROGRAMS[local]
        contents = dict(local)
        output_word = c89.ROLE_TO_WORD[output]
        for slot, direction in enumerate(DIRECTION_ORDER):
            original = contents[direction]
            for replacement, replacement_word in c89.ROLE_TO_WORD.items():
                if replacement == original:
                    continue
                words = [c89.ROLE_TO_WORD[contents[item]] for item in DIRECTION_ORDER]
                words[slot] = replacement_word
                candidate = flatten(tuple(words))
                prefix = common_prefix(candidate, reference)
                actual = assignments(pipeline_records(candidate, reference, output_word, prefix))
                substitution_count += 1
                if actual:
                    substitution_failures.append((output, slot, original, replacement, prefix, actual))
    check("C03 all 3,648 one-role substitutions stop quietly", substitution_count == 3_648 and not substitution_failures, str(substitution_failures[:1]))

    failures = []
    states = edges = terminals = 0
    outputs_seen = set()
    for local, output in SIX_ROWS:
        reference = ROW_PROGRAMS[local]
        output_word = c89.ROLE_TO_WORD[output]
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
                outputs_seen.add(decode_output(records, 48))
    check("C04 four pipelines have 264 states, 260 edges, four terminals", (states, edges, terminals) == (264, 260, 4), str((states, edges, terminals)))
    check("C05 every full-row physical frontier is exact", not failures, str(failures[:1]))
    check("C06 terminal words are exactly the four live outputs", outputs_seen == {c89.ROLE_TO_WORD[output] for _local, output in SIX_ROWS})
    check("C07 each pipeline has 262 supplied source records", all(len(pipeline_records(ROW_PROGRAMS[local], ROW_PROGRAMS[local], c89.ROLE_TO_WORD[output], 0)) == 262 for local, output in SIX_ROWS))


def covariance_and_scope_contract() -> None:
    section("D - Proper-cubic covariance and residual boundary")
    local, output = SIX_ROWS[0]
    program = ROW_PROGRAMS[local]
    output_word = c89.ROLE_TO_WORD[output]
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
            actual = assignments(transformed)
            if actual != transformed_expected:
                failures.append((rotation_index, transformed_expected, actual))
    check("D01 all 96 transformed pipeline controls are exact", not failures, str(failures[:1]))
    note = NOTE.read_text(encoding="utf-8").lower() if NOTE.is_file() else ""
    for marker in ("*", "`", ">"):
        note = note.replace(marker, "")
    note = " ".join(note.split())
    check("D02 note exists and carries authority none", NOTE.is_file() and "authority: none" in note)
    check("D03 note says all streams and program rails are supplied", "all streams and program rails are supplied" in note)
    check("D04 note names the open-direction residual", "open_direction_to_empty_word" in note)
    check("D05 note names serial-selector residual", "serial_program_selection" in note)
    check("D06 note denies foundation and axiom effects", "no foundation edit" in note and "no axiom addition follows" in note)


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    program_bank_contract()
    writer_contract()
    substitution_and_pipeline_contract()
    covariance_and_scope_contract()
    print("\nPROGRAMS=236 SLOT_BITS=48 EMPTY_SLOTS=742 SIX_ROWS=4")
    print("OUTPUT_CANONICAL=5 OUTPUT_RAW=48 PHYSICAL_UNION_RAW=5452")
    print("FULL_ROW_STATES=264 FULL_ROW_EDGES=260 SUBSTITUTIONS=3648")
    print(f"SUMMARY: {PASS} PASS / {FAIL} FAIL")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
