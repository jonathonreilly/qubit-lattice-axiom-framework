#!/usr/bin/env python3
"""Cycle 119: grow an R_B00 allocator and common role port from Cycle 117.

Cycle 117 ends with a fresh physical ``R_B10`` completion record.  This runner
adds three strict-nearest-neighbour rows: a contextual H0 guard, a fresh
``R_A00`` allocator, and an ``R_B00`` port that requires both the allocator and
the Cycle-117 completion.  No record is supplied at the new interface.

All prior rows remain live.  Every reachable append order is exhausted from
the exact 264-record Cycle-100 terminal.

Authority: none.  No foundation, registry, queue, policy, audit, or git state
is edited or selected by this runner.
"""

from __future__ import annotations

from collections import deque
from pathlib import Path

import r_b10_port_to_zero_source_word_completion_cycle117_2026_07_15 as c117


ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / "docs" / "work_history" / "repo" / "review_feedback"
NOTE = REVIEW / "R_B10_COMPLETION_TO_R_B00_ROLE_ALLOCATOR_COMMON_PORT_CYCLE119_NOTE_2026-07-15.md"

c115 = c117.c115
c112 = c117.c112
c109 = c117.c109
c105 = c117.c105
c101 = c117.c101
c100 = c117.c100
c53 = c117.c53
c59 = c117.c59

Coord = c117.Coord
Signature = c117.Signature
RawTable = c117.RawTable
H0 = c117.H0
H1 = c117.H1
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


GUARD: Coord = (3, 2, -2)
GUARD_OUTPUT = H0
ALLOCATOR: Coord = (3, 1, -2)
ALLOCATOR_OUTPUT = "R_A00"
PORT: Coord = (4, 1, -2)
PORT_OUTPUT = "R_B00"
ADAPTER_RECORDS = (
    (GUARD, GUARD_OUTPUT),
    (ALLOCATOR, ALLOCATOR_OUTPUT),
    (PORT, PORT_OUTPUT),
)


def build_adapter_table() -> dict[Signature, str]:
    records = c117.positive_terminal_records()
    table: dict[Signature, str] = {}
    for site, output in ADAPTER_RECORDS:
        add_canonical(table, records, site, output)
        records[site] = output
    return table


ADAPTER_TABLE = build_adapter_table()
ADAPTER_RAW = c59.raw_rule_outputs(ADAPTER_TABLE)
FULL_RAW = c112.merge_raw(c117.FULL_RAW, ADAPTER_RAW)
ADAPTER_OUTPUTS = dict(ADAPTER_RECORDS)
GROWN_OUTPUTS: dict[Coord, str] = {
    **c117.GROWN_OUTPUTS,
    **ADAPTER_OUTPUTS,
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


def ordering_violations() -> tuple[tuple[str, int], ...]:
    """Exhaust the exact graph and check the guard/allocator/port order."""
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
    guard_bit = 1 << compiled.index[GUARD]
    allocator_bit = 1 << compiled.index[ALLOCATOR]
    port_bit = 1 << compiled.index[PORT]
    completion_bit = 1 << compiled.index[c117.COMPLETION]
    word_mask = sum(1 << compiled.index[site] for site in c117.DATA_SITES)
    queue = deque((0,))
    seen = {0}
    violations: list[tuple[str, int]] = []

    while queue:
        state = queue.popleft()
        if state & allocator_bit and not state & guard_bit:
            violations.append(("allocator-before-guard", state))
        if state & port_bit:
            required = guard_bit | allocator_bit | completion_bit | word_mask
            if state & required != required:
                violations.append(("port-before-prerequisite", state))

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
    section("A - Exact guard, allocator, and R_B00 port")
    check("A01 Cycle 119 note exists", NOTE.is_file())
    check(
        "A02 adapter is three canonical / 72 proper-cubic raw rows",
        len(ADAPTER_TABLE) == 3
        and len(ADAPTER_RAW) == 72
        and all(len(values) == 1 for values in ADAPTER_RAW.values()),
        f"canonical={len(ADAPTER_TABLE)} raw={len(ADAPTER_RAW)}",
    )
    check(
        "A03 adapter raw domain is disjoint from Cycle 117",
        not (set(c117.FULL_RAW) & set(ADAPTER_RAW)),
    )
    check(
        "A04 complete 8,384-row union is single-valued and alphabet-closed",
        len(FULL_RAW) == 8_384
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
        "A05 extension adds zero supplied records to the exact 264 boundary",
        len(c112.SOURCE) == 264
        and set(ADAPTER_OUTPUTS).isdisjoint(c112.SOURCE),
    )

    records = c117.positive_terminal_records()
    guard_local = c53.local_signature(records, GUARD)
    records[GUARD] = GUARD_OUTPUT
    allocator_local = c53.local_signature(records, ALLOCATOR)
    records[ALLOCATOR] = ALLOCATOR_OUTPUT
    port_local = c53.local_signature(records, PORT)
    check(
        "A06 guard sees exactly L10, T_H0, and T_H2",
        guard_local
        == (
            ((-1, 0, 0), "L10"),
            ((0, 0, 1), "T_H0"),
            ((0, 1, 0), "T_H2"),
        ),
        str(guard_local),
    )
    check(
        "A07 allocator sees exactly S8, L7, GY, and the fresh H0 guard",
        allocator_local
        == (
            ((0, -1, 0), "S8"),
            ((0, 0, -1), "L7"),
            ((0, 0, 1), "GY"),
            ((0, 1, 0), H0),
        ),
        str(allocator_local),
    )
    check(
        "A08 R_B00 port sees R_A00, R_B10 completion, and L6",
        port_local
        == (
            ((-1, 0, 0), "R_A00"),
            ((0, -1, 0), "R_B10"),
            ((0, 0, -1), "L6"),
        ),
        str(port_local),
    )


def graph_contract() -> None:
    section("B - Full-history graph and exact prerequisite order")
    check(
        "B01 variable corpus is 82 inherited plus three adapter writes",
        len(c117.GROWN_OUTPUTS) == 82
        and len(ADAPTER_OUTPUTS) == 3
        and len(GROWN_OUTPUTS) == 85,
    )
    check(
        "B02 every compiled local subset has zero unexpected target",
        not POSITIVE.unexpected_condition_targets,
        str(POSITIVE.unexpected_condition_targets),
    )
    check(
        "B03 all schedules reach one complete 85-write terminal",
        POSITIVE.states == 228_296
        and POSITIVE.edges == 1_477_702
        and POSITIVE.terminals == 1
        and POSITIVE.terminal_states == (ALL_GROWN_MASK,)
        and POSITIVE.terminal_sizes == (85,)
        and POSITIVE.max_frontier == 12
        and not POSITIVE.bad,
        f"states={POSITIVE.states} edges={POSITIVE.edges} terminals={POSITIVE.terminals} max={POSITIVE.max_frontier}",
    )
    violations = ordering_violations()
    check(
        "B04 allocator never precedes guard; port never precedes full R_B10 completion",
        not violations,
        str(violations[:1]),
    )
    check(
        "B05 inherited Cycle-112 completion barrier remains exact",
        not POSITIVE.completion_violations,
        str(POSITIVE.completion_violations[:1]),
    )
    terminal = positive_terminal_records()
    check(
        "B06 terminal contains guard, fresh R_A00, and fresh R_B00 port",
        all(terminal.get(site) == output for site, output in ADAPTER_RECORDS),
    )
    check(
        "B07 completed adapter leaves only the repaired-rail frontier",
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

    rail_only = dict(c112.SOURCE)
    alias_hits = []
    for prefix in range(c105.RAIL_HORIZON + 1):
        for target in c53.open_candidates(rail_only):
            local = c53.local_signature(rail_only, target)
            if local in ADAPTER_RAW and local not in c117.FULL_RAW:
                alias_hits.append((prefix, target, local))
        if prefix < c105.RAIL_HORIZON:
            site, output = c105.RAIL_SEQUENCE[prefix]
            rail_only[site] = output
    rail_sites = {
        site for site, _output in c105.RAIL_SEQUENCE[: c105.RAIL_HORIZON]
    }
    distance = min(
        c101.manhattan(left, right)
        for left in ADAPTER_OUTPUTS
        for right in rail_sites
    )
    intended_guard_hits = (
        len(alias_hits) == c105.RAIL_HORIZON + 1
        and {prefix for prefix, _target, _local in alias_hits}
        == set(range(c105.RAIL_HORIZON + 1))
        and all(target == GUARD for _prefix, target, _local in alias_hits)
    )
    check(
        "C02 rail-only prefixes expose only the intended preallocated guard",
        distance >= 7 and intended_guard_hits,
        f"distance={distance} hits={len(alias_hits)} targets={sorted({target for _prefix, target, _local in alias_hits})}",
    )

    product_states = POSITIVE.states * (c105.RAIL_HORIZON + 1)
    product_edges = (
        POSITIVE.edges * (c105.RAIL_HORIZON + 1)
        + POSITIVE.states * c105.RAIL_HORIZON
    )
    check(
        "C03 exact locality product is 22,144,712 states / 165,253,510 edges",
        product_states == 22_144_712 and product_edges == 165_253_510,
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
        and len(late) == 1_561
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
        "C05 all 201,216 proper-cubic raw images preserve output",
        controls == len(FULL_RAW) * 24 == 201_216
        and not covariance_failures,
        str(covariance_failures[:1]),
    )

    shift = (191, -127, 101)
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
    preallocated = {GUARD, ALLOCATOR}
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
            or PORT in stats.reached
            or set(ADAPTER_OUTPUTS) & stats.reached != preallocated
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
            or PORT in stats.reached
            or set(ADAPTER_OUTPUTS) & stats.reached != preallocated
        ):
            failures.append((label, stats))
    expected = [
        (3_240, 12_726, (32,)),
        (2_760, 10_654, (31,)),
        (2_280, 8_582, (30,)),
        (1_560, 5_354, (29,)),
        (360, 954, (22,)),
        (600, 1_870, (22,)),
        (240, 616, (20,)),
        (180, 447, (19,)),
        (120, 278, (18,)),
        (60, 109, (17,)),
    ]
    check(
        "D01 all corrupt boundaries grow only guard/allocator and stop before R_B00",
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
            **c117.EXTENSION_OUTPUTS,
            **ADAPTER_OUTPUTS,
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
        "D03 typed-H0 grows only guard/allocator and never reaches R_B00",
        fault_stats.states == 132
        and fault_stats.edges == 379
        and fault_stats.terminals == 2
        and fault_stats.terminal_sizes == (8, 9)
        and not fault_stats.bad
        and set(ADAPTER_OUTPUTS) & fault_stats.reached == preallocated,
        f"states={fault_stats.states} edges={fault_stats.edges} sizes={fault_stats.terminal_sizes} bad={fault_stats.bad[:1]} reached={sorted(set(ADAPTER_OUTPUTS) & fault_stats.reached)}",
    )


def scope_contract() -> None:
    section("E - Scope and no-go-discipline boundary")
    note = NOTE.read_text(encoding="utf-8").lower() if NOTE.is_file() else ""
    check(
        "E01 note names exact bounded positive",
        "r_b10_completion_to_r_b00_role_allocator_common_port" in note,
    )
    check(
        "E02 note names exact next object",
        "r_b00_port_to_zero_source_word_and_completion" in note,
    )
    check(
        "E03 note states Cycle 118 contributes zero rows",
        "cycle 118 contributes zero rows" in note,
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
        "E07 Cycle 119 writes only runner and review note",
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
        f"\nADAPTER_CANONICAL={len(ADAPTER_TABLE)} "
        f"ADAPTER_RAW={len(ADAPTER_RAW)} UNION_RAW={len(FULL_RAW)}"
    )
    print(
        f"GROWN={len(GROWN_OUTPUTS)} LOCAL_STATES={POSITIVE.states} "
        f"LOCAL_EDGES={POSITIVE.edges}"
    )
    print(f"PRODUCT_STATES={product_states} PRODUCT_EDGES={product_edges}")
    print(f"PASS={PASS} FAIL={FAIL}")
    print(
        "RESULT=R_B10_COMPLETION_TO_R_B00_ROLE_ALLOCATOR_COMMON_PORT"
        if FAIL == 0
        else "RESULT=FAIL"
    )
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
