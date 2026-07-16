#!/usr/bin/env python3
"""Expose the phase bit of one signed-row role through a physical port."""

from __future__ import annotations

from itertools import product

import physical_row_reader_payload_tap_probe_2026_07_16 as tap


ported = tap.ported
terminal = ported.terminal
cell = tap.cell
c53 = tap.c53
five = ported.five
FRAME = tap.FRAME
Coord = tuple[int, int, int]
Signature = c53.Signature
ROWS = tuple(product((0, 1), repeat=5))
SOURCE = (0, 0, 0)
TARGET = (1, 0, 0)
PORT = (2, 0, 0)
INDEX = (1, 0, 1)
FIXED = {
    INDEX: terminal.INDEX_ROLES[4],
    (1, 1, 0): FRAME,
    (1, -1, 0): FRAME,
    (1, 0, -1): FRAME,
}


def local(row) -> Signature:
    records = {
        SOURCE: five.ROW_ROLE[row],
        **FIXED,
    }
    return c53.canonical_signature(c53.local_signature(records, TARGET))


CANONICAL_TABLE = {
    local(row): ported.bit(row[4])
    for row in ROWS
}
SIGN_RAW = cell.merge_raw(*(
    cell.raw_orbit(signature, output)
    for signature, output in CANONICAL_TABLE.items()
))
OVERLAP = set(SIGN_RAW) & set(tap.MERGED_RAW)
MERGED_RAW = cell.merge_raw(tap.MERGED_RAW, SIGN_RAW)
RAW_CONFLICTS = {
    signature: outputs
    for signature, outputs in MERGED_RAW.items()
    if len(outputs) != 1
}


def apparatus(row):
    records = {
        SOURCE: five.ROW_ROLE[row],
        **FIXED,
    }
    dynamic = {TARGET, PORT}
    core = set(records) | dynamic
    cage = {
        c53.add(site, direction)
        for site in core
        for direction in c53.DIRECTIONS
        if c53.add(site, direction) not in core
    }
    records.update({site: FRAME for site in cage})
    records.pop(TARGET, None)
    records.pop(PORT, None)
    return records


def enabled(records):
    return {
        target: MERGED_RAW[signature]
        for target in c53.open_candidates(records)
        if (signature := c53.local_signature(records, target)) in MERGED_RAW
    }


def graph(row, rotation=None):
    initial = apparatus(row)
    expected = {TARGET: ported.bit(row[4])}
    port = PORT
    if rotation is not None:
        shift = (449, -457, 461)
        initial = c53.transform_records(initial, rotation, shift)
        expected = c53.transform_records(expected, rotation, shift)
        port = next(iter(c53.transform_records({PORT: "port"}, rotation, shift)))
    actual = enabled(initial)
    wanted = {
        target: frozenset((output,))
        for target, output in expected.items()
    }
    if actual != wanted:
        return False, ("initial", actual, wanted, len(initial))
    records = dict(initial)
    records.update(expected)
    terminal = enabled(records)
    return (
        not terminal and port not in records,
        (2, 1, 1, len(initial), tuple(sorted(terminal.items()))),
    )


def deletion_failures():
    failures = []
    parents = (SOURCE, *FIXED)
    for row in ROWS:
        initial = apparatus(row)
        for parent in parents:
            altered = dict(initial)
            altered.pop(parent, None)
            if TARGET in enabled(altered):
                failures.append((row, parent, enabled(altered)[TARGET]))
    return tuple(failures)


def main() -> int:
    print(
        "LAW",
        len(tap.MERGED_RAW),
        len(CANONICAL_TABLE),
        len(SIGN_RAW),
        len(OVERLAP),
        len(MERGED_RAW),
        len(RAW_CONFLICTS),
    )
    if RAW_CONFLICTS:
        print("CONFLICT_SAMPLE", tuple(RAW_CONFLICTS.items())[:10])
    failures = []
    sizes = set()
    for rotation_index, rotation in enumerate(c53.ROTATIONS):
        for row in ROWS:
            ok, detail = graph(row, rotation)
            if not ok:
                failures.append((rotation_index, row, detail))
            else:
                sizes.add(detail)
    deletions = deletion_failures()
    print("GRAPHS", 24 * len(ROWS), sorted(sizes), len(failures))
    print("DELETIONS", len(ROWS) * (1 + len(FIXED)), len(deletions))
    if failures or deletions:
        print("FAILURE_SAMPLE", (failures[:3], deletions[:3]))

    result = (
        len(CANONICAL_TABLE) == 32
        and len(SIGN_RAW) == 768
        and not OVERLAP
        and len(MERGED_RAW) == 98_156
        and not RAW_CONFLICTS
        and not failures
        and not deletions
    )
    print("RESULT", "PHYSICAL_PORTED_SIGN_READER" if result else "OPEN")
    return 0 if result else 1


if __name__ == "__main__":
    raise SystemExit(main())
