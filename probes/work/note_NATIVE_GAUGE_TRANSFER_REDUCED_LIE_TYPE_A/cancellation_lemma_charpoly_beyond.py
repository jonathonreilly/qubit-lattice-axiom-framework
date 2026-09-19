#!/usr/bin/env python3
"""J:note check for NATIVE_GAUGE_TRANSFER_REDUCED_LIE_TYPE_A2_DIAGONAL_SIMILARITY_SECTOR_CANCELLATION (on main).

Proof steps verified literally, with machinery disjoint from the note's runner (which uses the Rayleigh-Schrodinger formula (3) on one
five-dimensional realization and monomials up to degree eight):

  P1   identity (1): R H = G1, R Q = 3u, P2 e^{-Q} = (1/2) R^2 W + 3 W, re-derived in sympy; and [R, L] = 0 on EVERY monomial x^a y^b of total
       degree <= 14 (beyond 8), applied as differential operators;
  P2   the finite cancellation lemma mu_i^(2) = 3 mu_i, by exact implicit differentiation of the characteristic polynomial
       p(lambda, eps) = det(T0 + eps T1 + eps^2 T2_diag - lambda I) at (mu_i, 0) (derivatives from the characteristic polynomial and from
       Jacobi's formula at shifted lambda, interpolated exactly) -- no eigenvector formula -- for random exact
       realizations of dimension 6, 7, 8 (beyond 5): T0 = O D O^T with O rational orthogonal (Cayley transform of a random rational skew
       matrix) and D distinct rationals (zero and negative values included), R random rational skew; every eigenvalue is checked, plus the
       first-order coefficient 0; the falsifier's non-uniform remainder (3 T0 replaced by 3 T0 + diag(0,..,0,1)) must break the pairwise
       relative cancellation.
"""
from __future__ import annotations

import itertools
import random

import sympy as sp

x, y = sp.symbols("x y")


def p1():
    H = x * y * (x + y) / 2
    Q = x ** 2 + x * y + y ** 2
    W = H * sp.exp(-Q)
    u = x + y
    G1 = (u ** 2 + 2 * x * y) / 2
    P2 = sp.Rational(3, 2) * u - 3 * u * G1 + sp.Rational(9, 2) * u ** 2 * H
    Rop = lambda f: sp.diff(f, x) + sp.diff(f, y)
    Lop = lambda f: (sp.diff(f, x, 2) - sp.diff(f, x, y) + sp.diff(f, y, 2)) / 3
    ok1 = sp.simplify(Rop(H) - G1) == 0 and sp.simplify(Rop(Q) - 3 * u) == 0
    ok2 = sp.simplify(P2 * sp.exp(-Q) - (Rop(Rop(W)) / 2 + 3 * W)) == 0
    n_mono = 0
    ok3 = True
    for d in range(0, 15):
        for a in range(d + 1):
            m = x ** a * y ** (d - a)
            ok3 &= sp.expand(Rop(Lop(m)) - Lop(Rop(m))) == 0
            n_mono += 1
    return ok1, ok2, ok3, n_mono


def rational_orthogonal(n, rng):
    A = sp.zeros(n, n)
    for i in range(n):
        for j in range(i + 1, n):
            v = sp.Rational(rng.randint(-5, 5), rng.randint(1, 4))
            A[i, j], A[j, i] = v, -v
    I = sp.eye(n)
    return (I - A) * (I + A).inv()


def random_skew(n, rng):
    R = sp.zeros(n, n)
    for i in range(n):
        for j in range(i + 1, n):
            v = sp.Rational(rng.randint(-4, 4), rng.randint(1, 3))
            R[i, j], R[j, i] = v, -v
    return R


def _interp_at_zero(hs, vals, deriv):
    """value (deriv=0) or first derivative (deriv=1) at h = 0 of the polynomial through (hs, vals), exact."""
    h = sp.Symbol("h")
    poly = sp.interpolate(list(zip(hs, vals)), h)
    return sp.nsimplify(poly.subs(h, 0)) if deriv == 0 else sp.nsimplify(sp.diff(poly, h).subs(h, 0))


def second_order_by_charpoly(T0, T1, T2, mu):
    """Taylor coefficients a, b of the eigenvalue branch lambda(eps) = mu + a eps + b eps^2 of T0 + eps T1 + eps^2 T2, from the derivatives of
    p(lambda, eps) = det(T0 + eps T1 + eps^2 T2 - lambda I) at (mu, 0): p_lambda, p_lambdalambda from the characteristic polynomial of T0;
    p_eps, p_epseps, p_lambdaeps by Jacobi's formula at the shifted points lambda = mu + h (h = j + 1/7, j = 0..n+1, where T0 - lambda I is invertible)
    and exact polynomial interpolation back to h = 0 (each is a polynomial in h of degree <= n)."""
    n = T0.shape[0]
    lam = sp.Symbol("lam")
    cp = (T0 - lam * sp.eye(n)).det(method="berkowitz")
    pl = sp.diff(cp, lam).subs(lam, mu)
    pll = sp.diff(cp, lam, 2).subs(lam, mu)
    hs = [sp.Integer(j) + sp.Rational(1, 7) for j in range(n + 2)]   # mu + h never equals a (half-integer) eigenvalue
    g1, g2 = [], []
    for hv in hs:
        A = T0 - (mu + hv) * sp.eye(n)
        detA = A.det(method="berkowitz")
        Ai = A.inv()
        X = Ai * T1
        t1 = X.trace()
        t2 = (Ai * (2 * T2)).trace()
        t11 = (X * X).trace()
        g1.append(detA * t1)                       # d/deps det(T(eps) - (mu+h) I) at eps = 0
        g2.append(detA * (t2 + t1 ** 2 - t11))     # d^2/deps^2 det(...) at eps = 0
    pe = _interp_at_zero(hs, g1, 0)
    ple = _interp_at_zero(hs, g1, 1)               # lambda = mu + h, so d/dlambda = d/dh
    pee = _interp_at_zero(hs, g2, 0)
    a = -pe / pl
    b = -(sp.Rational(1, 2) * pll * a ** 2 + ple * a + sp.Rational(1, 2) * pee) / pl
    return sp.nsimplify(a), sp.nsimplify(b)


def p2(seed=2026):
    rng = random.Random(seed)
    rows = []
    for n in (6, 7, 8):
        O = rational_orthogonal(n, rng)
        assert sp.simplify(O.T * O - sp.eye(n)) == sp.zeros(n, n)
        vals = rng.sample([sp.Rational(k, 2) for k in range(-9, 10)], n)
        if 0 not in vals:
            vals[0] = sp.Integer(0)
        D = sp.diag(*vals)
        T0 = O * D * O.T
        R = random_skew(n, rng)
        T1 = R * T0 - T0 * R
        T2 = (R * T1 - T1 * R) / 2 + 3 * T0
        ok = True
        for mu in vals:
            a, b = second_order_by_charpoly(T0, T1, T2, mu)
            ok &= a == 0 and b == 3 * mu
        # the falsifier's non-uniform remainder: 3 T0 + diag(0, ..., 0, 1) (in the lab basis)
        extra = sp.zeros(n, n)
        extra[n - 1, n - 1] = 1
        T2bad = (R * T1 - T1 * R) / 2 + 3 * T0 + extra
        rel = []
        for mu in [v for v in vals if v != 0][:2]:
            a, b = second_order_by_charpoly(T0, T1, T2bad, mu)
            rel.append(b / mu)
        broken = rel[0] != rel[1]
        rows.append((n, ok, broken, [str(v) for v in vals]))
    return rows


def main():
    ok1, ok2, ok3, n_mono = p1()
    print(f"P1 R H = G1 and R Q = 3u: {ok1}; P2 e^(-Q) = (1/2) R^2 W + 3 W: {ok2}; [R, L] = 0 on all {n_mono} monomials of degree <= 14: {ok3}")
    rows = p2()
    for n, ok, broken, vals in rows:
        print(f"P2 dimension {n}, eigenvalues {vals}: first-order coefficient 0 and mu^(2) = 3 mu for every eigenvalue (char-poly implicit "
              f"differentiation): {ok}; non-uniform remainder breaks the relative cancellation: {broken}")
    all_ok = ok1 and ok2 and ok3 and all(ok and broken for _, ok, broken, _ in rows)
    if all_ok:
        print("SUMMARY: the proof steps hold beyond the note's sizes with disjoint machinery: identity (1) re-derived, [R, L] = 0 on all "
              f"{n_mono} monomials of degree <= 14, and mu^(2) = 3 mu for every simple eigenvalue of exact rational realizations of dimension "
              "6, 7, 8 (zero and negative eigenvalues included) by implicit differentiation of det(T(eps) - lambda I); the non-uniform "
              "remainder falsifier breaks the relative cancellation as the note says")
    else:
        print(f"HIT: a proof step fails: P1 {ok1}/{ok2}/{ok3}, P2 {[(n, ok, broken) for n, ok, broken, _ in rows]}")
        print("SUMMARY: falsifier fired; see the lines above")


if __name__ == "__main__":
    main()
