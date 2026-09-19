#!/usr/bin/env python3
"""Referee of J:derive:formation-response-kernel:a6 (author w-macbookpro90c72-jc53b, grok-4.6); referee
w-jonathonsmac4f50-jf6d0 (claude-opus-5). Independent machinery (none of the author's code). Provenance note: the
attempt builds on the referee report of a3 by this referee's model family (referee_w-jonathonsmac4f50-jceaa); the checks
below are written afresh and also cover the claims a6 adds (R_8 identically 3/2 on an axis, no pole on the drift
diagonal, the count of non-real modes, the visit-sum identity, the multinomial covariance).

G1  (a) and step 2: R = 1/(1 - phi z) as power series; E = 3(|1 - phi e^{iw}|^2 + 1 - |phi|^2) at k = (q1 + w, q2 + w, w)
G2  (b) step 3: G(n, m) = (3/2) C(n+m, n) 2^{-(n+m)} solves G = P G + delta on N^2 (zero outside) and equals the visit sum
    sum_p multinomial(n+m+p; n, m, p) 3^{-(n+m+p)} (exact, truncated tails bounded); G(n, n) sqrt(pi n) -> 3/2
G3  (c) step 4: point response = trinomial (exact iteration to t = 10); n T(n, n, n) -> sqrt3/(2 pi) (30 digits); the
    step covariance (1/3) I - 11^T/9; exponential decay off the axis (relative entropy rate > 0 at two directions)
G4  (c) step 5: R_8(kappa, 0, 0) = 3/2 identically (sympy simplification and 20 rational points); kappa^2 R_8 -> 3/2 on
    (kappa, -kappa, 0) and kappa^2/E -> 1/2; kappa^2 R_8 -> 0 on (kappa, kappa, kappa)
G5  (d) step 6: phi(pi/2, 0) = (2 + i)/3, 1/(1 - phi) = 3(1 + i)/2, 1/(1 - |phi|^2) = 9/4; exactly 10 of the 15 nonzero
    modes of L = 4 have Im phi != 0
"""
from __future__ import annotations

import itertools
import sys
from fractions import Fraction
from math import comb, factorial

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


def g1():
    q1, q2, w, z, s = sp.symbols("q1 q2 w z s", real=True)
    phi = (1 + sp.exp(sp.I * q1) + sp.exp(sp.I * q2)) / 3
    k = (q1 + w, q2 + w, w)
    E = sum(2 * (1 - sp.cos(kj)) for kj in k)
    a = phi * sp.exp(sp.I * w)
    rhs = 3 * (sp.expand((1 - a) * sp.conjugate(1 - a), complex=True) + 1 - sp.expand(phi * sp.conjugate(phi), complex=True))
    okE = sp.simplify(sp.expand_trig(sp.expand(E - rhs, complex=True))) == 0
    okR = sp.expand(sp.series(1 / (1 - s * z), z, 0, 10).removeO() - sum((s * z) ** n for n in range(10))) == 0
    check("G1", okE and okR, "steps 1-2: sum_t (phi z)^t = 1/(1 - phi z) and the E-identity hold identically")


def g2():
    n_max = 12
    G = {}
    for tot in range(0, 2 * n_max + 1):
        for a in range(0, tot + 1):
            b = tot - a
            if a > n_max or b > n_max:
                continue
            val = Fraction(3, 2) * comb(a + b, a) / 2 ** (a + b)
            G[(a, b)] = val
    # stationary equation G(x) = (G(x) + G(x-e1) + G(x-e2))/3 + delta(x)
    ok = all(G[(a, b)] == (G[(a, b)] + G.get((a - 1, b), 0) + G.get((a, b - 1), 0)) / 3 + (1 if (a, b) == (0, 0) else 0)
             for (a, b) in G)
    # visit sum, truncated at p <= 400: the tail is below 3^-p p^(n+m) ... bounded crudely, compare to 1e-40
    vis_ok = True
    for (a, b) in [(0, 0), (1, 0), (2, 3), (5, 5)]:
        s = Fraction(0)
        for p in range(0, 400):
            s += Fraction(factorial(a + b + p), factorial(a) * factorial(b) * factorial(p)) / 3 ** (a + b + p)
        vis_ok = vis_ok and 0 <= G[(a, b)] - s < Fraction(1, 10 ** 40)
    r = mp.mpf(3) / 2 * mp.binomial(20000, 10000) / mp.mpf(4) ** 10000 * mp.sqrt(mp.pi * 10000)
    ok = ok and vis_ok and abs(r - mp.mpf(3) / 2) < mp.mpf("1e-4")
    check("G2", ok, "step 3: G(n, m) = (3/2) C(n+m, n)/2^(n+m) solves the stationary equation on N^2 (x1, x2 <= 12, zero "
          "outside) and equals the visit sum of the trinomial walk (four points, 400 terms, gap < 1e-40); "
          f"G(n, n) sqrt(pi n) at n = 10000 is {mp.nstr(r, 8)} -> 3/2")


def g3():
    ok = True
    m = {(0, 0, 0): Fraction(1)}
    for t in range(1, 11):
        new = {}
        for x, v in m.items():
            for e in ((1, 0, 0), (0, 1, 0), (0, 0, 1)):
                y = (x[0] + e[0], x[1] + e[1], x[2] + e[2])
                new[y] = new.get(y, 0) + v / 3
        m = new
        ok = ok and all(v == Fraction(factorial(t), factorial(x[0]) * factorial(x[1]) * factorial(x[2]) * 3 ** t)
                        for x, v in m.items())
    vals = []
    for n in (100, 10000, 1000000):
        lt = mp.loggamma(3 * n + 1) - 3 * mp.loggamma(n + 1) - 3 * n * mp.log(3)
        vals.append(n * mp.e ** lt)
    tgt = mp.sqrt(3) / (2 * mp.pi)
    ok = ok and abs(vals[-1] - tgt) < mp.mpf("1e-6")
    # step covariance: steps e1, e2, e3 with probability 1/3
    E1 = sp.Matrix([sp.Rational(1, 3)] * 3)
    EXX = sp.eye(3) / 3
    cov = EXX - E1 * E1.T
    ok = ok and cov == sp.eye(3) / 3 - sp.ones(3, 3) / 9
    # off-axis exponential rate: T(2n, n, 0) and T(2n, n, n)
    def logT(a, b, c):
        return mp.loggamma(a + b + c + 1) - mp.loggamma(a + 1) - mp.loggamma(b + 1) - mp.loggamma(c + 1) - (a + b + c) * mp.log(3)
    rates = [(logT(20, 10, 0) - logT(40, 20, 0)) / 10, (logT(20, 10, 10) - logT(40, 20, 20)) / 10]
    ok = ok and all(rt > 0.05 for rt in rates)
    check("G3", ok, "step 4: the point response is the trinomial (exact iteration to t = 10); n T(n, n, n) = "
          + ", ".join(mp.nstr(v, 9) for v in vals) + f" (n = 1e2, 1e4, 1e6) -> sqrt3/(2 pi) = {mp.nstr(tgt, 9)}, i.e. "
          "T R -> 3/(2 pi) with R = sqrt3 n; the step covariance is I/3 - 11^T/9; off the axis the kernel decays "
          f"exponentially (rates {mp.nstr(rates[0], 4)}, {mp.nstr(rates[1], 4)} per n along (2,1,0), (2,1,1))")


def R8(k):
    tot = 0
    for e in itertools.product((1, -1), repeat=3):
        phi = sum(sp.exp(-sp.I * e[j] * k[j]) for j in range(3)) / 3
        tot += 1 / (1 - phi)
    return tot / 8


def g4():
    kap = sp.symbols("kappa", positive=True)
    ax = sp.simplify(sp.expand_complex(R8((kap, 0, 0))).rewrite(sp.cos))
    pts_ok = all(abs(sp.N(R8((sp.Rational(i, 7), 0, 0)), 40) - sp.Rational(3, 2)) < 1e-35 for i in range(1, 21))
    lim_plane = sp.limit(sp.simplify(kap ** 2 * R8((kap, -kap, 0))), kap, 0)
    E = sum(2 * (1 - sp.cos(c)) for c in (kap, -kap, 0))
    limE = sp.limit(kap ** 2 / E, kap, 0)
    diag_vals = [abs(sp.N((c ** 2) * R8((c, c, c)), 30)) for c in (sp.Rational(1, 10), sp.Rational(1, 100), sp.Rational(1, 1000))]
    ok = sp.simplify(ax - sp.Rational(3, 2)) == 0 and pts_ok and lim_plane == sp.Rational(3, 2) and limE == sp.Rational(1, 2)
    ok = ok and diag_vals[0] > diag_vals[1] > diag_vals[2] and diag_vals[2] < 1e-4
    check("G4", ok, f"step 5: R_8(kappa, 0, 0) simplifies to {ax} (and equals 3/2 at 20 rational kappa, 40 digits); along "
          f"(kappa, -kappa, 0) kappa^2 R_8 -> {lim_plane}, kappa^2/E -> {limE}; along (kappa, kappa, kappa) kappa^2 |R_8| = "
          + ", ".join(mp.nstr(mp.mpf(str(v)), 4) for v in diag_vals)
          + " at kappa = 0.1, 0.01, 0.001 -> 0")


def g5():
    phi = (1 + sp.I + 1) / 3
    chi = sp.simplify(1 / (1 - phi))
    var = sp.simplify(1 / (1 - phi * sp.conjugate(phi)))
    ok = sp.simplify(chi - sp.Rational(3, 2) * (1 + sp.I)) == 0 and var == sp.Rational(9, 4)
    ipow = {0: 1, 1: sp.I, 2: -1, 3: -sp.I}
    nonreal = sum(1 for a in range(4) for b in range(4) if (a, b) != (0, 0) and sp.im((1 + ipow[a] + ipow[b]) / 3) != 0)
    ok = ok and nonreal == 10
    check("G5", ok, f"step 6: phi(pi/2, 0) = (2 + i)/3, 1/(1 - phi) = {chi}, 1/(1 - |phi|^2) = {var}; {nonreal} of the 15 "
          "nonzero modes of L = 4 have non-real phi")


def main():
    try:
        g1()
        g2()
        g3()
        g4()
        g5()
    except Exception as exc:
        print(f"FAIL: X unexpected exception {type(exc).__name__}: {exc}")
        print("SUMMARY: referee check.py crashed")
        return 1
    print(f"TOTAL: PASS={PASSES} FAIL={FAILS}")
    if FAILS:
        print("SUMMARY: fails at a checked step (see FAIL lines)")
        return 1
    print("HIT: confirmed - a6's partial result survives: the static response on Z^2 is (3/2) C(n+m, n)/2^(n+m) on the "
          "forward quadrant (0 elsewhere), the point response is the trinomial with n T(n, n, n) -> sqrt3/(2 pi) (a directed "
          "1/R, T R -> 3/(2 pi), along the level axis), R_8 is identically 3/2 on a coordinate axis, has a 1/k^2 pole along "
          "(kappa, -kappa, 0) (kappa^2 R_8 -> 3/2 against kappa^2/E -> 1/2) and none along the drift diagonal, and "
          "equilibrium FDR fails (10 of 15 modes of L = 4 non-real); every finite claim re-derived with independent code")
    print("SUMMARY: confirmed - no failing step; provenance: the attempt builds on this referee family's a3 report, whose "
          "findings it re-derives and extends (identical 3/2 on an axis, no pole on the drift diagonal)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
