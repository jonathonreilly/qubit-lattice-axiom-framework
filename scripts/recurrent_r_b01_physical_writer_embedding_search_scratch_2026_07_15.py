#!/usr/bin/env python3
"""Search recurrent-cell embeddings of a physical R_B01 byte writer.

The direct C->D root row is removed.  A rotated copy of the proven Cycle-121
self-caging writer geometry is anchored with its completion at that root and
retargeted to 10010001 -> R_B01.  A static survivor must fit twice, one period
apart, under the same canonical rows before any exhaustive graph is attempted.

Scratch search only; no foundation, registry, policy, audit, or git authority.
"""

from __future__ import annotations

from collections import Counter

import recurrent_post_oz_payload_prototype_2026_07_15 as payload


c141 = payload.c141
cell = payload.cell
c112 = payload.c112
Coord = c141.Coord


# Cycle-121 writer coordinates relative to its completion site (5,4,-2).
TEMPLATE: dict[str, Coord] = {
    "D0": (-1, -3, 1),
    "D1": (-1, -2, 1),
    "D2": (-1, -1, 0),
    "D3": (0, -2, 1),
    "D4": (-1, -1, 1),
    "D5": (0, -1, 1),
    "D6": (0, 0, 1),
    "D7": (-1, 0, 1),
    "FRONT": (-1, -2, 0),
    "TAIL": (0, 0, 2),
    "MID": (0, -1, 2),
    "INHERITED": (0, -1, 0),
    "JOIN": (-1, 0, 0),
    "COMPLETION": (0, 0, 0),
}
OUTPUTS = {
    "D0": "H1",
    "D1": "H0",
    "D2": "H0",
    "D3": "H1",
    "D4": "H0",
    "D5": "H0",
    "D6": "H0",
    "D7": "H1",
    "FRONT": "T_H3",
    "TAIL": "R_B41",
    "MID": "T_H3",
    "INHERITED": "H1",
    "JOIN": "R_C00",
    "COMPLETION": "R_B01",
}
SEQUENCE = (
    "D0", "D1", "FRONT", "D2", "D3", "D4",
    "TAIL", "MID", "D5", "INHERITED", "D7", "D6",
    "JOIN", "COMPLETION",
)


def transform_relative(rotation, root: Coord, relative: Coord) -> Coord:
    standard = c141.add(root, cell.c52.matvec(rotation, relative))
    return c141.transform_site(standard)


def root_row_orbit():
    canonical = next(
        signature
        for signature, origin in cell.ORIGINS.items()
        if origin[:4] == ("rail", "C", "D", 4)
    )
    local = cell.ORIGINS[canonical][4]
    return cell.raw_orbit(local, "R_B01"), local


DIRECT_ROOT_ROW, DIRECT_ROOT_LOCAL = root_row_orbit()
BASE_RAW = {
    local: values
    for local, values in c141.FULL_RAW.items()
    if local not in DIRECT_ROOT_ROW
}


def put_slice(records: dict[Coord, str], x: int, old: str, new: str, *, stop: int | None = None):
    path = cell.PATHS[(old, new)]
    limit = len(path) if stop is None else stop
    for yz in path[:limit]:
        records[c141.transform_site(cell.site(x, yz))] = cell.CONTENT[(new, yz)]
    if stop is None:
        for yz in cell.EXTRA_ORDERS[new]:
            records[c141.transform_site(cell.site(x, yz))] = cell.CONTENT[(new, yz)]


def first_pre_root_records() -> dict[Coord, str]:
    records = dict(c141.BASE)
    records[c141.LOWER] = c141.LOWER_VALUE
    records[c141.GUARD] = c141.GUARD_VALUE
    put_slice(records, 1, "A", "B")
    put_slice(records, 2, "B", "C")
    put_slice(records, 3, "C", "D", stop=4)
    return records


def advance_to_second_pre_root(records: dict[Coord, str]) -> None:
    # The first root/completion already exists.  Finish D, then A/B/C, the
    # first socket, and its newly retained payload before testing recurrence.
    path = cell.PATHS[("C", "D")]
    for yz in path[5:]:
        records[c141.transform_site(cell.site(3, yz))] = cell.CONTENT[("D", yz)]
    for yz in cell.EXTRA_ORDERS["D"]:
        records[c141.transform_site(cell.site(3, yz))] = cell.CONTENT[("D", yz)]
    put_slice(records, 4, "D", "A")
    put_slice(records, 5, "A", "B")
    for site, output in (
        (cell.site(5, cell.NOTCH_YZ), cell.HELPER_CONTENT),
        (cell.site(4, cell.NOTCH_YZ), cell.H1),
        (cell.site(3, cell.NOTCH_YZ), cell.OZ),
        (cell.site(3, (-1, 1)), payload.RELAY_VALUE),
        (cell.site(3, (-2, 1)), payload.PAYLOAD_VALUE),
        (cell.site(3, (-3, 1)), payload.TERMINAL_VALUE),
    ):
        records[c141.transform_site(site)] = output
    put_slice(records, 6, "B", "C")
    put_slice(records, 7, "C", "D", stop=4)


def raw_matches(records: dict[Coord, str], raw) -> tuple[Coord, ...]:
    return tuple(sorted(
        target
        for target in c112.c53.open_candidates(records)
        if c112.c53.local_signature(records, target) in raw
    ))


def build_first(rotation):
    records = first_pre_root_records()
    root = cell.site(3, cell.ROOT_YZ)
    sites = {
        name: transform_relative(rotation, root, relative)
        for name, relative in TEMPLATE.items()
    }
    if len(set(sites.values())) != len(sites):
        return None, ("self-overlap",)
    occupied = tuple(sorted(
        (name, site, records[site])
        for name, site in sites.items()
        if site in records
    ))
    if occupied:
        return None, ("occupied", occupied)

    table = {}
    locals_seen = []
    exact_targets = []
    for name in SEQUENCE:
        target = sites[name]
        output = OUTPUTS[name]
        local = c112.c53.local_signature(records, target)
        if not local:
            return None, ("empty", name, target)
        canonical = cell.canonical(local)
        prior = table.get(canonical)
        if prior is not None and prior != output:
            return None, ("canonical-conflict", name, prior, output, canonical)
        orbit = cell.raw_orbit(local, output)
        matches = raw_matches(records, orbit)
        if matches != (target,):
            return None, ("coimages", name, target, matches, local)
        table[canonical] = output
        records[target] = output
        locals_seen.append(canonical)
        exact_targets.append(matches)

    writer_raw = c141.replacement_probe.merge_raw(*(
        cell.raw_orbit(signature, output)
        for signature, output in table.items()
    ))
    union = c141.replacement_probe.merge_raw(BASE_RAW, writer_raw)
    if any(len(values) != 1 for values in union.values()):
        conflicts = tuple(
            (local, values, BASE_RAW.get(local), writer_raw.get(local))
            for local, values in union.items()
            if len(values) != 1
        )
        return None, ("raw-conflict", conflicts[:3])
    return {
        "records": records,
        "sites1": sites,
        "table": table,
        "locals1": tuple(locals_seen),
        "writer_raw": writer_raw,
        "union": union,
    }, None


def test_second(rotation, candidate):
    records = dict(candidate["records"])
    advance_to_second_pre_root(records)
    root = cell.site(7, cell.ROOT_YZ)
    sites = {
        name: transform_relative(rotation, root, relative)
        for name, relative in TEMPLATE.items()
    }
    cross = set(sites.values()) & set(candidate["sites1"].values())
    if cross:
        return None, ("period-overlap", tuple(sorted(cross)))
    occupied = tuple(sorted(
        (name, site, records[site])
        for name, site in sites.items()
        if site in records
    ))
    if occupied:
        return None, ("second-occupied", occupied)

    locals_seen = []
    for name in SEQUENCE:
        target = sites[name]
        output = OUTPUTS[name]
        local = c112.c53.local_signature(records, target)
        canonical = cell.canonical(local)
        values = candidate["union"].get(local)
        if values != frozenset((output,)):
            return None, ("second-row", name, target, local, values)
        if canonical != candidate["locals1"][len(locals_seen)]:
            return None, (
                "nonrecurrent-local", name,
                candidate["locals1"][len(locals_seen)], canonical,
            )
        records[target] = output
        locals_seen.append(canonical)
    return {**candidate, "records2": records, "sites2": sites}, None


def main() -> None:
    print("DIRECT_ROOT_LOCAL", DIRECT_ROOT_LOCAL)
    print("DIRECT_ROOT_RAW", len(DIRECT_ROOT_ROW))
    print("BASE_RAW", len(BASE_RAW))
    reasons = Counter()
    details = {}
    survivors = []
    for index, rotation in enumerate(cell.c52.ROTATIONS):
        candidate, failure = build_first(rotation)
        if failure is not None:
            reasons[failure[0]] += 1
            details.setdefault(failure[0], (index, failure))
            continue
        recurrent, failure = test_second(rotation, candidate)
        if failure is not None:
            reasons[failure[0]] += 1
            details.setdefault(failure[0], (index, failure))
            continue
        survivors.append((index, recurrent))

    print("REASONS", reasons)
    for reason, detail in details.items():
        print("FIRST", reason, detail)
    print("SURVIVORS", len(survivors))
    for index, candidate in survivors:
        print(
            "SURVIVOR", index,
            "canonical", len(candidate["table"]),
            "raw", len(candidate["writer_raw"]),
            "union", len(candidate["union"]),
            "sites1", tuple(candidate["sites1"].items()),
        )
    print("RESULT", "STATIC_RECURRENT_WRITER_SURVIVOR" if survivors else "NO_STATIC_TEMPLATE_SURVIVOR")


if __name__ == "__main__":
    main()
