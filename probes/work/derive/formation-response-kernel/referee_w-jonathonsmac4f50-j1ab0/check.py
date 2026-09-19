#!/usr/bin/env python3
"""Referee of J:derive:formation-response-kernel:a5 (author w-macbookpro90c72-jcaf5, grok-4.6); referee w-jonathonsmac4f50-j1ab0
(claude-opus-5). Independent code (sympy, exact rationals, big integers); nothing from the author's check.py. Provenance: this
referee's model family refereed attempts a1, a2, a3 and a6 of this problem (all grok); the directed 1/R of the point response was
checked in those reports.

Linear formation on the level plane: phi(k) = (1 + e^{ik_1} + e^{ik_2})/3, E(k) = 2 sum_j (1 - cos k_j), C = sigma^2/(1 - |phi|^2).

V1  R(k, w) = sum_t (phi e^{iw})^t = 1/(1 - phi e^{iw}), chi = R(k, 0) = 1/(1 - phi) (sympy)
V2  at k = (pi, 0): phi = 1/3, chi = 3/2, C = 9/8 (sigma^2 = 1), E = 4, chi/C = 4/3 = 1 + phi
V3  the four in-plane corner orders phi = (1 + e^{+-ik_1} + e^{+-ik_2})/3 all equal 1/3 at (pi, 0), so each chi is 3/2; truncated sum
    (1 - phi^4)/(1 - phi) = 40/27
V4  the equal-level covariance is two-dimensional: the return sum L^-2 sum_{k != 0} 1/(1 - |phi|^2) grows by a constant per doubling
V5  what the one-momentum argument does not give: chi != 1/E as functions (one point suffices), but not the absence of 1/r decay;
    the point response T(n,n,n) = (3n)!/(n!^3 27^n) along the drift diagonal has n T -> sqrt3/(2 pi), a directed 1/R channel, so the
    SUMMARY's 'no 1/r in 3D' holds only as 'no isotropic 1/r'
"""
from __future__ import annotations

import math
import sys
from fractions import Fraction as F
from math import factorial

import numpy as np
import sympy as sp

fails = []


def check(name, ok, msg):
    print(("PASS " if ok else "FAIL ") + name + ": " + msg)
    if not ok:
        fails.append(name)


def main():
    z = sp.symbols("z")
    t = sp.symbols("t", integer=True, nonnegative=True)
    geo = sp.summation(z ** t, (t, 0, sp.oo))
    ok = sp.simplify(geo.args[0][0] - 1 / (1 - z)) == 0 if isinstance(geo, sp.Piecewise) else sp.simplify(geo - 1 / (1 - z)) == 0
    check("V1", ok, "sum_t (phi e^{iw})^t = 1/(1 - phi e^{iw}) for |phi| < 1; chi = R at w = 0")

    phi = F(1 + (-1) + 1, 3)
    chi, C, E = 1 / (1 - phi), 1 / (1 - phi * phi), 2 * (1 - (-1)) + 2 * (1 - 1)
    check("V2", (phi, chi, C, E, chi / C) == (F(1, 3), F(3, 2), F(9, 8), 4, F(4, 3)),
          f"(pi, 0): phi = {phi}, chi = {chi}, C = {C}, E = {E}, 1/E = {F(1, E)}, chi/C = {chi / C}")

    corners = []
    for s1 in (1, -1):
        for s2 in (1, -1):
            corners.append(sp.nsimplify((1 + sp.exp(sp.I * s1 * sp.pi) + sp.exp(sp.I * s2 * 0)) / 3))
    trunc = (1 - phi ** 4) / (1 - phi)
    check("V3", all(c == sp.Rational(1, 3) for c in corners) and trunc == F(40, 27),
          f"corner phi's at (pi, 0): {corners}; each chi = 3/2; truncated sum {trunc}")

    rows = []
    for L in (8, 16, 32, 64, 128):
        g = np.meshgrid(*[2 * np.pi * np.arange(L) / L] * 2, indexing="ij")
        ph = (1 + np.exp(1j * g[0]) + np.exp(1j * g[1])) / 3
        w = 1 - np.abs(ph) ** 2
        w.flat[0] = np.inf
        rows.append((L, float((1 / w).sum() / L ** 2)))
    inc = [b[1] - a[1] for a, b in zip(rows, rows[1:])]
    check("V4", max(inc) - min(inc) < 0.01 and min(inc) > 0.5, f"return sums {[(L, round(v, 4)) for L, v in rows]}, increments "
          f"{[round(x, 4) for x in inc]} per doubling: logarithmic")

    vals = {}
    for n in (100, 1000, 3000):
        T = F(factorial(3 * n), factorial(n) ** 3 * 27 ** n)
        vals[n] = float(n * T)
    target = math.sqrt(3) / (2 * math.pi)
    check("V5", abs(vals[3000] - target) < 1e-4 and abs(vals[3000] - target) < abs(vals[100] - target),
          "n T(n,n,n) = " + ", ".join(f"{v:.7f} (n = {n})" for n, v in vals.items()) + f" -> sqrt3/(2 pi) = {target:.7f}: a directed 1/R "
          "decay along the drift diagonal")

    if fails:
        print("SUMMARY: fails at a checked step (see FAIL lines)")
        return 1
    print("HIT: confirmed - formation-response-kernel a5: R = 1/(1 - phi e^{iw}), chi = 1/(1 - phi); at (pi, 0) phi = 1/3, chi = 3/2, "
          "C = 9/8, 1/E = 1/4, chi/C = 4/3 = 1 + phi (fluctuation-response fails); the four in-plane corner orders all give chi = 3/2 "
          "there, so no channel equals 1/E; truncated sum 40/27; the equal-level covariance is logarithmic; recomputed independently. "
          "Correction: a single momentum shows 'not equal to 1/E', not 'no 1/r decay' - the point response has a directed 1/R along "
          "the drift diagonal (n T(n,n,n) -> sqrt3/(2 pi)), so the SUMMARY's 'no 1/r in 3D' should read 'no isotropic 1/r'")
    print("SUMMARY: confirmed with a correction to the scope of 'no 1/r' (one momentum; a directed 1/R channel exists)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
