#!/usr/bin/env python3
"""Cycle 117: grow the physical R_B10 word and its completion token.

Cycle 115 ends at a generated ``R_B10`` role port.  This runner keeps that
role record intact and consumes it contextually to grow the literal physical
word ``10010011``.  Eight new strict-nearest-neighbour rows write the data
bits.  Two intermediate cage records are inherited images of already-live
rows, not new table content.  One final row joins the two last writer branches
at a fresh ``R_B10`` completion record.

All Cycle-109, Cycle-112, and Cycle-115 rows remain live.  Every reachable
append order is exhausted from the exact 264-record Cycle-100 terminal.

Authority: none.  No foundation, registry, queue, policy, audit, or git state
is edited or selected by this runner.
"""

from __future__ import annotations

from collections import deque
from pathlib import Path

import first_autonomous_successor_role_port_cycle115_2026_07_15 as c115


ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / "docs" / "work_history" / "repo" / "review_feedback"
NOTE = REVIEW / "R_B10_PORT_TO_ZERO_SOURCE_WORD_COMPLETION_CYCLE117_NOTE_2026-07-15.md"

c112 = c115.c112
c109 = c115.c109
c105 = c115.c105
c101 = c115.c101
c100 = c115.c100
c53 = c115.c53
c59 = c115.c59

Coord = c115.Coord
Signature = c115.Signature
RawTable = c115.RawTable
H0 = c115.H0
H1 = c115.H1
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


def add_canonical(
    table: dict[Signature, str],
    records: dict[Coord, str],
    site: Coord,
    output: str,
) -> None:
    local = c53.local_signature(records, site)
    canonical = c53.canonical_signature(local)
    prior = table.get(canonical)
    if prior is not None and prior != output:
        raise ValueError((canonical, prior, output))
    table[canonical] = output


# The port remains a role record.  D0 forms beside it, so the generated port
# is a contextual parent rather than a data cell whose content is overwritten.
DATA_WORD = (1, 0, 0, 1, 0, 0, 1, 1)
DATA_SITES: tuple[Coord, ...] = (
    (5, 2, 1),
    (5, 1, 0),
    (5, 0, 0),
    (5, -1, 0),
    (5, -1, -1),
    (4, -1, -1),
    (4, -1, -2),
    (4, 0, -1),
)
DATA_OUTPUTS = tuple(H1 if bit else H0 for bit in DATA_WORD)
DATA_RECORDS = tuple(zip(DATA_SITES, DATA_OUTPUTS))

# These are forced images of pre-Cycle-117 raw rows.  X0 cages the D0/D1
# turn; X1 cages the D4/D5/D7 turn.  Neither consumes a new canonical row.
X0: Coord = (5, 2, 0)
X0_OUTPUT = "TZ"
X1: Coord = (5, 0, -1)
X1_OUTPUT = H1
INHERITED_OUTPUTS: dict[Coord, str] = {
    X0: X0_OUTPUT,
    X1: X1_OUTPUT,
}

COMPLETION: Coord = (4, 0, -2)
COMPLETION_OUTPUT = "R_B10"


def build_writer_table() -> dict[Signature, str]:
    records = c115.positive_terminal_records()
    table: dict[Signature, str] = {}
    for index, (site, output) in enumerate(DATA_RECORDS):
        add_canonical(table, records, site, output)
        records[site] = output
        if index == 0:
            records[X0] = X0_OUTPUT
        if index == 4:
            records[X1] = X1_OUTPUT
    return table


def writer_terminal_records() -> dict[Coord, str]:
    return {
        **c115.positive_terminal_records(),
        **dict(DATA_RECORDS),
        **INHERITED_OUTPUTS,
    }


def build_completion_table() -> dict[Signature, str]:
    records = writer_terminal_records()
    table: dict[Signature, str] = {}
    add_canonical(table, records, COMPLETION, COMPLETION_OUTPUT)
    return table


WRITER_TABLE = build_writer_table()
WRITER_RAW = c59.raw_rule_outputs(WRITER_TABLE)
COMPLETION_TABLE = build_completion_table()
COMPLETION_RAW = c59.raw_rule_outputs(COMPLETION_TABLE)
FULL_RAW = c112.merge_raw(c115.FULL_RAW, WRITER_RAW, COMPLETION_RAW)

WRITER_OUTPUTS = dict(DATA_RECORDS)
COMPLETION_OUTPUTS = {COMPLETION: COMPLETION_OUTPUT}
EXTENSION_OUTPUTS: dict[Coord, str] = {
    **WRITER_OUTPUTS,
    **INHERITED_OUTPUTS,
    **COMPLETION_OUTPUTS,
}
GROWN_OUTPUTS: dict[Coord, str] = {
    **c115.GROWN_OUTPUTS,
    **EXTENSION_OUTPUTS,
}


def enabled(
    records: dict[Coord, str],
    raw: RawTable = FULL_RAW,
) -> dict[Coord, frozenset[str]]:
    return {
        target: raw[local]
        for target in c53.open_candidates(records)
        if (local := c53.local_signature(records, target)) in raw
    }


POSITIVE = c112.append_graph(
    source=c112.SOURCE,
    outputs=GROWN_OUTPUTS,
    raw=FULL_RAW,
)
ALL_GROWN_MASK = (1 << len(GROWN_OUTPUTS)) - 1


def positive_terminal_records() -> dict[Coord, str]:
    if POSITIVE.terminal_states != (ALL_GROWN_MASK,):
        raise RuntimeError(POSITIVE.terminal_states)
    return c112.records_at(
        ALL_GROWN_MASK,
        c112.SOURCE,
        GROWN_OUTPUTS,
    )


def completion_barrier_violations() -> tuple[int, ...]:
    """Exhaust the same graph while checking the new eight-bit barrier."""
    compiled = c112.compile_conditions(
        c112.SOURCE,
        GROWN_OUTPUTS,
        FULL_RAW,
        c112.RAIL_ZERO,
    )
    actions = tuple(
        (compiled.index.get(target), target, conditions)
        for target, conditions in compiled.conditions.items()
    )
    required_mask = sum(1 << compiled.index[site] for site in DATA_SITES)
    completion_index = compiled.index[COMPLETION]
    queue = deque((0,))
    seen = {0}
    violations: list[int] = []

    while queue:
        state = queue.popleft()
        if (
            state >> completion_index & 1
            and state & required_mask != required_mask
        ):
            violations.append(state)

        legal: list[int] = []
        for index, target, conditions in actions:
            if index is not None and state >> index & 1:
                continue
            for present_mask, neighbourhood_mask, values in conditions:
                if state & neighbourhood_mask != present_mask:
                    continue
                if target in c112.RAIL_ZERO and values == c112.RAIL_ZERO[target]:
                    break
                if (
                    index is not None
                    and values == frozenset((GROWN_OUTPUTS[target],))
                ):
                    legal.append(index)
                    break
                raise RuntimeError((state, target, values))

        for index in legal:
            future = state | 1 << index
            if future not in seen:
                seen.add(future)
                queue.append(future)
    return tuple(violations)


def append_rail(records: dict[Coord, str]) -> tuple[dict[Coord, str], tuple[object, ...]]:
    answer = dict(records)
    failures: list[object] = []
    for prefix, (site, output) in enumerate(
        c105.RAIL_SEQUENCE[: c105.RAIL_HORIZON]
    ):
        actual = enabled(answer)
        expected = {site: frozenset((output,))}
        if actual != expected:
            failures.append((prefix, expected, actual))
            break
        answer[site] = output
    if not failures and enabled(answer) != {
        c105.NEXT_RAIL[0]: frozenset((c105.NEXT_RAIL[1],))
    }:
        failures.append((c105.RAIL_HORIZON, enabled(answer)))
    return answer, tuple(failures)


def table_contract() -> None:
    section("A - R_B10 physical writer, inherited cages, and completion row")
    check("A01 Cycle 117 note exists", NOTE.is_file())
    check(
        "A02 writer is eight canonical / 192 proper-cubic raw rows",
        len(WRITER_TABLE) == 8
        and len(WRITER_RAW) == 192
        and all(len(values) == 1 for values in WRITER_RAW.values()),
        f"canonical={len(WRITER_TABLE)} raw={len(WRITER_RAW)}",
    )
    check(
        "A03 completion is one canonical / 24 raw rows",
        len(COMPLETION_TABLE) == 1
        and len(COMPLETION_RAW) == 24
        and set(WRITER_RAW).isdisjoint(COMPLETION_RAW),
        f"canonical={len(COMPLETION_TABLE)} raw={len(COMPLETION_RAW)}",
    )
    check(
        "A04 new raw domains are disjoint from Cycle 115",
        not (set(c115.FULL_RAW) & (set(WRITER_RAW) | set(COMPLETION_RAW))),
    )
    check(
        "A05 complete 8,312-row union is single-valued and alphabet-closed",
        len(FULL_RAW) == 8_312
        and all(len(values) == 1 for values in FULL_RAW.values())
        and {
            content
            for local, values in FULL_RAW.items()
            for content in [
                *(value for _direction, value in local),
                *values,
            ]
        }
        <= c105.c89.FULL_ROLES,
    )
    check(
        "A06 extension adds zero supplied records to the exact 264 boundary",
        len(c112.SOURCE) == 264
        and set(EXTENSION_OUTPUTS).isdisjoint(c112.SOURCE),
    )

    records = c115.positive_terminal_records()
    d0 = DATA_SITES[0]
    records[d0] = DATA_OUTPUTS[0]
    x0_local = c53.local_signature(records, X0)
    x0_values = c115.FULL_RAW.get(x0_local)

    records[X0] = X0_OUTPUT
    for site, output in DATA_RECORDS[1:5]:
        records[site] = output
    x1_local = c53.local_signature(records, X1)
    x1_values = c115.FULL_RAW.get(x1_local)
    check(
        "A07 X0=TZ and X1=H1 are inherited images, not new rows",
        x0_values == frozenset((X0_OUTPUT,))
        and x1_values == frozenset((X1_OUTPUT,))
        and x0_local not in WRITER_RAW
        and x1_local not in WRITER_RAW,
        f"X0={x0_local}->{x0_values} X1={x1_local}->{x1_values}",
    )

    terminal = writer_terminal_records()
    decoded = tuple(1 if terminal[site] == H1 else 0 for site in DATA_SITES)
    check(
        "A08 eight physical records decode literal R_B10=10010011",
        decoded == DATA_WORD,
        str(decoded),
    )
    completion_local = c53.local_signature(terminal, COMPLETION)
    check(
        "A09 completion is the common join of D6, D7, S8, and L5",
        completion_local
        == (
            ((-1, 0, 0), "S8"),
            ((0, -1, 0), H1),
            ((0, 0, -1), "L5"),
            ((0, 0, 1), H1),
        ),
        str(completion_local),
    )


def graph_contract() -> None:
    section("B - All-current-rows asynchronous exhaustion and exact barrier")
    check(
        "B01 variable corpus is 71 inherited plus 11 Cycle-117 writes",
        len(c115.GROWN_OUTPUTS) == 71
        and len(EXTENSION_OUTPUTS) == 11
        and len(GROWN_OUTPUTS) == 82,
    )
    check(
        "B02 every compiled local subset has zero unexpected target",
        not POSITIVE.unexpected_condition_targets,
        str(POSITIVE.unexpected_condition_targets),
    )
    check(
        "B03 all schedules reach one complete 82-write terminal",
        POSITIVE.states == 76_056
        and POSITIVE.edges == 441_682
        and POSITIVE.terminals == 1
        and POSITIVE.terminal_states == (ALL_GROWN_MASK,)
        and POSITIVE.terminal_sizes == (82,)
        and POSITIVE.max_frontier == 11
        and not POSITIVE.bad,
        f"states={POSITIVE.states} edges={POSITIVE.edges} terminals={POSITIVE.terminals} max={POSITIVE.max_frontier}",
    )
    violations = completion_barrier_violations()
    check(
        "B04 no reachable completion precedes any of the eight R_B10 bits",
        not violations,
        str(violations[:1]),
    )
    check(
        "B05 inherited Cycle-112 completion barrier also remains exact",
        not POSITIVE.completion_violations,
        str(POSITIVE.completion_violations[:1]),
    )
    terminal = positive_terminal_records()
    check(
        "B06 terminal carries word, both cages, and fresh R_B10 completion",
        all(terminal.get(site) == output for site, output in DATA_RECORDS)
        and all(
            terminal.get(site) == output
            for site, output in INHERITED_OUTPUTS.items()
        )
        and terminal.get(COMPLETION) == COMPLETION_OUTPUT,
    )
    check(
        "B07 completed writer leaves only the repaired-rail frontier",
        enabled(terminal) == c112.RAIL_ZERO,
        str(enabled(terminal)),
    )


def rail_contract() -> None:
    section("C - 96-prefix product, late rail, and covariance")
    records, failures = append_rail(positive_terminal_records())
    check(
        "C01 all 96 rail appends remain exact singleton fronts",
        not failures,
        str(failures[:1]),
    )

    new_raw = c112.merge_raw(WRITER_RAW, COMPLETION_RAW)
    rail_only = dict(c112.SOURCE)
    alias_hits = []
    for prefix in range(c105.RAIL_HORIZON + 1):
        for target in c53.open_candidates(rail_only):
            local = c53.local_signature(rail_only, target)
            if local in new_raw and local not in c115.FULL_RAW:
                alias_hits.append((prefix, target, local))
        if prefix < c105.RAIL_HORIZON:
            site, output = c105.RAIL_SEQUENCE[prefix]
            rail_only[site] = output
    new_sites = set(EXTENSION_OUTPUTS)
    rail_sites = {
        site for site, _output in c105.RAIL_SEQUENCE[: c105.RAIL_HORIZON]
    }
    distance = min(
        c101.manhattan(left, right)
        for left in new_sites
        for right in rail_sites
    )
    check(
        "C02 Cycle-117 support is rail-separated with zero 97-prefix aliases",
        distance >= 7 and not alias_hits,
        f"distance={distance} hits={alias_hits[:1]}",
    )

    product_states = POSITIVE.states * (c105.RAIL_HORIZON + 1)
    product_edges = (
        POSITIVE.edges * (c105.RAIL_HORIZON + 1)
        + POSITIVE.states * c105.RAIL_HORIZON
    )
    check(
        "C03 exact locality product is 7,377,432 states / 50,144,530 edges",
        product_states == 7_377_432 and product_edges == 50_144_530,
        f"states={product_states} edges={product_edges}",
    )

    long_rail = c105.c108.c104.rail_sequence(102, c105.ROLE_MAP)
    late = positive_terminal_records()
    late_failures = []
    for prefix, (site, output) in enumerate(long_rail[: 101 * 12]):
        actual = enabled(late)
        expected = {site: frozenset((output,))}
        if actual != expected:
            late_failures.append((prefix, expected, actual))
            break
        late[site] = output
    next_site, next_output = long_rail[101 * 12]
    check(
        "C04 late control grows 101 complete slices / 1,212 records",
        not late_failures
        and len(late) == 1_558
        and enabled(late) == {next_site: frozenset((next_output,))},
        str(late_failures[:1]),
    )

    covariance_failures = []
    controls = 0
    for local, values in FULL_RAW.items():
        for rotation in c53.ROTATIONS:
            controls += 1
            actual = FULL_RAW.get(c53.rotate_signature(local, rotation))
            if actual != values:
                covariance_failures.append((local, rotation, values, actual))
                break
    check(
        "C05 all 199,488 proper-cubic raw images preserve output",
        controls == len(FULL_RAW) * 24 == 199_488
        and not covariance_failures,
        str(covariance_failures[:1]),
    )

    shift = (181, -113, 97)
    rotated_failures = []
    for rotation in c53.ROTATIONS:
        transformed = c105.transform_records(records, rotation, shift)
        next_site = c101.transform_site(c105.NEXT_RAIL[0], rotation, shift)
        expected = {next_site: frozenset((c105.NEXT_RAIL[1],))}
        actual = enabled(transformed)
        if actual != expected:
            rotated_failures.append((rotation, expected, actual))
            break
    check(
        "C06 every rotated completed history exposes only rotated next rail",
        not rotated_failures,
        str(rotated_failures[:1]),
    )


def corruption_contract() -> None:
    section("D - Wrong-word, VALID/READY, and typed-H0 controls")
    failures = []
    observed = []
    new_sites = set(EXTENSION_OUTPUTS)
    for index, site in enumerate(c100.CODE_SITES):
        source = dict(c112.SOURCE)
        source[site] = H0 if source[site] == H1 else H1
        outputs = dict(GROWN_OUTPUTS)
        if index == 5:
            outputs[c101.BIT5_REJECT] = H1
        stats = c112.append_graph(source, outputs, raw=FULL_RAW)
        observed.append((stats.states, stats.edges, stats.terminal_sizes))
        if (
            stats.terminals != 1
            or stats.bad
            or new_sites & stats.reached
        ):
            failures.append((f"bit-{index}", stats))
    for label, site in (("valid", c100.VALID), ("ready", c100.READY)):
        source = dict(c112.SOURCE)
        source[site] = H0
        stats = c112.append_graph(source, GROWN_OUTPUTS, raw=FULL_RAW)
        observed.append((stats.states, stats.edges, stats.terminal_sizes))
        if (
            stats.terminals != 1
            or stats.bad
            or new_sites & stats.reached
        ):
            failures.append((label, stats))
    expected = [
        (1_080, 3_522, (30,)),
        (920, 2_938, (29,)),
        (760, 2_354, (28,)),
        (520, 1_438, (27,)),
        (120, 238, (20,)),
        (200, 490, (20,)),
        (80, 152, (18,)),
        (60, 109, (17,)),
        (40, 66, (16,)),
        (20, 23, (15,)),
    ]
    check(
        "D01 all eight flips plus wrong VALID/READY stop before Cycle 117",
        not failures,
        str(failures[:1]),
    )
    check("D02 corrupted graph census remains pinned", observed == expected, str(observed))

    fault_source = c109.fault_records(3)
    fault_outputs = {
        site: output
        for site, output in {
            **c112.EXTENSION_OUTPUTS,
            **c115.SUCCESSOR_OUTPUTS,
            **EXTENSION_OUTPUTS,
        }.items()
        if site not in fault_source
    }
    fault_outputs[c112.GUARD_SPINE[1]] = H1
    fault_outputs[c112.GUARD_SPINE[2]] = H1
    fault_stats = c112.append_graph(
        fault_source,
        fault_outputs,
        raw=FULL_RAW,
    )
    check(
        "D03 exhausted typed-H0 alternate reaches no Cycle-117 record",
        fault_stats.states == 44
        and fault_stats.edges == 97
        and fault_stats.terminals == 2
        and fault_stats.terminal_sizes == (6, 7)
        and not fault_stats.bad
        and not (new_sites & fault_stats.reached),
        f"states={fault_stats.states} edges={fault_stats.edges} sizes={fault_stats.terminal_sizes} bad={fault_stats.bad[:1]} reached={sorted(new_sites & fault_stats.reached)}",
    )


def scope_contract() -> None:
    section("E - Scope and no-go-discipline boundary")
    note = NOTE.read_text(encoding="utf-8").lower() if NOTE.is_file() else ""
    check(
        "E01 note names exact bounded positive",
        "r_b10_port_to_zero_source_word_and_completion" in note,
    )
    check(
        "E02 note names exact next object",
        "r_b10_completion_to_r_b00_role_allocator_common_port" in note,
    )
    check(
        "E03 note states Cycle 116 contributes zero rows",
        "cycle 116 contributes zero rows" in note,
    )
    check(
        "E04 note carries refreshed N1-N8 discipline",
        all(f"n{index}" in note for index in range(1, 9)),
    )
    check(
        "E05 note denies generic addressability and unbounded recurrence",
        "does not establish generic candidate-selectable addressability" in note
        and "does not establish unbounded recurrence" in note,
    )
    check("E06 note makes no axiom addition", "no axiom addition follows" in note)
    check(
        "E07 Cycle 117 writes only runner and review note",
        all(path.parent in (ROOT / "scripts", REVIEW) for path in (Path(__file__), NOTE)),
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    table_contract()
    graph_contract()
    rail_contract()
    corruption_contract()
    scope_contract()
    product_states = POSITIVE.states * (c105.RAIL_HORIZON + 1)
    product_edges = (
        POSITIVE.edges * (c105.RAIL_HORIZON + 1)
        + POSITIVE.states * c105.RAIL_HORIZON
    )
    print(
        f"\nWRITER_CANONICAL={len(WRITER_TABLE)} WRITER_RAW={len(WRITER_RAW)} "
        f"INHERITED={len(INHERITED_OUTPUTS)} "
        f"COMPLETION_CANONICAL={len(COMPLETION_TABLE)} "
        f"COMPLETION_RAW={len(COMPLETION_RAW)}"
    )
    print(
        f"GROWN={len(GROWN_OUTPUTS)} UNION_RAW={len(FULL_RAW)} "
        f"LOCAL_STATES={POSITIVE.states} LOCAL_EDGES={POSITIVE.edges}"
    )
    print(f"PRODUCT_STATES={product_states} PRODUCT_EDGES={product_edges}")
    print(f"PASS={PASS} FAIL={FAIL}")
    print(
        "RESULT=R_B10_PORT_TO_ZERO_SOURCE_WORD_AND_COMPLETION"
        if FAIL == 0
        else "RESULT=FAIL"
    )
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
