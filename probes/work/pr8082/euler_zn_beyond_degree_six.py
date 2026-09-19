#!/usr/bin/env python3
"""J:falsifier:PR8082 — Euler scalar recurrence beyond the note's reused m0..m6.

Note: n Z_n = sum_{j=1}^n j ell_j Z_{n-j}, Z_0=1, with accepted m0..m6
determining lower ell. Machinery disjoint from the receipt-checker runner:
(1) iterate the recurrence in exact Fractions to n=20; (2) independently
Z = exp(sum ell_j t^j) via truncated exponential of the log-series, same
truncation. HIT if the two Z sequences disagree at any n<=20.
"""
from __future__ import annotations

from fractions import Fraction as F
from math import factorial

HITS: list[str] = []


def hit(msg: str) -> None:
    HITS.append(msg)
    print("HIT:", msg)


def rec_Z(ell, N):
    """ell[1..], 1-based list with ell[0] unused."""
    Z = [F(1)]
    for n in range(1, N + 1):
        s = F(0)
        for j in range(1, n + 1):
            if j < len(ell):
                s += j * ell[j] * Z[n - j]
        Z.append(s / n)
    return Z


def exp_series_of_log(ell, N):
    """[t^n] exp(sum_{j=1}^N ell_j t^j) truncated at N."""
    # L coeffs: L[0]=0, L[j]=ell[j]
    L = [F(0)] * (N + 1)
    for j in range(1, min(len(ell), N + 1)):
        L[j] = ell[j]
    # exp via recurrence: n E_n = sum_{k=1}^n k L_k E_{n-k}, E_0=1
    # that's the same recurrence. Use truncated powers of L instead:
    # exp(L) = sum L^k / k!
    E = [F(0)] * (N + 1)
    E[0] = F(1)
    # power of L
    Pk = [F(0)] * (N + 1)
    Pk[0] = F(1)  # L^0
    for k in range(1, N + 1):
        nxt = [F(0)] * (N + 1)
        for i, a in enumerate(Pk):
            if a == 0:
                continue
            for j in range(1, N + 1 - i):
                nxt[i + j] += a * L[j]
        Pk = nxt
        fac = F(1, factorial(k))
        for i in range(N + 1):
            E[i] += fac * Pk[i]
    return E


def main() -> int:
    N = 20
    # generic ell: 1/j! style, beyond the note's reused degree 6
    ell = [F(0)] + [F(1, factorial(j)) for j in range(1, N + 1)]
    Zrec = rec_Z(ell, N)
    Zexp = exp_series_of_log(ell, N)
    for n in range(N + 1):
        eq = Zrec[n] == Zexp[n]
        if n in (0, 1, 6, 7, 10, 15, 20) or not eq:
            print(f"n={n} rec={Zrec[n]} exp={Zexp[n]} eq={eq}")
        if not eq:
            hit(f"n={n} rec {Zrec[n]} != exp {Zexp[n]}")
            break
    else:
        print(f"OK: Euler Z vs exp(sum ell t^j) through n={N}")

    # second ell: ell_j = 1/2^j
    ell2 = [F(0)] + [F(1, 2**j) for j in range(1, N + 1)]
    Z2 = rec_Z(ell2, N)
    E2 = exp_series_of_log(ell2, N)
    bad = [n for n in range(N + 1) if Z2[n] != E2[n]]
    print(f"ell=2^{{-j}}: mismatches {bad[:8]} count={len(bad)}")
    if bad:
        hit(f"geometric ell mismatches at {bad[:6]}")

    if HITS:
        print("SUMMARY: Euler Z_n falsifier FIRED - " + "; ".join(HITS))
        return 0
    print(
        "SUMMARY: Euler recurrence n Z_n = sum_j j ell_j Z_{n-j} matches "
        f"exp(sum ell t^j) through n={N} (beyond reused m0..m6) for two ell "
        "sequences; falsifier does not fire"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
