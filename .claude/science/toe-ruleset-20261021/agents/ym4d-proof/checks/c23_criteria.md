# c23 criteria (written 2026-10-27 BEFORE checks/c23_n2_residual.py; RTARGET §16)

Purpose: test Lemma N2-a (gauge-orbit / flat ⇒ zero residual), the Whitney test-configuration bound of N2-b, and the
field-size question of REVIEW_S9_S10, numerically. Jobs run sequentially, nice 10, BLAS threads 1, peak < 2 GB.

## Part A: abelian linearised soft chain (Setting SC), κ_i = 1
Geometry: S4' root-based linearised map Q (all d! orders, all y in the block), L = 3, roots at block centres, levels
nested. d = 2: coarse torus side T = 9, k = 1, 2, 3, 4. d = 4: c22 geometry (9^4 fine, 3^4 coarse), k = 1.
Minimisation: sparse least squares (LSMR, atol = btol = 1e-14) of the stacked chain residual vector.
Data: (R) a random coarse 1-form B_k (seeded); (S) a smooth low-mode B_k; (G) B_k = (R) + dλ + c with λ a random coarse
scalar of size 50 and c a constant 1-form of size 10; (Z) B_k = dλ + c (closed).
- **V1 (validity).** LSMR converged (its stop flag 1 or 2) for every solve, and the normal-equation residual
  ||M^T(Mx - b)|| ≤ 1e-6 ||M^T b|| for data (R), (S), (G).
- **V2 (validity: Whitney test configuration).** For every k and data: R_k W B_k = B_k to 1e-12 (relative), and the
  minimum E_k ≤ E_W (the explicit test energy) × (1 + 1e-8).
- **Q1 (N2-a, gauge orbit).** For every k: max|r_{k-1}(G) - r_{k-1}(R)| ≤ 1e-6 max|r_{k-1}(R)|, the same for the fine
  curvature dB_0, and |E_k(G) - E_k(R)| ≤ 1e-6 E_k(R).
- **Q2 (N2-a, closed data).** E_k(Z) ≤ 1e-12 ||B_k(Z)||² for every k.
- **Q3 (N2-b, no growth in k; d = 2).** max_k E_W/||dB_k||² ≤ 1.5 × (E_W/||dB_k||² at k = 2), and the same for the
  true minimum E_k, for data (R) and (S).
- **I1 (informational).** sup|r_{k-1}| / sup|dB_k| and the coarse-normalised sup|f_0| / sup|dB_k| vs k (data R).
- **I2 (informational, for N2-c).** Response to curvature localised at one coarse link (B_k = indicator of that link):
  the chain energy per coarse cell vs coarse distance r; a log-linear fit of the decay rate m_k over 2 ≤ r ≤ 4 for each
  k. Expectation stated in advance: m_k roughly k-independent (m_4 ≥ 0.5 m_2). Not a pass/fail criterion.

## Part B: SU(2), d = 4, one soft step (c22 machinery unchanged: 9^4 fine, L = 3, κ = 1, same minimiser and tolerance)
Data, with Xc = c22's coarse field and t = 0.1:
- (B0) V = exp(t Xc);
- (B1) V' = h_X V h_Y^{-1}, h a Haar-random coarse gauge transformation (a large pure gauge);
- (B2) V'' = D V, D a constant flat diagonal field, D_μ = exp(θ_μ σ_3-direction) with θ = (0.9, 0.7, 0.5, 0.3) (half-angle
  parametrisation of c22), so the field size max|log V''| ≈ 0.9 ≫ t;
- (B3) V = D alone (flat, non-trivial holonomy).
Each run starts from c22's start_config(V) (the gauge-naive lift). Measured: R_top := max_c |log(V_c^{-1} polar M̄_c)|,
the mean residual, the coarse curvature C := max_P |log V_P| (coarse plaquettes), the field size Φ := max_c |log V_c|,
and the plaquette sup S of c22.
- **V3 (validity).** Every run converged (|g|/|g0| ≤ 1e-7) within 6000 iterations.
- **Q4 (orbit).** |E(B1) - E(B0)| ≤ 1e-4 E(B0) and |R_top(B1)/R_top(B0) - 1| ≤ 0.05. (A FAIL with a higher energy means
  the gauge-naive start reached a different local minimum; that does not test the lemma, which is about global
  minimisers, and is recorded as such.)
- **Q5 (field size vs curvature).** R_top(B2)/R_top(B0) ≤ 2 C(B2)/C(B0), and R_top(B2)/R_top(B0) ≤ 0.5 Φ(B2)/Φ(B0).
- **Q6 (flat).** E(B3) ≤ 1e-8 and R_top(B3) ≤ 1e-4 (the same local-minimum caveat as Q4).
