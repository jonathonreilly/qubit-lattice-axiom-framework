# w1 criteria (written 2026-10-28 02:02:25 UTC, after HW.md §2-§7 and BEFORE checks/w1_kernel_moments.py exists)

Purpose: numerical sanity checks of the elementary inequalities and counts that HW.md makes load-bearing. Informational;
never a proof. One run under the numeric lock, nice 10, BLAS threads 1. Every result is reported, including failures.

## A. Lemma KS (SU(2)) — load-bearing for (M-i), KS-chain, H4-red
- A1. g(b) := b·E_b[1 - cos α], density ∝ e^{-b(1-cos α)} sin²α on [0, π], computed two ways: (i) direct quadrature in α;
  (ii) Bessel form E_b[w] = 1 - I_2(b)/I_1(b) (from 𝒩(b) = 2e^{-b}I_1(b)/b). Grid b ∈ logspace(-4, 7, 400).
  PASS iff max_b g(b) ≤ 1.5 + 1e-9 by both methods, the two methods agree to 1e-7 (absolute, on g) where quadrature is used
  (b ≤ 1e4), and g(1e7) ≥ 1.4999 (sharpness of 3/2).
- A2. R(b, λ) := 𝒩((1-λ)b)/𝒩(b) ≤ (1-λ)^{-3/2}·(1 + 1e-12) for all b in the grid and λ ∈ {0.05, 0.1, …, 0.95, 0.99}. PASS iff it holds.
- A3. Negative control: the FALSE claim R(b, λ) ≤ (1-λ)^{-1} must fail somewhere on the grid. PASS iff it fails (discriminates).
- A4. Monte Carlo, Haar SU(2) (uniform unit quaternions), 2·10⁵ samples, fixed seed: (a) for 200 random M = rŴ (r ∈ (0, 1]),
  φ_M(V) := ½[Re tr(W_0⁻¹M) - Re tr(V⁻¹M)] with W_0 = Ŵ equals r·||V - Ŵ||²_op/2 to 1e-12 on 1000 V each; (b) no random W (10⁴)
  gives Re tr(W⁻¹M) > Re tr(Ŵ⁻¹M) + 1e-12; (c) MC estimate of 𝒩(b) = E_Haar[e^{-b(1-cos α)}] agrees with the Bessel form within
  4 standard errors at b ∈ {0.5, 2, 8, 32}. PASS iff (a), (b), (c) all hold.

## B. (KS-N), scalar case, SU(3) — informational (I), not a pass/fail item
- g_3(b) := b·E_b[1 - Re tr X/3] under Haar SU(3) by the Weyl integration formula (θ_3 = -θ_1 - θ_2), b ∈ logspace(-3, 4, 60).
  Report max_b g_3(b), g_3 at the largest b, and compare with D/2 = 4. I-PASS (informational) iff max ≤ 4 + 1e-3.

## C. Counts — load-bearing constants of Lemma TE (iii), W-bad, DJ, K3-a (d = 4, L = 3)
- C1. In a cube of L⁴ sites: n_int = 216 links with both endpoints in the cube; every such link lies in ≤ 2(d-1) = 6 plaquettes
  with all four vertices in the cube (and some link in exactly 6). PASS iff both.
- C2. A site is a corner of exactly 24 plaquettes (HIST §15.1 overlap). PASS iff 24.
- C3. On a 9⁴ torus of cubes: a cube lies in N_1(Q) for exactly 81 cubes Q; |N_1(A)| ≤ 81|A| for 50 random *-connected A
  (n ≤ 60). PASS iff both.

Overall: PASS iff A1-A4 and C1-C3 PASS. B is reported only.
