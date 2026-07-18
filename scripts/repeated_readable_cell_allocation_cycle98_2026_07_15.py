#!/usr/bin/env python3
"""Cycle 98: repeated readable cells and the exact static-allocation residual.

Starting from Cycle 94's live R_B11 macrostep, this probe instantiates two
complete successor cells and the following comparator on the actual Cycle-85
endpoint.  It then exhausts the 51 row/geometry phases needed for indefinite
translation of the same pre-laid cell architecture.

The positive result is deliberately conditional: every cell's 280 static
source records are supplied, while its predecessor grows the START and the
cell grows 83 records.  Every one of the 280 source records is nevertheless
consumed by an exact intended signature.  The current table has no first
write from a completed predecessor into that source, so autonomous allocation
is not claimed.

Authority: none.  No foundation, registry, queue, audit, or git state follows.
"""

from __future__ import annotations

from collections import Counter, defaultdict, deque
from dataclasses import dataclass
from pathlib import Path

import four_open_reservation_comb_cycle59_2026_07_14 as c59
import live_directional_program_writer_cycle90_2026_07_15 as c90
import live_eight_bit_physical_comparator_cycle89_2026_07_15 as c89
import live_seed_row_readable_macrostep_cycle94_2026_07_15 as c94
import official_seed_to_rail_nucleation_cycle53_2026_07_14 as c53
import three_phase_recurrent_append_tube_cycle80_2026_07_14 as c80


ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / "docs" / "work_history" / "repo" / "review_feedback"
NOTE = REVIEW / "REPEATED_READABLE_CELL_ALLOCATION_CYCLE98_NOTE_2026-07-15.md"

Coord = tuple[int, int, int]
Signature = c53.Signature
Word = c89.Word
Matrix = tuple[tuple[int, int, int], tuple[int, int, int], tuple[int, int, int]]
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


def scale(value: int, site: Coord) -> Coord:
    return tuple(value * coordinate for coordinate in site)  # type: ignore[return-value]


def manhattan(left: Coord, right: Coord) -> int:
    return sum(abs(a - b) for a, b in zip(left, right))


def dot(left: Coord, right: Coord) -> int:
    return sum(a * b for a, b in zip(left, right))


def bit_content(bit: int) -> str:
    return H1 if bit else H0


def matmul(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(sum(left[row][axis] * right[axis][column] for axis in range(3)) for column in range(3))
        for row in range(3)
    )  # type: ignore[return-value]


IDENTITY: Matrix = ((1, 0, 0), (0, 1, 0), (0, 0, 1))


def transform_site(site: Coord, rotation: Matrix, shift: Coord) -> Coord:
    return add(c53.matvec(rotation, site), shift)


def transform_records(
    records: dict[Coord, str], rotation: Matrix, shift: Coord
) -> dict[Coord, str]:
    return {
        transform_site(site, rotation, shift): content
        for site, content in records.items()
    }


def translated(records: dict[Coord, str], shift: Coord) -> dict[Coord, str]:
    return {add(site, shift): content for site, content in records.items()}


def translated_additions(
    additions: tuple[tuple[Coord, str], ...], shift: Coord
) -> tuple[tuple[Coord, str], ...]:
    return tuple((add(site, shift), content) for site, content in additions)


def merge_records(*parts: dict[Coord, str]) -> dict[Coord, str]:
    answer: dict[Coord, str] = {}
    for part in parts:
        for site, content in part.items():
            if site in answer and answer[site] != content:
                raise ValueError((site, answer[site], content))
            answer[site] = content
    return answer


def merge_raw(
    *tables: dict[Signature, frozenset[str]],
) -> dict[Signature, frozenset[str]]:
    outputs: dict[Signature, set[str]] = defaultdict(set)
    for table in tables:
        for local, values in table.items():
            outputs[local].update(values)
    return {local: frozenset(values) for local, values in outputs.items()}


# ---------------------------------------------------------------------------
# The only Cycle-94 phase repair: its final tap hard-coded H1 behind the tap.
# That site is also comparator reference bit 47.  Two recurrent A rows end in
# H0, so the same equality tap needs the H0-back image for equal DATA bits.
# ---------------------------------------------------------------------------

EXTENDED_TAP_TABLE: dict[Signature, str] = {}
for equal_bit in (H0, H1):
    EXTENDED_TAP_TABLE[c94.canonical({
        (-1, 0, 0): H0,
        (1, 0, 0): c94.BRIDGE_TOKEN,
        (0, -1, 0): equal_bit,
        (0, 1, 0): equal_bit,
        (0, 0, 1): c94.FINAL_TAP_GUARD,
    })] = H1

EXTENDED_TAP_RAW = c59.raw_rule_outputs(EXTENDED_TAP_TABLE)
COMBINED_RAW = merge_raw(c94.COMBINED_RAW, EXTENDED_TAP_RAW)


def enabled(records: dict[Coord, str]) -> dict[Coord, frozenset[str]]:
    return {
        target: COMBINED_RAW[local]
        for target in c53.open_candidates(records)
        if (local := c53.local_signature(records, target)) in COMBINED_RAW
    }


def generalized_readable_source(program: tuple[int, ...], word: Word) -> dict[Coord, str]:
    records = c94.readable_source(word, word, port=False)
    records[c94.FINAL_TAP_BACK] = bit_content(program[-1])
    return records


def recurrent_rows() -> tuple[tuple[Signature, str], ...]:
    by_output = {output: local for local, output in c80.CONSTRUCTION.table.items()}
    return tuple(
        (by_output[c80.role(phase, y, z)], c80.role(phase, y, z))
        for phase in ("B", "C", "A")
        for y, z in c80.layer_order(phase)
    )


ROWS = recurrent_rows()


@dataclass(frozen=True)
class Cell:
    index: int
    signature: Signature
    output: str
    program: tuple[int, ...]
    word: Word
    rotation: Matrix
    shift: Coord
    start: Coord
    match: Coord
    comparator_source: dict[Coord, str]
    writer_source: dict[Coord, str]
    source: dict[Coord, str]
    comparator_additions: tuple[tuple[Coord, str], ...]
    writer_additions: tuple[tuple[Coord, str], ...]
    additions: tuple[tuple[Coord, str], ...]
    support: frozenset[Coord]


def build_cells(count: int) -> tuple[Cell, ...]:
    cells: list[Cell] = []
    rotation = IDENTITY
    shift = (0, 0, 0)
    for index in range(count):
        signature, output = ROWS[index % len(ROWS)]
        program = c90.ROW_PROGRAMS[signature]
        word = c89.ROLE_TO_WORD[output]

        comparator_local = c90.stream_harness(program, program)
        comparator_local.pop(c94.PRIMARY_START)
        writer_local = c94.translated(
            generalized_readable_source(program, word), c94.READ_SHIFT
        )
        comparator_source = transform_records(comparator_local, rotation, shift)
        writer_source = transform_records(writer_local, rotation, shift)
        source = merge_records(comparator_source, writer_source)

        comparator_additions = tuple(
            (transform_site(site, rotation, shift), H1)
            for site in c94.PRIMARY_CERT
        )
        writer_additions = tuple(
            (
                transform_site(c94.translate(site, c94.READ_SHIFT), rotation, shift),
                content,
            )
            for site, content in c94.readable_additions(word)
        )
        additions = comparator_additions + writer_additions
        start = transform_site(c94.PRIMARY_START, rotation, shift)
        match = transform_site(c94.READ_MATCH, rotation, shift)
        dynamic_sites = {site for site, _content in additions}
        support = frozenset(set(source) | dynamic_sites | {start})
        cells.append(Cell(
            index=index,
            signature=signature,
            output=output,
            program=program,
            word=word,
            rotation=rotation,
            shift=shift,
            start=start,
            match=match,
            comparator_source=comparator_source,
            writer_source=writer_source,
            source=source,
            comparator_additions=comparator_additions,
            writer_additions=writer_additions,
            additions=additions,
            support=support,
        ))

        # Cycle 94's next comparator is exactly the next cell's local frame.
        shift = add(c53.matvec(rotation, c94.NEXT_SHIFT), shift)
        rotation = matmul(rotation, c94.NEXT_ROTATION)
    return tuple(cells)


CELLS = build_cells(105)
CELL0, CELL1, CELL2 = CELLS[:3]


# ---------------------------------------------------------------------------
# Two actual recurrent handoffs on Cycle 85, with all predecessor debris.
# ---------------------------------------------------------------------------

LOCAL_SOURCE = merge_records(CELL0.source, CELL1.source, CELL2.comparator_source)
LOCAL_ADDITIONS = (
    ((CELL0.start, H1),)
    + CELL0.additions
    + CELL1.additions
    + CELL2.comparator_additions
)
APPARATUS = transform_records(LOCAL_SOURCE, c94.PLACEMENT_ROTATION, c94.PLACEMENT_SHIFT)
SOURCE = merge_records(c94.ENDPOINT, APPARATUS)
ADDITIONS = tuple(
    (transform_site(site, c94.PLACEMENT_ROTATION, c94.PLACEMENT_SHIFT), content)
    for site, content in LOCAL_ADDITIONS
)


def records_at(step: int) -> dict[Coord, str]:
    records = dict(SOURCE)
    records.update(dict(ADDITIONS[:step]))
    return records


def expected_at(step: int) -> dict[Coord, frozenset[str]]:
    if step == len(ADDITIONS):
        return {}
    site, content = ADDITIONS[step]
    return {site: frozenset((content,))}


def component_sizes(sites: set[Coord]) -> tuple[int, ...]:
    unseen = set(sites)
    sizes: list[int] = []
    while unseen:
        seed = unseen.pop()
        queue = deque((seed,))
        size = 0
        while queue:
            site = queue.popleft()
            size += 1
            for direction in c53.DIRECTIONS:
                neighbor = add(site, direction)
                if neighbor in unseen:
                    unseen.remove(neighbor)
                    queue.append(neighbor)
        sizes.append(size)
    return tuple(sorted(sizes, reverse=True))


def interval_gap(left: tuple[int, int], right: tuple[int, int]) -> int:
    if left[1] < right[0]:
        return right[0] - left[1]
    if right[1] < left[0]:
        return left[0] - right[1]
    return 0


def adjacent_or_overlapping(left: set[Coord] | frozenset[Coord], right: set[Coord] | frozenset[Coord]) -> bool:
    if not set(left).isdisjoint(right):
        return True
    return any(add(site, direction) in right for site in left for direction in c53.DIRECTIONS)


# ---------------------------------------------------------------------------
# Contracts.
# ---------------------------------------------------------------------------

def table_and_phase_contract() -> None:
    section("A - Minimal final-tap phase repair and all recurrent rows")
    check("A01 Cycle 98 note exists", NOTE.is_file())
    phase_census = Counter(output[-1] if output.startswith("R_L") else output[2] for _local, output in ROWS)
    check("A02 recurrent order has exactly B,C,A Hamiltonian rows", len(ROWS) == 51 and phase_census == {"A": 17, "B": 17, "C": 17})
    check("A03 first three actual rows are R_B11,R_B10,R_B00", tuple(output for _local, output in ROWS[:3]) == ("R_B11", "R_B10", "R_B00"))
    check("A04 phase repair adds exactly two canonical H0-back equality rows", len(EXTENDED_TAP_TABLE) == 2 and set(EXTENDED_TAP_TABLE.values()) == {H1})
    check("A05 phase repair has exactly 48 proper-cubic raw rows", len(EXTENDED_TAP_RAW) == 48)
    check("A06 phase repair is disjoint from the Cycle-94 union", set(EXTENDED_TAP_RAW).isdisjoint(c94.COMBINED_RAW))
    check("A07 extended mixed union has exactly 5,728 raw inputs", len(COMBINED_RAW) == 5_728)
    check("A08 every mixed raw input remains single-valued", all(len(values) == 1 for values in COMBINED_RAW.values()))
    h0_tail_rows = tuple(index for index, (local, _output) in enumerate(ROWS) if c90.ROW_PROGRAMS[local][-1] == 0)
    check("A09 only recurrent rows 48 and 49 need the H0-back repair", h0_tail_rows == (48, 49), str(h0_tail_rows))


def cell_census_contract() -> None:
    section("B - Exact supplied, grown, shared, and certified census")
    check("B01 every complete cell has 192 comparator source records", all(len(cell.comparator_source) == 192 for cell in CELLS[:51]))
    check("B02 every complete cell has 89 writer source records", all(len(cell.writer_source) == 89 for cell in CELLS[:51]))
    check("B03 one safe comparator/writer alias leaves 280 static records", all(len(set(cell.comparator_source) & set(cell.writer_source)) == 1 and len(cell.source) == 280 for cell in CELLS[:51]))
    check("B04 every cell grows exactly 48+35=83 records after START", all(len(cell.comparator_additions) == 48 and len(cell.writer_additions) == 35 and len(cell.additions) == 83 for cell in CELLS[:51]))
    check("B05 predecessor MATCH is literally successor START", all(left.match == right.start for left, right in zip(CELLS, CELLS[1:])))
    check("B06 consecutive complete cells share only MATCH/START", all(set(left.support) & set(right.support) == {left.match} for left, right in zip(CELLS[:52], CELLS[1:53])))

    payload = set(CELL1.comparator_source) & {
        transform_site(site, CELL1.rotation, CELL1.shift)
        for site in tuple((index, 0, 0) for index in range(48)) + tuple((index, 2, 0) for index in range(48))
    }
    payload |= {
        transform_site(c94.translate(site, c94.READ_SHIFT), CELL1.rotation, CELL1.shift)
        for site in c94.PROGRAM + c94.REFERENCE
    }
    fixed = set(CELL1.source) - payload
    check("B07 successor payload is exactly 112 records", len(payload) == 112)
    check("B08 successor fixed frame/cage is exactly 168 records", len(fixed) == 168)
    check("B09 successor static source has exactly twelve components", component_sizes(set(CELL1.source)) == (123, 82, 65, 2, 1, 1, 1, 1, 1, 1, 1, 1), str(component_sizes(set(CELL1.source))))
    distances = tuple(manhattan(CELL1.start, site) for site in CELL1.source)
    check("B10 START is distance two from the source and adjacent to none", min(distances) == 2 and distances.count(1) == 0)

    # The handoff itself writes only START.  Its launched comparator then
    # consumes all 192 comparator records; the writer consumes 89 records with
    # one overlap, so the complete launched interval checks all 280.
    predecessor_use = {
        add(target, direction)
        for target, _content in CELL0.additions
        for direction in c53.DIRECTIONS
        if add(target, direction) in CELL1.source
    }

    # Exact-signature consumption: record every cell-1 source neighbour used
    # by its intended 83 writes, then remove that record at its first use.
    records = merge_records(CELL0.source, CELL1.source, CELL2.source, {CELL0.start: H1})
    records.update(dict(CELL0.additions))
    first_use: dict[Coord, tuple[dict[Coord, str], Coord, str]] = {}
    for target, content in CELL1.additions:
        for direction in c53.DIRECTIONS:
            site = add(target, direction)
            if site in CELL1.source and site not in first_use:
                first_use[site] = (dict(records), target, content)
        records[target] = content
    removal_same = []
    removal_kills = 0
    removal_flips = 0
    for site, (stage, target, content) in first_use.items():
        without = dict(stage)
        without.pop(site)
        actual = enabled(without)
        expected = {target: frozenset((content,))}
        if actual == expected:
            removal_same.append((site, target, content))
        elif actual == {}:
            removal_kills += 1
        elif set(actual) == {target} and actual[target] != expected[target]:
            removal_flips += 1
    comparator_use = {
        site
        for site, (_stage, target, _content) in first_use.items()
        if target in {target_site for target_site, _value in CELL1.comparator_additions}
    }
    writer_use = set(first_use) - comparator_use
    check("B11 predecessor completion grows START but consumes zero successor-static records", not predecessor_use and CELL0.match == CELL1.start)
    check("B12 launched comparator consumes 192 source records and writer adds the other 88", len(comparator_use) == 192 and len(writer_use) == 88 and comparator_use | writer_use == set(CELL1.source), f"comparator={len(comparator_use)} writer_new={len(writer_use)}")
    check("B13 all 280 static records occur in an intended exact signature", set(first_use) == set(CELL1.source), f"used={len(first_use)}")
    check("B14 equal-path deletion makes 242 records indispensable and leaves 38 H1 guards redundant", len(first_use) == 280 and removal_kills == 232 and removal_flips == 10 and len(removal_same) == 38, f"kill={removal_kills} flip={removal_flips} same={len(removal_same)}")

    # Those 38 records are not removable from a comparator.  Each is the H1
    # cage beside a reference-one bit.  Deleting it while changing that
    # candidate bit to H0 exposes an H0 append instead of rejecting the row.
    selector_failures = []
    selector_controls = 0
    for reference_signature, _output in ROWS:
        reference = c90.ROW_PROGRAMS[reference_signature]
        for candidate in c90.ROW_PROGRAMS.values():
            prefix = c90.common_prefix(candidate, reference)
            stage = c90.stream_harness(candidate, reference)
            stage.update({(index, 1, 0): H1 for index in range(prefix)})
            if prefix < 48:
                selector_controls += 1
                actual = COMBINED_RAW.get(c53.local_signature(stage, (prefix, 1, 0)))
                if actual is not None:
                    selector_failures.append((reference_signature, prefix, actual))
    guard_controls = []
    for index, bit in enumerate(CELL1.program):
        if not bit:
            continue
        candidate = list(CELL1.program)
        candidate[index] = 0
        stage = c90.stream_harness(tuple(candidate), CELL1.program)
        stage.update({(prior, 1, 0): H1 for prior in range(index)})
        stage.pop((index, 1, -1))
        guard_controls.append(COMBINED_RAW.get(c53.local_signature(stage, (index, 1, 0))))
    check("B15 all 11,985 unequal row/reference controls stop at their first mismatch", selector_controls == 51 * 235 and not selector_failures, f"controls={selector_controls} failures={selector_failures[:1]}")
    check("B16 all 38 equal-path-redundant H1 guards block a mismatched H0 append", len(guard_controls) == 38 and set(guard_controls) == {frozenset((H0,))})

    predecessor_only = merge_records(CELL0.source, {CELL0.start: H1})
    predecessor_only.update(dict(CELL0.additions))
    check("B17 completed predecessor alone writes none of the absent successor source", enabled(predecessor_only) == {}, str(enabled(predecessor_only)))


def actual_two_handoff_contract() -> None:
    section("C - Two consecutive actual recurrent-row handoffs with old debris")
    check("C01 local source is exactly 280+280+192=752 supplied records", len(LOCAL_SOURCE) == 752)
    check("C02 physical apparatus stays disjoint from the actual Cycle-85 endpoint", set(APPARATUS).isdisjoint(c94.ENDPOINT))
    check("C03 actual endpoint initially enables only the original R_B11 port", enabled(SOURCE) == {c94.PHYSICAL_TARGET: frozenset((H1,))}, str(enabled(SOURCE)))
    failures = []
    for step in range(len(ADDITIONS) + 1):
        actual = enabled(records_at(step))
        expected = expected_at(step)
        if actual != expected:
            failures.append((step, expected, actual))
    check("C04 all 216 states have their exact singleton-or-terminal frontier", len(ADDITIONS) == 215 and not failures, str(failures[:1]))
    check("C05 two full cells and the third comparator grow exactly 215 records", len(ADDITIONS) == 1 + 83 + 83 + 48)
    check("C06 terminal is quiet and conflict-free", enabled(records_at(len(ADDITIONS))) == {})
    terminal = records_at(len(ADDITIONS))
    physical_match1 = transform_site(CELL0.match, c94.PLACEMENT_ROTATION, c94.PLACEMENT_SHIFT)
    physical_match2 = transform_site(CELL1.match, c94.PLACEMENT_ROTATION, c94.PLACEMENT_SHIFT)
    check("C07 first verified R_B11 MATCH remains as old debris", terminal.get(physical_match1) == H1)
    check("C08 second verified R_B10 MATCH starts the complete R_B00 comparator", terminal.get(physical_match2) == H1 and all(transform_site(site, c94.PLACEMENT_ROTATION, c94.PLACEMENT_SHIFT) in terminal for site, _content in CELL2.comparator_additions))
    check("C09 the two completed readable values are exactly R_B11 and R_B10", CELL0.word == c89.ROLE_TO_WORD["R_B11"] and CELL1.word == c89.ROLE_TO_WORD["R_B10"])


def phase_quotient_contract() -> None:
    section("D - All 51 adjacent phase handoffs, schedules, and mixed parasites")
    failures = []
    states = 0
    edges = 0
    for index in range(51):
        previous, current, following = CELLS[index:index + 3]
        records = merge_records(previous.source, current.source, following.source, {previous.start: H1})
        records.update(dict(previous.additions))
        for step in range(len(current.additions) + 1):
            states += 1
            actual = enabled(records)
            if step < len(current.additions):
                target, content = current.additions[step]
                expected = {target: frozenset((content,))}
            else:
                target, content = following.comparator_additions[0]
                expected = {target: frozenset((content,))}
            if actual != expected:
                failures.append((index, step, expected, actual))
                break
            if step < len(current.additions):
                target, content = current.additions[step]
                records[target] = content
                edges += 1
    check("D01 all 51 row/geometry phases have exact mixed-union frontiers", not failures, str(failures[:1]))
    check("D02 quotient exhausts exactly 4,284 states and 4,233 writes", states == 51 * 84 and edges == 51 * 83, f"states={states} edges={edges}")
    check("D03 every reachable frontier is singleton, so all asynchronous schedules coincide", not failures and edges == 4_233)

    covariance_failures = []
    covariance_controls = 0
    for signature, expected in COMBINED_RAW.items():
        for rotation in c53.ROTATIONS:
            covariance_controls += 1
            actual = COMBINED_RAW.get(c53.rotate_signature(signature, rotation))
            if actual != expected:
                covariance_failures.append((signature, rotation, expected, actual))
    check("D04 all 137,472 proper-cubic raw images retain the same output", covariance_controls == 5_728 * 24 and not covariance_failures, str(covariance_failures[:1]))


def unbounded_induction_contract() -> None:
    section("E - Translation/phase induction and nonlocal-debris exclusion")
    rotation3 = matmul(matmul(c94.NEXT_ROTATION, c94.NEXT_ROTATION), c94.NEXT_ROTATION)
    drift3 = sub(CELLS[3].start, CELL0.start)
    drift51 = sub(CELLS[51].start, CELL0.start)
    check("E01 cell orientation has order exactly three", rotation3 == IDENTITY and c94.NEXT_ROTATION != IDENTITY and matmul(c94.NEXT_ROTATION, c94.NEXT_ROTATION) != IDENTITY)
    check("E02 every third cell is translated by (49,-49,-49)", drift3 == (49, -49, -49) and all(CELLS[index + 3].support == frozenset(add(site, drift3) for site in CELLS[index].support) for index in range(51)))
    check("E03 row, orientation, content, and source repeat after 51 cells", drift51 == (833, -833, -833) and all(CELLS[index + 51].source == translated(CELLS[index].source, drift51) and CELLS[index + 51].additions == translated_additions(CELLS[index].additions, drift51) for index in range(51)))

    # Exact unbounded separation proof.  Geometry repeats every three cells by
    # D3.  Projection u=(1,-1,-1) advances 147 per three-cell block.  Only the
    # finitely many residue/block pairs whose projection intervals lie within
    # one can possibly touch; exhaust those pairs as literal site sets.
    projection = (1, -1, -1)
    advance = dot(projection, drift3)
    bases = tuple(CELLS[index].support for index in range(3))
    intervals = tuple((min(dot(projection, site) for site in support), max(dot(projection, site) for site in support)) for support in bases)
    near_pairs: list[tuple[int, int, int, int]] = []
    separation_failures = []
    for left_residue in range(3):
        for right_residue in range(3):
            for block_delta in range(-10, 11):
                index_delta = 3 * block_delta + right_residue - left_residue
                if index_delta < 2:
                    continue
                shifted_interval = tuple(value + block_delta * advance for value in intervals[right_residue])
                if interval_gap(intervals[left_residue], shifted_interval) <= 1:
                    near_pairs.append((left_residue, right_residue, block_delta, index_delta))
                    shifted_right = {add(site, scale(block_delta, drift3)) for site in bases[right_residue]}
                    if adjacent_or_overlapping(bases[left_residue], shifted_right):
                        separation_failures.append((left_residue, right_residue, block_delta, index_delta))
    # The [-10,10] window contains every possible near interval because even
    # its nearest outer interval is farther than one in projection.
    outside_separated = all(
        interval_gap(intervals[left], tuple(value + block * advance for value in intervals[right])) > 1
        for left in range(3)
        for right in range(3)
        for block in (-11, 11)
    )
    check("E04 projection advance is exactly 147 and bounds all distant blocks", advance == 147 and outside_separated, f"intervals={intervals}")
    check("E05 no nonconsecutive residue/block pair can even approach NN range", not near_pairs and not separation_failures, str(separation_failures[:1]))

    # Pin the nearest actual nonconsecutive separation rather than relying only
    # on the Boolean exclusion.
    min_nonconsecutive = min(
        manhattan(left, right)
        for left in CELLS[0].support
        for right in CELLS[2].support
    )
    check("E06 the nearest gap-two supports are exactly L1 distance 49", min_nonconsecutive == 49, str(min_nonconsecutive))
    check("E07 51 phase quotients plus the exact drift form an unbounded conditional induction", not separation_failures and drift51 == (833, -833, -833) and len(ROWS) == 51)


def scope_and_no_go_contract() -> None:
    section("F - Bounded allocation result and N1-N8 discipline")
    note = NOTE.read_text(encoding="utf-8").lower()
    check("F01 note pins 752 supplied and 215 grown in the actual run", "752 supplied" in note and "215 grown" in note)
    check("F02 note pins 280 static, 83 grown, and one predecessor START per complete successor", "280 static" in note and "83" in note and "predecessor" in note)
    check("F03 note separates the 168 fixed and 112 payload residuals", "168" in note and "112" in note)
    check("F04 note does not claim autonomous self-allocation", "does not prove autonomous self-allocation" in note)
    check("F05 note names the next MATCH-to-allocation-spine construction", "match_to_successor_allocation_spine" in note)
    check("F06 note contains the full N1-N8 stress test", all(f"n{index}" in note for index in range(1, 9)))
    check("F07 note keeps alternative architectures live", "live alternative" in note and "cycle 52" in note)
    check("F08 Cycle 98 writes only its runner and review note", all(path.parent in (ROOT / "scripts", REVIEW) for path in (Path(__file__), NOTE)))


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    table_and_phase_contract()
    cell_census_contract()
    actual_two_handoff_contract()
    phase_quotient_contract()
    unbounded_induction_contract()
    scope_and_no_go_contract()
    print(f"\nROWS={len(ROWS)} EXTENDED_CANONICAL={len(EXTENDED_TAP_TABLE)} EXTENDED_RAW={len(EXTENDED_TAP_RAW)} UNION_RAW={len(COMBINED_RAW)}")
    print(f"ACTUAL_SUPPLIED={len(LOCAL_SOURCE)} ACTUAL_GROWN={len(LOCAL_ADDITIONS)} COMPLETE_CELL_STATIC={len(CELL1.source)} COMPLETE_CELL_GROWN={len(CELL1.additions)}")
    print(f"DRIFT3={sub(CELLS[3].start, CELL0.start)} DRIFT51={sub(CELLS[51].start, CELL0.start)}")
    print(f"SUMMARY: {PASS} PASS / {FAIL} FAIL")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
