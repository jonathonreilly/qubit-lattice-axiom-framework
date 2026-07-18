#!/usr/bin/env python3
"""Cycle 113: fixed-word status and alternate reject/launch completion.

Cycle 112's guarded writer replaces the provisional Cycle-113 zipper in full.
This runner consumes only that writer surface, then grows one literal Cycle-93
H1 status on the positive history.  Replacing D3 by H0 after the writer is a
typed alternate-history control: it grows the exact Cycle-95 AUX decision and
the exact Cycle-95 A_0_0 launch at a bounded local completion cone.

The positive graph starts at the exact 264-record Cycle-100 terminal and
exhausts all append orders through Cycle 109, the Cycle-112 writer, and the
Cycle-113 H1 completion.  The H0 control is not positive evidence.  Literal
Cycle-114 compatibility is tested separately: its lawful H1 history enters
this cone while its lawful H0 history exits at Cycle 109's earlier reject.

Cycle 112's own completion and Cycle 115's successor are locally competing
continuations at several shared sites.  They are compared here but are not
silently combined with this alternative completion.

Authority: none.  No foundation, registry, queue, audit, policy, or git state
is edited or selected by this runner.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from pathlib import Path

import aux_gated_candidate_transport_cycle95_2026_07_15 as c95
import eight_bit_status_completion_front_cycle112_2026_07_15 as c112
import first_autonomous_successor_role_port_cycle115_2026_07_15 as c115
import lawful_h0_reference_fork_cycle114_2026_07_15 as c114


ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / "docs" / "work_history" / "repo" / "review_feedback"
NOTE = REVIEW / "DIRECTED_PAYLOAD_REUSABLE_CONE_CYCLE113_NOTE_2026-07-15.md"

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


def merge_raw(*tables: RawTable) -> RawTable:
    outputs: dict[Signature, set[str]] = defaultdict(set)
    for table in tables:
        for local, values in table.items():
            outputs[local].update(values)
    return {local: frozenset(values) for local, values in outputs.items()}


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
# Common positive support after the literal Cycle-112 writer.
#
# The first row sees the final writer tail T_H1 and inherited R_A31.  Proper
# cubic covariance forces exactly two T_H3 images.  They direct a five-record
# support chain into the two literal Cycle-95 decision guards.  The chain is
# deliberately not started by unary JOINT or unary J3: both shorter prototypes
# produced early writes during the full Cycle-109 growth graph.
# ---------------------------------------------------------------------------

X_SITES: tuple[Coord, ...] = ((5, 6, 3), (4, 6, 4))
X_OUTPUT = "T_H3"
NORTH_SUPPORT = (5, 6, 2)
NORTH_OUTPUT = "T_N1"
BASE_SUPPORT = (5, 6, 1)
BASE_OUTPUT = "T_N2"
MARK = (5, 5, 1)
MARK_OUTPUT = "T_G0"
GUARD_H0 = (5, 4, 1)
GUARD_H1 = (5, 5, 2)
STATUS = c112.STATUS


# ---------------------------------------------------------------------------
# Alternate H0 completion.
#
# The H0 control replaces the fixed writer's D3 only after the lawful writer
# frontier.  Existing C93 writes STATUS=H0.  Existing C95 then writes AUX at
# DECISION.  Five new rows grow the remaining launch support; the final write
# at LAUNCH is the exact existing C95 A_0_0 row.
# ---------------------------------------------------------------------------

DECISION = (5, 4, 2)
TURN = (5, 4, 3)
TURN_OUTPUT = "T_H2"
LAUNCH_GUARD = (5, 3, 3)
R_C02_SIDES: tuple[Coord, ...] = ((6, 3, 3), (5, 3, 4))
SIDE_GUARD_SITES: tuple[Coord, ...] = ((6, 4, 3), (5, 4, 4))
SIDE_GUARD_OUTPUT = "T_H2"
H0_TURN = (6, 4, 2)
H0_TURN_OUTPUT = "T_G0"
LAUNCH_H0 = (6, 3, 2)
LAUNCH = (5, 3, 2)


def writer_terminal_records() -> dict[Coord, str]:
    records = c109.positive_terminal_records()
    records.update(c112.WRITER_OUTPUTS)
    return records


def build_cycle113_table() -> dict[Signature, str]:
    records = writer_terminal_records()
    table: dict[Signature, str] = {}

    add_canonical(table, records, X_SITES[0], X_OUTPUT)
    records.update({site: X_OUTPUT for site in X_SITES})
    for site, output in (
        (NORTH_SUPPORT, NORTH_OUTPUT),
        (BASE_SUPPORT, BASE_OUTPUT),
        (MARK, MARK_OUTPUT),
        (GUARD_H0, "T_H0"),
        (GUARD_H1, "T_H1"),
    ):
        add_canonical(table, records, site, output)
        records[site] = output

    # STATUS=H1 is inherited C93 content, not a Cycle-113 row.
    records[STATUS] = H1

    alternate = dict(records)
    alternate.pop(c112.D3)
    alternate.pop(STATUS)
    alternate[c112.D3] = H0
    alternate[STATUS] = H0
    alternate[DECISION] = "AUX"  # exact inherited C95 decision

    for site, output in (
        (TURN, TURN_OUTPUT),
        (LAUNCH_GUARD, "LAUNCH_A"),
    ):
        add_canonical(table, alternate, site, output)
        alternate[site] = output

    # The inherited unary LAUNCH_A row forces exactly these two local images.
    alternate.update({site: "R_C02" for site in R_C02_SIDES})
    add_canonical(table, alternate, SIDE_GUARD_SITES[0], SIDE_GUARD_OUTPUT)
    alternate.update({site: SIDE_GUARD_OUTPUT for site in SIDE_GUARD_SITES})

    for site, output in ((H0_TURN, H0_TURN_OUTPUT), (LAUNCH_H0, H0)):
        add_canonical(table, alternate, site, output)
        alternate[site] = output
    return table


NEW_TABLE = build_cycle113_table()
NEW_RAW = c59.raw_rule_outputs(NEW_TABLE)

# Cycle 95's old base is deliberately not imported.  NEW_RAW plus the
# compatible C95/C93 subsets are literal proper-cubic tables.
FULL_RAW = merge_raw(
    c109.FULL_RAW,
    c112.WRITER_RAW,
    c95.c93.STATUS_RAW,
    c95.c93.FINAL_RAW,
    c95.NEW_RAW,
    NEW_RAW,
)


def enabled(
    records: dict[Coord, str],
    raw: RawTable = FULL_RAW,
) -> dict[Coord, frozenset[str]]:
    return {
        target: raw[local]
        for target in c53.open_candidates(records)
        if (local := c53.local_signature(records, target)) in raw
    }


COMMON_OUTPUTS: dict[Coord, str] = {
    **{site: X_OUTPUT for site in X_SITES},
    NORTH_SUPPORT: NORTH_OUTPUT,
    BASE_SUPPORT: BASE_OUTPUT,
    MARK: MARK_OUTPUT,
    GUARD_H0: "T_H0",
    GUARD_H1: "T_H1",
}
CORRECT_OUTPUTS: dict[Coord, str] = {**COMMON_OUTPUTS, STATUS: H1}
SELECTED_GROWN_OUTPUTS: dict[Coord, str] = {
    **c109.GROWN_OUTPUTS,
    **c112.WRITER_OUTPUTS,
    **CORRECT_OUTPUTS,
}
POSITIVE = c112.append_graph(
    c112.SOURCE,
    SELECTED_GROWN_OUTPUTS,
    raw=FULL_RAW,
)
ALL_POSITIVE_MASK = (1 << len(SELECTED_GROWN_OUTPUTS)) - 1


def positive_terminal_records() -> dict[Coord, str]:
    if POSITIVE.terminal_states != (ALL_POSITIVE_MASK,):
        raise RuntimeError(POSITIVE.terminal_states)
    return c112.records_at(
        ALL_POSITIVE_MASK,
        c112.SOURCE,
        SELECTED_GROWN_OUTPUTS,
    )


def alternate_source_records() -> dict[Coord, str]:
    records = writer_terminal_records()
    records.update(COMMON_OUTPUTS)
    records.pop(c112.D3)
    records[c112.D3] = H0
    return records


ALTERNATE_OUTPUTS: dict[Coord, str] = {
    STATUS: H0,
    DECISION: "AUX",
    TURN: TURN_OUTPUT,
    LAUNCH_GUARD: "LAUNCH_A",
    **{site: "R_C02" for site in R_C02_SIDES},
    **{site: SIDE_GUARD_OUTPUT for site in SIDE_GUARD_SITES},
    H0_TURN: H0_TURN_OUTPUT,
    LAUNCH_H0: H0,
    LAUNCH: "A_0_0",
}
ALTERNATE = c112.append_graph(
    alternate_source_records(),
    ALTERNATE_OUTPUTS,
    raw=FULL_RAW,
)
ALL_ALTERNATE_MASK = (1 << len(ALTERNATE_OUTPUTS)) - 1


def alternate_terminal_records() -> dict[Coord, str]:
    if ALTERNATE.terminal_states != (ALL_ALTERNATE_MASK,):
        raise RuntimeError(ALTERNATE.terminal_states)
    return c112.records_at(
        ALL_ALTERNATE_MASK,
        alternate_source_records(),
        ALTERNATE_OUTPUTS,
    )


# Literal Cycle-114 coexistence control.  Its H1 history enters the selected
# writer/cone; its H0 history exits through Cycle 109 and never starts it.
C114_RAW = merge_raw(FULL_RAW, c114.FORK_RAW)
C114_ALLOWED = dict(c114.allowed_outputs())
for _site, _output in {**c112.WRITER_OUTPUTS, **CORRECT_OUTPUTS}.items():
    C114_ALLOWED[_site] = C114_ALLOWED.get(_site, frozenset()) | frozenset((_output,))
# Cycle 112's own H0-history control proves that the two middle writer-spine
# sites lawfully become harmless H1 cages when Cycle 109 takes its H0 exit.
for _site in c112.GUARD_SPINE[1:3]:
    C114_ALLOWED[_site] = C114_ALLOWED.get(_site, frozenset()) | frozenset((H1,))
C114_GRAPH = c114.append_graph(raw=C114_RAW, allowed=C114_ALLOWED)


def c114_terminal_records() -> tuple[dict[Coord, str], ...]:
    return tuple(c114.records_at(state) for state in C114_GRAPH.terminals)


def c114_extended_label(records: dict[Coord, str]) -> str:
    """Label after downstream D0 lawfully occupies Cycle 109's launch site."""
    if (
        records.get(c109.DIRECTED_PAYLOAD) == "R_B11"
        and records.get(STATUS) == H1
        and all(records.get(site) == output for site, output in c112.WRITER_OUTPUTS.items())
    ):
        return "H1_COMPLETION"
    if c114.branch_label(records) == "H0_REJECT":
        return "H0_REJECT"
    return "UNKNOWN"


# Literal comparison with the now-green Cycle-112 completion and Cycle-115
# successor.  Raw tables can coexist, but physical records compete at named
# sites; this is an alternate completion, not their simultaneous extension.
C115_UNION_RAW = merge_raw(FULL_RAW, c115.FULL_RAW)
C115_RAW_CONFLICTS = {
    local: values
    for local, values in C115_UNION_RAW.items()
    if len(values) != 1
}
POSITIVE_C112_CONFLICTS = {
    site: (output, c112.COMPLETION_OUTPUTS[site])
    for site, output in CORRECT_OUTPUTS.items()
    if site in c112.COMPLETION_OUTPUTS
    and output != c112.COMPLETION_OUTPUTS[site]
}
ALTERNATE_C112_CONFLICTS = {
    site: (output, c112.COMPLETION_OUTPUTS[site])
    for site, output in {**COMMON_OUTPUTS, **ALTERNATE_OUTPUTS}.items()
    if site in c112.COMPLETION_OUTPUTS
    and output != c112.COMPLETION_OUTPUTS[site]
}
C115_EXTRA_CONFLICTS = {
    site: (output, c115.SUCCESSOR_OUTPUTS[site])
    for site, output in {**CORRECT_OUTPUTS, **ALTERNATE_OUTPUTS}.items()
    if site in c115.SUCCESSOR_OUTPUTS
    and output != c115.SUCCESSOR_OUTPUTS[site]
}


def append_rail(
    records: dict[Coord, str],
    raw: RawTable = FULL_RAW,
) -> tuple[dict[Coord, str], tuple[object, ...]]:
    answer = dict(records)
    failures: list[object] = []
    for prefix, (site, output) in enumerate(c105.RAIL_SEQUENCE[: c105.RAIL_HORIZON]):
        actual = enabled(answer, raw)
        expected = {site: frozenset((output,))}
        if actual != expected:
            failures.append((prefix, expected, actual))
            break
        answer[site] = output
    if not failures and enabled(answer, raw) != {
        c105.NEXT_RAIL[0]: frozenset((c105.NEXT_RAIL[1],))
    }:
        failures.append((c105.RAIL_HORIZON, enabled(answer, raw)))
    return answer, tuple(failures)


def table_and_geometry_contract() -> None:
    section("A - Literal Cycle-112 writer and exact C93/C95 rows")
    check("A01 Cycle-113 note exists", NOTE.is_file())
    check(
        "A02 new completion support is 11 canonical / 264 raw rows",
        len(NEW_TABLE) == 11 and len(NEW_RAW) == 264,
        f"canonical={len(NEW_TABLE)} raw={len(NEW_RAW)}",
    )
    check(
        "A03 new rows are disjoint from every selected predecessor subset",
        set(NEW_RAW).isdisjoint(c109.FULL_RAW)
        and set(NEW_RAW).isdisjoint(c112.WRITER_RAW)
        and set(NEW_RAW).isdisjoint(c95.c93.STATUS_RAW)
        and set(NEW_RAW).isdisjoint(c95.c93.FINAL_RAW)
        and set(NEW_RAW).isdisjoint(c95.NEW_RAW),
    )
    check(
        "A04 selected 11,186-row union is single-valued and alphabet-closed",
        len(FULL_RAW) == 11_186
        and all(len(values) == 1 for values in FULL_RAW.values())
        and {
            content
            for local, values in FULL_RAW.items()
            for content in [*(value for _direction, value in local), *values]
        }
        <= c105.c89.FULL_ROLES,
        f"raw={len(FULL_RAW)} multi={sum(len(values) != 1 for values in FULL_RAW.values())} missing={sorted({content for local, values in FULL_RAW.items() for content in [*(value for _direction, value in local), *values]} - c105.c89.FULL_ROLES)}",
    )

    writer = writer_terminal_records()
    status_local = c53.local_signature(writer, STATUS)
    check(
        "A05 centre is the literal inherited Cycle-93 H1 five-record row",
        c95.c93.STATUS_RAW.get(status_local) == frozenset((H1,))
        and sorted(output for _direction, output in status_local)
        == [H0, H1, H1, H1, H1],
        str(status_local),
    )

    alt = alternate_source_records()
    alt[STATUS] = H0
    decision_local = c53.local_signature(alt, DECISION)
    check(
        "A06 alternate decision is the exact inherited Cycle-95 AUX row",
        c95.NEW_RAW.get(decision_local) == frozenset(("AUX",))
        and sorted(output for _direction, output in decision_local)
        == [H0, "T_H0", "T_H1"],
        str(decision_local),
    )

    launch_before = alternate_terminal_records()
    launch_before.pop(LAUNCH)
    launch_local = c53.local_signature(launch_before, LAUNCH)
    check(
        "A07 alternate launch is the exact inherited Cycle-95 A_0_0 row",
        c95.NEW_RAW.get(launch_local) == frozenset(("A_0_0",))
        and sorted(output for _direction, output in launch_local)
        == ["AUX", H0, H0, "LAUNCH_A"],
        str(launch_local),
    )


def graph_contract() -> None:
    section("B - Full positive growth and bounded alternate completion")
    check(
        "B01 Cycle-112 writer replaces the provisional zipper wholesale",
        set(c112.WRITER_OUTPUTS) <= set(SELECTED_GROWN_OUTPUTS)
        and all(
            SELECTED_GROWN_OUTPUTS[site] == output
            for site, output in c112.WRITER_OUTPUTS.items()
        ),
    )
    check(
        "B02 exact positive corpus has 69 zero-added-source writes",
        len(c112.SOURCE) == 264
        and len(SELECTED_GROWN_OUTPUTS) == 69
        and set(SELECTED_GROWN_OUTPUTS).isdisjoint(c112.SOURCE),
    )
    check(
        "B03 every full-growth schedule reaches one complete positive terminal",
        POSITIVE.states == 77_336
        and POSITIVE.edges == 452_018
        and POSITIVE.terminals == 1
        and POSITIVE.terminal_states == (ALL_POSITIVE_MASK,)
        and POSITIVE.terminal_sizes == (69,)
        and POSITIVE.max_frontier == 11
        and not POSITIVE.bad
        and not POSITIVE.unexpected_condition_targets,
        f"states={POSITIVE.states} edges={POSITIVE.edges} max={POSITIVE.max_frontier}",
    )
    check(
        "B04 positive terminal is quiet except for the inherited rail",
        enabled(positive_terminal_records()) == c112.RAIL_ZERO,
        str(enabled(positive_terminal_records())),
    )
    check(
        "B05 typed H0 control reaches one complete 11-write alternate terminal",
        ALTERNATE.states == 22
        and ALTERNATE.edges == 31
        and ALTERNATE.terminals == 1
        and ALTERNATE.terminal_states == (ALL_ALTERNATE_MASK,)
        and ALTERNATE.terminal_sizes == (11,)
        and ALTERNATE.max_frontier == 2
        and not ALTERNATE.bad
        and not ALTERNATE.unexpected_condition_targets,
        f"states={ALTERNATE.states} edges={ALTERNATE.edges}",
    )
    check(
        "B06 alternate terminal is quiet except for the inherited rail",
        enabled(alternate_terminal_records()) == c112.RAIL_ZERO,
        str(enabled(alternate_terminal_records())),
    )
    check(
        "B07 LAUNCH_A forces exactly two local R_C02 and two side-guard images",
        all(alternate_terminal_records().get(site) == "R_C02" for site in R_C02_SIDES)
        and all(
            alternate_terminal_records().get(site) == SIDE_GUARD_OUTPUT
            for site in SIDE_GUARD_SITES
        ),
    )


def history_and_comparison_contract() -> None:
    section("C - Lawful histories and comparison with Cycle 112/115 completion")
    terminals = c114_terminal_records()
    labels = Counter(c114_extended_label(records) for records in terminals)
    check(
        "C01 literal Cycle-114 union remains single-valued",
        len(C114_RAW) == len(FULL_RAW) + len(c114.FORK_RAW)
        and all(len(values) == 1 for values in C114_RAW.values()),
        f"raw={len(C114_RAW)}",
    )
    check(
        "C02 Cycle-114 union has exactly one lawful H1 and one lawful H0 terminal",
        not C114_GRAPH.bad
        and C114_GRAPH.states == 115_160
        and C114_GRAPH.edges == 686_514
        and len(C114_GRAPH.terminals) == 2
        and C114_GRAPH.terminal_sizes == (54, 69)
        and labels == {"H1_COMPLETION": 1, "H0_REJECT": 1},
        f"states={C114_GRAPH.states} edges={C114_GRAPH.edges} sizes={C114_GRAPH.terminal_sizes} labels={labels} bad={C114_GRAPH.bad[:1]}",
    )
    h1_terminal = next(
        (records for records in terminals if c114_extended_label(records) == "H1_COMPLETION"),
        {},
    )
    h0_terminal = next(
        (records for records in terminals if c114_extended_label(records) == "H0_REJECT"),
        {},
    )
    check(
        "C03 lawful H1 completes the writer/cone while lawful H0 stops at the earlier reject",
        all(h1_terminal.get(site) == output for site, output in c112.WRITER_OUTPUTS.items())
        and h1_terminal.get(STATUS) == H1
        and h0_terminal.get(c109.DIRECTED_PAYLOAD) == "AUX"
        and h0_terminal.get(c109.LAUNCH) == "A_0_0"
        and h0_terminal.get(STATUS) is None
        and h0_terminal.get(c112.RELAY) is None
        and not any(site in h0_terminal for site in X_SITES),
    )

    check(
        "C04 Cycle-112/Cycle-115 raw comparison exposes exactly two rotated conflict classes",
        len(C115_UNION_RAW) == 11_282
        and len(C115_RAW_CONFLICTS) == 48
        and Counter(C115_RAW_CONFLICTS.values())
        == {
            frozenset(("T_H0", "R_A10")): 24,
            frozenset(("LAUNCH_A", "T_N1")): 24,
        },
        f"raw={len(C115_UNION_RAW)} conflicts={len(C115_RAW_CONFLICTS)} outputs={Counter(C115_RAW_CONFLICTS.values())}",
    )
    check(
        "C05 physical-site comparison exposes the alternate-completion boundary",
        POSITIVE_C112_CONFLICTS == {GUARD_H1: ("T_H1", "T_H2")}
        and set(ALTERNATE_C112_CONFLICTS)
        == {STATUS, GUARD_H1, DECISION, LAUNCH_GUARD, LAUNCH}
        and C115_EXTRA_CONFLICTS == {GUARD_H0: ("T_H0", "R_A10")},
        f"positive={POSITIVE_C112_CONFLICTS} alternate={ALTERNATE_C112_CONFLICTS} c115={C115_EXTRA_CONFLICTS}",
    )


def rail_contract() -> None:
    section("D - 96-append rail, long tail, and locality product")
    cases: list[tuple[str, dict[Coord, str], RawTable]] = [
        ("positive", positive_terminal_records(), FULL_RAW),
        ("alternate", alternate_terminal_records(), FULL_RAW),
    ]
    for records in c114_terminal_records():
        cases.append((c114_extended_label(records), records, C114_RAW))
    failures = []
    for label, records, raw in cases:
        _complete, local_failures = append_rail(records, raw)
        if local_failures:
            failures.append((label, local_failures[0]))
    check("D01 all four positive/alternate histories retain 96 exact rail appends", not failures, str(failures[:1]))

    new_sites = set(CORRECT_OUTPUTS) | set(ALTERNATE_OUTPUTS)
    rail_sites = {site for site, _output in c105.RAIL_SEQUENCE[: c105.RAIL_HORIZON]}
    distance = min(c101.manhattan(left, right) for left in new_sites for right in rail_sites)
    hits = []
    rail_only = dict(c112.SOURCE)
    for prefix in range(c105.RAIL_HORIZON + 1):
        for target in c53.open_candidates(rail_only):
            local = c53.local_signature(rail_only, target)
            if local in NEW_RAW:
                hits.append((prefix, target, local))
        if prefix < c105.RAIL_HORIZON:
            site, output = c105.RAIL_SEQUENCE[prefix]
            rail_only[site] = output
    check(
        "D02 Cycle-113 support is rail-separated with zero 97-prefix aliases",
        distance >= 7 and not hits,
        f"distance={distance} hits={hits[:1]}",
    )

    product_states = POSITIVE.states * (c105.RAIL_HORIZON + 1)
    product_edges = POSITIVE.edges * (c105.RAIL_HORIZON + 1) + POSITIVE.states * c105.RAIL_HORIZON
    check(
        "D03 exact positive 97-prefix product is computed",
        product_states == 7_501_592 and product_edges == 51_270_002,
        f"states={product_states} edges={product_edges}",
    )

    long_rail = c105.c108.c104.rail_sequence(102, c105.ROLE_MAP)
    records = positive_terminal_records()
    late_failures = []
    for prefix, (site, output) in enumerate(long_rail[: 101 * 12]):
        actual = enabled(records)
        expected = {site: frozenset((output,))}
        if actual != expected:
            late_failures.append((prefix, expected, actual))
            break
        records[site] = output
    next_site, next_output = long_rail[101 * 12]
    check(
        "D04 101 complete late slices remain exact",
        not late_failures
        and enabled(records) == {next_site: frozenset((next_output,))},
        str(late_failures[:1]),
    )


def corruption_contract() -> list[tuple[str, dict[Coord, str]]]:
    section("E - Wrong-word, wrong-status-role, and stopped-history controls")
    cases: list[tuple[str, dict[Coord, str]]] = []
    failures = []
    observed = []
    for index, site in enumerate(c100.CODE_SITES):
        source = dict(c112.SOURCE)
        source[site] = H0 if source[site] == H1 else H1
        outputs = dict(SELECTED_GROWN_OUTPUTS)
        if index == 5:
            outputs[c101.BIT5_REJECT] = H1
        stats = c112.append_graph(source, outputs, raw=FULL_RAW)
        observed.append((stats.states, stats.edges, stats.terminal_sizes))
        if (
            stats.terminals != 1
            or stats.bad
            or set(c112.DATA_SITES) & stats.reached
            or STATUS in stats.reached
        ):
            failures.append((f"bit-{index}", stats))
            continue
        cases.append((f"bit-{index}", c112.records_at(stats.terminal_states[0], source, outputs)))

    for label, site in (("valid", c100.VALID), ("ready", c100.READY)):
        source = dict(c112.SOURCE)
        source[site] = H0
        stats = c112.append_graph(source, SELECTED_GROWN_OUTPUTS, raw=FULL_RAW)
        observed.append((stats.states, stats.edges, stats.terminal_sizes))
        if (
            stats.terminals != 1
            or stats.bad
            or set(c112.DATA_SITES) & stats.reached
            or STATUS in stats.reached
        ):
            failures.append((label, stats))
            continue
        cases.append((label, c112.records_at(stats.terminal_states[0], source, SELECTED_GROWN_OUTPUTS)))

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
        "E01 all eight bit flips plus wrong VALID/READY stop before writer/cone",
        len(cases) == 10 and not failures,
        str(failures[:1]),
    )
    check("E02 stopped-history census remains pinned", observed == expected, str(observed))

    rail_failures = []
    for label, records in cases:
        _complete, local_failures = append_rail(records)
        if local_failures:
            rail_failures.append((label, local_failures[0]))
    check("E03 all ten stopped histories retain 96 exact rail appends", not rail_failures, str(rail_failures[:1]))

    typed_failures = []
    pre_status = alternate_source_records()
    pre_status.pop(c112.D3)
    for role in (H0, H1, "AUX", "ALL", "T_G0", "T_H0", "T_H1", "R_B11"):
        records = dict(pre_status)
        records[c112.D3] = role
        actual = enabled(records)
        if role == H0:
            expected_front = {**c112.RAIL_ZERO, STATUS: frozenset((H0,))}
        elif role == H1:
            expected_front = {**c112.RAIL_ZERO, STATUS: frozenset((H1,))}
        elif role == "ALL":
            expected_front = {
                **c112.RAIL_ZERO,
                LAUNCH: frozenset(("R1",)),
            }
        else:
            expected_front = c112.RAIL_ZERO
        if actual != expected_front:
            typed_failures.append((role, expected_front, actual))
    check("E04 D3 role controls expose only H0/H1 status or the separate ALL-to-R1 front", not typed_failures, str(typed_failures))
    return cases


def covariance_and_scope_contract(stopped_cases: list[tuple[str, dict[Coord, str]]]) -> None:
    section("F - Proper-cubic covariance and bounded claim discipline")
    failures = []
    controls = 0
    for local, values in FULL_RAW.items():
        for rotation in c53.ROTATIONS:
            controls += 1
            actual = FULL_RAW.get(c53.rotate_signature(local, rotation))
            if actual != values:
                failures.append((local, rotation, values, actual))
                break
    check(
        "F01 all 268,464 proper-cubic raw images preserve output",
        controls == len(FULL_RAW) * 24 == 268_464 and not failures,
        str(failures[:1]),
    )

    cases: list[tuple[str, dict[Coord, str], RawTable]] = [
        ("positive", positive_terminal_records(), FULL_RAW),
        ("alternate", alternate_terminal_records(), FULL_RAW),
        *((label, records, FULL_RAW) for label, records in stopped_cases),
    ]
    rotated_failures = []
    shift = (173, -109, 83)
    for label, records, raw in cases:
        completed, rail_failures = append_rail(records, raw)
        if rail_failures:
            rotated_failures.append((label, rail_failures[0]))
            continue
        for rotation in c53.ROTATIONS:
            transformed = c105.transform_records(completed, rotation, shift)
            next_site = c101.transform_site(c105.NEXT_RAIL[0], rotation, shift)
            expected = {next_site: frozenset((c105.NEXT_RAIL[1],))}
            actual = enabled(transformed, raw)
            if actual != expected:
                rotated_failures.append((label, rotation, expected, actual))
                break
    check(
        "F02 positive/alternate/stopped terminal rotations expose only next rail",
        len(cases) == 12 and not rotated_failures,
        str(rotated_failures[:1]),
    )

    note = NOTE.read_text(encoding="utf-8").lower() if NOTE.is_file() else ""
    check("F03 note names positive history and alternate history", "positive history" in note and "alternate history" in note)
    check("F04 note names Cycle 112 writer-only surface", "writer-only surface" in note)
    check("F05 note compares Cycle 115 completion", "cycle 115" in note and "alternate completion" in note)
    check("F06 note carries N1-N8 discipline", all(f"n{index}" in note for index in range(1, 9)))
    check(
        "F07 note avoids reusable/addressable overclaim",
        "not establish an addressable reusable harness" in note,
    )
    check("F08 note makes no axiom addition", "no axiom addition follows" in note)
    check(
        "F09 Cycle 113 writes only runner and review note",
        all(path.parent in (ROOT / "scripts", REVIEW) for path in (Path(__file__), NOTE)),
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    table_and_geometry_contract()
    graph_contract()
    history_and_comparison_contract()
    rail_contract()
    stopped_cases = corruption_contract()
    covariance_and_scope_contract(stopped_cases)
    product_states = POSITIVE.states * (c105.RAIL_HORIZON + 1)
    product_edges = POSITIVE.edges * (c105.RAIL_HORIZON + 1) + POSITIVE.states * c105.RAIL_HORIZON
    print(
        f"\nNEW_CANONICAL={len(NEW_TABLE)} NEW_RAW={len(NEW_RAW)} "
        f"UNION_RAW={len(FULL_RAW)} POSITIVE_WRITES={len(SELECTED_GROWN_OUTPUTS)}"
    )
    print(
        f"POSITIVE_STATES={POSITIVE.states} POSITIVE_EDGES={POSITIVE.edges} "
        f"ALTERNATE_STATES={ALTERNATE.states} ALTERNATE_EDGES={ALTERNATE.edges}"
    )
    print(
        f"C114_STATES={C114_GRAPH.states} C114_EDGES={C114_GRAPH.edges} "
        f"PRODUCT_STATES={product_states} PRODUCT_EDGES={product_edges}"
    )
    print(f"PASS={PASS} FAIL={FAIL}")
    print("RESULT=FIXED_WORD_STATUS_ALTERNATE_COMPLETION" if FAIL == 0 else "RESULT=FAIL")
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
