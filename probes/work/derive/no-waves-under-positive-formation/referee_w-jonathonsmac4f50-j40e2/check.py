#!/usr/bin/env python3
"""Referee of J:derive:no-waves-under-positive-formation:a3 (author w-macbookpro90c72-j2425, grok-4.6); referee
w-jonathonsmac4f50-j40e2 (claude-opus-5). Independent machinery (sympy series, exact rationals), none of the author's code.

V1  steps 1-2: |lambda| <= 1 with equality exactly where the characters coincide (exact divisibility test on 8x8 and 12x12
    torus grids for NEC and a sublattice-supported set); lambda = 1 - i m.k - (1/2) k^T M k + O(k^3) with M the SECOND moment,
    and |lambda|^2 = 1 - k^T Cov k + O(k^4), exact series for NEC and three random positive weight sets
V2  NEC (predecessors (0,0), (-1,0), (0,-1)): mean (-1/3, -1/3), det Cov = 1/27, Hessian of |lambda|^2 at 0 = -2 Cov with entries
    -4/9, 2/9 and determinant 4/27
V3  step 3: the 7-stencil lambda = 1 - E/7 is real, |lambda| < 1 for k != 0 in (-pi, pi]^3 (E in (0, 12], lambda in [-5/7, 1)),
    Hessian of |lambda|^2 at 0 = -(4/7) I
V4  step 4: collinear support has det Cov = 0 and |lambda| = 1 EXACTLY along the transverse direction (to all orders, not
    only to second); a singleton is a pure phase e^{-ik.v}
V5  step 5 (a reading, not a proof): the negative-weight example (2, -1) gives |lambda(pi)| = 3, growth rather than a wave; the
    two-level recursion with weight -1 on the earlier level (discrete wave equation) is a gain-one wave with |z| = 1 and
    arg z = c k + O(k^3) - the exception the task names, which the attempt does not exhibit
"""
from __future__ import annotations

import itertools
import math
import cmath
import random
import sys
from fractions import Fraction

import sympy as sp


def main():
    fails = 0

    def check(tag, ok, msg):
        nonlocal fails
        fails += (not ok)
        print(("PASS: " if ok else "FAIL: ") + tag + " " + msg)

    k1, k2, t = sp.symbols("k1 k2 t", real=True)
    kv = sp.Matrix([k1, k2])

    def lam_of(ws, vs):
        return sum(sp.Rational(w) * sp.exp(-sp.I * (k1 * v[0] + k2 * v[1])) for w, v in zip(ws, vs))

    def coeffs(expr, order):
        s = sp.expand(sp.series(expr.subs({k1: t * k1, k2: t * k2}), t, 0, order + 1).removeO())
        return [sp.simplify(s.coeff(t, n)) for n in range(order + 1)]

    # V1
    ok = True
    for ws, vs in (((Fraction(1, 3),) * 3, [(0, 0), (-1, 0), (0, -1)]), ((Fraction(1, 2), Fraction(1, 4), Fraction(1, 4)), [(0, 0), (2, 0), (0, 2)])):
        for L in (8, 12):
            for n1, n2 in itertools.product(range(L), repeat=2):
                allc = all((n1 * (v[0] - vs[0][0]) + n2 * (v[1] - vs[0][1])) % L == 0 for v in vs)
                val = abs(sum(float(w) * cmath.exp(-2j * math.pi * (n1 * v[0] + n2 * v[1]) / L) for w, v in zip(ws, vs)))
                ok = ok and val <= 1 + 1e-12 and ((val > 1 - 1e-12) == allc)
    random.seed(3)
    sets = [((Fraction(1, 3),) * 3, [(0, 0), (-1, 0), (0, -1)])]
    for _ in range(3):
        n = random.randint(2, 4)
        raw = [random.randint(1, 5) for _ in range(n)]
        sets.append((tuple(Fraction(r, sum(raw)) for r in raw), [(random.randint(-2, 2), random.randint(-2, 2)) for _ in range(n)]))
    for ws, vs in sets:
        lam = lam_of(ws, vs)
        wr = [sp.Rational(w) for w in ws]
        m = sp.Matrix([sum(w * v[i] for w, v in zip(wr, vs)) for i in range(2)])
        M = sp.Matrix(2, 2, lambda i, j: sum(w * v[i] * v[j] for w, v in zip(wr, vs)))
        Cov = M - m * m.T
        c = coeffs(lam, 2)
        ok = ok and sp.simplify(c[1] + sp.I * (m.T * kv)[0]) == 0 and sp.simplify(c[2] + sp.Rational(1, 2) * (kv.T * M * kv)[0]) == 0
        a2 = coeffs(sp.expand(lam * sp.conjugate(lam), complex=True), 3)
        ok = ok and sp.simplify(a2[2] + (kv.T * Cov * kv)[0]) == 0 and sp.simplify(a2[3]) == 0 and sp.simplify(a2[1]) == 0
    check("V1", ok, "|lambda| <= 1 with equality exactly where the characters coincide (8x8, 12x12 grids); lambda = 1 - i m.k - (1/2) k^T M k "
          "+ O(k^3) with M the second moment, and |lambda|^2 = 1 - k^T Cov k + O(k^4), exact series on NEC and three random positive sets")

    # V2
    wr = [sp.Rational(1, 3)] * 3
    vs = [(0, 0), (-1, 0), (0, -1)]
    m = sp.Matrix([sum(w * v[i] for w, v in zip(wr, vs)) for i in range(2)])
    M = sp.Matrix(2, 2, lambda i, j: sum(w * v[i] * v[j] for w, v in zip(wr, vs)))
    Cov = M - m * m.T
    lam = lam_of(wr, vs)
    mod2 = sp.expand(lam * sp.conjugate(lam), complex=True)
    H = sp.Matrix(2, 2, lambda i, j: sp.simplify(sp.diff(mod2, [k1, k2][i], [k1, k2][j]).subs({k1: 0, k2: 0})))
    ok = m == sp.Matrix([-sp.Rational(1, 3), -sp.Rational(1, 3)]) and Cov.det() == sp.Rational(1, 27) and H == -2 * Cov
    ok = ok and H[0, 0] == -sp.Rational(4, 9) and H[0, 1] == sp.Rational(2, 9) and H.det() == sp.Rational(4, 27)
    check("V2", ok, f"NEC: mean {list(m)}, det Cov = {Cov.det()}, Hessian of |lambda|^2 at 0 = {H.tolist()} = -2 Cov, det {H.det()}")

    # V3
    k3 = sp.symbols("k3", real=True)
    lam7 = (1 + 2 * (sp.cos(k1) + sp.cos(k2) + sp.cos(k3))) / 7
    E = sum(2 * (1 - sp.cos(k)) for k in (k1, k2, k3))
    ok = sp.simplify(lam7 - (1 - E / 7)) == 0
    H7 = sp.Matrix(3, 3, lambda i, j: sp.simplify(sp.diff(lam7 ** 2, [k1, k2, k3][i], [k1, k2, k3][j]).subs({k1: 0, k2: 0, k3: 0})))
    ok = ok and H7 == -sp.Rational(4, 7) * sp.eye(3)
    grid = [sp.pi * sp.Rational(n, 6) for n in range(-5, 7)]
    vals = [sp.nsimplify((1 - E / 7).subs({k1: a, k2: b, k3: c})) for a in grid for b in grid for c in grid if (a, b, c) != (0, 0, 0)]
    ok = ok and all(-sp.Rational(5, 7) <= v < 1 for v in vals) and min(vals) == -sp.Rational(5, 7)
    check("V3", ok, "7-stencil: lambda = 1 - E/7 identically, real; on a (pi/6) grid of (-pi, pi]^3 minus 0 it lies in [-5/7, 1), so |lambda| < 1; "
          "Hessian of |lambda|^2 at 0 = -(4/7) I")

    # V4
    ws = [sp.Rational(1, 3)] * 3
    col = [(0, 0), (1, 1), (2, 2)]
    mm = sp.Matrix([sum(w * v[i] for w, v in zip(ws, col)) for i in range(2)])
    MM = sp.Matrix(2, 2, lambda i, j: sum(w * v[i] * v[j] for w, v in zip(ws, col)))
    CC = MM - mm * mm.T
    s = sp.symbols("s", real=True)
    lamc = lam_of(ws, col).subs({k1: s, k2: -s})
    ok = CC.det() == 0 and sp.simplify(sp.expand(lamc * sp.conjugate(lamc), complex=True) - 1) == 0
    lam1 = lam_of([1], [(2, -1)])
    ok = ok and sp.simplify(sp.expand(lam1 * sp.conjugate(lam1), complex=True) - 1) == 0
    check("V4", ok, "collinear support {(0,0),(1,1),(2,2)}: det Cov = 0 and |lambda(s, -s)| = 1 identically (undamped to all orders, "
          "not only to second); a singleton gives a pure phase")

    # V5
    lam_neg = 2 - sp.exp(-sp.I * sp.pi)
    c, k = sp.symbols("c k", positive=True)
    b = 2 - 4 * c ** 2 * sp.sin(k / 2) ** 2
    disc_ok = all(sp.simplify((b ** 2 - 4).subs({c: sp.Rational(1, 2), k: sp.pi * n / 12})) <= 0 for n in range(25))
    argz = sp.acos(b / 2).subs(c, sp.Rational(1, 2))
    ser = sp.series(argz, k, 0, 4).removeO()
    ok = sp.Abs(lam_neg) == 3 and disc_ok and sp.simplify(ser - (k / 2 + sp.Rational(1, 24) * (sp.Rational(1, 8) - sp.Rational(1, 2)) * k ** 3)) == 0
    check("V5", ok, "step 5: weights (2, -1) give |lambda(pi)| = 3 (growth, not a wave); the gain-one two-level recursion with weight -1 on "
          "the earlier level (discrete wave equation, product of roots 1, discriminant <= 0 at c = 1/2) has |z| = 1 and arg z = k/2 + O(k^3): "
          "the wave the task names as excluded by positivity, not exhibited by the attempt, whose step 5 is a reading")

    if fails:
        print("SUMMARY: fails at a checked step (see FAIL lines)")
        return 1
    print("HIT: confirmed - a3's one-level statement survives: for a finite nonnegative predecessor measure, |lambda| <= 1 with equality only "
          "where the characters coincide, lambda = 1 - i m.k - (1/2) k^T M k + O(k^3) (M the second moment), |lambda|^2 = 1 - k^T Cov k + "
          "O(k^4), so with Cov positive definite the mode nearest 1 is drift plus diffusion, never |lambda| = 1 with arg = c|k|; NEC and the "
          "7-stencil values, and the collinear and singleton exceptions (undamped to all orders transversally) re-verified")
    print("SUMMARY: confirmed - no failing step for the one-level statement; the multi-level case is stated as not done, and step 5's "
          "list of what would give waves is a reading whose negative-weight example is growth (the wave-equation example is not given)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
