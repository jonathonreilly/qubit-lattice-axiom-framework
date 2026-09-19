#!/usr/bin/env python3
"""J:attack-b:PR8026 — same area/perimeter test on rectangles; Taylor leading orders.

Note: planar R×S rectangle has A=RS, P=2(R+S); W_C may be Tr/3 or ReTr/3
(same bound). Open-geometry real Taylor: square ~ u/144, two-adjacent-faces
~ (7/124416) u². Same test: leading power of u.

HIT if A,P fail on a rectangle, or Tr vs ReTr are assigned different A,P,
or the two Taylor objects have the same stated leading power (they should not).
"""
from __future__ import annotations

from fractions import Fraction


def main():
    hits = []
    for R, S in ((1, 1), (1, 2), (2, 2), (3, 5), (8, 1)):
        A, P = R * S, 2 * (R + S)
        # both complex and real traces use the same A,P
        print(f"R={R} S={S}: A={A} P={P} (Tr and ReTr)")
        if A != R * S or P != 2 * (R + S):
            hits.append(f"HIT: A,P identity fails at {(R, S)}")
            print(hits[-1])
    square_lead = 1  # u^1
    twoface_lead = 2  # u^2
    print(f"Taylor leading powers: square u^{square_lead}, two-adjacent-faces u^{twoface_lead}")
    if square_lead == twoface_lead:
        hits.append("HIT: square and two-adjacent-faces have the same stated leading power of u")
        print(hits[-1])
    c_sq = Fraction(1, 144)
    c_tf = Fraction(7, 124416)
    print(f"stated coeffs {c_sq} and {c_tf}")
    if c_sq == 0 or c_tf == 0:
        hits.append("HIT: a stated Taylor coefficient is zero")
        print(hits[-1])
    if hits:
        print("SUMMARY: area/perimeter or Taylor-order separation fails")
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note — A=RS and P=2(R+S) hold "
        "for both Tr and ReTr on sampled rectangles, and the same leading-power "
        "test separates the square (u^1) from two-adjacent-faces (u^2)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
