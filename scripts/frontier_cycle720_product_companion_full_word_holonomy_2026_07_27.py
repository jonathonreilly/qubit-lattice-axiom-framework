#!/usr/bin/env python3
"""Cycle-720 product-companion state encoding and full-word holonomy test.

The cell-Majorana companion representation closes the local even-CAR
subsystem algebra, but that fact alone does not construct a state encoder.
This runner tests the simplest bounded candidate explicitly:

    E_product |psi> = |psi>_matter tensor |000>_companion per cell.

It executes the actual coin/reverse/seam/contact word on sparse vacuum,
one-particle, and two-particle columns.  The companion holonomy is reconstructed
independently from exact Clifford conjugation.  A bounded CNOT reset removes
the companion-bit holonomy, after which the exact residual matter phase is
solved as a diagonal Clifford.  The locality of that required phase repair is
then measured on held and scaling boxes rather than assumed.
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
    "scripts/frontier_cycle720_bounded_general_clifford_orbit_2026_07_27.py",
    "scripts/frontier_cycle720_cell_majorana_companion_geometry_2026_07_27.py",
    "scripts/frontier_cycle720_coherent_cell_edge_gauge_common_e_2026_07_27.py",
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

from collections import Counter
from hashlib import sha256
from itertools import combinations, product
import json
import math

import numpy as np

import frontier_cycle720_cell_majorana_companion_geometry_2026_07_27 as M
import frontier_cycle720_coherent_cell_edge_gauge_common_e_2026_07_27 as C
import frontier_full128_25site_nn_circuit_core_2026_07_24 as S25
import frontier_full128_cycle_encoder_2026_07_24 as F128


Pauli = M.Pauli
TOL = 4.0e-10
SQRT_HALF = 2.0 ** -0.5


def anticommutes(qubits: int, left: Pauli, right: Pauli) -> bool:
    return bool(M.symplectic(
        left.symplectic(qubits), right.symplectic(qubits), qubits
    ))


def conjugate_rotation(qubits: int, generator: Pauli, row: Pauli) -> Pauli:
    """Conjugate by exp(-i*pi*generator/4), including the signed phase."""
    if not anticommutes(qubits, generator, row):
        return row
    result = generator @ row
    return Pauli((result.phase + 3) % 4, result.x, result.z)


def conjugate_cnot(row: Pauli, control: int, target: int) -> Pauli:
    """Conjugate by CNOT(control,target) in i^p X^x Z^z convention."""
    return Pauli(
        row.phase,
        row.x ^ (((row.x >> control) & 1) << target),
        row.z ^ (((row.z >> target) & 1) << control),
    )


def conjugate_word(qubits: int, row: Pauli, word: tuple[Pauli, ...]) -> Pauli:
    for generator in word:
        row = conjugate_rotation(qubits, generator, row)
    return row


def seam_order(fixture: M.CompanionFixture) -> tuple[int, ...]:
    return tuple(sorted(
        range(len(fixture.edges)),
        key=lambda edge: (
            C.R.schedule_colour((
                fixture.edges[edge][2], fixture.edges[edge][3]
            )),
            fixture.edges[edge][2],
            fixture.edges[edge][3],
        ),
    ))


def seam_words(fixture: M.CompanionFixture) -> tuple[tuple[Pauli, ...], tuple[Pauli, ...]]:
    order = seam_order(fixture)
    return (
        tuple(row for edge in order for row in fixture.physical_terms(edge)),
        tuple(row for edge in order for row in fixture.target_terms(edge)),
    )


def support_diameter(fixture: M.CompanionFixture, modes: int) -> int:
    cells = {mode // 6 for mode in range(fixture.matter_qubits) if (modes >> mode) & 1}
    return max((
        sum(abs(a - b) for a, b in zip(fixture.cells[left], fixture.cells[right]))
        for left in cells for right in cells
    ), default=0)


def apply_pauli_sparse(state: dict[int, complex], row: Pauli) -> dict[int, complex]:
    output: dict[int, complex] = {}
    for basis, amplitude in state.items():
        target = basis ^ row.x
        value = amplitude * (1j ** row.phase) * (-1) ** ((row.z & basis).bit_count())
        output[target] = output.get(target, 0.0j) + value
    return output


def apply_rotation_sparse(state: dict[int, complex], row: Pauli) -> dict[int, complex]:
    rotated = apply_pauli_sparse(state, row)
    output = {basis: SQRT_HALF * amplitude for basis, amplitude in state.items()}
    for basis, amplitude in rotated.items():
        output[basis] = output.get(basis, 0.0j) - 1j * SQRT_HALF * amplitude
    return {
        basis: amplitude for basis, amplitude in output.items()
        if abs(amplitude) > 2.0e-13
    }


def apply_gate_sparse(
    state: dict[int, complex], matrix: np.ndarray, wires: tuple[int, ...]
) -> dict[int, complex]:
    """Apply a small dense gate using the repo's little-endian wire convention."""
    output: dict[int, complex] = {}
    local_count = len(wires)
    for basis, amplitude in state.items():
        source = sum(((basis >> wire) & 1) << index for index, wire in enumerate(wires))
        for target in range(1 << local_count):
            coefficient = matrix[target, source]
            if abs(coefficient) < 2.0e-14:
                continue
            changed = basis
            for index, wire in enumerate(wires):
                if (target >> index) & 1:
                    changed |= 1 << wire
                else:
                    changed &= ~(1 << wire)
            output[changed] = output.get(changed, 0.0j) + coefficient * amplitude
    return {
        basis: amplitude for basis, amplitude in output.items()
        if abs(amplitude) > 2.0e-13
    }


def apply_cnot_sparse(
    state: dict[int, complex], control: int, target: int
) -> dict[int, complex]:
    return {
        basis ^ ((((basis >> control) & 1) << target)): amplitude
        for basis, amplitude in state.items()
    }


def state_residual(left: dict[int, complex], right: dict[int, complex]) -> float:
    return float(math.sqrt(sum(
        abs(left.get(basis, 0.0j) - right.get(basis, 0.0j)) ** 2
        for basis in set(left) | set(right)
    )))


def holonomy_certificate(fixture: M.CompanionFixture) -> dict[str, object]:
    matter = fixture.matter_qubits
    qubits = fixture.qubits
    matter_mask = (1 << matter) - 1
    physical_word, target_word = seam_words(fixture)

    reset_cnots: list[tuple[int, int]] = []
    raw_product_stabilizer_failures = 0
    holonomy_form_failures = 0
    holonomy_weights = []
    holonomy_diameters = []
    for auxiliary in range(qubits - matter):
        bit = matter + auxiliary
        image = conjugate_word(qubits, Pauli(z=1 << bit), physical_word)
        matter_holonomy = image.z & matter_mask
        raw_product_stabilizer_failures += image != Pauli(z=1 << bit)
        holonomy_form_failures += (
            image.phase != 0
            or image.x != 0
            or (image.z >> matter) != (1 << auxiliary)
        )
        holonomy_weights.append(matter_holonomy.bit_count())
        holonomy_diameters.append(support_diameter(fixture, matter_holonomy))
        reset_cnots.extend(
            (mode, bit) for mode in range(matter)
            if (matter_holonomy >> mode) & 1
        )

    def corrected_physical(row: Pauli) -> Pauli:
        row = conjugate_word(qubits, row, physical_word)
        for control, target in reset_cnots:
            row = conjugate_cnot(row, control, target)
        return row

    stabilizer_return_failures = sum(
        corrected_physical(Pauli(z=1 << (matter + auxiliary)))
        != Pauli(z=1 << (matter + auxiliary))
        for auxiliary in range(qubits - matter)
    )

    z_action_failures = 0
    x_permutation_failures = 0
    auxiliary_x_leakage = 0
    diagonal_rows = [0] * matter
    phase_by_output = [0] * matter
    auxiliary_z_by_output = [0] * matter
    for mode in range(matter):
        physical_z = corrected_physical(Pauli(z=1 << mode))
        target_z = conjugate_word(matter, Pauli(z=1 << mode), target_word)
        z_action_failures += physical_z != target_z

        physical_x = corrected_physical(Pauli(x=1 << mode))
        target_x = conjugate_word(matter, Pauli(x=1 << mode), target_word)
        x_permutation_failures += (
            (physical_x.x & matter_mask) != target_x.x
            or physical_x.x >> matter != 0
        )
        auxiliary_x_leakage += (physical_x.x >> matter).bit_count()
        output_mode = target_x.x.bit_length() - 1
        diagonal_rows[output_mode] = (physical_x.z ^ target_x.z) & matter_mask
        phase_by_output[output_mode] = (target_x.phase - physical_x.phase) % 4
        auxiliary_z_by_output[output_mode] = physical_x.z >> matter

    symmetry_failures = sum(
        ((diagonal_rows[left] >> right) & 1)
        != ((diagonal_rows[right] >> left) & 1)
        for left in range(matter) for right in range(left)
    )
    phase_parity_failures = 0
    z_sign_mask = 0
    for mode, row in enumerate(diagonal_rows):
        difference = (phase_by_output[mode] - ((row >> mode) & 1)) % 4
        phase_parity_failures += difference & 1
        if difference // 2:
            z_sign_mask |= 1 << mode

    cz_edges = tuple(
        (left, right)
        for left in range(matter) for right in range(left)
        if (diagonal_rows[left] >> right) & 1
    )
    cz_distance_census = Counter(
        sum(abs(a - b) for a, b in zip(
            fixture.cells[left // 6], fixture.cells[right // 6]
        ))
        for left, right in cz_edges
    )

    # Independently apply the solved diagonal Clifford to every logical Pauli
    # generator.  Auxiliary Z factors are legal only because |0...0> is the
    # explicitly declared product-state range.
    exact_x_action_failures = 0
    for mode in range(matter):
        row = corrected_physical(Pauli(x=1 << mode))
        output_mode = row.x.bit_length() - 1
        diagonal = diagonal_rows[output_mode]
        row = Pauli(
            (row.phase + ((diagonal >> output_mode) & 1)
             + 2 * ((z_sign_mask >> output_mode) & 1)) % 4,
            row.x,
            row.z ^ diagonal,
        )
        target = conjugate_word(matter, Pauli(x=1 << mode), target_word)
        exact_x_action_failures += (
            (row.phase, row.x & matter_mask, row.z & matter_mask)
            != (target.phase, target.x, target.z)
            or row.x >> matter != 0
        )

    return {
        "raw_product_stabilizer_failures": raw_product_stabilizer_failures,
        "auxiliary_qubits": qubits - matter,
        "holonomy_form_failures": holonomy_form_failures,
        "minimum_holonomy_matter_weight": min(holonomy_weights, default=0),
        "maximum_holonomy_matter_weight": max(holonomy_weights, default=0),
        "maximum_holonomy_cell_diameter": max(holonomy_diameters, default=0),
        "bounded_reset_CNOTs": len(reset_cnots),
        "bounded_reset_maximum_cell_diameter": max(holonomy_diameters, default=0),
        "stabilizer_return_failures_after_reset": stabilizer_return_failures,
        "logical_Z_action_failures_after_reset": z_action_failures,
        "logical_X_permutation_failures_after_reset": x_permutation_failures,
        "logical_X_auxiliary_X_leakage": auxiliary_x_leakage,
        "diagonal_phase_matrix_symmetry_failures": symmetry_failures,
        "diagonal_phase_solve_parity_failures": phase_parity_failures,
        "exact_logical_X_action_failures_after_diagonal_repair": exact_x_action_failures,
        "required_diagonal_CZ_gates": len(cz_edges),
        "required_diagonal_Z_gates": z_sign_mask.bit_count(),
        "required_diagonal_CZ_distance_census": dict(sorted(cz_distance_census.items())),
        "required_diagonal_CZ_maximum_cell_distance": max(cz_distance_census, default=0),
        "required_diagonal_CZ_beyond_R2": sum(
            count for distance, count in cz_distance_census.items() if distance > 2
        ),
        "maximum_diagonal_row_weight": max(
            (row.bit_count() for row in diagonal_rows), default=0
        ),
        "reset_CNOTs": tuple(reset_cnots),
        "diagonal_rows": tuple(diagonal_rows),
        "diagonal_Z_sign_mask": z_sign_mask,
        "auxiliary_Z_by_output": tuple(auxiliary_z_by_output),
        "diagonal_digest": sha256(
            ("|".join(f"{row:x}" for row in diagonal_rows)
             + f"|z={z_sign_mask:x}").encode()
        ).hexdigest(),
    }


def full_word_sparse_certificate(
    fixture: M.CompanionFixture, holonomy: dict[str, object]
) -> dict[str, object]:
    matter = fixture.matter_qubits
    matter_mask = (1 << matter) - 1
    coin, _mass, _phase = F128.common_coin()
    coin_schedule, _qr = S25.compile_adjacent_qr(coin)
    contact = np.diag((1, 1, 1, np.exp(1j * F128.CONTACT))).astype(complex)
    order = seam_order(fixture)

    selected_cells = tuple(dict.fromkeys((0, len(fixture.cells) // 2, len(fixture.cells) - 1)))
    columns = [0]
    for cell in selected_cells:
        columns.extend(1 << (6 * cell + mode) for mode in range(6))
    for left, right in combinations(range(6), 2):
        columns.append((1 << left) | (1 << right))
    if fixture.edges:
        left, right, _owner, _axis, left_mode, right_mode = fixture.edges[len(fixture.edges) // 2]
        columns.append((1 << left_mode) | (1 << right_mode))
        columns.append(1 << left_mode)
    columns = tuple(dict.fromkeys(columns))

    reset_cnots = holonomy["reset_CNOTs"]
    diagonal_rows = holonomy["diagonal_rows"]
    z_sign_mask = int(holonomy["diagonal_Z_sign_mask"])
    cz_edges = tuple(
        (left, right)
        for left in range(matter) for right in range(left)
        if (diagonal_rows[left] >> right) & 1
    )

    def execute(initial: int, physical: bool) -> dict[int, complex]:
        state = {initial: 1.0 + 0.0j}
        for cell in range(len(fixture.cells)):
            offset = 6 * cell
            for _kind, wires, matrix in coin_schedule:
                state = apply_gate_sparse(
                    state, matrix, tuple(offset + wire for wire in wires)
                )
        for cell in range(len(fixture.cells)):
            offset = 6 * cell
            for left, right in ((0, 1), (2, 3), (4, 5)):
                state = apply_gate_sparse(
                    state, S25.FSWAP, (offset + left, offset + right)
                )
        for edge in order:
            terms = fixture.physical_terms(edge) if physical else fixture.target_terms(edge)
            for row in terms:
                state = apply_rotation_sparse(state, row)
        for cell in range(len(fixture.cells)):
            offset = 6 * cell
            for left, right in combinations(range(6), 2):
                state = apply_gate_sparse(
                    state, contact, (offset + left, offset + right)
                )
        return state

    raw_gauge_return_failures = 0
    post_reset_state_residuals = []
    repaired_state_residuals = []
    maximum_sparse_width = 0
    for initial in columns:
        physical = execute(initial, True)
        target = execute(initial, False)
        maximum_sparse_width = max(maximum_sparse_width, len(physical), len(target))
        raw_gauge_return_failures += any(basis >> matter for basis in physical)

        reset = physical
        for control, target_auxiliary in reset_cnots:
            reset = apply_cnot_sparse(reset, control, target_auxiliary)
        stripped = {
            basis & matter_mask: amplitude
            for basis, amplitude in reset.items() if basis >> matter == 0
        }
        leaked_norm = math.sqrt(sum(
            abs(amplitude) ** 2 for basis, amplitude in reset.items()
            if basis >> matter
        ))
        post_reset_state_residuals.append(
            math.sqrt(state_residual(stripped, target) ** 2 + leaked_norm ** 2)
        )

        repaired: dict[int, complex] = {}
        for basis, amplitude in reset.items():
            matter_basis = basis & matter_mask
            phase_exponent = (
                (z_sign_mask & matter_basis).bit_count()
                + sum(
                    ((matter_basis >> left) & 1) * ((matter_basis >> right) & 1)
                    for left, right in cz_edges
                )
            ) & 1
            repaired[matter_basis] = repaired.get(matter_basis, 0.0j) + (
                (-1) ** phase_exponent * amplitude
            )
        repaired_state_residuals.append(state_residual(repaired, target))

    return {
        "sparse_basis_columns": len(columns),
        "column_classes": "vacuum + selected all-port one-particle + onsite pairs + seam pair",
        "maximum_sparse_state_width": maximum_sparse_width,
        "raw_product_gauge_return_failed_columns": raw_gauge_return_failures,
        "maximum_state_residual_after_bounded_gauge_reset": max(
            post_reset_state_residuals, default=0.0
        ),
        "maximum_state_residual_after_exact_diagonal_repair": max(
            repaired_state_residuals, default=0.0
        ),
        "exact_repaired_columns": sum(
            residual < TOL for residual in repaired_state_residuals
        ),
    }


def fixture_certificate(shape: tuple[int, int, int], sparse: bool) -> dict[str, object]:
    fixture = M.CompanionFixture.build(shape)
    holonomy = holonomy_certificate(fixture)
    report = {
        "shape": shape,
        "cells": len(fixture.cells),
        "matter_modes": fixture.matter_qubits,
        "companion_qubits": fixture.qubits - fixture.matter_qubits,
        "holonomy": {
            key: value for key, value in holonomy.items()
            if key not in (
                "reset_CNOTs", "diagonal_rows", "diagonal_Z_sign_mask",
                "auxiliary_Z_by_output",
            )
        },
    }
    if sparse:
        report["full_word_sparse"] = full_word_sparse_certificate(fixture, holonomy)
    return report


def main() -> None:
    required_shapes = ((2, 2, 2), (3, 2, 2), (3, 3, 2), (5, 3, 2))
    scaling_shapes = ((4, 4, 3), (5, 5, 4))
    required = tuple(fixture_certificate(shape, True) for shape in required_shapes)
    scaling = tuple(fixture_certificate(shape, False) for shape in scaling_shapes)
    checks = []

    def check(label: str, condition: bool) -> None:
        checks.append({"label": label, "pass": bool(condition)})
        print("PASS" if condition else "FAIL", label)

    check(
        "the uncorrected per-cell |000> companion product state fails active gauge return",
        all(
            row["holonomy"]["raw_product_stabilizer_failures"]
            == row["companion_qubits"]
            and row["full_word_sparse"]["raw_product_gauge_return_failed_columns"] > 0
            for row in required
        ),
    )
    check(
        "the exact companion holonomy is bounded and a local matter-to-companion CNOT layer returns every product stabilizer",
        all(
            row["holonomy"]["holonomy_form_failures"] == 0
            and row["holonomy"]["maximum_holonomy_cell_diameter"] <= 2
            and row["holonomy"]["stabilizer_return_failures_after_reset"] == 0
            for row in required + scaling
        ),
    )
    check(
        "after bounded gauge reset the matter permutation is exact and the residual is an independently solved diagonal Clifford",
        all(
            row["holonomy"]["logical_Z_action_failures_after_reset"] == 0
            and row["holonomy"]["logical_X_permutation_failures_after_reset"] == 0
            and row["holonomy"]["logical_X_auxiliary_X_leakage"] == 0
            and row["holonomy"]["diagonal_phase_matrix_symmetry_failures"] == 0
            and row["holonomy"]["diagonal_phase_solve_parity_failures"] == 0
            and row["holonomy"]["exact_logical_X_action_failures_after_diagonal_repair"] == 0
            for row in required + scaling
        ),
    )
    check(
        "the complete coin/reverse/seam/contact word agrees on sparse columns only after the exact diagonal repair",
        all(
            row["full_word_sparse"]["maximum_state_residual_after_exact_diagonal_repair"] < TOL
            and row["full_word_sparse"]["exact_repaired_columns"]
            == row["full_word_sparse"]["sparse_basis_columns"]
            for row in required
        ),
    )
    check(
        "the required diagonal repair is not an R<=2 repair in this product-state route and grows on scaling boxes",
        all(row["holonomy"]["required_diagonal_CZ_beyond_R2"] > 0 for row in required)
        and scaling[-1]["holonomy"]["required_diagonal_CZ_maximum_cell_distance"]
        > required[-1]["holonomy"]["required_diagonal_CZ_maximum_cell_distance"]
        and scaling[-1]["holonomy"]["maximum_diagonal_row_weight"]
        > required[-1]["holonomy"]["maximum_diagonal_row_weight"],
    )
    check(
        "the bounded product-state compiler is rejected by an active unrepaired state residual and nonlocal phase gate",
        all(
            row["full_word_sparse"]["maximum_state_residual_after_bounded_gauge_reset"]
            > 1e-3
            and row["full_word_sparse"]["maximum_state_residual_after_exact_diagonal_repair"]
            < TOL
            and row["holonomy"]["required_diagonal_CZ_beyond_R2"] > 0
            for row in required
        ),
    )

    public_required = required
    report = {
        "status": "cycle720-product-companion-E-falsified__bounded-holonomy-reset-positive__nonlocal-phase-repair",
        "pass": all(row["pass"] for row in checks),
        "authority": "none",
        "audit": "unset",
        "baseline": "origin/main@f7d78df6455d41cf50c143e41c81f204d3dec72e",
        "checks": checks,
        "required_fixtures": public_required,
        "scaling_stress_fixtures": scaling,
        "supplied": [
            "the fixed total-parity sector used by the parent subsystem construction",
            "three companion qubits per cell initialized in |000>",
            "the existing within-cell matter and companion Majorana order",
            "the fixed checkerboard seam schedule; it is not physical time",
            "Cycle219 coin and Cycle230 contact parameters",
        ],
        "derived": [
            "the exact active companion Z-stabilizer holonomy of the full seam layer",
            "a bounded radius-two matter-to-companion CNOT gauge-return layer",
            "exact matter occupation transport after that bounded reset",
            "the unique symmetric diagonal Clifford needed to match the target JW state action",
            "exact sparse-column full-word agreement after applying that diagonal Clifford",
        ],
        "open": [
            "a bounded replacement for the growing diagonal state-phase repair",
            "a different entangled local gauge preparation whose full-word holonomy cancels",
            "autonomous gauge genesis/repair and coherent parity transport",
            "active proper-cubic operator covariance",
        ],
        "claim_ceiling": (
            "The simplest per-cell product companion encoder is falsified.  Its active gauge-bit "
            "holonomy is exactly bounded and reset locally, but exact target-state phases require "
            "a diagonal Clifford whose range and row weight grow on scaling boxes.  This is a "
            "route-specific state-encoding failure, not a no-go for the local subsystem code."
        ),
        "compiler_claim_gate": {
            "local_subsystem_algebra": "PASS_in_parent_runner",
            "product_companion_gauge_return_without_repair": "FAIL",
            "bounded_companion_holonomy_reset": "PASS",
            "bounded_target_phase_repair": "FAIL",
            "full_product_state_compiler_claim_allowed": False,
        },
        "no_go_discipline": {
            "N1_alternatives": "entangled local gauge states, subsystem encoders, Pin(6) coframes, Euler/BKSF routes, and recurrent gauge cycles remain live",
            "N2_wall_independence": "bounded gauge-bit return closes while target state-phase locality fails",
            "N3_hidden_imports": "product state, parity sector, local orders, schedule, and parameters are explicit",
            "N4_residual_matching": "stabilizer, Pauli-action, sparse-state, phase-solve, and locality residuals are separate",
            "N5_resolution": "four required boxes plus 4x4x3 and 5x5x4 scaling stress without refit",
            "N6_partial_closure": "bounded holonomy reset is retained despite failure of the full product E",
            "N7_steelman": "a bounded entangled gauge state or full-cycle gauge Clifford can cancel the phase holonomy",
            "N8_cross_cycle_echo": "tests the Cycle658 companion geometry at the state level rather than repeating algebraic Gram checks",
            "gate": "FAIL_for_broad_no_go__one_explicit_product-state_route_only",
        },
    }
    report["report_sha256"] = sha256(json.dumps(
        report, sort_keys=True, separators=(",", ":")
    ).encode()).hexdigest()
    print("SUMMARY_JSON", json.dumps(report, sort_keys=True))
    print("PRODUCT_COMPANION_STATE_E_FALSIFIED__BOUNDED_HOLONOMY_RESET_POSITIVE")
    if not report["pass"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
