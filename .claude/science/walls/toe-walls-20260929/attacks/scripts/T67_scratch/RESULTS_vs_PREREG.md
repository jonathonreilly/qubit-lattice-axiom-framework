# Results against the pre-registered readings (T67)

Test A (R2, NN bond lengths as carrier). Pre-registered survive condition: leakage < 1e-3 AND Q_aa(0) = 0 AND relaxed rank >= 2.
Observed: leakage 0.50 (all |k| tested); Q_aa(0) = diag-like (-18,-2,-2,-2); relaxed rank 0 at generic k. -> R2 FAILS on both branches.
Control (axes + 6 face diagonals relaxed): rank 6, 4 exact gauge zero modes -> passes, so the harness works.
Caveat: at momenta with two or more zero components the Schur complement is inconsistent (residual ~2e-4); only generic k and the single-zero case are claimed.

Test B (R1, order + number).
B1: event density per site per unit time = exp(-t) (matches to 3 digits) -> not stationary. FAIL as pre-registered.
B2: futures of iid clock: mean 17 sites, max L1 extent 10, no growth with L (24, 48, 72). -> FAIL (bounded).
B3 (nucleation): pre-registered thresholds (speed spread < 3%, future fraction < 0.5) cannot be evaluated as written because futures vanish beyond ~9 sites in
the 60-source sample (P(later event in future) = 0 median at |d|=9,12); future fraction 0.0004-0.0017 << 0.5 but no cone speed exists to compare. Recorded as FAIL (no cone at tested sizes; asymptotics unresolved).
B3b control: deterministic seeded NN front gives speeds 1.000 : 0.714 : 0.583 vs taxicab prediction 1.000 : 0.707 : 0.577 -> the harness detects macroscopic cones when they exist; the cone is taxicab and the seed is privileged.

Test C (group characters): NN axis lines A1+E; NNN lines A1+E+T2; body lines A1+T2. Exact (integer multiplicities from characters of the 24 proper rotations).

Not done: any test of R3; nonlinear (T66) closure; larger sizes for the coupled clause; a proof of Lemma V beyond the counting argument (events <= sites, so uniform density rho over a window T needs rho*T <= n).
