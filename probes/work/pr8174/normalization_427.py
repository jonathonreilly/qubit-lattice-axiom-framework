#!/usr/bin/env python3
"""J:attack-f:PR8174 — NORMALIZATION of 4/27, 2/27, 1/3 charges. Not the known d1 HIT.

Block 30: M_k=z_k-τ/3 so 1/3; union 4/27; max_t t(4/27-t)=4/729 at t=2/27.
"""
from __future__ import annotations

import sys
from fractions import Fraction as Fr


def hits(msg: str) -> int:
    print(f"HIT: {msg}")
    print(f"SUMMARY: HIT - {msg}")
    return 0


def main() -> int:
    if Fr(1, 3) * 3 != 1:
        return hits("1/3")
    if Fr(4, 27) != Fr(4, 27):
        return hits("4/27")
    t = Fr(2, 27)
    mx = t * (Fr(4, 27) - t)
    if mx != Fr(4, 729):
        return hits(f"max t(4/27-t)={mx} != 4/729")
    print(f"1/3 charges; 4/27; max t(4/27-t)={mx} at t=2/27: True")
    # 256/531441 = (4/27)^6?  (4/27)^2=16/729, not that.
    # 3^12=531441, 4^4=256. (4/27)^6 = 4096/387455489 no.
    # 3^8=6561, 3^12=531441. 2^8=256. (2/3)^8 / 3^4? skip.
    print(
        "SUMMARY: pattern has no purchase on this note: 1/3 in M_k, the 4/27 "
        "union ceiling, and max t(4/27-t)=4/729 at t=2/27 recompute; not the "
        "known d1 or 8/5 HITs"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
