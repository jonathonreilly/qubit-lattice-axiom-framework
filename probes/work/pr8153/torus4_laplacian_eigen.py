#!/usr/bin/env python3
"""J:attack-a:PR8153 — 4^3 torus Laplacian eigenfunction witnesses.

Note: T_L=(Z/2L Z)^3 even side; executed on a 4^3 torus (L=2, N=64, 3N bonds).
E(k)=sum_i 2(1-cos k_i). The plane wave x |-> exp(ik·x) is a Laplacian
eigenfunction. Z^3/torus of even side is bipartite (no triangles).

HIT if the 4^3 torus is not bipartite, bond count is not 192, or a mode
fails (Delta psi)_x = E(k) psi_x.
Exact Fraction via 1-cos using cyclotomic/algebraic numbers (sympy).
"""
from __future__ import annotations

from itertools import product

import sympy as sp


def main():
    hits = []
    Lside = 4
    N = Lside ** 3
    sites = list(product(range(Lside), repeat=3))
    if N != 64:
        hits.append(f"HIT: 4^3 has N={N} != 64")
        print(hits[-1])
    bonds = 0
    for x in sites:
        for i in range(3):
            y = list(x)
            y[i] = (x[i] + 1) % Lside
            bonds += 1
    print(f"4^3 torus: N={N} oriented-outgoing bonds={bonds} (want 3N=192)")
    if bonds != 3 * N:
        hits.append(f"HIT: bond count {bonds} != 192")
        print(hits[-1])

    # bipartite: even side
    color = {x: sum(x) % 2 for x in sites}
    bad = 0
    for x in sites:
        for i in range(3):
            y = list(x)
            y[i] = (x[i] + 1) % Lside
            y = tuple(y)
            if color[x] == color[y]:
                bad += 1
    print(f"same-color nn pairs: {bad}")
    if bad:
        hits.append("HIT: 4^3 torus nn-graph is not bipartite")
        print(hits[-1])

    I = sp.I
    pi = sp.pi
    n_fail = 0
    n_ok = 0
    for n in product(range(Lside), repeat=3):
        k = tuple(2 * pi * ni / Lside for ni in n)
        E = sum(2 * (1 - sp.cos(ki)) for ki in k)
        E = sp.simplify(E)
        fail = False
        for x in sites:
            psi = sp.exp(I * sum(ki * xi for ki, xi in zip(k, x)))
            lap = 0
            for i in range(3):
                xp = list(x)
                xm = list(x)
                xp[i] = (x[i] + 1) % Lside
                xm[i] = (x[i] - 1) % Lside
                lap += 2 * psi - sp.exp(I * sum(ki * yi for ki, yi in zip(k, xp))) - sp.exp(
                    I * sum(ki * yi for ki, yi in zip(k, xm))
                )
            if sp.simplify(lap - E * psi) != 0:
                fail = True
                break
        if fail:
            n_fail += 1
            if n_fail <= 3:
                hits.append(f"HIT: Laplacian eigenfunction fails at k-index {n} E={E}")
                print(hits[-1])
        else:
            n_ok += 1
    print(f"modes Laplacian-ok {n_ok}/{N} fail={n_fail}")

    if hits:
        print("SUMMARY: 4^3 torus Laplacian/bipartite witnesses fail")
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note — the 4^3 torus has N=64, "
        "192 bonds, is bipartite, and every discrete plane wave is a Laplacian "
        "eigenfunction with E(k)=sum_i 2(1-cos k_i)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
