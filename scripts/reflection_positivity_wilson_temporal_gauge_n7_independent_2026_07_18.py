#!/usr/bin/env python3
"""Independent N7 resolution surface for the finite two-slice Wilson RP bridge.

This helper deliberately does not import the primary runner, its result tables,
its cache, or audit-ledger state.  It reconstructs a second evidence surface
from deterministic complex matrices and exact symbolic normalization:

* realification makes ``Re Tr(U_i U_j^dagger)`` an ordinary real Gram;
* entrywise exponentiation at nonnegative coupling is checked against its
  Schur-power series on deterministic ``SU(2)`` and ``SU(3)`` families;
* finite products and an integrated ``W diag(kappa) W^dagger`` block are
  reconstructed directly;
* positive-entry, negative-coupling, and wrong-antilinearity hostile controls
  show why the theorem needs more than pointwise positivity or finite samples.

The symbolic identities are exact algebra.  Matrix spectra and series
remainders are deterministic numerical support and are labelled accordingly.
No audit outcome is read, predicted, or applied.
"""

from __future__ import annotations

import math
from collections import Counter

import numpy as np
import sympy


AUDIT_TIMEOUT_SEC = 120
TOL = 2.0e-10

COUNTS: Counter[str] = Counter()
FAIL = 0


def check(evidence_class: str, label: str, condition: object, detail: str) -> None:
    """Record one recomputed object in an explicit evidence class."""
    global FAIL
    ok = bool(condition)
    COUNTS[evidence_class] += int(ok)
    FAIL += int(not ok)
    tag = "PASS" if ok else "FAIL"
    print(f"  [{tag}] [{evidence_class}] {label} ({detail})")


def section(title: str) -> None:
    print()
    print("-" * 92)
    print(title)
    print("-" * 92)


def realified_coordinates(matrices: list[np.ndarray]) -> np.ndarray:
    return np.asarray(
        [np.concatenate((matrix.real.ravel(), matrix.imag.ravel())) for matrix in matrices]
    )


def trace_gram(matrices: list[np.ndarray]) -> np.ndarray:
    return np.asarray(
        [
            [float(np.real(np.trace(left @ right.conj().T))) for right in matrices]
            for left in matrices
        ]
    )


def exponential_kernel(gram: np.ndarray, coupling: float) -> np.ndarray:
    return np.exp(coupling * gram)


def schur_exponential_partial(
    gram: np.ndarray, coupling: float, max_order: int
) -> np.ndarray:
    total = np.zeros_like(gram)
    power = np.ones_like(gram)
    coefficient = 1.0
    for order in range(max_order + 1):
        if order:
            power = power * gram
            coefficient *= coupling / order
        total += coefficient * power
    return total


def su2_family() -> list[np.ndarray]:
    identity = np.eye(2, dtype=complex)
    return [
        identity,
        -identity,
        np.diag([1j, -1j]),
        np.asarray([[0.0, 1.0], [-1.0, 0.0]], dtype=complex),
        identity.copy(),  # repeated element: an intentional rank-deficiency control
    ]


def su3_family() -> list[np.ndarray]:
    identity = np.eye(3, dtype=complex)
    omega = np.exp(2j * np.pi / 3.0)
    shift = np.asarray(
        [[0.0, 1.0, 0.0], [0.0, 0.0, 1.0], [1.0, 0.0, 0.0]],
        dtype=complex,
    )
    return [
        identity,
        omega * identity,
        omega**2 * identity,
        np.diag([omega, omega**2, 1.0]),
        shift,
        identity.copy(),  # repeated element
    ]


def group_family_checks(name: str, matrices: list[np.ndarray], beta: float) -> dict[str, float]:
    dimension = matrices[0].shape[0]
    alpha = beta / dimension
    identity = np.eye(dimension)
    unitary_residual = max(
        float(np.max(np.abs(matrix @ matrix.conj().T - identity)))
        for matrix in matrices
    )
    determinant_residual = max(abs(np.linalg.det(matrix) - 1.0) for matrix in matrices)

    coordinates = realified_coordinates(matrices)
    gram = trace_gram(matrices)
    coordinate_residual = float(np.max(np.abs(gram - coordinates @ coordinates.T)))
    gram_eigenvalues = np.linalg.eigvalsh((gram + gram.T) / 2.0)

    kernel = exponential_kernel(gram, alpha)
    kernel_eigenvalues = np.linalg.eigvalsh((kernel + kernel.T) / 2.0)
    schur_partial = schur_exponential_partial(gram, alpha, max_order=36)
    schur_residual = float(np.max(np.abs(kernel - schur_partial)))

    zero_kernel = exponential_kernel(gram, 0.0)
    zero_eigenvalues = np.linalg.eigvalsh((zero_kernel + zero_kernel.T) / 2.0)

    check(
        "NUMERICAL_SUPPORT",
        f"{name} deterministic matrices satisfy the group carrier",
        unitary_residual < TOL and determinant_residual < TOL,
        f"count={len(matrices)}, unitarity_residual={unitary_residual:.3e}, "
        f"determinant_residual={determinant_residual:.3e}",
    )
    check(
        "NUMERICAL_SUPPORT",
        f"{name} trace form equals a real coordinate Gram",
        coordinate_residual < TOL and gram_eigenvalues.min() >= -TOL,
        f"coordinate_residual={coordinate_residual:.3e}, "
        f"min_eig_H={gram_eigenvalues.min():+.3e}",
    )
    check(
        "NUMERICAL_SUPPORT",
        f"{name} positive-coupling entrywise exponential is PSD",
        kernel_eigenvalues.min() >= -TOL,
        f"beta={beta}, alpha=beta/N={alpha:.12g}, "
        f"min_eig_K={kernel_eigenvalues.min():+.3e}",
    )
    check(
        "NUMERICAL_SUPPORT",
        f"{name} direct exponential agrees with the Schur-power series",
        schur_residual < 2.0e-11,
        f"orders=0..36, max_residual={schur_residual:.3e}",
    )
    check(
        "BOUNDARY_EVIDENCE",
        f"{name} beta=0 kernel is the rank-one all-ones anchor",
        np.max(np.abs(zero_kernel - np.ones_like(zero_kernel))) < TOL
        and np.count_nonzero(zero_eigenvalues > TOL) == 1,
        f"rank={np.count_nonzero(zero_eigenvalues > TOL)}, "
        f"min_eig={zero_eigenvalues.min():+.3e}",
    )
    check(
        "BOUNDARY_EVIDENCE",
        f"{name} repeated elements make the finite restriction rank deficient without violating PSD",
        kernel_eigenvalues.min() >= -TOL
        and np.count_nonzero(kernel_eigenvalues < TOL) >= 1,
        f"near_zero_eigenvalues={np.count_nonzero(kernel_eigenvalues < TOL)}",
    )
    return {
        "alpha": alpha,
        "kernel_min_eigenvalue": float(kernel_eigenvalues.min()),
        "schur_residual": schur_residual,
    }


def symbolic_normalization_checks() -> None:
    beta = sympy.symbols("beta", nonnegative=True)
    n_c = sympy.symbols("N", integer=True, positive=True)
    real_part, imag_part = sympy.symbols("real_part imag_part", real=True)
    chi = real_part + sympy.I * imag_part
    chi_bar = real_part - sympy.I * imag_part
    half_residual = sympy.simplify(
        beta * (chi + chi_bar) / (2 * n_c) - beta * real_part / n_c
    )

    order = sympy.symbols("n", integer=True, nonnegative=True)
    weight = (beta / (2 * n_c)) ** order / sympy.factorial(order)
    recurrence_residual = sympy.simplify(
        (order + 1) * weight.subs(order, order + 1)
        - beta * weight / (2 * n_c)
    )
    majorant_residual = sympy.simplify(
        (beta / (2 * n_c)) ** order * (2 * n_c) ** order
        / sympy.factorial(order)
        - beta**order / sympy.factorial(order)
    )

    check(
        "EXACT_ALGEBRA",
        "Wilson beta/N and character factor one-half are identical",
        half_residual == 0,
        f"symbolic_residual={half_residual}",
    )
    check(
        "EXACT_ALGEBRA",
        "all-order scalar weights obey a division-free nonnegative recurrence",
        recurrence_residual == 0,
        f"(n+1)w_(n+1)-(beta/(2N))w_n={recurrence_residual}",
    )
    check(
        "EXACT_ALGEBRA",
        "tensor-dimension majorant reduces termwise to beta^n/n!",
        majorant_residual == 0,
        "sum_n beta^n/n! = exp(beta) for R=F with dim(F)=N",
    )


def product_and_integrated_block() -> None:
    matrices = su3_family()
    gram = trace_gram(matrices)
    first = exponential_kernel(gram, 0.7 / 3.0)
    permutation = [2, 4, 1, 5, 0, 3]
    second = exponential_kernel(gram[np.ix_(permutation, permutation)], 1.1 / 3.0)
    product = first * second
    product_min = float(np.linalg.eigvalsh((product + product.T) / 2.0).min())

    phases = np.arange(product.shape[0], dtype=float)
    observables = np.asarray(
        [
            np.ones(product.shape[0], dtype=complex),
            np.exp(1j * phases / 3.0),
            np.asarray([np.trace(matrix) for matrix in matrices]),
            np.asarray([matrix[0, 1] for matrix in matrices]),
        ]
    )
    half_weight = np.exp(0.05 * np.real(np.asarray([np.trace(m) for m in matrices])))
    weighted_observables = observables * half_weight[None, :]
    direct = np.conj(weighted_observables) @ product @ weighted_observables.T

    kappa, eigenvectors = np.linalg.eigh((product + product.T) / 2.0)
    factor_coordinates = np.conj(weighted_observables) @ eigenvectors
    factored = factor_coordinates @ np.diag(kappa) @ factor_coordinates.conj().T
    factor_residual = float(np.max(np.abs(direct - factored)))
    direct_min = float(np.linalg.eigvalsh((direct + direct.conj().T) / 2.0).min())
    partition = float(
        np.ones(product.shape[0]) @ product @ np.ones(product.shape[0])
    ) / (product.shape[0] ** 2)

    check(
        "NUMERICAL_SUPPORT",
        "two spatial-link factors compose by a Schur product",
        product_min >= -TOL,
        f"factor_count=2, configuration_count={product.shape[0]}, "
        f"min_eig_product={product_min:+.3e}",
    )
    check(
        "NUMERICAL_SUPPORT",
        "integrated block equals W diag(kappa) W^dagger",
        factor_residual < TOL and direct_min >= -TOL,
        f"observables={observables.shape[0]}, factor_residual={factor_residual:.3e}, "
        f"min_eig_G={direct_min:+.3e}",
    )
    check(
        "BOUNDARY_EVIDENCE",
        "finite normalized partition function is strictly positive and finite",
        math.isfinite(partition) and partition > 0.0,
        f"normalized_counting_measure_Z={partition:.12g}",
    )


def hostile_controls() -> dict[str, float]:
    positive_entry_matrix = np.asarray([[1.0, 2.0], [2.0, 1.0]])
    positive_entry_min = float(np.linalg.eigvalsh(positive_entry_matrix).min())

    su2 = su2_family()[:2]
    su2_negative = exponential_kernel(trace_gram(su2), -0.1)
    su2_negative_min = float(np.linalg.eigvalsh(su2_negative).min())

    su3 = su3_family()[:3]
    su3_negative = exponential_kernel(trace_gram(su3), -0.1)
    su3_negative_min = float(np.linalg.eigvalsh(su3_negative).min())

    wrong_feature = np.asarray([[1.0, 1.0], [1j, -1j]])
    right_reflection = wrong_feature @ wrong_feature.conj().T
    wrong_reflection = wrong_feature @ wrong_feature.T
    right_min = float(np.linalg.eigvalsh(right_reflection).min())
    wrong_min = float(
        np.linalg.eigvalsh((wrong_reflection + wrong_reflection.conj().T) / 2.0).min()
    )

    check(
        "BOUNDARY_EVIDENCE",
        "pointwise-positive entries alone do not imply PSD",
        positive_entry_matrix.min() > 0.0 and positive_entry_min < 0.0,
        f"positive_entry_min={positive_entry_matrix.min():.1f}, min_eig={positive_entry_min:+.1f}",
    )
    check(
        "BOUNDARY_EVIDENCE",
        "negative coupling fails on a deterministic SU(2) restriction",
        su2_negative_min < -1.0e-3,
        f"alpha=-0.1, min_eig={su2_negative_min:+.6e}",
    )
    check(
        "BOUNDARY_EVIDENCE",
        "negative coupling fails on the SU(3) center restriction",
        su3_negative_min < -1.0e-3,
        f"alpha=-0.1, min_eig={su3_negative_min:+.6e}",
    )
    check(
        "BOUNDARY_EVIDENCE",
        "dropping reflection antilinearity changes W W^dagger to a non-PSD W W^T block",
        right_min >= -TOL and wrong_min < -1.0e-3,
        f"right_min={right_min:+.3e}, wrong_min={wrong_min:+.3e}",
    )
    return {
        "positive_entry_min": positive_entry_min,
        "su2_negative_min": su2_negative_min,
        "su3_negative_min": su3_negative_min,
        "wrong_reflection_min": wrong_min,
    }


def run_independent_surface() -> int:
    """Run the standalone reconstruction; callable by the primary independent mode."""
    print("=" * 92)
    print("Independent N7 resolution surface: finite two-slice pure-gauge Wilson RP")
    print("No primary-runner import, result table, cache text, target boolean, or audit verdict")
    print("=" * 92)

    section("Exact algebra: coupling and all-order majorant normalization")
    symbolic_normalization_checks()

    section("Deterministic complex-matrix reconstructions")
    su2 = group_family_checks("SU(2)", su2_family(), beta=1.4)
    su3 = group_family_checks("SU(3)", su3_family(), beta=1.4)

    section("Finite product and integrated Gram reconstruction")
    product_and_integrated_block()

    section("Hostile controls and N7 resolutions")
    hostile = hostile_controls()
    print(
        "  N7_STEELMAN objection=pointwise positivity is insufficient; "
        f"resolution=positive-entry control has min_eig={hostile['positive_entry_min']:+.1f}, "
        "while the proved route uses the real Gram and Schur powers."
    )
    print(
        "  N7_STEELMAN objection=finite SU(2)/SU(3) restrictions do not prove all SU(N); "
        f"resolution=agreed, samples are support only (mins {su2['kernel_min_eigenvalue']:+.3e}, "
        f"{su3['kernel_min_eigenvalue']:+.3e}); the universal theorem route additionally "
        "requires nonnegative tensor multiplicities, while this helper independently "
        "recomputes the symbolic beta/N normalization and exp(beta) majorant."
    )
    print(
        "  N7_STEELMAN objection=negative coupling or linear reflection may fail; "
        f"resolution=hostile mins SU2={hostile['su2_negative_min']:+.3e}, "
        f"SU3={hostile['su3_negative_min']:+.3e}, wrong_reflection="
        f"{hostile['wrong_reflection_min']:+.3e}; theorem keeps beta>=0 and antilinear Theta."
    )
    print(
        "  N7_STEELMAN objection=temporal gauge was not globally derived; "
        "resolution=not claimed: U0=identity is an explicit datum of the finite open two-slice carrier."
    )

    section("Summary")
    total_pass = sum(COUNTS.values())
    print(
        "EVIDENCE_COUNTS "
        f"exact_algebra={COUNTS['EXACT_ALGEBRA']} "
        f"numerical_support={COUNTS['NUMERICAL_SUPPORT']} "
        f"boundary_evidence={COUNTS['BOUNDARY_EVIDENCE']} failures={FAIL}"
    )
    print(f"TOTAL: {total_pass} PASS / {FAIL} FAIL")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(run_independent_surface())
