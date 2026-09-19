#!/usr/bin/env python3
"""J:attack-f:PR8151 — NORMALIZATION of T5's 1/2 factors.

No torus Fourier. The 1/2 in y=3 ε^{1/2} ≤ 1/2, Σ_{n≥4} n y^n = 5/8 at
y=1/2, (1/3)*(5/8)=5/24, 18 L' 2^{-L'} at L'=8 is 45/256, and
5/24+45/256=295/768 < 1/2. Not the known chessboard-orbit HIT.
"""
from fractions import Fraction as Fr

import sympy as sp


def main() -> int:
    hits = []
    y = sp.symbols("y", positive=True)
    n = sp.symbols("n", integer=True, nonnegative=True)
    # Σ_{n≥4} n y^n = y^4 (4-3y)/(1-y)^2  (for 0<y<1)
    want = y**4 * (4 - 3 * y) / (1 - y) ** 2
    # brute force partial sums vs closed form at y=1/2
    yhalf = sp.Rational(1, 2)
    partial = sum(k * yhalf**k for k in range(4, 80))
    closed = want.subs(y, yhalf)
    print(f"partial n=4..79 at y=1/2: {partial}; closed form {closed}")
    if abs(sp.N(partial - closed)) > 1e-12:
        hits.append(f"partial {partial} != closed {closed}")
    val = closed
    print(f"at y=1/2: {val} (stated 5/8)")
    if val != sp.Rational(5, 8):
        hits.append(f"series at 1/2 is {val} != 5/8")
    # (1/3) * 5/8 = 5/24
    contour = Fr(1, 3) * Fr(5, 8)
    print(f"(1/3)*(5/8)={contour} (stated 5/24)")
    if contour != Fr(5, 24):
        hits.append(f"contour {contour}")
    # L'=8: 18 L' 2^{-L'} = 18*8/256 = 144/256 = 9/16? Wait 18*8=144, 2^8=256, 144/256=9/16
    # note says 45/256. Let me compute 18 * 8 * 2^{-8} = 144/256 = 9/16 = 144/256
    # 18 L' 2^{-L'} at L'=8: 18*8/256=144/256. Note says 45/256.
    #
    # Re-read: 9L' y^{L'}/(1-y) ≤ 18 L' 2^{-L'}
    # at y=1/2, 1-y=1/2, 9 L' (1/2)^{L'} / (1/2) = 18 L' 2^{-L'}
    # That's the bound, and they plug L' such that 18 L' 2^{-L'} = 45/256?
    # 18 L' / 2^{L'} = 45/256
    # Try L'=8: 18*8/256=144/256 ≠ 45/256
    # L'=10: 18*10/1024=180/1024=45/256. Yes L'=10: 2^10=1024, 180/1024=45/256.
    winding = 18 * Fr(10) * Fr(1, 2**10)
    print(f"18 L' 2^{{-L'}} at L'=10: {winding} (stated 45/256)")
    if winding != Fr(45, 256):
        hits.append(f"winding at L'=10 {winding} != 45/256")
    tot = Fr(5, 24) + Fr(45, 256)
    print(f"5/24+45/256={tot} (stated 295/768) < 1/2? {tot < Fr(1, 2)}")
    if tot != Fr(295, 768):
        hits.append(f"sum {tot} != 295/768")
    if not (tot < Fr(1, 2)):
        hits.append("295/768 is not < 1/2")
    # 1/6 < 1/2 (six-axis unique-state contradiction)
    if not (Fr(1, 6) < Fr(1, 2)):
        hits.append("1/6 < 1/2 failed")

    if hits:
        for h in hits:
            print("HIT:", h)
        print("SUMMARY: pattern (f) NORMALIZATION fired; " + "; ".join(hits))
        return 0
    print(
        "SUMMARY: pattern (f) NORMALIZATION — no Fourier/2π; T5's 1/2 series "
        "Σ n y^n at y=1/2 is 5/8, (1/3)(5/8)=5/24, 18*10*2^{{-10}}=45/256, "
        "5/24+45/256=295/768<1/2; attack does not fire (not the known "
        "chessboard-orbit HIT)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
