#!/usr/bin/env python3
"""Cycle 797: execute the reversible center-syndrome Stinespring word.

The algebraic triangular pump requires later syndrome bits to track earlier
corrections. This runner realizes that bookkeeping with an explicit reversible
auxiliary circuit:

  1. coherently extract every independent commuting center check into a clean
     syndrome register using H--controlled-Pauli--H;
  2. copy the current pivot bit into one fresh retained outcome M2;
  3. conditionally apply the atlas Pauli correction to the physical bank; and
  4. CNOT that retained bit into every syndrome-register bit toggled by the
     correction.

The last operation is the missing executed update.  It keeps the register
equal to the current physical syndrome and clears it after one triangular
pass.  All outcomes are retained, so the induced channel is trace preserving
and nonpostselected.  The axial frame, boundary corner and finite priority
front remain explicit supplies.  No circuit ordinal is physical time.
"""

from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path
import random

import numpy as np

import frontier_cycle797_companion_priority_center_preparation_2026_07_30 as TRI
import frontier_cycle797_companion_center_local_pump_discriminator_2026_07_30 as DESCENT
import frontier_cycle797_companion_axial_center_core_2026_07_30 as EDGE

M = TRI.M
SHAPES = ((2, 2, 1), (2, 2, 2), (3, 2, 2), (5, 3, 2))


def atlas_data(shape):
    fixture = M.CompanionFixture.build(shape)
    edge_index, plaquettes = EDGE.geometry(fixture)
    logical = EDGE.logical_rows(fixture)
    parity = M.Pauli(
        z=(1 << fixture.matter_qubits) - 1
    ).symplectic(fixture.qubits)
    independent = tuple(
        index
        for index, (cell, first, second, _boundary, _row)
        in enumerate(plaquettes)
        if 0 in (first, second) or cell[0] == 0
    )
    moves, maximum_local_rank, enumerated = TRI.local_projected_moves(
        fixture, logical, parity, plaquettes, independent, 2
    )
    atlas, attempts, best_length = TRI.triangular_atlas(
        moves, len(independent), 720789 + len(fixture.cells)
    )
    return {
        "fixture": fixture,
        "edge_index": edge_index,
        "plaquettes": plaquettes,
        "logical": logical,
        "parity": parity,
        "independent": independent,
        "atlas": atlas,
        "maximum_local_rank": maximum_local_rank,
        "enumerated": enumerated,
        "attempts": attempts,
        "best_length": best_length,
    }


def execute_reversible_syndrome_word(
    full_syndrome,
    independent,
    atlas,
    *,
    dirty_register=0,
    dirty_outcomes=0,
    delete_extraction=None,
    delete_copy=None,
    delete_correction=None,
    delete_update=None,
):
    """Execute the extraction/copy/correction/XOR circuit on basis sectors."""
    physical = full_syndrome
    projected = TRI.projected_syndrome(physical, independent)
    syndrome = dirty_register
    extraction_gates = []
    for bit in range(len(independent)):
        extraction_gates.append(("CENTER_EXTRACT_XOR", bit))
        if bit != delete_extraction:
            syndrome ^= ((projected >> bit) & 1) << bit
    outcomes = dirty_outcomes
    trace = []
    gates = list(extraction_gates)
    for ordinal, (pivot, move, data) in enumerate(atlas):
        gates.append(("COPY_PIVOT_TO_RETAINED", pivot, ordinal))
        if ordinal != delete_copy:
            outcomes ^= ((syndrome >> pivot) & 1) << ordinal
        control = (outcomes >> ordinal) & 1
        gates.append(("CONTROLLED_PHYSICAL_PAULI", ordinal, data[1]))
        if control and ordinal != delete_correction:
            physical ^= data[2]
        for bit in range(len(independent)):
            if not ((move >> bit) & 1):
                continue
            gates.append(("SYNDROME_UPDATE_CNOT", ordinal, bit))
            if control and (ordinal, bit) != delete_update:
                syndrome ^= 1 << bit
        trace.append((ordinal, pivot, control, syndrome, physical))
    return {
        "physical_full_syndrome": physical,
        "physical_projected_syndrome": TRI.projected_syndrome(
            physical, independent
        ),
        "syndrome_register": syndrome,
        "retained_outcomes": outcomes,
        "trace": tuple(trace),
        "gates": tuple(gates),
    }


def stale_register_word(full_syndrome, independent, atlas):
    """Hostile comparator: extract once but omit the update CNOTs."""
    physical = full_syndrome
    syndrome = TRI.projected_syndrome(physical, independent)
    outcomes = 0
    for ordinal, (pivot, _move, data) in enumerate(atlas):
        control = (syndrome >> pivot) & 1
        outcomes |= control << ordinal
        if control:
            physical ^= data[2]
    return physical, outcomes


def coordinate_words(data):
    k = len(data["independent"])
    if k <= 9:
        return tuple(range(1 << k)), "exhaustive"
    rng = random.Random(970_827 + len(data["fixture"].cells))
    words = {
        0,
        (1 << k) - 1,
        *(1 << bit for bit in range(k)),
        *(rng.getrandbits(k) for _ in range(4096)),
    }
    return tuple(sorted(words)), "basis+all+deterministic-held"


def full_syndrome_lifts(data):
    basis = TRI.edge_lift_basis(
        data["fixture"], data["edge_index"],
        data["plaquettes"], data["independent"],
    )
    return tuple(
        EDGE.coboundary(
            data["edge_index"], data["plaquettes"], edge_word
        )
        for edge_word in basis
    )


def support_and_gate_certificate(data):
    fixture = data["fixture"]
    plaquettes = data["plaquettes"]
    independent = data["independent"]
    maximum_measure_cells = 0
    maximum_measure_diameter = 0
    maximum_correction_cells = 0
    maximum_correction_diameter = 0
    maximum_macro_cells = 0
    maximum_macro_diameter = 0
    maximum_update_cell_distance = 0
    maximum_center_weight = 0
    correction_weight = 0
    update_cnot_count = 0
    center_weight = 0
    cell_lookup = {cell: index for index, cell in enumerate(fixture.cells)}
    for pivot, move, atlas_row in data["atlas"]:
        _key, physical, _full, _anchor, correction_cells = atlas_row
        pivot_center = plaquettes[independent[pivot]]
        pivot_cells = TRI.support_cells(
            fixture, pivot_center[4].symplectic(fixture.qubits)
        )
        toggled_center_cells = set()
        pivot_owner = cell_lookup[pivot_center[0]]
        for bit in range(len(independent)):
            if not ((move >> bit) & 1):
                continue
            center = plaquettes[independent[bit]]
            cells = TRI.support_cells(
                fixture, center[4].symplectic(fixture.qubits)
            )
            toggled_center_cells.update(cells)
            update_cnot_count += 1
            maximum_update_cell_distance = max(
                maximum_update_cell_distance,
                DESCENT.distance(fixture, pivot_owner, cell_lookup[center[0]]),
            )
        macro_cells = (
            set(correction_cells) | set(pivot_cells) | toggled_center_cells
        )
        maximum_measure_cells = max(maximum_measure_cells, len(pivot_cells))
        maximum_measure_diameter = max(
            maximum_measure_diameter,
            TRI.diameter(fixture, pivot_cells),
        )
        maximum_correction_cells = max(
            maximum_correction_cells, len(correction_cells)
        )
        maximum_correction_diameter = max(
            maximum_correction_diameter,
            TRI.diameter(fixture, correction_cells),
        )
        maximum_macro_cells = max(maximum_macro_cells, len(macro_cells))
        maximum_macro_diameter = max(
            maximum_macro_diameter,
            TRI.diameter(fixture, macro_cells),
        )
        mask = (1 << fixture.qubits) - 1
        correction_weight += (
            (physical & mask) | (physical >> fixture.qubits)
        ).bit_count()
        local_center_weight = (
            pivot_center[4].x | pivot_center[4].z
        ).bit_count()
        center_weight += local_center_weight
        maximum_center_weight = max(
            maximum_center_weight, local_center_weight
        )
    k = len(independent)
    return {
        "syndrome_register_M2": k,
        "retained_outcome_M2": k,
        "center_extraction_H_gates": 2 * k,
        "center_extraction_controlled_Pauli_factors": center_weight,
        "pivot_copy_CNOTs": k,
        "controlled_correction_Pauli_factors": correction_weight,
        "syndrome_update_CNOTs": update_cnot_count,
        "maximum_center_measurement_Pauli_weight": maximum_center_weight,
        "maximum_measurement_cells": maximum_measure_cells,
        "maximum_measurement_diameter": maximum_measure_diameter,
        "maximum_correction_cells": maximum_correction_cells,
        "maximum_correction_diameter": maximum_correction_diameter,
        "maximum_complete_macro_cells": maximum_macro_cells,
        "maximum_complete_macro_diameter": maximum_macro_diameter,
        "maximum_syndrome_update_owner_distance_cells": (
            maximum_update_cell_distance
        ),
        "maximum_syndrome_update_fanout": max(
            move.bit_count() for _pivot, move, _data in data["atlas"]
        ),
        "literal_NN_route_executed": False,
    }


def frame_support_certificate(data):
    fixture = data["fixture"]
    frames = tuple(M.C.R.F.base.proper_cubic_frames())
    supports = []
    for pivot, move, atlas_row in data["atlas"]:
        _key, _physical, _full, _anchor, correction_cells = atlas_row
        cells = set(correction_cells)
        for bit in range(len(data["independent"])):
            if (move >> bit) & 1:
                center = data["plaquettes"][data["independent"][bit]][4]
                cells.update(TRI.support_cells(
                    fixture, center.symplectic(fixture.qubits)
                ))
        supports.append(tuple(fixture.cells[cell] for cell in cells))
    distance_failures = 0
    for frame in frames:
        for support in supports:
            moved = tuple(
                tuple(int(value) for value in frame @ np.asarray(cell))
                for cell in support
            )
            before = sorted(
                sum(abs(a - b) for a, b in zip(left, right))
                for left in support for right in support
            )
            after = sorted(
                sum(abs(a - b) for a, b in zip(left, right))
                for left in moved for right in moved
            )
            distance_failures += before != after
    product_failures = 0
    cells = tuple(fixture.cells)
    for left in frames:
        for right in frames:
            product = left @ right
            for cell in cells:
                vector = np.asarray(cell)
                product_failures += not np.array_equal(
                    left @ (right @ vector), product @ vector
                )
    return {
        "proper_cubic_frames": len(frames),
        "ordered_frame_products": len(frames) ** 2,
        "transported_support_distance_failures": distance_failures,
        "frame_product_coordinate_failures": product_failures,
        "scope": (
            "conditional transport of the supplied axial atlas support; "
            "not an autonomous frame/front selector"
        ),
    }


def dense_environment_isometry(environment_images, k):
    dimension = 1 << k
    matrix = np.zeros((dimension, dimension), dtype=complex)
    for source, environment in enumerate(environment_images):
        matrix[environment, source] = 1
    gram = matrix.conj().T @ matrix
    return float(np.linalg.norm(gram - np.eye(dimension)))


def certificate(shape):
    data = atlas_data(shape)
    fixture = data["fixture"]
    k = len(data["independent"])
    words, test_kind = coordinate_words(data)
    lift_syndromes = full_syndrome_lifts(data)
    reset_failures = register_failures = host_disagreements = 0
    environment_images = {}
    maximum_applied = 0
    for coordinate in words:
        full = 0
        for bit, lift in enumerate(lift_syndromes):
            if (coordinate >> bit) & 1:
                full ^= lift
        result = execute_reversible_syndrome_word(
            full, data["independent"], data["atlas"]
        )
        host = TRI.pump_remeasure(
            full, data["independent"], data["atlas"]
        )
        reset_failures += bool(
            result["physical_full_syndrome"]
            or result["physical_projected_syndrome"]
        )
        register_failures += bool(result["syndrome_register"])
        host_disagreements += (
            result["physical_full_syndrome"] != host[1]
            or result["physical_projected_syndrome"] != host[0]
        )
        environment_images[coordinate] = result["retained_outcomes"]
        maximum_applied = max(
            maximum_applied,
            result["retained_outcomes"].bit_count(),
        )

    # The circuit is GF(2)-linear on center sectors.  Full rank of the retained
    # outcome map proves injectivity, hence Stinespring isometry, on every one
    # of 2^k sectors even when the held campaign is sampled.
    environment_basis = tuple(
        execute_reversible_syndrome_word(
            lift_syndromes[bit], data["independent"], data["atlas"]
        )["retained_outcomes"]
        for bit in range(k)
    )
    environment_rank = DESCENT.rank(environment_basis)
    dense_residual = None
    if k <= 9:
        dense_images = tuple(environment_images[state] for state in range(1 << k))
        dense_residual = dense_environment_isometry(dense_images, k)

    deletions = {
        "extraction": 0,
        "copy": 0,
        "physical_correction": 0,
        "syndrome_update": 0,
    }
    for ordinal, (pivot, move, atlas_row) in enumerate(data["atlas"]):
        full = atlas_row[2]
        extraction = execute_reversible_syndrome_word(
            full, data["independent"], data["atlas"],
            delete_extraction=pivot,
        )
        copy = execute_reversible_syndrome_word(
            full, data["independent"], data["atlas"],
            delete_copy=ordinal,
        )
        correction = execute_reversible_syndrome_word(
            full, data["independent"], data["atlas"],
            delete_correction=ordinal,
        )
        # Every triangular move contains its pivot, and no later move can
        # revisit an already processed pivot.  Deleting this specific update
        # therefore leaves an unambiguous, load-bearing work-register defect;
        # deleting another set bit can be repaired by a later triangular row.
        update_bit = pivot
        update = execute_reversible_syndrome_word(
            full, data["independent"], data["atlas"],
            delete_update=(ordinal, update_bit),
        )
        deletions["extraction"] += not bool(
            extraction["physical_full_syndrome"]
            or extraction["syndrome_register"]
        )
        deletions["copy"] += not bool(
            copy["physical_full_syndrome"] or copy["syndrome_register"]
        )
        deletions["physical_correction"] += not bool(
            correction["physical_full_syndrome"]
        )
        deletions["syndrome_update"] += not bool(
            update["syndrome_register"]
        )

    dirty_register_not_exposed = 0
    dirty_outcome_not_exposed = 0
    for bit in range(k):
        dirty = execute_reversible_syndrome_word(
            0, data["independent"], data["atlas"],
            dirty_register=1 << bit,
        )
        dirty_register_not_exposed += not bool(
            dirty["physical_full_syndrome"]
            or dirty["syndrome_register"]
        )
        dirty = execute_reversible_syndrome_word(
            0, data["independent"], data["atlas"],
            dirty_outcomes=1 << bit,
        )
        dirty_outcome_not_exposed += not bool(
            dirty["physical_full_syndrome"]
            or dirty["syndrome_register"]
        )

    reversed_failures = 0
    stale_failures = 0
    for coordinate in words:
        full = 0
        for bit, lift in enumerate(lift_syndromes):
            if (coordinate >> bit) & 1:
                full ^= lift
        reversed_result = execute_reversible_syndrome_word(
            full, data["independent"], tuple(reversed(data["atlas"]))
        )
        reversed_failures += bool(
            reversed_result["physical_full_syndrome"]
            or reversed_result["syndrome_register"]
        )
        stale_physical, _outcomes = stale_register_word(
            full, data["independent"], data["atlas"]
        )
        stale_failures += bool(stale_physical)

    q = fixture.qubits
    logical_failures = parity_failures = 0
    center_vectors = tuple(
        row[4].symplectic(q) for row in data["plaquettes"]
    )
    center_logical_failures = center_parity_failures = 0
    for center in center_vectors:
        center_logical_failures += sum(
            M.symplectic(center, logical, q) for logical in data["logical"]
        )
        center_parity_failures += M.symplectic(center, data["parity"], q)
    for _pivot, _move, atlas_row in data["atlas"]:
        physical = atlas_row[1]
        logical_failures += sum(
            M.symplectic(physical, logical, q) for logical in data["logical"]
        )
        parity_failures += M.symplectic(physical, data["parity"], q)

    locality = support_and_gate_certificate(data)
    frame = frame_support_certificate(data)
    return {
        "shape": shape,
        "cells": len(fixture.cells),
        "independent_center_checks": k,
        "atlas_rows": len(data["atlas"]),
        "construction_attempts": data["attempts"],
        "tested_center_sectors": len(words),
        "test_kind": test_kind,
        "physical_reset_failures": reset_failures,
        "syndrome_register_return_failures": register_failures,
        "host_remeasurement_disagreements": host_disagreements,
        "retained_environment_map_rank": environment_rank,
        "dense_small_Stinespring_Gram_residual": dense_residual,
        "maximum_applied_corrections": maximum_applied,
        "deletion_not_exposed": deletions,
        "dirty_syndrome_register_mutations_not_exposed": (
            dirty_register_not_exposed
        ),
        "dirty_retained_outcome_mutations_not_exposed": (
            dirty_outcome_not_exposed
        ),
        "hostile_reversed_order_residual_sectors": reversed_failures,
        "hostile_stale_register_residual_sectors": stale_failures,
        "logical_commutator_failures": logical_failures,
        "parity_commutator_failures": parity_failures,
        "center_measurement_logical_commutator_failures": (
            center_logical_failures
        ),
        "center_measurement_parity_commutator_failures": (
            center_parity_failures
        ),
        "locality_and_gate_census": locality,
        "conditional_frame_support": frame,
    }


def source_hashes():
    modules = (
        TRI,
        DESCENT,
        EDGE,
    )
    return {
        Path(module.__file__).name: sha256(
            Path(module.__file__).read_bytes()
        ).hexdigest()
        for module in modules
    }


def main():
    fixtures = tuple(certificate(shape) for shape in SHAPES)
    checks = {
        "executed_reversible_syndrome_word_matches_remeasurement_and_resets_every_tested_sector": all(
            row["physical_reset_failures"] == 0
            and row["syndrome_register_return_failures"] == 0
            and row["host_remeasurement_disagreements"] == 0
            for row in fixtures
        ),
        "retained_outcome_map_is_an_isometry_on_every_center_sector": all(
            row["retained_environment_map_rank"]
            == row["independent_center_checks"]
            and (
                row["dense_small_Stinespring_Gram_residual"] is None
                or row["dense_small_Stinespring_Gram_residual"] < 1e-12
            )
            for row in fixtures
        ),
        "extraction_copy_correction_and_update_deletions_are_active": all(
            all(value == 0 for value in row["deletion_not_exposed"].values())
            for row in fixtures
        ),
        "dirty_auxiliary_inputs_are_not_silently_accepted": all(
            row["dirty_syndrome_register_mutations_not_exposed"] == 0
            and row["dirty_retained_outcome_mutations_not_exposed"] == 0
            for row in fixtures
        ),
        "nontrivial_triangular_updates_are_load_bearing_while_diagonal_atlases_are_order_independent": all(
            row["locality_and_gate_census"][
                "maximum_syndrome_update_fanout"
            ] == 1
            or (
                row["hostile_reversed_order_residual_sectors"] > 0
                and row["hostile_stale_register_residual_sectors"] > 0
            )
            for row in fixtures
        ) and any(
            row["locality_and_gate_census"][
                "maximum_syndrome_update_fanout"
            ] > 1
            for row in fixtures
        ),
        "measurements_and_corrections_preserve_logical_even_CAR_and_parity": all(
            row["logical_commutator_failures"] == 0
            and row["parity_commutator_failures"] == 0
            and row["center_measurement_logical_commutator_failures"] == 0
            and row["center_measurement_parity_commutator_failures"] == 0
            for row in fixtures
        ),
        "complete_measure_copy_correct_update_macros_have_held_bounded_support": all(
            row["locality_and_gate_census"][
                "maximum_complete_macro_diameter"
            ] <= 6
            and row["locality_and_gate_census"][
                "maximum_syndrome_update_fanout"
            ] <= 5
            for row in fixtures
        ),
        "conditional_atlas_support_transports_in_24_frames_and_576_products": all(
            row["conditional_frame_support"]["proper_cubic_frames"] == 24
            and row["conditional_frame_support"]["ordered_frame_products"] == 576
            and row["conditional_frame_support"][
                "transported_support_distance_failures"
            ] == 0
            and row["conditional_frame_support"][
                "frame_product_coordinate_failures"
            ] == 0
            for row in fixtures
        ),
    }
    passed = all(checks.values())
    report = {
        "status": (
            "PASS_EXECUTED_REVERSIBLE_CENTER_SYNDROME_STINESPRING__"
            "FRAME_FRONT_AND_NN_ROUTING_SUPPLIED"
            if passed else "FAIL_ROUTE_B_REVERSIBLE_SYNDROME_EXECUTION"
        ),
        "authority": "none",
        "audit": "unset",
        "checks": checks,
        "fixtures": fixtures,
        "source_sha256": source_hashes(),
        "derived": [
            "an explicit reversible syndrome-register circuit replacing every host-side later-bit update by retained-outcome-to-syndrome CNOTs",
            "a trace-preserving nonpostselected center-preparation Stinespring channel with exhaustive 1/5/9-center and held 30-center algebraic tests",
            "exact logical-even-CAR and total-parity preservation for every center measurement and physical correction",
            "bounded complete measurement/copy/correction/update macro support and conditional proper-cubic support transport",
        ],
        "supplied": [
            "one axial proper-cubic frame, open-boundary corner, and finite triangular priority/front atlas",
            "clean syndrome and retained-outcome M2 registers",
            "bounded controlled-Pauli measurement/correction primitives and a route chart",
        ],
        "open": [
            "literal nearest-neighbor routing, returned work, and collision coloring of every controlled-Pauli and syndrome-update macro",
            "derive the axial frame, boundary corner, and triangular front from a translation-compatible recurrent law",
            "autonomous clean-auxiliary genesis, fault repair, renewal, and occurrence",
            "compose this center pump with the raw-to-L logical insertion and recurrent free/seam/contact G",
        ],
        "boundary": (
            "The host-update gap is closed at the reversible syndrome-register "
            "and nonpostselected channel level.  It is not a literal routed "
            "physical-M2 program, translation-invariant autonomous front, "
            "physical time law, no-go, minimum, or axiom-pressure result."
        ),
    }
    report["report_sha256"] = sha256(json.dumps(
        report, sort_keys=True, separators=(",", ":"), default=str
    ).encode()).hexdigest()
    print("SUMMARY_JSON", json.dumps(report, sort_keys=True, default=str))
    print(report["status"])
    raise SystemExit(0 if passed else 1)


if __name__ == "__main__":
    main()
