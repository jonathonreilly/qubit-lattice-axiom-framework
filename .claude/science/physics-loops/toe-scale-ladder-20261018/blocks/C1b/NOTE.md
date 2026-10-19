# C1b — Finite-temperature plaquette-cluster + parallel-tempering QMC with winding-changing moves for the cubic spin-1/2 link ring model: exact L=2 validation passes; winding populations at β ≥ L do not equilibrate at L ≥ 4 in budget, so the pre-declared Coulomb/confined verdict is INCONCLUSIVE

**Block:** `toe-scale-ladder-20261018 / C1b`. This is the decisive follow-up that C1 §10 recommended: a
finite-T QMC with non-local, winding-changing updates.
**Claim types:**
- [THM] a proof, or an exhaustive check;
- [NUM] numerical evidence from this block's code;
- [EXT] a result from elsewhere in the repo, not re-verified here;
- [VERDICT] a pre-declared criterion applied as declared;
- [POST HOC] a diagnostic not declared before the data were seen.

**Status:** unaudited block output. No independent check has been done yet (§9).
**History:** every timestamp is in `WORKLOG.md`. The criteria were declared at 01:32 UTC, the production
settings at 03:35, and the estimator addendum at 03:40. All three predate any L ≥ 4 production observable.

---

## 0. Bottom line

1. **The method is sign-free and exact for Tr e^{−βH} over the whole Gauss sector, and it is validated at L=2**
   [NUM]. Its components are continuous-time plaquette clusters (Swendsen–Wang type, with diagonal projector
   markers), static winding loops, a new cube move, and parallel tempering in β. Validation was against brute-force
   enumeration and diagonalisation of all 9600 Gauss states:
   - `logs/validate_L2_val3.log` gives **TOTAL: PASS=25 FAIL=0**. It covers E, ⟨W²⟩, P(W=0), N_circ and S(π) at
     β = 0.25 to 4.
   - `logs/validate_TI_L2.log` gives **TOTAL: PASS=10 FAIL=0**. It covers both winding free-energy estimators.
2. **Two algorithmic results, found by the validation itself** [THM + NUM]:
   - **(a)** SW-type plaquette clusters alone can never generate the elementary-cube classes of the net-flip
     2-cycle (C1 Lemma 3). A cluster's time-slice set can only gain plaquette boundaries that are disjoint from it,
     or lose ones that it contains. This produced an 8–27σ bias at L=2. A 3↔3 cube-relabelling move fixes it (§2).
   - **(b)** Starting from an event-free path causes pathological winding trapping. At n_F = 0 every base state has
     the same weight, so the winding loops randomise W before the flip events build up. At L=8, β=16 the system
     froze into W = (0,0,±16), where E = −388 against a ground energy near −444. The fix is to switch the winding
     loops off at β > 1 during thermalisation. It was found after the first production runs (L4_s1/s2, L6_s1/s2),
     which are therefore **compromised for winding observables** and are not used for verdicts.
3. **The winding populations at β ≥ L relax very slowly** [NUM]. At L=4 the relaxation takes ≫ 10 PT round trips:
   after ~30k sweeps the per-chunk values are still drifting. Clean L=4 runs from opposite sides (all W=0, or half
   the replicas at W=1) only agree in their last 15-minute chunk. So **the declared equilibration test fails at
   β = L** for L = 4 and 6. L = 8 (and 10) PT was operationally infeasible, at about 600 sweeps per 15 min.
4. **[VERDICT] (pre-declared criteria, applied as declared):**
   - **Winding criteria C-W / X-W: INCONCLUSIVE.** Fewer than two equilibrated L values are available.
   - **S_T exponent: NOT EVALUABLE.** The declared equilibration test fails at the two largest L.
   - No string tension is resolved, and none is excluded beyond C1.
5. **Equilibrated-looking numbers that survive** [NUM]:
   - At **L=4, β = L/2 = 2.05**, P(|W_a|=1) is stationary in every chunk of both clean runs. The winding free-energy
     gap is dF1 = 0.505(25), from the direct estimate, which agrees between starts.
   - At **L=4, β=4**, the last-chunk P1 is 0.055–0.058 from both sides, so dF1 ≈ 0.88. This is a [POST HOC] reading.
   - **L=4 thermal energy:** E(β=8) = −56.20(6). This is consistent with C1's projector E0 = −56.253(45), and
     E(β) ≥ E0 holds as it must.
   - **L=8 energy (one-sided check requested by the C1 review):** E(β=16) = −443.4 ± 0.5. This comes from one start, L8E_s3: 6.4k sweeps, W stayed 0. The binned error grows from 0.31 to 0.43 as the bins lengthen, and the five sub-run means range from −444.8 to −442.3. At this precision the run **does not discriminate** between C1's −443.83(14) and the repo's −443.364(31) (§5.5).

---

## 1. Supplied model (named premise, same as C1)

- Lattice: periodic cubic torus L³ with even L only. The stoquastic gauge argument and the zero-winding sector
  need even L (C1 §2 and the C1 review).
- Degrees of freedom: one spin-1/2 per link, with E_l = σ^z_l/2.
- Gauss law: div E = 0 at every vertex (3 in, 3 out). On the cubic torus the background is ρ_v = 0. The repo's
  "staggered background" convention exists only for the 2D ladder (C1 §1).
- Hamiltonian: H = −g Σ_p (U_p + U_p†) + V Σ_p n_p, with g = 1 and V = 0 throughout.
- Sign structure: for g > 0, H is stoquastic in the σ^z basis with no gauge needed (C1 Thm 1).
- Ensemble: Tr e^{−βH} over the **entire** Gauss sector: every winding sector and every flip component,
  including frozen ones.
- Winding: W_a = Σ E_a over the a-directed links that cross the plane x_a = 0. This is an integer, conserved by H.
  One quantum corresponds to reversing one directed winding line.

## 2. Algorithm [construction; detailed balance argued below, validated in §3]

**Representation.** Continuous imaginary time, with u = τ/β ∈ [0,1). A configuration is a base state s0 plus a
set of flip events F = {(u_k, p_k)}. Its weight is (gβ)^{n_F}; at V = 0 there is no diagonal factor.

**Augmentation.** On the 2-dimensional circulating subspace of a plaquette,
−g σ^x_p = −2g |+⟩⟨+|_p + g n_p. Expanding the projector term gives two vertex types, each of weight g:
- F vertices (flips);
- P markers (diagonal), which may sit only where the plaquette is circulating.

The diagonal remainder supplies a factor exp(−gβ Ī), where Ī = ∫_0^1 N_circ(u) du. Integrating the P markers
out returns exactly (gβ)^{n_F}.

**One sweep per replica** consists of the following moves (`scripts/ctqmc.py`):

1. **Gibbs resampling of the P markers.** The markers are drawn as a Poisson process of rate gβ on the
   circulating plaquette-time set.
2. **Plaquette clusters (Swendsen–Wang type).**
   - Each vertex binds its 4 lower legs together and its 4 upper legs together. Link-worldline segments connect
     the vertices. Clusters are the connected components, built with union–find.
   - Flipping a cluster keeps every vertex valid. It turns P into F, and F into P, at every vertex where the
     cluster contains only one side. n_F + n_P is unchanged, so the only weight change is exp(−gβΔĪ).
     ΔĪ is computed exactly, and checked against recomputation from scratch.
   - **Super-clusters.** A single cluster can leave static Gauss charges. Because the cluster partition does not
     encode the Gauss law, every cluster that is charged at a τ = 0 site is merged with the other charged
     clusters at that site and with the vertex-free links there. |Q_v(c)| does not change under any flip, so the
     partition is the same in the forward and reverse configurations. The new base state is checked for Gauss
     legality, and the flip is rejected if the check fails.
   - Each super-cluster is flipped with heat-bath probability 1/(1+e^{gβΔĪ}), in random order. The partition
     depends only on vertex positions, so each step satisfies detailed balance.
   - A cluster holding more than half of all segments ("giant") is skipped, a choice that depends only on
     positions. The global reversal E → −E, an exact symmetry, is applied with probability 1/2.
3. **Static ice loops (the winding-changing move).**
   - The move uses links whose four plaquettes carry no vertex. A Barkema–Newman directed walk chooses uniformly
     among the available outgoing links.
   - The proposal is symmetric because the number of available outgoing links at each loop site is unchanged by
     the flip. This was checked by exhaustive enumeration in pure Python on random free-link sets.
   - Acceptance is heat-bath in exp(−gβΔĪ). A loop that wraps the torus changes W by ±1. The move is efficient
     only at small β.
4. **Cube 3↔3 moves (new; V = 0).**
   - Three consecutive events lie on three distinct faces T of an elementary cube, with no other event on any
     plaquette that touches the cube's links in between, and the window does not wrap u = 0.
   - At the same times, these events are relabelled to the complementary faces T′, in a uniformly chosen valid
     order. The number of events is unchanged, so the weight ratio is 1, and the acceptance is min(1, N′/N),
     where N and N′ count the valid orderings.
   - **Why it is needed (found during validation, §3.2).** A single SW cluster's time-slice set S(τ) can only
     add a plaquette boundary disjoint from S or remove one contained in S. So the clusters can never generate
     the elementary-cube classes of the net-flip 2-cycle (C1 Lemma 3). Empirically, Σ_p n_p² never took the
     value 6.
5. **Parallel tempering in β.** Configurations are stored in u units, so the swap acceptance is
   min(1, (β_j/β_i)^{n_F,a − n_F,b}). This carries the winding changes made at small β, and decorrelated flux
   configurations, down to β = L.

**Estimators.**
- Energy: E = −⟨n_F⟩/β.
- Winding: P(W_a) and ⟨W_a²⟩.
- Flippable count N_circ at 4 time slices.
- Transverse structure factor S_T(q) = (1/3N_v) Σ_b Σ_a |E_a(q e_b)|², for q₁ = 2π/L (S1) and q₂ = 4π/L (S2).
  The component a ∥ q vanishes identically because div E = 0.
- Winding free-energy gap dF1 = −(1/β) ln[P(|W_a|=1)/(2P(W_a=0))], pooled over a. Two estimators:
  - direct, from the PT histogram;
  - TI (declared 03:40 UTC): ln[Z_S1/(2Z_S0)](β) = ln[P1/(2P0)](β_min) − ∫ (E_S1 − E_S0) dβ′, which is exact
    because H conserves W. Quadrature is a cubic spline.

## 3. Validation (exact L=2, full Gauss sector) [NUM]

**Exact reference.** `scripts/exact_L2.py` enumerates all 2^24 link configurations and keeps the 9600 Gauss
states, which fall into 937 flip components. It diagonalises each component densely. E0 = −9.0267209135, which
matches the repo and C1. The reference shares no code with the sampler except the lattice tables. Output is
`data/exact_L2.json`.

### 3.1 History (all runs are 2 PT runs × 15 min, 11 β values from 0.1 to 4, 1500–2000 round trips)

| version | change | result |
|---|---|---|
| v1 (scratch) | clusters + loops, Metropolis | E(β=1) biased by about −0.08 (single-β tests) |
| v2 (`logs/validate_L2_val2.log`) | + super-cluster merging of Gauss-charged clusters, heat-bath | **PASS=16 FAIL=9**. E is biased at β=1, 2, 4, with z up to +27. |
| v3 (`logs/validate_L2_val3.log`) | + cube 3↔3 moves | **PASS=25 FAIL=0** (max \|z\| = 1.78) |
| TI/direct dF1 (`logs/validate_TI_L2.log`) | v3 data | **PASS=10 FAIL=0**. The trapezoid quadrature failed at β=2 with z = −3.9; a cubic spline was adopted on L=2 data only. |

### 3.2 Diagnosis of the v2 failure [THM + NUM]

Let n_p be the net signed flip count of plaquette p over a period. The quantity Σ_p n_p² never took the value 6 in
v2. A value of 6 corresponds to an elementary-cube class: ±1 on each of a cube's 6 faces.

**Reason.** Each side of a vertex binds all 4 legs. So a single cluster's time-slice set S(τ) changes, at a one-sided
vertex, only by adding ∂p where ∂p ∩ S = ∅, or by removing ∂p where ∂p ⊆ S. Sweeping a cube needs XOR updates on
shared links, which these two operations cannot produce.

The super-cluster unions do not help, because their segment sets are disjoint. Plane classes do occur in v2, and so
do some odd n_p.

### 3.3 Other checks (scratch tests in the session; results logged in WORKLOG 01:45–02:35)

- **ΔĪ bookkeeping.** It equals the recomputation from scratch after every sweep (3000 sweeps).
- **Conditional detailed balance at fixed vertex positions.** The visit frequencies of all reachable configurations
  were compared with ∝ e^{−gβĪ}. For example: χ² = 19.5 with 19 dof, and 66.6 with 31 dof after 4× longer runs.
- **Loop-proposal symmetry.** Checked exhaustively in pure Python on random free-link sets: 0 asymmetric pairs.
- **Marker intensities.** These equal gβ times the circulating time per plaquette, to within 0.013.

## 4. Pre-declared criteria (copied from WORKLOG 01:32 / 03:35 / 03:40)

- **V1.** The L=2 validation rule above.
- **EQ.** At least 2 independent PT runs from different starts. E, ⟨W²⟩ and S_T(q1) must agree within 2.5σ, with at
  least 10 round trips per run. Points that fail are reported as not equilibrated.
- **Winding gap.** K(L) = ⟨W_a²⟩ and dF1 = −(1/β) ln[P(|W_a|=1)/(2P(W_a=0))] are measured at β = L; then
  a(L) = L·dF1.
  - **C-W (Coulomb):** a weighted fit a = a0 + sL gives |s| ≤ 2σ, and K(L_max) ≥ 0.02.
  - **X-W (confined):** s > 0 at more than 3σ, and K falls by more than a factor 2 per ΔL = 2.
  - Otherwise the result is inconclusive.
- **03:40 addendum.** The TI estimator of the same dF1. Both estimators must agree; otherwise the result is
  inconclusive.
- **S_T exponent.** p is taken from S_T(2π/L) at the two largest L. Coulomb: p ∈ [0.6, 1.4]. Gapped: p ≥ 1.6.
  Classical/RK-like: p ≤ 0.4.
- **Production settings.**
  - β ladders `data/ladders/L{4,6,8}.txt`, with β_max = 8, 6, 8 for L = 4, 6, 8. Both β = L and β = L/2 are on
    every ladder.
  - Measure every 2 sweeps, and discard the first 20%.
  - Errors use 20 bins per run. The combined error is the larger of the binned error and the seed scatter.

## 5. Results [NUM]

### 5.1 Runs

| tag | L | start | chunks (15 min) | sweeps | round trips | status |
|---|---|---|---|---|---|---|
| L4_s1 / L4_s2 | 4 | canonical / loop-scrambled | 4 / 4 | 39.7k / 40.2k | 27 / 24 | **compromised** (event-free start, §0.2b) |
| L6_s1 / L6_s2 | 6 | canonical / loop-scrambled | 7 / 7 | 24.1k / 24.6k | 13 / 15 | **compromised** |
| L4_s3 / L4_s4 | 4 | canonical / mixW_rot | 3 / 3 | 29.4k / 29.9k | 11 / 13 | clean (no loops at β > 1 for the first 2000 sweeps) |
| L6_s4 | 6 | mixW_rot | 2 | 6.6k | 0 | clean, one start only |
| L8E_s3 | 8 | canonical | 2 | 6.4k | – (single β=16) | clean |

**Start conventions.**
- `mixW_rot` alternates the replicas between the axis-rotated canonical state and the same state with one directed
  x-line reversed. These are W = 0 and W = (±1,0,0) respectively, so the winding population is approached from
  above.
- `canonical` (all W = 0) approaches it from below.

### 5.2 Drift of the winding populations: the central operational fact

P(|W_a|=1) per 15-minute chunk (`scripts/drift.py`):

| run | β | chunk 0 | 1 | 2 | 3 |
|---|---|---|---|---|---|
| L4_s3 (from below) | 2.05 | 0.390 | 0.434 | 0.394 | |
| L4_s4 (from above) | 2.05 | 0.477 | 0.405 | 0.389 | |
| L4_s3 | 4 | 0.016 | 0.088 | 0.058 | |
| L4_s4 | 4 | 0.253 | 0.175 | 0.055 | |
| L4_s3 | 8 | 0.000 | 0.000 | 0.000 | |
| L4_s4 | 8 | 0.034 | 0.029 | 0.002 | |
| L4_s1 (compromised) | 8 | 0.140 | 0.104 | 0.005 | 0.000 |
| L4_s2 (compromised) | 8 | 0.226 | 0.070 | 0.001 | 0.002 |

- At β = L/2 the populations are stationary.
- At β ≥ L they relax on a time scale comparable to the whole run. Only the last chunk of L4_s3/s4 agrees from both
  sides.
- The PT round-trip criterion (≥ 10 trips) is satisfied throughout and is therefore **not** a sufficient test of
  equilibration for winding observables. The start-agreement test also passed for L4_s1/s2 at 15 trips, while both
  runs were drifting together.

### 5.3 L = 4, clean runs (s3, s4; 20% discarded; `SEEDS=3,4 scripts/analyze_prod.py 4`)

| β | E | ⟨W_a²⟩ | P(\|W_a\|=1) | dF1 direct | dF1 TI (s3 / s4) | S_T(q1=π/2) | S_T(q2=π) |
|---|---|---|---|---|---|---|---|
| 2.05 | | 0.49–0.54 (chunks) | 0.39–0.43 | 0.510(34) / 0.500(28) | 0.540(36) / 0.455(39) | | |
| 4 = L | −54.63(8) | 0.100(31); start z = −3.0 | 0.100(31) | 0.82(3) / 0.65(4); z = +3.3 | 0.805(34) / 0.620(48) | 0.328(6); z = −2.2 | 0.541(4) |
| 8 | −56.20(6) | 0.007(7) | 0.007(7) | ≥ 0.6 (s3 has 2 samples) | 1.08(7) / 0.62(7) | 0.310(2) | 0.530(4) |

At β = L the EQ test fails on ⟨W²⟩ (z = −3.0); S_T is borderline (z = −2.2). The TI estimator also disagrees
between starts at β ≥ L. This shows that the sector-conditional energies of the W=1 sector are themselves not
equilibrated in s4 (they were seeded by the initial W=1 walkers).

### 5.4 L = 6

- **Compromised runs (s1, s2), β=6.** P1 per chunk scatters between 0.06 and 0.57. ⟨W²⟩ start z = −3.4. These
  runs are not used. S_T(q1 = π/3) = 0.2447(20) agrees between their starts (z = 0.2), but the runs remain
  compromised.
- **Clean run L6_s4**, one start only, so the EQ test cannot be applied: 
  - P1(β=6) per chunk is 0.123 then 0.018: the population is still relaxing, with 0 round trips.
  - dF1(β=6) = 0.71(4) direct and 0.67(7) TI; dF1(β=3) = 0.66(4) direct and 0.62(11) TI.
  - S_T(q1, β=6) = 0.2254(33). That is 5σ below the compromised runs' 0.2447(20). So **S_T is also shifted by the
    winding-population artifact**, and agreement between starts in the compromised runs did not protect against it.
  - [POST HOC] Using clean L4 S_T(β=4) = 0.328(6) together with this value gives p = ln(0.328/0.2254)/ln 1.5 = 0.93(5).
    That lies inside the declared Coulomb window, but it is **not** a valid evaluation of the criterion: L=6 has one
    start, 0 round trips, and is still drifting.

### 5.5 L = 8 energy (one-sided check)

`scripts/energy_L8.py`, `logs/energy_L8.log`. The run was L=8 at β=16 from the canonical start, with no
winding loops at β > 1 during the first 2000 sweeps, for 2 chunks (6.4k sweeps). W stayed (0,0,0).
- E = −443.36, with a binned error of 0.31–0.43 (40 to 10 bins). The five sub-run means are −443.3, −444.8, −443.4,
  −442.3 and −442.9, so the autocorrelation is long. A realistic error is ≳ 0.5.
- Since ⟨H⟩_β ≥ E0(global) for every β, a value significantly below −443.364 would have shown that the repo's
  guided value lies above the ground energy. **The result is not significant either way.** It is compatible with
  both the repo's −443.364(31) and C1's −443.83(14).
- The first attempt (L8E_s1/s2) started from an event-free path and froze into W = (0,0,−16) and (−11,0,0), at
  E = −388 and −407. That is §0.2b. It was discarded.

## 6. Verdicts against the pre-declared criteria [VERDICT]

| criterion | outcome |
|---|---|
| V1 (L=2 exact validation) | **PASS** (25/25, plus 10/10 for the winding estimators) |
| EQ at β = L | **FAIL** at L=4 (⟨W²⟩ z = −3.0, with a drifting chunk series); **FAIL** at L=6 (compromised runs; clean run has one start); L=8 not run |
| C-W / X-W (a(L) fit at β = L) | **INCONCLUSIVE**: no two L have equilibrated β = L winding data |
| TI vs direct agreement | not established at β ≥ L (start-dependent at L=4) |
| S_T exponent p | **NOT EVALUABLE** (EQ fails at the two largest L). For the record [POST HOC], clean L4 (β=4) with clean single-start L6_s4 (β=6, drifting) gives p = 0.93(5); this is not a criterion evaluation. |
| Overall OBL-R2.1 | **INCONCLUSIVE**. This is an operational result: the winding-sector mixing time at low T exceeds the budget. It is not physical evidence. |

## 7. What is learned, and what is not

- **The winding-changing machinery works** where it can [NUM]:
  - At β ≲ 0.5 (L=4) and β ≲ 1 (L=6) the winding changes every sweep. Hundreds of distinct W vectors are
    visited at β_min.
  - At L=2 the full winding distribution is reproduced exactly at every β, including β=4, where P(W ≠ 0) = 0.3%.
- **The bottleneck is transport, not proposal.** At β ≥ L, W can only change when PT carries a walker up to
  β ≲ 1 and back. With 34–40 replicas each round trip takes about 1000–1600 sweeps. The sector *populations* need
  many such trips, because the heavy W ≠ 0 walkers are expelled from low T only slowly. This mirrors C1's
  frozen-middle failure in a different guise: low-T flux sectors are dynamically isolated for every local or
  plaquette-cluster dynamics. In the compromised L=6 runs, E, N_circ and S_T agree between starts, but both starts
  share the same winding artifact. The clean run shows that S_T is shifted by it (§5.4), so start agreement is not
  evidence of equilibrium here.
- **No evidence of confinement** [NUM, weak]:
  - At L=4 the winding free-energy cost at β = L/2 is about 0.5g, which is O(1/L)-sized.
  - The dF2/dF1 ratios at L=4 and 6 are about 3.2–4.1 [POST HOC; from the compromised runs, so indicative only].
    That is closer to the quadratic (Coulomb-like) value 4 than to the linear string value 2.
  - None of these is a declared criterion, and none is decisive.

## 8. Context

[EXT] comparison of energies and winding gaps at L = 4:
- C1 open-path projector: E0(W=0 canonical component) = −56.253(45), and ΔE(W=1 line) = 0.676(63).
- Repo guided projector: ΔE = 0.7315(84).
- This block: thermal E(β=8) = −56.20(6), consistent with E(β) ≥ E0 and with small thermal excitation at β = 2L.
- The free-energy gap dF1 at β = L/2 to L (0.5 to about 0.9) is of the same size as ΔE. It contains entropic terms of
  order ln(g1/g0)/β, so it is not an estimate of ΔE.

[LIT] is as in C1 §8, recalled from memory and not re-checked. Coulomb-phase QMC in pyrochlore ring models has used
microscopic XXZ models with worm/directed-loop updates, in which the ring term is perturbative. For the strict ring
model, no exact winding-ergodic finite-T cluster algorithm is known to me. That is consistent with what was found
here.

## 9. Load-bearing steps and what an independent check must do

1. **Detailed balance plus ergodicity of the move set.** The evidence is the L=2 exact validation (§3), which is the
   only exact check. In particular the cube move (`cube_moves` in `scripts/ctqmc.py`) must be verified: its
   acceptance min(1, N′/N) and its window rules. An independent check should:
   - re-derive the acceptance of the cube move;
   - test at L=4 against an independent method at small β, for example a high-temperature series for E(β) and
     ⟨W²⟩ to O(β⁶), or exact enumeration of a 4×4×2 slab if one is defined.
2. **The equilibration claim (negative).** The drift table §5.2 can be checked from `data/raw/*` with
   `scripts/drift.py`. An independent check should run longer (≥ 10× more sweeps). It should also start from
   *both* sides (all W=0, and half the replicas W=1), and report the per-chunk P1(β=L). The two sides must
   converge for several consecutive chunks.
3. **The L=8 one-sided energy check:** not informative at the present precision (±0.5). It needs at least 10× more sweeps and at least 2 starts.

Re-running these scripts with new seeds is not independent. A different code (for example SSE with the same cube and
cluster moves, written separately), or a guided projector with sector-resolved forward walking, would be.

## 10. What a decisive follow-up needs

1. **Faster winding transport at low T.** Options:
   - PT with far fewer replicas, by using a better swap observable. The swap acceptance is limited by Poisson noise
     in n_F (σ ~ √n_F), so about 2√(cNβ) replicas are needed.
   - Simulated tempering combined with Wang–Landau weights in (β, W).
   - Most promising: a **sector-resolved TI**, with separate PT runs inside the fixed sectors W=(0,0,0) and
     W=(1,0,0). It needs equilibration only *within* each sector, which the clusters achieve. The sector ratio at
     β_min comes from classical loop counting. The validated TI estimator (`scripts/ti.py`) applies unchanged.
2. **Thermalisation protocol.** Always switch the winding loops off at large β until n_F has equilibrated (§0.2b).
   Seed the replicas from both W=0 and W≠0 sides.
3. **Larger L.** L ≥ 8 needs a roughly 5–10× faster kernel. The cost is dominated by plaquette-integral merges
   and by Python measurement overhead.

## 11. Files

- **Scripts** (`scripts/`):
  - `ctqmc.py`: numba kernel with the sweep (markers, super-clusters, loops), `cube_moves`, `check_config`;
  - `sim.py`: PT driver, starts, measurements;
  - `run_pt.py`: resumable 15-min chunk runner;
  - `queue.sh`, `jobs_*.txt`: queues;
  - `ladder.py`;
  - `exact_L2.py`, `validate_L2.py`, `validate_ti_L2.py`;
  - `analyze.py`, `analyze_prod.py`, `ti.py`, `drift.py`, `posthoc.py`, `energy_L8.py`, `save_bins.py`.
- **Logs** (`logs/`):
  - `validate_L2_val3.log` (TOTAL: PASS=25 FAIL=0);
  - `validate_TI_L2.log` (TOTAL: PASS=10 FAIL=0);
  - `validate_L2_val2.log` (superseded; TOTAL: PASS=16 FAIL=9);
  - `queue_*.log`, `prod_chunks.jsonl`, `val*_s*.chunk.log`.
- **Data** (`data/`):
  - `exact_L2.json`;
  - `ladders/`;
  - `raw/` (production chunks, 15-min measurement files);
  - `ckpt/` (PT checkpoints);
  - `val_bins_L2.npz` (20-bin summaries of the L=2 validation runs; the raw validation files of 125 MB were moved
    out of the block for the 50 MB limit);
  - `summary_prod.json`.
