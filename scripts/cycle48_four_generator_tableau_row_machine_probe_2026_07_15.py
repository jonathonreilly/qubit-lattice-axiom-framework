#!/usr/bin/env python3
"""Reduce the physical tableau row machine to four declared generators."""

from __future__ import annotations

from collections import deque
from itertools import combinations, product

import cycle48_physical_tableau_row_gate_probe_2026_07_15 as five


algebra = five.algebra
unified = five.unified
cell = five.cell
KEEP = (0, 1, 2, 4)  # H0,H1,S0,CX01
S1_WORD = (4, 0, 1, 4, 0, 2, 0, 4, 0, 1, 4)
CX10_WORD = (0, 1, 4, 0, 1)
SWAP_WORD = (4, *CX10_WORD, 4)
DECLARED_WORD = {
    0: (0,),
    1: (1,),
    2: (2,),
    3: S1_WORD,
    4: (4,),
    5: CX10_WORD,
    6: SWAP_WORD,
}


CANONICAL_TABLE = {
    five.row_local(record, gate_id): five.ROW_ROLE[algebra.apply_gate(record, gate_id)]
    for record in five.ROWS
    for gate_id in KEEP
}
ROW_GATE_RAW = cell.merge_raw(*(
    cell.raw_orbit(local, output)
    for local, output in CANONICAL_TABLE.items()
))
MERGED_RAW = cell.merge_raw(unified.MERGED_RAW, ROW_GATE_RAW)
RAW_CONFLICTS = {
    local: values for local, values in MERGED_RAW.items() if len(values) != 1
}


def enabled(records):
    return {
        target: MERGED_RAW[local]
        for target in five.c53.open_candidates(records)
        if (local := five.c53.local_signature(records, target)) in MERGED_RAW
    }


def run(record: algebra.Row, gates: tuple[int, ...]):
    source, expected = five.apparatus(record, gates)
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


GATE_NAMES = ("H0", "H1", "S0", "S1", "CX01")
GATE_PERMUTATIONS = tuple(
    tuple(algebra.tableau_gate_image(algebra.STATE_GENERATORS[state_id], gate_id) for state_id in range(60))
    for gate_id in range(5)
)
IDENTITY = tuple(range(60))


def compose(left, right):
    return tuple(left[right[index]] for index in range(60))


def closure(gates: tuple[int, ...]):
    generators = tuple(GATE_PERMUTATIONS[index] for index in gates)
    seen = {IDENTITY}
    queue = deque((IDENTITY,))
    while queue:
        current = queue.popleft()
        for generator in generators:
            future = compose(generator, current)
            if future not in seen:
                seen.add(future)
                queue.append(future)
    return frozenset(seen)


def main() -> int:
    print("TABLE", len(CANONICAL_TABLE), len(ROW_GATE_RAW), len(MERGED_RAW), len(RAW_CONFLICTS))
    failures = []
    states = edges = 0
    sizes = set()
    for record in five.ROWS:
        for gate_id in range(7):
            gates = DECLARED_WORD[gate_id]
            ok, detail = run(record, gates)
            expected = algebra.apply_gate(record, gate_id)
            observed = algebra.apply_sequence(record, gates)
            if not ok or observed != expected:
                failures.append((record, gate_id, detail, observed, expected))
            else:
                local_states, local_edges, size = detail
                states += local_states
                edges += local_edges
                sizes.add(size)
    print("DECLARED", 32 * 7, states, edges, sorted(sizes), len(failures))
    if failures:
        print("FAILURE_SAMPLE", failures[:20])

    subset_sizes = {}
    for size in range(1, 6):
        for subset in combinations(range(5), size):
            subset_sizes[subset] = len(closure(subset))
    full = subset_sizes[(0, 1, 2, 3, 4)]
    minimal = tuple(
        subset for subset, group_size in subset_sizes.items()
        if group_size == full
        and not any(
            subset_sizes[proper] == full
            for length in range(1, len(subset))
            for proper in combinations(subset, length)
        )
    )
    print("GROUP", full, minimal, {tuple(GATE_NAMES[i] for i in subset): subset_sizes[subset] for subset in minimal})
    result = (
        len(CANONICAL_TABLE) == 128
        and len(ROW_GATE_RAW) == 3_072
        and not RAW_CONFLICTS
        and not failures
        and full == 11_520
        and minimal == ((0, 1, 2, 4), (0, 1, 3, 4), (0, 2, 3, 4))
    )
    print("RESULT", "FOUR_GENERATOR_PHYSICAL_TABLEAU_ROW_MACHINE" if result else "OPEN")
    return 0 if result else 1


if __name__ == "__main__":
    raise SystemExit(main())
