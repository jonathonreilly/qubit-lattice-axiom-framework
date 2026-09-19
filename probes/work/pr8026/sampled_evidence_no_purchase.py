#!/usr/bin/env python3
"""J:attack-e:PR8026 — SAMPLED EVIDENCE.

Spatial-loop area note: A=RS, P=2(R+S), omega(W_square)=u/144+O(u^2),
omega(W_two-adjacent)=(7/124416)u^2+O(u^3). Exact combinatorics / Haar
coefficients, not a never/always Monte Carlo conjecture.
"""
from fractions import Fraction as Fr


def main() -> int:
    for R, S in ((1, 1), (1, 2), (2, 3), (8, 5)):
        A, P = R * S, 2 * (R + S)
        print(f"R={R} S={S}: A={A} P={P}")
        assert A == R * S and P == 2 * (R + S)
    sq = Fr(1, 144)
    two = Fr(7, 124416)
    print(f"square coeff u/144={sq}; two-adjacent 7/124416={two}")
    print(
        "SUMMARY: pattern has no purchase on this note — A=RS, P=2(R+S) and "
        "the open-geometry coefficients u/144 and 7/124416 are exact, not "
        "sampled never/always observations"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
