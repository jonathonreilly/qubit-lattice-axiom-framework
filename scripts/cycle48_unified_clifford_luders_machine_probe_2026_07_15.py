#!/usr/bin/env python3
"""Mix Clifford and conditional Pauli/Lueders events on one record tape."""

from __future__ import annotations

from itertools import product

import cycle48_pauli_luders_update_compilation_probe_2026_07_15 as measure


t = measure.clifford
d = measure.d
c53 = measure.c53
Coord = tuple[int, int, int]
Event = tuple[str, int, int]
MERGED_RAW = measure.MERGED_RAW

CLIFFORD_EVENTS: tuple[Event, ...] = tuple(("C", gate_id, 0) for gate_id in range(8))
MEASUREMENT_EVENTS: tuple[Event, ...] = tuple(
    ("M", measurement_id, outcome_bit)
    for measurement_id in range(15)
    for outcome_bit in (0, 1)
)
EVENTS = CLIFFORD_EVENTS + MEASUREMENT_EVENTS


def state_site(step: int) -> Coord:
    return (0, 0, -step)


def event_sides(step: int, event: Event) -> dict[Coord, str]:
    kind, index, outcome = event
    if kind == "C":
        bits = t.gate_word(index)
        return {
            (1, 0, -step): d.CAGE_ROLE,
            (-1, 0, -step): d.bit_role(bits[0]),
            (0, 1, -step): d.bit_role(bits[1]),
            (0, -1, -step): d.bit_role(bits[2]),
        }
    return {
        (1, 0, -step): d.CAGE_ROLE,
        (-1, 0, -step): measure.MEASUREMENT_ROLE[index],
        (0, 1, -step): d.bit_role(outcome),
        (0, -1, -step): d.CAGE_ROLE,
    }


def event_output(state_id: int, event: Event):
    kind, index, outcome = event
    if kind == "C":
        output = t.transition_output(state_id, index)
        return output, t.ROLE_STATE.get(output)
    output = measure.update_output(state_id, index, outcome)
    probability, target = measure.BRANCH[(state_id, index, outcome)]
    return output, (target if probability else None)


def apparatus(state_id: int, events: tuple[Event, ...]):
    states = tuple(state_site(step) for step in range(len(events) + 1))
    sides: dict[Coord, str] = {}
    for step, event in enumerate(events, 1):
        sides.update(event_sides(step, event))
    next_port = state_site(len(events) + 1)
    sides[(1, 0, -(len(events) + 1))] = d.CAGE_ROLE
    sides[(0, -1, -(len(events) + 1))] = d.CAGE_ROLE
    core = set(states) | set(sides) | {next_port}
    cage = {
        c53.add(site, direction)
        for site in core
        for direction in c53.DIRECTIONS
        if c53.add(site, direction) not in core
    }
    source = {
        site: d.CAGE_ROLE
        for site in cage
        if site not in states[1:] and site != next_port
    }
    source.update(sides)
    source[states[0]] = t.STATE_ROLE[state_id]
    expected = {}
    current = state_id
    for step, event in enumerate(events, 1):
        output, target = event_output(current, event)
        expected[state_site(step)] = output
        if target is None:
            break
        current = target
    return source, expected


def enabled(records):
    return {
        target: MERGED_RAW[local]
        for target in c53.open_candidates(records)
        if (local := c53.local_signature(records, target)) in MERGED_RAW
    }


def run(state_id: int, events: tuple[Event, ...]):
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
    print("EVENTS", len(CLIFFORD_EVENTS), len(MEASUREMENT_EVENTS), len(EVENTS))
    print("RAW", len(MERGED_RAW), len(measure.RAW_CONFLICTS))
    failures = []
    states = edges = 0
    sizes = set()
    for state_id in range(60):
        for pair in product(EVENTS, repeat=2):
            ok, detail = run(state_id, pair)
            if not ok:
                failures.append((state_id, pair, detail))
            else:
                local_states, local_edges, size = detail
                states += local_states
                edges += local_edges
                sizes.add(size)
    print("PAIR", 60 * 38 * 38, states, edges, sorted(sizes), len(failures))
    if failures:
        print("FAILURE_SAMPLE", failures[:20])
    result = len(EVENTS) == 38 and not measure.RAW_CONFLICTS and not failures
    print("RESULT", "UNIFIED_CONDITIONAL_STABILIZER_EVENT_TAPE" if result else "OPEN")
    return 0 if result else 1


if __name__ == "__main__":
    raise SystemExit(main())
