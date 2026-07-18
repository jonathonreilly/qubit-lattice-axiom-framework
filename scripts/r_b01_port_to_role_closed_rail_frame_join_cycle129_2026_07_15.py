#!/usr/bin/env python3
"""Cycle 129: join the generated R_B01 head to the renewed role rail.

Cycle 124 ends at a generated ``R_B01`` role port while the executable
campaign period-four rail exposes its first renewed slice.  Sixteen new
canonical rows grow a
finite phase-labelled bridge.  One row has two covariant images; every other
row has one.  A fresh two-parent guard removes the transient unary-GU aliases
found by the unguarded draft.  The final Y2 record literally sees both the
head-descended T_N0 phase and the first slice's B_0_2 frame role.

Every append ordering is exhausted from the exact 264-record source.  The
runner has no authority and edits no foundation, registry, queue, policy,
audit, or git state.
"""

from __future__ import annotations

from collections import deque
from pathlib import Path

import r_b00_completion_to_r_b01_role_allocator_common_port_cycle124_2026_07_15 as c124


ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / "docs" / "work_history" / "repo" / "review_feedback"
NOTE = REVIEW / "R_B01_PORT_TO_ROLE_CLOSED_RAIL_FRAME_JOIN_CYCLE129_NOTE_2026-07-15.md"

c121 = c124.c121
c119 = c124.c119
c112 = c124.c112
c105 = c124.c105
c101 = c124.c101
c53 = c124.c53
c59 = c124.c59

Coord = c124.Coord
Signature = c124.Signature
RawTable = c124.RawTable
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


# The first renewed 12-role slice is the physical frame consumed by CONTACT.
RAIL_SLICE = tuple(c105.RAIL_SEQUENCE[:12])
RAIL_OUTPUTS = dict(RAIL_SLICE)
NEXT_RAIL = c105.RAIL_SEQUENCE[12]
IGNORED_NEXT = {NEXT_RAIL[0]: frozenset((NEXT_RAIL[1],))}

# Each tuple is one canonical generation.  Generation 8 has two exact
# covariant images; neither is debris.  P_GUARD is the full-history repair:
# its fixed W1+T_N0 signature is absent at both transient unary-GU aliases.
GROUPS: tuple[tuple[tuple[Coord, ...], str], ...] = (
    (((5, 3, -3),), "OZ"),
    (((4, 3, -3),), "W3"),
    (((4, 2, -3),), "A_0_0"),
    (((3, 2, -3),), "A_1_2"),
    (((4, 3, -4),), "A_2_0"),
    (((4, 2, -4),), "A_3_1"),
    (((3, 2, -4),), "A_3_2"),
    (((2, 2, -4),), "COMPLETE"),
    (((1, 2, -4), (2, 3, -4)), "TY"),
    (((0, 2, -4),), "W4"),
    (((0, 2, -3),), "AUXZ"),
    (((0, 2, -2),), "GU"),
    (((-1, 3, -2),), "R_C01"),
    (((-1, 2, -2),), "JOINT"),
    (((-1, 2, -1),), "T_N0"),
    (((-2, 2, -1),), "Y2"),
)

P_GUARD: Coord = (-1, 3, -2)
P_GUARD_OUTPUT = "R_C01"
JOINT: Coord = (-1, 2, -2)
JOINT_OUTPUT = "JOINT"
HEAD_PHASE: Coord = (-1, 2, -1)
HEAD_PHASE_OUTPUT = "T_N0"
FRAME_PARENT: Coord = (-2, 2, 0)
FRAME_PARENT_OUTPUT = "B_0_2"
CONTACT: Coord = (-2, 2, -1)
CONTACT_OUTPUT = "Y2"

BRIDGE_OUTPUTS: dict[Coord, str] = {
    site: output
    for sites, output in GROUPS
    for site in sites
}


def build_table(
    groups: tuple[tuple[tuple[Coord, ...], str], ...],
    *,
    require_exact_matches: bool = True,
) -> tuple[
    dict[Signature, str],
    tuple[tuple[Coord, ...], ...],
    tuple[Signature, ...],
]:
    records = {**c124.positive_terminal_records(), **RAIL_OUTPUTS}
    table: dict[Signature, str] = {}
    observed: list[tuple[Coord, ...]] = []
    locals_seen: list[Signature] = []
    for declared, output in groups:
        local = c53.local_signature(records, declared[0])
        canonical = c53.canonical_signature(local)
        matches = tuple(sorted(
            site
            for site in c53.open_candidates(records)
            if c53.canonical_signature(c53.local_signature(records, site))
            == canonical
        ))
        if require_exact_matches and matches != tuple(sorted(declared)):
            raise RuntimeError((declared, matches, local, canonical))
        prior = table.get(canonical)
        if prior is not None and prior != output:
            raise RuntimeError((canonical, prior, output))
        table[canonical] = output
        # The guarded candidate construction writes every covariant match.  The
        # deliberately unguarded negative control instead advances only its
        # intended sites so the raw unary rule can be compiled against the
        # untouched old aliases below; those aliases are the failure being
        # measured, not part of the diagnostic construction.
        written = matches if require_exact_matches else tuple(sorted(declared))
        records.update({site: output for site in written})
        observed.append(matches)
        locals_seen.append(local)
    return table, tuple(observed), tuple(locals_seen)


BRIDGE_TABLE, OBSERVED_GROUPS, GROUP_LOCALS = build_table(GROUPS)
BRIDGE_RAW = c59.raw_rule_outputs(BRIDGE_TABLE)
FULL_RAW = c112.merge_raw(c124.FULL_RAW, BRIDGE_RAW)

# Exact negative control for the attractive draft that omitted P_GUARD.  Its
# completed-C124 factor has one extra unary-GU coimage, and the full campaign
# history has two additional transient unary-GU contexts.  Both resolutions
# are compiled explicitly below.
UNGUARDED_GROUPS = (*GROUPS[:12], *GROUPS[13:])
UNGUARDED_TABLE, _UNGUARDED_OBSERVED, _UNGUARDED_LOCALS = build_table(
    UNGUARDED_GROUPS,
    require_exact_matches=False,
)
UNGUARDED_RAW = c59.raw_rule_outputs(UNGUARDED_TABLE)
UNGUARDED_FULL_RAW = c112.merge_raw(c124.FULL_RAW, UNGUARDED_RAW)
UNGUARDED_BRIDGE_OUTPUTS = {
    site: output
    for sites, output in UNGUARDED_GROUPS
    for site in sites
}
UNGUARDED_GROWN_OUTPUTS = {
    **c124.GROWN_OUTPUTS,
    **RAIL_OUTPUTS,
    **UNGUARDED_BRIDGE_OUTPUTS,
}

FACTOR_OUTPUTS: dict[Coord, str] = {**RAIL_OUTPUTS, **BRIDGE_OUTPUTS}
GROWN_OUTPUTS: dict[Coord, str] = {**c124.GROWN_OUTPUTS, **FACTOR_OUTPUTS}
BASE_TERMINAL = c124.positive_terminal_records()
UNGUARDED_FACTOR_OUTPUTS = {
    **RAIL_OUTPUTS,
    **UNGUARDED_BRIDGE_OUTPUTS,
}


def enabled(records: dict[Coord, str], raw: RawTable = FULL_RAW):
    return {
        target: raw[local]
        for target in c53.open_candidates(records)
        if (local := c53.local_signature(records, target)) in raw
    }


FACTOR = c112.append_graph(
    source=BASE_TERMINAL,
    outputs=FACTOR_OUTPUTS,
    raw=FULL_RAW,
    ignored=IGNORED_NEXT,
)
ALL_FACTOR_MASK = (1 << len(FACTOR_OUTPUTS)) - 1

# Remove the exact launch orientation while leaving its other proper-cubic
# images in place.  This controlled symmetry fault must be detected and must
# prevent the tested factor from completing.
BROKEN_CUBIC_LOCAL = GROUP_LOCALS[0]
BROKEN_CUBIC_RAW = dict(FULL_RAW)
del BROKEN_CUBIC_RAW[BROKEN_CUBIC_LOCAL]
BROKEN_CUBIC_FACTOR = c112.append_graph(
    source=BASE_TERMINAL,
    outputs=FACTOR_OUTPUTS,
    raw=BROKEN_CUBIC_RAW,
    ignored=IGNORED_NEXT,
)

POSITIVE = c112.append_graph(
    source=c112.SOURCE,
    outputs=GROWN_OUTPUTS,
    raw=FULL_RAW,
    ignored=IGNORED_NEXT,
    state_limit=7_000_000,
)
ALL_GROWN_MASK = (1 << len(GROWN_OUTPUTS)) - 1

UNGUARDED_COMPILED = c112.compile_conditions(
    c112.SOURCE,
    UNGUARDED_GROWN_OUTPUTS,
    UNGUARDED_FULL_RAW,
    IGNORED_NEXT,
)
UNGUARDED_FACTOR_COMPILED = c112.compile_conditions(
    BASE_TERMINAL,
    UNGUARDED_FACTOR_OUTPUTS,
    UNGUARDED_FULL_RAW,
    IGNORED_NEXT,
)
UNGUARDED_GRAPH = c112.append_graph(
    source=c112.SOURCE,
    outputs=UNGUARDED_GROWN_OUTPUTS,
    raw=UNGUARDED_FULL_RAW,
    ignored=IGNORED_NEXT,
)


def positive_terminal_records() -> dict[Coord, str]:
    if POSITIVE.terminal_states != (ALL_GROWN_MASK,):
        raise RuntimeError(POSITIVE.terminal_states)
    return c112.records_at(ALL_GROWN_MASK, c112.SOURCE, GROWN_OUTPUTS)


def factor_contact_violations() -> tuple[int, ...]:
    """Require every primary bridge generation and B_0_2 before CONTACT."""
    compiled = c112.compile_conditions(
        BASE_TERMINAL,
        FACTOR_OUTPUTS,
        FULL_RAW,
        IGNORED_NEXT,
    )
    actions = tuple(
        (compiled.index.get(target), target, conditions)
        for target, conditions in compiled.conditions.items()
    )
    required = {sites[0] for sites, _output in GROUPS[:-1]} | {FRAME_PARENT}
    required_mask = sum(1 << compiled.index[site] for site in required)
    contact_bit = 1 << compiled.index[CONTACT]
    queue = deque((0,))
    seen = {0}
    violations: list[int] = []
    while queue:
        state = queue.popleft()
        if state & contact_bit and state & required_mask != required_mask:
            violations.append(state)
        legal: list[int] = []
        for index, target, conditions in actions:
            if index is not None and state >> index & 1:
                continue
            for present_mask, neighbourhood_mask, values in conditions:
                if state & neighbourhood_mask != present_mask:
                    continue
                if target in IGNORED_NEXT and values == IGNORED_NEXT[target]:
                    break
                if index is not None and values == frozenset((FACTOR_OUTPUTS[target],)):
                    legal.append(index)
                    break
                raise RuntimeError((state, target, values))
        for index in legal:
            future = state | 1 << index
            if future not in seen:
                seen.add(future)
                queue.append(future)
    return tuple(violations)


def append_to_eighth_slice(records: dict[Coord, str]):
    answer = dict(records)
    failures = []
    for prefix, (site, output) in enumerate(c105.RAIL_SEQUENCE[12:96], 12):
        actual = enabled(answer)
        expected = {site: frozenset((output,))}
        if actual != expected:
            failures.append((prefix, expected, actual))
            break
        answer[site] = output
    return answer, tuple(failures)


def table_contract() -> None:
    section("A - Exact phase bridge and guarded frame contact")
    check("A01 Cycle 129 note exists", NOTE.is_file())
    check(
        "A02 sixteen canonical rows expand to 366 proper-cubic raw rows",
        len(BRIDGE_TABLE) == 16
        and len(BRIDGE_RAW) == 366
        and all(len(values) == 1 for values in BRIDGE_RAW.values()),
        f"canonical={len(BRIDGE_TABLE)} raw={len(BRIDGE_RAW)}",
    )
    check(
        "A03 new raw domain is disjoint from Cycle 124",
        not (set(BRIDGE_RAW) & set(c124.FULL_RAW)),
    )
    check(
        "A04 9,110-row union is single-valued and alphabet-closed",
        len(FULL_RAW) == 9_110
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
        "A05 sixteen generations grow exactly seventeen physical bridge records",
        OBSERVED_GROUPS == tuple(tuple(sorted(sites)) for sites, _output in GROUPS)
        and len(BRIDGE_OUTPUTS) == 17,
    )
    check(
        "A06 first phase literally consumes the fresh R_B01 head",
        GROUP_LOCALS[0]
        == (((0, 0, 1), "H1"), ((0, 1, 0), c124.PORT_OUTPUT)),
        str(GROUP_LOCALS[0]),
    )
    check(
        "A07 fresh guard sees exactly fixed W1 and T_N0 parents",
        GROUP_LOCALS[12]
        == (((0, 0, 1), "W1"), ((1, 0, 0), "T_N0")),
        str(GROUP_LOCALS[12]),
    )
    check(
        "A08 JOINT is two-parent GU plus R_C01, never unary GU",
        set(value for _direction, value in GROUP_LOCALS[13])
        == {"GU", P_GUARD_OUTPUT}
        and len(GROUP_LOCALS[13]) == 2,
        str(GROUP_LOCALS[13]),
    )
    check(
        "A09 final Y2 literally joins T_N0 head phase to B_0_2 frame",
        GROUP_LOCALS[15]
        == (((0, 0, 1), FRAME_PARENT_OUTPUT), ((1, 0, 0), HEAD_PHASE_OUTPUT)),
        str(GROUP_LOCALS[15]),
    )


def graph_contract() -> None:
    section("B - Post-head factor and exact full-history exhaustion")
    factor_compiled = c112.compile_conditions(
        BASE_TERMINAL, FACTOR_OUTPUTS, FULL_RAW, IGNORED_NEXT
    )
    full_compiled = c112.compile_conditions(
        c112.SOURCE, GROWN_OUTPUTS, FULL_RAW, IGNORED_NEXT
    )
    check(
        "B01 factor compiler has 30 targets and zero unexpected target",
        len(factor_compiled.conditions) == 30
        and not factor_compiled.unexpected_targets,
        f"conditions={len(factor_compiled.conditions)} unexpected={factor_compiled.unexpected_targets}",
    )
    check(
        "B02 post-C124 factor is 618 states / 1,653 edges / one 29-write terminal",
        FACTOR.states == 618
        and FACTOR.edges == 1_653
        and FACTOR.terminals == 1
        and FACTOR.terminal_states == (ALL_FACTOR_MASK,)
        and FACTOR.terminal_sizes == (29,)
        and FACTOR.max_frontier == 4
        and not FACTOR.bad
        and len(FACTOR.reached) == 29,
        f"states={FACTOR.states} edges={FACTOR.edges} terminals={FACTOR.terminals} max={FACTOR.max_frontier}",
    )
    check(
        "B03 full compiler has 131 targets and zero unexpected target",
        len(full_compiled.conditions) == 131
        and not full_compiled.unexpected_targets,
        f"conditions={len(full_compiled.conditions)} unexpected={full_compiled.unexpected_targets}",
    )
    check(
        "B04 all full histories reach one complete 130-write terminal",
        len(GROWN_OUTPUTS) == 130
        and POSITIVE.states == 6_541_456
        and POSITIVE.edges == 51_107_588
        and POSITIVE.terminals == 1
        and POSITIVE.terminal_states == (ALL_GROWN_MASK,)
        and POSITIVE.terminal_sizes == (130,)
        and POSITIVE.max_frontier == 14
        and not POSITIVE.bad
        and not POSITIVE.unexpected_condition_targets
        and len(POSITIVE.reached) == 130,
        f"states={POSITIVE.states} edges={POSITIVE.edges} terminals={POSITIVE.terminals} max={POSITIVE.max_frontier} bad={POSITIVE.bad[:1]}",
    )
    violations = factor_contact_violations()
    check(
        "B05 CONTACT never precedes any primary head phase or B_0_2 frame parent",
        not violations,
        str(violations[:1]),
    )
    terminal = positive_terminal_records()
    check(
        "B06 complete bridge leaves only the next ordered rail record",
        enabled(terminal) == {NEXT_RAIL[0]: frozenset((NEXT_RAIL[1],))},
        str(enabled(terminal)),
    )


def rail_and_covariance_contract() -> None:
    section("C - Continued renewal, late rail, and proper-cubic covariance")
    records, failures = append_to_eighth_slice(positive_terminal_records())
    check(
        "C01 remaining 84 writes through eight slices stay singleton fronts",
        not failures
        and enabled(records)
        == {c105.RAIL_SEQUENCE[96][0]: frozenset((c105.RAIL_SEQUENCE[96][1],))},
        str(failures[:1]),
    )

    long_rail = c105.c108.c104.rail_sequence(102, c105.ROLE_MAP)
    late = positive_terminal_records()
    late_failures = []
    for prefix in range(12, 101 * 12):
        site, output = long_rail[prefix]
        actual = enabled(late)
        expected = {site: frozenset((output,))}
        if actual != expected:
            late_failures.append((prefix, expected, actual))
            break
        late[site] = output
    next_site, next_output = long_rail[101 * 12]
    check(
        "C02 late control reaches 101 complete slices / 1,212 rail records",
        not late_failures
        and len(late) == 1_594
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
        "C03 all 218,640 proper-cubic raw images preserve output",
        controls == len(FULL_RAW) * 24 == 218_640
        and not covariance_failures,
        str(covariance_failures[:1]),
    )

    shift = (211, -149, 127)
    rotated_failures = []
    for rotation in c53.ROTATIONS:
        transformed = c105.transform_records(records, rotation, shift)
        rotated_next = c101.transform_site(c105.RAIL_SEQUENCE[96][0], rotation, shift)
        expected = {
            rotated_next: frozenset((c105.RAIL_SEQUENCE[96][1],))
        }
        actual = enabled(transformed)
        if actual != expected:
            rotated_failures.append((rotation, expected, actual))
            break
    check(
        "C04 every rotated completed history exposes only rotated ninth-slice start",
        not rotated_failures,
        str(rotated_failures[:1]),
    )

    broken_mismatches = []
    for local, values in FULL_RAW.items():
        for rotation in c53.ROTATIONS:
            rotated = c53.rotate_signature(local, rotation)
            if BROKEN_CUBIC_RAW.get(rotated) != values:
                broken_mismatches.append((local, rotation, rotated))
    check(
        "C05 deleting one launch orientation is detected and blocks the factor",
        bool(broken_mismatches)
        and ALL_FACTOR_MASK not in BROKEN_CUBIC_FACTOR.terminal_states
        and GROUPS[0][0][0] not in BROKEN_CUBIC_FACTOR.reached,
        f"mismatches={len(broken_mismatches)} terminals={BROKEN_CUBIC_FACTOR.terminal_sizes}",
    )


def causal_controls() -> None:
    section("D - Head absence and two-parent guard controls")
    without_head = dict(BASE_TERMINAL)
    without_head.pop(c124.PORT)
    no_head_failures = []
    for prefix, (site, output) in enumerate(RAIL_SLICE):
        actual = enabled(without_head)
        head_dependent = set(BRIDGE_OUTPUTS) - {P_GUARD}
        if set(actual) & head_dependent:
            no_head_failures.append((prefix, actual))
            break
        if actual.get(site) != frozenset((output,)):
            no_head_failures.append((prefix, site, output, actual))
            break
        without_head[site] = output
    check(
        "D01 removing R_B01 leaves only preallocated guard, not head-descended bridge",
        not no_head_failures
        and enabled(without_head).get(P_GUARD)
        == frozenset((P_GUARD_OUTPUT,))
        and not (set(enabled(without_head)) & head_dependent),
        str(no_head_failures[:1]),
    )

    prefix = {**BASE_TERMINAL, **RAIL_OUTPUTS}
    for sites, output in GROUPS[:12]:
        prefix.update({site: output for site in sites})
    before = enabled(prefix)
    prefix[P_GUARD] = P_GUARD_OUTPUT
    after = enabled(prefix)
    check(
        "D02 GU alone cannot write JOINT; adding W1+T_N0 guard enables it",
        JOINT not in before
        and before.get(P_GUARD) == frozenset((P_GUARD_OUTPUT,))
        and after.get(JOINT) == frozenset((JOINT_OUTPUT,)),
        f"before_joint={before.get(JOINT)} guard={before.get(P_GUARD)} after_joint={after.get(JOINT)}",
    )

    no_frame = {**BASE_TERMINAL}
    for sites, output in GROUPS[:-1]:
        no_frame.update({site: output for site in sites})
    check(
        "D03 head phase without B_0_2 cannot write final frame contact",
        CONTACT not in enabled(no_frame),
        str(enabled(no_frame).get(CONTACT)),
    )

    terminal_aliases = frozenset(((3, 2, 5),))
    transient_aliases = frozenset(((3, 3, 4), (5, 2, 3)))
    unguarded_aliases = terminal_aliases | transient_aliases
    check(
        "D04 unguarded compiler partitions one terminal and two transient aliases",
        all(len(values) == 1 for values in UNGUARDED_FULL_RAW.values())
        and UNGUARDED_FACTOR_COMPILED.unexpected_targets == terminal_aliases
        and UNGUARDED_COMPILED.unexpected_targets == unguarded_aliases,
        f"factor={tuple(sorted(UNGUARDED_FACTOR_COMPILED.unexpected_targets))} "
        f"full={tuple(sorted(UNGUARDED_COMPILED.unexpected_targets))}",
    )
    first_bad = UNGUARDED_GRAPH.bad[:1]
    check(
        "D05 unguarded full graph rejects a JOINT alias at source state zero",
        UNGUARDED_GRAPH.states == 1
        and UNGUARDED_GRAPH.edges == 0
        and UNGUARDED_GRAPH.terminals == 0
        and bool(first_bad)
        and first_bad[0][0] == 0
        and first_bad[0][1] in unguarded_aliases
        and first_bad[0][2] == frozenset((JOINT_OUTPUT,)),
        str(first_bad),
    )


def scope_contract() -> None:
    section("E - Exact scope and constitutional boundary")
    note = NOTE.read_text(encoding="utf-8").lower() if NOTE.is_file() else ""
    check(
        "E01 note names the exact bounded positive",
        "r_b01_port_to_role_closed_rail_frame_join" in note,
    )
    check(
        "E02 note preserves post-terminal factor separately from full history",
        "factor reachable states" in note
        and "full reachable states" in note
        and "6,541,456" in note,
    )
    check(
        "E03 note carries refreshed N1-N8 discipline",
        all(f"n{index}" in note for index in range(1, 9)),
    )
    check(
        "E04 note denies recurrence theorem and exact-law selection",
        "recurrence theorem" in note and "does not select" in note,
    )
    check(
        "E05 note makes no axiom addition",
        "no axiom addition follows" in note,
    )
    check(
        "E06 Cycle 129 writes only runner and review note",
        all(path.parent in (ROOT / "scripts", REVIEW) for path in (Path(__file__), NOTE)),
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    table_contract()
    graph_contract()
    rail_and_covariance_contract()
    causal_controls()
    scope_contract()
    print(
        f"\nBRIDGE_CANONICAL={len(BRIDGE_TABLE)} BRIDGE_RAW={len(BRIDGE_RAW)} "
        f"BRIDGE_RECORDS={len(BRIDGE_OUTPUTS)} UNION_RAW={len(FULL_RAW)}"
    )
    print(
        f"FACTOR_STATES={FACTOR.states} FACTOR_EDGES={FACTOR.edges} "
        f"FULL_STATES={POSITIVE.states} FULL_EDGES={POSITIVE.edges}"
    )
    print(f"PASS={PASS} FAIL={FAIL}")
    print(
        "RESULT=R_B01_PORT_TO_ROLE_CLOSED_RAIL_FRAME_JOIN"
        if FAIL == 0
        else "RESULT=FAIL"
    )
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
