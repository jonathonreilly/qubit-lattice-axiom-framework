#!/usr/bin/env python3
"""Cycle 797: bounded companion-center preparation with supplied priority.

The companion center is represented by elementary eta-plaquette flux.  In a
fixed axial frame, the independent checks are all xy/xz plaquettes plus yz
plaquettes on the x=0 face.  For each radius-two cell ball this probe
enumerates the complete syndrome subspace of physical Paulis that commute
with the logical even-CAR character and total parity.  It then constructs a
raw-move triangular atlas: the move for a pivot toggles that pivot and only
later pivots.  A one-pass measurement/conditional-Pauli channel therefore
resets every lawful center syndrome with no postselection; measurement and
work environments are retained.

The finite axial priority/front, boundary corner, and proper-cubic frame are
still supplied.  This result is not yet a translation-compatible autonomous
recurrent law and does not insert raw six-mode logical data.  Each check is
remeasured just in time, so no stale syndrome register is host-updated.
"""

from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path
import random

import frontier_cycle720_cell_majorana_companion_geometry_2026_07_27 as M
import frontier_cycle720_companion_subsystem_m2_update_2026_07_27 as U720
import frontier_cycle797_companion_center_local_pump_discriminator_2026_07_30 as S
import frontier_cycle797_companion_axial_center_core_2026_07_30 as A


def paired_basis(rows):
    """Independent syndrome rows retaining their physical representatives."""
    pivots = {}
    output = []
    for syndrome, physical in rows:
        while syndrome:
            pivot = syndrome.bit_length() - 1
            if pivot in pivots:
                syndrome ^= pivots[pivot][0]
                physical ^= pivots[pivot][1]
            else:
                pivots[pivot] = (syndrome, physical)
                output.append((syndrome, physical))
                break
    return tuple(output)


def support_cells(fixture, vector):
    mask = (1 << fixture.qubits) - 1
    occupied = (vector & mask) | (vector >> fixture.qubits)
    return frozenset(
        M.qubit_cell(fixture, qubit)
        for qubit in range(fixture.qubits)
        if (occupied >> qubit) & 1
    )


def diameter(fixture, cells):
    return max((S.distance(fixture, left, right) for left in cells for right in cells), default=0)


def local_projected_moves(fixture, logical, parity, plaquettes, independent, radius=2):
    """Enumerate every local syndrome in each radius-R commutant subspace."""
    center_vectors = tuple(row[4].symplectic(fixture.qubits) for row in plaquettes)
    best = {}
    maximum_local_syndrome_rank = 0
    enumerated = 0
    for anchor in range(len(fixture.cells)):
        allowed = {
            cell for cell in range(len(fixture.cells))
            if S.distance(fixture, anchor, cell) <= radius
        }
        raw = S.physical_nullspace_basis(fixture, logical, allowed)
        even = [row for row in raw if not M.symplectic(row, parity, fixture.qubits)]
        odd = [row for row in raw if M.symplectic(row, parity, fixture.qubits)]
        if odd:
            even.extend(odd[0] ^ row for row in odd[1:])
        basis = paired_basis(tuple(
            (
                sum(M.symplectic(row, center, fixture.qubits) << index for index, center in enumerate(center_vectors)),
                row,
            )
            for row in even
        ))
        maximum_local_syndrome_rank = max(maximum_local_syndrome_rank, len(basis))
        for coefficients in range(1, 1 << len(basis)):
            full_syndrome = 0
            physical = 0
            for index, (syndrome, row) in enumerate(basis):
                if (coefficients >> index) & 1:
                    full_syndrome ^= syndrome
                    physical ^= row
            projected = sum(
                ((full_syndrome >> old) & 1) << new
                for new, old in enumerate(independent)
            )
            if not projected or projected.bit_count() > 5:
                continue
            enumerated += 1
            cells = support_cells(fixture, physical)
            mask = (1 << fixture.qubits) - 1
            key = (
                projected.bit_count(),
                len(cells),
                diameter(fixture, cells),
                ((physical & mask) | (physical >> fixture.qubits)).bit_count(),
                full_syndrome,
                physical,
            )
            if projected not in best or key < best[projected][0]:
                best[projected] = (key, physical, full_syndrome, anchor, cells)
    return best, maximum_local_syndrome_rank, enumerated


def triangular_atlas(moves, coordinates, seed):
    """Construct and independently replay a raw-row triangular atlas."""
    by_bit = tuple(
        tuple((mask, data) for mask, data in moves.items() if (mask >> bit) & 1)
        for bit in range(coordinates)
    )
    best_length = 0
    for attempt in range(4096):
        rng = random.Random(seed + attempt)
        remaining = (1 << coordinates) - 1
        atlas = []
        while remaining:
            candidates = []
            for bit in range(coordinates):
                if not ((remaining >> bit) & 1):
                    continue
                options = tuple((mask, data) for mask, data in by_bit[bit] if not (mask & ~remaining))
                if options:
                    candidates.append((len(options), min(mask.bit_count() for mask, _data in options), bit, options))
            if not candidates:
                break
            candidates.sort(key=lambda row: row[:3])
            pool = candidates[: min(len(candidates), 1 + (attempt % 8))]
            _count, _minimum, pivot, options = rng.choice(pool)
            minimum_weight = min(mask.bit_count() for mask, _data in options)
            options = tuple(row for row in options if row[0].bit_count() == minimum_weight)
            mask, data = rng.choice(options)
            atlas.append((pivot, mask, data))
            remaining ^= 1 << pivot
        best_length = max(best_length, len(atlas))
        if not remaining:
            return tuple(atlas), attempt + 1, best_length
    return (), 4096, best_length


def projected_syndrome(full_syndrome, independent):
    return sum(
        ((full_syndrome >> old) & 1) << new
        for new, old in enumerate(independent)
    )


def pump_remeasure(full_syndrome, independent, atlas, dirty_at=None):
    """Sequential just-in-time check measurement and controlled correction."""
    applied = []
    for index, (pivot, _move, data) in enumerate(atlas):
        # This value is remeasured from the current physical center sector;
        # it is not a host update of a stale syndrome register.
        measured = (projected_syndrome(full_syndrome, independent) >> pivot) & 1
        if index == dirty_at:
            measured ^= 1
        if measured:
            full_syndrome ^= data[2]
            applied.append(pivot)
    return projected_syndrome(full_syndrome, independent), full_syndrome, tuple(applied)


def edge_lift_basis(fixture, edge_index, plaquettes, independent):
    equations = []
    for old in independent:
        boundary = plaquettes[old][3]
        equations.append(sum(1 << edge_index[key] for key in boundary))
    output = []
    for target in range(len(independent)):
        solution = A.solve(
            tuple((mask, int(index == target)) for index, mask in enumerate(equations)),
            len(fixture.edges),
        )
        if solution is None:
            raise AssertionError(("independent plaquette coordinate has no edge lift", target))
        output.append(solution)
    return tuple(output)


def certificate(shape):
    fixture = M.CompanionFixture.build(shape)
    edge_index, plaquettes = A.geometry(fixture)
    logical = A.logical_rows(fixture)
    parity = M.Pauli(z=(1 << fixture.matter_qubits) - 1).symplectic(fixture.qubits)
    # Axial cohomology coordinates: all faces involving x, plus yz on x=0.
    independent = tuple(
        index for index, (cell, first, second, _boundary, _row) in enumerate(plaquettes)
        if 0 in (first, second) or cell[0] == 0
    )
    expected = len(fixture.edges) - len(fixture.cells) + 1
    moves, maximum_local_rank, enumerated = local_projected_moves(
        fixture, logical, parity, plaquettes, independent, 2
    )
    atlas, attempts, best_length = triangular_atlas(
        moves, len(independent), 720789 + len(fixture.cells)
    )
    processed = 0
    triangular_failures = 0
    logical_failures = 0
    parity_failures = 0
    maximum_cells = 0
    maximum_diameter = 0
    maximum_weight = 0
    maximum_syndrome_weight = 0
    maximum_joint_measure_correct_cells = 0
    maximum_joint_measure_correct_diameter = 0
    for pivot, move, data in atlas:
        _key, physical, _full, _anchor, cells = data
        triangular_failures += not ((move >> pivot) & 1)
        triangular_failures += bool(move & processed)
        processed |= 1 << pivot
        logical_failures += sum(M.symplectic(physical, row, fixture.qubits) for row in logical)
        parity_failures += M.symplectic(physical, parity, fixture.qubits)
        maximum_cells = max(maximum_cells, len(cells))
        maximum_diameter = max(maximum_diameter, diameter(fixture, cells))
        mask = (1 << fixture.qubits) - 1
        maximum_weight = max(maximum_weight, ((physical & mask) | (physical >> fixture.qubits)).bit_count())
        maximum_syndrome_weight = max(maximum_syndrome_weight, move.bit_count())
        center_cells = support_cells(
            fixture, plaquettes[independent[pivot]][4].symplectic(fixture.qubits)
        )
        joint_cells = cells | center_cells
        maximum_joint_measure_correct_cells = max(
            maximum_joint_measure_correct_cells, len(joint_cells)
        )
        maximum_joint_measure_correct_diameter = max(
            maximum_joint_measure_correct_diameter,
            diameter(fixture, joint_cells),
        )

    center_vectors = tuple(row[4].symplectic(fixture.qubits) for row in plaquettes)
    operator_rows = M.operator_rows(fixture)
    relation_rows = M.relation_certificate(fixture)["relation_rows"]
    _gauge_report, gauge = U720.gauge_structure(
        fixture,
        tuple(row[1] for row in operator_rows),
        relation_rows,
    )
    actual_center_rows, _gauge_pairs = A.F.symplectic_split_vectors(
        gauge, fixture.qubits
    )
    actual_center_rank = A.rank(actual_center_rows)
    plaquette_plus_parity_rank = A.rank(center_vectors + (parity,))
    actual_center_span_mismatches = sum(
        A.rank(actual_center_rows + (row,)) != actual_center_rank
        for row in center_vectors + (parity,)
    )
    rng = random.Random(789720 + len(fixture.cells))
    lift_basis = edge_lift_basis(fixture, edge_index, plaquettes, independent)
    if len(independent) <= 9:
        coordinate_words = tuple(range(1 << len(independent)))
        test_kind = "exhaustive independent center syndromes"
    else:
        coordinate_words = tuple(
            sorted({0, (1 << len(independent)) - 1, *(1 << bit for bit in range(len(independent))), *(rng.getrandbits(len(independent)) for _ in range(4096))})
        )
        test_kind = "zero+all+single-coordinate+deterministic-held"
    residual_failures = 0
    maximum_applied = 0
    for coordinate_word in coordinate_words:
        edge_word = 0
        for bit, lift in enumerate(lift_basis):
            if (coordinate_word >> bit) & 1:
                edge_word ^= lift
        full = A.coboundary(edge_index, plaquettes, edge_word)
        projected, residual, applied = pump_remeasure(full, independent, atlas)
        residual_failures += bool(projected or residual)
        maximum_applied = max(maximum_applied, len(applied))

    deletion_control_failures = 0
    for deleted, (_pivot, _move, data) in enumerate(atlas):
        full = data[2]
        projected, residual, _applied = pump_remeasure(
            full, independent, atlas[:deleted] + atlas[deleted + 1:]
        )
        deletion_control_failures += not bool(projected or residual)
    dirty_ancilla_failures_not_exposed = 0
    for dirty in range(len(atlas)):
        projected, residual, _applied = pump_remeasure(
            0, independent, atlas, dirty_at=dirty
        )
        dirty_ancilla_failures_not_exposed += not bool(projected or residual)
    return {
        "shape": shape,
        "cells": len(fixture.cells),
        "physical_M2": fixture.qubits,
        "plaquettes": len(plaquettes),
        "center_rank": S.rank(center_vectors),
        "axial_independent_checks": len(independent),
        "expected_center_rank": expected,
        "actual_Cycle720_center_rank_including_parity": actual_center_rank,
        "plaquette_plus_parity_rank": plaquette_plus_parity_rank,
        "actual_Cycle720_center_span_mismatches": actual_center_span_mismatches,
        "local_syndromes_enumerated_weight_at_most_5": enumerated,
        "unique_projected_local_moves": len(moves),
        "maximum_local_syndrome_rank": maximum_local_rank,
        "triangular_atlas_rows": len(atlas),
        "construction_attempts": attempts,
        "best_partial_atlas_rows": best_length,
        "triangular_replay_failures": triangular_failures,
        "logical_commutator_failures": logical_failures,
        "parity_commutator_failures": parity_failures,
        "maximum_move_cells": maximum_cells,
        "maximum_move_diameter": maximum_diameter,
        "maximum_move_Pauli_weight": maximum_weight,
        "maximum_projected_syndrome_weight": maximum_syndrome_weight,
        "maximum_joint_measure_correct_cells": maximum_joint_measure_correct_cells,
        "maximum_joint_measure_correct_diameter": maximum_joint_measure_correct_diameter,
        "flux_tests": len(coordinate_words),
        "flux_test_kind": test_kind,
        "full_center_residual_failures": residual_failures,
        "atlas_row_deletions_not_detected": deletion_control_failures,
        "dirty_measurement_ancilla_mutations_not_exposed": dirty_ancilla_failures_not_exposed,
        "maximum_applied_moves": maximum_applied,
        "center_rows_nonhermitian": sum(row[4].phase % 2 != (row[4].x & row[4].z).bit_count() % 2 for row in plaquettes),
        "center_relation_phase_failures": M.C.R.F.base.stabilizer_phase_failures([row[4] for row in plaquettes], fixture.qubits),
    }


def main():
    fixtures = tuple(certificate(shape) for shape in ((2, 2, 1), (2, 2, 2), (3, 2, 2), (5, 3, 2)))
    checks = {
        "axial_checks_are_complete_center_coordinates": all(row["center_rank"] == row["axial_independent_checks"] == row["expected_center_rank"] for row in fixtures),
        "plaquettes_plus_parity_equal_the_actual_Cycle720_center_span": all(
            row["actual_Cycle720_center_rank_including_parity"]
            == row["plaquette_plus_parity_rank"]
            == row["expected_center_rank"] + 1
            and row["actual_Cycle720_center_span_mismatches"] == 0
            for row in fixtures
        ),
        "a_full_raw_move_triangular_atlas_was_constructed": all(row["triangular_atlas_rows"] == row["expected_center_rank"] and row["triangular_replay_failures"] == 0 for row in fixtures),
        "every_atlas_move_is_bounded_radius_two": all(row["maximum_move_diameter"] <= 4 for row in fixtures),
        "every_atlas_move_preserves_logical_even_CAR_and_parity": all(row["logical_commutator_failures"] == row["parity_commutator_failures"] == 0 for row in fixtures),
        "one_pass_resets_every_tested_full_lawful_flux": all(row["full_center_residual_failures"] == 0 for row in fixtures),
        "every_atlas_row_deletion_is_active": all(row["atlas_row_deletions_not_detected"] == 0 for row in fixtures),
        "dirty_measurement_ancilla_mutations_are_not_silently_accepted": all(row["dirty_measurement_ancilla_mutations_not_exposed"] == 0 for row in fixtures),
        "center_character_is_phase_consistent": all(row["center_rows_nonhermitian"] == row["center_relation_phase_failures"] == 0 for row in fixtures),
    }
    report = {
        "status": "PASS_BOUNDED_NONPOSTSELECTED_CENTER_PUMP__PRIORITY_FRAME_SUPPLIED" if all(checks.values()) else "FAIL_RADIUS2_TRIANGULAR_CENTER_PUMP",
        "authority": "none",
        "audit": "unset",
        "checks": checks,
        "fixtures": fixtures,
        "channel": (
            "in triangular priority order remeasure the current bounded axial plaquette pivot into a fresh retained register, "
            "apply the associated radius-two logical-commuting Pauli iff that just-in-time outcome is -1, "
            "and retain every measurement and control environment"
        ),
        "derived_if_pass": [
            "projection is upgraded to a trace-preserving nonpostselected center-sector preparation channel at stabilizer-macro level",
            "the complete logical even-CAR character and both total-parity blocks are unchanged",
            "every measurement/correction macro has bounded spatial support on the tested boxes",
        ],
        "supplied": [
            "one axial proper-cubic frame and open-boundary corner",
            "the finite-box triangular priority/front atlas",
            "fresh local syndrome/work registers initialized blank",
        ],
        "open": [
            "derive the priority/front as a translation-compatible recurrent local law and audit all 24 frames/576 products",
            "literal nearest-neighbor routing and collision colors for the controlled Pauli measurements",
            "prepare or renew a lawful gauge factor",
            "insert arbitrary raw six-mode logical coordinates into companion L",
            "compose seam/contact/update and held-size recurrence",
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
