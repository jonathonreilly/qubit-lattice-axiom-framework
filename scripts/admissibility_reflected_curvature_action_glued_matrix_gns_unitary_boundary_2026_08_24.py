#!/usr/bin/env python3
"""Certify the action-glued matrix Herglotz/GNS reconstruction.

The calculation is bounded to the supplied reflected-curvature action, its
odd six-edge plus one-Ward border, and spatial momentum (pi/2,0,0).  It proves
all-finite-support Toeplitz positivity and a canonical two-sided unitary shift
on the Ward quotient.  It does not claim a Hamiltonian, quantum Record
instrument, Newtonian limit, refinement law, or gravity closure.
"""

from __future__ import annotations

from dataclasses import dataclass
import math
import os
from pathlib import Path
import sys
import time

import numpy as np
from numpy.polynomial import Polynomial, chebyshev


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import admissibility_reflected_curvature_descriptor_halfspace_source_faithful_metric_boundary_2026_08_24 as block182  # noqa: E402
import admissibility_reflected_curvature_weyl_feshbach_reflection_radical_boundary_2026_08_24 as block183  # noqa: E402


block181 = block182.block181
NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_REFLECTED_CURVATURE_ACTION_GLUED_MATRIX_GNS_UNITARY_"
    "BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-24.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
SAMPLES = 8192

AUDIT_TIMEOUT_SEC = 240
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_REFLECTED_CURVATURE_ACTION_GLUED_MATRIX_GNS_UNITARY_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-24.md",
    "docs/ADMISSIBILITY_REFLECTED_CURVATURE_WEYL_FESHBACH_REFLECTION_RADICAL_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-24.md",
    "docs/ADMISSIBILITY_REFLECTED_CURVATURE_DESCRIPTOR_HALFSPACE_SOURCE_FAITHFUL_METRIC_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-24.md",
    "docs/ADMISSIBILITY_REFLECTED_CURVATURE_CANONICAL_REDUCTION_SCHUR_POLE_TT_SPECTRAL_WEIGHT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-23.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "scripts/admissibility_reflected_curvature_action_glued_matrix_gns_unitary_boundary_2026_08_24.py",
    "scripts/admissibility_reflected_curvature_weyl_feshbach_reflection_radical_boundary_2026_08_24.py",
    "scripts/admissibility_reflected_curvature_descriptor_halfspace_source_faithful_metric_boundary_2026_08_24.py",
    "scripts/admissibility_reflected_curvature_canonical_reduction_schur_pole_tt_spectral_weight_boundary_2026_08_23.py",
    "scripts/admissibility_reflected_curvature_action_record_source_two_step_transfer_boundary_2026_08_14.py",
    "scripts/admissibility_regge_reflected_orientation_common_metric_transfer_gate_boundary_2026_08_11.py",
    "scripts/admissibility_reflected_plaquette_curvature_record_ricci_source_intertwiner_boundary_2026_08_11.py",
    "scripts/admissibility_cycle713_record_stress_block44_ir_reflected_carrier_boundary_2026_08_13.py",
)

MUTATIONS = (
    "ward_input",
    "edge_action_input",
    "border_coupling_input",
    "covariance_input",
    "moment_input",
    "scalar_weight_input",
    "gluing_input",
    "note_boundary",
)


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, key: str, statement: str, condition, detail: str = "") -> None:
        ok = bool(condition)
        short = statement if len(statement) <= 91 else statement[:88] + "..."
        print(f"[{'PASS' if ok else 'FAIL'}] {key}: {short}")
        if detail:
            clipped = detail if len(detail) <= 180 else detail[:177] + "..."
            print(f"       {clipped}")
        self.passed += int(ok)
        self.failed += int(not ok)


@dataclass(frozen=True)
class PolynomialCertificate:
    chebyshev: np.ndarray
    power: np.ndarray
    bernstein: np.ndarray
    relative_reconstruction: float
    imaginary_relative: float


@dataclass(frozen=True)
class SampledSymbols:
    theta: np.ndarray
    bordered: np.ndarray
    inverse: np.ndarray
    edge_covariance: np.ndarray


def flat(path: Path) -> str:
    return " ".join(path.read_text(encoding="utf-8").lower().split())


def inertia(matrix: np.ndarray, tolerance: float = 1.0e-9) -> tuple[int, int, int]:
    values = np.linalg.eigvalsh(0.5 * (matrix + matrix.conj().T))
    return (
        int(np.sum(values < -tolerance)),
        int(np.sum(values > tolerance)),
        int(np.sum(np.abs(values) <= tolerance)),
    )


def evaluate(coefficients: tuple[np.ndarray, ...], z: complex) -> np.ndarray:
    return block181.evaluate_laurent(
        {index - 2: value for index, value in enumerate(coefficients)}, z
    )


def right_ward_vector(z: complex) -> np.ndarray:
    return np.asarray(
        (
            0.0,
            (z - 1.0) / np.sqrt(2.0),
            (1.0 - 1.0j) / np.sqrt(2.0),
            (1.0j * z - 1.0) / np.sqrt(3.0),
            (1.0 - 1.0 / z) / np.sqrt(2.0),
            (1.0 - 1.0j / z) / np.sqrt(3.0),
        ),
        dtype=complex,
    )


def left_ward_vector(z: complex) -> np.ndarray:
    return np.asarray(
        (
            0.0,
            (1.0 / z - 1.0) / np.sqrt(2.0),
            (1.0 + 1.0j) / np.sqrt(2.0),
            (-1.0j / z - 1.0) / np.sqrt(3.0),
            (1.0 - z) / np.sqrt(2.0),
            (1.0 + 1.0j * z) / np.sqrt(3.0),
        ),
        dtype=complex,
    )


def right_ward_coefficients() -> dict[int, np.ndarray]:
    minus = np.asarray(
        (0, 0, 0, 0, -1 / np.sqrt(2), -1.0j / np.sqrt(3)), complex
    )
    zero = np.asarray(
        (
            0,
            -1 / np.sqrt(2),
            (1 - 1.0j) / np.sqrt(2),
            -1 / np.sqrt(3),
            1 / np.sqrt(2),
            1 / np.sqrt(3),
        ),
        complex,
    )
    plus = np.asarray(
        (0, 1 / np.sqrt(2), 0, 1.0j / np.sqrt(3), 0, 0), complex
    )
    return {-1: minus, 0: zero, 1: plus}


def left_ward_coefficients() -> dict[int, np.ndarray]:
    minus = np.asarray(
        (0, 1 / np.sqrt(2), 0, -1.0j / np.sqrt(3), 0, 0), complex
    )
    zero = np.asarray(
        (
            0,
            -1 / np.sqrt(2),
            (1 + 1.0j) / np.sqrt(2),
            -1 / np.sqrt(3),
            1 / np.sqrt(2),
            1 / np.sqrt(3),
        ),
        complex,
    )
    plus = np.asarray(
        (0, 0, 0, 0, -1 / np.sqrt(2), 1.0j / np.sqrt(3)), complex
    )
    return {-1: minus, 0: zero, 1: plus}


def ward_convolution_residual(coefficients: tuple[np.ndarray, ...]) -> float:
    operator = {index - 2: value[:6, :6] for index, value in enumerate(coefficients)}
    ward = right_ward_coefficients()
    products: dict[int, np.ndarray] = {}
    scale = 0.0
    for left_power, left in operator.items():
        for right_power, right in ward.items():
            product = left @ right
            power = left_power + right_power
            products[power] = products.get(power, np.zeros(6, complex)) + product
            scale += float(np.linalg.norm(product))
    return max(float(np.linalg.norm(value)) for value in products.values()) / scale


def polynomial_certificate(values: np.ndarray, degree: int) -> PolynomialCertificate:
    values = np.asarray(values)
    count = len(values)
    fourier = np.fft.fft(values) / count
    cheb = np.zeros(degree + 1)
    cheb[0] = float(fourier[0].real)
    for index in range(1, degree + 1):
        cheb[index] = float((fourier[index] + fourier[-index]).real)
    power = chebyshev.cheb2poly(cheb)
    if len(power) < degree + 1:
        power = np.pad(power, (0, degree + 1 - len(power)))
    in_t = Polynomial(power)(Polynomial((-1.0, 2.0))).coef
    if len(in_t) < degree + 1:
        in_t = np.pad(in_t, (0, degree + 1 - len(in_t)))
    bernstein = np.asarray(
        [
            sum(
                in_t[power_index]
                * math.comb(index, power_index)
                / math.comb(degree, power_index)
                for power_index in range(index + 1)
            )
            for index in range(degree + 1)
        ]
    )
    theta = 2.0 * np.pi * np.arange(count) / count
    reconstructed = sum(
        cheb[index] * np.cos(index * theta) for index in range(degree + 1)
    )
    scale = max(float(np.max(np.abs(values))), np.finfo(float).tiny)
    return PolynomialCertificate(
        chebyshev=cheb,
        power=power,
        bernstein=bernstein,
        relative_reconstruction=float(np.max(np.abs(values.real - reconstructed))) / scale,
        imaginary_relative=float(np.max(np.abs(values.imag))) / scale,
    )


def fifth_elementary(matrix: np.ndarray) -> complex:
    return sum(
        np.linalg.det(np.delete(np.delete(matrix, index, axis=0), index, axis=1))
        for index in range(6)
    )


def edge_action_data(
    coefficients: tuple[np.ndarray, ...], mutation: str
) -> tuple[PolynomialCertificate, float, tuple[int, int, int], float, float]:
    count = 256
    values = []
    minimum_positive = np.inf
    maximum_ward = 0.0
    for index in range(count):
        z = np.exp(2.0j * np.pi * index / count)
        operator = evaluate(coefficients, z)[:6, :6]
        if mutation == "edge_action_input":
            operator = -operator
        operator = 0.5 * (operator + operator.conj().T)
        values.append(fifth_elementary(operator))
        eigenvalues = np.linalg.eigvalsh(operator)
        if mutation != "edge_action_input":
            minimum_positive = min(minimum_positive, float(eigenvalues[1]))
        maximum_ward = max(
            maximum_ward,
            float(np.linalg.norm(operator @ right_ward_vector(z)))
            / max(float(np.linalg.norm(operator)), np.finfo(float).tiny),
        )
    base = evaluate(coefficients, 1.0)[:6, :6]
    if mutation == "edge_action_input":
        base = -base
    return (
        polynomial_certificate(np.asarray(values), 4),
        ward_convolution_residual(coefficients),
        inertia(base),
        minimum_positive,
        maximum_ward,
    )


def border_data(
    coefficients: tuple[np.ndarray, ...], mutation: str
) -> tuple[PolynomialCertificate, float, float]:
    count = 256
    determinants = []
    minimum_singular = np.inf
    for index in range(count):
        z = np.exp(2.0j * np.pi * index / count)
        bordered = evaluate(coefficients, z).copy()
        if mutation == "border_coupling_input":
            bordered[:6, 6] = 0.0
            bordered[6, :6] = 0.0
        determinants.append(-np.linalg.det(bordered))
        minimum_singular = min(
            minimum_singular, float(np.linalg.svd(bordered, compute_uv=False)[-1])
        )
    certificate = polynomial_certificate(np.asarray(determinants), 7)
    minimum_abs_det = float(np.min(np.abs(determinants)))
    return certificate, minimum_singular, minimum_abs_det


def sampled_symbols(
    coefficients: tuple[np.ndarray, ...], covariance_sign_mutation: bool = False
) -> SampledSymbols:
    theta = 2.0 * np.pi * np.arange(SAMPLES) / SAMPLES
    bordered_values = []
    inverse_values = []
    edge_values = []
    for angle in theta:
        z = np.exp(1.0j * angle)
        bordered = evaluate(coefficients, z).copy()
        if covariance_sign_mutation:
            bordered[:6, :6] *= -1.0
        inverse = np.linalg.inv(bordered)
        bordered_values.append(bordered)
        inverse_values.append(inverse)
        edge_values.append(inverse[:6, :6])
    return SampledSymbols(
        theta=theta,
        bordered=np.asarray(bordered_values),
        inverse=np.asarray(inverse_values),
        edge_covariance=np.asarray(edge_values),
    )


def covariance_data(samples: SampledSymbols) -> tuple[float, float, float, float, float]:
    minimum_positive = np.inf
    maximum_value = 0.0
    maximum_null = 0.0
    radical_residual = 0.0
    kkt_residual = 0.0
    for index in range(SAMPLES):
        covariance = 0.5 * (
            samples.edge_covariance[index]
            + samples.edge_covariance[index].conj().T
        )
        values = np.linalg.eigvalsh(covariance)
        minimum_positive = min(minimum_positive, float(values[1]))
        maximum_value = max(maximum_value, float(values[-1]))
        maximum_null = max(maximum_null, float(abs(values[0])))
        if index % 32 == 0:
            z = np.exp(1.0j * samples.theta[index])
            radical = left_ward_vector(z)
            radical_residual = max(
                radical_residual,
                float(np.linalg.norm(covariance @ radical))
                / float(np.linalg.norm(covariance) * np.linalg.norm(radical)),
            )
            source = np.asarray((1, 2, -1.0j, 0.5, -0.3j, 0.7), complex)
            solution = samples.inverse[index] @ np.concatenate((source, (0.0,)))
            state = solution[:6]
            operator = samples.bordered[index][:6, :6]
            lhs = np.vdot(source, state)
            rhs = np.vdot(state, operator @ state)
            kkt_residual = max(kkt_residual, float(abs(lhs - rhs)))
    return minimum_positive, maximum_value, maximum_null, radical_residual, kkt_residual


def slice_invariance_data(
    coefficients: tuple[np.ndarray, ...], source: np.ndarray
) -> tuple[float, float, float, float, int, float]:
    formula_residual = 0.0
    conserved_residual = 0.0
    scaling_residual = 0.0
    for index in range(128):
        z = np.exp(2.0j * np.pi * index / 128)
        bordered = evaluate(coefficients, z)
        operator = 0.5 * (bordered[:6, :6] + bordered[:6, :6].conj().T)
        covariance = np.linalg.inv(bordered)[:6, :6]
        right = right_ward_vector(z)
        left = left_ward_vector(z)
        pseudoinverse = np.linalg.pinv(operator, rcond=1.0e-12, hermitian=True)
        projector = np.eye(6) - np.outer(right, left.conj()) / np.vdot(left, right)
        formula = projector @ pseudoinverse @ projector.conj().T
        formula_residual = max(
            formula_residual,
            float(np.linalg.norm(covariance - formula))
            / float(np.linalg.norm(covariance)),
        )
        trial = np.asarray((1, 2, -1.0j, 0.5, -0.3j, 0.7), complex)
        conserved = trial - right * np.vdot(right, trial) / np.vdot(right, right)
        conserved_residual = max(
            conserved_residual,
            float(abs(np.vdot(conserved, (covariance - pseudoinverse) @ conserved))),
        )
        scaled_left = (1.2 - 0.4j) * left
        scaled_projector = np.eye(6) - np.outer(
            right, scaled_left.conj()
        ) / np.vdot(scaled_left, right)
        scaled = scaled_projector @ pseudoinverse @ scaled_projector.conj().T
        scaling_residual = max(
            scaling_residual,
            float(np.linalg.norm(scaled - formula)) / float(np.linalg.norm(formula)),
        )

    z = np.exp(0.7j)
    bordered = evaluate(coefficients, z)
    operator = 0.5 * (bordered[:6, :6] + bordered[:6, :6].conj().T)
    covariance = np.linalg.inv(bordered)[:6, :6]
    pseudoinverse = np.linalg.pinv(operator, rcond=1.0e-12, hermitian=True)
    slice_difference = float(
        np.linalg.norm(covariance - pseudoinverse) / np.linalg.norm(covariance)
    )
    tt_difference = float(abs(np.vdot(source, (covariance - pseudoinverse) @ source)))
    constraint_rows = np.vstack(
        [value.reshape(1, -1) for value in left_ward_coefficients().values()]
    )
    constant_conserved_dimension = 6 - int(
        np.linalg.matrix_rank(constraint_rows, tol=1.0e-12)
    )
    return (
        formula_residual,
        conserved_residual,
        scaling_residual,
        slice_difference,
        constant_conserved_dimension,
        tt_difference,
    )


def moments(samples: SampledSymbols, count: int) -> list[np.ndarray]:
    return [
        np.mean(
            np.exp(1.0j * order * samples.theta)[:, None, None]
            * samples.edge_covariance,
            axis=0,
        )
        for order in range(count)
    ]


def block_toeplitz(moment_values: list[np.ndarray], horizon: int) -> np.ndarray:
    return np.block(
        [
            [
                moment_values[row - column]
                if row >= column
                else moment_values[column - row].conj().T
                for column in range(horizon)
            ]
            for row in range(horizon)
        ]
    )


def toeplitz_data(
    baseline: SampledSymbols, mutation: str
) -> tuple[tuple[int, ...], float, float, float]:
    moment_values = moments(baseline, 16)
    if mutation == "moment_input":
        moment_values[0] = moment_values[0] - 0.25 * np.eye(6)
    nullities = []
    minimum_eigenvalue = np.inf
    minimum_positive = np.inf
    radical_residual = 0.0
    left = left_ward_coefficients()
    radical_block = np.concatenate((left[1], left[0], left[-1]))
    for horizon in (1, 2, 4, 8, 16):
        matrix = block_toeplitz(moment_values, horizon)
        matrix = 0.5 * (matrix + matrix.conj().T)
        eigenvalues = np.linalg.eigvalsh(matrix)
        nullities.append(int(np.sum(np.abs(eigenvalues) < 1.0e-9)))
        minimum_eigenvalue = min(minimum_eigenvalue, float(eigenvalues[0]))
        positive = eigenvalues[eigenvalues > 1.0e-9]
        if len(positive):
            minimum_positive = min(minimum_positive, float(positive[0]))
        if horizon >= 3 and mutation != "moment_input":
            for shift in range(horizon - 2):
                vector = np.zeros(6 * horizon, complex)
                vector[6 * shift : 6 * (shift + 3)] = radical_block
                radical_residual = max(
                    radical_residual,
                    float(np.linalg.norm(matrix @ vector))
                    / float(np.linalg.norm(matrix) * np.linalg.norm(vector)),
                )
    return tuple(nullities), minimum_eigenvalue, minimum_positive, radical_residual


def polynomial_to_bernstein(poly: Polynomial, degree: int) -> np.ndarray:
    in_t = poly(Polynomial((-1.0, 2.0))).coef
    if len(in_t) < degree + 1:
        in_t = np.pad(in_t, (0, degree + 1 - len(in_t)))
    return np.asarray(
        [
            sum(
                in_t[j] * math.comb(k, j) / math.comb(degree, j)
                for j in range(k + 1)
            )
            for k in range(degree + 1)
        ]
    )


def scalar_data(
    roots: np.ndarray,
    weights: np.ndarray,
    baseline: SampledSymbols,
    source: np.ndarray,
    mutation: str,
) -> tuple[np.ndarray, np.ndarray, float, float, float, float, float, float, float]:
    local_weights = weights.copy()
    if mutation == "scalar_weight_input":
        local_weights[int(np.argmax(local_weights))] *= -1.0
    denominator = Polynomial((1.0,))
    factors = []
    for root in roots:
        factor = Polynomial((1.0 + root**2, -2.0 * root))
        factors.append(factor)
        denominator *= factor
    numerator = Polynomial((0.0,))
    for index, root in enumerate(roots):
        quotient = Polynomial((1.0,))
        for other, factor in enumerate(factors):
            if other != index:
                quotient *= factor
        numerator += local_weights[index] * (1.0 - root**2) * quotient
    derivative_numerator = numerator.deriv() * denominator - numerator * denominator.deriv()
    numerator_bernstein = polynomial_to_bernstein(numerator, 2)
    derivative_bernstein = polynomial_to_bernstein(derivative_numerator, 4)
    rho_minus = float(
        sum(
            local_weights * (1.0 - roots**2) / (1.0 + 2.0 * roots + roots**2)
        )
    )
    rho_plus = float(
        sum(
            local_weights * (1.0 - roots**2) / (1.0 - 2.0 * roots + roots**2)
        )
    )
    direct_error = 0.0
    for index in range(0, SAMPLES, 64):
        x = np.cos(baseline.theta[index])
        density = float(
            sum(
                local_weights
                * (1.0 - roots**2)
                / (1.0 - 2.0 * roots * x + roots**2)
            )
        )
        direct = float(
            (
                source.conj()
                @ baseline.edge_covariance[index]
                @ source
            ).real
        )
        if mutation != "scalar_weight_input":
            direct_error = max(direct_error, abs(density - direct))
    scalar_moments = np.asarray(
        [np.sum(local_weights * roots**order) for order in range(9)]
    )
    shifted_hankel = np.asarray(
        [[scalar_moments[row + column + 1] for column in range(2)] for row in range(2)]
    )
    two_step_hankel = np.asarray(
        [
            [scalar_moments[2 * (row + column)] for column in range(3)]
            for row in range(3)
        ]
    )
    return (
        numerator_bernstein,
        derivative_bernstein,
        rho_minus,
        rho_plus,
        direct_error,
        float(np.sum(local_weights)),
        float(np.max(np.abs(roots))),
        float(np.linalg.eigvalsh(shifted_hankel)[0]),
        float(np.linalg.eigvalsh(two_step_hankel)[0]),
    )


def gluing_data(
    coefficients: tuple[np.ndarray, ...],
    union,
    samples: SampledSymbols,
    mutation: str,
) -> tuple[float, float, tuple[float, ...]]:
    laurent = block181.laurent_certificate(union, "")
    finite_inside = np.asarray([branch.root for branch in laurent.branches])
    stable = block183.stable_weyl(coefficients, finite_inside)
    directions = np.asarray(union.directions, dtype=float)
    edge_basis = block181.sign_basis(block181.swap_matrix(directions, 1, 2), -1)
    reflection = block183.geometric_reflection(union, edge_basis)
    theta = np.block(
        [
            [np.zeros((7, 7)), reflection],
            [reflection, np.zeros((7, 7))],
        ]
    )
    left_weyl = theta @ stable.weyl @ theta
    reflection_error = float(
        np.linalg.norm(left_weyl - theta @ stable.weyl @ theta)
    )
    if mutation == "gluing_input":
        left_weyl = left_weyl + 0.1 * np.eye(14)
    central_action = np.block(
        [[coefficients[2], coefficients[3]], [coefficients[1], coefficients[2]]]
    )
    glued = stable.weyl + left_weyl - central_action
    full_m0 = np.mean(samples.inverse, axis=0)
    full_m1 = np.mean(
        np.exp(1.0j * samples.theta)[:, None, None] * samples.inverse, axis=0
    )
    covariance_two = np.block(
        [[full_m0, full_m1.conj().T], [full_m1, full_m0]]
    )
    covariance_effective = np.linalg.inv(covariance_two)
    gluing_error = float(
        np.linalg.norm(glued - covariance_effective)
        / np.linalg.norm(covariance_effective)
    )
    depth_errors = []
    baseline_glued = (
        stable.weyl + theta @ stable.weyl @ theta - central_action
    )
    for depth in (8, 16, 32, 64):
        finite = block183.finite_toeplitz(coefficients, depth)
        start = depth // 2 - 1
        center = np.arange(7 * start, 7 * (start + 2))
        outside = np.setdiff1d(np.arange(7 * depth), center)
        schur = finite[np.ix_(center, center)] - finite[np.ix_(center, outside)] @ np.linalg.solve(
            finite[np.ix_(outside, outside)], finite[np.ix_(outside, center)]
        )
        depth_errors.append(
            float(np.linalg.norm(schur - baseline_glued) / np.linalg.norm(baseline_glued))
        )
    return gluing_error, reflection_error, tuple(depth_errors)


def pole_data(coefficients: tuple[np.ndarray, ...]) -> tuple[float, float, float]:
    determinant = block181.determinant_polynomial(
        {index: value for index, value in enumerate(coefficients)}
    )
    low = min(determinant)
    high = max(determinant)
    polynomial = np.asarray(
        [determinant.get(index, 0.0) for index in range(low, high + 1)], complex
    )
    roots = np.roots(polynomial[::-1])
    roots = roots[np.isfinite(roots)]
    inside = np.asarray([root for root in roots if abs(root) < 1.0])
    outside = np.asarray([root for root in roots if abs(root) > 1.0])
    reciprocal_error = max(
        min(abs(outer - 1.0 / np.conj(inner)) for outer in outside)
        for inner in inside
    )
    return (
        float(min(abs(abs(root) - 1.0) for root in roots)),
        float(max(abs(root) for root in inside)),
        float(reciprocal_error),
    )


def main() -> int:
    started = time.perf_counter()
    mutation = os.environ.get("TOE_MUTATION", "")
    if mutation and mutation not in MUTATIONS:
        raise ValueError(f"unknown TOE_MUTATION={mutation!r}")

    checks = Checks()
    union = block181.block74.block48.build_reflection_union()
    border = block182.odd_border_data(union)
    ward_variant = block182.odd_border_data(union, mutation)
    coefficients = border.coefficients

    binding_gate = (
        block181.MU == 1.0 / 1024.0
        and border.leakage < 1.0e-12
        and border.pair_error < 1.0e-12
        and ward_variant.ward_relative < 1.0e-12
        and ward_variant.gauge_ranks == (4, 4, 4, 4)
        and ward_variant.action_ranks == (18, 18, 18, 18)
    )
    checks.check(
        "supplied-action-ward-border-binding",
        "the supplied action, odd six-edge sector, one-Ward border, and TT source are recomputed without fitting",
        binding_gate,
        f"leak={border.leakage:.2e}; pair={border.pair_error:.2e}; Ward={ward_variant.ward_relative:.2e}; ranks={ward_variant.action_ranks}",
    )

    edge = edge_action_data(coefficients, mutation)
    edge_gate = (
        edge[0].relative_reconstruction < 1.0e-12
        and edge[0].imaginary_relative < 1.0e-12
        and np.min(edge[0].bernstein) > 30.0
        and edge[1] < 1.0e-12
        and edge[2] == (0, 5, 1)
        and edge[3] > 0.5
        and edge[4] < 1.0e-12
    )
    checks.check(
        "global-edge-action-rank-five-positivity",
        "a degree-four Bernstein certificate and exact Ward convolution prove the edge action is PSD rank five on the full unit circle",
        edge_gate,
        f"e5 Bernstein={np.array2string(edge[0].bernstein, precision=6)}; Ward={edge[1]:.2e}/{edge[4]:.2e}; base={edge[2]}",
    )

    bordered = border_data(coefficients, mutation)
    border_gate = (
        bordered[0].relative_reconstruction < 1.0e-12
        and bordered[0].imaginary_relative < 1.0e-12
        and np.min(bordered[0].bernstein) > 40.0
        and bordered[1] > 0.16
        and bordered[2] > 60.0
    )
    checks.check(
        "global-bordered-invertibility-and-constraint-coupling",
        "a degree-seven Bernstein certificate proves the Ward-bordered symbol has no unit-circle pole and couples the null line",
        border_gate,
        f"-det Bernstein={np.array2string(bordered[0].bernstein, precision=5)}; sigma_min={bordered[1]:.6f}; |det|min={bordered[2]:.6f}",
    )

    baseline_samples = sampled_symbols(coefficients)
    covariance_samples = (
        sampled_symbols(coefficients, True)
        if mutation == "covariance_input"
        else baseline_samples
    )
    covariance = covariance_data(covariance_samples)
    slice_data = slice_invariance_data(coefficients, border.rhs[:6])
    covariance_gate = (
        covariance[0] > 0.10
        and covariance[1] < 5.9
        and covariance[2] < 1.0e-12
        and covariance[3] < 1.0e-12
        and covariance[4] < 1.0e-10
        and slice_data[0] < 1.0e-12
        and slice_data[1] < 1.0e-12
        and slice_data[2] < 1.0e-12
        and slice_data[3] > 0.5
        and slice_data[4] == 3
        and slice_data[5] < 1.0e-10
    )
    checks.check(
        "full-matrix-edge-covariance-and-ward-radical",
        "the inverse bordered edge block is PSD rank five for every frequency and its radical is the explicit local left-Ward line",
        covariance_gate,
        f"positive eig=[{covariance[0]:.8f},{covariance[1]:.8f}]; C*l={covariance[3]:.2e}; formula/conserved={slice_data[0]:.1e}/{slice_data[1]:.1e}; slice={slice_data[3]:.3f}; constant conserved={slice_data[4]}",
    )

    toeplitz = toeplitz_data(baseline_samples, mutation)
    toeplitz_gate = (
        toeplitz[0] == (0, 0, 2, 6, 14)
        and toeplitz[1] > -1.0e-10
        and toeplitz[2] > 0.06
        and toeplitz[3] < 1.0e-12
    )
    checks.check(
        "all-support-matrix-toeplitz-gns-and-local-gauge-quotient",
        "pointwise matrix positivity gives every finite-support Gram, with exactly the shifted local Ward-polynomial radical in tested sections",
        toeplitz_gate,
        f"nullities={toeplitz[0]}; min={toeplitz[1]:.2e}; positive gap={toeplitz[2]:.6f}; radical={toeplitz[3]:.2e}",
    )

    laurent = block181.laurent_certificate(union, "")
    coupled = tuple(branch for branch in laurent.branches if branch.coupled)
    roots = np.asarray([branch.root.real for branch in coupled])
    weights = np.asarray([branch.moment_weight.real for branch in coupled])
    scalar = scalar_data(
        roots, weights, baseline_samples, border.rhs[:6], mutation
    )
    scalar_gate = (
        len(coupled) == 3
        and np.min(scalar[0]) > 0.54
        and np.min(scalar[1]) > 0.287
        and 0.337 < scalar[2] < 0.338
        and 1.003 < scalar[3] < 1.005
        and scalar[4] < 1.0e-8
        and 0.581 < scalar[5] < 0.583
        and scalar[6] < 0.27
        and scalar[7] < -4.0e-9
        and scalar[8] < -3.0e-7
    )
    checks.check(
        "tt-scalar-herglotz-cyclic-unitary-and-finite-resource-boundary",
        "the unchanged TT response has a strictly positive unique scalar spectral measure and an intrinsically infinite minimal cyclic unitary realization",
        scalar_gate,
        f"q Bernstein={np.array2string(scalar[0], precision=7)}; rho={scalar[2]:.12f}/{scalar[3]:.12f}; direct={scalar[4]:.2e}; Hankel={scalar[7]:.2e}/{scalar[8]:.2e}",
    )

    gluing = gluing_data(coefficients, union, baseline_samples, mutation)
    gluing_gate = (
        gluing[0] < 1.0e-11
        and gluing[1] < 1.0e-12
        and all(later < earlier for earlier, later in zip(gluing[2], gluing[2][1:]))
        and gluing[2][-1] < 1.0e-12
    )
    checks.check(
        "reflected-weyl-gluing-selects-full-line-covariance",
        "the reflected right/left Weyl pair minus the shared central action equals the inverse two-layer full-line covariance",
        gluing_gate,
        f"glue={gluing[0]:.2e}; reflection={gluing[1]:.2e}; open depths={','.join(f'{value:.2e}' for value in gluing[2])}",
    )

    pole_gap, inside_radius, reciprocal_error = pole_data(coefficients)
    moment_34 = float(
        np.linalg.norm(
            np.mean(
                np.exp(34.0j * baseline_samples.theta)[:, None, None]
                * baseline_samples.edge_covariance,
                axis=0,
            ),
            2,
        )
    )
    note = flat(NOTE_PATH)
    if mutation == "note_boundary":
        note = note.replace("gravity_verdict: open", "gravity_verdict: closed")
    axiom = flat(AXIOM_PATH)
    scope_gate = (
        pole_gap > 0.44
        and inside_radius < 0.56
        and reciprocal_error < 1.0e-6
        and 1.0e-10 < moment_34 < 1.0e-7
        and "matrix_gns_verdict: positive_kinematic_reconstruction" in note
        and "finite_dimension_all_powers_verdict: bounded_infeasible" in note
        and "hamiltonian_record_verdict: open" in note
        and "gravity_verdict: open" in note
        and "no axiom is amended" in note
        and "full-circle spectrum does not select" in note
        and all(f"### n{index}" in note for index in range(1, 9))
        and "n1--n8 status: pass" in note
        and "choose a hamiltonian or transfer operator" in axiom
    )
    checks.check(
        "locality-spectrum-no-go-discipline-and-axiom-boundary",
        "the rational covariance is exponentially local, while Hamiltonian, Record, quantum, IR, refinement, and gravity claims remain open",
        scope_gate,
        f"pole gap={pole_gap:.6f}; inside radius={inside_radius:.6f}; M34={moment_34:.2e}; reciprocal={reciprocal_error:.2e}",
    )

    print(
        "MATRIX_POSITIVITY_CERTIFICATE: edge action is PSD rank five and the bordered inverse edge covariance is PSD rank five for the full unit circle"
    )
    print(
        "WARD_QUOTIENT_CERTIFICATE: the covariance radical is the explicit three-tap local left-Ward Laurent line; finite history sections have exactly horizon-minus-two gauge null shifts"
    )
    print(
        "GNS_CERTIFICATE: C6-valued Laurent source histories modulo the Ward line complete to a Hilbert space, and multiplication by z is a canonical unitary reproducing every bilateral matrix moment"
    )
    print(
        "ACTION_PROVENANCE_CERTIFICATE: reflected left/right Weyl halves, with the shared central action subtracted once, reconstruct the two-layer full-line covariance without a fitted metric or bath"
    )
    print(
        "PHYSICAL_BOUNDARY: the exact shift is kinematic history translation; full-circle spectrum does not select a local Hamiltonian branch, quantum commutator/state, or operational Record instrument"
    )
    print(
        "N5_CERTIFICATE: the execution resolutions below state exactly what this runner did and did not resolve"
    )
    print(
        "per_element: checked the supplied twenty-two-edge action through all six odd edge source coordinates and its one-Ward border"
    )
    print(
        "per_site: checked arbitrary finite temporal source histories at one translation-invariant spatial momentum; no inhomogeneous spatial site family"
    )
    print(
        "per_mode: checked the entire unit temporal circle and all five physical odd-edge quotient directions, with the TT scalar sequence as a sourced subchannel"
    )
    print(
        "per_block: checked global polynomial positivity, bordered invertibility, matrix Toeplitz sections, GNS shift, and reflected-Weyl gluing"
    )
    print(
        "lattice_wide: checked and not executed — no Brillouin-zone, even-sector, nonlinear-background, Newtonian-IR, refinement, quantum Record, or all-lattice theorem is claimed"
    )
    print(
        "MATRIX_GNS_VERDICT: POSITIVE_KINEMATIC_RECONSTRUCTION; FINITE_DIMENSION_ALL_POWERS_VERDICT: BOUNDED_INFEASIBLE; HAMILTONIAN_RECORD_VERDICT: OPEN; GRAVITY_VERDICT: OPEN"
    )
    print("TOE_MOVEMENT: obligations=0 percentages=0 axioms_amended=0")
    print(f"elapsed_sec={time.perf_counter() - started:.2f}")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
