#!/usr/bin/env python3
"""Cycle 797: local center controllability and frozen-pump discriminator.

The probe independently reconstructs radius-one Pauli moves that commute with
the complete logical even-CAR basis and total parity.  It then freezes the
following asynchronous local law: apply a move iff it strictly lowers the
number of violated nonparity center checks in the bounded neighborhood that
the move toggles.  Every application is a stabilizer measurement followed by
a syndrome-controlled Pauli with the syndrome environment retained.

This tests actual syndrome dynamics.  Full span alone is not accepted as a
pump, and the runner makes no claim about inserting raw six-mode coordinates.
Failure of the three frozen policies is route-specific, not a no-go.
"""

from __future__ import annotations

from hashlib import sha256
from itertools import product
import json
import random
from pathlib import Path

import frontier_cycle720_cell_majorana_companion_geometry_2026_07_27 as M
import frontier_cycle720_companion_subsystem_m2_update_2026_07_27 as U
import frontier_cycle720_companion_subsystem_mixed_gauge_factorization_2026_07_27 as F


def rank(rows) -> int:
    pivots = {}
    for original in rows:
        row = int(original)
        while row:
            pivot = row.bit_length() - 1
            if pivot in pivots:
                row ^= pivots[pivot]
            else:
                pivots[pivot] = row
                break
    return len(pivots)


def nullspace(row_masks: tuple[int, ...], variables: int) -> tuple[int, ...]:
    rows = list(row_masks)
    pivots = {}
    cursor = 0
    for column in range(variables):
        pivot = next((r for r in range(cursor, len(rows)) if (rows[r] >> column) & 1), None)
        if pivot is None:
            continue
        rows[cursor], rows[pivot] = rows[pivot], rows[cursor]
        for other in range(len(rows)):
            if other != cursor and ((rows[other] >> column) & 1):
                rows[other] ^= rows[cursor]
        pivots[column] = cursor
        cursor += 1
    output = []
    for free in range(variables):
        if free in pivots:
            continue
        vector = 1 << free
        for column, row_index in pivots.items():
            vector |= (((rows[row_index] & vector).bit_count() & 1) << column)
        output.append(vector)
    return tuple(output)


def distance(fixture, left, right):
    return sum(abs(a - b) for a, b in zip(fixture.cells[left], fixture.cells[right]))


def support_cells(fixture, vector):
    mask = (1 << fixture.qubits) - 1
    occupied = (vector & mask) | (vector >> fixture.qubits)
    return frozenset(
        M.qubit_cell(fixture, qubit)
        for qubit in range(fixture.qubits)
        if (occupied >> qubit) & 1
    )


def cell_diameter(fixture, cells):
    return max((distance(fixture, a, b) for a in cells for b in cells), default=0)


def independent_local_centers(fixture, gauge):
    radicals, _pairs = F.symplectic_split_vectors(gauge, fixture.qubits)
    parity = M.Pauli(z=(1 << fixture.matter_qubits) - 1).symplectic(fixture.qubits)
    pivots = {parity.bit_length() - 1: parity}
    local = []
    for original in F.local_center_basis(fixture, gauge, 2):
        row = original
        while row:
            pivot = row.bit_length() - 1
            if pivot in pivots:
                row ^= pivots[pivot]
            else:
                pivots[pivot] = row
                local.append(original)
                break
        if len(local) == len(radicals) - 1:
            break
    assert len(local) == len(radicals) - 1
    return tuple(local), parity


def physical_nullspace_basis(fixture, logical_rows, allowed_cells):
    q = fixture.qubits
    allowed_qubits = tuple(
        qubit for qubit in range(q)
        if M.qubit_cell(fixture, qubit) in allowed_cells
    )
    positions = allowed_qubits + tuple(q + qubit for qubit in allowed_qubits)
    equation_masks = []
    for logical in logical_rows:
        x, z = logical & ((1 << q) - 1), logical >> q
        equation_masks.append(sum(
            ((((z >> position) & 1) if position < q else ((x >> (position - q)) & 1)) << variable)
            for variable, position in enumerate(positions)
        ))
    output = []
    for solution in nullspace(tuple(equation_masks), len(positions)):
        output.append(sum(
            (((solution >> variable) & 1) << position)
            for variable, position in enumerate(positions)
        ))
    return tuple(output)


def fixture_data(shape):
    fixture = M.CompanionFixture.build(shape)
    operator_rows = M.operator_rows(fixture)
    physical = tuple(row[1].symplectic(fixture.qubits) for row in operator_rows)
    target = tuple(row[2].symplectic(fixture.matter_qubits) for row in operator_rows)
    paired = F.independent_paired_basis(physical, target)
    _radicals, pairs = F.symplectic_split_paired(paired, fixture.qubits)
    logical_rows = tuple(row[0] for pair in pairs for row in pair)
    relation_rows = M.relation_certificate(fixture)["relation_rows"]
    _gauge_report, gauge = U.gauge_structure(
        fixture, tuple(row[1] for row in operator_rows), relation_rows
    )
    centers, parity = independent_local_centers(fixture, gauge)

    # Reconstruct bounded logical-commuting moves.  Pair the odd-parity
    # nullspace generators so every retained move also commutes with parity.
    by_syndrome = {}
    raw_rows = 0
    for anchor in range(len(fixture.cells)):
        allowed = frozenset(
            cell for cell in range(len(fixture.cells))
            if distance(fixture, anchor, cell) <= 1
        )
        basis = physical_nullspace_basis(fixture, logical_rows, allowed)
        even = [row for row in basis if not M.symplectic(row, parity, fixture.qubits)]
        odd = [row for row in basis if M.symplectic(row, parity, fixture.qubits)]
        if odd:
            even.extend(odd[0] ^ row for row in odd[1:])
        for row in even:
            syndrome = sum(
                M.symplectic(row, center, fixture.qubits) << index
                for index, center in enumerate(centers)
            )
            if not syndrome:
                continue
            raw_rows += 1
            cells = support_cells(fixture, row)
            key = (len(cells), cell_diameter(fixture, cells), ((row & ((1 << fixture.qubits) - 1)) | (row >> fixture.qubits)).bit_count(), row)
            if syndrome not in by_syndrome or key < by_syndrome[syndrome][0]:
                by_syndrome[syndrome] = (key, row, anchor, cells)
    moves = tuple(
        (syndrome, data[1], data[2], data[3])
        for syndrome, data in sorted(
            by_syndrome.items(), key=lambda item: (item[0].bit_count(), item[0], item[1][0])
        )
    )
    return fixture, logical_rows, centers, parity, moves, raw_rows


def descend(state, move_masks, potential="hamming"):
    trace = []
    while state:
        changed = False
        for index, move in enumerate(move_masks):
            after = state ^ move
            lower = (
                after.bit_count() < state.bit_count()
                if potential == "hamming"
                else after < state
            )
            if lower:
                trace.append(index)
                state = after
                changed = True
        if not changed:
            break
    return state, tuple(trace)


def triangular_local_priority(move_masks, center_count):
    """Find raw local moves forming a column-permuted triangular reset atlas."""
    compatible_cache = {}
    def compatible(remaining, center):
        key = (remaining, center)
        if key not in compatible_cache:
            compatible_cache[key] = tuple(
                move for move in move_masks
                if ((move >> center) & 1) and not (move & ~remaining)
            )
        return compatible_cache[key]

    failed = set()
    def solve(remaining):
        if not remaining:
            return ()
        if remaining in failed:
            return None
        candidates = []
        cursor = remaining
        while cursor:
            bit = cursor & -cursor
            center = bit.bit_length() - 1
            options = compatible(remaining, center)
            if options:
                candidates.append((len(options), min(row.bit_count() for row in options), center, options))
            cursor ^= bit
        for _count, _weight, center, options in sorted(candidates):
            # The first item in the returned order has highest priority.  Its
            # reset move touches only itself and still-lower-priority bits.
            for move in sorted(options, key=lambda row: (row.bit_count(), row)):
                tail = solve(remaining ^ (1 << center))
                if tail is not None:
                    return ((center, move),) + tail
        failed.add(remaining)
        return None
    return solve((1 << center_count) - 1)


def descend_triangular(state, atlas):
    trace = []
    while state:
        selected = next(
            ((center, move) for center, move in atlas if (state >> center) & 1),
            None,
        )
        if selected is None:
            break
        center, move = selected
        trace.append(center)
        state ^= move
    return state, tuple(trace)


def cyclic_local_rule(state, move_masks, policy, limit=4096):
    """Iterate one fixed local sweep and return zero or a recurrent cycle."""
    seen = {}
    for sweep in range(limit):
        if not state:
            return 0, sweep, 0
        if state in seen:
            return state, sweep, sweep - seen[state]
        seen[state] = sweep
        for move in move_masks:
            overlap = (state & move).bit_count()
            if policy == "lit":
                fire = overlap > 0
            elif policy == "nonincrease":
                fire = 2 * overlap >= move.bit_count()
            else:
                raise ValueError(policy)
            if fire:
                state ^= move
    return state, limit, -1


def frozen_rule_certificate(shape, exhaustive_limit=18):
    fixture, logical_rows, centers, parity, moves, raw_rows = fixture_data(shape)
    masks = tuple(row[0] for row in moves)
    k = len(centers)
    all_states = tuple(range(1 << k)) if k <= exhaustive_limit else ()
    rng = random.Random(720_789 + len(fixture.cells))
    sampled = set()
    if not all_states:
        sampled.update(1 << bit for bit in range(k))
        sampled.update(((1 << k) - 1,))
        sampled.update(rng.getrandbits(k) for _ in range(4096))
    states = all_states or tuple(sorted(sampled))
    potential_results = {}
    for potential in ("hamming", "binary_lexicographic"):
        stuck = []
        maximum_steps = 0
        for state in states:
            residual, trace = descend(state, masks, potential)
            maximum_steps = max(maximum_steps, len(trace))
            if residual:
                stuck.append((state, residual, len(trace)))
        potential_results[potential] = {
            "stuck_nonzero_syndromes": len(stuck),
            "first_stuck": stuck[:16],
            "maximum_accepted_moves": maximum_steps,
        }
    cyclic_results = {}
    for policy in ("lit", "nonincrease"):
        stuck = []
        maximum_sweeps = 0
        cycle_lengths = {}
        for state in states:
            residual, sweeps, cycle = cyclic_local_rule(state, masks, policy)
            maximum_sweeps = max(maximum_sweeps, sweeps)
            if residual:
                stuck.append((state, residual, cycle))
                cycle_lengths[cycle] = cycle_lengths.get(cycle, 0) + 1
        cyclic_results[policy] = {
            "nonzero_recurrent_or_trapped_syndromes": len(stuck),
            "first_failures": stuck[:16],
            "cycle_length_counts": cycle_lengths,
            "maximum_sweeps": maximum_sweeps,
        }
    max_move_cells = max((len(row[3]) for row in moves), default=0)
    max_move_diameter = max((cell_diameter(fixture, row[3]) for row in moves), default=0)
    return {
        "shape": shape,
        "cells": len(fixture.cells),
        "physical_M2": fixture.qubits,
        "nonparity_centers": k,
        "raw_local_commutant_rows_with_nonzero_syndrome": raw_rows,
        "unique_local_syndrome_moves": len(moves),
        "move_syndrome_rank": rank(masks),
        "maximum_move_cells": max_move_cells,
        "maximum_move_diameter": max_move_diameter,
        "logical_commutator_failures": sum(
            M.symplectic(move[1], logical, fixture.qubits)
            for move in moves for logical in logical_rows
        ),
        "parity_commutator_failures": sum(
            M.symplectic(move[1], parity, fixture.qubits) for move in moves
        ),
        "tested_syndromes": len(states),
        "test_kind": "exhaustive" if all_states else "singletons+all+deterministic-sample",
        "potential_results": potential_results,
        "cyclic_local_rule_results": cyclic_results,
    }


def main():
    fixtures = tuple(
        frozen_rule_certificate(shape)
        for shape in ((2, 2, 1), (2, 2, 2), (3, 2, 2), (5, 3, 2))
    )
    checks = {
        "radius_one_moves_span_every_nonparity_center": all(row["move_syndrome_rank"] == row["nonparity_centers"] for row in fixtures),
        "strict_weight_descent_trap_is_detected": any(
            row["potential_results"]["hamming"]["stuck_nonzero_syndromes"] > 0
            for row in fixtures
        ),
        "cyclic_lit_move_recurrence_is_detected": any(
            row["cyclic_local_rule_results"]["lit"]["nonzero_recurrent_or_trapped_syndromes"] > 0
            for row in fixtures
        ),
        "cyclic_nonincrease_trap_or_recurrence_is_detected": any(
            row["cyclic_local_rule_results"]["nonincrease"]["nonzero_recurrent_or_trapped_syndromes"] > 0
            for row in fixtures
        ),
        "every_move_preserves_logical_even_CAR": all(row["logical_commutator_failures"] == 0 for row in fixtures),
        "every_move_preserves_total_parity": all(row["parity_commutator_failures"] == 0 for row in fixtures),
        "move_support_is_radius_one_cell_ball": all(row["maximum_move_diameter"] <= 2 for row in fixtures),
    }
    report = {
        "status": (
            "PASS_LOCAL_CONTROLLABILITY_AND_FROZEN_PUMP_DISCRIMINATOR"
            if all(checks.values()) else "FAIL_DISCRIMINATOR"
        ),
        "authority": "none",
        "audit": "unset",
        "rules": [
            "fair strict-Hamming descent over every radius-one move",
            "fixed cyclic sweep firing every move that touches a violated center",
            "fixed cyclic sweep firing every move that does not increase local violated-center count",
        ],
        "checks": checks,
        "fixtures": fixtures,
        "derived": [
            "radius-one logical-preserving moves span the nonparity center syndrome space on every tested box",
            "all reconstructed moves exactly commute with the logical even-CAR basis and supplied total parity",
            "span does not imply a pump: each of three frozen local dynamics has an executed trap or recurrent orbit",
        ],
        "supplied": [
            "Cycle-720 companion physical dictionary and local-center basis",
            "one total-parity superselection label",
            "fresh local syndrome environments and a fair recurrent local-rule scheduler",
        ],
        "open": [
            "a translation-compatible convergent center-reset law rather than a finite global syndrome solve",
            "literal gate routing/coloring for simultaneous overlapping moves",
            "raw six-mode logical-coordinate insertion into companion L",
            "gauge-factor preparation and renewal",
            "proper-cubic covariance of a successful recurrent law",
        ],
    }
    report["source_sha256"] = sha256(Path(__file__).read_bytes()).hexdigest()
    payload = json.dumps(report, sort_keys=True, separators=(",", ":"))
    report["report_sha256"] = sha256(payload.encode()).hexdigest()
    print("REPORT_JSON", json.dumps(report, sort_keys=True))
    if not all(checks.values()):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
