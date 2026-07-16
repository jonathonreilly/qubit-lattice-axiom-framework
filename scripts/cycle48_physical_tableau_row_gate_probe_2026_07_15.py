#!/usr/bin/env python3
"""Compile compact signed-tableau row gates into a recurrent local tape."""

from __future__ import annotations

from itertools import product

import cycle48_symplectic_tableau_compression_probe_2026_07_15 as algebra
import cycle48_unified_clifford_luders_machine_probe_2026_07_15 as unified


m = unified.measure
d = unified.d
c53 = d.c53
cell = d.cell
Coord = tuple[int, int, int]
Signature = c53.Signature

ROWS = tuple(product((0, 1), repeat=5))
ROW_ROLE = {record: role for record, role in zip(ROWS, d.PREFIX_ROLES[:32])}
ROLE_ROW = {role: record for record, role in ROW_ROLE.items()}

PRIMITIVES = (0, 1, 2, 3, 4)  # H0,H1,S0,S1,CX01
GATE_ROLES = ("R_A22", "R_B01", "R_B21", "R_C22", "R_C23")
GATE_ROLE = dict(zip(PRIMITIVES, GATE_ROLES))
ROLE_GATE = {role: gate for gate, role in GATE_ROLE.items()}
FRAME_ROLE = d.CAGE_ROLE


def row_local(record: algebra.Row, gate_id: int) -> Signature:
    records = {
        (0, 0, 1): ROW_ROLE[record],
        (1, 0, 0): FRAME_ROLE,
        (-1, 0, 0): GATE_ROLE[gate_id],
        (0, 1, 0): FRAME_ROLE,
        (0, -1, 0): FRAME_ROLE,
    }
    return c53.canonical_signature(c53.local_signature(records, (0, 0, 0)))


def build_table():
    table: dict[Signature, str] = {}
    for record in ROWS:
        for gate_id in PRIMITIVES:
            local = row_local(record, gate_id)
            output = ROW_ROLE[algebra.apply_gate(record, gate_id)]
            prior = table.get(local)
            if prior is not None and prior != output:
                raise ValueError((record, gate_id, prior, output))
            table[local] = output
    return table


CANONICAL_TABLE = build_table()
ROW_GATE_RAW = cell.merge_raw(*(
    cell.raw_orbit(local, output)
    for local, output in CANONICAL_TABLE.items()
))
MERGED_RAW = cell.merge_raw(unified.MERGED_RAW, ROW_GATE_RAW)
RAW_CONFLICTS = {
    local: values for local, values in MERGED_RAW.items() if len(values) != 1
}


def state_site(step: int) -> Coord:
    return (0, 0, -step)


def apparatus(record: algebra.Row, gates: tuple[int, ...]):
    states = tuple(state_site(step) for step in range(len(gates) + 1))
    sides = {}
    for step, gate_id in enumerate(gates, 1):
        sides.update({
            (1, 0, -step): FRAME_ROLE,
            (-1, 0, -step): GATE_ROLE[gate_id],
            (0, 1, -step): FRAME_ROLE,
            (0, -1, -step): FRAME_ROLE,
        })
    next_port = state_site(len(gates) + 1)
    sides.update({
        (1, 0, -(len(gates) + 1)): FRAME_ROLE,
        (0, 1, -(len(gates) + 1)): FRAME_ROLE,
        (0, -1, -(len(gates) + 1)): FRAME_ROLE,
    })
    core = set(states) | set(sides) | {next_port}
    cage = {
        c53.add(site, direction)
        for site in core
        for direction in c53.DIRECTIONS
        if c53.add(site, direction) not in core
    }
    source = {
        site: FRAME_ROLE
        for site in cage
        if site not in states[1:] and site != next_port
    }
    source.update(sides)
    source[states[0]] = ROW_ROLE[record]
    expected = {}
    current = record
    for step, gate_id in enumerate(gates, 1):
        current = algebra.apply_gate(current, gate_id)
        expected[state_site(step)] = ROW_ROLE[current]
    return source, expected


def enabled(records):
    return {
        target: MERGED_RAW[local]
        for target in c53.open_candidates(records)
        if (local := c53.local_signature(records, target)) in MERGED_RAW
    }


def run(record: algebra.Row, gates: tuple[int, ...]):
    source, expected = apparatus(record, gates)
    records = dict(source)
    for step, (target, output) in enumerate(expected.items()):
        actual = enabled(records)
        wanted = {target: frozenset((output,))}
        if actual != wanted:
            return False, ("front", step, actual, wanted, len(source))
        records[target] = output
    if (actual := enabled(records)):
        return False, ("terminal", actual, len(source))
    return True, (len(expected) + 1, len(expected), len(source))


def main() -> int:
    print("ROLES", len(ROW_ROLE), GATE_ROLE)
    print("TABLE", len(CANONICAL_TABLE), len(ROW_GATE_RAW), len(MERGED_RAW), len(RAW_CONFLICTS))
    if RAW_CONFLICTS:
        print("CONFLICT_SAMPLE", tuple(RAW_CONFLICTS.items())[:20])
    failures = []
    states = edges = 0
    sizes = set()
    for record in ROWS:
        for gates in product(PRIMITIVES, repeat=2):
            ok, detail = run(record, gates)
            if not ok:
                failures.append((record, gates, detail))
            else:
                local_states, local_edges, size = detail
                states += local_states
                edges += local_edges
                sizes.add(size)
    print("TAPES", 32 * 25, states, edges, sorted(sizes), len(failures))
    if failures:
        print("FAILURE_SAMPLE", failures[:20])

    basis_failures = []
    for state_id in range(60):
        for basis in algebra.all_bases(state_id):
            for gate_id in PRIMITIVES:
                observed = algebra.KEY_STATE[algebra.group_key(*(
                    ROLE_ROW[ROW_ROLE[algebra.apply_gate(record, gate_id)]]
                    for record in basis
                ))]
                expected = algebra.clifford.GATE_IMAGE[(state_id, gate_id)]
                if observed != expected:
                    basis_failures.append((state_id, basis, gate_id, observed, expected))
    print("STATE_BASES", 60 * 6 * 5, len(basis_failures))
    result = (
        len(CANONICAL_TABLE) == 160
        and len(ROW_GATE_RAW) == 3_840
        and not RAW_CONFLICTS
        and not failures
        and not basis_failures
    )
    print("RESULT", "PHYSICAL_TABLEAU_ROW_GATE" if result else "OPEN")
    return 0 if result else 1


if __name__ == "__main__":
    raise SystemExit(main())
