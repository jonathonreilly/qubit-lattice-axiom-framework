#!/usr/bin/env python3
"""Expose one whole-row payload tap beside retained physical row readers."""

from __future__ import annotations

from collections import deque
from itertools import product

import physical_transport_bound_commuting_multiplier_probe_2026_07_15 as prior
import physical_three_row_spacious_commutator_bind_probe_2026_07_15 as readers


ported = readers.ported
twoport = readers.twoport
cable = readers.cable
c53 = readers.c53
cell = readers.isolation.cell
FRAME = readers.FRAME
Coord = tuple[int, int, int]
ROWS = tuple(product((0, 1), repeat=5))
SOURCE = (0, 0, 0)
TAP = (0, 0, 1)
PAYLOAD_PATH = (
    TAP,
    (0, 0, 2),
    (0, 0, 3),
    (0, 0, 4),
    (1, 0, 4),
    (2, 0, 4),
)
PAYLOAD_PORT = (3, 0, 4)


def add(left: Coord, right: Coord) -> Coord:
    return tuple(a + b for a, b in zip(left, right))  # type: ignore[return-value]


def tap_local(role: str):
    records = {
        SOURCE: role,
        **{
            site: index_role
            for site, index_role in zip(
                ported.INDEX_SITES, ported.INDEX_ROLES, strict=True
            )
        },
    }
    return c53.canonical_signature(c53.local_signature(records, TAP))


TAP_TABLE = {tap_local(role): role for role in ported.five.ROLE_ROW}
TAP_RAW = cell.merge_raw(*(
    cell.raw_orbit(signature, output)
    for signature, output in TAP_TABLE.items()
))
MERGED_RAW = cell.merge_raw(prior.MERGED_RAW, TAP_RAW)
RAW_CONFLICTS = {
    signature: outputs
    for signature, outputs in MERGED_RAW.items()
    if len(outputs) != 1
}


def place(records: dict[Coord, str], site: Coord, role: str) -> None:
    old = records.get(site)
    if old is not None and old != role:
        raise ValueError((site, old, role))
    records[site] = role


def payload_items(role: str):
    return ((role, PAYLOAD_PATH),)


def apparatus(row, mode: str):
    role = ported.five.ROW_ROLE[row]
    if mode == "ported":
        records = ported.interface_source(row)
        expected = dict(ported.outputs(row))
        bit_items = ()
        bit_ports = frozenset(ported.PORTS)
    elif mode == "twoport":
        records = twoport.interface_source(row)
        expected = dict(twoport.outputs(row))
        bit_items = tuple(
            (twoport.bit(row[bit_index]), path)
            for bit_index, paths in enumerate(twoport.PATHS)
            for path in paths
        )
        bit_ports = twoport.EXTERNAL_PORTS
    else:
        raise ValueError(mode)

    records.pop(TAP)
    items = (*bit_items, *payload_items(role))
    protected = frozenset(
        {PAYLOAD_PORT, *bit_ports}
        | {site for _value, path in items for site in path}
    )
    records, cable_outputs, ports = cable.multi_path_core(
        items,
        constraints=records,
        extra_protected=protected,
    )
    generated_ports = (
        frozenset((PAYLOAD_PORT,))
        if mode == "ported"
        else frozenset({PAYLOAD_PORT, *bit_ports})
    )
    wanted_ports = frozenset({PAYLOAD_PORT, *bit_ports})
    if ports != generated_ports:
        raise ValueError(("wrong-ports", mode, ports, generated_ports))
    expected.update(cable_outputs)
    expected[TAP] = role

    core = set(records) | set(expected) | set(wanted_ports)
    cage = {
        add(site, direction)
        for site in core
        for direction in c53.DIRECTIONS
        if add(site, direction) not in core
    }
    for site in cage:
        place(records, site, FRAME)
    for site in set(expected) | set(wanted_ports):
        records.pop(site, None)
    return records, expected, wanted_ports


def enabled(records):
    return {
        target: MERGED_RAW[signature]
        for target in c53.open_candidates(records)
        if (signature := c53.local_signature(records, target)) in MERGED_RAW
    }


def graph(row, mode: str, rotation=None):
    initial, expected, ports = apparatus(row, mode)
    if rotation is not None:
        shift = (523, -541, 547)
        initial = c53.transform_records(initial, rotation, shift)
        expected = c53.transform_records(expected, rotation, shift)
        ports = frozenset(
            c53.transform_records({site: "port" for site in ports}, rotation, shift)
        )
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
    return len(seen), edges, terminals, maximum, tuple(bad), len(initial), len(expected)


def main() -> int:
    print(
        "LAW",
        len(TAP_TABLE),
        len(TAP_RAW),
        len(prior.MERGED_RAW),
        len(MERGED_RAW),
        len(set(TAP_RAW) & set(prior.MERGED_RAW)),
        len(RAW_CONFLICTS),
    )
    failures = []
    shapes = {}
    for mode in ("ported", "twoport"):
        counts = set()
        for row in ROWS:
            result = graph(row, mode)
            counts.add(result)
            if result[4]:
                failures.append((mode, row, result))
        shapes[mode] = counts
    representative = (0, 1, 0, 1, 0)
    rotation_shapes = {}
    for mode in ("ported", "twoport"):
        counts = set()
        for rotation_index, rotation in enumerate(c53.ROTATIONS):
            result = graph(representative, mode, rotation)
            counts.add(result)
            if result[4]:
                failures.append((mode, rotation_index, result))
        rotation_shapes[mode] = counts
    deletion_failures = []
    for mode in ("ported", "twoport"):
        initial, _expected, _ports = apparatus(representative, mode)
        initial.pop(SOURCE)
        if actual := enabled(initial):
            deletion_failures.append((mode, actual))
    print("IDENTITY", shapes)
    print("ROTATIONS", rotation_shapes)
    print("DELETION", len(deletion_failures))
    if failures or deletion_failures:
        print("FAILURE_SAMPLE", failures[:10], deletion_failures[:10])
    result = (
        len(TAP_TABLE) == 32
        and len(TAP_RAW) == 768
        and len(MERGED_RAW) == 97_388
        and not RAW_CONFLICTS
        and not failures
        and not deletion_failures
    )
    print("RESULT", "PHYSICAL_ROW_READER_PAYLOAD_TAP" if result else "OPEN")
    return 0 if result else 1


if __name__ == "__main__":
    raise SystemExit(main())
