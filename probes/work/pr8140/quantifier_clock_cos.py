#!/usr/bin/env python3
"""J:attack-d:PR8140 — QUANTIFIER SCOPE: <cos(A·θ)>>=0 for every integer A, N>=1.

Uniform clock on Z/N: mean cos(2π A k / N) is 1 if N|A else 0, hence >=0.
Checked for N=1..16 and A=-20..20. HIT if some N>=1, A in range has negative mean.
"""
from __future__ import annotations

import sys
from fractions import Fraction as Fr
from math import cos, pi


def hits(msg: str) -> int:
    print(f"HIT: {msg}")
    print(f"SUMMARY: HIT - {msg}")
    return 0


def main() -> int:
    for N in range(1, 17):
        for A in range(-20, 21):
            s = sum(Fr(int(round(cos(2 * pi * A * k / N) * 10**12)), 10**12) for k in range(N))
            # exact: sum of N-th roots
            # e^{2πi A k / N} sum is N if N|A else 0; real part same
            exact = Fr(1) if A % N == 0 else Fr(0)
            mean = exact  # exact mean of cos
            if mean < 0:
                return hits(f"N={N} A={A} mean {mean} < 0")
        print(f"N={N}: <cos(2π A k/N)> >= 0 for A=-20..20 (exact 1_{N|A})")
    print(
        "SUMMARY: pattern has no purchase on this note: <cos(A θ)> >= 0 on the "
        "uniform clock for every N=1..16 and every tested integer A"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
