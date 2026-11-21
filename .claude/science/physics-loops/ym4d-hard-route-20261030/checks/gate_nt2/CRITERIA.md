# Criteria for gate_nt2, written before any run

Commit 2285befef. Each check states what passes, what fails, and what it cannot establish.

## C1 `nt2_box.py`: coefficients from exact group elements, finite contractible box

Box of 3^4 sites, open boundary, Wilson action, SU(2) matrices. Triple (Gamma_12, Gamma_23, Gamma_31) at an interior site. Two charts: Landau slice (orthogonal to gradients), maximal-tree gauge (two different trees).

- C1a PASS if K_comp, K_vert from the Wick formulas of Proposition 2.1 agree with Monte Carlo means of t_4 and -t_3 F_3, where t_3, t_4, F_3 are extracted by finite differences of the exact group functions in gamma, within 4 standard errors. FAIL means a sign or normalization error in (NT2-C).
- C1b PASS if K_T = K_comp + K_vert agrees across charts to 1e-9 relative. FAIL means K_T is not chart-free on this box.
- C1c Predicted outcome: K_vert differs across charts by more than 1e-3 absolute. If it does not, the chart-dependence defect is withdrawn.
- C1d Build the explicit rank-one linear chart of the report, with K_vert(tau_*) = 0 to 1e-9 and K_T unchanged. PASS confirms the defect. FAIL (no such chart, or the chart is not a slice) withdraws it.
- C1e The same chart must satisfy the slice property: projection idempotent, annihilating gradients, colour diagonal.
- Cannot establish: anything about blocked limits or about Wilson at finite coupling.

## C2 `nt2_box.py`: transport

- C2a PASS if E[D t_3 . B] = -E[t_3 F_3] (B1) within 4 standard errors, with B = -(1/3) C grad F_3.
- C2b With covariance C_rho and B still built from the unit C, PASS if the Monte Carlo mean agrees with the Wick prediction: the mean over which of the three legs carries the unit C and which two carry C_rho.
- Cannot establish: the remainder estimates of a coherent law.

## C3 `nt2_algebra.py`: exact algebra

- C3a Moment polynomials of library C, sympy. PASS on exact equality.
- C3b Formula (6), and the 48 a^3 difference: exact Wick enumeration over the 15 pairings. PASS on exact equality.
- C3c (C1) with general weights: d/dkappa at 0 of the excess equals 120 sum_b w_b r_b^3, by finite-difference-free symbolic expansion on 3 correlated Gaussians. PASS on exact equality.
- C3d Stieltjes monotonicity: for Proca mixtures, rho(z) = z D(z) non-decreasing, and the loop flux variance non-increasing in r on a grid. For rho = 1/(c + b log(1 + z)), z D(z) decreasing and the implied spectral density negative. PASS on sign.

## C4 `nt2_blocked.py`: blocked corner vertex, Feynman prescription

Formula (B-6) on a periodic lattice of side n S, block B-1, n = 1, 3, 5.

- C4a PASS at n = 1 if K_vert reproduces 0.2188 and P values reproduce the known Green's function values within finite-size effects.
- C4b Report K_vert(n, S). If |K_vert| trends to a value distinct from 0 by more than 5 times the spread in S, that is numerical evidence for (NV) in that prescription, not a proof. If it trends to 0, (NV) is in doubt.
- Cannot establish: a bound on the limit, K_comp, or K_T for any nonlinear map.

## Discipline

One job at a time under `lab_ops.py numeric-lock`, BLAS threads 1, nice, RSS stop at 2 GB, memory_pressure at 50 percent free or more before each start.
