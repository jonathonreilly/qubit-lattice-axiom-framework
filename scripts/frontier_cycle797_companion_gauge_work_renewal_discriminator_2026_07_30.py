#!/usr/bin/env python3
"""Cycle 797: gauge-only Bell work and bounded renewal discriminator.

This runner asks two narrow questions of the landed Cycle-789 three-register
prefix:

1. Does the corrected Bell leg leave the output/reference character algebra
   tensor-factorized from a fixed environment algebra?
2. Can the environment stabilizers be generated in bounded cell
   neighbourhoods, so an inverse local Clifford cleanup is algebraically
   available rather than only a dense global completion?

The one-mode analogue also executes an explicit six-gate environment-only
cleanup and includes deletion and hostile-order controls.  Circuit ordinals
and rotor labels below are scheduling structure, not physical time.  The
multi-cell result classifies the remaining work; it does not construct a
translation-compatible renewal law.
"""

from __future__ import annotations

from hashlib import sha256
import json
from itertools import product

import numpy as np

import frontier_companion_bank_bell_character_dilation_2026_07_28 as B
import frontier_cycle720_companion_subsystem_m2_update_2026_07_27 as U720
import frontier_cycle720_companion_subsystem_mixed_gauge_factorization_2026_07_27 as F720
import frontier_cycle789_three_register_even_car_channel_2026_07_30 as C789
import frontier_cycle789_three_bank_fixed_coframe_schedule_2026_07_30 as S789
import frontier_cycle789_two_bank_input_collision_discriminator_2026_07_30 as D789


TOL = 1.0e-12


def binary_rank(rows: tuple[int, ...]) -> int:
    pivots: dict[int, int] = {}
    for original in rows:
        row = original
        while row:
            pivot = row.bit_length() - 1
            if pivot in pivots:
                row ^= pivots[pivot]
            else:
                pivots[pivot] = row
                break
    return len(pivots)


def kernel_combinations(restrictions: tuple[int, ...]) -> tuple[int, ...]:
    """Basis of coefficient words whose XOR of restrictions vanishes."""
    pivots: dict[int, tuple[int, int]] = {}
    kernel: list[int] = []
    for index, original in enumerate(restrictions):
        row = original
        combination = 1 << index
        while row:
            pivot = row.bit_length() - 1
            if pivot in pivots:
                row ^= pivots[pivot][0]
                combination ^= pivots[pivot][1]
            else:
                pivots[pivot] = (row, combination)
                break
        if row == 0:
            kernel.append(combination)
    return tuple(kernel)


def restriction(row, excluded_mask: int, width: int) -> int:
    return (row.x & excluded_mask) | ((row.z & excluded_mask) << width)


def subgroup_supported_in(
    generators: tuple,
    allowed_mask: int,
    width: int,
) -> tuple[int, ...]:
    all_mask = (1 << width) - 1
    excluded = all_mask ^ allowed_mask
    return kernel_combinations(tuple(
        restriction(row, excluded, width) for row in generators
    ))


def combination_vectors(generators, combinations: tuple[int, ...], width: int):
    vectors = tuple(row.symplectic(width) for row in generators)
    output = []
    for combination in combinations:
        row = 0
        while combination:
            bit = combination & -combination
            row ^= vectors[bit.bit_length() - 1]
            combination ^= bit
        output.append(row)
    return tuple(output)


def sector_bases(fixture):
    q = fixture.qubits
    operator_rows = B.M.operator_rows(fixture)
    physical_paulis = tuple(row[1] for row in operator_rows)
    physical = tuple(row.symplectic(q) for row in physical_paulis)
    target = tuple(
        row[2].symplectic(fixture.matter_qubits) for row in operator_rows
    )
    paired = F720.independent_paired_basis(physical, target)
    _algebra_radicals, logical_pairs = F720.symplectic_split_paired(paired, q)
    logical = tuple(item[0] for pair in logical_pairs for item in pair)
    relation_rows = B.M.relation_certificate(fixture)["relation_rows"]
    _gauge_report, gauge = U720.gauge_structure(
        fixture, physical_paulis, relation_rows
    )
    gauge_radicals, _gauge_pairs = F720.symplectic_split_vectors(gauge, q)
    parity = B.M.Pauli(
        z=(1 << fixture.matter_qubits) - 1
    ).symplectic(q)

    # Reconstruct the landed local-center complement to total parity without
    # importing another scratch probe.
    pivots = {parity.bit_length() - 1: parity}
    centers = []
    for original in F720.local_center_basis(fixture, gauge, 2):
        row = original
        while row:
            pivot = row.bit_length() - 1
            if pivot in pivots:
                row ^= pivots[pivot]
            else:
                pivots[pivot] = row
                centers.append(original)
                break
        if len(centers) == len(gauge_radicals) - 1:
            break
    if len(centers) != len(gauge_radicals) - 1:
        raise AssertionError("failed to reconstruct local center complement")
    return logical, gauge, tuple(centers), parity


def local_center_move_rank(fixture, logical, centers, parity, radius=1):
    """Center syndromes spanned by local logical-commuting parity-even moves."""
    q = fixture.qubits
    center_rows = centers + (parity,)
    all_local_syndromes = []
    for anchor in range(len(fixture.cells)):
        allowed_qubits = tuple(
            qubit for qubit in range(q)
            if manhattan(
                fixture.cells[B.M.qubit_cell(fixture, qubit)],
                fixture.cells[anchor],
            ) <= radius
        )
        positions = allowed_qubits + tuple(q + qubit for qubit in allowed_qubits)
        restrictions = []
        for position in positions:
            if position < q:  # X variable sees logical Z.
                restrictions.append(sum(
                    ((row >> (q + position)) & 1) << index
                    for index, row in enumerate(logical)
                ))
            else:  # Z variable sees logical X.
                qubit = position - q
                restrictions.append(sum(
                    ((row >> qubit) & 1) << index
                    for index, row in enumerate(logical)
                ))
        local_basis = kernel_combinations(tuple(restrictions))
        syndromes = []
        for solution in local_basis:
            vector = 0
            for variable, position in enumerate(positions):
                vector |= ((solution >> variable) & 1) << position
            syndromes.append(sum(
                B.M.symplectic(vector, center, q) << index
                for index, center in enumerate(center_rows)
            ))
        even = [row for row in syndromes if not ((row >> len(centers)) & 1)]
        odd = [row for row in syndromes if (row >> len(centers)) & 1]
        if odd:
            even.extend(odd[0] ^ row for row in odd[1:])
        all_local_syndromes.extend(
            row & ((1 << len(centers)) - 1) for row in even
        )
    return binary_rank(tuple(all_local_syndromes))


def manhattan(left, right) -> int:
    return sum(abs(a - b) for a, b in zip(left, right))


def mask_for_cell_set(obj, cells: frozenset, owners) -> int:
    q = obj["q"]
    mask = 0
    fixture = obj["fixture"]
    for bank in (1, 2):  # environment I and L, not O or diagnostic R
        for local_qubit in range(q):
            cell_index, _local = S789.local_nine_index(fixture, local_qubit)
            if fixture.cells[cell_index] in cells:
                mask |= 1 << (bank * q + local_qubit)
    for index, owner in enumerate(owners):
        if owner in cells:
            mask |= 1 << (4 * q + index)
    return mask


def local_factor_certificate(shape, atlas):
    obj = C789.circuit_objects(shape, atlas)
    fixture = obj["fixture"]
    q = obj["q"]
    rank = obj["rank"]
    width = obj["width"]
    initial = obj["resource"] + obj["live_reference"] + obj["ancilla_z"]
    final = C789.conjugate_basis(initial, obj["gates"])
    output_binary_failures, output_signed_failures = C789.signed_span_failures(
        obj["output_reference"], final, width
    )
    owners = tuple(
        S789.tag_owner_slot(fixture, tag)[0]
        for tag in obj["compiled"]["tags"]
    )

    output_reference_mask = (
        ((1 << q) - 1)
        | (((1 << q) - 1) << (3 * q))
    )
    environment_mask = (
        (((1 << (2 * q)) - 1) << q)
        | (((1 << rank) - 1) << (4 * q))
    )
    output_subgroup = subgroup_supported_in(
        final, output_reference_mask, width
    )
    environment_subgroup = subgroup_supported_in(final, environment_mask, width)

    output_local_vectors = combination_vectors(
        final, output_subgroup, width
    )
    output_image_vectors = tuple(
        (row.x & output_reference_mask)
        | ((row.z & output_reference_mask) << width)
        for row in final
    )
    logical, gauge, centers, parity = sector_bases(fixture)

    def lift_output(vector):
        x = vector & ((1 << q) - 1)
        z = vector >> q
        return x | (z << width)

    def cross_quotient(extra):
        extra = tuple(lift_output(row) for row in extra)
        return (
            binary_rank(output_image_vectors + extra)
            - binary_rank(output_local_vectors + extra)
        )

    raw_cross_quotient = (
        binary_rank(output_image_vectors) - binary_rank(output_local_vectors)
    )
    gauge_diameters = []
    for row in gauge:
        support = frozenset(
            B.M.qubit_cell(fixture, qubit)
            for qubit in range(q)
            if (((row & ((1 << q) - 1)) | (row >> q)) >> qubit) & 1
        )
        gauge_diameters.append(max((
            manhattan(fixture.cells[left], fixture.cells[right])
            for left in support for right in support
        ), default=0))
    center_move_rank = local_center_move_rank(
        fixture, logical, centers, parity, radius=1
    )

    radius_rows = []
    for radius in (0, 1, 2):
        local_combinations = []
        maximum_local_kernel = 0
        for center in fixture.cells:
            neighborhood = frozenset(
                cell for cell in fixture.cells
                if manhattan(center, cell) <= radius
            )
            allowed = mask_for_cell_set(obj, neighborhood, owners)
            kernel = subgroup_supported_in(final, allowed, width)
            local_combinations.extend(kernel)
            maximum_local_kernel = max(maximum_local_kernel, len(kernel))
        local_rank = binary_rank(tuple(local_combinations))
        radius_rows.append({
            "radius_cells": radius,
            "generated_environment_rank": local_rank,
            "environment_rank_target": 2 * rank,
            "rank_deficit": 2 * rank - local_rank,
            "maximum_single_neighborhood_kernel_rank": maximum_local_kernel,
        })

    return {
        "shape": list(shape),
        "cells": len(fixture.cells),
        "edges": len(fixture.edges),
        "character_rank": rank,
        "total_stabilizer_rank": binary_rank(tuple(
            row.symplectic(width) for row in final
        )),
        "output_reference_subgroup_rank": len(output_subgroup),
        "output_reference_binary_span_failures": output_binary_failures,
        "output_reference_signed_span_failures": output_signed_failures,
        "environment_subgroup_rank": len(environment_subgroup),
        "factorization_rank_sum": len(output_subgroup) + len(environment_subgroup),
        "factorization_rank_deficit": 3 * rank - (
            len(output_subgroup) + len(environment_subgroup)
        ),
        "N_plus_2E_deficit_prediction": (
            len(fixture.cells) + 2 * len(fixture.edges)
        ),
        "sector_quotient": {
            "raw_output_environment_cross_rank": raw_cross_quotient,
            "logical_pair_rows": len(logical),
            "cross_rank_after_quotient_by_logical_rows": cross_quotient(logical),
            "nonparity_local_center_rows": len(centers),
            "radius_one_logical_commuting_center_move_rank": center_move_rank,
            "cross_rank_after_nonparity_center_reset": cross_quotient(centers),
            "cross_rank_after_center_plus_supplied_parity": cross_quotient(
                centers + (parity,)
            ),
            "local_gauge_rows": len(gauge),
            "maximum_landed_gauge_generator_cell_diameter": max(
                gauge_diameters, default=0
            ),
            "cross_rank_after_quotient_by_full_gauge": cross_quotient(gauge),
            "retained_syndrome_boundary": (
                "a coherent center reset transfers its old signs to retained syndrome; "
                "rank reachability does not return that syndrome blank or define a convergent local rule"
            ),
        },
        "local_generation": radius_rows,
        "final_tableau_sha256": sha256("|".join(
            f"{row.phase}:{row.x:x}:{row.z:x}" for row in final
        ).encode()).hexdigest(),
    }


def cnot(state, control: int, target: int):
    return D789.apply_controlled_pauli(
        state, control, ((target, D789.X),), 5
    )


def cz(state, control: int, target: int):
    return D789.apply_controlled_pauli(
        state, control, ((target, D789.Z),), 5
    )


def repaired_one_mode_state(live):
    # Registers O,I,L,aZ,aX.
    state = D789.prepare_bell_oi(live)
    state = D789.bell_measure_character(
        state, 3, ((1, D789.Z), (2, D789.Z)), 5
    )
    state = D789.bell_measure_character(
        state, 4, ((1, D789.X), (2, D789.X)), 5
    )
    state = D789.apply_controlled_pauli(
        state, 3, ((0, D789.X),), 5
    )
    return D789.apply_controlled_pauli(
        state, 4, ((0, D789.Z),), 5
    )


def cleanup_one_mode(state, *, delete_index: int | None = None, hostile=False):
    operations = (
        ("CZ", 2, 4),
        ("CNOT", 2, 3),
        ("CNOT", 1, 3),
        ("H", 4),
        ("H", 2),
        ("H", 1),
    )
    if hostile:
        operations = tuple(reversed(operations))
    for index, operation in enumerate(operations):
        if index == delete_index:
            continue
        if operation[0] == "CZ":
            state = cz(state, operation[1], operation[2])
        elif operation[0] == "CNOT":
            state = cnot(state, operation[1], operation[2])
        else:
            state = D789.apply_one(state, D789.H, operation[1], 5)
    return state


def one_mode_cleanup_certificate():
    states = {
        "zero": D789.ZERO,
        "one": D789.ONE,
        "plus": (D789.ZERO + D789.ONE) / np.sqrt(2),
        "plus_i": (D789.ZERO + 1j * D789.ONE) / np.sqrt(2),
    }
    clean_residuals = []
    deletion_residuals = []
    hostile_residuals = []
    environment_vectors = []
    for live in states.values():
        final = repaired_one_mode_state(live)
        target = D789.kron_states((
            live, D789.ZERO, D789.ZERO, D789.ZERO, D789.ZERO
        ))
        clean_residuals.append(float(np.linalg.norm(
            cleanup_one_mode(final) - target
        )))
        deletion_residuals.append(float(np.linalg.norm(
            cleanup_one_mode(final, delete_index=1) - target
        )))
        hostile_residuals.append(float(np.linalg.norm(
            cleanup_one_mode(final, hostile=True) - target
        )))
        tensor = final.reshape(2, -1)
        # Since O is pure and exactly transferred, contract it out to compare
        # the environment ray across four independent inputs.
        environment_vectors.append(live.conj() @ tensor)
    overlaps = [
        abs(np.vdot(left, right))
        for left, right in product(environment_vectors, repeat=2)
    ]
    return {
        "registers": "O,I,L,aZ,aX",
        "tested_inputs": list(states),
        "cleanup_gates": [
            "CZ(L,aX)", "CNOT(L,aZ)", "CNOT(I,aZ)",
            "H(aX)", "H(L)", "H(I)",
        ],
        "maximum_clean_output_plus_blank_environment_residual": max(clean_residuals),
        "minimum_environment_ray_overlap": min(overlaps),
        "deleted_cleanup_gate_residual": min(deletion_residuals),
        "hostile_reversed_cleanup_residual": min(hostile_residuals),
    }


def multimode_reversibility_controls(atlas):
    obj = C789.circuit_objects((1, 1, 1), atlas)
    initial = obj["resource"] + obj["live_reference"] + obj["ancilla_z"]
    final = C789.conjugate_basis(initial, obj["gates"])
    round_trip = C789.conjugate_basis(final, tuple(reversed(obj["gates"])))
    inverse_mismatches = sum(
        B.fields(left) != B.fields(right)
        for left, right in zip(initial, round_trip)
    )

    dirty = list(initial)
    dirty_index = len(obj["resource"]) + len(obj["live_reference"])
    row = dirty[dirty_index]
    dirty[dirty_index] = B.Pauli((row.phase + 2) % 4, row.x, row.z)
    dirty_final = C789.conjugate_basis(tuple(dirty), obj["gates"])
    dirty_binary, dirty_signed = C789.signed_span_failures(
        obj["output_reference"], dirty_final, obj["width"]
    )

    missing_live = (
        obj["resource"]
        + obj["live_reference"][:-1]
        + obj["ancilla_z"]
    )
    missing_final = C789.conjugate_basis(missing_live, obj["gates"])
    missing_binary, missing_signed = C789.signed_span_failures(
        obj["output_reference"], missing_final, obj["width"]
    )
    source_controls = C789.deletion_controls(atlas)
    return {
        "one_cell_inverse_round_trip_tableau_mismatches": inverse_mismatches,
        "dirty_Bell_ancilla_output_binary_failures": dirty_binary,
        "dirty_Bell_ancilla_output_signed_failures": dirty_signed,
        "missing_live_character_output_binary_failures": missing_binary,
        "missing_live_character_output_signed_failures": missing_signed,
        "deleted_private_dual_output_binary_failures": source_controls[
            "deleted_private_dual_output_binary_failures"
        ],
        "deleted_private_dual_output_signed_failures": source_controls[
            "deleted_private_dual_output_signed_failures"
        ],
        "hostile_self_comparison_output_binary_failures": source_controls[
            "self_comparison_output_binary_failures"
        ],
        "hostile_self_comparison_output_signed_failures": source_controls[
            "self_comparison_output_signed_failures"
        ],
    }


def covariance_label_certificate():
    frames = tuple(
        tuple(tuple(int(v) for v in row) for row in frame)
        for frame in B.V.T.proper_cubic_frames()
    )
    points = tuple(product(range(-1, 2), repeat=3))
    coordinate_failures = 0
    product_failures = 0
    distance_failures = 0
    for frame in frames:
        for point in points:
            mapped = S789.matvec(frame, point)
            distance_failures += manhattan(point, (0, 0, 0)) != manhattan(
                mapped, (0, 0, 0)
            )
        coordinate_failures += len({
            S789.matvec(frame, point) for point in points
        }) != len(points)
    for left in frames:
        for right in frames:
            combined = S789.matmul(left, right)
            product_failures += any(
                S789.matvec(left, S789.matvec(right, point))
                != S789.matvec(combined, point)
                for point in points
            )
    return {
        "proper_cubic_frames": len(frames),
        "ordered_frame_products": len(frames) ** 2,
        "coordinate_bijection_failures": coordinate_failures,
        "cell_radius_transport_failures": distance_failures,
        "product_failures": product_failures,
        "boundary": (
            "support-radius and label transport only; the landed Cycle-794 "
            "runner owns the full signed-prefix 24/576 audit"
        ),
    }


def main():
    atlas = B.P.build_private_atlases()
    boxes = tuple(local_factor_certificate(shape, atlas) for shape in (
        (1, 1, 1),
        (2, 1, 1),
        (2, 2, 1),
        (2, 2, 2),
        (3, 2, 2),
        (4, 1, 3),
        (1, 4, 3),
        (5, 3, 2),
    ))
    dense = one_mode_cleanup_certificate()
    controls = multimode_reversibility_controls(atlas)
    covariance = covariance_label_certificate()
    checks = {
        "Bell_output_exact_but_environment_does_not_factor": all(
            row["output_reference_subgroup_rank"] == row["character_rank"]
            and row["output_reference_binary_span_failures"] == 0
            and row["output_reference_signed_span_failures"] == 0
            and row["factorization_rank_deficit"] > 0
            for row in boxes
        ),
        "all_cross_correlations_are_gauge_not_logical_on_tested_boxes": all(
            row["sector_quotient"]["raw_output_environment_cross_rank"]
            == row["factorization_rank_deficit"]
            and row["sector_quotient"]["cross_rank_after_quotient_by_logical_rows"]
            == row["factorization_rank_deficit"]
            and row["sector_quotient"]["cross_rank_after_quotient_by_full_gauge"] == 0
            for row in boxes
        ),
        "radius_one_moves_span_every_nonparity_center_syndrome": all(
            row["sector_quotient"]["radius_one_logical_commuting_center_move_rank"]
            == row["sector_quotient"]["nonparity_local_center_rows"]
            for row in boxes
        ),
        "held_size_falsifies_naive_N_plus_2E_extrapolation": (
            boxes[-1]["factorization_rank_deficit"]
            != boxes[-1]["N_plus_2E_deficit_prediction"]
        ),
        "anisotropic_raw_gauge_environment_is_order_sensitive_but_logical_quotient_is_not": (
            boxes[-3]["cells"] == boxes[-2]["cells"]
            and boxes[-3]["edges"] == boxes[-2]["edges"]
            and boxes[-3]["factorization_rank_deficit"]
            != boxes[-2]["factorization_rank_deficit"]
            and boxes[-3]["sector_quotient"]["cross_rank_after_quotient_by_full_gauge"] == 0
            and boxes[-2]["sector_quotient"]["cross_rank_after_quotient_by_full_gauge"] == 0
        ),
        "maximal_environment_subgroup_has_bounded_radius_one_generating_set": all(
            row["local_generation"][1]["generated_environment_rank"]
            == row["environment_subgroup_rank"]
            for row in boxes
        ),
        "one_mode_environment_only_cleanup_is_exact": (
            dense["maximum_clean_output_plus_blank_environment_residual"] < TOL
            and dense["minimum_environment_ray_overlap"] > 1 - TOL
        ),
        "cleanup_deletion_and_hostile_order_are_detected": (
            dense["deleted_cleanup_gate_residual"] > 0.1
            and dense["hostile_reversed_cleanup_residual"] > 0.1
        ),
        "multimode_prefix_is_injective_and_controls_are_active": (
            controls["one_cell_inverse_round_trip_tableau_mismatches"] == 0
            and controls["dirty_Bell_ancilla_output_signed_failures"] > 0
            and controls["missing_live_character_output_binary_failures"] > 0
            and (
                controls["deleted_private_dual_output_binary_failures"] > 0
                or controls["deleted_private_dual_output_signed_failures"] > 0
            )
            and (
                controls["hostile_self_comparison_output_binary_failures"] > 0
                or controls["hostile_self_comparison_output_signed_failures"] > 0
            )
        ),
        "support_radius_is_24_frame_576_product_covariant": (
            covariance["proper_cubic_frames"] == 24
            and covariance["ordered_frame_products"] == 576
            and not covariance["coordinate_bijection_failures"]
            and not covariance["cell_radius_transport_failures"]
            and not covariance["product_failures"]
        ),
    }
    report = {
        "status": "PASS" if all(checks.values()) else "FAIL",
        "authority": "none",
        "audit": "unset",
        "checks": checks,
        "one_mode_cleanup": dense,
        "multimode_controls": controls,
        "boxes": boxes,
        "covariance": covariance,
        "supplied": [
            "Cycle-789 Choi resource on O/I, live character code on L, private-dual atlas, clean Bell syndrome ancillas",
            "finite fixture boundary and transported local cell labels",
            "the landed Cycle-794 literal prefix and G remain separate acceptance evidence",
        ],
        "derived": [
            "exact output/reference character transfer together with an exact subsystem-rank census of residual correlations",
            "held-size falsification of the provisional N+2E extrapolation and an anisotropic raw-gauge diagnostic",
            "an exact rank quotient showing all residual cross correlations lie in the landed local gauge span and none in the logical span",
            "radius-one logical-commuting moves span all nonparity center syndromes, but only with retained bookkeeping",
            "radius-one generation of the maximal environment-only stabilizer subgroup",
            "an explicit six-gate environment-only cleanup in the exact one-mode repaired channel",
            "deletion and hostile-order discrimination plus support-radius 24/576 covariance",
        ],
        "open": [
            "classify and refresh the noncentral gauge-pair correlations left after center-sector reset",
            "a translation-compatible convergent center/gauge renewal rule and a reversible destination for retained syndrome",
            "synthesis of a multi-row local inverse Clifford or gauge-refresh channel after that bookkeeping question is resolved",
            "renewal of the supplied O/I Choi resource and clean Bell ancillas from the preceding physical epoch",
            "translation-compatible genesis/enforcement of local coframe, cell colours and legal character sector",
            "one literal returned NN epoch composing preparation, Cycle-789 prefix, Cycle-720 G and cleanup",
        ],
        "verdict": (
            "The repaired one-mode Bell/correction work is exactly recyclable, and the maximal environment-only subgroup of the landed multi-row channel is radius-one generated. "
            "The landed retained even-CAR tableau still has output-environment cross correlations, so a clean recurrent work return is not yet licensed. "
            "Every one of those correlations is gauge-only under the actual Cycle-720 factorization, and radius-one moves span the nonparity center slice. "
            "What remains is not logical-channel fidelity but a translation-local reversible bookkeeping law that refreshes gauge/center work without accumulating retained syndrome."
        ),
        "claim_boundary": (
            "Executable local-renewal discriminator, not a recurrent physical compiler, no-go, minimum, or axiom-pressure result."
        ),
    }
    encode = lambda value: value.item() if isinstance(value, np.generic) else value
    report["report_sha256"] = sha256(json.dumps(
        report, sort_keys=True, separators=(",", ":"), default=encode
    ).encode()).hexdigest()
    print("SUMMARY_JSON", json.dumps(report, sort_keys=True, default=encode))
    if report["status"] != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
