#!/usr/bin/env python3
"""Build an output-ported commutator from separated retained AND/XOR cells."""

from __future__ import annotations

import physical_three_row_dual_commutation_bind_probe_2026_07_15 as prior


alu = prior.comm.alu
cable = prior.cable
d = prior.d
c53 = prior.c53
MERGED_RAW = prior.MERGED_RAW
FRAME = prior.FRAME
Coord = tuple[int, int, int]
AND_CENTERS = ((-60, -60, 60), (-20, -60, 60), (20, -60, 60), (60, -60, 60))
XOR_CENTERS = ((-40, 40, 0), (0, 40, 0), (40, 40, 0))
FINAL_PORT = (40, 40, -1)


def add(left: Coord, right: Coord) -> Coord:
    return tuple(a + b for a, b in zip(left, right))  # type: ignore[return-value]


def sub(left: Coord, right: Coord) -> Coord:
    return tuple(a - b for a, b in zip(left, right))  # type: ignore[return-value]


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


def routed_path(source: Coord, target: Coord, floor: int, lane: int):
    path = [source, add(source, (0, 0, -1)), add(source, (0, 0, -2)), add(source, (0, 0, -3))]
    # Left inputs sit above their XOR target and must be approached downward.
    if target[2] == 1:
        launch = path[-1]
        line_to(path, (launch[0], launch[1], floor), (2,))
        line_to(path, (launch[0], lane, floor), (1,))
        line_to(path, (target[0], lane, floor), (0,))
        staging_z = max(10, floor)
        line_to(path, (target[0], lane, staging_z), (2,))
        line_to(path, (target[0], target[1], staging_z), (1,))
        line_to(path, target, (2,))
    else:
        # Right inputs are approached from negative x so the XOR target is the
        # cable's terminal port.
        launch = path[-1]
        line_to(path, (launch[0], launch[1], floor), (2,))
        line_to(path, (launch[0], lane, floor), (1,))
        dock_x = target[0] - 12
        line_to(path, (dock_x, lane, floor), (0,))
        line_to(path, (dock_x, target[1], floor), (1,))
        line_to(path, (dock_x, target[1], target[2]), (2,))
        line_to(path, target, (0,))
    terminal = add(path[-1], sub(path[-1], path[-2]))
    expected_terminal = (
        add(target, (0, 0, -1)) if target[2] == 1 else add(target, (1, 0, 0))
    )
    if terminal != expected_terminal:
        raise ValueError(("wrong-terminal", source, target, path[-2:], terminal, expected_terminal))
    return tuple(path)


def paths():
    left_inputs = tuple(add(center, (0, 0, 1)) for center in XOR_CENTERS)
    right_inputs = tuple(add(center, (-1, 0, 0)) for center in XOR_CENTERS)
    return (
        routed_path(AND_CENTERS[0], left_inputs[0], 30, -100),
        routed_path(AND_CENTERS[1], right_inputs[0], 24, -80),
        routed_path(AND_CENTERS[2], right_inputs[1], 18, -60),
        routed_path(AND_CENTERS[3], right_inputs[2], 12, -40),
        routed_path(XOR_CENTERS[0], left_inputs[1], -20, 60),
        routed_path(XOR_CENTERS[1], left_inputs[2], -30, 80),
    )


PATHS = paths()
_ROUTING_CACHE = None


def apparatus(inputs):
    global _ROUTING_CACHE
    if len(inputs) != 8:
        raise ValueError(("eight-inputs-required", inputs))
    products = tuple(inputs[2 * index] & inputs[2 * index + 1] for index in range(4))
    xor_values = (
        products[0] ^ products[1],
        products[0] ^ products[1] ^ products[2],
        products[0] ^ products[1] ^ products[2] ^ products[3],
    )
    records: dict[Coord, str] = {}
    expected: dict[Coord, str] = {}
    dependencies: dict[Coord, frozenset[Coord]] = {}

    for index, center in enumerate(AND_CENTERS):
        left = inputs[2 * index]
        right = inputs[2 * index + 1]
        for site, role in {
            add(center, (0, 0, 1)): alu.bit(left),
            add(center, (-1, 0, 0)): alu.bit(right),
            add(center, (1, 0, 0)): alu.AND_ROLE,
            add(center, (0, 1, 0)): FRAME,
            add(center, (0, -1, 0)): FRAME,
        }.items():
            place(records, site, role)
        expected[center] = alu.bit(products[index])
        dependencies[center] = frozenset()

    for center in XOR_CENTERS:
        for site, role in {
            add(center, (1, 0, 0)): alu.XOR_ROLE,
            add(center, (0, 1, 0)): FRAME,
            add(center, (0, -1, 0)): FRAME,
        }.items():
            place(records, site, role)

    path_values = (
        alu.bit(products[0]),
        alu.bit(products[1]),
        alu.bit(products[2]),
        alu.bit(products[3]),
        alu.bit(xor_values[0]),
        alu.bit(xor_values[1]),
    )
    items = tuple(zip(path_values, PATHS, strict=True))
    xor_targets = set(XOR_CENTERS)
    protected = {
        site for _value, path in items for site in path
    } | set(expected) | xor_targets | {FINAL_PORT}
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
    if terminal_ports != frozenset(XOR_CENTERS):
        raise ValueError(("wrong-xor-ports", terminal_ports, XOR_CENTERS))

    for index, center in enumerate(XOR_CENTERS):
        expected[center] = alu.bit(xor_values[index])
        dependencies[center] = frozenset((
            add(center, (0, 0, 1)),
            add(center, (-1, 0, 0)),
        ))

    core = set(records) | set(expected) | {FINAL_PORT}
    cage = {
        add(site, direction)
        for site in core
        for direction in c53.DIRECTIONS
        if add(site, direction) not in core
    }
    for site in cage:
        place(records, site, FRAME)
    for site in set(expected) | {FINAL_PORT}:
        records.pop(site, None)
    return records, expected, dependencies, xor_values[-1]


def enabled(records):
    return {
        target: MERGED_RAW[signature]
        for target in c53.open_candidates(records)
        if (signature := c53.local_signature(records, target)) in MERGED_RAW
    }


def deterministic_run(inputs, rotation=None):
    initial, expected, dependencies, result = apparatus(inputs)
    if rotation is not None:
        shift = (463, -467, 479)
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
    actual = enabled(records)
    formed = set()
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
            return False, (len(formed), actual, frontier, len(initial), len(expected), result)
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
    return (not actual, (len(expected) + 1, edges, maximum, len(initial), len(expected), result, actual))


def main() -> int:
    inputs = (1, 1, 1, 0, 0, 1, 1, 1)
    try:
        ok, detail = deterministic_run(inputs)
    except ValueError as error:
        print("LAYOUT_FAILURE", str(error)[:8_000])
        print("RESULT", "OPEN")
        return 1
    print("PATH_LENGTHS", tuple(map(len, PATHS)))
    print("SMOKE", ok, detail)
    print("RESULT", "SPACIOUS_AND_XOR_STREAMING_COMMUTATOR" if ok else "OPEN")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
