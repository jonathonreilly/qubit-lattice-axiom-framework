#!/usr/bin/env python3
"""Build symplectic commutation from four physical ANDs and parity."""

from __future__ import annotations

from collections import deque
from itertools import product

import binary_xor_and_record_alu_probe_2026_07_15 as alu


d = alu.d
c53 = alu.c53
cell = alu.cell
Coord = tuple[int, int, int]
Signature = c53.Signature
FRAME = d.CAGE_ROLE
CENTER = (0, 0, 0)
TERMS = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0))
FRAMES = ((0, 0, 1), (0, 0, -1))

PARENT_GEOMETRY = (
    {"left": (2, 0, 0), "right": (1, 0, -1), "op": (1, 0, 1), "g1": (1, -1, 0), "g2": (1, 1, 0)},
    {"left": (-2, 0, 0), "right": (-1, 0, 1), "op": (-1, 0, -1), "g1": (-1, -1, 0), "g2": (-1, 1, 0)},
    {"left": (0, 2, 0), "right": (0, 1, 1), "op": (0, 1, -1), "g1": (-1, 1, 0), "g2": (1, 1, 0)},
    {"left": (0, -2, 0), "right": (0, -1, -1), "op": (0, -1, 1), "g1": (-1, -1, 0), "g2": (1, -1, 0)},
)


def parity_table():
    table: dict[Signature, str] = {}
    for values in product((0, 1), repeat=4):
        records = {site: alu.bit(value) for site, value in zip(TERMS, values)}
        records.update({site: FRAME for site in FRAMES})
        local = c53.canonical_signature(c53.local_signature(records, CENTER))
        output = alu.bit(sum(values) & 1)
        prior = table.get(local)
        if prior is not None and prior != output:
            raise ValueError((values, local, prior, output))
        table[local] = output
    return table


PARITY_TABLE = parity_table()
PARITY_RAW = cell.merge_raw(*(
    cell.raw_orbit(local, output)
    for local, output in PARITY_TABLE.items()
))
MERGED_RAW = cell.merge_raw(alu.MERGED_RAW, PARITY_RAW)
RAW_CONFLICTS = {
    local: values for local, values in MERGED_RAW.items() if len(values) != 1
}


def term_values(left, right):
    return (
        left[0] & right[2],
        left[2] & right[0],
        left[1] & right[3],
        left[3] & right[1],
    )


def source(left, right):
    inputs = (
        (left[0], right[2]),
        (left[2], right[0]),
        (left[1], right[3]),
        (left[3], right[1]),
    )
    records: dict[Coord, str] = {site: FRAME for site in FRAMES}
    for geometry, (first, second) in zip(PARENT_GEOMETRY, inputs):
        records[geometry["left"]] = alu.bit(first)
        records[geometry["right"]] = alu.bit(second)
        records[geometry["op"]] = alu.AND_ROLE
        records[geometry["g1"]] = FRAME
        records[geometry["g2"]] = FRAME

    core = set(records) | set(TERMS) | {CENTER}
    cage = {
        c53.add(site, direction)
        for site in core
        for direction in c53.DIRECTIONS
        if c53.add(site, direction) not in core
    }
    records.update({site: FRAME for site in cage})
    # The output holes must remain open after the shell is constructed.
    for site in (*TERMS, CENTER):
        records.pop(site, None)
    return records


def outputs(left, right):
    values = term_values(left, right)
    return {
        **{site: alu.bit(value) for site, value in zip(TERMS, values)},
        CENTER: alu.bit(sum(values) & 1),
    }


def enabled(records):
    return {
        target: MERGED_RAW[local]
        for target in c53.open_candidates(records)
        if (local := c53.local_signature(records, target)) in MERGED_RAW
    }


def graph(left, right, rotation=None):
    initial = source(left, right)
    expected = outputs(left, right)
    if rotation is not None:
        shift = (73, -79, 83)
        initial = c53.transform_records(initial, rotation, shift)
        expected = c53.transform_records(expected, rotation, shift)
    sites = tuple(expected)
    index = {site: bit for bit, site in enumerate(sites)}
    all_mask = (1 << len(sites)) - 1
    queue = deque((0,))
    seen = {0}
    edges = 0
    bad = []
    terminals = 0
    maximum = 0
    while queue:
        mask = queue.popleft()
        records = dict(initial)
        records.update({site: expected[site] for site, bit_index in index.items() if mask >> bit_index & 1})
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
    print("PARITY", len(PARITY_TABLE), len(PARITY_RAW), len(MERGED_RAW), len(RAW_CONFLICTS))
    if RAW_CONFLICTS:
        print("CONFLICT_SAMPLE", tuple(RAW_CONFLICTS.items())[:20])
    failures = []
    totals = [0, 0]
    rows = tuple(product((0, 1), repeat=5))
    for rotation_index, rotation in enumerate(c53.ROTATIONS):
        for left in rows:
            for right in rows:
                result = graph(left, right, rotation)
                if result != (17, 33, 1, 4, ()):  # four independent terms, then parity
                    failures.append((rotation_index, left, right, result))
                totals[0] += result[0]
                totals[1] += result[1]
    print("GRAPHS", 24 * 32 * 32, totals, len(failures))
    if failures:
        print("FAILURE_SAMPLE", failures[:20])
    result = not RAW_CONFLICTS and not failures
    print("RESULT", "PHYSICAL_SYMPLECTIC_COMMUTATION" if result else "OPEN")
    return 0 if result else 1


if __name__ == "__main__":
    raise SystemExit(main())
