#!/usr/bin/env python3
"""Expose four symplectic row bits with one open transport port per output."""

from __future__ import annotations

from collections import deque
from itertools import product

import physical_literal_bit_cable_probe_2026_07_15 as cable


terminal = cable.fanout
d = cable.d
five = terminal.five
c53 = cable.c53
cell = cable.cell
Coord = tuple[int, int, int]
Signature = c53.Signature
FRAME = d.CAGE_ROLE
SOURCE = (0, 0, 0)
TARGETS = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0))
PORTS = tuple(tuple(2 * value for value in target) for target in TARGETS)
INDEX_SITES = tuple(c53.add(target, (0, 0, 1)) for target in TARGETS)
INDEX_ROLES = terminal.INDEX_ROLES[:4]


def bit(value: int) -> str:
    return d.H1 if value else d.H0


def local(row, bit_index: int) -> Signature:
    target = TARGETS[bit_index]
    port = PORTS[bit_index]
    index_site = INDEX_SITES[bit_index]
    records = {
        SOURCE: five.ROW_ROLE[row],
        index_site: INDEX_ROLES[bit_index],
    }
    for direction in c53.DIRECTIONS:
        site = c53.add(target, direction)
        if site not in {SOURCE, port, index_site}:
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

PORTED_RAW = cell.merge_raw(*(
    cell.raw_orbit(signature, output)
    for signature, output in CANONICAL_TABLE.items()
))
MERGED_RAW = cell.merge_raw(cable.MERGED_RAW, PORTED_RAW)
RAW_CONFLICTS = {
    signature: values for signature, values in MERGED_RAW.items() if len(values) != 1
}


def interface_source(row):
    records: dict[Coord, str] = {
        SOURCE: five.ROW_ROLE[row],
        **{site: role for site, role in zip(INDEX_SITES, INDEX_ROLES, strict=True)},
        (0, 0, -1): FRAME,
        (0, 0, 1): FRAME,
    }
    for bit_index, target in enumerate(TARGETS):
        for direction in c53.DIRECTIONS:
            site = c53.add(target, direction)
            if site not in {SOURCE, PORTS[bit_index], INDEX_SITES[bit_index]}:
                prior = records.get(site)
                if prior is not None and prior != FRAME:
                    raise ValueError((site, prior, FRAME, target))
                records[site] = FRAME
    return records


def source(row):
    records = interface_source(row)
    core = set(records) | set(TARGETS) | set(PORTS)
    cage = {
        c53.add(site, direction)
        for site in core
        for direction in c53.DIRECTIONS
        if c53.add(site, direction) not in core
    }
    records.update({site: FRAME for site in cage})
    for site in (*TARGETS, *PORTS):
        records.pop(site, None)
    return records


def outputs(row):
    return {target: bit(value) for target, value in zip(TARGETS, row[:4], strict=True)}


def enabled(records):
    return {
        target: MERGED_RAW[signature]
        for target in c53.open_candidates(records)
        if (signature := c53.local_signature(records, target)) in MERGED_RAW
    }


def graph(row, rotation=None):
    initial = source(row)
    expected = outputs(row)
    ports = {site: "port" for site in PORTS}
    if rotation is not None:
        shift = (223, -227, 229)
        initial = c53.transform_records(initial, rotation, shift)
        expected = c53.transform_records(expected, rotation, shift)
        ports = c53.transform_records(ports, rotation, shift)
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
            if set(ports) & set(records):
                bad.append((mask, "port-filled", set(ports) & set(records)))
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
    print("ROLES", INDEX_ROLES)
    print("TABLE", len(CANONICAL_TABLE), len(PORTED_RAW), len(MERGED_RAW), len(RAW_CONFLICTS))
    if RAW_CONFLICTS:
        print("CONFLICT_SAMPLE", tuple(RAW_CONFLICTS.items())[:20])
    failures = []
    sizes = set()
    for rotation_index, rotation in enumerate(c53.ROTATIONS):
        for row in product((0, 1), repeat=5):
            result = graph(row, rotation)
            if result != (16, 32, 1, 4, ()):
                failures.append((rotation_index, row, result))
            else:
                sizes.add(len(source(row)))
    print("GRAPHS", 24 * 32, sorted(sizes), len(failures))
    if failures:
        print("FAILURE_SAMPLE", failures[:20])
    result = not RAW_CONFLICTS and not failures
    print("RESULT", "PHYSICAL_PORTED_SYMPLECTIC_ROW_FANOUT" if result else "OPEN")
    return 0 if result else 1


if __name__ == "__main__":
    raise SystemExit(main())
