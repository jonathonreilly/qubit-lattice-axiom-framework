#!/usr/bin/env python3
"""Bind two transported physical rows through the retained commuting multiplier."""

from __future__ import annotations

from collections import deque
from functools import lru_cache
from itertools import product

import physical_isolated_row_mux_common_output_probe_2026_07_15 as prior


m = prior.pivot.mult
cable = prior.cable
c53 = prior.c53
FRAME = prior.FRAME
MERGED_RAW = prior.MERGED_RAW
Coord = tuple[int, int, int]
ROWS = tuple(product((0, 1), repeat=5))
LEFT_PATH = ((0, 0, 6), (0, 0, 5), (0, 0, 4), (0, 0, 3), (0, 0, 2), m.LEFT)
RIGHT_PATH = ((0, 0, -6), (0, 0, -5), (0, 0, -4), (0, 0, -3), (0, 0, -2), m.RIGHT)
OUTPUT_PATH = (m.TARGET, (0, -1, 0), (1, -1, 0), (2, -1, 0), (3, -1, 0), (4, -1, 0))
OUTPUT_PORT = (5, -1, 0)


def add(left: Coord, right: Coord) -> Coord:
    return tuple(a + b for a, b in zip(left, right))  # type: ignore[return-value]


def place(records: dict[Coord, str], site: Coord, role: str) -> None:
    old = records.get(site)
    if old is not None and old != role:
        raise ValueError((site, old, role))
    records[site] = role


@lru_cache(maxsize=1)
def scaffold():
    zero = (0, 0, 0, 0, 0)
    role = m.five.ROW_ROLE[zero]
    fixed = {**{site: m.FRAME_ROLE for site in m.FRAMES}, m.PORT_FRAME: m.FRAME_ROLE}
    items = ((role, LEFT_PATH), (role, RIGHT_PATH), (role, OUTPUT_PATH))
    path_sites = frozenset(site for _value, path in items for site in path)
    chosen, _expected, ports = cable.multi_path_core(
        items, constraints=fixed, extra_protected=path_sites
    )
    if ports != frozenset((m.TARGET, OUTPUT_PORT)):
        raise ValueError(("wrong-ports", ports))
    sources = {LEFT_PATH[0], RIGHT_PATH[0], OUTPUT_PATH[0]}
    return {
        site: value for site, value in chosen.items()
        if site not in sources and site not in path_sites
    }


def apparatus(left, right):
    if m.algebra.symplectic(left, right):
        raise ValueError((left, right, "noncommuting"))
    product_row = m.algebra.multiply_commuting(left, right)
    left_role = m.five.ROW_ROLE[left]
    right_role = m.five.ROW_ROLE[right]
    product_role = m.five.ROW_ROLE[product_row]
    records: dict[Coord, str] = {
        LEFT_PATH[0]: left_role,
        RIGHT_PATH[0]: right_role,
        **{site: m.FRAME_ROLE for site in m.FRAMES},
        m.PORT_FRAME: m.FRAME_ROLE,
    }
    for site, role in scaffold().items():
        place(records, site, role)

    expected = {
        **{site: left_role for site in LEFT_PATH[1:]},
        **{site: right_role for site in RIGHT_PATH[1:]},
        m.TARGET: product_role,
        **{site: product_role for site in OUTPUT_PATH[1:]},
    }
    dependencies = {
        LEFT_PATH[1]: frozenset(),
        RIGHT_PATH[1]: frozenset(),
    }
    dependencies.update({
        target: frozenset((previous,))
        for path in (LEFT_PATH, RIGHT_PATH)
        for previous, target in zip(path[1:], path[2:])
    })
    dependencies[m.TARGET] = frozenset((m.LEFT, m.RIGHT))
    dependencies.update({
        target: frozenset((previous,))
        for previous, target in zip(OUTPUT_PATH, OUTPUT_PATH[1:])
    })

    path_sites = set(LEFT_PATH) | set(RIGHT_PATH) | set(OUTPUT_PATH)
    core = set(records) | path_sites | {OUTPUT_PORT}
    cage = {
        add(site, direction)
        for site in core
        for direction in c53.DIRECTIONS
        if add(site, direction) not in core
    }
    for site in cage:
        place(records, site, FRAME)
    for site in set(expected) | {OUTPUT_PORT}:
        records.pop(site, None)
    return records, expected, dependencies, product_role


def enabled(records):
    return {
        target: MERGED_RAW[signature]
        for target in c53.open_candidates(records)
        if (signature := c53.local_signature(records, target)) in MERGED_RAW
    }


def graph(left, right, rotation=None):
    initial, expected, _dependencies, product_role = apparatus(left, right)
    output_port = OUTPUT_PORT
    if rotation is not None:
        shift = (503, -509, 521)
        initial = c53.transform_records(initial, rotation, shift)
        expected = c53.transform_records(expected, rotation, shift)
        output_port = next(iter(c53.transform_records({OUTPUT_PORT: "port"}, rotation, shift)))
    sites = tuple(expected)
    index = {site: bit for bit, site in enumerate(sites)}
    all_mask = (1 << len(sites)) - 1
    queue = deque((0,))
    seen = {0}
    edges = 0
    terminals = 0
    maximum = 0
    bad = []
    while queue:
        mask = queue.popleft()
        records = dict(initial)
        records.update({
            site: expected[site]
            for site, bit in index.items()
            if mask >> bit & 1
        })
        actual = enabled(records)
        wrong = {
            site: values for site, values in actual.items()
            if site not in expected or values != frozenset((expected[site],))
        }
        if wrong:
            bad.append((mask, wrong))
            continue
        futures = tuple(
            site for site in actual
            if site in index and not (mask >> index[site] & 1)
        )
        maximum = max(maximum, len(futures))
        if mask == all_mask:
            terminals += int(not actual)
            if actual or output_port in records:
                bad.append((mask, actual, output_port in records))
            continue
        if not futures:
            bad.append((mask, "dead"))
            continue
        for site in futures:
            edges += 1
            future = mask | 1 << index[site]
            if future not in seen:
                seen.add(future)
                queue.append(future)
    return len(seen), edges, terminals, maximum, tuple(bad), len(initial), product_role


def main() -> int:
    pairs = tuple(
        (left, right)
        for left in ROWS
        for right in ROWS
        if not m.algebra.symplectic(left, right)
    )
    representative = ((1, 0, 0, 1, 0), (0, 1, 1, 0, 1))
    failures = []
    shapes = set()
    for left, right in pairs:
        result = graph(left, right)
        shapes.add(result[:6])
        if result[:5] != (42, 66, 1, 2, ()):
            failures.append((left, right, result))
    rotation_failures = []
    rotation_shapes = set()
    for rotation_index, rotation in enumerate(c53.ROTATIONS):
        result = graph(*representative, rotation=rotation)
        rotation_shapes.add(result[:6])
        if result[:5] != (42, 66, 1, 2, ()):
            rotation_failures.append((rotation_index, result))
    deletion_failures = []
    for label, source in (("left", LEFT_PATH[0]), ("right", RIGHT_PATH[0])):
        initial, _expected, _dependencies, _product = apparatus(*representative)
        initial.pop(source)
        actual = enabled(initial)
        wanted = {
            RIGHT_PATH[1]: frozenset((m.five.ROW_ROLE[representative[1]],))
        } if label == "left" else {
            LEFT_PATH[1]: frozenset((m.five.ROW_ROLE[representative[0]],))
        }
        if actual != wanted:
            deletion_failures.append((label, actual, wanted))
    print("LAW", len(MERGED_RAW), len(pairs), len(scaffold()))
    print("GRAPHS", len(pairs), shapes, len(failures))
    print("ROTATIONS", len(c53.ROTATIONS), rotation_shapes, len(rotation_failures))
    print("DELETION", len(deletion_failures))
    if failures or rotation_failures or deletion_failures:
        print("FAILURE_SAMPLE", failures[:5], rotation_failures[:5], deletion_failures[:5])
    result = (
        len(MERGED_RAW) == 96_620
        and len(pairs) == 544
        and not failures
        and not rotation_failures
        and not deletion_failures
    )
    print("RESULT", "PHYSICAL_TRANSPORT_BOUND_COMMUTING_MULTIPLIER" if result else "OPEN")
    return 0 if result else 1


if __name__ == "__main__":
    raise SystemExit(main())
