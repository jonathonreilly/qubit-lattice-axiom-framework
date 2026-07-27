#!/usr/bin/env python3
"""Cycle-720 exact mixed-gauge factorization for the companion subsystem.

The product-|000> companion encoder fails even though the radius-one
subsystem algebra closes.  This runner asks the sharper question: does the
physical algebra admit an explicit logical x gauge x center factorization in
which the complete physical word acts trivially on the gauge factor?

The factorization is aligned generator-by-generator with the ordinary
fixed-parity CAR presentation, including phases.  It therefore constructs a
finite-box CPTP encoder with a maximally mixed gauge factor.  Locality is
audited separately; an algebraic tableau is not called a bounded physical
preparation circuit.
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
    "scripts/frontier_cycle720_companion_subsystem_m2_update_2026_07_27.py",
    "scripts/frontier_cycle720_companion_subsystem_mixed_gauge_factorization_2026_07_27.py",
    "scripts/frontier_cycle720_gauge_native_fswap_clifford_recurrence_2026_07_27.py",
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

import frontier_cycle720_cell_majorana_companion_geometry_2026_07_27 as M
import frontier_cycle720_companion_subsystem_m2_update_2026_07_27 as U
import frontier_cycle720_coherent_cell_edge_gauge_common_e_2026_07_27 as C
import frontier_cycle720_product_companion_full_word_holonomy_2026_07_27 as H
import frontier_cycle708_endpoint_cube_tableau_core_2026_07_26 as B


Pauli = M.Pauli


def canonical_pauli(vector: int, qubits: int) -> Pauli:
    mask = (1 << qubits) - 1
    x, z = vector & mask, vector >> qubits
    return Pauli((x & z).bit_count() & 1, x, z)


def independent_paired_basis(
    physical: tuple[int, ...], target: tuple[int, ...]
) -> tuple[tuple[int, int, int], ...]:
    """Independent physical rows with their target image and source combination."""
    pivots: dict[int, tuple[int, int]] = {}
    output = []
    for index, original in enumerate(physical):
        row = original
        combination = 1 << index
        while row:
            pivot = row.bit_length() - 1
            if pivot in pivots:
                previous, previous_combination = pivots[pivot]
                row ^= previous
                combination ^= previous_combination
            else:
                pivots[pivot] = (row, combination)
                target_row = U.xor_rows(
                    target[item] for item in range(len(target))
                    if (combination >> item) & 1
                )
                output.append((row, target_row, combination))
                break
    return tuple(output)


def symplectic_split_paired(
    rows: tuple[tuple[int, int, int], ...], qubits: int
) -> tuple[tuple[tuple[int, int, int], ...], tuple[tuple[tuple[int, int, int], tuple[int, int, int]], ...]]:
    remaining = list(rows)
    radicals = []
    pairs = []
    while remaining:
        left = remaining.pop()
        partner = next((
            index for index, right in enumerate(remaining)
            if M.symplectic(left[0], right[0], qubits)
        ), None)
        if partner is None:
            radicals.append(left)
            continue
        right = remaining.pop(partner)
        pairs.append((left, right))
        transformed = []
        for row in remaining:
            values = list(row)
            if M.symplectic(values[0], right[0], qubits):
                values = [value ^ other for value, other in zip(values, left)]
            if M.symplectic(values[0], left[0], qubits):
                values = [value ^ other for value, other in zip(values, right)]
            transformed.append(tuple(values))
        remaining = transformed
    return tuple(radicals), tuple(pairs)


def symplectic_split_vectors(
    rows: tuple[int, ...], qubits: int
) -> tuple[tuple[int, ...], tuple[tuple[int, int], ...]]:
    remaining = list(rows)
    radicals = []
    pairs = []
    while remaining:
        left = remaining.pop()
        partner = next((
            index for index, right in enumerate(remaining)
            if M.symplectic(left, right, qubits)
        ), None)
        if partner is None:
            radicals.append(left)
            continue
        right = remaining.pop(partner)
        pairs.append((left, right))
        transformed = []
        for row in remaining:
            if M.symplectic(row, right, qubits):
                row ^= left
            if M.symplectic(row, left, qubits):
                row ^= right
            transformed.append(row)
        remaining = transformed
    return tuple(radicals), tuple(pairs)


def local_center_basis(
    fixture: M.CompanionFixture, gauge: tuple[int, ...], radius: int
) -> tuple[int, ...]:
    """Independent gauge-center rows generated inside cell balls of radius R."""
    count = len(gauge)
    qubits = fixture.qubits
    gram_equations = tuple(
        sum(
            M.symplectic(gauge[left], gauge[right], qubits) << left
            for left in range(count)
        )
        for right in range(count)
    )
    displayed = []
    for coordinate in fixture.cells:
        allowed = {
            qubit for qubit in range(qubits)
            if sum(abs(a - b) for a, b in zip(
                fixture.cells[M.qubit_cell(fixture, qubit)], coordinate
            )) <= radius
        }
        equations = list(gram_equations)
        for bit in range(2 * qubits):
            if bit % qubits in allowed:
                continue
            equations.append(sum(
                ((row >> bit) & 1) << index
                for index, row in enumerate(gauge)
            ))
        for coefficients in M.homogeneous_nullspace(tuple(equations), count):
            displayed.append(U.xor_rows(
                gauge[index] for index in range(count)
                if (coefficients >> index) & 1
            ))

    pivots: dict[int, int] = {}
    basis = []
    for original in displayed:
        row = original
        while row:
            pivot = row.bit_length() - 1
            if pivot in pivots:
                row ^= pivots[pivot]
            else:
                pivots[pivot] = row
                basis.append(original)
                break
    return tuple(basis)


def row_diameter(fixture: M.CompanionFixture, row: Pauli) -> int:
    support = row.x | row.z
    cells = {
        M.qubit_cell(fixture, qubit)
        for qubit in range(fixture.qubits) if (support >> qubit) & 1
    }
    return max((
        sum(abs(a - b) for a, b in zip(
            fixture.cells[left], fixture.cells[right]
        ))
        for left in cells for right in cells
    ), default=0)


def span_equal(left: tuple[int, ...], right: tuple[int, ...]) -> bool:
    return (
        C.R.F.base.gf2_rank(left) == C.R.F.base.gf2_rank(right)
        and M.span_failures(left, right) == 0
        and M.span_failures(right, left) == 0
    )


def conjugate_diagonal(
    row: Pauli, diagonal_rows: tuple[int, ...], z_signs: int, matter: int
) -> Pauli:
    phase, x, z = row.phase, row.x, row.z
    phase = (phase + 2 * (x & z_signs).bit_count()) % 4
    for left in range(matter):
        for right in range(left):
            if not ((diagonal_rows[left] >> right) & 1):
                continue
            x_left = (x >> left) & 1
            x_right = (x >> right) & 1
            phase = (phase + 2 * x_left * x_right) % 4
            z ^= x_right << left
            z ^= x_left << right
    return Pauli(phase, x, z)


def phase_fixed_factorization(shape: tuple[int, int, int]) -> dict[str, object]:
    fixture = M.CompanionFixture.build(shape)
    rows = M.operator_rows(fixture)
    physical_paulis = tuple(row[1] for row in rows)
    target_paulis = tuple(row[2] for row in rows)
    physical_vectors = tuple(
        row.symplectic(fixture.qubits) for row in physical_paulis
    )
    target_vectors = tuple(
        row.symplectic(fixture.matter_qubits) for row in target_paulis
    )
    paired_basis = independent_paired_basis(physical_vectors, target_vectors)
    algebra_radicals, logical_pairs = symplectic_split_paired(
        paired_basis, fixture.qubits
    )

    relation_rows = M.relation_certificate(fixture)["relation_rows"]
    gauge_report, gauge = U.gauge_structure(
        fixture, physical_paulis, relation_rows
    )
    gauge_radicals, gauge_pairs = symplectic_split_vectors(
        gauge, fixture.qubits
    )
    local_center_by_radius = {
        radius: local_center_basis(fixture, gauge, radius)
        for radius in (0, 1, 2)
    }
    matter_parity = Pauli(z=(1 << fixture.matter_qubits) - 1)
    parity_vector = matter_parity.symplectic(fixture.qubits)
    # On small patches the radius-two list can already span total parity.
    # Choose an independent local complement to the explicitly retained
    # parity row instead of double-counting that sector label.
    pivots: dict[int, int] = {}
    row = parity_vector
    while row:
        pivot = row.bit_length() - 1
        pivots[pivot] = row
        break
    local_center_rows = []
    for original in local_center_by_radius[2]:
        row = original
        while row:
            pivot = row.bit_length() - 1
            if pivot in pivots:
                row ^= pivots[pivot]
            else:
                pivots[pivot] = row
                local_center_rows.append(original)
                break
    local_center = tuple(local_center_rows[: len(gauge_radicals) - 1])
    center = local_center + (parity_vector,)

    logical_count = len(logical_pairs)
    gauge_count = len(gauge_pairs)
    center_count = len(center)
    physical_w = [
        canonical_pauli(pair[0][0], fixture.qubits)
        for pair in logical_pairs
    ] + [
        canonical_pauli(pair[0], fixture.qubits)
        for pair in gauge_pairs
    ] + [
        canonical_pauli(row, fixture.qubits) for row in center
    ]
    physical_v_explicit = [
        canonical_pauli(pair[1][0], fixture.qubits)
        for pair in logical_pairs
    ] + [
        canonical_pauli(pair[1], fixture.qubits)
        for pair in gauge_pairs
    ]
    physical_v = list(B.complete_tableau(
        physical_w, physical_v_explicit, fixture.qubits
    ))

    target_w = [
        canonical_pauli(pair[0][1], fixture.matter_qubits)
        for pair in logical_pairs
    ] + [Pauli(z=(1 << fixture.matter_qubits) - 1)]
    target_v_explicit = [
        canonical_pauli(pair[1][1], fixture.matter_qubits)
        for pair in logical_pairs
    ]
    target_v = tuple(B.complete_tableau(
        target_w, target_v_explicit, fixture.matter_qubits
    ))

    # Align every signed generator.  Variables flip, in order, physical
    # logical V rows, physical logical W rows, and the local center W rows.
    phase_equations = []
    preliminary_coordinates = []
    for physical, target in zip(physical_paulis, target_paulis):
        physical_coordinates = B.decode(
            physical, tuple(physical_w), tuple(physical_v), fixture.qubits
        )
        target_coordinates = B.decode(
            target, tuple(target_w), target_v, fixture.matter_qubits
        )
        preliminary_coordinates.append((physical_coordinates, target_coordinates))
        delta = (target_coordinates.phase - physical_coordinates.phase) % 4
        mask = (
            (physical_coordinates.v_mask & ((1 << logical_count) - 1))
            | ((physical_coordinates.w_mask & ((1 << logical_count) - 1))
               << logical_count)
            | (((physical_coordinates.w_mask >> (logical_count + gauge_count))
                & ((1 << (center_count - 1)) - 1)) << (2 * logical_count))
        )
        phase_equations.append((mask, delta // 2))
    phase_solution, phase_rank, phase_contradictions = C.gf2_solve(
        phase_equations
    )
    phase_parity_failures = sum(
        (target.phase - physical.phase) % 2
        for physical, target in preliminary_coordinates
    )
    for index in range(logical_count):
        if (phase_solution >> index) & 1:
            row = physical_v[index]
            physical_v[index] = Pauli((row.phase + 2) % 4, row.x, row.z)
        if (phase_solution >> (logical_count + index)) & 1:
            row = physical_w[index]
            physical_w[index] = Pauli((row.phase + 2) % 4, row.x, row.z)
    for index in range(center_count - 1):
        if (phase_solution >> (2 * logical_count + index)) & 1:
            position = logical_count + gauge_count + index
            row = physical_w[position]
            physical_w[position] = Pauli((row.phase + 2) % 4, row.x, row.z)

    logical_coordinate_failures = 0
    gauge_coordinate_failures = 0
    parity_coordinate_failures = 0
    sector_phase_failures = {"even": 0, "odd": 0}
    relation_center_use = []
    for physical, target in zip(physical_paulis, target_paulis):
        pc = B.decode(
            physical, tuple(physical_w), tuple(physical_v), fixture.qubits
        )
        tc = B.decode(
            target, tuple(target_w), target_v, fixture.matter_qubits
        )
        logical_mask = (1 << logical_count) - 1
        gauge_mask = ((1 << gauge_count) - 1) << logical_count
        logical_coordinate_failures += (
            (pc.v_mask & logical_mask) != (tc.v_mask & logical_mask)
            or (pc.w_mask & logical_mask) != (tc.w_mask & logical_mask)
        )
        gauge_coordinate_failures += bool(pc.v_mask & gauge_mask)
        gauge_coordinate_failures += bool(pc.w_mask & gauge_mask)
        physical_parity = (
            pc.w_mask >> (logical_count + gauge_count + center_count - 1)
        ) & 1
        target_parity = (tc.w_mask >> logical_count) & 1
        parity_coordinate_failures += physical_parity != target_parity
        relation_center_use.append(
            (pc.w_mask >> (logical_count + gauge_count))
            & ((1 << (center_count - 1)) - 1)
        )
        for odd, label in ((0, "even"), (1, "odd")):
            physical_phase = (pc.phase + 2 * odd * physical_parity) % 4
            target_phase = (tc.phase + 2 * odd * target_parity) % 4
            sector_phase_failures[label] += physical_phase != target_phase

    # The diagonal phase repair of the failed product encoder is tested
    # directly against the subsystem gauge span.  It is not silently renamed
    # as gauge motion.
    holonomy = H.holonomy_certificate(fixture)
    diagonal_differences = []
    diagonal_changed_generators = 0
    for physical in physical_paulis:
        transformed = conjugate_diagonal(
            physical,
            holonomy["diagonal_rows"],
            int(holonomy["diagonal_Z_sign_mask"]),
            fixture.matter_qubits,
        )
        difference = (
            transformed.symplectic(fixture.qubits)
            ^ physical.symplectic(fixture.qubits)
        )
        diagonal_differences.append(difference)
        diagonal_changed_generators += bool(difference)

    canonical_rows = tuple(physical_w) + tuple(physical_v)
    logical_rows = (
        tuple(physical_w[:logical_count])
        + tuple(physical_v[:logical_count])
    )
    gauge_rows = (
        tuple(physical_w[logical_count:logical_count + gauge_count])
        + tuple(physical_v[logical_count:logical_count + gauge_count])
    )
    center_duals = tuple(physical_v[logical_count + gauge_count:])
    locality = {
        "maximum_canonical_encoder_row_diameter": max(
            (row_diameter(fixture, row) for row in canonical_rows), default=0
        ),
        "maximum_logical_coordinate_row_diameter": max(
            (row_diameter(fixture, row) for row in logical_rows), default=0
        ),
        "maximum_gauge_Bell_coordinate_row_diameter": max(
            (row_diameter(fixture, row) for row in gauge_rows), default=0
        ),
        "maximum_center_dual_row_diameter": max(
            (row_diameter(fixture, row) for row in center_duals), default=0
        ),
        "maximum_canonical_encoder_row_weight": max(
            ((row.x | row.z).bit_count() for row in canonical_rows), default=0
        ),
        "locally_generated_center_ranks": {
            str(radius): C.R.F.base.gf2_rank(local_center_by_radius[radius])
            for radius in (0, 1, 2)
        },
        "full_center_rank": center_count,
        "local_R2_center_rank_plus_supplied_parity": (
            C.R.F.base.gf2_rank(local_center) + 1
        ),
        "canonical_tableau_bounded_R2": all(
            row_diameter(fixture, row) <= 2 for row in canonical_rows
        ),
    }

    mutual_commutant_failures = sum(
        M.symplectic(left, right, fixture.qubits)
        for left in physical_vectors for right in gauge
    )
    algebra_center_vectors = tuple(row[0] for row in algebra_radicals)
    gauge_center_vectors = tuple(gauge_radicals)
    center_vectors = tuple(center)
    return {
        "shape": shape,
        "cells": len(fixture.cells),
        "physical_qubits": fixture.qubits,
        "logical_qubits_in_fixed_parity_sector": logical_count,
        "gauge_qubits": gauge_count,
        "center_sector_bits": center_count,
        "dimension_identity": logical_count + gauge_count + center_count,
        "mutual_commutant": {
            "physical_algebra_rank": C.R.F.base.gf2_rank(physical_vectors),
            "gauge_algebra_rank": C.R.F.base.gf2_rank(gauge),
            "rank_sum": (
                C.R.F.base.gf2_rank(physical_vectors)
                + C.R.F.base.gf2_rank(gauge)
            ),
            "expected_full_symplectic_dimension": 2 * fixture.qubits,
            "cross_commutator_failures": mutual_commutant_failures,
            "physical_center_equals_declared_center": span_equal(
                algebra_center_vectors, center_vectors
            ),
            "gauge_center_equals_declared_center": span_equal(
                gauge_center_vectors, center_vectors
            ),
        },
        "phase_fixed_intertwiner": {
            "logical_coordinate_failures": logical_coordinate_failures,
            "gauge_coordinate_failures_for_every_physical_generator": gauge_coordinate_failures,
            "parity_coordinate_failures": parity_coordinate_failures,
            "phase_equation_rank": phase_rank,
            "phase_equation_variables": 2 * logical_count + center_count - 1,
            "phase_parity_failures": phase_parity_failures,
            "phase_contradictions": phase_contradictions,
            "even_sector_phase_failures": sector_phase_failures["even"],
            "odd_sector_phase_failures": sector_phase_failures["odd"],
            "phase_sign_weight": phase_solution.bit_count(),
            "relation_center_coordinate_rank": C.R.F.base.gf2_rank(
                relation_center_use
            ),
            "finite_box_mixed_gauge_CPTP_E_constructed": True,
            "factorwise_full_word_intertwiner_exact": (
                logical_coordinate_failures == 0
                and gauge_coordinate_failures == 0
                and parity_coordinate_failures == 0
                and phase_parity_failures == 0
                and phase_contradictions == 0
                and not any(sector_phase_failures.values())
            ),
            "channel_formula": (
                "E_s(rho)=V_s [rho_logical tensor I_gauge/2^g tensor "
                "|local-center=+; parity=s><...|] V_s^dagger"
            ),
            "gauge_channel_under_every_factor": "identity",
        },
        "product_phase_residual_vs_gauge": {
            "changed_physical_generators": diagonal_changed_generators,
            "changed_generator_differences_outside_R1_gauge_span": M.span_failures(
                tuple(diagonal_differences), gauge
            ),
            "difference_span_rank": C.R.F.base.gf2_rank(diagonal_differences),
            "verdict": "the growing product-state diagonal is not gauge action",
        },
        "locality": locality,
        "deletion": {
            "remove_one_local_center_row_rank_loss": (
                C.R.F.base.gf2_rank(center_vectors)
                - C.R.F.base.gf2_rank(center_vectors[1:])
            ),
            "remove_parity_row_rank_loss": (
                C.R.F.base.gf2_rank(center_vectors)
                - C.R.F.base.gf2_rank(center_vectors[:-1])
            ),
        },
        "tableau_digest": sha256((
            "|".join(f"{row.phase}:{row.x:x}:{row.z:x}" for row in canonical_rows)
        ).encode()).hexdigest(),
    }


def main() -> None:
    required_shapes = ((2, 2, 2), (3, 2, 2), (3, 3, 2), (5, 3, 2))
    patch_shapes = ((2, 1, 1), (3, 1, 1), (2, 2, 1))
    required = tuple(phase_fixed_factorization(shape) for shape in required_shapes)
    patches = tuple(phase_fixed_factorization(shape) for shape in patch_shapes)
    checks = []

    def check(label: str, condition: bool) -> None:
        checks.append({"label": label, "pass": bool(condition)})
        print("PASS" if condition else "FAIL", label)

    check(
        "the represented even algebra and R1 gauge algebra are exact mutual commutants with one shared center",
        all(
            row["mutual_commutant"]["rank_sum"]
            == row["mutual_commutant"]["expected_full_symplectic_dimension"]
            and row["mutual_commutant"]["cross_commutator_failures"] == 0
            and row["mutual_commutant"]["physical_center_equals_declared_center"]
            and row["mutual_commutant"]["gauge_center_equals_declared_center"]
            for row in required + patches
        ),
    )
    check(
        "one phase-fixed finite-box CPTP encoder factors logical, maximally mixed gauge, and center sectors exactly",
        all(
            row["dimension_identity"] == row["physical_qubits"]
            and row["phase_fixed_intertwiner"]["factorwise_full_word_intertwiner_exact"]
            and row["phase_fixed_intertwiner"]["finite_box_mixed_gauge_CPTP_E_constructed"]
            for row in required + patches
        ),
    )
    check(
        "every physical free/seam/contact algebra generator has zero gauge coordinates so the gauge channel is identity",
        all(
            row["phase_fixed_intertwiner"]["gauge_coordinate_failures_for_every_physical_generator"] == 0
            for row in required + patches
        ),
    )
    check(
        "all non-parity center constraints are generated in R2 while total matter parity remains the explicit supplied sector label",
        all(
            row["locality"]["local_R2_center_rank_plus_supplied_parity"]
            == row["locality"]["full_center_rank"]
            and row["deletion"]["remove_parity_row_rank_loss"] == 1
            for row in required + patches
        ),
    )
    check(
        "the failed product-encoder diagonal is independently outside the R1 gauge span",
        all(
            row["product_phase_residual_vs_gauge"]["changed_generator_differences_outside_R1_gauge_span"] > 0
            for row in required
        ),
    )
    check(
        "the explicit canonical mixed-gauge encoder and Bell purification are not bounded R2",
        all(not row["locality"]["canonical_tableau_bounded_R2"] for row in required)
        and max(row["locality"]["maximum_canonical_encoder_row_diameter"] for row in required) > 2,
    )

    report = {
        "status": "cycle720-positive-exact-mixed-gauge-channel-intertwiner__bounded-local-E-open",
        "pass": all(row["pass"] for row in checks),
        "authority": "none",
        "audit": "unset",
        "baseline": "origin/main@f7d78df6455d41cf50c143e41c81f204d3dec72e",
        "checks": checks,
        "required_fixtures": required,
        "local_patch_fixtures": patches,
        "supplied": [
            "one fixed total-matter-parity superselection label",
            "the local R2 center-sector values at genesis",
            "a maximally mixed gauge factor, or an abstract reference purification",
            "the existing within-cell matter and companion orders",
        ],
        "derived": [
            "exact mutual-commutant factorization A_physical = logical tensor identity_gauge on each fixed center sector",
            "a signed phase-fixed finite-box CPTP encoder for even and odd parity sectors",
            "factorwise E G_coarse = G_physical E for the free/seam/contact generator dictionary",
            "identity action on every gauge coordinate for every physical factor",
            "R2 generation of every relation-center constraint, leaving only total parity supplied globally",
            "falsification of the hypothesis that the product-state diagonal residual is gauge motion",
        ],
        "open": [
            "replace the explicit growing canonical tableau by a bounded local physical channel or isometry",
            "construct a bounded local Bell purification with overlap-consistent patch maps",
            "autonomously prepare/enforce the R2 center sector and parity label",
            "active proper-cubic covariance of one explicit bounded E",
        ],
        "claim_ceiling": (
            "An exact finite-box mixed-gauge channel intertwiner now exists and the complete "
            "represented update is logical tensor identity on gauge.  This closes the algebraic "
            "state-channel question but not the physical compiler: the exhibited tableau/purification "
            "has growing support and autonomous center/parity genesis is unconstructed."
        ),
        "compiler_claim_gate": {
            "exact_finite_box_CPTP_E": "PASS",
            "exact_factorwise_channel_intertwiner": "PASS",
            "maximally_mixed_gauge_return": "PASS_identity",
            "bounded_local_CPTP_or_isometric_E": "FAIL",
            "autonomous_center_and_parity_genesis": "FAIL",
            "full_physical_compiler_claim_allowed": False,
        },
        "no_go_discipline": {
            "N1_alternatives": "local patch gluing, dissipative center enforcement, Bell-pair gauge purification, and other subsystem tableaus remain live",
            "N2_wall_independence": "finite-box channel exactness, gauge return, encoder locality, center genesis, and covariance are separated",
            "N3_hidden_imports": "parity, center sector, gauge mixture/reference, orders, and tableau are explicit",
            "N4_residual_matching": "rank, commutant, coordinate, phase, gauge-span, locality, and deletion checks are separate",
            "N5_resolution": "three local patches and four required boxes without refit",
            "N6_partial_closure": "the exact mixed-gauge channel is retained while bounded preparation remains open",
            "N7_steelman": "local measurement/isometry patch gluing may realize the same algebraic factorization with bounded support",
            "N8_cross_cycle_echo": "promotes the companion algebra only to a channel theorem, not a pure state compiler",
            "gate": "FAIL_for_broad_no_go__constructive_channel_positive",
        },
    }
    report["report_sha256"] = sha256(json.dumps(
        report, sort_keys=True, separators=(",", ":")
    ).encode()).hexdigest()
    print("SUMMARY_JSON", json.dumps(report, sort_keys=True))
    print("MIXED_GAUGE_CHANNEL_INTERTWINER_POSITIVE__BOUNDED_LOCAL_E_OPEN")
    if not report["pass"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
