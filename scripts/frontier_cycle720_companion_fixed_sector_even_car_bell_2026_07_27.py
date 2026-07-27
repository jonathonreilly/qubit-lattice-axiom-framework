#!/usr/bin/env python3
"""Cycle-720 fixed-sector live encoder through local even-CAR Bell rows.

The raw-mode Bell attempt required nonlocal Jordan--Wigner cleanup.  This
route changes the measured error coordinates, not the target channel: it
measures the doubled local even-CAR generator family (onsite parities,
onsite adjacent Majorana pairs, and nearest-neighbour seam factor two).
Every doubled row is supported on one cell or one edge in the CAR algebra.
Its outcome character drives the frozen output-only private-dual correction
for the matching Choi row, whose physical M2 support is also one cell or one
edge.  Thus no odd operator, parity string, or host parity query is used.

The construction is a CPTP encoder on a supplied common fixed-parity sector,
with a mixed gauge factor and retained measurement banks.  It is not a pure
isometry, autonomous sector selector, genesis theorem, Record/Born law, time
law, or source/gravity law.
"""

from __future__ import annotations

AUDIT_TIMEOUT_SEC = 900
NOTE_PATH = "docs/RECURRENT_COMPANION_PHYSICAL_M2_UPDATE_LOCAL_CHOI_PREPARATION_CYCLE720_BOUNDED_THEOREM_NOTE_2026-07-27.md"
AUDIT_INPUT_PATHS = (
    "docs/RECURRENT_COMPANION_PHYSICAL_M2_UPDATE_LOCAL_CHOI_PREPARATION_CYCLE720_BOUNDED_THEOREM_NOTE_2026-07-27.md",
    "scripts/ROUTE2_LOCAL_GAUGE_CAR_COMPILER_CYCLE232_2026_07_17.py",
    "scripts/active_cubic_source_response_cycle211_2026_07_16.py",
    "scripts/archive_carrier_source_ledger_cycle227_2026_07_17.py",
    "scripts/autonomous_cubic_field_emission_cycle214_2026_07_16.py",
    "scripts/common_matter_field_coin_family_cycle219_2026_07_16.py",
    "scripts/finite_coin_scalar_wave_dilation_cycle215_2026_07_16.py",
    "scripts/fock_modular_boundary_current_cycle229_2026_07_17.py",
    "scripts/frontier_cycle703_local_gauss_bksf_full_parity_2026_07_25.py",
    "scripts/frontier_cycle706_openreference_patchgraph_four_rail_equivalence_2026_07_26.py",
    "scripts/frontier_cycle708_cube_basis_gauge_core_2026_07_26.py",
    "scripts/frontier_cycle708_endpoint_cube_tableau_core_2026_07_26.py",
    "scripts/frontier_cycle708_physical_endpoint_cube_core_2026_07_26.py",
    "scripts/frontier_cycle709_local_seam_clifford_core_2026_07_26.py",
    "scripts/frontier_cycle709_local_seam_physical_core_2026_07_26.py",
    "scripts/frontier_cycle712_joint_two_cell_full_update_physical_m2_2026_07_26.py",
    "scripts/frontier_cycle720_bounded_general_clifford_orbit_2026_07_27.py",
    "scripts/frontier_cycle720_cell_majorana_companion_geometry_2026_07_27.py",
    "scripts/frontier_cycle720_coherent_cell_edge_gauge_common_e_2026_07_27.py",
    "scripts/frontier_cycle720_companion_2cube_m2_stinespring_covariance_2026_07_27.py",
    "scripts/frontier_cycle720_companion_checkerboard_frame_cocycle_2026_07_27.py",
    "scripts/frontier_cycle720_companion_fixed_sector_even_car_bell_2026_07_27.py",
    "scripts/frontier_cycle720_companion_local_choi_pump_covariance_2026_07_27.py",
    "scripts/frontier_cycle720_companion_local_choi_tree_plaquette_pump_2026_07_27.py",
    "scripts/frontier_cycle720_companion_parity_rail_local_gauge_2026_07_27.py",
    "scripts/frontier_cycle720_companion_repeated_star_choi_tensor_2026_07_27.py",
    "scripts/frontier_cycle720_companion_subsystem_m2_update_2026_07_27.py",
    "scripts/frontier_cycle720_companion_subsystem_mixed_gauge_factorization_2026_07_27.py",
    "scripts/frontier_cycle720_gauge_native_fswap_clifford_recurrence_2026_07_27.py",
    "scripts/frontier_cycle720_overlap_star_mixed_gauge_choi_2026_07_27.py",
    "scripts/frontier_cycle720_product_companion_full_word_holonomy_2026_07_27.py",
    "scripts/frontier_full128_25site_nn_circuit_core_2026_07_24.py",
    "scripts/frontier_full128_bare_frame_pair_cocycle_2026_07_24.py",
    "scripts/frontier_full128_code_projectors_2026_07_24.py",
    "scripts/frontier_full128_cycle_cocycle_intertwiner_2026_07_24.py",
    "scripts/frontier_full128_cycle_encoder_2026_07_24.py",
    "scripts/frontier_full128_two_rail_fixed_law_core_2026_07_24.py",
    "scripts/frontier_literal_patchgraph_cycle656_projected_trace_cycle707_2026_07_26.py",
    "scripts/frontier_literal_patchgraph_z3_m2_placement_core_cycle707_2026_07_26.py",
    "scripts/local_conservative_commit_resource_gravity_cycle9_2026_07_14.py",
    "scripts/local_generator_source_tournament_cycle228_2026_07_17.py",
    "scripts/proper_cubic_bound_object_equivalence_cycle210_2026_07_16.py",
    "scripts/retarded_cubic_mass_field_cycle213_2026_07_16.py",
    "scripts/spatial_car_contact_seam_form_factor_cycle230_2026_07_17.py",
    "scripts/virtual_exchange_green_kernel_cycle216_2026_07_16.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

from hashlib import sha256
import json

import numpy as np

import frontier_cycle720_cell_majorana_companion_geometry_2026_07_27 as M
import frontier_cycle720_companion_checkerboard_frame_cocycle_2026_07_27 as Q
import frontier_cycle720_companion_local_choi_tree_plaquette_pump_2026_07_27 as P
import frontier_cycle720_companion_local_choi_pump_covariance_2026_07_27 as V
import frontier_cycle720_overlap_star_mixed_gauge_choi_2026_07_27 as O


Pauli = M.Pauli


def canonical(row: Pauli) -> Pauli:
    return Pauli((row.x & row.z).bit_count() & 1, row.x, row.z)


def target_rows(
    fixture: M.CompanionFixture, tags: tuple[tuple, ...]
) -> tuple[Pauli, ...]:
    rows = []
    for tag in tags:
        if tag[0] == "onsite_Z":
            rows.append(Pauli(z=1 << (6 * tag[1] + tag[2])))
        elif tag[0] == "onsite_XX":
            left = 6 * tag[1] + tag[2]
            rows.append(Pauli(x=(1 << left) | (1 << (left + 1))))
        else:
            rows.append(fixture.target_terms(tag[1])[2])
    return tuple(rows)


def pauli_product(rows) -> Pauli:
    output = Pauli()
    for row in rows:
        output = output @ row
    return canonical(output)


def tag_modes(
    fixture: M.CompanionFixture, tag: tuple
) -> frozenset[tuple[int, int]]:
    if tag[0] == "onsite_Z":
        return frozenset(((tag[1], tag[2]),))
    if tag[0] == "onsite_XX":
        return frozenset(((tag[1], tag[2]), (tag[1], tag[2] + 1)))
    left, right, _owner, _axis, left_mode, right_mode = fixture.edges[tag[1]]
    return frozenset(((left, left_mode % 6), (right, right_mode % 6)))


def greedy_layers(supports: tuple[frozenset, ...]) -> tuple[int, ...]:
    layers: list[list[frozenset]] = []
    assignment = []
    for support in supports:
        for layer, occupied in enumerate(layers):
            if all(not (support & other) for other in occupied):
                occupied.append(support)
                assignment.append(layer)
                break
        else:
            layers.append([support])
            assignment.append(len(layers) - 1)
    return tuple(assignment)


def deterministic_even_samples(modes: int) -> tuple[Pauli, ...]:
    rows = {Pauli(), Pauli(z=(1 << modes) - 1)}
    for mode in range(modes):
        rows.add(Pauli(z=1 << mode))
    for mode in range(1, modes):
        rows.add(canonical(Pauli(x=1 | (1 << mode))))
    for seed in range(64):
        x = int.from_bytes(
            sha256(f"x:{modes}:{seed}".encode()).digest(), "little"
        ) & ((1 << modes) - 1)
        if x.bit_count() & 1:
            x ^= 1
        z = int.from_bytes(
            sha256(f"z:{modes}:{seed}".encode()).digest(), "little"
        ) & ((1 << modes) - 1)
        rows.add(canonical(Pauli(x=x, z=z)))
    return tuple(sorted(rows, key=lambda row: (row.x, row.z, row.phase)))


def box_certificate(
    shape: tuple[int, int, int], atlas: dict[str, object]
) -> dict[str, object]:
    fixture = O.arbitrary_fixture(Q.shape_cells(shape))
    graph, tags = P.direct_graph_basis(fixture)
    targets = target_rows(fixture, tags)
    corrections = tuple(
        P.correction_from_atlas(fixture, tag, atlas) for tag in tags
    )
    m = fixture.matter_qubits
    q = fixture.qubits
    total = q + m

    target_rank = P.C.R.F.base.gf2_rank(
        row.symplectic(m) for row in targets
    )
    doubled_rows = tuple(
        P.R.choi_pauli(row, row, m) for row in targets
    )
    doubled_rank = P.C.R.F.base.gf2_rank(
        row.symplectic(2 * m) for row in doubled_rows
    )
    doubled_commutator_failures = sum(
        M.symplectic(
            left.symplectic(2 * m), right.symplectic(2 * m), 2 * m
        )
        for index, left in enumerate(doubled_rows)
        for right in doubled_rows[:index]
    )
    car_supports = tuple(tag_modes(fixture, tag) for tag in tags)
    car_support_cell_failures = sum(
        len({cell for cell, _mode in support})
        > (2 if tag[0] == "edge" else 1)
        for tag, support in zip(tags, car_supports)
    )
    car_edge_distance_failures = 0
    for tag in tags:
        if tag[0] != "edge":
            continue
        left, right, *_rest = fixture.edges[tag[1]]
        car_edge_distance_failures += (
            sum(abs(a - b) for a, b in zip(
                fixture.cells[left], fixture.cells[right]
            )) != 1
        )

    correction_supports = tuple(P.pauli_cells(fixture, row) for row in corrections)
    correction_support_failures = 0
    correction_syndrome_failures = 0
    maximum_correction_cells = 0
    maximum_correction_diameter = 0
    for target, (tag, correction, support) in enumerate(
        zip(tags, corrections, correction_supports)
    ):
        declared = (
            {fixture.cells[tag[1]]}
            if tag[0] != "edge"
            else {fixture.cells[cell] for cell in fixture.edges[tag[1]][:2]}
        )
        correction_support_failures += not support <= declared
        maximum_correction_cells = max(maximum_correction_cells, len(support))
        maximum_correction_diameter = max(
            maximum_correction_diameter, P.R.support_diameter(support)
        )
        for row, stabilizer in enumerate(graph):
            correction_syndrome_failures += M.symplectic(
                correction.symplectic(total),
                stabilizer.symplectic(total), total,
            ) != int(row == target)

    measurement_layers = greedy_layers(car_supports)
    correction_layers = greedy_layers(tuple(
        frozenset(
            qubit for qubit in range(q)
            if ((row.x | row.z) >> qubit) & 1
        ) for row in corrections
    ))

    branch_syndrome_failures = 0
    branch_relation_failures = 0
    branch_target_character_failures = 0
    samples = deterministic_even_samples(m)
    target_relations = M.kernel_relations(tuple(
        row.symplectic(m) for row in targets
    ))
    for error in samples:
        syndrome = tuple(M.symplectic(
            error.symplectic(m), target.symplectic(m), m
        ) for target in targets)
        correction = pauli_product(
            row for bit, row in zip(syndrome, corrections) if bit
        )
        replay = tuple(M.symplectic(
            correction.symplectic(total),
            row.symplectic(total), total,
        ) for row in graph)
        branch_syndrome_failures += replay != syndrome
        branch_target_character_failures += sum(
            actual != expected for actual, expected in zip(replay, syndrome)
        )
        branch_relation_failures += sum(
            sum(
                bit for index, bit in enumerate(syndrome)
                if (relation >> index) & 1
            ) & 1
            for relation in target_relations
        )

    # Deleting the matching local private dual must leave its outcome sign.
    deleted = len(corrections) // 2
    deletion_residual = M.symplectic(
        corrections[deleted].symplectic(total),
        graph[deleted].symplectic(total), total,
    )
    return {
        "shape": shape,
        "cells": len(fixture.cells),
        "edges": len(fixture.edges),
        "matter_M2": m,
        "local_even_CAR_rows": len(targets),
        "target_even_algebra_rank": target_rank,
        "expected_connected_even_algebra_rank": 2 * m - 1,
        "fixed_sector_random_Bell_bits": target_rank - 1,
        "expected_fixed_sector_Bell_bits": 2 * (m - 1),
        "doubled_Bell_row_rank": doubled_rank,
        "doubled_Bell_row_commutator_failures": doubled_commutator_failures,
        "CAR_measurement_support_cell_failures": car_support_cell_failures,
        "CAR_edge_nearest_neighbor_failures": car_edge_distance_failures,
        "measurement_conflict_layers": max(measurement_layers, default=-1) + 1,
        "physical_private_dual_syndrome_failures": correction_syndrome_failures,
        "physical_private_dual_support_failures": correction_support_failures,
        "maximum_private_dual_support_cells": maximum_correction_cells,
        "maximum_private_dual_support_diameter": maximum_correction_diameter,
        "physical_correction_conflict_layers": max(correction_layers, default=-1) + 1,
        "lawful_even_characters_tested": len(samples),
        "branch_private_dual_character_failures": branch_syndrome_failures,
        "branch_character_entry_failures": branch_target_character_failures,
        "target_relation_rows": len(target_relations),
        "branch_target_relation_character_failures": branch_relation_failures,
        "delete_matching_private_dual_residual": deletion_residual,
        "input_output_identity": (
            "for every local even row T_i and lawful Bell error U, "
            "s_i=[U,T_i]; the physical correction product has exactly "
            "[C(s),P_i]=s_i, so the corrected fixed-sector Choi character "
            "is the identity character"
        ),
    }


def sector_matrix(row: Pauli, modes: int, parity: int) -> np.ndarray:
    I = np.eye(2, dtype=complex)
    X = np.asarray(((0, 1), (1, 0)), dtype=complex)
    Y = np.asarray(((0, -1j), (1j, 0)), dtype=complex)
    Z = np.asarray(((1, 0), (0, -1)), dtype=complex)
    factors = []
    for mode in reversed(range(modes)):
        x = (row.x >> mode) & 1
        z = (row.z >> mode) & 1
        factors.append((I, X, Z, Y)[x + 2 * z])
    full = np.asarray(((1,),), dtype=complex)
    for factor in factors:
        full = np.kron(full, factor)
    basis = tuple(
        state for state in range(1 << modes)
        if state.bit_count() % 2 == parity
    )
    return full[np.ix_(basis, basis)]


def abstract_teleportation_certificate(modes: int) -> dict[str, object]:
    # A line is enough: all onsite Z and adjacent Majorana-pair rows generate
    # the full even algebra.  Quotient by total parity on the fixed sector.
    rows = tuple(Pauli(z=1 << mode) for mode in range(modes)) + tuple(
        Pauli(x=(1 << mode) | (1 << (mode + 1)))
        for mode in range(modes - 1)
    )
    even = []
    for x in range(1 << modes):
        if x.bit_count() & 1:
            continue
        for z in range(1 << modes):
            matrix = sector_matrix(canonical(Pauli(x=x, z=z)), modes, 0)
            if not any(
                min(np.linalg.norm(matrix - phase * old) for phase in (1, -1, 1j, -1j))
                < 1.0e-12 for old in even
            ):
                even.append(matrix)
    d = 1 << (modes - 1)
    phi = np.eye(d, dtype=complex) / np.sqrt(d)
    bell = tuple(error @ phi for error in even)
    gram = np.asarray([
        [np.vdot(left, right) for right in bell] for left in bell
    ])
    max_branch_residual = 0.0
    completeness = np.zeros((d, d), dtype=complex)
    for error, bell_matrix in zip(even, bell):
        # K[o,l] = sum_r <B|l,r> Phi[r,o] = U^dagger/d.
        kraus = bell_matrix.conj().T / np.sqrt(d)
        corrected = error @ kraus
        max_branch_residual = max(
            max_branch_residual,
            float(np.linalg.norm(corrected - np.eye(d) / d)),
        )
        completeness += kraus.conj().T @ kraus
    return {
        "modes": modes,
        "fixed_sector_dimension": d,
        "Bell_outcomes": len(bell),
        "expected_outcomes": d * d,
        "Bell_basis_orthonormality_residual": float(
            np.linalg.norm(gram - np.eye(d * d))
        ),
        "corrected_branch_identity_residual": max_branch_residual,
        "Kraus_completeness_residual": float(
            np.linalg.norm(completeness - np.eye(d))
        ),
        "generator_rank": P.C.R.F.base.gf2_rank(
            row.symplectic(modes) for row in rows
        ),
        "expected_even_rank": 2 * modes - 1,
    }


def main() -> None:
    atlas = P.build_private_atlases()
    shapes = ((2, 2, 2), (5, 3, 2), (5, 5, 3), (6, 5, 4))
    boxes = tuple(box_certificate(shape, atlas) for shape in shapes)
    exact = tuple(abstract_teleportation_certificate(modes) for modes in (2, 3))
    covariance = V.frame_certificate((2, 2, 2), atlas)
    products = V.product_certificate(atlas)
    checks = []

    def check(label: str, condition: bool) -> None:
        checks.append({"label": label, "pass": bool(condition)})
        print("PASS" if condition else "FAIL", label)

    check(
        "local doubled even-CAR rows give a complete fixed-sector Bell algebra",
        all(
            box["target_even_algebra_rank"]
            == box["expected_connected_even_algebra_rank"]
            and box["fixed_sector_random_Bell_bits"]
            == box["expected_fixed_sector_Bell_bits"]
            and box["doubled_Bell_row_rank"]
            == box["target_even_algebra_rank"]
            and box["doubled_Bell_row_commutator_failures"] == 0
            and box["CAR_measurement_support_cell_failures"] == 0
            and box["CAR_edge_nearest_neighbor_failures"] == 0
            for box in boxes
        ),
    )
    check(
        "frozen private-dual atlas stays physical-M2 local on the held ladder",
        all(
            box["physical_private_dual_syndrome_failures"] == 0
            and box["physical_private_dual_support_failures"] == 0
            and box["maximum_private_dual_support_cells"] <= 2
            and box["maximum_private_dual_support_diameter"] <= 1
            for box in boxes
        ),
    )
    check(
        "measurement and correction words admit size-independent conflict coloring",
        max(box["measurement_conflict_layers"] for box in boxes) <= 6
        and max(box["physical_correction_conflict_layers"] for box in boxes) <= 24
        and len({box["measurement_conflict_layers"] for box in boxes[1:]}) == 1
        and len({box["physical_correction_conflict_layers"] for box in boxes[1:]}) == 1,
    )
    check(
        "lawful even Bell characters are exactly cancelled without changing fixed centers",
        all(
            box["branch_private_dual_character_failures"] == 0
            and box["branch_character_entry_failures"] == 0
            and box["branch_target_relation_character_failures"] == 0
            for box in boxes
        ),
    )
    check(
        "small-sector matrices certify CPTP teleportation rather than a formal syndrome relabeling",
        all(
            row["Bell_outcomes"] == row["expected_outcomes"]
            and row["generator_rank"] == row["expected_even_rank"]
            and row["Bell_basis_orthonormality_residual"] < 1.0e-12
            and row["corrected_branch_identity_residual"] < 1.0e-12
            and row["Kraus_completeness_residual"] < 1.0e-12
            for row in exact
        ),
    )
    check(
        "proper-cubic 24-frame and 576-product action preserves projector, atlas, corrections, and schedules",
        covariance["proper_cubic_frames"] == 24
        and all(covariance[key] == 0 for key in (
            "signed_projector_failures",
            "private_correction_syndrome_failures",
            "private_correction_support_failures",
            "route_locality_support_or_return_failures",
            "atlas_key_inverse_transport_failures",
            "schedule_key_inverse_transport_failures",
            "Bell_reference_conjugate_chart_failures",
            "syndrome_register_bijection_failures",
            "oriented_factor_2_or_3_edge_row_failures",
        ))
        and products["ordered_frame_products"] == 576
        and all(value == 0 for key, value in products.items() if key.endswith("failures")),
    )
    check(
        "deleting a matching local private dual leaves a nonzero Bell sign residual",
        all(box["delete_matching_private_dual_residual"] == 1 for box in boxes),
    )
    report = {
        "status": "PASS" if all(row["pass"] for row in checks) else "FAIL",
        "checks": checks,
        "atlas": {key: value for key, value in atlas.items() if key not in ("onsite", "edge")},
        "boxes": boxes,
        "exact_CPTP_controls": exact,
        "covariance": covariance,
        "frame_products": products,
        "derived": (
            "fixed-sector CPTP live-input encoder using bounded local even-CAR "
            "Bell rows and bounded physical-M2 private-dual corrections; exact "
            "character intertwiner, held-size reuse, constant conflict layers, "
            "and proper-cubic covariance"
        ),
        "supplied": (
            "common fixed parity/center sector; one-time locally pumped Choi "
            "resource; mixed gauge reference; retained Bell/syndrome banks; "
            "finite 64-port-environment correction atlas; finite layer colors; "
            "coframe-origin gauge sector"
        ),
        "open": (
            "autonomous sector and genesis selection; collision-free merge of "
            "preparation, Bell, correction, and recurrent-G epochs; sector-summed "
            "live E; downstream time/source/Record/Born acceptance harnesses"
        ),
        "claim_boundary": (
            "positive CPTP encoder only on a supplied common fixed-parity "
            "sector; CAR-local input measurements are domain operations, while "
            "all compiled corrections are bounded physical M2; not a pure "
            "isometry, sector law, physical time, Record, Born law, or source law"
        ),
        "input_Bell_measurement_physical_M2_compiled": False,
        "authority": "none",
        "audit": "unset",
    }
    print(json.dumps(report, indent=2, sort_keys=True))
    if report["status"] != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
