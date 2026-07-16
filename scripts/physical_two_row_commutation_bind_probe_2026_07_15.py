#!/usr/bin/env python3
"""Compose two row records through fanout/cables to one physical commutation bit."""

from __future__ import annotations

from functools import lru_cache
from itertools import combinations

import physical_ported_symplectic_row_fanout_probe_2026_07_15 as ported


cable = ported.cable
terminal = ported.terminal
pivot = terminal.pivot
comm = pivot.mult.c150.p
d = ported.d
c53 = ported.c53
Coord = tuple[int, int, int]
FRAME = d.CAGE_ROLE
MERGED_RAW = ported.MERGED_RAW
LEFT_CENTER = (0, 0, 40)
RIGHT_CENTER = (0, 0, -40)

LEFT_TERM_BY_BIT = {0: 0, 2: 1, 1: 2, 3: 3}
RIGHT_TERM_BY_BIT = {2: 0, 0: 1, 3: 2, 1: 3}
LEFT_SPATIAL_BITS = (0, 2, 1, 3)
RIGHT_SPATIAL_BITS = (2, 0, 3, 1)


def add(left: Coord, right: Coord) -> Coord:
    return tuple(a + b for a, b in zip(left, right))  # type: ignore[return-value]


def sub(left: Coord, right: Coord) -> Coord:
    return tuple(a - b for a, b in zip(left, right))  # type: ignore[return-value]


def scale(factor: int, vector: Coord) -> Coord:
    return tuple(factor * value for value in vector)  # type: ignore[return-value]


def shift_records(records: dict[Coord, str], shift: Coord):
    return {add(site, shift): role for site, role in records.items()}


def permuted_interface_source(row, spatial_bits):
    records = ported.interface_source(row)
    for spatial_index, bit_index in enumerate(spatial_bits):
        records[ported.INDEX_SITES[spatial_index]] = ported.INDEX_ROLES[bit_index]
    return records


def permuted_outputs(row, spatial_bits):
    return {
        ported.TARGETS[spatial_index]: ported.bit(row[bit_index])
        for spatial_index, bit_index in enumerate(spatial_bits)
    }


def place(records: dict[Coord, str], site: Coord, role: str) -> None:
    prior = records.get(site)
    if prior is not None and prior != role:
        raise ValueError((site, prior, role))
    records[site] = role


def line_to(path: list[Coord], target: Coord, axes=(0, 1, 2)) -> None:
    current = list(path[-1])
    for axis in axes:
        while current[axis] != target[axis]:
            current[axis] += 1 if target[axis] > current[axis] else -1
            point = tuple(current)  # type: ignore[assignment]
            if point in path:
                raise ValueError(("path-self-contact", point, path, target))
            path.append(point)


def routed_path(
    center: Coord,
    spatial_index: int,
    input_site: Coord,
    term_site: Coord,
    side: str,
) -> tuple[Coord, ...]:
    direction = ported.TARGETS[spatial_index]
    start = add(center, direction)
    forced = add(center, ported.PORTS[spatial_index])
    final_direction = sub(term_site, input_site)
    path = [
        start,
        forced,
        add(center, scale(3, direction)),
        add(center, scale(4, direction)),
    ]

    if side == "left":
        # The four upper fanout ports are aligned with the four left AND
        # inputs.  Each cable therefore descends in its own radial half-plane
        # and finishes with the same direction as the input-to-term edge.
        launch = path[-1]
        line_to(path, (launch[0], launch[1], 0), (2,))
        line_to(path, input_site, (0, 1, 2))
    elif side == "right" and final_direction[2] == 1:
        # The two lower inputs approach on staggered negative docking layers.
        # This leaves a clean gap between their runs and the upper cables.
        launch = path[-1]
        plane = -4 if direction[1] < 0 else -2
        line_to(path, (launch[0], launch[1], plane), (2,))
        line_to(path, (input_site[0], input_site[1], plane), (0, 1))
        line_to(path, input_site, (2,))
    elif side == "right" and final_direction[2] == -1:
        # The two upper inputs first move to radius eight, rise to staggered
        # positive docking layers, and dogleg around the upper radial columns.
        line_to(path, add(center, scale(8, direction)), (0, 1))
        launch = path[-1]
        plane = 4 if direction[1] > 0 else 2
        line_to(path, (launch[0], launch[1], plane), (2,))
        if direction[0]:
            lane_y = 2 if direction[0] < 0 else -2
            radial_x = input_site[0] + direction[0]
            line_to(path, (launch[0], lane_y, plane), (1,))
            line_to(path, (radial_x, lane_y, plane), (0,))
            line_to(path, (radial_x, input_site[1], plane), (1,))
            line_to(path, (input_site[0], input_site[1], plane), (0,))
        else:
            lane_x = 2 if direction[1] > 0 else -2
            radial_y = input_site[1] + direction[1]
            line_to(path, (lane_x, launch[1], plane), (0,))
            line_to(path, (lane_x, radial_y, plane), (1,))
            line_to(path, (input_site[0], radial_y, plane), (0,))
            line_to(path, (input_site[0], input_site[1], plane), (1,))
        line_to(path, input_site, (2,))
    else:
        raise ValueError(("unsupported-side-or-tail", side, input_site, term_site))

    terminal = add(path[-1], sub(path[-1], path[-2]))
    if terminal != term_site:
        raise ValueError(("wrong-terminal", terminal, term_site, path[-2:]))
    return tuple(path)


def paths():
    answer = {}
    for spatial_index, bit_index in enumerate(LEFT_SPATIAL_BITS):
        term_index = LEFT_TERM_BY_BIT[bit_index]
        geometry = comm.PARENT_GEOMETRY[term_index]
        answer[("left", bit_index)] = routed_path(
            LEFT_CENTER,
            spatial_index,
            geometry["left"],
            comm.TERMS[term_index],
            "left",
        )
    for spatial_index, bit_index in enumerate(RIGHT_SPATIAL_BITS):
        term_index = RIGHT_TERM_BY_BIT[bit_index]
        geometry = comm.PARENT_GEOMETRY[term_index]
        answer[("right", bit_index)] = routed_path(
            RIGHT_CENTER,
            spatial_index,
            geometry["right"],
            comm.TERMS[term_index],
            "right",
        )
    return answer


PATHS = paths()


def commutation_core():
    records: dict[Coord, str] = {site: FRAME for site in comm.FRAMES}
    for geometry in comm.PARENT_GEOMETRY:
        records[geometry["op"]] = comm.alu.AND_ROLE
        records[geometry["g1"]] = FRAME
        records[geometry["g2"]] = FRAME
    return records


def component_geometry():
    left_outputs = shift_records({site: "left" for site in ported.TARGETS}, LEFT_CENTER)
    right_outputs = shift_records({site: "right" for site in ported.TARGETS}, RIGHT_CENTER)
    expected_sites = set(left_outputs) | set(right_outputs) | set(comm.TERMS) | {comm.CENTER}
    terminal_ports = set(comm.TERMS)
    for path in PATHS.values():
        expected_sites.update(path)
    return expected_sites, terminal_ports


EXPECTED_SITES, _TERMINAL_PORTS = component_geometry()


def component_records(left, right):
    records: dict[Coord, str] = {}
    for site, role in shift_records(
        permuted_interface_source(left, LEFT_SPATIAL_BITS), LEFT_CENTER
    ).items():
        place(records, site, role)
    for site, role in shift_records(
        permuted_interface_source(right, RIGHT_SPATIAL_BITS), RIGHT_CENTER
    ).items():
        place(records, site, role)
    for site, role in commutation_core().items():
        place(records, site, role)
    return records


def path_items(left, right):
    items = []
    for side, row in (("left", left), ("right", right)):
        for bit_index in range(4):
            path = PATHS[(side, bit_index)]
            value = ported.bit(row[bit_index])
            items.append((value, path))
    return tuple(items)


@lru_cache(maxsize=1)
def routing_scaffold():
    zero = (0, 0, 0, 0, 0)
    fixed = component_records(zero, zero)
    items = path_items(zero, zero)
    chosen, _outputs, terminal_ports = cable.multi_path_core(
        items,
        constraints=fixed,
        extra_protected=frozenset(EXPECTED_SITES),
    )
    starts = {path[0] for _value, path in items}
    scaffold = {
        site: role
        for site, role in chosen.items()
        if site not in fixed and site not in starts
    }
    return scaffold, terminal_ports


def apparatus(left, right):
    records = component_records(left, right)
    scaffold, terminal_ports = routing_scaffold()
    for site, role in scaffold.items():
        place(records, site, role)

    expected = {
        **shift_records(permuted_outputs(left, LEFT_SPATIAL_BITS), LEFT_CENTER),
        **shift_records(permuted_outputs(right, RIGHT_SPATIAL_BITS), RIGHT_CENTER),
    }
    dependencies: dict[Coord, frozenset[Coord]] = {
        site: frozenset() for site in expected
    }
    items = path_items(left, right)
    cable_outputs: dict[Coord, str] = {}
    for value, path in items:
        for site in path[1:]:
            prior = cable_outputs.get(site)
            if prior is not None and prior != value:
                raise ValueError((site, prior, value, "path-output-conflict"))
            cable_outputs[site] = value
    expected.update(cable_outputs)
    for side, row in (("left", left), ("right", right)):
        for bit_index in range(4):
            path = PATHS[(side, bit_index)]
            for previous, target in zip(path, path[1:]):
                dependencies[target] = frozenset((previous,))
    if terminal_ports != frozenset(comm.TERMS):
        raise ValueError(("wrong-terminal-ports", terminal_ports, comm.TERMS))

    term_values = comm.term_values(left, right)
    for term, value, geometry in zip(comm.TERMS, term_values, comm.PARENT_GEOMETRY):
        expected[term] = comm.alu.bit(value)
        dependencies[term] = frozenset((geometry["left"], geometry["right"]))
    expected[comm.CENTER] = comm.alu.bit(sum(term_values) & 1)
    dependencies[comm.CENTER] = frozenset(comm.TERMS)

    core = set(records) | set(expected)
    cage = {
        c53.add(site, direction)
        for site in core
        for direction in c53.DIRECTIONS
        if c53.add(site, direction) not in core
    }
    for site in cage:
        place(records, site, FRAME)
    for site in expected:
        records.pop(site, None)
    return records, expected, dependencies


def enabled(records):
    return {
        target: MERGED_RAW[signature]
        for target in c53.open_candidates(records)
        if (signature := c53.local_signature(records, target)) in MERGED_RAW
    }


def deterministic_run(left, right):
    initial, expected, dependencies = apparatus(left, right)
    records = dict(initial)
    formed = set()
    edges = 0
    maximum = 0
    while len(formed) < len(expected):
        frontier = {
            target: frozenset((expected[target],))
            for target, required in dependencies.items()
            if target not in formed and required <= formed
        }
        actual = enabled(records)
        maximum = max(maximum, len(frontier))
        if actual != frontier:
            return False, (len(formed), actual, frontier, len(initial), len(expected))
        target = min(frontier)
        records[target] = expected[target]
        formed.add(target)
        edges += len(frontier)
    actual = enabled(records)
    if actual:
        return False, ("terminal", actual, len(initial), len(expected))
    return True, (len(expected) + 1, edges, maximum, len(initial), len(expected))


def ancestors(dependencies):
    cache: dict[Coord, frozenset[Coord]] = {}

    def visit(site: Coord):
        if site not in cache:
            direct = dependencies.get(site, frozenset())
            cache[site] = frozenset(direct) | frozenset(
                ancestor for parent in direct for ancestor in visit(parent)
            )
        return cache[site]

    for site in dependencies:
        visit(site)
    return cache


def subsets(items):
    items = tuple(items)
    for size in range(len(items) + 1):
        yield from combinations(items, size)


def local_schedule_proof(left, right, rotation=None):
    initial, expected, dependencies = apparatus(left, right)
    if rotation is not None:
        shift = (307, -311, 313)
        initial = c53.transform_records(initial, rotation, shift)
        expected = c53.transform_records(expected, rotation, shift)
        dependencies = {
            next(iter(c53.transform_records({site: "x"}, rotation, shift))): frozenset(
                next(iter(c53.transform_records({parent: "x"}, rotation, shift)))
                for parent in required
            )
            for site, required in dependencies.items()
        }
    ancestry = ancestors(dependencies)
    descendants = {
        site: frozenset(other for other, prior in ancestry.items() if site in prior)
        for site in expected
    }
    failures = []
    cases = 0

    for target, output in expected.items():
        fixed = {
            site: initial[site]
            for direction in c53.DIRECTIONS
            if (site := c53.add(target, direction)) in initial
        }
        variable = tuple(
            site
            for direction in c53.DIRECTIONS
            if (site := c53.add(target, direction)) in expected
            and site not in descendants[target]
        )
        for present_tuple in subsets(variable):
            present = frozenset(present_tuple)
            if any(
                ancestor in variable and ancestor not in present
                for site in present
                for ancestor in ancestry[site]
            ):
                continue
            local_records = {**fixed, **{site: expected[site] for site in present}}
            signature = c53.local_signature(local_records, target)
            actual = MERGED_RAW.get(signature, frozenset())
            wanted = frozenset((output,)) if dependencies[target] <= present else frozenset()
            cases += 1
            if actual != wanted:
                failures.append(("target", target, present, dependencies[target], actual, wanted, signature))
                if len(failures) >= 20:
                    return cases, tuple(failures)

    universe = set(initial) | set(expected)
    outside = {
        c53.add(site, direction)
        for site in universe
        for direction in c53.DIRECTIONS
        if c53.add(site, direction) not in universe
    }
    for target in outside:
        fixed = {
            site: initial[site]
            for direction in c53.DIRECTIONS
            if (site := c53.add(target, direction)) in initial
        }
        variable = tuple(
            site
            for direction in c53.DIRECTIONS
            if (site := c53.add(target, direction)) in expected
        )
        for present_tuple in subsets(variable):
            present = frozenset(present_tuple)
            if any(
                ancestor in variable and ancestor not in present
                for site in present
                for ancestor in ancestry[site]
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
    print("PATH_LENGTHS", {key: len(path) for key, path in PATHS.items()})
    print("PATH_CONTACTS", len({site for path in PATHS.values() for site in path}), sum(map(len, PATHS.values())))
    smoke_left = (0, 1, 0, 1, 0)
    smoke_right = (1, 0, 1, 0, 1)
    ok, detail = deterministic_run(smoke_left, smoke_right)
    print("SMOKE", ok, detail, "EXPECTED", comm.alu.bit(comm.alu.compact.algebra.symplectic(smoke_left, smoke_right)))
    cases, failures = local_schedule_proof(smoke_left, smoke_right)
    print("LOCAL_PROOF", cases, len(failures))
    if failures:
        print("FAILURE_SAMPLE", failures[:20])
    result = ok and not failures
    print("RESULT", "PHYSICAL_TWO_ROW_COMMUTATION_BIND" if result else "OPEN")
    return 0 if result else 1


if __name__ == "__main__":
    raise SystemExit(main())
