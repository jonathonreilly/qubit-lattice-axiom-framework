# T-SPIRAL and T-SPIRAL-2 report

**Both readings come out negative: SPIRAL-ABSENT under T-SPIRAL as registered, and SPIRAL2-ABSENT under T-SPIRAL-2.**

**Plain version.** I built the record rule from rules already on main. A site with no record forms one at a rate that grows with its number of recorded neighbours (coupling μ). The new record copies its recorded neighbours with a bias K. Records never unlock. I ran this on Z² and Z³ and coarse-grained the finished record pattern by block-spin matching.
- **2D:** there is no fixed point anywhere inside the coupling plane. The flow always weakens the correlations, toward independent coin flips.
- **3D:** the only "fixed points" sit where one ordered grain fills the whole box. Their eigenvalues change with every variant, so they are artefacts of box size and truncation.
- **General reason (Lemma C, proved below):** when formation rates are bounded and records are permanent, the correlation length is finite at every finite coupling. So there is no critical point inside the plane for a flow to spiral around. A long passage in this class needs the rate ratio itself to be enormous, and that ratio is a supplied number.

This is a same-family run (Opus 5.5), not refereed. PREREG.md was written before any run. The T-SPIRAL-2 follow-up was appended to it at 17:00Z, after the grid runs and two 3D size checks had already finished. It is dated and says so.

## Read first
- `MINIMAL_AXIOMS_2026-06-29.md` in full.
- `PRIMITIVE_REGISTRY_CHECK.md` and `SCALE_REFERENCE_PRIMITIVE_NOTE.md`.
- `derivation_obligations.json`: it has no hierarchy entries.
- WALL.md, TESTS.md and R4/REPORT.md.

## Prior art (origin/main 58475576)
- **Not mapped:** nothing on Monte Carlo RG, complex eigenvalue pairs or RG spirals for formation rules. The "spiral" hits on main are relational spiral frames, which are unrelated.
- **Landed rules used** (none of these notes selects a rule):
  - the binary class (P) in its formation reading (09-06 note);
  - record-determined clocks (09-24);
  - the uniform race, μ = 0 (09-22). I reproduce its nucleation density 1/(1+2d): 0.2010 vs 0.2000 in 2D, 0.1422 vs 0.1429 in 3D.
- **Why the rule must be order-sensitive:** order-blind positive rules give 1-dependent fields (10-16 note), so they have no non-trivial fixed point at all.
- **Related decay result:** exponential decay is landed only for a sweep order at weak coupling (09-15 monotone-law note).

## Method
- **Simulation:** exact rejection-free kinetic Monte Carlo. The bias acts as a heat bath on recorded neighbours, P(s|N) ∝ e^{K s m}, with formation rate e^{μ n}.
- **What the RG acts on:** the frozen record pattern, not the spacetime process. Only records are readable.
- **Blocking and matching:** majority-rule blocks with b = 2 and b = 3. Matching sets A^{(L)}_{n+1}(θ) = A^{(L/b)}_n(Rθ), with equal final sizes, for n = 0 and n = 1.
- **Observable sets:** S2 = {nearest-neighbour, plaquette}; S5 = S2 plus three more.
- **Fixed points:** found on spline fits over the pre-registered grid (11 values of tanh K × 13 values of μ from −3 to 9). Eigenvalues come from the fitted gradients, with y = ln λ / ln b.
- **Lattices:** 2D 128/64 and 162/54; 3D 32/16 and 36/12; 192–256 samples per point.

## Results
- **Method check (checked).** On the K = 0 fixed line, the 2D b=2 eigenvalue is 0.285–0.296, against the analytic 2(3/8)² = 0.281. 3D and b=3 are within 10–20% of their analytic values. All are real, with y between −1.3 and −1.8.
- **2D (checked).** There is no interior fixed point in any of the 8 variants (b × S × n). This does not depend on the fits. At all 130 grid points with K > 0, the blocked lattice's nearest-neighbour correlation is below the comparison lattice's by 3.6σ to 350σ. So the coupling always decreases.
- **3D (checked).** There are 7 zeros, all at μ ≈ 7.7–9 and tanh K ≈ 0.62–0.87:
  - b=2, n=1, S2: (1.42 ± 0.64i), (1.00, 0.018), (−1.58, 1.34)
  - b=2, n=1, S5: (1.33, 11.1), (0.57, −37.9)
  - b=3, n=0: (1.00, 1.31), (0.77, −1.60), (0.76, 4.37), (0.71, −4.33)
  - None of these appears in more than one variant. The only complex pair has y = 0.64 ± 0.61i, so Re/|Im| = 1.05 and |Re y| = 0.64.
- **Readings:**
  - **T-SPIRAL:** every fixed point is real or has Re/|Im| ≥ 0.1. **SPIRAL-ABSENT.**
  - **T-SPIRAL-2:** every fixed point is real or has |Re y| ≥ 0.2. **SPIRAL2-ABSENT.**
  - **Lyapunov coefficient:** not applicable. No fixed point comes near |Re y| ≤ 0.06, so I computed no sign.

## Truncation-artefact checks (T-SPIRAL-2)
1. **Exact criterion**, fixed in PREREG before the correlation-length runs. An exact block map shrinks the correlation length by b, so a true fixed point needs it to be 0 or infinite. Lemma C makes it finite at every finite coupling. So every interior zero is an artefact (proved, given Lemma C).
2. **Box size at the 3D zeros (checked).** The correlation length grows with the box: 18, 29 and 42 at L = 64, 96 and 128 for the first zero. The correlation at half the box size stays at 0.17–0.86, so one grain fills the box at every size I could reach.
3. **The crossover moves with L (checked).** At tanh K = 0.6 it sits at μ > 9 (L = 32), 8.9 (L = 64) and 8.15 (L = 96). It has not converged.
4. **No stability across variants:** see the 3D eigenvalues above.
5. **Not counted for any reading:** complex eigenvalues of the linearised map away from fixed points have no RG meaning. They cluster at small K, where μ barely affects the pattern and its matched value is poorly determined.

## Lemma C (proved here; no theorem of this form found on main)
**Statement.** Take any irreversible nearest-neighbour formation rule on Z^d, with any alphabet and any content rule (K = ∞ included). Let the rates depend on the recorded neighbourhood and lie in [h_min, h_max] with h_min > 0. Then the finished field obeys |Cov| ≤ 8e^{−r/ξ_b} at distance 2r, with ξ_b = 2d·e²·h_max/h_min.

**Proof.** It is a standard Poisson-clock, finite-speed argument:
- Give each site a Poisson process of rate h_max and thin it to realise the rates.
- The chance a site is still unrecorded at time t is at most e^{−h_min t}.
- The chance that backward dependence reaches distance r within time t is at most (2d·e·h_max·t/r)^r.
- Choosing t = r/(2d·e²·h_max) bounds both terms, and disjoint dependency regions are independent. ∎

**Consequences:**
- **Absorbing states:** at every finite coupling, each site reaches its permanent record in finite time and the correlation length is finite. So no non-trivial fixed point exists at finite couplings under absorbing states. Candidates exist only where h_min/h_max → 0, that is μ → ±∞.
- **Boundaries:** at K = 0 (proved) and at μ = +∞ (suggested) the boundary is invariant, so the eigenvalues there are real.
- **Passage length:** whatever shape the flow has, the number of e-folds is at most 2d|μ| + ln(2d·e²). Reaching L* = 38.4 needs a rate ratio of at least e^{35} (proved bound).
- **In practice:** the measured growth is ln ξ ≈ (0.41–0.47)·μ (checked), so about μ ≈ 85 would be needed.
- **What the scale is:** a grain size set by a supplied rate ratio, of the nucleation-and-growth type (comparator), not a spiral.

## Scope and what stays open
- The tested class has two couplings, one content rule and one clock family. Lemma C covers every clocked rule with bounded rates.
- **Not covered:** the level-time (light-cone) reading on the event lattice, where formation time is a lattice coordinate. Lemma C does not apply there, and a real critical point exists: the 09-23 note finds a reflection-positive bilayer ordered above β = 0.5905. Reflection-positivity theorems suggest real exponents there (comparator; not tested).
- **Not run:** an RG of the spacetime process.
- **No claim about v.**

## Files
All in `/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/hierwall/T/`:
- `PREREG.md`, including the dated T-SPIRAL-2 follow-up
- `sim.py`, `check.py` / `check.out`
- `analysis.py` with `an_d2_b2.out`, `an_d2_b3.out`, `an_d3.out`
- `xi_fit.py` / `xi.out`
- not pre-registered: `ext.py`, `ext2.py`, `xi_check.py` and their `.out` files
- the data, `*.npz`

Peak memory was 351 MB, one process at a time. One correlation-length run hit the 0.4 GB cap and was killed; I reran it with smaller lattices. Nothing is left running, and nothing outside the folder was edited.