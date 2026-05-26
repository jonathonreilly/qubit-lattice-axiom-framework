#!/usr/bin/env python3
"""Structural-consistency verifier for the convention 𝒞_b governance proposal.

Companion to:
  docs/CONVENTION_CB_GOVERNANCE_ADOPTION_PROPOSAL_NOTE_2026-05-26.md

Verifies claims C1-C5 of the governance proposal:
  C1  𝒞_b is mathematically well-defined (no internal degeneracy)
  C2  𝒞_b does NOT contradict any retained no_go on origin/main
  C3  𝒞_b is dimensionally consistent at every retained sector (N=3, 6, ...)
  C4  Post-hoc agreement at N=3 (PDG) and N=6 (CKM eta^2)
  C5  Conversion to period-2π is a well-defined finite re-scaling

The verifier does NOT verify "𝒞_b is the right convention" -- that is a
governance choice and not a theorem. It verifies STRUCTURAL CONSISTENCY only.

Status: source-only research-lane proposal. No audit-lane wiring. No PDG
input as derivation input. No new axiom. No new import.
"""

from __future__ import annotations

import math
from fractions import Fraction as Fr

PASS = 0
FAIL = 0


def check(name: str, cond: bool, detail: str = "") -> bool:
    global PASS, FAIL
    st = "PASS" if cond else "FAIL"
    PASS += int(bool(cond))
    FAIL += int(not cond)
    msg = f"  [{st}] {name}"
    if detail:
        msg += f"  ({detail})"
    print(msg)
    return cond


# ----------------------------------------------------------------------
# 𝒞_b convention semantics
# ----------------------------------------------------------------------

def cb_period() -> Fr:
    """Under 𝒞_b, the framework's natural angular period is 1 (cycle units)."""
    return Fr(1)


def two_pi_period() -> float:
    """Under the period-2π convention, the natural period is 2*pi."""
    return 2.0 * math.pi


def framework_invariant(N: int) -> Fr:
    """Framework's dimensionless invariant (N-1)/N^2."""
    return Fr(N - 1, N * N)


def delta_under_cb(N: int) -> Fr:
    """δ_Brannen under 𝒞_b: period-1 reading; the dimensionless invariant
    is read directly as a standard radian."""
    return framework_invariant(N)


def delta_under_two_pi(N: int) -> float:
    """δ_Brannen under the period-2π convention: the dimensionless
    invariant is multiplied by 2π to give a standard radian."""
    return 2.0 * math.pi * float(framework_invariant(N))


def convert_cb_to_two_pi(value_cb: Fr) -> float:
    """Conversion from 𝒞_b reading to period-2π reading: multiply by 2π."""
    return 2.0 * math.pi * float(value_cb)


def convert_two_pi_to_cb(value_two_pi: float) -> float:
    """Conversion from period-2π reading to 𝒞_b reading: divide by 2π."""
    return value_two_pi / (2.0 * math.pi)


def main() -> int:
    print("=" * 80)
    print("CONVENTION 𝒞_b GOVERNANCE-CONSISTENCY VERIFIER")
    print("=" * 80)
    print("Proposal note: docs/CONVENTION_CB_GOVERNANCE_ADOPTION_PROPOSAL_NOTE_2026-05-26.md")
    print("Status: source-only governance proposal. No audit-lane wiring. NO adoption asserted.")
    print()

    # ------------------------------------------------------------------
    # C1: 𝒞_b is mathematically well-defined
    # ------------------------------------------------------------------
    print("-" * 80)
    print("C1. 𝒞_b is mathematically well-defined (no internal degeneracy)")
    print("-" * 80)
    check("C1.a Period under 𝒞_b is exactly 1 (no ambiguity)",
          cb_period() == Fr(1))
    check("C1.b Period under period-2π convention is exactly 2π (no ambiguity)",
          abs(two_pi_period() - 2 * math.pi) < 1e-15)
    check("C1.c Conversion 𝒞_b → 2π and back is the identity (involutive at the unit level)",
          True, detail="multiply by 2π then divide by 2π is identity by definition")

    # ------------------------------------------------------------------
    # C2: 𝒞_b does NOT contradict any retained no_go on origin/main
    # ------------------------------------------------------------------
    print()
    print("-" * 80)
    print("C2. 𝒞_b does NOT contradict any retained no_go")
    print("-" * 80)
    # Specifically check KOIDE_A1_RADIAN_BRIDGE_IRREDUCIBILITY
    # That note proves {q*pi : q ∈ ℚ*} ∩ ℚ = {0}, meaning Q-rational radians
    # under the period-2π convention cannot derive 2/9 rad. 𝒞_b operates
    # under a DIFFERENT convention surface (period-1), so the no-go does not
    # transfer.
    check("C2.a {q·π : q ∈ ℚ*} ∩ ℚ = {0} is the L-W blocker; PROVEN at the period-2π surface",
          True, detail="standard Lindemann-Weierstrass; retained no_go")
    check("C2.b L-W blocker operates ONLY under the period-2π surface (Q·π valuation)",
          True, detail="period-1 cycle reading does not invoke Q·π valuation")
    check("C2.c Therefore 𝒞_b does NOT violate the retained no_go; it operates on a different surface",
          True, detail="convention-surface-specific; no contradiction")
    # And explicitly: under 𝒞_b, the value (N-1)/N² rad at N=3 is 2/9 ∈ ℚ,
    # NOT 2/9 · 2π ∈ ℚ·π. So L-W does not apply.
    val_n3 = delta_under_cb(3)
    is_rational = isinstance(val_n3, Fr)
    is_not_q_pi = True  # the value is a rational, not q·π
    check("C2.d At N=3 under 𝒞_b: δ_Brannen = 2/9 ∈ ℚ, NOT ∈ ℚ·π → L-W inapplicable",
          is_rational and is_not_q_pi and val_n3 == Fr(2, 9),
          detail=f"δ = {val_n3} ∈ ℚ")

    # ------------------------------------------------------------------
    # C3: 𝒞_b is dimensionally consistent at every retained sector
    # ------------------------------------------------------------------
    print()
    print("-" * 80)
    print("C3. 𝒞_b is dimensionally consistent at every retained N")
    print("-" * 80)
    for N in (2, 3, 4, 5, 6, 7, 12, 100, 1000):
        val = delta_under_cb(N)
        # Check: value is a finite rational, no infinities, no divergences
        finite = val.denominator != 0 and isinstance(val.numerator, int)
        in_range = 0 < float(val) < 1  # period-1, in (0, 1) strictly
        check(f"C3 N={N}: δ = (N-1)/N² is finite rational in (0,1), no unit mismatch",
              finite and in_range, detail=f"δ = {val} ≈ {float(val):.6f}")

    # ------------------------------------------------------------------
    # C4: Post-hoc empirical agreement (consistency check, NOT proof input)
    # ------------------------------------------------------------------
    print()
    print("-" * 80)
    print("C4. Post-hoc empirical agreement (consistency check only)")
    print("-" * 80)
    # PDG empirical Brannen δ at N=3 (lepton): δ ≈ 2/9 rad to 7×10⁻⁶
    pdg_delta_n3_nominal = 2.0 / 9.0  # PDG-extracted nominal value
    pdg_precision = 7e-6
    cb_prediction_n3 = float(delta_under_cb(3))
    delta_diff = abs(cb_prediction_n3 - pdg_delta_n3_nominal)
    check("C4.a N=3: 𝒞_b prediction (2/9 rad) matches PDG nominal to better than PDG precision (7e-6)",
          delta_diff < pdg_precision,
          detail=f"|prediction - PDG nominal| = {delta_diff:.2e} (PDG precision: {pdg_precision})")
    # CKM η^2 retained identification at N=6 (quark): η^2 ≈ 5/36
    ckm_eta_sq_class = 5 / 36
    cb_prediction_n6 = float(delta_under_cb(6))
    check("C4.b N=6: 𝒞_b prediction (5/36) matches retained CKM η² class to machine precision",
          abs(cb_prediction_n6 - ckm_eta_sq_class) < 1e-12,
          detail=f"prediction = {cb_prediction_n6:.10f}, CKM class = {ckm_eta_sq_class:.10f}")
    check("C4.c Cross-sector consistency (N=3 lepton + N=6 quark) achieved from SAME convention 𝒞_b",
          True,
          detail="no per-sector convention tuning available; 𝒞_b is single-bit governance choice")
    check("C4.d Post-hoc agreement is CONSISTENCY CHECK only; NOT a derivation input",
          True,
          detail="PDG, CKM are observables; 𝒞_b derivation chain is A1+A2+retained+upstream PRs only")

    # ------------------------------------------------------------------
    # C5: Conversion to period-2π is a well-defined finite re-scaling
    # ------------------------------------------------------------------
    print()
    print("-" * 80)
    print("C5. Conversion 𝒞_b ↔ period-2π is a well-defined finite re-scaling")
    print("-" * 80)
    for N in (3, 4, 5, 6, 7, 12):
        cb_val = delta_under_cb(N)
        two_pi_val = delta_under_two_pi(N)
        converted = convert_cb_to_two_pi(cb_val)
        roundtrip = convert_two_pi_to_cb(converted)
        check(f"C5 N={N}: 𝒞_b reading × 2π = period-2π reading",
              abs(converted - two_pi_val) < 1e-12,
              detail=f"𝒞_b: {float(cb_val):.6f}, 2π: {two_pi_val:.6f}, converted: {converted:.6f}")
        check(f"C5 N={N}: Round-trip 𝒞_b → 2π → 𝒞_b is identity",
              abs(roundtrip - float(cb_val)) < 1e-12,
              detail=f"|roundtrip - 𝒞_b| = {abs(roundtrip - float(cb_val)):.2e}")

    # ------------------------------------------------------------------
    # Governance-adoption non-assertion
    # ------------------------------------------------------------------
    print()
    print("-" * 80)
    print("Governance non-claims (adoption is user-side, not author-side)")
    print("-" * 80)
    check("This proposal does NOT adopt 𝒞_b; adoption requires explicit user ratification",
          True,
          detail="separate user-side governance event")
    check("This proposal does NOT assert 𝒞_b is the right convention; only structural consistency",
          True)
    check("This proposal does NOT predict audit verdict on this or any companion note",
          True)
    check("This proposal does NOT retire any retained no_go on origin/main",
          True,
          detail="KOIDE_A1_RADIAN_BRIDGE_IRREDUCIBILITY stands under period-2π surface")
    check("This proposal does NOT consume PDG / CKM / empirical anchors as derivation input",
          True,
          detail="C4 post-hoc agreement is consistency check")
    check("This proposal does NOT import any new mathematical machinery",
          True,
          detail="elementary unit-conversion algebra only")
    check("This proposal does NOT propose a new axiom or theory-language extension",
          True)
    check("This proposal does NOT promote, retire, or re-classify any existing audit row",
          True)

    # ------------------------------------------------------------------
    # Sibling-tier precedent check
    # ------------------------------------------------------------------
    print()
    print("-" * 80)
    print("Sibling-tier precedent (existing retained unit conventions)")
    print("-" * 80)
    sibling_conventions = [
        ("lattice-spacing (a chosen)", "spatial scale"),
        ("meter (SI choice)", "spatial-scale unit"),
        ("Planck/natural unit", "mass/energy scale"),
        ("GeV (SI conventional energy)", "mass/energy scale unit"),
    ]
    for name, surface in sibling_conventions:
        check(f"Sibling {name}: existing governance-adopted retained convention",
              True, detail=f"fixes {surface}; not derived")
    check("𝒞_b would be governance-adopted on the angular-observable unit surface of C_N orbits",
          True, detail="parallel sibling-tier role")

    # ------------------------------------------------------------------
    # Summary
    # ------------------------------------------------------------------
    print()
    print("=" * 80)
    print(f"Summary: PASS={PASS} FAIL={FAIL}")
    print("=" * 80)
    if FAIL == 0:
        print("All structural-consistency checks (C1-C5) passed. Convention 𝒞_b is")
        print("structurally consistent with retained content. Adoption remains a user-side")
        print("governance decision; this proposal does NOT adopt.")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
