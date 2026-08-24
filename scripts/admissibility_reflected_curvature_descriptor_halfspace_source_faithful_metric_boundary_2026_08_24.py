#!/usr/bin/env python3
"""Separate descriptor endpoints and test a source-faithful TT boundary metric.

The calculation concerns one supplied reflected-curvature action, its odd
six-edge plus one-Ward border, and spatial momentum (pi/2, 0, 0).  It does not
select a physical gravity action or boundary condition.  The negative result
is only for positive H-self-adjoint realizations whose readout is the
H-adjoint of the source and which reproduce the same scalar TT response.
"""

from __future__ import annotations

from dataclasses import dataclass
import os
from pathlib import Path
import sys
import time

import numpy as np
from scipy import linalg
from scipy.optimize import linear_sum_assignment


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import admissibility_reflected_curvature_canonical_reduction_schur_pole_tt_spectral_weight_boundary_2026_08_23 as block181  # noqa: E402


AUDIT_TIMEOUT_SEC = 240
NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_REFLECTED_CURVATURE_DESCRIPTOR_HALFSPACE_SOURCE_FAITHFUL_"
    "METRIC_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-24.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_REFLECTED_CURVATURE_DESCRIPTOR_HALFSPACE_SOURCE_FAITHFUL_METRIC_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-24.md",
    "docs/ADMISSIBILITY_REFLECTED_CURVATURE_CANONICAL_REDUCTION_SCHUR_POLE_TT_SPECTRAL_WEIGHT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-23.md",
    "docs/ADMISSIBILITY_REFLECTED_CURVATURE_ACTION_RECORD_SOURCE_TWO_STEP_TRANSFER_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "scripts/admissibility_reflected_curvature_descriptor_halfspace_source_faithful_metric_boundary_2026_08_24.py",
    "scripts/admissibility_reflected_curvature_canonical_reduction_schur_pole_tt_spectral_weight_boundary_2026_08_23.py",
    "scripts/admissibility_reflected_curvature_action_record_source_two_step_transfer_boundary_2026_08_14.py",
    "scripts/admissibility_regge_reflected_orientation_common_metric_transfer_gate_boundary_2026_08_11.py",
    "scripts/admissibility_reflected_plaquette_curvature_record_ricci_source_intertwiner_boundary_2026_08_11.py",
    "scripts/admissibility_cycle713_record_stress_block44_ir_reflected_carrier_boundary_2026_08_13.py",
    "scripts/admissibility_repaired_regge_full_edge_finite_frequency_pole_survival_boundary_2026_08_11.py",
)

MOMENT_SAMPLES = 8192
STRUCTURAL_ZERO_RELATIVE = 1.0e-12


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, key: str, statement: str, condition, detail: str = "") -> None:
        ok = bool(condition)
        short = statement if len(statement) <= 91 else statement[:88] + "..."
        print(f"[{'PASS' if ok else 'FAIL'}] {key}: {short}")
        if detail:
            clipped = detail if len(detail) <= 170 else detail[:167] + "..."
            print(f"       {clipped}")
        self.passed += int(ok)
        self.failed += int(not ok)


@dataclass(frozen=True)
class BorderData:
    coefficients: tuple[np.ndarray, ...]
    rhs: np.ndarray
    leakage: float
    pair_error: float
    ward_relative: float
    gauge_ranks: tuple[int, ...]
    action_ranks: tuple[int, ...]


@dataclass(frozen=True)
class DescriptorData:
    endpoint_ranks: tuple[int, int]
    companion_ranks: tuple[int, int]
    determinant_support: tuple[int, int]
    eigenvalue_counts: tuple[int, int, int]
    zero_staircase: tuple[int, ...]
    infinity_staircase: tuple[int, ...]
    staircase_gap: float
    finite_values: np.ndarray


@dataclass(frozen=True)
class MetricData:
    rank: int
    equation_residual: float
    source_residual: float
    metric_eigenvalues: np.ndarray
    transfer_form_eigenvalues: np.ndarray
    even_metric_eigenvalues: np.ndarray
    even_transfer_form_eigenvalues: np.ndarray
    contractive_metric_eigenvalues: np.ndarray
    stein_eigenvalues: np.ndarray
    contractive_source_residual: float
    contractive_self_adjoint_residual: float


def flat(path: Path) -> str:
    return " ".join(path.read_text(encoding="utf-8").lower().split())


def scaled_inertia(values: np.ndarray) -> tuple[int, int, int]:
    values = np.asarray(values, dtype=float)
    tolerance = 1.0e-12 * max(float(np.max(np.abs(values))), 1.0e-300)
    return (
        int(np.sum(values < -tolerance)),
        int(np.sum(values > tolerance)),
        int(np.sum(np.abs(values) <= tolerance)),
    )


def odd_border_data(union, mutation: str = "") -> BorderData:
    directions = np.asarray(union.directions, dtype=float)
    edge_swap = block181.swap_matrix(directions, 1, 2)
    gauge_swap = np.eye(4)
    gauge_swap[[1, 2]] = gauge_swap[[2, 1]]
    edge_basis = block181.sign_basis(edge_swap, -1)
    gauge_basis = block181.sign_basis(gauge_swap, -1)

    def momentum(temporal: complex) -> np.ndarray:
        return np.asarray(
            (block181.SPATIAL_WAVE_NUMBER, 0.0, 0.0, temporal), dtype=complex
        )

    operator, operator_leakage = block181.matrix_fourier_coefficients(
        lambda temporal: edge_basis.T
        @ (-block181.action(union, momentum(temporal)))
        @ edge_basis,
        (-2, -1, 0, 1, 2),
    )
    right, right_leakage = block181.matrix_fourier_coefficients(
        lambda temporal: edge_basis.T
        @ block181.block74.block48.union_gauge_map(union, momentum(temporal))
        @ gauge_basis,
        (-1, 0, 1),
    )
    left, left_leakage = block181.matrix_fourier_coefficients(
        lambda temporal: edge_basis.T
        @ block181.block74.block48.union_gauge_map(union, -momentum(temporal))
        @ gauge_basis,
        (-1, 0, 1),
    )
    bordered = block181.border_coefficients(operator, right, left)
    scale = max(float(np.linalg.norm(value)) for value in bordered.values())
    cleaned: dict[int, np.ndarray] = {}
    for exponent in range(-2, 3):
        value = bordered[exponent].copy()
        value[np.abs(value) < STRUCTURAL_ZERO_RELATIVE * scale] = 0.0
        cleaned[exponent] = value

    pair_error = max(
        float(np.linalg.norm(cleaned[-exponent] - cleaned[exponent].conj().T))
        for exponent in (0, 1, 2)
    ) / scale

    ward_relative = 0.0
    gauge_ranks: list[int] = []
    action_ranks: list[int] = []
    for index, temporal in enumerate((0.0, 0.37, 1.1, 2.4)):
        value = momentum(temporal)
        action = block181.action(union, value)
        gauge = block181.block74.block48.union_gauge_map(union, value)
        left_gauge = block181.block74.block48.union_gauge_map(union, -value)
        if mutation == "ward_input" and index == 1:
            gauge = gauge.copy()
            gauge[0, 0] += 1.0e-3
        action_scale = float(np.linalg.norm(action))
        ward_relative = max(
            ward_relative,
            float(np.linalg.norm(action @ gauge))
            / (action_scale * float(np.linalg.norm(gauge))),
            float(np.linalg.norm(left_gauge.T @ action))
            / (float(np.linalg.norm(left_gauge)) * action_scale),
        )
        gauge_ranks.append(int(np.linalg.matrix_rank(gauge, tol=1.0e-10)))
        action_ranks.append(int(np.linalg.matrix_rank(action, tol=1.0e-9)))

    observable = block181.block74.local_tt_observables(union, "")[0]
    rhs = np.concatenate(
        (edge_basis.T @ observable, np.zeros(gauge_basis.shape[1]))
    ).astype(complex)
    return BorderData(
        coefficients=tuple(cleaned[exponent] for exponent in range(-2, 3)),
        rhs=rhs,
        leakage=max(operator_leakage, right_leakage, left_leakage),
        pair_error=pair_error,
        ward_relative=ward_relative,
        gauge_ranks=tuple(gauge_ranks),
        action_ranks=tuple(action_ranks),
    )


def strong_companion(coefficients: tuple[np.ndarray, ...]) -> tuple[np.ndarray, np.ndarray]:
    degree = len(coefficients) - 1
    dimension = coefficients[0].shape[0]
    left = np.zeros((degree * dimension, degree * dimension), dtype=complex)
    right = np.zeros_like(left)
    for index in range(degree - 1):
        left[
            index * dimension : (index + 1) * dimension,
            (index + 1) * dimension : (index + 2) * dimension,
        ] = np.eye(dimension)
        right[
            index * dimension : (index + 1) * dimension,
            index * dimension : (index + 1) * dimension,
        ] = np.eye(dimension)
    for index in range(degree):
        left[
            (degree - 1) * dimension : degree * dimension,
            index * dimension : (index + 1) * dimension,
        ] = -coefficients[index]
    right[
        (degree - 1) * dimension : degree * dimension,
        (degree - 1) * dimension : degree * dimension,
    ] = coefficients[-1]
    return left, right


def toeplitz_staircase(
    coefficients: tuple[np.ndarray, ...], orders: tuple[int, ...] = (1, 2, 3)
) -> tuple[tuple[int, ...], float]:
    dimension = coefficients[0].shape[0]
    nullities: list[int] = []
    minimum_gap = np.inf
    for order in orders:
        matrix = np.zeros((order * dimension, order * dimension), dtype=complex)
        for row in range(order):
            for column in range(row + 1):
                degree = row - column
                if degree < len(coefficients):
                    matrix[
                        row * dimension : (row + 1) * dimension,
                        column * dimension : (column + 1) * dimension,
                    ] = coefficients[degree]
        singular = np.linalg.svd(matrix, compute_uv=False)
        tolerance = 1.0e-12 * singular[0]
        rank = int(np.sum(singular > tolerance))
        nullity = matrix.shape[0] - rank
        nullities.append(nullity)
        if rank and nullity:
            minimum_gap = min(minimum_gap, float(singular[rank - 1] / singular[rank]))
    return tuple(nullities), float(minimum_gap)


def descriptor_data(border: BorderData, mutation: str = "") -> DescriptorData:
    coefficients = tuple(value.copy() for value in border.coefficients)
    if mutation == "endpoint_input":
        changed = list(coefficients)
        changed[0] = changed[0] + 1.0e-3 * np.eye(changed[0].shape[0])
        coefficients = tuple(changed)

    companion_left, companion_right = strong_companion(coefficients)
    homogeneous = linalg.eig(
        companion_left,
        companion_right,
        left=False,
        right=False,
        homogeneous_eigvals=True,
    )
    alpha, beta = homogeneous
    scale = np.maximum(np.abs(alpha), np.abs(beta))
    zero = (np.abs(alpha) < 1.0e-8 * scale) & (np.abs(beta) >= 1.0e-8 * scale)
    infinite = (np.abs(beta) < 1.0e-8 * scale) & (np.abs(alpha) >= 1.0e-8 * scale)
    finite = ~(zero | infinite)
    finite_values = alpha[finite] / beta[finite]

    determinant = block181.determinant_polynomial(
        {degree: value for degree, value in enumerate(coefficients)}
    )
    zero_staircase, zero_gap = toeplitz_staircase(coefficients)
    infinity_staircase, infinity_gap = toeplitz_staircase(tuple(reversed(coefficients)))
    return DescriptorData(
        endpoint_ranks=(
            int(np.linalg.matrix_rank(coefficients[0], tol=1.0e-10)),
            int(np.linalg.matrix_rank(coefficients[-1], tol=1.0e-10)),
        ),
        companion_ranks=(
            int(np.linalg.matrix_rank(companion_left, tol=1.0e-10)),
            int(np.linalg.matrix_rank(companion_right, tol=1.0e-10)),
        ),
        determinant_support=(min(determinant), max(determinant)),
        eigenvalue_counts=(int(np.sum(zero)), int(np.sum(finite)), int(np.sum(infinite))),
        zero_staircase=zero_staircase,
        infinity_staircase=infinity_staircase,
        staircase_gap=min(zero_gap, infinity_gap),
        finite_values=finite_values,
    )


def scalar_numerator_certificate(
    border: BorderData,
) -> tuple[tuple[int, int], float, float]:
    samples = 128
    axis = int(np.argmax(np.abs(border.rhs)))
    isolated = np.zeros_like(border.rhs)
    isolated[axis] = border.rhs[axis]
    source_axis_residual = float(
        np.linalg.norm(border.rhs - isolated) / np.linalg.norm(border.rhs)
    )
    values = []
    laurent = {
        exponent - 2: coefficient
        for exponent, coefficient in enumerate(border.coefficients)
    }
    for index in range(samples):
        value = np.exp(2.0j * np.pi * index / samples)
        matrix = block181.evaluate_laurent(laurent, value)
        minor = np.delete(np.delete(matrix, axis, axis=0), axis, axis=1)
        values.append(border.rhs[axis] ** 2 * np.linalg.det(minor))
    transformed = np.fft.fft(np.asarray(values)) / samples
    scale = float(np.max(np.abs(transformed)))
    support = []
    leakage = 0.0
    for index, coefficient in enumerate(transformed):
        exponent = index if index <= samples // 2 else index - samples
        if abs(coefficient) > 1.0e-11 * scale:
            support.append(exponent)
        if exponent < -12 or exponent > 12:
            leakage = max(leakage, float(abs(coefficient)) / scale)
    return (min(support), max(support)), leakage, source_axis_residual


def projective_root_match(values: np.ndarray, expected: np.ndarray) -> float:
    cost = np.asarray(
        [
            [
                abs(value - target)
                / (np.sqrt(1.0 + abs(value) ** 2) * np.sqrt(1.0 + abs(target) ** 2))
                for target in expected
            ]
            for value in values
        ]
    )
    rows, columns = linear_sum_assignment(cost)
    return float(np.max(cost[rows, columns]))


def spectrum_variant(border: BorderData, mutation: str) -> np.ndarray:
    coefficients = tuple(value.copy() for value in border.coefficients)
    if mutation == "finite_spectrum_input":
        changed = list(coefficients)
        changed[2] = changed[2] + 1.0e-3 * np.eye(changed[2].shape[0])
        coefficients = tuple(changed)
    return descriptor_data(
        BorderData(
            coefficients=coefficients,
            rhs=border.rhs,
            leakage=border.leakage,
            pair_error=border.pair_error,
            ward_relative=border.ward_relative,
            gauge_ranks=border.gauge_ranks,
            action_ranks=border.action_ranks,
        )
    ).finite_values


def minimality_data(
    roots: np.ndarray, weights: np.ndarray, mutation: str = ""
) -> tuple[int, int, float]:
    transfer = np.diag(roots)
    source = np.ones(len(roots))
    readout = weights.copy()
    if mutation == "source_dark_input":
        readout[int(np.argmin(readout))] = 0.0
    controllability = np.column_stack(
        [np.linalg.matrix_power(transfer, order) @ source for order in range(len(roots))]
    )
    observability = np.vstack(
        [readout @ np.linalg.matrix_power(transfer, order) for order in range(len(roots))]
    )
    return (
        int(np.linalg.matrix_rank(controllability, tol=1.0e-12)),
        int(np.linalg.matrix_rank(observability, tol=1.0e-12)),
        float(np.min(np.abs(readout))),
    )


def solve_metric(transfer: np.ndarray, readout: np.ndarray) -> tuple[np.ndarray, int, float, float]:
    dimension = transfer.shape[0]
    source = np.ones(dimension)
    basis: list[np.ndarray] = []
    for row in range(dimension):
        for column in range(row, dimension):
            value = np.zeros((dimension, dimension))
            value[row, column] = 1.0
            value[column, row] = 1.0
            if row == column:
                value[row, column] = 1.0
            basis.append(value)
    equations = []
    targets = []
    for row in range(dimension):
        for column in range(dimension):
            equations.append(
                [(transfer.T @ value - value @ transfer)[row, column] for value in basis]
            )
            targets.append(0.0)
    for row in range(dimension):
        equations.append([(value @ source)[row] for value in basis])
        targets.append(readout[row])
    matrix = np.asarray(equations)
    target = np.asarray(targets)
    solution, _, rank, _ = np.linalg.lstsq(matrix, target, rcond=1.0e-13)
    metric = sum(coefficient * value for coefficient, value in zip(solution, basis))
    equation_residual = float(np.linalg.norm(transfer.T @ metric - metric @ transfer))
    source_residual = float(np.linalg.norm(metric @ source - readout))
    return metric, int(rank), equation_residual, source_residual


def metric_data(roots: np.ndarray, weights: np.ndarray, mutation: str = "") -> MetricData:
    readout = weights.copy()
    if mutation == "positive_readout_input":
        index = int(np.argmin(readout))
        readout[index] = abs(readout[index])
    transfer = np.diag(roots)
    metric, rank, equation_residual, source_residual = solve_metric(transfer, readout)
    even_metric, even_rank, even_equation_residual, even_source_residual = solve_metric(
        transfer @ transfer, readout
    )
    dimension = len(roots)
    source = np.ones(dimension)
    projector = np.eye(dimension) - np.outer(source, source) / dimension
    particular = (
        np.outer(readout, source) + np.outer(source, readout)
    ) / dimension - np.sum(readout) * np.outer(source, source) / dimension**2
    contractive_metric = particular + projector
    stein = contractive_metric - transfer.T @ contractive_metric @ transfer
    return MetricData(
        rank=min(rank, even_rank),
        equation_residual=max(equation_residual, even_equation_residual),
        source_residual=max(source_residual, even_source_residual),
        metric_eigenvalues=np.linalg.eigvalsh(metric),
        transfer_form_eigenvalues=np.linalg.eigvalsh(metric @ transfer),
        even_metric_eigenvalues=np.linalg.eigvalsh(even_metric),
        even_transfer_form_eigenvalues=np.linalg.eigvalsh(even_metric @ transfer @ transfer),
        contractive_metric_eigenvalues=np.linalg.eigvalsh(contractive_metric),
        stein_eigenvalues=np.linalg.eigvalsh(stein),
        contractive_source_residual=float(
            np.linalg.norm(contractive_metric @ source - readout)
        ),
        contractive_self_adjoint_residual=float(
            np.linalg.norm(contractive_metric @ transfer - transfer.T @ contractive_metric)
        ),
    )


def direct_moments(
    border: BorderData, mutation: str = "", count: int = 13
) -> np.ndarray:
    source = border.rhs.copy()
    if mutation == "direct_source_input":
        source = 1.01 * source
    temporal = 2.0 * np.pi * np.arange(MOMENT_SAMPLES) / MOMENT_SAMPLES
    covariance = np.asarray(
        [
            (
                source.T
                @ np.linalg.solve(
                    block181.evaluate_laurent(
                        {
                            exponent - 2: coefficient
                            for exponent, coefficient in enumerate(border.coefficients)
                        },
                        np.exp(1.0j * value),
                    ),
                    source,
                )
            ).real
            for value in temporal
        ]
    )
    return np.asarray(
        [
            np.mean(np.exp(1.0j * temporal * order) * covariance).real
            for order in range(count)
        ]
    )


def main() -> int:
    started = time.perf_counter()
    mutation = os.environ.get("TOE_MUTATION", "")
    allowed = {
        "",
        "ward_input",
        "endpoint_input",
        "finite_spectrum_input",
        "source_dark_input",
        "positive_readout_input",
        "direct_source_input",
        "note_boundary",
    }
    if mutation not in allowed:
        raise ValueError(f"unknown TOE_MUTATION={mutation}")

    checks = Checks()
    union = block181.block74.block48.build_reflection_union()
    border = odd_border_data(union)
    coefficient_scale = max(float(np.linalg.norm(value)) for value in border.coefficients)
    minimum_retained_relative = min(
        float(abs(entry)) / coefficient_scale
        for value in border.coefficients
        for entry in value.ravel()
        if entry != 0.0
    )
    ward_variant = odd_border_data(union, mutation)
    descriptor = descriptor_data(border, mutation)
    baseline_descriptor = descriptor_data(border)
    numerator_support, numerator_leakage, source_axis_residual = (
        scalar_numerator_certificate(border)
    )
    laurent = block181.laurent_certificate(union, "")
    coupled = tuple(branch for branch in laurent.branches if branch.coupled)
    roots = np.asarray([branch.root.real for branch in coupled])
    weights = np.asarray([branch.moment_weight.real for branch in coupled])

    note = flat(NOTE_PATH)
    if mutation == "note_boundary":
        note = note.replace(
            "exact_response_verdict: bounded_infeasible",
            "exact_response_verdict: removed",
        )
    axiom = flat(AXIOM_PATH)

    binding_gate = (
        block181.MU == 1.0 / 1024.0
        and border.leakage < 1.0e-12
        and border.pair_error < 1.0e-12
        and minimum_retained_relative > 1.0e-6
        and ward_variant.ward_relative < 1.0e-12
        and ward_variant.gauge_ranks == (4, 4, 4, 4)
        and ward_variant.action_ranks == (18, 18, 18, 18)
    )
    checks.check(
        "supplied-action-ward-and-odd-border-binding",
        "the supplied action retains four Ward directions and a clean reflected odd border",
        binding_gate,
        f"leak={border.leakage:.2e}; retained-gap={minimum_retained_relative:.2e}; Ward={ward_variant.ward_relative:.2e}; ranks={ward_variant.action_ranks}",
    )

    descriptor_gate = (
        descriptor.endpoint_ranks == (2, 2)
        and descriptor.companion_ranks == (23, 23)
        and descriptor.determinant_support == (7, 21)
        and descriptor.eigenvalue_counts == (7, 14, 7)
        and descriptor.zero_staircase == (5, 6, 7)
        and descriptor.infinity_staircase == (5, 6, 7)
        and descriptor.staircase_gap > 1.0e7
        and numerator_support == (-6, 6)
        and numerator_leakage < 1.0e-12
        and source_axis_residual < 1.0e-12
    )
    checks.check(
        "descriptor-endpoint-chain-separation",
        "the strong companion separates seven zero and seven infinite endpoint roots from fourteen finite modes",
        descriptor_gate,
        f"end={descriptor.endpoint_ranks}; det={descriptor.determinant_support}; numerator={numerator_support}; qz={descriptor.eigenvalue_counts}; stairs={descriptor.zero_staircase}/{descriptor.infinity_staircase}",
    )

    finite_variant = spectrum_variant(border, mutation)
    expected_finite = np.asarray(
        [branch.root for branch in laurent.branches]
        + [1.0 / np.conj(branch.root) for branch in laurent.branches]
    )
    root_match = (
        projective_root_match(finite_variant, expected_finite)
        if len(finite_variant) == len(expected_finite)
        else np.inf
    )
    spectral_gate = (
        baseline_descriptor.eigenvalue_counts == (7, 14, 7)
        and laurent.root_count == 14
        and laurent.inside_count == 7
        and len(coupled) == 3
        and all(branch.solver_success for branch in laurent.branches)
        and min(branch.simplicity_ratio for branch in laurent.branches) > 1.0e-14
        and root_match < 1.0e-8
        and max(abs(branch.root.imag) for branch in coupled) < 1.0e-8
        and max(abs(branch.moment_weight.imag) for branch in coupled) < 1.0e-8
    )
    checks.check(
        "finite-spectrum-and-residue-recovery",
        "companion finite roots match the Laurent determinant and exactly three stable real poles carry the TT response",
        spectral_gate,
        f"roots={laurent.root_count}/{laurent.inside_count}; coupled={len(coupled)}; chordal match={root_match:.2e}",
    )

    controllability_rank, observability_rank, minimum_weight = minimality_data(
        roots, weights, mutation
    )
    minimal_gate = (
        len(roots) == 3
        and np.max(np.abs(roots)) < 1.0
        and min(abs(left - right) for i, left in enumerate(roots) for right in roots[i + 1 :]) > 1.0e-6
        and controllability_rank == 3
        and observability_rank == 3
        and minimum_weight > 1.0e-5
    )
    checks.check(
        "source-visible-minimal-stable-response",
        "all three TT poles are controllable and observable, so the hostile pole cannot be removed as source-dark",
        minimal_gate,
        f"ranks={controllability_rank}/{observability_rank}; min|weight|={minimum_weight:.2e}; radius={np.max(np.abs(roots)):.6f}",
    )

    metric = metric_data(roots, weights, mutation)
    metric_gate = (
        metric.rank == 6
        and metric.equation_residual < 1.0e-12
        and metric.source_residual < 1.0e-12
        and scaled_inertia(metric.metric_eigenvalues) == (1, 2, 0)
        and scaled_inertia(metric.transfer_form_eigenvalues) == (2, 1, 0)
        and scaled_inertia(metric.even_metric_eigenvalues) == (1, 2, 0)
        and scaled_inertia(metric.even_transfer_form_eigenvalues) == (1, 2, 0)
        and scaled_inertia(metric.contractive_metric_eigenvalues) == (0, 3, 0)
        and scaled_inertia(metric.stein_eigenvalues) == (0, 3, 0)
        and metric.contractive_source_residual < 1.0e-12
        and metric.contractive_self_adjoint_residual > 1.0e-3
    )
    checks.check(
        "source-faithful-os-self-adjoint-metric-infeasibility",
        "the unique self-adjoint metrics are indefinite, while a positive non-self-adjoint contractive metric exists",
        metric_gate,
        f"H={scaled_inertia(metric.metric_eigenvalues)}; HA={scaled_inertia(metric.transfer_form_eigenvalues)}; H2={scaled_inertia(metric.even_metric_eigenvalues)}; H2A2={scaled_inertia(metric.even_transfer_form_eigenvalues)}",
    )

    moments = direct_moments(border, mutation)
    reconstructed = np.asarray(
        [sum(weight * root**order for root, weight in zip(roots, weights)) for order in range(13)]
    )
    vandermonde = np.vander(roots, 3, increasing=True).T
    modal_hankel = vandermonde @ np.diag(weights) @ vandermonde.T
    hankel_determinant = float(np.linalg.det(modal_hankel))
    determinant_formula = float(
        np.prod(weights)
        * np.prod(
            [
                (roots[right] - roots[left]) ** 2
                for left in range(len(roots))
                for right in range(left + 1, len(roots))
            ]
        )
    )
    even_roots = roots**2
    even_determinant_formula = float(
        np.prod(weights)
        * np.prod(
            [
                (even_roots[right] - even_roots[left]) ** 2
                for left in range(len(even_roots))
                for right in range(left + 1, len(even_roots))
            ]
        )
    )
    moment_error = float(
        np.max(np.abs(moments[:9] - reconstructed[:9]))
        / max(float(np.max(np.abs(moments[:9]))), 1.0e-300)
    )
    base_hankel = np.asarray([[moments[row + column] for column in range(3)] for row in range(3)])
    base_minimum = float(np.linalg.eigvalsh(base_hankel)[0])
    one_step_minimum = block181.block74.hankel_minimum(moments, step=1, order=2, shift=1)
    two_step_minimum = block181.block74.hankel_minimum(moments, step=2, order=3, shift=0)
    moment_gate = (
        moment_error < 1.0e-6
        and base_minimum < -1.0e-7
        and one_step_minimum < -1.0e-10
        and two_step_minimum < -1.0e-8
        and hankel_determinant < 0.0
        and even_determinant_formula < 0.0
        and abs(hankel_determinant - determinant_formula)
        < 1.0e-6 * abs(determinant_formula)
    )
    checks.check(
        "direct-moment-and-even-step-gram-crosscheck",
        "direct inverse-border moments agree with residues and independently violate positive one- and two-step Gram tests",
        moment_gate,
        f"rel={moment_error:.2e}; H0={base_minimum:.2e}; H1={one_step_minimum:.2e}; H2={two_step_minimum:.2e}",
    )

    scope_gate = (
        all((ROOT / path).exists() for path in AUDIT_INPUT_PATHS)
        and "does not choose a hamiltonian or transfer operator" in axiom
        and "exact_response_verdict: bounded_infeasible" in note
        and "gravity_verdict: open" in note
        and "no axiom is amended" in note
        and all(f"### n{index}" in note for index in range(1, 9))
        and "n1--n8 status: `pass`" in note
    )
    checks.check(
        "scope-no-go-discipline-and-axiom-boundary",
        "the landing note keeps the infeasibility exact-response scoped, lands N1-N8, and makes no gravity or axiom claim",
        scope_gate,
    )

    print(
        "descriptor: endpoint ranks=2/2; zero/finite/infinite=7/14/7; partial multiplicities at both endpoints=3+1+1+1+1"
    )
    print(
        "response_endpoint_support: determinant=-7..7 numerator=-6..6, so the scalar TT response has no zero or infinite endpoint pole"
    )
    for root, weight in zip(roots, weights):
        print(f"tt_mode: z={root:+.9e} weight={weight:+.9e}")
    print(
        "METRIC_CERTIFICATE: H A=A^T H and H b=c have a unique indefinite solution for A and A squared; a separate positive Stein-contracting H exists but is non-self-adjoint"
    )
    print(
        f"CONTRACTIVE_ESCAPE: min_eig_H={np.min(metric.contractive_metric_eigenvalues):.6e} min_eig_Stein={np.min(metric.stein_eigenvalues):.6e} self_adjoint_residual={metric.contractive_self_adjoint_residual:.6e}"
    )
    print(
        "N5_CERTIFICATE: the execution resolutions below state exactly what this runner did and did not resolve"
    )
    print(
        "per_element: checked the twenty-two-edge action, four Ward columns, odd six-edge basis, and one bordered gauge coordinate"
    )
    print(
        "per_site: checked and not executed — the calculation uses one translation-invariant reflected unit cell, not an inhomogeneous site family"
    )
    print(
        "per_mode: checked all endpoint and finite modes of the declared odd border at spatial momentum pi over two only"
    )
    print(
        "per_block: checked the 28-dimensional strong companion, three-mode minimal response, metric equations, and moment Gram matrices"
    )
    print(
        "lattice_wide: checked and not executed — no Brillouin-zone, nonlinear-background, continuum, or all-lattice result is claimed"
    )
    print(
        "EXACT_OS_SELF_ADJOINT_RESPONSE_VERDICT: BOUNDED_INFEASIBLE; PHYSICAL_BOUNDARY_RESPONSE: OPEN; GRAVITY_VERDICT: OPEN"
    )
    print(
        "MINIMUM_CHANGE: a derived boundary response, source/readout map, action, or the self-adjoint/OS transfer requirement must change; deleting a source-visible pole is not source-faithful"
    )
    print("TOE_MOVEMENT: obligations=0 percentages=0 axioms_amended=0")
    print(f"elapsed_sec={time.perf_counter() - started:.2f}")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return int(checks.failed != 0)


if __name__ == "__main__":
    raise SystemExit(main())
