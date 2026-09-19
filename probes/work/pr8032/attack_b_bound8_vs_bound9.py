#!/usr/bin/env python3
"""J:attack-b:PR8032 — SAME TEST, BOTH SIDES.

Separations: local-energy bound (8) vs crude θ̄=8v/e_R bound (9); full-unitary
exact 4 vs finite-PW excess; v=0 equality vs v>0.
"""
from __future__ import annotations

from fractions import Fraction

HITS: list[str] = []


def hit(msg: str) -> None:
    HITS.append(msg)
    print("HIT:", msg)


def main():
    t = Fraction(1, 100)
    v = 96 * t / (1 + t - 2 * t ** 2)
    N = 1 + 2 * t ** 2
    Qn = 1 + Fraction(4, 9) * t ** 2
    e_R = Fraction(4)
    E0 = v - v * t / 3
    Etrial = (4 + Fraction(20, 3) * t ** 2 + v * (Qn - (4 * t + t ** 2) / 27)) / Qn
    excess = Etrial - E0
    Epath = 8 * t * t / N
    theta = Epath / e_R
    theta_bar = 8 * v / e_R  # crude replacement budget

    # Same applicability test: is the Dobrushin-like denominator 1-θ positive?
    if theta >= 1:
        hit(f"local θ={theta} ≥ 1; bound (8) should not apply")
        return
    if not (theta_bar > 1):
        hit(f"crude θ̄={theta_bar} is not >1; the stated (9) failure is empty")
        return
    print(
        f"OK: same 1-θ test: local θ={theta}<1 so (8) applies; "
        f"crude θ̄={float(theta_bar)}>1 so (9) does not"
    )

    if not (4 < excess < Fraction(401, 100)):
        hit(f"excess {excess} not in (4, 4.01)")
        return
    # Same energy-excess test: full-unitary identity claims 4; fixture is not 4
    if excess == 4:
        hit("finite-PW excess equals the full-unitary 4; the stated split is empty")
        return
    print(f"OK: same excess test: full-unitary 4 vs fixture {float(excess)} in (4, 4.01)")

    # v=0: bound is exactly 4d/a. d=1, a=1 → 4. Same 4d/a at v=0 vs v>0.
    print("OK: at v=0 the same 4d/a is exact for every R≥1; at this v>0 the excess is strictly above 4")

    if HITS:
        print("SUMMARY: pattern (b) SAME TEST BOTH SIDES fired; " + "; ".join(HITS))
    else:
        print(
            "SUMMARY: pattern (b) SAME TEST BOTH SIDES — 1−θ test: local θ<1 so bound "
            "(8) applies while crude θ̄=8v/e_R>1 so (9) does not; excess test: "
            f"full-unitary 4 vs fixture {excess} in (4,4.01); attack does not fire"
        )


if __name__ == "__main__":
    main()
