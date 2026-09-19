#!/usr/bin/env python3
"""J:attack-a:PR8079 — witness realizability of the stated configurations.

15 two-link defects = C(6,2) direction-pairs; 90 ordered disjoint pairs;
T 6-regular so ||T||=6; rho4 ellipse confocal with [a,2a];
(3/2)^2-(17/16)^2-(15/16)^2=31/128 and Re z>|Im z|;
67 dyadic panels, Gauss26 degree 51, 1742 nodes, 3484 oracles;
X=6-2Σ cos on T^3 has EX=6, EX^2=42; Z^3 has no triangles.
"""
from __future__ import annotations

import itertools
import sys
from fractions import Fraction as Fr
from math import comb


def hits(msg: str) -> int:
    print(f"HIT: {msg}")
    print(f"SUMMARY: HIT - {msg}")
    return 0


def main() -> int:
    labels = list(itertools.combinations(range(6), 2))
    print(f"two-link defects C(6,2)={len(labels)}")
    if len(labels) != 15:
        return hits(f"{len(labels)} two-link labels != 15")
    ordered = [
        (a, c)
        for a, c in itertools.permutations(labels, 2)
        if set(a).isdisjoint(c)
    ]
    print(f"ordered disjoint pairs {len(ordered)}")
    if len(ordered) != 90:
        return hits(f"{len(ordered)} ordered disjoint pairs != 90")
    deg = [sum(set(a).isdisjoint(c) for c in labels if c != a) for a in labels]
    if deg != [6] * 15:
        return hits(f"T degrees {deg} != 6-regular")
    print("T is 6-regular on 15 vertices (||T||=6 for the 0-1 adjacency): True")

    # Z^3 bipartite: no 3-cycles in a box
    box = range(4)
    verts = list(itertools.product(box, box, box))
    E = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
    adj = {v: [] for v in verts}

    def wrap(v, e):
        return tuple((v[i] + e[i]) % 4 for i in range(3))

    for v in verts:
        for e in E:
            w = wrap(v, e)
            adj[v].append(w)
            adj[w].append(v)
    for v in verts:
        for a, b in itertools.combinations(adj[v], 2):
            if a in adj[b]:
                return hits(f"triangle in Z^3 torus: {v,a,b}")
    print("Z^3 (4^3 torus) has no triangles: True")

    ell = Fr(9, 4) - Fr(17, 16) ** 2 - Fr(15, 16) ** 2
    print(f"ellipse c^2-p^2-q^2 = {ell}")
    if ell != Fr(31, 128):
        return hits(f"ellipse identity {ell} != 31/128")
    # confocal with [a,2a]: p^2-q^2 = (half-length/a)^2 = 1/4
    foc = Fr(17, 16) ** 2 - Fr(15, 16) ** 2
    if foc != Fr(1, 4):
        return hits(f"ellipse not confocal with [a,2a]: p^2-q^2={foc} != 1/4")
    # Re z > |Im z|: min of 3/2 + (17/16)cos - (15/16)|sin| occurs at
    # tan θ = -15/17 in Q2, value 3/2 - sqrt(514)/16; 576 > 514
    if not (24**2 > 514):
        return hits("3/2 <= sqrt(514)/16 so Re z>|Im z| fails")
    print("rho4 ellipse exists, confocal with [a,2a], Re z>|Im z|: True")

    n_panels = (2 - (-64)) + 1
    if n_panels != 67:
        return hits(f"dyadic panels k=-64..2 count {n_panels} != 67")
    if 67 * 26 != 1742 or 1742 * 2 != 3484:
        return hits("1742 nodes / 3484 oracles census failed")
    if 2 * 26 - 1 != 51:
        return hits("Gauss26 exactness degree != 51")
    print("67 panels, Gauss26 deg 51, 1742 nodes, 3484 oracles: True")

    # Haar on T^3: E cos=0, E cos^2=1/2, distinct axes independent
    E_c = Fr(0)
    E_c2 = Fr(1, 2)
    # X=6-2(c1+c2+c3); EX=6; EX^2=36+4*E[(sum c)^2]=36+4*(3/2)=42
    EX = 6 - 2 * 3 * E_c
    EX2 = 36 + 4 * (3 * E_c2)
    print(f"EX={EX} EX^2={EX2}")
    if EX != 6 or EX2 != 42:
        return hits(f"Haar moments EX={EX} EX^2={EX2} != 6,42")
    # j=2√2 h, J*J=8h^2 I
    if Fr(2) ** 2 * 2 != 8:
        return hits("(2√2)^2 != 8")
    print("j=2√2, J*J=8h^2; M1=6 M2=42: True")

    # panel [a,2a] is nonempty for a=2^k, k=-64..2, and covers (2^{-64}, 8]
    starts = [Fr(2) ** k for k in range(-64, 3)]
    if starts[0] != Fr(1, 2**64) or starts[-1] != 4:
        return hits("panel starts are not 2^{-64} .. 4")
    if starts[-1] * 2 != 8:
        return hits("last panel does not end at 8")
    print("dyadic panels [2^k, 2^{k+1}] from 2^{-64} to 8 exist: True")

    print(
        "SUMMARY: pattern has no purchase on this note: the 15 two-link defects "
        "and 90 ordered disjoint pairs exist as C(6,2) with disjointness, T is "
        "6-regular, the rho4 ellipse is a confocal [a,2a] ellipse with Re z>|Im z|, "
        "the Gauss-panel census and Haar moments M1=6 M2=42 are realized, and Z^3 "
        "is triangle-free"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
