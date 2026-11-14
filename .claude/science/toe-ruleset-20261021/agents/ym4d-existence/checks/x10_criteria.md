# x10 criteria (written 2026-10-28 04:27:55 UTC (mtime), after EXISTENCE §20.0 and before any x10 script)

Purpose: T33's null-model question. Does the odd, f^{abc}-carrying corner cumulant
  O := tr(Y_12[Y_23, Y_31]),  Y_μν := principal log of the plaquette U_μ(0)U_ν(e_μ)U_μ(e_ν)^{-1}U_ν(0)^{-1}
vanish for centred Gaussian gauge fields? (It is real for anti-Hermitian Y's.) Basis: T^a with tr(T^aT^b) = -½δ^{ab}
(SU(2): -iσ_a/2; SU(3): -iλ_a/2). Gaussian links: A_b = Σ_a x_{b,a}T^a, U_b = exp(A_b).

By-hand prediction (exploratory, before this file): for i.i.d. links with E[x_{b,a}x_{b',a'}] = σ²δ_{bb'}δ_{aa'},
  E[O] = c_4σ⁴ + O(σ⁶),  c_4 = ¾N(N² - 1)  (SU(2): 4.5; SU(3): 18),
coming only from the BCH commutator terms of the plaquette logs (path ordering); odd orders vanish by x ↦ -x.

A (load-bearing for the claim "a centred Gaussian connection gives O ≠ 0 at order σ⁴"). Monte Carlo with exact matrix
  exponentials and principal logs, σ ∈ {0.10, 0.15, 0.20, 0.25, 0.30}, n = 2·10⁶ samples per σ (chunks), SU(2) and SU(3);
  fixed seeds. Fit E[O]/σ⁴ = c_4 + c_6σ² by weighted least squares.
  - A1 PASS iff, for both N, the fitted c_4 is within 3 SE + 2% of ¾N(N² - 1).
  - A2 PASS iff E[O]/σ⁴ > 0 by more than 3 SE at every σ, for both N.
B0 (exact formula check). The general order-σ⁴ Wick formula
  c_4[Γ] = K Σ_cyc Σ_{i<j} ½s_is_j[γ(ℓ_i, L_Q)γ(ℓ_j, L_R) - γ(ℓ_i, L_R)γ(ℓ_j, L_Q)],  K = -½N(N² - 1),
  (Γ the link covariance in units of σ²; L_Q the signed link sum of plaquette Q) evaluated at Γ = identity.
  PASS iff it equals ¾N(N² - 1) to 1e-12.
B (informational). c_4[Γ_F] for the Feynman-gauge lattice Maxwell link covariance Γ_F((x,μ),(y,ν)) = δ_μνG_T(x - y),
  G_T(r) = T^{-4}Σ_{k≠0}e^{ik·r}/k̂², on T = 16, 24, 32. Report value, sign and T-convergence. No pass/fail.
C (control). The same Monte Carlo with Y replaced by the linear signed link sum L_μν (the abelianised plaquette log):
  PASS iff |mean O_lin|/σ⁴ ≤ 4 SE at every σ, both N.

Run rules: numeric lock (mkdir/rmdir once, no trap), nice 10, BLAS threads 1, python3 without -I, no `timeout`,
load < 8 at start, chunks so that peak memory < 600 MB. Output checks/x10_out.txt, record checks/x10_time.txt.
Load-bearing: A1, A2 (with C as control) only. B is informational.
