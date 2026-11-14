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
- Step 4c (2026-11-14T12:13Z): beta 2.6 L = 10, 12, 14 done. Incident: at 12:10Z I added the `glue26` phase to `run954.sh` while bash was executing that file; after its L = 14 run (exit 0, results intact) the running `main26` invocation read a shifted file and stopped with 'syntax error: unexpected end of file'. Nothing was lost: `main26` had no step after L = 14, and `main26big` (L = 16) started as a fresh invocation at 12:12:10Z. The glueball run is chained after the batch in a separate job.
- Step 4b (2026-11-14T11:58Z): beta 2.3 (5c) and U(1) (5d) done and written; beta 2.6 L = 4, 6, 8 done (winding sector 1.54, 0.64, 0.25; flux energy about 0.13-0.15 at all three; local sectors about 0.11); L = 10, 12, 14, 16 running. Planned after the batch, inside the 60-minute compute budget: `glueball954.py` (smeared-loop 0++ correlator, no gradients) at beta 2.6 L = 16 and beta 2.3 L = 10 for the glueball floor of Lemma GAP-R, because the plaquette-size local fields overlap poorly with the beta 2.6 glueball.
- Step 4a (2026-11-14T11:30Z): lock taken 11:25:57Z; self-test PASS; C1, C2, C5 PASS (Section 5a); main batch running in background since 11:29Z (about 40 min). Next: read the batch, write 5b-5d, analysis.
- Step 3b (2026-11-14T10:31Z): strip-gradient bug found by reading and fixed before any run; finite-difference self-test, gap correlators and runner `run954.sh` added; criteria amendments (A1)-(A3) written before any run. Waiting for the numeric lock (row 952 holds it). Next: selftest, then calib (C1, C5, C2), then timing, then the main runs.
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

## Section 5. Runs (GUIDE). 5a: self-test and calibrations (lock holder gap-lsij-954 from 11:25:57Z; 70 percent memory free; one thread, nice 10)

Logs: `/tmp/lane954/logs/*.log` (copied to `library/guide/lane954/logs/` at the end); JSON summaries with the full sector matrices C and G (main runs only): `library/guide/lane954/out/`. The row-952 lock was released before 11:25:57Z; no run of this row overlapped another numeric job.

**Self-test (11:26Z): PASS.** Finite-difference directional derivatives (eps = 1e-5, random links, random tangent field, L = 4) against the analytic tangent gradients of every observable: SU(2) S0e (36 observables), S0o (8), one S1e copy (24, real and imaginary parts), one S1o copy; U(1) U0c (27), U0s (24), U1c and U1s copies (24 each), U0w (4). Largest relative error 1.6e-9.

**C1, exact calibration at beta = 0 (Haar links), L = 4, K = 2, 300 configurations x 3 pairs: PASS.**

| sector | top (raw) | bias-corrected | exact |
|---|---|---|---|
| SU(2) S0e | 0.1771 +- 0.0069 | 0.1674 | 1/6 = 0.1667 |
| SU(2) S1e | 0.1713 +- 0.0032 | 0.1696 | 1/6 |
| SU(2) S0o | 0.0861 +- 0.0023 | 0.0847 | 1/(3L) = 0.0833 |
| SU(2) S1o | 0.0853 +- 0.0011 | 0.0850 | 1/(3L) |
| U(1) U0c | 0.5378 +- 0.0216 | 0.5112 | 1/2 |
| U(1) U0s | 0.5387 +- 0.0157 | 0.5169 | 1/2 |
| U(1) U1s | 0.5123 +- 0.0089 | 0.4954 | 1/2 |
| U(1) U0w | single lines 0.239-0.256 +- 0.006 | | 1/L = 0.25 |

All 70 single-observable ratios (plaquettes 1/12, time-like plaquettes 1/6, 1x2 rectangles 1/18, 2x2 loops 1/24, time-like rectangles 1/12, strip and P^x P^w 1/(6L), P^2 1/(8L); U(1): 1/4, 1/2, 1/6, 1/8, 1/4, 1/(2L)) lie within 2.0 errors of the exact values. The raw top eigenvalue is biased upward by noise (here by 0.5 to 2.4 errors); the jackknife bias correction removes it. Both are reported below.

**C5, independent implementation against row 947 Run 3 (SU(2), L = 4, beta 2.3, K = 6, 400 configurations x 3 pairs): PASS.** E c_p = 0.6044 +- 0.0013 (row 947: 0.6058), E t = 0.6054 +- 0.0014 (0.6049), E t^2 = 0.4581 +- 0.0012 (0.4575). Top of the zero-momentum centre-even sector S0e = 0.167 +- 0.010 against row 947's top of its 3-span 0.1547 +- 0.0041 (1.2 combined errors; my span contains theirs).
**But the centre-odd winding sector is much larger on this box:** S0o top = 0.515 +- 0.020 (single M_x: 0.302). The winding-line time correlator gives E_eff(tau) = 0.473, 0.388, 0.350, 0.434, 0.381 (+-0.016 to 0.10) for tau = 0..4: the lightest flux state (torelon) of the 4^3 box has energy about 0.37 +- 0.03, and Lemma GAP-R puts the floor 1/(2 beta E_1) at about 0.57 or more. Row 947's span had no winding observable, so its 0.155 missed this. (Measured on J_K with K = 6; the main run below repeats it at K = 10.)

**C2, Gaussian check (compact U(1), beta 8, L = 6, K = 6, 300 configurations x 3 pairs): PASS.** Photon sector U1s top = 0.0811 +- 0.0016 (bias-corrected 0.0777) against the free value 1/(beta (e^omega - 1)) = 0.0773 (+4.9 percent, inside 10 percent) and 0.0797 with beta_R = beta - 1/4 (0.9 errors). The magnetic-field correlator at k_min gives E_eff = 0.960 +- 0.014, 1.022 +- 0.038 against omega_min = 0.9624. The constant (holonomy) mode is a free rotor as computed by hand in amendment (A1): winding E_eff = 0.0095 to 0.011 against 1/(2 beta L) = 0.0104; its variational ratio U0w = 10.4 +- 0.5 raw, 6.1 bias-corrected (lag-1 autocorrelation 0.82: the local algorithm moves the holonomy slowly, so this error is too small), against the floor 1/(2 beta E) of about 6. So compact U(1) has R_J of order L from its zero mode alone.

**Timing.** SU(2): 0.43 ms per sweep at L = 4 (N_t = 16), 16 ms at L = 12 (N_t = 22); measurement of two pairs plus the slab time series about 0.2 s per configuration at L = 12. U(1) about twice that. Peak memory below 0.2 GB.

**Main batch, started 11:29Z** (one background job, sequential): SU(2) beta 2.3, L = 4, 6, 8, 10, 12 (central pair at K' = 10, extra pair at K = 6 for C4, 1200 configurations, 2 sweeps apart); U(1) beta 1.5, L = 4, 6, 8, 10, 12 (K' = 10, K = 6, 800 configurations); SU(2) beta 2.6, L = 4, 6, 8, 10, 12, 14 (K' = 12, K = 8, 1200 configurations); SU(2) beta 2.6, L = 16 (800 configurations). Thermalisation 300 sweeps from a cold start.

### 5b. Interim (11:32Z), SU(2) beta 2.3, L = 4 and 6 (central pair K' = 10; 1200 configurations each)

| L | S0e | S0o (winding, odd) | S1e | S1o | R_J^top | C4: same sector at K = 6 | E_wind plateau (tau 1-3) | floor 1/(2 beta E_wind) |
|---|---|---|---|---|---|---|---|---|
| 4 | 0.1595 +- 0.0055 | 0.5665 +- 0.0172 | 0.1197 +- 0.0022 | 0.1016 +- 0.0011 | 0.567 (S0o) | 0.574 +- 0.020 | 0.333 +- 0.008 | 0.654 +- 0.015 |
| 6 | 0.1504 +- 0.0049 | 0.1353 +- 0.0027 | 0.1342 +- 0.0022 | 0.0813 +- 0.0011 | 0.150 (S0e) | 0.173 +- 0.011 | 0.652 +- 0.021 | 0.333 +- 0.010 |

C4 (central pair at K' = 10 against the pair at K = 6), all sectors: deviations +0.6, -0.3, +0.1, -1.6 (L = 4) and -1.9, +1.1, +0.3, +1.0 (L = 6) combined errors: PASS (all within 3).
Reading (GUIDE). On the 4^3 box the largest ratio is in the winding (flux) sector, carried by the light torelon (E about 0.33, close to the recalled string-tension estimate 0.39). From L = 4 to L = 6 the torelon energy doubles and the winding ratio falls by a factor 4. At L = 6 the variational top (0.15) lies well below the floor (0.33): raw winding lines overlap poorly with the lightest flux state, so for flux states the floor of Lemma GAP-R is the stronger lower bound. Both are lower bounds on the true R_J; neither can show boundedness.

## Section 6. What carries R_J on a finite box (ARGUED, with the PROVED floor of 4.2)

**6.1 Three channels.** On a periodic box of side L the slow gauge-invariant modes of the two-slice law come in three kinds, and Lemma GAP-R ties each to an energy of the transfer matrix:
- (F) Flux states ('t Hooft electric flux; the torelon, a flux tube wound once around the box). Centre-odd: winding lines. Energy E_flux(L): in a box larger than the deconfinement length, about sigma L - pi/(3L), growing with L; in a box below it, a tunnelling splitting between the ordered values of the spatial Polyakov loops, small. Floor 1/(2 beta E_flux).
- (P) Flux pairs: two torelons with opposite winding, centre-even, energy about 2 E_flux. In the span through P^2, P^x P^w and the strip. They are the lightest centre-even states while 2 E_flux < m_G.
- (G) Local glueball states, energy m_G at zero momentum (heavier at k != 0). In the span through the plaquette-type fields. Floor 1/(2 beta m_G).
On the seed box (side >= 720) E_flux is about sigma times 720 (about 98 at beta 2.3, about 13 at beta 2.6, by the recalled string tensions), so (F) and (P) are irrelevant there and only (G) and other local modes remain. On the measured boxes (F) and (P) can dominate. So a measured R_J that falls with L because (F) gets heavy says nothing for the seed box; the seed-relevant numbers are the local sectors at the largest L, and the glueball floor.
**6.2 Consequence for (LSI-J-seed) (PROVED given 4.2; same content as row 947 4.2).** On the seed box, R_J >= 1/(2 beta m_G) whenever m_G <= 1 (with m_G the lowest energy there). (LSI-J-seed)_a needs R_J <= 1/(2 beta K_a). So it needs m_G >= K_a. With recalled lattice values of the 0++ mass (m_G about 3.7 sqrt(sigma): about 1.37 at beta 2.3, about 0.49 at beta 2.6; recalled, not checked here; this run's plaquette correlators give a rough check in Section 7) this would rule out a <= 40 at beta 2.6 (K_40 = 0.716) and be marginal at a = 60 (K_60 = 0.490); at beta 2.3 it rules out nothing for a >= 30 (K_30 = 0.936 < 1.37). This last step rests on recalled masses: GUIDE, not PROVED.

### 5c. SU(2) beta 2.3, all sizes (GUIDE; runs 11:29-11:40Z; 1200 configurations each, central pair at K' = 10; logs `su2_b2.3_L*.log`)

Top generalized eigenvalue per sector (raw +- jackknife error; bias-corrected in brackets). R_J^top = max over sectors.

| L | S0e (k = 0, even) | S0o (k = 0, winding) | S1e (k_min, even) | S1o (k_min, winding) | R_J^top | C4: max deviation K' = 10 vs K = 6 |
|---|---|---|---|---|---|---|
| 4 | 0.1595 +- 0.0055 | **0.5665 +- 0.0172** | 0.1197 +- 0.0022 | 0.1016 +- 0.0011 | 0.567 (S0o) | 1.6 err |
| 6 | **0.1504 +- 0.0049** | 0.1353 +- 0.0027 | 0.1342 +- 0.0022 | 0.0813 +- 0.0011 | 0.150 (S0e) | 1.9 err |
| 8 | **0.1696 +- 0.0061** | 0.0574 +- 0.0016 | 0.1461 +- 0.0025 | 0.0519 +- 0.0006 | 0.170 (S0e) | 1.2 err |
| 10 | **0.1708 +- 0.0081** | 0.0382 +- 0.0011 | 0.1460 +- 0.0017 | 0.0368 +- 0.0004 | 0.171 (S0e) | 1.4 err |
| 12 | **0.1638 +- 0.0080** | 0.0294 +- 0.0008 | 0.1500 +- 0.0019 | 0.0294 +- 0.0004 | 0.164 (S0e) | 1.2 err |

Energies from the slab time correlators (E_eff over tau = 1-3, weighted; plaquette channel E_eff(1)) and the floors of Lemma GAP-R:

| L | E_flux (winding) | floor 1/(2 beta E_flux) | E_eff(1) plaquette channel | floor 1/(2 beta E) |
|---|---|---|---|---|
| 4 | 0.333 +- 0.008 | 0.654 +- 0.015 | 1.26 +- 0.27 | 0.17 |
| 6 | 0.652 +- 0.021 | 0.333 +- 0.010 | 1.73 +- 0.26 | 0.13 |
| 8 | 1.20 +- 0.13 | 0.18 +- 0.02 | 1.16 +- 0.18 | 0.19 |
| 10 | 1.48 +- 0.42 | 0.15 +- 0.04 | 1.43 +- 0.23 | 0.15 |
| 12 | (noise) | - | 1.27 +- 0.16 | 0.17 |

(An effective energy approaches the lowest energy from above, so a floor computed from it is itself an underestimate of 1/(2 beta E_1).) The flux energies agree with sigma L - pi/(3L) for the recalled sigma = 0.136 (0.28, 0.64, 0.96); the plaquette channel gives m_G about 1.3, against the recalled 1.37.

**Verdicts at beta 2.3 (pre-stated rules of Section 2).**
- C4: PASS at every L (largest deviation 1.9 combined errors, over all 20 sector comparisons).
- S1: fit of log R_J^top against log L over L = 6, 8, 10, 12: kappa = 0.162 +- 0.077 (chi^2 3.7 for 2 dof), 2.1 sigma, below the 3 sigma required; R(12) - R(6) = +0.013 +- 0.009 (1.4 combined errors, below 3). **No GROWTH: R_J^top is bounded over L = 4..12 at beta 2.3 (GUIDE only; proves nothing).** Per sector: S0e kappa = 0.16 +- 0.08; S0o kappa = -2.26 +- 0.05; S1o kappa = -1.48 +- 0.03; S1e kappa = 0.146 +- 0.029 (5 sigma, but the values 0.134, 0.146, 0.146, 0.150 saturate: k_min = 2 pi/L tends to 0, and S1e tends to the zero-momentum value of the same fields, which S0e bounds at about 0.17; a saturating approach, not a power).
- S3: on the 4^3 box R_J^top - 3 err = 0.515 exceeds R*_30, R*_40, R*_60 (0.232, 0.305, 0.446). So the 4^3 box has no (LSI-J) with alpha_J >= 2 beta K_a for a <= 60 (GUIDE, box-local). Cause: the light torelon (E = 0.33). On boxes 6 to 12 nothing exceeds any threshold: the largest R_J^top - 3 err is 0.151 (L = 8), against R*_30 = 0.232.
- Local sector against the glueball floor: on L = 8 to 12 the variational S0e top (0.164 to 0.171) equals, within errors, the floor 1/(2 beta m_G) of about 0.17 from the plaquette channel. Two estimators (the variational span and the gap floor through Lemma GAP-R) agree on the size of the local slow mode. They use the same configurations, so this is not an independent check.

### 5d. Compact U(1), beta 1.5 (Coulomb phase), control (GUIDE; runs 11:39-11:53Z; 800 configurations each, central pair K' = 10; logs `u1_b1.5_L*.log`)

| L | U1s (k_min, sin fields) | U1s-B: space-like (magnetic) fields only | free photon 1/c_min (Section 3) | U1s-B / free | E_eff(tau = 1) of B(k_min) | free omega_min | U0w (holonomy, variational) | E_wind | floor 1/(2 beta E_wind) | U0c, U0s, U1c |
|---|---|---|---|---|---|---|---|---|---|---|
| 4 | 0.3714 +- 0.0069 | 0.268 | 0.2440 | 1.10 | 1.411 +- 0.048 | 1.3170 | 4.33 +- 0.13 | 0.107 | 3.12 +- 0.08 | 0.229, 0.412, 0.175 |
| 6 | 0.4143 +- 0.0059 | 0.414 | 0.4120 | 1.00 | 0.936 +- 0.018 | 0.9624 | 4.45 +- 0.15 | 0.069 | 4.82 +- 0.09 | 0.213, 0.426, 0.196 |
| 8 | 0.5247 +- 0.0115 | 0.523 | 0.5993 | 0.87 | 0.758 +- 0.011 | 0.7478 | 3.97 +- 0.14 | 0.054 | 6.14 +- 0.07 | 0.202, 0.402, 0.203 |
| 10 | 0.6102 +- 0.0153 | 0.609 | 0.7957 | 0.77 | 0.609 +- 0.009 | 0.6086 | 3.31 +- 0.12 | 0.047 | 7.16 +- 0.19 | 0.213, 0.394, 0.200 |
| 12 | 0.6687 +- 0.0155 | 0.668 | 0.9970 | 0.67 | 0.512 +- 0.007 | 0.5120 | 2.73 +- 0.10 | 0.038 | 8.84 +- 0.18 | 0.229, 0.416, 0.215 |

(U1s-B errors: scaled from the U1s error, about 2 percent.) At L = 4 the top of U1s is the longitudinal electric mode (sin of the time-like plaquette at momentum along its own link): in temporal gauge the relative gauge mode between the slices has precision about beta_eff, so its ratio is about 1/(2 beta_eff), near 0.37-0.41 at every L. From L = 6 on the transverse magnetic mode (the photon) is the top.

**Verdicts (pre-stated, with amendment (A1)).**
- C3 growth: photon sector U1s, kappa = 0.711 +- 0.036 over L = 6..12 (chi^2 2.6 for 2 dof); 0.84 +- 0.02 over L = 4..12. kappa > 0.5 by 5.8 sigma: **PASS**. The method sees a massless mode as growth in L.
- C3 size: at L = 12 the measured photon ratio is 0.670 of the free value, inside the pre-stated factor 1.5 (bound 0.667): **PASS, barely.** My pre-run expectation (about 1.2 times free, from beta_R = beta - 1/4) was wrong in direction. The energies agree with the free dispersion to 2 percent at L >= 6 (0.936, 0.758, 0.609, 0.512 against 0.962, 0.748, 0.609, 0.512), so the deficit is in the observable, not in the photon. Reading (ARGUED): the gradient of sin(theta_p) carries a k-independent incoherent part (about 4 Var(cos theta_p) per plaquette), while the coherent part falls like |khat|^2; at L = 12 they are comparable, which lowers the ratio of a local magnetic observable below 1/c as k_min -> 0. A smoothed photon field would do better; not tried.
- C4: all 25 sector comparisons (K' = 10 against K = 6) within 2.0 combined errors: PASS.
- A lesson for the SU(2) verdicts (GUIDE): in U(1) the variational top over ALL sectors is the holonomy sector U0w, and it FALLS with L (kappa = -0.69 +- 0.07), while the true R_J grows. The floor from the holonomy gap (Lemma GAP-R) grows like L (3.1 to 8.8; E_wind follows the rotor value 1/(2 beta_R L) with beta_R about 1.2), and so does the photon sector. Raw winding lines lose their overlap with the rotor states (factor p^2, amendment (A1)). So a flat or falling R_J^top does not by itself show boundedness: each sector and each floor has to be read. The SU(2) verdicts below are read that way.

### 5e (interim, 12:05Z). SU(2) beta 2.6, L = 4..12 (1200 configurations each, central pair K' = 12, extra pair K = 8)

| L | S0e | S0o (winding) | S1e | S1o | R_J^top | E_flux (weighted tau 1-3) | floor 1/(2 beta E_flux) | Binder U of M |
|---|---|---|---|---|---|---|---|---|
| 4 | 0.1221 +- 0.0057 | **1.5419 +- 0.0565** | 0.0933 +- 0.0015 | 0.0885 +- 0.0012 | 1.542 (S0o) | 0.132 | 1.46 +- 0.03 | 0.42 |
| 6 | 0.1147 +- 0.0045 | **0.6396 +- 0.0244** | 0.1057 +- 0.0019 | 0.0832 +- 0.0014 | 0.640 (S0o) | 0.136 | 1.42 +- 0.05 | 0.31 |
| 8 | 0.1072 +- 0.0032 | **0.2464 +- 0.0076** | 0.1076 +- 0.0019 | 0.0654 +- 0.0009 | 0.246 (S0o) | 0.152 | 1.27 +- 0.03 | 0.18 |
| 10 | **0.1118 +- 0.0047** | 0.1084 +- 0.0042 | 0.1080 +- 0.0026 | 0.0474 +- 0.0006 | 0.112 (S0e) | 0.165 | 1.17 +- 0.04 | 0.105 |
| 12 | **0.1179 +- 0.0054** | 0.0555 +- 0.0016 | 0.1130 +- 0.0020 | 0.0359 +- 0.0006 | 0.118 (S0e) | 0.168 | 1.14 +- 0.08 | 0.035 |

The flux energy stays near 0.13-0.17 from L = 4 to 12 (box at or below the deconfinement length; Nambu-Goto with the recalled sigma = 0.0176 gives 0.11 at L = 10 and 0.16 at L = 12), so the floor of Lemma GAP-R stays at 1.1-1.5, while the variational winding sector falls by a factor 28 (raw winding lines lose their overlap with the flux state as the Polyakov loops disorder: Binder U 0.42 -> 0.105). The local sectors are flat at 0.107-0.122. C4 (K' = 12 against K = 8), computed: all 20 sector comparisons at L = 4..12 within 2.3 combined errors (largest: S1e at L = 6, +2.3): PASS. (An earlier draft of this line said 1.7 before the deviations were computed; corrected at 12:05Z.)

### 5f. SU(2) beta 2.6, L = 14 and 16, and the verdicts at beta 2.6 (runs to 12:20:23Z; L = 14: 1200 configurations, L = 16: 800)

| L | S0e | S0o (winding) | S1e | S1o | R_J^top | E_flux (weighted tau 1-3) | floor 1/(2 beta E_flux) | Binder U | C4 max deviation |
|---|---|---|---|---|---|---|---|---|---|
| 14 | **0.1170 +- 0.0062** | 0.0311 +- 0.0007 | 0.1085 +- 0.0016 | 0.0281 +- 0.0003 | 0.117 (S0e) | 0.238 +- 0.028 | 0.81 +- 0.10 | -0.015 | 1.9 err |
| 16 | **0.1182 +- 0.0059** | 0.0239 +- 0.0008 | 0.1057 +- 0.0023 | 0.0227 +- 0.0004 | 0.118 (S0e) | 0.30 +- 0.11 | 0.65 +- 0.24 | -0.042 | 1.1 err |

(The E_flux and floor columns of the interim table 5e were first written from E_eff(tau) by eye (about 1.49, 1.42, 1.30, 1.28, 1.3); at 12:21Z they were replaced by the computed weighted plateaus of `analyze954.py`.) The flux energy starts to grow at L = 14-16 (Nambu-Goto with the recalled sigma: 0.21 and 0.25), and the Polyakov loops are disordered (Binder U about 0) from L = 12 on, as S2 placed L_c near 10.6.

**Verdicts at beta 2.6 (pre-stated rules).**
- C4: PASS at every L (largest deviation over all 28 sector comparisons: 2.3 combined errors, S1e at L = 6).
- S1: R_J^top = 1.542, 0.640, 0.246, 0.112, 0.118, 0.117, 0.118 for L = 4, 6, ..., 16. Fit over L >= 6: kappa = -1.81 +- 0.05 (not a power law: chi^2 306 for 4 dof; it falls, then is flat); R(16) - R(6) = -0.52 +- 0.03. **No GROWTH at beta 2.6 over L = 4..16 (GUIDE only).** Per sector over L >= 6: S0e kappa = 0.068 +- 0.052 (values 0.115, 0.107, 0.112, 0.118, 0.117, 0.118: flat); S1e kappa = 0.024 +- 0.022 (flat); S0o kappa = -3.50 +- 0.04; S1o kappa = -1.38 +- 0.02.
- S2: no growth to classify. The large values at L = 4-8 sit in the winding sector, in boxes at or below L_c (Binder U 0.42, 0.31, 0.18), as S2 anticipated; above L_c (L = 12-16) the top is the local sector, flat at 0.117-0.118.
- S3 (variational, box-local): R_J^top - 3 err exceeds R*_a on the 4^3 box for every a in {30, 40, 60, 100, 200}, on 6^3 for a in {30, 40, 60}, on 8^3 for a = 30; on 10^3 to 16^3 for no a (largest R_J^top - 3 err = 0.102 against R*_30 = 0.205).
- Floors (Lemma GAP-R, CONDITIONAL on row 947's unchecked (BR-gap) and Lemma J): the flux floor is 1.46, 1.42, 1.27, 1.17, 1.14 for L = 4-12 (errors 0.03-0.08), 0.81 +- 0.10 at L = 14, 0.65 +- 0.24 at L = 16. If GAP-R holds, every measured beta 2.6 box up to L = 14 has R_J above R*_a for a <= 100 (R*_100 = 0.630), through its light flux state. Box-local; the flux energy on the seed box is about sigma x 720, about 13.
