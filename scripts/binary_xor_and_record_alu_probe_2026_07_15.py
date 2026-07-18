#!/usr/bin/env python3
"""A recurrent literal H0/H1 XOR/AND ALU under the Cycle-149 law."""

from __future__ import annotations

from itertools import product

import cycle48_four_generator_tableau_row_machine_probe_2026_07_15 as compact


d = compact.five.d
c53 = d.c53
cell = d.cell
Coord = tuple[int, int, int]
Signature = c53.Signature
XOR_ROLE = "R_LB"
AND_ROLE = "W3"
OP_ROLE = (XOR_ROLE, AND_ROLE)
FRAME_ROLE = d.CAGE_ROLE


def bit(value: int) -> str:
    return d.H1 if value else d.H0


def output(left: int, right: int, operation: int) -> int:
    return (left ^ right) if operation == 0 else (left & right)


def alu_local(left: int, right: int, operation: int) -> Signature:
    records = {
        (0, 0, 1): bit(left),
        (-1, 0, 0): bit(right),
        (1, 0, 0): OP_ROLE[operation],
        (0, 1, 0): FRAME_ROLE,
        (0, -1, 0): FRAME_ROLE,
    }
    return c53.canonical_signature(c53.local_signature(records, (0, 0, 0)))


CANONICAL_TABLE = {
    alu_local(left, right, operation): bit(output(left, right, operation))
    for left, right, operation in product((0, 1), repeat=3)
}
ALU_RAW = cell.merge_raw(*(
    cell.raw_orbit(local, result)
    for local, result in CANONICAL_TABLE.items()
))
MERGED_RAW = cell.merge_raw(compact.MERGED_RAW, ALU_RAW)
RAW_CONFLICTS = {
    local: values for local, values in MERGED_RAW.items() if len(values) != 1
}


def value_site(step: int) -> Coord:
    return (0, 0, -step)


def apparatus(initial: int, program: tuple[tuple[int, int], ...]):
    values = tuple(value_site(step) for step in range(len(program) + 1))
    sides = {}
    for step, (operation, operand) in enumerate(program, 1):
        sides.update({
            (-1, 0, -step): bit(operand),
            (1, 0, -step): OP_ROLE[operation],
            (0, 1, -step): FRAME_ROLE,
            (0, -1, -step): FRAME_ROLE,
        })
    next_port = value_site(len(program) + 1)
    sides.update({
        (1, 0, -(len(program) + 1)): FRAME_ROLE,
        (0, 1, -(len(program) + 1)): FRAME_ROLE,
        (0, -1, -(len(program) + 1)): FRAME_ROLE,
    })
    core = set(values) | set(sides) | {next_port}
    cage = {
        c53.add(site, direction)
        for site in core
        for direction in c53.DIRECTIONS
        if c53.add(site, direction) not in core
    }
    source = {
        site: FRAME_ROLE
        for site in cage
        if site not in values[1:] and site != next_port
    }
    source.update(sides)
    source[values[0]] = bit(initial)
    expected = {}
    current = initial
    for step, (operation, operand) in enumerate(program, 1):
        current = output(current, operand, operation)
        expected[value_site(step)] = bit(current)
    return source, expected, current


def enabled(records):
    return {
        target: MERGED_RAW[local]
        for target in c53.open_candidates(records)
        if (local := c53.local_signature(records, target)) in MERGED_RAW
    }


def run(initial: int, program: tuple[tuple[int, int], ...], rotation=None):
    source, expected, result = apparatus(initial, program)
    if rotation is not None:
        shift = (61, -67, 71)
        source = c53.transform_records(source, rotation, shift)
        expected = c53.transform_records(expected, rotation, shift)
    records = dict(source)
    for step, (target, value) in enumerate(expected.items()):
        actual = enabled(records)
        wanted = {target: frozenset((value,))}
        if actual != wanted:
            return False, ("front", step, actual, wanted, len(source))
        records[target] = value
    if (actual := enabled(records)):
        return False, ("terminal", actual, len(source))
    return True, (len(expected) + 1, len(expected), len(source), result)


def main() -> int:
    print("TABLE", len(CANONICAL_TABLE), len(ALU_RAW), len(MERGED_RAW), len(RAW_CONFLICTS))
    if RAW_CONFLICTS:
        print("CONFLICT_SAMPLE", tuple(RAW_CONFLICTS.items())[:20])
    failures = []
    states = edges = 0
    sizes = set()
    instructions = tuple(product((0, 1), repeat=2))
    for rotation_index, rotation in enumerate(c53.ROTATIONS):
        for initial in (0, 1):
            for program in product(instructions, repeat=3):
                ok, detail = run(initial, program, rotation)
                if not ok:
                    failures.append((rotation_index, initial, program, detail))
                else:
                    local_states, local_edges, size, _result = detail
                    states += local_states
                    edges += local_edges
                    sizes.add(size)
    print("PROGRAMS", 24 * 2 * 4**3, states, edges, sorted(sizes), len(failures))
    if failures:
        print("FAILURE_SAMPLE", failures[:20])
    result = (
        len(CANONICAL_TABLE) == 8
        and len(ALU_RAW) == 192
        and not RAW_CONFLICTS
        and not failures
    )
    print("RESULT", "BINARY_XOR_AND_RECORD_ALU" if result else "OPEN")
    return 0 if result else 1


if __name__ == "__main__":
    raise SystemExit(main())
