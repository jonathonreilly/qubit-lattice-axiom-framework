#!/usr/bin/env python3
"""Spatial TT rough-Laplacian spectrum and momentum-scale arithmetic.

The historical variable names m_* denote mass-equivalent spectral scales
p/c only; no rest mass or massive spin-2 field is established. The T3 ratio
is conditional on R=ell and Lambda=3/ell^2, not a Higuchi stability test.
"""

from __future__ import annotations

import math
from fractions import Fraction
import sys

PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, condition: bool, detail: str = "") -> bool:
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if condition else "FAIL"
    line = f"  [{status}] {name}"
    if detail:
        line += f"  ({detail})"
    print(line)
    if condition:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    return condition


def banner(title: str) -> None:
    print()
    print("-" * 88)
    print(title)
    print("-" * 88)


# --------------------------------------------------------------------------
# Structural data
# --------------------------------------------------------------------------

def lichnerowicz_eigenvalue(l: int) -> int:
    """Returns l(l+2) - 2, the TT rough-Laplacian eigenvalue numerator in units of 1/R^2."""
    return l * (l + 2) - 2


# Observational comparators (post-derivation only)
# The retained graviton-mass note uses the Hubble radius R = c/H_0 for numerical
# evaluation. The cosmology-scale-identification note earlier flagged R = c/H_inf
# as a candidate alternative; both pins are BOUNDED (not native-axiom). The
# structural tower identity holds for every R > 0; we use R = c/H_0 here to
# match the retained numerical m_g.
HBAR_J_S = 1.054571817e-34    # J*s
C_LIGHT = 2.99792458e8        # m/s
EV_PER_J = 6.241509074e18     # eV/J
H_0_PER_S = 2.184e-18         # s^-1, Planck 2018 H_0 = 67.4 km/s/Mpc
R_HUBBLE_M = C_LIGHT / H_0_PER_S    # m, ≈ 1.373e26 m
M_G_RETAINED_NUMERICAL_EV = 3.52e-33    # eV, retained graviton-mass note (using R = c/H_0)


# --------------------------------------------------------------------------
# Part 0: reproduce spectral mass-equivalent scale from tower at l = 2
# --------------------------------------------------------------------------

def part0_single_mode_consistency() -> None:
    banner("Part 0: tower at l = 2 reproduces spectral mass-equivalent identity (not rest mass)")

    l_val = 2
    numerator_2 = lichnerowicz_eigenvalue(l_val)
    print(f"  lambda_2^TT * R^2 = l(l+2) - 2 = {numerator_2}")

    # m_g^2 = lambda_2^TT * hbar^2 / c^2 = 6 hbar^2 / (c^2 R^2)
    # Equivalently m_g^2 = 2 hbar^2 Lambda / c^2 with Lambda = 3/R^2.
    m_g_squared_coefficient_in_lambda = 2 * Fraction(numerator_2, 6)  # should equal 2
    check(
        "T1 at l=2 gives m_g^2 = 2 hbar^2 Lambda / c^2 (spectral identity only)",
        m_g_squared_coefficient_in_lambda == 2,
        f"coefficient in front of hbar^2 Lambda / c^2 = {m_g_squared_coefficient_in_lambda}",
    )
    # lambda_2^TT * R^2 = 6 exactly (retained numerical coefficient)
    check(
        "T1 at l=2 gives lambda_2^TT * R^2 = 6 exactly",
        numerator_2 == 6,
        f"l=2 numerator = {numerator_2}",
    )


# --------------------------------------------------------------------------
# Part 1: T1 tower eigenvalues for l = 2, ..., 20 are positive integers
# --------------------------------------------------------------------------

def part1_t1_tower_integers() -> None:
    banner("Part 1: T1 tower eigenvalues l(l+2) - 2 for l = 2, ..., 20 are positive integers")

    vals = {}
    for l in range(2, 21):
        lam = lichnerowicz_eigenvalue(l)
        vals[l] = lam
        check(
            f"T1 at l={l}: l(l+2) - 2 = {lam} (positive integer)",
            isinstance(lam, int) and lam > 0,
            f"l(l+2) - 2 = {lam}",
        )

    # Print the first few tower values
    print()
    print("  Tower eigenvalues (l, l(l+2) - 2, m_l / m_2 ratio):")
    m_2_factor = vals[2]
    for l in range(2, 11):
        ratio_sq = Fraction(vals[l], m_2_factor)
        print(f"    l = {l}:  lam * R^2 = {vals[l]:3d},  (m_l/m_2)^2 = {ratio_sq} = {float(ratio_sq):.4f}")


# --------------------------------------------------------------------------
# Part 2: T1 gap differences are consecutive odd numbers
# --------------------------------------------------------------------------

def part2_gap_differences() -> None:
    banner("Part 2: T1 gaps lambda_{l+1}^TT - lambda_l^TT are 2l + 3 (consecutive odd numbers)")

    for l in range(2, 11):
        gap = lichnerowicz_eigenvalue(l + 1) - lichnerowicz_eigenvalue(l)
        expected = 2 * l + 3
        check(
            f"T1 gap at l={l}: lambda_{{l+1}} - lambda_l = {gap}, expected 2l+3 = {expected}",
            gap == expected,
            f"gap = {gap}, expected = {expected}",
        )


# --------------------------------------------------------------------------
# Part 3: T2 pure-rational ratio identities
# --------------------------------------------------------------------------

def part3_t2_rational_ratios() -> None:
    banner("Part 3: T2 squared momentum ratios (m_l/m_k)^2 are rational for all integer pairs")

    # Check a grid of pairs
    test_pairs = [(2, 3), (2, 4), (2, 5), (3, 4), (3, 5), (4, 7), (5, 10), (2, 100), (2, 1000)]
    for (l, k) in test_pairs:
        lam_l = lichnerowicz_eigenvalue(l)
        lam_k = lichnerowicz_eigenvalue(k)
        ratio = Fraction(lam_l, lam_k)
        check(
            f"T2 (m_{l}/m_{k})^2 = {ratio} (rational)",
            isinstance(ratio, Fraction) and ratio > 0,
            f"({lam_l}/{lam_k}) = {ratio}",
        )

    # Spectrum-normalised ratios (m_l/m_2)^2 match published table
    expected = {
        3: Fraction(13, 6),
        4: Fraction(22, 6),  # = 11/3
        5: Fraction(33, 6),  # = 11/2
        6: Fraction(46, 6),  # = 23/3
        7: Fraction(61, 6),
        8: Fraction(78, 6),  # = 13
    }
    for l, expected_ratio in expected.items():
        computed = Fraction(lichnerowicz_eigenvalue(l), 6)
        check(
            f"T2 (m_{l}/m_2)^2 matches expected {expected_ratio}",
            computed == expected_ratio,
            f"computed {computed} vs expected {expected_ratio}",
        )


# --------------------------------------------------------------------------
# Part 4: T3 uniform conditional curvature ratio
# --------------------------------------------------------------------------

def part4_t3_higuchi_margin() -> None:
    banner("Part 4: T3 conditional curvature ratio m_l^2 / (2 Lambda / 3) = [l(l+2) - 2] / 2")

    margins = {}
    for l in range(2, 21):
        lam = lichnerowicz_eigenvalue(l)
        # conditional curvature ratio = m_l^2 / (2 Lambda / 3)
        # m_l^2 = lam * hbar^2 / (c^2 R^2)
        # 2 Lambda / 3 = 2 * 3 / (3 R^2) * hbar^2 / c^2 = 2 * hbar^2 / (c^2 R^2)
        # margin = lam / 2
        margin = Fraction(lam, 2)
        margins[l] = margin
        check(
            f"T3 at l={l}: conditional curvature ratio = {margin} (>= 3)",
            margin >= 3,
            f"margin = {margin}",
        )

    # The lowest margin (at l=2) must be exactly 3 (saturating)
    check(
        "T3 lowest margin at l=2 equals 3 exactly (curvature-ratio factor 3)",
        margins[2] == 3,
        f"margin at l=2 = {margins[2]}",
    )

    # Higher margins are strictly > 3
    for l in range(3, 11):
        check(
            f"T3 margin at l={l} strictly > 3 (conditional spectral ratio only)",
            margins[l] > 3,
            f"margin = {margins[l]}",
        )

    # Growth: margin(l) ~ l^2 / 2 for large l
    l_large = 100
    margin_large = Fraction(lichnerowicz_eigenvalue(l_large), 2)
    leading_prediction = l_large ** 2 / 2
    check(
        "T3 asymptotic margin at large l ~ l^2 / 2",
        abs(float(margin_large) - leading_prediction) / leading_prediction < 0.05,
        f"margin(l=100) = {float(margin_large):.1f} vs leading l^2/2 = {leading_prediction}",
    )


# --------------------------------------------------------------------------
# Part 5: numerical evaluation at observed R_Lambda
# --------------------------------------------------------------------------

def part5_numerical_evaluation() -> None:
    banner("Part 5: spectral energy scales at supplied R=c/H_0 (bounded; cosmology-scale pin)")

    # Spatial momentum p_l=hbar*sqrt(lam)/R, energy scale E_l=c*p_l.
    # This dimensional scale is not a rest mass or a dispersion derivation.
    prefactor_eV = HBAR_J_S * C_LIGHT / R_HUBBLE_M * EV_PER_J

    print(f"  Observation-pinned R = c/H_0 = {R_HUBBLE_M:.3e} m (bounded, matches retained m_g note)")
    print(f"  Spectral energy prefactor hbar*c/R = {prefactor_eV:.4e} eV")
    print()
    print(f"  {'l':>3}  {'lam = l(l+2)-2':>15}  {'E_l (eV)':>14}  {'m_l/m_2':>10}  {'conditional curvature ratio':>15}")

    m_2_eV = prefactor_eV * math.sqrt(lichnerowicz_eigenvalue(2))
    for l in range(2, 11):
        lam = lichnerowicz_eigenvalue(l)
        m_l_eV = prefactor_eV * math.sqrt(lam)
        ratio = math.sqrt(lam / 6)
        margin = Fraction(lam, 2)
        print(f"  {l:>3d}  {lam:>15d}  {m_l_eV:>14.3e}  {ratio:>10.4f}  {str(margin):>15s}")

    # Verify l=2 matches spectral mass-equivalent scale value
    check(
        "numerical m_2 at R = c/H_0 matches historical spectral scale ~ 3.52e-33 eV",
        abs(m_2_eV - M_G_RETAINED_NUMERICAL_EV) / M_G_RETAINED_NUMERICAL_EV < 0.02,
        f"m_2 = {m_2_eV:.3e} eV vs retained m_g = {M_G_RETAINED_NUMERICAL_EV:.3e} eV",
    )

    # Verify tower ratio values
    m_3_eV = prefactor_eV * math.sqrt(lichnerowicz_eigenvalue(3))
    ratio_32 = m_3_eV / m_2_eV
    check(
        "numerical m_3/m_2 = sqrt(13/6)",
        abs(ratio_32 - math.sqrt(13.0 / 6.0)) < 1e-10,
        f"ratio = {ratio_32:.6f} vs sqrt(13/6) = {math.sqrt(13.0/6.0):.6f}",
    )


# --------------------------------------------------------------------------
# Part 6: joint consistency with Lambda identity
# --------------------------------------------------------------------------

def part6_lambda_consistency() -> None:
    banner("Part 6: joint consistency with retained Lambda = 3/R^2 identity")

    # On retained surface: Lambda = 3/R^2, so m_l^2 * R^2 = lam, and m_l^2 / Lambda = lam/3
    for l in range(2, 11):
        lam = lichnerowicz_eigenvalue(l)
        ratio_sq = Fraction(lam, 3)
        check(
            f"m_{l}^2 / Lambda = [l(l+2) - 2] / 3 = {ratio_sq} (hbar^2/c^2 units)",
            isinstance(ratio_sq, Fraction) and ratio_sq > Fraction(2, 3),
            f"m_{l}^2 / Lambda = {ratio_sq} > comparison value 2/3",
        )

    # Specifically: m_2^2 / Lambda = 2 (spectral mass-equivalent identity (not rest mass) coefficient)
    check(
        "m_2^2 / Lambda = 2 exactly (reproduces retained m_g^2 = 2 hbar^2 Lambda / c^2)",
        Fraction(lichnerowicz_eigenvalue(2), 3) == 2,
        f"m_2^2 / Lambda = {Fraction(lichnerowicz_eigenvalue(2), 3)}",
    )


# --------------------------------------------------------------------------
# Part 7: closed-form check of T1-T3
# --------------------------------------------------------------------------

def part7_closed_form_structural() -> None:
    banner("Part 7: closed-form structural checks across l = 2, ..., 20")

    all_t1 = all(lichnerowicz_eigenvalue(l) == l * l + 2 * l - 2 for l in range(2, 21))
    check("T1 closed form l(l+2) - 2 = l^2 + 2l - 2", all_t1, "algebraic identity")

    # T3 asymptotic behavior: margin grows as l^2/2 + l - 1
    all_t3_asymptote = True
    for l in range(2, 21):
        margin = Fraction(lichnerowicz_eigenvalue(l), 2)
        asymptote = Fraction(l * l, 2) + l - 1
        if margin != asymptote:
            all_t3_asymptote = False
    check(
        "T3 asymptotic closed form margin(l) = l^2/2 + l - 1",
        all_t3_asymptote,
        "exact form across tower",
    )

    # T2 reducibility: (m_l/m_2)^2 = [l(l+2) - 2] / 6 gives integer quotients for l congruent to 2 modulo6 (including l=2)
    print()
    print("  Integer-quotient modes (m_l/m_2)^2 = integer:")
    for l in range(2, 25):
        ratio = Fraction(lichnerowicz_eigenvalue(l), 6)
        if ratio.denominator == 1:
            print(f"    l = {l}: (m_{l}/m_2)^2 = {ratio.numerator} (integer)")
    check(
        "T2 at l=8 gives (m_8/m_2)^2 = 78/6 = 13 (integer)",
        Fraction(lichnerowicz_eigenvalue(8), 6) == 13,
        f"at l=8: (m_8/m_2)^2 = {Fraction(lichnerowicz_eigenvalue(8), 6)}",
    )


# --------------------------------------------------------------------------
# Part 8: summary
# --------------------------------------------------------------------------

def part8_summary() -> None:
    banner("Part 8: spatial spectrum and conditional curvature comparison")
    print("T1: lambda_l=[l(l+2)-2]/R^2; p_l=hbar*sqrt(lambda_l).")
    print("T2: squared spatial momentum ratios are rational.")
    print("T3: lambda_l/(2 Lambda/3)>=3 only with R=ell, Lambda=3/ell^2.")
    print("Legacy m_* variables denote p_l/c; no rest mass is established.")
    print("No Higuchi stability, detector reach, or massive-particle claim follows.")
    print("On global de Sitter slices a(t)=ell*cosh(ct/ell), the ratio varies.")


# --------------------------------------------------------------------------
# Main
# --------------------------------------------------------------------------

def main() -> int:
    print("=" * 88)
    print("Graviton TT compactness spectral tower theorem verification")
    print("See docs/GRAVITON_SPECTRAL_TOWER_THEOREM_NOTE_2026-04-24.md")
    print("=" * 88)

    part0_single_mode_consistency()
    part1_t1_tower_integers()
    part2_gap_differences()
    part3_t2_rational_ratios()
    part4_t3_higuchi_margin()
    part5_numerical_evaluation()
    part6_lambda_consistency()
    part7_closed_form_structural()
    part8_summary()

    print()
    print("=" * 88)
    print(f"  TOTAL: PASS={PASS_COUNT}, FAIL={FAIL_COUNT}")
    print("=" * 88)
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
