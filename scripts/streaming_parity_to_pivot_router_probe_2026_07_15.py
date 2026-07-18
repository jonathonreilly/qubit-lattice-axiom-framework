#!/usr/bin/env python3
"""Test recurrent XOR selectors feeding the four-case pivot controller core."""

from __future__ import annotations

import physical_three_row_dual_commutation_bind_probe_2026_07_15 as prior
import physical_case_role_isolation_cable_probe_2026_07_15 as isolation


pivot = prior.ported.terminal.pivot
alu = prior.comm.alu
cable = prior.cable
d = prior.d
c53 = prior.c53
MERGED_RAW = isolation.MERGED_RAW
FRAME = prior.FRAME
Coord = tuple[int, int, int]
CHAIN_SHIFTS = ((-60, 0, 60), (60, 0, 60))
ROUTER_SHIFT = (0, 0, 0)


def add(left: Coord, right: Coord) -> Coord:
    return tuple(a + b for a, b in zip(left, right))  # type: ignore[return-value]


def sub(left: Coord, right: Coord) -> Coord:
    return tuple(a - b for a, b in zip(left, right))  # type: ignore[return-value]


def shift_records(records: dict[Coord, str], shift: Coord):
    return {add(site, shift): role for site, role in records.items()}


def place(records: dict[Coord, str], site: Coord, role: str) -> None:
    prior_role = records.get(site)
    if prior_role is not None and prior_role != role:
        raise ValueError((site, prior_role, role))
    records[site] = role


def line_to(path: list[Coord], target: Coord, axes=(0, 1, 2)) -> None:
    current = list(path[-1])
    for axis in axes:
        while current[axis] != target[axis]:
            current[axis] += 1 if target[axis] > current[axis] else -1
            point = tuple(current)  # type: ignore[assignment]
            if point in path:
                raise ValueError(("path-self-contact", point, target))
            path.append(point)


def selector_paths():
    finals = tuple(add(alu.value_site(3), shift) for shift in CHAIN_SHIFTS)
    c1 = add(pivot.CASE_INPUTS["c1"], ROUTER_SHIFT)
    c2 = add(pivot.CASE_INPUTS["c2"], ROUTER_SHIFT)

    first = [finals[0], add(finals[0], (0, 0, -1))]
    first.extend((add(finals[0], (0, 0, -2)), add(finals[0], (0, 0, -3))))
    line_to(first, (first[-1][0], -30, first[-1][2]), (1,))
    line_to(first, (0, -30, first[-1][2]), (0,))
    line_to(first, (0, 0, first[-1][2]), (1,))
    line_to(first, c1, (2,))

    second = [finals[1], add(finals[1], (0, 0, -1))]
    second.extend((add(finals[1], (0, 0, -2)), add(finals[1], (0, 0, -3))))
    line_to(second, (second[-1][0], second[-1][1], 12), (2,))
    line_to(second, (second[-1][0], 30, 12), (1,))
    line_to(second, (-12, 30, 12), (0,))
    line_to(second, (-12, 30, 0), (2,))
    line_to(second, (-12, 0, 0), (1,))
    line_to(second, c2, (0,))

    case_site = add(pivot.CASE_SITE, ROUTER_SHIFT)
    if add(first[-1], sub(first[-1], first[-2])) != case_site:
        raise ValueError(("wrong-c1-terminal", first[-2:], case_site))
    if add(second[-1], sub(second[-1], second[-2])) != case_site:
        raise ValueError(("wrong-c2-terminal", second[-2:], case_site))
    return tuple(first), tuple(second)


PATHS = selector_paths()
REMOTE_LANES = ((-40, -40, -40), (40, -40, -40))


def isolated_case_paths():
    case_site = add(pivot.CASE_SITE, ROUTER_SHIFT)
    first = [case_site, add(pivot.LANE1, ROUTER_SHIFT)]
    line_to(first, (0, 0, -10), (2,))
    line_to(first, (-40, 0, -10), (0,))
    line_to(first, (-40, -40, -10), (1,))
    line_to(first, add(REMOTE_LANES[0], (0, 0, 1)), (2,))

    second = [case_site, add(pivot.LANE2, ROUTER_SHIFT)]
    line_to(second, (0, -10, 0), (1,))
    line_to(second, (40, -10, 0), (0,))
    line_to(second, (40, -10, -40), (2,))
    line_to(second, add(REMOTE_LANES[1], (0, 1, 0)), (1,))

    terminals = (
        add(first[-1], sub(first[-1], first[-2])),
        add(second[-1], sub(second[-1], second[-2])),
    )
    if terminals != REMOTE_LANES:
        raise ValueError(("wrong-isolated-lane-terminals", terminals, REMOTE_LANES))
    return tuple(first), tuple(second)


CASE_PATHS = isolated_case_paths()
_ROUTING_CACHE = None


def chain(bits, shift):
    program = tuple((0, bit) for bit in bits[1:])
    source, expected, result = alu.apparatus(bits[0], program)
    source = shift_records(source, shift)
    port = add(alu.value_site(4), shift)
    # The standalone ALU terminator frames the unused next cell.  This
    # composition consumes that port, so its cable guides are solved jointly.
    for direction in c53.DIRECTIONS:
        source.pop(add(port, direction), None)
    return source, shift_records(expected, shift), result


def apparatus(g1, g2, measured):
    global _ROUTING_CACHE
    selector_bits = (
        tuple(prior.comm.term_values(g1, measured)),
        tuple(prior.comm.term_values(g2, measured)),
    )
    records: dict[Coord, str] = {}
    expected: dict[Coord, str] = {}
    dependencies: dict[Coord, frozenset[Coord]] = {}
    selector_values = []
    for bits, shift in zip(selector_bits, CHAIN_SHIFTS, strict=True):
        source, outputs, result = chain(bits, shift)
        for site, role in source.items():
            place(records, site, role)
        prior_target = None
        for target, role in outputs.items():
            expected[target] = role
            dependencies[target] = (
                frozenset() if prior_target is None else frozenset((prior_target,))
            )
            prior_target = target
        selector_values.append(alu.bit(result))

    c_inputs = {
        add(pivot.CASE_INPUTS["c1"], ROUTER_SHIFT),
        add(pivot.CASE_INPUTS["c2"], ROUTER_SHIFT),
    }
    case = pivot.pivot_rows(g1, g2, measured)[0]
    case_role = pivot.CASE_ROLE[case]
    first_selector, second_selector = pivot.LANE_OUTPUT[case]
    lane1, lane2 = REMOTE_LANES
    router_source = {
        add(pivot.CASE_INPUTS["mark"], ROUTER_SHIFT): FRAME,
        add(pivot.CASE_INPUTS["start"], ROUTER_SHIFT): d.START_ROLE,
        add(lane1, (0, 1, 0)): pivot.LANE_ROLES[0],
        add(lane1, (0, -1, 0)): FRAME,
        add(lane1, (0, 0, -1)): FRAME,
        add(lane2, (0, 0, 1)): pivot.LANE_ROLES[1],
        add(lane2, (0, 0, -1)): FRAME,
    }
    open_sockets = {
        add(lane1, (1, 0, 0)),
        add(lane1, (-1, 0, 0)),
        add(lane2, (1, 0, 0)),
        add(lane2, (-1, 0, 0)),
        add(lane2, (0, -1, 0)),
    }
    for site, role in router_source.items():
        place(records, site, role)

    case_site = add(pivot.CASE_SITE, ROUTER_SHIFT)
    router_expected = {
        case_site: case_role,
        lane1: first_selector,
        lane2: second_selector,
    }
    items = (
        *tuple(zip(selector_values, PATHS, strict=True)),
        *((case_role, path) for path in CASE_PATHS),
    )
    protected = {
        site for _value, path in items for site in path
    } | set(expected) | set(router_expected) | open_sockets
    starts = {path[0] for _value, path in items}
    if _ROUTING_CACHE is None:
        chosen, _cable_outputs, terminal_ports = cable.multi_path_core(
            items, constraints=records, extra_protected=frozenset(protected)
        )
        scaffold = {
            site: role for site, role in chosen.items()
            if site not in records and site not in starts
        }
        if set(scaffold.values()) - {FRAME, cable.GUIDE_ROLE}:
            raise ValueError(("nonstructural-scaffold", set(scaffold.values())))
        _ROUTING_CACHE = scaffold, terminal_ports
    scaffold, terminal_ports = _ROUTING_CACHE
    for site, role in scaffold.items():
        if site not in records:
            place(records, site, role)
    cable_outputs = {}
    for value, path in items:
        for target in path[1:]:
            prior_cable = cable_outputs.get(target)
            if prior_cable is not None and prior_cable != value:
                raise ValueError((target, prior_cable, value, "cable-conflict"))
            cable_outputs[target] = value
            prior_role = expected.get(target)
            if prior_role is not None and prior_role != value:
                raise ValueError((target, prior_role, value, "expected-conflict"))
            expected[target] = value
        for previous, target in zip(path, path[1:]):
            dependencies[target] = frozenset((previous,))
    if set(cable_outputs) - set(expected):
        raise ValueError(("untracked-cable", set(cable_outputs) - set(expected)))
    wanted_ports = frozenset((case_site, lane1, lane2))
    if terminal_ports != wanted_ports:
        raise ValueError(("wrong-terminal", terminal_ports, wanted_ports))

    expected.update(router_expected)
    dependencies[case_site] = frozenset(c_inputs)
    dependencies[lane1] = frozenset((CASE_PATHS[0][-1],))
    dependencies[lane2] = frozenset((CASE_PATHS[1][-1],))

    core = set(records) | set(expected) | open_sockets
    cage = {
        add(site, direction)
        for site in core
        for direction in c53.DIRECTIONS
        if add(site, direction) not in core
    }
    for site in cage:
        place(records, site, FRAME)
    for site in set(expected) | open_sockets:
        records.pop(site, None)
    return records, expected, dependencies


def enabled(records):
    return {
        target: MERGED_RAW[signature]
        for target in c53.open_candidates(records)
        if (signature := c53.local_signature(records, target)) in MERGED_RAW
    }


def deterministic_run(g1, g2, measured, rotation=None):
    initial, expected, dependencies = apparatus(g1, g2, measured)
    if rotation is not None:
        shift = (487, -491, 499)
        initial = c53.transform_records(initial, rotation, shift)
        expected = c53.transform_records(expected, rotation, shift)
        dependencies = {
            next(iter(c53.transform_records({site: "x"}, rotation, shift))): frozenset(
                next(iter(c53.transform_records({parent: "x"}, rotation, shift)))
                for parent in parents
            )
            for site, parents in dependencies.items()
        }
    records = dict(initial)
    formed = set()
    actual = enabled(records)
    edges = 0
    maximum = 0
    while len(formed) < len(expected):
        frontier = {
            target: frozenset((expected[target],))
            for target, parents in dependencies.items()
            if target not in formed and parents <= formed
        }
        maximum = max(maximum, len(frontier))
        if actual != frontier:
            return False, (len(formed), actual, frontier, len(initial), len(expected))
        target = min(frontier)
        records[target] = expected[target]
        formed.add(target)
        edges += len(frontier)
        actual.pop(target, None)
        for direction in c53.DIRECTIONS:
            candidate = add(target, direction)
            if candidate in records:
                actual.pop(candidate, None)
                continue
            signature = c53.local_signature(records, candidate)
            if signature in MERGED_RAW:
                actual[candidate] = MERGED_RAW[signature]
            else:
                actual.pop(candidate, None)
    return (not actual, (len(expected) + 1, edges, maximum, len(initial), len(expected), actual))


def main() -> int:
    g1 = (1, 0, 0, 1, 0)
    g2 = (0, 1, 1, 0, 1)
    measured = (1, 1, 0, 1, 0)
    try:
        ok, detail = deterministic_run(g1, g2, measured)
    except ValueError as error:
        print("LAYOUT_FAILURE", str(error)[:8_000])
        print("RESULT", "OPEN")
        return 1
    print("PATHS", tuple(map(len, PATHS)), len(set(PATHS[0]) | set(PATHS[1])))
    print("SMOKE", ok, detail)
    print("RESULT", "STREAMING_PARITY_TO_PIVOT_CONTROLLER" if ok else "OPEN")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
