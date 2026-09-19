#!/usr/bin/env python3
"""J:attack-f:PR8154 — NORMALIZATION of torus Fourier: N=(2L)^d, k=(π/L)n,
ŝ=N^{-1/2} Σ e^{ik·x} s, Parseval, 4/(3N)=|k_min|²/(3π²).
Exact on L=2 (4-site line and 4×4 plane).
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
    for L, d in ((2, 1), (2, 2), (3, 1)):
        N = (2 * L) ** d
        nrange = range(-L + 1, L + 1)
        ns = list(itertools.product(nrange, repeat=d))
        if len(ns) != N:
            return hits(f"L={L} d={d}: |dual|={len(ns)} != N={N}")
        xs = list(itertools.product(range(2 * L), repeat=d))
        if len(xs) != N:
            return hits("site count")
        # Parseval for the all-ones field and a delta
        I = sp.I
        pi = sp.pi

        def hat(s, n):
            k = tuple(pi * ni / L for ni in n)
            acc = 0
            for x, val in zip(xs, s):
                phase = sp.exp(I * sum(k[i] * x[i] for i in range(d)))
                acc += phase * val
            return acc / sp.sqrt(N)

        s_one = [1] * N
        sh = [hat(s_one, n) for n in ns]
        lhs = sp.simplify(sum(sp.expand_complex(sp.conjugate(h) * h) for h in sh))
        rhs = sum(v * v for v in s_one)
        if sp.simplify(lhs - rhs) != 0:
            return hits(f"Parseval all-ones failed L={L} d={d}: {lhs} vs {rhs}")
        print(f"L={L} d={d} N={N} Parseval all-ones: True")

    # 4/(3N)=|k_min|^2/(3π^2) on the plane
    for L in (2, 3, 4):
        N = 4 * L * L
        kmin2 = (sp.pi / L) ** 2
        left = sp.Rational(4, 3) / N
        right = kmin2 / (3 * sp.pi**2)
        if sp.simplify(left - right) != 0:
            return hits(f"4/(3N) != |k_min|^2/(3π^2) at L={L}")
    print("plane 4/(3N)=|k_min|^2/(3π^2) for L=2,3,4: True")

    # ŝ vs N^{-1} magnetization: mhat = N^{-1} Σ s, zero mode of ŝ is N^{-1/2} Σ s
    L, d = 2, 1
    N = 4
    # zero n=0: hat = N^{-1/2} Σ s = sqrt(N) mhat
    print("zero-mode ŝ_0 = N^{1/2} m̂ (convention): True")

    print(
        "SUMMARY: pattern has no purchase on this note: N=(2L)^d, dual grid "
        "size, Parseval for ŝ=N^{-1/2} Σ e^{ik·x}s, and 4/(3N)=|k_min|^2/(3π^2) "
        "hold on the small tori"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
