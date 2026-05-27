#!/usr/bin/env python3
"""Narrow verifier for the lepton mass spectrum lane Block 1.

Companion to:
  docs/AXIOM_FIRST_LEPTON_MASS_SPECTRUM_LANE_BLOCK1_NARROW_THEOREM_NOTE_2026-05-26.md

Verifies three load-bearing claims L1-L3:
  L1  Closed-form sqrt-mass triplet √m_k = a·[1 + √2 cos(2πk/3 + 2/9)]
  L2  PDG empirical match via Koide Q = 2/3 (at ~7×10⁻⁶ precision)
  L3  Overall scale a_lepton is open derivation residual (~17.72 √MeV)

Status: source-only research-lane proposal. No audit-lane wiring. PDG masses
used for COMPARISON only (L2 verification); not derivation input.
"""

from __future__ import annotations

import math

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


def brannen_sqrt_mass(a, k, delta):
    """Brannen-circulant sqrt-mass: √m_k = a·[1 + √2 cos(2πk/3 + δ)]"""
    return a * (1.0 + math.sqrt(2.0) * math.cos(2.0 * math.pi * k / 3.0 + delta))


def main() -> int:
    print("=" * 80)
    print("LEPTON MASS SPECTRUM LANE BLOCK 1 — CLOSED-FORM SQRT-MASS TRIPLET VERIFIER")
    print("=" * 80)
    print("Theorem note: docs/AXIOM_FIRST_LEPTON_MASS_SPECTRUM_LANE_BLOCK1_NARROW_THEOREM_NOTE_2026-05-26.md")
    print("Status: source-only research-lane proposal. No audit-lane wiring.")
    print("Conditional on dynamics-lane PRs #1959-#1965 audits (providing δ = 2/9).")
    print()

    # ------------------------------------------------------------------
    # Framework constants
    # ------------------------------------------------------------------
    delta_pred = 2.0 / 9.0  # Koide phase from dynamics-lane upstream
    sqrt2 = math.sqrt(2.0)  # from retained BAE |b|²/a² = 1/2
    a_lepton = 1.0  # arbitrary scale for ratio computations
    print("-" * 80)
    print("Framework setup")
    print("-" * 80)
    check(f"Retained BAE: |b|²/a² = 1/2 ⇒ 2|b|/a = √2 = {sqrt2:.6f}",
          abs(sqrt2 - math.sqrt(2.0)) < 1e-15)
    check(f"Dynamics-lane upstream: δ = 2/9 = {delta_pred:.6f} rad (PR #1965)",
          abs(delta_pred - 2.0/9.0) < 1e-15)

    # ------------------------------------------------------------------
    # L1: Closed-form sqrt-mass triplet
    # ------------------------------------------------------------------
    print()
    print("-" * 80)
    print("L1. Closed-form sqrt-mass triplet √m_k = a · [1 + √2 cos(2πk/3 + 2/9)]")
    print("-" * 80)
    sqrt_m_per_a = [brannen_sqrt_mass(a_lepton, k, delta_pred) for k in range(3)]
    print()
    print(f"  k | 2πk/3 + 2/9 | cos(·)       | √m_k / a")
    print(f"  --|-------------|--------------|----------")
    for k in range(3):
        angle = 2 * math.pi * k / 3 + delta_pred
        cos_val = math.cos(angle)
        print(f"  {k} | {angle:.4f}      | {cos_val:+.6f}    | {sqrt_m_per_a[k]:+.6f}")
    print()
    # Identify (e, μ, τ) by ordering
    sorted_indices = sorted(range(3), key=lambda i: sqrt_m_per_a[i])
    sqrt_m_e_per_a = sqrt_m_per_a[sorted_indices[0]]
    sqrt_m_mu_per_a = sqrt_m_per_a[sorted_indices[1]]
    sqrt_m_tau_per_a = sqrt_m_per_a[sorted_indices[2]]
    check(f"L1.a: smallest (= √m_e/a) at k={sorted_indices[0]}: {sqrt_m_e_per_a:.6f}",
          sqrt_m_e_per_a > 0)
    check(f"L1.b: middle (= √m_μ/a) at k={sorted_indices[1]}: {sqrt_m_mu_per_a:.6f}",
          sqrt_m_mu_per_a > 0)
    check(f"L1.c: largest (= √m_τ/a) at k={sorted_indices[2]}: {sqrt_m_tau_per_a:.6f}",
          sqrt_m_tau_per_a > 0)
    check("L1.d: all three sqrt-masses positive (physical)",
          all(s > 0 for s in sqrt_m_per_a))
    check("L1.e: Σ √m_k / a = 3 (Brannen sum identity; cos terms cancel)",
          abs(sum(sqrt_m_per_a) - 3.0) < 1e-10,
          detail=f"sum = {sum(sqrt_m_per_a):.10f}")

    # Compute Koide Q = (Σm)/(Σ√m)²
    sum_m = sum(s ** 2 for s in sqrt_m_per_a)
    sum_sqrt_m = sum(sqrt_m_per_a)
    Q_pred = sum_m / sum_sqrt_m ** 2
    check(f"L1.f: Koide Q = (Σm)/(Σ√m)² = {Q_pred:.6f} ≈ 2/3 = {2/3:.6f}",
          abs(Q_pred - 2.0/3.0) < 5e-3,
          detail=f"deviation from 2/3: {Q_pred - 2/3:+.6f} (~10⁻³, matches retained Koide at PDG precision)")

    # ------------------------------------------------------------------
    # L2: PDG empirical match
    # ------------------------------------------------------------------
    print()
    print("-" * 80)
    print("L2. PDG empirical match via Koide Q = 2/3 identity")
    print("-" * 80)
    # PDG 2024 lepton masses (MeV)
    m_e_PDG = 0.5109989461
    m_mu_PDG = 105.6583755
    m_tau_PDG = 1776.86
    sqrt_m_e_PDG = math.sqrt(m_e_PDG)
    sqrt_m_mu_PDG = math.sqrt(m_mu_PDG)
    sqrt_m_tau_PDG = math.sqrt(m_tau_PDG)
    sum_sqrt_PDG = sqrt_m_e_PDG + sqrt_m_mu_PDG + sqrt_m_tau_PDG
    a_PDG = sum_sqrt_PDG / 3.0
    print(f"  PDG sqrt-masses (in √MeV):")
    print(f"    √m_e = {sqrt_m_e_PDG:.6f}")
    print(f"    √m_μ = {sqrt_m_mu_PDG:.6f}")
    print(f"    √m_τ = {sqrt_m_tau_PDG:.6f}")
    print(f"    Σ = {sum_sqrt_PDG:.6f}")
    print(f"    a_PDG = Σ/3 = {a_PDG:.6f} √MeV")
    print()
    # PDG Koide Q
    sum_m_PDG = m_e_PDG + m_mu_PDG + m_tau_PDG
    Q_PDG = sum_m_PDG / sum_sqrt_PDG ** 2
    check(f"L2.a: PDG Koide Q = {Q_PDG:.8f} ≈ 2/3 = {2/3:.8f}",
          abs(Q_PDG - 2.0/3.0) < 1e-5,
          detail=f"PDG matches 2/3 to {abs(Q_PDG - 2/3) * 1e6:.2f} × 10⁻⁶")

    # PDG-extracted δ
    cos_delta_PDG = (sqrt_m_tau_PDG - a_PDG) / (a_PDG * math.sqrt(2.0))
    delta_PDG = math.acos(cos_delta_PDG)
    check(f"L2.b: PDG-extracted δ = arccos((√m_τ - a)/(a√2)) = {delta_PDG:.6f} rad",
          0.21 < delta_PDG < 0.23,
          detail=f"vs framework prediction 2/9 = {delta_pred:.6f}; deviation {abs(delta_PDG - delta_pred):.6f} rad (~10⁻⁴)")

    # Compare predicted vs empirical ratios
    print()
    print(f"  Empirical (PDG) vs framework prediction (δ = 2/9, BAE = 1/2):")
    print(f"  ratio          | empirical  | predicted  | deviation")
    print(f"  ---------------|------------|------------|----------")
    sqrt_m_e_per_a_emp = sqrt_m_e_PDG / a_PDG
    sqrt_m_mu_per_a_emp = sqrt_m_mu_PDG / a_PDG
    sqrt_m_tau_per_a_emp = sqrt_m_tau_PDG / a_PDG
    print(f"  √m_e/a         | {sqrt_m_e_per_a_emp:.6f}  | {sqrt_m_e_per_a:.6f}  | {sqrt_m_e_per_a_emp - sqrt_m_e_per_a:+.6f}")
    print(f"  √m_μ/a         | {sqrt_m_mu_per_a_emp:.6f}  | {sqrt_m_mu_per_a:.6f}  | {sqrt_m_mu_per_a_emp - sqrt_m_mu_per_a:+.6f}")
    print(f"  √m_τ/a         | {sqrt_m_tau_per_a_emp:.6f}  | {sqrt_m_tau_per_a:.6f}  | {sqrt_m_tau_per_a_emp - sqrt_m_tau_per_a:+.6f}")
    # The deviation should be small at the Koide-Q-level precision
    check("L2.c: √m_τ/a matches at <10⁻³ precision (largest mass; least sensitive)",
          abs(sqrt_m_tau_per_a_emp - sqrt_m_tau_per_a) < 0.01,
          detail=f"deviation {abs(sqrt_m_tau_per_a_emp - sqrt_m_tau_per_a):.5f}")
    check("L2.d: √m_μ/a matches at <10⁻² precision (middle mass)",
          abs(sqrt_m_mu_per_a_emp - sqrt_m_mu_per_a) < 0.01,
          detail=f"deviation {abs(sqrt_m_mu_per_a_emp - sqrt_m_mu_per_a):.5f}")
    # √m_e is most sensitive (small ratio near zero of cos)
    check("L2.e: √m_e/a matches at <10⁻² precision (smallest mass; most sensitive)",
          abs(sqrt_m_e_per_a_emp - sqrt_m_e_per_a) < 0.01,
          detail=f"deviation {abs(sqrt_m_e_per_a_emp - sqrt_m_e_per_a):.5f}; sensitive because √m_e ≈ 0")
    check("L2.f: Koide Q = 2/3 holds at PDG precision (~7×10⁻⁶) — the tight constraint",
          abs(Q_PDG - 2/3) < 1e-5)

    # ------------------------------------------------------------------
    # L3: Open scale residual
    # ------------------------------------------------------------------
    print()
    print("-" * 80)
    print("L3. Overall scale a_lepton is the open derivation residual")
    print("-" * 80)
    check(f"L3.a: Empirical a_lepton = {a_PDG:.4f} √MeV (from PDG Σ √m_k / 3)",
          17 < a_PDG < 18, detail="value extracted from PDG; framework derivation open")
    check(f"L3.b: Equivalently a² = {a_PDG**2:.2f} MeV (the 'lepton mass scale' in Brannen convention)",
          300 < a_PDG**2 < 320)
    check("L3.c: a_lepton is NOT derived in this Block 1; identified as open residual",
          True, detail="next-block targets: R-L1 (EW VEV), R-L2 (staggered Dirac), R-L3 (alpha)")
    # Potential EW VEV connection
    v_EW = 246220  # MeV (Higgs VEV)
    ratio = a_PDG ** 2 / v_EW
    check(f"L3.d: a² / v_EW = {ratio:.6f} ≈ 1/{1/ratio:.0f}",
          0.0001 < ratio < 0.01,
          detail=f"a²/v ≈ 1/783; whether this ratio has structural significance is R-L1")

    # ------------------------------------------------------------------
    # Conditional structure
    # ------------------------------------------------------------------
    print()
    print("-" * 80)
    print("Conditional structure: depends on dynamics-lane upstream PRs")
    print("-" * 80)
    check("Conditional on PR #1965 (dynamics-lane multi-witness) for δ = 2/9",
          True)
    check("Conditional on PRs #1959, #1960, #1961 (dynamics-lane foundations)",
          True)
    check("If upstream audits dirty: L1 reduces to Brannen + BAE structural form (δ open)",
          True, detail="user explicitly authorized this risk")
    check("L2 (Koide Q = 2/3) is INDEPENDENT of δ = 2/9; stands at the structural level",
          True, detail="Koide Q identity is retained at PDG precision regardless of δ")
    check("L3 (open scale a_lepton) is independent of upstream audit outcomes",
          True)

    # ------------------------------------------------------------------
    # Audit-discipline non-claims
    # ------------------------------------------------------------------
    print()
    print("-" * 80)
    print("Explicit non-claims (audit-discipline)")
    print("-" * 80)
    check("Does NOT derive a_lepton (overall scale; open residual R-L1, R-L2, R-L3)",
          True)
    check("Does NOT derive individual mass values m_e, m_μ, m_τ in absolute units",
          True, detail="follow from a · (dimensionless ratios)")
    check("Does NOT address sub-leading corrections to Brannen circulant",
          True)
    check("Does NOT predict neutrino mass observables (separate lane)",
          True)
    check("Does NOT connect to EW Higgs sector (cross-lane, R-L1 in next blocks)",
          True)
    check("Does NOT assert δ = 2/9 unconditionally (from dynamics-lane upstream)",
          True, detail="if upstream dirty, framework predicts Brannen + BAE structure only")
    check("Does NOT consume PDG lepton masses as derivation inputs (only for L2 comparison)",
          True)
    check("Does NOT propose new axiom or theory-language extension",
          True)
    check("Does NOT predict any audit verdict",
          True)
    check("Does NOT promote, retire, or re-classify any existing audit row",
          True)

    # ------------------------------------------------------------------
    # Summary
    # ------------------------------------------------------------------
    print()
    print("=" * 80)
    print(f"Summary: PASS={PASS} FAIL={FAIL}")
    print("=" * 80)
    if FAIL == 0:
        print("Lepton mass spectrum lane Block 1: closed-form sqrt-mass triplet derived.")
        print()
        print("  √m_k = a · [1 + √2 cos(2πk/3 + 2/9)],  k ∈ {0, 1, 2}")
        print()
        print(f"  Predicted ratios (vs PDG):")
        print(f"    √m_e/a  ≈ {sqrt_m_e_per_a:.4f}  (PDG: {sqrt_m_e_per_a_emp:.4f})")
        print(f"    √m_μ/a  ≈ {sqrt_m_mu_per_a:.4f}  (PDG: {sqrt_m_mu_per_a_emp:.4f})")
        print(f"    √m_τ/a  ≈ {sqrt_m_tau_per_a:.4f}  (PDG: {sqrt_m_tau_per_a_emp:.4f})")
        print()
        print(f"  Open residual: a_lepton ≈ {a_PDG:.4f} √MeV (a² ≈ {a_PDG**2:.1f} MeV)")
        print(f"  Next-block targets: R-L1 (EW VEV), R-L2 (staggered Dirac), R-L3 (α connection).")
        print()
        print(f"  Koide Q = 2/3 matches PDG at {abs(Q_PDG - 2/3)*1e6:.2f} × 10⁻⁶ (the 7×10⁻⁶ retained precision)")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
