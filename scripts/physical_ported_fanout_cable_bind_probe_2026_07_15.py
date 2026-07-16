#!/usr/bin/env python3
"""Bind the four ported row bits to four physical straight copy cables."""

from __future__ import annotations

from collections import deque
from itertools import product

import physical_ported_symplectic_row_fanout_probe_2026_07_15 as ported


cable = ported.cable
d = ported.d
c53 = ported.c53
Coord = tuple[int, int, int]
FRAME = d.CAGE_ROLE
MERGED_RAW = ported.MERGED_RAW


def scale(factor: int, vector: Coord) -> Coord:
    return tuple(factor * value for value in vector)  # type: ignore[return-value]


def place(records: dict[Coord, str], site: Coord, role: str) -> None:
    prior = records.get(site)
    if prior is not None and prior != role:
        raise ValueError((site, prior, role))
    records[site] = role


def apparatus(row):
    records = ported.interface_source(row)
    expected = ported.outputs(row)
    terminal_ports = set()
    paths = []
    for bit_index, direction in enumerate(ported.TARGETS):
        path = tuple(scale(step, direction) for step in range(1, 5))
        value = ported.bit(row[bit_index])
        core, cable_outputs, terminal_port = cable.path_core(value, path)
        core.pop(path[0], None)
        for site, role in core.items():
            place(records, site, role)
        expected.update(cable_outputs)
        terminal_ports.add(terminal_port)
        paths.append(path)

    core_sites = set(records) | set(expected) | terminal_ports
    cage = {
        c53.add(site, direction)
        for site in core_sites
        for direction in c53.DIRECTIONS
        if c53.add(site, direction) not in core_sites
    }
    for site in cage:
        place(records, site, FRAME)
    for site in (*expected, *terminal_ports):
        records.pop(site, None)
    return records, expected, terminal_ports, tuple(paths)


def enabled(records):
    return {
        target: MERGED_RAW[signature]
        for target in c53.open_candidates(records)
        if (signature := c53.local_signature(records, target)) in MERGED_RAW
    }


def graph(row, rotation=None):
    initial, expected, terminal_ports, _paths = apparatus(row)
    if rotation is not None:
        shift = (233, -239, 241)
        initial = c53.transform_records(initial, rotation, shift)
        expected = c53.transform_records(expected, rotation, shift)
        terminal_ports = set(c53.transform_records({site: "x" for site in terminal_ports}, rotation, shift))
    sites = tuple(expected)
    index = {site: bit_index for bit_index, site in enumerate(sites)}
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
            for site, bit_index in index.items()
            if mask >> bit_index & 1
        })
        actual = enabled(records)
        wrong = {
            site: values
            for site, values in actual.items()
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
            if actual:
                bad.append((mask, actual))
            if terminal_ports & set(records):
                bad.append((mask, "terminal-port-filled", terminal_ports & set(records)))
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
    return len(seen), edges, terminals, maximum, tuple(bad)


def main() -> int:
    failures = []
    sizes = set()
    instances = 0
    for rotation_index, rotation in enumerate(c53.ROTATIONS):
        for row in product((0, 1), repeat=5):
            result = graph(row, rotation)
            instances += 1
            if result != (625, 2_000, 1, 4, ()):
                failures.append((rotation_index, row, result))
            else:
                sizes.add(len(apparatus(row)[0]))
    print("GRAPHS", instances, sorted(sizes), len(failures))
    if failures:
        print("FAILURE_SAMPLE", failures[:20])
    print("RESULT", "PHYSICAL_PORTED_FANOUT_CABLE_BIND" if not failures else "OPEN")
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
