#!/usr/bin/env python3
"""J:attack-d:PR8026 — QUANTIFIER SCOPE: P<=4A for positive integer side lengths.

Perimeter P=2(l+w), area A=l*w. HIT if some l,w>=1 has P>4A.
Also 4×4 rectangle on 5×5 torus: area 16, complement 9 as stated.
"""
from __future__ import annotations

import sys


def hits(msg: str) -> int:
    print(f"HIT: {msg}")
    print(f"SUMMARY: HIT - {msg}")
    return 0


def main() -> int:
    for l in range(1, 31):
        for w in range(1, 31):
            P = 2 * (l + w)
            A = l * w
            if P > 4 * A:
                return hits(f"P={P} > 4A={4*A} at {l}x{w}")
    print("P<=4A for all 1<=l,w<=30: True")
    if 5 * 5 - 16 != 9:
        return hits("4x4 on 5x5 complement != 9")
    print("4×4 on 5×5 torus: area 16, complement 9: True")
    print(
        "SUMMARY: pattern has no purchase on this note: P<=4A holds on integer "
        "rectangles and the 4×4-in-5×5 complement example is 9 as written"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
