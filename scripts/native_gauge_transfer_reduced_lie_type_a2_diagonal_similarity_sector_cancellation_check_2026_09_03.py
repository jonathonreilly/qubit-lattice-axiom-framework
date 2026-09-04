#!/usr/bin/env python3
"""Exact reduced Lie-type A2 diagonal similarity-sector cancellation.

The runner is self-contained and reads no repository input. It proves one
polynomial identity and one finite-dimensional perturbation lemma. The symbol
``T2_diag`` denotes only the declared diagonal-multiplier/similarity-sector
coefficient; it is not a full saddle coefficient and contains no heat term.

Output is fail-closed: one PASS/FAIL line per check, then
``TOTAL: PASS=N FAIL=M``. The process exits nonzero whenever FAIL is nonzero.
"""
from __future__ import annotations

import itertools

import sympy as sp


AUDIT_TIMEOUT_SEC = 120

PASS = 0
FAIL = 0


def check(name: str, condition: bool) -> None:
    """Evaluate and print one fail-closed check."""
    global PASS, FAIL
    if bool(condition):
        PASS += 1
        print(f"PASS: {name}")
    else:
        FAIL += 1
        print(f"FAIL: {name}")


def matrix_coefficient(matrix: sp.Matrix, symbol: sp.Symbol, degree: int) -> sp.Matrix:
    return matrix.applyfunc(lambda value: sp.expand(value).coeff(symbol, degree))


def main() -> int:
    print("[Part 1] exact reduced Lie-type A2 polynomial identities")
    x, y = sp.symbols("x y", real=True)
    h = x * y * (x + y) / 2
    q = x**2 + x * y + y**2
    u = x + y
    g1 = (u**2 + 2 * x * y) / 2
    p1 = sp.expand(g1 - 3 * u * h)
    p2 = sp.expand(
        sp.Rational(3, 2) * u
        - 3 * u * g1
        + sp.Rational(9, 2) * u**2 * h
    )
    w = h * sp.exp(-q)

    def r(poly: sp.Expr) -> sp.Expr:
        return sp.diff(poly, x) + sp.diff(poly, y)

    def ell(poly: sp.Expr) -> sp.Expr:
        return sp.Rational(1, 3) * (
            sp.diff(poly, x, 2)
            - sp.diff(poly, x, y)
            + sp.diff(poly, y, 2)
        )

    check("R h = (u^2+2xy)/2", sp.expand(r(h) - g1) == 0)
    check("R q = 3u", sp.expand(r(q) - 3 * u) == 0)
    check(
        "R(h exp(-q)) = p1 exp(-q)",
        sp.simplify(sp.exp(q) * r(w) - p1) == 0,
    )
    p2_identity = sp.simplify(
        sp.exp(q) * (p2 * sp.exp(-q) - sp.Rational(1, 2) * r(r(w)) - 3 * w)
    )
    check("p2 exp(-q) = (1/2)R^2(h exp(-q)) + 3h exp(-q)", p2_identity == 0)
    derived_shift = sp.simplify(
        (p2 * sp.exp(-q) - sp.Rational(1, 2) * r(r(w))) / w
    )
    check("the residual multiplier is the constant 3", derived_shift == 3)

    monomials = [x**i * y**j for i in range(9) for j in range(9 - i)]
    coefficients = sp.symbols(f"c0:{len(monomials)}")
    generic = sum(c * m for c, m in zip(coefficients, monomials))
    check(
        "[R,L]=0 on a generic bivariate polynomial of total degree at most 8",
        sp.expand(r(ell(generic)) - ell(r(generic))) == 0,
    )

    check(
        "mutation: changing the one-half polynomial coefficient is detected",
        sp.simplify(
            sp.exp(q) * (p2 * sp.exp(-q) - r(r(w)) - 3 * w)
        )
        != 0,
    )
    check(
        "mutation: changing the common residual scalar is detected",
        sp.simplify(
            sp.exp(q)
            * (p2 * sp.exp(-q) - sp.Rational(1, 2) * r(r(w)) - 2 * w)
        )
        != 0,
    )

    print("[Part 2] exact finite-dimensional perturbation lemma")
    eigenvalues = [sp.Integer(v) for v in (2, 3, 5, 7, 11)]
    t0 = sp.diag(*eigenvalues)
    raw = sp.Matrix(
        [
            [0, 2, -1, 3, 0],
            [4, 0, 5, -2, 1],
            [2, -3, 0, 1, 4],
            [1, 2, -5, 0, 3],
            [-2, 1, 0, 4, 0],
        ]
    )
    rmat = raw - raw.T
    t1 = rmat * t0 - t0 * rmat
    d2 = sp.Rational(1, 2) * (rmat * t1 - t1 * rmat)
    t2_diag = d2 + derived_shift * t0

    check("R is exactly skew-symmetric", rmat.T == -rmat)
    check("T1=[R,T0] is exactly symmetric", t1.T == t1)
    check("D2=(1/2)[R,[R,T0]] is exactly symmetric", d2.T == d2)
    check("T2_diag-D2=3T0 exactly", t2_diag - d2 == 3 * t0)

    mixing_terms: list[sp.Expr] = []
    corrections: list[sp.Expr] = []
    relative: list[sp.Expr] = []
    for i, mu_i in enumerate(eigenvalues):
        mixing = sum(
            t1[k, i] ** 2 / (mu_i - eigenvalues[k])
            for k in range(len(eigenvalues))
            if k != i
        )
        mixing = sp.simplify(mixing)
        correction = sp.simplify(t2_diag[i, i] + mixing)
        mixing_terms.append(mixing)
        corrections.append(correction)
        relative.append(sp.simplify(correction / mu_i))
        check(
            f"state {i}: mixing cancels the diagonal double-commutator term",
            sp.simplify(mixing + d2[i, i]) == 0,
        )

    check("all five unnormalized corrections equal 3 mu_i",
          corrections == [3 * value for value in eigenvalues])
    check("all five relative corrections equal 3", relative == [sp.Integer(3)] * 5)
    check(
        "all ten pairwise relative corrections cancel",
        all(sp.simplify(relative[i] - relative[j]) == 0
            for i, j in itertools.combinations(range(5), 2)),
    )

    eps = sp.Symbol("eps")
    identity = sp.eye(t0.rows)
    left = identity + eps * rmat + eps**2 * rmat**2 / 2
    right = identity - eps * rmat + eps**2 * rmat**2 / 2
    expanded = sp.expand(left * t0 * right)
    check(
        "similarity expansion has first coefficient [R,T0]",
        matrix_coefficient(expanded, eps, 1) == t1,
    )
    check(
        "similarity expansion has second coefficient D2",
        matrix_coefficient(expanded, eps, 2) == d2,
    )

    wrong_d2 = -d2
    wrong_d2_relative = [
        sp.simplify((wrong_d2[i, i] + 3 * eigenvalues[i] + mixing_terms[i]) / eigenvalues[i])
        for i in range(5)
    ]
    check(
        "mutation: reversing the double-commutator order is detected",
        wrong_d2_relative != [sp.Integer(3)] * 5,
    )
    wrong_mixing_relative = [
        sp.simplify((t2_diag[i, i] - mixing_terms[i]) / eigenvalues[i])
        for i in range(5)
    ]
    check(
        "mutation: reversing the perturbative denominator sign is detected",
        wrong_mixing_relative != [sp.Integer(3)] * 5,
    )
    nonuniform = sp.diag(0, 0, 0, 0, 1)
    control_relative = [
        sp.simplify((t2_diag[i, i] + nonuniform[i, i] + mixing_terms[i]) / eigenvalues[i])
        for i in range(5)
    ]
    check(
        "falsifier: a nonuniform diagonal remainder breaks ratio cancellation",
        len(set(control_relative)) > 1,
    )

    print(f"relative corrections: {relative}")
    print(f"control relative corrections: {control_relative}")
    print(
        "SUMMARY: exact cancellation for the declared diagonal P2/similarity-sector coefficient; "
        "no claim about omitted heat terms or a full second-order saddle coefficient."
    )
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 1 if FAIL else 0


if __name__ == "__main__":
    raise SystemExit(main())
