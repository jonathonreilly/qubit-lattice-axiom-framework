# ba2 criteria (written 2026-10-28 ≈05:44 UTC, BEFORE checks/ba2_lin.py exists; BFT_A §7, session 2 of lane A)

Purpose: (V) the exact identities of Lemma BL-1 and Proposition BL-6 (b) and the sizes of Lemma BL-2 on real-space
chains; (M) the data constants of Proposition BL-4 (the gauge-invariant components of the linear M-norm at the trivial
background) for depths k = 1..4 from the exact symbols. Part M can only fail to see growth with k; it is not a proof,
and the measured numbers are not compared with G_D (whose LES constant C_α is uncomputed).

## Part V (real space; d = 4, L = 3; the S4' root-based chain and LSMR solver of checks/c26_led.py, imported)
Direct side: minimisation of E_src by conjugate gradients on the normal equations M^TMx = M^Tb + g, with g the explicit
gradient of the source functional as defined in BFT_A §7.1 (no completing the square). Reference side: the formula of
BL-1 (LSMR, or CG when a plain current remains, at the shifted data B_k + τ_k, then x = y - τ).
Cases: (T, k, κ) = (3, 1, (1)), (2, 2, (1, 1)), (2, 2, (0.5, 2)); fixed seeds.
- **V0** every CG solve reaches relative normal-equation residual ≤ 1e-10; every LSMR solve ne ≤ 1e-8.
- **V1 (BL-1 (i))** random Gaussian data and residual-type sources at every level: max_l |r_l(x) - r_l(y) - σ_l|_∞,
  |dx_0 - dy_0|_∞ and (k = 2) |d_1x_1 - d_1y_1 + d_1τ_1|_∞, each relative to the max of the corresponding output of x,
  ≤ 1e-7.
- **V2 (BL-1 (ii) with (i))** k = 2 cases: a random co-closed level-1 current j_1 = d_1^*ψ + c (ψ a random level-1
  2-form, c a random constant 1-form) and random data: the direct solve vs the solve with the level-0 current Q_0^Tj_1 at
  data B_k + τ_k (τ from s_0 = -j_1), minus τ: gauge-invariant outputs agree to ≤ 1e-7 relative.
- **V3 (BL-6 (b))** k = 2, T = 2, κ = (1, 1) and (0.5, 2): B_k = 0, j_1 := Q_1^T(c e_1), c = 0.37:
  |r_1(x) - (c/κ_1)e_1|_∞ ≤ 1e-8, |r_0(x)|_∞ ≤ 1e-8, |d_0x_0|_∞ ≤ 1e-8.
- **V4 (BL-2)** at k = 2, T = 2: coarse-unit row norms L^{-(b-a)}·max_row ℓ¹(Q^{(a→b)}) ≤ 5 for (a, b) ∈ {(0, 1),
  (1, 2), (0, 2)}; Q_l(constant e_μ) = L·(constant e_μ) to 1e-13; for 20 random co-closed level-1 currents j,
  L³||Q_0^Tj||_∞/||j||_∞ ≤ 1 + 1e-12 and ||d_0^*Q_0^Tj||_∞ ≤ 1e-12·||j||_∞.

## Part M (exact symbols; d = 4, L = 3, coarse torus T = 16; P_symbol, r_from_b, Phi_f of checks/c26_led.py, imported;
validated there by c26 Q1/Q4)
- N_r(k) := ||B_k ↦ r_{k-1}||_{∞→∞}: max over the 4 output components of the sum over the 4 data components and all
  coarse sites of |kernel|. k = 1..4; κ ≡ 1, 0.25, 4.
- N_f(k) := max over the computed fine offsets u and the 6 planes of ||B_k ↦ f_0(n·+u)||_{∞→∞}. Offsets: κ = 1, the two
  lines below; κ = 0.25, 4: corner, centre and 3 fixed pseudo-random offsets.
- H_f(k, α) := max over the 6 planes and over pairs 0 ≤ t < t' ≤ n on a line of ||K_t - K_t'||_1/((t' - t)/n)^α, K_t
  the B_k ↦ f_0 kernel at offset u(t); line A: u(t) = (t, 0, 0, 0); line B: u(t) = (t, c, c, c), c = (n - 1)/2;
  t = n is the next coarse site (computed directly from the Bloch formula; its agreement with the shifted t = 0 kernel
  is printed as a sanity value, informational). α ∈ {0.25, 0.5}, κ = 1. This is a lower bound for the operator norm of
  B_k ↦ [f_0]^∞_α restricted to pairs along e_1.
Pre-registered:
- **Q1** for each κ: max_{k∈{2,3,4}}N_r(k) ≤ 1.10·min_{k∈{2,3,4}}N_r(k).
- **Q2** for each κ: max_{k∈{2,3,4}}N_f(k) ≤ 1.25·min_{k∈{2,3,4}}N_f(k).
- **Q3** for α ∈ {0.25, 0.5}: H_f(4, α) ≤ 1.25·max(H_f(2, α), H_f(3, α)).
- **I1** (informational) N_f and H_f at T = 12, k = 3, line A, κ = 1, against T = 16.
- **I2** (informational, analytic, no numerics of the chain) the lower bounds of BL-5 (c) (necessity, its first term) and
  BL-6 (b) (F3 slot) tabulated for k = 1..8 at (α, θ) = (0.5, 0.25), (0.25, 0.5), (0.5, 0.5).

## Run discipline
One run (Part V then Part M, sequential processes) under the numeric lock (mkdir lock, load < 8, memory ≥ 30% free);
nice 10; OMP/OPENBLAS/MKL/VECLIB thread variables 1; python3 without -I (imports c26_led from this directory); no
timeout; target < 20 min wall, peak RSS < 1 GB. Outputs checks/ba2_outV.txt, checks/ba2_outM.txt; times in
checks/ba2_time.txt. A FAIL is recorded as written; the criteria are not edited after the script exists.
