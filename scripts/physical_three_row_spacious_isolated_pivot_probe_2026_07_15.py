#!/usr/bin/env python3
"""Drive the isolated pivot controller from three physical row records."""

from __future__ import annotations

from functools import lru_cache
from itertools import combinations

import physical_three_row_spacious_commutator_bind_probe_2026_07_15 as bound
import streaming_parity_to_pivot_router_probe_2026_07_15 as controller


pivot = controller.pivot
cable = controller.cable
d = controller.d
c53 = controller.c53
FRAME = controller.FRAME
MERGED_RAW = bound.MERGED_RAW
Coord = tuple[int, int, int]
CONTROLLER_SHIFT = (0, 360, 0)


def add(left: Coord, right: Coord) -> Coord:
    return tuple(a + b for a, b in zip(left, right))  # type: ignore[return-value]


def sub(left: Coord, right: Coord) -> Coord:
    return tuple(a - b for a, b in zip(left, right))  # type: ignore[return-value]


def shift_records(records: dict[Coord, str], shift: Coord):
    return {add(site, shift): role for site, role in records.items()}


def place(records: dict[Coord, str], site: Coord, role: str) -> None:
    previous = records.get(site)
    if previous is not None and previous != role:
        raise ValueError((site, previous, role))
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
    sources = tuple(
        add(bound.spacious.XOR_CENTERS[-1], shift)
        for shift in bound.COMM_SHIFTS
    )
    c1 = add(pivot.CASE_INPUTS["c1"], CONTROLLER_SHIFT)
    c2 = add(pivot.CASE_INPUTS["c2"], CONTROLLER_SHIFT)

    first = [sources[0], add(sources[0], (0, 0, -1)), add(sources[0], (0, 0, -2))]
    line_to(first, (first[-1][0], first[-1][1], -70), (2,))
    line_to(first, (first[-1][0], 330, -70), (1,))
    line_to(first, (0, 330, -70), (0,))
    line_to(first, (0, 330, 2), (2,))
    line_to(first, (0, 360, 2), (1,))
    line_to(first, c1, (2,))

    second = [sources[1], add(sources[1], (0, 0, -1)), add(sources[1], (0, 0, -2))]
    line_to(second, (second[-1][0], second[-1][1], -90), (2,))
    line_to(second, (second[-1][0], 400, -90), (1,))
    line_to(second, (-2, 400, -90), (0,))
    line_to(second, (-2, 400, 0), (2,))
    line_to(second, (-2, 360, 0), (1,))
    line_to(second, c2, (0,))

    case_site = add(pivot.CASE_SITE, CONTROLLER_SHIFT)
    if add(first[-1], sub(first[-1], first[-2])) != case_site:
        raise ValueError(("wrong-c1-terminal", first[-2:], case_site))
    if add(second[-1], sub(second[-1], second[-2])) != case_site:
        raise ValueError(("wrong-c2-terminal", second[-2:], case_site))
    return tuple(first), tuple(second)


SELECTOR_PATHS = selector_paths()
CASE_PATHS = tuple(
    tuple(add(site, CONTROLLER_SHIFT) for site in path)
    for path in controller.CASE_PATHS
)
REMOTE_LANES = tuple(add(site, CONTROLLER_SHIFT) for site in controller.REMOTE_LANES)


def controller_fixed():
    lane1, lane2 = REMOTE_LANES
    return {
        add(pivot.CASE_INPUTS["mark"], CONTROLLER_SHIFT): FRAME,
        add(pivot.CASE_INPUTS["start"], CONTROLLER_SHIFT): d.START_ROLE,
        add(lane1, (0, 1, 0)): pivot.LANE_ROLES[0],
        add(lane1, (0, -1, 0)): FRAME,
        add(lane1, (0, 0, -1)): FRAME,
        add(lane2, (0, 0, 1)): pivot.LANE_ROLES[1],
        add(lane2, (0, 0, -1)): FRAME,
    }


def open_sockets():
    lane1, lane2 = REMOTE_LANES
    return frozenset((
        add(lane1, (1, 0, 0)),
        add(lane1, (-1, 0, 0)),
        add(lane2, (1, 0, 0)),
        add(lane2, (-1, 0, 0)),
        add(lane2, (0, -1, 0)),
    ))


def path_items(g1, g2, measured):
    results = tuple(
        bound.comm.alu.compact.algebra.symplectic(generator, measured)
        for generator in (g1, g2)
    )
    case = pivot.pivot_rows(g1, g2, measured)[0]
    case_role = pivot.CASE_ROLE[case]
    return (
        (d.H1 if results[0] else d.H0, SELECTOR_PATHS[0]),
        (d.H1 if results[1] else d.H0, SELECTOR_PATHS[1]),
        (case_role, CASE_PATHS[0]),
        (case_role, CASE_PATHS[1]),
    )


@lru_cache(maxsize=1)
def routing_scaffold():
    zero = (0, 0, 0, 0, 0)
    records, expected, _dependencies, _results, _ports = bound.uncaged_apparatus(
        zero, zero, zero
    )
    for site, role in controller_fixed().items():
        place(records, site, role)
    items = path_items(zero, zero, zero)
    protected = frozenset(set(expected) | set(open_sockets()) | set(REMOTE_LANES))
    scaffold, terminal_ports = bound.sequential_routing_scaffold(
        items, records, protected
    )
    case_site = add(pivot.CASE_SITE, CONTROLLER_SHIFT)
    required = {case_site, *REMOTE_LANES}
    if not required <= set(terminal_ports):
        raise ValueError(("missing-controller-ports", required - set(terminal_ports)))
    return scaffold, terminal_ports


def apparatus(g1, g2, measured):
    records, expected, dependencies, results, _final_ports = bound.uncaged_apparatus(
        g1, g2, measured
    )
    for site, role in controller_fixed().items():
        place(records, site, role)
    scaffold, terminal_ports = routing_scaffold()
    for site, role in scaffold.items():
        place(records, site, role)

    items = path_items(g1, g2, measured)
    for value, path in items:
        for target in path[1:]:
            previous = expected.get(target)
            if previous is not None and previous != value:
                raise ValueError((target, previous, value, "controller-path-conflict"))
            expected[target] = value
        for previous, target in zip(path, path[1:]):
            dependencies[target] = frozenset((previous,))

    case = pivot.pivot_rows(g1, g2, measured)[0]
    case_site = add(pivot.CASE_SITE, CONTROLLER_SHIFT)
    c_inputs = frozenset((
        add(pivot.CASE_INPUTS["c1"], CONTROLLER_SHIFT),
        add(pivot.CASE_INPUTS["c2"], CONTROLLER_SHIFT),
    ))
    expected[case_site] = pivot.CASE_ROLE[case]
    dependencies[case_site] = c_inputs
    lane_outputs = pivot.LANE_OUTPUT[case]
    for lane, output, path in zip(REMOTE_LANES, lane_outputs, CASE_PATHS, strict=True):
        expected[lane] = output
        dependencies[lane] = frozenset((path[-1],))

    required = {case_site, *REMOTE_LANES}
    if not required <= set(terminal_ports):
        raise ValueError(("wrong-controller-ports", required - set(terminal_ports)))
    sockets = open_sockets()
    core = set(records) | set(expected) | set(sockets)
    cage = {
        add(site, direction)
        for site in core
        for direction in c53.DIRECTIONS
        if add(site, direction) not in core
    }
    for site in cage:
        place(records, site, FRAME)
    for site in set(expected) | set(sockets):
        records.pop(site, None)
    return records, expected, dependencies, results, case, lane_outputs, sockets


def enabled(records):
    return {
        target: MERGED_RAW[signature]
        for target in c53.open_candidates(records)
        if (signature := c53.local_signature(records, target)) in MERGED_RAW
    }


def execute(prepared, rotation=None):
    initial, expected, dependencies, results, case, lane_outputs, sockets = prepared
    if rotation is not None:
        shift = (601, -607, 613)

        def moved(site):
            return add(c53.matvec(rotation, site), shift)

        initial = c53.transform_records(initial, rotation, shift)
        expected = c53.transform_records(expected, rotation, shift)
        dependencies = {
            moved(site): frozenset(moved(parent) for parent in parents)
            for site, parents in dependencies.items()
        }
        sockets = frozenset(moved(site) for site in sockets)
    records = dict(initial)
    formed = set()
    actual = enabled(records)
    maximum = 0
    edges = 0
    while len(formed) < len(expected):
        frontier = {
            target: frozenset((expected[target],))
            for target, parents in dependencies.items()
            if target not in formed and parents <= formed
        }
        maximum = max(maximum, len(frontier))
        if actual != frontier:
            return False, (
                len(formed), actual, frontier, len(initial), len(expected), results, case
            )
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
    return (
        not actual and not (set(sockets) & set(records)),
        (
            len(expected) + 1,
            edges,
            maximum,
            len(initial),
            len(expected),
            results,
            case,
            lane_outputs,
            actual,
        ),
    )


def deterministic_run(g1, g2, measured, rotation=None):
    return execute(apparatus(g1, g2, measured), rotation=rotation)


def subsets(items):
    items = tuple(items)
    for size in range(len(items) + 1):
        yield from combinations(items, size)


def local_schedule_proof(prepared):
    initial, expected, dependencies, _results, _case, _lane_outputs, _sockets = prepared

    ancestry_cache = {}

    def is_ancestor(ancestor, site):
        key = (ancestor, site)
        if key in ancestry_cache:
            return ancestry_cache[key]
        stack = [site]
        seen = set()
        result = False
        while stack:
            current = stack.pop()
            if current in seen:
                continue
            seen.add(current)
            parents = dependencies.get(current, frozenset())
            if ancestor in parents:
                result = True
                break
            for parent in parents:
                cached = ancestry_cache.get((ancestor, parent))
                if cached is True:
                    result = True
                    stack.clear()
                    break
                if cached is not False:
                    stack.append(parent)
        ancestry_cache[key] = result
        return result

    failures = []
    cases = 0
    for target, output in expected.items():
        fixed = {
            site: initial[site]
            for direction in c53.DIRECTIONS
            if (site := add(target, direction)) in initial
        }
        neighboring_expected = tuple(
            site
            for direction in c53.DIRECTIONS
            if (site := add(target, direction)) in expected
        )
        variable = tuple(
            site for site in neighboring_expected if not is_ancestor(target, site)
        )
        for present_tuple in subsets(variable):
            present = frozenset(present_tuple)
            if any(
                is_ancestor(ancestor, site) and ancestor not in present
                for site in present
                for ancestor in variable
            ):
                continue
            local_records = {**fixed, **{site: expected[site] for site in present}}
            signature = c53.local_signature(local_records, target)
            actual = MERGED_RAW.get(signature, frozenset())
            wanted = (
                frozenset((output,))
                if dependencies[target] <= present
                else frozenset()
            )
            cases += 1
            if actual != wanted:
                failures.append(("target", target, present, actual, wanted, signature))
                if len(failures) >= 20:
                    return cases, tuple(failures)

    universe = set(initial) | set(expected)
    outside = {
        add(site, direction)
        for site in expected
        for direction in c53.DIRECTIONS
        if add(site, direction) not in universe
    }
    for target in outside:
        fixed = {
            site: initial[site]
            for direction in c53.DIRECTIONS
            if (site := add(target, direction)) in initial
        }
        variable = tuple(
            site
            for direction in c53.DIRECTIONS
            if (site := add(target, direction)) in expected
        )
        for present_tuple in subsets(variable):
            present = frozenset(present_tuple)
            if any(
                is_ancestor(ancestor, site) and ancestor not in present
                for site in present
                for ancestor in variable
            ):
                continue
            local_records = {**fixed, **{site: expected[site] for site in present}}
            signature = c53.local_signature(local_records, target)
            actual = MERGED_RAW.get(signature, frozenset())
            cases += 1
            if actual:
                failures.append(("outside", target, present, actual, signature))
                if len(failures) >= 20:
                    return cases, tuple(failures)
    return cases, tuple(failures)


def main() -> int:
    g1 = (1, 0, 0, 1, 0)
    g2 = (0, 1, 1, 0, 1)
    measured = (1, 1, 0, 1, 0)
    try:
        ok, detail = deterministic_run(g1, g2, measured)
    except ValueError as error:
        print("LAYOUT_FAILURE", str(error)[:12_000])
        print("RESULT", "OPEN")
        return 1
    wanted_results = tuple(
        bound.comm.alu.compact.algebra.symplectic(generator, measured)
        for generator in (g1, g2)
    )
    wanted_case = pivot.pivot_rows(g1, g2, measured)[0]
    print("SELECTOR_PATH_LENGTHS", tuple(map(len, SELECTOR_PATHS)))
    print("SMOKE", ok, detail, "WANTED", wanted_results, wanted_case)
    result = ok and detail[5] == wanted_results and detail[6] == wanted_case
    print("RESULT", "PHYSICAL_THREE_ROW_SPACIOUS_ISOLATED_PIVOT" if result else "OPEN")
    return 0 if result else 1


if __name__ == "__main__":
    raise SystemExit(main())
