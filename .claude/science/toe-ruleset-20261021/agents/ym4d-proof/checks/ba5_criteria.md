# ba5 criteria (BFT lane A, session 5). Written before checks/ba5_y.py exists (see BFT_A_LOG for the file times).

Tests the statements of BFT_A §21 (PRE-STATED, session 5). The thresholds are exactness tolerances, a-priori tolerance
factors and trend rules. No constant derived in session 5 appears here. Model: the matrix-free chain of
checks/ba2_lin / REVIEW_BFT_A_S4 (c26 axial template, L = 3, κ ≡ 1, d = 4), with general k ≤ 2.

- **P1 (Lemma PC).** 4 random compactly supported co-closed e = d^T F (F random in a cube), cube sides q ∈ {3, 5}. The
  construction 𝒫e is computed. PASS iff max|d^T G - e| ≤ 1e-12·max|e| and G = 0 outside the cube, for every case. The
  ratio Σ|G|/(qΣ|e|) is informational.
- **P2a (Lemma LD, first identity).** (k, T) ∈ {(1, 4), (2, 2)}; cutoffs r ∈ {2, 3} and r = ∞. The outputs dY_0 and r_j
  of Y^p (direct solve) equal those of g-chain + Z (data β, current d^T G'). PASS iff the max difference is
  ≤ 1e-8·max|dY^p_0|. Also, for finite r, d^T G' must vanish on the links at ℓ^∞ distance ≤ r/2 - 3 from p (to
  1e-12·max|d^T G'|).
- **P2b (Lemma LD, second identity).** Same cases: Z = Z' + x(e) in the outputs dx_0, r_j, with x(e) the response to
  the level-0 current e. PASS iff ≤ 1e-8 relative.
- **P3 (Lemma DUAL).** For each designed w of P4: |dx_0(w)(p) - ⟨w, Y^p_l⟩| ≤ 1e-8·max(|dx_0(w)(p)|, 1e-30). PASS iff
  all cases.
- **P4 (Theorem Y numerics).** D(k, T, l) := L^{2l}|⟨w*, Y^p_l⟩|/sup|w*|, with w* := P_R s(P_R Y^p_l) and s the sign
  thresholded at 1e-12·max (designed lower bound). U(k, T, l) := L^{2l}||P_R Y^p_l||_1 (upper bound over R_l).
  k = 1: T = 2..6. k = 2: T = 2, 3, 4. l = 0..k - 1. Normalised: D̂ := D/(k - l + 1).
  - **Y1:** for every l and T ∈ {2, 3, 4}: D̂(2, T, l) ≤ 2·max_{T'}D̂(1, T', 0). The factor 2 is an a-priori tolerance.
  - **Y2 (trend):** for k = 2 and each l, the increment D(2, 4, l) - D(2, 3, l) is ≤ D(2, 3, l) - D(2, 2, l) + 0.05·D(2, 2, l).
  - **Y3 (trend, partial replication):** for k = 1, l = 0, the U-increments over T = 4, 5, 6 are non-increasing
    (U(6) - U(5) ≤ U(5) - U(4) + 0.02·U(4)). The values at T = 3, 4, 6 appear in REVIEW_BFT_A_S4, so Y3 carries reduced
    weight.
- **P5 (Theorem CO-0R sup ratio).** S(k, T, l) := L^{2l}max|dx_0(w*)|/((k - l + 1)sup|w*|). **Y4:** for every l and
  T ∈ {2, 3, 4}: S(2, T, l) ≤ 2·max_{T'}S(1, T', 0).
- **B1 (bootstrap proxy; Lemma LD's error current).** k = 1, T = 12 (M = 36), r ∈ {3, 4, 6, 9}. Let q be the side of
  the smallest axial cube containing supp e. Then q·Σ|e| is strictly decreasing in r. Σ|d^T G'| and Σ|e| are
  informational.
- Resources: every part < 20 min and < 1 GB RSS (else the part is reported as not run). Lock, nice 10, threads 1.
