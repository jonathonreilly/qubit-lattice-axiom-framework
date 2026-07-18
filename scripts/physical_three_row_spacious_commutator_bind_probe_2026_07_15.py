#!/usr/bin/env python3
"""Bind three physical row records to two output-ported commutators."""

from __future__ import annotations

from collections import defaultdict
from functools import lru_cache

import physical_case_role_isolation_cable_probe_2026_07_15 as isolation
import physical_three_row_dual_commutation_bind_probe_2026_07_15 as prior
import spacious_and_xor_streaming_commutator_probe_2026_07_15 as spacious


ported = prior.ported
twoport = prior.twoport
cable = prior.cable
comm = prior.comm
d = prior.d
c53 = prior.c53
FRAME = prior.FRAME
MERGED_RAW = isolation.MERGED_RAW
Coord = tuple[int, int, int]

COMM_SHIFTS = ((-240, 0, 0), (240, 0, 0))
GENERATOR_CENTERS = ((-240, 0, 180), (240, 0, 180))
MEASURED_CENTER = (0, 0, -180)


def add(left: Coord, right: Coord) -> Coord:
    return tuple(a + b for a, b in zip(left, right))  # type: ignore[return-value]


def sub(left: Coord, right: Coord) -> Coord:
    return tuple(a - b for a, b in zip(left, right))  # type: ignore[return-value]


def scale(factor: int, vector: Coord) -> Coord:
    return tuple(factor * value for value in vector)  # type: ignore[return-value]


def shift_records(records: dict[Coord, str], shift: Coord):
    return {add(site, shift): role for site, role in records.items()}


def shift_dependencies(dependencies, shift: Coord):
    return {
        add(site, shift): frozenset(add(parent, shift) for parent in parents)
        for site, parents in dependencies.items()
    }


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


def generator_path(branch_index: int, term_index: int):
    bit_index = prior.single.LEFT_SPATIAL_BITS[term_index]
    center = GENERATOR_CENTERS[branch_index]
    direction = ported.TARGETS[bit_index]
    source = add(center, direction)
    path = [
        source,
        add(center, scale(2, direction)),
        add(center, scale(3, direction)),
        add(center, scale(4, direction)),
    ]
    input_site = add(
        add(spacious.AND_CENTERS[term_index], COMM_SHIFTS[branch_index]),
        (0, 0, 1),
    )
    high = 112 + 6 * term_index
    lane = -150 - 12 * term_index
    line_to(path, (path[-1][0], path[-1][1], high), (2,))
    line_to(path, (path[-1][0], lane, high), (1,))
    line_to(path, (input_site[0], lane, high), (0,))
    line_to(path, (input_site[0], input_site[1], high), (1,))
    line_to(path, input_site, (2,))
    if add(path[-1], sub(path[-1], path[-2])) != add(input_site, (0, 0, -1)):
        raise ValueError(("wrong-generator-terminal", branch_index, term_index, path[-2:]))
    return tuple(path)


def measured_path(branch_index: int, term_index: int):
    bit_index = prior.single.RIGHT_SPATIAL_BITS[term_index]
    local_stem = twoport.PATHS[bit_index][branch_index]
    source = add(MEASURED_CENTER, local_stem[-1])
    direction = cable.terminal_direction(local_stem)
    if branch_index == 0:
        escape_origin = (0, 0, 0)
        escape_direction = direction
        path = [
            source,
            add(MEASURED_CENTER, scale(3, direction)),
            add(MEASURED_CENTER, scale(4, direction)),
        ]
    else:
        radial = twoport.TARGETS[bit_index]
        turn_depth = 8 if radial[1] else 12
        path = [source]
        for depth in range(1, turn_depth + 1):
            path.append(add(source, (0, 0, -depth)))
        turn = path[-1]
        for radius in range(1, 9):
            path.append(add(turn, scale(radius, radial)))
        escape_origin = (0, 0, 0)
        escape_direction = radial
    input_site = add(
        add(spacious.AND_CENTERS[term_index], COMM_SHIFTS[branch_index]),
        (-1, 0, 0),
    )
    floor = (-132 if branch_index == 0 else -224) - 8 * term_index
    lane = 150 + 12 * term_index + 70 * branch_index
    dock = add(input_site, (-1, 0, 0))
    line_to(path, (path[-1][0], path[-1][1], floor), (2,))
    radius = 40 + 8 * term_index
    escape = add(escape_origin, scale(radius, escape_direction))
    line_to(path, (escape[0], escape[1], floor), (0, 1))
    if escape_direction[1]:
        escape_x = (-120 - 10 * term_index) if branch_index == 0 else (120 + 10 * term_index)
        line_to(path, (escape_x, path[-1][1], floor), (0,))
        line_to(path, (escape_x, lane, floor), (1,))
    else:
        line_to(path, (path[-1][0], lane, floor), (1,))
    line_to(path, (dock[0], lane, floor), (0,))
    approach_y = input_site[1] - 32 - 4 * term_index
    line_to(path, (dock[0], approach_y, floor), (1,))
    line_to(path, (dock[0], approach_y, dock[2]), (2,))
    line_to(path, dock, (1,))
    line_to(path, input_site, (0,))
    if add(path[-1], sub(path[-1], path[-2])) != add(input_site, (1, 0, 0)):
        raise ValueError(("wrong-measured-terminal", branch_index, term_index, path[-2:]))
    return tuple(path)


GENERATOR_PATHS = {
    (branch_index, term_index): generator_path(branch_index, term_index)
    for branch_index in range(2)
    for term_index in range(4)
}
MEASURED_PATHS = {
    (branch_index, term_index): measured_path(branch_index, term_index)
    for branch_index in range(2)
    for term_index in range(4)
}


def module_inputs(generator, measured):
    return tuple(
        value
        for term_index in range(4)
        for value in (
            generator[prior.single.LEFT_SPATIAL_BITS[term_index]],
            measured[prior.single.RIGHT_SPATIAL_BITS[term_index]],
        )
    )


@lru_cache(maxsize=1)
def measured_fork_scaffold():
    zero = (0, 0, 0, 0, 0)
    fixed = twoport.interface_source(zero)
    items = tuple(
        (twoport.bit(0), path)
        for bit_paths in twoport.PATHS
        for path in bit_paths
    )
    chosen, _outputs, terminal_ports = cable.multi_path_core(items, constraints=fixed)
    starts = {path[0] for _value, path in items}
    scaffold = {
        site: role
        for site, role in chosen.items()
        if site not in fixed and site not in starts
    }
    if terminal_ports != twoport.EXTERNAL_PORTS:
        raise ValueError(("wrong-measured-fork-ports", terminal_ports))
    return scaffold


@lru_cache(maxsize=1)
def module_scaffold():
    spacious.apparatus((0,) * 8)
    if spacious._ROUTING_CACHE is None:
        raise AssertionError("spacious routing cache was not populated")
    scaffold, terminal_ports = spacious._ROUTING_CACHE
    if terminal_ports != frozenset(spacious.XOR_CENTERS):
        raise ValueError(("wrong-spacious-ports", terminal_ports))
    return dict(scaffold)


def module_component(inputs):
    products = tuple(inputs[2 * index] & inputs[2 * index + 1] for index in range(4))
    xor_values = (
        products[0] ^ products[1],
        products[0] ^ products[1] ^ products[2],
        products[0] ^ products[1] ^ products[2] ^ products[3],
    )
    records: dict[Coord, str] = {}
    expected: dict[Coord, str] = {}
    dependencies: dict[Coord, frozenset[Coord]] = {}

    for center in spacious.AND_CENTERS:
        place(records, add(center, (1, 0, 0)), spacious.alu.AND_ROLE)
        place(records, add(center, (0, 1, 0)), FRAME)
        place(records, add(center, (0, -1, 0)), FRAME)
    for center in spacious.XOR_CENTERS:
        place(records, add(center, (1, 0, 0)), spacious.alu.XOR_ROLE)
        place(records, add(center, (0, 1, 0)), FRAME)
        place(records, add(center, (0, -1, 0)), FRAME)
    for site, role in module_scaffold().items():
        place(records, site, role)

    for index, center in enumerate(spacious.AND_CENTERS):
        expected[center] = spacious.alu.bit(products[index])
        dependencies[center] = frozenset((
            add(center, (0, 0, 1)),
            add(center, (-1, 0, 0)),
        ))

    path_values = (
        spacious.alu.bit(products[0]),
        spacious.alu.bit(products[1]),
        spacious.alu.bit(products[2]),
        spacious.alu.bit(products[3]),
        spacious.alu.bit(xor_values[0]),
        spacious.alu.bit(xor_values[1]),
    )
    for value, path in zip(path_values, spacious.PATHS, strict=True):
        for target in path[1:]:
            previous = expected.get(target)
            if previous is not None and previous != value:
                raise ValueError((target, previous, value, "module-path-conflict"))
            expected[target] = value
        for previous, target in zip(path, path[1:]):
            dependencies[target] = frozenset((previous,))

    for index, center in enumerate(spacious.XOR_CENTERS):
        expected[center] = spacious.alu.bit(xor_values[index])
        dependencies[center] = frozenset((
            add(center, (0, 0, 1)),
            add(center, (-1, 0, 0)),
        ))
    return records, expected, dependencies, xor_values[-1]


def component_records(g1, g2, measured):
    records: dict[Coord, str] = {}
    for row, center in zip((g1, g2), GENERATOR_CENTERS, strict=True):
        for site, role in shift_records(ported.interface_source(row), center).items():
            place(records, site, role)
    for site, role in shift_records(twoport.interface_source(measured), MEASURED_CENTER).items():
        place(records, site, role)
    for site, role in shift_records(measured_fork_scaffold(), MEASURED_CENTER).items():
        place(records, site, role)
    for branch_index, generator in enumerate((g1, g2)):
        local, _expected, _dependencies, _result = module_component(
            module_inputs(generator, measured)
        )
        for site, role in shift_records(local, COMM_SHIFTS[branch_index]).items():
            place(records, site, role)
    return records


def path_items(g1, g2, measured):
    items = []
    for branch_index, generator in enumerate((g1, g2)):
        for term_index in range(4):
            generator_bit = prior.single.LEFT_SPATIAL_BITS[term_index]
            measured_bit = prior.single.RIGHT_SPATIAL_BITS[term_index]
            items.append((
                ported.bit(generator[generator_bit]),
                GENERATOR_PATHS[(branch_index, term_index)],
            ))
            items.append((
                twoport.bit(measured[measured_bit]),
                MEASURED_PATHS[(branch_index, term_index)],
            ))
    return tuple(items)


def sequential_routing_scaffold(items, fixed, protected):
    placed = dict(fixed)
    terminal_ports = set()
    all_path_sites = {site for _value, path in items for site in path}
    protected = frozenset(set(protected) | all_path_sites)
    lower_paths = {
        path: (8 if twoport.TARGETS[prior.single.RIGHT_SPATIAL_BITS[term_index]][1] else 12) + 8
        for term_index, path in (
            (term_index, MEASURED_PATHS[(1, term_index)])
            for term_index in range(4)
        )
    }
    lower_prefixes = []
    remaining = []
    for value, path in items:
        if path in lower_paths:
            cut = lower_paths[path]
            lower_prefixes.append((value, path[:cut]))
            remaining.append((value, path[cut - 1 :]))
        else:
            remaining.append((value, path))
    by_source = defaultdict(list)
    for item in remaining:
        by_source[item[1][0]].append(item)
    groups = [tuple(lower_prefixes)] + sorted(
        (tuple(group) for group in by_source.values()),
        key=lambda group: (sum(len(path) for _value, path in group), group[0][1][0]),
    )
    starts = {path[0] for group in groups for _value, path in group}
    for group in groups:
        placed, _outputs, ports = cable.multi_path_core(
            group, constraints=placed, extra_protected=protected
        )
        terminal_ports.update(ports)
    scaffold = {
        site: role
        for site, role in placed.items()
        if site not in fixed and site not in starts
    }
    return scaffold, frozenset(terminal_ports)


def base_expected(g1, g2, measured):
    expected: dict[Coord, str] = {}
    dependencies: dict[Coord, frozenset[Coord]] = {}
    for row, center in zip((g1, g2), GENERATOR_CENTERS, strict=True):
        outputs = shift_records(ported.outputs(row), center)
        expected.update(outputs)
        dependencies.update({site: frozenset() for site in outputs})
    outputs = shift_records(twoport.outputs(measured), MEASURED_CENTER)
    expected.update(outputs)
    dependencies.update({site: frozenset() for site in outputs})
    for bit_index, bit_paths in enumerate(twoport.PATHS):
        value = twoport.bit(measured[bit_index])
        source = add(twoport.TARGETS[bit_index], MEASURED_CENTER)
        for path in bit_paths:
            endpoint = add(path[-1], MEASURED_CENTER)
            expected[endpoint] = value
            dependencies[endpoint] = frozenset((source,))
    results = []
    for branch_index, generator in enumerate((g1, g2)):
        _records, local_expected, local_dependencies, result = module_component(
            module_inputs(generator, measured)
        )
        expected.update(shift_records(local_expected, COMM_SHIFTS[branch_index]))
        dependencies.update(shift_dependencies(local_dependencies, COMM_SHIFTS[branch_index]))
        results.append(result)
    return expected, dependencies, tuple(results)


@lru_cache(maxsize=1)
def routing_scaffold():
    zero = (0, 0, 0, 0, 0)
    fixed = component_records(zero, zero, zero)
    expected, _dependencies, _results = base_expected(zero, zero, zero)
    items = path_items(zero, zero, zero)
    final_ports = {
        add(spacious.FINAL_PORT, shift) for shift in COMM_SHIFTS
    }
    scaffold, terminal_ports = sequential_routing_scaffold(
        items,
        fixed,
        frozenset(set(expected) | final_ports),
    )
    required_ports = {
        add(spacious.AND_CENTERS[term_index], COMM_SHIFTS[branch_index])
        for branch_index in range(2)
        for term_index in range(4)
    }
    if not required_ports <= set(terminal_ports):
        raise ValueError(("missing-and-ports", required_ports - set(terminal_ports)))
    return scaffold, terminal_ports


def uncaged_apparatus(g1, g2, measured):
    records = component_records(g1, g2, measured)
    scaffold, terminal_ports = routing_scaffold()
    for site, role in scaffold.items():
        place(records, site, role)
    expected, dependencies, results = base_expected(g1, g2, measured)
    for value, path in path_items(g1, g2, measured):
        for target in path[1:]:
            previous = expected.get(target)
            if previous is not None and previous != value:
                raise ValueError((target, previous, value, "row-path-conflict"))
            expected[target] = value
        for previous, target in zip(path, path[1:]):
            dependencies[target] = frozenset((previous,))

    required_ports = {
        add(spacious.AND_CENTERS[term_index], COMM_SHIFTS[branch_index])
        for branch_index in range(2)
        for term_index in range(4)
    }
    if not required_ports <= set(terminal_ports):
        raise ValueError(("wrong-terminal-ports", required_ports - set(terminal_ports)))
    final_ports = {
        add(spacious.FINAL_PORT, shift) for shift in COMM_SHIFTS
    }
    return records, expected, dependencies, results, frozenset(final_ports)


def apparatus(g1, g2, measured):
    records, expected, dependencies, results, final_ports = uncaged_apparatus(
        g1, g2, measured
    )
    core = set(records) | set(expected) | final_ports
    cage = {
        add(site, direction)
        for site in core
        for direction in c53.DIRECTIONS
        if add(site, direction) not in core
    }
    for site in cage:
        place(records, site, FRAME)
    for site in set(expected) | final_ports:
        records.pop(site, None)
    return records, expected, dependencies, results, frozenset(final_ports)


def enabled(records):
    return {
        target: MERGED_RAW[signature]
        for target in c53.open_candidates(records)
        if (signature := c53.local_signature(records, target)) in MERGED_RAW
    }


def deterministic_run(g1, g2, measured):
    initial, expected, dependencies, results, final_ports = apparatus(g1, g2, measured)
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
            return False, (len(formed), actual, frontier, len(initial), len(expected), results)
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
        not actual and not (set(final_ports) & set(records)),
        (len(expected) + 1, edges, maximum, len(initial), len(expected), results, actual),
    )


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
    wanted = tuple(
        comm.alu.compact.algebra.symplectic(generator, measured)
        for generator in (g1, g2)
    )
    print("PATH_LENGTHS", tuple(map(len, (*GENERATOR_PATHS.values(), *MEASURED_PATHS.values()))))
    print("SMOKE", ok, detail, "WANTED", wanted)
    result = ok and detail[5] == wanted
    print("RESULT", "PHYSICAL_THREE_ROW_SPACIOUS_COMMUTATOR_BIND" if result else "OPEN")
    return 0 if result else 1


if __name__ == "__main__":
    raise SystemExit(main())
