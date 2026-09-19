#!/usr/bin/env python3
"""J:attack-g:PR8173 — pattern (g) PROOF STEP BY BRUTE FORCE.

T1 proof: Delta e^{ik.x} = E(k) e^{ik.x} with E(k)=2 sum_j (1-cos k_j), and
sum_{y~x}(e^{ik.x}-e^{ik.y}) = e^{ik.x} sum_j (2-e^{ik_j}-e^{-ik_j}), on every
finite torus. Distinct from the known executed-numbers HIT on c(beta,k) in
0.86-0.98.

HIT if the identity fails at any mode of T_L^3 for L=2,3,4.
"""
from __future__ import annotations

import itertools

import sympy as sp

HITS = []
I = sp.I
pi = sp.pi


def E(k):
    return sum(2 * (1 - sp.cos(kj)) for kj in k)


def check_L(L):
    fails = 0
    nmodes = 0
    x0 = (0, 0, 0)
    for n in itertools.product(range(L), repeat=3):
        if n == (0, 0, 0):
            continue
        k = tuple(2 * pi * nj / L for nj in n)
        nmodes += 1
        phase = lambda x: sp.exp(I * sum(k[j] * x[j] for j in range(3)))
        # Laplacian: sum_{j,pm} (f(x) - f(x +- e_j))
        lap = 0
        for j in range(3):
            for s in (1, -1):
                y = list(x0)
                y[j] = (y[j] + s) % L
                lap += phase(x0) - phase(tuple(y))
        rhs = E(k) * phase(x0)
        def same(a, b):
            d = sp.simplify(sp.expand_complex(a - b).rewrite(sp.cos))
            return d == 0

        if not same(lap, rhs):
            fails += 1
            HITS.append(f"L={L} n={n}: Delta psi != E psi")
        ident = sum(2 - sp.exp(I * k[j]) - sp.exp(-I * k[j]) for j in range(3))
        if not same(ident, E(k)):
            fails += 1
            HITS.append(f"L={L} n={n}: sum_j(2-e^{{ikj}}-e^{{-ikj}}) != E(k)")
    print(f"L={L}: {nmodes} nonzero modes, fails={fails}")
    return fails


def main():
    for L in (2, 3, 4):
        check_L(L)
    if HITS:
        print("HIT: " + "; ".join(HITS[:8]))
        print(
            "SUMMARY: attack pattern (g) PROOF STEP BY BRUTE FORCE on T1 Laplacian "
            "plane-wave identity - " + "; ".join(HITS[:8])
        )
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note - T1 Laplacian identity "
        "Delta e^{ik.x}=E(k)e^{ik.x} with E=2 sum(1-cos k_j) holds on every "
        "nonzero mode of T_L^3 for L=2,3,4 (not a re-find of the c in 0.86-0.98 HIT)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
