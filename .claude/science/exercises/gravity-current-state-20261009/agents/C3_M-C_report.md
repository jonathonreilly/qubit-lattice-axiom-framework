# C3 lane M-C: worker report (Claude Opus 5.5, max effort; 2026-10-10)

Verbatim. Adversarial check (Opus 5.5 xhigh) below the report. **Codex sol referee: CONFIRMED WITH CORRECTIONS** (C3_M-C_referee.md).

**Verdict (worker):** M-C overall: FAIL (no-go), by the readings fixed in PREREG.md. Q1, rules with every weight nonnegative: C0-FAIL, EXACT. Q2, positive hops with the sign moved elsewhere: C1-FAIL, EXACT in both parts (moving the sign is only a relabelling; descent from a positive parent cannot give a 3+1 massive pole). Q3, coherence of the most promising route found: M-PASS, source-driven scope only. That route is C2, a direct kernel with no path sum; it is signed, so it does not rescue 'without signed weights'. Because this is a no-go, the codex sol referee must review it before it is recorded.

**Plain summary:** No. On the event substrate, a rule whose weights are all positive cannot make a massive matter wave. The total of a positive field can never go negative, but the total of a massive wave swings like sin(mt) (exact). Moving the sign out of the hops (into the particle's internal state, a background field, or the read-out) is always possible, but it is a relabelling that leaves the noise unchanged. The one natural way to move it, mass as motion along an extra dimension, works only for a world with two space dimensions: positive massless propagation exists only up to 3+1 dimensions, and the trick costs one dimension (exact). What the sign buys is the ability to wave and interfere, not slowness: positive rules can still move classical particles slower than light, but those particles cannot interfere. One route does keep electron and proton packets coherent over 1 km, with noise near 1e-103: drop the path sum instead of the sign, and make the amplitude between two events a fixed function of how many events lie between them, so that every sign is decided by about 1e150 events instead of one. But that route puts the mass and the whole propagator in by hand.

# M-C report: mass without signed weights (campaign C3)

**Worker:** Claude Opus 5.5, max effort.
**Dates:** PREREG.md was stamped `Sat Oct 10 01:05:46 UTC 2026` before any computation. The runs ended at 01:26Z.

**Setting.** A test setting only: the E1/E1′ event substrate, a Poisson sprinkling of Minkowski space at density ρ = ℓ⁻⁴ with ℓ = ℓ_P and the causal order supplied. The E1/E1′ axiom conflicts apply unchanged:
- Lattice is replaced.
- The order is supplied, because records carry no time (A36).
- Records-as-events conflicts with "one record per site, permanent".

**Repository.** No repository file was edited; `git status` is clean. One script was reused by copying it into the scratch folder, so that no cache files were written into the repository.

## Verdicts against the fixed readings (PREREG.md)

| Question | Reading | Verdict | Basis |
|---|---|---|---|
| Q1: C0, every weight ≥ 0 | C0-FAIL / PASS / INCONCLUSIVE | **C0-FAIL (no-go)** | Lemma A (EXACT) |
| Q2: C1, positive hops with the sign in the state, a background or the readout | C1-FAIL needs (i) relabelling and (ii) no positive descent to a 3+1 pole | **C1-FAIL (no-go)** | (i) Lemma B (EXACT); (ii) Lemma D (EXACT) |
| **Overall M-C: "massive matter without signed weights"** | FAIL if Q1 and Q2 are both FAIL | **FAIL (no-go), in 3+1, under H1–H4** | needs the codex sol referee before it is recorded |
| Q3: coherence of the most promising route found (lane M readings) | M-PASS / M-FAIL / M-INCONCLUSIVE | **M-PASS, source-driven scope** | route C2 (a signed direct kernel with no path sum): exact U-statistic law plus a Poincaré estimator bound; Var/mean² ≤ 1e-103 at 1 km for both particles |

C2 is not "without signed weights". It answers only the literal "without a signed **path sum**". It leaves the M-C FAIL standing.

## What I read

**Read in full:**
- `docs/MINIMAL_AXIOMS_2026-06-29.md` (233 lines);
- `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md` (three primitives: scale reference, kinetic isotropy, realized state);
- the packet's TESTS.md (524 lines): the rules, E1′, E1′-b, and Campaign C3;
- SUMMARY.md §7–9;
- `agents/E1p_report.md`, `agents/E1p_referee.md`, `agents/supervisor_E1p_b.md`, `agents/E1p_b_referee.md`.

**Code:**
- the header and docstring of `scripts/E1p/e1p_core.py`;
- `scripts/E1p/E1p_1_massless_needle.py`, which I copied verbatim and reused unchanged.

**Not read directly:** the block 122 note on main. It is cited only as SUMMARY and E1′ quote it ("waves need signed weights; nonnegative rules undamped only by rigid transport"). Lemma A below is its Lorentzian, event-substrate analogue.

**Prior art (COMPARATOR):**
- Johnston's path sum, as refereed in E1′, is the signed reference.
- Lemma A uses the elementary positivity of the zero mode, plus the Pringsheim–Landau / Bernstein theory of Laplace transforms (Widder).
- Lemma D is the standard Riesz/Hadamard descent structure of the Green functions in D dimensions, with G_D = (1/π)∂_σG_{D−2}.

## Hypotheses

- **H1.** The matter observable is linear in the source: φ = ρ⁻¹KJ and S = ρ⁻²Σ D*KJ.
- **H2.** The law is translation-invariant (Lemma A). For Lemma D, the parent is Poincaré-invariant in law and retarded.
- **H3.** The target of the mean test is the continuum 3+1 retarded Klein–Gordon kernel, G_R = θ(t)[δ(σ)/2π − (m/4πτ)J₁(mτ)θ(σ)].
- **H4.** Observables are source-driven, as in E1′.

## Results

### 1. Lemma A: a positive rule cannot make a massive wave (Q1; EXACT)

**Statement.** Take any C0 rule, with every hop, re-emission, source and readout weight ≥ 0. With H1 and H2, its mean kernel k(x − y) = E K(x,y) is a nonnegative measure. So its zero mode is nonnegative at every time:

  f(t) = ∫d³x k(t,x) ≥ 0.

The massive retarded kernel has f(t) = sin(mt)/m, which is negative on (π/m, 2π/m). Hence no C0 mean is massive.

**Numerical check (mc1).** The zero modes equal sin(mt)/m to 10 digits at t = 0.5–12 (m = 1) in 1+1, 2+1 and 3+1. For example, at t = 4 the 3+1 value is −0.7568024953.

**Carrier inequality (EXACT).** For f ≥ 0, |f̂(ε + iω)| ≤ f̂(ε). So a massive pole at s = ±im with residue r forces lim inf ε·f̂(ε) ≥ |r|: there must be a non-oscillating zero mode at least as large as the massive one (Pringsheim–Landau: the singularity at the abscissa of convergence is real). For example, f = 1 + sin t is the minimal positive case, and it gives ε·f̂(ε) → 1 against ε·|f̂(ε + i)| → 0.5.

A positive rule can therefore carry a massive mode only as a modulation on a larger massless or growing carrier, and removing the carrier needs a signed readout.

**Corollaries.**
- **Johnston's family with b ≥ 0** (positive re-emission) is C0. Its continuum mean solves (□ − bρ)G = δ, a tachyon (EXACT, given Johnston's mean equation). A positive condensate coupling therefore gives growth, not mass.
- **Positive superpositions** of positive kernels are positive, so they are excluded. This covers Källén–Lehmann-type mixtures and mixtures of dilated link kernels. The Lorentzian Schwinger form carries e^{−ism²}, which is complex; only the Euclidean form is positive.
- **Classical massive transport is not excluded.** A positive kernel on the proper-time hyperboloid moves matter slower than light. But it cannot oscillate, so it cannot interfere. **The sign buys the wave, not the slowness.**

### 2. Lemma B: moving the sign is a relabelling (Q2(i); EXACT)

Take any signed or complex observable S = Σᵢ wᵢXᵢ, where the Xᵢ ≥ 0 are functionals of the sprinkling (link indicators, chains, counts).

**One direction.** S equals, realization by realization, the Fourier readout ∫e^{iθ}S̃(dθ) of the positive rule S̃ = Σᵢ|wᵢ|Xᵢ·δ_{arg wᵢ} on events × U(1). In that rule each hop is a positive weight times a rigid internal rotation, which is block 122's rigid-transport exception.

**The other direction.** Every C1 observable (positive hops; sign in the state, a background, or a linear readout) is a signed observable on the base.

**Consequence.** C1 observables and signed observables are the same random variables, so positivity of the hops never changes Var/mean². What matters is *which events decide each sign*, not where the sign is written.

### 3. Lemma D: descent fails in 3+1 (Q2(ii); EXACT). Lemma C: it works in 2+1 (EXACT and CHECKED)

**The descent map.** Take a parent kernel f(σ) one dimension up, and read out its mode e^{imw} along the extra coordinate w. With T = σ_D:

  F(T) = ∫₀ᵀ k(T − u)f(u)du, with k(v) = cos(m√v)/√v.

So F̂ = k̂·f̂, with k̂(s) = √(π/s)·e^{−m²/4s} (checked to 10 digits). By Laplace uniqueness, the parent that matches a given massive retarded kernel is forced (mc1, 8 digits at s = 0.25–8):

| Massive target | Forced parent f̂(s) | Parent kernel | Completely monotone? |
|---|---|---|---|
| 1+1 | s^{−1/2}/(2√π) | 2+1 massless, θ(σ)/(2π√σ) | yes |
| 2+1 | 1/(2π) | 3+1 massless, δ(σ)/(2π) | yes |
| **3+1** | **s^{1/2}/(2π^{3/2})**, independent of m (checked at m = 0.5, 1, 2) | 4+1 massless, **−FP σ₊^{−3/2}/(4π²)**, negative at every interior point | **no** |

**Why this excludes 3+1.**
- A nonnegative Poincaré-invariant retarded mean on M^{1,4} has the form θ(t)ν(σ) with ν ≥ 0 (orbit decomposition), plus at most a contact term. The contact term descends to a contact term, so it must vanish.
- The Laplace transform of such a measure is completely monotone (Bernstein). The forced parent s^{1/2} is increasing, so it is not.
- In general the forced parent is f̂_D ∝ s^{(D−4)/2}. That is completely monotone only for D ≤ 4: positive massless propagation exists only up to Huygens' dimension 3+1, and descent costs one dimension.
- So positive-hop descent gives massive matter in 2+1 and 1+1, never in 3+1.
- If the parent's 4+1 invariance is dropped, w is no longer a dimension. It becomes a phase register, and that is Lemma B: a relabelling.

**Lemma C, the 2+1 control.** Take positive 3+1 link hops with the state profile cos(mz).

| Item | Result | Label |
|---|---|---|
| Finite-density mean | → cos(mτ)/(2πτ). Error relative to the envelope: 3.5e-2 at τ/ℓ = 5 down to 4.5e-4 at τ/ℓ = 80 (mℓ = 0.05); 2.8e-2 down to 3.6e-3 (mℓ = 0.5) (mc2). | CHECKED |
| Noise law | Var ≤ (3 + C·s/D)·Ñ, with Ñ = ρ∫\|J\|e^{−ρV}, so rel. noise ≤ R·√((3 + Cs/D)/Ñ), where R = Ñ/\|mean\| is the cancellation ratio set by the smooth profile. This extends E1′-b's Poincaré argument, which uses only \|J\| ≤ 1. | EXACT |
| Noise check with signed profiles (mc6) | Var/Ñ = 0.78–0.86 against the bound 3. Var/diag = 0.99–1.13. The means match exact quadrature within 1.4–1.9σ. | CHECKED |
| Unsigned controls (mc6) | Fano 1.42 (D, s = 60, 6) and 2.31 (40, 12), against E1′'s 1.38 ± 0.04 and 2.30 ± 0.09. | CHECKED |

In the signed case, oscillating profiles cancel the positive link–link correlations.

### 4. The candidates

| Candidate | Class | 3+1 massive one-cone mean? | Noise | Label |
|---|---|---|---|---|
| Any rule with all weights positive | C0 | no (Lemma A) | — | EXACT |
| (b) Positive condensate re-emission | C0 | no: a tachyon | — | EXACT |
| (b) Higgs-like, m² = yΦ² > 0 | signed (re-emission weight −yΦ²) | Johnston-type | Johnston's per-event structure; m self-averages | ARGUED |
| (c) Positive Källén–Lehmann or Schwinger mixtures | C0 | no (Lemma A) | — | EXACT |
| (c) Descent / Kaluza–Klein | C1 | 2+1 only (Lemmas C, D) | massless-type in 2+1 | EXACT, CHECKED |
| (c-E) Euclidean positive walks plus OS reconstruction | outside the event setting | standard (a killing walk gives e^{−mr}) | per-realization real time is undefined on a random Euclidean set; B1 c5 found white TT noise | ARGUED, COMPARATOR |
| (a) Composites of massless constituents | C0 or C1 | free constituents separate at c (EXACT kinematics). Positive contact binding of massless constituents gives no bound state or a tachyonic one, since the threshold is at s = 0. A sharp mass needs signed binding or supplied walls (a bag). | — | ARGUED |
| Lifting (internal U(1) clock) | C1 | that of the signed rule it relabels | identical to it (Lemma B) | EXACT |
| **(d) C2: direct order-invariant kernel** | **signed, no path sum** | **yes, by construction** | **~1e-103 at 1 km** | see §5 |

### 5. Q3: the most promising route, C2

**Definition.**
- The kernel is K(x,y) = a·L(x,y) + T(τ̂_xy)·1{y ≺ x}, with:
  - T(τ) = −(m/4πτ)J₁(mτ);
  - τ̂ = (24n/(πρ))^{1/4};
  - n = the number of events in the open interval I(y,x).
- The detector signal is S = ρ⁻²Σ_{x≠y} D*(x)K(x,y)J(y).
- There is no recursion and no regeneration along the trip (EXACT, by definition).

**Mean.**
- E[aL] → δ(σ)/2π (Johnston).
- n ~ Poisson(ρV) exactly (Slivnyak–Mecke). So E T(τ̂) → T(τ), with relative bias ≤ 1e-3 at N = 536 to 3.4e5 (mc3) and a phase smear of e^{−(mτ)²/(32N)}.
- So the mean is the 3+1 massive retarded kernel, with one cone: every species uses the same order (CHECKED; the near-cone region is ARGUED to be negligible).

**Noise law.**
- **Point to point.** sd/envelope = |T′|τ/(4√N). It matches the exact Poisson sums to within 1% (one turning-point row is off by 3%). It is 7e-4 to 2e-2 at τ/ℓ = 8–40, against Johnston's ρ-independent two-link floor of 0.15–8.5 at the same (τ, m). It falls as ρ^{−1/2}.
- **Packet plus detector (EXACT Poisson U-statistic):**
  Var/S̄² = 1/(ρV_part,det) + 1/(ρV_part,src) + ρ⁻²∫∫|D|²T²|J|²/S̄²,
  with V_part the participation 4-volume of the packet in the window.
- **Estimator term (EXACT Poincaré inequality, given Poisson concentration):** at most (mτ)²/(16N_Δ)·η⁻², where η ≤ 1 is the coherence efficiency of the source–detector pair. The full bound is Var ≤ 3·[U-terms + estimator term].
- **1+1 check (mc4, ρ = 1):**

| Run | Mean S (sim) | Continuum | Var S_true (sim) | Exact U-statistic | Var_est − Var_true | Common-mode estimate |
|---|---|---|---|---|---|---|
| A: m = 0.4, w = 6, t₀ = 150, 300 realizations | 412.7 ± 2.4 | 415.1 | 1743 ± 140 | 1777 | 1.97e4 | 2.00e4 |
| B: m = 0.2, w = 8, t₀ = 170, 150 realizations | 1804 ± 11 | 1791 | (1.68 ± 0.19)e4 | 1.81e4 | 6.8e4 | 8.7e4 |

  - The rigorous Poincaré bound holds in run A: 1.6e7 against a simulated 2.1e4. It is loose because of the triangle inequality.
  - The per-realization relative noise is dominated by the estimator at these low densities: 0.37 in run A and 0.16 in run B.

**Translation (ℓ = ℓ_P, L = 1 km, τ = L/(βγ); mc5).**
- Assumed inputs (ARGUED):
  - packet width σ ≥ 1 nm, with V_part ≥ σ³·σ/β;
  - the estimator term multiplied by a safety factor of 4;
  - the pair term bounded through a resonant-source efficiency of 4m²/(T_sT_W).
- The bar is Var/mean² < 0.1.

| Particle | β | Kinetic energy | τ (m) | N_Δ | Estimator term | U-terms (1 nm) | Pair term ≤ | Total |
|---|---|---|---|---|---|---|---|---|
| electron | 1e-8 | 1.1e-10 eV | 1e11 | 1.9e182 | 8.7e-137 | 1.4e-111 | 1e-274 | 1.4e-111 |
| electron | 1e-3 | 0.26 eV | 1e6 | 1.9e162 | 8.7e-127 | 1.4e-106 | 1e-249 | 1.4e-106 |
| electron | 0.9 | 661 keV | 484 | 1.1e149 | 3.7e-120 | 1.2e-103 | 9e-234 | 1.2e-103 |
| proton | 1e-8 | 2.1e-7 eV | 1e11 | 1.9e182 | 3.0e-130 | 1.4e-111 | 8e-265 | 1.4e-111 |
| proton | 1e-3 | 469 eV | 1e6 | 1.9e162 | 3.0e-120 | 1.4e-106 | 8e-240 | 1.4e-106 |
| proton | 0.9 | 1.2 GeV | 484 | 1.1e149 | 1.3e-113 | 1.2e-103 | 6e-224 | 1.2e-103 |

- Even with η⁻² ≤ 1e12, the estimator term stays ≤ 1e-101.
- The Fresnel number mσ²/τ is ≲ 10 for the listed packets, so η = O(1). This is ARGUED by stationary phase.

**Verdict for Q3: M-PASS, source-driven scope.**
- Not tested: interactions along the trip, composition of kernels (G∘G ≠ G), and initial-value evolution.
- The source-driven scope matches E1′'s gravity PASS. TESTS.md's "include regeneration" requirement does not apply: C2 has none, by definition.

## What any such route would add to the axioms (prices only)

**C0 (all weights positive).** No axiom change rescues it, because Lemma A is a theorem about positive Lorentzian kernels. The ways around it leave the setting:
- a Euclidean substrate with OS reconstruction (the framework's own Z³×Z_τ regulator is of this type), losing per-realization real time on random sets;
- nonlinear readouts (ratios, logarithms, post-selection), which lie outside H1 and are untested.

**C1 descent.** A Poincaré-invariant extra spatial dimension: a Lattice and dimension change. It still fails in 3+1.

**C1 lifting.**
- Price: an internal U(1) phase per event.
- The Qubit axiom's M₂(C) already carries phases, so this is arguably not new structure (ARGUED).
- It buys nothing for noise.

**(b) Higgs-like.** A condensate field on links, its own dynamics, and a coupling. The re-emission weight stays signed (−yΦ²), with Johnston's structure.

**(a) Composites.** A binding or confining dynamics with phases, or supplied walls.

**C2 (the route that is coherent).**
1. The E1′ event substrate, with all its conflicts.
2. A supplied kernel F_m(n), one function per mass. The mass and the propagator are inputs, not derived.
3. All-pairs coupling, weighted by the interval count. This goes beyond nearest-neighbour Admissibility and has unbounded valency.
4. Signed or complex amplitude values.
5. No evolution law and no interaction vertex.
6. Calibration of τ̂ by the density ρ.

## What a referee should re-check

1. **Lemma A:** whether translation invariance and linearity are the right hypotheses, given that a detection probability is |S|² of a linear amplitude S.
2. **Lemma D:**
   - (i) the orbit decomposition of nonnegative Lorentz-invariant retarded measures on M^{1,4};
   - (ii) the descent identity for measures, including the image sum on S¹;
   - (iii) Lerch uniqueness for distributions on [0, ∞);
   - (iv) the Bernstein step;
   - (v) a compact w with only local 4+1 invariance.
3. **Lemma B:** that it covers every C1 form allowed by the PREREG, including random backgrounds (the identity holds per realization).
4. **C2:** the U-statistic variance formula, the Poincaré estimator bound and its η, and mc4 runs A and B. Run B's common-mode estimate is 1.3× the measured excess, i.e. conservative.
5. **Whether C2 is admissible for Q3,** since it supplies the propagator by hand, and whether source-driven scope satisfies the lane M reading.
6. **mc6:** the signed-source extension of E1′-b.
7. **Rows labelled ARGUED in §4:** the composite and Higgs-like discussions are ARGUED, not proved.

## Suggested next test (a dated new entry, not a change to any reading)

**"M-A′: re-emission averaged over many events".** Johnston's sign is decided at single events. Replace the single-event re-emission ab·Σ_{z⋖x} with an average over a Lorentz-invariant set of N_s events (for example, interval layers). Then measure:
- whether the two-link floor falls like N_s^{−1/2};
- what non-locality scale that costs.

This is the bridge between M-A's noisy recursion and C2's coherent direct kernel.

## Files

Scratch folder: `/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/c3/M-C/`

- `PREREG.md`
- **`scripts/`:**
  - `mc1_lemmas.py`
  - `mc2_descent_mean.py`
  - `mc3_direct_point.py`
  - `mc4_direct_1p1_sim.py`
  - `mc5_translate.py`
  - `mc6_signed_source.py`
  - `mc7_poincare_bound_1p1.py`
  - `e1p_needle_copy.py` (a verbatim copy of the packet's `E1p_1_massless_needle.py`)
- **`out/`:**
  - `mc1_lemmas.out`, `mc2_descent_mean.out`, `mc3_direct_point.out`, `mc5_translate.out`, `mc7_poincare_bound_1p1.out`;
  - the 1+1 runs: `mc4_run_A.out`, `mc4_run_B.out`, and their arrays `mc4_m0.4_w6.0_t150.0_R300_s11.npz`;
  - the signed-source checks: `mc6_D60_s6.out`, `mc6_D40_s12.out`.


---

## Adversarial check (Opus 5.5 xhigh)

**Supported:** False

**Corrected verdict:** The labels survive under the worker's own PREREG readings, but only in narrower form. The verdict as worded claims more than was proved.

Q1, C0-FAIL: CONFIRMED (EXACT, elementary).
- No linear, translation-invariant, source-driven rule with every weight ≥ 0 has the KG-massive retarded kernel as its mean.
- This holds in every dimension, not only 3+1, because the zero mode is sin(mt)/m in 1+1, 2+1 and 3+1 alike.
- A nonnegative kernel can carry the m-pole only on top of a non-oscillating carrier at least as large (the carrier inequality, which is correct).

Q2, C1-FAIL: met as the PREREG words it, but carries no information about mass.
- Part (i) is a tautology: a positive hop times a signed state is a signed observable.
- Because of (i), the C1-PASS branch ("not a relabelling of a signed rule") could never be reached under the PREREG's own wording.
- Part (ii), Lemma D, is EXACT only for Fourier-mode (Kaluza–Klein) descent.
- C1 is not a no-go on mass. C1 rules with an exact 3+1 massive mean exist:
  - Johnston's rule lifted to an internal U(1) phase;
  - a nonnegative, 4+1 Lorentz-invariant cone parent δ(σ₅) read out with the signed, non-Fourier profile g(w) = δ(w)/2π − (m/4π)J₁(m|w|). This gives exactly δ(σ)/2π − mJ₁(mτ)/(4πτ) (checked).

Overall M-C: FAIL, retitled.
- New title: "No KG-massive wave from all-nonnegative linear weights. Moving the sign into the state, readout, background or an extra coordinate gives the same random variable as a signed rule."
- Not established: "positivity cannot be the mechanism of mass". Positive slower-than-light transport is not excluded, and nonlinear readouts are untested.
- The no-go still needs the codex sol referee.

Q3, route C2: Var/mean² ≪ 0.1 at 1 km for the electron and the proton is CONFIRMED and robust.
- The estimator term stays ≤ 1e-57 even with a hostile cancellation ratio.
- The total is ≤ 1.2e-103. It is set by the assumed 1 nm source and detector 4-volumes (Poisson sampling), not by anything about the mass.
- Record it as "C2 coherence PASS under the M-C PREREG Q3 reading: supplied kernel (one function per mass), all-pairs non-local, source-driven, no dynamics and no regeneration".
- Do not record it as a lane-M or M-A matter-coherence PASS, and do not cite it as evidence for mass without signed weights.

**Issues:** 1. Lemma D's scope is overstated, and part of it is refuted.
   - Overstated text: "positive-hop descent gives massive matter in 2+1 and 1+1, never in 3+1"; the candidate-table row "(c) Descent | 2+1 only"; the prices line "C1 descent ... still fails in 3+1"; and the claim that the only alternative is a phase register.
   - Lemma D excludes only the Fourier-mode readout e^{imw}.
   - Counterexample: keep a nonnegative, 4+1 Lorentz-invariant parent (the cone measure δ(σ₅), which is the normalised mean shape of positive 4+1 link hops). Read it out over w with the signed, non-Fourier profile g = δ(w)/2π − (m/4π)J₁(m|w|). The result is exactly the 3+1 massive retarded kernel.
   - Checked: pointwise error O(ε) (1e-4 at ε = 1e-3), and Laplace transforms agree to 10 digits.
   - 4+1 invariance is kept, so this is not the "phase register" case. It is a C1 rule, and like every C1 rule it is a relabelling.
   - Lemma D's own steps are correct: k̂ = √(π/s)e^{−m²/4s}; forced parent s^{1/2}/(2π^{3/2}) = −FP σ₊^{−3/2}/(4π²). The Bernstein step needs Laplace transformability; Titchmarsh's Volterra uniqueness on [0,T] removes that need.

2. The C1-FAIL "(no-go)" label is a strong word not earned. Under Lemma B, (i) is true by definition, and C1-PASS required "not a relabelling", which Lemma B makes impossible. So Q2 was decided by how it was worded, not by a result. C1 rules do reach the massive mean (point 1, and the lifted Johnston rule). C1 "fails" only in that it is not sign-free.

3. The headline is broader than the proof (headline scope discipline).
   - What is proved: under H1–H3, a linear observable with all weights ≥ 0 cannot have the KG kernel as its mean.
   - Lemma A is close to trivial: G_R's tail is negative just inside the cone (−m²/8π), so no nonnegative measure can equal it. The carrier inequality is the content beyond that.
   - The worker concedes that positive massive transport is not excluded ("the sign buys the wave"). So "massive matter without signed weights: FAIL" and the PREREG gloss "positivity cannot be the mechanism of mass" need the narrower title above.
   - The qualifier "in 3+1" matters only for Lemma D. Lemma A holds in every dimension.

4. Q3: the mc4 table misreports the observable.
   - The column "Mean S (sim)", run A 412.7 ± 2.4 and run B 1804 ± 11, is S_true, the kernel evaluated at the true τ.
   - The C2 observable is S_est. Its simulated mean is 395.0 ± 8.5 in run A, 2.4σ below the continuum value 415.1.
   - The cause is the phase smear of the τ̂ estimator. The exact Mecke mean of S_est is 398.2 (factor 0.959) in run A and 1771.9 (factor 0.989) in run B, and the simulations agree (pulls −0.38σ and −0.16σ).
   - The smear is negligible at physical parameters (factor e^{−(mτ)²/(32N)} differs from 1 by ~1e-120). The report should show S_est's mean and name the bias.

5. mc5 kinetic energies at β = 1e-8 are double-precision cancellation artifacts in γ − 1.
   - Electron: the correct value is 2.6e-11 eV, not 1.1e-10. Proton: 4.7e-8 eV, not 2.1e-7.
   - τ = L/(βγ) is correct, so the noise numbers are unaffected.

6. Small misstatements:
   - "Var/mean² ≤ 1e-103": the maximum is 1.23e-103.
   - "relative bias ≤ 1e-3": the maximum is 1.01e-3.
   - "Fresnel number ≲ 10": the actual values are 1e-17 to 1e-5. The statement is true but loose, and it supports η = O(1).
   - Run B's common-mode estimate is called "conservative". It is an unbounded estimate that sits about 2σ high, not a bound.

7. Q3 is near-automatic by construction.
   - C2 supplies the propagator. Its only randomness is Poisson sampling of the source and detector, plus the N^{−1/2} error of the volume estimator.
   - Any smooth kernel of macroscopic interval counts would pass.
   - Q3 is the worker's own reading. The lane-M reading in TESTS.md was written for a path sum that "includes regeneration along the trip" and does not transfer.
   - The worker states most of these prices; the label must carry them.

8. The packets spread a great deal over 1 km: from 1 nm to about 4e7 m for the slow electron, about 2e4 m for the slow proton. This does not hurt the noise bound, which is set by the detector and source 4-volumes. It does mean "packet width σ ≥ 1 nm" describes the source, not the packet at the detector.

No problems found with the following:
- the zero modes, k̂, the forced parents and their m-independence (re-run, identical);
- the point-to-point estimator law (re-run, identical);
- the Poisson U-statistic variance (an independent seed reproduces it: 2184 ± 350 against 1777, and the estimator excess 1.89e4 against 2.0e4);
- the signed-source extension of E1′-b (an independent seed gives Var/Ñ = 0.80–0.93 against the bound 3);
- τ = L/(βγ);
- the claim that no repository file was edited (git status is clean; the needle copy is verbatim).

**Re-runs:** All checks were run with OMP_NUM_THREADS=2, and each took under 1 minute. Folder: /private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/c3/M-C/verify/

- **v_mc1.py, v_mc3.py:** verbatim re-runs of mc1_lemmas.py and mc3_direct_point.py. Output is byte-identical to the worker's mc1_lemmas.out and mc3_direct_point.out.
- **v1_nonfourier_descent.py:** the counterexample to the general Lemma D. A positive 4+1 cone parent with a signed non-Fourier w-profile gives the 3+1 massive tail, with relative error 1e-3 at ε = 1e-2 and 1e-4 at ε = 1e-3. Its Laplace transform equals e^{−m²/4s}/2π to 10 digits.
- **v2_c2_mean_smear.py:** the exact Mecke mean of the C2 observable S_est in the 1+1 control.
  - Run A: 398.17 against the simulated 394.96 ± 8.5. The phase smear gives a factor of 0.959 relative to S_true's 415.09.
  - Run B: 1771.9 against 1768.0 ± 24 (factor 0.989).
- **v3_translate_checks.py:**
  - kinetic energies without the γ − 1 cancellation (the β = 1e-8 values in mc5 are artifacts);
  - τ = L/(βγ) confirmed;
  - Fresnel numbers 2.6e-17 to 9.8e-6;
  - with a hostile cancellation ratio (σE)⁴ per side, the estimator term is still ≤ 6e-58;
  - packet spreading estimates.
- **v_mc4.py 0.4 6 150 80 99** (independent seed, R = 80):
  - mean S_est 392 ± 16;
  - Var S_true 2184 ± 350 against the exact U-statistic value 1777;
  - Var_est − Var_true 1.89e4 against the common-mode estimate 2.0e4.
- **v_mc6.py 60 6 500 77** (independent seed): Var/Ñ = 0.80–0.93 against the bound 3; the means match the exact values within 1σ.
- **Not re-run:** mc4 run B in full, mc6 at D = 40, s = 12, and mc7. The mc7 bound was checked by reading it: it is loose, as stated, because it uses the triangle inequality.
