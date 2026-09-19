#!/usr/bin/env python3
"""J:attack-f:PR8153 — NORMALIZATION of torus Green G_L = N^{-1} Σ_{k≠0} 1/E(k).

N=L^3, k=2π n/L, E=Σ_i 2(1-cos k_i). Not 1/L or (2π)^{-3} at finite L.
Recomputed exactly on L=2 (N=8) and L=3 (N=27).
"""
from fractions import Fraction as Fr
from itertools import product

import sympy as sp

I = sp.I
pi = sp.pi


def E_of(n, L):
    return sum(2 * (1 - sp.cos(2 * pi * ni / L)) for ni in n)


def main() -> int:
    hits = []
    for L in (2, 3):
        N = L**3
        modes = list(product(range(L), repeat=3))
        s = 0
        n_nz = 0
        e0 = sp.simplify(E_of((0, 0, 0), L))
        if e0 != 0:
            hits.append(f"L={L} E(0)={e0} != 0")
        for n in modes:
            if n == (0, 0, 0):
                continue
            e = sp.simplify(E_of(n, L))
            if e == 0:
                hits.append(f"L={L} E=0 at {n}")
                continue
            s += 1 / e
            n_nz += 1
        g = sp.simplify(s / N)
        g_wrong_L = sp.simplify(s / L)
        print(f"L={L} N={N} nonzero modes={n_nz}  G_L=N^{{-1}}Σ 1/E = {g}")
        print(f"  wrong 1/L convention would give {g_wrong_L}")
        if n_nz != N - 1:
            hits.append(f"L={L} nonzero count {n_nz}")
        # L=2: k_i in {0,π}, E = 2*# of π-components * (1-(-1))= 4 * (number of π axes)
        if L == 2:
            # 7 modes: three axis (E=4), three face (E=8), one body (E=12)
            want = (3 * Fr(1, 4) + 3 * Fr(1, 8) + Fr(1, 12)) / 8
            want = Fr(3, 4) / 8 + Fr(3, 8) / 8 + Fr(1, 12) / 8
            # 3/4 + 3/8 + 1/12 = 9/12+3/8 wait no: the SUM of 1/E is 3*(1/4)+3*(1/8)+1/12
            se = 3 * Fr(1, 4) + 3 * Fr(1, 8) + Fr(1, 12)
            want_g = se / 8
            print(f"  L=2 expected Σ1/E={se} G={want_g}")
            if sp.simplify(s - se) != 0:
                hits.append(f"L=2 Σ1/E={s} != {se}")
            if sp.simplify(g - want_g) != 0:
                hits.append(f"L=2 G={g} != {want_g}")

    # 1-cos u >= 2 (u/π)^2 on [0,π]: at u=π, 1-(-1)=2 and 2*1=2, equality
    if 1 - sp.cos(pi) != 2:
        hits.append("1-cos π != 2")
    if sp.simplify(2 * (pi / pi) ** 2 - 2) != 0:
        hits.append("2(u/π)^2 at π != 2")
    print("at u=π: 1-cos=2 equals 2(u/π)^2=2 (chord bound saturates)")

    if hits:
        for h in hits:
            print("HIT:", h)
        print("SUMMARY: pattern (f) NORMALIZATION fired; " + "; ".join(hits))
        return 0
    print(
        "SUMMARY: pattern (f) NORMALIZATION — G_L=N^{{-1}}Σ_{k≠0} 1/E(k) with "
        "N=L^3 and k=2π n/L recomputes exactly on L=2 (Σ1/E=29/24, G=29/192) "
        "and L=3 (G=44/243); the 1/L convention disagrees; attack does not fire"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
