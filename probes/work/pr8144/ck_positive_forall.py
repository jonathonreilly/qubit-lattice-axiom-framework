#!/usr/bin/env python3
"""J:attack-d:PR8144 — QUANTIFIER SCOPE: c_k>0 for every k in Z_N, every beta>0, N>=1.

HIT if some (N,beta,k) in range has c_k<=0.
"""
from __future__ import annotations

from math import exp


def c_vec(N, beta, R=30):
    out = [0.0] * N
    for r in range(-R * N, R * N + 1):
        out[r % N] += exp(-(r * r) / (2 * beta))
    return out


def main():
    hits = []
    for N in range(1, 9):
        for beta in (0.05, 0.25, 1.0, 4.0, 16.0):
            c = c_vec(N, beta)
            bad = [k for k, v in enumerate(c) if v <= 0]
            print(f"N={N} beta={beta} min_c={min(c):.3e} bad={bad}")
            if bad:
                hits.append(f"N={N} beta={beta} k={bad} c<=0")
    if hits:
        print("HIT: " + hits[0])
        print("SUMMARY: QUANTIFIER SCOPE (PR #8144): " + "; ".join(hits[:3]))
    else:
        print(
            "SUMMARY: QUANTIFIER SCOPE on c_k>0 (PR #8144): strictly positive for "
            "every k in Z_N, N=1..8, beta in {0.05,0.25,1,4,16}; no in-range failure"
        )


if __name__ == "__main__":
    main()
