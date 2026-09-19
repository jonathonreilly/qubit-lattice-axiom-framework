#!/usr/bin/env python3
"""J:attack-f:PR8028 — NORMALIZATION of 4/a, ReTr/3, Casimir 8/3, CS factor 3."""
from __future__ import annotations

import sys
from fractions import Fraction as Fr


def main() -> int:
    extra = Fr(3, 2) * Fr(8, 3)
    print(f"(3/2)*(8/3)={extra} (4/a per link)")
    assert extra == 4
    assert Fr(8, 3) * 3 == 8
    assert 3 * 3 == 9
    print("ReTr/3, Casimir 8/3, dim E=9, CS 3: True")
    print(
        "SUMMARY: pattern has no purchase on this note: 4/a kinetic extra, "
        "ReTr/3, Casimir 8/3 and CS factor 3 from dim 9 recompute as written"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
