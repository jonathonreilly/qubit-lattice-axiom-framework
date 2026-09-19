#!/usr/bin/env python3
"""J:attack-a:PR8154 — witness realizability of the plane/line tori and H2 shells.

T_L^{(d)}=(Z/2LZ)^d has N=(2L)^d sites and dN bonds. Dual n in {-L+1,...,L}^d.
Plane shells: |n|_∞=j has 8j points (1≤j≤L-1) and 4L-1 at j=L.
Line: exactly 2⌊√L⌋ wavevectors with 1≤|n|≤⌊√L⌋ for L≥2.
4×4 torus is L=2. Z^3 is triangle-free; plane/line are coordinate sublattices.
"""
from __future__ import annotations

import itertools
import math
import sys
from fractions import Fraction as Fr


def hits(msg: str) -> int:
    print(f"HIT: {msg}")
    print(f"SUMMARY: HIT - {msg}")
    return 0


def dual(L: int, d: int):
    rng = range(-L + 1, L + 1)
    return list(itertools.product(rng, repeat=d))


def main() -> int:
    for L, d in [(1, 1), (2, 1), (2, 2), (2, 3), (3, 2), (4, 2), (5, 2), (8, 2)]:
        N = (2 * L) ** d
        n_sites = N
        n_bonds = d * N
        n_dual = len(dual(L, d))
        print(f"T_L^({d}) L={L}: N={n_sites} bonds={n_bonds} |dual|={n_dual}")
        if n_sites != (2 * L) ** d:
            return hits("N != (2L)^d")
        if n_dual != (2 * L) ** d:
            return hits(f"dual grid size {n_dual} != (2L)^d")
        # dual includes 0 and has unique k=(π/L)n
        if (0,) * d not in dual(L, d) and tuple([0] * d) not in [tuple(x) for x in dual(L, d)]:
            return hits("dual missing 0")

    # L=2 plane is 4×4
    if (2 * 2) ** 2 != 16:
        return hits("L=2 plane is not the 4×4 torus")
    print("L=2 plane is the executed 4×4 torus: True")

    for L in range(2, 13):
        rng = range(-L + 1, L + 1)
        buckets = {}
        for n1, n2 in itertools.product(rng, rng):
            if n1 == 0 and n2 == 0:
                continue
            j = max(abs(n1), abs(n2))
            buckets.setdefault(j, []).append((n1, n2))
        for j in range(1, L):
            c = len(buckets.get(j, []))
            if c != 8 * j:
                return hits(f"L={L} shell j={j} has {c} != 8j={8*j}")
            if any(n1 * n1 + n2 * n2 > 2 * j * j for n1, n2 in buckets[j]):
                return hits(f"L={L} shell j={j} has |n|^2 > 2j^2")
        cL = len(buckets.get(L, []))
        if cL != 4 * L - 1:
            return hits(f"L={L} shell j=L has {cL} != 4L-1={4*L-1}")
        # H2(d): N=4L^2, 4/(3N)=1/(3L^2)= (π/L)^2 / (3π^2) as rationals in 1/L^2
        N = 4 * L * L
        if Fr(4, 3 * N) != Fr(1, 3 * L * L):
            return hits("4/(3N) != 1/(3L^2)")
    print("plane shells 8j and 4L-1, |n|^2<=2j^2, 4/(3N)=1/(3L^2) for L=2..12: True")

    for L in range(2, 401):
        m = math.isqrt(L)
        # 1<=|n|<=m both in {-L+1,...,L}
        if m > L - 1:
            return hits(f"m=floor(sqrt(L))={m} > L-1 at L={L}")
        count = sum(1 for n in range(-L + 1, L + 1) if 1 <= abs(n) <= m)
        if count != 2 * m:
            return hits(f"line block count {count} != 2m={2*m} at L={L}")
        if 4 * m * m < L:
            return hits(f"4m^2 < L at L={L} m={m}")
    print("line: 2 floor(sqrt(L)) wavevectors and 4m^2>=L for L=2..400: True")

    # Z^3 bipartite; plane/line as coordinate sublattices of a 4^3 torus
    box = range(4)
    for x, y, z in itertools.product(box, box, box):
        nbrs = []
        for e in ((1, 0, 0), (0, 1, 0), (0, 0, 1)):
            w = ((x + e[0]) % 4, (y + e[1]) % 4, (z + e[2]) % 4)
            nbrs.append(w)
            # parity of coordinate sum
            if (x + y + z) % 2 == (w[0] + w[1] + w[2]) % 2:
                return hits("Z^3 edge joins equal parity (not bipartite)")
    print("Z^3 is bipartite; plane z=0 and line y=z=0 are coordinate sublattices: True")

    # H2(b) dyadic: block 2^{i-1} < j <= 2^i has 2^{i-1} terms
    for m in range(0, 13):
        H = sum(Fr(1, j) for j in range(1, 2**m + 1))
        if not (H >= 1 + Fr(m, 2)):
            return hits(f"H_{2**m} = {H} < 1+m/2")
    print("H_{2^m} >= 1+m/2 for m=0..12: True")

    print(
        "SUMMARY: pattern has no purchase on this note: the plane/line tori, "
        "dual grids, H2 shells 8j and 4L-1, the 4x4 torus, the line wavevector "
        "block, Z^3 bipartiteness, and the dyadic harmonic lower bound all exist "
        "as written"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
