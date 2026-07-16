#!/usr/bin/env python3
"""Probe isolated selector-gated row muxes with one common output per lane."""

from __future__ import annotations

from functools import lru_cache

import physical_row_role_fork_cable_probe_2026_07_15 as transport


pivot = transport.pivot
cable = transport.cable
cell = transport.cell
c53 = transport.c53
FRAME = transport.FRAME
GUIDE = cable.GUIDE_ROLE
Coord = tuple[int, int, int]
Signature = c53.Signature
ROW_ROLES = tuple(pivot.five.ROLE_ROW)
SELECTORS = tuple(pivot.SELECTOR_ROLES)
SELECTOR_INDEX = {
    pivot.SEL_L1_G1: 0,
    pivot.SEL_L1_P: 1,
    pivot.SEL_L2_G2: 0,
    pivot.SEL_L2_P: 1,
    pivot.SEL_L2_PRODUCT: 2,
}
SOCKET_SELECTORS = {
    2: (pivot.SEL_L1_G1, pivot.SEL_L1_P),
    3: (pivot.SEL_L2_G2, pivot.SEL_L2_P, pivot.SEL_L2_PRODUCT),
}
SOCKET_PATTERNS = {
    pivot.SEL_L1_G1: {(0, 1, 0): pivot.ROUTER_MARKER, (-1, 0, 0): FRAME, (0, -1, 0): FRAME},
    pivot.SEL_L1_P: {(0, 1, 0): GUIDE, (-1, 0, 0): FRAME, (0, -1, 0): FRAME},
    pivot.SEL_L2_G2: {(0, 1, 0): pivot.ROUTER_MARKER, (-1, 0, 0): FRAME, (0, -1, 0): FRAME},
    pivot.SEL_L2_P: {(0, 1, 0): GUIDE, (-1, 0, 0): FRAME, (0, -1, 0): FRAME},
    pivot.SEL_L2_PRODUCT: {(0, 1, 0): GUIDE, (-1, 0, 0): pivot.ROUTER_MARKER, (0, -1, 0): FRAME},
}


def add(left: Coord, right: Coord) -> Coord:
    return tuple(a + b for a, b in zip(left, right))  # type: ignore[return-value]


def neg(vector: Coord) -> Coord:
    return tuple(-value for value in vector)  # type: ignore[return-value]


def scale(factor: int, vector: Coord) -> Coord:
    return tuple(factor * value for value in vector)  # type: ignore[return-value]


def gate_local(selector: str, row_role: str) -> Signature:
    records = {
        (0, 0, 1): selector,
        (0, 0, -1): row_role,
        **SOCKET_PATTERNS[selector],
    }
    return c53.canonical_signature(c53.local_signature(records, (0, 0, 0)))


GATE_TABLE = {
    gate_local(selector, row_role): row_role
    for selector in SELECTORS
    for row_role in ROW_ROLES
}
GATE_RAW = cell.merge_raw(*(
    cell.raw_orbit(signature, output)
    for signature, output in GATE_TABLE.items()
))


def join_local(row_role: str) -> Signature:
    records = {
        (0, 0, 1): row_role,
        (0, 1, 0): GUIDE,
        (0, -1, 0): FRAME,
    }
    return c53.canonical_signature(c53.local_signature(records, (0, 0, 0)))


JOIN_TABLE = {join_local(row_role): row_role for row_role in ROW_ROLES}
JOIN_RAW = cell.merge_raw(*(
    cell.raw_orbit(signature, output)
    for signature, output in JOIN_TABLE.items()
))


TERMINAL_PATTERN = {
    (0, 1, 0): GUIDE,
    (-1, 0, 0): FRAME,
    (0, -1, 0): FRAME,
    (0, 0, -1): pivot.ROUTER_MARKER,
}


def terminal_local(row_role: str) -> Signature:
    records = {(0, 0, 1): row_role, **TERMINAL_PATTERN}
    return c53.canonical_signature(c53.local_signature(records, (0, 0, 0)))


TERMINAL_TABLE = {terminal_local(row_role): row_role for row_role in ROW_ROLES}
TERMINAL_RAW = cell.merge_raw(*(
    cell.raw_orbit(signature, output)
    for signature, output in TERMINAL_TABLE.items()
))
MERGED_RAW = cell.merge_raw(
    transport.MERGED_RAW, GATE_RAW, JOIN_RAW, TERMINAL_RAW
)
RAW_CONFLICTS = {
    signature: outputs for signature, outputs in MERGED_RAW.items()
    if len(outputs) != 1
}


SELECTOR_SITE = (0, 0, 0)
BRANCH_DIRECTIONS = ((1, 0, 0), (-1, 0, 0), (0, 1, 0))
PORT_DIRECTIONS = ((0, -1, 0), (0, 0, -1), (0, 0, 1))
COMMON = (0, 30, 0)
TERMINALS = ((1, 30, 0), (-1, 30, 0), (0, 30, 1))
PRETERMINALS = ((1, 29, 0), (-1, 29, 0), (0, 31, 1))
JOIN_GUIDE = (0, 31, 0)
JOIN_FRAME = (0, 29, 0)


def line_to(path: list[Coord], target: Coord, axes=(0, 1, 2)) -> None:
    current = list(path[-1])
    for axis in axes:
        while current[axis] != target[axis]:
            current[axis] += 1 if target[axis] > current[axis] else -1
            point = tuple(current)  # type: ignore[assignment]
            if point in path:
                raise ValueError(("path-self-contact", point, target))
            path.append(point)


def branch_paths() -> tuple[tuple[Coord, ...], ...]:
    starts = BRANCH_DIRECTIONS
    paths: list[list[Coord]] = []

    first = [starts[0], (1, -1, 0), (1, -2, 0), (1, -3, 0)]
    line_to(first, (20, -3, 0), (0,))
    line_to(first, (20, -3, -10), (2,))
    line_to(first, (20, 30, -10), (1,))
    line_to(first, (2, 30, -10), (0,))
    line_to(first, (2, 28, 0), (1, 2))
    line_to(first, (1, 28, 0), (0,))
    line_to(first, PRETERMINALS[0], (1,))
    paths.append(first)

    second = [starts[1], (-1, 0, -1), (-1, 0, -2), (-1, 0, -3)]
    line_to(second, (-20, 0, -3), (0,))
    line_to(second, (-20, 0, -20), (2,))
    line_to(second, (-20, 30, -20), (1,))
    line_to(second, (-2, 30, -20), (0,))
    line_to(second, (-2, 28, 0), (1, 2))
    line_to(second, (-1, 28, 0), (0,))
    line_to(second, PRETERMINALS[1], (1,))
    paths.append(second)

    third = [starts[2], (0, 1, 1), (0, 1, 2), (0, 1, 3)]
    line_to(third, (10, 1, 3), (0,))
    line_to(third, (10, 1, 20), (2,))
    line_to(third, (10, 30, 20), (1,))
    line_to(third, (0, 30, 20), (0,))
    line_to(third, (0, 32, 2), (1, 2))
    line_to(third, (0, 32, 1), (2,))
    line_to(third, PRETERMINALS[2], (1,))
    paths.append(third)

    for path, preterminal, terminal in zip(
        paths, PRETERMINALS, TERMINALS, strict=True
    ):
        if (
            path[-1] != preterminal
            or add(path[-1], cable.terminal_direction(tuple(path))) != terminal
        ):
            raise ValueError(("wrong-directed-terminal", path[-2:], preterminal, terminal))
    return tuple(map(tuple, paths))


PATHS = branch_paths()


def place(records: dict[Coord, str], site: Coord, role: str) -> None:
    prior = records.get(site)
    if prior is not None and prior != role:
        raise ValueError((site, prior, role))
    records[site] = role


def gate_fixed(selector: str, candidates: tuple[str, ...]):
    records: dict[Coord, str] = {SELECTOR_SITE: selector}
    socket_selectors = SOCKET_SELECTORS[len(candidates)]
    for direction, port, row_role, socket_selector in zip(
        BRANCH_DIRECTIONS[:len(candidates)],
        PORT_DIRECTIONS[:len(candidates)],
        candidates,
        socket_selectors,
        strict=True,
    ):
        target = direction
        bus = scale(2, direction)
        rx = port
        rz = neg(direction)
        ry = cable.cross(rz, rx)

        def moved(vector: Coord) -> Coord:
            return tuple(
                vector[0] * rx[index]
                + vector[1] * ry[index]
                + vector[2] * rz[index]
                for index in range(3)
            )  # type: ignore[return-value]

        place(records, bus, row_role)
        for local_direction, role in SOCKET_PATTERNS[socket_selector].items():
            place(records, add(target, moved(local_direction)), role)
    place(records, JOIN_GUIDE, GUIDE)
    place(records, JOIN_FRAME, FRAME)
    for terminal, preterminal in zip(
        TERMINALS[:len(candidates)], PRETERMINALS[:len(candidates)], strict=True
    ):
        rx = tuple(COMMON[index] - terminal[index] for index in range(3))
        rz = tuple(preterminal[index] - terminal[index] for index in range(3))
        ry = cable.cross(rz, rx)

        def terminal_moved(vector: Coord) -> Coord:
            return tuple(
                vector[0] * rx[index]
                + vector[1] * ry[index]
                + vector[2] * rz[index]
                for index in range(3)
            )  # type: ignore[return-value]

        for local_direction, role in TERMINAL_PATTERN.items():
            place(records, add(terminal, terminal_moved(local_direction)), role)
    return records


@lru_cache(maxsize=None)
def structural_scaffold(count: int):
    candidates = ROW_ROLES[:count]
    selector = (
        pivot.SEL_L1_G1 if count == 2 else pivot.SEL_L2_G2
    )
    fixed = gate_fixed(selector, candidates)
    items = tuple((role, PATHS[index]) for index, role in enumerate(candidates))
    all_path_sites = frozenset(site for _role, path in items for site in path)
    protected = frozenset({
        SELECTOR_SITE,
        COMMON,
        *BRANCH_DIRECTIONS[:count],
        *(scale(2, direction) for direction in BRANCH_DIRECTIONS[:count]),
        *TERMINALS[:count],
        *PRETERMINALS[:count],
        (0, 30, -1),
        *all_path_sites,
    })
    chosen, _outputs, terminal_ports = cable.multi_path_core(
        items,
        constraints=fixed,
        extra_protected=protected,
    )
    if terminal_ports != frozenset(TERMINALS[:count]):
        raise ValueError(("wrong-terminal-port", terminal_ports))
    starts = {path[0] for _role, path in items}
    scaffold = {
        site: role for site, role in chosen.items()
        if site not in starts
        and site not in {scale(2, direction) for direction in BRANCH_DIRECTIONS[:count]}
        and site != SELECTOR_SITE
    }
    return scaffold


def apparatus(selector: str, candidate_rows: tuple[tuple[int, ...], ...]):
    count = 2 if selector in {pivot.SEL_L1_G1, pivot.SEL_L1_P} else 3
    if len(candidate_rows) != count:
        raise ValueError((selector, len(candidate_rows), count))
    candidates = tuple(pivot.five.ROW_ROLE[row] for row in candidate_rows)
    selected_index = SELECTOR_INDEX[selector]
    selected_role = candidates[selected_index]
    records = gate_fixed(selector, candidates)
    for site, role in structural_scaffold(count).items():
        place(records, site, role)

    selected_path = PATHS[selected_index]
    expected = {site: selected_role for site in selected_path}
    expected[TERMINALS[selected_index]] = selected_role
    expected[COMMON] = selected_role
    dependencies = {selected_path[0]: frozenset()}
    dependencies.update({
        target: frozenset((previous,))
        for previous, target in zip(selected_path, selected_path[1:])
    })
    dependencies[TERMINALS[selected_index]] = frozenset((selected_path[-1],))
    dependencies[COMMON] = frozenset((TERMINALS[selected_index],))

    all_paths = PATHS[:count]
    all_path_sites = {site for path in all_paths for site in path}
    join_neighbors = {add(COMMON, direction) for direction in c53.DIRECTIONS}
    terminal_sites = set(TERMINALS[:count])
    core = set(records) | all_path_sites | terminal_sites | {COMMON} | join_neighbors
    cage = {
        add(site, direction)
        for site in core
        for direction in c53.DIRECTIONS
        if add(site, direction) not in core
    }
    for site in cage:
        place(records, site, FRAME)
    for site in all_path_sites | terminal_sites | {COMMON}:
        records.pop(site, None)
    return records, expected, dependencies, selected_role


def enabled(records):
    return {
        target: MERGED_RAW[signature]
        for target in c53.open_candidates(records)
        if (signature := c53.local_signature(records, target)) in MERGED_RAW
    }


def execute(prepared, rotation=None):
    initial, expected, dependencies, selected_role = prepared
    if rotation is not None:
        shift = (487, -491, 499)

        def moved(site):
            return add(c53.matvec(rotation, site), shift)

        initial = c53.transform_records(initial, rotation, shift)
        expected = c53.transform_records(expected, rotation, shift)
        dependencies = {
            moved(site): frozenset(moved(parent) for parent in parents)
            for site, parents in dependencies.items()
        }
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
    common = COMMON if rotation is None else moved(COMMON)
    return (
        not actual and records[common] == selected_role,
        (len(expected) + 1, edges, maximum, len(initial), len(expected), selected_role, actual),
    )


def main() -> int:
    print(
        "TABLE",
        len(GATE_TABLE),
        len(GATE_RAW),
        len(JOIN_TABLE),
        len(JOIN_RAW),
        len(TERMINAL_TABLE),
        len(TERMINAL_RAW),
        len(transport.MERGED_RAW),
        len(MERGED_RAW),
        len(set(GATE_RAW) & set(transport.MERGED_RAW)),
        len(set(JOIN_RAW) & set(cell.merge_raw(transport.MERGED_RAW, GATE_RAW))),
        len(set(TERMINAL_RAW) & set(cell.merge_raw(transport.MERGED_RAW, GATE_RAW, JOIN_RAW))),
        len(RAW_CONFLICTS),
    )
    if RAW_CONFLICTS:
        print("CONFLICT_SAMPLE", tuple(RAW_CONFLICTS.items())[:20])
    zero = (0, 0, 0, 0, 0)
    one = (1, 1, 1, 1, 1)
    alt = (0, 1, 0, 1, 0)
    failures = []
    shapes = set()
    cases = (
        (pivot.SEL_L1_G1, (zero, one)),
        (pivot.SEL_L1_P, (zero, one)),
        (pivot.SEL_L2_G2, (zero, one, alt)),
        (pivot.SEL_L2_P, (zero, one, alt)),
        (pivot.SEL_L2_PRODUCT, (zero, one, alt)),
    )
    for selector, rows in cases:
        for rotation_index, rotation in enumerate(c53.ROTATIONS):
            try:
                ok, detail = execute(apparatus(selector, rows), rotation)
            except ValueError as error:
                failures.append((selector, rotation_index, "layout", str(error)))
                continue
            if ok:
                shapes.add((selector, detail[:5]))
            else:
                failures.append((selector, rotation_index, detail))
    print("GRAPHS", len(cases) * 24, len(shapes), len(failures))
    if failures:
        print("FAILURE_SAMPLE", failures[:20])
    identity_failures = []
    identity_shapes = set()
    rows = tuple(pivot.five.ROLE_ROW.values())
    for selector, template in cases:
        selected_index = SELECTOR_INDEX[selector]
        for row in rows:
            candidate_rows = list(template)
            candidate_rows[selected_index] = row
            ok, detail = execute(apparatus(selector, tuple(candidate_rows)))
            if ok:
                identity_shapes.add((selector, detail[:5]))
            else:
                identity_failures.append((selector, row, detail))
    print("IDENTITY", len(cases) * len(rows), len(identity_shapes), len(identity_failures))
    if identity_failures:
        print("IDENTITY_FAILURE_SAMPLE", identity_failures[:20])

    deletion_failures = []
    for selector, rows in cases:
        initial, expected, _dependencies, selected = apparatus(selector, rows)
        without_selector = dict(initial)
        without_selector.pop(SELECTOR_SITE)
        if actual := enabled(without_selector):
            deletion_failures.append((selector, "selector", actual))
        selected_index = SELECTOR_INDEX[selector]
        selected_bus = scale(2, BRANCH_DIRECTIONS[selected_index])
        without_selected = dict(initial)
        without_selected.pop(selected_bus)
        if actual := enabled(without_selected):
            deletion_failures.append((selector, "selected-bus", actual))
        for index in range(len(rows)):
            if index == selected_index:
                continue
            without_unselected = dict(initial)
            without_unselected.pop(scale(2, BRANCH_DIRECTIONS[index]))
            wanted = {PATHS[selected_index][0]: frozenset((selected,))}
            if (actual := enabled(without_unselected)) != wanted:
                deletion_failures.append((selector, "unselected-bus", index, actual, wanted))
    print("DELETION", len(deletion_failures))
    result = (
        len(GATE_TABLE) == 160
        and len(GATE_RAW) == 3_840
        and len(JOIN_TABLE) == 32
        and len(JOIN_RAW) == 768
        and len(TERMINAL_TABLE) == 32
        and len(TERMINAL_RAW) == 768
        and len(MERGED_RAW) == 96_620
        and not RAW_CONFLICTS
        and not failures
        and not identity_failures
        and not deletion_failures
    )
    print("RESULT", "PHYSICAL_ISOLATED_ROW_MUX_COMMON_OUTPUT" if result else "OPEN")
    return 0 if result else 1


if __name__ == "__main__":
    raise SystemExit(main())
