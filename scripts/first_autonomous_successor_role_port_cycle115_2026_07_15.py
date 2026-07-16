#!/usr/bin/env python3
"""Cycle 115: first zero-source successor role port after Cycle 112.

Cycle 112 ends with a fresh R_B11 completion record but does not consume it.
This runner adds two canonical strict-nearest-neighbour rows.  The first grows
a fresh R_A10 allocator from two completed-writer records.  The second consumes
that allocator, the completed R_B11 record, and an already-written H0 address
record to write R_B10 at one common open port.

All Cycle-109 and Cycle-112 rows remain live.  Every reachable append order is
exhausted from the exact 264-record Cycle-100 terminal.  The result is one
bounded successor-role port, not the R_B10 word writer, a repeated allocator,
or a selected exact physical law.

Authority: none.  No foundation, registry, queue, policy, audit, or git state
is edited or selected by this runner.
"""

from __future__ import annotations

from pathlib import Path

import eight_bit_status_completion_front_cycle112_2026_07_15 as c112


ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / "docs" / "work_history" / "repo" / "review_feedback"
NOTE = REVIEW / "FIRST_AUTONOMOUS_SUCCESSOR_ROLE_PORT_CYCLE115_NOTE_2026-07-15.md"

c109 = c112.c109
c105 = c112.c105
c101 = c112.c101
c100 = c112.c100
c53 = c112.c53
c59 = c112.c59

Coord = c112.Coord
Signature = c112.Signature
RawTable = c112.RawTable
H0 = c112.H0
H1 = c112.H1
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


# The clean pair was selected by exhaustive enumeration of every open site at
# L1 distance two from Cycle 112's NEXT_FRONT.  Unlike the tempting unary
# T_G0 route, both rows have complete context and compile to zero unexpected
# targets over every local subset of the 71 variable sites.
ALLOCATOR: Coord = (5, 4, 1)
ALLOCATOR_OUTPUT = "R_A10"
SUCCESSOR_PORT: Coord = (5, 3, 1)
SUCCESSOR_OUTPUT = "R_B10"


def build_successor_table() -> dict[Signature, str]:
    records = c112.positive_terminal_records()
    table: dict[Signature, str] = {}
    add_canonical(table, records, ALLOCATOR, ALLOCATOR_OUTPUT)
    records[ALLOCATOR] = ALLOCATOR_OUTPUT
    add_canonical(table, records, SUCCESSOR_PORT, SUCCESSOR_OUTPUT)
    return table


SUCCESSOR_TABLE = build_successor_table()
SUCCESSOR_RAW = c59.raw_rule_outputs(SUCCESSOR_TABLE)
FULL_RAW = c112.merge_raw(c112.FULL_RAW, SUCCESSOR_RAW)
SUCCESSOR_OUTPUTS: dict[Coord, str] = {
    ALLOCATOR: ALLOCATOR_OUTPUT,
    SUCCESSOR_PORT: SUCCESSOR_OUTPUT,
}
GROWN_OUTPUTS: dict[Coord, str] = {
    **c112.GROWN_OUTPUTS,
    **SUCCESSOR_OUTPUTS,
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


POSITIVE = c112.append_graph(outputs=GROWN_OUTPUTS, raw=FULL_RAW)
ALL_GROWN_MASK = (1 << len(GROWN_OUTPUTS)) - 1


def positive_terminal_records() -> dict[Coord, str]:
    if POSITIVE.terminal_states != (ALL_GROWN_MASK,):
        raise RuntimeError(POSITIVE.terminal_states)
    return c112.records_at(ALL_GROWN_MASK, c112.SOURCE, GROWN_OUTPUTS)


def table_contract() -> None:
    section("A - Exact two-row successor adapter")
    check("A01 Cycle 115 note exists", NOTE.is_file())
    terminal = c112.positive_terminal_records()
    allocator_local = c53.local_signature(terminal, ALLOCATOR)
    with_allocator = dict(terminal)
    with_allocator[ALLOCATOR] = ALLOCATOR_OUTPUT
    successor_local = c53.local_signature(with_allocator, SUCCESSOR_PORT)
    check(
        "A02 allocator sees exactly D1=H0 and SIGNAL_STATUS=T_G0",
        allocator_local
        == (((-1, 0, 0), H0), ((0, 0, 1), "T_G0")),
        str(allocator_local),
    )
    check(
        "A03 successor sees D2=H0, fresh R_A10, and completed R_B11",
        successor_local
        == (
            ((-1, 0, 0), H0),
            ((0, 0, 1), "R_B11"),
            ((0, 1, 0), "R_A10"),
        ),
        str(successor_local),
    )
    check(
        "A04 adapter is two canonical / 48 proper-cubic raw rows",
        len(SUCCESSOR_TABLE) == 2
        and len(SUCCESSOR_RAW) == 48
        and all(len(values) == 1 for values in SUCCESSOR_RAW.values()),
        f"canonical={len(SUCCESSOR_TABLE)} raw={len(SUCCESSOR_RAW)}",
    )
    overlap = set(c112.FULL_RAW) & set(SUCCESSOR_RAW)
    check("A05 adapter raw domain is disjoint from Cycle 112", not overlap, str(tuple(overlap)[:1]))
    check(
        "A06 complete 8,096-row union is single-valued and alphabet-closed",
        len(FULL_RAW) == 8_096
        and all(len(values) == 1 for values in FULL_RAW.values())
        and {ALLOCATOR_OUTPUT, SUCCESSOR_OUTPUT} <= c105.c89.FULL_ROLES,
    )
    check(
        "A07 source remains exactly the 264-record Cycle-100 terminal",
        len(c112.SOURCE) == 264
        and set(SUCCESSOR_OUTPUTS).isdisjoint(c112.SOURCE),
    )


def graph_contract() -> None:
    section("B - Full-history asynchronous exhaustion")
    check(
        "B01 variable corpus is 69 inherited plus two successor writes",
        len(c112.GROWN_OUTPUTS) == 69 and len(GROWN_OUTPUTS) == 71,
    )
    check(
        "B02 every compiled local subset has zero unexpected target",
        not POSITIVE.unexpected_condition_targets,
        str(POSITIVE.unexpected_condition_targets),
    )
    check(
        "B03 all schedules reach one complete 71-write terminal",
        POSITIVE.states == 74_264
        and POSITIVE.edges == 433_682
        and POSITIVE.terminals == 1
        and POSITIVE.terminal_states == (ALL_GROWN_MASK,)
        and POSITIVE.terminal_sizes == (71,)
        and POSITIVE.max_frontier == 11
        and not POSITIVE.bad,
        f"states={POSITIVE.states} edges={POSITIVE.edges} terminals={POSITIVE.terminals} max={POSITIVE.max_frontier}",
    )
    check(
        "B04 successor never violates the Cycle-112 completion barrier",
        not POSITIVE.completion_violations,
        str(POSITIVE.completion_violations[:1]),
    )
    terminal = positive_terminal_records()
    check(
        "B05 terminal contains fresh R_A10 and the first R_B10 successor role",
        terminal.get(ALLOCATOR) == ALLOCATOR_OUTPUT
        and terminal.get(SUCCESSOR_PORT) == SUCCESSOR_OUTPUT,
    )
    check(
        "B06 completed successor leaves only the repaired-rail frontier",
        enabled(terminal) == c112.RAIL_ZERO,
        str(enabled(terminal)),
    )


def rail_and_covariance_contract() -> None:
    section("C - Rail locality, covariance, and rotated terminal")
    records = positive_terminal_records()
    failures = []
    for prefix, (site, output) in enumerate(c105.RAIL_SEQUENCE[: c105.RAIL_HORIZON]):
        actual = enabled(records)
        expected = {site: frozenset((output,))}
        if actual != expected:
            failures.append((prefix, expected, actual))
            break
        records[site] = output
    check(
        "C01 all 96 rail appends remain exact singleton fronts",
        not failures
        and enabled(records)
        == {c105.NEXT_RAIL[0]: frozenset((c105.NEXT_RAIL[1],))},
        str(failures[:1]),
    )

    new_sites = set(SUCCESSOR_OUTPUTS)
    rail_sites = {
        site for site, _output in c105.RAIL_SEQUENCE[: c105.RAIL_HORIZON]
    }
    distance = min(
        c101.manhattan(left, right)
        for left in new_sites
        for right in rail_sites
    )
    alias_hits = []
    rail_only = dict(c112.SOURCE)
    for prefix in range(c105.RAIL_HORIZON + 1):
        for target in c53.open_candidates(rail_only):
            local = c53.local_signature(rail_only, target)
            if local in SUCCESSOR_RAW:
                alias_hits.append((prefix, target, local))
        if prefix < c105.RAIL_HORIZON:
            site, output = c105.RAIL_SEQUENCE[prefix]
            rail_only[site] = output
    check(
        "C02 successor support is rail-separated with zero 97-prefix aliases",
        distance >= 7 and not alias_hits,
        f"distance={distance} hits={alias_hits[:1]}",
    )

    product_states = POSITIVE.states * (c105.RAIL_HORIZON + 1)
    product_edges = (
        POSITIVE.edges * (c105.RAIL_HORIZON + 1)
        + POSITIVE.states * c105.RAIL_HORIZON
    )
    check(
        "C03 exact 97-prefix product is 7,203,608 states / 49,196,498 edges",
        product_states == 7_203_608 and product_edges == 49_196_498,
        f"states={product_states} edges={product_edges}",
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
        "C04 all 194,304 proper-cubic raw images preserve output",
        controls == len(FULL_RAW) * 24 == 194_304
        and not covariance_failures,
        str(covariance_failures[:1]),
    )

    shift = (173, -109, 89)
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
        "C05 every rotated completed history exposes only the rotated next rail",
        not rotated_failures,
        str(rotated_failures[:1]),
    )


def corruption_contract() -> None:
    section("D - Wrong-word and H0-branch controls")
    failures = []
    observed = []
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
            or ALLOCATOR in stats.reached
            or SUCCESSOR_PORT in stats.reached
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
            or ALLOCATOR in stats.reached
            or SUCCESSOR_PORT in stats.reached
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
        "D01 all eight flips plus wrong VALID/READY stop before successor",
        not failures,
        str(failures[:1]),
    )
    check("D02 corrupted graph census remains pinned", observed == expected, str(observed))

    fault_source = c109.fault_records(3)
    fault_outputs = {
        site: output
        for site, output in {
            **c112.EXTENSION_OUTPUTS,
            **SUCCESSOR_OUTPUTS,
        }.items()
        if site not in fault_source
    }
    fault_outputs[c112.GUARD_SPINE[1]] = H1
    fault_outputs[c112.GUARD_SPINE[2]] = H1
    fault_stats = c112.append_graph(fault_source, fault_outputs, raw=FULL_RAW)
    check(
        "D03 exhausted H0 reject history never reaches allocator or successor",
        fault_stats.states == 44
        and fault_stats.edges == 97
        and fault_stats.terminals == 2
        and fault_stats.terminal_sizes == (6, 7)
        and not fault_stats.bad
        and ALLOCATOR not in fault_stats.reached
        and SUCCESSOR_PORT not in fault_stats.reached,
        f"states={fault_stats.states} edges={fault_stats.edges} sizes={fault_stats.terminal_sizes} bad={fault_stats.bad[:1]}",
    )


def scope_contract() -> None:
    section("E - Scope, N1-N8, and constitutional boundary")
    note = NOTE.read_text(encoding="utf-8").lower() if NOTE.is_file() else ""
    check("E01 note names exact bounded positive", "first_zero_source_successor_role_port" in note)
    check("E02 note names exact next object", "r_b10_port_to_zero_source_word_and_completion" in note)
    check("E03 note states Cycle 114 contributes zero rows", "cycle 114 contributes zero rows" in note)
    check("E04 note carries remote N1-N8 discipline", all(f"n{index}" in note for index in range(1, 9)))
    check("E05 note denies generic addressability", "does not establish candidate-selected common-port addressability" in note)
    check("E06 note makes no axiom addition", "no axiom addition follows" in note)
    check(
        "E07 Cycle 115 writes only runner and review note",
        all(path.parent in (ROOT / "scripts", REVIEW) for path in (Path(__file__), NOTE)),
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    table_contract()
    graph_contract()
    rail_and_covariance_contract()
    corruption_contract()
    scope_contract()
    product_states = POSITIVE.states * (c105.RAIL_HORIZON + 1)
    product_edges = (
        POSITIVE.edges * (c105.RAIL_HORIZON + 1)
        + POSITIVE.states * c105.RAIL_HORIZON
    )
    print(
        f"\nSUCCESSOR_CANONICAL={len(SUCCESSOR_TABLE)} "
        f"SUCCESSOR_RAW={len(SUCCESSOR_RAW)} UNION_RAW={len(FULL_RAW)}"
    )
    print(
        f"LOCAL_STATES={POSITIVE.states} LOCAL_EDGES={POSITIVE.edges} "
        f"PRODUCT_STATES={product_states} PRODUCT_EDGES={product_edges}"
    )
    print(f"PASS={PASS} FAIL={FAIL}")
    print("RESULT=FIRST_AUTONOMOUS_SUCCESSOR_ROLE_PORT" if FAIL == 0 else "RESULT=FAIL")
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
