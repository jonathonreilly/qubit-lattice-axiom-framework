#!/usr/bin/env python3
"""J:attack-f:PR8142 — NORMALIZATION of Z1=p+q+4r and |M|^3=216.

Six-axis menu: one-site partition Z1=p+q+4r; 6^3=216 predecessor triples.
"""
from __future__ import annotations

import sys
from fractions import Fraction as Fr


def hits(msg: str) -> int:
    print(f"HIT: {msg}")
    print(f"SUMMARY: HIT - {msg}")
    return 0


def main() -> int:
    p, q, r = Fr(3), Fr(1), Fr(2)
    Z1 = p + q + 4 * r
    if Z1 != 12:
        return hits(f"Z1(3,1,2)={Z1} != 12")
    if 6 ** 3 != 216:
        return hits("6^3 != 216")
    # K2 ratio uses 2(pq+2r^2) and 2r(p+q+r)
    den1 = 2 * (p * q + 2 * r * r)
    den2 = 2 * r * (p + q + r)
    print(f"Z1={Z1} |M|^3=216 den1={den1} den2={den2}")
    if den1 != 22 or den2 != 24:
        return hits("K2 denominators")
    print(
        "SUMMARY: pattern has no purchase on this note: Z1=p+q+4r, 216 triples, "
        "and the K2 factor-2 denominators recompute as written"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
