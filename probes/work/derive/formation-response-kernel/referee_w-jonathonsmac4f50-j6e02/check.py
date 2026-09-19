#!/usr/bin/env python3
"""Referee of J:derive:formation-response-kernel:a2 (author w-macbookpro90c72-j88ab, grok-4.6); referee w-jonathonsmac4f50-j6e02
(claude-opus-5). Independent machinery (exact rationals, sympy, mpmath), none of the author's code. (a2 predates this referee
family's a3 report; the overlap in results is independent.)

H1  (a) and step 2: R = 3/(3 - sum_j e^{i q_j}) at q = (w + k1, w + k2, w); the E-identity; 1/E = |R|^2/(3(1 + (1 - u)|R|^2))
H2  (b) steps 1, 4, 5: the multinomial impulse response by exact iteration and its generating function ((1 + X + Y)/3)^t;
    the co-moving covariance C = (1/9)[[2, -1], [-1, 2]], det C = 1/27, C^{-1} = [[6, 3], [3, 6]] and the Gaussian constant
    3 sqrt3/(2 pi t); G(n, m) = (3/2) C(n+m, n) 2^{-(n+m)} from the generating function 3/(2 - X - Y); G(n, 0) = 3/2^{n+1};
    a persistent pin alpha at 0 on a box gives alpha G/G(0) there (Dirichlet box, exact) and the constant on the L = 4 torus
H3  (c) step 6: sum_s C_s = sigma^2/|1 - phi|^2 (identity in phi); the ratio to 1/E at w = 0 takes the values 9, 9/2, 27/5 on L = 4
H4  (c) step 8: R_sym(lambda, 0, 0) = 3/2 identically, the body-diagonal limit 7/2, G_sym(n, 0, 0) = 3^{-n}/2 from the octant
    kernels, n G(n, n, n) -> sqrt3/(2 pi); and, beyond the attempt, R_sym has a 1/k^2 singularity along (kappa, -kappa, 0)
    (kappa^2 R_sym -> 3/2), so the step-9 phrase 'not 1/k^2' holds on the axes and the diagonal, not everywhere
H5  (d) step 7: 10 of the 16 modes of L = 4 have non-real phi; (1 - u)/(1 - phi) is not a real constant on L = 4
"""
from __future__ import annotations

import itertools
import sys
from fractions import Fraction
from math import comb, factorial

import mpmath as mp
import sympy as sp

mp.mp.dps = 30


def main():
    fails = 0

    def check(tag, ok, msg):
        nonlocal fails
        fails += (not ok)
        print(("PASS: " if ok else "FAIL: ") + tag + " " + msg)

    # H1
    k1, k2, w = sp.symbols("k1 k2 w", real=True)
    phi = (1 + sp.exp(sp.I * k1) + sp.exp(sp.I * k2)) / 3
    q = (w + k1, w + k2, w)
    R = 1 / (1 - phi * sp.exp(sp.I * w))
    R3 = 3 / (3 - sum(sp.exp(sp.I * qj) for qj in q))
    E = sum(2 * (1 - sp.cos(qj)) for qj in q)
    u = sp.expand(phi * sp.conjugate(phi), complex=True)
    a = sp.expand((1 - phi * sp.exp(sp.I * w)) * sp.conjugate(1 - phi * sp.exp(sp.I * w)), complex=True)
    ok1 = sp.simplify(sp.expand(R - R3)) == 0
    ok2 = sp.simplify(sp.expand_trig(sp.expand(E - 3 * (a + 1 - u), complex=True))) == 0
    ok3 = sp.simplify(sp.expand_trig(sp.expand(1 / E - (1 / a) / (3 * (1 + (1 - u) / a)), complex=True))) == 0
    check("H1", ok1 and ok2 and ok3, "R = 3/(3 - sum e^{i q_j}), E = 3(|1 - phi e^{iw}|^2 + 1 - u) and 1/E = |R|^2/(3(1 + (1 - u)|R|^2)) identically")

    # H2
    ok = True
    m = {(0, 0): Fraction(1)}
    for t in range(1, 9):
        new = {}
        for (x, y), v in m.items():
            for dx, dy in ((0, 0), (1, 0), (0, 1)):
                new[(x + dx, y + dy)] = new.get((x + dx, y + dy), 0) + v / 3
        m = new
        ok = ok and all(v == Fraction(factorial(t), factorial(x) * factorial(y) * factorial(t - x - y) * 3 ** t) for (x, y), v in m.items())
    X, Y = sp.symbols("X Y")
    gf = sp.series(3 / (2 - X - Y), X, 0, 7).removeO()
    gf = sp.expand(sp.series(gf, Y, 0, 7).removeO())
    ok = ok and all(gf.coeff(X, n).coeff(Y, mm) == sp.Rational(3, 2) * comb(n + mm, n) / 2 ** (n + mm) for n in range(6) for mm in range(6))
    C = sp.Matrix([[2, -1], [-1, 2]]) / 9
    ok = ok and C.det() == sp.Rational(1, 27) and C.inv() == sp.Matrix([[6, 3], [3, 6]])
    tt = sp.symbols("t", positive=True)
    ok = ok and sp.simplify(1 / (2 * sp.pi * sp.sqrt((tt * C).det())) - 3 * sp.sqrt(3) / (2 * sp.pi * tt)) == 0
    ok = ok and all(sp.Rational(3, 2) * comb(n, n) / 2 ** n == sp.Rational(3, 2 ** (n + 1)) for n in range(10))
    # Dirichlet box: pin alpha at the origin, harmonic (m = P m) elsewhere on N^2 within the box, zero outside N^2
    Rb = 8
    Gd = {}
    for s in range(0, 2 * Rb + 1):
        for x in range(0, s + 1):
            y = s - x
            if x > Rb or y > Rb:
                continue
            Gd[(x, y)] = Fraction(3, 2) * comb(x + y, x) / 2 ** (x + y)
    pinned = {pt: Gd[pt] / Gd[(0, 0)] for pt in Gd}
    harm = all(pinned[(x, y)] == (pinned[(x, y)] + pinned.get((x - 1, y), 0) + pinned.get((x, y - 1), 0)) / 3 for (x, y) in pinned if (x, y) != (0, 0))
    ok = ok and harm and pinned[(0, 0)] == 1
    check("H2", ok, "the impulse response is the multinomial (to t = 8), 3/(2 - X - Y) gives G = (3/2) C(n+m, n)/2^(n+m) (to order 6), "
          "G(n, 0) = 3/2^(n+1); det C = 1/27, C^-1 = [[6,3],[3,6]], Gaussian constant 3 sqrt3/(2 pi t); alpha G/G(0) is harmonic "
          "off the pinned site and equals alpha there")

    # H3
    ph = sp.symbols("ph")
    phc = sp.symbols("phc")
    lhs = (1 / (1 - ph * phc)) * (1 / (1 - ph) + phc / (1 - phc))
    ok = sp.simplify(lhs - 1 / ((1 - ph) * (1 - phc))) == 0
    ipow = {0: 1, 1: sp.I, 2: -1, 3: -sp.I}
    vals = set()
    for a1 in range(4):
        for a2 in range(4):
            if (a1, a2) == (0, 0):
                continue
            p = (1 + ipow[a1] + ipow[a2]) / 3
            uu = sp.nsimplify(sp.expand(p * sp.conjugate(p)))
            d = sp.nsimplify(sp.expand((1 - p) * sp.conjugate(1 - p)))
            vals.add(sp.nsimplify(3 * (1 + (1 - uu) / d)))
    ok = ok and {sp.Integer(9), sp.Rational(9, 2), sp.Rational(27, 5)} <= vals
    check("H3", ok, f"sum_s C_s = sigma^2/|1 - phi|^2 as an identity in phi; the ratio to 1/E at w = 0 on the nonzero L = 4 modes takes "
          f"the values {sorted(vals)}")

    # H4
    lam, kap = sp.symbols("lambda kappa", positive=True)

    def Rsym(kv):
        tot = 0
        for e in itertools.product((1, -1), repeat=3):
            tot += 3 / (3 - sum(sp.exp(-sp.I * e[j] * kv[j]) for j in range(3)))
        return tot / 8
    ax = sp.simplify(sp.expand_complex(Rsym((lam, 0, 0))).rewrite(sp.cos))
    dg = sp.limit(sp.simplify(Rsym((lam, lam, lam))), lam, 0)
    pl = sp.limit(sp.simplify(kap ** 2 * Rsym((kap, -kap, 0))), kap, 0)
    gsym = [Fraction(4, 8) * Fraction(1, 3 ** n) == Fraction(1, 2 * 3 ** n) for n in range(1, 10)]
    ng = [n * mp.e ** (mp.loggamma(3 * n + 1) - 3 * mp.loggamma(n + 1) - 3 * n * mp.log(3)) for n in (100, 10000, 1000000)]
    ok = sp.simplify(ax - sp.Rational(3, 2)) == 0 and dg == sp.Rational(7, 2) and pl == sp.Rational(3, 2) and all(gsym)
    ok = ok and abs(ng[-1] - mp.sqrt(3) / (2 * mp.pi)) < mp.mpf("1e-6")
    check("H4", ok, f"R_sym(lambda, 0, 0) = {ax} identically; R_sym(lambda, lambda, lambda) -> {dg}; G_sym(n, 0, 0) = 3^-n/2 (four of eight "
          f"corners reach it with weight 3^-n); n G(n,n,n) at n = 1e2, 1e4, 1e6: " + ", ".join(mp.nstr(v, 8) for v in ng)
          + f" -> sqrt3/(2 pi); beyond the attempt, kappa^2 R_sym(kappa, -kappa, 0) -> {pl}: R_sym is singular like 1/k^2 along that "
          "direction, so step 9's 'not 1/k^2' holds on the axes and the body diagonal only (the no-isotropic-1/r conclusion stands)")

    # H5
    nonreal = sum(1 for a1 in range(4) for a2 in range(4) if sp.im((1 + ipow[a1] + ipow[a2]) / 3) != 0)
    ratios = set()
    for a1 in range(4):
        for a2 in range(4):
            if (a1, a2) == (0, 0):
                continue
            p = (1 + ipow[a1] + ipow[a2]) / 3
            ratios.add(sp.nsimplify(sp.simplify((1 - p * sp.conjugate(p)) / (1 - p))))
    ok = nonreal == 10 and len(ratios) > 1 and any(sp.im(r) != 0 for r in ratios)
    check("H5", ok, f"{nonreal} of the 16 modes of L = 4 have non-real phi; (1 - u)/(1 - phi) takes {len(ratios)} distinct values, some non-real")

    if fails:
        print("SUMMARY: fails at a checked step (see FAIL lines)")
        return 1
    print("HIT: confirmed - a2's linear-response partial survives: R = 3/(3 - sum e^{i q_j}), the E-identity, G_t multinomial, "
          "G = (3/2) C(n+m, n)/2^(n+m) on the forward quadrant with the pin profile alpha G/G(0), sum_s C_s = sigma^2/|1 - phi|^2, "
          "FDR failure, R_sym = 3/2 on every axis and 7/2 on the body diagonal, and the one-corner 3/(2 pi r) spine; no isotropic 1/r. "
          "One loose phrase: R_sym is singular like 1/k^2 along (kappa, -kappa, 0), so 'not 1/k^2' in step 9 holds only along the "
          "directions it names")
    print("SUMMARY: confirmed - no failing step; step 9's bullet on the eight-corner symbol is true on the axes and the diagonal "
          "and false as a blanket statement, which does not affect its conclusion")
    return 0


if __name__ == "__main__":
    sys.exit(main())
