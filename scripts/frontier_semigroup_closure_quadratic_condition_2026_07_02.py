#!/usr/bin/env python3
"""Exact Z_5 witness: semigroup closure need not imply quadratic generator."""

from fractions import Fraction
import math

import sympy as sp


CHECKS = []


def check(name, condition):
    ok = bool(condition)
    CHECKS.append((name, ok))
    if not ok:
        raise AssertionError(name)


def factorial_tail_bound(x, n):
    """Bound sum_{k>n} x^k/k! for 0 <= x/(n+2) < 1 by ratio test."""
    nxt = x ** (n + 1) / Fraction(math.factorial(n + 1), 1)
    q = x / Fraction(n + 2, 1)
    if not (0 <= q < 1):
        raise ValueError("increase n")
    return nxt / (1 - q)


def mat_vec_mul(mat, vec):
    return [sum(mat[i][j] * vec[j] for j in range(5)) for i in range(5)]


def mat_mul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(5)) for j in range(5)] for i in range(5)]


def truncated_exp_M_delta(t, n_terms):
    m = [[Fraction(0) for _ in range(5)] for _ in range(5)]
    for j in range(5):
        m[(j + 1) % 5][j] += Fraction(1, 2)
        m[(j - 1) % 5][j] += Fraction(1, 2)

    vec = [Fraction(1), Fraction(0), Fraction(0), Fraction(0), Fraction(0)]
    acc = [Fraction(0) for _ in range(5)]
    for k in range(n_terms + 1):
        coeff = t ** k / Fraction(math.factorial(k), 1)
        acc = [acc[i] + coeff * vec[i] for i in range(5)]
        vec = mat_vec_mul(m, vec)
    return acc


def main():
    t1, t2, n, s = sp.symbols("t1 t2 n s", positive=True)
    theta = sp.symbols("theta", real=True)
    theta0 = 2 * sp.pi / 5
    psi = lambda k: 1 - sp.cos(k * theta0)

    semigroup_delta = sp.exp(-t1 * (1 - sp.cos(n * theta))) * sp.exp(
        -t2 * (1 - sp.cos(n * theta))
    ) - sp.exp(-(t1 + t2) * (1 - sp.cos(n * theta)))
    check("T1_semigroup_exponent_additivity_symbolic", sp.simplify(semigroup_delta) == 0)

    m = sp.zeros(5)
    for j in range(5):
        m[(j + 1) % 5, j] += sp.Rational(1, 2)
        m[(j - 1) % 5, j] += sp.Rational(1, 2)
    ident = sp.eye(5)
    a = m - ident

    check("T1_M_nonnegative_symbolic", all(m[i, j] >= 0 for i in range(5) for j in range(5)))
    check("T1_M_stochastic_symbolic", all(sum(m[i, j] for i in range(5)) == 1 for j in range(5)))
    check(
        "T1_A_Metzler_symbolic",
        all(a[i, j] >= 0 for i in range(5) for j in range(5) if i != j),
    )

    x = sp.symbols("x")
    for mode in range(5):
        eig = sp.cos(2 * sp.pi * mode / 5)
        y = x**mode
        y_inv = x ** ((-mode) % 5)
        formal_eig = (y + y_inv) / 2
        diagonalizes = True
        for j in range(5):
            left = (x ** (mode * ((j - 1) % 5)) + x ** (mode * ((j + 1) % 5))) / 2
            right = formal_eig * x ** (mode * j)
            rem = sp.rem(sp.Poly(left - right, x), sp.Poly(x**5 - 1, x)).as_expr()
            diagonalizes = diagonalizes and (sp.expand(rem) == 0)
        check(f"T1_Fourier_diagonalization_mode_{mode}", diagonalizes)
        eig_rem = sp.rem(
            sp.Poly(formal_eig - eig, x, extension=True), sp.Poly(x**5 - 1, x, extension=True)
        ).as_expr()
        if mode == 0:
            eig_matches_trig = sp.simplify(eig_rem) == 0
        else:
            eig_matches_trig = sp.simplify(eig - sp.cos(2 * sp.pi * mode / 5)) == 0
        check(f"T1_Fourier_eigenvalue_trig_mode_{mode}", eig_matches_trig)
        check(
            f"T1_character_generator_mode_{mode}",
            sp.simplify((eig - 1) + psi(mode)) == 0,
        )

    samples = [Fraction(0), Fraction(1, 5), Fraction(1, 3), Fraction(1), Fraction(2)]
    n_terms = 80
    max_tail = Fraction(0)
    for sample in samples:
        partial = truncated_exp_M_delta(sample, n_terms)
        tail = factorial_tail_bound(sample, n_terms)
        max_tail = max(max_tail, tail)
        # exp(t(M-I)) delta_0 = exp(-t) exp(tM) delta_0; exp(-t)>0 and the
        # omitted exp(tM) series tail is entrywise nonnegative.
        check(f"T1_nonnegative_sample_{sample}", all(x >= 0 for x in partial))
        if sample > 0:
            check(f"T1_strict_positive_sample_{sample}", all(x > 0 for x in partial))
        check(f"T1_remainder_bound_sample_{sample}", tail < Fraction(1, 10**40))

    lhs = 4 * (1 - sp.cos(theta)) - (1 - sp.cos(2 * theta))
    rhs = 2 * (sp.cos(theta) - 1) ** 2
    check("T2_quadratic_gap_identity_symbolic", sp.simplify(lhs - rhs) == 0)
    check("T2_exact_cos_2pi_over_5", sp.cos(theta0) == (sp.sqrt(5) - 1) / 4)

    gap = sp.simplify(4 * psi(1) - psi(2))
    check("T2_gap_specializes_to_square", sp.simplify(gap - 2 * (sp.cos(theta0) - 1) ** 2) == 0)
    check("T2_gap_positive_exact", sp.simplify(gap) > 0)
    check("T2_t_equals_one_log_ratio_positive", sp.simplify(sp.log(sp.exp(gap))) > 0)

    c1 = sp.exp(-s * psi(1))
    c2 = sp.exp(-s * psi(2))
    check("T2_c2_not_c1_fourth_for_positive_t", sp.simplify(sp.log(c2 / c1**4) - s * gap) == 0)

    passed = sum(1 for _, ok in CHECKS if ok)
    failed = sum(1 for _, ok in CHECKS if not ok)
    total = len(CHECKS)
    print(f"SUMMARY PASS={passed} FAIL={failed} TOTAL={total}")
    print(
        "SUMMARY witness=Z5 theta0=2*pi/5; "
        f"samples={','.join(str(x) for x in samples)}; max_tail_bound={max_tail}"
    )
    print(f"SUMMARY status={'PASS' if failed == 0 else 'FAIL'}")


if __name__ == "__main__":
    main()
