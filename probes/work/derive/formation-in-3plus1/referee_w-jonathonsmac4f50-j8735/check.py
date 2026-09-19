#!/usr/bin/env python3
"""Referee of J:derive:formation-in-3plus1:a2 (author w-macbookpro90c72-j8a75, grok-4.6); referee w-jonathonsmac4f50-j8735
(claude-opus-5). Independent code (sympy with hyperbolics rewritten in exponentials, exact Gaussian-rational Fourier sums, mpmath
spot values); nothing from the author's check.py. Provenance: the monotonicity of A(k)/k was first proved in block 27 (PR #8171,
by series) in this referee's model family's campaign; the attempt gives a different proof. G_4 = 1913/1344 was re-derived by this
referee's family in the kernel-normalization referee (two ways).

Setting (backward 3+1, n = 4 predecessors): phi(k) = (1 + sum_j e^{-i k_j})/4; A(k) = coth k - 1/k.

P1  (i) (A/k)' = -g/k^3 with g = k^2 csch^2 k + k coth k - 2 = n(2k)/(4 sinh^2 k), n(u) = u^2 + u sinh u - 4 cosh u + 4;
    n(0) = n'(0) = n''(0) = n'''(0) = 0, n'''' = u sinh u (sympy); hence n > 0 on (0, inf) and A/k strictly decreasing;
    A/k -> 1/3 (k -> 0), -> 0 (k -> inf); spot values of A/k decreasing at 41 points in (0, 50] (mpmath)
P2  (ii) A(k) = k/3 - k^3/45 + ..., so m -> A(n beta m) has slope n beta/3 at 0: unstable iff beta > 3/4 for n = 4
P3  (iii) the Hessian of 1 - |phi|^2 at 0 is H = (1/8)[[3,-1,-1],[-1,3,-1],[-1,-1,3]] with eigenvalues 1/8 (along (1,1,1)) and
    1/2 (twice); M = H/2 has 1/16 and 1/4 (twice), det M = 1/256; Im phi = -(k_1 + k_2 + k_3)/4 + O(k^3)
P4  (iv) on (Z/4)^3: G_4 = (1/64) sum_{k != 0} 1/(1 - |phi(k)|^2) = 1913/1344 (exact, e^{-ik} in {1, -i, -1, i})
"""
from __future__ import annotations

import itertools
import sys
from fractions import Fraction as F

import mpmath as mp
import sympy as sp

fails = []


def check(name, ok, msg):
    print(("PASS " if ok else "FAIL ") + name + ": " + msg)
    if not ok:
        fails.append(name)


def main():
    k, u = sp.symbols("k u", positive=True)
    A = sp.coth(k) - 1 / k
    dAk = sp.diff(A / k, k)
    g = k ** 2 / sp.sinh(k) ** 2 + k * sp.coth(k) - 2
    n = u ** 2 + u * sp.sinh(u) - 4 * sp.cosh(u) + 4
    ok1 = sp.simplify((dAk + g / k ** 3).rewrite(sp.exp)) == 0
    ok2 = sp.simplify((g - n.subs(u, 2 * k) / (4 * sp.sinh(k) ** 2)).rewrite(sp.exp)) == 0
    ders = [sp.simplify(sp.diff(n, u, j).subs(u, 0)) for j in range(4)]
    ok3 = ders == [0, 0, 0, 0] and sp.simplify(sp.diff(n, u, 4) - u * sp.sinh(u)) == 0
    l0 = sp.limit((A / k).rewrite(sp.exp), k, 0)          # sympy's limit of the coth form misfires at 0; the exp form is exact
    linf = sp.limit((A / k).rewrite(sp.exp), k, sp.oo)
    mp.mp.dps = 30
    xs = [mp.mpf(j) / 4 for j in range(1, 41)] + [mp.mpf(50)]
    vals = [(mp.coth(x) - 1 / x) / x for x in xs]
    ok4 = all(a > b for a, b in zip(vals, vals[1:]))
    check("P1", ok1 and ok2 and ok3 and l0 == sp.Rational(1, 3) and linf == 0 and ok4,
          f"(A/k)' = -g/k^3 ({ok1}); g = n(2k)/(4 sinh^2 k) ({ok2}); n(0..3)(0) = {ders}, n'''' = u sinh u ({ok3}); "
          f"limits {l0}, {linf}; A/k decreasing at 41 points in (0, 50] ({ok4})")

    ser = sp.series(A, k, 0, 5).removeO()
    check("P2", sp.simplify(ser - (k / 3 - k ** 3 / 45)) == 0 and sp.Rational(4, 3) * sp.Rational(3, 4) == 1,
          f"A = {ser} + O(k^5): slope n beta/3 at m = 0, threshold beta = 3/n = 3/4 at n = 4")

    k1, k2, k3 = sp.symbols("k1 k2 k3", real=True)
    ks = (k1, k2, k3)
    phi = (1 + sum(sp.exp(-sp.I * kk) for kk in ks)) / 4
    one_minus = sp.simplify(sp.expand_complex(1 - phi * sp.conjugate(phi)))
    H = sp.Matrix(3, 3, lambda a, b: sp.simplify(sp.diff(one_minus, ks[a], ks[b]).subs({k1: 0, k2: 0, k3: 0})))
    Hwant = sp.Rational(1, 8) * sp.Matrix([[3, -1, -1], [-1, 3, -1], [-1, -1, 3]])
    Mm = H / 2
    ev = Mm.eigenvals()
    v111 = Mm * sp.Matrix([1, 1, 1])
    imphi = sp.series(sp.im(sp.expand_complex(phi)).subs({k2: 0, k3: 0}), k1, 0, 3).removeO()
    grad = [sp.diff(sp.im(sp.expand_complex(phi)), kk).subs({k1: 0, k2: 0, k3: 0}) for kk in ks]
    check("P3", H == Hwant and ev == {sp.Rational(1, 16): 1, sp.Rational(1, 4): 2} and v111 == sp.Rational(1, 16) * sp.Matrix([1, 1, 1])
          and Mm.det() == sp.Rational(1, 256) and grad == [-sp.Rational(1, 4)] * 3 and sp.simplify(imphi + k1 / 4) == 0,
          f"H = {H.tolist()}; M eigenvalues {ev} ((1,1,1) carries 1/16), det M = {Mm.det()}; grad Im phi = {grad}")

    units = [(1, 0), (0, -1), (-1, 0), (0, 1)]                           # e^{-i pi m/2}, m = 0..3, as (re, im)
    tot = F(0)
    wvals = []
    for m in itertools.product(range(4), repeat=3):
        if m == (0, 0, 0):
            continue
        re = F(1 + sum(units[j][0] for j in m), 4)
        im = F(sum(units[j][1] for j in m), 4)
        w = 1 / (1 - (re * re + im * im))
        wvals.append(w)
        tot += w
    G4 = tot / 64
    check("P4", G4 == F(1913, 1344), f"G_4 = {G4} (63 nonzero modes; weights from {min(wvals)} to {max(wvals)})")

    if fails:
        print("SUMMARY: fails at a checked step (see FAIL lines)")
        return 1
    print("HIT: confirmed - formation-in-3plus1 a2: A(k)/k strictly decreasing from 1/3 to 0 by the n(u) route (g = n(2k)/(4 sinh^2 k), "
          "n and its first three derivatives vanish at 0, n'''' = u sinh u), mean-field threshold 3/4 at n = 4, 1 - |phi|^2 = k^T M k "
          "+ O(k^4) with M eigenvalues 1/16 along (1,1,1) and 1/4 twice (det 1/256), drift (1,1,1)/4, and G_4 = 1913/1344 on "
          "(Z/4)^3, all recomputed independently; the attempt states correctly that sphere LRO on Z^4 is not proved")
    print("SUMMARY: confirmed - no failing step in (i)-(iv); the monotonicity of A/k was already known (block 27, by series) and "
          "is re-proved here by a different route")
    return 0


if __name__ == "__main__":
    sys.exit(main())
