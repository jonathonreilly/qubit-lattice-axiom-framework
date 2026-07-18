#!/usr/bin/env python3
"""Cycle 112: one exact eight-bit payload writer and completion front.

Starting only from Cycle 100's 264-record terminal, the live Cycle 109 law
first makes its directed ``R_B11`` decision.  A guarded writer then records
the literal role word ``10010100`` as eight physical H0/H1 records.  The
existing Cycle 93 comparator writes H1 at the centre.  A two-branch completion
join consumes that status and the remaining D4 tail before writing one fresh
``R_B11`` completion/renewal token.

This is one fixed selected-output writer.  The fresh token is not consumed by
a translated second writer here, so this runner does not claim generic word
addressability, successor allocation, or unbounded recurrence.  Cycle 114's
schedule-fork rows are not imported.  Cycle 113's reusable-cone geometry is a
named downstream integration seam rather than part of this table.

Authority: none.  No foundation, registry, queue, audit, policy, or git state
is edited or selected by this runner.
"""

from __future__ import annotations

from collections import defaultdict, deque
from dataclasses import dataclass
from pathlib import Path

import four_open_reservation_comb_cycle59_2026_07_14 as c59
import status_gated_typed_payload_handoff_cycle109_2026_07_15 as c109


ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / "docs" / "work_history" / "repo" / "review_feedback"
NOTE = REVIEW / "EIGHT_BIT_STATUS_COMPLETION_FRONT_CYCLE112_NOTE_2026-07-15.md"

c105 = c109.c105
c101 = c105.c101
c100 = c101.c100
c53 = c100.c53
c93 = c109.c95.c93

Coord = c109.Coord
Signature = c109.Signature
RawTable = c109.RawTable
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
    local = c53.local_signature(records, site)
    canonical = c53.canonical_signature(local)
    prior = table.get(canonical)
    if prior is not None and prior != output:
        raise ValueError((canonical, prior, output))
    table[canonical] = output


# ---------------------------------------------------------------------------
# Literal selected-output word and the tail-dependent relay spine.
#
# D0..D7 are physical records written after Cycle 109's directed R_B11
# decision.  They are not a supplied word and not repeated comparator inputs.
# D5 is deliberately not unary: it waits for the R_LC relay.  That removes the
# transient unary-R_B01 collision which a fixed-C109-terminal-only probe hid.
# ---------------------------------------------------------------------------

D0 = (4, 5, 2)
D1 = (4, 4, 1)
D2 = (4, 3, 1)
D3 = (4, 3, 2)
D4 = (4, 3, 3)
D5 = (4, 4, 3)
D6 = (3, 5, 3)
D7 = (2, 5, 3)
DATA_SITES: tuple[Coord, ...] = (D0, D1, D2, D3, D4, D5, D6, D7)
DATA_WORD = c100.R_B11_WORD
DATA_OUTPUTS = tuple(H1 if bit else H0 for bit in DATA_WORD)
DATA_RECORDS: tuple[tuple[Coord, str], ...] = tuple(zip(DATA_SITES, DATA_OUTPUTS))

GUARD_SPINE: tuple[Coord, ...] = (
    (1, 6, 3),
    (2, 6, 3),
    (3, 6, 3),
    (4, 6, 3),
)
GUARD_OUTPUTS: tuple[str, ...] = ("T_G1", "T_N0", "T_N2", "T_H1")
RELAY = (4, 5, 3)
RELAY_OUTPUT = "R_LC"

# Cycle 109 already contains unary R_LC -> R_A31.  Once RELAY forms, exactly
# these two open images inherit that landed row; the other four neighbours are
# already occupied by D0, D6, D5's R_B01 support, and the guard spine.
RELAY_IMAGES: tuple[Coord, ...] = ((5, 5, 3), (4, 5, 4))
RELAY_IMAGE_OUTPUT = "R_A31"


# ---------------------------------------------------------------------------
# Literal C93 status and a two-branch completion join.
#
# STATUS can precede D4.  Therefore the renewal token does not use STATUS
# alone.  SIGNAL_D4 consumes D4; SIGNAL_STATUS consumes STATUS; NEXT_FRONT
# joins both branches and is the first post-completion R_B11 token.
# ---------------------------------------------------------------------------

STATUS = (4, 4, 2)
STATUS_OUTPUT = H1

PAIR_IMAGES: tuple[Coord, ...] = ((5, 4, 3), (5, 5, 2), (4, 4, 4))
PAIR_OUTPUT = "T_H2"
SIGNAL_D4_IMAGES: tuple[Coord, ...] = ((5, 3, 3), (4, 3, 4))
SIGNAL_D4_OUTPUT = "T_N1"
SIGNAL_STATUS = (5, 4, 2)
SIGNAL_STATUS_OUTPUT = "T_G0"
NEXT_FRONT = (5, 3, 2)
NEXT_FRONT_OUTPUT = "R_B11"


def build_tables() -> tuple[dict[Signature, str], dict[Signature, str]]:
    records = c109.positive_terminal_records()
    writer: dict[Signature, str] = {}

    # The two independent branches can start in either order.  D4/D5 are
    # intentionally delayed until after the tail-dependent relay.
    for index in (0, 1, 2, 3, 6, 7):
        site, output = DATA_RECORDS[index]
        add_canonical(writer, records, site, output)
        put(records, site, output)

    for site, output in zip(GUARD_SPINE, GUARD_OUTPUTS):
        add_canonical(writer, records, site, output)
        put(records, site, output)

    add_canonical(writer, records, RELAY, RELAY_OUTPUT)
    put(records, RELAY, RELAY_OUTPUT)

    unary = c53.local_signature(records, RELAY_IMAGES[0])
    if c109.FULL_RAW.get(unary) != frozenset((RELAY_IMAGE_OUTPUT,)):
        raise ValueError((unary, c109.FULL_RAW.get(unary)))
    for site in RELAY_IMAGES:
        put(records, site, RELAY_IMAGE_OUTPUT)

    add_canonical(writer, records, D5, H1)
    put(records, D5, H1)
    add_canonical(writer, records, D4, H0)
    put(records, D4, H0)

    completion: dict[Signature, str] = {}
    add_canonical(completion, records, PAIR_IMAGES[0], PAIR_OUTPUT)
    for site in PAIR_IMAGES:
        put(records, site, PAIR_OUTPUT)

    # This is an inherited Cycle-93 row, not a Cycle-112 canonical row.
    put(records, STATUS, STATUS_OUTPUT)

    add_canonical(
        completion,
        records,
        SIGNAL_D4_IMAGES[0],
        SIGNAL_D4_OUTPUT,
    )
    for site in SIGNAL_D4_IMAGES:
        put(records, site, SIGNAL_D4_OUTPUT)

    add_canonical(completion, records, SIGNAL_STATUS, SIGNAL_STATUS_OUTPUT)
    put(records, SIGNAL_STATUS, SIGNAL_STATUS_OUTPUT)
    add_canonical(completion, records, NEXT_FRONT, NEXT_FRONT_OUTPUT)
    return writer, completion


WRITER_TABLE, COMPLETION_TABLE = build_tables()
WRITER_RAW = c59.raw_rule_outputs(WRITER_TABLE)
COMPLETION_RAW = c59.raw_rule_outputs(COMPLETION_TABLE)

WRITER_OUTPUTS: dict[Coord, str] = {
    **dict(DATA_RECORDS),
    **dict(zip(GUARD_SPINE, GUARD_OUTPUTS)),
    RELAY: RELAY_OUTPUT,
    **{site: RELAY_IMAGE_OUTPUT for site in RELAY_IMAGES},
}
COMPLETION_OUTPUTS: dict[Coord, str] = {
    STATUS: STATUS_OUTPUT,
    **{site: PAIR_OUTPUT for site in PAIR_IMAGES},
    **{site: SIGNAL_D4_OUTPUT for site in SIGNAL_D4_IMAGES},
    SIGNAL_STATUS: SIGNAL_STATUS_OUTPUT,
    NEXT_FRONT: NEXT_FRONT_OUTPUT,
}
EXTENSION_OUTPUTS: dict[Coord, str] = {
    **WRITER_OUTPUTS,
    **COMPLETION_OUTPUTS,
}
GROWN_OUTPUTS: dict[Coord, str] = {
    **c109.GROWN_OUTPUTS,
    **EXTENSION_OUTPUTS,
}

FULL_RAW = merge_raw(
    c109.FULL_RAW,
    c93.STATUS_RAW,
    WRITER_RAW,
    COMPLETION_RAW,
)

SOURCE = dict(c101.TERMINAL)
RAIL_ZERO = {c105.FIRST_RAIL[0]: frozenset((c105.FIRST_RAIL[1],))}


def enabled(
    records: dict[Coord, str],
    raw: RawTable = FULL_RAW,
) -> dict[Coord, frozenset[str]]:
    return {
        target: raw[local]
        for target in c53.open_candidates(records)
        if (local := c53.local_signature(records, target)) in raw
    }


# ---------------------------------------------------------------------------
# Exact asynchronous graph compiler.
#
# The compiler enumerates every local subset of the 69 variable record sites,
# including target signatures which would be unintended.  The graph then
# exhausts every reachable append ordering.  This is equivalent to rescanning
# all open lattice neighbours at every state but is substantially faster.
# ---------------------------------------------------------------------------

Condition = tuple[int, int, frozenset[str]]


@dataclass(frozen=True)
class CompiledConditions:
    sites: tuple[Coord, ...]
    index: dict[Coord, int]
    conditions: dict[Coord, tuple[Condition, ...]]
    unexpected_targets: frozenset[Coord]


def compile_conditions(
    source: dict[Coord, str],
    outputs: dict[Coord, str],
    raw: RawTable = FULL_RAW,
    ignored: dict[Coord, frozenset[str]] = RAIL_ZERO,
) -> CompiledConditions:
    sites = tuple(sorted(outputs))
    index = {site: position for position, site in enumerate(sites)}
    universe: set[Coord] = set()
    for site in set(source) | set(sites):
        for direction in c53.DIRECTIONS:
            universe.add(c53.add(site, direction))
    universe.difference_update(source)

    conditions: dict[Coord, tuple[Condition, ...]] = {}
    for target in universe:
        fixed: list[tuple[Coord, str]] = []
        variable: list[tuple[int, Coord, str]] = []
        for direction in c53.DIRECTIONS:
            neighbour = c53.add(target, direction)
            if neighbour in source:
                fixed.append((direction, source[neighbour]))
            elif neighbour in index:
                variable.append((index[neighbour], direction, outputs[neighbour]))

        neighbourhood_mask = sum(1 << item[0] for item in variable)
        local_conditions: list[Condition] = []
        for subset in range(1 << len(variable)):
            parts = list(fixed)
            present_mask = 0
            for local_index, (global_index, direction, output) in enumerate(variable):
                if subset >> local_index & 1:
                    parts.append((direction, output))
                    present_mask |= 1 << global_index
            values = raw.get(tuple(sorted(parts)))
            if values is not None:
                local_conditions.append((present_mask, neighbourhood_mask, values))
        if local_conditions:
            conditions[target] = tuple(local_conditions)

    unexpected = frozenset(set(conditions) - set(outputs) - set(ignored))
    return CompiledConditions(sites, index, conditions, unexpected)


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
    unexpected_condition_targets: frozenset[Coord]
    completion_violations: tuple[int, ...]


def append_graph(
    source: dict[Coord, str] | None = None,
    outputs: dict[Coord, str] | None = None,
    raw: RawTable = FULL_RAW,
    ignored: dict[Coord, frozenset[str]] = RAIL_ZERO,
    state_limit: int = 5_000_000,
) -> GraphStats:
    actual_source = SOURCE if source is None else source
    actual_outputs = GROWN_OUTPUTS if outputs is None else outputs
    compiled = compile_conditions(actual_source, actual_outputs, raw, ignored)
    actions = tuple(
        (compiled.index.get(target), target, conditions)
        for target, conditions in compiled.conditions.items()
    )

    queue = deque((0,))
    seen = {0}
    edges = 0
    terminal_states: list[int] = []
    bad: list[object] = []
    reached: set[Coord] = set()
    max_frontier = 0
    completion_violations: list[int] = []

    required_sites = set(DATA_SITES) | {STATUS}
    required_mask = sum(
        1 << compiled.index[site]
        for site in required_sites
        if site in compiled.index
    )
    completion_index = compiled.index.get(NEXT_FRONT)

    while queue:
        state = queue.popleft()
        if (
            completion_index is not None
            and state >> completion_index & 1
            and state & required_mask != required_mask
        ):
            completion_violations.append(state)

        legal: list[int] = []
        for index, target, conditions in actions:
            if index is not None and state >> index & 1:
                continue
            for present_mask, neighbourhood_mask, values in conditions:
                if state & neighbourhood_mask != present_mask:
                    continue
                if target in ignored and values == ignored[target]:
                    break
                if (
                    index is not None
                    and values == frozenset((actual_outputs[target],))
                ):
                    legal.append(index)
                    break
                bad.append((state, target, values))
                break
            if bad:
                break
        if bad:
            break

        max_frontier = max(max_frontier, len(legal))
        if not legal:
            terminal_states.append(state)
            continue
        for index in legal:
            future = state | 1 << index
            edges += 1
            reached.add(compiled.sites[index])
            if future not in seen:
                seen.add(future)
                queue.append(future)
                if len(seen) > state_limit:
                    bad.append(("state-limit", state_limit))
                    queue.clear()
                    break

    return GraphStats(
        states=len(seen),
        edges=edges,
        terminals=len(terminal_states),
        terminal_states=tuple(terminal_states),
        terminal_sizes=tuple(sorted({state.bit_count() for state in terminal_states})),
        max_frontier=max_frontier,
        bad=tuple(bad),
        reached=frozenset(reached),
        unexpected_condition_targets=compiled.unexpected_targets,
        completion_violations=tuple(completion_violations),
    )


def records_at(
    state: int,
    source: dict[Coord, str],
    outputs: dict[Coord, str],
) -> dict[Coord, str]:
    records = dict(source)
    for index, site in enumerate(sorted(outputs)):
        if state >> index & 1:
            records[site] = outputs[site]
    return records


POSITIVE = append_graph()
ALL_GROWN_MASK = (1 << len(GROWN_OUTPUTS)) - 1


def positive_terminal_records() -> dict[Coord, str]:
    if POSITIVE.terminal_states != (ALL_GROWN_MASK,):
        raise RuntimeError(POSITIVE.terminal_states)
    return records_at(ALL_GROWN_MASK, SOURCE, GROWN_OUTPUTS)


# ---------------------------------------------------------------------------
# Contracts.
# ---------------------------------------------------------------------------

def table_and_writer_contract() -> None:
    section("A - Literal fixed-word writer and table partition")
    check("A01 note exists", NOTE.is_file())
    check(
        "A02 writer is 13 canonical / 312 proper-cubic raw rows",
        len(WRITER_TABLE) == 13
        and len(WRITER_RAW) == 312
        and all(len(values) == 1 for values in WRITER_RAW.values()),
        f"canonical={len(WRITER_TABLE)} raw={len(WRITER_RAW)}",
    )
    check(
        "A03 completion is four canonical / 96 raw rows",
        len(COMPLETION_TABLE) == 4
        and len(COMPLETION_RAW) == 96
        and set(WRITER_RAW).isdisjoint(COMPLETION_RAW),
        f"canonical={len(COMPLETION_TABLE)} raw={len(COMPLETION_RAW)}",
    )
    check(
        "A04 full 8,048-row law is single-valued and alphabet-closed",
        len(FULL_RAW) == 8_048
        and all(len(values) == 1 for values in FULL_RAW.values())
        and {
            content
            for local, values in FULL_RAW.items()
            for content in [*(value for _direction, value in local), *values]
        }
        <= c105.c89.FULL_ROLES,
    )
    check(
        "A05 extension adds zero supplied records to the exact 264 boundary",
        len(SOURCE) == 264 and set(EXTENSION_OUTPUTS).isdisjoint(SOURCE),
    )

    writer_records = c109.positive_terminal_records()
    writer_records.update(WRITER_OUTPUTS)
    decoded = tuple(1 if writer_records[site] == H1 else 0 for site in DATA_SITES)
    check(
        "A06 eight physical records decode literal R_B11=10010100",
        decoded == DATA_WORD == (1, 0, 0, 1, 0, 1, 0, 0),
        str(decoded),
    )

    status_local = c53.local_signature(writer_records, STATUS)
    check(
        "A07 centre is a literal inherited Cycle-93 H1 comparator",
        c93.STATUS_RAW.get(status_local) == frozenset((H1,))
        and dict(status_local).values() is not None
        and sorted(value for _direction, value in status_local) == [H0, H1, H1, H1, H1],
        str(status_local),
    )

    relay_pre = c109.positive_terminal_records()
    for index in (0, 1, 2, 3, 6, 7):
        relay_pre[DATA_SITES[index]] = DATA_OUTPUTS[index]
    relay_pre.update(dict(zip(GUARD_SPINE, GUARD_OUTPUTS)))
    relay_pre[RELAY] = RELAY_OUTPUT
    inherited_images = {
        target
        for target, values in enabled(relay_pre, c109.FULL_RAW).items()
        if values == frozenset((RELAY_IMAGE_OUTPUT,))
    }
    check(
        "A08 inherited R_LC row has exactly two R_A31 relay images",
        inherited_images == set(RELAY_IMAGES),
        str(inherited_images),
    )


def graph_and_completion_contract() -> None:
    section("B - All-current-rows asynchronous composition")
    check(
        "B01 exact variable corpus is 46 inherited plus 23 new writes",
        len(c109.GROWN_OUTPUTS) == 46
        and len(EXTENSION_OUTPUTS) == 23
        and len(GROWN_OUTPUTS) == 69,
    )
    check(
        "B02 every local subset has no non-expected enabled target",
        not POSITIVE.unexpected_condition_targets,
        str(POSITIVE.unexpected_condition_targets),
    )
    check(
        "B03 all schedules give one complete 69-write terminal",
        POSITIVE.states == 73_656
        and POSITIVE.edges == 430_754
        and POSITIVE.terminals == 1
        and POSITIVE.terminal_states == (ALL_GROWN_MASK,)
        and POSITIVE.terminal_sizes == (69,)
        and POSITIVE.max_frontier == 11
        and not POSITIVE.bad,
        f"states={POSITIVE.states} edges={POSITIVE.edges} terminals={POSITIVE.terminals} max={POSITIVE.max_frontier}",
    )
    check(
        "B04 next front never precedes all eight data records plus status",
        not POSITIVE.completion_violations,
        str(POSITIVE.completion_violations[:1]),
    )
    terminal = positive_terminal_records()
    check(
        "B05 terminal carries the exact fresh post-completion R_B11 token",
        terminal.get(NEXT_FRONT) == NEXT_FRONT_OUTPUT
        and all(terminal.get(site) == output for site, output in DATA_RECORDS)
        and terminal.get(STATUS) == H1,
    )
    check(
        "B06 terminal exposes only the inherited repaired-rail front",
        enabled(terminal) == RAIL_ZERO,
        str(enabled(terminal)),
    )


def rail_contract() -> None:
    section("C - 96-prefix rail product and late-alias control")
    records = positive_terminal_records()
    failures = []
    for prefix, (site, content) in enumerate(c105.RAIL_SEQUENCE[: c105.RAIL_HORIZON]):
        actual = enabled(records)
        expected = {site: frozenset((content,))}
        if actual != expected:
            failures.append((prefix, expected, actual))
            break
        records[site] = content
    check(
        "C01 all 96 rail appends remain exact singleton fronts",
        not failures
        and enabled(records) == {c105.NEXT_RAIL[0]: frozenset((c105.NEXT_RAIL[1],))},
        str(failures[:1]),
    )

    extension_raw = merge_raw(WRITER_RAW, COMPLETION_RAW, c93.STATUS_RAW)
    rail_only = dict(SOURCE)
    hits = []
    for prefix in range(c105.RAIL_HORIZON + 1):
        for target in c53.open_candidates(rail_only):
            local = c53.local_signature(rail_only, target)
            if local in extension_raw and local not in c109.FULL_RAW:
                hits.append((prefix, target, local))
        if prefix < c105.RAIL_HORIZON:
            site, content = c105.RAIL_SEQUENCE[prefix]
            rail_only[site] = content
    new_sites = set(EXTENSION_OUTPUTS)
    rail_sites = {site for site, _content in c105.RAIL_SEQUENCE[: c105.RAIL_HORIZON]}
    distance = min(c101.manhattan(left, right) for left in new_sites for right in rail_sites)
    check(
        "C02 extension is rail-separated and has zero 97-prefix aliases",
        distance >= 7 and not hits,
        f"distance={distance} hits={hits[:1]}",
    )

    product_states = POSITIVE.states * (c105.RAIL_HORIZON + 1)
    product_edges = (
        POSITIVE.edges * (c105.RAIL_HORIZON + 1)
        + POSITIVE.states * c105.RAIL_HORIZON
    )
    check(
        "C03 exact locality product is 7,144,632 states / 48,854,114 edges",
        product_states == 7_144_632 and product_edges == 48_854_114,
        f"states={product_states} edges={product_edges}",
    )

    long_rail = c105.c108.c104.rail_sequence(102, c105.ROLE_MAP)
    late = positive_terminal_records()
    late_failures = []
    for prefix, (site, content) in enumerate(long_rail[: 101 * 12]):
        actual = enabled(late)
        expected = {site: frozenset((content,))}
        if actual != expected:
            late_failures.append((prefix, expected, actual))
            break
        late[site] = content
    next_site, next_content = long_rail[101 * 12]
    check(
        "C04 late control grows 101 complete slices / 1,212 records",
        not late_failures
        and len(late) == 1_545
        and enabled(late) == {next_site: frozenset((next_content,))},
        str(late_failures[:1]),
    )


def append_rail(records: dict[Coord, str]) -> tuple[dict[Coord, str], tuple[object, ...]]:
    answer = dict(records)
    failures: list[object] = []
    for prefix, (site, content) in enumerate(c105.RAIL_SEQUENCE[: c105.RAIL_HORIZON]):
        actual = enabled(answer)
        expected = {site: frozenset((content,))}
        if actual != expected:
            failures.append((prefix, expected, actual))
            break
        answer[site] = content
    if not failures and enabled(answer) != {
        c105.NEXT_RAIL[0]: frozenset((c105.NEXT_RAIL[1],))
    }:
        failures.append((c105.RAIL_HORIZON, enabled(answer)))
    return answer, tuple(failures)


def corruption_contract() -> list[tuple[str, dict[Coord, str]]]:
    section("D - Every word corruption and the H0 reject control")
    cases: list[tuple[str, dict[Coord, str]]] = []
    observed = []
    failures = []
    for index, site in enumerate(c100.CODE_SITES):
        source = dict(SOURCE)
        source[site] = H0 if source[site] == H1 else H1
        outputs = dict(GROWN_OUTPUTS)
        if index == 5:
            outputs[c101.BIT5_REJECT] = H1
        stats = append_graph(source, outputs)
        observed.append((stats.states, stats.edges, stats.terminal_sizes))
        if (
            stats.terminals != 1
            or stats.bad
            or set(DATA_SITES) & stats.reached
            or STATUS in stats.reached
            or NEXT_FRONT in stats.reached
        ):
            failures.append((f"bit-{index}", stats))
            continue
        terminal = records_at(stats.terminal_states[0], source, outputs)
        cases.append((f"bit-{index}", terminal))

    for label, site in (("valid", c100.VALID), ("ready", c100.READY)):
        source = dict(SOURCE)
        source[site] = H0
        stats = append_graph(source)
        observed.append((stats.states, stats.edges, stats.terminal_sizes))
        if (
            stats.terminals != 1
            or stats.bad
            or set(DATA_SITES) & stats.reached
            or STATUS in stats.reached
            or NEXT_FRONT in stats.reached
        ):
            failures.append((label, stats))
            continue
        terminal = records_at(stats.terminal_states[0], source, GROWN_OUTPUTS)
        cases.append((label, terminal))

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
        "D01 all eight flips plus wrong VALID/READY stop before the writer",
        len(cases) == 10 and not failures,
        str(failures[:1]),
    )
    check("D02 corrupt graph census is executable and pinned", observed == expected, str(observed))

    rail_failures = []
    for label, terminal in cases:
        _complete, local_failures = append_rail(terminal)
        if local_failures:
            rail_failures.append((label, local_failures[0]))
    check(
        "D03 all ten corrupt terminals retain 96 exact rail appends",
        not rail_failures,
        str(rail_failures[:1]),
    )

    fault_expected = (
        (c109.c106.STATUS, H0),
        (c109.DIRECTED_PAYLOAD, "AUX"),
        (c109.LAUNCH, "A_0_0"),
        (None, None),
    )
    projection_failures = []
    extension_sites = set(EXTENSION_OUTPUTS)
    reject_projection_sites = {
        c109.c106.STATUS,
        c109.DIRECTED_PAYLOAD,
        c109.LAUNCH,
    }
    for stage, (target, output) in enumerate(fault_expected):
        actual = enabled(c109.fault_records(stage))
        projected = {
            site: values
            for site, values in actual.items()
            if (
                (site not in extension_sites or site in reject_projection_sites)
                and site not in RAIL_ZERO
            )
        }
        expected_projection = {} if target is None else {target: frozenset((output,))}
        if projected != expected_projection:
            projection_failures.append((stage, expected_projection, projected))
    check(
        "D04 H0 control retains exact STATUS->AUX->A_0_0 reject projection",
        not projection_failures,
        str(projection_failures[:1]),
    )

    fault_source = c109.fault_records(3)
    fault_outputs = {
        site: output
        for site, output in EXTENSION_OUTPUTS.items()
        if site not in fault_source
    }
    # Under the H0 reference/status history, the inherited H0+H0 row writes
    # harmless H1 cages at the two would-be middle guard sites.
    fault_outputs[GUARD_SPINE[1]] = H1
    fault_outputs[GUARD_SPINE[2]] = H1
    fault_stats = append_graph(fault_source, fault_outputs)
    fault_cases = [
        (
            f"fault-terminal-{index}",
            records_at(state, fault_source, fault_outputs),
        )
        for index, state in enumerate(fault_stats.terminal_states)
    ]
    fault_front_failures = []
    for label, terminal in fault_cases:
        _complete, local_failures = append_rail(terminal)
        if local_failures:
            fault_front_failures.append((label, local_failures[0]))
    check(
        "D05 exhausted H0 control has two exact partial terminals and no completion",
        fault_stats.states == 44
        and fault_stats.edges == 97
        and fault_stats.terminals == 2
        and fault_stats.terminal_sizes == (6, 7)
        and not fault_stats.bad
        and STATUS not in fault_stats.reached
        and NEXT_FRONT not in fault_stats.reached
        and not fault_front_failures,
        f"states={fault_stats.states} edges={fault_stats.edges} sizes={fault_stats.terminal_sizes} bad={fault_stats.bad[:1]}",
    )
    return cases + fault_cases


def covariance_and_scope_contract(extra_cases: list[tuple[str, dict[Coord, str]]]) -> None:
    section("E - Proper-cubic covariance and bounded scope")
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
        "E01 all 193,152 proper-cubic raw images preserve output",
        controls == len(FULL_RAW) * 24 == 193_152 and not covariance_failures,
        str(covariance_failures[:1]),
    )

    completed_cases = []
    correct, correct_failures = append_rail(positive_terminal_records())
    if correct_failures:
        completed_cases.append(("correct-rail-failure", positive_terminal_records()))
    else:
        completed_cases.append(("correct", correct))
    for label, records in extra_cases:
        complete, failures = append_rail(records)
        if failures:
            completed_cases.append((label + "-rail-failure", records))
        else:
            completed_cases.append((label, complete))

    rotated_failures = []
    shift = (157, -103, 83)
    for label, records in completed_cases:
        for rotation in c53.ROTATIONS:
            transformed = c105.transform_records(records, rotation, shift)
            next_site = c101.transform_site(c105.NEXT_RAIL[0], rotation, shift)
            expected = {next_site: frozenset((c105.NEXT_RAIL[1],))}
            actual = enabled(transformed)
            if actual != expected:
                rotated_failures.append((label, rotation, expected, actual))
                break
    check(
        "E02 correct/corrupt/H0 terminal corpora expose only rotated next rail",
        len(completed_cases) == 13 and not rotated_failures,
        str(rotated_failures[:1]),
    )

    note = NOTE.read_text(encoding="utf-8").lower() if NOTE.is_file() else ""
    check("E03 note names selected output/payload writer", "selected output/payload word" in note)
    check("E04 note names STREAM_COMPLETION_TO_REUSABLE_CONE seam", "stream_completion_to_reusable_cone" in note)
    check("E05 note states Cycle 114 contributes zero rows", "cycle 114 contributes zero rows" in note)
    check("E06 note carries the remote N1-N8 discipline", all(f"n{index}" in note for index in range(1, 9)))
    check("E07 note makes no generic addressability claim", "does not establish generic candidate-selectable addressability" in note)
    check("E08 note makes no axiom addition", "no axiom addition follows" in note)
    check(
        "E09 Cycle 112 writes only runner and review note",
        all(path.parent in (ROOT / "scripts", REVIEW) for path in (Path(__file__), NOTE)),
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    table_and_writer_contract()
    graph_and_completion_contract()
    rail_contract()
    extra_cases = corruption_contract()
    covariance_and_scope_contract(extra_cases)
    product_states = POSITIVE.states * (c105.RAIL_HORIZON + 1)
    product_edges = (
        POSITIVE.edges * (c105.RAIL_HORIZON + 1)
        + POSITIVE.states * c105.RAIL_HORIZON
    )
    print(
        f"\nWRITER_CANONICAL={len(WRITER_TABLE)} WRITER_RAW={len(WRITER_RAW)} "
        f"COMPLETION_CANONICAL={len(COMPLETION_TABLE)} COMPLETION_RAW={len(COMPLETION_RAW)}"
    )
    print(
        f"GROWN={len(GROWN_OUTPUTS)} UNION_RAW={len(FULL_RAW)} "
        f"LOCAL_STATES={POSITIVE.states} LOCAL_EDGES={POSITIVE.edges}"
    )
    print(f"PRODUCT_STATES={product_states} PRODUCT_EDGES={product_edges}")
    print(f"PASS={PASS} FAIL={FAIL}")
    print("RESULT=EIGHT_BIT_STATUS_COMPLETION_FRONT" if FAIL == 0 else "RESULT=FAIL")
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
