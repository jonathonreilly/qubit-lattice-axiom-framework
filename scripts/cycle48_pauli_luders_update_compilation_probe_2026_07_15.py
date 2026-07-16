#!/usr/bin/env python3
"""Compile Cycle-48 conditional Pauli/Lueders updates into local records."""

from __future__ import annotations

from fractions import Fraction
from itertools import product

import cycle48_clifford_transition_compilation_probe_2026_07_15 as clifford
import cycle48_decoder_clifford_bind_probe_2026_07_15 as bind


d = clifford.decoder
c48 = clifford.c48
c53 = d.c53
cell = d.cell
Coord = tuple[int, int, int]
Signature = c53.Signature
FRAME_ROLE = d.CAGE_ROLE
REJECT_ROLE = clifford.REJECT_ROLE

MEASUREMENT_ROLE_POOL = tuple(sorted(
    d.RESERVED_ROLES
    - {d.H0, d.H1, d.START_ROLE, d.TAG_ROLE, d.BACKSTOP_ROLE}
))
MEASUREMENT_ROLE = {
    measurement_id: role
    for measurement_id, role in enumerate(MEASUREMENT_ROLE_POOL[:15])
}
ROLE_MEASUREMENT = {role: index for index, role in MEASUREMENT_ROLE.items()}


def branch_table():
    table = {}
    for state_id, rho in enumerate(clifford.STATES):
        for measurement_id, (_name, pauli) in enumerate(c48.NONTRIVIAL_PAULI_2):
            for outcome_bit, outcome in ((0, -1), (1, 1)):
                effect = (c48.I4 + outcome * pauli) / 2.0
                probability = c48.probability_fraction(float(c48.np.trace(effect @ rho).real))
                assert probability in {Fraction(0), Fraction(1, 2), Fraction(1)}
                target = None
                if probability:
                    post = effect @ rho @ effect / float(probability)
                    target = c48.state_index(clifford.STATES, post)
                    assert target is not None
                table[(state_id, measurement_id, outcome_bit)] = (probability, target)
    return table


BRANCH = branch_table()


def update_local(state_id: int, measurement_id: int, outcome_bit: int) -> Signature:
    records = {
        (0, 0, 1): clifford.STATE_ROLE[state_id],
        (1, 0, 0): FRAME_ROLE,
        (-1, 0, 0): MEASUREMENT_ROLE[measurement_id],
        (0, 1, 0): d.bit_role(outcome_bit),
        (0, -1, 0): FRAME_ROLE,
    }
    return c53.canonical_signature(c53.local_signature(records, (0, 0, 0)))


def update_output(state_id: int, measurement_id: int, outcome_bit: int) -> str:
    _probability, target = BRANCH[(state_id, measurement_id, outcome_bit)]
    return REJECT_ROLE if target is None else clifford.STATE_ROLE[target]


def build_table():
    table: dict[Signature, str] = {}
    for state_id in range(60):
        for measurement_id in range(15):
            for outcome_bit in (0, 1):
                local = update_local(state_id, measurement_id, outcome_bit)
                output = update_output(state_id, measurement_id, outcome_bit)
                prior = table.get(local)
                if prior is not None and prior != output:
                    raise ValueError((state_id, measurement_id, outcome_bit, prior, output))
                table[local] = output
    return table


CANONICAL_TABLE = build_table()
UPDATE_RAW = cell.merge_raw(*(
    cell.raw_orbit(local, output)
    for local, output in CANONICAL_TABLE.items()
))
MERGED_RAW = cell.merge_raw(bind.MERGED_RAW, UPDATE_RAW)
RAW_CONFLICTS = {
    local: values for local, values in MERGED_RAW.items() if len(values) != 1
}


def state_site(step: int) -> Coord:
    return (0, 0, -step)


def side_records(step: int, measurement_id: int, outcome_bit: int):
    return {
        (1, 0, -step): FRAME_ROLE,
        (-1, 0, -step): MEASUREMENT_ROLE[measurement_id],
        (0, 1, -step): d.bit_role(outcome_bit),
        (0, -1, -step): FRAME_ROLE,
    }


def apparatus(state_id: int, events: tuple[tuple[int, int], ...]):
    states = tuple(state_site(step) for step in range(len(events) + 1))
    sides: dict[Coord, str] = {}
    for step, (measurement_id, outcome_bit) in enumerate(events, 1):
        sides.update(side_records(step, measurement_id, outcome_bit))
    next_port = state_site(len(events) + 1)
    sides[(1, 0, -(len(events) + 1))] = FRAME_ROLE
    sides[(0, -1, -(len(events) + 1))] = FRAME_ROLE
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
    source[states[0]] = clifford.STATE_ROLE[state_id]
    expected = {}
    current = state_id
    for step, (measurement_id, outcome_bit) in enumerate(events, 1):
        output = update_output(current, measurement_id, outcome_bit)
        expected[state_site(step)] = output
        probability, target = BRANCH[(current, measurement_id, outcome_bit)]
        if probability == 0:
            break
        assert target is not None
        current = target
    return source, expected


def enabled(records):
    return {
        target: MERGED_RAW[local]
        for target in c53.open_candidates(records)
        if (local := c53.local_signature(records, target)) in MERGED_RAW
    }


def run(state_id: int, events: tuple[tuple[int, int], ...]):
    source, expected = apparatus(state_id, events)
    records = dict(source)
    for step, (target, output) in enumerate(expected.items()):
        actual = enabled(records)
        wanted = {target: frozenset((output,))}
        if actual != wanted:
            return False, ("front", step, actual, wanted, len(source))
        records[target] = output
    actual = enabled(records)
    if actual:
        return False, ("terminal", actual, len(source))
    return True, (len(expected) + 1, len(expected), len(source))


def main() -> int:
    probabilities = {value[0] for value in BRANCH.values()}
    counts = {probability: sum(value[0] == probability for value in BRANCH.values()) for probability in probabilities}
    print("BRANCH", len(BRANCH), counts)
    print("ROLES", MEASUREMENT_ROLE)
    print("TABLE", len(CANONICAL_TABLE), len(UPDATE_RAW), len(MERGED_RAW), len(RAW_CONFLICTS))
    if RAW_CONFLICTS:
        print("RAW_CONFLICT_SAMPLE", tuple(RAW_CONFLICTS.items())[:20])
    failures = []
    states = edges = 0
    sizes = set()
    events = tuple(product(range(15), (0, 1)))
    for state_id in range(60):
        for pair in product(events, repeat=2):
            ok, detail = run(state_id, pair)
            if not ok:
                failures.append((state_id, pair, detail))
            else:
                local_states, local_edges, source_size = detail
                states += local_states
                edges += local_edges
                sizes.add(source_size)
    print("PAIR", 60 * 30 * 30, states, edges, sorted(sizes), len(failures))
    if failures:
        print("FAILURE_SAMPLE", failures[:20])
    result = (
        len(BRANCH) == 1_800
        and counts == {Fraction(0): 180, Fraction(1, 2): 1_440, Fraction(1): 180}
        and len(CANONICAL_TABLE) == 1_800
        and len(UPDATE_RAW) == 43_200
        and not RAW_CONFLICTS
        and not failures
    )
    print("RESULT", "CONDITIONAL_PAULI_LUDERS_UPDATE_GRAMMAR" if result else "OPEN")
    return 0 if result else 1


if __name__ == "__main__":
    raise SystemExit(main())
