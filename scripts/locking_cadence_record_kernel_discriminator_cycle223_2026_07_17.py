#!/usr/bin/env python3
"""Cycle 223: discriminate coherent pointers, dephasing, and read/reset cadence.

Apply rank-one squared-modulus kernels to the supplied Cycle-222 proper-cubic
coin. The probe distinguishes coherent pointer correlation from an explicit
dephasing channel modeled as a retained archive, tests whether
``B(U^n)=|U^n|^2`` composes as one
tickwise Markov law, and measures what per-tick read/reset does to phase,
propagation, force response, and the previously calibrated mass coordinate.

The squared-modulus weights, pointer frame, archive channel, and cadence are
all supplied diagnostic structure.  This runner neither derives a Record,
outcome selection, Born frequencies, a clock, nor an axiom change.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import numpy as np

import conditional_flavor_mass_operator_compiler_cycle222_2026_07_17 as c222
import generated_beta_phase_register_cycle220_2026_07_16 as c220
import proper_cubic_bound_object_equivalence_cycle210_2026_07_16 as c210


ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "LOCKING_CADENCE_RECORD_KERNEL_DISCRIMINATOR_CYCLE223_NOTE_2026-07-17.md"
)
THEOREM_NOTE = (
    ROOT
    / "docs/"
    "READ_RESET_CADENCE_INTERFERENCE_CHANNEL_BOUNDED_THEOREM_NOTE_2026-07-17.md"
)

PASS = 0
FAIL = 0


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def note_contract() -> None:
    text = " ".join(NOTE.read_text(encoding="utf-8").lower().split())
    theorem_text = " ".join(
        THEOREM_NOTE.read_text(encoding="utf-8").lower().split()
    )
    required = (
        "bounded channel discriminator",
        "one and two coherent pointer copies induce the same reduced channel",
        "separately supplied nonselective dephasing",
        "cadence is operationally consequential in this protocol",
        "rank-one mass-position-direction frame is supplied",
        "squared-modulus weights are supplied",
        "a rank-one read/reset after every tick is exactly blind to the diagonal force phase",
        "does not derive a clock",
        "does not derive a record",
        "cycle-200 remains open",
        "n1",
        "n8",
        "broad record-only no-go fails",
        "global novelty has not been established",
        "audit unset",
        "no axiom conclusion",
        "draft pr #5389",
    )
    theorem_required = (
        "claim type:** bounded_theorem",
        "exact cadence-defect identity",
        "all-time closure criterion",
        "does not derive an instrument, record, occurrence rule, clock, mass law, or axiom content",
        "audit unset",
        "supports no axiom conclusion",
    )
    missing = tuple(phrase for phrase in required if phrase not in text) + tuple(
        phrase for phrase in theorem_required if phrase not in theorem_text
    )
    check("note preserves the bounded claim and all supplied-content walls", not missing, missing)


def born_kernel(unitary: np.ndarray) -> np.ndarray:
    """Column-stochastic transition weights in the declared rank-one frame."""
    return np.abs(np.asarray(unitary, dtype=complex)) ** 2


def semigroup_defect(unitary: np.ndarray, first: int, second: int) -> np.ndarray:
    left = np.linalg.matrix_power(unitary, first)
    right = np.linalg.matrix_power(unitary, second)
    return born_kernel(left @ right) - born_kernel(left) @ born_kernel(right)


def interference_defect(unitary: np.ndarray, first: int, second: int) -> np.ndarray:
    left = np.linalg.matrix_power(unitary, first)
    right = np.linalg.matrix_power(unitary, second)
    paths = np.einsum("ik,kj->ikj", left, right, optimize=True)
    coherent = np.abs(np.sum(paths, axis=1)) ** 2
    incoherent = np.sum(np.abs(paths) ** 2, axis=1)
    return coherent - incoherent


def kernel_metrics(matrix: np.ndarray) -> dict[str, float]:
    return {
        "max_column_tv": float(0.5 * np.max(np.sum(np.abs(matrix), axis=0))),
        "normalized_frobenius": float(
            np.linalg.norm(matrix) / np.sqrt(matrix.shape[0])
        ),
        "row_residual": float(np.max(np.abs(np.sum(matrix, axis=1)))),
        "column_residual": float(np.max(np.abs(np.sum(matrix, axis=0)))),
    }


def cycle_coefficients(beta: float, tick: int) -> tuple[float, float]:
    even = 1.0 if tick % 2 == 0 else 1 / 3
    vector = np.cos(tick * beta) if tick % 2 == 0 else -np.cos(tick * beta) / 3
    return even, float(vector)


def cycle_kernel_closed(beta: float, tick: int) -> np.ndarray:
    even, vector = cycle_coefficients(beta, tick)
    return c210.P_SCALAR + even * c210.P_EVEN + vector * c210.P_VECTOR


def cycle_defect_closed(beta: float, first: int, second: int) -> np.ndarray:
    even_first, vector_first = cycle_coefficients(beta, first)
    even_second, vector_second = cycle_coefficients(beta, second)
    even_total, vector_total = cycle_coefficients(beta, first + second)
    return (even_total - even_first * even_second) * c210.P_EVEN + (
        vector_total - vector_first * vector_second
    ) * c210.P_VECTOR


@dataclass(frozen=True)
class BlindBlock:
    c3_phase: float
    vector: np.ndarray
    block: np.ndarray


@dataclass(frozen=True)
class PhasedBlock:
    c3_phase: float
    vector: np.ndarray
    block: np.ndarray
    beta: float


def c3_blind_blocks(coin: np.ndarray) -> tuple[BlindBlock, ...]:
    """Extract sectors from C3 characters without reading M or target masses."""
    shift = c222.cyclic_shift_three()
    values, vectors = np.linalg.eig(shift)
    rows = []
    for _, character in zip(values, vectors.T):
        character = character / np.linalg.norm(character)
        pivot = int(np.argmax(np.abs(character)))
        character *= np.exp(-1j * np.angle(character[pivot]))
        vector = np.concatenate((np.zeros(1, dtype=complex), character))
        block = c220.extract_direction_block(coin, vector)
        c3_phase = float(np.angle(np.vdot(character, shift @ character)))
        rows.append(BlindBlock(c3_phase, vector, block))
    return tuple(sorted(rows, key=lambda row: row.c3_phase))


def attach_register_phases(
    blocks: tuple[BlindBlock, ...], register: np.ndarray
) -> tuple[PhasedBlock, ...]:
    """Attach analytic beta labels after the target-unfed blocks are frozen."""
    return tuple(
        PhasedBlock(
            row.c3_phase,
            row.vector,
            row.block,
            float(np.angle(np.vdot(row.vector, register @ row.vector))),
        )
        for row in blocks
    )


def doubly_stochastic(kernel: np.ndarray, tolerance: float = 5e-12) -> bool:
    return (
        np.min(kernel) > -tolerance
        and np.max(np.abs(np.sum(kernel, axis=0) - 1)) < tolerance
        and np.max(np.abs(np.sum(kernel, axis=1) - 1)) < tolerance
    )


def exact_coin_kernel_controls(blocks: tuple[PhasedBlock, ...]) -> None:
    stochastic_errors = []
    cross_term_errors = []
    closed_errors = []
    defect_errors = []
    direction_metrics = []
    eigenbasis_metrics = []
    relabel_errors = []

    spectral_basis_generator = (
        c210.P_SCALAR + 2 * c210.P_EVEN + 3 * c210.P_VECTOR
    )
    _, spectral_basis = np.linalg.eigh(spectral_basis_generator)
    permutation = np.eye(6)[[2, 5, 0, 4, 1, 3]]
    phases = np.diag(np.exp(1j * np.linspace(0.1, 1.1, 6)))
    monomial_basis = permutation @ phases

    for row in blocks:
        for tick in range(1, 13):
            direct = born_kernel(np.linalg.matrix_power(row.block, tick))
            stochastic_errors.append(
                max(
                    np.max(np.abs(np.sum(direct, axis=0) - 1)),
                    np.max(np.abs(np.sum(direct, axis=1) - 1)),
                    max(0.0, -float(np.min(direct))),
                )
            )
            closed_errors.append(
                np.linalg.norm(direct - cycle_kernel_closed(row.beta, tick))
            )
        for first in range(1, 7):
            for second in range(1, 7):
                direct_defect = semigroup_defect(row.block, first, second)
                cross_term_errors.append(
                    np.linalg.norm(
                        direct_defect
                        - interference_defect(row.block, first, second)
                    )
                )
                defect_errors.append(
                    np.linalg.norm(
                        direct_defect
                        - cycle_defect_closed(row.beta, first, second)
                    )
                )

        direction_defect = semigroup_defect(row.block, 1, 1)
        direction_metrics.append(kernel_metrics(direction_defect))
        diagonal = spectral_basis.conj().T @ row.block @ spectral_basis
        eigenbasis_metrics.append(
            kernel_metrics(semigroup_defect(diagonal, 1, 1))
        )
        represented = monomial_basis.conj().T @ row.block @ monomial_basis
        relabel_errors.append(
            np.linalg.norm(
                semigroup_defect(represented, 1, 1)
                - permutation.T @ direction_defect @ permutation
            )
        )

    check(
        "all declared coin kernels are entrywise nonnegative and doubly stochastic",
        max(stochastic_errors) < 5e-12,
        max(stochastic_errors),
    )
    check(
        "the semigroup defect is exactly the deleted path-interference cross term",
        max(cross_term_errors) < 5e-12,
        max(cross_term_errors),
    )
    check(
        "the Cycle-222 sector kernels and defects obey the closed projector formula",
        max(closed_errors) < 5e-11 and max(defect_errors) < 5e-11,
        {"kernel": max(closed_errors), "defect": max(defect_errors)},
    )
    check(
        "the direction-frame one-plus-one defect is large in every massive sector",
        min(row["max_column_tv"] for row in direction_metrics) > 0.6
        and max(row["row_residual"] for row in direction_metrics) < 2e-12
        and max(row["column_residual"] for row in direction_metrics) < 2e-12,
        direction_metrics,
    )
    check(
        "the same unitary has a vacuous Markov closure in its supplied eigenbasis",
        max(row["normalized_frobenius"] for row in eigenbasis_metrics) < 1e-10,
        eigenbasis_metrics,
    )
    check(
        "monomial relabeling and rephasing preserve the exact defect",
        max(relabel_errors) < 2e-12,
        relabel_errors,
    )

    rng = np.random.default_rng(22301)
    raw = rng.normal(size=(6, 6)) + 1j * rng.normal(size=(6, 6))
    haar, upper = np.linalg.qr(raw)
    diagonal = np.diag(upper)
    haar = haar @ np.diag(diagonal / np.abs(diagonal))
    haar_defect = semigroup_defect(haar, 2, 3)
    forward_kernel_order = (
        born_kernel(np.linalg.matrix_power(haar, 2))
        @ born_kernel(np.linalg.matrix_power(haar, 3))
    )
    reverse_kernel_order = (
        born_kernel(np.linalg.matrix_power(haar, 3))
        @ born_kernel(np.linalg.matrix_power(haar, 2))
    )
    haar_cross_error = np.linalg.norm(
        haar_defect - interference_defect(haar, 2, 3)
    )
    order_difference = np.linalg.norm(
        forward_kernel_order - reverse_kernel_order
    )
    check(
        "a seeded Haar control has noncommuting induced K2 and K3 kernels",
        haar_cross_error < 5e-12 and order_difference > 0.1,
        {
            "cross_term_error": float(haar_cross_error),
            "order_difference": float(order_difference),
        },
    )

    odd_lower_bounds = []
    classification_errors = []
    remaining_classification_errors = []
    for row in blocks:
        for first in range(1, 12, 2):
            for second in range(1, 12, 2):
                defect = cycle_defect_closed(row.beta, first, second)
                odd_lower_bounds.append(np.linalg.norm(defect))
                even_first, vector_first = cycle_coefficients(row.beta, first)
                even_second, vector_second = cycle_coefficients(row.beta, second)
                even_total, vector_total = cycle_coefficients(
                    row.beta, first + second
                )
                classification_errors.append(abs(even_total - even_first * even_second - 8 / 9))
        for first in range(1, 12):
            for second in range(1, 12):
                if first % 2 and second % 2:
                    continue
                _, vector_first = cycle_coefficients(row.beta, first)
                _, vector_second = cycle_coefficients(row.beta, second)
                _, vector_total = cycle_coefficients(row.beta, first + second)
                total_is_odd = bool((first + second) % 2)
                scale = 1 / 3 if total_is_odd else 1.0
                expected = (
                    scale * np.sin(first * row.beta) * np.sin(second * row.beta)
                )
                remaining_classification_errors.append(
                    abs(
                        vector_total
                        - vector_first * vector_second
                        - expected
                        if total_is_odd
                        else vector_total
                        - vector_first * vector_second
                        + expected
                    )
                )
    check(
        "both intervals odd can never close the Cycle-222 tickwise kernel",
        min(odd_lower_bounds) > 1.0
        and max(classification_errors) < 5e-12
        and max(remaining_classification_errors) < 5e-12,
        {
            "minimum_defect_norm": min(odd_lower_bounds),
            "remaining_parity_identity_error": max(
                remaining_classification_errors
            ),
        },
    )


def cadence_controls(blocks: tuple[PhasedBlock, ...]) -> None:
    total_ticks = 16
    # Cadence 16 is the final-only diagnostic: no intermediate intervention.
    cadences = (1, 2, 4, 8, 16)
    rows = []
    analytic_errors = []
    for block_row in blocks:
        coherent = born_kernel(np.linalg.matrix_power(block_row.block, total_ticks))
        sector_rows = []
        for cadence in cadences:
            repetitions = total_ticks // cadence
            direct = np.linalg.matrix_power(
                born_kernel(np.linalg.matrix_power(block_row.block, cadence)),
                repetitions,
            )
            even, vector = cycle_coefficients(block_row.beta, cadence)
            closed = (
                c210.P_SCALAR
                + even**repetitions * c210.P_EVEN
                + vector**repetitions * c210.P_VECTOR
            )
            analytic_errors.append(np.linalg.norm(direct - closed))
            sector_rows.append(
                (
                    cadence,
                    repetitions,
                    kernel_metrics(coherent - direct)["max_column_tv"],
                )
            )
        rows.append((block_row.c3_phase, block_row.beta, sector_rows))
    check(
        "each cadence schedule agrees with its exact projector-power formula",
        max(analytic_errors) < 1e-10,
        max(analytic_errors),
    )
    check(
        "requested intervention cadences differ from the final-only read",
        all(sector[2][0][2] > 0.6 for sector in rows)
        and all(
            item[2] > 1e-5
            for sector in rows
            for item in sector[2][:-1]
        )
        and all(abs(sector[2][-1][2]) < 2e-12 for sector in rows),
        rows,
    )


def dephase(rho: np.ndarray, projectors: tuple[np.ndarray, ...]) -> np.ndarray:
    return sum((projector @ rho @ projector for projector in projectors), np.zeros_like(rho))


def reduced_system_pure(state: np.ndarray, dimension: int) -> np.ndarray:
    matrix = state.reshape(dimension, -1)
    return matrix @ matrix.conj().T


def reduced_system_density(rho: np.ndarray, dimension: int) -> np.ndarray:
    ancillary_dimension = rho.shape[0] // dimension
    reshaped = rho.reshape(
        dimension, ancillary_dimension, dimension, ancillary_dimension
    )
    return np.einsum("iaja->ij", reshaped, optimize=True)


def purity(rho: np.ndarray) -> float:
    return float(np.trace(rho @ rho).real)


def pointer_archive_and_basis_controls(
    compiled: c222.Compiled, blocks: tuple[BlindBlock, ...]
) -> None:
    dimension = 4
    identity = np.eye(dimension, dtype=complex)
    zero = np.array((1, 0), dtype=complex)
    x_gate = np.array(((0, 1), (1, 0)), dtype=complex)
    first = blocks[0].vector
    second = blocks[1].vector
    psi = (first + 1j * second) / np.sqrt(2)
    projector = np.outer(second, second.conj())
    complement = identity - projector
    projectors = (complement, projector)
    write = np.kron(complement, np.eye(2)) + np.kron(projector, x_gate)
    cnot = np.array(
        ((1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 0, 1), (0, 0, 1, 0)),
        dtype=complex,
    )
    copy = np.kron(identity, cnot)
    one_pointer = write @ np.kron(psi, zero)
    two_pointers = copy @ np.kron(one_pointer, zero)
    expected = dephase(np.outer(psi, psi.conj()), projectors)
    reduced_one = reduced_system_pure(one_pointer, dimension)
    reduced_two = reduced_system_pure(two_pointers, dimension)

    write_first_of_two = (
        np.kron(np.kron(complement, np.eye(2)), np.eye(2))
        + np.kron(np.kron(projector, x_gate), np.eye(2))
    )
    write_second_of_two = (
        np.kron(np.kron(complement, np.eye(2)), np.eye(2))
        + np.kron(np.kron(projector, np.eye(2)), x_gate)
    )
    direct_two_pointers = (
        write_second_of_two
        @ write_first_of_two
        @ np.kron(np.kron(psi, zero), zero)
    )
    erased_one = write.conj().T @ one_pointer
    one_access_two = write_first_of_two.conj().T @ two_pointers
    erased_both = write_first_of_two.conj().T @ copy.conj().T @ two_pointers
    direct_erased_both = (
        write_first_of_two.conj().T
        @ write_second_of_two.conj().T
        @ direct_two_pointers
    )
    target_one = np.kron(psi, zero)
    target_two = np.kron(np.kron(psi, zero), zero)

    check(
        "one and two coherent pointer copies induce the same reduced channel",
        np.linalg.norm(reduced_one - expected) < 3e-12
        and np.linalg.norm(reduced_two - expected) < 3e-12
        and np.linalg.norm(reduced_one - reduced_two) < 3e-12
        and np.linalg.norm(direct_two_pointers - two_pointers) < 3e-12
        and abs(purity(reduced_one) - 0.5) < 3e-12,
        {
            "one_error": float(np.linalg.norm(reduced_one - expected)),
            "two_error": float(np.linalg.norm(reduced_two - expected)),
            "copy_vs_two_direct_writes": float(
                np.linalg.norm(direct_two_pointers - two_pointers)
            ),
            "purity": purity(reduced_one),
        },
    )
    check(
        "modeled write reversal must remove both coherent pointer correlations",
        abs(abs(np.vdot(target_one, erased_one)) ** 2 - 1) < 3e-12
        and np.linalg.norm(reduced_system_pure(one_access_two, dimension) - expected)
        < 3e-12
        and abs(abs(np.vdot(target_two, erased_both)) ** 2 - 1) < 3e-12
        and abs(abs(np.vdot(target_two, direct_erased_both)) ** 2 - 1) < 3e-12,
        {
            "one_pointer_erase_fidelity": float(abs(np.vdot(target_one, erased_one)) ** 2),
            "reverse_first_write_only_system_purity": purity(
                reduced_system_pure(one_access_two, dimension)
            ),
            "reverse_both_modeled_writes_fidelity": float(
                abs(np.vdot(target_two, erased_both)) ** 2
            ),
        },
    )

    # Append an archive bit and explicitly dephase it.  This is an additional
    # nonunitary channel, not a consequence of the second coherent copy.
    append_history = np.kron(np.eye(dimension * 2), cnot)
    coherent_history = append_history @ np.kron(two_pointers, zero)
    rho_history = np.outer(coherent_history, coherent_history.conj())
    history_zero = np.kron(np.eye(dimension * 4), np.diag((1, 0)))
    history_one = np.kron(np.eye(dimension * 4), np.diag((0, 1)))
    archived = dephase(rho_history, (history_zero, history_one))
    reverse_modeled_pointers = (
        np.kron(write_first_of_two.conj().T, np.eye(2))
        @ np.kron(copy.conj().T, np.eye(2))
    )
    reversed_archived = (
        reverse_modeled_pointers
        @ archived
        @ reverse_modeled_pointers.conj().T
    )
    reversed_system = reduced_system_density(reversed_archived, dimension)
    check(
        "the supplied archive channel mixes the modeled pointer-history state",
        abs(purity(np.outer(coherent_history, coherent_history.conj())) - 1) < 3e-12
        and abs(purity(archived) - 0.5) < 3e-12
        and abs(np.trace(archived).real - 1) < 3e-12,
        {
            "coherent_purity": purity(
                np.outer(coherent_history, coherent_history.conj())
            ),
            "archive_purity": purity(archived),
        },
    )
    check(
        "the archive restriction blocks recovery by pointer reversal alone",
        np.linalg.norm(reversed_system - expected) < 3e-12
        and abs(purity(reversed_system) - 0.5) < 3e-12,
        {
            "reversed_reduced_purity": purity(reversed_system),
            "reversed_reduced_error": float(
                np.linalg.norm(reversed_system - expected)
            ),
        },
    )

    mass_expectations = (
        float(np.vdot(psi, compiled.recovered_mass @ psi).real),
        float(
            np.vdot(
                one_pointer,
                np.kron(compiled.recovered_mass, np.eye(2)) @ one_pointer,
            ).real
        ),
        float(
            np.vdot(
                two_pointers,
                np.kron(compiled.recovered_mass, np.eye(4)) @ two_pointers,
            ).real
        ),
        float(
            np.vdot(
                direct_two_pointers,
                np.kron(compiled.recovered_mass, np.eye(4))
                @ direct_two_pointers,
            ).real
        ),
    )
    check(
        "zero one and two coherent pointer writes preserve matter mass expectation",
        max(abs(value - mass_expectations[0]) for value in mass_expectations) < 3e-10,
        mass_expectations,
    )

    mass_values, mass_vectors = np.linalg.eigh(compiled.recovered_mass)
    mass_projectors = tuple(
        np.outer(vector, vector.conj()) for vector in mass_vectors.T
    )
    selected = blocks[0].vector
    selected_rho = np.outer(selected, selected.conj())
    mass_dephased = dephase(selected_rho, mass_projectors)
    coordinate_projectors = tuple(
        np.outer(np.eye(dimension)[index], np.eye(dimension)[index])
        for index in range(dimension)
    )
    coordinate_dephased = dephase(selected_rho, coordinate_projectors)
    weights_before = np.array(
        [np.trace(projector @ selected_rho).real for projector in mass_projectors]
    )
    weights_coordinate = np.array(
        [np.trace(projector @ coordinate_dephased).real for projector in mass_projectors]
    )
    check(
        "mass-frame dephasing preserves a mass sector while coordinate-register dephasing mixes it",
        np.linalg.norm(mass_dephased - selected_rho) < 3e-12
        and 0.5 * np.sum(np.abs(weights_before - weights_coordinate)) > 0.6
        and abs(np.sum(weights_coordinate) - 1) < 3e-12,
        {
            "before": weights_before.tolist(),
            "coordinate_register": weights_coordinate.tolist(),
        },
    )

    rng = np.random.default_rng(223)
    raw = rng.normal(size=(dimension, dimension)) + 1j * rng.normal(
        size=(dimension, dimension)
    )
    basis, _ = np.linalg.qr(raw)
    represented_rho = basis @ selected_rho @ basis.conj().T
    represented_projectors = tuple(
        basis @ projector @ basis.conj().T for projector in mass_projectors
    )
    check(
        "passive co-transformation preserves the supplied dephasing experiment",
        np.linalg.norm(
            dephase(represented_rho, represented_projectors)
            - basis @ mass_dephased @ basis.conj().T
        )
        < 3e-12,
    )


def axis_walk(block: np.ndarray, length: int) -> np.ndarray:
    unitary = np.zeros((6 * length, 6 * length), dtype=complex)
    for position in range(length):
        for old_direction in range(6):
            for new_direction in range(6):
                target = (
                    position + int(c210.DIRECTIONS[new_direction, 0])
                ) % length
                unitary[
                    6 * target + new_direction, 6 * position + old_direction
                ] = block[new_direction, old_direction]
    return unitary


def linear_force(length: int, strength: float) -> np.ndarray:
    positions = np.arange(length, dtype=float) - length // 2
    phases = np.repeat(np.exp(1j * strength * positions), 6)
    return np.diag(phases)


def position_weights(weights: np.ndarray, length: int) -> np.ndarray:
    return np.sum(weights.reshape(length, 6), axis=1)


def full_walk_force_and_coarse_record_controls(
    blocks: tuple[BlindBlock, ...]
) -> None:
    length = 13
    strength = 0.01
    force_rows = []
    response_rows = []
    coarse_rows = []
    boundary_comparators = []
    for row in blocks:
        walk = axis_walk(row.block, length)
        symmetric = linear_force(length, strength / 2) @ walk @ linear_force(
            length, strength / 2
        )
        reverse_symmetric = (
            linear_force(length, -strength / 2)
            @ walk
            @ linear_force(length, -strength / 2)
        )
        cadence_differences = []
        source_columns = np.arange(
            6 * (length // 2), 6 * (length // 2 + 1)
        )
        for cadence in (1, 2, 3, 4):
            unforced_kernel = born_kernel(np.linalg.matrix_power(walk, cadence))
            forced_kernel = born_kernel(
                np.linalg.matrix_power(symmetric, cadence)
            )
            reverse_kernel = born_kernel(
                np.linalg.matrix_power(reverse_symmetric, cadence)
            )
            cadence_differences.append(
                (
                    cadence,
                    float(np.linalg.norm(forced_kernel - unforced_kernel)),
                    float(np.linalg.norm(reverse_kernel - unforced_kernel)),
                    float(
                        np.linalg.norm(
                            (forced_kernel - unforced_kernel)[:, source_columns]
                        )
                    ),
                    float(
                        np.linalg.norm(
                            (reverse_kernel - unforced_kernel)[:, source_columns]
                        )
                    ),
                    doubly_stochastic(unforced_kernel),
                    doubly_stochastic(forced_kernel),
                    doubly_stochastic(reverse_kernel),
                )
            )
        force_rows.append((row.c3_phase, cadence_differences))

        larger_length = 17
        larger_walk = axis_walk(row.block, larger_length)
        larger_force = linear_force(larger_length, strength / 2)
        larger_forced = larger_force @ larger_walk @ larger_force
        larger_columns = np.arange(
            6 * (larger_length // 2), 6 * (larger_length // 2 + 1)
        )
        boundary_comparators.append(
            abs(
                cadence_differences[2][3]
                - np.linalg.norm(
                    (
                        born_kernel(np.linalg.matrix_power(larger_forced, 3))
                        - born_kernel(np.linalg.matrix_power(larger_walk, 3))
                    )[:, larger_columns]
                )
            )
        )

        initial = np.zeros(6 * length)
        initial[6 * (length // 2) : 6 * (length // 2 + 1)] = 1 / 6
        histories = []
        for candidate in (walk, symmetric, reverse_symmetric):
            kernel = born_kernel(candidate)
            weights = initial.copy()
            positions = []
            coordinate = np.arange(length, dtype=float) - length // 2
            for _ in range(9):
                positions.append(
                    float(
                        coordinate
                        @ position_weights(weights, length)
                    )
                )
                weights = kernel @ weights
            histories.append(np.asarray(positions))
        response_rows.append(
            (
                row.c3_phase,
                float(np.max(np.abs(histories[1] - histories[0]))),
                float(np.max(np.abs(histories[2] - histories[0]))),
            )
        )

        centre = length // 2
        first_state = np.zeros(6 * length, dtype=complex)
        second_state = np.zeros(6 * length, dtype=complex)
        first_state[6 * centre] = 1
        second_state[6 * centre + 1] = 1
        first_future = position_weights(np.abs(walk @ first_state) ** 2, length)
        second_future = position_weights(np.abs(walk @ second_state) ** 2, length)
        coarse_rows.append(
            (
                row.c3_phase,
                float(0.5 * np.sum(np.abs(first_future - second_future))),
            )
        )

    check(
        "per-tick rank-one read-reset is blind to the diagonal force phase",
        all(
            sector[1][0][1] < 5e-12
            and sector[1][0][2] < 5e-12
            and sector[1][0][3] < 5e-12
            and sector[1][0][4] < 5e-12
            and all(all(item[5:]) for item in sector[1])
            for sector in force_rows
        ),
        force_rows,
    )
    check(
        "coherent intervals make the force visible before the next intervention",
        all(
            sector[1][2][3] > 1e-6 and sector[1][2][4] > 1e-6
            for sector in force_rows
        )
        and max(boundary_comparators) < 3e-14,
        {"rows": force_rows, "boundary_comparators": boundary_comparators},
    )
    check(
        "a per-tick read-reset has zero odd force response or F-over-a inertia",
        max(max(abs(item) for item in row[1:]) for row in response_rows) < 5e-13,
        response_rows,
    )
    check(
        "a coarse mass-position symbol does not fix the future when direction is hidden",
        min(row[1] for row in coarse_rows) > 0.1,
        coarse_rows,
    )


def tilted_diffusion(kernel: np.ndarray, step: float = 0.005) -> float:
    increments = c210.DIRECTIONS[:, 0].astype(float)
    values = []
    for sign in (-1, 1):
        tilted = np.diag(np.exp(1j * sign * step * increments)) @ kernel
        eigenvalues = np.linalg.eigvals(tilted)
        eigenvalue = eigenvalues[int(np.argmin(np.abs(eigenvalues - 1)))]
        values.append(-float(np.log(eigenvalue).real) / step**2)
    return float(np.mean(values))


def diffusion_and_phase_controls(blocks: tuple[PhasedBlock, ...]) -> None:
    diffusion_rows = []
    sign_errors = []
    global_phase_errors = []
    phase_rows = []
    # One geometry-fixed tester is used unchanged in all sectors: one update
    # from the opposite +x/-x direction pair.
    common_tick = 1
    common_first = 0
    common_second = 1
    for row in blocks:
        kernel = born_kernel(row.block)
        mass_coordinate = float(3 * np.tan(-row.beta / 2))
        analytic = float(
            (2 * mass_coordinate**2 + 9) / (6 * (mass_coordinate**2 + 18))
        )
        numeric = tilted_diffusion(kernel)
        diffusion_rows.append(
            (row.c3_phase, row.beta, mass_coordinate, analytic, numeric)
        )
        baseline = c210.cubic_coin(np.pi, row.beta, 0.37)
        phase_shifted = c210.cubic_coin(np.pi, row.beta, -1.11)
        sign_reversed = c210.cubic_coin(np.pi, -row.beta, 0.37)
        global_phase_errors.append(
            np.linalg.norm(born_kernel(baseline) - born_kernel(phase_shifted))
        )
        sign_errors.append(
            np.linalg.norm(born_kernel(baseline) - born_kernel(sign_reversed))
        )

        tick = common_tick
        first = common_first
        second = common_second
        unitary = np.linalg.matrix_power(row.block, tick)
        coherent_outputs = []
        diagonal = np.zeros(6)
        diagonal[first] = diagonal[second] = 0.5
        markov_output = born_kernel(unitary) @ diagonal
        markov_errors = []
        for phase in (0.0, np.pi / 2, np.pi):
            state = np.zeros(6, dtype=complex)
            state[first] = 1 / np.sqrt(2)
            state[second] = np.exp(1j * phase) / np.sqrt(2)
            coherent_outputs.append(np.abs(unitary @ state) ** 2)
            markov_errors.append(
                np.linalg.norm(
                    born_kernel(unitary) @ np.abs(state) ** 2 - markov_output
                )
            )
        separations = [
            0.5 * np.sum(np.abs(left - right))
            for left in coherent_outputs
            for right in coherent_outputs
        ]
        phase_rows.append(
            (
                row.c3_phase,
                tick,
                first,
                second,
                float(max(separations)),
                float(max(markov_errors)),
            )
        )

    check(
        "per-tick read-reset has the stated exact asymptotic diffusion coefficient",
        max(abs(row[4] / row[3] - 1) for row in diffusion_rows) < 2e-5,
        diffusion_rows,
    )
    check(
        "the per-tick kernel loses rest phase and the sign of the phase-mass coordinate",
        max(global_phase_errors) < 3e-12 and max(sign_errors) < 3e-12,
        {
            "global_phase_errors": global_phase_errors,
            "beta_sign_errors": sign_errors,
        },
    )
    check(
        "same-diagonal phase fibres separate coherently but not under one kernel",
        min(row[4] for row in phase_rows) > 0.8
        and max(row[5] for row in phase_rows) < 3e-12,
        phase_rows,
    )


@dataclass(frozen=True)
class InertiaRun:
    acceleration: float
    norm: float
    band: float
    boundary: float


@dataclass(frozen=True)
class FrozenMassRow:
    c3_phase: float
    vector: np.ndarray
    dispersion_grid: tuple[float, ...]
    response_rows: tuple[tuple[int, float, float, float, InertiaRun, InertiaRun], ...]


def block_inertia(
    block: np.ndarray,
    strength: float,
    *,
    length: int = 4096,
    width: float = 0.006,
    duration: int = 160,
) -> InertiaRun:
    positions, momenta, packet = c222.prepare_block_packet(block, length, width)
    half = np.exp(0.5j * strength * positions)[:, None]
    means = [float(np.sum(positions * np.sum(np.abs(packet) ** 2, axis=1)))]
    for _ in range(duration):
        packet *= half
        packet = c210.local_molecular_step(packet, block, axis=0)
        packet *= half
        means.append(float(np.sum(positions * np.sum(np.abs(packet) ** 2, axis=1))))
    times = np.arange(duration + 1, dtype=float)
    acceleration = float(
        2 * np.polyfit(times, np.asarray(means) - means[0], 2)[0]
    )
    weights = np.sum(np.abs(packet) ** 2, axis=1)
    boundary = float(np.sum(weights[np.abs(positions) > length / 4]))
    return InertiaRun(
        acceleration,
        float(np.linalg.norm(packet)),
        c222.block_branch_probability(packet, momenta, block),
        boundary,
    )


def freeze_target_unfed_coherent_mass_rows(
    blocks: tuple[BlindBlock, ...]
) -> tuple[FrozenMassRow, ...]:
    """Measure C3-keyed blocks with no mass operator available to this function."""
    frozen_rows = []
    for row in blocks:
        dispersion_grid = []
        for step in (0.002, 0.003, 0.004):
            curvature = c222.block_curvature_tensor(row.block, step=step)
            dispersion_grid.append(1 / float(np.mean(np.diag(curvature))))
        duration_rows = []
        for duration in (128, 160, 192):
            for strength in (0.5e-6, 1e-6, 2e-6):
                positive = block_inertia(
                    row.block, strength, duration=duration
                )
                negative = block_inertia(
                    row.block, -strength, duration=duration
                )
                odd_acceleration = (
                    positive.acceleration - negative.acceleration
                ) / 2
                measured_inertia = -strength / odd_acceleration
                even_contamination = abs(
                    positive.acceleration + negative.acceleration
                ) / max(
                    abs(positive.acceleration - negative.acceleration), 1e-30
                )
                duration_rows.append(
                    (
                        duration,
                        strength,
                        measured_inertia,
                        even_contamination,
                        positive,
                        negative,
                    )
                )
        frozen_rows.append(
            FrozenMassRow(
                row.c3_phase,
                row.vector,
                tuple(dispersion_grid),
                tuple(duration_rows),
            )
        )

    health = []
    consistency = []
    for row in frozen_rows:
        reference_dispersion = row.dispersion_grid[1]
        consistency.extend(
            abs(value / reference_dispersion - 1)
            for value in row.dispersion_grid
        )
        for (
            _,
            _,
            inertia,
            even_contamination,
            positive,
            negative,
        ) in row.response_rows:
            consistency.append(abs(inertia / reference_dispersion - 1))
            health.append(
                abs(positive.norm - 1) < 3e-10
                and abs(negative.norm - 1) < 3e-10
                and min(positive.band, negative.band) > 0.999
                and max(positive.boundary, negative.boundary) < 2e-12
                and even_contamination < 1e-8
                and np.isfinite(inertia)
                and inertia > 0
                and positive.acceleration * negative.acceleration < 0
            )
    check(
        "target-unfed C3 sectors retain coherent dispersion and force inertia",
        max(consistency) < 0.002 and all(health),
        {
            "maximum_relative_spread": max(consistency),
            "rows": [
                (
                    phase,
                    dispersion,
                    [
                        (duration, strength, inertia, even)
                        for duration, strength, inertia, even, _, _ in duration_rows
                    ],
                )
                for row in frozen_rows
                for phase, dispersion, duration_rows in (
                    (row.c3_phase, row.dispersion_grid, row.response_rows),
                )
            ],
        },
    )
    return tuple(frozen_rows)


def unblind_coherent_mass_rows(
    frozen_rows: tuple[FrozenMassRow, ...], mass: np.ndarray
) -> None:
    """Compare frozen operational rows with M only after measurement returns."""
    unblinded = []
    for row in frozen_rows:
        target = float(np.vdot(row.vector, mass @ row.vector).real)
        reference_row = next(
            item
            for item in row.response_rows
            if item[0] == 160 and abs(item[1] - 1e-6) < 1e-15
        )
        inertia = reference_row[2]
        unblinded.append(
            (row.c3_phase, target, row.dispersion_grid[1], inertia)
        )
    check(
        "the frozen coherent measurements unblind to the Cycle-222 mass operator",
        max(
            max(abs(row[2] / row[1] - 1), abs(row[3] / row[1] - 1))
            for row in unblinded
        )
        < 0.002,
        unblinded,
    )


def scope_and_predecessor_controls() -> None:
    predecessors = (
        ROOT / "scripts/common_matter_field_coin_family_cycle219_2026_07_16.py",
        ROOT / "scripts/generated_beta_phase_register_cycle220_2026_07_16.py",
        ROOT / "scripts/operator_mass_equivalence_cycle221_2026_07_17.py",
        ROOT / "scripts/conditional_flavor_mass_operator_compiler_cycle222_2026_07_17.py",
    )
    check(
        "Cycles 219 through 222 remain present as explicit predecessors",
        all(path.is_file() for path in predecessors),
        [path.name for path in predecessors],
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    note_contract()
    compiled = c222.compile_operator(c222.REFERENCE_SCALE)
    blocks = c3_blind_blocks(compiled.coin)
    shift = c222.cyclic_shift_three()
    characters = np.column_stack([row.vector[1:] for row in blocks])
    phases = tuple(row.c3_phase for row in blocks)
    check(
        "three massive blocks are selected by C3 character without a mass lookup",
        len(blocks) == 3
        and len({round(phase, 10) for phase in phases}) == 3
        and max(
            abs(np.exp(3j * row.c3_phase) - 1) for row in blocks
        )
        < 3e-12
        and np.linalg.norm(characters.conj().T @ characters - np.eye(3))
        < 3e-12
        and max(
            np.linalg.norm(
                shift @ row.vector[1:]
                - np.exp(1j * row.c3_phase) * row.vector[1:]
            )
            for row in blocks
        )
        < 3e-12
        and max(
            np.linalg.norm(row.block.conj().T @ row.block - np.eye(6))
            for row in blocks
        )
        < 3e-12,
        {
            "phases": phases,
            "character_gram_error": float(
                np.linalg.norm(characters.conj().T @ characters - np.eye(3))
            ),
            "shift_eigen_errors": [
                float(
                    np.linalg.norm(
                        shift @ row.vector[1:]
                        - np.exp(1j * row.c3_phase) * row.vector[1:]
                    )
                )
                for row in blocks
            ],
            "block_unitarity_errors": [
                float(
                    np.linalg.norm(row.block.conj().T @ row.block - np.eye(6))
                )
                for row in blocks
            ],
        },
    )
    frozen_rows = freeze_target_unfed_coherent_mass_rows(blocks)
    phased_blocks = attach_register_phases(blocks, compiled.register)
    exact_coin_kernel_controls(phased_blocks)
    cadence_controls(phased_blocks)
    pointer_archive_and_basis_controls(compiled, blocks)
    full_walk_force_and_coarse_record_controls(blocks)
    diffusion_and_phase_controls(phased_blocks)
    unblind_coherent_mass_rows(frozen_rows, compiled.recovered_mass)
    scope_and_predecessor_controls()
    print(f"SUMMARY {PASS} passed, {FAIL} failed")
    return 1 if FAIL else 0


if __name__ == "__main__":
    raise SystemExit(main())
