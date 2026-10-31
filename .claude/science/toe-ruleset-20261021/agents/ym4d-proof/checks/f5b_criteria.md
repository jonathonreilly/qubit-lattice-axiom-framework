# f5b criteria (written 2026-10-28 00:01 UTC [file mtime], while f5's scan was running, before checks/f5b_quad.py)

Why f5b. f5's pre-registered quadrature line (C) FAILED (c_Γ(5, 1): n_P = 6 vs 10 differ by 6.3e-5, 2%) and its
k-step line (D) FAILED (h = 1e-3 vs 2e-3 differ by 7e-6 relative > 1e-6). At the time of writing, f5 had printed the
validation lines and the ℓ = 3, 5, 7 rows of its scan; its (E), (F), (G) outcomes were not yet known. Diagnosis: the
class integrand is periodic and analytic in the coarse momentum P but its nearest complex singularity approaches the
real cell near P = 0 (the kernel-regularised K = 0 alias), at a distance ~ 0.3-0.7 in coarse units, so the uniform
midpoint rule converges like e^{-a n_P} with a small a. f5b uses the same class integrand (imported from
checks/f5_cov_kernel.py, unchanged) with:
- a clustering periodic map per coordinate, P = t - α sin(ℓt)/ℓ, α = 0.65, trapezoid in t (n points per coordinate,
  t-midpoints), weights dP/dt;
- the exact symmetries of the class integrand for modes in directions 1, 2 with k in the (1, 2) plane: P_3 → -P_3,
  P_4 → -P_4, P_3 ↔ P_4 (summed with multiplicities);
- the k-derivative by central differences with h = 3e-4.
The object, the observables (c_Γ, c^M, c^K), the ℓ list and the κ_c list are f5's.

Pre-registered criteria:
- (S) symmetry: at 5 random P (ℓ = 5, κ_c = 1, k = (1e-3, 2e-3, 0, 0)), |f(P) - f(RP)| ≤ 1e-12·|f(P)| for R each of the
  three symmetries (f the per-class total).
- (C') quadrature: c_Γ(5, κ_c) with n = 10 and n = 14, each κ_c ∈ {0.25, 1, 4}: |difference| ≤ 1e-5·|c_Γ|.
- (D') k-step: c_Γ(5, 1) at h = 3e-4 and 6e-4 (n = 12): Richardson error estimate |c(h) - c(2h)|/3 ≤ 1e-6·|c_Γ|.
- (E') = f5 (E) with n = 12: at (11, 13), |s·48π² - 1| ≤ 0.03 for each κ_c ∈ {0.25, 1, 4}.
- (F') = f5 (F): κ spread at (11, 13) ≤ 0.03/(48π²).
- (G') = f5 (G): |s^K·48π²| ≤ 0.05 at (11, 13) for each κ_c, and |s^K(11, 13)| ≤ |s^K(7, 9)|.
Informational: comparison with f5's n_P = 8 values; slope deviations against ℓ^{-2}.

Outcome in checks/f5b_out.txt, checks/f5b_time.txt. A FAIL is reported as a FAIL.
