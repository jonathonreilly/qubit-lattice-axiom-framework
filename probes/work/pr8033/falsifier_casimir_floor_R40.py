#!/usr/bin/env python3
"""J:falsifier:PR8033 — Section 3 finite check: occupied-link Casimir >= 4.

Beyond the note/runner sizes (R=1..16 executed in attack-b): R=1..40.
HIT if any occupied (p,q) with p+q<=R has Q<4, or the shell min
h_R = R^2-floor(R^2/4)+3R fails.
"""
from math import floor

HITS: list[str] = []


def Q(p, q):
    return p * p + p * q + q * q + 3 * p + 3 * q


def main() -> int:
    if Q(0, 0) != 0:
        HITS.append("Q(0,0)!=0")
    if Q(1, 0) != 4 or Q(0, 1) != 4:
        HITS.append(f"fundamental Q {Q(1,0)} {Q(0,1)} != 4")
    for R in range(1, 41):
        occ = [Q(p, q) for p in range(R + 1) for q in range(R - p + 1) if p + q >= 1]
        mn = min(occ)
        h = R * R - floor(R * R / 4) + 3 * R
        shell = [Q(p, R - p) for p in range(R + 1)]
        shmin = min(shell)
        if mn != 4:
            HITS.append(f"R={R} min occupied Q={mn} != 4")
            break
        if shmin != h:
            HITS.append(f"R={R} shell min {shmin} != h_R={h}")
            break
    print(f"R=1..40: occupied min Q=4, shell min = h_R; Q(0,0)=0 Q(1,0)={Q(1,0)}")
    if HITS:
        for h in HITS:
            print("HIT:", h)
        print("SUMMARY: falsifier FIRED; " + "; ".join(HITS))
        return 0
    print(
        "SUMMARY: falsifier (Sec.3 charged free floor) did not fire — every "
        "occupied SU(3) label with p+q<=R has Casimir >=4 (min 4 at (1,0)/(0,1)) "
        "and shell min = R^2-floor(R^2/4)+3R for R=1..40"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
