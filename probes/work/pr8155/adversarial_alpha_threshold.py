#!/usr/bin/env python3
"""J:attack-e:PR8155 — SAMPLED EVIDENCE: uniqueness threshold is algebraic, not sampled.

Not the known W5 L=1 torus degree-3 HIT.
α=2√3 β and α<1 iff β<√3/6. No 'never observed' sampling claim to hill-climb.
Adversarial check of the threshold identity and α at β=√3/6, just below, just above.
"""
from __future__ import annotations

import sys
from fractions import Fraction as Fr

import sympy as sp


def hits(msg: str) -> int:
    print(f"HIT: {msg}")
    print(f"SUMMARY: HIT - {msg}")
    return 0


def main() -> int:
    beta = sp.symbols("beta", positive=True)
    alpha = 2 * sp.sqrt(3) * beta
    thresh = sp.sqrt(3) / 6
    if sp.simplify(alpha.subs(beta, thresh) - 1) != 0:
        return hits("α(√3/6) != 1")
    print("α=2√3 β equals 1 exactly at β=√3/6: True")
    # adversarial points
    for b, want_lt in ((thresh / 2, True), (thresh, False), (thresh * Fr(2), False)):
        a = sp.simplify(alpha.subs(beta, b))
        lt = sp.simplify(a - 1) < 0
        # evaluate
        aval = sp.N(a)
        print(f"β={b} α≈{aval} α<1? {aval < 1} want_strict_below_1={want_lt}")
        if want_lt and aval >= 1:
            return hits(f"α>=1 at β={b} below the threshold")
        if b == thresh and abs(aval - 1) > 1e-12:
            return hits("α not 1 at the stated threshold")
    print(
        "SUMMARY: pattern has no purchase on this note: there is no sampled "
        "never/always claim to hill-climb; α=2√3β<1 iff β<√3/6 holds exactly, "
        "and this is not the known W5 L=1 torus HIT"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
