#!/usr/bin/env python3
"""J:attack-f:PR8158 — NORMALIZATION of φ-spectrum and TV 1/2, not the Q4 triangle HIT.

φ = Z1 P0 + (p-q) Podd + (p+q-2r) Peven on the six-axis menu;
Z1=p+q+4r; TV=(1/2)Σ|μ-ν|. Recomputed on the 6-point menu by brute force.
"""
from __future__ import annotations

import sys
from fractions import Fraction as Fr

import sympy as sp


def hits(msg: str) -> int:
    print(f"HIT: {msg}")
    print(f"SUMMARY: HIT - {msg}")
    return 0


AXES = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]


def main() -> int:
    p, q, r = sp.symbols("p q r", positive=True)
    Z1 = p + q + 4 * r

    def phi_val(i, j):
        d = sum(AXES[i][k] * AXES[j][k] for k in range(3))
        return p if d == 1 else (q if d == -1 else r)

    Phi = sp.Matrix(6, 6, lambda i, j: phi_val(i, j))
    # action on constants
    ones = sp.Matrix([1] * 6)
    if sp.simplify(Phi * ones - Z1 * ones) != sp.zeros(6, 1):
        return hits("φ 1 != Z1 1 with Z1=p+q+4r")
    print("Z1=p+q+4r is the constant eigenvalue: True")

    # odd: f(-v)=-f(v). Basis: e1-e(-1), e2-e(-2), e3-e(-3)
    odds = []
    for ax in range(3):
        f = sp.zeros(6, 1)
        f[2 * ax] = 1
        f[2 * ax + 1] = -1
        odds.append(f)
        lam = (p - q)
        if sp.simplify(Phi * f - lam * f) != sp.zeros(6, 1):
            return hits(f"odd axis {ax} is not eigenvalue p-q")
    print("P_odd (dim 3): eigenvalue p-q: True")

    # even zero-sum: f(-v)=f(v), sum=0. Dim 2.
    # e.g. (1,1,-1,-1,0,0) and (1,1,0,0,-1,-1)
    evens = []
    for pair in ((0, 1), (0, 2)):
        f = sp.zeros(6, 1)
        f[0] = 1
        f[1] = 1
        f[2 * pair[1]] = -1
        f[2 * pair[1] + 1] = -1
        evens.append(f)
        lam = p + q - 2 * r
        if sp.simplify(Phi * f - lam * f) != sp.zeros(6, 1):
            return hits("even vector is not eigenvalue p+q-2r")
    print("P_even (dim 2): eigenvalue p+q-2r: True")
    if 1 + 3 + 2 != 6:
        return hits("sector dimensions 1+3+2 != 6")

    # TV 1/2: two equal laws; a point mass vs another
    def tv(mu, nu):
        return Fr(1, 2) * sum(abs(mu[i] - nu[i]) for i in range(6))

    u = [Fr(1, 6)] * 6
    if tv(u, u) != 0:
        return hits("TV(μ,μ) != 0")
    e0 = [Fr(1), 0, 0, 0, 0, 0]
    e1 = [0, Fr(1), 0, 0, 0, 0]
    if tv(e0, e1) != 1:
        return hits(f"TV of distinct point masses = {tv(e0,e1)} != 1 (1/2 convention)")
    print("TV=(1/2)Σ|μ-ν|: TV=0 on equals, TV=1 on distinct point masses: True")

    print(
        "SUMMARY: pattern has no purchase on this note: Z1=p+q+4r, φ-spectrum "
        "(1, p-q, p+q-2r) with dims 1+3+2, and TV 1/2 all recompute on the six-axis "
        "menu; not the known Q4 triangle HIT"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
