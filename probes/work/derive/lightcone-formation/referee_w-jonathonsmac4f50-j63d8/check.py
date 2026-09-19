#!/usr/bin/env python3
"""Referee of J:derive:lightcone-formation:a5 (author w-macbookpro90c72-j795a, grok-4.6); referee
w-jonathonsmac4f50-j63d8 (claude-opus-5). Independent machinery (sympy, mpmath at 30 digits, an LP for the numerical
part), none of the author's code.

L1  steps 1-4: q' = kappa(kappa cosh - sinh), r' = kappa sinh (sympy); A'(kappa) < 1/3 and A(kappa)/kappa <= 1/3 on a
    grid of 400 points in (0, 40] at 30 digits; both tend to 1/3 at 0
L2  step 5, first half: the Jacobian of the mean map m(S) = A(beta|S|) S/|S| is beta [A' SS^T/|S|^2 + (A/kappa)(I - SS^T/|S|^2)]
    (sympy at a generic point), so its norm is <= beta/3 by L1
L3  step 5, second half: a Lipschitz mean map does not bound the Wasserstein-1 influence. W1 between two laws is at least
    the distance of their means, and the W1 rate in a direction u of the natural parameter is sup over chord-1-Lipschitz
    f of Cov(f, u.s), not the eigenvalue Cov(u.s, u.s). Witness: at kappa = 3, f(s) = -|s - n| (1-Lipschitz by the
    triangle inequality) has Cov(f, s.n) = 0.113646 > A'(3) = 0.101147
L4  (INFO, numerical) the W1 rates by a linear program on 300 Fibonacci points of the sphere, longitudinal and
    transverse, kappa = 0 .. 3: all at or below 1/3 up to discretization, maximal at kappa = 0 (where the value is 1/3
    exactly: the reflection coupling and f = s_1 match); the claimed threshold beta < 3/7 is not contradicted
L5  step 6: 49/(E(14 - E)) lies between 49/(14E) and 49/(2E) for E in (0, 12], and E <= 12 on Z^3
"""
from __future__ import annotations

import sys

import mpmath as mp
import sympy as sp

mp.mp.dps = 30
PASSES = 0
FAILS = 0


def check(tag, ok, msg):
    global PASSES, FAILS
    if ok:
        PASSES += 1
    else:
        FAILS += 1
    print(f"{'PASS' if ok else 'FAIL'}: {tag} {msg}")


def A(k):
    return mp.coth(k) - 1 / k


def Ap(k):
    return 1 / k ** 2 - 1 / mp.sinh(k) ** 2


def l1():
    k = sp.symbols("kappa", positive=True)
    q = (3 + k ** 2) * sp.sinh(k) - 3 * k * sp.cosh(k)
    r = k * sp.cosh(k) - sp.sinh(k)
    ok = sp.simplify(sp.diff(q, k) - k * r) == 0 and sp.simplify(sp.diff(r, k) - k * sp.sinh(k)) == 0
    lim1 = sp.limit(1 / k ** 2 - 1 / sp.sinh(k) ** 2, k, 0)
    lim2 = sp.limit((k * sp.cosh(k) - sp.sinh(k)) / (k ** 2 * sp.sinh(k)), k, 0)   # (coth k - 1/k)/k, written without coth
    ok = ok and lim1 == sp.Rational(1, 3) and lim2 == sp.Rational(1, 3)
    grid = [mp.mpf(i) / 10 for i in range(1, 401)]
    ok = ok and all(Ap(x) < mp.mpf(1) / 3 for x in grid) and all(A(x) / x <= mp.mpf(1) / 3 for x in grid)
    ok = ok and all(mp.sinh(x) < x * mp.e ** (x ** 2 / 6) for x in grid[:17])
    check("L1", ok, "steps 1-4: q' = kappa r and r' = kappa sinh (sympy); A'(kappa) < 1/3 and A(kappa)/kappa <= 1/3 at 400 "
          "points of (0, 40] (30 digits), both -> 1/3 as kappa -> 0; sinh kappa < kappa e^{kappa^2/6} on (0, 1.7]: "
          "||Cov_vMF(kappa)|| <= 1/3 holds")


def l2():
    x, y, z, b = sp.symbols("x y z beta", positive=True)
    S = sp.Matrix([x, y, z])
    nS = sp.sqrt(x ** 2 + y ** 2 + z ** 2)
    kap = b * nS
    Afun = sp.coth(kap) - 1 / kap
    m = Afun * S / nS
    J = m.jacobian(S)
    kk = sp.symbols("kk", positive=True)
    Apsym = sp.diff(sp.coth(kk) - 1 / kk, kk).subs(kk, kap)
    P = S * S.T / nS ** 2
    expected = b * (Apsym * P + (Afun / kap) * (sp.eye(3) - P))
    pt = {x: sp.Rational(1, 2), y: sp.Rational(-1, 3), z: sp.Rational(2, 5), b: sp.Rational(3, 7)}
    diff = (J - expected).subs(pt)
    ok = all(abs(sp.N(e, 30)) < 1e-25 for e in diff)
    check("L2", ok, "step 5, first half: the Jacobian of m(S) = A(beta|S|) S/|S| equals beta [A' P + (A/kappa)(I - P)], "
          "P the projector on S (checked at a generic point, 30 digits); by L1 its norm is at most beta/3")


def l3():
    kappa = mp.mpf(3)
    Z = mp.quad(lambda mu: mp.e ** (kappa * mu), [-1, 1])

    def E(g):
        return mp.quad(lambda mu: g(mu) * mp.e ** (kappa * mu), [-1, 1]) / Z
    f = lambda mu: -mp.sqrt(2 * (1 - mu))          # -|s - n| as a function of mu = s.n
    cov = E(lambda mu: f(mu) * mu) - E(f) * E(lambda mu: mu)
    ok = cov > Ap(kappa) + mp.mpf("0.01")
    check("L3", ok,
          f"step 5, second half: at kappa = 3 the 1-Lipschitz f(s) = -|s - n| has d/dt E_(vMF((3 + t) n)) f = Cov(f, s.n) = "
          f"{mp.nstr(cov, 8)} > A'(3) = {mp.nstr(Ap(kappa), 8)}: the Wasserstein-1 rate of the kernel in the longitudinal "
          "direction exceeds the covariance eigenvalue, so the mean map's Lipschitz constant beta/3 does not bound the "
          "W1 influence of a predecessor (W1 >= |difference of means|, not <=)")


def l4():
    try:
        import numpy as np
        from scipy.optimize import linprog
        from scipy.sparse import coo_matrix
    except Exception:
        print("INFO: L4 skipped (numpy/scipy unavailable)")
        return

    def fib(n):
        i = np.arange(n) + 0.5
        ph = np.arccos(1 - 2 * i / n)
        th = np.pi * (1 + 5 ** 0.5) * i
        return np.stack([np.cos(th) * np.sin(ph), np.sin(th) * np.sin(ph), np.cos(ph)], 1)

    def rate(kappa, u, n=300):
        X = fib(n)
        p = np.exp(kappa * X[:, 2])
        p /= p.sum()
        g = X @ u
        nu = (g - (g * p).sum()) * p
        Dm = np.linalg.norm(X[:, None, :] - X[None, :, :], axis=2)
        I, J = np.nonzero(~np.eye(n, dtype=bool))
        rows = np.arange(len(I))
        Amat = coo_matrix((np.concatenate([np.ones(len(I)), -np.ones(len(I))]),
                           (np.concatenate([rows, rows]), np.concatenate([I, J]))), shape=(len(I), n))
        res = linprog(-nu, A_ub=Amat, b_ub=Dm[I, J], bounds=[(None, None)] * n, method="highs")
        return -res.fun
    rows = []
    mx = 0
    for kappa in (0.0, 0.5, 1.0, 2.0, 3.0):
        lo = rate(kappa, np.array([0, 0, 1.0]))
        tr = rate(kappa, np.array([1.0, 0, 0]))
        mx = max(mx, lo, tr)
        rows.append(f"kappa={kappa}: longitudinal {lo:.4f}, transverse {tr:.4f}")
    print("INFO: L4 (numerical LP, 300 points; not a claim) W1 rates per unit of the natural parameter: " + "; ".join(rows)
          + f"; maximum {mx:.4f} (1/3 up to discretization, at kappa = 0)")


def l5():
    Ev = sp.symbols("E", positive=True)
    Sk = 49 / (Ev * (14 - Ev))
    ok = sp.simplify(Sk - 1 / (1 - (1 - Ev / 7) ** 2)) == 0
    for e in [sp.Rational(i, 10) for i in range(1, 121)]:
        v = Sk.subs(Ev, e)
        ok = ok and sp.Rational(49, 14) / e <= v <= sp.Rational(49, 2) / e
    k = sp.pi
    Emax = 3 * 2 * (1 - sp.cos(k))
    ok = ok and Emax == 12
    check("L5", ok, "step 6: 1/(1 - phi^2) = 49/(E(14 - E)) with phi = 1 - E/7, between 49/(14E) and 49/(2E) on a grid of "
          "(0, 12], and E <= 12 on Z^3 (attained at (pi, pi, pi))")


def main():
    try:
        l1()
        l2()
        l3()
        l4()
        l5()
    except Exception as exc:
        print(f"FAIL: X unexpected exception {type(exc).__name__}: {exc}")
        print("SUMMARY: referee check.py crashed")
        return 1
    print(f"TOTAL: PASS={PASSES} FAIL={FAILS}")
    if FAILS:
        print("SUMMARY: referee checks failed (see FAIL lines)")
        return 1
    print("SUMMARY: fails at step 5 - ||Cov_vMF|| <= 1/3 (steps 1-4, re-verified) makes the MEAN map (beta/3)-Lipschitz, but "
          "the Dobrushin/Wasserstein influence of a predecessor is the W1-Lipschitz constant of S -> vMF(beta S), i.e. "
          "sup over chord-1-Lipschitz f of Cov(f, u.s), which the covariance does not control: at kappa = 3, "
          "f = -|s - n| gives 0.1136 > A'(3) = 0.1011. The threshold beta < 3/7 is therefore not proved; a numerical LP "
          "finds the W1 rates at or below 1/3 for kappa in [0, 3] (maximal at kappa = 0), so the claim is not "
          "contradicted, and the missing lemma is sup_{u, f} Cov_kappa(f, u.s) <= 1/3. Step 6's envelope of the linear "
          "kernel holds")
    return 0


if __name__ == "__main__":
    sys.exit(main())
