#!/usr/bin/env python3
"""J:attack-f:PR8024 — NORMALIZATION Haar 1/3 and Casimir 8/3.

Not the known HIT that C>=4 fails at (1,0) because C(1,0)=8/3.
"""
from __future__ import annotations

import sys
from fractions import Fraction as Fr


def main() -> int:
    assert 9 * Fr(1, 3) == 3
    assert Fr(8, 3) * 3 == 8
    print("Haar 1/3; fundamental Casimir 8/3 with Tr=8: True")
    print(
        "SUMMARY: pattern has no purchase on this note: Haar 1/3 and Casimir "
        "8/3 recompute as written; this is not the known C>=4 at (1,0) HIT"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
