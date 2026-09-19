#!/usr/bin/env python3
"""J:attack-f:PR8157 — NORMALIZATION of the 3/2 and 1/2 in P1, and 2π in dσ.

P1: |<s0·sx>| <= (3/2) times each pair bound because
  (C12+C13+C23)=2 <s·s'>, so |dot| <= (1/2)(|C12|+|C13|+|C23|).
Surface measure dσ=dζ dφ with φ∈[0,2π). Bond factor (t^2/2) cosh t.
Recomputed at small size / exact identities.
"""
from fractions import Fraction as Fr

import sympy as sp


def main() -> int:
    hits = []
    # 1/2 pairing: for any a,b,c, |a+b+c| <= (1/2)(|a+b|+|a+c|+|b+c|)
    for trip in (
        (Fr(1), Fr(1), Fr(1)),
        (Fr(1), Fr(-1), Fr(0)),
        (Fr(2), Fr(-1), Fr(-1)),
        (Fr(3), Fr(4), Fr(-5)),
        (Fr(0), Fr(0), Fr(1)),
    ):
        a, b, c = trip
        lhs = abs(a + b + c)
        rhs = Fr(1, 2) * (abs(a + b) + abs(a + c) + abs(b + c))
        print(f"{trip}: |sum|={lhs} <= (1/2) pair-sums={rhs}")
        if lhs > rhs:
            hits.append(f"1/2 pairing fails at {trip}: {lhs} > {rhs}")
        if lhs == 0 and rhs < 0:
            hits.append("negative rhs")
    # equality on (1,1,1): 3 <= (1/2)*6 = 3, so 3/2 per pair if each |Cij|<=1
    if Fr(3, 2) * 1 != Fr(3, 2):
        hits.append("3/2")

    # 2π: ∫_0^{2π} dφ = 2π, so dσ=dζ dφ on ζ∈[-1,1] has total area 2 * 2π = 4π
    phi = sp.symbols("phi", real=True)
    area_phi = sp.integrate(1, (phi, 0, 2 * sp.pi))
    print(f"∫_0^{{2π}} dφ = {area_phi} (stated 2π); sphere area 2*2π={2 * area_phi}=4π")
    if sp.simplify(area_phi - 2 * sp.pi) != 0:
        hits.append(f"phi integral {area_phi} != 2π")
    if sp.simplify(2 * area_phi - 4 * sp.pi) != 0:
        hits.append("sphere area != 4π")

    # (t^2/2) cosh t vs cosh t - 1: coefficient ratio 2/((2k)(2k-1)) <= 1
    t = sp.symbols("t")
    lhs = sp.series(sp.cosh(t) - 1, t, 0, 10).removeO()
    rhs = sp.series((t**2 / 2) * sp.cosh(t), t, 0, 10).removeO()
    print(f"cosh t-1 series {lhs}")
    print(f"(t^2/2)cosh t series {rhs}")
    # each coeff of lhs <= corresponding rhs for even powers
    for k in range(1, 5):
        cl = lhs.coeff(t, 2 * k) or 0
        cr = rhs.coeff(t, 2 * k) or 0
        ratio = sp.simplify(cl / cr) if cr != 0 else None
        print(f"  t^{2*k}: lhs/rhs = {ratio} (stated 2/((2k)(2k-1)) <= 1)")
        want = sp.Rational(2, (2 * k) * (2 * k - 1))
        if ratio != want:
            hits.append(f"t^{2*k} ratio {ratio} != {want}")
        if ratio is not None and ratio > 1:
            hits.append(f"t^{2*k} ratio {ratio} > 1")

    if hits:
        for h in hits:
            print("HIT:", h)
        print("SUMMARY: pattern (f) NORMALIZATION fired; " + "; ".join(hits))
        return 0
    print(
        "SUMMARY: pattern (f) NORMALIZATION — |a+b+c|<=(1/2)(|a+b|+|a+c|+|b+c|) "
        "gives the 3/2 in P1, ∫dφ=2π gives dσ area 4π, and (t^2/2)cosh t "
        "dominates cosh t-1 coefficient-wise; attack does not fire"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
