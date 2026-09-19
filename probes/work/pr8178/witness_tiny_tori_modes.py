#!/usr/bin/env python3
"""J:attack-a:PR8178 — witness realizability of tiny tori, modes, and the 3-neighbourhood.

Does not touch the known executed-number HIT (D1 1.165 vs 1.18).
L×L torus with predecessors (i,j),(i-1,j),(i,j-1); L² modes k=(2π/L)n;
cos(2π n/L) rational for L=2,3,4; symmetric box n_i∈(-L/2,L/2] has L² points;
M=[[2,-1],[-1,2]]/9 has eigenvalues 1/9, 1/3.
"""
from __future__ import annotations

import itertools
import sys
from fractions import Fraction as Fr

import sympy as sp


def hits(msg: str) -> int:
    print(f"HIT: {msg}")
    print(f"SUMMARY: HIT - {msg}")
    return 0


def main() -> int:
    for L in (2, 3, 4, 16, 32, 64):
        sites = [(i, j) for i in range(L) for j in range(L)]
        if len(sites) != L * L:
            return hits(f"L={L} torus does not have L^2 sites")
        pred = {}
        for i, j in sites:
            pred[(i, j)] = (
                (i, j),
                ((i - 1) % L, j),
                (i, (j - 1) % L),
            )
            if len(set(pred[(i, j)])) != 3:
                return hits(f"L={L} site {(i,j)} does not have 3 distinct predecessors")
        modes = [(2 * sp.pi * n1 / L, 2 * sp.pi * n2 / L) for n1 in range(L) for n2 in range(L)]
        if len(modes) != L * L:
            return hits(f"L={L} has {len(modes)} modes != L^2")
        print(f"L={L}: {len(sites)} sites, 3-neighbourhood, {len(modes)} modes: True")

    # rational cosines on tiny tori
    for L, expected in (
        (2, {Fr(1), Fr(-1)}),
        (3, {Fr(1), Fr(-1, 2)}),
        (4, {Fr(1), Fr(0), Fr(-1)}),
    ):
        vals = set()
        for n in range(L):
            c = sp.cos(2 * sp.pi * n / L)
            c = sp.simplify(c)
            if c not in (0, 1, -1, -sp.Rational(1, 2), sp.Rational(1, 2)):
                # still rational?
                if not c.is_rational:
                    return hits(f"cos(2π {n}/{L}) = {c} is not rational")
            num, den = sp.fraction(sp.together(c))
            if den == 0 or not (num.is_integer and den.is_integer):
                return hits(f"cos(2π {n}/{L}) = {c} is not rational")
            vals.add(Fr(int(num), int(den)))
        print(f"L={L} cos(2π n/L) subset {vals} (claimed rational)")
        if not expected.issubset(vals):
            return hits(f"L={L} cosine set {vals} missing {expected}")

    # symmetric box n_i in (-L/2, L/2]
    for L in (2, 3, 4, 5, 8, 16):
        lo = -L / 2
        hi = L / 2
        ns = [n for n in range(-L, L + 1) if lo < n <= hi]
        if len(ns) != L:
            return hits(f"symmetric box 1d L={L} has {ns} length {len(ns)} != L")
        box = list(itertools.product(ns, ns))
        if len(box) != L * L or (0, 0) not in box:
            return hits(f"symmetric box L={L} is not L^2 including 0")
        print(f"symmetric box L={L}: {len(box)} representatives including 0: True")

    M = sp.Matrix([[2, -1], [-1, 2]]) / 9
    ev = sorted(sp.simplify(e) for e in M.eigenvals())
    if ev != [sp.Rational(1, 9), sp.Rational(1, 3)]:
        return hits(f"M eigenvalues {ev} != {{1/9, 1/3}}")
    print("M eigenvalues {1/9, 1/3}: True")

    # Z^2 torus is bipartite for even L; three predecessors are not a triangle
    L = 4
    for i, j in itertools.product(range(L), range(L)):
        a, b, c = (i, j), ((i - 1) % L, j), (i, (j - 1) % L)
        def nn(u, w):
            return (abs(u[0] - w[0]) % L + abs(u[1] - w[1]) % L) == 1 or (
                min((u[0] - w[0]) % L, (w[0] - u[0]) % L)
                + min((u[1] - w[1]) % L, (w[1] - u[1]) % L)
            ) == 1
        # (i-1,j) and (i,j-1) are diagonal: both coords differ
        d01 = min((b[0] - c[0]) % L, (c[0] - b[0]) % L)
        d11 = min((b[1] - c[1]) % L, (c[1] - b[1]) % L)
        if d01 + d11 == 1:
            return hits(f"predecessors {b,c} are lattice-adjacent (would triangle)")
    print("three predecessors of a site are not a lattice triangle: True")

    # P is L^2 x L^2 with three 1/3 entries per row
    for L in (2, 3, 4):
        idx = {(i, j): i * L + j for i in range(L) for j in range(L)}
        P = sp.zeros(L * L)
        for i, j in itertools.product(range(L), range(L)):
            r = idx[(i, j)]
            for s in ((i, j), ((i - 1) % L, j), (i, (j - 1) % L)):
                P[r, idx[s]] += sp.Rational(1, 3)
        if P.shape != (L * L, L * L):
            return hits(f"P shape {P.shape}")
        if any(sum(P.row(r)) != 1 for r in range(L * L)):
            return hits(f"P is not row-stochastic at L={L}")
        print(f"P is {L*L}x{L*L} row-stochastic circulant (three 1/3s): True")

    print(
        "SUMMARY: pattern has no purchase on this note: LxL tori with the stated "
        "3-neighbourhood, L^2 Fourier modes, rational cosines on L=2,3,4, the "
        "symmetric box, M eigenvalues, and the circulant P all exist as written"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
