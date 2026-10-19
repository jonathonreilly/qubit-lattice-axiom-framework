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
