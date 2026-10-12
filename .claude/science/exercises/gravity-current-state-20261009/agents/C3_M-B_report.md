# C3 lane M-B: worker report (Claude Opus 5.5, max effort; 2026-10-10)

Verbatim. Adversarial check (Opus 5.5 xhigh) below the report. **Codex sol referee: CONFIRMED WITH CORRECTIONS. The lane is INCONCLUSIVE. Theorem A: no jointly Poincare-equivariant isometry with finite event fibers can move amplitude between events. Theorem B: the sprinkling cannot select an antichain. Neither excludes supplied-slice dynamics or link (arc) states. The swerve result holds only for the greedy chain, typically about 9.75 Planck times. An arc unitary, a massive mean and 1 km coherence are all open** (C3_M-B_referee.md).

**Verdict (worker):** INCONCLUSIVE. The no-go covers event states and slice states (EXACT under stated hypotheses) but not link (arc) states, which are the checkerboard's own structure. Arc states survive the definability obstruction. Their simplest unitary form, single-chain or permutation transport, swerves to the light cone within about 20 Planck times. Spreading arc rules remain open: no mean dispersion and no controlled coherence law. The no-go parts need the codex sol referee before they are recorded.

**Plain summary:** I tried to build a norm-preserving (unitary) matter rule on a Poisson sprinkling from the order and links alone. If the quantum state is an amplitude, or a finite spinor, per event, no such rule exists. Lorentz invariance in law would force each event's normalized emission to spread evenly over infinitely many boosted directions, which is impossible. This is an exact BHS-type theorem that holds in every dimension, 1+1 included. Slices do not rescue it: the law cannot choose a slice, link rules have no finite-depth slice data, and on finite regions the slice's dimension changes at most growth steps. A rule whose state lives on the links themselves escapes the theorem, because each incoming link supplies its own frame. But its simplest unitary form, where each link continues to one next link, kicks the velocity by about half a unit of rapidity per Planck step, and a particle at rest runs off toward light speed within about 20 Planck times. Whether a spreading link rule can keep electrons and protons coherent over a kilometre is open, so the lane is INCONCLUSIVE, and the no-go parts go to the referee.

# M-B report: unitary matter on links (campaign C3, lane M)

**Worker:** Claude Opus 5.5, max effort.
**Timeline:** PREREG.md stamped Sat Oct 10 01:02:17 UTC 2026, before any computation. Runs 01:05–01:20Z.
**Setting:** test setting only. The E1/E1′ axiom conflicts apply: Lattice is replaced, the causal order is supplied, and records-as-events conflict with one record per site.
**Edits:** no repository file was edited. No papers were downloaded.

## Verdict against the fixed reading (TESTS.md, C3, M-B)

**INCONCLUSIVE.**
- **Not PASS.** No rule was built that is norm-preserving, Lorentz-invariant in law, massive with one cone in mean, and coherent over 1 km by a controlled law.
- **Not FAIL.**
  - The no-go below covers states that live on events (class E) and on slices (class S).
  - It does not cover states that live on links ("arcs", class R). Arcs are the Feynman checkerboard's own structure: on the regular checkerboard the state is (site, direction).
  - Class R survives the definability obstruction.
  - My pre-registered mapping, fixed before any run, was: a no-go for some classes with another class open maps to INCONCLUSIVE.
- **Bounded no-go results inside** (Theorem A, Theorem B, Proposition C, Proposition R3) must go to the codex sol referee before they are recorded. Hence needs_referee = true.
- **If the referee rules arc states outside the registered setting,** Theorem A alone would make the reading FAIL under stated hypotheses. I think arc states are inside the setting ("chiral hopping … or any unitary link walk").

## What I read

**In full:**
- `docs/MINIMAL_AXIOMS_2026-06-29.md` (233 lines);
- `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md` (3 primitives; none bears on this lane);
- in the packet:
  - TESTS.md: the rules, E1′, the E1′ results, E1′-b and its result, and all of Campaign C3;
  - SUMMARY.md §7–9;
  - agents/E1p_report.md, E1p_referee.md, supervisor_E1p_b.md, E1p_b_referee.md, prior_art_event_history.md;
- block 122 (`docs/ADMISSIBILITY_RULE_WAVES_NEED_SIGNED_WEIGHTS_…_2026-09-24.md`);
- `scripts/E1p/e1p_core.py`.

I reused `sprinkle4d_diamond` and `past_links` from e1p_core (read-only import).

**Prior art, not repeated.**
- The 2026-03/04 event era used complex-phase path sums on Euclidean-coordinate DAGs and died of rank-1 transfer collapse.
- Here: Lorentzian Poisson sprinklings, no coordinates in any law, no transfer matrices. The results are about the structure of norm preservation, not finite-N means.

**Block 122 connection.**
- Johnston's massive kernel needs signed weights.
- A unitary rule replaces "signed weights" with "unitary amplitudes". The question becomes whether a Lorentz-invariant law can carry a normalized amplitude at all.

## Classes and hypotheses

**Common setting.**
- Π is a Poisson sprinkling of M^{1,d}, d = 1 (control) and d = 3, at density ρ = ℓ^{-(d+1)}, with ρ = 1 in the numerics.
- A rule "built from order and links" is a measurable map from the configuration to amplitudes that is equivariant under the proper orthochronous Poincaré group. Order-only and link-only rules automatically qualify, since Poincaré maps preserve the order.
- I.i.d. auxiliary marks with a Lorentz-invariant law, such as random phases, are allowed.

**The four classes:**
- **E (event states):** a finite-dimensional state per event (C^k, with any finite-dimensional Lorentz representation), with an event-local positive norm.
- **S (slice states):** amplitudes on antichains, with slice-to-slice maps.
- **R (arc states):** one amplitude per link, with a coin at each event mapping in-arcs to out-arcs.
- **SJ:** the global Sorkin–Johnston Fock construction.

## 1. Event states: no propagating norm-preserving rule (Theorem A, EXACT)

**Hypotheses.**
- **(A1) Equivariance.** For each Poincaré g = (Λ, a):
  - W_{gΠ}(gy, gx) = D(Λ) W_Π(y,x) D(Λ)^{-1};
  - N_{gΠ}(gx) = D(Λ)^{-†} N_Π(x) D(Λ)^{-1};
  - D is any finite-dimensional representation of (the cover of) SO⁺(1,d), N_x > 0 is the norm density at x, and W(y,x) ∈ M_k(C) is the amplitude from x to y.
- **(A2) Single-event isometry.** Σ_y ξ†W(y,x)†N_yW(y,x)ξ = ξ†N_xξ for all ξ, a.s. for every x ∈ Π. The step that hands x's amplitude to its successors (any successor set, including all future links, with an optional "stay" term W(x,x)) conserves the norm.
- **(A3) Full sprinkling.** No boundary, and no supplied slice or frame.

**Conclusion.** W(y,x) = 0 for every y ≠ x, a.s. Amplitude never leaves its event.

**Proof.**
1. Define n(y,x) = tr(N_x^{-1}W(y,x)†N_yW(y,x))/k ≥ 0. By cyclicity of the trace it is invariant under the (A1) transformation for any D, and (A2) gives Σ_y n(y,x) = 1.
2. By the Mecke equation and Slivnyak's theorem (the Palm version of Π at 0 is Π ∪ {0}; with marks, an independent mark at 0), ν(B) := E⁰[Σ_{y∈Π∪{0}} n(y,0)1_B(y)] is a probability measure on R^{1,d}.
3. Lorentz maps fix 0 and preserve the Palm law. With step 1, ν is Lorentz-invariant.
4. **Lemma: the only Lorentz-invariant probability measure on R^{1,d} is δ₀.**
   - With u = t + x¹ and v = t − x¹, the rapidity-1 boost maps the shell {e^j ≤ |u| < e^{j+1}} onto the next shell.
   - Invariance makes all shells equal in measure; finiteness makes them 0. So ν{u ≠ 0} = 0, and likewise for v.
   - So ν lives on {t = x¹ = 0}. Boosts along x², …, x^d leave only the origin.
5. Hence ν = δ₀. So W(y,0) = 0 for y ≠ 0 Palm-a.s., and by Mecke W(y,x) = 0 for all x ≠ y, a.s. ∎

**Remark (d = 3).** If D is non-trivial, an equivariant N cannot exist at all.
- A boost acts on N by N → e^{−ηK†}Ne^{−ηK}, where K has real non-zero eigenvalues λ_j.
- This rescales the diagonal entry N_jj by e^{−2ηλ_j}. No probability law for ln N_jj is invariant under all those shifts.
- This is BHS's no-frame obstruction in the form "no equivariant positive norm density" (COMPARATOR: Bombelli–Henson–Sorkin 2009; the proof above is self-contained).

**In plain words.** One unit of norm cannot be shared evenly among infinitely many boosted directions. Weighting some directions more than others picks a frame, and no equivariant rule can pick one.

**What Theorem A kills:**
- normalized complex-weight link path sums with per-event amplitudes, including any attempt to rescale Johnston's aL or aL(I − abL)^{-1} into a unitary step;
- chiral or checkerboard hopping whose components sit on the event, with any mass-flip amplitude ∝ i·m·ℓ;
- vertex quantum walks on the link graph, and any rule that picks a successor set from the order;
- the same rules with i.i.d. random phases or coins.

**What it does not cover:**
- arc states (class R);
- supplied frames or slices;
- non-local norms (SJ-type);
- rules that are isometric only on a subspace of extended states, for example a spectral subspace of an equivariant operator.

## 2. Slice states

**Theorem B (EXACT): the law cannot choose a slice.** No measurable, time-translation-equivariant map selects a nonempty antichain of Π.
- Such an antichain A would be a stationary point process with E#(A ∩ [0,T]×Q) = λTδ^d, for a spatial cube Q of side δ.
- Two points of the column R×Q more than √dδ apart in time are timelike-related. So A's points in the column lie in one window of length √dδ.
- Their number is at most the maximum Poisson count over about T/(√dδ) windows, whose mean is O(log T). So λ = 0 and A = ∅ a.s. ∎
- **So any slice is supplied boundary data, and it carries a frame.**

**Proposition C1 (EXACT in expectation; a.s. ARGUED, standard): link rules have no finite-depth slice data.**
- In a link rule, ψ(y) depends on ψ at all of y's past links.
- By Mecke, the expected number of past links whose time extent in a fixed frame exceeds any h is infinite. Link velocities fill H^d with constant intensity, and boosted links are long.
- So continuing across any cut needs amplitudes at events arbitrarily deep below it. An event-state slice is not Cauchy data. The Cauchy data of a link rule are the links crossing the cut, which is class R.

**Proposition C2 (EXACT count; CHECKED frequencies; `s3_frontier_merge.py`).**
- Grow a sprinkled diamond in time order (a natural labelling).
- Adding element e removes the k frontier elements below e. EXACT: these are exactly e's past links that are still maximal. Then e is added.
- So dim ℓ²(frontier) changes by 1 − k. An isometry needs k ≤ 1; a unitary needs k = 1.

| dim | N | P(k=0) | P(k=1) | P(k≥2) | per-realization P(k≥2) |
|---|---|---|---|---|---|
| 3+1 | 574 | 0.557 | 0.252 | 0.192 | 0.178–0.203 |
| 3+1 | 2720 | 0.500 | 0.274 | 0.225 | 0.222–0.229 |
| 3+1 | 8569 | 0.482 | 0.284 | 0.234 | 0.232–0.235 |
| 1+1 | 1582 | 0.350 | 0.394 | 0.257 | 0.251–0.260 |
| 1+1 | 6287 | 0.342 | 0.405 | 0.254 | 0.251–0.257 |
| 1+1 | 19609 | 0.334 | 0.415 | 0.251 | 0.251–0.252 |

About a quarter of growth steps destroy dimension, and only 28–42% preserve it. Only the time-ordered labelling in one frame was tested.

**Quantum walks between maximal antichains therefore fail in three ways:**
- the slices must be supplied (Theorem B);
- event-state slices are not Cauchy data for link rules (C1);
- on finite regions the dimension changes (C2).

## 3. Arc states (class R): what survives and what is known

**R1. Why Theorem A does not apply, and the price (EXACT).**
- The norm unit is attached to an incoming link. Its stabilizer is the compact rotation group SO(d) about the link's own velocity.
- The Palm measure over (in-arc, out-arc) pairs is an infinite invariant coupling of the in- and out-link intensity measures. No invariant probability measure is needed, so there is no contradiction.
- **The price:** the per-event state space is ℓ² of infinitely many in-links, on which Lorentz acts (in law) by permutation. Unitarity plus Lorentz invariance forces an infinite-dimensional internal "velocity" degree of freedom. Finite-dimensional unitary representations of SO⁺(1,d), d ≥ 2, are trivial (standard).
- **Definability:** an equivariant unitary coin is plausible but not constructed. Candidates are the polar part of an invariant kernel operator, or an equivariant perfect matching, as in Lyons–Nazarov-type results on non-amenable spaces (COMPARATOR, unverified). This is ARGUED.

**R2. The link-velocity process (EXACT; CHECKED; `s1`, `s4`).**
- By Mecke, an event's link 4-velocities form an invariant point process on H^d with intensity ρ∫τ^d e^{−ρV(τ)}dτ per unit hyperbolic volume:
  - 6/π = 1.9099 in 3+1;
  - exactly 1 per unit rapidity in 1+1.
  - Both integrals were checked by quadrature.

| ball radius r (rapidity) | exact mean (6/π)·vol_H³(r) | measured mean | ratio | per-realization var/mean (Fano) |
|---|---|---|---|---|
| 0.5 | 1.051 | 0.985 ± 0.054 | 0.94 ± 0.05 | 1.23 |
| 1.0 | 9.761 | 9.54 ± 0.25 | 0.977 ± 0.026 | 2.83 |
| 1.5 | 42.11 | 41.79 ± 0.70 | 0.993 ± 0.017 | 4.58 |
| 2.0 | 139.74 | 139.57 ± 1.50 | 0.999 ± 0.011 | 6.46 |
| 2.5 | 415.22 | 419.1 ± 2.4 | 1.009 ± 0.006 | 8.06 |

The counts are overdispersed, with Fano ≈ 3.2·r for r = 1–2.5 (CHECKED range only). Velocity counts self-average more slowly than Poisson counts.

**R3. Single-chain transport swerves (EXACT in law; CHECKED; `s1`, `s2`).**
- **Rule.** The amplitude of an in-arc continues on exactly one out-arc. This covers any permutation coin and the checkerboard's "continue straight" leg.
- **(i) EXACT inequality.** The kick (hyperbolic distance between in- and out-velocity) is at least the distance to the nearest out-arc. Measured on 4052 in-arcs: mean 0.465, median 0.449, P(> 0.2) = 0.94.
- **(ii) Greedy chain** (take the nearest-velocity out-link each step, the smallest kick possible):
  - The explored region is a stopping set disjoint from the current event's future, so by the strong Markov property of the Poisson process the kicks are i.i.d. and isotropic in the current rest frame (EXACT in law).
  - Hence cosh d_{k+1} = cosh d_k·cosh s_k + sinh d_k·sinh s_k·cos θ_k, and d_N/N → E[s coth s] − 1 a.s. The identity (1/2)∫ln(cosh s + c·sinh s)dc = s coth s − 1 was checked by quadrature.

| | 3+1 (60 chains × 600 links) | 1+1 (40 chains × 2500 links) |
|---|---|---|
| kick | s mean 0.462, sd 0.185 | E w² = 0.250, mean w = 0.0004 |
| law | drift E[s coth s] − 1 = 0.0805 ± 0.0003 per link | rms rapidity √(0.250·N) |
| measured | slope 0.0812 (links 300–600); mean rapidity 41.8 ± 0.8 at 500 links, per-chain sd 6.2 | rms 17.2 at 1000 links (law: 15.8; 40 chains) |
| chosen-link τ | 1.35ℓ | 1.05ℓ |

- Truncation flags: 31 of 36,000 steps in 3+1; 1% of steps in 1+1, where any missed closer link would need τ > 5ℓ.
- **Consequence.** A particle at rest reaches γ = 2 after about 16 links in 3+1 (about 22 Planck times, 1.2e-42 s), or about 7 links in 1+1. Its velocity escapes toward the light cone, so the mean is not massive with one cone.
- **Labels.** For general permutation coins the kick bound (i) is EXACT. Their kick directions may correlate with the past configuration, so their drift is ARGUED.

**R3b. Unitary permutation coins (CHECKED proxy; `s5`).**
- Minimum-cost bijections between in- and out-arcs within rapidity 2.5, reporting the in-arcs with rapidity ≤ 1.
- Mean kick 0.88 with distance cost, 0.98 with cosh cost: about twice the nearest-neighbour bound.
- Isotropic-drift proxy: 0.32–0.34 per link.
- Part of the excess is in/out count imbalance in the window (R2's overdispersion).

**R4. The unitarity mismatch (EXACT lemma; CHECKED numbers; `s4`, `s4b`).**
- **Lemma.** For any unitary coin C and any target b: ‖Ca − b‖ ≥ |‖a‖ − ‖b‖|.
- **Application.** Suppose coherence means reproducing a fixed velocity profile f on the arcs: amplitude f(velocity) times a phase on each arc.
  - Then ‖a‖² and ‖b‖² are the sums of |f|² over the in- and out-arcs.
  - The past and future cones are disjoint, so these sums are independent.
  - So every event costs fidelity at least δ = (√S_in − √S_out)²/E[S], whatever the coin.
- **Measured (300 independent cone pairs each):**

| profile | E S | per-realization relative sd | E[δ] per event |
|---|---|---|---|
| ball r = 0.5 | 1.05 | 1.08 | 0.79 ± 0.06 |
| ball r = 1.0 | 10.1 | 0.53 | 0.137 ± 0.011 |
| ball r = 1.5 | 43.4 | 0.33 | 0.053 ± 0.004 |
| ball r = 2.0 | 142.0 | 0.21 | 0.024 ± 0.003 |
| ball r = 2.5 | 419.1 | 0.14 | 0.010 ± 0.001 |
| Gaussian σ = 0.5 | 1.47 | 0.62 | 0.188 ± 0.014 |
| Gaussian σ = 0.75 | 5.92 | 0.42 | 0.086 ± 0.007 |
| Gaussian σ = 1.0 | 17.6 | 0.29 | 0.042 ± 0.003 |

- A packet whose arc profile stays within rapidity about 2.5 of its own velocity loses at least about 1% fidelity per event (CHECKED) against any fixed-profile representation. It decoheres in about 100 Planck steps.
- **Not covered:**
  - **Much wider profiles.** δ falls roughly like r·e^{−2r} in the tested range. Reaching 1e-38 per step would need r ≈ 45. There arcs are so long that the proton's mass phase m·τ·cosh r is O(1). ARGUED, not used for the verdict.
  - **Representations whose normalization adapts event by event.**

**R5. The mean coin (EXACT structure; ARGUED consequence).**
- Lorentz invariance in law makes the first-moment coin, acting on the internal velocity profile, a radial operator on L²(H^d): a function of the hyperbolic Laplacian, with spherical symbol k̂(λ).
- **If the coin's reach decays exponentially in rapidity:**
  - k̂ is analytic and tends to 0, so |k̂| = 1 only at isolated internal frequencies;
  - the mean coin then cannot be unitary on any band of normalizable profiles;
  - the deficit goes into fluctuations, by the sum rule E‖Cψ‖² = ‖E[C]ψ‖² + E‖(C − E C)ψ‖². Applying this to arc states is ARGUED.
- **Coins with slowly decaying reach,** with amplitude on arbitrarily boosted links (tails ~e^{−r}/r), can be unitary in mean on a band. They are not excluded.

**R6. Open.**
- No spreading arc coin was constructed. Its mean dispersion and per-realization coherence were not computed.
- **The open question:** is there an equivariant, long-reach unitary arc coin whose mean on a band of internal profiles is massive with one cone, with per-step fluctuations ≲ 2e-38 there?

## 4. Sorkin–Johnston (ARGUED)

- SJ is unitary at the Fock level: a positive state from iΔ, with Δ = K_R − K_A. It has no step evolution.
- Packet amplitudes are W(g,f) with W = Pos(iΔ), built from Johnston's signed K_R.
- So its noise is M-A's question, not a new unitary route. Not computed.

## 5. 1+1 against 3+1

- Theorems A, B and C hold for every d ≥ 1, because SO⁺(1,1) is non-compact. 1+1 does not escape.
- **Velocity space:** R (amenable) in 1+1, H³ (non-amenable) in 3+1. Single chains diffuse in 1+1 (√N) and drift ballistically in 3+1 (0.08 per link). Both swerve.
- 1+1 has extra intrinsic structure: the conjugate order of a 2D order fixes left/right up to a global swap (COMPARATOR, unverified). It might support a chiral arc rule with no 3+1 analogue. Not tested.

## 6. Translation to 1 km (τ = L/(βγ))

**Proper times:**
- proton at p = 1 GeV/c: βγ = 1.066, τ = 938 m = 5.8e37 ℓ_P, about 4.3e37 link steps;
- electron at p = 1 MeV/c: βγ = 1.957, τ = 511 m = 3.2e37 ℓ_P, about 2.3e37 link steps.

**Per class:**
- **Classes E and S:** no rule, so no number.
- **Class R, single chains:** γ = 2 within about 16 links (1.2e-42 s). Excluded for both particles at any momentum.
- **Class R, fixed-profile coherence:**
  - 1 km needs a per-step infidelity ≲ 2e-38.
  - The exact bound gives ≥ 1e-2 per step for profiles within rapidity 2.5.
  - Wider profiles were not tested. There is no controlled law, so no verdict.

**Context outside the fixed reading (COMPARATOR + ARGUED).**
- Several estimates point to a dephasing proper time of order 1/(m²ℓ):
  - the E1′ renewal gain;
  - an argued phase walk along chains;
  - the δ-scaling above.
- That is 2.7e3 m for the proton and 9.2e9 m for the electron.
- It scales as 1/m², so heavy atoms test it harder. For Cs it is 0.16 m/c = 5e-10 s, while atom interferometers keep Cs/Rb coherent for about 1 s.
- If a later reading uses this scale, the e/p 1 km bar is not the sharpest test.

## What a referee should re-check

1. **Theorem A, hypothesis (A2).**
   - Is single-event isometry the right formalization of "norm-preserving" for event-state rules?
   - The loophole of rules isometric only on a subspace of extended states is listed as outside the theorem.
2. **The invariance of n(y,x)** for non-unitary D, and the Mecke/Slivnyak step with marks.
3. **The Lemma:** the only Lorentz-invariant probability measure on R^{1,d} is δ₀ (the shell argument).
4. **Theorem B's column argument,** and C1's step from expectation to almost surely.
5. **The C2 identification:** the frontier elements below e are exactly e's still-maximal past links.
6. **The stopping-set argument** that makes greedy kicks i.i.d. and isotropic, and the drift law. Is the "unsafe" truncation rate (0.09% in 3+1) negligible?
7. **Whether fixed-profile targets are a fair definition** of coherence for arc states; the adaptive-normalization loophole.
8. **The R5 claims:** analytic symbols for exponentially short-reach coins, and the sum rule applied to arc states.
9. **The SJ identification** (argued only).
10. **Scope:** are arc states inside the registered M-B setting? If not, Theorem A gives FAIL under stated hypotheses.

## Files

Scratch: `/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/c3/M-B/`
- `PREREG.md`
- `scripts/`:
  - `mb_common.py`
  - `s1_link_velocity_intensity_and_kicks_3p1.py`
  - `s2_greedy_chain_swerve.py`
  - `s3_frontier_merge.py`
  - `s4_arc_norm_mismatch_3p1.py`
  - `s4b_arc_norm_mismatch_gauss_3p1.py`
  - `s5_matching_coin_kicks_3p1.py`
- `out/`:
  - `s1_link_velocity_intensity_and_kicks_3p1.out`, `s1_kicks.npz`
  - `s2_greedy_chain_swerve_3p1.out`, `s2_greedy_chain_swerve_1p1.out`, `s2_greedy3p1.npz`, `s2_greedy1p1.npz`
  - `s3_frontier_merge.out`
  - `s4_arc_norm_mismatch_3p1.out`
  - `s4b_arc_norm_mismatch_gauss_3p1.out`
  - `s5_matching_coin_kicks_3p1.out`


---

## Adversarial check (Opus 5.5 xhigh)

**Supported:** True

**Corrected verdict:** M-B: INCONCLUSIVE. The verdict holds, with corrections to the supporting claims.

Why INCONCLUSIVE follows:
- No rule meets PASS.
- The fixed FAIL reading needs a no-go that covers the M-B setting. Arc (link) states are clearly inside that setting: the regular-lattice checkerboard named in it has arc states (site, direction), and "any unitary link walk" includes walks on links. Class R is not excluded, so the worker's pre-registered mapping gives INCONCLUSIVE.

Status of the pieces, all pending the codex sol referee:
- **Theorem A (class E): CONFIRMED by my reading.** Steps 1–5 are correct and the shell lemma is correct. The proof uses only joint Poincaré invariance in law of (Π, W), so it also covers "Lorentz-invariant-in-law" rules, not only factor maps.
- **Class S: only a partial no-go.** It holds for local single-element-merge isometries along a natural labelling on finite regions (C2, EXACT identity). Theorem B is a slice-selection theorem, not a dynamics no-go. C1 is about link propagation rules.
- **Class R: open.** EXACT kick lower bound for any permutation coin; EXACT drift for the greedy lower-bound chain; drift ARGUED for general permutation coins. The fixed-profile infidelity bound is CHECKED only for profiles within rapidity 2.5.
- **SJ: ARGUED only.**

Corrected statements:
1. "The no-go covers class E and class S" becomes: it covers class E, and class S only for local merge maps on finite regions.
2. "If arc states were ruled out of the setting, Theorem A alone would give FAIL" is not true under the worker's own pre-registered mapping: class S is not fully covered.
3. γ = 2 is reached at a median of 7 links in 3+1 (mean 8.3), about 9.5 ℓ_P, not 16 links. In 1+1 the median is 8 links.
4. Section 6: "single chains excluded" becomes EXACT for the greedy chain only (which is not itself unitary) and ARGUED for permutation coins.
5. "Decoheres in about 100 Planck steps" becomes: at least about 1% infidelity per walk step against a fixed-profile target, for the tested ball and Gaussian profiles.
6. The wide-profile remark is wrong as stated. The arc route stays at least as open as reported.

**Issues:** 1. **Overclaim on class S** (verdict section: "the no-go covers states on events (E) and on slices (S)").
   - Theorem B only shows that no equivariant rule can pick out a slice. A slice rule can be defined for every slice (or every slice pair) and still be equivariant; the initial slice and state are supplied data, as for any packet. So B is not a dynamics no-go.
   - C1 is about link propagation rules (event data are not Cauchy data), not about slice walks.
   - C2 is EXACT only for local maps that merge k frontier elements into one, along a natural labelling, on finite regions. On the infinite sprinkling, maximal antichains are infinite, so counting ℓ² dimensions gives no obstruction. Non-local slice maps are not covered. Only the time-ordered labelling was tested, and that labelling is itself frame-dependent. Nothing shows that steps with k ≥ 2 are unavoidable under every labelling.
   - "And it carries a frame" (after Theorem B) is not proved. A supplied slice breaks translation invariance; nothing shows it picks a Lorentz frame.

2. **Inconsistency with the PREREG.** The report says that if arc states fall outside the setting, "Theorem A alone would make the reading FAIL". The worker's own fixed mapping says FAIL only if the no-go covers every class in the setting. Class S is only partly covered, so FAIL would still not follow.

3. **Numerical slip (R3, §6).** "γ = 2 after about 16 links (22 Planck times, 1.2e-42 s)" comes from applying the large-d drift 0.0805 per link from d = 0 (arccosh 2 / 0.0805 = 16.4). The worker's own chain data (`s2_greedy3p1.npz`) show:
   - the first link with γ ≥ 2 has median 7 and mean 8.3 (range 2–22);
   - mean rapidity is already 1.635 at link 10.
   The true time is about 7 × 1.35 ℓ ≈ 9.5 ℓ_P ≈ 5e-43 s. In 1+1 the median is 8 links (mean 12.8); the report says about 7. The error makes the result look weaker than it is, not stronger.

4. **Strong word in §6.** "Class R, single chains: … Excluded for both particles at any momentum" is stronger than R3's own labels.
   - Only the kick lower bound (mean 0.465) is EXACT for all permutation coins.
   - A lower bound on each kick does not force drift: a rule that looks back along its chain could steer back toward its earlier velocity.
   - The drift law is EXACT only for the greedy chain, which is a lower bound and not a bijection (not unitary).
   - It should read: ARGUED for permutation coins, EXACT for the greedy chain.

5. **Strong word in R4.** "It decoheres in about 100 Planck steps" is not earned.
   - A unitary rule on one realization keeps a pure state.
   - What R4 bounds is infidelity to a fixed velocity-profile target, not the M-reading observable (Var/mean² of a detector amplitude), which is not computed.
   - For the r = 2.5 ball, one walk step advances packet-frame time by about E τ · E cosh η ≈ 1.507 × 4.27 ≈ 6.4 ℓ, not 1 ℓ_P.
   - "At least about 1% for any profile within rapidity 2.5" is CHECKED only for the ball and for Gaussians with σ ≤ 1.

6. **The lab/walk-step to proper-time conversion is wrong for wide profiles** (R4 "not covered" remark; ARGUED, not used for the verdict).
   - The remark counts 1 km as τ/1.35ℓ ≈ 4.3e37 walk steps whatever the profile width, and finds r ≈ 45, where the proton's mass phase m·τ·cosh r is O(1).
   - But a step along an arc of rapidity η advances packet-frame time by τ cosh η. So the number of steps falls like 1/E[cosh η].
   - Redoing the count with the worker's own δ ≈ Fano/(2 E S) and Fano ≈ 3.2r gives r ≈ 30, where the mass phase is about 7e-7, not O(1).
   - So the obstacle the remark implies goes away, and the wide-profile loophole is more open than reported.
   - Deeper issue: for wide profiles a walk step is not a time slice at all (arcs advance different times), so the step-to-proper-time map needs a stated detector observable.
   - The τ = L/(βγ) conversion itself is correct:
     - proton: βγ = 1.0658, τ = 938.3 m = 5.80e37 ℓ_P;
     - electron: βγ = 1.957, τ = 511.0 m = 3.16e37 ℓ_P.
   - The step counts use the greedy chain's τ of 1.35ℓ. The mean link τ is 1.507ℓ. This is an O(10%) issue.

7. **SJ (§4).** "Its noise is M-A's question" is overstated. Pos(iΔ) is a non-local, non-linear spectral functional of iΔ, and its per-realization noise is not the noise of the retarded kernel K_R. This is labelled ARGUED, but the identification should be dropped.

8. **Minor points.**
   - The R2 table mixes sources without saying so: the means for r ≤ 2.0 come from s1 (400 realizations), while the r = 2.5 row and the whole Fano column come from s4 (300 cone pairs).
   - "Only 28–42% preserve it" should be 25–42%: P(k=1) = 0.252 at N = 574 in 3+1.
   - The 1+1 truncation sentence wrongly attaches the τ > 5ℓ guarantee to the 1% unsafe steps. It holds for the safe steps. The truncation bias is in fact negligible (my check).
   - The Cs and atom-interferometer context assumes the composite's total mass enters as m (ARGUED). The numbers are right: 2.74e3 m, 9.23e9 m, 0.157 m, 5.2e-10 s.

9. **Checked and found correct.**
   - Theorem A: n(y,x) invariance (cyclic trace, also for non-unitary D); Mecke and Slivnyak step; shell lemma (only δ₀); W = 0 off the diagonal.
   - The Remark: correct for d = 3, where boost generators are diagonalizable with real eigenvalues. In d = 1, unipotent representations need a separate argument; the claim still holds, and the worker limited the Remark to d = 3.
   - Theorem B: the column / O(log T) argument.
   - C2: the identification that frontier elements below e are exactly e's still-maximal past links.
   - R2 intensities: 6/π and 1.
   - R3: the strong-Markov argument. The explored set is I⁺(e_j) minus the future cones of e_j's links, a stopping set disjoint from I⁺(e_{j+1}). The identity ½∫ln(cosh s + c sinh s)dc = s coth s − 1 holds.
   - R4: the lemma ‖Ca − b‖ ≥ |‖a‖ − ‖b‖|, and the independence of the past and future cones.
   - R5: the sum rule. Analyticity of k̂ needs reach decaying faster than e^{-r} on H³, which matches the worker's long-reach exception.
   - No mean over seeds is presented as a per-realization law. C2 and R2 give per-realization spreads; R4 is a per-event mean, which is the relevant quantity for an extended packet.

**Re-runs:** All my checks are in /private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/c3/M-B/verify/. No repository file and no worker output was modified. s2 and s4 were re-run as copies, with fresh seeds, in verify/scripts.

- **v1_frontier_bruteforce.py: independent check of C2.**
  - Method: full causal and link matrices; diamonds in 3+1 (N ≈ 850–910) and 1+1 (N ≈ 850–890), 3 realizations each.
  - Results: 0 frontier mismatches against brute-force maximal elements, and 0 frontier-below elements that are not links. The identity is CONFIRMED.
  - Frequencies:
    - 3+1: P(k ≥ 2) = 0.198–0.212, P(k = 1) = 0.24–0.27;
    - 1+1: P(k ≥ 2) = 0.255–0.261, P(k = 1) = 0.38–0.40;
    - both consistent with the worker's table.
- **v2_checks.py: integrals, chain crossings and conversions.**
  - ∫τ³e^{-πτ⁴/24} = 1.909859 = 6/π.
  - The 1+1 integral is 1.000.
  - ½∫ln(cosh s + c sinh s)dc equals s coth s − 1 to 6 digits at s = 0.2, 0.5, 1 and 2.
  - Mean link τ (3+1) = 1.507ℓ; the greedy chosen-link τ is 1.353ℓ.
  - From the worker's npz:
    - 3+1: the first link with γ ≥ 2 has median 7 and mean 8.3;
    - 1+1: median 8 and mean 12.8.
  - Conversions:
    - proton τ = 938.3 m = 5.805e37 ℓ_P;
    - electron τ = 511.0 m = 3.162e37 ℓ_P;
    - 1/(m²ℓ) = 2.74e3 m for the proton, 9.23e9 m for the electron, and 0.157 m (5.2e-10 s) for Cs.
- **v3_theoremA_and_extrap.py: Theorem A step 1 and the wide-profile recount.**
  - The invariance of n under 200 random SL(2,C) D (boosts plus rotations, non-unitary) holds to a relative error of 1.2e-9.
  - The worker's model δ(2.5) = 0.0096 against the measured 0.0104.
  - Required r: 44.9 with the report's step count; 30.1 with the packet-frame-time step count (mass phase 1.9 versus 7e-7).
- **s2 copy, seed 90210.**
  - 3+1, 30 chains × 400 links: kick mean 0.4625, sd 0.187; predicted drift 0.0808 ± 0.0006; second-half slope 0.0854 (still converging); 13 unsafe steps.
  - 1+1, 40 chains × 1000 links: E w² = 0.247; rms 14.7 at 1000 links against a law value of 15.7.
- **v4_1p1_window.py: 1+1 truncation check.** E w² = 0.2498 ± 0.0033 at U = 16 and 0.2484 ± 0.0032 at U = 60. The truncation bias is negligible.
- **s4 copy, seed 31337, 100 cone pairs.**
  - δ = 1.01 ± 0.11 at r = 0.5, 0.179 ± 0.034 at r = 1.0, 0.070 ± 0.011 at r = 1.5, 0.0247 ± 0.0042 at r = 2.0, and 0.0107 ± 0.0019 at r = 2.5.
  - Fano = 1.26, 2.71, 4.87, 6.73 and 8.51 at the same radii.
  - These reproduce the worker's values within errors.
