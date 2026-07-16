#!/usr/bin/env python3
"""Bind g1, g2, and one measured row to two physical commutation records."""

from __future__ import annotations

from functools import lru_cache
from itertools import combinations

import physical_two_port_row_four_fork_probe_2026_07_15 as twoport
import physical_two_row_commutation_bind_probe_2026_07_15 as single


ported = twoport.ported
cable = twoport.cable
comm = single.comm
d = twoport.d
c53 = twoport.c53
Coord = tuple[int, int, int]
FRAME = twoport.FRAME
MERGED_RAW = twoport.MERGED_RAW
COMM_CENTERS = ((-120, 0, 0), (120, 0, 0))
GENERATOR_CENTERS = tuple(
    single.add(center, single.LEFT_CENTER) for center in COMM_CENTERS
)
MEASURED_CENTER = (0, 0, -80)
ENTRY_DIRECTION = {
    2: (0, 0, 1),
    0: (0, 0, 1),
    3: (0, 0, -1),
    1: (0, 0, -1),
}
HEIGHT = {
    (0, 2): -50,
    (0, 0): -56,
    (0, 3): -30,
    (0, 1): -24,
    (1, 2): -62,
    (1, 0): -68,
    (1, 3): -18,
    (1, 1): -12,
}
LANE = {
    (0, 2): -80,
    (0, 0): 20,
    (0, 3): -16,
    (0, 1): -20,
    (1, 2): 20,
    (1, 0): 40,
    (1, 3): 60,
    (1, 1): 80,
}


def add(left: Coord, right: Coord) -> Coord:
    return tuple(a + b for a, b in zip(left, right))  # type: ignore[return-value]


def sub(left: Coord, right: Coord) -> Coord:
    return tuple(a - b for a, b in zip(left, right))  # type: ignore[return-value]


def scale(factor: int, vector: Coord) -> Coord:
    return tuple(factor * value for value in vector)  # type: ignore[return-value]


def shift_records(records: dict[Coord, str], shift: Coord):
    return {add(site, shift): role for site, role in records.items()}


def shift_path(path: tuple[Coord, ...], shift: Coord):
    return tuple(add(site, shift) for site in path)


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
                raise ValueError(("path-self-contact", point, target))
            path.append(point)


def continuation_path(branch_index: int, bit_index: int):
    internal = shift_path(
        twoport.PATHS[bit_index][branch_index], MEASURED_CENTER
    )
    endpoint = internal[-1]
    direction = cable.terminal_direction(internal)
    forced = add(endpoint, direction)
    base = shift_path(
        single.PATHS[("right", bit_index)], COMM_CENTERS[branch_index]
    )
    staging_source = base[0]
    outward = sub(base[1], staging_source)
    approach = {
        0: (0, -1, 0),
        1: (-1, 0, 0),
        2: (0, 1, 0),
        3: (-1, 0, 0),
    }[bit_index]
    if sum(a * b for a, b in zip(outward, approach)):
        raise ValueError(("nonperpendicular-approach", outward, approach))
    incoming = ENTRY_DIRECTION[bit_index]
    height = HEIGHT[(branch_index, bit_index)]
    lane = LANE[(branch_index, bit_index)]
    if incoming[2] > 0 and height >= staging_source[2]:
        raise ValueError(("height-not-below", branch_index, bit_index, height))
    if incoming[2] < 0 and height <= staging_source[2]:
        raise ValueError(("height-not-above", branch_index, bit_index, height))

    path = [endpoint, forced]
    if direction[2]:
        # The lower fanout leaves on four diagonal/private elevator shafts;
        # the upper fanout already owns the four axial shafts.
        # The y pair turns immediately while the x pair descends to a second
        # layer.  Running both orthogonal pairs down the same four close
        # columns creates an avoidable guide-role cycle.
        drop = 6 if bit_index in (0, 1) else 0
        line_to(path, add(forced, scale(drop, direction)), (2,))
        launch = path[-1]
        elbow = {
            0: (32, 0, 0),
            1: (-32, 0, 0),
            2: (0, 32, 0),
            3: (0, -32, 0),
        }[bit_index]
        line_to(path, add(launch, elbow), (0, 1))
        launch = path[-1]
    else:
        path.extend((add(forced, direction), add(forced, scale(2, direction))))
        launch = path[-1]
    line_to(path, (launch[0], launch[1], height), (2,))
    # Enter the inherited tail from a transverse direction.  Approaching
    # opposite its outward ray would force paired bit cables to cross one
    # another's vertical docking column.
    reach = 4 if approach[0] else 12
    far = add(staging_source, scale(reach, approach))
    if approach[0]:
        line_to(path, (launch[0], lane, height), (1,))
        line_to(path, (far[0], lane, height), (0,))
        line_to(path, (far[0], far[1], height), (1,))
    else:
        line_to(path, (lane, launch[1], height), (0,))
        line_to(path, (lane, far[1], height), (1,))
        line_to(path, (far[0], far[1], height), (0,))
    line_to(path, (staging_source[0], staging_source[1], height), (0, 1))
    line_to(path, staging_source, (2,))
    if sub(staging_source, path[-2]) != incoming:
        raise ValueError(("wrong-entry-direction", path[-2:], incoming))
    for point in base[1:]:
        if point in path:
            raise ValueError(("tail-self-contact", point, branch_index, bit_index))
        path.append(point)
    return tuple(path)


GENERATOR_PATHS = {
    (branch_index, bit_index): shift_path(
        single.PATHS[("left", bit_index)], COMM_CENTERS[branch_index]
    )
    for branch_index in range(2)
    for bit_index in range(4)
}
MEASURED_INTERNAL_PATHS = {
    (branch_index, bit_index): shift_path(
        twoport.PATHS[bit_index][branch_index], MEASURED_CENTER
    )
    for branch_index in range(2)
    for bit_index in range(4)
}
MEASURED_CONTINUATIONS = {
    (branch_index, bit_index): continuation_path(branch_index, bit_index)
    for branch_index in range(2)
    for bit_index in range(4)
}


def commutation_core(center: Coord):
    return shift_records(single.commutation_core(), center)


def component_records(g1, g2, measured):
    records: dict[Coord, str] = {}
    for row, center in zip((g1, g2), GENERATOR_CENTERS, strict=True):
        source = single.permuted_interface_source(
            row, single.LEFT_SPATIAL_BITS
        )
        for site, role in shift_records(source, center).items():
            place(records, site, role)
    for site, role in shift_records(
        twoport.interface_source(measured), MEASURED_CENTER
    ).items():
        place(records, site, role)
    for center in COMM_CENTERS:
        for site, role in commutation_core(center).items():
            place(records, site, role)
    return records


def path_items(g1, g2, measured):
    items = []
    for branch_index, row in enumerate((g1, g2)):
        for bit_index in range(4):
            items.append((
                ported.bit(row[bit_index]),
                GENERATOR_PATHS[(branch_index, bit_index)],
            ))
            measured_value = twoport.bit(measured[bit_index])
            items.append((
                measured_value,
                MEASURED_INTERNAL_PATHS[(branch_index, bit_index)],
            ))
            items.append((
                measured_value,
                MEASURED_CONTINUATIONS[(branch_index, bit_index)],
            ))
    return tuple(items)


def expected_graph(g1, g2, measured):
    expected: dict[Coord, str] = {}
    dependencies: dict[Coord, frozenset[Coord]] = {}

    for row, center in zip((g1, g2), GENERATOR_CENTERS, strict=True):
        outputs = shift_records(
            single.permuted_outputs(row, single.LEFT_SPATIAL_BITS), center
        )
        expected.update(outputs)
        dependencies.update({site: frozenset() for site in outputs})
    measured_outputs = shift_records(twoport.outputs(measured), MEASURED_CENTER)
    expected.update(measured_outputs)
    dependencies.update({site: frozenset() for site in measured_outputs})

    for value, path in path_items(g1, g2, measured):
        for target in path[1:]:
            prior = expected.get(target)
            if prior is not None and prior != value:
                raise ValueError((target, prior, value, "expected-conflict"))
            expected[target] = value
        for previous, target in zip(path, path[1:]):
            dependencies[target] = frozenset((previous,))

    for branch_index, (row, center) in enumerate(
        zip((g1, g2), COMM_CENTERS, strict=True)
    ):
        term_values = comm.term_values(row, measured)
        for term, value, geometry in zip(
            comm.TERMS, term_values, comm.PARENT_GEOMETRY, strict=True
        ):
            target = add(term, center)
            left = add(geometry["left"], center)
            right = add(geometry["right"], center)
            expected[target] = comm.alu.bit(value)
            dependencies[target] = frozenset((left, right))
        center_site = add(comm.CENTER, center)
        expected[center_site] = comm.alu.bit(sum(term_values) & 1)
        dependencies[center_site] = frozenset(
            add(term, center) for term in comm.TERMS
        )

    return expected, dependencies


@lru_cache(maxsize=1)
def routing_scaffold():
    zero = (0, 0, 0, 0, 0)
    fixed = component_records(zero, zero, zero)
    expected, _dependencies = expected_graph(zero, zero, zero)
    items = path_items(zero, zero, zero)
    path_sites = {site for _value, path in items for site in path}
    comm_sites = {
        add(site, center)
        for center in COMM_CENTERS
        for site in (*comm.TERMS, comm.CENTER)
    }
    chosen, _cable_outputs, terminal_ports = cable.multi_path_core(
        items,
        constraints=fixed,
        extra_protected=frozenset(path_sites | comm_sites | set(expected)),
    )
    starts = {path[0] for _value, path in items}
    scaffold = {
        site: role
        for site, role in chosen.items()
        if site not in fixed and site not in starts
    }
    return scaffold, terminal_ports


def apparatus(g1, g2, measured):
    records = component_records(g1, g2, measured)
    scaffold, terminal_ports = routing_scaffold()
    for site, role in scaffold.items():
        place(records, site, role)
    expected, dependencies = expected_graph(g1, g2, measured)
    required_ports = {
        add(term, center) for center in COMM_CENTERS for term in comm.TERMS
    }
    if not required_ports <= set(terminal_ports):
        raise ValueError(("missing-comm-ports", required_ports, terminal_ports))

    core = set(records) | set(expected)
    cage = {
        add(site, direction)
        for site in core
        for direction in c53.DIRECTIONS
        if add(site, direction) not in core
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


def deterministic_run(g1, g2, measured):
    initial, expected, dependencies = apparatus(g1, g2, measured)
    records = dict(initial)
    formed = set()
    edges = 0
    maximum = 0
    actual = enabled(records)
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
        # Appending one record can change admissibility only at that site and
        # its six nearest neighbors.  Maintaining the exact enabled set here
        # is equivalent to rescanning every open neighbor after every write,
        # while preserving full unexpected-target screening.
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


def local_schedule_proof(g1, g2, measured, rotation=None):
    initial, expected, dependencies = apparatus(g1, g2, measured)
    if rotation is not None:
        shift = (431, -433, 439)
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
            if (site := add(target, direction)) in initial
        }
        variable = tuple(
            site
            for direction in c53.DIRECTIONS
            if (site := add(target, direction)) in expected
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
            wanted = (
                frozenset((output,))
                if dependencies[target] <= present
                else frozenset()
            )
            cases += 1
            if actual != wanted:
                failures.append((
                    "target", target, present, dependencies[target],
                    actual, wanted, signature,
                ))
                if len(failures) >= 20:
                    return cases, tuple(failures)

    universe = set(initial) | set(expected)
    outside = {
        add(site, direction)
        for site in universe
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
    print(
        "PATH_CONTACTS",
        len({
            site
            for paths in (
                GENERATOR_PATHS,
                MEASURED_INTERNAL_PATHS,
                MEASURED_CONTINUATIONS,
            )
            for path in paths.values()
            for site in path
        }),
        sum(
            len(path)
            for paths in (
                GENERATOR_PATHS,
                MEASURED_INTERNAL_PATHS,
                MEASURED_CONTINUATIONS,
            )
            for path in paths.values()
        ),
    )
    g1 = (1, 0, 0, 1, 0)
    g2 = (0, 1, 1, 0, 1)
    measured = (1, 1, 0, 1, 0)
    try:
        ok, detail = deterministic_run(g1, g2, measured)
    except ValueError as error:
        print("LAYOUT_FAILURE", str(error)[:4_000])
        print("RESULT", "OPEN")
        return 1
    wanted = tuple(
        comm.alu.bit(comm.alu.compact.algebra.symplectic(row, measured))
        for row in (g1, g2)
    )
    print("SMOKE", ok, detail, "EXPECTED", wanted)
    print("RESULT", "PHYSICAL_THREE_ROW_DUAL_COMMUTATION_BIND" if ok else "OPEN")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
