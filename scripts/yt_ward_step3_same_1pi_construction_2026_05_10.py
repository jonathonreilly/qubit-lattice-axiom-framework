#!/usr/bin/env python3
"""Exact checker for the doubly conditional Step-3 coefficient theorem."""

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


def unit(n: int, row: int, col: int) -> sp.Matrix:
    out = sp.zeros(n)
    out[row, col] = 1
    return out


def centralizer_basis(n: int) -> list[sp.Matrix]:
    variables = tuple(sp.symbols(f"h0:{n * n}"))
    matrix = sp.Matrix(n, n, variables)
    equations: list[sp.Expr] = []
    for row in range(n):
        for col in range(n):
            generator = unit(n, row, col)
            equations.extend(matrix * generator - generator * matrix)
    coefficient_matrix, _ = sp.linear_eq_to_matrix(equations, variables)
    return coefficient_matrix.nullspace()


def derive_h_matrix(n: int) -> tuple[sp.Matrix, list[sp.Expr]]:
    basis = centralizer_basis(n)
    vector = basis[0]
    generator = sp.Matrix(n, n, list(vector))
    pivot = next(entry for entry in generator if entry != 0)
    generator = sp.simplify(generator / pivot)
    c = sp.symbols("c", real=True)
    branches = sp.solve(sp.Eq(sp.trace((c * generator).H * (c * generator)), 1), c)
    positive = [branch for branch in branches if branch.is_nonnegative]
    return sp.simplify(positive[0] * generator), branches


def su3_fierz_coefficients() -> tuple[float, float, float]:
    l1 = np.array([[0, 1, 0], [1, 0, 0], [0, 0, 0]], dtype=complex)
    l2 = np.array([[0, -1j, 0], [1j, 0, 0], [0, 0, 0]], dtype=complex)
    l3 = np.diag([1, -1, 0]).astype(complex)
    l4 = np.array([[0, 0, 1], [0, 0, 0], [1, 0, 0]], dtype=complex)
    l5 = np.array([[0, 0, -1j], [0, 0, 0], [1j, 0, 0]], dtype=complex)
    l6 = np.array([[0, 0, 0], [0, 0, 1], [0, 1, 0]], dtype=complex)
    l7 = np.array([[0, 0, 0], [0, 0, -1j], [0, 1j, 0]], dtype=complex)
    l8 = np.diag([1, 1, -2]).astype(complex) / np.sqrt(3.0)
    generators = [matrix / 2.0 for matrix in (l1, l2, l3, l4, l5, l6, l7, l8)]
    rows: list[list[float]] = []
    values: list[float] = []
    residual = 0.0
    for i, j, k, ell in product(range(3), repeat=4):
        lhs = sum(matrix[i, j] * matrix[k, ell] for matrix in generators).real
        exchange = float(i == ell and j == k)
        singlet = float(i == j and k == ell)
        rhs = 0.5 * (exchange - singlet / 3.0)
        residual = max(residual, abs(lhs - rhs))
        rows.append([exchange, singlet])
        values.append(lhs)
    coefficients, *_ = np.linalg.lstsq(np.array(rows), np.array(values), rcond=None)
    return float(coefficients[0]), float(coefficients[1]), residual


def main() -> int:
    checks = Checks()
    n_c = sp.Integer(3)
    n_iso = sp.Integer(2)
    n = int(n_c * n_iso)

    section("H-MATRIX conditional reconstruction")
    h_matrix, norm_branches = derive_h_matrix(n)
    checks.check(
        "matrix-unit constraints and positivity derive I_6/sqrt(6)",
        h_matrix == sp.eye(n) / sp.sqrt(n),
        f"norm_branches={norm_branches}",
    )
    overlaps = [sp.simplify(h_matrix[index, index]) for index in range(n)]
    checks.check(
        "conditional diagonal expectations are uniformly 1/sqrt(6)",
        all(sp.simplify(value - 1 / sp.sqrt(n)) == 0 for value in overlaps),
        f"overlaps={overlaps}",
    )

    section("Independent SU(3) coefficient reconstruction")
    exchange, singlet, residual_error = su3_fierz_coefficients()
    checks.check(
        "SU(3) Fierz tensor is reconstructed over every index tuple",
        residual_error < 1.0e-12,
        f"max_error={residual_error:.3e}",
    )
    checks.check(
        "exchange and singlet coefficients are 1/2 and -1/6",
        abs(exchange - 0.5) < 1.0e-12 and abs(singlet + 1 / 6) < 1.0e-12,
        f"exchange={exchange:.12g}, singlet={singlet:.12g}",
    )

    section("Conditional coefficient algebra")
    g_bare = sp.symbols("g_bare", real=True)
    c_s = sp.symbols("c_S", real=True)
    c_a = c_s * g_bare**2 / (2 * n_c)
    c_b = sp.simplify(h_matrix[0, 0] ** 2)
    coefficient_residual = sp.factor(c_a - c_b)
    expected = (n_iso * c_s * g_bare**2 - 2) / (2 * n_c * n_iso)
    checks.check(
        "H-MATRIX gives C_B=1/(N_c N_iso)",
        sp.simplify(c_b - 1 / (n_c * n_iso)) == 0,
        f"C_B={c_b}",
    )
    checks.check(
        "formal Rep-A minus Rep-B residual is derived exactly",
        sp.simplify(coefficient_residual - expected) == 0,
        f"residual={coefficient_residual}",
    )
    gate = sp.solve(sp.Eq(coefficient_residual, 0), g_bare**2)
    checks.check(
        "SAME-1PI equality condition yields c_S g_bare^2=2/N_iso",
        len(gate) == 1 and sp.simplify(gate[0] - 2 / (c_s * n_iso)) == 0,
        f"g_bare^2 solutions={gate}",
    )
    canonical_residual = sp.simplify(coefficient_residual.subs(c_s, 1))
    checks.check(
        "arithmetic specialization has residual (g_bare^2-1)/6",
        sp.simplify(canonical_residual - (g_bare**2 - 1) / 6) == 0,
        f"residual={canonical_residual}",
    )
    checks.check(
        "without SAME-1PI the off-surface residual remains nonzero",
        canonical_residual.subs(g_bare, 2) == sp.Rational(1, 2)
        and sp.Poly(canonical_residual, g_bare).degree() == 2,
        f"residual(g_bare=2)={canonical_residual.subs(g_bare, 2)}",
    )

    section("Missing H-MATRIX branch")
    f = sp.Function("f")(g_bare)
    unbridged_residual = sp.simplify(c_a - f**2)
    checks.check(
        "without H-MATRIX the Rep-B coefficient remains an unconstrained function",
        bool(unbridged_residual.atoms(sp.Function))
        and sp.simplify(unbridged_residual - coefficient_residual) != 0,
        f"unbridged_residual={unbridged_residual}",
    )

    print(f"\nTOTAL: PASS={checks.passed}, FAIL={checks.failed}")
    return 1 if checks.failed else 0


if __name__ == "__main__":
    sys.exit(main())
