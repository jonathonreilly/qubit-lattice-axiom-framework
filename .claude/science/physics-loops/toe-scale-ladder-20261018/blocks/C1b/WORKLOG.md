# C1b WORKLOG (finite-T QMC with non-local updates, cubic spin-1/2 link ring model)

## RESUME INSTRUCTIONS (read first after a container restart)
- All code in scripts/, outputs in data/ and logs/. Every job is < 20 min, writes checkpoint files
  data/ckpt_*.npz and appends results to data/*.jsonl. Status of each step is in the "Status" section below.
- To resume: read "Status"; re-launch the listed command for any job without a final result line.

## Model (named premise, same as C1)
L^3 even torus, spin-1/2 per link, E=sigma/2, Gauss law div E = 0 (rho=0 on the cubic torus: the
"staggered background" is a ladder-only convention, see C1 NOTE §1). H = -g sum_p (U_p+U_p^dag) + V sum_p n_p,
g=1, V=0 primarily. g>0 -> stoquastic in sigma^z basis without gauge (C1 Thm 1; review: gauge D only for g<0).
Even L only.

## Algorithm plan (declared 2026-10-19 before any code)
Continuous-time path integral for Tr e^{-beta H} over the FULL Gauss sector (all windings, all flip components).
Write -g sigma^x_p (on the 2-dim circulating subspace) = -2g |+><+|_p + g n_p.
Augmented configuration: base state + F events (flips, weight g) + P markers (diagonal |+><+| graph,
weight g, only on circulating plaquette-time) with weight (g beta)^(nF+nP) exp(-g beta Ibar),
Ibar = int_0^1 N_circ(u) du. Integrating P markers gives back exactly (g beta)^nF (V=0).
Updates per sweep:
 1. Gibbs resample of P markers (Poisson process, rate g on circulating intervals) - exact heat bath.
 2. Swendsen-Wang-type plaquette clusters: every vertex (P or F) binds its 4 lower legs and its 4 upper
    legs; link worldline segments connect vertices. Each cluster flip keeps every vertex valid, toggles
    P<->F for vertices touched on one side (this changes the net-flip class n_p, removing C1 Lemma 3's
    class restriction), keeps nF+nP; accepted with Metropolis exp(-g beta dIbar) and only if the new base
    state is Gauss-legal. Partition depends only on vertex positions -> sequential Metropolis is DB.
    Global E->-E reversal (exact symmetry) added.
 3. Static directed-loop moves (Barkema-Newman ice loops) on links whose 4 plaquettes carry no vertex
    (uniform choice among available outgoing links; proposal symmetric), Metropolis exp(-g beta dIbar).
    These change electric winding (wrapping loops); effective at small beta.
 4. Parallel tempering in beta (config in u=tau/beta units, marginal weight (g beta)^nF):
    swap acceptance min(1,(b_j/b_i)^(nF_a - nF_b)). Carries winding changes and decorrelated flux
    configurations from high T down to beta = L.
Estimators: E = -<nF>/beta; W_a = sum E_x over a cross-section plane (integers); P(W); S_T(q) equal-time
(averaged over several tau slices); N_circ.

## Pre-declared criteria (declared 2026-10-19, before any production data; no L>=4 data seen by this block)
V1 (validation, L=2 exact over all 9600 Gauss states): at beta in {0.5,1,2,4} (and PT ensemble), E, <W^2>,
   <N_circ>, P(W=0) agree with exact within 3 sigma (binned errors, >=2 seeds). A failure is reported as is.
EQ (equilibration, per production point): >=2 independent PT runs from different starts (canonical,
   rotated-canonical/random-loop-scrambled); E, <W^2>, S_T(q1) agree within 2.5 sigma; >=10 PT round trips
   (lowest<->highest beta) per run counted. Points failing EQ are reported as not equilibrated, not used for verdicts.
Physics (V=0, beta = L, also beta = L/2 from the same ladder):
 K(L) = <W_a^2> averaged over a=x,y,z.  Define a(L) = L * dF1, dF1 = -(1/beta) ln[ P(|W_a|=1) / (2 P(W_a=0)) ]
 (sector free-energy gap per quantum).
 C-W (Coulomb): finite electric stiffness <=> a(L) bounded: weighted linear fit a(L)=a0+s*L over available L
   has |s| consistent with 0 within 2 sigma AND K(beta=L) at the largest L >= 0.02 (resolvable).
 X-W (confined, string tension sigma): dF1 ~ sigma*L => a(L) grows ~ L^2: fit s > 0 at > 3 sigma and
   K(L) decreasing by more than a factor 2 per DeltaL=2 at the largest L.
 Otherwise: inconclusive.
 S_T exponent p from S_T(q_min=2pi/L) at the two largest L (as C1): Coulomb p in [0.6,1.4];
   gapped/confined p >= 1.6; classical/RK-like p <= 0.4; otherwise inconclusive.
 Secondary (not a verdict input): E(beta) at L=8 compared to C1 (-443.83(14)) and repo (-443.364(31))
   ground energies; E(beta) is an upper estimate of E0 only up to thermal excitation; reported as such.

## Status
- [x] code: scripts/ctqmc.py (numba kernel), scripts/sim.py (PT driver), scripts/run_pt.py (resumable chunk runner)
- [x] exact L=2: scripts/exact_L2.py -> data/exact_L2.json (9600 states, 937 comps, E0=-9.0267209135 matches repo/C1)
- [~] validation L=2 PT: tags val2_s1, val2_s2 (see Log 02:40)

## Log
- 01:32 worklog + criteria declared.
- 01:45-02:35 debugging at L=2 (scratch tests, not kept as runners):
  * first version: E(beta=1) biased (-4.89 vs -4.976). Found that single plaquette-clusters are often Gauss-illegal
    alone (static charges); added "super-cluster" merging of charged clusters (+ vertex-free links) at the tau=0
    sites (partition invariant under flips -> DB kept). Conditional DB of cluster phase verified by enumeration of
    visited configurations at fixed vertex positions (chi2/dof ~ 1, scratch t14/t16); loop proposal symmetry
    verified exhaustively in pure Python (t18); dIbar bookkeeping verified against recomputation (t8);
    Gibbs marker intensities verified (t24). Apparent residual biases in single-beta runs traced to slow mixing
    between flip components / windings (seed scatter large); PT validation is the decisive test.
- 02:40 launched PT validation (L=2, 11 betas 0.1..4, 15 min each):
    cd scripts; python3 run_pt.py val2_s1 2 1 canonical 0.1,0.18,0.25,0.35,0.5,0.7,1.0,1.4,2.0,2.8,4.0 15 2000 1
    (and val2_s2 ... 2 2 scrambled ...). Re-running the same command continues from data/ckpt/<tag>.npz.
- 02:58 val2 (PT, 300k sweeps x2, 2000 round trips) FAILED: E biased at beta=1,2,4 (z up to 27).
  Diagnosis (02:59, scratch t28): sum_p n_p^2 of the net-flip class never takes the value 6 -> elementary
  CUBE classes (n = +-boundary of a cube) are never generated. Reason (proved by inspection): a single
  plaquette cluster's time-slice set S(tau) can only change by ADDING a plaquette boundary disjoint from S
  or REMOVING one contained in S (SW binding of all 4 legs of a vertex side), so sweeping a cube (which needs
  XOR with shared links) is impossible. Plane classes do occur.
  Fix: new move cube_moves (ctqmc.py): three consecutive events on three distinct faces T of a cube (no
  other event on any plaquette touching the cube links in between, window not wrapping u=0) are relabelled,
  same times, to the complementary faces T' in a uniformly chosen valid order; equal weight; acceptance
  min(1, N'/N). V=0 only. val2 result kept in logs/validate_L2_val2.log (superseded).
- 03:02 launched val3 (same command as val2 with tag val3_s1/val3_s2) with cube moves on.
- 03:35 val3 PASSED: logs/validate_L2_val3.log  TOTAL: PASS=25 FAIL=0 (E, <W^2>, P(W=0), N_circ, S(pi) at
  beta=0.25..4; 1519+1558 round trips; both starts). Code state = current ctqmc.py/sim.py (cube moves on).
  Validation rule unchanged from declaration (3 sigma, max(binned, seed-scatter) error).
- 03:35 production settings (declared before any L>=4 production data; pilots at L=4,6 seen only for
  timing/acceptance and one L=4 beta=8 energy -0.293/plaquette, consistent with C1's E0/N_p=-0.2930):
  ladders data/ladders/L{4,6,8}.txt (ladder.py L 0.15 bmax 1.0 0.27 1.2; bmax = 8, 6, 8 for L = 4, 6, 8;
  beta = L and L/2 on every ladder). Measure every 2 sweeps, thermalisation 2000 (L4) / 1000 sweeps, and the
  analysis discards the first 20% of measurements. Two runs per L: canonical start and loop-scrambled start
  (different seeds). Errors: 20 bins per run; combined = max(binned, seed scatter).
  Queues: scripts/queue.sh jobs_A.txt A ; scripts/queue.sh jobs_B.txt B  (restart-safe: just relaunch both
  with nohup; each chunk is 15 min and checkpoints in data/ckpt/).
- 03:40 (before looking at any L>=4 production observable; only chunk bookkeeping seen: L4_s1 chunk0 =
  9499 sweeps, 10 round trips) ESTIMATOR ADDENDUM, declared now:
  PT round trips are slow (~1 per 950 sweeps at L=4), so the direct estimate of P(|W_a|=1)/P(W_a=0) at
  beta=L has few independent samples. Added a second estimator of the SAME declared quantity dF1:
  Z_S(beta) = sum_{s in S} <s|e^{-beta H}|s> for S0={W_a=0}, S1={|W_a|=1} (unions of conserved sectors), so
  d ln Z_S/d beta = -<H>_S exactly and
     ln[Z_S1/(2 Z_S0)](beta) = ln[P1/(2 P0)](beta_min) - int_{beta_min}^{beta} (E_S1 - E_S0) dbeta'
  (thermodynamic integration over the PT ladder with sector-conditional energies, trapezoid rule, errors
  from 20 time bins with bin-wise jackknife). Criteria C-W / X-W are applied to BOTH estimators; if they
  disagree the point is reported as inconclusive. (Implemented in scripts/ti.py.)
  Also: run_pt now records full observables (S, Nc) only at beta in {bmin, L/2, L, bmax}; E and W at all betas.
  L6 ladder regenerated (ladder.py 6 0.3 6 1.0 0.27 1.3, 40 betas) before any L6 run started.
- 03:42 TI estimator check at L=2 (val3 data): trapezoid on the coarse 11-point L=2 ladder gave dF1(beta=2)
  1.4046(64) vs exact 1.4294 (3.9 sigma: quadrature error). Switched quadrature to cubic spline
  (TI_QUAD=spline default in ti.py; decided on L=2 validation data only, before any production analysis).
  logs/validate_TI_L2.log: TOTAL: PASS=10 FAIL=0 (TI and direct dF1 at beta=0.25..4).
- 03:55 L4 after 2 chunks/run (15 trips each): EQ check fails narrowly (<W^2> at beta=L=4 start-diff
  z=2.62 > 2.5; |W|=2 visits only in run 1). Not used for verdict yet; 2 more chunks per run appended to
  the queues (after L6). Runs L6_s1/L6_s2 started 03:54.
- 04:12 L6 chunk 0: 3500 sweeps/15 min, 0-1 round trips per run. PT at L=8 (76 betas, est. ~600 sweeps per
  chunk) is not feasible in the remaining budget -> L=8 winding/S_T measurement dropped (operational).
  Queue plan (appended to jobs_A/B.txt): L6 6 chunks -> L4 to 4 chunks -> L6 to 10 chunks -> L8E (single
  beta=16 at L=8, 2 chunks, two starts) for a one-sided check of the 8^3 ground energy:
  <H>_beta >= E0(global) for every beta, so a thermal energy significantly below -443.364 would show the
  repo guided-projector value lies above the true ground energy (declared before running).
- 04:41 status: L6 3 chunks/run (trips 1 and ~6). Preliminary look (not a verdict): W distribution at
  beta=L=6 is walker-dominated (13-16 distinct W vectors visited; P(|W|=2) 2.5% vs 28% between runs) ->
  EQ fails so far. Queues continue automatically. RESUME: if the container restarted, relaunch
    cd scripts; nohup ./queue.sh jobs_A.txt A >/dev/null 2>&1 & nohup ./queue.sh jobs_B.txt B >/dev/null 2>&1 &
  (completed chunks are skipped by counting data/raw/TAG_c*.npz).
- 05:27 L6 after 6 chunks (trips 9/13): EQ still fails on <W^2> at beta=6 (z=-2.91); run L6_s2 never visits
  W=(0,0,0) at beta=6 (marginal P0=0.57 per direction) -> walker-dominated winding populations. E and S1
  agree between starts. Post hoc diagnostics script scripts/posthoc.py (dF1 along ladder, dF2/dF1, S2/S1,
  E|W=000) written; its outputs are labelled post hoc in the NOTE.
- 05:58 KEY FINDING (drift diagnostic scripts/drift.py, per 15-min chunk): at L=4 the winding populations
  at beta >= L are still drifting after 27/24 round trips: P(|W_a|=1) at beta=8 went 0.14 -> 0.10 -> 0.005
  -> 0.000 (run 1) and 0.23 -> 0.07 -> 0.001 -> 0.002 (run 2); at beta=4 0.32 -> 0.07 / 0.36 -> 0.11.
  Both starts drift TOGETHER, so the declared EQ test (start agreement + >=10 trips) passes while the data
  are non-stationary: the declared EQ test is insufficient; W-observables at beta >= L are NOT equilibrated
  at L=4 or L=6 (L=6 chunk values of P1 at beta=6 scatter 0.06-0.57). At beta = L/2 = 2.05 (L=4) P1 is
  stationary across chunks (0.44-0.49). The L=6 queue was stopped after chunk 6/7 completes (operational:
  winding mixing at L=6 is far from converged); remaining time: L8E (2 chunks/start) then L4 to 8 chunks
  per run to test whether the L=4 drift stops. New queues: scripts/relaunch2.sh -> queue.sh jobs_A2.txt A2,
  queue.sh jobs_B2.txt B2 (RESUME: relaunch those two queue commands with nohup if the container restarted).
- 06:13 size limit: raw L=2 validation measurement files (val2/val3, 125 MB) moved out of the block to the
  session scratchpad; 20-bin summaries kept in data/val_bins_L2.npz (scripts/save_bins.py). The validation
  logs were produced from the full raw files before the move. L6 stopped at 7 chunks per run (15/13 trips).
  L8E_s1/L8E_s2 (L=8, single beta=16) started 06:10.
- 06:35 SECOND KEY FINDING: L8E (L=8, beta=16 single replica) ran into W=(0,0,-16) and (-11,0,0) with
  E = -388 / -407 (ground ~ -443.8); configs valid (check_config=0). Reproduced at L=4, beta=8 (scratch
  t31): in the FIRST sweep from the event-free start, W jumped 0 -> 7. Cause: every replica starts with
  n_F = 0, where all base states have equal weight (gβ)^0 = 1, so the static loop move randomises W freely
  before events build up; once events are dense, W is frozen at low T. This is correct detailed balance but
  a pathological initial condition (metastable high-W trapping), and it explains the excess winding at low T
  and the slow monotone drift of P1 seen in the L4/L6 PT runs (walkers initialised with large W must be
  expelled by PT). The L4_s1/s2, L6_s1/s2 production data are therefore compromised by the initialisation
  and are NOT used for verdicts (kept and reported as such). L8E_s1/s2 discarded (killed in chunk 1).
  FIX (thermalisation only, does not change the stationary dynamics): no static loops at beta > 1 during the
  first NOLOOP_SWEEPS sweeps (sim.PT.noloop_sweeps; env NOLOOP_SWEEPS in queue.sh). Check at L=4,
  beta=8, seed 1: E/N_p -> -0.29, W stays 0.
  New runs (06:37): queue.sh jobs_C.txt C and jobs_D.txt D with NOLOOP_SWEEPS=2000:
    L4_s3 (canonical, 3 chunks) -> L8E_s3 (canonical, beta=16, 2 chunks)
    L4_s4 (mixW_rot: alternate replicas W=0 / W=(1,0,0) rotated canonical, 3 chunks) -> L8E_s4 (2 chunks)
  RESUME: cd scripts; export NOLOOP_SWEEPS=2000; nohup ./queue.sh jobs_C.txt C & nohup ./queue.sh jobs_D.txt D &
- 06:55 L4_s3/s4 chunk 0: P1(beta=4) = 0.016 (W=0 start) vs 0.25 (half-W=1 start); populations at
  beta >= L still start-dependent -> brackets. Changed queue D second job from L8E_s4 to L6_s4 (mixW_rot,
  2 chunks) to get sector-conditional energies at L=6 for the TI estimator (which needs equilibration only
  within sectors, not of the sector populations). L8E then has one start only (L8E_s3).
- 07:22 L4_s3/s4 done (3 chunks, 11/13 trips). Declared EQ fails at beta=L=4 (W2 z=-3.0, S1 z=-2.2).
  Per-chunk P1(beta=4): s3 0.016 -> 0.088 -> 0.058 ; s4 0.253 -> 0.175 -> 0.055 (last chunks agree,
  approached from both sides). beta=L/2=2.05: P1 0.39-0.43 in all chunks of both runs; dF1_direct
  0.510(34) / 0.500(28). L8E_s3 and L6_s4 running until ~07:52.
- 07:53 final runs done. L8E_s3 (beta=16, 6.4k sweeps): E = -443.36 +- >=0.4 (sub-run means -444.8..-442.3):
  not discriminating C1 vs repo. L6_s4 (2 chunks, 0 trips): P1(beta=6) 0.123 -> 0.018, still relaxing;
  S_T(q1,beta=6)=0.2254(33) vs compromised 0.2447(20) -> S_T also biased by the winding artifact.
  Final analysis logs: logs/analysis_L4_clean.log, analysis_compromised_L4_L6.log, analysis_L6_s4.log,
  drift.log, ti_estimates.log, posthoc.log, energy_L8.log. VERDICT (declared criteria): INCONCLUSIVE
  (EQ fails at beta=L for L=4,6; L=8 PT infeasible). NOTE.md written. No jobs running. Block complete.
- review applied to NOTE.md (Review dispositions section added).
