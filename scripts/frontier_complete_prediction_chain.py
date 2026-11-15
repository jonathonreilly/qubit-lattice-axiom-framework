#!/usr/bin/env python3
"""
Canonical synthesis runner for COMPLETE_PREDICTION_CHAIN_2026_04_15.md.

This script is intentionally package-level rather than route-level. It
collects the current support-inventory quantitative rows and prints the
reviewer-facing prediction card on `main`. Audit status and retained-grade
reuse are pipeline-derived, not granted by this runner.

Subcomponent provenance:
  - plaquette/u0/alpha_LM/alpha_s(v)/v: hierarchy + zero-import chain
  - alpha_LM^2 = alpha_bare alpha_s(v): coupling-chain identity
  - R_conn, g_1(v), g_2(v), sin^2(theta_W), 1/alpha_EM: color projection stack
  - y_t(v), m_t(pole): Ward + color-singlet projection stack
  - m_H (2-loop): corrected-y_t stability boundary
  - m_H historical 125.10: supplied inventory literal, not a fresh 3-loop calculation
  - vacuum stability: historical sampled truncated-flow diagnostic only

Named premises: the four framework axioms (Lattice, Qubit, Admissibility,
Record) and the approved units reference a^-1 = M_Pl
(scale_reference_primitive, units only). Everything else printed below is a
supplied input or a supplied literal.

Counted checks (2026-11-14): five arithmetic checks of statements the note
makes (alpha_LM^2 = alpha_bare alpha_s(v), the 246.28 GeV hierarchy readout,
the 7/18 taste weight, the exact 682527/5320 GeV calibration value, and its
difference from the 125.10 literal). They check arithmetic only, not physics.
The rest is printed inventory. The runner exits nonzero if a check fails.
"""

from __future__ import annotations

import math
import sys
from fractions import Fraction
from canonical_plaquette_surface import (
    CANONICAL_ALPHA_BARE,
    CANONICAL_ALPHA_LM,
    CANONICAL_ALPHA_S_V,
    CANONICAL_PLAQUETTE,
    CANONICAL_U0,
)

AUDIT_TIMEOUT_SEC = 120

PI = math.pi
M_PL = 1.2209e19
PLAQ = CANONICAL_PLAQUETTE
R_CONN = 8.0 / 9.0

U0 = CANONICAL_U0
ALPHA_BARE = CANONICAL_ALPHA_BARE
ALPHA_LM = CANONICAL_ALPHA_LM
ALPHA_S_V = CANONICAL_ALPHA_S_V
V = M_PL * ((7.0 / 8.0) ** 0.25) * (ALPHA_LM ** 16)
TASTE_WEIGHT = (7.0 / 8.0) * 0.5 * R_CONN

# Current EW support-inventory values from the complete chain.
SIN2_MZ = 0.23061
INV_ALPHA_EM_MZ = 127.665
G1_V = 0.464376
G2_V = 0.648031

# Current Yukawa / top support-inventory values.
YT_WARD_V = 0.973220
YT_PHYSICAL_V = 0.9176
MT_POLE_2L = 172.57
MT_POLE_3L = 173.10

# Current Higgs / vacuum support-inventory values.
MH_2L = 119.77
MH_3L = 125.10
VACUUM_READOUT = "Sampled-flow diagnostic; no all-scale proof"


PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, condition: bool, detail: str = "") -> bool:
    global PASS_COUNT, FAIL_COUNT
    if condition:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    msg = f"  [{'PASS' if condition else 'FAIL'}] {name}"
    if detail:
        msg += f"  ({detail})"
    print(msg)
    return condition


def exact_calibration() -> Fraction:
    """The supplied calibration formula in exact rational arithmetic."""
    mt, mt_ref, mt_step = Fraction("172.57"), Fraction("173.34"), Fraction("0.76")
    a_s, a_ref, a_step = Fraction("0.1181"), Fraction("0.1184"), Fraction("0.0007")
    return Fraction("129.6") + Fraction("1.5") * (mt - mt_ref) / mt_step \
        - Fraction("0.5") * (a_s - a_ref) / a_step


def pct(pred: float, obs: float) -> float:
    return 100.0 * (pred - obs) / obs


def main() -> int:
    print("==============================================================================")
    print("COMPLETE PREDICTION CHAIN: CANONICAL PACKAGE SYNTHESIS")
    print("==============================================================================")
    print()
    print("Framework inputs")
    print(f"  <P>             = {PLAQ:.4f}")
    print(f"  u_0             = {U0:.6f}")
    print(f"  alpha_LM        = {ALPHA_LM:.6f}")
    print(f"  alpha_s(v)      = {ALPHA_S_V:.6f}")
    print(f"  alpha_LM^2      = {ALPHA_LM ** 2:.6f} (= alpha_bare * alpha_s(v))")
    print(f"  v               = {V:.2f} GeV")
    print(f"  R_conn          = {R_CONN:.6f}")
    print(f"  taste_weight    = {TASTE_WEIGHT:.6f} (= 7/18)")
    print()
    print("Conditional historical support inventory; most rows below are supplied literals")
    print("PREMISES: four framework axioms; approved units reference a^-1 = M_Pl (scale_reference_primitive, units only)")
    print("INPUT_SCOPE: supplied pure-gauge plaquette and Ward/threshold/readout conventions")
    print("OPEN, NOT USED FOR UNITS: gravity identification of the natural unit with the Planck length; a^-1 as a physical cutoff")
    print("MATCHING_SCOPE: kappa_EW=0 and kappa_Y=0 are supplied specializations")
    print("HIGGS_SCOPE: 125.10 is not derived here; displayed calibration inputs give the value below")
    calibration_check = 129.6 + 1.5 * (MT_POLE_2L - 173.34) / 0.76 - 0.5 * (0.1181 - 0.1184) / 0.0007
    print(f"  Supplied calibration formula at mt=172.57, alpha_s=0.1181: {calibration_check:.4f} GeV")
    print("This arithmetic is not a full RGE execution or a physical Higgs prediction")
    rows = [
        ("v [GeV]", V, 246.22),
        ("alpha_s(M_Z)", 0.118066, 0.1179),
        ("sin^2(theta_W)(M_Z)", SIN2_MZ, 0.23122),
        ("1/alpha_EM(M_Z)", INV_ALPHA_EM_MZ, 127.951),
        ("g_1(v)", G1_V, 0.463986),
        ("g_2(v)", G2_V, 0.646288),
        ("y_t(v)", YT_PHYSICAL_V, 0.9170),
        ("m_t(pole, 2-loop) [GeV]", MT_POLE_2L, 172.69),
        ("m_t(pole, 3-loop) [GeV]", MT_POLE_3L, 172.69),
        ("m_H(2-loop) [GeV]", MH_2L, 125.25),
        ("m_H(historical literal) [GeV]", MH_3L, 125.25),
    ]
    for label, pred, obs in rows:
        print(f"  {label:<28} {pred:>10.4f}   obs {obs:>10.4f}   dev {pct(pred, obs):>+7.3f}%")
    print(
        "  Vacuum stability".ljust(28)
        + VACUUM_READOUT
        + "   comparator SM metastability"
    )
    print()
    print("Primary support stack")
    print("  COMPLETE_PREDICTION_CHAIN_2026_04_15.md")
    print("  ALPHA_LM_GEOMETRIC_MEAN_IDENTITY_THEOREM_NOTE_2026-04-24.md")
    print("  RCONN_DERIVED_NOTE.md")
    print("  YT_EW_COLOR_PROJECTION_THEOREM.md")
    print("  YT_COLOR_PROJECTION_CORRECTION_NOTE.md")
    print("  YT_QFP_INSENSITIVITY_SUPPORT_NOTE.md")
    print("  HIGGS_MASS_FROM_AXIOM_NOTE.md")
    print()
    print("Arithmetic checks (counted)")
    check("alpha_LM^2 = alpha_bare * alpha_s(v) on the canonical surface",
          abs(ALPHA_LM ** 2 - ALPHA_BARE * ALPHA_S_V) < 1e-12,
          f"{ALPHA_LM ** 2:.10f} vs {ALPHA_BARE * ALPHA_S_V:.10f}")
    check("v = M_Pl (7/8)^(1/4) alpha_LM^16 reproduces the inventory's 246.28 GeV",
          abs(V - 246.28) < 0.005,
          f"v = {V:.4f} GeV at M_Pl = {M_PL:.4e} GeV")
    check("taste weight (7/8)(1/2)(8/9) = 7/18 exactly",
          Fraction(7, 8) * Fraction(1, 2) * Fraction(8, 9) == Fraction(7, 18)
          and abs(TASTE_WEIGHT - 7.0 / 18.0) < 1e-15,
          f"{TASTE_WEIGHT:.15f}")
    exact = exact_calibration()
    check("printed calibration value equals the exact 682527/5320 GeV",
          exact == Fraction(682527, 5320) and abs(calibration_check - float(exact)) < 1e-9,
          f"exact {exact} = {float(exact):.9f}; printed {calibration_check:.9f}")
    check("the calibration value is not the 125.10 GeV historical literal",
          abs(float(exact) - MH_3L) > 1.0,
          f"difference {float(exact) - MH_3L:+.4f} GeV")
    print()
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    print("Status: support inventory; audit status is pipeline-derived")
    return 1 if FAIL_COUNT else 0


if __name__ == "__main__":
    sys.exit(main())
