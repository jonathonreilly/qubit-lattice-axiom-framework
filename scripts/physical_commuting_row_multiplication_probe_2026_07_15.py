#!/usr/bin/env python3
"""Physical role-level multiplication of commuting signed Pauli rows."""

from __future__ import annotations

from itertools import product

import literal_bit_alu_symplectic_commutation_cycle150_2026_07_15 as c150


p = c150.p
alu = p.alu
compact = alu.compact
five = compact.five
algebra = compact.algebra
d = alu.d
c53 = alu.c53
cell = alu.cell
Coord = tuple[int, int, int]
Signature = c53.Signature
TARGET = (0, 0, 0)
LEFT = (0, 0, 1)
RIGHT = (0, 0, -1)
FRAMES = ((1, 0, 0), (-1, 0, 0), (0, 1, 0))
PORT = (0, -1, 0)
PORT_FRAME = (0, -2, 0)
FRAME_ROLE = d.CAGE_ROLE
ROWS = tuple(product((0, 1), repeat=5))


def local(left, right):
    records = {
        LEFT: five.ROW_ROLE[left],
        RIGHT: five.ROW_ROLE[right],
        **{site: FRAME_ROLE for site in FRAMES},
    }
    return c53.canonical_signature(c53.local_signature(records, TARGET))


def build_table():
    table: dict[Signature, str] = {}
    for left in ROWS:
        for right in ROWS:
            if algebra.symplectic(left, right):
                continue
            signature = local(left, right)
            output = five.ROW_ROLE[algebra.multiply_commuting(left, right)]
            prior = table.get(signature)
            if prior is not None and prior != output:
                raise ValueError((left, right, prior, output, signature))
            table[signature] = output
    return table


CANONICAL_TABLE = build_table()
MULTIPLY_RAW = cell.merge_raw(*(
    cell.raw_orbit(signature, output)
    for signature, output in CANONICAL_TABLE.items()
))
MERGED_RAW = cell.merge_raw(p.MERGED_RAW, MULTIPLY_RAW)
RAW_CONFLICTS = {
    signature: values for signature, values in MERGED_RAW.items() if len(values) != 1
}


def source(left, right):
    records = {
        LEFT: five.ROW_ROLE[left],
        RIGHT: five.ROW_ROLE[right],
        PORT_FRAME: FRAME_ROLE,
        **{site: FRAME_ROLE for site in FRAMES},
    }
    core = set(records) | {TARGET, PORT}
    cage = {
        c53.add(site, direction)
        for site in core
        for direction in c53.DIRECTIONS
        if c53.add(site, direction) not in core
    }
    records.update({site: FRAME_ROLE for site in cage})
    records.pop(TARGET, None)
    records.pop(PORT, None)
    return records


def enabled(records):
    return {
        target: MERGED_RAW[signature]
        for target in c53.open_candidates(records)
        if (signature := c53.local_signature(records, target)) in MERGED_RAW
    }


def run(left, right, rotation=None):
    records = source(left, right)
    expected_site = TARGET
    expected_value = five.ROW_ROLE[algebra.multiply_commuting(left, right)]
    if rotation is not None:
        shift = (89, -97, 101)
        records = c53.transform_records(records, rotation, shift)
        transformed = c53.transform_records({TARGET: expected_value}, rotation, shift)
        expected_site, expected_value = next(iter(transformed.items()))
    actual = enabled(records)
    wanted = {expected_site: frozenset((expected_value,))}
    if actual != wanted:
        return False, (actual, wanted, len(records))
    records[expected_site] = expected_value
    if (actual := enabled(records)):
        return False, ("terminal", actual, len(records))
    return True, len(records)


def main() -> int:
    commuting = tuple((left, right) for left in ROWS for right in ROWS if not algebra.symplectic(left, right))
    print("TABLE", len(commuting), len(CANONICAL_TABLE), len(MULTIPLY_RAW), len(MERGED_RAW), len(RAW_CONFLICTS))
    if RAW_CONFLICTS:
        print("CONFLICT_SAMPLE", tuple(RAW_CONFLICTS.items())[:20])
    failures = []
    sizes = set()
    for rotation_index, rotation in enumerate(c53.ROTATIONS):
        for left, right in commuting:
            ok, detail = run(left, right, rotation)
            if not ok:
                failures.append((rotation_index, left, right, detail))
            else:
                sizes.add(detail)
    print("INSTANCES", 24 * len(commuting), sorted(sizes), len(failures))
    if failures:
        print("FAILURE_SAMPLE", failures[:20])
    result = not RAW_CONFLICTS and not failures
    print("RESULT", "PHYSICAL_COMMUTING_ROW_MULTIPLICATION" if result else "OPEN")
    return 0 if result else 1


if __name__ == "__main__":
    raise SystemExit(main())
