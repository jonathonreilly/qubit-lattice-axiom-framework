#!/usr/bin/env python3
"""Transport, onsite-algebra, Fock, polynomial, and factor-census controls.

Ordinary-import helper for the finite flat-link even-CAR support census.  This
module is source-complete in the restricted audit packet; it is not a separate
claim or authority surface.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass
from hashlib import sha256
from itertools import combinations, product
import json
import math

import numpy as np

from frontier_finite_flat_link_even_car_support_census_graph_2026_07_23 import (
    DIRECTIONS,
    FRAME_INDEX,
    FRAMES,
    K,
    Pauli,
    direction_map,
    frame_data,
    link_covariance,
    link_mapping,
    onsite_hopping,
    pauli_pivots,
    pauli_remainder,
    support,
    support_diameter,
    transform_graph_link_pauli,
    transform_pauli,
)


TOL = 2e-11
BETA = -0.3
CONTACT_COUPLING = 0.37
I6 = np.eye(6, dtype=complex)
REVERSE = np.zeros((6, 6), dtype=complex)
REVERSE[np.arange(6), (1, 0, 3, 2, 5, 4)] = 1
UNIFORM = np.ones(6, dtype=complex) / math.sqrt(6)
P_SCALAR = np.outer(UNIFORM, UNIFORM.conj())
P_EVEN = (I6 + REVERSE) / 2 - P_SCALAR
P_VECTOR = (I6 - REVERSE) / 2


def covariance_controls(rows, internals) -> dict:
    mode_maps = tuple(direction_map(frame) for frame in FRAMES)
    mode_group_failures = 0
    for left_index, left in enumerate(FRAMES):
        for right_index, right in enumerate(FRAMES):
            direct = mode_maps[FRAME_INDEX[tuple(int(value) for value in (left @ right).ravel())]]
            mode_group_failures += tuple(
                mode_maps[left_index][mode_maps[right_index][mode]] for mode in range(6)
            ) != direct

    size_rows = []
    total_failures = mode_group_failures
    for row, code in zip(rows, internals):
        length = row["length"]
        graph = code["graph"]
        link = code["link"]
        link_maps = tuple(link_mapping(link, frame, length) for frame in FRAMES)
        B_failures = A_failures = link_dressing_failures = 0
        combined_covariance_executed = length == 3
        combined_local_failures = combined_correlation_failures = 0
        combined_pivots = (
            pauli_pivots(code["combined_constraints"], code["total_qubits"])
            if combined_covariance_executed
            else {}
        )
        for frame, link_map in zip(FRAMES, link_maps):
            data = frame_data(graph, frame)
            for source, generator in enumerate(code["B"]):
                B_failures += transform_pauli(generator, data) != code["B"][data.vertex_map[source]]
            for edge, (source, target, _kind, _owner) in enumerate(graph.base.edges):
                transformed = transform_pauli(graph.mapped_matter_A(edge), data)
                target_edge = graph.base.edge_lookup[frozenset((data.vertex_map[source], data.vertex_map[target]))]
                target_raw = graph.mapped_matter_A(target_edge)
                target_source, target_target, _target_kind, _target_owner = graph.base.edges[target_edge]
                expected_phase = 2 if (data.vertex_map[source], data.vertex_map[target]) == (target_target, target_source) else 0
                expected = Pauli((target_raw.phase + expected_phase) % 4, target_raw.x, target_raw.z)
                A_failures += transformed != expected
                linked = code["A_link"][edge]
                mapped_link = None if linked is None else link_map[linked]
                link_dressing_failures += mapped_link != code["A_link"][target_edge]
            if combined_covariance_executed:
                combined_local_failures += sum(
                    pauli_remainder(
                        transform_graph_link_pauli(
                            generator, data, link_map, code["graph_qubits"]
                        ),
                        combined_pivots,
                        code["total_qubits"],
                    )
                    != Pauli()
                    for generator in code["local_constraints"]
                )
                combined_correlation_failures += sum(
                    pauli_remainder(
                        transform_graph_link_pauli(
                            generator, data, link_map, code["graph_qubits"]
                        ),
                        combined_pivots,
                        code["total_qubits"],
                    )
                    != Pauli()
                    for generator in code["correlation_section"]
                )
        link_control = link_covariance(link, length)
        failures = B_failures + A_failures + link_dressing_failures + int(not link_control["pass"])
        total_failures += failures
        size_rows.append(
            {
                "length": length,
                "B_generator_map_failures": B_failures,
                "oriented_A_map_failures": A_failures,
                "link_dressing_map_failures": link_dressing_failures,
                "combined_code_space_covariance_executed": combined_covariance_executed,
                "combined_local_constraint_span_failures": combined_local_failures if combined_covariance_executed else None,
                "fixed_chart_correlation_span_failures": combined_correlation_failures if combined_covariance_executed else None,
                "fixed_combined_code_space_covariant": (
                    combined_local_failures == combined_correlation_failures == 0
                    if combined_covariance_executed
                    else None
                ),
                "transported_chart_covariant_by_construction": True,
                "link_covariance": link_control,
                "pass": failures == 0,
            }
        )
    return {
        "proper_cubic_frames": len(FRAMES),
        "frame_products": len(FRAMES) ** 2,
        "signed_six_mode_all576_group_failures": mode_group_failures,
        "fixed_chart_combined_code_space_covariant_at_L3": size_rows[0]["fixed_combined_code_space_covariant"],
        "combined_code_space_covariance_sizes": (3,),
        "fixed_chart_invariant_claimed": False,
        "compile_time_chart_transport_supplied": True,
        "size_rows": size_rows,
        "pass": total_failures == 0,
    }


def onsite_even_car_controls(internals) -> dict:
    """Execute the complete 6 B / 15 H onsite incidence algebra and transport."""

    size_rows = []
    total_failures = 0
    for code in internals:
        graph = code["graph"]
        local = code["local_constraints"]
        pivots = pauli_pivots(local, graph.qubits)
        B_square_failures = B_pair_commutator_failures = 0
        H_square_failures = B_H_incidence_failures = H_H_incidence_failures = 0
        H_triangle_on_code_phase_failures = 0
        derived_exact_frame_failures = derived_on_code_frame_failures = 0

        for cell in graph.cells:
            B = tuple(
                graph.B(graph.base.vertex_index[(cell, mode)]) for mode in range(6)
            )
            H = {
                pair: onsite_hopping(graph, cell, *pair)
                for pair in combinations(range(6), 2)
            }
            B_square_failures += sum(row @ row != Pauli() for row in B)
            B_pair_commutator_failures += sum(
                not B[left].commutes(B[right]) for left, right in combinations(range(6), 2)
            )
            H_square_failures += sum(row @ row != Pauli() for row in H.values())
            B_H_incidence_failures += sum(
                B[mode].commutes(row) == (mode in pair)
                for pair, row in H.items()
                for mode in range(6)
            )
            H_H_incidence_failures += sum(
                left_row.commutes(right_row) == (len(set(left_pair) & set(right_pair)) == 1)
                for (left_pair, left_row), (right_pair, right_row) in combinations(H.items(), 2)
            )
            H_triangle_on_code_phase_failures += sum(
                pauli_remainder(
                    H[(left, middle)] @ H[(middle, right)] @ H[(left, right)],
                    pivots,
                    graph.qubits,
                )
                != Pauli(phase=3)
                for left, middle, right in combinations(range(6), 3)
            )

        for frame in FRAMES:
            data = frame_data(graph, frame)
            modes = direction_map(frame)
            # One cell represents the translation orbit; the definitions and
            # frame map are exactly translation-covariant on the periodic torus.
            for cell in (graph.cells[0],):
                target_cell = tuple(
                    int(value % graph.length) for value in frame @ np.asarray(cell)
                )
                for left, right in combinations(range(6), 2):
                    transformed = transform_pauli(
                        onsite_hopping(graph, cell, left, right), data
                    )
                    mapped_left, mapped_right = modes[left], modes[right]
                    target = onsite_hopping(
                        graph,
                        target_cell,
                        min(mapped_left, mapped_right),
                        max(mapped_left, mapped_right),
                    )
                    if mapped_left > mapped_right:
                        target = Pauli((target.phase + 2) % 4, target.x, target.z)
                    difference = transformed @ target
                    derived_exact_frame_failures += difference != Pauli()
                    derived_on_code_frame_failures += (
                        pauli_remainder(difference, pivots, graph.qubits) != Pauli()
                    )

        failures = (
            B_square_failures
            + B_pair_commutator_failures
            + H_square_failures
            + B_H_incidence_failures
            + H_H_incidence_failures
            + H_triangle_on_code_phase_failures
            + derived_on_code_frame_failures
        )
        total_failures += failures
        size_rows.append(
            {
                "length": graph.length,
                "onsite_B_rows": 6 * graph.length**3,
                "onsite_H_rows": 15 * graph.length**3,
                "B_square_failures": B_square_failures,
                "B_pair_commutator_failures": B_pair_commutator_failures,
                "H_square_failures": H_square_failures,
                "B_H_endpoint_incidence_failures": B_H_incidence_failures,
                "H_H_endpoint_incidence_failures": H_H_incidence_failures,
                "H_triangle_minus_i_on_code_failures": H_triangle_on_code_phase_failures,
                "derived_all24_exact_Pauli_failures": derived_exact_frame_failures,
                "derived_all24_on_code_failures": derived_on_code_frame_failures,
                "derived_frame_translation_orbit_representatives": 1,
                "pass": failures == 0,
            }
        )
    return {
        "proper_cubic_frames": len(FRAMES),
        "complete_onsite_bilinears_per_cell": 15,
        "size_rows": size_rows,
        "pass": total_failures == 0,
    }


@dataclass(frozen=True)
class ModeGate:
    kind: str
    sites: tuple[int, ...]
    matrix: tuple[complex, ...]


def common_coin(beta: float = BETA) -> tuple[np.ndarray, float]:
    inertial_mass = float(3 * np.tan(-beta / 2))
    rest_phase = inertial_mass / 3
    coin = np.exp(1j * rest_phase) * (
        P_SCALAR - P_EVEN + np.exp(1j * beta) * P_VECTOR
    )
    return coin, inertial_mass


def one_particle_matrix(gate: ModeGate) -> np.ndarray:
    size = 1 if gate.kind == "phase" else 2
    return np.asarray(gate.matrix, dtype=complex).reshape(size, size)


def compile_adjacent_qr(unitary: np.ndarray):
    work = unitary.copy()
    eliminations = []
    for column in range(5):
        for lower in range(5, column, -1):
            upper = lower - 1
            a = work[upper, column]
            b = work[lower, column]
            if abs(b) < 1e-13:
                continue
            radius = np.sqrt(abs(a) ** 2 + abs(b) ** 2)
            elimination = np.asarray(
                ((np.conj(a) / radius, np.conj(b) / radius), (-b / radius, a / radius)),
                dtype=complex,
            )
            work[[upper, lower], :] = elimination @ work[[upper, lower], :]
            eliminations.append((upper, lower, elimination))
    schedule = []
    for index, phase in enumerate(np.diag(work)):
        if abs(phase - 1) >= 1e-13:
            schedule.append(ModeGate("phase", (index,), (complex(phase),)))
    for upper, lower, elimination in reversed(eliminations):
        schedule.append(ModeGate("givens", (upper, lower), tuple(elimination.conj().T.reshape(-1))))
    reconstructed = np.eye(6, dtype=complex)
    for gate in schedule:
        factor = np.eye(6, dtype=complex)
        factor[np.ix_(gate.sites, gate.sites)] = one_particle_matrix(gate)
        reconstructed = factor @ reconstructed
    return tuple(schedule), {
        "givens": sum(gate.kind == "givens" for gate in schedule),
        "phases": sum(gate.kind == "phase" for gate in schedule),
        "diagonalization_residual": float(np.linalg.norm(work - np.diag(np.diag(work)))),
        "reconstruction_residual": float(np.linalg.norm(reconstructed - unitary)),
        "reconstructed": reconstructed,
    }


def occupied_modes(basis: int, mode_count: int):
    return tuple(mode for mode in range(mode_count) if (basis >> mode) & 1)


def fock_lift(unitary: np.ndarray) -> np.ndarray:
    mode_count = unitary.shape[0]
    dimension = 1 << mode_count
    occupied = tuple(occupied_modes(basis, mode_count) for basis in range(dimension))
    output = np.zeros((dimension, dimension), dtype=complex)
    for target, target_modes in enumerate(occupied):
        for source, source_modes in enumerate(occupied):
            if len(target_modes) != len(source_modes):
                continue
            output[target, source] = 1 if not target_modes else np.linalg.det(
                unitary[np.ix_(target_modes, source_modes)]
            )
    return output


def embedded_gate(gate: ModeGate) -> np.ndarray:
    one_particle = np.eye(6, dtype=complex)
    one_particle[np.ix_(gate.sites, gate.sites)] = one_particle_matrix(gate)
    return fock_lift(one_particle)


def number_sector_leakage(matrix: np.ndarray) -> float:
    numbers = np.asarray([basis.bit_count() for basis in range(matrix.shape[0])])
    forbidden = numbers[:, None] != numbers[None, :]
    return float(np.linalg.norm(matrix[forbidden]))


def local_factor_controls() -> tuple[dict, tuple[ModeGate, ...]]:
    coin, analytic_mass = common_coin()
    schedule, qr = compile_adjacent_qr(coin)
    gamma_coin = fock_lift(coin)
    compiled_coin = np.eye(64, dtype=complex)
    for gate in schedule:
        compiled_coin = embedded_gate(gate) @ compiled_coin

    contact_diagonal = np.asarray(
        [np.exp(1j * CONTACT_COUPLING * basis.bit_count() * (basis.bit_count() - 1) / 2) for basis in range(64)],
        dtype=complex,
    )
    contact = np.diag(contact_diagonal)
    compiled_contact_diagonal = np.ones(64, dtype=complex)
    for left, right in combinations(range(6), 2):
        for basis in range(64):
            if ((basis >> left) & 1) and ((basis >> right) & 1):
                compiled_contact_diagonal[basis] *= np.exp(1j * CONTACT_COUPLING)
    compiled_contact = np.diag(compiled_contact_diagonal)

    reverse_gates = tuple(
        ModeGate("givens", pair, tuple(np.asarray(((0, 1), (1, 0)), dtype=complex).reshape(-1)))
        for pair in ((0, 1), (2, 3), (4, 5))
    )
    compiled_reverse = np.eye(64, dtype=complex)
    for gate in reverse_gates:
        compiled_reverse = embedded_gate(gate) @ compiled_reverse
    direct_reverse = fock_lift(REVERSE)

    # This is a canonical 64-dimensional word reconstruction.  It is not an
    # intertwiner into the graph/link M2 factors: no such E is constructed here.
    direct = contact @ direct_reverse @ gamma_coin
    compiled = compiled_contact @ compiled_reverse @ compiled_coin
    explicit_inverse = np.eye(64, dtype=complex)
    for factor in (
        compiled_contact.conj().T,
        compiled_reverse.conj().T,
        compiled_coin.conj().T,
    ):
        explicit_inverse = factor @ explicit_inverse

    deleted_coin = np.eye(64, dtype=complex)
    for gate in schedule[1:]:
        deleted_coin = embedded_gate(gate) @ deleted_coin
    deleted_contact_diagonal = np.ones(64, dtype=complex)
    deleted_pair = next(iter(combinations(range(6), 2)))
    for left, right in tuple(combinations(range(6), 2))[1:]:
        for basis in range(64):
            if ((basis >> left) & 1) and ((basis >> right) & 1):
                deleted_contact_diagonal[basis] *= np.exp(1j * CONTACT_COUPLING)
    deleted_contact = np.diag(deleted_contact_diagonal)

    scalar_phase = complex(np.vdot(UNIFORM, qr["reconstructed"] @ UNIFORM))
    compiled_mass = float(np.angle(scalar_phase)) / (1 / 3)
    identity = np.eye(64, dtype=complex)
    rows = {
        "QR_Givens": qr["givens"],
        "QR_onsite_phases": qr["phases"],
        "one_particle_reconstruction_residual": qr["reconstruction_residual"],
        "exterior_coin_reconstruction_residual": float(np.linalg.norm(compiled_coin - gamma_coin)),
        "fifteen_contact_reconstruction_residual": float(np.linalg.norm(compiled_contact - contact)),
        "reverse_FSWAP_word_reconstruction_residual": float(np.linalg.norm(compiled_reverse - direct_reverse)),
        "full_M64_ordered_word_reconstruction_residual": float(np.linalg.norm(compiled - direct)),
        "full_M64_word_unitarity_residual": float(np.linalg.norm(compiled.conj().T @ compiled - identity)),
        "full_M64_explicit_inverse_residual": float(np.linalg.norm(explicit_inverse @ compiled - identity)),
        "number_sector_leakage_residual": number_sector_leakage(compiled),
        "compiled_rest_mass": compiled_mass,
        "analytic_mass_fixture": analytic_mass,
        "mass_fixture_residual": abs(compiled_mass - analytic_mass),
        "contact_active_two_particle_states": sum(basis.bit_count() == 2 for basis in range(64)),
        "contact_deletion_residual": float(np.linalg.norm(deleted_contact - contact, ord=2)),
        "expected_contact_deletion_residual": float(abs(np.exp(1j * CONTACT_COUPLING) - 1)),
        "deleted_coin_factor_residual": float(np.linalg.norm(deleted_coin - gamma_coin, ord=2)),
        "deleted_contact_pair": deleted_pair,
    }
    rows["pass"] = bool(
        rows["QR_Givens"] == 10
        and rows["QR_onsite_phases"] == 1
        and rows["one_particle_reconstruction_residual"] < TOL
        and rows["exterior_coin_reconstruction_residual"] < TOL
        and rows["fifteen_contact_reconstruction_residual"] < TOL
        and rows["reverse_FSWAP_word_reconstruction_residual"] < TOL
        and rows["full_M64_ordered_word_reconstruction_residual"] < TOL
        and rows["full_M64_word_unitarity_residual"] < TOL
        and rows["full_M64_explicit_inverse_residual"] < TOL
        and rows["number_sector_leakage_residual"] == 0
        and rows["mass_fixture_residual"] < TOL
        and rows["contact_active_two_particle_states"] == 15
        and abs(rows["contact_deletion_residual"] - rows["expected_contact_deletion_residual"]) < TOL
        and rows["deleted_coin_factor_residual"] > 1e-3
    )
    return rows, schedule


def polynomial_controls(schedule: tuple[ModeGate, ...]) -> dict:
    eye = np.eye(2, dtype=complex)
    x = np.asarray(((0, 1), (1, 0)), dtype=complex)
    y = np.asarray(((0, -1j), (1j, 0)), dtype=complex)
    z = np.diag((1, -1)).astype(complex)
    left_B = np.kron(z, eye)
    right_B = np.kron(eye, z)
    hopping = np.kron(y, x)
    basis = []
    for left, right, active in product((0, 1), repeat=3):
        basis.append(
            (
                f"Bl^{left} Br^{right} A^{active}",
                np.linalg.matrix_power(left_B, left)
                @ np.linalg.matrix_power(right_B, right)
                @ np.linalg.matrix_power(hopping, active),
            )
        )

    def expand(matrix):
        coefficients = tuple(np.trace(row.conj().T @ matrix) / 4 for _name, row in basis)
        rebuilt = sum(
            (value * row for value, (_name, row) in zip(coefficients, basis)),
            np.zeros((4, 4), dtype=complex),
        )
        return coefficients, float(np.linalg.norm(rebuilt - matrix))

    maximum_coin = 0.0
    payload = []
    for gate in schedule:
        if gate.kind == "givens":
            matrix = fock_lift(one_particle_matrix(gate))
            coefficients, residual = expand(matrix)
            maximum_coin = max(maximum_coin, residual)
            payload.append(
                {
                    "sites": gate.sites,
                    "coefficients": tuple(
                        (basis[index][0], value.real.hex(), value.imag.hex())
                        for index, value in enumerate(coefficients)
                    ),
                }
            )

    phase = np.exp(1j * CONTACT_COUPLING)
    contact = np.diag((1, 1, 1, phase)).astype(complex)
    contact_coefficients, contact_residual = expand(contact)
    fswap = fock_lift(np.asarray(((0, 1), (1, 0)), dtype=complex))
    fswap_coefficients, fswap_residual = expand(fswap)
    expected_fswap = {
        "Bl^0 Br^1 A^0": 0.5,
        "Bl^0 Br^1 A^1": -0.5j,
        "Bl^1 Br^0 A^0": 0.5,
        "Bl^1 Br^0 A^1": 0.5j,
    }
    fswap_sign_failures = sum(
        abs(value - expected_fswap.get(name, 0)) > 1e-14
        for value, (name, _row) in zip(fswap_coefficients, basis)
    )
    contact_expected = {
        "Bl^0 Br^0 A^0": (3 + phase) / 4,
        "Bl^0 Br^1 A^0": (1 - phase) / 4,
        "Bl^1 Br^0 A^0": (1 - phase) / 4,
        "Bl^1 Br^1 A^0": (phase - 1) / 4,
    }
    contact_sign_failures = sum(
        abs(value - contact_expected.get(name, 0)) > 1e-14
        for value, (name, _row) in zip(contact_coefficients, basis)
    )
    rows = {
        "maximum_coin_polynomial_reconstruction_residual": maximum_coin,
        "contact_polynomial_reconstruction_residual": contact_residual,
        "FSWAP_polynomial_reconstruction_residual": fswap_residual,
        "contact_exact_coefficient_sign_failures": contact_sign_failures,
        "FSWAP_exact_coefficient_sign_failures": fswap_sign_failures,
        "coin_coefficient_sha256": sha256(json.dumps(payload, sort_keys=True).encode()).hexdigest(),
    }
    rows["pass"] = bool(
        maximum_coin < TOL
        and contact_residual < TOL
        and fswap_residual < TOL
        and contact_sign_failures == fswap_sign_failures == 0
    )
    return rows


def three_mode_gate_controls(schedule: tuple[ModeGate, ...]) -> dict:
    """Catch cancellation of the helper parity in a two-edge onsite path.

    The endpoint modes occupy positions 0 and 2 and the path helper occupies
    position 1.  In little-endian Fock order the correct endpoint bilinear is
    ``Y_2 Z_1 X_0``.  The former extra ``B_helper`` changed it to
    ``Y_2 I_1 X_0``; applying identical polynomial coefficients to that wrong
    bilinear gives an operator-level comparison control.
    """

    eye = np.eye(2, dtype=complex)
    x = np.asarray(((0, 1), (1, 0)), dtype=complex)
    y = np.asarray(((0, -1j), (1j, 0)), dtype=complex)
    z = np.diag((1, -1)).astype(complex)
    left_B = np.kron(np.kron(z, eye), eye)
    helper_B = np.kron(np.kron(eye, z), eye)
    right_B = np.kron(np.kron(eye, eye), z)
    correct_A = np.kron(np.kron(y, z), x)
    cancelled_A = helper_B @ correct_A

    def algebra_basis(active_A):
        return tuple(
            np.linalg.matrix_power(left_B, left)
            @ np.linalg.matrix_power(right_B, right)
            @ np.linalg.matrix_power(active_A, active)
            for left, right, active in product((0, 1), repeat=3)
        )

    correct_basis = algebra_basis(correct_A)
    cancelled_basis = algebra_basis(cancelled_A)

    def residuals(matrix):
        coefficients = tuple(np.trace(row.conj().T @ matrix) / 8 for row in correct_basis)
        correct = sum(
            (coefficient * row for coefficient, row in zip(coefficients, correct_basis)),
            np.zeros((8, 8), dtype=complex),
        )
        cancelled = sum(
            (coefficient * row for coefficient, row in zip(coefficients, cancelled_basis)),
            np.zeros((8, 8), dtype=complex),
        )
        return float(np.linalg.norm(correct - matrix)), float(np.linalg.norm(cancelled - matrix, ord=2))

    reverse_pairs = {(0, 1), (2, 3), (4, 5)}
    tested = []
    for gate in schedule:
        if gate.kind != "givens" or tuple(gate.sites) not in reverse_pairs:
            continue
        one_particle = np.eye(3, dtype=complex)
        one_particle[np.ix_((0, 2), (0, 2))] = one_particle_matrix(gate)
        tested.append(("coin_Givens", gate.sites, *residuals(fock_lift(one_particle))))
    swap = np.eye(3, dtype=complex)
    swap[np.ix_((0, 2), (0, 2))] = np.asarray(((0, 1), (1, 0)), dtype=complex)
    for pair in sorted(reverse_pairs):
        tested.append(("reverse_FSWAP", pair, *residuals(fock_lift(swap))))

    correct = [row[2] for row in tested]
    cancelled = [row[3] for row in tested]
    rows = {
        "three_mode_factors_tested": len(tested),
        "correct_two_edge_maximum_Frobenius_residual": max(correct),
        "extra_helper_B_minimum_operator_residual": min(cancelled),
        "factor_rows": tuple(
            {
                "kind": kind,
                "coarse_modes": pair,
                "correct_Frobenius_residual": good,
                "extra_helper_B_operator_residual": bad,
            }
            for kind, pair, good, bad in tested
        ),
    }
    rows["pass"] = bool(
        rows["three_mode_factors_tested"] == 8
        and rows["correct_two_edge_maximum_Frobenius_residual"] < TOL
        and rows["extra_helper_B_minimum_operator_residual"] > 1e-2
    )
    return rows


def factor_presentation(length: int, code, schedule: tuple[ModeGate, ...]):
    graph = code["graph"]
    B = code["B"]
    A = code["A"]
    factors = []

    def bv(cell, mode):
        return B[graph.base.vertex_index[(cell, mode)]]

    def add(kind, stage, cell, modes, rows):
        mask = 0
        for row in rows:
            mask |= support(row)
        factors.append(
            {
                "kind": kind,
                "stage": stage,
                "cell": cell,
                "modes": modes,
                "support": mask,
                "weight": mask.bit_count(),
            }
        )

    for gate_index, gate in enumerate(schedule):
        for cell in graph.cells:
            if gate.kind == "phase":
                mode = gate.sites[0]
                add("coin_phase", f"coin_{gate_index}", cell, (mode,), (bv(cell, mode),))
            else:
                left, right = gate.sites
                add(
                    "coin_Givens",
                    f"coin_{gate_index}",
                    cell,
                    (left, right),
                    (bv(cell, left), bv(cell, right), onsite_hopping(graph, cell, left, right)),
                )
    for reverse_index, (left, right) in enumerate(((0, 1), (2, 3), (4, 5))):
        for cell in graph.cells:
            add(
                "reverse_FSWAP",
                f"reverse_{reverse_index}",
                cell,
                (left, right),
                (bv(cell, left), bv(cell, right), onsite_hopping(graph, cell, left, right)),
            )
    for edge, (source, target, kind, _owner) in enumerate(graph.base.edges):
        if kind == "outer_square":
            left_cell, left_mode = graph.base.vertices[source]
            _right_cell, right_mode = graph.base.vertices[target]
            add("spatial_FSWAP", "spatial_stream", left_cell, (left_mode, right_mode), (B[source], B[target], A[edge]))
    for contact_index, (left, right) in enumerate(combinations(range(6), 2)):
        for cell in graph.cells:
            add(
                "contact_phase",
                f"contact_{contact_index}",
                cell,
                (left, right),
                (bv(cell, left), bv(cell, right)),
            )

    stages = defaultdict(list)
    for factor in factors:
        stages[factor["stage"]].append(factor)
    palette = total_layers = disjoint_failures = 0
    histogram = Counter()
    for stage in sorted(stages):
        colors = []
        for factor in stages[stage]:
            for color, union in enumerate(colors):
                if not (union & factor["support"]):
                    colors[color] |= factor["support"]
                    factor["color"] = color
                    break
            else:
                factor["color"] = len(colors)
                colors.append(factor["support"])
        palette = max(palette, len(colors))
        total_layers += len(colors)
        histogram[len(colors)] += 1
        by_color = defaultdict(list)
        for factor in stages[stage]:
            by_color[factor["color"]].append(factor["support"])
        for masks in by_color.values():
            union = 0
            for mask in masks:
                disjoint_failures += bool(union & mask)
                union |= mask

    modulus = 2 * K * length
    maximum_diameter = max(
        support_diameter(factor["support"], code["positions"], modulus) for factor in factors
    )
    cells = length**3
    kinds = Counter(factor["kind"] for factor in factors)
    row = {
        "length": length,
        "split": f"L{length}-finite-census",
        "complete_factor_count": len(factors),
        "expected_factor_count": 32 * cells,
        "factor_counts": dict(kinds),
        "ordered_stage_groups": len(stages),
        "finite_color_palette": palette,
        "sequential_color_layers": total_layers,
        "stage_color_count_histogram": dict(histogram),
        "support_disjoint_color_failures": disjoint_failures,
        "maximum_factor_M2_weight": max(factor["weight"] for factor in factors),
        "maximum_factor_fine_L1_diameter": maximum_diameter,
        "constant_overhead_active_algebra_M2_per_cell": 25,
        "factor_order_supplied": True,
        "autonomous_controller_constructed": False,
    }
    row["pass"] = bool(
        len(factors) == 32 * cells
        and kinds
        == {
            "coin_Givens": 10 * cells,
            "coin_phase": cells,
            "reverse_FSWAP": 3 * cells,
            "spatial_FSWAP": 3 * cells,
            "contact_phase": 15 * cells,
        }
        and len(stages) == 30
        and palette <= 7
        and total_layers <= 58
        and disjoint_failures == 0
        and row["maximum_factor_M2_weight"] <= 14
        and maximum_diameter <= 4 * K
    )
    return row
