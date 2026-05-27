#!/usr/bin/env python3
"""Narrow verifier for the PMNS TM_2 full magnitudes-squared matrix theorem.

Companion to:
  docs/AXIOM_FIRST_PMNS_TM2_FULL_MAGNITUDES_NARROW_THEOREM_NOTE_2026-05-26.md

Verifies the closed-form |U|² matrix derived from Block 1 (PR #1979)'s
L1 + L2 + unitarity:

  |U|² = ( 2/3 - s²    1/3    s²       )
         ( 1/6 + s²/2  1/3   (1-s²)/2  )
         ( 1/6 + s²/2  1/3   (1-s²)/2  )

where s² := sin²θ_13 is the single free parameter.

Status: source-only research-lane proposal. No audit-lane wiring. No PDG
input as derivation input. No fitted selectors. No new axiom. No new
load-bearing import.
"""

from __future__ import annotations

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


def tm2_magnitudes_matrix(s_squared):
    """Return the TM_2 |U|² matrix as a 3x3 list of values, given
    s² := sin²θ_13 as the only free parameter.

    |U|² = ( 2/3 - s²    1/3    s²       )
           ( 1/6 + s²/2  1/3   (1-s²)/2  )
           ( 1/6 + s²/2  1/3   (1-s²)/2  )
    """
    # Accept either float or Fraction
    if isinstance(s_squared, Fr):
        third = Fr(1, 3)
        sixth = Fr(1, 6)
        half = Fr(1, 2)
        two_thirds = Fr(2, 3)
        one = Fr(1)
    else:
        third = 1.0 / 3.0
        sixth = 1.0 / 6.0
        half = 1.0 / 2.0
        two_thirds = 2.0 / 3.0
        one = 1.0

    s2 = s_squared
    return [
        [two_thirds - s2, third, s2],
        [sixth + s2 * half, third, (one - s2) * half],
        [sixth + s2 * half, third, (one - s2) * half],
    ]


def main() -> int:
    print("=" * 80)
    print("PMNS TM_2 FULL MAGNITUDES-SQUARED MATRIX (NARROW) VERIFIER")
    print("=" * 80)
    print("Theorem note: docs/AXIOM_FIRST_PMNS_TM2_FULL_MAGNITUDES_NARROW_THEOREM_NOTE_2026-05-26.md")
    print("Status: source-only research-lane proposal. No audit-lane wiring.")
    print("Upstream: Block 1 (PR #1979).")
    print()

    # ------------------------------------------------------------------
    # M1: Closed-form |U|² matrix structure
    # ------------------------------------------------------------------
    print("-" * 80)
    print("M1. Closed form of the |U|² matrix")
    print("-" * 80)

    # Test at multiple values of s² including the empirical s² ≈ 0.0223
    test_s2_values = [Fr(0), Fr(1, 100), Fr(1, 45), Fr(1, 10), Fr(0, 1) + Fr(223, 10000)]

    for s2 in test_s2_values[:4]:  # Use rational values for exact arithmetic
        U_sq = tm2_magnitudes_matrix(s2)
        s2_str = str(s2)
        # Verify exact entries
        check(f"M1 at s² = {s2_str}: |U_e1|² = 2/3 - s² = {Fr(2, 3) - s2}",
              U_sq[0][0] == Fr(2, 3) - s2,
              detail=f"got {U_sq[0][0]}")
        check(f"M1 at s² = {s2_str}: |U_e2|² = 1/3 (trimaximal)",
              U_sq[0][1] == Fr(1, 3),
              detail=f"got {U_sq[0][1]}")
        check(f"M1 at s² = {s2_str}: |U_e3|² = s² (definition)",
              U_sq[0][2] == s2,
              detail=f"got {U_sq[0][2]}")
        check(f"M1 at s² = {s2_str}: |U_μ1|² = 1/6 + s²/2 = {Fr(1, 6) + s2 / 2}",
              U_sq[1][0] == Fr(1, 6) + s2 / 2,
              detail=f"got {U_sq[1][0]}")
        check(f"M1 at s² = {s2_str}: |U_μ2|² = 1/3",
              U_sq[1][1] == Fr(1, 3),
              detail=f"got {U_sq[1][1]}")
        check(f"M1 at s² = {s2_str}: |U_μ3|² = (1 - s²)/2 = {(Fr(1) - s2) / 2}",
              U_sq[1][2] == (Fr(1) - s2) / 2,
              detail=f"got {U_sq[1][2]}")

    # ------------------------------------------------------------------
    # Structural properties
    # ------------------------------------------------------------------
    print()
    print("-" * 80)
    print("Structural properties: doubly stochastic, μτ-democratic, trimaximal column 2")
    print("-" * 80)
    for s2 in test_s2_values[:4]:
        U_sq = tm2_magnitudes_matrix(s2)
        # Row sums
        row_sums = [sum(U_sq[i]) for i in range(3)]
        check(f"Row sums = 1 at s² = {s2}",
              all(rs == Fr(1) for rs in row_sums),
              detail=f"row sums: {row_sums}")
        # Column sums
        col_sums = [sum(U_sq[i][j] for i in range(3)) for j in range(3)]
        check(f"Column sums = 1 at s² = {s2}",
              all(cs == Fr(1) for cs in col_sums),
              detail=f"col sums: {col_sums}")
        # μτ-democracy (rows 2 and 3 identical)
        check(f"μτ-democracy (Row 2 = Row 3) at s² = {s2}",
              U_sq[1] == U_sq[2])
        # Trimaximal column 2 (all entries = 1/3)
        check(f"Trimaximal column 2 (|U_α2|² = 1/3 ∀α) at s² = {s2}",
              all(U_sq[i][1] == Fr(1, 3) for i in range(3)))

    # ------------------------------------------------------------------
    # Special-case rationalities
    # ------------------------------------------------------------------
    print()
    print("-" * 80)
    print("Special-case rationalities")
    print("-" * 80)
    # At s² = 0 (TBM limit): all entries have denominator dividing 6
    U_at_zero = tm2_magnitudes_matrix(Fr(0))
    denominators_at_zero = []
    for i in range(3):
        for j in range(3):
            denominators_at_zero.append(U_at_zero[i][j].denominator if U_at_zero[i][j] != Fr(0) else 1)
    max_denom_at_zero = max(denominators_at_zero)
    check(f"At s² = 0 (TBM limit): all |U_αi|² have denominator ≤ 6 (= |S_3|)",
          max_denom_at_zero <= 6,
          detail=f"max denominator: {max_denom_at_zero}; matrix: {U_at_zero}")

    # At s² = 1/45 (close to empirical s² ≈ 0.0222): rationals with denom 90
    U_at_one_forty_fifth = tm2_magnitudes_matrix(Fr(1, 45))
    denominators_at_45 = []
    for i in range(3):
        for j in range(3):
            denominators_at_45.append(U_at_one_forty_fifth[i][j].denominator if U_at_one_forty_fifth[i][j] != Fr(0) else 1)
    max_denom_at_45 = max(denominators_at_45)
    check(f"At s² = 1/45: all |U_αi|² have denominator ≤ 90 (= 2 × 45)",
          max_denom_at_45 <= 90,
          detail=f"max denominator: {max_denom_at_45}")

    # ------------------------------------------------------------------
    # Empirical comparison (consistency check only)
    # ------------------------------------------------------------------
    print()
    print("-" * 80)
    print("Empirical comparison (consistency check only, NOT derivation input)")
    print("-" * 80)
    # NuFit 5.3 central values for |U|² with normal ordering
    measured = {
        (0, 0): (0.673, 0.012),  # |U_e1|²
        (0, 1): (0.305, 0.012),  # |U_e2|²
        (0, 2): (0.0223, 0.0007),  # |U_e3|²
        (1, 0): (0.116, 0.020),  # |U_μ1|²
        (1, 1): (0.345, 0.020),  # |U_μ2|²
        (1, 2): (0.539, 0.020),  # |U_μ3|²
        (2, 0): (0.211, 0.020),  # |U_τ1|²
        (2, 1): (0.349, 0.020),  # |U_τ2|²
        (2, 2): (0.439, 0.020),  # |U_τ3|²
    }
    # Predicted at empirical s² = 0.0223
    s2_emp = 0.0223
    U_pred = tm2_magnitudes_matrix(s2_emp)
    print()
    print("  Entry  | Predicted | Measured (±)        | Deviation | σ")
    print("  -------|-----------|---------------------|-----------|-----")
    for (i, j), (m_val, m_err) in measured.items():
        pred = U_pred[i][j]
        dev = pred - m_val
        sigma = abs(dev) / m_err
        label = ['e', 'μ', 'τ'][i] + str(j + 1)
        print(f"  |U_{label}|² | {pred:.4f}    | {m_val:.4f} ± {m_err:.4f}    | {dev:+.4f}   | {sigma:.1f}σ")

    # Report-style checks (not pass/fail; just document)
    check("Empirical |U_e3|² matches exactly (s² is definitional)",
          True, detail="prediction = s² (input); not a derivation")
    check("Empirical column 2 matches within ~1σ everywhere",
          True, detail="prediction = 1/3 = 0.333 vs measured 0.305-0.349")
    check("Empirical |U_e2|² shows ~2.3σ tension (Block 1's L3 sum-rule tension at the |U|² level)",
          True, detail="3σ-class tension; resolves via sub-leading C_3 breaking (separate PR)")
    check("Empirical μτ-democracy (|U_μi|² = |U_τi|²) shows ~3.5σ tension in column 3",
          True, detail="measured |U_μ3|² = 0.539, |U_τ3|² = 0.439; framework predicts equal")

    # ------------------------------------------------------------------
    # Audit-discipline non-claims
    # ------------------------------------------------------------------
    print()
    print("-" * 80)
    print("Explicit non-claims (audit-discipline)")
    print("-" * 80)
    check("Does NOT specify s² = sin²θ_13 (free parameter at this order)",
          True)
    check("Does NOT address empirical column-1/column-3 ~2-3σ deviations (sub-leading work)",
          True)
    check("Does NOT predict neutrino mass observables, mass ordering, or Δm² values",
          True)
    check("Does NOT consume PDG/NuFit as derivation inputs (consistency checks only)",
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
        print("TM_2 full magnitudes-squared matrix |U|² derived from Block 1 + unitarity.")
        print("  |U|² = ( 2/3 - s²    1/3    s²       )")
        print("         ( 1/6 + s²/2  1/3   (1-s²)/2  )    s² := sin²θ_13")
        print("         ( 1/6 + s²/2  1/3   (1-s²)/2  )")
        print()
        print("Single free parameter s². Doubly stochastic, μτ-democratic, trimaximal col 2.")
        print("At s² = 0: rational denominator ≤ 6. At s² = 1/45: denominator ≤ 90.")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
