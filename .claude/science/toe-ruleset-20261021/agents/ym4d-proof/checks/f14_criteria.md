# f14 criteria (lane C, session 11; written before any f14 script)

Pre-statement: FLOW.md §84 (U1)-(U7) and its "Check f14" paragraph. This file fixes the computations, thresholds and
verdict lines before any f14 script exists. No number computed in session 11 appears here. Reference values are closed
forms (L = 3, s = 4, c_g = 1/(96π²), log L/(8π²) = 1.3914e-2) or session-9/10 functions (checks/f12_proxy_2pt.py, executed
unchanged, md5 printed).

Run conditions: one NUMERIC LOCK acquisition per official run, released once with rmdir (no trap); nice 10; all BLAS
threads = 1; plain python3; no `timeout`; load < 8 and memory free ≥ 35% checked inside the lock before starting; job
< 20 min, peak RSS < 1 GB (measured by /usr/bin/time -l). A run that starts outside these conditions is VOID and is
re-run, and the void output is set aside unused.

Conventions: level grid = half-shifted grid 2π(i + ½)/N in each direction (the antiperiodic torus of §74 (1), §75 (a));
P = 2πj/N in direction 2 (a grid momentum); fibre (alias) sums over m ∈ (Z/ℓ)⁴ by the f12 proper-time factorisation (the
Fibre class), with direction-2 kernels g_ab(T; A, B), ∫_0^∞dT e^{-Tx}g_ab = (A + x)^{-a}(B + x)^{-b}, extended to a + b ≤ 4 by
the Feynman-parameter formula (Kummer-type integral evaluated by its power series for z < 2 and by lower incomplete gamma
functions otherwise); the extension must reproduce f12's g_11, g_21, g_12 to ≤ 1e-12 relative on the run's arguments
(verdict line X0).

## Part A: b_n, w_n of FLOW §75 (REVIEW_FLOW_S10 S10-4)
b_n, w_n, γ_n are implemented FROM THE TEXT of §75 (level-unit dictionary d, λ̃, σ, ŵ, ũ, ũ^-, ũ^{(−)}, m̃, c_n, c_2; the
K − P intermediate term on the fibre K − P), with the form-factor functions G_κ, F2_i, δ_r, D_1 and c_level, c2_vertex of
f12 (unchanged). T_n − I_n from f12's `integrand` (unchanged).
- A1 (the finite-torus identity), n = 1, 2, 3, 4, N = 8, j ∈ {1, 2}: with
  LHS := mean_K ℓ^{-4}(T_n − I_n), R1 := mean_K ℓ^{-4}Σ_m(W_m/λ_m − Σ_m²/(λ_mλ'_m)), R2 := ℓ^{-2}mean_K[w_n/γ_n − b_n²/(γ_nγ_n(K + P))],
  |LHS − R1 − R2| ≤ 1e-10·(|LHS| + |R1| + |R2|). Eight verdict lines.
- A2 (Ward identities at P = 0), n = 1, 2, 3, at the four level momenta K = (0.7, 0.4, 0.3, 0.2), (1.9, −0.8, 0.5, 1.1),
  (−2.6, 1.3, −0.4, 0.9), (0.35, 2.2, 1.7, −1.2): |b_n(K; 0) − ∂_1γ_n(K)| ≤ 1e-7·max(|∂_1γ_n(K)|, 1e-3) and
  |w_n(K; 0) − ∂_1²γ_n(K)| ≤ 1e-7·max(|∂_1²γ_n(K)|, 1e-3), with ∂_1 by the five-point central difference in K_1, step 2e-3
  (step-halving change reported). Six verdict lines (max over the four K).
- A3 (control): the A1 computation at n = 2, j = 1 with the sign of the d'ũ^-/λ̃' term of b_n flipped must FAIL the A1
  tolerance by a factor ≥ 1e4 (relative defect ≥ 1e-6). One verdict line.

## Part B: Proposition G2-log (U2) and Proposition SP-div (U7)
- B1 (log slope): ḡ_n(K) := g2_n(K) − λ̃_n(K)^{-2}, g2_n(K) = ℓ^{-4}Σ_mλ(k_m)^{-2} (fine units = level units), at
  K_a = (0.7, 0.4, 0.3, 0.2) and K_b = (2.1, −1.3, 0.9, 2.8), n = 1..7. Prediction: |(ḡ_n − ḡ_{n−1})/(log L/(8π²)) − 1| ≤ 0.05
  for n = 4, 5, 6, 7 at both K. Eight verdict lines. Step control: proper-time step h_u = 0.3 vs 0.15 changes ḡ_n by
  ≤ 1e-9 relative (one verdict line, max over n and K).
- B2 (U2 inequality, straight-path map, U = 1, 𝒞 omitted (𝒞 ≥ 0 only adds)): the level symbol x_n(K)_{μν} =
  δ_{μν}ℓ^{-4}Σ_m|S_μ(k_m)|²/λ(k_m), S_μ(k) := Σ_{j<ℓ}e^{ik_μj}; at K_a, K_b and n = 1..4: Σ_μ|D̂_ℓμ|²x_{n,μμ} − |D̂_ℓ|⁴g2_n ≥
  −1e-10·Σ_μ|D̂_ℓμ|²x_{n,μμ} (D̂_ℓμ(K) = 1 − e^{iK_μ}). One verdict line (min over n, K).
- B3 (SP-div): ρ_n := x_{n,11}(K_a)/x_{n−1,11}(K_a), n = 2..6. Prediction: |ρ_n/L − 1| ≤ 0.10 for n = 3, 4, 5, 6. Four
  verdict lines. Reported: x_{n,11}(K_a), and the same at K_b.

## Part C: the mechanism behind (U4), scalar model P_n(U) := −log det Δ_U − ½log det G2_U
Level part: y_n(P) := [ε̃²]τ_n log G2_U/(P²/2) = (2/P²)mean_K[g2^{(2)}/g2 − ¼b2²/(g2·g2(K + P))] (level units), with, in fine
units on the fibre (Σ_m = 2 sin k_{m,1}, W_m = 2cos k_{m,1}, λ_± = λ(k_m ± pe_2)):
  g2 = ℓ^{-4}Σ_mλ_m^{-2},  b2_fine = −ℓ^{-4}Σ_mΣ_m[λ_m^{-2}λ_+^{-1} + λ_m^{-1}λ_+^{-2}]  (b2 = b2_fine/ℓ),
  g2^{(2)}_fine = ℓ^{-4}Σ_m{¼Σ_m²Σ_±[2λ_m^{-3}λ_±^{-1} + λ_m^{-2}λ_±^{-2}] − ½W_mλ_m^{-3}}  (g2^{(2)} = g2^{(2)}_fine/ℓ²)
(the ϑ-free ε² coefficient of ι^*Δ_U^{-2}ι with Δ_U = Δ + a·2sin k_1 + a²cos k_1 + …, a = ε cos(px_2 + ϑ)).
- C1 (brute force, S11-F4), n = 1: fine torus 12 × 24 × 3 × 3, antiperiodic in all directions, U_{x,1} = exp(iε cos(px_2 + ϑ)),
  ϑ = 0.3, p = 2πj/24, j ∈ {1, 2} (P = π/4, π/2); G2 = ι^*Δ_U^{-2}ι on the 32 level sites (sparse LU); [ε²] per level site by the
  symmetric second difference at ε = 0.02, 0.01 with one Richardson step; against the Riemann sum of the formula on the level
  grid 4 × 8 × 1 × 1: relative difference ≤ 1e-6. Two verdict lines.
- C2 (classification, S11-F3), n = 1..6, P ∈ {π/4, π/2}, N = 16 (P = 2πj/16, j = 2, 4): D_n(P) := y_n(P) − y_{n−1}(P),
  ratios r_n(P) := |D_n(P)/D_{n−1}(P)|, n = 3..6.
  - Step control: N = 24 (j = 3, 6) vs N = 16 changes D_n(P) by ≤ 0.1|D_n(P)| for n = 5, 6, both P. Four verdict lines.
    (If any fails, the classification below is reported as unresolved.)
  - Classification line (one verdict line, "slow" prediction): PASS iff r_6(P) ≥ 0.5 at both P (slow, non-geometric);
    reported verbatim also whether r_5, r_6 ≤ 0.2 at both P (geometric).
  - Reported: y_n(P), y_n(P) + 4c_g log(1/P), D_n(P), r_n(P), and ḡ_n at K_a for comparison.

## Output
Every verdict line is "[PASS]" or "[FAIL]" with the measured number and its threshold. Total line: number of PASS / total.
