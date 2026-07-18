#!/usr/bin/env python3
"""Probe a four-value case-role cable for pivot spatial isolation."""

from __future__ import annotations

from collections import deque

import physical_three_row_dual_commutation_bind_probe_2026_07_15 as prior


pivot = prior.ported.terminal.pivot
cable = prior.cable
cell = prior.twoport.cell
d = prior.d
c53 = prior.c53
Coord = tuple[int, int, int]
FRAME = prior.FRAME
SOURCE = (0, 0, 0)
PATHS = (
    (SOURCE, (0, 0, -1), (0, 0, -2), (1, 0, -2), (2, 0, -2), (3, 0, -2)),
    (SOURCE, (0, -1, 0), (0, -2, 0), (0, -2, 1), (0, -2, 2), (0, -2, 3)),
)


def canonical_local(role: str, kind: str):
    target = (0, 0, 0)
    previous = (0, 0, 1)
    future = (0, 0, -1) if kind == "straight" else (1, 0, 0)
    observed, records = cable.segment_records(target, previous, future, role)
    if observed != kind:
        raise AssertionError((observed, kind))
    return c53.canonical_signature(c53.local_signature(records, target))


CANONICAL_TABLE = {
    canonical_local(role, kind): role
    for role in pivot.CASE_ROLES
    for kind in ("straight", "turn")
}
CASE_CABLE_RAW = cell.merge_raw(*(
    cell.raw_orbit(signature, output)
    for signature, output in CANONICAL_TABLE.items()
))
MERGED_RAW = cell.merge_raw(prior.MERGED_RAW, CASE_CABLE_RAW)
RAW_CONFLICTS = {
    signature: outputs for signature, outputs in MERGED_RAW.items()
    if len(outputs) != 1
}


def add(left: Coord, right: Coord) -> Coord:
    return tuple(a + b for a, b in zip(left, right))  # type: ignore[return-value]


def apparatus(role: str):
    items = tuple((role, path) for path in PATHS)
    protected = frozenset(site for _value, path in items for site in path)
    records, expected, ports = cable.multi_path_core(
        items, extra_protected=protected
    )
    starts = {path[0] for _value, path in items}
    records = {
        site: value for site, value in records.items()
        if site not in set(expected) and (site in starts or value in {FRAME, cable.GUIDE_ROLE})
    }
    core = set(records) | set(expected) | set(ports)
    cage = {
        add(site, direction)
        for site in core
        for direction in c53.DIRECTIONS
        if add(site, direction) not in core
    }
    records.update({site: FRAME for site in cage})
    for site in set(expected) | set(ports):
        records.pop(site, None)
    return records, expected, ports


def enabled(records):
    return {
        target: MERGED_RAW[signature]
        for target in c53.open_candidates(records)
        if (signature := c53.local_signature(records, target)) in MERGED_RAW
    }


def graph(role: str, rotation=None):
    initial, expected, ports = apparatus(role)
    if rotation is not None:
        shift = (449, -457, 461)
        initial = c53.transform_records(initial, rotation, shift)
        expected = c53.transform_records(expected, rotation, shift)
        ports = frozenset(c53.transform_records(
            {site: "port" for site in ports}, rotation, shift
        ))
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
            if actual or set(ports) & set(records):
                bad.append((mask, actual, set(ports) & set(records)))
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
    for role in pivot.CASE_ROLES:
        for rotation_index, rotation in enumerate(c53.ROTATIONS):
            result = graph(role, rotation)
            if result[:5] != (36, 60, 1, 2, ()):
                failures.append((role, rotation_index, result))
            else:
                sizes.add(result[5])
    deletion_failures = []
    for role in pivot.CASE_ROLES:
        initial, _expected, _ports = apparatus(role)
        initial.pop(SOURCE)
        if actual := enabled(initial):
            deletion_failures.append((role, actual))
    print(
        "TABLE",
        len(CANONICAL_TABLE),
        len(CASE_CABLE_RAW),
        len(MERGED_RAW),
        len(RAW_CONFLICTS),
    )
    print("GRAPHS", 4 * 24, sorted(sizes), len(failures))
    print("DELETION", len(deletion_failures))
    if failures or deletion_failures or RAW_CONFLICTS:
        print("FAILURE_SAMPLE", failures[:5], deletion_failures[:5], tuple(RAW_CONFLICTS.items())[:5])
    result = (
        len(CANONICAL_TABLE) == 8
        and not RAW_CONFLICTS
        and not failures
        and not deletion_failures
    )
    print("RESULT", "PHYSICAL_CASE_ROLE_ISOLATION_CABLE" if result else "OPEN")
    return 0 if result else 1


if __name__ == "__main__":
    raise SystemExit(main())
