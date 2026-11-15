# bb7g criteria (lane B session 7; written after BFT_B §21 and Step 1, before checks/bb7g_n1g.py exists)

Purpose: checks/ reproduction of Lemma N1G (REVIEW_BFT_B_S6 D.4; RS6-6). Exact discrete Fourier inversion (FFT) of the mean-zero
Green function G_M of -Δ (nearest-neighbour, 4D torus of side M); ∇_1G(y) := G(y + e_1) - G(y). Thresholds are floating-point
precision; the predicted values are the reviewer's closed forms (no session-7 constant).
- G1 (M even ∈ {8, 12, 16, 24, 32, 48}): |Σ_y|∇_1G_M(y)| - M/4| ≤ 1e-8·M. PASS required.
- G2 (M odd ∈ {9, 15}): |Σ_y|∇_1G_M(y)| - (M² - 1)/(4M)| ≤ 1e-8·M (hence < M/4). PASS required.
- G3 cycle heat kernel q_t(x) = M^{-1}Σ_ξ e^{-t(2 - 2cos ξ)}cos(ξx) (exact eigen-sum), M ∈ {8, 9, 16, 32, 48},
  t ∈ {0.1, 0.5, 1, 4, 16, 64, M²}: max_{0≤x<⌊M/2⌋}(q_t(x + 1) - q_t(x)) ≤ 1e-14·max q_t. PASS required.
- G4 monotonicity: for M ∈ {8, 16}, for every y' the map y_1 ↦ G_M(y_1, y') is symmetric and non-increasing in |y_1|
  (y_1 ∈ [0, M/2]): max violation ≤ 1e-12·max|G_M|. PASS required.
- G5 transverse sum: g(y_1) := Σ_{y'}G_M(y_1, y') equals -|y_1|/2 + y_1²/(2M) + c (c fixed by mean zero), M ∈ {8, 16, 32}:
  max deviation ≤ 1e-10. PASS required.
- G6 informational: max_y |y|³|∇_1G_M(y)| (|y| the Euclidean torus distance) for each even M.
Resources: rfftn on M = 48 (5.3·10⁶ sites), float64; expected peak < 1 GB.
