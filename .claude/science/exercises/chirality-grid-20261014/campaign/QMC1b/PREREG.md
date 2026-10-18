# QMC-1b PREREG: is the GPR-like signal set by the corner filter?

Written 2026-10-17, finished before any gate or production run (time stamp at the end). Worker: Claude Opus 5.5 at
xhigh (same family as every packet agent; not independent). Never edited after the stamp; follow-ups are appended.

## 0. Inputs read

- Fixed item: TESTS.md "Campaign wave 3" (branch claude/chirality-grid-exercise-20261014), QMC-1b, TESTS.md:667-678.
- campaign_common.txt; SUMMARY.md; docs/MINIMAL_AXIOMS_2026-06-29.md (in full, read-only).
- QMC-1: campaign/QMC1/REPORT.md, PREREG.md (sections 1-6, follow-ups A-J headers), scripts afqmc.py, runner.py,
  analysis.py, readout.py, validate_a.py, ed_exact.py, ed_reduced_gate3.py, run logs.
- QMC-1 referee: ref_QMC1/REFEREE.md and REFEREE_VERDICT.md (verdict CONFIRMED WITH CORRECTIONS, reading OPEN; E2/E3/E3w
  are not gap estimators; E3w's bound holds only as a symmetric-window average, REFEREE.md:211-224; the mirror propagator
  should average the 32 components, REFEREE.md:169-175; binning dropped the remainder, REFEREE.md:263-267).
- Panel E strategy lens: campaign/panel_E/strategy/statement.md:42-56, 112-118, 139-146 (why f_Gamma; X2' puts the
  light content at Gamma with a filter vanishing only there).
- Step 0 prior art on main (`git grep` for Golterman/Petcher/Eichten-Preskill/symmetric mass generation/AFQMC/filtered
  quartic): docs/SPIN10_SYMMETRIC_ATOMIC_GAPS_..._2026-09-14.md:1-40, 70-100 (an on-site Spin(10) atom with a unique
  symmetric ground state: the atomic-limit comparator, not a filtered lattice simulation);
  docs/NATIVE_WEYL_LOCAL_INTERACTION_COVARIANCE_BOUNDED_THEOREM_NOTE_2026-09-13.md:391 ("a general filtered quartic is
  not automatically in that class"). Nothing on main simulates a momentum-filtered quartic; the only prior simulation
  is the unmerged QMC-1 (campaign/QMC1), which this item reuses.

## 1. Fixed item (verbatim, TESTS.md:667-678)

- Setup. QMC-1's engine and scope. Compare f_Gamma = (2 - cos p_x - cos p_y)/4 with a rerun of f2. L = 4 and 6,
  beta = 4, dtau = 0.05, W in {2, 4}, at least 200 sweeps. Gates (i)-(iv) are re-passed first.
- Precondition (not a gap claim). A suppressed window: E3w <= 0.1 at both L.
- FILTER-SENSITIVE: for f_Gamma, some window W has an S10/L^2 L6/L4 ratio <= 0.75 and at least 2 sigma below 1, while
  f2 gives >= 0.85.
- FILTER-ROBUST: both filters give >= 0.85 at every window W.
- OPEN: otherwise.
- Neither reading establishes a gap, SMG or GPR.

## 2. Model (QMC-1's, unchanged except the filter)

Ungauged X2 matter Hamiltonian analogue, global Spin(10), lambda1 = 0, 2+1D periodic L x L, L in {4, 6}:
H = sum_k psi_k^dag (sigma_x sin k_x + sigma_y sin k_y) psi_k + W sum_x Q_x, Q_x = -(1/4) sum_a (Bh^a Bh^a + h.c.),
Bh^a = (1/2) psi_S^T (i sigma_y x N^a) psi_S, psi_S(x) = sum_y f(x - y) psi(y) (QMC-1 PREREG section 1).
32 complex modes per site. All four corners (0,0), (pi,0), (0,pi), (pi,pi) are free zero modes (sin = 0).

Filters (real, symmetric taps):
- f2 = (1 + cos p_x cos p_y)/2 (QMC-1's): taps 1/2 on site, 1/8 on the 4 diagonals. Zeros exactly at (pi,0), (0,pi)
  (light). Mirrors (0,0), (pi,pi), both f2 = 1. rho = sum taps^2 = 5/16.
- f_Gamma = (2 - cos p_x - cos p_y)/4 (code name "fG"): taps 1/2 on site, -1/8 on the 4 nearest neighbours. Zero only
  at Gamma = (0,0) (light; f = |q|^2/8 near Gamma). Mirrors (pi,pi) with f = 1 and (pi,0), (0,pi) with f = 1/2.
  rho = 5/16 (same as f2, so the vertex normalisation and local coupling scale match). Five taps, same cost as f2.
- Gate (iii) only, 1+1D: g1 = (1 - cos p)/2 ("g1"), taps 1/2, -1/4, -1/4 (exercises negative taps, as f_Gamma has);
  light corner p = 0. QMC-1's f1 = (1 + cos p)/2 is re-run too.

## 3. Engine

QMC-1's engine is copied into QMC1b/scripts (afqmc.py, runner.py, analysis.py, readout.py, x2model.py, ed_exact.py).
Same frame, Fierz point kappa = (sing8v 1.5, trip8v -0.5, 0, 0), 64 HS channels per vertex, pCN vertex moves,
Woodbury updates, pivoted-QR stabilisation every 0.4 in imaginary time, det(1 + M_d) weight.

Changes (disclosed; before this PREREG I ran only engineering checks, no observable was read: two one-sweep timing
profiles at L6 f2 W2 printing time and acceptance, prof/prof_L6*.out; a benchmark on random matrices, prof/bench.out;
and the equivalence check below):
- (a) Lattice: filters "fG" and "g1" and their corner sets (mirror/light) added; nothing else in the model touched.
- (b) Speed, arithmetic-identical: the kinetic step's spatial DFT is a dense N x N matmul instead of np.fft; the
  Woodbury update G <- G - (G F^T) K (F (1 - G)) is done in place by BLAS zgemm. Check `equiv_check.py`: with the same
  seed and Lattice, 2 sweeps at L4, W = 2, dtau = 0.05, n_s = 8, both f2 and fG, the new and the unmodified QMC-1 engines
  give identical accept counts (2186/2560, 2176/2560), identical fields, and final G equal to 1.9e-13
  (`equiv_check.out`). PASS.
- (c) Planned speed change, MCMC-valid but not arithmetic-identical: alternating upward and downward sweeps (the
  downward sweep builds the left stack incrementally, so the full left-stack rebuild after every sweep disappears). The
  local update, ratio and Woodbury formulas are unchanged; only the visiting order of vertices alternates. Acceptance
  rule for using it: (c1) wrapped-vs-fresh G deviation <= 1e-6 at every stabilisation point of both sweep directions
  in a test at L4 f2 and fG W = 2; (c2) gate (iii) passes with it. If either fails, or it is not ready by 12:30Z,
  production uses QMC-1's upward sweeps. Which one is used is recorded in a follow-up before production starts.
- (d) Diagnostics thinning: the secondary equal-time diagnostics S(pi,pi) and <W Q> are measured every 4th measured
  sweep (S10 at Q = 0 and the mirror/light propagators every sweep). No reading uses them.

## 4. Gates (re-passed before any production run; QMC-1 PREREG section 4 definitions)

- (i) W = 0: engine G(tau, k) equals the analytic free G at every k and tau, <= 1e-10: f2 L4, fG L4, fG L6.
- (ii) Every weight real and positive: (ii-a) full weights det(1 + M) on random prior-scale fields, 2D L4 fG, beta = 1,
  W = 4: |phase| <= 1e-8, slice matrices commute with T2; (ii-b) in every production run the max |arg ratio| over all
  proposals <= 1e-8 (a run violating it is discarded and reported).
- (iii) Finite-W exact check, reduced flavours (1 s + 1 c flavour, D = 4), 1D ring L = 3, W = 2, beta = 2, dtau = 0.05,
  against psi-frame ED (`ed_exact.py`): filters f1 (QMC-1's point) and g1 (negative taps). 6000 measured sweeps each
  (eqt_points 5, kinetic on), same engine and sweep schedule as production. Observables: W<Q> from the HS channels
  (WQc), sum_a (S_X + S_Y), E_kin. PASS = every observable within 2 sigma (binning error, 20 bins) of ED for both
  filters. If an observable misses by more than 2 sigma, one rerun at dtau = 0.025 is made and PASS then needs
  agreement within 2 sigma there; otherwise the gate fails and the reading is OPEN (validation not passed).
- (iv) Light corners: per configuration, |v_k^dag G(tau, 0) v_k - 1/2| <= 1e-8 at every light corner and tau, in every
  production run (fG: Gamma; f2: (pi,0), (0,pi)). Also checked in the gate (i) runs.

## 5. Production

Parameters: beta = 4, dtau = 0.05 (L_tau = 80), n_s = 8 (stabilisation and the tau grid every 0.4: tau = 0, 0.4, ...,
4.0), n_hit = 1, initial pCN step 0.3 adapted (target acceptance 0.35-0.65) during the first 80% of the warm-up
only. Warm-up 20 sweeps at L4 and 10 at L6 (cost); then 200 measured sweeps. Equal-time S10 at tau = beta every sweep.

W = 0 references (one sweep, no updates, deterministic): fG and f2 at L4 and L6, for the free S10/L^2.

Order (one process at a time, driver `production.sh`):
1. L4: fG W4, f2 W4, fG W2, f2 W2 (seeds 41004, 42004, 41002, 42002).
2. L6 queue, built mechanically by `queue_b.py` from the L4 results, in the order fG W4, f2 W4, fG W2, f2 W2 (seeds
   61004, 62004, 61002, 62002), keeping only (filter, W) points whose L4 E3w (primary, below) is <= 0.1 (a point that
   fails at L4 cannot be a window). One data-dependent skip, which cannot change the reading: the fG W2 L6 run is
   skipped if fG W4 already satisfies the fG clause of FILTER-SENSITIVE (a window with ratio <= 0.75 and >= 2 sigma
   below 1); this frees time for f2 W2. The queue is re-evaluated after every L6 run.
3. Wall clock: production stops at 22:35Z (runner --tmax per run). A run with fewer than 200 measured sweeps is
   reported as incomplete and cannot enter a mechanical reading; if a reading depends on it, the reading is OPEN
   (budget), stating which run.

Budget estimate (QMC-1 timings, sweeps at dtau = 0.05: L4 ~5-6.5 s, L6 ~40-46 s): L4 total ~1.3 h; one L6 run 2.3-2.8 h.
Four L6 runs may not fit before 22:35Z; that is why the queue order and skip rule are fixed here.

## 6. Observables and estimators

- S10/L^2 = (1/N^2) sum_a [<(sum_x X_x^a)^2> + <(sum_x Y_x^a)^2>] (QMC-1's `structure`, component sum), N = L^2.
- Ratio R(filter, W) = [S10/L^2](L6) / [S10/L^2](L4); sigma_R by error propagation from independent runs.
- Errors: binning over all 200 measured sweeps. sigma = max(error with 20 bins of 10 sweeps, error with 10 bins of 20
  sweeps) (conservative against autocorrelation). Integrated autocorrelation time reported (Sokal window).
- E3w (precondition only): 2 cosh(beta E/2) x mean over the symmetric grid points in [1, beta - 1] (tau = 1.2, 1.6, 2.0,
  2.4, 2.8) of the mirror propagator G_m(tau), E = 1, central value. The bound holds for the symmetric-window average
  (REFEREE.md:211-220); it bounds low-energy mirror spectral weight; it is not a gap.
  - PRIMARY G_m: average over all mirror corners and over all 32 components (s and c blocks equally; 16 + 16), per
    REFEREE.md:169-175. f2: (0,0), (pi,pi). fG: (pi,pi), (pi,0), (0,pi).
  - Reported, not used for the reading: s block only (QMC-1's definition); each corner class separately
    (fG: (pi,pi) [f = 1] and (pi,0)/(0,pi) [f = 1/2]); E3w with 2 sigma added.
- Window: (filter, W) is a window iff primary E3w <= 0.1 at L4 and at L6.

## 7. Readings (mechanical, from the completed runs)

Let Win(f) be the set of W in {2, 4} that are windows for filter f.
- "f2 gives >= 0.85": Win(f2) is non-empty and R(f2, W) >= 0.85 (central) at every W in Win(f2). (Reading of the fixed
  text adopted here. The alternative "at the same W as the f_Gamma window" is also reported; if the two disagree, the
  report says so, and the mechanical reading uses the definition fixed here.)
- FILTER-SENSITIVE: some W in Win(fG) has R(fG, W) <= 0.75 and (1 - R)/sigma_R >= 2, and f2 gives >= 0.85.
- FILTER-ROBUST: Win(fG) and Win(f2) are both non-empty and R >= 0.85 (central) at every W in Win(fG) and in Win(f2).
- OPEN: otherwise, naming the reason (no fG window; f2 below 0.85 at a window; fG ratio between the thresholds;
  budget; validation).
- A window whose L6 run is incomplete is treated as unknown: a reading stands only if it holds for every possible value
  of the unknown runs; otherwise OPEN (budget).

## 8. Secondary reports (no reading)

Free S10/L^2 and its L6/L4 ratio per filter; Spin(10) anisotropy (fraction of S10 in the (9,10) plane; isotropic 0.2);
S(pi,pi)/L^2; acceptance; max phase; light deviation; wrap deviation; E2 effective decay scale (not a gap); drift by
thirds; comparison with QMC-1's f2 numbers (dtau = 0.1 / 0.05, 45-60 sweeps).

## 9. Scope (stated with every headline)

Ungauged 2+1D analogue of the X2 lambda1 = 0 matter Hamiltonian, global Spin(10); filters f2 and f_Gamma; periodic
L = 4 and 6; beta = 4 (finite temperature; Mermin-Wagner forbids true continuous order); dtau = 0.05 (no dtau -> 0
extrapolation); single chains of 200 measured sweeps; binning errors. Neither reading establishes a gap, SMG or GPR,
and pilot sizes cannot decide the thermodynamic limit or 3+1D.

## 10. Memory and process rules

Every computation through `zsh scripts/capped.sh OUT python3 ...` (1.5 GB cap, 2 BLAS threads); one process at a
time; peak RSS of QMC-1's L6 dtau = 0.05 run was 0.95 GB. All my processes are killed and checked with
`ps -axo pid,rss,command | grep -i python` before I return. Data (npz, logs) archived in scripts/runs/.

Stamp: PREREG completed 2026-10-17 at 11:40Z (from `date -u`). No gate or production run had started.

## Follow-up A (11:50Z, before any production run)

- Gates re-passed (all PASS), with the production engine and sweep schedule:
  - (i) W = 0 free G at every k, tau: f2 L4 4.9e-15, fG L4 4.9e-15, fG L6 6.4e-15; light-corner dev <= 4.9e-15;
    filter symbols equal their formulas to 2.2e-16 (scripts/runs/gates_i_iia.out).
  - (ii-a) fG L4 random prior-scale fields: |phase| <= 1.6e-14; T2 B T2^-1 = B to 8.4e-16 (same file).
  - (iii) reduced flavours, 1D L = 3, W = 2, beta = 2, dtau = 0.05, 6000 sweeps, alternating sweeps: f1 0.09, 1.30,
    0.26 sigma; g1 (negative taps) 1.61, 1.06, 0.61 sigma for W<Q>, sum S, E_kin (scripts/runs/gate3_compare.out).
  - (iv) is monitored per configuration in every production run.
- Engine change (c), alternating sweeps, ADOPTED: (c1) wrapped-vs-fresh <= 1.0e-12 in both directions at L4 f2/fG W = 2
  (scripts/test_alternate.out; rerun scripts/test_alternate2.out after the memory edit below); (c2) gate (iii) above.
- Memory edit (no arithmetic change): in alternating mode, consumed left/right-stack entries are released, so only
  about one stack is alive; L6 fG W = 4 up + down test: peak RSS 0.89 GB, wrap deviation 5.4e-11
  (scripts/test_mem_L6.out). The L6 sweep took ~26 s there (lighter machine load than the earlier profile).
- The driver runs queue_b.py through capped.sh too. Production (scripts/production.sh) starts now.
- Note: while appending this follow-up, unquoted backticks in my shell heredoc were evaluated as commands; each failed
  with "no such file or directory" (relative paths), so nothing ran. Text corrected in the same minute.

## Follow-up B (12:40Z): supplementary runs after the fixed queue (cannot change the fixed reading)

- Seen so far: only the driver/queue log. The queue printed fG W4 L4 primary E3w = 0.1818 > 0.1, so fG W4 is not a
  window (PREREG 5.2); the queue then started L6 f2 W4. No other L4 observable has been read.
- Added, to run only after the fixed queue is empty (driver scripts/supplementary.sh, started by a waiter when
  production.sh logs "driver done"; one process at a time):
  - S1: fG at W = 8, L4 (seed 41008, warm 20) then L6 (seed 61008, warm 10), same beta, dtau, n_s, 200 sweeps. The L6
    run is made only if the L4 primary E3w <= 0.1.
  - S2: f2 at W = 8, L4 (42008) then L6 (62008), same rule, as the matched control.
  - An L6 supplementary run starts only if at least 2.3 h remain before 22:35Z; otherwise skipped.
- Supplementary readout: the same windows, ratios and errors as PREREG section 6, labelled SUPPLEMENTARY (W = 8 is
  outside the fixed W in {2, 4}). It is reported next to the fixed reading and cannot change it.
- Also reported (already registered in section 6): per-corner E3w for fG, (pi,pi) [f = 1] against (pi,0)/(0,pi)
  [f = 1/2], to say which mirrors are unsuppressed.

## Follow-up C (14:02Z): conditional fG W = 16 (supplementary; before any W >= 8 data)

- Seen since follow-up B: only the queue log. fG W2 L4 primary E3w = 1.134 and fG W4 = 0.182, both > 0.1, so f_Gamma
  has no window in the fixed set; the fixed reading will be OPEN (no fG window) whatever f2 gives. L6 f2 W4 completed
  (200 sweeps; its observables not yet read); L6 f2 W2 is running (its L4 E3w passed).
- Supplementary order (scripts/supplementary.sh, restarted; the waiting copy had started nothing): S1 fG W8 (L4, then
  L6 if window); S3 only if S1's L4 is not a window: fG W16, L4 (seed 41016) then L6 (61016) if window; then S2 f2 W8
  (L4, L6 if window). Same rules as follow-up B (2.3 h needed to start an L6 run). All SUPPLEMENTARY.

## Follow-up D (18:44Z): W = 8 supplementary runs fail gate (ii-b); rerun with n_s = 4

- All fixed runs and supplementary runs are complete (200 measured sweeps each); readout in scripts/runs/readout_final.out.
  The fixed reading is mechanically OPEN (no fG window: L4 E3w 1.134 at W = 2 and 0.182 at W = 4).
- Gate (ii-b) as registered (max |arg ratio| <= 1e-8; a violating run is discarded and reported) fails for all four
  W = 8 supplementary runs at n_s = 8: max phase 4.4e-7 (L4 f2), 5.9e-8 (L4 fG), 2.7e-7 (L6 f2), 2.3e-7 (L6 fG); wrap
  deviation up to 7.8e-7. These are roundoff growth over 8 strong slices (QMC-1 used n_s = 2 at L4 W = 8). They are
  DISCARDED; their files stay archived as L*_W8.* and are reported only as discarded. Every W in {2, 4} run passes
  (max phase <= 9.8e-10, light dev <= 1.0e-13).
- Rerun (supplementary, same rules as follow-up B otherwise): fG and f2 at W = 8, n_s = 4 (stabilisation every 0.2;
  tau grid 0.2, so the E3w window uses tau = 1.0, 1.2, ..., 3.0, still symmetric), 200 measured sweeps, warm-up 20
  (L4) / 10 (L6), seeds 41108, 42108 (L4), 61108, 62108 (L6). Order: L4 fG, L4 f2, L6 fG, L6 f2. Stop at 22:35Z; an
  incomplete run is reported with its sweep count. Output names L*_*_W8ns4.*. Peak memory estimate at L6 with
  21 stack entries: about 1.35 GB (under the 1.5 GB cap).
- Same readout as follow-up B; gate (ii-b) and (iv) applied again.

## Follow-up E (22:32Z): close

- All runs ended; no process of mine is running. Final readout: scripts/runs/readout_final2.out (fixed section
  identical to readout_final.out). Fixed reading: OPEN (no f_Gamma window at W in {2, 4}).
- W = 8 reruns at n_s = 4 pass gate (ii-b) (max phase <= 1.1e-9). L6 f2 W8 stopped at 171 measured sweeps (wall clock;
  machine slowed to 35.9 s/sweep): incomplete, reported as such. Supplementary only.
