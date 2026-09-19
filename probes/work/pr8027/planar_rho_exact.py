#!/usr/bin/env python3
"""J:attack-g:PR8027 — brute-force the planar geodesic flip-spectrum identities.

Words of r letters 1 and s letters 2; A_geo joins adjacent unequal-letter swaps.
rho_(r,s) = 2 sum_{k=1}^s cos(π k/(L+1)), L=r+s; rho(1,1)=1, rho(2,1)^2=2,
rho(2,2)^2=5; unique geodesic rho=0; r↔s symmetry; path count L!/(n1!n2!n3!).
Exact sympy / Fraction. Independent of the existing falsifier (no numpy graph).
"""
from __future__ import annotations

import itertools
import math
import sys
from fractions import Fraction as Fr

import sympy as sp


def hits(msg: str) -> int:
    print(f"HIT: {msg}")
    print(f"SUMMARY: HIT - {msg}")
    return 0


def words(r: int, s: int) -> list[tuple[int, ...]]:
    # combinations of positions of the s direction-2 steps in L=r+s slots
    L = r + s
    return list(itertools.combinations(range(L), s))


def adjacency(r: int, s: int) -> sp.Matrix:
    ws = words(r, s)
    ix = {w: i for i, w in enumerate(ws)}
    n = len(ws)
    A = sp.zeros(n)
    L = r + s
    for i, w in enumerate(ws):
        occ = set(w)
        for pos in w:
            for nb in (pos - 1, pos + 1):
                if 0 <= nb < L and nb not in occ:
                    nxt = tuple(sorted(p if p != pos else nb for p in w))
                    A[i, ix[nxt]] += 1
    return A


def rho_formula(r: int, s: int):
    L = r + s
    if s == 0 or r == 0:
        return sp.Integer(0)
    return 2 * sum(sp.cos(sp.pi * k / (L + 1)) for k in range(1, s + 1))


def main() -> int:
    # path counts vs multinomial, including 3d
    for n1, n2, n3 in [(1, 0, 0), (1, 1, 0), (2, 1, 0), (2, 2, 0), (3, 1, 0), (2, 1, 1), (1, 1, 1), (3, 2, 1)]:
        L = n1 + n2 + n3
        stated = math.factorial(L) // (math.factorial(n1) * math.factorial(n2) * math.factorial(n3))
        seq = [0] * n1 + [1] * n2 + [2] * n3
        enum = len(set(itertools.permutations(seq)))
        if enum != stated:
            return hits(f"path count ({n1},{n2},{n3}): enum {enum} != L!/n! {stated}")
    print("geodesic counts = L!/(n1!n2!n3!) on enumerated displacements: True")

    stated_ex = {
        (1, 1): (sp.Integer(1), None),
        (2, 1): (sp.sqrt(2), 2),
        (2, 2): (sp.sqrt(5), 5),
    }
    for (r, s), (want, sq) in stated_ex.items():
        A = adjacency(r, s)
        ev = A.eigenvals()
        rho = max(sp.simplify(lam) for lam in ev)
        form = sp.simplify(rho_formula(r, s))
        print(f"rho_({r},{s}): graph={rho} formula={form} stated={want}")
        if sp.simplify(rho - want) != 0 or sp.simplify(form - want) != 0:
            return hits(f"rho_({r},{s}) graph={rho} formula={form} != {want}")
        if sq is not None and sp.simplify(rho**2 - sq) != 0:
            return hits(f"rho_({r},{s})^2 != {sq}")

    # unique geodesic: (L,0) one word, A=0, rho=0
    for L in range(1, 6):
        A = adjacency(L, 0)
        if A.shape != (1, 1) or A[0, 0] != 0:
            return hits(f"unique geodesic L={L} adjacency is not [0]")
        if rho_formula(L, 0) != 0:
            return hits(f"formula rho_({L},0) != 0")
    print("unique geodesic rho=0 for (L,0), L=1..5: True")

    # spectrum of A vs sums of s distinct 2cos(πk/(L+1)) for small r,s
    for r, s in [(1, 1), (2, 1), (3, 1), (2, 2), (3, 2), (4, 1), (3, 3), (4, 2)]:
        A = adjacency(r, s)
        L = r + s
        lams = [2 * sp.cos(sp.pi * k / (L + 1)) for k in range(1, L + 1)]
        x = sp.symbols("x")
        chi_A = A.charpoly(x).all_coeffs()
        chi_f = sp.Integer(1)
        for comb in itertools.combinations(range(L), s):
            chi_f *= x - sum(lams[i] for i in comb)
        chi_f_c = sp.Poly(sp.expand(chi_f), x).all_coeffs()
        if len(chi_A) != len(chi_f_c):
            return hits(f"({r},{s}) charpoly degree mismatch {len(chi_A)} vs {len(chi_f_c)}")
        for deg_from_top, (cA, cF) in enumerate(zip(chi_A, chi_f_c)):
            if abs(sp.N(sp.Integer(cA) - cF, 40)) > sp.N("1e-25"):
                return hits(f"({r},{s}) charpoly coeff mismatch at leading-{deg_from_top}: A={cA} fermi={cF}")
        rho_f = rho_formula(r, s)
        if sp.simplify(rho_f - rho_formula(s, r)) != 0:
            return hits(f"rho({r},{s}) != rho({s},{r})")
        print(f"({r},{s}) fermi charpoly=A_geo and r↔s: True  rho={sp.simplify(rho_f)}")

    # connected by adjacent swaps: sorting (bubble sort on the word)
    for r, s in [(2, 2), (3, 2), (4, 2)]:
        A = adjacency(r, s)
        n = A.shape[0]
        # BFS from 0
        seen = {0}
        q = [0]
        while q:
            i = q.pop()
            for j in range(n):
                if A[i, j] != 0 and j not in seen:
                    seen.add(j)
                    q.append(j)
        if len(seen) != n:
            return hits(f"A_geo not connected at ({r},{s})")
    print("A_geo connected by adjacent swaps: True")

    # Haar coefficient 1/18 algebra: (1/3)*(1/6)=1/18 from Tr/3 and (chi+bar chi)/6
    if Fr(1, 3) * Fr(1, 6) != Fr(1, 18):
        return hits("source-trace 1/3 times (chi+barchi)/6 is not 1/18")
    print("normalized source trace 1/3 * ReTr/3 identity 1/18: True")

    print(
        "SUMMARY: pattern has no purchase on this note: geodesic counts, "
        "rho_(1,1)=1, rho_(2,1)^2=2, rho_(2,2)^2=5, the fermionic cosine-sum "
        "spectrum of A_geo, unique-geodesic rho=0, r↔s, connectivity, and 1/18 "
        "all hold exactly as written"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
