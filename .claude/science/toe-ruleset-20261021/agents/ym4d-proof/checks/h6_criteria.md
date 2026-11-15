# h6 criteria (lane D session 3; written BEFORE checks/h6_msg_cone.py exists; not to be edited after the script is written)

Setting: SU(2) (N = 2), L = 3, κ = 1, S4' with the 4! (d = 4) or 2! (d = 2) order pairing, SU(2) maximiser
W_0(M) = M/sqrt(det M) (exact for non-negative combinations of SU(2) elements), open boxes (the cone W_P^{(i)} of HIST §15.1:
2L^{k-i} × 2L^{k-i} × L^{k-i} × L^{k-i} level-i sites in d = 4; 2L^{k-i} × 2L^{k-i} in d = 2), P the level-k plaquette in the
(0,1) plane at the origin. Chains are generated bottom-up: U_0 = exp(a_0) on the level-0 box, U_{i+1}(c) := W_0(M̄_c(U_i))·exp(t r_c)
for every level-(i+1) link c with both endpoints in W_P^{(i+1)}. E_𝒞(P) := Σ s(U_0(p)) over all level-0 plaquettes of the box +
κΣ φ over all cone kernel terms (levels 1..k). Norms: HS for logs in ratios, op for MSG sizes. Lie components: X = (i/2)Σa_jσ_j.

## A (d = 4, depth k = 2): non-abelian cone ratio
Families (t ∈ {0.0025, 0.005, 0.01, 0.02, 0.04}):
- A-smooth (seeds 1-3): a_0 = t·H, H a smooth non-abelian lowest-mode field over the box (components O(1)); r ≡ 0.
- A-noise (seeds 4-6): a_0 = t·(iid standard normal components); r iid standard normal at levels 1 and 2.
- A-res (seeds 7-9): a_0 = 0; r iid standard normal at levels 1 and 2.
- A-coh (one sample): a_0 = 0; r = 0 at level 1; on P's four links r = (+v, +v, -v, -v) in the order (c1, c2, c3, c4) of
  U_P = U(c1)U(c2)U(c3)^{-1}U(c4)^{-1}, v = (1, 0, 0), r = 0 on the other level-2 links (there are none in the cone).
R_NA := |log U_2(P)|²_HS / E_𝒞(P). R_lin := |dB_2(P)|²_HS / E^lin, with the abelian chain B_0 = a_0, B_{i+1} = Q_root B_i + t r
(Q_root the abelian S4' contour average on the same contours) and E^lin := Σ|dB_0|²_HS/(2N) + κΣ|t r|²_HS/(2N).
- **A1** R_NA ≤ N·C_loc = 80 for every sample and t.
- **A2** |R_NA/R_lin - 1| ≤ 0.05 at t = 0.0025 for every sample.
- **A3** per sample, D(t) := |R_NA/R_lin - 1|: if D(0.0025) < 1e-7 the sample is reported "below floor" (counted as consistent);
  otherwise the least-squares slope of log D against log t on t ∈ {0.005, 0.01, 0.02, 0.04} (the smallest t excluded, rounding
  lesson of h5 B3) lies in [0.7, 2.3].
- A4 (info) max R_NA and R_lin per family.

## B (d = 4, depth 2): the MSG gauge
Built exactly as HIST §19 Target S4's route: complete axial gauge (coordinate order 0,1,2,3, root at the box origin) on the
level-1 box; then V := exp(I a_1) with I the clamped lowest-order cubical Whitney interpolation, and level-0 gauge
h(x) = hol_U(γ_x)^† h_1(X) hol_V(γ_x), γ_x the axial path (order 0,1,2,3) from the block centre c_X to x inside block X.
ε := max of (i) ||1 - U_i(p)||_op over cone plaquettes at levels 0, 1 and (ii) ||U_{i+1}(c) - W_0(M̄_c)||_op at levels 1, 2.
Applied to every A sample at every t.
- **B1** gauge invariance: every plaquette s at levels 0, 1, 2 and every kernel φ unchanged by the MSG gauge to ≤ 1e-11.
- **B2** hol_V(S_c) = exp(a_c) to ≤ 1e-12 (op) for every level-1 cone link c; max_b|Ia(b)|_op ≤ (1 + 1e-12)·max_c|a_c|_op/L.
- **B3** C_meas := max over levels 0, 1, 2 and cone links of |log U_i^g(b)|_op / ε ≤ 450 (a loose a-priori bound that the proof's
  constants must respect).
- B4 (info) per level the ratio max|log U_i^g|_op/ε; and max|log U_0^g| against max|log U_1^g|/L.

## C (d = 2, depths k = 1..5): depth-uniformity of the MSG constant
Families per depth: C-noise (seeds 11, 12): a_0 = t·iid normal, r iid normal at all levels, t = 0.01. C-smooth (seeds 13, 14):
a_0 = (0.3/S)·H(x/S), H smooth non-abelian lowest modes on the level-0 box of side S, r ≡ 0. MSG gauge as in B (top level k - 1
axial, order (0,1); interpolation steps for i = k - 2, …, 0). For k = 1 the gauge is the axial gauge on the level-0 box.
- **C1** C_meas(k) ≤ 450 for every sample and depth.
- **C2** depth-uniformity: max over samples of C_meas at k = 5 ≤ 1.5·(max over samples at k = 2) + 0.5.
- **C3** contrast: for C-noise, C_ax(k) := max|log U_0|_op/ε in complete axial gauge on the whole level-0 box; C_ax(5)/C_meas(5) ≥ 2
  (both seeds).
- C4 (info) the table C_meas(k), C_ax(k), ε(k).

OVERALL PASS iff A1-A3, B1-B3, C1-C3 all PASS. Resources: numeric lock, nice 10, BLAS/OMP threads 1, load < 8, ≥ 25% free memory,
peak RSS < 1 GB (A/B processed in chunks), python3 without -I, no `timeout`.
