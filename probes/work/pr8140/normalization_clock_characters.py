#!/usr/bin/env python3
"""J:attack-f:PR8140 — NORMALIZATION.

Recompute the clock Fourier sum (1/N) Σ_k exp(2π i j k / N) = 1_{N|j}
and the Gaussian 1/2 in φ_β(u)=Σ_k exp[-β(u-2πk)²/2] at small N.
Not the 4-cube r=17 P=24 witness census.
"""
from __future__ import annotations

import math

import sympy as sp

HITS = []


def char_sum_coeffs(N, j):
    """Histogram of jk mod N: geometric sum of Nth roots is N iff all mass is at 0."""
    hist = [0] * N
    for k in range(N):
        hist[(j * k) % N] += 1
    return hist


def main():
    for N in range(1, 9):
        for j in range(-N, 2 * N + 1):
            hist = char_sum_coeffs(N, j)
            if j % N == 0:
                if hist[0] != N or any(hist[i] != 0 for i in range(1, N)):
                    HITS.append(f"N={N} j={j} hist={hist} not N at 0")
            else:
                if hist[0] == N:
                    HITS.append(f"N={N} j={j} trivial character but N doesn't divide j")
                # equally spread on the subgroup gcd(j,N) Z/N
                g = math.gcd(j % N, N)
                for i in range(N):
                    want = g if i % g == 0 else 0
                    if hist[i] != want:
                        HITS.append(f"N={N} j={j} hist[{i}]={hist[i]} != {want}")
                        break
        print(f"N={N}: clock characters (1/N)Σ exp(2πi j k/N)=1_{{N|j}}")

    # φ_β Gaussian 1/2: at u=0, k=0 term is 1; k=±1 terms exp[-β (2π)² / 2]
    beta, u, k = sp.symbols("beta u k", real=True)
    term = sp.exp(-beta * (u - 2 * sp.pi * k) ** 2 / 2)
    t0 = sp.simplify(term.subs({u: 0, k: 0}))
    t1 = sp.simplify(term.subs({u: 0, k: 1}))
    print(f"φ term k=0 u=0: {t0}; k=1: {t1}")
    if t0 != 1:
        HITS.append(f"k=0 term {t0} != 1")
    stated = sp.exp(-beta * 2 * sp.pi ** 2)
    if sp.simplify(t1 - stated) != 0:
        HITS.append(f"1/2 in Gaussian: {t1} vs exp(-2 π² β)={stated}")

    # C_β 2π factor: (2π β)^{-r/2} at r=0 empty is 1; r=2 is 1/(2πβ)
    r = 2
    C = (2 * sp.pi * beta) ** (-sp.Rational(r, 2))
    print(f"C_β r=2 = {sp.simplify(C)}")
    if sp.simplify(C - 1 / (2 * sp.pi * beta)) != 0:
        HITS.append("C_β r=2")

    if HITS:
        print("HIT: " + "; ".join(HITS))
        print("SUMMARY: attack pattern (f) NORMALIZATION - " + "; ".join(HITS))
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note - clock characters "
        "sum to N 1_{N|j} for N=1..8; the Villain 1/2 produces exp(-2π²β) "
        "at the first alias; C_β=(2πβ)^{-r/2} at r=2"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
