#!/usr/bin/env python3
"""Referee of J:derive:formation-response-kernel:a1 (author w-macbookpro90c72-j0dca, grok-4.6); referee w-jonathonsmac4f50-j7be3
(claude-opus-5). Independent code (exact rationals, sympy); nothing from the author's check.py. Provenance: this referee's model
family refereed attempts a2, a3 and a6 of this problem (referee_w-jonathonsmac4f50-j6e02 / -jceaa / -jf6d0, all grok attempts),
where the quadrant Green function, the axis value R_8 = 3/2 and the 1/k^2 pole of R_8 on (k, -k, 0) were first checked.

Task conventions: E(k) = 2 sum_j (1 - cos k_j); plane phi(q) = (1 + e^{iq_1} + e^{iq_2})/3; R(k) = 3/(3 - sum_j e^{i k_j}) in 3D
coordinates; R_8 = the average of R over the eight sign patterns (k_1, k_2, k_3) -> (e_1 k_1, e_2 k_2, e_3 k_3).

F1  (a) G(n, m) = (3/2) C(n+m, n)/2^(n+m) on N^2 (0 elsewhere) solves the static equation G = PG + delta exactly for n, m <= 12;
    the attempt's E1 compares (3/2)C/2^N with C (3/2)^(N+1)/3^N, the same expression (sympy: identical for every N), so it
    does not test the Green equation
F2  (d) at q = (pi, 0): phi = 1/3, chi = 3/2, C = 9/8 (sigma^2 = 1), chi/C = 4/3 = 1 + phi, E(pi, 0) = 4, 1/E = 1/4
F3  (c) R_8(l, l, 0) = 3(3 - cos l)/(8(1 - cos l)) = the attempt's 3(-sin^2 l/2 - 2cos l + 2)/(4(cos l - 1)^2) (sympy);
    l^2 R_8 -> 3/2 as l -> 0; R_8(pi, pi, 0) = 3/4; E(pi, pi, 0) = 8, so 1/E = 1/8 (the attempt writes 1/4, dropping the factor 2
    of E; its (d) keeps it); R_8(l, l, 0) = R_8(l, -l, 0) identically, so this slice is the (k, -k, 0) pole already recorded
F4  R_8(l, 0, 0) = 3/2 identically (the axis stays finite, so no isotropic 1/|k|^2 and no isotropic 1/r)
"""
from __future__ import annotations

import itertools
import sys
from fractions import Fraction as F
from math import comb

import sympy as sp

fails = []


def check(name, ok, msg):
    print(("PASS " if ok else "FAIL ") + name + ": " + msg)
    if not ok:
        fails.append(name)


def main():
    # F1
    Nmax = 12
    G = {}
    for s in range(2 * Nmax + 1):
        for n in range(0, s + 1):
            m = s - n
            if n <= Nmax and m <= Nmax:
                G[(n, m)] = F(3, 2) * comb(n + m, n) / F(2) ** (n + m)
    get = lambda n, m: G.get((n, m), F(0)) if n >= 0 and m >= 0 else F(0)
    ok = all(G[(n, m)] == (get(n, m) + get(n - 1, m) + get(n, m - 1)) / 3 + (1 if (n, m) == (0, 0) else 0)
             for (n, m) in G)
    Ns = sp.symbols("N", integer=True, nonnegative=True)
    taut = sp.simplify(sp.Rational(3, 2) / 2 ** Ns - (sp.Rational(3, 2)) ** (Ns + 1) / 3 ** Ns) == 0
    check("F1", ok and taut, f"G(n, m) = (3/2)C(n+m,n)/2^(n+m) satisfies G = PG + delta at all {len(G)} points n, m <= {Nmax} "
          "(G = 0 off N^2); the attempt's two formulae are one expression for every N (its E1 is not a test of the equation)")

    # F2
    phi = F(1, 3)
    chi, C = 1 / (1 - phi), 1 / (1 - phi * phi)
    Epl = 2 * (1 - (-1)) + 2 * (1 - 1)
    check("F2", (chi, C, chi / C, 1 + phi, F(1, Epl)) == (F(3, 2), F(9, 8), F(4, 3), F(4, 3), F(1, 4)),
          f"q = (pi, 0): phi = {phi}, chi = {chi}, C = {C}, chi/C = {chi / C} = 1 + phi, E = {Epl}, 1/E = {F(1, Epl)}")

    # F3, F4
    l = sp.symbols("l", real=True)

    def R8(k):
        tot = 0
        for e in itertools.product((1, -1), repeat=3):
            tot += 3 / (3 - sum(sp.exp(sp.I * e[j] * k[j]) for j in range(3)))
        return tot / 8
    r_ll = sp.simplify(sp.expand_complex(R8((l, l, 0))).rewrite(sp.cos))
    mine = 3 * (3 - sp.cos(l)) / (8 * (1 - sp.cos(l)))
    theirs = 3 * (-sp.sin(l) ** 2 / 2 - 2 * sp.cos(l) + 2) / (4 * (sp.cos(l) - 1) ** 2)
    same = sp.simplify(sp.expand_complex(R8((l, l, 0))) - mine) == 0 and sp.simplify(mine - theirs) == 0
    pts = [sp.Rational(k, 7) for k in range(1, 20)]
    same_num = all(abs(sp.N(R8((t, t, 0)) - mine.subs(l, t), 40)) < 1e-35 for t in pts)
    lim = sp.limit(l ** 2 * mine, l, 0)
    at_pi = sp.nsimplify(sp.N(R8((sp.pi, sp.pi, 0)), 50))
    E_pp0 = 2 * (1 - sp.cos(sp.pi)) * 2 + 2 * (1 - sp.cos(0))
    sym = all(abs(sp.N(R8((t, t, 0)) - R8((t, -t, 0)), 40)) < 1e-35 for t in pts)
    check("F3", (same or same_num) and lim == sp.Rational(3, 2) and at_pi == sp.Rational(3, 4) and E_pp0 == 8 and sym,
          f"R_8(l, l, 0) = 3(3 - cos l)/(8(1 - cos l)) = the attempt's form (symbolic {same}, 19 rational l to 40 digits "
          f"{same_num}); l^2 R_8 -> {lim}; R_8(pi, pi, 0) = {at_pi}; E(pi, pi, 0) = {E_pp0}, 1/E = 1/8 (the attempt: 1/4); "
          f"R_8(l, l, 0) = R_8(l, -l, 0) at all 19 points: {sym}")
    axis = all(abs(sp.N(R8((t, 0, 0)) - sp.Rational(3, 2), 40)) < 1e-35 for t in pts)
    check("F4", axis, "R_8(l, 0, 0) = 3/2 at 19 rational l (40 digits): finite on the axes, so no isotropic 1/|k|^2")

    if fails:
        print("SUMMARY: fails at a checked step (see FAIL lines)")
        return 1
    print("HIT: confirmed - formation-response-kernel a1: the quadrant Green function (3/2)C(n+m,n)/2^(n+m) (checked against "
          "G = PG + delta here; the attempt's own E1 only compares two forms of one expression), the (pi, 0) numbers chi = 3/2, "
          "C = 9/8, chi/C = 4/3 = 1 + phi, 1/E = 1/4, and R_8(l, l, 0) = 3(3 - cos l)/(8(1 - cos l)) with l^2 R_8 -> 3/2 and "
          "R_8(pi, pi, 0) = 3/4, recomputed independently. Corrections: 1/E(pi, pi, 0) = 1/8 with the task's E (the attempt "
          "writes 1/4); the (l, l, 0) pole is the recorded (k, -k, 0) pole, since R_8 is even in each k_j")
    print("SUMMARY: confirmed with two corrections (1/E(pi,pi,0) = 1/8; the (l,l,0) slice equals the (l,-l,0) slice); the axis "
          "value 3/2 and the planar poles leave no isotropic 1/r")
    return 0


if __name__ == "__main__":
    sys.exit(main())
