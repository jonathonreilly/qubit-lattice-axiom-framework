#!/usr/bin/env python3
"""Exact checker for the conditional same-projected named-gap theorem."""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
import sys

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


def derive_conditional_matrix(n: int) -> tuple[sp.Matrix, int]:
    variables = tuple(sp.symbols(f"h0:{n*n}"))
    generic = sp.Matrix(n, n, variables)
    equations: list[sp.Expr] = []
    for row in range(n):
        for col in range(n):
            matrix_unit = unit(n, row, col)
            equations.extend(generic * matrix_unit - matrix_unit * generic)
    coefficient_matrix, _ = sp.linear_eq_to_matrix(equations, variables)
    nullspace = coefficient_matrix.nullspace()
    generator = sp.Matrix(n, n, list(nullspace[0]))
    pivot = next(entry for entry in generator if entry != 0)
    generator = sp.simplify(generator / pivot)
    c = sp.symbols("c", real=True)
    norm_solutions = sp.solve(sp.Eq(sp.trace((c * generator).H * (c * generator)), 1), c)
    positive = [solution for solution in norm_solutions if solution.is_nonnegative]
    return sp.simplify(positive[0] * generator), len(nullspace)


def main() -> int:
    checks = Checks()
    n = 6

    section("Conditional H-MATRIX branch")
    h_matrix, centralizer_nullity = derive_conditional_matrix(n)
    checks.check(
        "full matrix-unit commutant is one-dimensional",
        centralizer_nullity == 1,
        f"nullity={centralizer_nullity}",
    )
    checks.check(
        "positivity and HS-unit norm derive I_6/sqrt(6)",
        h_matrix == sp.eye(n) / sp.sqrt(n),
    )
    r_b = sp.simplify(h_matrix[0, 0] ** 2)
    checks.check(
        "under H-MATRIX the diagonal-overlap square is 1/6",
        r_b == sp.Rational(1, 6),
        f"R_B={r_b}",
    )

    section("Exact projected residual")
    g = sp.symbols("g_bare", real=True)
    r_oge = g**2 / 6
    residual = sp.factor(r_oge - r_b)
    checks.check(
        "conditional OGE minus Rep-B residual is (g_bare^2-1)/6",
        sp.simplify(residual - (g**2 - 1) / 6) == 0,
        f"Delta={residual}",
    )
    checks.check(
        "conditional residual is a nonzero quadratic polynomial",
        sp.Poly(residual, g).degree() == 2 and residual != 0,
    )
    samples = (
        (Fraction(1, 2), Fraction(-1, 8)),
        (Fraction(1, 1), Fraction(0, 1)),
        (Fraction(3, 2), Fraction(5, 24)),
        (Fraction(2, 1), Fraction(1, 2)),
    )
    for argument, expected in samples:
        value = argument * argument / 6 - Fraction(1, 6)
        checks.check(
            f"exact conditional sample Delta({argument})",
            value == expected,
            f"Delta={value}",
        )
    roots = sp.solve(sp.Eq(residual, 0), g)
    checks.check(
        "point equality occurs only at the two Hermitian algebraic roots",
        set(roots) == {-sp.Integer(1), sp.Integer(1)},
        f"roots={roots}",
    )

    section("Missing-H-MATRIX branch")
    unbridged_form_factor = sp.Function("f")(g)
    unbridged_residual = sp.simplify(r_oge - unbridged_form_factor**2)
    checks.check(
        "without H-MATRIX the physical Rep-B coefficient remains symbolic",
        bool(unbridged_residual.atoms(sp.Function))
        and sp.simplify(unbridged_residual - residual) != 0,
        f"unbridged_residual={unbridged_residual}",
    )
    checks.check(
        "no arbitrary-parameter identity follows from point equality",
        residual.subs(g, 1) == 0 and residual.subs(g, 2) != 0,
        f"Delta(1)={residual.subs(g, 1)}, Delta(2)={residual.subs(g, 2)}",
    )

    print(f"\nTOTAL: PASS={checks.passed}, FAIL={checks.failed}")
    return 1 if checks.failed else 0


if __name__ == "__main__":
    sys.exit(main())
