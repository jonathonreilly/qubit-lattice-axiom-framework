#!/usr/bin/env python3
"""Cycle 109: status-gated typed payload handoff.

Cycle 105's generated shell and literal three-parent JOINT are retained.  Its
single unconditional JOINT -> R_B11 cap row is the one integration
substitution: a grown one-bit status now gates the same positive-z target.
Correct status writes literal R_B11; the explicit H0 fault control writes AUX
at that target and then grows Cycle 95's physical A_0_0 reject-launch role.

The exact Cycle-100 terminal remains the only initial boundary.  No Cycle-109
record is supplied.  The finite construction is schedule-exhausted, screened
against 96 required renewed-rail appends and a 101-slice late-alias control,
and rotated through every proper-cubic image.  This is a bounded one-bit
handoff, not a complete reusable 48-bit harness or unbounded compiler.

Authority: none.  No foundation, registry, queue, audit, or git state follows.
"""

from __future__ import annotations

from collections import defaultdict, deque
from dataclasses import dataclass
from pathlib import Path

import aux_gated_candidate_transport_cycle95_2026_07_15 as c95
import first_self_grown_selector_payload_bit0_cycle106_2026_07_15 as c106
import four_open_reservation_comb_cycle59_2026_07_14 as c59
import read_status_to_generated_rail_spine_cycle105_2026_07_15 as c105


ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / "docs" / "work_history" / "repo" / "review_feedback"
NOTE = REVIEW / "STATUS_GATED_TYPED_PAYLOAD_HANDOFF_CYCLE109_NOTE_2026-07-15.md"

Coord = c105.Coord
Signature = c105.Signature
RawTable = c105.RawTable
H0 = "H0"
H1 = "H1"
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


def merge_raw(*tables: RawTable) -> RawTable:
    outputs: dict[Signature, set[str]] = defaultdict(set)
    for table in tables:
        for local, values in table.items():
            outputs[local].update(values)
    return {local: frozenset(values) for local, values in outputs.items()}


def put(records: dict[Coord, str], site: Coord, output: str) -> None:
    prior = records.get(site)
    if prior is not None and prior != output:
        raise ValueError((site, prior, output))
    records[site] = output


def add_canonical(
    table: dict[Signature, str],
    records: dict[Coord, str],
    site: Coord,
    output: str,
) -> None:
    local = c105.c101.c100.c53.local_signature(records, site)
    canonical = c105.c101.c100.c53.canonical_signature(local)
    prior = table.get(canonical)
    if prior is not None and prior != output:
        raise ValueError((canonical, prior, output))
    table[canonical] = output


# ---------------------------------------------------------------------------
# Three route probes.
#
# Route 1 keeps Cycle 105 literally and asks for the smallest cap-only cage.
# Proper-cubic closure forces three equal BACKSTOP images, so the one-row
# reduction cages the cap but does not pick a direction.
#
# Route 2 is the landed construction.  It removes only the unconditional
# unary cap row, retains all seventeen shell/JOIN rows, and makes the original
# positive-z cap target depend on a physically grown comparison status.
#
# Route 3 asks whether the complete Cycle-95 law can simply be imported.  Its
# only direct conflicts remain the six rotations of unary R_LA, while the
# Cycle-95 new transport block and Cycle-93 status/final blocks are compatible.
# ---------------------------------------------------------------------------

UNARY_CAP_CANONICAL = c105.c101.c100.c53.canonical_signature(
    (((1, 0, 0), c105.JOIN_OUTPUT),)
)
SPINE_JOIN_TABLE = {
    local: output
    for local, output in c105.BRIDGE_TABLE.items()
    if local != UNARY_CAP_CANONICAL
}
SPINE_JOIN_RAW = c59.raw_rule_outputs(SPINE_JOIN_TABLE)

DIRECTED_PAYLOAD = c106.REJECT
DIRECTED_OUTPUT = c105.PAYLOAD_OUTPUT
LAUNCH = c106.LAUNCH
LAUNCH_OUTPUT = "A_0_0"


def build_harness_table() -> dict[Signature, str]:
    table: dict[Signature, str] = {}

    # Use the actual Cycle-105 completed shell/JOIN record corpus with its
    # symmetric payload images removed.  The first three Cycle-106 writes are
    # replaced by Cycle 105's AUX/BTG shell and literal JOINT; its independent
    # CAGE -> reference-guard -> reference -> status chain is retained.
    records = c105.positive_terminal_records()
    for site in c105.PAYLOAD_SITES:
        records.pop(site)

    for site, output in c106.CORRECT_NEW[3:]:
        add_canonical(table, records, site, output)
        put(records, site, output)

    # Correct status commits the typed payload at the former cap/reject site.
    add_canonical(table, records, DIRECTED_PAYLOAD, DIRECTED_OUTPUT)

    # The alternate H0 reference is an explicit typed fault control only.
    fault = c105.positive_terminal_records()
    for site in c105.PAYLOAD_SITES:
        fault.pop(site)
    for site, output in c106.CORRECT_NEW[3:5]:
        put(fault, site, output)
    put(fault, c106.REFERENCE, H0)
    for site, output in c106.WRONG_CONTROL:
        add_canonical(table, fault, site, output)
        put(fault, site, output)
    return table


HARNESS_TABLE = build_harness_table()
HARNESS_RAW = c59.raw_rule_outputs(HARNESS_TABLE)
FULL_RAW = merge_raw(c105.BASE_RAW, SPINE_JOIN_RAW, HARNESS_RAW)

CAP_CAGE_SITES: tuple[Coord, ...] = ((4, 7, 2), (5, 6, 2), (5, 7, 1))
CAP_CAGE_OUTPUT = "BACKSTOP"


def build_cap_cage_table() -> dict[Signature, str]:
    records = c105.positive_terminal_records()
    table: dict[Signature, str] = {}
    add_canonical(table, records, CAP_CAGE_SITES[0], CAP_CAGE_OUTPUT)
    return table


CAP_CAGE_TABLE = build_cap_cage_table()
CAP_CAGE_RAW = c59.raw_rule_outputs(CAP_CAGE_TABLE)
CAP_CAGE_UNION = merge_raw(c105.FULL_RAW, CAP_CAGE_RAW)


def cap_cage_graph() -> tuple[int, int, int, tuple[object, ...]]:
    queue = deque((0,))
    seen = {0}
    edges = 0
    terminals = 0
    bad: list[object] = []
    while queue:
        state = queue.popleft()
        records = c105.positive_terminal_records()
        for index, site in enumerate(CAP_CAGE_SITES):
            if state >> index & 1:
                records[site] = CAP_CAGE_OUTPUT
        actual = enabled(records, CAP_CAGE_UNION)
        legal: list[int] = []
        for target, values in actual.items():
            if target == c105.FIRST_RAIL[0] and values == RAIL_ZERO[target]:
                continue
            if target in CAP_CAGE_SITES:
                index = CAP_CAGE_SITES.index(target)
                if not state >> index & 1 and values == frozenset((CAP_CAGE_OUTPUT,)):
                    legal.append(index)
                    continue
            bad.append((state, target, values))
        if not legal:
            terminals += 1
        for index in legal:
            future = state | 1 << index
            edges += 1
            if future not in seen:
                seen.add(future)
                queue.append(future)
    return len(seen), edges, terminals, tuple(bad)


def enabled(
    records: dict[Coord, str],
    raw: RawTable = FULL_RAW,
) -> dict[Coord, frozenset[str]]:
    return {
        target: raw[local]
        for target in c105.c101.c100.c53.open_candidates(records)
        if (local := c105.c101.c100.c53.local_signature(records, target))
        in raw
    }


# ---------------------------------------------------------------------------
# Exact generic append graph.  The 46 variable records comprise Cycle 101's
# 22-record reader, inherited TYPE, seventeen shell records, JOINT, the four
# grown comparison records, and one directed typed payload.
# ---------------------------------------------------------------------------

GROWN_OUTPUTS: dict[Coord, str] = {
    **c105.c101.FRAGMENT_OUTPUTS,
    c105.NATURAL_TYPE: c105.NATURAL_TYPE_OUTPUT,
    **dict(zip(c105.PRIMARY_SPINE, c105.SPINE_OUTPUTS)),
    c105.P2_SIBLING: c105.SPINE_OUTPUTS[10],
    c105.JOIN: c105.JOIN_OUTPUT,
    **dict(c106.CORRECT_NEW[3:]),
    DIRECTED_PAYLOAD: DIRECTED_OUTPUT,
}
GROWN_SITES = tuple(sorted(GROWN_OUTPUTS))
GROWN_INDEX = {site: index for index, site in enumerate(GROWN_SITES)}
ALL_GROWN_MASK = (1 << len(GROWN_SITES)) - 1
RAIL_ZERO = {c105.FIRST_RAIL[0]: frozenset((c105.FIRST_RAIL[1],))}


def records_at(
    state: int,
    source: dict[Coord, str] | None = None,
    outputs: dict[Coord, str] = GROWN_OUTPUTS,
    sites: tuple[Coord, ...] = GROWN_SITES,
) -> dict[Coord, str]:
    records = dict(c105.c101.TERMINAL if source is None else source)
    for index, site in enumerate(sites):
        if state >> index & 1:
            records[site] = outputs[site]
    return records


@dataclass(frozen=True)
class GraphStats:
    states: int
    edges: int
    terminals: int
    terminal_states: tuple[int, ...]
    terminal_sizes: tuple[int, ...]
    max_frontier: int
    bad: tuple[object, ...]
    reached: frozenset[Coord]


def append_graph(
    source: dict[Coord, str] | None = None,
    outputs: dict[Coord, str] = GROWN_OUTPUTS,
) -> GraphStats:
    sites = tuple(sorted(outputs))
    index_of = {site: index for index, site in enumerate(sites)}
    queue = deque((0,))
    seen = {0}
    edges = 0
    terminals: list[int] = []
    bad: list[object] = []
    max_frontier = 0
    reached: set[Coord] = set()

    while queue:
        state = queue.popleft()
        records = records_at(state, source, outputs, sites)
        actual = enabled(records)
        legal: list[int] = []
        local_bad: list[object] = []
        for target, values in actual.items():
            if target == c105.FIRST_RAIL[0] and values == RAIL_ZERO[target]:
                continue
            index = index_of.get(target)
            if (
                index is not None
                and not state >> index & 1
                and values == frozenset((outputs[target],))
            ):
                legal.append(index)
            else:
                local_bad.append((state, target, values))
        if local_bad:
            bad.extend(local_bad)
            break
        max_frontier = max(max_frontier, len(legal))
        if not legal:
            terminals.append(state)
            continue
        for index in legal:
            future = state | 1 << index
            edges += 1
            reached.add(sites[index])
            if future not in seen:
                seen.add(future)
                queue.append(future)

    return GraphStats(
        states=len(seen),
        edges=edges,
        terminals=len(terminals),
        terminal_states=tuple(terminals),
        terminal_sizes=tuple(sorted({state.bit_count() for state in terminals})),
        max_frontier=max_frontier,
        bad=tuple(bad),
        reached=frozenset(reached),
    )


POSITIVE = append_graph()


def positive_terminal_records() -> dict[Coord, str]:
    if POSITIVE.terminal_states != (ALL_GROWN_MASK,):
        raise RuntimeError(POSITIVE.terminal_states)
    return records_at(ALL_GROWN_MASK)


# ---------------------------------------------------------------------------
# Contracts.
# ---------------------------------------------------------------------------

def route_and_table_contract() -> None:
    section("A - Three open routes and exact integration table")
    check("A01 note exists", NOTE.is_file())
    check(
        "A02 route 1 keeps literal Cycle-105 cap and adds one cap-cage row",
        len(CAP_CAGE_TABLE) == 1
        and set(CAP_CAGE_RAW).isdisjoint(c105.FULL_RAW)
        and all(len(values) == 1 for values in CAP_CAGE_UNION.values()),
        f"canonical={len(CAP_CAGE_TABLE)} raw={len(CAP_CAGE_RAW)}",
    )

    cap_records = c105.positive_terminal_records()
    cap_front = enabled(cap_records, CAP_CAGE_UNION)
    expected_cap = {
        **RAIL_ZERO,
        **{site: frozenset((CAP_CAGE_OUTPUT,)) for site in CAP_CAGE_SITES},
    }
    check(
        "A03 cap-only cage necessarily exposes all three proper-cubic images",
        cap_front == expected_cap,
        str(cap_front),
    )
    for site in CAP_CAGE_SITES:
        cap_records[site] = CAP_CAGE_OUTPUT
    cap_states, cap_edges, cap_terminals, cap_bad = cap_cage_graph()
    check(
        "A04 reduced literal-cap graph is exact 8-state / 12-edge and terminates with three cages",
        cap_states == 8
        and cap_edges == 12
        and cap_terminals == 1
        and not cap_bad
        and enabled(cap_records, CAP_CAGE_UNION) == RAIL_ZERO,
        f"states={cap_states} edges={cap_edges} terminals={cap_terminals} bad={cap_bad[:1]}",
    )

    check(
        "A05 route 2 retains 17 Cycle-105 shell/JOIN rows and substitutes one cap row",
        len(c105.BRIDGE_TABLE) == 18
        and len(SPINE_JOIN_TABLE) == 17
        and UNARY_CAP_CANONICAL not in SPINE_JOIN_TABLE
        and len(SPINE_JOIN_RAW) == 408,
        f"canonical={len(SPINE_JOIN_TABLE)} raw={len(SPINE_JOIN_RAW)}",
    )
    check(
        "A06 status handoff is eight canonical / 192 raw rows",
        len(HARNESS_TABLE) == 8 and len(HARNESS_RAW) == 192,
        f"canonical={len(HARNESS_TABLE)} raw={len(HARNESS_RAW)}",
    )
    pairwise_disjoint = (
        set(c105.BASE_RAW).isdisjoint(SPINE_JOIN_RAW)
        and set(c105.BASE_RAW).isdisjoint(HARNESS_RAW)
        and set(SPINE_JOIN_RAW).isdisjoint(HARNESS_RAW)
    )
    check(
        "A07 7,496-row selected union is disjoint, single-valued, and alphabet-closed",
        pairwise_disjoint
        and len(FULL_RAW) == 7_496
        and all(len(values) == 1 for values in FULL_RAW.values())
        and {
            content
            for local, values in FULL_RAW.items()
            for content in [*(value for _direction, value in local), *values]
        }
        <= c105.c89.FULL_ROLES,
    )

    conflicts = {
        local: (FULL_RAW[local], c95.COMBINED_RAW[local])
        for local in set(FULL_RAW) & set(c95.COMBINED_RAW)
        if FULL_RAW[local] != c95.COMBINED_RAW[local]
    }
    check(
        "A08 route 3 full Cycle-95 import has exactly six unary-R_LA conflicts",
        len(conflicts) == 6
        and all(len(local) == 1 and local[0][1] == "R_LA" for local in conflicts)
        and all(left == frozenset((H1,)) and right == frozenset(("R_B11",)) for left, right in conflicts.values()),
        str(conflicts),
    )
    compatible_parts = (c95.NEW_RAW, c95.c93.STATUS_RAW, c95.c93.FINAL_RAW)
    check(
        "A09 Cycle-95 new transport and Cycle-93 status/final surfaces remain literal-compatible",
        all(
            all(FULL_RAW[local] == part[local] for local in set(FULL_RAW) & set(part))
            for part in compatible_parts
        ),
    )


def constructive_contract() -> None:
    section("B - Zero-added-source status-gated typed handoff")
    check(
        "B01 initial boundary is exactly Cycle-100 terminal with zero Cycle-109 supply",
        len(c105.c101.TERMINAL) == 264
        and set(GROWN_OUTPUTS).isdisjoint(c105.c101.TERMINAL),
    )
    check(
        "B02 exact variable set has 46 grown physical records",
        len(GROWN_OUTPUTS) == 46
        and len(c105.c101.FRAGMENT_OUTPUTS) == 22
        and DIRECTED_PAYLOAD in GROWN_OUTPUTS,
        str(len(GROWN_OUTPUTS)),
    )
    before = positive_terminal_records()
    before.pop(DIRECTED_PAYLOAD)
    local = c105.c101.c100.c53.local_signature(before, DIRECTED_PAYLOAD)
    check(
        "B03 correct payload literally sees JOINT plus grown H1 status",
        dict(local) == {(-1, 0, 0): H1, (0, 0, -1): c105.JOIN_OUTPUT}
        and FULL_RAW.get(local) == frozenset((DIRECTED_OUTPUT,)),
        str(local),
    )
    check(
        "B04 correct handoff writes one directed onsite R_B11 payload",
        positive_terminal_records().get(DIRECTED_PAYLOAD) == "R_B11"
        and all(site not in positive_terminal_records() for site in c105.PAYLOAD_SITES[1:]),
    )
    check(
        "B05 every schedule reaches one complete 46-write terminal",
        POSITIVE.states == 11_320
        and POSITIVE.edges == 54_066
        and POSITIVE.terminals == 1
        and POSITIVE.terminal_sizes == (46,)
        and POSITIVE.terminal_states == (ALL_GROWN_MASK,)
        and not POSITIVE.bad
        and POSITIVE.max_frontier == 9,
        f"states={POSITIVE.states} edges={POSITIVE.edges} terminals={POSITIVE.terminals} max={POSITIVE.max_frontier}",
    )
    check(
        "B06 terminal exposes only the first repaired-rail append",
        enabled(positive_terminal_records()) == RAIL_ZERO,
        str(enabled(positive_terminal_records())),
    )


def rail_contract() -> None:
    section("C - Required rail product and 101-slice late-alias control")
    records = positive_terminal_records()
    rail_failures = []
    for prefix, (site, content) in enumerate(c105.RAIL_SEQUENCE[: c105.RAIL_HORIZON]):
        actual = enabled(records)
        expected = {site: frozenset((content,))}
        if actual != expected:
            rail_failures.append((prefix, expected, actual))
            break
        records[site] = content
    check(
        "C01 all 96 required rail appends remain exact singleton fronts",
        not rail_failures
        and enabled(records) == {c105.NEXT_RAIL[0]: frozenset((c105.NEXT_RAIL[1],))},
        str(rail_failures[:1]),
    )

    added_support = {site for site, _output in c106.CORRECT_NEW[3:]} | {
        DIRECTED_PAYLOAD
    }
    rail_sites = {site for site, _content in c105.RAIL_SEQUENCE[: c105.RAIL_HORIZON]}
    min_distance = min(
        c105.c101.manhattan(left, right)
        for left in added_support
        for right in rail_sites
    )
    new_rail_hits = []
    rail_records = dict(c105.c101.TERMINAL)
    for prefix in range(c105.RAIL_HORIZON + 1):
        for target in c105.c101.c100.c53.open_candidates(rail_records):
            local = c105.c101.c100.c53.local_signature(rail_records, target)
            if local in HARNESS_RAW:
                new_rail_hits.append((prefix, target, local))
        if prefix < c105.RAIL_HORIZON:
            site, content = c105.RAIL_SEQUENCE[prefix]
            rail_records[site] = content
    check(
        "C02 new handoff support is rail-separated and no handoff row aliases any rail prefix",
        min_distance >= 7 and not new_rail_hits,
        f"distance={min_distance} hits={new_rail_hits[:1]}",
    )
    product_states = POSITIVE.states * (c105.RAIL_HORIZON + 1)
    product_edges = (
        POSITIVE.edges * (c105.RAIL_HORIZON + 1)
        + POSITIVE.states * c105.RAIL_HORIZON
    )
    check(
        "C03 exact locality product is 1,098,040 states / 6,331,122 edges",
        product_states == 1_098_040 and product_edges == 6_331_122,
        f"states={product_states} edges={product_edges}",
    )

    long_rail = c105.c108.c104.rail_sequence(102, c105.ROLE_MAP)
    long_horizon = 101 * 12
    late = positive_terminal_records()
    late_failures = []
    for prefix, (site, content) in enumerate(long_rail[:long_horizon]):
        actual = enabled(late)
        expected = {site: frozenset((content,))}
        if actual != expected:
            late_failures.append((prefix, expected, actual))
            break
        late[site] = content
    next_site, next_content = long_rail[long_horizon]
    check(
        "C04 late-alias control grows 101 full slices / 1,212 records exactly",
        not late_failures
        and len(late) == 1_522
        and enabled(late) == {next_site: frozenset((next_content,))},
        str(late_failures[:1]),
    )


def fault_records(stage: int) -> dict[Coord, str]:
    records = positive_terminal_records()
    for site in (c106.REFERENCE, c106.STATUS, DIRECTED_PAYLOAD):
        records.pop(site)
    records[c106.REFERENCE] = H0
    if stage >= 1:
        records[c106.STATUS] = H0
    if stage >= 2:
        records[DIRECTED_PAYLOAD] = "AUX"
    if stage >= 3:
        records[LAUNCH] = LAUNCH_OUTPUT
    return records


def fault_and_corruption_contract() -> list[tuple[str, dict[Coord, str]]]:
    section("D - Exact reject launch and every literal corruption")
    fault_expected = (
        {c106.STATUS: frozenset((H0,))},
        {DIRECTED_PAYLOAD: frozenset(("AUX",))},
        {LAUNCH: frozenset((LAUNCH_OUTPUT,))},
        {},
    )
    fault_failures = []
    fault_cases: list[tuple[str, dict[Coord, str]]] = []
    for stage, expected_local in enumerate(fault_expected):
        records = fault_records(stage)
        actual = enabled(records)
        expected = {**RAIL_ZERO, **expected_local}
        if actual != expected:
            fault_failures.append((stage, expected, actual))
        fault_cases.append((f"fault-{stage}", records))
    check(
        "D01 injected H0 follows exact STATUS -> AUX -> A_0_0 reject path then quiet",
        not fault_failures,
        str(fault_failures[:1]),
    )

    compatibility_raw = merge_raw(FULL_RAW, c95.NEW_RAW, c95.c93.STATUS_RAW, c95.c93.FINAL_RAW)
    compatibility_failures = []
    for label, records in [("correct", positive_terminal_records()), *fault_cases]:
        actual = enabled(records, compatibility_raw)
        expected = enabled(records)
        if actual != expected:
            compatibility_failures.append((label, expected, actual))
    check(
        "D02 correct/reject interface is quiet under compatible Cycle-95/Cycle-93 rows",
        not compatibility_failures
        and all(len(values) == 1 for values in compatibility_raw.values()),
        str(compatibility_failures[:1]),
    )

    corrupt_cases: list[tuple[str, dict[Coord, str]]] = []
    corrupt_failures = []
    observed = []
    for index, site in enumerate(c105.c101.c100.CODE_SITES):
        source = dict(c105.c101.TERMINAL)
        source[site] = H0 if source[site] == H1 else H1
        outputs = dict(GROWN_OUTPUTS)
        if index == 5:
            outputs[c105.c101.BIT5_REJECT] = H1
        stats = append_graph(source, outputs)
        observed.append((stats.states, stats.edges, stats.terminal_sizes))
        if (
            stats.terminals != 1
            or stats.bad
            or c105.JOIN in stats.reached
            or c106.STATUS in stats.reached
            or DIRECTED_PAYLOAD in stats.reached
        ):
            corrupt_failures.append((index, stats))
        terminal = records_at(
            stats.terminal_states[0], source, outputs, tuple(sorted(outputs))
        )
        corrupt_cases.append((f"bit-{index}", terminal))

    for label, site in (("valid", c105.c101.c100.VALID), ("ready", c105.c101.c100.READY)):
        source = dict(c105.c101.TERMINAL)
        source[site] = H0
        stats = append_graph(source)
        observed.append((stats.states, stats.edges, stats.terminal_sizes))
        if (
            stats.terminals != 1
            or stats.bad
            or c105.JOIN in stats.reached
            or c106.STATUS in stats.reached
            or DIRECTED_PAYLOAD in stats.reached
        ):
            corrupt_failures.append((label, stats))
        terminal = records_at(
            stats.terminal_states[0], source, GROWN_OUTPUTS, GROWN_SITES
        )
        corrupt_cases.append((label, terminal))

    check(
        "D03 all eight word flips plus wrong VALID/READY stop before status and payload",
        len(corrupt_cases) == 10 and not corrupt_failures,
        str(corrupt_failures[:1]),
    )
    rail_failures = []
    for label, terminal in corrupt_cases:
        records = dict(terminal)
        for prefix, (site, content) in enumerate(c105.RAIL_SEQUENCE[: c105.RAIL_HORIZON]):
            actual = enabled(records)
            expected = {site: frozenset((content,))}
            if actual != expected:
                rail_failures.append((label, prefix, expected, actual))
                break
            records[site] = content
        if not rail_failures and enabled(records) != {
            c105.NEXT_RAIL[0]: frozenset((c105.NEXT_RAIL[1],))
        }:
            rail_failures.append((label, c105.RAIL_HORIZON, "next", enabled(records)))
    check(
        "D04 all ten corrupt terminals retain eight exact rail slices",
        not rail_failures,
        str(rail_failures[:1]),
    )
    expected_census = [
        (760, 2_274, (29,)),
        (680, 2_022, (28,)),
        (600, 1_770, (27,)),
        (440, 1_186, (26,)),
        (120, 238, (20,)),
        (200, 490, (20,)),
        (80, 152, (18,)),
        (60, 109, (17,)),
        (40, 66, (16,)),
        (20, 23, (15,)),
    ]
    check("D05 corrupt graph census is executable and pinned", observed == expected_census, str(observed))
    return corrupt_cases + fault_cases


def covariance_and_scope_contract(extra_cases: list[tuple[str, dict[Coord, str]]]) -> None:
    section("E - Proper-cubic covariance and bounded claim discipline")
    covariance_failures = []
    controls = 0
    for local, values in FULL_RAW.items():
        for rotation in c105.c101.c100.c53.ROTATIONS:
            controls += 1
            actual = FULL_RAW.get(c105.c101.c100.c53.rotate_signature(local, rotation))
            if actual != values:
                covariance_failures.append((local, rotation, values, actual))
    check(
        "E01 all 179,904 raw proper-cubic images preserve output",
        controls == len(FULL_RAW) * 24 == 179_904 and not covariance_failures,
        str(covariance_failures[:1]),
    )

    terminal = positive_terminal_records()
    terminal.update(dict(c105.RAIL_SEQUENCE[: c105.RAIL_HORIZON]))
    cases = [("correct", terminal)]
    for label, records in extra_cases:
        complete = dict(records)
        complete.update(dict(c105.RAIL_SEQUENCE[: c105.RAIL_HORIZON]))
        cases.append((label, complete))

    rotated_failures = []
    shift = (149, -101, 79)
    fault_fronts = {
        "fault-0": {c106.STATUS: H0},
        "fault-1": {DIRECTED_PAYLOAD: "AUX"},
        "fault-2": {LAUNCH: LAUNCH_OUTPUT},
        "fault-3": {},
    }
    for label, records in cases:
        for rotation in c105.c101.c100.c53.ROTATIONS:
            transformed = c105.transform_records(records, rotation, shift)
            next_site = c105.c101.transform_site(c105.NEXT_RAIL[0], rotation, shift)
            expected = {next_site: frozenset((c105.NEXT_RAIL[1],))}
            for site, output in fault_fronts.get(label, {}).items():
                transformed_site = c105.c101.transform_site(site, rotation, shift)
                expected[transformed_site] = frozenset((output,))
            actual = enabled(transformed)
            if actual != expected:
                rotated_failures.append((label, rotation, expected, actual))
                break
    check(
        "E02 all positive/fault/corrupt terminal rotations expose only next rail",
        len(cases) == 15 and not rotated_failures,
        str(rotated_failures[:1]),
    )

    note = NOTE.read_text(encoding="utf-8").lower() if NOTE.is_file() else ""
    check("E03 note names exact status-gated substitution", "status-gated substitution" in note)
    check("E04 note names positive reduced literal-cap cage", "positive reduced construction" in note)
    check("E05 note carries full N1-N8 discipline", all(f"n{index}" in note for index in range(1, 9)))
    check("E06 note avoids a complete reusable-harness claim", "does not close the complete reusable harness" in note)
    check("E07 note makes no axiom claim", "no axiom addition follows" in note)
    check(
        "E08 Cycle 109 writes only runner and review note",
        all(path.parent in (ROOT / "scripts", REVIEW) for path in (Path(__file__), NOTE)),
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    route_and_table_contract()
    constructive_contract()
    rail_contract()
    extra_cases = fault_and_corruption_contract()
    covariance_and_scope_contract(extra_cases)
    product_states = POSITIVE.states * (c105.RAIL_HORIZON + 1)
    product_edges = POSITIVE.edges * (c105.RAIL_HORIZON + 1) + POSITIVE.states * c105.RAIL_HORIZON
    print(
        f"\nGROWN={len(GROWN_OUTPUTS)} SPINE_JOIN_CANONICAL={len(SPINE_JOIN_TABLE)} "
        f"HANDOFF_CANONICAL={len(HARNESS_TABLE)} UNION_RAW={len(FULL_RAW)}"
    )
    print(
        f"LOCAL_STATES={POSITIVE.states} LOCAL_EDGES={POSITIVE.edges} "
        f"PRODUCT_STATES={product_states} PRODUCT_EDGES={product_edges}"
    )
    print(f"PASS={PASS} FAIL={FAIL}")
    print("RESULT=STATUS_GATED_TYPED_PAYLOAD_HANDOFF" if FAIL == 0 else "RESULT=FAIL")
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
