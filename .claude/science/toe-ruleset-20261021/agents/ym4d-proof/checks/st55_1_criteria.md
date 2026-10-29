# st55_1 — pre-registered criteria (written before any st55_1 script exists)

Object: STEP55 §2, Lemmas ST, Q2, CC, DS, CERT and Theorem LC (linear coercivity of the soft chain energy at the trivial
background), d = 4, L = 3, exact arithmetic only (python `fractions` / integers; no floats in any verdict; π enters only
through the rational bounds 333/106 < π < 355/113).

Conventions (LINEAR_PACKAGE §1.1-§1.2): block B(X) = LX + {0..L-1}^4, root c_X = LX + (1,1,1,1); S4′ contour of the coarse
link (X, μ) for order σ ∈ S_4 and y ∈ B(X): complete-axial path c_X → y in the order σ, straight L steps y → y + L e_μ, then
the reversed complete-axial path c_{X+e_μ} → y + L e_μ (same σ); Q_root = average over the 24·81 = 1944 contours of the
signed path sums; Q_str = the straight legs only; h = average of the first legs; ev = evaluation at roots.

## Part A — exact identities (random integer fields, two seeds each)
- A1  Q_root = Q_str − d∘h on 1-forms (fine side 6 → coarse side 2).
- A2  d∘Q_root = Q_2∘d (same lattices).
- A3  d*∘Q_rootᵀ = evᵀ∘d* on coarse 1-forms.
- A4  Q_rootᵀ∘d* = d*∘Q_2ᵀ on coarse 2-forms.
- A5  Lemma CERT for k = 1 (sides 6 → 2) and for k = 2 (sides 18 → 6 → 2): ⟨dB_k, Ξ⟩ = ⟨dB_0, Ξ_{−1}⟩ − Σ_i⟨r_i, d*Ξ_i⟩.
PASS: every equality holds exactly. FAIL: any discrepancy.
- A-ctl (designed to FAIL): A2 with Q_2 replaced by the average over (L−1) × (L−1) squares. PASS of the control = the identity
  FAILS (the gate can fire). If the wrong identity holds, the A-gates are void.

## Part B — the norm lemmas (exact rational comparisons)
- B1  ‖Q_2F‖² ≤ ‖F‖² for 4 random integer 2-forms F (fine side 6); and ‖Q_2F‖² = ‖F‖² exactly for F ≡ 1 on all plaquettes
  of one orientation (sharpness of L^{4−d} = 1).
- B2  for 4 random co-closed level-1 forms s = d*Ξ (Ξ a random integer 2-form on the side-6 level-1 torus, k = 2 lattices):
  Q_rootᵀs = Q_strᵀs exactly, d*(Q_rootᵀs) = 0 exactly, and ‖Q_rootᵀs‖² ≤ ‖s‖²/9; and equality ‖Q_rootᵀs‖² = ‖s‖²/9 for s ≡ 1 on
  all links of one direction (a co-closed constant).
- B2-ctl (designed to FAIL the bound): for the non-co-closed s = δ_c (one coarse link), ‖Q_rootᵀδ_c‖² > 1/9. Prediction made
  before running: ≈ 0.3 (first-link weight 10/81 on each of 8 root links at each end, plus straight legs 513/6561). If it is
  ≤ 1/9 the control did not fire and that is reported.
- B3  ‖d*Ξ‖² ≤ 16‖Ξ‖² for 4 random integer 2-forms (fine side 6); equality for Ξ = dB with B the transverse staggered mode
  B(x, μ) = (−1)^{x_0+x_1+x_2+x_3}·b_μ, b = (1, −1, 0, 0).

## Part C — complete check of Theorem LC at k = 1 on the coarse torus of side 2 (fine side 6), κ_0 = 1
E_1(B_1) − c‖dB_1‖² is a translation-invariant quadratic form in the 64 coarse link values, block-diagonal in the 16 real
characters χ ∈ {±1}^4 (p ∈ {0, π}^4), with 4 × 4 blocks A_E(χ), A_F(χ). Each block is computed exactly by minimising over the
fine field in the χ-twisted sector (324 unknowns; the gauge λ with λ(root) = 0 fixed by setting an 80-link axial spanning
tree of the fundamental domain to zero; the remaining 244 × 244 system solved by exact LDLᵀ).
- C0 (control) χ ≡ 1: A_E = A_F = 0 exactly (flat coarse fields cost nothing).
- C1  for the representatives with 1, 2, 3, 4 entries χ_α = −1: A_E − (1/34)A_F is positive semidefinite (exact LDLᵀ / minors).
  PASS: all four. FAIL: any one — that would refute Theorem LC (c_co(1) = 1/34).
- C2 (designed to FAIL) at χ ≡ −1 (p = (π,π,π,π)): A_E − (1/30)A_F ⪰ 0 is predicted to FAIL (prediction from PROOF `Lemma E-low`'s
  float record c31 E: per-mode minimum 0.0310 < 1/30). If it holds, the prediction was wrong and C1 is less sharp than expected.
- C3 (covariance control): the blocks for χ = (−1, 1, 1, 1) and χ = (1, −1, 1, 1) agree after the axis permutation 0 ↔ 1
  exactly (a test of the implementation's S4′ covariance).
- Report (no gate): the exact Rayleigh quotient at χ ≡ −1 on a physical polarisation, compared with c31 E's 0.0310.

## Part D — constants (report, exact)
c_co(1) = 1/34, c_co(2) = 9/338, c_co(3) = 81/3074, c_co = 1/38 at κ ≡ 1, L = 3; c_E = 2/(π²(1 + 4π²·89/72)) enclosed by the
rational π bounds; the interval for c_co/c_E; γ^♯_i old and new (2c_1L⁻²c, c_1 = 1/(3.5·10⁶)).

Overall PASS: all of A1-A5, B1, B2, B3, C0, C1, C3 PASS and every control fires (A-ctl fails, B2-ctl exceeds 1/9, C2 fails).
A control that does not fire is reported as such and its gate is marked void, not PASS.
