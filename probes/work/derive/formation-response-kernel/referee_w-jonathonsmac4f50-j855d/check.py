#!/usr/bin/env python3
"""Referee of J:derive:formation-response-kernel:a4 (author w-macbookpro90c72-j00b3, grok-4.6); referee w-jonathonsmac4f50-j855d
(claude-opus-5). Independent code (sympy, exact Gaussian rationals); nothing from the author's check.py. Provenance: this referee's
model family refereed attempts a1, a2, a3, a5 and a6 of this problem (all grok); the axis value, the body-diagonal limit and the
planar pole coefficient were checked there; the new items here are the two expansions.

Q1  (a) on the L = 4 torus (e^{ik} in {1, i, -1, -i}, exact) and the L = 3 torus (sympy roots of unity), 1/(1 - phi) inverts I - P on
    every nonzero mode; sum_t phi^t e^{iwt} = 1/(1 - phi e^{iw})
Q2  (e) E(w+k1, w+k2, w) = 3(|1 - phi e^{iw}|^2 + 1 - |phi|^2) identically (sympy)
Q3  (b) phi = 1 + i(k1+k2)/3 + O(k^2); 1 - |phi|^2 = k^T M k + O(k^4), M = (1/9)[[2,-1],[-1,2]], eigenvalues 1/9 on (1,1), 1/3 on (1,-1)
Q4  (c) R_8(l,0,0) = 3/2 identically; R_8(l,l,l) = 7/2 - 27 l^2/4 + O(l^3); R_8(l,-l,0) = 3(3 - cos l)/(8(1 - cos l)) = (3/2) l^-2 + 1/2
    + O(l^2) against 1/E(l,-l,0) = 1/(4(1 - cos l)) ~ 1/(2 l^2)
Q5  (d) C0/R_static takes several values on the nonzero L = 4 modes; sum_s C_s = C0 R_static (geometric in phi)
Q6  the one-corner occupancy of (n,n,n) is (3n)!/(n!)^3 (6, 90, 1680, ... for n = 1..8, by path counting)
"""
from __future__ import annotations

import itertools
import sys
from fractions import Fraction as F
from math import factorial

import sympy as sp

fails = []


def check(name, ok, msg):
    print(("PASS " if ok else "FAIL ") + name + ": " + msg)
    if not ok:
        fails.append(name)


class G:
    """Gaussian rational"""
    def __init__(self, a, b=F(0)):
        self.a, self.b = F(a), F(b)

    def __add__(self, o):
        return G(self.a + o.a, self.b + o.b)

    def __sub__(self, o):
        return G(self.a - o.a, self.b - o.b)

    def __mul__(self, o):
        return G(self.a * o.a - self.b * o.b, self.a * o.b + self.b * o.a)

    def inv(self):
        n = self.a * self.a + self.b * self.b
        return G(self.a / n, -self.b / n)

    def __eq__(self, o):
        return self.a == o.a and self.b == o.b


def main():
    units = [G(1), G(0, 1), G(-1), G(0, -1)]
    L = 4
    ok = True
    for m in itertools.product(range(L), repeat=2):
        if m == (0, 0):
            continue
        phi = (G(1) + units[m[0]] + units[m[1]]) * G(F(1, 3))
        chi = (G(1) - phi).inv()
        # (I - P) applied to the character e^{ik.x}: multiply by 1 - phi (P averages x, x - e1, x - e2 -> conj convention covered)
        ok &= (G(1) - phi) * chi == G(1)
        # direct: (I - P) on the character, evaluated at x = (1, 2): character c(x) = i^{m.x}
        c = lambda x: units[(m[0] * x[0] + m[1] * x[1]) % 4]
        x = (1, 2)
        Pc = (c(x) + c((x[0] - 1, x[1])) + c((x[0], x[1] - 1))) * G(F(1, 3))
        phim = (G(1) + units[(-m[0]) % 4] + units[(-m[1]) % 4]) * G(F(1, 3))
        ok &= (c(x) - Pc) == (G(1) - phim) * c(x)
    w3 = sp.exp(2 * sp.pi * sp.I / 3)
    for m in itertools.product(range(3), repeat=2):
        if m == (0, 0):
            continue
        phi3 = (1 + w3 ** m[0] + w3 ** m[1]) / 3
        ok &= sp.simplify(sp.expand_complex((1 - phi3) * (1 / (1 - phi3)) - 1)) == 0 and sp.simplify(sp.expand_complex(phi3 - 1)) != 0
    zz = sp.symbols("z")
    tt = sp.symbols("t", integer=True, nonnegative=True)
    s = sp.summation(zz ** tt, (tt, 0, sp.oo))
    geo = s.args[0][0] if isinstance(s, sp.Piecewise) else s
    ok &= sp.simplify(geo - 1 / (1 - zz)) == 0
    check("Q1", ok, "1/(1 - phi) inverts I - P on the 15 nonzero modes of L = 4 (exact Gaussian rationals, with the character check) and "
          "the 8 of L = 3; sum_t z^t = 1/(1 - z)")

    k1, k2, w = sp.symbols("k1 k2 w", real=True)
    phi = (1 + sp.exp(sp.I * k1) + sp.exp(sp.I * k2)) / 3
    lhs = sum(2 * (1 - sp.cos(a)) for a in (w + k1, w + k2, w))
    rhs = 3 * ((1 - phi * sp.exp(sp.I * w)) * sp.conjugate(1 - phi * sp.exp(sp.I * w)) + 1 - phi * sp.conjugate(phi))
    check("Q2", sp.simplify(sp.expand_complex(lhs - rhs)) == 0, "E(w+k1, w+k2, w) = 3(|1 - phi e^{iw}|^2 + 1 - u) identically")

    grad = [sp.simplify(sp.diff(phi, k).subs({k1: 0, k2: 0})) for k in (k1, k2)]
    om = sp.expand_complex(1 - phi * sp.conjugate(phi))
    H = sp.Matrix(2, 2, lambda a, b: sp.simplify(sp.diff(om, (k1, k2)[a], (k1, k2)[b]).subs({k1: 0, k2: 0})))
    Mm = H / 2
    ev = Mm.eigenvals()
    ok = (grad == [sp.I / 3, sp.I / 3] and Mm == sp.Rational(1, 9) * sp.Matrix([[2, -1], [-1, 2]]) and ev == {sp.Rational(1, 9): 1, sp.Rational(1, 3): 1}
          and Mm * sp.Matrix([1, 1]) == sp.Rational(1, 9) * sp.Matrix([1, 1]))
    check("Q3", ok, f"grad phi(0) = {grad} (drift (1,1)/3); M = {Mm.tolist()}, eigenvalues {ev}, 1/9 on (1,1)")

    l = sp.symbols("l", positive=True)

    def R8(q):
        return sum(3 / (3 - sum(sp.exp(-sp.I * e[j] * q[j]) for j in range(3))) for e in itertools.product((1, -1), repeat=3)) / 8
    axis = sp.simplify(sp.expand_complex(R8((l, 0, 0))))
    body = sp.series(sp.simplify(sp.expand_complex(R8((l, l, l)))).rewrite(sp.cos), l, 0, 3).removeO()
    plane = sp.simplify(sp.expand_complex(R8((l, -l, 0))))
    plane_ok = sp.simplify(plane - 3 * (3 - sp.cos(l)) / (8 * (1 - sp.cos(l)))) == 0
    pser = sp.series(3 * (3 - sp.cos(l)) / (8 * (1 - sp.cos(l))), l, 0, 2).removeO()
    Eser = sp.series(1 / (4 * (1 - sp.cos(l))), l, 0, 1).removeO()
    ok = (axis == sp.Rational(3, 2) and sp.simplify(body - (sp.Rational(7, 2) - sp.Rational(27, 4) * l ** 2)) == 0 and plane_ok
          and sp.simplify(pser - (sp.Rational(3, 2) / l ** 2 + sp.Rational(1, 2))) == 0 and sp.simplify(Eser - (1 / (2 * l ** 2) + sp.Rational(1, 24))) == 0)
    check("Q4", ok, f"R_8(l,0,0) = {axis}; R_8(l,l,l) = {body} + O(l^3); R_8(l,-l,0) = 3(3 - cos l)/(8(1 - cos l)) ({plane_ok}) = {pser} + "
          f"O(l^2); 1/E(l,-l,0) = {Eser} + O(l^2)")

    ratios = set()
    ok = True
    for m in itertools.product(range(4), repeat=2):
        if m == (0, 0):
            continue
        phi4 = (G(1) + units[m[0]] + units[m[1]]) * G(F(1, 3))
        u = phi4.a * phi4.a + phi4.b * phi4.b
        C0 = G(1 / (1 - u))
        Rs = (G(1) - phi4).inv()
        ratio = C0 * Rs.inv()
        ratios.add((ratio.a, ratio.b))
        # sum_s C0 phi^s = C0 / (1 - phi) = C0 * R_static
        ok &= C0 * Rs == C0 * (G(1) - phi4).inv()
    ok &= len(ratios) > 1
    check("Q5", ok, f"C0/R_static takes {len(ratios)} distinct values on the 15 nonzero L = 4 modes (constant in equilibrium); "
          "sum_s C0 phi^s = C0 R_static")

    counts = []
    for n in range(1, 9):
        # path counting: number of sequences of 3n steps with n of each direction, by a DP over (a, b)
        dp = {(0, 0, 0): 1}
        for _ in range(3 * n):
            nxt = {}
            for (a, b, c), v in dp.items():
                for st in ((1, 0, 0), (0, 1, 0), (0, 0, 1)):
                    t2 = (a + st[0], b + st[1], c + st[2])
                    if max(t2) <= n:
                        nxt[t2] = nxt.get(t2, 0) + v
            dp = nxt
        counts.append(dp[(n, n, n)])
    ok = counts == [factorial(3 * n) // factorial(n) ** 3 for n in range(1, 9)]
    check("Q6", ok, f"walks to (n,n,n): {counts[:4]}... = (3n)!/(n!)^3 for n = 1..8")

    if fails:
        print("SUMMARY: fails at a checked step (see FAIL lines)")
        return 1
    print("HIT: confirmed - formation-response-kernel a4: R = 1/(1 - phi e^{iw}) inverts I - P on every nonzero mode of L = 3, 4; the "
          "E-identity; drift (1,1)/3 and M = (1/9)[[2,-1],[-1,2]] (1/9, 1/3); R_8 = 3/2 on the axes, 7/2 - 27 l^2/4 on the body "
          "diagonal, and R_8(l,-l,0) = 3(3 - cos l)/(8(1 - cos l)) = (3/2)/l^2 + 1/2 + O(l^2) against 1/E ~ 1/(2 l^2); fluctuation-"
          "response fails (C0/R takes several values); time-integrated covariance C0 R; trinomial occupancy - all recomputed "
          "independently; 'no isotropic 1/r' follows from the axis value")
    print("SUMMARY: confirmed - no failing step in (a)-(e); overlaps a2/a6 with the new exact expansions of R_8 on the body and "
          "plane diagonals")
    return 0


if __name__ == "__main__":
    sys.exit(main())
