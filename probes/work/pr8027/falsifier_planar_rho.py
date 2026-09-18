#!/usr/bin/env python3
"""J:falsifier:PR8027 — independent planar/3d geodesic adjacency checks.

Disjoint from the PR runners (no sympy, no Haar/face-mod-3 census).
Reimplements word-swap adjacency and tests the note's finite identities
beyond the runner sizes (planar up to (5,5)/(8,4); 3d up to (2,2,2)/(3,3,1)).

HIT if path counts, rho_(1,1)=1, rho_(2,1)^2=2, rho_(2,2)^2=5, the cosine
sum formula, unique-geodesic rho=0, or 1/18 Haar coefficient fail.
"""
from __future__ import annotations

import math
from itertools import combinations, permutations
from math import factorial

import numpy as np

TOL = 1e-9


def planar_words(r: int, s: int) -> list[tuple[int, ...]]:
    return list(combinations(range(r + s), s))


def planar_adjacency(r: int, s: int) -> np.ndarray:
    words = planar_words(r, s)
    ix = {w: i for i, w in enumerate(words)}
    n = len(words)
    a = np.zeros((n, n), dtype=np.float64)
    length = r + s
    for i, w in enumerate(words):
        occ = set(w)
        for pos in w:
            for nb in (pos - 1, pos + 1):
                if 0 <= nb < length and nb not in occ:
                    nxt = tuple(sorted(p if p != pos else nb for p in w))
                    a[i, ix[nxt]] += 1.0
    return a


def rho_formula(r: int, s: int) -> float:
    if s == 0 or r == 0:
        return 0.0
    length = r + s
    return 2.0 * sum(math.cos(math.pi * k / (length + 1)) for k in range(1, s + 1))


def max_eig(a: np.ndarray) -> float:
    if a.size == 0 or a.shape[0] == 1:
        return float(a[0, 0]) if a.size else 0.0
    return float(np.max(np.linalg.eigvalsh(a)))


def multinomial(ns: tuple[int, ...]) -> int:
    length = sum(ns)
    out = factorial(length)
    for n in ns:
        out //= factorial(n)
    return out


def words_3d(n1: int, n2: int, n3: int) -> list[tuple[int, ...]]:
    letters = (0,) * n1 + (1,) * n2 + (2,) * n3
    return sorted(set(permutations(letters)))


def adjacency_3d(n1: int, n2: int, n3: int) -> tuple[int, int]:
    words = words_3d(n1, n2, n3)
    ix = {w: i for i, w in enumerate(words)}
    edges = 0
    for w in words:
        seen = set()
        lw = list(w)
        for k in range(len(lw) - 1):
            if lw[k] == lw[k + 1]:
                continue
            lw[k], lw[k + 1] = lw[k + 1], lw[k]
            t = tuple(lw)
            lw[k], lw[k + 1] = lw[k + 1], lw[k]
            j = ix[t]
            if j not in seen:
                seen.add(j)
                if j > ix[w]:
                    edges += 1
    return len(words), edges


def main() -> None:
    hits: list[str] = []
    reports: list[str] = []

    haar = (1 / 3) * (1 / 6)
    print(f"haar 1/3 * 1/6 = {haar}")
    if abs(haar - 1 / 18) > 1e-15:
        hits.append(f"1/18 coefficient {haar} != 1/18")

    named = {((1, 1), 1.0), ((2, 1), math.sqrt(2)), ((2, 2), math.sqrt(5))}
    for (r, s), expected in named:
        a = planar_adjacency(r, s)
        got = max_eig(a)
        print(f"named rho_({r},{s}) = {got} expected {expected}")
        if abs(got - expected) > TOL:
            hits.append(f"rho_({r},{s})={got} != {expected}")
        if abs(got * got - expected * expected) > 1e-8:
            hits.append(f"rho_({r},{s})^2={got*got} != {expected*expected}")

    planar = [(0, 5), (5, 0), (3, 3), (4, 3), (5, 3), (4, 4), (6, 4), (5, 5), (8, 4), (7, 1)]
    for r, s in planar:
        words = planar_words(r, s)
        n = len(words)
        want = multinomial((r, s))
        a = planar_adjacency(r, s)
        got = max_eig(a)
        form = rho_formula(r, s)
        print(f"planar ({r},{s}) paths={n} want={want} rho={got:.12f} formula={form:.12f}")
        if n != want:
            hits.append(f"path count ({r},{s}) {n} != {want}")
        if abs(a - a.T).max() > 0:
            hits.append(f"adjacency ({r},{s}) not symmetric")
        if abs(got - form) > 1e-8:
            hits.append(f"cosine formula ({r},{s}) {got} vs {form}")
        if (r == 0 or s == 0) and abs(got) > TOL:
            hits.append(f"unique geodesic ({r},{s}) rho={got} != 0")
        reports.append(f"({r},{s}):n={n},rho={got:.6f}")

    cubes = [(2, 2, 1), (3, 2, 1), (2, 2, 2), (3, 3, 1), (4, 2, 1)]
    for dims in cubes:
        n, e = adjacency_3d(*dims)
        want = multinomial(dims)
        print(f"3d {dims} geodesics={n} want={want} undirected_flips={e}")
        if n != want:
            hits.append(f"3d path count {dims} {n} != {want}")
        if n > 1 and e <= 0:
            hits.append(f"3d {dims} adjacency has no flips")
        reports.append(f"{dims}:n={n},flips={e}")

    # Riemann-sum asymptotic of the derivative coefficient; formula only, not a HIT.
    r, s = 40, 40
    length = r + s
    form = rho_formula(r, s)
    eta = s / length
    limit = (2 / math.pi) * math.sin(math.pi * eta)
    print(f"riemann ({r},{s}) formula/L={form/length:.8f} (2/pi)sin(pi eta)={limit:.8f}")

    if hits:
        for h in hits:
            print("HIT:", h)
        print("SUMMARY: PR8027 planar/3d geodesic falsifier FIRED: " + "; ".join(hits))
    else:
        print(
            "SUMMARY: PR8027 planar/3d geodesic falsifier did not fire: "
            "named rho 1, sqrt2, sqrt5; cosine formula and multinomial counts "
            f"beyond runner sizes ({', '.join(reports)})"
        )


if __name__ == "__main__":
    main()
