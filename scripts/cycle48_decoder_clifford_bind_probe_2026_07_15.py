#!/usr/bin/env python3
"""Bind the local Cycle-48 preparation decoder to one Clifford transition."""

from __future__ import annotations

import cycle48_clifford_transition_compilation_probe_2026_07_15 as transition


d = transition.decoder
c53 = d.c53
cell = d.cell
Coord = tuple[int, int, int]
Signature = c53.Signature

# The old decoder's east cage record becomes the live state-output port.
CURRENT = d.CHAIN[-1]
PORT = (6, 1, 0)
NEXT_PORT = (7, 1, 0)
FRAME = (6, 0, 0)
GATE_SITES = ((6, 2, 0), (6, 1, 1), (6, 1, -1))
NEXT_FRAME = (7, 0, 0)
SHIFT = d.SHIFT


def port_source(word: d.Word, gate_id: int) -> dict[Coord, str]:
    records = d.local_source(word)
    assert records.pop(PORT) == d.CAGE_ROLE
    records[FRAME] = d.CAGE_ROLE
    records.update({
        site: d.bit_role(bit)
        for site, bit in zip(GATE_SITES, transition.gate_word(gate_id))
    })
    records[NEXT_FRAME] = d.CAGE_ROLE

    core = set(records) | set(d.CHAIN) | {PORT, NEXT_PORT}
    transition_core = {CURRENT, PORT, NEXT_PORT, FRAME, NEXT_FRAME, *GATE_SITES}
    shell = {
        c53.add(site, direction)
        for site in transition_core
        for direction in c53.DIRECTIONS
        if c53.add(site, direction) not in core
    }
    records.update({site: d.CAGE_ROLE for site in shell})
    return records


def decoder_outputs(word: d.Word):
    return d.local_outputs(word)


def build_decoder_table() -> dict[Signature, str]:
    table: dict[Signature, str] = {}
    for prefix in d.PREFIXES:
        index = len(prefix) - 1
        word: d.Word = tuple(prefix + (0,) * (6 - len(prefix)))  # type: ignore[assignment]
        records = port_source(word, 0)
        records.update({
            d.CHAIN[prior]: d.PREFIX_ROLE[prefix[: prior + 1]]
            for prior in range(index)
        })
        locals_seen = set()
        for gate_id in range(8):
            gate_records = port_source(word, gate_id)
            gate_records.update({
                d.CHAIN[prior]: d.PREFIX_ROLE[prefix[: prior + 1]]
                for prior in range(index)
            })
            locals_seen.add(c53.canonical_signature(
                c53.local_signature(gate_records, d.CHAIN[index])
            ))
        if len(locals_seen) != 1:
            raise ValueError((prefix, locals_seen))
        local = next(iter(locals_seen))
        output = d.PREFIX_ROLE[prefix]
        prior = table.get(local)
        if prior is not None and prior != output:
            raise ValueError((prefix, local, prior, output))
        table[local] = output
    return table


DECODER_TABLE = build_decoder_table()
DECODER_RAW = cell.merge_raw(*(
    cell.raw_orbit(local, output)
    for local, output in DECODER_TABLE.items()
))
MERGED_RAW = cell.merge_raw(
    d.bound.FINAL_RAW,
    DECODER_RAW,
    transition.TRANSITION_RAW,
)
RAW_CONFLICTS = {
    local: values for local, values in MERGED_RAW.items() if len(values) != 1
}


def transform(records, rotation):
    return c53.transform_records(records, rotation, SHIFT)


def enabled(records):
    return {
        target: MERGED_RAW[local]
        for target in c53.open_candidates(records)
        if (local := c53.local_signature(records, target)) in MERGED_RAW
    }


def run(prep_id: int, gate_id: int, rotation):
    word: d.Word = tuple((prep_id >> shift) & 1 for shift in range(5, -1, -1))  # type: ignore[assignment]
    local_source = port_source(word, gate_id)
    # The apparatus is strictly separated from the Cycle-144 terminal.  Its
    # local graph is therefore computed independently; main() checks the
    # terminal frontier once under this same merged table and the exact product
    # follows from radius one.
    source = transform(local_source, rotation)
    local_expected = decoder_outputs(word)
    if prep_id < 60:
        local_expected[PORT] = transition.transition_output(prep_id, gate_id)
    expected = transform(local_expected, rotation)
    records = dict(source)
    order = (*d.CHAIN, *((PORT,) if prep_id < 60 else ()))
    for step, local_target in enumerate(order):
        target = next(iter(transform({local_target: "x"}, rotation)))
        actual = enabled(records)
        wanted = {target: frozenset((expected[target],))}
        if actual != wanted:
            return False, ("front", step, actual, wanted, len(local_source))
        records[target] = expected[target]
    actual = enabled(records)
    if actual:
        return False, ("terminal", actual, len(local_source))
    return True, (len(order) + 1, len(order), len(local_source))


def main() -> int:
    print(
        "TABLE",
        len(DECODER_TABLE), len(DECODER_RAW),
        len(transition.CANONICAL_TABLE), len(transition.TRANSITION_RAW),
        len(MERGED_RAW), len(RAW_CONFLICTS),
    )
    if RAW_CONFLICTS:
        print("RAW_CONFLICT_SAMPLE", tuple(RAW_CONFLICTS.items())[:12])
    bound_front = enabled(d.BOUND_TERMINAL)
    print("BOUND_FRONT", bound_front)
    failures = []
    states = edges = 0
    source_sizes = set()
    for rotation_index, rotation in enumerate(c53.ROTATIONS):
        for prep_id in range(64):
            for gate_id in range(8):
                ok, detail = run(prep_id, gate_id, rotation)
                if not ok:
                    failures.append((rotation_index, prep_id, gate_id, detail))
                else:
                    local_states, local_edges, source_size = detail
                    states += local_states
                    edges += local_edges
                    source_sizes.add(source_size)
    print("INSTANCE", 24 * 64 * 8, states, edges, sorted(source_sizes), len(failures))
    if failures:
        print("FAILURE_SAMPLE", failures[:20])
    result = (
        len(DECODER_TABLE) == 126
        and len(transition.CANONICAL_TABLE) == 480
        and not RAW_CONFLICTS
        and bound_front == d.BOUND_IGNORED
        and not failures
    )
    print("RESULT", "DECODER_TO_CLIFFORD_CAUSAL_BIND" if result else "OPEN")
    return 0 if result else 1


if __name__ == "__main__":
    raise SystemExit(main())
