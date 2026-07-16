#!/usr/bin/env python3
"""Fork one physical H0/H1 record into two independent cable branches."""

from __future__ import annotations

from collections import deque

import physical_literal_bit_cable_probe_2026_07_15 as cable


d = cable.d
c53 = cable.c53
Coord = tuple[int, int, int]
FRAME = cable.FRAME
MERGED_RAW = cable.MERGED_RAW
SOURCE = (0, 0, 0)
PATHS = (
    (SOURCE, (1, 0, 0), (2, 0, 0), (3, 0, 0)),
    (SOURCE, (0, 1, 0), (0, 2, 0), (0, 3, 0)),
)


def place(records: dict[Coord, str], site: Coord, role: str) -> None:
    prior = records.get(site)
    if prior is not None and prior != role:
        raise ValueError((site, prior, role))
    records[site] = role


def apparatus(value: str):
    records, expected, terminal_ports = cable.multi_path_core(
        tuple((value, path) for path in PATHS)
    )
    core = set(records) | set(expected) | set(terminal_ports)
    cage = {
        cable.add(site, direction)
        for site in core
        for direction in c53.DIRECTIONS
        if cable.add(site, direction) not in core
    }
    for site in cage:
        place(records, site, FRAME)
    for site in (*expected, *terminal_ports):
        records.pop(site, None)
    return records, expected, terminal_ports


def enabled(records):
    return {
        target: MERGED_RAW[signature]
        for target in c53.open_candidates(records)
        if (signature := c53.local_signature(records, target)) in MERGED_RAW
    }


def graph(value: str, rotation=None):
    initial, expected, terminal_ports = apparatus(value)
    if rotation is not None:
        shift = (331, -337, 347)
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
    for value in (d.H0, d.H1):
        for rotation_index, rotation in enumerate(c53.ROTATIONS):
            result = graph(value, rotation)
            if result[:5] != (16, 24, 1, 2, ()):
                failures.append((value, rotation_index, result))
            else:
                sizes.add(result[5])
    deletion_failures = []
    for value in (d.H0, d.H1):
        initial, _expected, _ports = apparatus(value)
        without_source = dict(initial)
        without_source.pop(SOURCE)
        if enabled(without_source):
            deletion_failures.append((value, enabled(without_source)))
    print("LAW", len(MERGED_RAW), MERGED_RAW is cable.MERGED_RAW)
    print("GRAPHS", 2 * len(c53.ROTATIONS), sorted(sizes), len(failures))
    print("SOURCE_DELETIONS", len(deletion_failures), deletion_failures[:1])
    if failures:
        print("FAILURE_SAMPLE", failures[:20])
    result = not failures and not deletion_failures
    print("RESULT", "PHYSICAL_LITERAL_BIT_FORK" if result else "OPEN")
    return 0 if result else 1


if __name__ == "__main__":
    raise SystemExit(main())
