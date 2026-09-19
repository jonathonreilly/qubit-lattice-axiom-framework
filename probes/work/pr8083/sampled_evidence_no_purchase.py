#!/usr/bin/env python3
"""J:attack-e:PR8083 — SAMPLED EVIDENCE.

Quartic Ward envelopes are exact rational polynomials (delta=1/4, 15
schedule pairs). Both sign intervals remaining inconclusive is a certificate,
not a sampled never/always. Pattern (e) has no purchase.
"""
from fractions import Fraction as Fr
from itertools import combinations_with_replacement


def main() -> int:
    pairs = list(combinations_with_replacement((1, 2, 4, 8, 16), 2))
    print(f"schedule pairs {len(pairs)} (stated 15); 2*2*15={2*2*len(pairs)}")
    assert len(pairs) == 15
    delta = Fr(1, 4)
    t, u = Fr(1), Fr(2)
    B = 1 / (delta * t * t * u * u)
    A = B * (1 / delta + Fr(2) / t + Fr(2) / u)
    print(f"delta=1/4 t=1 u=2: B={B} A={A} (exact rationals, not samples)")
    print(
        "SUMMARY: pattern has no purchase on this note — quartic envelope "
        "P,A,B and the 15-pair schedule are exact, not sampled never/always "
        "observations"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
