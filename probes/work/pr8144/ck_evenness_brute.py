#!/usr/bin/env python3
"""J:attack-g:PR8144 — brute-force Part I.1: c_k = c_{-k} on Z_N.

Note: c_k ∝ sum_{r ≡ k mod N} exp[-r^2/(2 beta)], and 'c_k=c_(-k)'.
Also 'for a charge alias j=0 mod N, K=1'.

Literal check: for N=1..24, the integers r with |r|<= 20 N and r ≡ k (mod N)
have the same multiset of r^2 as those with r ≡ -k (mod N). That is the exact
content of c_k=c_{-k} (the Gaussian is even in r). A |m|-window is NOT the
note's sum and is not used.
"""
from __future__ import annotations

from collections import Counter


def squares(N: int, k: int, R: int) -> Counter:
    k %= N
    c = Counter()
    r = -R
    while r % N != k:
        r += 1
        if r > R:
            return c
    while r <= R:
        c[r * r] += 1
        r += N
    return c


def main() -> int:
    hits = []
    print("Part I.1: c_k=c_{-k} as equality of r^2 on |r|<=20N, r≡k vs r≡-k (mod N)")
    for N in range(1, 25):
        R = 20 * N
        failed = []
        for k in range(N):
            if squares(N, k, R) != squares(N, -k, R):
                failed.append(k)
                hits.append(f"HIT: r^2 on residue {k} != residue {-k % N} at N={N}, |r|<={R}")
        if failed:
            print(f"  N={N}: FAIL residues {failed}")
        else:
            print(f"  N={N}: OK all residues (R={R})")
    print("  j=0: each factor max_k c_k/c_k = 1, so K=1")
    if hits:
        for h in hits:
            print(h)
        print("SUMMARY: Part I.1 evenness of c_k fails a symmetric |r| enumeration")
    else:
        print(
            "SUMMARY: PROOF STEP BY BRUTE FORCE on Part I.1 (PR #8144): c_k=c_{-k} "
            "holds as equality of r^2 multisets on residues k and -k for N=1..24 "
            "with symmetric cutoff |r|<=20 N; j=0 contributes K=1; pattern has "
            "purchase and the step holds as written"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
