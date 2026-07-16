#!/usr/bin/env python3
"""Produce four two-port row bits and fork each into two cable endpoints."""

from __future__ import annotations

from collections import deque
from itertools import product

import physical_ported_symplectic_row_fanout_probe_2026_07_15 as ported


cable = ported.cable
d = ported.d
c53 = ported.c53
cell = ported.cell
five = ported.five
Coord = tuple[int, int, int]
Signature = c53.Signature
FRAME = ported.FRAME
SOURCE = (0, 0, 0)
TARGETS = ported.TARGETS
INDEX_SITES = ported.INDEX_SITES
INDEX_ROLES = ported.INDEX_ROLES
UP = (0, 0, 1)
DOWN = (0, 0, -1)
OUTWARD_PORTS = ported.PORTS
LOWER_PORTS = tuple(c53.add(target, DOWN) for target in TARGETS)


def scale(factor: int, vector: Coord) -> Coord:
    return tuple(factor * value for value in vector)  # type: ignore[return-value]


def bit(value: int) -> str:
    return d.H1 if value else d.H0


def local(row, bit_index: int) -> Signature:
    target = TARGETS[bit_index]
    records = {
        SOURCE: five.ROW_ROLE[row],
        INDEX_SITES[bit_index]: INDEX_ROLES[bit_index],
    }
    open_sites = {
        OUTWARD_PORTS[bit_index],
        LOWER_PORTS[bit_index],
    }
    for direction in c53.DIRECTIONS:
        site = c53.add(target, direction)
        if site not in {SOURCE, INDEX_SITES[bit_index], *open_sites}:
            records[site] = FRAME
    return c53.canonical_signature(c53.local_signature(records, target))


CANONICAL_TABLE: dict[Signature, str] = {}
for row in product((0, 1), repeat=5):
    for bit_index in range(4):
        signature = local(row, bit_index)
        output = bit(row[bit_index])
        prior = CANONICAL_TABLE.get(signature)
        if prior is not None and prior != output:
            raise ValueError((row, bit_index, prior, output, signature))
        CANONICAL_TABLE[signature] = output

TWO_PORT_RAW = cell.merge_raw(*(
    cell.raw_orbit(signature, output)
    for signature, output in CANONICAL_TABLE.items()
))
MERGED_RAW = cell.merge_raw(ported.MERGED_RAW, TWO_PORT_RAW)
RAW_CONFLICTS = {
    signature: values for signature, values in MERGED_RAW.items()
    if len(values) != 1
}


def interface_source(row):
    records: dict[Coord, str] = {
        SOURCE: five.ROW_ROLE[row],
        **{
            site: role
            for site, role in zip(INDEX_SITES, INDEX_ROLES, strict=True)
        },
        UP: FRAME,
        DOWN: FRAME,
    }
    for bit_index, target in enumerate(TARGETS):
        open_sites = {
            OUTWARD_PORTS[bit_index],
            LOWER_PORTS[bit_index],
        }
        for direction in c53.DIRECTIONS:
            site = c53.add(target, direction)
            if site not in {SOURCE, INDEX_SITES[bit_index], *open_sites}:
                prior = records.get(site)
                if prior is not None and prior != FRAME:
                    raise ValueError((site, prior, FRAME, target))
                records[site] = FRAME
    return records


def outputs(row):
    return {
        target: bit(row[bit_index])
        for bit_index, target in enumerate(TARGETS)
    }


PATHS = tuple(
    (
        (target, outward),
        (target, lower),
    )
    for target, outward, lower in zip(
        TARGETS, OUTWARD_PORTS, LOWER_PORTS, strict=True
    )
)
EXTERNAL_PORTS = frozenset(
    site
    for bit_paths in PATHS
    for path in bit_paths
    for site in (cable.add(path[-1], cable.terminal_direction(path)),)
)


def place(records: dict[Coord, str], site: Coord, role: str) -> None:
    prior = records.get(site)
    if prior is not None and prior != role:
        raise ValueError((site, prior, role))
    records[site] = role


def apparatus(row):
    records = interface_source(row)
    expected = outputs(row)
    items = []
    for bit_index, paths in enumerate(PATHS):
        value = bit(row[bit_index])
        items.extend((value, path) for path in paths)
    records, cable_outputs, terminal_ports = cable.multi_path_core(
        tuple(items), constraints=records
    )
    if terminal_ports != EXTERNAL_PORTS:
        raise ValueError(("wrong-terminal-ports", terminal_ports, EXTERNAL_PORTS))
    expected.update(cable_outputs)

    core = set(records) | set(expected) | set(EXTERNAL_PORTS)
    cage = {
        c53.add(site, direction)
        for site in core
        for direction in c53.DIRECTIONS
        if c53.add(site, direction) not in core
    }
    for site in cage:
        place(records, site, FRAME)
    for site in (*expected, *EXTERNAL_PORTS):
        records.pop(site, None)
    return records, expected, EXTERNAL_PORTS


def enabled(records):
    return {
        target: MERGED_RAW[signature]
        for target in c53.open_candidates(records)
        if (signature := c53.local_signature(records, target)) in MERGED_RAW
    }


def graph(row, rotation=None):
    initial, expected, terminal_ports = apparatus(row)
    if rotation is not None:
        shift = (373, -379, 383)
        initial = c53.transform_records(initial, rotation, shift)
        expected = c53.transform_records(expected, rotation, shift)
        terminal_ports = frozenset(
            c53.transform_records(
                {site: "port" for site in terminal_ports}, rotation, shift
            )
        )
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
            site
            for site in actual
            if site in index and not (mask >> index[site] & 1)
        )
        maximum = max(maximum, len(futures))
        if mask == all_mask:
            terminals += int(not actual)
            if actual:
                bad.append((mask, "terminal", actual))
            if set(terminal_ports) & set(records):
                bad.append((mask, "port-filled", set(terminal_ports) & set(records)))
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
    return len(seen), edges, terminals, maximum, tuple(bad), len(initial)


def main() -> int:
    failures = []
    sizes = set()
    rows = tuple(product((0, 1), repeat=5))
    for row in rows:
        result = graph(row)
        if result[:5] != (625, 2_500, 1, 8, ()):
            failures.append(("row", row, result))
        else:
            sizes.add(result[5])
    representative = (0, 1, 0, 1, 0)
    for rotation_index, rotation in enumerate(c53.ROTATIONS):
        result = graph(representative, rotation)
        if result[:5] != (625, 2_500, 1, 8, ()):
            failures.append(("rotation", rotation_index, result))
    print(
        "TABLE",
        len(CANONICAL_TABLE),
        len(TWO_PORT_RAW),
        len(MERGED_RAW),
        len(RAW_CONFLICTS),
    )
    print("GRAPHS", len(rows) + len(c53.ROTATIONS), sorted(sizes), len(failures))
    if failures:
        print("FAILURE_SAMPLE", failures[:20])
    result = not RAW_CONFLICTS and not failures
    print("RESULT", "PHYSICAL_TWO_PORT_ROW_FOUR_FORK" if result else "OPEN")
    return 0 if result else 1


if __name__ == "__main__":
    raise SystemExit(main())
