I found no self-consistency condition inside the axioms that forces the integer or the near-marginal parameter. There is a general reason. When such a condition holds exactly, the system sits exactly at the marginal point and no finite scale appears. A hierarchy needs the condition to miss by a small amount, about 0.7–2%, and that miss is the number the axioms would have to supply. Picking an integer by balancing two exponentially small effects runs into the same need. One escape that HIER-1 does not cover turned up: with two or more couplings, a flow can spiral for a long time without ever slowing down. The axioms do not exclude it.

Same-family run (Opus 5.5), not refereed.

**What I read first.** I read `MINIMAL_AXIOMS_2026-06-29.md` in full, `PRIMITIVE_REGISTRY_CHECK.md`, and `SCALE_REFERENCE_PRIMITIVE_NOTE.md`. `derivation_obligations.json` has no hierarchy entries; its three entries are about AC and theta. I also read the WALL and the HIER-1/2/3 reports from PR #9783.

**Prior art.** I searched main for clockwork, self-organised criticality, ghost/bottleneck, fixed-point merger, Potts, Coleman–Weinberg, exponential sums, walking and Banks–Zaks. What is already mapped:
- the hyperbolic bound and its escapes E2–E4 (HIER-1);
- N_f = 16 flows to a Banks–Zaks fixed point (HIER-1(b));
- the one-loop window (`HIERARCHY_VALUE_FRONTIER_PROBE_2026-06-05.md:72-96`);
- the 16 depends on the regulator (`HIERARCHY_ALPHA_LM_EXPONENT_SPECIES_COUNT_..._NO_GO`).

I found nothing on balance-selected integers, slow-passage forms beyond the hyperbolic one, spirals, or integer-controlled mergers.

The budget is L* = ln(M_Pl/v) = 38.4 (36.8 with the reduced Planck mass).

## Route A: an integer fixed by a balance (wall depth, clockwork length)

**Object.** Any condition that fixes an extent N by balancing exponentially localised terms: F(N) = Σ c_j N^{p_j} e^{−k_j N} = 0. The amplitudes satisfy |c_j| ∈ [1/R, R], the gap between the two smallest rates is Δ, and the light mass is M e^{−κN*}, with κ one of the rates.

**Lemma A (proved, two lines).** The largest balance point satisfies N* ≤ [ln((J−1)R²) + p_max ln N*]/Δ. So κN* ≤ (κ/Δ)·ln((J−1)R²).
- Reaching L* needs κ/Δ ≥ 8.3 (R = 10) up to 17.5 (R = 3).
- That means either two decay rates within 6–12% of each other, or a light amplitude that is a product of n = κ/Δ ≈ 8–17 single overlaps.
- With R² = 1/α_LM ≈ 11 this gives n = 16.0 exactly. That is main's α_LM^16 shape. So the integer-extent escape (E4) collapses into the selection-order escape (E3). It supplies neither n nor R.

**Checked** (`a_integer_balance.out`):
- 2,084 random instances: no violations of the bound. In the class where all inputs are O(1) (Δ/κ ≥ 0.2, R ≤ 10), the largest κN* is 30.2, short of 38.4.
- Wilson–Dirac ring with a kink and an antikink:
  - The zero-mode splitting and the curvature of the sea energy share one decay rate (ratio 0.99 and 1.04; analytic value −ln|1−M0|).
  - The sea energy has no stationary point. The Wilson term gives the two mass regions different bulk energies, a constant pressure of 0.37–0.72 per site that collapses the pair.
  - So the fermion sector selects no depth at all.

**Number it would fix.** n and R. Neither is supplied: the axioms fix no amplitudes ("form and values" are downstream, axioms `:183-184`). HIER-1(a) already showed 16 is not protected.

**Strongest objection.** The class leaves out amplitudes that nearly cancel, but a near-cancellation is itself a small parameter. Branch cuts in place of discrete rates add only logarithmic corrections (suggested).

**Kill condition.** If no intrinsic condition forces both a protected multiplicity n ≥ 8 and a fixed amplitude ratio, the route is dead. As of now it is dead.

**Cheapest next test.** Ask whether Lieb-type flux self-consistency, whose optimum is π-flux, fixes R as well as the 2⁴ cell.

## Route B: slow passage near a fixed point (essential singularities, walking)

**Lemma B (proved in 1D).** Take one coupling with a start and end O(1) apart, and write T for the number of RG e-folds. Then T ≥ L* needs one of three things:
1. Hyperbolic tuning to e^{−yL*} (this is HIER-1).
2. A ghost: a non-degenerate minimum m of |β| with curvature k and m ≤ 2π²/(kL*²). For the normal form β = μ + bu², that is μ ≤ π²/(bL*²) = 6.7×10⁻³/b.
3. Weak coupling over the whole path: b·u0 ≤ 1/L*. This is HIER-3's window.

A small linear exponent alone does not help:
- transcritical form: T = (1/y)·ln(1 + y/(b u0)) ≤ 1/(b u0) for every y ≥ 0;
- pitchfork or weak-focus radial form: T ≤ 1/(2c r0²).

This sharpens HIER-1's E2. The condition y < 2/15 is necessary, not sufficient. For example, an O(3)-type cubic anisotropy with y ≈ 0.013 (comparator) still gives T ≈ 1 at O(1) anisotropy.

**Checked** (`b_slow_passage.out`):
- The closed forms match quadrature, and the ghost needs μ = 6.7×10⁻³ to reach 38.4.
- 18,041 random 1D flows reached a gap; 226 had T ≥ L*, and every one had min|β| ≤ 0.019 (median 6×10⁻⁵).

**New (checked, `b_spiral_inspect.out`).** About 2,300 random 2D flows reached a gap. Two had T ≥ L* with no slow point at all (minimum speed 0.39 and 1.12).
- Each spirals 8–25 times next to a nearly neutral focus, with Re/|Im| = 0.010 and 0.014 for the eigenvalue pair.
- This is a separate slow-passage form. The number it needs is Re y / Im y ≈ 0.01–0.025.
- HIER-1's cone hypothesis H2 excludes it.
- Unitary, reflection-positive theories forbid it (c-, F- and a-theorems; comparator). The axioms state no reflection positivity, and record formation is irreversible, so the axioms leave it open (reading).

**Integer-controlled mergers (comparator).** In the 2D Potts family the merger sits at the integer q_c = 4. q = 4 is exactly marginal, with no scale. q = 5 gives ξ = 2512, so T = 7.8. Reaching 38.4 needs q = 4.058. Integer steps are too coarse by a factor of about 16.

**General point (suggested; every case above fits it).** A self-consistency that holds exactly gives exact marginality and no finite scale. The hierarchy is the small amount by which it fails. An integer can supply that residual only by a Diophantine accident, with a chance of roughly μ*/(step per integer) ≈ 1–7% per family, or as a 1/N² correction with N ≈ 12–16. Self-organised criticality also tunes to the exact point; its residual is the ratio of drive to dissipation, which is supplied. If the tuning runs on cosmic history, v drifts in time unless something freezes it, and the freezing epoch is a supplied number (suggested).

**Number it would fix.** μ ≈ 6.7×10⁻³/b, or Re/Im ≈ 0.01, for the actual coarse-graining flow of the admissibility and record sector. That flow is not built, and the axioms supply no formation rates.

**Strongest objection.** Random polynomial flows are not the framework's flow. The route is conditional on a formation law that is not supplied.

**Kill conditions.**
- The spiral form dies if the sector's coarse-graining is gradient-like or reflection-positive, which gives real eigenvalues, or if it shows Re/Im ≥ 0.1.
- The ghost form dies if the intrinsic merger families (cubic axes q = 3, 4, 6, 8) have merger points at integers, or integer steps much larger than μ*.

**Cheapest next test.** Linearised real-space RG of a nearest-neighbour, cubic-covariant, non-reflection-positive two-state rule (and one with irreversible locking). Look for complex eigenvalue pairs and their Re/Im.

## Status
- **Proved:** Lemma A; Lemma B in 1D; the transcritical and pitchfork bounds.
- **Checked:** the random tests, the Wilson–Dirac ring, and the two 2D spirals.
- **Comparator:** Potts ξ(q), y_4 of O(3), and the unitarity theorems.

Peak memory was 125 MB, one process at a time, and nothing is left running. I edited nothing outside my folder.

Files are in `/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/hierwall/R4/`:
- `PREREG.md`, written before any run
- `a_integer_balance.py` / `.out`
- `b_slow_passage.py` / `.out`
- `b_spiral_inspect.py` / `.out`