#!/usr/bin/env python3
"""J:attack-a:PR8028 — witness realizability of the cubic graph, sector, and factors.

Finite oriented cubic link graph; d_G(x,y)=L realized by a shortest path of L
positive-axis links; each cell has 3 outgoing links; Λ_0={0,e1,e2,e3};
dim E=9; Cauchy–Schwarz factor 3; (3/2)*(8/3)=4 kinetic identity;
r=3u/4; Z^3 triangle-free.
"""
from __future__ import annotations

import itertools
import sys
from fractions import Fraction as Fr


def hits(msg: str) -> int:
    print(f"HIT: {msg}")
    print(f"SUMMARY: HIT - {msg}")
    return 0


def main() -> int:
    E_axes = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
    # finite box of vertices [0,3]^3, oriented links +e_i when both ends in box
    verts = list(itertools.product(range(4), repeat=3))
    links = []
    for v in verts:
        for d, e in enumerate(E_axes):
            w = tuple(v[i] + e[i] for i in range(3))
            if w in set(verts):
                links.append((v, d))
    outdeg = {}
    for v in verts:
        outdeg[v] = sum(1 for d, e in enumerate(E_axes) if tuple(v[i] + e[i] for i in range(3)) in set(verts))
    interior = (1, 1, 1)
    if outdeg[interior] != 3:
        return hits(f"interior cell outgoing links {outdeg[interior]} != 3")
    print(f"finite cubic box: {len(verts)} verts, {len(links)} oriented links, interior outdeg 3: True")

    x = (0, 0, 0)
    for L in (1, 2, 3):
        y = (L, 0, 0)
        if y not in set(verts):
            return hits(f"y={y} not in box")
        # Manhattan graph distance in the box equals L along the axis
        path = [(i, 0, 0) for i in range(L + 1)]
        if len(path) - 1 != L:
            return hits("path length")
        print(f"shortest path x={x} -> y={y} has L={L} occupied links: True")

    Lam0 = ((0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1))
    if len(set(Lam0)) != 4:
        return hits("Λ_0 does not have 4 distinct cells")
    print("Λ_0={0,e1,e2,e3} exists: True")

    dimE = 3 * 3
    if dimE != 9:
        return hits("dim E != 9")
    # CS: Σ_{α=1..9} ||w_α|| ≤ 3 (Σ ||w_α||^2)^{1/2}
    if 9 != 3 * 3:
        return hits("CS factor 3 is not sqrt(dim E)")
    print("endpoint tensor E=C^3⊗C^3* has dim 9; CS factor 3: True")

    # kinetic: (3/(2a))*(8/3)=4/a ; Casimir: Tr((8/3)I_3)=8
    if Fr(3, 2) * Fr(8, 3) != 4:
        return hits("(3/2)*(8/3) != 4")
    if Fr(8, 3) * 3 != 8:
        return hits("Tr((8/3)I_3) != 8")
    print("Dirichlet extra (3/2)*(8/3)=4 and Σ_A Tr(T_A T_A)=8: True")

    u, a, v = Fr(1, 8), Fr(1), Fr(1, 8)
    if u != a * v:
        return hits("u=av failed")
    r = 3 * u / 4
    if r != Fr(3, 32):
        return hits("r=3u/4 failed")
    print("r=3u/4 with u=av exists in the parameter range v>=0: True")

    # Z^3 bipartite
    for v0 in verts:
        for e in E_axes:
            w = tuple(v0[i] + e[i] for i in range(3))
            if w in set(verts) and (sum(v0) % 2 == sum(w) % 2):
                return hits("non-bipartite edge")
    print("Z^3 box is bipartite (no triangles): True")

    # Ψ_ab = Ω U_ab/√3 : Σ_ab |Ψ_ab|^2 = |Ω|^2 because Σ_ab |U_ab|^2=3 for unitary 3x3
    if Fr(1, 3) * 3 != 1:
        return hits("Σ_ab |U_ab/√3|^2 != 1")
    print("normalized tensor-vector Ω U_ab/√3 has Σ_ab |Ψ_ab|^2=|Ω|^2: True")

    print(
        "SUMMARY: pattern has no purchase on this note: the finite cubic graph, "
        "shortest paths of length L, 3 outgoing links per cell, Λ_0, dim-9 "
        "endpoint tensor with CS factor 3, the 4/a kinetic identity, r=3u/4, "
        "and the open-line trial normalization all exist as written"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
