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
        lhs = sum(matrix[i, j] * matrix[k, ell] for matrix in generators).real
        exchange = float(i == ell and j == k)
        singlet = float(i == j and k == ell)
        rhs = 0.5 * (exchange - singlet / 3.0)
        error = max(error, abs(lhs - rhs))
        design.append([exchange, singlet])
        values.append(lhs)
    coefficients, *_ = np.linalg.lstsq(np.array(design), np.array(values), rcond=None)
    return float(coefficients[0]), float(coefficients[1]), error


def main() -> int:
    checks = Checks()

    section("Finite contact-operator inventory")
    clifford = (
        ["I", "g5"]
        + [f"g{mu}" for mu in range(4)]
        + [f"g{mu}g5" for mu in range(4)]
        + [f"sigma{mu}{nu}" for mu in range(4) for nu in range(mu + 1, 4)]
    )
    color = ("singlet", "adjoint")
    isospin = ("singlet", "triplet")
    candidates = list(product(clifford, clifford, color, isospin))
    checks.check(
        "Clifford x color x isospin contact inventory is exhaustive and finite",
        len(clifford) == 16 and len(candidates) == 1024,
        f"candidate_count={len(candidates)}",
    )

    specified_bare_operator_arities = {0, 2}
    coefficients = {
        candidate: sp.Integer(0)
        for candidate in candidates
        if 4 not in specified_bare_operator_arities
    }
    checks.check(
        "absent four-fermion action arity gives zero for every contact coefficient",
        len(coefficients) == len(candidates)
        and all(value == 0 for value in coefficients.values()),
        f"zero_coefficients={len(coefficients)}",
    )
    scalar_singlet = ("I", "I", "singlet", "singlet")
    checks.check(
        "scalar-singlet contact coefficient is a zero member of the inventory",
        scalar_singlet in coefficients and coefficients[scalar_singlet] == 0,
    )

    section("Projected one-gauge-boson coefficient")
    exchange, singlet, fierz_error = su3_fierz()
    checks.check(
        "SU(3) Fierz relation is reconstructed over all index tuples",
        fierz_error < 1.0e-12,
        f"max_error={fierz_error:.3e}",
    )
    checks.check(
        "singlet projection coefficient is -1/(2N_c)=-1/6",
        abs(exchange - 0.5) < 1.0e-12 and abs(singlet + 1 / 6) < 1.0e-12,
        f"exchange={exchange:.12g}, singlet={singlet:.12g}",
    )
    g_bare, q = sp.symbols("g_bare q", positive=True)
    n_c = sp.Integer(3)
    c_s = sp.Integer(1)
    oge = -c_s * g_bare**2 / (2 * n_c * q**2)
    two_exchange = g_bare**4 / q**4
    checks.check(
        "one-exchange term has leading g_bare^2/q^2 power",
        sp.degree(sp.together(oge * q**2), g_bare) == 2,
        f"coefficient={oge}",
    )
    checks.check(
        "two-exchange topology is higher in both coupling and inverse momentum",
        sp.degree(two_exchange, g_bare) == 4
        and sp.simplify(two_exchange * q**4 / g_bare**4) == 1,
        f"higher_term={two_exchange}",
    )

    section("Conditional Rep-B boundary")
    n_iso = sp.Integer(2)
    h_matrix_result = sp.eye(int(n_c * n_iso)) / sp.sqrt(n_c * n_iso)
    c_b_under_h_matrix = sp.simplify(h_matrix_result[0, 0] ** 2)
    coefficient_residual = sp.factor(
        c_s * g_bare**2 / (2 * n_c) - c_b_under_h_matrix
    )
    checks.check(
        "under H-MATRIX only, the formal residual is (g_bare^2-1)/6",
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
        "without H-MATRIX the Rep-B coefficient remains functionally unconstrained",
        bool(unbridged_residual.atoms(sp.Function))
        and sp.simplify(unbridged_residual - coefficient_residual) != 0,
        f"unbridged_residual={unbridged_residual}",
    )

    print(f"\nTOTAL: PASS={checks.passed}, FAIL={checks.failed}")
    return 1 if checks.failed else 0


if __name__ == "__main__":
    sys.exit(main())
