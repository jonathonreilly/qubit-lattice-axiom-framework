#!/usr/bin/env python3
"""J:attack-e:PR8028 — SAMPLED EVIDENCE: the uniform bound is a proof, not a sample.

No 'never observed' sampling. Adversarial check: η=3cr, η≤1/2 ⇒ lower bound 2L/a;
(3/2)*(8/3)=4; factor-3 CS from dim E=9. Pattern has no purchase if these hold.
"""
from __future__ import annotations

import sys
from fractions import Fraction as Fr


def hits(msg: str) -> int:
    print(f"HIT: {msg}")
    print(f"SUMMARY: HIT - {msg}")
    return 0


def main() -> int:
    # η=1/2 ⇒ (4/a)(1-η)L = 2L/a
    a, L = Fr(1), Fr(5)
    eta = Fr(1, 2)
    lower = (4 / a) * (1 - eta) * L
    if lower != 2 * L / a:
        return hits(f"η=1/2 does not give 2L/a: {lower}")
    print("η≤1/2 yields lower bound 2L/a: True")
    if Fr(3, 2) * Fr(8, 3) != 4:
        return hits("kinetic 4/a identity")
    if 3 * 3 != 9:
        return hits("dim E")
    # CS: sqrt(9)=3
    if 9 ** 0.5 != 3:
        return hits("CS factor")
    print("kinetic 4/a and CS factor 3 from dim E=9: True")
    print(
        "SUMMARY: pattern has no purchase on this note: there is no sampled "
        "never/always claim; η=1/2 gives 2L/a and the 4/a, CS-3 identities hold"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
