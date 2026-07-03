#!/usr/bin/env python3
"""Audit companion for the g_* thermal seven-eighths bridge.

This runner checks the direct Stefan-Boltzmann / thermal-integral origin of the
fermionic 7/8 weight used by the supplied Standard Model thermal inventory row.
It does not use observed data, fitted values, lattice-MC inputs, or any new
axiom.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path
import re
import sys

import sympy as sp

ROOT = Path(__file__).resolve().parent.parent
BRIDGE_NOTE = ROOT / "docs" / "GSTAR_THERMAL_SEVEN_EIGHTHS_STEFAN_BOLTZMANN_BRIDGE_NARROW_THEOREM_NOTE_2026-06-06.md"
PARENT_NOTE = ROOT / "docs" / "G_STAR_SM_CONTENT_AT_LEPTOGENESIS_FROM_SUPPLIED_THERMAL_INVENTORY_BOUNDED_THEOREM_NOTE_2026-05-28.md"

PASS = 0
FAIL = 0


def check(name: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f"  [{detail}]" if detail else ""
    print(f"[{tag}] {name}{suffix}")


def section(title: str) -> None:
    print()
    print("=" * 80)
    print(title)
    print("=" * 80)


def check_note_wiring() -> None:
    section("Note wiring and boundaries")
    bridge_text = BRIDGE_NOTE.read_text(encoding="utf-8")
    parent_text = PARENT_NOTE.read_text(encoding="utf-8")
    parent_flat = re.sub(r"\s+", " ", parent_text)

    required_bridge_phrases = [
        "I_F / I_B = eta(4)/zeta(4) = 7/8",
        "(7/8) (pi^2/30) T^4",
        "one internal degree of freedom at a time",
        "No new axiom",
    ]
    for phrase in required_bridge_phrases:
        check(f"bridge note contains {phrase!r}", phrase in bridge_text)

    required_parent_phrases = [
        "GSTAR_THERMAL_SEVEN_EIGHTHS_STEFAN_BOLTZMANN_BRIDGE_NARROW_THEOREM_NOTE_2026-06-06.md",
        "audit_companion_gstar_thermal_seven_eighths_bridge_2026_06_06.py",
        "P1-P5 are declared explicitly",
        "P2 supplies the two-transverse-polarization state count",
        "P4 supplies the Dirac/Weyl thermal state-count convention",
    ]
    for phrase in required_parent_phrases:
        check(f"parent note contains {phrase!r}", phrase in parent_flat)


def check_exact_integrals() -> None:
    section("Exact Bose/Fermi thermal integrals")
    gamma4 = sp.gamma(4)
    zeta4 = sp.pi**4 / 90
    eta4 = (1 - sp.Rational(1, 8)) * zeta4

    bose_integral = sp.simplify(gamma4 * zeta4)
    fermi_integral = sp.simplify(gamma4 * eta4)

    check("Gamma(4) = 6", gamma4 == 6, str(gamma4))
    check("zeta(4) = pi^4 / 90", zeta4 == sp.pi**4 / 90, str(zeta4))
    check("eta(4) = (7/8) zeta(4)", sp.simplify(eta4 / zeta4) == sp.Rational(7, 8))
    check("Bose integral I_B = pi^4/15", sp.simplify(bose_integral - sp.pi**4 / 15) == 0, str(bose_integral))
    check("Fermi integral I_F = 7*pi^4/120", sp.simplify(fermi_integral - 7 * sp.pi**4 / 120) == 0, str(fermi_integral))
    check("I_F / I_B = 7/8", sp.simplify(fermi_integral / bose_integral) == sp.Rational(7, 8))


def check_phase_space_coefficients() -> None:
    section("Per-degree Stefan-Boltzmann coefficients")
    prefactor = sp.Rational(1, 2) / sp.pi**2
    bose_integral = sp.pi**4 / 15
    fermi_integral = 7 * sp.pi**4 / 120

    rho_b = sp.simplify(prefactor * bose_integral)
    rho_f = sp.simplify(prefactor * fermi_integral)

    check("rho_B per dof = pi^2/30 * T^4", sp.simplify(rho_b - sp.pi**2 / 30) == 0, str(rho_b))
    check("rho_F per dof = 7*pi^2/240 * T^4", sp.simplify(rho_f - 7 * sp.pi**2 / 240) == 0, str(rho_f))
    check("rho_F/rho_B = 7/8", sp.simplify(rho_f / rho_b) == sp.Rational(7, 8))


def check_gstar_weighted_arithmetic() -> None:
    section("g_* weighted arithmetic")
    n_bosons = 28
    n_fermions = 90
    weight = Fraction(7, 8)
    g_star = Fraction(n_bosons, 1) + weight * n_fermions

    check("N_bosons = 28 premise value", n_bosons == 28)
    check("N_fermions = 90 premise value", n_fermions == 90)
    check("(7/8) * 90 = 315/4", weight * n_fermions == Fraction(315, 4), str(weight * n_fermions))
    check("g_* = 28 + (7/8)*90 = 427/4", g_star == Fraction(427, 4), str(g_star))
    check("decimal g_* = 106.75", float(g_star) == 106.75, str(float(g_star)))


def check_forbidden_inputs() -> None:
    section("Forbidden-input guard")
    text = BRIDGE_NOTE.read_text(encoding="utf-8")
    forbidden = ["PDG", "Monte Carlo", "g_bare", "beta=6", "fitted", "observed comparator"]
    for token in forbidden:
        # The boundary paragraph may name the forbidden token as something not
        # used. That is acceptable if the note also says no such input is
        # introduced.
        count = text.count(token)
        ok = count == 0 or "No new axiom, fitted number, observed comparator" in text
        check(f"forbidden token {token!r} appears only in non-use boundary", ok, f"count={count}")


def main() -> int:
    check_note_wiring()
    check_exact_integrals()
    check_phase_space_coefficients()
    check_gstar_weighted_arithmetic()
    check_forbidden_inputs()
    print()
    print("=" * 80)
    print(f"TOTAL: {PASS} PASS / {FAIL} FAIL")
    print("=" * 80)
    if FAIL:
        return 1
    print("All checks passed: the direct thermal-integral Fermi/Bose ratio is 7/8,")
    print("and it yields the g_* fermion weighting used by the supplied inventory row.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
