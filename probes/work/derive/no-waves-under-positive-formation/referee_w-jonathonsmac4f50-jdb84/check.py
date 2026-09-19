#!/usr/bin/env python3
"""Referee of J:derive:no-waves-under-positive-formation:a4 (author w-macbookpro90c72-j1a93, grok-4.6); referee
w-jonathonsmac4f50-jdb84 (claude-opus-5). Independent machinery (sympy series, exact rationals), none of the author's code:

N1  the small-k form of lambda claimed in statement (A) and in the HIT line, 1 - i mu.k - (1/2) k^T Sigma k with
    Sigma = Cov(v), against the exact series of lambda: NEC and random positive weight sets
N2  what step 2 does establish: |lambda|^2 = 1 - k^T Sigma k + O(k^4) and arg lambda = -mu.k + O(k^3)
    (log lambda = -i mu.k - (1/2) k^T Sigma k + O(k^3)), exact series for the same weight sets
N3  |lambda| <= 1 with equality exactly on {k : k.(v_j - v_0) in 2 pi Z}: exact search on torus grids, including a
    predecessor set whose differences span only 2Z^2 (|lambda| = 1 at k != 0)
N4  several levels (statement B): the analytic root through z(0) = 1 against the renewal (space-time walk) drift and
    variance, exact series, for a two-level and a three-level example; the attempt proves only the first derivative
N5  the exceptions (C): the author's negative-weight example (2, -1) is |lambda| = 3 growth, not a wave; the two-level
    recursion with a negative weight on the earlier level (discrete wave equation) has |z| = 1 exactly and
    arg z = c k + O(k^3): the exception the task names, not exhibited in the attempt
"""
from __future__ import annotations

import itertools
import random
import sys
from fractions import Fraction

import sympy as sp

PASSES = 0
FAILS = 0


def check(tag, ok, msg):
    global PASSES, FAILS
    if ok:
        PASSES += 1
    else:
        FAILS += 1
    print(f"{'PASS' if ok else 'FAIL'}: {tag} {msg}")


k1, k2, t = sp.symbols("k1 k2 t", real=True)


def lam_of(ws, vs):
    return sum(sp.Rational(w) * sp.exp(-sp.I * (k1 * v[0] + k2 * v[1])) for w, v in zip(ws, vs))


def moments(ws, vs):
    ws = [sp.Rational(w) for w in ws]
    mu = sp.Matrix([sum(w * v[i] for w, v in zip(ws, vs)) for i in range(2)])
    S2 = sp.Matrix(2, 2, lambda i, j: sum(w * v[i] * v[j] for w, v in zip(ws, vs)))
    return mu, S2, S2 - mu * mu.T


def radial_coeffs(expr, order):
    """coefficients of t^0..t^order of expr(k -> t k) as polynomials in k1, k2"""
    s = sp.series(expr.subs({k1: t * k1, k2: t * k2}), t, 0, order + 1).removeO()
    s = sp.expand(s)
    return [sp.simplify(s.coeff(t, n)) for n in range(order + 1)]


def weight_sets():
    random.seed(35)
    sets = [((Fraction(1, 3),) * 3, [(0, 0), (1, 0), (0, 1)])]      # NEC (block 35's multiplier, conjugated)
    for _ in range(4):
        n = random.randint(2, 4)
        raw = [random.randint(1, 6) for _ in range(n)]
        ws = tuple(Fraction(r, sum(raw)) for r in raw)
        vs = [(random.randint(-2, 2), random.randint(-2, 2)) for _ in range(n)]
        sets.append((ws, vs))
    return sets


def n1_n2():
    ok_fail = True      # the claimed form must fail wherever mu != 0
    ok_true = True
    rows = []
    kv = sp.Matrix([k1, k2])
    for ws, vs in weight_sets():
        lam = lam_of(ws, vs)
        mu, S2, Sig = moments(ws, vs)
        c = radial_coeffs(lam, 2)
        claimed2 = sp.expand(-sp.Rational(1, 2) * (kv.T * Sig * kv)[0])
        true2 = sp.expand(-sp.Rational(1, 2) * (kv.T * S2 * kv)[0])
        c2 = sp.expand(c[2])
        ok_true = ok_true and sp.simplify(c2 - true2) == 0 and sp.simplify(c[1] + sp.I * (mu.T * kv)[0]) == 0
        if any(m != 0 for m in mu):
            ok_fail = ok_fail and sp.simplify(c2 - claimed2) != 0
        # N2: |lambda|^2 and arg
        a2 = radial_coeffs(sp.expand(lam * sp.conjugate(lam), complex=True), 3)
        ok_true = ok_true and sp.simplify(a2[0] - 1) == 0 and sp.simplify(a2[1]) == 0 and \
            sp.simplify(a2[2] + (kv.T * Sig * kv)[0]) == 0 and sp.simplify(a2[3]) == 0
        lg = radial_coeffs(sp.log(lam), 2)
        ok_true = ok_true and sp.simplify(lg[1] + sp.I * (mu.T * kv)[0]) == 0 and \
            sp.simplify(lg[2] + sp.Rational(1, 2) * (kv.T * Sig * kv)[0]) == 0
        if len(rows) == 0:
            rows.append(f"NEC: quadratic term of lambda = {c2}, claimed -(1/2)k^T Sigma k = {claimed2}, "
                        f"second moment -(1/2)k^T(Sigma + mu mu^T)k = {true2}")
    check("N1", ok_fail and ok_true,
          "statement (A) and the HIT line give lambda(k) = 1 - i mu.k - (1/2) k^T Sigma k with Sigma = Cov(v); the exact "
          "series of lambda has quadratic term -(1/2) k^T (Sigma + mu mu^T) k (the second moment, as step 2 itself "
          "collects), so the claimed form is false whenever mu != 0: " + rows[0] + " (NEC and four random positive "
          "weight sets on Z^2, all with mu != 0)")
    check("N2", ok_true,
          "what step 2 does establish, exact series on the same five weight sets: |lambda|^2 = 1 - k^T Sigma k + O(k^4) "
          "with no cubic term, and log lambda = -i mu.k - (1/2) k^T Sigma k + O(k^3), i.e. |lambda| = 1 - (1/2) k^T Sigma k "
          "and arg lambda = -mu.k to these orders: drift plus diffusion for one level")


def n3():
    import cmath
    import math
    ok = True
    rows = []
    cases = [((Fraction(1, 3),) * 3, [(0, 0), (1, 0), (0, 1)]),
             ((Fraction(1, 2), Fraction(1, 4), Fraction(1, 4)), [(0, 0), (2, 0), (0, 2)])]
    for ws, vs in cases:
        for L in (8, 12):
            eq = []
            for n1, n2 in itertools.product(range(L), repeat=2):
                # exact test of |lambda| = 1: all characters equal  <=>  k.(v_j - v_0) in 2 pi Z  <=>  L | (n.(v_j - v_0))
                ks = [(n1 * (v[0] - vs[0][0]) + n2 * (v[1] - vs[0][1])) % L == 0 for v in vs]
                lam_abs = abs(sum(float(w) * cmath.exp(-2j * math.pi * (n1 * v[0] + n2 * v[1]) / L) for w, v in zip(ws, vs)))
                ok = ok and lam_abs <= 1 + 1e-12 and ((lam_abs > 1 - 1e-12) == all(ks))
                if all(ks):
                    eq.append((n1, n2))
            rows.append(f"v = {vs}, L = {L}: |lambda| = 1 at {eq}")
    check("N3", ok,
          "|lambda| <= 1 on the torus grids, with equality exactly where all characters coincide; for a predecessor "
          "set whose differences span only 2Z^2 the unimodular set contains k != 0 (so 'only at k = 0' needs the "
          "differences to generate Z^d): " + "; ".join(rows))


def root_series(poly_in_z, order):
    z = sp.symbols("z")
    # analytic root through z = 1 at k = 0 by undetermined coefficients in t (k -> t k)
    cs = sp.symbols(f"c1:{order + 1}")
    zt = 1 + sum(c * t ** (i + 1) for i, c in enumerate(cs))
    eq = sp.expand(sp.series(poly_in_z(zt), t, 0, order + 1).removeO())
    sol = {}
    for n in range(1, order + 1):
        coeff = sp.expand(eq.coeff(t, n).subs(sol))
        s = sp.solve(coeff, cs[n - 1])
        sol[cs[n - 1]] = sp.simplify(s[0])
    return [sp.simplify(sol[c]) for c in cs]


def n4():
    k = sp.symbols("k", real=True)
    ok = True
    rows = []
    # two levels: theta_{t+1}(x) = p theta_t(x - u) + q theta_{t-1}(x); steps (v, T) = (u, 1) w.p. p, (0, 2) w.p. q
    for (p, q, u) in ((sp.Rational(2, 3), sp.Rational(1, 3), 1), (sp.Rational(1, 2), sp.Rational(1, 2), 2)):
        poly = lambda z: z ** 2 - p * sp.exp(-sp.I * k * t * u) * z - q
        c = root_series(lambda z: poly(z).subs(k, 1), 2)       # series in t at k = 1 (direction scale)
        ET = p * 1 + q * 2
        drift = p * u / ET
        var = (p * (u - drift * 1) ** 2 + q * (0 - drift * 2) ** 2) / ET
        # log z = -i drift t - (1/2) var t^2 + ...  <=>  z = 1 - i drift t + (-(1/2) var - drift^2/2) t^2
        ok = ok and sp.simplify(c[0] + sp.I * drift) == 0 and sp.simplify(c[1] - (-var / 2 - drift ** 2 / 2)) == 0 and var > 0
        rows.append(f"two levels (p, q, u) = ({p}, {q}, {u}): drift {drift}, variance rate {sp.nsimplify(var)}")
    # three levels: z^3 = a z^2 + b z + c with a = w1 e^{-i k}, b = w2 e^{+i k}, c = w3
    w1, w2, w3 = sp.Rational(1, 2), sp.Rational(1, 3), sp.Rational(1, 6)
    steps = [(w1, 1, 1), (w2, -1, 2), (w3, 0, 3)]         # (weight, displacement, time)
    poly3 = lambda z: z ** 3 - w1 * sp.exp(-sp.I * t) * z ** 2 - w2 * sp.exp(sp.I * t) * z - w3
    c = root_series(poly3, 2)
    ET = sum(w * T for w, v, T in steps)
    drift = sum(w * v for w, v, T in steps) / ET
    var = sum(w * (v - drift * T) ** 2 for w, v, T in steps) / ET
    ok = ok and sp.simplify(c[0] + sp.I * drift) == 0 and sp.simplify(c[1] - (-var / 2 - drift ** 2 / 2)) == 0 and var > 0
    rows.append(f"three levels (weights 1/2, 1/3, 1/6 at (v, T) = (1, 1), (-1, 2), (0, 3)): drift {drift}, variance "
                f"rate {sp.nsimplify(var)}")
    check("N4", ok,
          "statement (B) in examples: the root through z(0) = 1 has log z = -i (E v/E T) k - (1/2) (E(v - drift T)^2 / E T) "
          "k^2 + O(k^3) (the renewal drift and variance, positive): " + "; ".join(rows) + ". The attempt proves only "
          "the first derivative for two levels; the general PSD claim is stated, not proved (its own section (3))")


def n5():
    k, c = sp.symbols("k c", positive=True)
    lam = 2 - sp.exp(-sp.I * sp.pi)
    ok = sp.simplify(sp.Abs(lam) - 3) == 0
    # discrete wave equation: theta_{t+1} = 2 theta_t - theta_{t-1} + c^2 (theta_t(x+1) - 2 theta_t(x) + theta_t(x-1))
    # weights at level t: 2 - 2c^2, c^2, c^2; at level t-1: -1 (negative); sum = 1 (gain one)
    z = sp.symbols("z")
    b = 2 - 4 * c ** 2 * sp.sin(k / 2) ** 2
    poly = z ** 2 - b * z + 1
    prod_roots = 1                      # constant term
    disc = sp.simplify(b ** 2 - 4)
    # for 0 < c <= 1 and all k: b in [-2, 2], so the roots are complex conjugates with product 1: |z| = 1
    cv = sp.Rational(1, 2)
    grid_ok = all(sp.simplify((b ** 2 - 4).subs({c: cv, k: sp.pi * n / 12})) <= 0 for n in range(0, 25))
    # arg z = arccos(b/2) = 2 arcsin(c sin(k/2)) ~ c k
    argz = sp.acos(b / 2)
    ser = sp.series(argz.subs(c, cv), k, 0, 4).removeO()
    ok = ok and grid_ok and sp.simplify(ser - (cv * k + sp.Rational(1, 24) * (cv ** 3 - cv) * k ** 3)) == 0
    weights_sum = sp.simplify((2 - 2 * c ** 2) + 2 * c ** 2 - 1)
    ok = ok and weights_sum == 1
    check("N5", ok,
          "(C): the author's example lambda = 2 - e^{-ik} has |lambda(pi)| = 3, growth rather than a wave; the gain-one "
          "two-level recursion with the negative weight -1 on the earlier level (the discrete wave equation, weights "
          "2 - 2c^2, c^2, c^2 and -1, sum 1) has roots with product 1 and b^2 - 4 <= 0, so |z| = 1 exactly, and "
          "arg z = arccos(1 - 2c^2 sin^2(k/2)) = c k + (c^3 - c) k^3/24 + O(k^5) (checked at c = 1/2): a wave "
          "|z| = 1, arg z = c|k|; this is the exception the task names, and the attempt does not exhibit it")


def main():
    try:
        n1_n2()
        n3()
        n4()
        n5()
    except Exception as exc:
        print(f"FAIL: X unexpected exception {type(exc).__name__}: {exc}")
        print("SUMMARY: referee check.py crashed")
        return 1
    print(f"TOTAL: PASS={PASSES} FAIL={FAILS}")
    if FAILS:
        print("SUMMARY: referee checks failed (see FAIL lines)")
        return 1
    print("SUMMARY: fails at step 2 - the small-k form claimed in statement (A) and in the HIT line, "
          "lambda = 1 - i mu.k - (1/2) k^T Sigma k with Sigma = Cov(v), does not follow from step 2 (whose own quadratic "
          "term is the second moment Sigma + mu mu^T) and is false whenever mu != 0 (NEC: -(k1^2 + k2^2)/6 against "
          "-(k1^2 - k1 k2 + k2^2)/9); what survives for one level is |lambda| <= 1, |lambda|^2 = 1 - k^T Sigma k + O(k^4), "
          "arg lambda = -mu.k + O(k^3) (drift plus diffusion, re-verified); statement (B) is proved only to first order "
          "(true in the examples checked, via the renewal variance); (C) exhibits no wave - the negative-weight example "
          "is growth |lambda| = 3, while the negative weight on the earlier level (discrete wave equation) gives |z| = 1, "
          "arg z = c k + O(k^3)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
