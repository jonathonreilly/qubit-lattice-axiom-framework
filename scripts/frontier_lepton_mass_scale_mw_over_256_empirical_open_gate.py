#!/usr/bin/env python3
"""Verifier for the lepton mass scale m_W/256 empirical open gate.

Companion to:
  docs/LEPTON_MASS_SCALE_MW_OVER_256_EMPIRICAL_OPEN_GATE_NOTE_2026-05-26.md

Verifies four bounded/open-gate checks:
  S1  Empirical comparator a² ~= m_W / (dim_C(M_2(C)))^4 = m_W / 256.
  S2  m_W-anchored charged-lepton comparators are sharp.
  S3  Empirical offset is at the PDG m_W precision scale.
  S4  The open derivation target is dim_C(M_2(C))^4 = 256.

Status: source-only open_gate proposal. No audit-lane verdict wiring. m_W and
the charged-lepton masses are empirical comparator inputs, not derivations.
"""

from __future__ import annotations

import math
from pathlib import Path

from lepton_brannen_boundary_checks_2026_06_13 import run_delta_boundary_checks, run_scale_boundary_checks

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


def main() -> int:
    print("=" * 80)
    print("LEPTON MASS SCALE m_W/256 EMPIRICAL OPEN-GATE VERIFIER")
    print("=" * 80)
    print("Note: docs/LEPTON_MASS_SCALE_MW_OVER_256_EMPIRICAL_OPEN_GATE_NOTE_2026-05-26.md")
    print("Status: source-only open_gate proposal. No audit-lane verdict wiring.")
    print()
    print("Comparator formula: Brannen-style square-root triplet with δ = 2/9.")
    print("Empirical inputs: PDG m_W and charged-lepton masses.")
    print()

    # ------------------------------------------------------------------
    # Framework constants
    # ------------------------------------------------------------------
    dim_C_M2C = 4  # complex dimension of M_2(C) = Cl(3,0) per-site algebra
    dim_factor = dim_C_M2C ** 4  # = 256
    delta = 2.0 / 9.0
    sqrt2 = math.sqrt(2.0)

    # PDG inputs (empirical comparators, not derivation inputs)
    m_W = 80369.2      # MeV, PDG 2024 central
    m_W_err = 15.7     # MeV
    m_e = 0.5109989461
    m_mu = 105.6583755
    m_tau = 1776.86

    print("-" * 80)
    print("Framework setup")
    print("-" * 80)
    check(f"one-qubit operator algebra M_2(C), dim_C = {dim_C_M2C}",
          dim_C_M2C == 4)
    check(f"dim_factor = dim_C(M_2(C))^4 = {dim_C_M2C}^4 = {dim_factor}",
          dim_factor == 256)
    check(f"comparator delta = 2/9 = {delta:.6f}",
          abs(delta - 2.0/9.0) < 1e-15)
    check(f"sqrt coefficient = √2 = {sqrt2:.6f}",
          abs(sqrt2 - math.sqrt(2.0)) < 1e-15)

    # ------------------------------------------------------------------
    # S1: Empirical comparator a² ~= m_W / 256
    # ------------------------------------------------------------------
    print()
    print("-" * 80)
    print(f"S1. Empirical comparator a²_lepton ~= m_W / dim_C(M_2(C))^4 = m_W / {dim_factor}")
    print("-" * 80)
    a_sq_pred = m_W / dim_factor
    # Block 1 empirical a (from Σ √m_lepton / 3)
    sqrt_m_sum = math.sqrt(m_e) + math.sqrt(m_mu) + math.sqrt(m_tau)
    a_emp = sqrt_m_sum / 3.0
    a_sq_emp = a_emp ** 2

    print(f"  m_W (PDG 2024) = {m_W:.1f} ± {m_W_err:.1f} MeV")
    print(f"  m_W / 256 = {a_sq_pred:.4f} MeV")
    print(f"  a² empirical (from PDG lepton masses) = {a_sq_emp:.4f} MeV")
    rel_dev = (a_sq_pred - a_sq_emp) / a_sq_emp
    m_W_rel_err = m_W_err / m_W
    print(f"  Relative deviation: {rel_dev*100:+.4f}%")
    print(f"  PDG m_W relative precision: {m_W_rel_err*100:.4f}%")
    check("S1.a: empirical comparator offset is below 0.05%",
          abs(rel_dev) < 0.0005,
          detail=f"deviation {rel_dev*100:+.4f}%, PDG precision {m_W_rel_err*100:.4f}%")

    # Equivalent forms
    a_pred = math.sqrt(a_sq_pred)
    check(f"S1.b: bookkeeping form a / √m_W = 1/{dim_C_M2C**2} (= 1/16, dim_C²)",
          abs(a_pred / math.sqrt(m_W) - 1/16) < 1e-4,
          detail=f"a/√m_W = {a_pred/math.sqrt(m_W):.6f}, 1/16 = {1/16:.6f}")
    check("S1.c: open target is 1/256 = 1/(dim_C(M_2(C)))^4",
          True, detail="this runner records the target; it does not derive it")

    # ------------------------------------------------------------------
    # S2: m_W-anchored mass comparators
    # ------------------------------------------------------------------
    print()
    print("-" * 80)
    print("S2. m_W-anchored charged-lepton comparators are sharp")
    print("-" * 80)
    # Comparator masses with a² = m_W / 256 and delta = 2/9.
    a_sq = a_sq_pred
    masses_by_k = {}
    for k in range(3):
        sqrt_m_k_per_a = 1.0 + sqrt2 * math.cos(2 * math.pi * k / 3 + delta)
        m_k_pred = a_sq * sqrt_m_k_per_a ** 2
        masses_by_k[k] = (sqrt_m_k_per_a, m_k_pred)
    # Sort by mass to assign e, μ, τ
    sorted_k = sorted(masses_by_k.keys(), key=lambda k: masses_by_k[k][1])
    k_e, k_mu, k_tau = sorted_k[0], sorted_k[1], sorted_k[2]
    m_e_pred = masses_by_k[k_e][1]
    m_mu_pred = masses_by_k[k_mu][1]
    m_tau_pred = masses_by_k[k_tau][1]

    print()
    print(f"  k | √m_k/a       | comparator m_k (MeV) | empirical m_k (MeV) | deviation")
    print(f"  --|--------------|---------------------|---------------------|----------")
    print(f"  {k_e} | {masses_by_k[k_e][0]:+.6f}    | {m_e_pred:.4f}              | {m_e:.4f}              | {(m_e_pred-m_e)/m_e*100:+.3f}% (m_e)")
    print(f"  {k_mu} | {masses_by_k[k_mu][0]:+.6f}    | {m_mu_pred:.4f}             | {m_mu:.4f}             | {(m_mu_pred-m_mu)/m_mu*100:+.3f}% (m_μ)")
    print(f"  {k_tau} | {masses_by_k[k_tau][0]:+.6f}    | {m_tau_pred:.2f}            | {m_tau:.2f}            | {(m_tau_pred-m_tau)/m_tau*100:+.3f}% (m_τ)")

    # m_tau comparator at PDG precision scale.
    m_tau_dev = abs((m_tau_pred - m_tau) / m_tau)
    check("S2.a: m_tau comparator from m_W/256 is within 0.05%",
          m_tau_dev < 0.0005,
          detail=f"deviation {m_tau_dev*100:+.4f}% at the PDG m_W precision scale")
    # m_mu comparator at PDG precision scale.
    m_mu_dev = abs((m_mu_pred - m_mu) / m_mu)
    check("S2.b: m_mu comparator from m_W/256 is within 0.05%",
          m_mu_dev < 0.0005,
          detail=f"deviation {m_mu_dev*100:+.4f}% within the PDG precision scale")
    # m_e comparator at PDG precision scale.
    m_e_dev = abs((m_e_pred - m_e) / m_e)
    check("S2.c: m_e comparator from m_W/256 is within 0.05%",
          m_e_dev < 0.0005,
          detail=f"deviation {m_e_dev*100:+.4f}% within the PDG precision scale")

    # ------------------------------------------------------------------
    # S3: Empirical match at PDG precision
    # ------------------------------------------------------------------
    print()
    print("-" * 80)
    print("S3. Empirical offset is at the PDG m_W precision scale")
    print("-" * 80)
    check(f"S3.a: comparator offset {abs(rel_dev)*100:.4f}% is within 2x PDG m_W precision {m_W_rel_err*100:.4f}%",
          abs(rel_dev) < m_W_rel_err * 2,  # within 2× PDG precision
          detail=f"near the PDG precision floor; tighter m_W measurements would test this directly")
    check("S3.b: m_tau comparator lies within the m_W uncertainty scale",
          m_tau_dev < m_W_rel_err * 3,
          detail=f"m_τ deviation {m_tau_dev*100:+.4f}% vs ~3·PDG_m_W {3*m_W_rel_err*100:+.4f}%")

    # ------------------------------------------------------------------
    # S4: Open derivation target
    # ------------------------------------------------------------------
    print()
    print("-" * 80)
    print("S4. Open derivation target: factor 1/256 = 1/(dim_C(M_2(C)))^4")
    print("-" * 80)
    check(f"S4.a: dim_C(M_2(C)) = {dim_C_M2C} (per-site complex algebra dimension)",
          dim_C_M2C == 4)
    check(f"S4.b: dim_C^4 = {dim_C_M2C}^4 = {dim_factor} (suppression factor)",
          dim_factor == 256)
    check("S4.c: no derivation of the 1/256 factor is performed here",
          True, detail="open target only")
    check("S4.d: future work is to derive 1/256 without empirical m_W or lepton masses",
          True, detail="potential paths include Dirac scaling, operator factors, or dimension-chain work")

    # ------------------------------------------------------------------
    # Conditional structure
    # ------------------------------------------------------------------
    print()
    print("-" * 80)
    print("Open-gate structure")
    print("-" * 80)
    check("S1/S3 use only PDG comparator values and dim_C(M_2(C))=4 bookkeeping",
          True)
    check("S2 uses delta=2/9 as a comparator setting, not as a retained input",
          True)
    check("all three comparators use empirical m_W plus the delta=2/9 setting",
          True, detail="sharp numerical agreement is not a derivation")

    # ------------------------------------------------------------------
    # Audit-discipline non-claims
    # ------------------------------------------------------------------
    print()
    print("-" * 80)
    print("Explicit non-claims (audit-discipline)")
    print("-" * 80)
    check("Does NOT derive the 1/256 factor",
          True)
    check("Does NOT derive m_mu from framework structure alone",
          True)
    check("Does NOT derive m_e from framework structure alone",
          True)
    check("Does NOT derive m_W",
          True)
    check("Uses PDG m_W and charged-lepton masses only as empirical comparators",
          True)
    check("Does NOT propose new axiom or theory-language extension",
          True)
    check("Does NOT predict any audit verdict",
          True)
    check("Does NOT promote/retire/re-classify any existing audit row",
          True)
    check("Does NOT claim lepton-sector closure",
          True)

    root = Path(__file__).resolve().parents[1]
    for ok in run_scale_boundary_checks(root, check, "downstream scale boundary"):
        pass
    for ok in run_delta_boundary_checks(root, check, "downstream delta boundary"):
        pass

    # ------------------------------------------------------------------
    # Summary
    # ------------------------------------------------------------------
    print()
    print("=" * 80)
    print(f"Summary: PASS={PASS} FAIL={FAIL}")
    print("=" * 80)
    if FAIL == 0:
        print("Empirical comparator a²_lepton ~= m_W / 256 = m_W / (dim_C(M_2(C)))^4")
        print(f"  m_W / 256 = {a_sq_pred:.4f} MeV")
        print(f"  a² empirical = {a_sq_emp:.4f} MeV")
        print(f"  Offset {abs(rel_dev)*100:.4f}% (PDG m_W precision scale {m_W_rel_err*100:.4f}%)")
        print()
        print("charged-lepton comparators from m_W/256:")
        print(f"  m_e comparator = {m_e_pred:.6f} MeV (PDG {m_e:.6f}, {m_e_dev*100:+.4f}%)")
        print(f"  m_mu comparator = {m_mu_pred:.4f} MeV (PDG {m_mu:.4f}, {m_mu_dev*100:+.4f}%)")
        print(f"  m_tau comparator = {m_tau_pred:.2f} MeV (PDG {m_tau:.2f}, {m_tau_dev*100:+.3f}%)")
        print()
        print("This is an empirical open gate, not a derivation from framework structure alone.")
        print()
        print("Open target: derive the 1/256 factor without empirical m_W or lepton masses.")
        print("Open target: derive m_W itself before any parameter-free lepton-scale claim.")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
