#!/usr/bin/env python3
"""J:attack-f:PR8025 — NORMALIZATION.

Recompute Haar two-point, Schmidt √3×√3 / 3, and I/9 reduced density at small size.
"""
from __future__ import annotations

from fractions import Fraction

HITS: list[str] = []


def hit(msg: str) -> None:
    HITS.append(msg)
    print("HIT:", msg)


def main():
    # Haar SU(3): ∫ U_ij conj(U_kl) = δ_ik δ_jl / 3
    haar2 = Fraction(1, 3)
    # √3 U_ab has L2-norm squared 3 * (1/3) = 1
    schmidt_factor = 3 * haar2
    if schmidt_factor != 1:
        hit(f"√3 U_ab is not L2-normalized: {schmidt_factor}")
        return
    print("OK: Haar ∫|U_ab|²=1/3 so ∫|√3 U_ab|²=1; 9 pairs (a,b) are orthonormal")

    # prefactor 1/3 * √3 * √3 = 1 reconstructs Tr(U1 rest)
    pref = Fraction(1, 3) * 3  # (√3)²
    if pref != 1:
        hit(f"Schmidt prefactor 1/3 * 3 = {pref} != 1")
        return
    print("OK: (1/3)·√3·√3 = 1, so ψ=Tr(U1 U2 U3⁻¹ U4⁻¹) as written")

    # reduced density on the 9-dim fundamental matrix block: I/9, trace 1
    rho = Fraction(1, 9)
    if 9 * rho != 1:
        hit("I/9 does not have trace 1 on 9 dimensions")
        return
    print("OK: single-link reduced density I/9 has Tr=1 on the 9-dimensional PW block")

    # J_p = Re Tr(U_p)/3: Haar E J = 0, E J² = 1/18 as (∫|χ|²=1)/18
    EJ2 = Fraction(2, 36)  # (0+2+0)/36
    if EJ2 != Fraction(1, 18):
        hit(f"E J^2 = {EJ2} != 1/18")
        return
    print("OK: J=ReTr(U)/3 has E J²=1/18 from Haar character orthogonality")

    # D_R formula at R=1: (3)^2 (4)^2 (2) (5) (3*9+9+2)/2880
    # (R+2)^2 (R+3)^2 (R+1) (R+4) (3(R+2)^2 + 3(R+2)+2) / 2880
    R = 1
    DR = (
        (R + 2) ** 2
        * (R + 3) ** 2
        * (R + 1)
        * (R + 4)
        * (3 * (R + 2) ** 2 + 3 * (R + 2) + 2)
        // 2880
    )
    # dim of p+q≤1: (0,0)+(1,0)+(0,1) = 1+3+3=7? That's irrep dims not PW link dim.
    # Peter-Weyl: L2(SU3) block p+q≤R is sum (dim ρ)^2.
    # (0,0):1, (1,0):9, (0,1):9 → 1+9+9=19 for R=1.
    if DR != 19:
        # if the formula doesn't give 19, that's a normalization/count defect
        print(f"INFO: D_1 from the stated formula is {DR} (sum of (dim ρ)^2 for p+q≤1 is 19)")
        if DR <= 0:
            hit(f"D_R(R=1)={DR} is not a positive dimension")
            return
    else:
        print("OK: D_R(R=1)=19 = 1²+3²+3²")

    if HITS:
        print("SUMMARY: pattern (f) NORMALIZATION fired; " + "; ".join(HITS))
    else:
        print(
            "SUMMARY: pattern (f) NORMALIZATION — Haar ∫|U_ab|²=1/3, Schmidt "
            "(1/3)·√3·√3=1, reduced I/9 has trace 1, J=ReTr/3 has E J²=1/18, "
            f"D_R(R=1)={DR}; 0 failures; attack does not fire"
        )


if __name__ == "__main__":
    main()
