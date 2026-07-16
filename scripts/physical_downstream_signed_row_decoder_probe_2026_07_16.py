#!/usr/bin/env python3
"""Decode a signed row's phase through a downstream physical output port."""

from __future__ import annotations

from itertools import product

import physical_row_reader_payload_tap_probe_2026_07_16 as tap


ported = tap.ported
terminal = ported.terminal
cable = tap.cable
cell = tap.cell
c53 = tap.c53
five = ported.five
FRAME = tap.FRAME
H0 = ported.d.H0
H1 = ported.d.H1
Coord = tuple[int, int, int]
Signature = c53.Signature
ROWS = tuple(product((0, 1), repeat=5))
SOURCE = ported.SOURCE
ROW_TAP = tap.TAP
SIGN_TARGET = (0, 0, 2)
SIGN_INDEX = (1, 0, 2)
SIGN_PORT = (0, 0, 3)
SIGN_FRAMES = {
    (-1, 0, 2): FRAME,
    (0, 1, 2): FRAME,
    (0, -1, 2): FRAME,
}
SIGN_PATH = (
    SIGN_TARGET,
    SIGN_PORT,
    (0, 0, 4),
    (0, 0, 5),
)
TERMINAL_PORT = (0, 0, 6)


def add(left: Coord, right: Coord) -> Coord:
    return tuple(a + b for a, b in zip(left, right))  # type: ignore[return-value]


def place(records: dict[Coord, str], site: Coord, role: str) -> None:
    previous = records.get(site)
    if previous is not None and previous != role:
        raise ValueError(("placement-conflict", site, previous, role))
    records[site] = role


def sign_local(row) -> Signature:
    records = {
        ROW_TAP: five.ROW_ROLE[row],
        SIGN_INDEX: terminal.INDEX_ROLES[4],
        **SIGN_FRAMES,
    }
    return c53.canonical_signature(
        c53.local_signature(records, SIGN_TARGET)
    )


SIGN_TABLE = {
    sign_local(row): ported.bit(row[4])
    for row in ROWS
}
SIGN_RAW = cell.merge_raw(*(
    cell.raw_orbit(signature, output)
    for signature, output in SIGN_TABLE.items()
))
OVERLAP = set(SIGN_RAW) & set(tap.MERGED_RAW)
MERGED_RAW = cell.merge_raw(tap.MERGED_RAW, SIGN_RAW)
RAW_CONFLICTS = {
    signature: outputs
    for signature, outputs in MERGED_RAW.items()
    if len(outputs) != 1
}


def apparatus(row):
    row_role = five.ROW_ROLE[row]
    sign_role = ported.bit(row[4])
    records: dict[Coord, str] = {
        SOURCE: row_role,
        **{
            site: role
            for site, role in zip(
                ported.INDEX_SITES,
                ported.INDEX_ROLES,
                strict=True,
            )
        },
        **{site: FRAME for site in ported.TARGETS},
        (0, 0, -1): FRAME,
        SIGN_INDEX: terminal.INDEX_ROLES[4],
        **SIGN_FRAMES,
    }
    structural, cable_outputs, terminal_port = cable.path_core(
        sign_role,
        SIGN_PATH,
        constraints=records,
        extra_protected=frozenset((ROW_TAP, SIGN_TARGET)),
    )
    if terminal_port != TERMINAL_PORT:
        raise ValueError(("wrong-terminal-port", terminal_port))
    structural.pop(SIGN_TARGET, None)
    records = dict(structural)
    expected = {
        ROW_TAP: row_role,
        SIGN_TARGET: sign_role,
        **cable_outputs,
    }
    dependencies = {
        ROW_TAP: frozenset(),
        SIGN_TARGET: frozenset((ROW_TAP,)),
    }
    for previous, target in zip(SIGN_PATH, SIGN_PATH[1:]):
        dependencies[target] = frozenset((previous,))

    dynamic = set(expected) | {terminal_port}
    shell = {
        add(site, direction)
        for site in dynamic
        for direction in c53.DIRECTIONS
    }
    core = set(records) | dynamic | shell
    cage = {
        add(site, direction)
        for site in core
        for direction in c53.DIRECTIONS
        if add(site, direction) not in core
    }
    for site in cage:
        place(records, site, FRAME)
    for site in dynamic:
        records.pop(site, None)
    return records, expected, dependencies, terminal_port, SIGN_PATH[-1]


def enabled(records):
    return {
        target: MERGED_RAW[signature]
        for target in c53.open_candidates(records)
        if (signature := c53.local_signature(records, target)) in MERGED_RAW
    }


def transformed(prepared, rotation):
    initial, expected, dependencies, terminal_port, endpoint = prepared
    shift = (431, -433, 439)

    def moved(site):
        return add(c53.matvec(rotation, site), shift)

    return (
        c53.transform_records(initial, rotation, shift),
        c53.transform_records(expected, rotation, shift),
        {
            moved(site): frozenset(moved(parent) for parent in parents)
            for site, parents in dependencies.items()
        },
        moved(terminal_port),
        moved(endpoint),
    )


def run(row, rotation=None):
    prepared = apparatus(row)
    if rotation is not None:
        prepared = transformed(prepared, rotation)
    initial, expected, dependencies, terminal_port, endpoint = prepared
    records = dict(initial)
    formed = set()
    actual = enabled(records)
    edges = maximum = 0
    while len(formed) < len(expected):
        frontier = {
            target: frozenset((expected[target],))
            for target, parents in dependencies.items()
            if target not in formed and parents <= formed
        }
        maximum = max(maximum, len(frontier))
        if actual != frontier:
            return False, (
                "frontier",
                len(formed),
                actual,
                frontier,
                len(initial),
            )
        target = min(frontier)
        records[target] = expected[target]
        formed.add(target)
        edges += len(frontier)
        actual.pop(target, None)
        for direction in c53.DIRECTIONS:
            candidate = add(target, direction)
            if candidate in records:
                actual.pop(candidate, None)
                continue
            signature = c53.local_signature(records, candidate)
            if signature in MERGED_RAW:
                actual[candidate] = MERGED_RAW[signature]
            else:
                actual.pop(candidate, None)
    return (
        not actual and terminal_port not in records,
        (
            len(expected) + 1,
            edges,
            maximum,
            len(initial),
            records[endpoint],
            tuple(sorted(actual.items())),
        ),
    )


def deletion_failures():
    failures = []
    for row in ROWS:
        initial, expected, dependencies, _terminal_port, _endpoint = apparatus(row)
        records = dict(initial)
        formed = set()
        actual = enabled(records)
        controls = {
            ("tap-source", ROW_TAP): SOURCE,
            **{
                ("tap-index-" + str(index), ROW_TAP): site
                for index, site in enumerate(ported.INDEX_SITES)
            },
            ("sign-row-parent", SIGN_TARGET): ROW_TAP,
            ("sign-index", SIGN_TARGET): SIGN_INDEX,
            **{
                ("sign-frame-" + str(index), SIGN_TARGET): site
                for index, site in enumerate(SIGN_FRAMES)
            },
        }
        while len(formed) < len(expected):
            frontier = {
                target: frozenset((expected[target],))
                for target, parents in dependencies.items()
                if target not in formed and parents <= formed
            }
            if actual != frontier:
                failures.append((row, "frontier", actual, frontier))
                break
            for (label, child), parent in tuple(controls.items()):
                if child not in actual:
                    continue
                role = records.pop(parent, None)
                if role is None:
                    failures.append((row, label, "missing-parent", parent))
                elif c53.local_signature(records, child) in MERGED_RAW:
                    failures.append((row, label, "child-survives", child))
                records[parent] = role
                del controls[(label, child)]
            target = min(frontier)
            records[target] = expected[target]
            formed.add(target)
            actual.pop(target, None)
            for direction in c53.DIRECTIONS:
                candidate = add(target, direction)
                if candidate in records:
                    actual.pop(candidate, None)
                    continue
                signature = c53.local_signature(records, candidate)
                if signature in MERGED_RAW:
                    actual[candidate] = MERGED_RAW[signature]
                else:
                    actual.pop(candidate, None)
        if controls:
            failures.append((row, "unreached-controls", controls))
    return tuple(failures)


def main() -> int:
    print(
        "LAW",
        len(tap.MERGED_RAW),
        len(SIGN_TABLE),
        len(SIGN_RAW),
        len(OVERLAP),
        len(MERGED_RAW),
        len(RAW_CONFLICTS),
    )
    if RAW_CONFLICTS:
        print("CONFLICT_SAMPLE", tuple(RAW_CONFLICTS.items())[:10])

    failures = []
    shapes = set()
    for rotation_index, rotation in enumerate(c53.ROTATIONS):
        for row in ROWS:
            ok, detail = run(row, rotation)
            if not ok:
                failures.append((rotation_index, row, detail))
            else:
                shapes.add(detail)
    deletions = deletion_failures()
    print("GRAPHS", 24 * len(ROWS), sorted(shapes), len(failures))
    print("DELETIONS", len(ROWS) * 10, len(deletions))
    if failures or deletions:
        print("FAILURE_SAMPLE", (failures[:3], deletions[:3]))

    result = (
        len(SIGN_TABLE) == 32
        and not RAW_CONFLICTS
        and all(len(outputs) == 1 for outputs in MERGED_RAW.values())
        and not failures
        and not deletions
    )
    print(
        "RESULT",
        "PHYSICAL_DOWNSTREAM_SIGNED_ROW_DECODER" if result else "OPEN",
    )
    return 0 if result else 1


if __name__ == "__main__":
    raise SystemExit(main())
