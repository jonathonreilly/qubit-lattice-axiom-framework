#!/usr/bin/env python3
"""Fan one physical signed-Pauli row role into its five literal H0/H1 bits."""

from __future__ import annotations

from collections import deque
from itertools import product

import physical_four_case_pivot_router_probe_2026_07_15 as pivot


d = pivot.d
five = pivot.five
c53 = pivot.c53
cell = pivot.cell
Coord = tuple[int, int, int]
Signature = c53.Signature
FRAME = d.CAGE_ROLE

SOURCE = (0, 0, 0)
DIRECTIONS = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1))
TARGETS = tuple(DIRECTIONS)
INDEX_SITES = tuple(tuple(2 * value for value in direction) for direction in DIRECTIONS)
INDEX_ROLES = tuple(d.PREFIX_ROLES[44:49])
TARGET_INDEX = dict(zip(TARGETS, INDEX_ROLES, strict=True))


def bit(value: int) -> str:
    return d.H1 if value else d.H0


def local(row, bit_index: int) -> Signature:
    target = TARGETS[bit_index]
    records = {
        SOURCE: five.ROW_ROLE[row],
        INDEX_SITES[bit_index]: INDEX_ROLES[bit_index],
    }
    for direction in c53.DIRECTIONS:
        site = c53.add(target, direction)
        if site not in {SOURCE, INDEX_SITES[bit_index]}:
            records[site] = FRAME
    return c53.canonical_signature(c53.local_signature(records, target))


CANONICAL_TABLE: dict[Signature, str] = {}
for row in product((0, 1), repeat=5):
    for bit_index in range(5):
        signature = local(row, bit_index)
        output = bit(row[bit_index])
        prior = CANONICAL_TABLE.get(signature)
        if prior is not None and prior != output:
            raise ValueError((row, bit_index, prior, output, signature))
        CANONICAL_TABLE[signature] = output

FANOUT_RAW = cell.merge_raw(*(
    cell.raw_orbit(signature, output)
    for signature, output in CANONICAL_TABLE.items()
))
MERGED_RAW = cell.merge_raw(pivot.MERGED_RAW, FANOUT_RAW)
RAW_CONFLICTS = {
    signature: values for signature, values in MERGED_RAW.items() if len(values) != 1
}


def source(row):
    records: dict[Coord, str] = {
        SOURCE: five.ROW_ROLE[row],
        **{site: role for site, role in zip(INDEX_SITES, INDEX_ROLES, strict=True)},
    }
    for target in TARGETS:
        for direction in c53.DIRECTIONS:
            site = c53.add(target, direction)
            if site not in {SOURCE, *TARGETS, *INDEX_SITES}:
                records[site] = FRAME
    # The sixth face of the source is a quiet backstop.
    records[(0, 0, -1)] = FRAME
    core = set(records) | set(TARGETS)
    cage = {
        c53.add(site, direction)
        for site in core
        for direction in c53.DIRECTIONS
        if c53.add(site, direction) not in core
    }
    records.update({site: FRAME for site in cage})
    for target in TARGETS:
        records.pop(target, None)
    return records


def outputs(row):
    return {target: bit(value) for target, value in zip(TARGETS, row, strict=True)}


def enabled(records):
    return {
        target: MERGED_RAW[signature]
        for target in c53.open_candidates(records)
        if (signature := c53.local_signature(records, target)) in MERGED_RAW
    }


def graph(row, rotation=None):
    initial = source(row)
    expected = outputs(row)
    if rotation is not None:
        shift = (113, -127, 131)
        initial = c53.transform_records(initial, rotation, shift)
        expected = c53.transform_records(expected, rotation, shift)
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
    print("ROLES", len(five.ROW_ROLE), INDEX_ROLES)
    print(
        "TABLE",
        len(CANONICAL_TABLE),
        len(FANOUT_RAW),
        len(MERGED_RAW),
        len(RAW_CONFLICTS),
    )
    if RAW_CONFLICTS:
        print("CONFLICT_SAMPLE", tuple(RAW_CONFLICTS.items())[:20])
    failures = []
    instances = 0
    sizes = set()
    for rotation_index, rotation in enumerate(c53.ROTATIONS):
        for row in product((0, 1), repeat=5):
            result = graph(row, rotation)
            instances += 1
            if result != (32, 80, 1, 5, ()):
                failures.append((rotation_index, row, result))
            else:
                sizes.add(len(source(row)))
    print("GRAPHS", instances, sorted(sizes), len(failures))
    if failures:
        print("FAILURE_SAMPLE", failures[:20])
    result = not RAW_CONFLICTS and not failures
    print("RESULT", "PHYSICAL_ROW_ROLE_LITERAL_FANOUT" if result else "OPEN")
    return 0 if result else 1


if __name__ == "__main__":
    raise SystemExit(main())
