#!/usr/bin/env python3
"""J:attack-b:PR8031 — pattern (b) SAME TEST, BOTH SIDES.

Note: Haar transporter is unitary; finite PW compression U_R is not
(||D_R||=1). Same test: ||I - U* U||. Also the shell min
Q = R^2 - floor(R^2/4) + 3R for p+q=R.
"""
from __future__ import annotations

from math import floor

HITS = []


def Q(p, q):
    return p * p + p * q + q * q + 3 * p + 3 * q


def main():
    # same test: unitarity defect. Haar: 0. R=0 compression U=0: ||I||=1.
    haar_def = 0
    r0_def = 1
    print(f"unitarity defect Haar={haar_def} U_0={r0_def} (stated 0 vs 1)")
    if haar_def == r0_def:
        HITS.append("unitarity defect does not separate Haar from U_0")
    for R in range(1, 9):
        vals = [Q(p, R - p) for p in range(R + 1)]
        got = min(vals)
        want = R * R - floor(R * R / 4) + 3 * R
        print(f"R={R} min Q={got} formula={want} vals={vals}")
        if got != want:
            HITS.append(f"R={R} min {got} != {want}")
    if HITS:
        print("HIT: " + "; ".join(HITS))
        print("SUMMARY: attack pattern (b) SAME TEST BOTH SIDES - " + "; ".join(HITS))
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note - the same unitarity-defect "
        "test is 0 on Haar and 1 on U_0, and the shell min Q=R^2-floor(R^2/4)+3R "
        "holds for R=1..8"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
