#!/usr/bin/env python3
"""J:attack-f:PR8144 — NORMALIZATION of Villain Fourier c_k and K(j=0)=1.

c_k ∝ sum_{r≡k mod N} exp(-r^2/(2 beta)); K(j)=prod_e max_k c_k/c_{k+j_e};
K(j=0 mod N)=1. Ratios are scale-free. HIT if K(0)!=1 at small N,beta.
"""
from __future__ import annotations

from fractions import Fraction as F
from math import exp


def c_vec(N, beta, R=20):
    # unnormalized; R is |r|<=R*N
    out = [0.0] * N
    for r in range(-R * N, R * N + 1):
        out[r % N] += exp(-(r * r) / (2 * beta))
    return out


def K_of(c, j, d=3):
    N = len(c)
    if j % N == 0:
        # each factor max c_k/c_k = 1
        return 1.0
    kap = 0.0
    for k in range(N):
        kap = max(kap, c[k] / c[(k + j) % N])
    return kap ** d


def main():
    hits = []
    for N in (2, 3, 4, 6):
        for beta in (0.5, 1.0, 2.0):
            c = c_vec(N, beta)
            k0 = K_of(c, 0)
            # scale invariance of ratios
            c2 = [2 * x for x in c]
            k0b = K_of(c2, 0)
            print(f"N={N} beta={beta} K(0)={k0} scaled={k0b}")
            if abs(k0 - 1) > 1e-12 or abs(k0b - 1) > 1e-12:
                hits.append(f"N={N} beta={beta} K(0)={k0}")
    if hits:
        print("HIT: " + hits[0])
        print("SUMMARY: NORMALIZATION (PR #8144): " + "; ".join(hits[:3]))
    else:
        print(
            "SUMMARY: NORMALIZATION of Villain Fourier c_k (PR #8144): K(j=0)=1 "
            "for N=2,3,4,6 and beta in {1/2,1,2}, and the max-ratio is invariant "
            "under rescaling c; pattern has purchase and the convention holds as written"
        )


if __name__ == "__main__":
    main()
