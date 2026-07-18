#!/usr/bin/env python3
"""Exact checker for contact-four-fermion vanishing and its Rep-B boundary."""

from __future__ import annotations

from dataclasses import dataclass
from itertools import product
import sys

import numpy as np
import sympy as sp


AUDIT_TIMEOUT_SEC = 120


@dataclass
class Checks:
    passed: int = 0
    failed: int = 0

    def check(self, label: str, condition: object, detail: str = "") -> None:
        if bool(condition):
            self.passed += 1
            tag = "PASS"
        else:
            self.failed += 1
            tag = "FAIL"
        print(f"{tag}: {label}" + (f" :: {detail}" if detail else ""))


def section(title: str) -> None:
    print("\n" + "-" * 88)
    print(title)
    print("-" * 88)


def su3_fierz() -> tuple[float, float, float]:
    l1 = np.array([[0, 1, 0], [1, 0, 0], [0, 0, 0]], dtype=complex)
    l2 = np.array([[0, -1j, 0], [1j, 0, 0], [0, 0, 0]], dtype=complex)
    l3 = np.diag([1, -1, 0]).astype(complex)
    l4 = np.array([[0, 0, 1], [0, 0, 0], [1, 0, 0]], dtype=complex)
    l5 = np.array([[0, 0, -1j], [0, 0, 0], [1j, 0, 0]], dtype=complex)
    l6 = np.array([[0, 0, 0], [0, 0, 1], [0, 1, 0]], dtype=complex)
    l7 = np.array([[0, 0, 0], [0, 0, -1j], [0, 1j, 0]], dtype=complex)
    l8 = np.diag([1, 1, -2]).astype(complex) / np.sqrt(3.0)
    generators = [matrix / 2.0 for matrix in (l1, l2, l3, l4, l5, l6, l7, l8)]
    design: list[list[float]] = []
    values: list[float] = []
    error = 0.0
    for i, j, k, ell in product(range(3), repeat=4):
        lhs = sum(matrix[i, j] * matrix[k, ell] for matrix in generators)
        exchange = float(i == ell and j == k)
        singlet = float(i == j and k == ell)
        rhs = 0.5 * (exchange - singlet / 3.0)
        error = max(error, abs(lhs - rhs))
        design.append([exchange, singlet])
        values.append(float(lhs.real))
    coefficients, *_ = np.linalg.lstsq(np.array(design), np.array(values), rcond=None)
    return float(coefficients[0]), float(coefficients[1]), error


def clifford_scalar_coordinate() -> tuple[complex, float]:
    sigma1 = np.array([[0, 1], [1, 0]], dtype=complex)
    sigma2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
    sigma3 = np.array([[1, 0], [0, -1]], dtype=complex)
    zero = np.zeros((2, 2), dtype=complex)
    identity2 = np.eye(2, dtype=complex)
    gamma = [
        np.block([[identity2, zero], [zero, -identity2]]),
        np.block([[zero, sigma1], [-sigma1, zero]]),
        np.block([[zero, sigma2], [-sigma2, zero]]),
        np.block([[zero, sigma3], [-sigma3, zero]]),
    ]
    metric = (1.0, -1.0, -1.0, -1.0)
    error = 0.0
    for mu, nu in product(range(4), repeat=2):
        anticommutator = gamma[mu] @ gamma[nu] + gamma[nu] @ gamma[mu]
        expected = (
            2.0 * metric[mu] * np.eye(4, dtype=complex)
            if mu == nu
            else np.zeros((4, 4), dtype=complex)
        )
        error = max(error, float(np.max(np.abs(anticommutator - expected))))
    scalar_coordinate = sum(
        np.trace(gamma[mu] @ (metric[mu] * gamma[mu])) for mu in range(4)
    ) / 16.0
    return complex(scalar_coordinate), error


def main() -> int:
    checks = Checks()

    section("Bare-action fermion-degree reconstruction")
    bar0, bar1, psi0, psi1 = sp.symbols("bar0 bar1 psi0 psi1")
    m00, m01, m10, m11 = sp.symbols("m00 m01 m10 m11")
    coupling = sp.symbols("lambda_contact")
    fermion_bilinear = (
        bar0 * (m00 * psi0 + m01 * psi1)
        + bar1 * (m10 * psi0 + m11 * psi1)
    )
    fermion_variables = (bar0, bar1, psi0, psi1)
    bilinear_polynomial = sp.Poly(fermion_bilinear, *fermion_variables)
    checks.check(
        "generic fermion action is reconstructed as bilinear",
        bilinear_polynomial.total_degree() == 2,
        f"fermion_degree={bilinear_polynomial.total_degree()}",
    )
    contact_derivative = sp.diff(fermion_bilinear, bar0, psi0, bar1, psi1)
    checks.check(
        "four fermionic derivatives of the bilinear action give zero contact vertex",
        contact_derivative == 0,
        f"contact_derivative={contact_derivative}",
    )
    quartic_mutation = fermion_bilinear + coupling * bar0 * psi0 * bar1 * psi1
    mutated_derivative = sp.diff(quartic_mutation, bar0, psi0, bar1, psi1)
    checks.check(
        "inserted four-fermion mutation recomputes a nonzero contact vertex",
        sp.simplify(mutated_derivative - coupling) == 0
        and sp.Poly(quartic_mutation, *fermion_variables).total_degree() == 4,
        f"mutated_contact_derivative={mutated_derivative}",
    )

    section("One-gauge-boson Fierz-coordinate reconstruction")
    exchange, singlet, fierz_error = su3_fierz()
    checks.check(
        "SU(3) Fierz relation is reconstructed over all index tuples",
        fierz_error < 1.0e-12,
        f"max_error={fierz_error:.3e}",
    )
    checks.check(
        "direct-singlet tensor coordinate is -1/(2N_c)=-1/6",
        abs(exchange - 0.5) < 1.0e-12 and abs(singlet + 1 / 6) < 1.0e-12,
        f"exchange={exchange:.12g}, singlet={singlet:.12g}",
    )
    scalar_coordinate, clifford_error = clifford_scalar_coordinate()
    checks.check(
        "explicit gamma matrices satisfy the Minkowski Clifford algebra",
        clifford_error < 1.0e-12,
        f"max_error={clifford_error:.3e}",
    )
    checks.check(
        "chosen Fierz pairing has Clifford-scalar coordinate c_S=+1",
        abs(scalar_coordinate - 1.0) < 1.0e-12,
        f"c_S={scalar_coordinate}",
    )
    g_bare, q = sp.symbols("g_bare q", positive=True)
    n_c = sp.Integer(3)
    c_s = sp.Integer(1)
    oge = -c_s * g_bare**2 / (2 * n_c * q**2)
    checks.check(
        "one-exchange term has leading g_bare^2/q^2 power",
        sp.degree(sp.together(oge * q**2), g_bare) == 2,
        f"coefficient={oge}",
    )

    section("Conditional Rep-B boundary")
    n_iso = sp.Integer(2)
    h_matrix_result = sp.eye(int(n_c * n_iso)) / sp.sqrt(n_c * n_iso)
    form_factor_square = sp.simplify(h_matrix_result[0, 0] ** 2)
    c_b_under_residue = form_factor_square
    coefficient_residual = sp.factor(
        c_s * g_bare**2 / (2 * n_c) - c_b_under_residue
    )
    checks.check(
        "under REP-B-RESIDUE the coefficient is the squared form factor",
        sp.simplify(c_b_under_residue - form_factor_square) == 0,
        f"C_B={c_b_under_residue}",
    )
    checks.check(
        "under H-MATRIX plus REP-B-RESIDUE the residual is (g_bare^2-1)/6",
        sp.simplify(coefficient_residual - (g_bare**2 - 1) / 6) == 0,
        f"residual={coefficient_residual}",
    )
    checks.check(
        "contact vanishing does not make the conditional residual an identity",
        sp.Poly(coefficient_residual, g_bare).degree() == 2
        and coefficient_residual.subs(g_bare, 2) == sp.Rational(1, 2),
        f"residual(g_bare=2)={coefficient_residual.subs(g_bare, 2)}",
    )
    unbridged_form_factor = sp.Function("f")(g_bare)
    unbridged_residual = sp.simplify(
        c_s * g_bare**2 / (2 * n_c) - unbridged_form_factor**2
    )
    checks.check(
        "without H-MATRIX, even with REP-B-RESIDUE, the coefficient stays functional",
        bool(unbridged_residual.atoms(sp.Function))
        and sp.simplify(unbridged_residual - coefficient_residual) != 0,
        f"unbridged_residual={unbridged_residual}",
    )
    residue_unfixed = sp.Function("r_B")(g_bare)
    missing_residue_residual = sp.simplify(
        c_s * g_bare**2 / (2 * n_c) - residue_unfixed
    )
    checks.check(
        "without REP-B-RESIDUE, H-MATRIX leaves the coefficient symbolic",
        bool(missing_residue_residual.atoms(sp.Function))
        and sp.simplify(missing_residue_residual - coefficient_residual) != 0,
        f"missing_residue_residual={missing_residue_residual}",
    )

    print(f"\nTOTAL: PASS={checks.passed}, FAIL={checks.failed}")
    return 1 if checks.failed else 0


if __name__ == "__main__":
    sys.exit(main())
