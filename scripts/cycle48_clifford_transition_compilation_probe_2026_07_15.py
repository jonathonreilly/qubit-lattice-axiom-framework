#!/usr/bin/env python3
"""Probe a recurrent local compiler for Cycle-48 Clifford transitions."""

from __future__ import annotations

from itertools import product

import cycle48_six_bit_local_decoder_compilation_probe_2026_07_15 as decoder
import record_derived_coherent_carrier_decoder_cycle48_2026_07_14 as c48


c53 = decoder.c53
cell = decoder.cell
Coord = tuple[int, int, int]
Signature = c53.Signature
GateWord = tuple[int, int, int]
FRAME_ROLE = decoder.CAGE_ROLE
REJECT_ROLE = decoder.PREFIX_ROLE[(1, 1, 1, 1, 0, 0)]
STATE_ROLE = {
    state_id: decoder.PREFIX_ROLE[tuple((state_id >> shift) & 1 for shift in range(5, -1, -1))]
    for state_id in range(60)
}
ROLE_STATE = {role: state_id for state_id, role in STATE_ROLE.items()}


def gate_word(gate_id: int) -> GateWord:
    return tuple((gate_id >> shift) & 1 for shift in range(2, -1, -1))  # type: ignore[return-value]


STATES, _LABELS = c48.stabilizer_states()
GATE_IMAGE = {
    (state_id, gate_id): c48.state_index(
        STATES, gate @ state @ gate.conj().T
    )
    for state_id, state in enumerate(STATES)
    for gate_id, (_name, gate) in enumerate(c48.CLIFFORD_GATES)
}


def transition_local(state_id: int, gate_id: int) -> Signature:
    bits = gate_word(gate_id)
    records = {
        (0, 0, 1): STATE_ROLE[state_id],
        (1, 0, 0): FRAME_ROLE,
        (-1, 0, 0): decoder.bit_role(bits[0]),
        (0, 1, 0): decoder.bit_role(bits[1]),
        (0, -1, 0): decoder.bit_role(bits[2]),
    }
    return c53.canonical_signature(c53.local_signature(records, (0, 0, 0)))


def transition_output(state_id: int, gate_id: int) -> str:
    if gate_id == 7:
        return REJECT_ROLE
    result = GATE_IMAGE[(state_id, gate_id)]
    assert result is not None
    return STATE_ROLE[result]


def build_table() -> dict[Signature, str]:
    table: dict[Signature, str] = {}
    for state_id in range(60):
        for gate_id in range(8):
            local = transition_local(state_id, gate_id)
            output = transition_output(state_id, gate_id)
            prior = table.get(local)
            if prior is not None and prior != output:
                raise ValueError((state_id, gate_id, prior, output, local))
            table[local] = output
    return table


CANONICAL_TABLE = build_table()
TRANSITION_RAW = cell.merge_raw(*(
    cell.raw_orbit(local, output)
    for local, output in CANONICAL_TABLE.items()
))
MERGED_RAW = cell.merge_raw(decoder.MERGED_RAW, TRANSITION_RAW)
RAW_CONFLICTS = {
    local: outputs for local, outputs in MERGED_RAW.items() if len(outputs) != 1
}


def state_site(step: int) -> Coord:
    return (0, 0, -step)


def frame_site(step: int) -> Coord:
    return (1, 0, -step)


def gate_sites(step: int) -> tuple[Coord, Coord, Coord]:
    return ((-1, 0, -step), (0, 1, -step), (0, -1, -step))


def apparatus(state_id: int, gates: tuple[int, ...]):
    states = tuple(state_site(step) for step in range(len(gates) + 1))
    side_records: dict[Coord, str] = {}
    for step, gate_id in enumerate(gates, 1):
        side_records[frame_site(step)] = FRAME_ROLE
        side_records.update({
            site: decoder.bit_role(bit)
            for site, bit in zip(gate_sites(step), gate_word(gate_id))
        })
    # One frame record at the next open port suppresses all unary continuations
    # from the terminal state without supplying another operation.
    next_port = state_site(len(gates) + 1)
    side_records[frame_site(len(gates) + 1)] = FRAME_ROLE
    core = set(states) | set(side_records) | {next_port}
    cage_sites = {
        c53.add(site, direction)
        for site in core
        for direction in c53.DIRECTIONS
        if c53.add(site, direction) not in core
    }
    # Keep the state path and next port open; side records override cage cells.
    source = {
        site: FRAME_ROLE
        for site in cage_sites
        if site not in states[1:] and site != next_port
    }
    source.update(side_records)
    source[states[0]] = STATE_ROLE[state_id]
    expected: dict[Coord, str] = {}
    current = state_id
    for step, gate_id in enumerate(gates, 1):
        output = transition_output(current, gate_id)
        expected[state_site(step)] = output
        if gate_id == 7:
            break
        current = ROLE_STATE[output]
    return source, expected, next_port


def enabled(records):
    return {
        target: MERGED_RAW[local]
        for target in c53.open_candidates(records)
        if (local := c53.local_signature(records, target)) in MERGED_RAW
    }


def run(state_id: int, gates: tuple[int, ...]):
    source, expected, next_port = apparatus(state_id, gates)
    records = dict(source)
    for step, (target, output) in enumerate(expected.items()):
        actual = enabled(records)
        wanted = {target: frozenset((output,))}
        if actual != wanted:
            return False, ("front", step, actual, wanted, len(source))
        records[target] = output
    actual = enabled(records)
    if actual:
        return False, ("terminal", actual, next_port, len(source))
    return True, (len(expected) + 1, len(expected), len(source))


def main() -> int:
    print("TABLE", len(CANONICAL_TABLE), len(TRANSITION_RAW), len(MERGED_RAW), len(RAW_CONFLICTS))
    if RAW_CONFLICTS:
        print("RAW_CONFLICT_SAMPLE", tuple(RAW_CONFLICTS.items())[:12])
    failures = []
    states = edges = 0
    source_sizes = set()
    for state_id in range(60):
        for gates in product(range(8), repeat=2):
            ok, detail = run(state_id, gates)
            if not ok:
                failures.append((state_id, gates, detail))
            else:
                local_states, local_edges, source_size = detail
                states += local_states
                edges += local_edges
                source_sizes.add(source_size)
    print("PAIR_CENSUS", 60 * 64, states, edges, sorted(source_sizes), len(failures))
    if failures:
        print("FAILURE_SAMPLE", failures[:20])
    result = (
        len(CANONICAL_TABLE) == 480
        and len(TRANSITION_RAW) == 11_520
        and not RAW_CONFLICTS
        and not failures
    )
    print("RESULT", "LOCAL_CLIFFORD_TRANSITION_GRAMMAR" if result else "OPEN")
    return 0 if result else 1


if __name__ == "__main__":
    raise SystemExit(main())
