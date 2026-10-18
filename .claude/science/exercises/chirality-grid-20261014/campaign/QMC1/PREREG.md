# QMC-1 PREREG — sign-free AFQMC pilot of X2's mirror gapping

Written 2026-10-15 00:5xZ (clock at start of writing: 00:42Z), before any run.
Agent: Claude Opus 5.5 (same family as every packet agent; not independent).
Fixed readings: TESTS.md "24-hour campaign, wave 1", QMC-1 (packet branch
origin/claude/chirality-grid-exercise-20261014, TESTS.md:322-339). They are copied
below and are not changed here; this file only makes them operational.

## 0. Inputs used (read in full before writing)

- X2 model and lemmas: combos/X2/COMBO_REPORT.md:53-68 (law), :90-95 (X2-L2), :111-114 (X2-L5).
- K1 G1/G2 and GPR: kills/K1/KILL_REPORT.md:158-206.
- NT-3 and referee: next/NT3/REPORT.md, REFEREE_VERDICT.md (literal TG1-BROKEN; soft 6-vector mode near the filter zero; mirror gap not established).
- SIGN-1 and referee: panelwork/SIGN1/REPORT.md:62-72, REFEREE_VERDICT.md, referee/REFEREE_REPORT.md
  (Kramers pair T2 = i sigma_y K, T1 = (1 x i Gamma^9) T2, U(1)_c; lambda1 = 0 Fierz identity with
  Re coefficients (-34,+2,-2,+2), Im opposite; full trace det(1+M_d)/sqrt(det M_d); R = 0 at lambda1 = 0; rank 12).
- Prior art on main (step 0): docs/SPIN10_SYMMETRIC_ATOMIC_GAPS_MIRROR_BOUNDARY_PROJECTION_AND_CURRENT_RESPONSE_BOUNDED_THEOREM_NOTE_2026-09-14.md
  (an atomic projector Spin(10) singlet with exact gap; not the BB+h.c. quartic, no QMC). No QMC/DQMC code for
  SMG exists on main (grep for DQMC / auxiliary-field / Hubbard-Stratonovich / symmetric mass generation / Kramers positivity).
- docs/MINIMAL_AXIOMS_2026-06-29.md read in full (233 lines). Nothing here is axiom content; the model is supplied (X2 price table, COMBO_REPORT:208-220).

## 1. Model (supplied; ungauged; global Spin(10); lambda1 = 0)

Per site: psi_{s,alpha}, s in {up,dn} (walker spinor), alpha in 16 of Spin(10) (real Cl(9) gammas of SIGN-1 common.py:16-46;
N^a = Gamma^a for a = 1..9, N^10 = i*1). 32 complex modes per site.

H = sum_k psi_k^dag (sum_{a=1}^d sigma_a sin k_a) psi_k + W sum_x Q_x,
Q_x = -(1/4) sum_{a=1}^{10} ( Bh^a(x) Bh^a(x) + h.c. ),  Bh^a(x) = (1/2) psi_S(x)^T (i sigma_y x N^a) psi_S(x),
psi_S(x) = sum_y f(x-y) psi(y).

(Normalisation fixed here: Bh^a = psi_up^T N^a psi_dn is a sum of 16 unit-amplitude pairs. lambda2 = -1/4 in units of Bh;
the sign of lambda2 is immaterial by psi -> e^{i pi/4} psi, SIGN-1 REPORT:50.)

Geometries (periodic boundary conditions, L even so the light corners are lattice momenta):
- 1+1D: walker sigma_x sin p. Filter f1(p) = (1 + cos p)/2: zero only at p = pi (light corner), f1(0) = 1 (mirror corner);
  real space 1/2 on site, 1/4 on each neighbour; isotropic quadratic zero f1 = q^2/4 (same shape as X2's f_F1).
- 2+1D: walker sigma_x sin p_x + sigma_y sin p_y. Filter f2(p) = (1 + cos p_x cos p_y)/2: zeros exactly at the hw1
  corners (pi,0), (0,pi) and nowhere else; f2 = 1 at both mirror corners (0,0) and (pi,pi); Hessian 1/2 * identity at hw1
  (f2 = |q|^2/4), the 2D analogue of X2's f_F1 (COMBO_REPORT:61-66). Real space: 1/2 on site, 1/8 on the four diagonal neighbours.
  Reason for not using (cos p_x + cos p_y)/2: it vanishes on the whole lines p_x +- p_y = pi, leaving a line of exactly free
  modes (the f_NN-cone analogue); f2 isolates exactly the hw1 corners.
- Control (power reference): f == 1 (on-site, unfiltered) at the same sizes. In the control the light corners are NOT
  protected (it is the EP-like on-site channel); it is the SMG power reference only.

## 2. Algorithm (choice and justification by cost)

- Frame: d-frame of SIGN-1: d = psi on 8_s (Gamma^9 = +1), d = psi^dag on 8_c. Every HS slice conserves d-number (U(1)_c)
  and commutes with T2 restricted to the d-frame (T^2 = -1). Weight per field configuration
  w = e^{-phi^2/2} det(1 + M_d) / sqrt(det M_d) (referee form); since all HS operators are traceless the denominator is a
  constant and the sampled weight is det(1 + M_d) >= 0 (Kramers pairs (lambda, conj lambda)).
- det = |det_sector|^2: allowed only if a unitary symmetry of every slice splits the d-space into two sectors exchanged by
  T2. With the full Fierz decomposition the only slice symmetries are U(1)_c and T2 (and T1 = i T2 on the d-frame), so the
  factorisation is NOT available in general; I will check this and say so, and use the full complex d-frame determinant.
- Decomposition at lambda1 = 0: sum_a Bh^a Bh^a = sum_f kappa_f sum_{e in f} P_e P_e with U(1)_c-neutral pairings
  P_e = psi_s^T (tau x Y_e) psi_c (families sing/trip x 8v/56v of SIGN-1). Since (Re P)^2 - (Im P)^2 = (P^2 + P^dag^2)/2
  exactly, Q = -(1/2) sum_f kappa_f sum_e [(Re P_e)^2 - (Im P_e)^2] with NO remainder (R = 0). Sign rule (Kramers):
  coefficient <= 0 on T2-even channels (real field), >= 0 on T2-odd (imaginary field).
  Free choice fixed here: among sign-correct Fierz points (2-dim affine family, SIGN-1 p6 output) I take the one that
  minimises the HS noise sum_f |kappa_f| n_f ||O_f||^2 (an LP; the minimiser is a vertex, so fewer channels). If that LP
  fails, the SIGN-1/referee point (-34,+2,-2,+2) is used. The chosen identity is verified exhaustively on all
  C(32,4) = 35,960 four-annihilator components (relative residual <= 1e-12 required).
- HS: per vertex (slice l, site x) one exponential exp(F_x^dag h_{l,x} F_x), h = sum_e kappa_e phi_e O_e, kappa_e =
  sqrt(2 dtau W |c_e|) (times i for c_e > 0). With F_x F_x^dag = rho 1, exp(F^dag h F) = 1 + F^dag [(e^{rho h} - 1)/rho] F
  (rank 32). Slice: B_l = prod_x E_{l,x} e^{-dtau K}. Errors: Trotter + non-commuting HS, O(dtau^2) per slice.
- Updates: continuous Gaussian fields, per-vertex preconditioned Crank-Nicolson moves phi' = sqrt(1-s^2) phi + s xi
  (prior-reversible, acceptance = min(1, det ratio)), ratio and Green-function update by 32x32 Sherman-Morrison-Woodbury.
  Why not HMC: HMC needs the adjoint Frechet derivative of every vertex exponential at every MD step plus a full
  stabilised forward/backward pass per step (~6 N_d^3 L_tau per step, 10-20 steps per trajectory); local vertex moves cost
  ~2 N_d^3 L_tau acc per sweep and reuse the rank-32 structure. Why not single-field discrete updates: 64-512 fields per
  vertex x one 32x32 expm each is python-overhead bound; one pCN move per vertex (or a few) is cheaper per decorrelation at
  pilot sizes. (Cost model with numbers in the report.)
- Stabilisation: QR(pivoted)-UDV stacks every n_s slices (n_s = 4 initially; reduced if the wrap-vs-recompute
  deviation exceeds 1e-6), upward sweeps with the left stack rebuilt each sweep.
- dtau = min(0.1, 0.4/W); beta = 4 in 2+1D at both L (beta = 4 in 1+1D). Trotter check (see gate) at one strong W.

## 3. Measurements

- S10(L) = (1/N) sum_{x,y} sum_{a=1}^{10} < X^a(x) X^a(y) > + same for Y, X = Re Bh_S^a, Y = Im Bh_S^a (filtered vertex
  operators, the interaction channel), at Q = 0 (K1 B4: the uniform condensate leads). Also reported separately: X and Y
  parts, a <= 8 versus a = 9,10 (their per-component difference measures the dtau-induced Spin(10) -> Spin(8) x U(1)_c
  breaking of the decomposition), and Q = (pi,pi) (2D) / pi (1D) as a secondary.
- Mirror single-particle gap: G_psi(tau, k) at k = (0,0) and (pi,pi) (2D), k = 0 (1D), averaged over the 32 components,
  tau on the stabilisation grid. Gap Delta from a fit A cosh(Delta (tau - beta/2)) on tau in [1, beta - 1]; jackknife over
  bins. Free value Delta = 0 exactly (sin = 0 at the mirror corners), so any Delta > 0 is interaction-made.
- Light-corner G_psi(tau) at hw1 (2D: (pi,0),(0,pi); 1D: pi). Free value 1/2 at every tau.
- Average sign/phase: max relative phase over every accepted and proposed ratio, and of the full weight at every
  stabilisation recompute.
- Energies <H_W>, <W Q> (validation).
- Errors: binning (bins of >= 10 sweeps, >= 8 bins), integrated autocorrelation estimate from bin-size growth reported.

## 4. Validation gate (fixed, TESTS.md:330-334); must pass before any production reading

- (i) W = 0: engine G(tau, k) equals the analytic free G at every k and tau to <= 1e-10.
- (ii) every sampled weight real and positive: max relative phase <= 1e-8 over all ratios and recomputed weights in all
  validation and production runs (production runs that violate it are discarded and reported).
- (iii) finite-W exact check: reduced flavour content run through the same engine and channel builder: 1 s-flavour + 1
  c-flavour (D = 4 d-modes per site: walker spin x {s, c}), interaction Q_red = -(1/2) sum_f kappa_f sum_e [(Re P_e)^2 -
  (Im P_e)^2] with the singlet and triplet 1v families (kappa_sing = +1, kappa_trip = -1/3, sign-correct), on the 1D ring
  L = 3 with f1 and the walker, beta = 2, W = 2. Exact method: full ED in the psi-frame Fock space (4096 states) built
  independently from the psi-frame operators. Observables: <W Q> and the uniform singlet-pair structure factor.
  PASS = QMC agrees with ED within 2 sigma (statistical) at dtau = 0.05, and the dtau = 0.1 value is reported with its
  Trotter shift. This reduced model is not Spin(6)/SU(4) (no real Cl(5) 4x4 structure exists for the same code path);
  it is stated as a reduced-flavour engine check. In addition the full Spin(10) Fierz identity is checked exhaustively
  (Section 2) and Spin(10) weights at a small cluster are checked for positivity and Kramers pairing.
- (iv) even L, finite W: light-corner G(tau) equals the free value 1/2 (X2-L2); per configuration to <= 1e-8.

## 5. Production and readings (FIXED wording; operational definitions here)

Production: 2+1D L = 4 locator scan W in {0.5, 1, 2, 4, 8} for f2 and the f == 1 control; then L = 6 at three W chosen
by rule: W_lo = largest locator W with the f2 mirror gap closed, W_mid = smallest with it open, W_hi = the next locator W
(if the gap never opens or is open at all W, the three largest / smallest W). Same W for the control at L = 6 if time
allows (at least one). 1+1D: L = 8 and 16 at W in {1, 4} (validation and NT-3 comparison only; no reading from 1D).

Definitions: "mirror gap open" at (L, W): Delta - 2 sigma > max(0.2, 4/beta). "stable within errors between L = 4 and 6":
|Delta(6) - Delta(4)| <= 2 sigma_comb. "S10/L^2 decreases": S10(6)/36 < S10(4)/16 by more than 2 sigma_comb.
"flat or growing": S10(6)/36 >= S10(4)/16 - 2 sigma_comb.

FIXED readings (TESTS.md:335-338):
- SMG-PILOT: in 2+1D there is a W window where, between L = 4 and L = 6, the mirror gap is open and stable within errors
  and S10/L^2 decreases.
- GPR-PILOT: in 2+1D, at every W where the mirror gap is open, S10/L^2 is flat or growing between L = 4 and 6.
- OPEN: otherwise, including "sizes cannot separate" and "validation not passed in budget"; state which.

Operational note (not a change): with a decreasing S10/L^2 a symmetric gapped phase would give S10(6)/S10(4) ~ 1
(ratio of S10/L^2 = 16/36 = 0.44); long-range order gives S10/L^2 flat (ratio 1). I will report the ratio
R = [S10(6)/36]/[S10(4)/16] with error at each W, and the control's R at the same W.

Scope to be stated with every headline: ungauged, global Spin(10), lambda1 = 0, f2 filter, L = 4, 6 periodic, beta = 4,
dtau as stated, binning errors; pilot sizes cannot decide the thermodynamic limit or 3+1D.

## 6. Deliverables

Code in scripts/ (documented), validation outputs, production npz, cost model for 2+1D L = 8-12 and 3+1D, and what
dynamical G_SM links require. Memory: every run through scripts/capped.sh (1.5 GB), one process at a time.

---

## Follow-up A (2026-10-15 11:22Z)

- **Gap.** Work stopped at about 00:47Z (supervisor session ended) and resumed at 11:22Z. Nothing of mine was
  running at resume (checked with ps). New deadline 18:30Z (coordinator). Nothing above is changed.
- **Only run before the gap:** scripts/x2model.py -> x2model.out (algebra, no QMC). It applied the pre-registered
  LP rule of Section 2: chosen Fierz point kappa = (sing8v +1.5, trip8v -0.5, sing56v 0, trip56v 0), exhaustive
  relative residual 1.04e-15 on all 35,960 four-annihilator components, signs as required (nonzero families strictly
  inside: +1.5 >= 0, -0.5 <= 0). This gives 64 HS channels per vertex (Re/Im of 8 singlet + 24 triplet 8v pairings),
  instead of 512 at the SIGN-1 max-margin point. Kernel dimension 2 (consistent with SIGN-1 p6 and the referee).
- The reduced model's interaction is NOT taken from fierz() (its "fierz" line in x2model.out is meaningless: the
  reduced vector observable is not a sum of the 1v families); it is fixed as pre-registered: kappa_sing = +1,
  kappa_trip = -1/3.

## Follow-up B (2026-10-15 11:38Z)

- Validation part A (scripts/validate_a.py -> validate_a.out) passed: gate (i) to 1e-13; W = 0 Wick measurement code
  equals ED to 1e-16 (reduced model); Spin(10) slices commute with T2 to 1e-15, slice spectra conjugation-closed, weight
  phases <= 2.3e-14 on prior-scale random fields (a stress test at 4x prior scale gave 1.2e-8 at log|w| ~ 1900, a
  roundoff effect outside the sampled regime, reported not hidden); Fierz identity in expectation to 4e-14.
- Gate (iii) run 1 (runs/*_run1_wrongWQobs.*): S_X, S_Y per component and E_kin agree with ED, but the recorded
  "WQ" was the vector-channel energy -(1/4) sum_a (Bh Bh + h.c.), which for the REDUCED model is not its interaction
  (the reduced interaction is defined by the kappa families; the two coincide only for Spin(10), checked in A3).
  This is an observable-definition mismatch, not a change of the test: the runner now also records WQc =
  <W sum_e c_e O_e^2> (the simulated interaction), and gate (iii) compares WQc and S_X, S_Y with ED as pre-registered.
  Run 2 repeats both dtau values unchanged.
- Process note: scripts/fierz_points.py (algebra only, ~3 s, ~100 MB) was run once without capped.sh while the gate (iii)
  run 1 was in progress (two processes for ~3 s). Deviation from the memory rule; no effect on results. It found that
  the sign-correct Fierz polygon has three vertices: (sing8v 1.5, trip8v -0.5) [chosen], (sing8v 0.9, trip56v -0.1),
  and (sing8v 1.25, sing56v 0.25) [singlet only].

## Follow-up C (2026-10-15 11:56Z) — before any production run

- Gate (iii) PASSED (runs/gate3_dt005.log, analysis): reduced flavours, 1D L = 3, f1, W = 2, beta = 2.
  dtau = 0.05: WQc = -0.1338(6) vs ED -0.13438 (1.0 sigma); S10 sum = 0.5631(5) vs ED 0.56382 (1.4 sigma);
  E_kin = -2.4215(1) vs ED -2.42148. dtau = 0.1: WQc -0.1341(5), S10 0.5640(5), E_kin -2.4214(1): Trotter shift below
  statistical error.
- Engine speed fix (einsum -> BLAS contractions; tree product of the vertex core): validate_a rerun identical
  (validate_a_v2.out); tree vs loop core agree to 1.9e-15 (check_tree.out).
- Exploratory 2D L = 4 short runs (12 sweeps; runs/explore_*): free S10(Q0) = 8.65 (f2, W = 0). f2: W = 0.25
  nearly free (G_m(beta/2) ~ 0.48), W = 1 G_m(beta/2) ~ 0.1, W = 4 G_m ~ 0. Control f == 1 has a local interaction scale
  ~1/rho^2 ~ 10x larger than f2 at the same W (W Q per site ~ -75 at W = 1), and at W = 4 with dtau = 0.1, n_s = 4 the
  stabilisation FAILED (wrap-vs-fresh 1.8e-2, ratio phase 4.6e-3 > 1e-8): that run violates gate (ii) and is discarded.
- Locator additions (additions only; readings and rules unchanged): f2 locator W in {0.25, 0.5, 1, 2, 4, 8} (0.25 added
  so the closed side is bracketed). Control locator at its own scale: W in {0.05, 0.1, 0.25, 0.5, 1} (the PREREG's
  control W = 2, 4, 8 are deep strong coupling for f == 1 and need n_s = 1 and dtau << 0.1; dropped for budget, stated).
  n_s = 2 wherever W >= 4 (f2) or W >= 0.5 (control); any run with max ratio phase > 1e-8 is discarded and reported.
- Run lengths (budget): L = 4: 20 warm + 60 measured sweeps; L = 6: 15 warm + 45-60 measured sweeps. Errors: binning
  at 20 bins, with the 80/40/20-bin error levels reported to show whether autocorrelation is captured.

## Follow-up D (2026-10-15 12:23Z) — after the f2 L = 4 locator W <= 4, before any L = 6 run

- **Estimator failure (declared).** The pre-registered gap estimator (unweighted cosh fit on tau in [1, beta-1]) fails
  once the mirror propagator has decayed into noise by tau = 1: W = 2 gives 3.1 +- 1.1 (so "closed" by Delta - 2 sigma > 1
  although G_m(beta/2) = 0.003), W = 4 gives 49.6 +- 13.5 (noise fit). I keep it and report it, and ADD two estimators,
  reported side by side (the fixed readings are applied with each; if they disagree the reading is stated per estimator):
  (E2) weighted cosh fit (weights 1/sigma_bin^2) on tau in [0.4, beta - 0.4];
  (E3) model-independent low-energy spectral-weight bound from G(beta/2) = int A(w) / (2 cosh(beta w / 2)), A >= 0,
       int A = 1 (ensemble average): the mirror weight below |w| < 1 is at most w_1 = 2 cosh(beta/2) G(beta/2).
       "Open (E3)": w_1 + 2 sigma < 0.1.
- **L = 6 W choice.** The mechanical rule with the failed estimator would pick {2, 4, 8}; with E2/E3 it picks {1, 2, 4}
  (W = 1 is the borderline-closed point: E1 1.05(7)). I run {1, 2, 4} first and add 8 if time allows. Deviation stated.
- **Spin(10) anisotropy diagnostic.** At W = 2, 4 the charged components a = 9, 10 (the U(1)_c plane) carry S_X ~ 15-24
  each versus ~1-6 for a <= 8. The decomposition is exact (Fierz) and each HS factor is exact; the only Spin(10) -> Spin(8)
  x U(1)_c breaking is the Trotter ordering, O(dtau). A large component asymmetry therefore signals a large order-parameter
  susceptibility pinned by a small explicit anisotropy (or slow directional mixing). The readings use the component sum
  (as pre-registered). Added check if time allows: W = 2, L = 4 at dtau = 0.05 (component split and total).
- **Process.** analysis.py was run a few times outside capped.sh while a QMC run was active (each < 100 MB, ~2 s);
  from now on analysis also goes through capped.sh.

## Follow-up E (2026-10-15 12:40Z) — after the f2 L = 4 locator, L = 6 W = 2 running, no L = 6 result seen

- E2 also fails at W = 8 (fit collapses; G_m falls to noise by tau ~ 0.3). E3 (single point G(beta/2)) is noise-limited.
  Added E3w: the same rigorous bound with the window average, w_1 <= 2 cosh(beta/2) mean_{tau in [1, 3]} G_m(tau)
  (valid because the kernel e^{-tau w}/(1 + e^{-beta w}) >= 1/(2 cosh(beta/2)) for |w| <= 1 and all tau in [0, beta];
  it needs the averaged spectral function to be >= 0, true for the Hamiltonian ensemble, up to O(dtau) Trotter effects).
  Readings are reported per estimator E1 (pre-registered), E2, E3, E3w. E1 is the pre-registered one; the others are
  declared post hoc and only decide whether the E1 reading is robust.
- Free references (exact, W = 0): S10(Q0) = 8.65 at L = 4 and 10.60 at L = 6 (S10/N = 0.541, 0.294; ratio 0.54).
- Queue after the L = 6 f2 runs: control L = 4 (5 W), a dtau = 0.05 repeat of f2 W = 2 at L = 4 (Spin(10)-anisotropy
  check: S_{9,10}/S10 rises from 0.20 (isotropic value 2/10) at W <= 1 to 0.60-0.71 at W >= 2), control L = 6 (>= 1 W),
  1+1D runs, in that order, as time allows.

## Follow-up F (2026-10-15 14:20Z) — control L = 6 choice, after control L = 4 W <= 0.25

- Seen so far (no reading computed yet): f2 L = 6 at W = 1, 2, 4; control L = 4 at W = 0.05, 0.1, 0.25.
- Control L = 6 W: 0.25 (control L = 4: E2 gap 1.53(4), S10/N jumps 5.2 -> 28.7, U(1)_c-plane fraction 0.67) and 1
  (strong coupling; exploratory L = 4 S10/N ~ 11-17, i.e. below the W = 0.25 value). Both at n_s = 4 (memory at L = 6;
  follow-up C asked n_s = 2 for control W >= 0.5; gate (ii) is monitored and a violation discards the run).
- The f2 L = 6 W = 8 run uses dtau = 0.05 with n_s = 8 (same 0.4 stabilisation interval and memory as the other L = 6 runs).

## Follow-up G (2026-10-15 14:31Z)

- check_sector.out: with the singlet-only Fierz vertex (sing8v 1.25, sing56v 0.25) in 2+1D (f2 and f == 1),
  J_d = (-1)^{x+y} sigma_z x diag(1_s, -1_c) commutes with every slice (3.5e-17) and T2 J_d T2^-1 = -J_d, so
  det(1 + M) = |det(1 + M_+)|^2 with half-size sectors (checked: equal log dets to 1e-10). Not available with the
  production vertex (triplet x, y channels; commutator 0.42) nor in 3+1D (walker uses all three Pauli matrices).
  Production is NOT switched (mid-campaign); this is the recommended cluster configuration.
- Control L = 4 at W = 0.5, 1 seen: S10/N falls from 28.7 (W = 0.25) to 17.9 and 7.8, components isotropic again at
  W = 1, staggered S(Q = (pi, pi)) grows to 131. Added after the 1D f1 runs: f2 L = 4 W = 16 (dtau = 0.4/W = 0.025)
  to see whether the filtered S10 turns over at strong coupling (K1 gap G1). 1D control runs moved last.

## Follow-up H (2026-10-15 15:21Z) — f2 L = 6 complete; dtau check done; control L = 6 running

- f2 2+1D readings computed (scripts/readout.py -> runs/readout_mid.out), per estimator: E1 (pre-registered) OPEN (no W
  where E1 resolves an open gap at both sizes: the fit fails once G_m decays into noise before tau = 1); E2, E3, E3w
  GPR-PILOT (open at W = 2 (E2) / W = 4, 8 (E3w) / W = 8 (E3); S10/L^2 ratio L6/L4 = 0.98(5), 1.35(26), 0.87(10)
  at W = 2, 4, 8, all "flat or growing" by the 2 sigma rule; nowhere "open and decreasing").
- dtau check (W = 2, L = 4): dtau = 0.05 gives S10/N = 3.60(6) vs 3.23(12) at dtau = 0.1 (+11%, 2.7 sigma) and gap E2
  2.72(10) vs 2.61(13); the U(1)_c-plane fraction S_{9,10}/S10 falls from 0.60 to 0.21 (isotropic value 0.20). So the
  component anisotropy at dtau = 0.1 is a Trotter artefact; it does not create the large total S10 (the total is
  larger at smaller dtau). The L4/L6 ratios are computed at equal dtau = 0.1 (W <= 4) and 0.05 (W = 8); their Trotter
  shift is not measured.

## Follow-up I (2026-10-15 15:41Z)

- Control L = 6 at W = 0.25 seen: S10/N 22.7(2.1) vs 28.7(1.1) at L = 4 (ratio 0.79(8)); E2 gap 1.50(3) vs 1.53(4);
  U(1)_c-plane fraction 0.84 (dtau = 0.1 pinning).
- Added at the end of the queue: f2 L = 6, W = 2 at dtau = 0.05 (n_s = 8; 10 warm + up to 30 measured sweeps, wall-clock
  cap 35 min) so the key L4/L6 ratio at W = 2 can be formed at dtau = 0.05 too (L = 4 counterpart: L4dt_f2_W2_dt0.05).

## Follow-up J (2026-10-15 17:00Z) — all runs finished; nothing of mine running

- Final tables and readings: scripts/runs/readout_final.out; autocorrelation: scripts/runs/autocorr_final.out.
- Readings (f2, 2+1D, L = 4 vs 6): E1 (pre-registered) OPEN; E2, E3, E3w GPR-PILOT; no estimator finds an SMG window.
- L = 6, W = 2 at dtau = 0.05 (30 sweeps): S10/N 4.11(80) vs L = 4 3.60(6): ratio 1.14(22) (flat); E2 gap 4.1(8) vs
  2.72(10); U(1)_c-plane fraction 0.85 at L = 6 (0.21 at L = 4), so the directional pinning at L = 6 persists at dtau = 0.05.
- f2 L = 4 W = 16: S10/N 4.78(21) (W = 4, 8: 4.69, 5.28): plateau, no strong-coupling turnover (control: S10/N falls
  from 28.7 at W = 0.25 to 7.8 at W = 1).
- 1+1D f1 (L = 8 -> 16): W = 1 S10 unchanged (59.1 -> 60.4), E2 gap 2.01(6) -> 2.04(6); W = 4 S10 x1.59, gap >> 1.
- tau_int(S10) <= 1.3 sweeps for all f2 runs (crude Sokal estimate from 45-60 sweeps); control W = 1: 4.4 (L = 4), 2.9
  (L = 6), so its binning errors are underestimated by up to ~2x.
- Max watchdog RSS over all runs 0.99 GB; no run was capped.
