#!/usr/bin/env python3
"""Exact symbolic proof of Lemma 3.6 of parts/witness.md, plane by plane.

Lemma 3.6 is a sum over planes (mu, nu) of an identity in the variables of that plane plus the
vanishing of the same-index terms. So it is enough to prove, as rational functions:

 (a) d = 2, one plaquette: V_p = -2i * form, with form restricted to indices 1, 2, including the
     same-index terms mu = nu;
 (b) the same-index sum vanishes, sum_cyc cos(c) sin(a - b) = 0 for a + b + c = 0.

Given (a), (b) in d = 2 for each pair of indices, the d-dimensional form is the sum over planes of
the d = 2 forms minus the same-index terms, which vanish. Variables: half-angle phases u1, u2 for
k^1, v1, v2 for k^2, and k^3 = -k^1 - k^2, polarisations atil^i_1, atil^i_2.

PRE-REGISTERED CRITERION. S1: sympy simplifies the difference in (a) and the sum in (b) to 0.
FAIL means Lemma 3.6 is not an identity.
"""
from __future__ import annotations

import sympy as sp


def main():
    u1, u2, v1, v2 = sp.symbols("u1 u2 v1 v2", nonzero=True)
    a = sp.symbols("a11 a12 a21 a22 a31 a32")
    atil = [[a[0], a[1]], [a[2], a[3]], [a[4], a[5]]]
    # half-angle phases exp(i k^i_mu / 2)
    ph = [[u1, u2], [v1, v2], [1 / (u1 * v1), 1 / (u2 * v2)]]

    def cosh(x):
        return (x + 1 / x) / 2

    def sin2(x, y):
        # 2 sin((k^i - k^j)/2) with phases x = exp(i k^i/2), y = exp(i k^j/2)
        return (x / y - y / x) / sp.I

    # V_p for the plaquette with corner at the origin
    inc = []
    P = []
    for i in range(3):
        a1 = atil[i][0] * ph[i][0]
        a2 = atil[i][1] * ph[i][1]
        w1 = ph[i][0] ** 2
        w2 = ph[i][1] ** 2
        e = [a1, a2 * w1, -a1 * w2, -a2]
        inc.append(e)
        P.append(sum(e))
    V = 0
    for s in range(4):
        for t in range(s + 1, 4):
            M = sp.Matrix([[P[j], inc[j][s], inc[j][t]] for j in range(3)])
            V += M.det(method="berkowitz")

    form = 0
    for (i, j, l) in ((0, 1, 2), (1, 2, 0), (2, 0, 1)):
        pair = sum(atil[i][m] * atil[j][m] * cosh(ph[l][m]) for m in range(2))
        vec = sum(sin2(ph[i][n], ph[j][n]) * atil[l][n] for n in range(2))
        form += pair * vec

    diff = sp.simplify(sp.together(V + 2 * sp.I * form))
    print(f"(a) V + 2 i form simplifies to: {diff}")

    # (b) same-index sum, one direction
    x, y = sp.symbols("x y", nonzero=True)
    p = [x, y, 1 / (x * y)]
    same = 0
    for (i, j, l) in ((0, 1, 2), (1, 2, 0), (2, 0, 1)):
        same += cosh(p[l]) * sin2(p[i], p[j])
    same = sp.simplify(sp.together(same))
    print(f"(b) same-index sum simplifies to: {same}")
    print(f"S1 {'PASS' if diff == 0 and same == 0 else 'FAIL'}")


if __name__ == "__main__":
    main()
