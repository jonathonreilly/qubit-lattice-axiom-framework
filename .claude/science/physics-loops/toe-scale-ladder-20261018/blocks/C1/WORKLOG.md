# C1 WORKLOG

## 2026-10-18 18:56 UTC — setup, model fixed from repo, criteria declared (before any production data)

**Model (supplied premise, read from repo).**
- `docs/THE_PURE_SPIN_HALF_LINK_MODEL_ON_THE_CUBIC_TORUS_IS_GAPLESS_..._2026-09-04.md` (Definitions):
  `E_e = Z_e/2`, `U_e = sigma^+_e`, `G_v = (div E)_v - rho_v`, and **`rho_v = 0` on every
  torus (z_v = 6 even)**; the staggered background `2rho = +-(-1)^i` is declared only on the
  2D *ladder* geometry, not on the cubic torus.
- `docs/RING_MODEL_BETWEEN_THE_ROKHSAR_KIVELSON_AND_PURE_RING_POINTS_..._2026-09-24.md` and its
  runner: `H = V D - g A` on the ice (3-in/3-out) configurations, A = plaquette-flip adjacency,
  D = number of flippable plaquettes. RK point V = g.
- `docs/RING_MODEL_THE_ZERO_WINDING_GAUSS_SECTOR_HAS_FROZEN_FLIP_COMPONENTS_..._2026-10-01.md`:
  sector = flip component of the canonical zero-winding state; frozen states exist on every even L.
- Exact L=2 anchors (from those notes, to be recomputed here): 9600 Gauss states, 937 flip
  components, largest 864 (zero winding); at V=0, g=1: E0 = -9.0267209135, internal gap 2.2257853859.

**Discrepancy with the task text.** The task says "the repo's staggered background charge
convention". On the cubic torus the repo convention is rho_v = 0 (no background). I use rho = 0
and report this. (Staggered background appears only for the 2D ladder.)

**Method decision (justified in NOTE).** A periodic (finite-T trace) worldline with local
plaquette-flip pair updates conserves, for every plaquette, the net signed number of flips over the
period; these integers form a class label (cube boundaries + three global plane classes) that local
updates cannot change, so a local finite-T code samples a class-restricted ensemble, not Tr e^{-bH}.
I therefore use an **open-path, guide-free (uniform trial state) continuous-time path-integral
projector (PIGS-type)**: the ends are free, so single-flip end moves change every class, and the
middle of the path samples |psi0|^2 exactly as T -> infinity with no importance function.
Projection time T plays the role of beta; scaled T = a L (z=1) and T = b L^2 (z=2).
A periodic-mode run at L=2 vs exact thermal ED is kept as a negative/ergodicity control.

**Prior exposure disclosed.** I have read titles/summaries of the repo RING_MODEL notes (guide-
biased projector results: e.g. reptation S at k_min 0.62(2) on 4^3, 0.50(2) on 6^3 with guide
exp(0.2 N_flip); 09-04 note title "quadratic transverse mode not a Maxwell photon", unverified).
Literature recalled (no numbers relied upon): pyrochlore quantum ice Coulomb phase at V=0
(Hermele-Fisher-Balents 2004; Banerjee et al 2008; Shannon et al 2012); cubic QDM (Sikora et al
2009/2011): Coulomb phase only in a window below RK, ordered at smaller V (I do not recall the
window edges reliably).

### Pre-declared comparison criteria (fixed now, before production)

Observables (per site, N_v = L^3), measured at the path middle:
- S_T(k) = sum_a <|E_a(k)|^2>/N_v (S_L = 0 exactly by Gauss), at k_min = 2pi/L (avg over axes).
  Exponent p(L1,L2) = ln[S_T(k1)/S_T(k2)] / ln[K1/K2], K = 2 sin(k/2).
  Expectation: quantum Coulomb p = 1; classical/RK-like p = 0; gapped/confined p = 2.
- Flippability Bragg weights: S_n(Q) = <|sum_v (n_{v,o} - <n>) e^{-iQ.v}|^2>/N_v summed over the
  3 orientations o (and per orientation), for all Q in {0,pi}^3 \ 0 (and (pi/2,..)-type when L%4==0);
  E-field S_aa(Q) at the same Q. Bragg ratio R_Q = [S(Q,L_max)/S(Q,L=4)] / [N_v(L_max)/N_v(4)].
- Photon gap: omega_eff(k_min) from the imaginary-time transverse-E correlator at the middle.

Verdict rules (each V separately; L_max = largest L reached with converged projection):
1. **Ordered** if some Q has R_Q >= 0.5 with its 2-sigma lower bound >= 0.4 (Bragg weight
   not decaying like 1/N), OR p(two largest L) >= 1.6 at 2 sigma (lower bound).
2. **Coulomb (consistent)** if all R_Q <= 0.25 at 2-sigma upper bound, AND p from the two largest
   L lies in [0.6, 1.4] (2-sigma interval overlapping and central value inside), AND omega_eff*L
   at the two largest L agree within 25% (z=1) better than omega_eff*L^2 does.
3. **RK-like/classical** if p <= 0.4 and no Bragg.
4. Otherwise **inconclusive at accessible L**.
Projection convergence: a point is used only if the z=1 and z=2 (or two different T) values of
S_T(k_min) and E/N_p agree within 2 combined sigma; otherwise flagged.
Errors: binning with bin-size scan; quoted error = plateau (largest of the last bins) of binned SE.
Validation pass criteria vs exact L=2 (open path, finite T): |QMC - exact| <= 3 sigma for every
checked observable; additionally all relative errors < 1% for E.

## 19:23 UTC — step 1 done; QMC built; a sampler bug found and fixed; validation re-running

- Step 1 (`scripts/step1_stoquastic.py`, `logs/step1_stoquastic.log`, TOTAL PASS=26 FAIL=0):
  off-diagonals are -g x {0,1} (stoquastic for g>0 by construction, no multiplicity, distinct plaquette
  link sets for L=2..12); diagonal gauge Lambda = {x-links, y+z even} U {y-links, z even} hits every
  plaquette an odd number of times for every even L (checked L=2..12, proved in NOTE), so
  D H(g) D = H(-g) on every Gauss/winding sector; independent GF(2) solve agrees (L=2,4,6), and for odd L
  (3,5) no diagonal gauge exists (plane-cycle obstruction, L^2 odd). L=2 exact: 9600/937/864 reproduced,
  E0(V=0) = -9.0267209135 reproduced, +g/-g spectra equal on all 937 components for V = 0, 0.5, 0.9.
- QMC: `scripts/qmc.py` (numba), `scripts/driver.py`. Open path, uniform trial both ends, pair
  insert/remove, shift, single-kink end moves.
- **Bug found by exact tests and fixed:** the first validation showed kink-count / kinetic estimators
  low by 1.5-3% (z up to -4.5 against the exact identity <n> = gT<N_f(end)> at V=0). Isolation:
  single-move transition rates matched a pure-Python reference exactly, but the *sweep* used a number of
  moves that depended on the current kink count; a state-dependent number of moves between
  measurements biases the sampled law. Fixed by freezing moves/sweep after thermalisation; the
  fixed-end-state P(n) histogram then matches the exact distribution (T=0.3: 0.1675/0.2002/0.2403 vs
  exact 0.1665/0.1998/0.2397). Also: the correlator check is only defined for tau <= T/2.
- Faster V-term integral `delta_toggle_fast` checked bit-identical to the reference on 8524 random
  nonzero intervals (logs/test_delta_fast.log). (No real speed-up; V != 0 is ~12x slower than V = 0.)
- Production queue A (V=0, L=4..12, T=2L and T=L^2/2-type checks) launched 19:22.

## 19:40 UTC — slow MC modes found; production restructured (multi-start seeds, symmetrised estimators)

- First validation (single chains) passed 8/9; the failure (V=0.9, T=8: S_T z=-4.5) was traced to
  underestimated errors: three fresh 150k-sweep chains give S_T 0.809(14), 0.785(11), 0.800(10) vs exact
  0.7913 and binned SEs that do not plateau (logs/dbg_v09.log). Validation now uses 4 independent chains
  per case and sigma = max(seed scatter/2, combined binned SE) (re-running, logs/step2_validate_L2.log).
- Periodic-trace local-move control vs exact thermal trace on the 864 component (L=2): energy -7.92 vs
  -9.02 at beta=4 (V=0), N_f z=+6.8 — the predicted class restriction is real and large.
- L=4, V=0 pilots (logs/dbg_tau_L4*.log, data/dbg_tau_*.npy): S_T(k_min) has a slow MC mode
  (autocorrelation tail ~0.1 decaying over ~3e4 sweeps), anticorrelated with N_flip (block corr -0.75).
  Flippability spectra are NOT cubic-symmetric within one chain (e.g. L=6 T=12: S_n(0,pi,0)=4.8 vs
  S_n(pi,0,0)=0.9): the chain keeps a pattern related to the (symmetry-breaking) canonical start.
  Consequences adopted (before looking at L>=8 data): (i) only cubic-star-symmetrised estimators are
  used for decisions: m2(star) = sum over the 3 Q's of a star and the 3 orientations of S_n(Q), / N_v;
  S_T averaged over the 6 k_min directions; (ii) every point is run from >=2 different starts
  (canonical state rotated 0/1/2 times by the cyclic axis permutation, seed s -> (s-1) mod 3) and the
  error is max(seed scatter, binned); (iii) agreement between starts is itself reported as a mixing check.
- The single-chain S_T(k_min) at L=4 depends on T (T=4: ~0.345, T=8: ~0.339, T=16: 0.268 seed 1); not
  yet known whether projection or mixing. To be resolved by the multi-start runs.

## 20:05 UTC — validation result; two-macrostate slow mode at L=4; whole-history update tried

- `logs/step2_validate_L2.log` (4 chains per case): TOTAL PASS=8 FAIL=1. The failure: V=0.9, T=3,
  end observables N_f(end) 8.0650(139) vs exact 8.1082 (z=-3.1) (mid observables pass). Follow-up with
  6 *fresh* chains (logs/dbg_vend.log): T=3: 8.1045(105) vs 8.1082 (z=-0.3); T=1: 8.1037(162) vs
  8.1043. Read: statistical (long autocorrelation near RK), not a V-term bug; the delta-integral code was
  also checked bit-identical to a reference implementation. Both results are reported, not replaced.
- Periodic local-move control: E = -7.95 vs thermal -9.02 (beta=4, V=0) — class restriction confirmed.
- Whole-history heat-bath update for one plaquette (V=0; forward-filter/backward-sample of the 2-state
  parity process given all other histories) implemented (`qmc.hist_update_V0`), exact P(n) at L=2
  reproduced (logs: printed in session; dbg_hist.py). It does NOT remove the slow mode at L=4 T=8
  (autocorr ~0.1 at 2000 sweeps) and costs ~10x per sweep -> not used in production.
- Diagnosis of the slow mode (dbg_modes.py, L=4 T=4): block means switch between two macrostates of
  equal kink number (equal energy within noise): (A) higher N_flip (0.328/plaq) with enhanced
  flippability Bragg weight at X = (pi,0,0)-type (orientations containing the Q axis) and enhanced
  E-field weight at R/M; (B) lower N_flip (0.312) with larger S_T(k_min). Interpretation deferred.
- Production restructured: queue A3 (V=0: L=6..12, rotated-canonical starts s=1,2 and "RK-typical"
  random-walk starts s>=11) and B2 (V=0.5/0.9 controls, both start types). Hysteresis between start
  types at fixed (L,T) is a pre-declared mixing diagnostic; for chains stuck in different macrostates the
  lower-energy one is the better ground-state estimate (energy comparison declared now, before data).

## 20:27 UTC — first multi-start results (L=4,6) and the electric-winding energy test
(Clock note: the entry headed "20:05" was actually written ~19:57.)
- Added a robust, guide-free observable: E0(W=1) - E0(W=0) from the mixed estimator (a Rayleigh
  quotient, exact in expectation, and the one estimator on which chains from different starts agree).
  Pre-declared reading (stated now, before L>=8): Coulomb ⇒ dE ∝ 1/L (dE*L → const);
  confined ⇒ dE ∝ L (string tension, dE/L → const).
  L=4 (T=8): dE = 0.676(63), dE*L = 2.71(25); L=6 (T=12): dE = 0.440(102), dE*L = 2.64(61).
- Middle observables keep a memory of the start: L=6 T=12, S_T(k1) = 0.185 / 0.248 / 0.369 for the
  canonical / rotated / RK-walk starts, X-star flippability Bragg 0.031 / 0.011 / 0.013, while E_mid agree
  (-0.2880(4), -0.2893(4), -0.2894(5)) and E_mix agree (-0.28938, -0.28905, -0.28942). The middle-state
  structure factors are NOT equilibrated at L>=6 within 1e5 sweeps; they will be reported as per-start
  ranges, not as converged values.

## 22:25 UTC — L=8,10 results
- Middle observables at L=8 keep the start: S_T(k1) = 0.154 (canonical) vs 0.392 (RK-walk), M-star
  flippability Bragg 0.0145 vs 0.0047 per site; L=8 T=32 canonical chain: E_mid = -0.2795(1) vs
  E_mix = -0.28904(9) — the middle is grossly out of equilibrium (E_mid must equal E_mix in expectation).
  => Bragg/S_T criteria of the pre-declared list CANNOT be evaluated (mixing failure, not physics).
- Electric-winding gap (mixed energies; chains from different starts agree): V=0, T=2L:
  dE = 0.676(63), 0.440(102), 0.161(120), 0.505(252) for L = 4,6,8,10.
  Fits (scripts/winding_fit.py): A/L: A = 2.64(23), chi2 = 3.0/3; A/L + sigma L: sigma = -0.010(16);
  sigma L only: chi2 = 49.6/3 (rejected). T-convergence concern: L=8 E_mix(T=32) - E_mix(T=16) =
  -0.17(15) total, same order as dE(L=8); W=1 at T=32 pending.
- V=0.9: dE(L=8) = -0.119(48) < 0 — not physical for a converged ground state comparison; read as
  insufficient projection near RK (soft k^2 modes need T ~ L^2). V=0.5 only L=4,6.
