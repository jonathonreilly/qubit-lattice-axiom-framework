# s7 criteria (lane F session 7; written BEFORE checks/s7_sf.py exists; no constant derived in session 7 appears here)

Scope: PROOF's level-0 trivial-background operator Õ_0 (Setting N5-bg at (U, V) = (1, 1), κ_0 = 1, d = 4, L = 3; scalar, Õ(1, 1) = Õ_0 ⊗ 1).
Method parameters (choices made after the logged exploratory scratch runs sf7/ex1, sf7/ex2; they are not results): torus n = 12 blocks for
the float inverse; support of K̃ = the links whose midpoint lies within ℓ^∞ distance 3R + 3/2 (fine units) of the block-0 centre, R = 5;
K̃ defined by 8-or-fewer canonical columns (one per hyperoctahedral orbit of link types), made exactly Stab-invariant; weights e^{m d}
with d the midpoint ℓ¹ distance, m in the grid {0, 0.005, 0.01, 0.02, 0.03}. Rounding: Higham γ_n, upward rounding, inputs exact.

Known inputs quoted from PROOF (not derived here): N_0(|Õ_0|) = 10462237/410670 (N5-w0, c36 C); γ_0 = 1/(3.5·10⁶)·(1/2)/9 (N5-sf0);
ν_w = 30/13; K_FP ≤ 514.5; p_L = 11; r_1 = 20; PROOF's 𝔠_∞ ≈ 2.0·10³⁷; SF's τ^A, ε_bg^{(TH-bg)}, ρ_band, r_sol columns of §19.2.

## Part A (exact rational arithmetic)
- A1 PASS iff the exact rows of Õ_0 (324 link types) are supported in the 3⁴ blocks around their block, are exactly symmetric, and
  max row abs sum = 10462237/410670 exactly (reproduces PROOF N5-w0).
- A2 PASS iff the hyperoctahedral covariance A(gZ) = P_gA(Z)P_g^T holds with ZERO mismatches (exact Fractions) for Õ_0 and for 1 - Π
  under the three generators (axis transposition, 4-cycle, reflection through the block centre).
- A2n (negative control) PASS iff a reflection through a plane NOT through the block centre (x_1 ↦ -x_1) gives > 0 mismatches.
- A3 PASS iff the orbits of the 324 link types under the group partition them (sizes sum to 324) and each canonical column's
  support set is invariant (asserted inside the canonicalisation).
- A4 (report) q := N_0(|ΠQ^TQΠ|) exactly (rows at κ = 1 minus rows at κ = 0), for the κ-window.

## Part B (the certificate, Proposition CI-0 / CI-bg)
- B1 (evidential) PASS iff on the support the canonicalised K̃ differs from the float torus column by ≤ 1e-12 (max entry), for every
  canonical column.
- B2 (proof input) PASS iff the certified e_0 ≥ N_0(|E|) satisfies e_0 < 1. Reported: k_0, k′_0, e_0, and e_m, k_m, k′_m on the m grid.
  The certified quantities are upper bounds: |E| ≤ |fl(E)| + (γ_n + 2u)(1 + γ_n)·e^{mD_A}·Σ_j a_ij v_j^m (+ the u-term of the identity
  entry), all sums rounded upward; row sums assembled from the canonical columns by exact covariance.
- B2x (validation of the rounding model, incl. BLAS) PASS iff for ≥ 40 entries per sampled column (the largest |fl E| and random
  ones), the exact rational E (exact Õ_0 rows times the exact dyadic K̃) satisfies |E_exact - fl(E)| ≤ the entry's rounding radius.
- B3 (proof input) PASS iff e_0 + δk_0 < 1 with δ := γ_0/2 (CI-bg on 𝔑(α_*)).
- B4 (consistency) PASS iff (a) the float estimate of N_0(|G_12|) (full torus inverse, row sums assembled by covariance) is ≤ the
  certified k_0/(1 - e_0); and (b) the float λ_min of the torus symbol at K = (π, π, π, π) (n = 12 grid) is ≥ the certified
  (1 - e_0)/k_0.
- B5n (negative control) PASS iff truncating the same canonical column at R = 2 gives a strictly larger residual column total than
  at R = 5 (the truncation is load-bearing).
- Pre-registered target (owner): 𝔠_∞^♯ ≤ 10³; recorded as MET or NOT MET (not a PASS criterion).

## Part C (arithmetic, mpmath / Fractions; PASS iff computed and finite, and the stated inequalities hold)
- C1 𝔠_∞^♯ = k′_0 + δ + k_0(e_0 + δk_0)/(1 - e_0 - δk_0); certified λ_min ≥ (1 - e_0 - δk_0)/k_0; the largest grid m with e_m + e^{mr_1}δk_m < 1,
  converted to the base-point metric by the factor e^m; the κ-window |κ - 1| ≤ (1 - e_0 - δk_0)/(2qk_0).
- C2 CHEB-f: with a := certified λ_min, b := 10462237/410670 + δ: ρ_0 = σ + √(σ² - 1), and for f = x^{1/2} at a chosen ρ < ρ_0 and μ <
  ln ρ/12 the explicit bound for N_μ(|Õ^{1/2}|); for f = x^{-1/2} the analogous bound for N_μ(|Õ^{-1/2}|).
- C3 BR1 with 𝔠_∞^♯: C_bg, the five ε_br entries (C_♭, C_Δ, r_♭ symbolic), (TH-ch″)'s ε_1 ceiling at τ^A (and τ^♯ for the record).
- C4 (proposed PROOF edit) N5-sf0's chain re-evaluated with the certified λ_min(Õ_0) in place of γ_0 (m from N5-w0's exact first
  moment, R_* from ε_R ≤ ½, ε_* in units of 1/C_Δ); reproduces PROOF's ε_* ≈ 1.7·10⁻²⁴/C_Δ when γ_0 is input (control).
- C5 DX′-1's ceiling recomputed (τ^A column; N_r, C_Ω symbolic, reported at N_r = 1) with ||C|| ≤ 1/λ_min and the CHEB-f rate; and
  the old value 1.49·10⁻²³⁷ reproduced from the session-5 inputs (control).
- C6 the STEP-1 (TH-2) table: 1/(24𝔠_∞²) at 𝔠_∞ = 2.0·10³⁷, /(1.011√3), and the §19.4 ε_1-driven rows by their scalings.

## Resources
- R1 PASS iff wall time < 20 min and peak RSS < 1 GB, under the numeric lock (one rmdir), nice 10, BLAS threads 1.
