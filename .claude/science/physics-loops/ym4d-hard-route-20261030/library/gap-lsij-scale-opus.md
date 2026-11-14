lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-14T22:07Z

# gap-lsij-scale-opus (row 954): does the two-slice Poincare ratio R_J stay bounded as the box grows?

Claude Opus 5.5 max, Mac mini worker 2, started 2026-11-14T10:07Z, pinned at branch commit 2a9e82c69.
GUIDE item (refute only). No statement here is a proof step of the chain. A run may refute or guide; it proves nothing.

Credit: the (LSI-J) / (LSI-J-seed) framework is row 947 (`library/gap-fc-max.md`, Claude Fable 5.2 max), built on rows 931-946 and on the Sussman-Alpoge complete account (CA-I/II/III at 31a47c543775, authored with Claude and Codex). Any statement or construction taken from them is credited where used.

## Plan (at most eight steps; one step per response)

1. Read row 947 (`library/gap-fc-max.md`): Theorem BR, Corollary BR-J, (LSI-J-seed), its test, the definition of the two-slice law, of grad, of K_a, and the seed threshold 1/(2 beta K_a). Read check 943's finite-cylinder caveat and row 946's code under `library/guide/lane946/` for reuse. Write the exact definitions used here (Section 1).
2. Pre-state the measurement, the observable span, and pass/fail criteria before any run (Section 2). Free-photon exact formula for R_J by hand (Section 3).
3. Write the code (SU(2) and U(1) heat-bath/overrelaxation on L^3 x T, two-slice extraction, gradient estimator, generalized-eigenvalue variational ratio). Unit tests: free-photon and one-plaquette calibrations (Section 4).
4. Controls: compact U(1) at beta about 1.5, L = 4..10; compare with the photon formula (Section 5).
5. SU(2) runs at beta 2.3, L = 4, 6, 8, 10 (12 if cheap) (Section 6).
6. SU(2) runs at beta 2.6, same sides (Section 6).
7. Analysis: R_J versus L with errors, scaling exponent fit, comparison with 1/(2 beta K_a), finite-cylinder handling (Section 7).
8. Verdicts per statement and the RESULT line (Section 8).

## State of work

(updated in place after each step)

- Step 0 (2026-11-14T10:07Z): file created; FINISH row 954 read; no earlier run of this item exists at 2a9e82c69.
- Step 3a (2026-11-14T10:30Z): code written (Section 4.1), Lemma GAP-R (4.2). Numeric lock held by row 952 (lane952-opus, since 10:14:52Z, expires 11:14:52Z at the latest); a background waiter takes it when free. No run yet.
- Step 2 (2026-11-14T10:30Z): Sections 2 (criteria, before any run) and 3 (free photon exact) written. Next: Step 3, the code and the C1, C2, C5 calibrations.
- Step 1 (2026-11-14T10:20Z): row 947 read in full; check 943's finite-cylinder caveat read (`library/gap-lsivac-check-astra.md` 158-162); row 946's code listed. Duplicate check (rule 0a): `grep -i "LSI-J|two-slice|R_J|poincare"` on `library/open-core.md`, `library/l17c.md`, `library/open-registry.md` gives only an unrelated radius r_J (OL-W0). FINISH rows naming R_J or (LSI-J): 947 (author), 954 (this row), 955 (literature), 956 (check of this row). No other row runs this test. Proceed.

## Section 1. Definitions used here (READ from row 947 and row 941; no new claim)

**Setting (row 941 (A1), row 947 5.1).** B = periodic spatial box of side L, with 3L^3 links. A slice x is a point of M = (S^3)^(3L^3) inside R^N, N = 12 L^3; SU(2) = unit quaternions, (1/2) tr(a b^dagger) = <a, b> (Euclidean inner product of R^4). V(x) = -beta sum over space-like plaquettes of (1/2) tr x_p. Transfer kernel T_0(x, w) = e^(-V(x)/2) e^(beta <x, w>) e^(-V(w)/2), top eigenfunction Omega, eigenvalue lambda_0.

**Two-slice vacuum law (row 941 (A1)).** J(dx, dw) = Omega(x) T_0(x, w) Omega(w) dx dw / lambda_0. In the 4D lattice: x = the spatial links of time slice t; w = the spatial links of slice t+1 transported to slice t by the temporal links: w_i(y) := U_0(y, t) U_i(y, t+1) U_0(y+i, t)^dagger. Then the time-like plaquette at (y, i) is (1/2) tr(x_i(y) w_i(y)^dagger) = <x_i(y), w_i(y)> =: t_i(y). J is symmetric under (x, w) -> (w, x).

**Gauge invariance.** Phi(x, w) is gauge invariant if Phi(g.x, g.w) = Phi(x, w) for every g: sites -> SU(2), acting on both slices at once (g.x_i(y) = g(y) x_i(y) g(y+i)^dagger). Closed loops in x, in w, or through both (using x and w^dagger as the two time-like sides) are gauge invariant.

**Gradient.** Tangential gradient on M x M for the round unit sphere S^3 in R^4: for a link variable u, grad_u Phi = Pi_u (d Phi/d u), Pi_u z = z - <z, u> u. |grad Phi|^2 = sum over the 6 L^3 links of x and w of |grad_u Phi|^2.

**Ratio (row 947 7.4).** R_J(Phi) := Var_J(Phi) / E_J[ |grad_x Phi|^2 + |grad_w Phi|^2 ]. R_J := sup over gauge-invariant Phi (bounded, C^1). (LSI-J)_(alpha_J) implies R_J <= 1/alpha_J (Poincare from log-Sobolev). Here R_J is estimated from below by the top generalized eigenvalue of (C, G) on a finite span: C_ab = Cov_J(Phi_a, Phi_b), G_ab = E_J <grad Phi_a, grad Phi_b>.

**Seed threshold (row 947 7.3-7.4).** (LSI-J-seed)_a: on B = (24a)^3, one even a >= 30, alpha_J >= 2 beta K_a, K_a = (C_beta(x_*) + 3 log a)/(a - 2), with C_beta = 16.0 at beta 2.3 and 16.12 at beta 2.6 (row 947 4.2: 24 C_beta = 384.0 and 386.9). It implies R_J <= R*_a := 1/(2 beta K_a) on that box. Hand arithmetic (3 log a = 10.204, 11.067, 12.283, 13.816, 15.895 for a = 30, 40, 60, 100, 200):

| a | 30 | 40 | 60 | 100 | 200 |
|---|---|---|---|---|---|
| K_a, beta 2.3 | 0.9359 | 0.7123 | 0.4876 | 0.3043 | 0.1611 |
| R*_a, beta 2.3 | 0.232 | 0.305 | 0.446 | 0.714 | 1.350 |
| K_a, beta 2.6 | 0.9401 | 0.7155 | 0.4897 | 0.3055 | 0.1617 |
| R*_a, beta 2.6 | 0.205 | 0.269 | 0.393 | 0.630 | 1.189 |

The seed box has side 24a >= 720. Every box measured here is smaller by a factor of at least 60.

**Check 943's finite-cylinder caveat, and how it is handled here.** On a periodic time circle of N slices the slice-pair law is T_0(x, w) T_0^(N-1)(w, x)/Tr T_0^N, not J; the backward factor depends on (x, w), and states of every sector enter with weight e^(-E N). Here the time direction is OPEN (free boundary): slices 0, ..., N_t - 1, temporal links only between consecutive slices, every plaquette inside the slab. The measured pair (slice t, slice t+1) then has law
  J_K(x, w) = (T_0^K b)(x) T_0(x, w) (T_0^(K') b)(w) / Z,   b := e^(-V/2),   K = t, K' = N_t - 2 - t.
(Temporal gauge on the slab; the boundary vector b is the boundary half of the end-slice plaquette weight.) Two facts make J_K a controlled approximation of J:
- (OB1, PROVED, one line) b is gauge invariant and invariant under the centre maps z_i (multiply every link in direction i that crosses one fixed plane by -1): each plaquette contains 0 or 2 such links. z_i commutes with T_0. So T_0^K b has no component in the sectors odd under any z_i (the 't Hooft electric-flux sectors). Flux states, which are the light states of a small box, cannot enter J_K at any K. On a periodic time circle they do enter, with weight e^(-E_flux N).
- (OB2, standard spectral bound, stated, not used in any proof) T_0^K b = lambda_0^K <Omega, b> (Omega + O(e^(-E_even K))), with E_even the gap of T_0 in the flux-free, centre-even sector. So expectations under J_K differ from those under J by a relative O(e^(-E_even min(K, K'))).
The ground-state limit is checked empirically (criterion C4 below): each R_J is measured at two values of K, and the run is accepted only if they agree within errors.

## Section 2. Measurement, observable span, and criteria (written 2026-11-14T10:25Z, BEFORE any run)

**Lattice and updates.** L^3 x N_t, spatial directions periodic, time open, N_t = 2K + 2 + 2m, with the 2m+1 central slice pairs measured (each at distance at least K from both ends). SU(2): Kennedy-Pendleton heat bath plus 2 overrelaxation sweeps per sweep; U(1): von Mises heat bath (Best-Fisher) plus 2 overrelaxation sweeps. Code in C (sweeps) and numpy (measurement), `library/guide/lane954/`.

**Observable span (pre-stated).** Local gauge-invariant fields at each site y of the slice:
1. c^x_(jk)(y), c^w_(jk)(y): space-like plaquettes of x and of w, planes 12, 13, 23 (6 fields);
2. t_i(y) = <x_i(y), w_i(y)>: time-like plaquettes (3 fields);
3. r^x_(jk), r^w_(jk): 1x2 space-like rectangles, both orientations summed within each plane (6 fields);
4. q^x_(jk), q^w_(jk): 2x2 space-like loops ("smeared plaquettes") (6 fields);
5. s_i(y) = (1/2) tr(x_i(y) x_i(y+i) w_i(y+i)^dagger w_i(y)^dagger): time-like 2x1 rectangles (3 fields).
Winding observables, for each direction i and transverse position y_perp: P^x_i(y_perp), P^w_i(y_perp) (straight winding lines of x and w), the strip (1/2) tr(P^x_i P^w_i^dagger), the product P^x_i P^w_i, and P^x_i^2, P^w_i^2; with M^x_i := mean over y_perp of P^x_i, also (M^x_i)^3, (M^w_i)^3, (M^x_i)^2 M^w_i, M^x_i (M^w_i)^2, (M^x_i)^5, (M^w_i)^5 (odd polynomials that approach a sign function, to see a bimodal law of the winding lines).
Momenta: each local field at k = 0 and at k = (2 pi/L) e_j (cos and sin parts); winding lines at transverse momentum 0 and (2 pi/L) e_j, j transverse to i.
Sectors (exact symmetries of J: translations, cubic rotations, the centre maps z_i, the swap x <-> w): the generalized eigenproblem is solved in each sector, with C and G averaged over the copies that the symmetries map onto each other, and R_J^top := max over sectors. Sectors: S0e (k = 0, centre-even: 24 local fields + 6 x 3 winding-even sums), S0o_i (k = 0, odd under z_i: 8 odd observables), S1e (k = k_min, centre-even: 24 local fields; 6 copies), S1o (k = k_min, winding lines in the 2 directions transverse to k; odd). In odd sectors and at k != 0 the exact mean 0 is used.
For U(1) the same fields with (1/2) tr replaced by cos of the loop angle, plus the sin parts (sin of plaquette angles: the magnetic field), since U(1) has no centre-even restriction on these.

**Errors.** Jackknife over 20 blocks of consecutive measurements (blocks long against the measured autocorrelation). Report the raw top eigenvalue and the jackknife bias-corrected one.

**Criteria (pre-stated).**
- C1 (exact calibration, SU(2) at beta = 0, Haar links). By hand: a loop of n links of fundamental characters is an eigenfunction of the Laplacian on (S^3)^n with eigenvalue 3n (Casimir of spin 1/2 on the unit S^3 is 3). So R_J(t-sum) = 1/6, R_J(plaquette sum) = 1/12, R_J(2x1 rectangle) = 1/18, R_J(2x2 loop) = 1/24, R_J(winding sum) = 1/(3L), and the top of every span is 1/6. Pass: each within 3 err (or 2 percent). Fail: stop and fix the code. U(1) at beta = 0: t-sum 1/2, plaquette 1/4.
- C2 (free photon, Gaussian check): compact U(1) at beta = 8, L = 6: the k_min magnetic mode must give R within 10 percent of the free-photon value 1/(beta (e^omega - 1)), omega = 2 asinh(sin(pi/L)) (Section 3), allowing the known one-loop shift beta_R = beta - 1/4 + O(1/beta) (about 3 percent at beta 8).
- C3 (U(1) Coulomb-phase control, beta 1.5, L = 4, 6, 8, 10, 12 if cheap): R_J^top must grow with L: fitted exponent kappa > 0.5 at 3 sigma over the sizes run, and R at the largest L within a factor 1.5 of the free-photon value at beta 1.5 (expected about 1.2 times it, from beta_R near beta - 1/4). If C3 fails, the method cannot see a massless mode and every SU(2) verdict below is void.
- C4 (ground-state limit): at each (group, beta, L) the top eigenvalue at K and at a larger K' (K' >= K + 4) must agree within 3 combined errors. If not, K is raised and the smaller K is discarded.
- C5 (independent implementation check): at L = 4, beta 2.3, K = 6, R_J of the zero-momentum t-sum must agree with row 947's Run 3 (0.1545 +- 0.0041) within 3 combined errors, and E c_p with 0.6058.
- S1 (growth over the measured range, SU(2), each beta): weighted fit of log R_J^top against log L over the sizes run with L >= 6; exponent kappa with error. GROWTH iff kappa > 0 at 3 sigma AND R_J^top(L_max) - R_J^top(6) > 3 combined errors. GROWTH at a coupling is reported plainly as "REFUTES a box-uniform (LSI-J) at that coupling over the measured range (GUIDE)", and the sector and observable carrying it are named. No GROWTH: "bounded over L = 4..L_max (GUIDE only; proves nothing)".
- S2 (what growth would mean for the seed). The seed box has side >= 720. A growth that is carried by the winding (centre-odd) sector in a box smaller than the deconfinement length L_c(beta) = 1/(T_c a) is a small-box effect: the spatial Polyakov loops order there, and the flux sectors become light. Recalled lattice values (not checked here; used only to place L_c): T_c/sqrt(sigma) = 0.71 for SU(2), sqrt(sigma) a = 0.37 at beta 2.3 and 0.133 at beta 2.6, so L_c is about 3.8 at beta 2.3 and about 10.6 at beta 2.6. So at beta 2.3 every L >= 4 is above L_c, and S1 there is a test of the large-box regime. At beta 2.6 the sizes 4 to 10 are at or below L_c; growth there threatens (LSI-J-seed) only if it persists at L above L_c (14 if cheap). This classification is stated now, before the run, and is reported together with the per-sector numbers, so a reader can disagree with it.
- S3 (seed threshold on the measured box, row 947's rule): REFUTES (LSI-J-seed)_a ON THE MEASURED BOX iff R_J^top - 3 err > R*_a. Since the measured box is not the seed box, this is reported as a box-local statement only.
- S4: report kappa (with error) for each beta and for U(1).
- Amendments written 10:30Z, still BEFORE any run (no number had been produced):
  (A1) C3 is applied to the photon sector U1s (sin of plaquette angles at k_min: the row's "lowest photon mode"). Reason found by hand at 10:28Z: compact U(1) has a second massless channel, the spatially constant mode (holonomy phi of each direction, a free rotor on the circle with kinetic weight e^(-(beta L/2)(phi_x - phi_w)^2), charge-one energy about 1/(2 beta L)). Its variational ratio in the span (mean winding phase) carries a factor p^2, p the line-fluctuation factor, which falls with L, so U0w may dominate R_J^top at small L without growing. U0w is reported separately, with its gap from the winding correlator.
  (A2) Gap floor (Lemma GAP-R, 4.2): for each run the effective energies E_eff(tau) of the zero-momentum plaquette-sum and mean-winding-line time correlators are reported; the floor 1/(2 beta E) is compared with the variational top. This is a second data path for the size of R_J (same configurations, different estimator); it is not an independent check.
  (A3) Code fix before any run: the strip loop tr(P^x P^w^dagger) depends on its base point in SU(2); the gradient now uses a fixed base point per line (prefix and suffix products). A finite-difference self-test of every gradient (k = 0 sectors, one k_min copy, the odd sectors) runs first; a FAIL stops all runs.

## Section 3. Free photon: R_J exactly (PROVED by hand; the numbers are small arithmetic)

**Statement.** Non-compact U(1) lattice photon (Wilson form, link angles theta in R, weight exp(-(beta/2) sum_p theta_p^2), temporal gauge), periodic spatial box of side L. For a transverse mode of lattice momentum k (unit-normalised mode vector, amplitude a), with |khat|^2 = sum_i 4 sin^2(k_i/2) and omega_k = 2 asinh(|khat|/2):
  (FP-J) the two-slice vacuum law of (a_x, a_w) is Gaussian with precision [[beta + c_k, -beta], [-beta, beta + c_k]], c_k = beta (e^(omega_k) - 1);
  (FP-R) the largest Poincare ratio over functions of this mode is 1/c_k, attained by a_x + a_w (and by any magnetic-field observable proportional to it).
**Proof.** One mode: V(a)/2 = (beta/4)|khat|^2 a^2, kinetic factor e^(-(beta/2)(a - a')^2). Try Omega = e^(-gamma a^2/2). The Gaussian integral of T_0(a, a') Omega(a') over a' returns e^(-gamma a^2/2) iff gamma = beta |khat|^2/2 + beta - beta^2/(beta + c) with c := gamma + beta |khat|^2/2. Put u = (beta + c)/beta; then u + 1/u = 2 + |khat|^2 = 2 cosh omega_k, so u = e^(omega_k). The law J ~ Omega(a) T_0(a, a') Omega(a') has the stated precision; its eigenvalues are c_k (vector (1, 1)) and 2 beta + c_k (vector (1, -1)). For a Gaussian law the Poincare constant is the inverse of the smallest precision eigenvalue, attained by the linear function along that eigenvector; a ratio is unchanged when the observable is scaled, so the magnetic field of the mode gives the same value. QED
Modes decouple, so on the box the sup over all functions of transverse modes is 1/c at the smallest non-zero |khat|, k = (2 pi/L) e_j: |khat| = 2 sin(pi/L), omega_min = 2 asinh(sin(pi/L)). (The spatially constant modes are not transverse waves; in the non-compact theory they are free and have no Poincare constant at all; in compact U(1) they are compact rotors, see Section 5.)
For large L, 1/c_min = (L/(2 pi beta))(1 + O(1/L)): exponent 1 in L.

| L | 4 | 6 | 8 | 10 | 12 | 14 | 16 |
|---|---|---|---|---|---|---|---|
| omega_min | 1.3170 | 0.9624 | 0.7478 | 0.6086 | 0.5120 | 0.4415 | 0.3878 |
| 1/c_min at beta 1.5 | 0.2440 | 0.4120 | 0.5993 | 0.7957 | 0.9970 | 1.2013 | 1.4075 |
| 1/c_min at beta 8 | 0.0458 | 0.0773 | 0.1124 | 0.1492 | 0.1869 | 0.2252 | 0.2639 |

(Evaluated with a two-line script; the values for L = 4, 6, 8, 10, 12 at beta 1.5 were also done by hand in this step and agree to 3 digits.)
Use: criterion C2 (compact U(1) at beta 8 must approach these, up to beta_R = beta - 1/4) and C3 (compact U(1) at beta 1.5 must grow like this, at about 1.2 times these values).

## Section 4. Code, and a floor on R_J from the transfer-matrix gap

**4.1 Code (written 10:20-10:27Z; not yet run).** `library/guide/lane954/lgt_sweep.c` (C, compiled to a scratch library outside the repository: `clang -O2 -shared -fPIC -o /tmp/lane954/build/liblgt954.dylib lgt_sweep.c -lm`): xoshiro256** generator; SU(2) heat bath (Creutz below k = 2, Kennedy-Pendleton above, exact Haar at k = 0) and overrelaxation u -> W u^dagger W, W = S^dagger/|S|; U(1) von Mises heat bath (Best-Fisher) and overrelaxation; open time (temporal links of the last slice absent; time-like staples only inside the slab). `library/guide/lane954/rj954.py`: slices, temporal-gauge transport, every loop of Section 2 with exact Euclidean gradients from cyclic prefix and suffix products (forward link: conj(rest); backward link: rest; then the tangent projection z - <z, u> u), Fourier sums, sector matrices C and G with symmetry copies averaged in rotation-adapted labels, top generalized eigenvalue after whitening G (directions with eigenvalue below 1e-9 of the largest dropped), jackknife over 20 blocks with bias correction. Per configuration it also records, for every slice of the slab, the zero-momentum space-like plaquette sum and the mean winding line M_i(t) (U(1): also the magnetic field at k_min), for the gap estimates of 4.2. U(1) uses the same quaternion code on links (cos theta, 0, 0, sin theta); sin of a loop angle is Re(W e3^dagger). Peak memory is capped at 2 GB in the script.

**4.2 Lemma GAP-R (CONDITIONAL on row 947's (BR-gap) and the variance form of Lemma J, both proved there by hand and not yet checked; check = row 949).** Let E_1 be the gap of the one-step operator P on gauge-invariant functions of mean zero in L^2(nu) (all centre sectors included), on any box. If E_1 <= 1, then
  R_J >= 1/(2 beta E_1).
Proof. Row 947 7.2, variance form: E_1 >= Xi(rho)/2, rho = beta/gam_J, gam_J = 1/R_J, Xi(rho) = integral over (0, 1) of d lam/(rho + (1 - 2 rho) lam (1 - lam)). If rho < 1/2, the denominator is at most (1 + 2 rho)/4 < 1/2, so Xi > 2 and E_1 > 1. Hence E_1 <= 1 forces rho >= 1/2; then the denominator is at most rho, Xi >= 1/rho = gam_J/beta, and 2 E_1 >= gam_J/beta. So gam_J <= 2 beta E_1, that is R_J >= 1/(2 beta E_1). QED
Use. E_1 is the lowest excitation energy of the lattice transfer matrix over all gauge-invariant states, including the 't Hooft electric-flux states (winding lines carry them). It can be read from Euclidean time correlators on the same slab. This gives a floor for the true R_J along a data path independent of the variational span. If the span's top is far below the floor, the span misses the slowest mode. It also shows where large R_J must come from in small boxes: from light flux states (torelons, or the tunnelling doublets of a box below the deconfinement length).
Consistency. On the seed box the flux states are heavy (energy about sigma times the side), so E_1 is the lightest glueball mass m_G; the floor is 1/(2 beta m_G); (LSI-J-seed)_a needs R_J <= 1/(2 beta K_a); together they need m_G >= K_a, which is row 947's necessary condition 4.2 again. Nothing new for the seed; a check of the measurement.
For the free photon: E_1 = omega_min and the floor is 1/(2 beta omega_min), against the exact 1/(beta (e^(omega_min) - 1)); the floor is lower by a factor of about 2 for small omega (Section 3), as it must be.
