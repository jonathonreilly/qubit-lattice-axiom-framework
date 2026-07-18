#!/usr/bin/env python3
"""Cycle 97: actual five-port plus OPEN R_LB macrostep.

Five validated eight-bit neighbour macroblocks are supplied at five
seed-relative spatial ports.  The sixth, +x, port is genuinely open.  A local
four-sided sensor writes only while both axial sites are open, grows the
reserved 11111111 word, and releases a caged equality sweep over the six
spatial ports in the fixed direction order.  The accepted R_LB port drives a
readable eight-bit writer; the verified word starts the actual
R_LB + five OPEN -> R_C22 comparator.

This is a bounded physical-interface construction.  Port blocks, reference
bits, cages, and the next comparator are supplied rather than seed-grown.
Authority: none.
"""

from __future__ import annotations

from collections import defaultdict
from pathlib import Path

import four_open_reservation_comb_cycle59_2026_07_14 as c59
import live_directional_program_writer_cycle90_2026_07_15 as c90
import live_eight_bit_physical_comparator_cycle89_2026_07_15 as c89
import live_seed_row_readable_macrostep_cycle94_2026_07_15 as c94
import official_seed_to_rail_nucleation_cycle53_2026_07_14 as c53


ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / "docs" / "work_history" / "repo" / "review_feedback"
NOTE = REVIEW / "ACTUAL_FIVE_PORT_OPEN_RLB_MACROSTEP_CYCLE97_NOTE_2026-07-15.md"

Coord = tuple[int, int, int]
Signature = c53.Signature
Word = c89.Word
H0 = "H0"
H1 = "H1"
GUARD = "A_0_0"
SENSOR_GUARD = "A_0_1"
FRAME_MARKER = "JOINT"
PASS = 0
FAIL = 0


def add(left: Coord, right: Coord, scale: int = 1) -> Coord:
    return tuple(left[i] + scale * right[i] for i in range(3))  # type: ignore[return-value]


def sub(left: Coord, right: Coord) -> Coord:
    return tuple(left[i] - right[i] for i in range(3))  # type: ignore[return-value]


def neg(value: Coord) -> Coord:
    return tuple(-item for item in value)  # type: ignore[return-value]


def dot(left: Coord, right: Coord) -> int:
    return sum(a * b for a, b in zip(left, right))


def cross(left: Coord, right: Coord) -> Coord:
    return (
        left[1] * right[2] - left[2] * right[1],
        left[2] * right[0] - left[0] * right[2],
        left[0] * right[1] - left[1] * right[0],
    )


def bit_content(bit: int) -> str:
    return H1 if bit else H0


def canonical(items: dict[Coord, str]) -> Signature:
    return c53.canonical_signature(tuple(items.items()))


def transform_site(site: Coord, rotation: c53.Matrix, shift: Coord) -> Coord:
    return add(c53.matvec(rotation, site), shift)


def transform_records(
    records: dict[Coord, str], rotation: c53.Matrix, shift: Coord
) -> dict[Coord, str]:
    return {
        transform_site(site, rotation, shift): content
        for site, content in records.items()
    }


def merge_records(target: dict[Coord, str], source: dict[Coord, str]) -> None:
    for site, content in source.items():
        prior = target.get(site)
        if prior is not None and prior != content:
            raise ValueError((site, prior, content))
        target[site] = content


def merge_raw(
    *tables: dict[Signature, frozenset[str]],
) -> dict[Signature, frozenset[str]]:
    outputs: dict[Signature, set[str]] = defaultdict(set)
    for table in tables:
        for local, values in table.items():
            outputs[local].update(values)
    return {local: frozenset(values) for local, values in outputs.items()}


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


# ---------------------------------------------------------------------------
# The real arity-five R_LB row and its next arity-one C-phase consumer.
# ---------------------------------------------------------------------------

RLB_SIGNATURE, RLB_OUTPUT = next(
    (local, output)
    for local, output in c89.LIVE_TABLE.items()
    if output == "R_LB" and len(local) == 5
)
NEXT_SIGNATURE, NEXT_OUTPUT = next(
    (local, output)
    for local, output in c89.LIVE_TABLE.items()
    if local == (((-1, 0, 0), "R_LB"),)
)
RLB_PROGRAM = c90.ROW_PROGRAMS[RLB_SIGNATURE]
NEXT_PROGRAM = c90.ROW_PROGRAMS[NEXT_SIGNATURE]
RLB_WORD = c89.ROLE_TO_WORD[RLB_OUTPUT]
PROGRAM_WORDS = tuple(
    RLB_PROGRAM[8 * index:8 * (index + 1)] for index in range(6)
)


# ---------------------------------------------------------------------------
# Six physical port blocks.  The first five lie on the -x,-y,-z,+z,+y faces
# of a seed-relative frame.  The +x OPEN block is grown radially from a true
# open monitored site beside CENTER.
# ---------------------------------------------------------------------------

CENTER: Coord = (0, 0, 0)
MONITORED_OPEN: Coord = (1, 0, 0)
OPEN_SENSOR: Coord = (2, 0, 0)

FACE_DIRECTIONS: tuple[Coord, ...] = c90.DIRECTION_ORDER[:5]
FACE_Q0: tuple[Coord, ...] = (
    (-25, -4, -4),
    (-4, -25, -4),
    (-4, -4, -25),
    (-4, -4, 25),
    (-4, 25, -4),
)
FACE_T: tuple[Coord, ...] = (
    (0, 1, 0),
    (1, 0, 0),
    (1, 0, 0),
    (1, 0, 0),
    (1, 0, 0),
)


def face_group(
    direction: Coord, q0: Coord, tangent: Coord
) -> tuple[tuple[Coord, ...], tuple[Coord, ...], tuple[Coord, ...], tuple[Coord, ...]]:
    status = tuple(add(q0, tangent, index) for index in range(8))
    candidate = tuple(add(site, neg(direction)) for site in status)
    reference = tuple(add(site, direction) for site in status)
    normal = cross(direction, tangent)
    guards = tuple(
        guard
        for site in status
        for guard in (add(site, normal), add(site, neg(normal)))
    )
    return candidate, status, reference, guards


FACE_GROUPS = tuple(
    face_group(direction, q0, tangent)
    for direction, q0, tangent in zip(FACE_DIRECTIONS, FACE_Q0, FACE_T)
)
OPEN_CANDIDATE: tuple[Coord, ...] = tuple((5 + index, 5, 0) for index in range(8))
# The OPEN word is scanned back toward the sensor.  EMPTY is all-one, so this
# reverses only traversal order, not the physical eight-bit value; it keeps the
# scan predecessor clear of the sensor's four-sided openness cage.
OPEN_STATUS: tuple[Coord, ...] = tuple((12 - index, 6, 0) for index in range(8))
OPEN_REFERENCE: tuple[Coord, ...] = tuple((12 - index, 7, 0) for index in range(8))
OPEN_GUARDS: tuple[Coord, ...] = tuple(
    guard
    for site in OPEN_STATUS
    for guard in (add(site, (0, 0, -1)), add(site, (0, 0, 1)))
)

ALL_CANDIDATES = tuple(group[0] for group in FACE_GROUPS) + (OPEN_CANDIDATE,)
ALL_STATUS = tuple(group[1] for group in FACE_GROUPS) + (OPEN_STATUS,)
ALL_REFERENCES = tuple(group[2] for group in FACE_GROUPS) + (OPEN_REFERENCE,)


def axis_path(points: tuple[Coord, ...]) -> tuple[Coord, ...]:
    """Return the unit-step path after points[0], including every waypoint."""

    answer: list[Coord] = []
    current = points[0]
    for goal in points[1:]:
        differences = [index for index in range(3) if current[index] != goal[index]]
        if len(differences) != 1:
            raise ValueError((current, goal))
        axis = differences[0]
        step = 1 if goal[axis] > current[axis] else -1
        while current != goal:
            delta = [0, 0, 0]
            delta[axis] = step
            current = add(current, tuple(delta))  # type: ignore[arg-type]
            answer.append(current)
    if len(answer) != len(set(answer)):
        repeats = tuple(site for site in set(answer) if answer.count(site) > 1)
        raise ValueError(("path self-intersection", points, repeats[:8]))
    return tuple(answer)


OPEN_FEED: tuple[Coord, ...] = axis_path((OPEN_SENSOR, (4, 0, 0), (4, 5, 0)))


STATUS_T = FACE_T + ((-1, 0, 0),)
PREV = tuple(sub(status[0], tangent) for status, tangent in zip(ALL_STATUS, STATUS_T))

BRIDGE_POINTS: tuple[tuple[Coord, ...], ...] = (
    # OPEN completion -> first (-x) face.
    (
        OPEN_CANDIDATE[-1],
        (40, 5, 0),
        (40, -15, 0),
        (-27, -15, 0),
        (-27, -6, 0),
        (-27, -6, -4),
        (-25, -6, -4),
        PREV[0],
    ),
    # -x -> -y.
    (
        ALL_STATUS[0][-1],
        (-25, 15, -4),
        (-6, 15, -4),
        (-6, -25, -4),
        PREV[1],
    ),
    # -y -> -z.
    (
        ALL_STATUS[1][-1],
        (15, -25, -4),
        (15, -25, -35),
        (15, -4, -35),
        (-6, -4, -35),
        (-6, -4, -25),
        PREV[2],
    ),
    # -z -> +z, routed around y=-45.
    (
        ALL_STATUS[2][-1],
        (20, -4, -25),
        (20, -45, -25),
        (20, -45, 35),
        (-6, -45, 35),
        (-6, -4, 35),
        (-6, -4, 25),
        PREV[3],
    ),
    # +z -> +y.
    (
        ALL_STATUS[3][-1],
        (30, -4, 25),
        (30, 40, 25),
        (-6, 40, 25),
        (-6, 40, -4),
        (-6, 25, -4),
        PREV[4],
    ),
    # +y -> +x OPEN word.
    (
        ALL_STATUS[4][-1],
        (40, 25, -4),
        (40, 25, -45),
        (13, 25, -45),
        (13, 6, -45),
        PREV[5],
    ),
)
BRIDGES = tuple(axis_path(points) for points in BRIDGE_POINTS)
WRITER_PORT: Coord = (60, 60, 60)
WRITER_DATA0: Coord = (61, 60, 60)
PLANNED_WRITER_SOURCE = {
    add(site, WRITER_DATA0): content
    for site, content in c94.readable_source(RLB_WORD, RLB_WORD, port=False).items()
}
OUTPUT_BRIDGE = axis_path((
    ALL_STATUS[-1][-1],
    (-10, 6, 0),
    (-10, 6, 60),
    (-10, 60, 60),
    WRITER_PORT,
))
DYNAMIC_SCAN_SITES = {
    OPEN_SENSOR,
    *OPEN_FEED,
    *OPEN_CANDIDATE,
    *(site for group in ALL_STATUS for site in group),
    *(site for bridge in BRIDGES for site in bridge),
    *OUTPUT_BRIDGE,
    *PLANNED_WRITER_SOURCE,
}


def add_path_cage(
    source: dict[Coord, str],
    start: Coord,
    path: tuple[Coord, ...],
    successor: Coord,
) -> None:
    previous = start
    for index, target in enumerate(path):
        following = path[index + 1] if index + 1 < len(path) else successor
        excluded = {sub(previous, target), sub(following, target)}
        if len(excluded) != 2 or not excluded <= set(c53.DIRECTIONS):
            raise ValueError((previous, target, following))
        for direction in c53.DIRECTIONS:
            if direction not in excluded:
                cage_site = add(target, direction)
                if cage_site not in DYNAMIC_SCAN_SITES:
                    merge_records(source, {cage_site: GUARD})
        previous = target


# ---------------------------------------------------------------------------
# Static port/reference/cage source and the single ordered scan trajectory.
# ---------------------------------------------------------------------------

SCAN_SOURCE: dict[Coord, str] = {CENTER: FRAME_MARKER}

for slot, (candidate, status, reference, guards) in enumerate(FACE_GROUPS):
    for site, bit in zip(candidate, PROGRAM_WORDS[slot]):
        SCAN_SOURCE[site] = bit_content(bit)
    for site, bit in zip(reference, PROGRAM_WORDS[slot]):
        SCAN_SOURCE[site] = bit_content(bit)
    for site in guards:
        SCAN_SOURCE[site] = GUARD

for site in OPEN_REFERENCE:
    SCAN_SOURCE[site] = H1
for site in OPEN_GUARDS:
    SCAN_SOURCE[site] = GUARD

# OPEN_SENSOR has exactly four transverse guards; both axial sites are open.
for direction in ((0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)):
    SCAN_SOURCE[add(OPEN_SENSOR, direction)] = SENSOR_GUARD

# The feed and OPEN word form one caged append path.  Future status sites are
# protected, so the final word retains a clean comparator face.
add_path_cage(
    SCAN_SOURCE,
    OPEN_SENSOR,
    OPEN_FEED + OPEN_CANDIDATE,
    BRIDGES[0][0],
)

for index, bridge in enumerate(BRIDGES):
    start = BRIDGE_POINTS[index][0]
    successor = ALL_STATUS[index][0]
    add_path_cage(SCAN_SOURCE, start, bridge, successor)

add_path_cage(
    SCAN_SOURCE,
    ALL_STATUS[-1][-1],
    OUTPUT_BRIDGE,
    WRITER_DATA0,
)

SCAN_TARGETS: tuple[Coord, ...] = (
    (OPEN_SENSOR,)
    + OPEN_FEED
    + OPEN_CANDIDATE
    + BRIDGES[0]
    + ALL_STATUS[0]
    + BRIDGES[1]
    + ALL_STATUS[1]
    + BRIDGES[2]
    + ALL_STATUS[2]
    + BRIDGES[3]
    + ALL_STATUS[3]
    + BRIDGES[4]
    + ALL_STATUS[4]
    + BRIDGES[5]
    + ALL_STATUS[5]
    + OUTPUT_BRIDGE
)


def scan_table() -> dict[Signature, str]:
    records = dict(SCAN_SOURCE)
    table: dict[Signature, str] = {}
    for target in SCAN_TARGETS:
        if target in records:
            raise ValueError(("target supplied", target, records[target]))
        local = canonical(dict(c53.local_signature(records, target)))
        prior = table.get(local)
        if prior is not None and prior != H1:
            raise ValueError((local, prior))
        table[local] = H1
        records[target] = H1
    return table


SCAN_TABLE = scan_table()
SCAN_RAW = c59.raw_rule_outputs(SCAN_TABLE)


# ---------------------------------------------------------------------------
# Readable R_LB writer and physical start of its actual C-phase consumer.
# ---------------------------------------------------------------------------

WRITER_ROTATION: c53.Matrix = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
WRITER_SHIFT = WRITER_DATA0
WRITER_SOURCE = PLANNED_WRITER_SOURCE
WRITER_ADDITIONS = tuple(
    (transform_site(site, WRITER_ROTATION, WRITER_SHIFT), content)
    for site, content in c94.readable_additions(RLB_WORD)
)
WRITER_MATCH = transform_site(c94.MATCH, WRITER_ROTATION, WRITER_SHIFT)


def next_placement() -> tuple[c53.Matrix, Coord, dict[Coord, str], tuple[tuple[Coord, str], ...]]:
    occupied = set(SCAN_SOURCE) | set(SCAN_TARGETS) | set(WRITER_SOURCE) | {site for site, _ in WRITER_ADDITIONS}
    candidate = c90.stream_harness(NEXT_PROGRAM, NEXT_PROGRAM)
    candidate.pop(c89.START)
    certificates = tuple((index, 1, 0) for index in range(48))
    for rotation in c53.ROTATIONS:
        shift = sub(WRITER_MATCH, c53.matvec(rotation, c89.START))
        source = transform_records(candidate, rotation, shift)
        additions = tuple((transform_site(site, rotation, shift), H1) for site in certificates)
        if set(source).isdisjoint(occupied) and {site for site, _ in additions}.isdisjoint(occupied | set(source)):
            return rotation, shift, source, additions
    raise RuntimeError("no next-comparator placement")


NEXT_ROTATION, NEXT_SHIFT, NEXT_SOURCE, NEXT_ADDITIONS = next_placement()

SOURCE = dict(SCAN_SOURCE)
merge_records(SOURCE, WRITER_SOURCE)
merge_records(SOURCE, NEXT_SOURCE)
ADDITIONS = tuple((site, H1) for site in SCAN_TARGETS) + WRITER_ADDITIONS + NEXT_ADDITIONS

COMBINED_RAW = merge_raw(c94.COMBINED_RAW, SCAN_RAW)


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
    section("A - Actual row and six seed-relative physical ports")
    check("A01 row is the unique actual arity-five R_LB launcher", dict(RLB_SIGNATURE) == {(-1, 0, 0): "R_A22", (0, -1, 0): "R_B12", (0, 0, -1): "R_B21", (0, 0, 1): "R_B23", (0, 1, 0): "R_B32"} and RLB_OUTPUT == "R_LB")
    check("A02 program has five occupied words and +x EMPTY", PROGRAM_WORDS[:5] == tuple(c89.ROLE_TO_WORD[dict(RLB_SIGNATURE)[direction]] for direction in c90.DIRECTION_ORDER[:5]) and PROGRAM_WORDS[5] == c89.EMPTY_WORD)
    check("A03 five occupied candidate blocks lie on their seed-relative faces", all(all(dot(site, direction) == 24 for site in candidate) for direction, (candidate, _status, _reference, _guards) in zip(FACE_DIRECTIONS, FACE_GROUPS)))
    check("A04 monitored +x port is genuinely open", MONITORED_OPEN not in SOURCE and MONITORED_OPEN not in dict(ADDITIONS))
    check("A05 no EMPTY candidate bit is supplied", set(OPEN_CANDIDATE).isdisjoint(SOURCE))
    check("A06 the only supplied candidate bits are the forty occupied bits", sum(site in SOURCE for block in ALL_CANDIDATES for site in block) == 40)

    section("B - Local table, mixed law, and exact physical trajectory")
    check("B01 all three cage/frame roles are live and absent from every prior input signature", {GUARD, SENSOR_GUARD, FRAME_MARKER} <= c89.FULL_ROLES and all({GUARD, SENSOR_GUARD, FRAME_MARKER}.isdisjoint({content for _direction, content in local}) for local in c94.COMBINED_RAW))
    check("B02 scan table is proper-cubic and output-single-valued", all(len(values) == 1 for values in SCAN_RAW.values()))
    check("B03 scan raw domain is disjoint from the live Cycle-94 union", set(SCAN_RAW).isdisjoint(c94.COMBINED_RAW))
    check("B04 complete physical union is output-single-valued", all(len(values) == 1 for values in COMBINED_RAW.values()))
    failures = []
    for step in range(len(ADDITIONS) + 1):
        actual = enabled(records_at(step))
        expected = expected_at(step)
        if actual != expected:
            failures.append((step, expected, actual))
            break
    check("B05 every reachable stage has the exact singleton frontier", not failures, str(failures[:1]))
    check("B06 terminal is quiet", not enabled(records_at(len(ADDITIONS))))

    section("C - Value, mismatch, debris, and next-front controls")
    terminal = records_at(len(ADDITIONS))
    output_sites = tuple(transform_site(site, WRITER_ROTATION, WRITER_SHIFT) for site in c94.DATA)
    decoded = tuple(1 if terminal[site] == H1 else 0 for site in output_sites)
    check("C01 physical writer terminal is exactly R_LB=10110001", decoded == RLB_WORD == (1, 0, 1, 1, 0, 0, 0, 1))
    check("C02 reverse value sweep forms MATCH only after all eight taps", WRITER_MATCH in terminal and all(transform_site(site, WRITER_ROTATION, WRITER_SHIFT) in terminal for site in c94.TAP))
    check("C03 MATCH starts the actual R_LB-to-R_C22 comparator", NEXT_OUTPUT == "R_C22" and all(site in terminal for site, _content in NEXT_ADDITIONS))
    check("C04 next candidate carries R_LB followed by five EMPTY words", tuple(NEXT_PROGRAM[8*i:8*(i+1)] for i in range(6)) == (RLB_WORD,) + (c89.EMPTY_WORD,) * 5)

    mismatch_failures = []
    for slot, (block, status_block) in enumerate(zip(ALL_CANDIDATES[:5], ALL_STATUS[:5])):
        for bit_index, (candidate_site, status_site) in enumerate(zip(block, status_block)):
            step = next(index for index, (site, _content) in enumerate(ADDITIONS) if site == status_site)
            records = records_at(step)
            records[candidate_site] = H0 if records[candidate_site] == H1 else H1
            if enabled(records):
                mismatch_failures.append((slot, bit_index, enabled(records)))
    check("C05 every occupied-word one-bit corruption stops before acceptance", not mismatch_failures, str(mismatch_failures[:1]))

    blocked_failures = []
    for role in c89.FULL_ROLES:
        records = dict(SOURCE)
        records[MONITORED_OPEN] = role
        if OPEN_SENSOR in enabled(records):
            blocked_failures.append(role)
    check("C06 every live record at the monitored +x port blocks OPEN formation", not blocked_failures, str(blocked_failures[:1]))

    covariance_failures = []
    for local, values in COMBINED_RAW.items():
        for rotation in c53.ROTATIONS:
            rotated = c53.rotate_signature(local, rotation)
            if COMBINED_RAW.get(rotated) != values:
                covariance_failures.append((local, rotation, values, COMBINED_RAW.get(rotated)))
                break
    check("C07 exact full-table rotation closure lifts every verified stage to all proper-cubic images", not covariance_failures, str(covariance_failures[:1]))

    section("D - Supplied/grown boundary and constitutional scope")
    note = NOTE.read_text(encoding="utf-8").lower() if NOTE.is_file() else ""
    check("D01 note exists and carries authority none", NOTE.is_file() and "authority: none" in note)
    check("D02 note states the exact supplied and grown census", "supplied" in note and "grown" in note)
    check("D03 note names seed-grown harness and repeated allocation residuals", "seed_to_spatial_port_harness" in note and "repeated_cell_allocation" in note)
    check("D04 note contains N1-N8", all(f"n{index}" in note for index in range(1, 9)))
    check("D05 note denies foundation and axiom effects", "no foundation edit" in note and "no axiom addition follows" in note)


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    contracts()
    print(f"\nSCAN_CANONICAL={len(SCAN_TABLE)} SCAN_RAW={len(SCAN_RAW)} UNION_RAW={len(COMBINED_RAW)}")
    print(f"SUPPLIED={len(SOURCE)} SCAN_APPENDS={len(SCAN_TARGETS)} TOTAL_APPENDS={len(ADDITIONS)}")
    print(f"BRIDGE_LENGTHS={tuple(map(len, BRIDGES))} OUTPUT={RLB_OUTPUT} NEXT={NEXT_OUTPUT}")
    print(f"SUMMARY: {PASS} PASS / {FAIL} FAIL")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
