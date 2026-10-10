# C3 lane D: worker report (Claude Opus 5.5, max effort; 2026-10-10)

Verbatim. Adversarial check (Opus 5.5 xhigh) below the report. **Codex sol referee: NOT CONFIRMED. The lane is INCONCLUSIVE. Exact narrow no-gos: order alone gives no per-event spinor or frame mark, no handedness, and no gamma.Delta mean of a fixed-fiber kernel. But scalar link propagation plus apparatus differentiation, and the order-only Kahler-Dirac cochain dG, reproduce the massless Dirac response in mean. Chiral matter needs an orientation and spin-transport primitive, as a price** (C3_D_referee.md).

**Verdict (worker):** FAIL (bounded), matching the fixed reading's named example: the order alone gives no spinor structure and no chirality without a frame (exact theorems). A referee is required. Two loopholes are flagged for the referee. (1) Frames held by the source and detector (class E): if the referee counts these as a "link-only spin-1/2 propagator", the verdict becomes INCONCLUSIVE pending lane M. (2) The non-chiral Kähler–Dirac route: its coboundary is order-only and coherent, but its codifferential is untested.

**Plain summary:** The causal order alone cannot carry spin-1/2. Anything computed from the order looks the same after any Lorentz transformation and after a mirror reflection, so its average can never be a spinor propagator and it can never tell left-handed from right-handed (exact). Nor can a Lorentz-invariant event substrate hold a frame, a null direction, a spinor or a finite cell structure at its events (exact, extending Bombelli–Henson–Sorkin). If the source and detector supply the frame, link-only propagation gives the exact massless Weyl/Dirac propagator, with noise bounded like E1′'s scalar field. The spin then lives in the apparatus, and the massive case is lane M's open problem. If instead a frame is put on every link, the mean is still right, but the noise grows by a factor (π/√2)·D·λ̄/ℓ², confirmed numerically to 0.01%; for every real source that leaves the signal swamped by 26 to 46 orders of magnitude. The frame-free Kähler–Dirac route (forms on chains of events) passes the noise test for its order-only part, but it cannot be chiral, and its other half (the codifferential) is untested. One qubit per event has no Chen–Kapustin analogue, and Jordan–Wigner strings span about half of all events.

# Lane D (campaign C3): spin-1/2 matter on links. Worker report

**Worker:** Claude Opus 5.5, max effort. **Date:** 2026-10-10, from 00:53Z.

**Pre-registration:** `PREREG.md`, stamped `Sat Oct 10 01:12:48 UTC 2026`. It was written before any computation.

**Setting:** a test setting only. The E1/E1′ axiom conflicts apply:
- Lattice is replaced.
- The causal order is supplied, because records carry no time.
- Records as events conflict with "one record per site, permanent".

## Verdict against the fixed reading

**FAIL (bounded).** This follows the pre-registered mapping B, and it is the reading's named FAIL example: "no spinor structure from order alone without a frame". Under TESTS.md:9 and the C3 rules it must go to the referee.

**Established.**
- **T1 (EXACT).** No order-only rule has a spin-1/2 propagator as its mean.
- **T2 (EXACT).** No order-only rule can tell left-handed from right-handed.
- **T3 (EXACT).** No Lorentz-invariant event substrate can carry a frame, a null direction, a spinor or a locally finite cell structure at its events. This holds even as independently supplied random marks.

**What a supplied frame buys.**
- **Class E: frame at the source and detector only.**
  - The mean is exact.
  - The noise is bounded by E1′-b extended to signed weights.
  - The spin structure lives in the apparatus, not in the substrate.
  - The massive leg is exactly lane M's scalar problem.
- **Class F: frame on every link.**
  - The mean is right, CHECKED to 0.1%.
  - The noise is (π/√2)·D·λ̄/ℓ² times class E's: exact diagonal law, asymptotic CHECKED to 1e-4.
  - For every real source this means incoherence by a factor of 1e26 to 1e46.

**Flags for the referee.**
- **Flag 1 (pre-registered).** If apparatus-held frames are ruled a "link-only spin-1/2 propagator", class E must meet the M-bars for the electron and the proton. That is lane M, so the verdict would become **INCONCLUSIVE pending lane M**.
- **Flag 2 (found during the work).** The **Kähler–Dirac route** (fields as cochains on chains of events, "spin from taste" as in G0c and staggered fermions) is not excluded.
  - Its coboundary d is order-only. Its noise penalty is only λ̄/δ (CHECKED), which is affordable.
  - It cannot be chiral (T2).
  - Its codifferential, which needs the metric, was not tested.
  - The FAIL therefore rests on the chirality requirement (part of the registered mean: "one cone, chirality") and on genuine spinor indices. It does not rest on a proof that no taste-type Dirac fermion can come from the order.

## Plain summary

- **What the order cannot do.**
  - Anything computed from the causal order alone looks the same after any Lorentz transformation and after a mirror reflection.
  - So its average can never be a spinor propagator, and it can never tell left-handed from right-handed.
  - No Lorentz-invariant event substrate can carry a frame, a null direction, a spinor or a finite cell structure at its events.
- **Frame at the source and detector.** Link-only propagation then gives the exact massless Weyl/Dirac propagator, with noise bounded like E1′'s scalar field. But the spin lives in the apparatus, and the massive case is lane M's open problem.
- **Frame on every link.** The mean is still right, but the noise grows by (π/√2)·D·λ̄/ℓ². That is at least about λ̄/ℓ ≈ 1e13 to 1e22 for any real source, which leaves the signal swamped by 26 to 46 orders of magnitude.
- **The Kähler–Dirac route.** Forms on chains of events pass the noise test for their order-only part. But they cannot be chiral, and their codifferential is untested.
- **One qubit per event.** There is no Chen–Kapustin analogue, and Jordan–Wigner strings span about half of all events.

## What I read

- **In full:**
  - `docs/MINIMAL_AXIOMS_2026-06-29.md` (233 lines);
  - `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md`, with all 3 primitives. None supplies a frame or an orientation on events. On Z³ the Lattice axiom's "proper cubic rotations" supply both, which is what G0c used.
- **Packet TESTS.md:**
  - lines 1–40, the rules plus T1's setup;
  - lines 143–546: E1, E1 results, E1′ and its results, E1′-b and its result, campaign C3, and the added lanes including Lane D at 538–546.
  - Lines 41–142 (the T1 and T2 results) were not read.
- **Packet SUMMARY.md** §7–9 (lines 117–232).
- **Packet agents files:**
  - `prior_art_event_history.md`, `E1p_report.md` and `E1p_referee.md`, all in full;
  - `E1p_b_referee.md` and `supervisor_E1p_b.md`, both in full (the massless bound reused here).
- **Candidate pack** `TEST_LOG.md`, lines 195–324: G0 and G0c, with the referee.
- **Code:**
  - `scripts/E1p/e1p_core.py` and `scripts/E1p/E1p_1_massless_needle.py` in full; both were copied into my scratch folder and reused;
  - `scripts/E1/bd_core.py`, lines 1–80.

## Hypotheses

- **H1.** A Poisson sprinkling of M^{1,3} at density ρ = ℓ⁻⁴, with M^{1,1} as a control. Its law is invariant under translations and under the whole orthochronous Lorentz group, parity included.
- **H2 (order-only).** A measurable function of the isomorphism class of the marked poset (Π ∪ {endpoints}, ≺). It may use fixed internal matrices and independent randomness. "Link-only" is the special case that depends only on links.
- **H3.** Source-driven fields from smooth macroscopic sources, as in E1′, on a flat background.
- **H4 (targets).** The massless retarded Weyl propagator S_W = σ̄^μ∂_μG_R and the Dirac propagator S_R = iγ^μ∂_μG_R, with G_R = θ(t)δ(τ²)/2π. The massive target is (iγ·∂+m)G_R^{(m)}. Chirality is included.

## Survey (COMPARATOR)

These come from web-search excerpts and abstracts only. Nothing was downloaded; `lit/` is empty.

**The comparators.**
- **Johnston's thesis** (arXiv:1010.5514). It calls a retarded Dirac propagator on causal sets elusive and sketches two routes:
  - a checkerboard path sum over null zigzags;
  - a "square root" of the Klein–Gordon kernel. The 2023 review arXiv:2306.04800 notes this root is non-unique.
- **Noldus** (arXiv:1305.0443). A "generating structure" replaces the Dirac operator, with ghosts and negative-norm states. A massless example on a diamond uses a chosen structure.
- **Gudder** (arXiv:1507.01281). A discrete Dirac operator on "covariant causal sets" with shell sequences. I saw the abstract only, so whether it is order-only was not checked.
- **Foster–Jacobson** (hep-th/0310166 and arXiv:1610.01142). Spinors on regular lattices with null faces, so the frame is built in.
- **Jacobson (1984).** A spinor-chain path integral built from products of (Δ·σ).
- **Review** (arXiv:2306.04800). It gives no 4D fermion construction.
- **BHS** (gr-qc/0605006): there is no equivariant direction. See also Dowker–Sorkin (arXiv:1909.06070).
- **Kähler–Dirac / geometric fermions** (Becher–Joos; Banks–Dothan–Horn; Rabin, 1982), from memory: forms carry 4 Dirac tastes.

**Where the comparators sit in this report's classes.**
- Checkerboard and spinor-chain sums need a null direction per segment, so they are class F.
- An order-only square root is excluded by T1. The non-uniqueness Johnston names is the symptom: nothing in the order selects the γ structure.

## Results

### D-T1 (EXACT): the mean of any order-only rule is a Lorentz scalar

**Statement.** Under H1–H2, take any F(Π; x, y, U) with values in End(V), with E|F| < ∞. Then:
- **(i) Per realization:** F(ΛΠ+a; Λx+a, Λy+a, U) = F(Π; x, y, U) for every orthochronous Λ, proper or improper. The reason is that Λ maps the marked poset order-isomorphically.
- **(ii) In mean:** M(Δ) = E F depends on Δ = x − y only through τ² (and the time direction), because ΛΠ+a has the same law as Π.

**The mean cannot be a spinor kernel.** The Weyl and Dirac kernels contain σ̄^iΔ_i·δ′(τ²)/π, which changes under spatial rotations, so M ≠ S. Approximation fails too: for any rotation-invariant norm, ‖M − S‖ ≥ ½·sup_R ‖S∘R − S‖ > 0.

**The covariant case.** Suppose F is also required to be covariant, U(Λ)FU(Λ)⁻¹ = F(Λ·). Then F commutes with the whole spinor representation, so by Schur's lemma it is a scalar on each irreducible block. Again there is no γ·Δ structure.

**Invariant decorations do not help.** Decorations whose joint law with Π is Lorentz invariant (for example random internal gauge fields) give the same conclusion.

### D-T2 (EXACT): the order has no handedness

**Statement.** Parity P is an order isomorphism, F(PΠ; Px, Py, U) = F(Π; x, y, U), and PΠ has the same law as Π.

**Consequences.**
- Every order-only quantity is parity-even in each realization.
- Every parity-odd order-only quantity is identically 0. This covers handedness, the ε-tensor part of a spinor trace such as tr[(Δ₁·σ)(Δ₂·σ̄)(Δ₃·σ)(Δ₄·σ̄)], and γ⁵ on forms (the Hodge star needs an orientation).
- **Hence every order-only fermion theory is vector-like.**

**What chirality would need.** A supplied orientation:
- at least one global bit;
- plus a rule to read local orientation, which no local order functional can supply.

**Contrast with the axioms.** On Z³ the Lattice axiom covers only *proper* rotations, so it supplies the orientation.

### D-T3 (EXACT; BHS-type, extended): no frame, direction, spinor or finite cell structure at an event

**Statement.** Use the Palm process Π ∪ {0} (Slivnyak). Its law is invariant under SO⁺(1,3), or under SL(2,C) for spinor targets. Then no measurable equivariant map D(Π∪{0}, U) ∈ X exists, even with independent randomness U, for any of these targets X:
- the hyperboloid H³ (timelike directions; this case is BHS);
- de Sitter dS₃ (spacelike unit vectors);
- the celestial sphere S² (null directions);
- Weyl spinors C²∖{0};
- spinors up to phase (null flags);
- spin frames SL(2,C) and orthonormal frames SO⁺(1,3);
- nonempty finite subsets of M⁴∖{0}, i.e. finite neighbour sets.

**Proof.** The pushforward would be an invariant probability measure on X. None exists:
- **H³, dS₃ and frames.** Boosts carry a compact set of positive mass into infinitely many disjoint copies of equal mass.
- **S².** The boost z ↦ eᵗz pushes S²∖{0,∞} into any neighbourhood of ∞. Rotation-transitivity makes every atom zero, so ν = 0, a contradiction.
- **Spinors, flags and spin frames.** Each maps equivariantly to S² via ξ ↦ [ξ].
- **Finite subsets.** Boosts in random directions send every nonzero point to infinity. That contradicts invariance of the positive-mass set of configurations of bounded extent.

**Extension to supplied marks (EXACT).** Let each event carry a mark in any such X, with a Poincaré-invariant joint law. Then the Palm law of the mark is again an invariant probability measure on X, which cannot exist. Likewise, a mark in a finite-dimensional representation with no invariant vectors (spinors, vectors) must be 0 almost surely, by boost contraction.

**Consequences.**
- **(a) Frames break Lorentz invariance.** Any frame or spinor carried by events, whether derived from the order or supplied at random, breaks Lorentz invariance in law. A gauge-redundant frame with a non-normalizable orbit measure is not a probabilistic record state.
- **(b) Locked values must be invariant.** A record that locks spinor- or vector-valued content at events cannot have a Lorentz-invariant law. The locked content must be invariant, and spin can enter only through relations or amplitudes. This matches §8's "an event happening ≠ a value being locked".
- **(c) No equivariant cell complex.** No Lorentz-equivariant locally finite cell complex can be built on the events. Its cells at the Palm point would form a finite neighbour set.

### 1+1 control

**What the order supplies.** In 1+1 the two null directions are invariant under boosts.
- COMPARATOR: by Dushnik–Miller (1941) and Gallai (1967), a *prime* 2D order fixes its conjugate (left/right) order up to reversal.
- So the null directions *are* order-supplied, up to one global parity bit.
- That a large sprinkled diamond is prime is ARGUED, not checked.

**What it does not.** The boost frame (rapidity ∈ ℝ) has no invariant probability measure. Spinor components carry boost weight ±½, so T1 still applies.

**The lesson.** In 3+1 the order lacks both the directions and the boost frame. In 1+1 it lacks only the boost frame, plus the parity bit.

### Class E: frame at the source and detector only (bulk = scalar links)

**Construction.** ψ_E(x) = ρ⁻¹Σ_{y⋖x} a·(iγ^μ∂_μη)(y). The bulk transports an internal C⁴ by the identity.

**Mean (EXACT).** S_R = iγ·∂G_R, so integrating by parts onto the source gives E ψ_E → ∫S_Rη. This inherits E1′'s E[aL] → G_R. Chirality comes from the apparatus projections only (T2).

**Noise (ARGUED from the refereed E1′-b proof, plus CHECKED).**
- The Poincaré bound carries over with |J| in the cut terms. The triangle inequality is the only new step.
- So Var ψ_E ≤ (3 + C′_J·s/D)·Diag(|J|²), where C′_J includes a source-regularity constant.

**Massive.** ψ = ρ⁻¹ΣK_m(x,y)[(iγ·∂+m)η](y). Its noise is **exactly lane M's scalar problem**, which is M-INCONCLUSIVE in E1′. It is not computed here.

**Scope.** Class E is the spin-1/2 analogue of lane G-B (a tensor from a conserved source on links). It is valid in flat space between frame-carrying apparatus. It gives no spin–curvature coupling, and parity violation comes only from the apparatus.

### Class F: frame on every link (embedding vector Δ = x − y per link)

**Construction.** ψ_F = ρ⁻¹Σ_y (ρ/12)·σ̄·Δ·[L0 − 2L1](x,y)·η(y). Here L0 is the link indicator and L1 = 1{|I(y,x)| = 1}. The profile is order-only.

**Profile identity (EXACT, CHECKED numerically).**
- Write m = ρπτ⁴/24 and Q(s) = (πρ/12)(1−2m)e^{−m}, with s = τ².
- Then ∫Q ds = 0, ∫sQ ds = −1 and ∫s²Q ds = −√24·ℓ². Numerically: 1.3e-6, −1.0000000000, −4.898979.
- So Q → δ′(τ²), and E ψ_F → ∫σ̄·∂G_Rη: the right mean.

**Noise ratio law.**
- **EXACT:** the Mecke diagonal terms.
- **CHECKED:** the asymptotic, numerically.
- Shell integrals: ∫e^{−m}ds = √6 and ∫(1+4m)e^{−m}ds = 3√6.
- These give R² ≡ [Diag_F/m_F²]/[Diag_E/m_E²] → (3/(144a²))·∫_cone r g²/∫_cone (∂_tg)²/r → (π²/2)·D²λ_eff²/ℓ⁴.
- Here λ_eff² = ⟨g²⟩/⟨(∂_tg)²⟩ on the cone section; for a wave, λ_eff = λ̄.

**Lower bound (ARGUED).**
- Var ψ_F ≥ (1 − C′s/D)·Diag_F. The pair terms are supported on needle overlaps (E1′-b geometry). The rigorous route is the first-chaos bound Var ≥ ‖E D_zψ‖².
- Cauchy–Schwarz gives |m_E| ≤ √(Diag_E·N̄_supp).
- Together: rel_F ≥ √(1−C′s/D)·R/√N̄_supp ≈ 0.98·(λ̄/ℓ)·(D/s)^{3/2}, which is ≳ λ̄/ℓ for every source with s ≤ D.

**Why it fails.** The derivative is taken across the link shell, whose cone-normal thickness is about ℓ²/D. The mean is a cancellation between layers, and the noise does not cancel.

### Kähler–Dirac route (cochains on the order complex)

- **The coboundary is order-only.** The coboundary d is order-only and finite (EXACT). From a 0-form source η₀ the Kähler–Dirac field is exactly dφ, with φ = G_Rη₀ the scalar link field.
- **No shared links (EXACT).** For substrate events x1 ≺ x0, no source point is linked to both, because y ≺ x1 puts x1 inside I(y,x0).
- **Noise (CHECKED, D7).** Var(dN) equals Var N0 + Var N1 to within |corr| ≤ 0.07. So rel(dφ) ≈ √2·(λ̄/δ)·rel(φ) for chains of extent δ ≫ ℓ²/D.
- **Physical scales (ARGUED).** The penalty λ̄/ℓ (1e13 to 1e22) is below class E's margin of 1e28 to 1e36, so the coboundary part stays coherent.
- **Below the shell thickness.** The mutual blocking of substrate events distorts the mean: the dt = 0.05 row has the wrong sign.
- **Still missing (ARGUED):**
  - The codifferential δ needs the Hodge star, i.e. the metric. An order-only δ needs sums of the Benincasa–Dowker (BD) type over unboundedly many chains (E1's noise gain). Not tested.
  - Taste multiplicity 4.
  - Spin read only from taste.
  - In curved geometry, forms couple as integer-spin tensors (COMPARATOR).
  - Non-chiral (T2).

### One qubit per event (G0c analogue)

- **Chen–Kapustin (G0c).** It needs a locally finite cellulation plus a framing, so T3(c) and T3 exclude any Lorentz-equivariant version (EXACT, given CK's structural needs, which are COMPARATOR).
- **Jordan–Wigner along a natural labelling (CHECKED, D5).**
  - Strings are extensive and depend on the labelling.
  - 83–89% of string sites are spacelike to both ends of the hop.
  - Mean links per event: 12.6, 34 and 67 at T = 8, 12, 16, i.e. unbounded valency.
- **Untested.** Infinite-valency structures, for example Hasse-diagram diamonds as plaquettes. There, products such as ∏_{f⊂t} Z_f are infinite (ARGUED).

## Tables

### D1: per-realization statistics, time component of the Weyl field

Setting: ρ = 1, x at the origin, source on a ball of radius s at distance D, Gaussian g of width w offset by u0 = w. Exact means come from quadrature (D1b) and are given relative to the continuum value ∂_tφ.

| D, s, w | n | class | exact mean / continuum | sample mean ± se (exact) | Var/Diag | sd/\|mean\| per realization |
|---|---|---|---|---|---|---|
| 10, 4, 2 | 3000 | E | 1.0165 | 0.1304 ± 0.0008 (0.1297) | 1.613 ± 0.048 | 0.338 |
| | | F | 1.0249 | 0.164 ± 0.043 (0.131) | 1.524 ± 0.045 | 17.98 |
| 40, 8, 4 | 1000 | E | 1.0021 | 0.1277 ± 0.0009 (0.1279) | 1.444 ± 0.065 | 0.230 |
| | | F | 1.0033 | −0.04 ± 0.42 (0.128) | 1.307 ± 0.058 | 103.6 |
| 100, 8, 4 | 1000 | E | 1.0008 | 0.0506 ± 0.0005 (0.0511) | 1.132 ± 0.052 | 0.319 |
| | | F | 1.0013 | −0.78 ± 0.63 (0.051) | 1.133 ± 0.052 | 391.8 |
| 100, 12, 6 | 600 | E | 1.0006 | 0.1158 ± 0.0009 (0.1149) | 1.330 ± 0.074 | 0.190 |
| | | F | 1.0009 | 1.50 ± 1.56 (0.115) | 1.231 ± 0.071 | 332.8 |
| 200, 8, 4 | 600 | E | 1.0004 | 0.0255 ± 0.0005 (0.0255) | 1.117 ± 0.064 | 0.454 |
| | | F | 1.0007 | −0.88 ± 1.18 (0.026) | 1.129 ± 0.062 | 1132 |

**Unsigned scalar control.** Var/Diag = 1.78, 1.60, 1.26, 1.57, 1.21, consistent with E1′.

**Class F sample means.** They agree with the exact means within +0.77, −0.40, −1.32, +0.89 and −0.77 standard errors.

**Measured noise ratio F/E** against the exact diagonal R:

| D, s, w | measured F/E | exact R |
|---|---|---|
| 10, 4, 2 | 53 | 55 |
| 40, 8, 4 | 450 | 475 |
| 100, 8, 4 | 1228 | 1226 |
| 100, 12, 6 | 1755 | 1822 |
| 200, 8, 4 | 2492 | 2478 |

**Indicator validation** (links and L1 per realization against Campbell):

| D, s, w | links | Campbell | L1 | Campbell |
|---|---|---|---|---|
| 10, 4, 2 | 32.73 | 32.64 | 16.17 | 16.20 |
| 40, 8, 4 | 65.70 | 65.80 | 32.97 | 32.72 |
| 100, 8, 4 | 26.11 | 26.01 | 13.25 | 13.11 |
| 100, 12, 6 | 89.13 | 88.51 | 44.16 | 44.23 |
| 200, 8, 4 | 13.16 | 13.19 | 6.55 | 6.55 |

### D1c: the ratio law

| D, s, w | exact R | shell asymptotic | ratio | (π/√2)·D·λ_eff |
|---|---|---|---|---|
| 10, 4, 2 | 54.7 | 56.9 | 0.961 | 59.4 |
| 40, 8, 4 | 474.9 | 477.4 | 0.995 | 488 |
| 100, 8, 4 | 1225.8 | 1228.4 | 0.998 | 1240 |
| 100, 12, 6 | 1822.4 | 1825.0 | 0.999 | 1850 |
| 100, 16, 8 | 2407.5 | 2410.0 | 0.999 | 2454 |
| 200, 8, 4 | 2477.9 | 2480.6 | 0.999 | 2492 |
| 400, 8, 4 | 4982 | 4985 | 0.9995 | 4997 |
| 1000, 8, 4 | 12496 | 12499 | 0.9998 | 12511 |
| 3000, 12, 6 | 56297 | 56300 | 0.99995 | 56326 |

Both class means equal the continuum value to 1.0000 at D = 3000.

### D6: translation at ℓ = ℓ_P

**Assumptions.**
- The class E noise bound is √(3·C_coh/N̄), with C_coh = 2 as measured.
- The class F lower bound is R/√N̄_supp.
- N̄ = (√6/2)·V₃/(Dℓ²).

| case | λ̄ | N̄ | class E rel noise ≤ | R | class F rel noise ≥ |
|---|---|---|---|---|---|
| lab, 1 MeV, 1 mm source, 1 km | 2.0e-13 m | 2.0e58 | 1.7e-29 | 1.7e60 | 1.2e31 |
| lab, 1 GeV, 1 mm, 1 km | 2.0e-16 m | 2.0e58 | 1.7e-29 | 1.7e57 | 1.2e28 |
| ν, 3 MeV, 1 m source, 1 km | 6.6e-14 m | 2.0e67 | 5.5e-34 | 5.6e59 | 1.3e26 |
| SN1987A ν, 15 MeV, 3e4 m, 1.6e21 m | 1.3e-14 m | 3.3e62 | 1.3e-31 | 1.8e77 | 9.7e45 |
| ν, 1 PeV, 1e9 m, 1 Gpc | 2.0e-22 m | 6.4e71 | 3.1e-36 | 5.2e73 | 6.5e37 |

### D7: Kähler–Dirac coboundary on a chain

Setting: D = 40, s = 8, w = 4, n = 300 per row, chain x1 = x0 − (dt, 0, 0, 0). "Shared" is the number of source points linked to both ends.

| dt | shared | E N0 | E N1 | E dN (sim) | corr(N0,N1) | Var(dN) vs Var0+Var1 | rel noise of dN | rel noise of N0 |
|---|---|---|---|---|---|---|---|---|
| 0.05 | 0 | 12.50 | 13.05 | −0.549 (−0.65 ± 0.21) | −0.007 | 13.59 / 13.49 | 6.71 | 0.207 |
| 0.5 | 0 | 13.30 | 12.21 | +1.091 (+0.82 ± 0.20) | +0.072 | 12.12 / 13.06 | 3.19 | 0.194 |
| 1.0 | 0 | 13.11 | 10.97 | +2.134 (+2.03 ± 0.20) | +0.004 | 11.49 / 11.53 | 1.59 | 0.197 |

The predicted penalty √2·λ_t/dt, with λ_t ≈ 6.1, is 17 and 8.6. The measured penalties are 16.4 and 8.1.

### D5: Jordan–Wigner string lengths on 4D diamonds, two realizations each

| T | N | links | mean string | strings > 0.1N | boosted-labelling mean | strings changed by relabelling | string sites spacelike to both ends |
|---|---|---|---|---|---|---|---|
| 8 | 561 / 552 | 7.1e3 | 0.53 / 0.54 N | 97% | 0.38 N | 99.7% | 83–84% |
| 12 | 2733 / 2758 | 9.3e4 | 0.52 / 0.51 N | 97% | 0.36 N | 99.9% | 88–89% |
| 16 | 8693 / 8523 | 5.8e5 | 0.49 N | 97% | 0.34 N | 100% | 89% |

## Verdict in detail and scope

**FAIL**, by pre-registered mapping B.
- Class O (order-only) is excluded EXACTLY: in mean by T1 and in chirality by T2.
- The frame that the correct-mean constructions need is EXACTLY not suppliable by the order (T3). It is not suppliable by any Lorentz-invariant mark field either (T3 extended).

**What the FAIL does not say.**
- That fermions are impossible on events with added structure.
- That the Kähler–Dirac (taste) route fails: its codifferential is untested.
- Anything about interacting bulk vertices, which were not tested.
- Anything about a quantum sum over orders.

**What extra structure would cost.** Under PRIMITIVE_REGISTRY_CHECK, such structure is an unregistered primitive. That means a frame or tetrad field (which breaks Lorentz invariance in law, by T3), or an orientation field.

**Class E reading.** Free spin-1/2 propagation with apparatus frames passes the E1′ massless bar by about 28 orders of magnitude. This is a scope result, not a PASS of the lane: the electron and proton M-bars are lane M's.

## What a referee should re-check

1. **The proofs of T1–T3.** In particular:
   - the absence of invariant probability measures on S² and on finite configurations;
   - the Palm/Slivnyak invariance;
   - the extension to marks;
   - whether "order-only" in H2 is the right reading of "order-only or link-only".
2. **Flag 1.** Whether class E counts as a link-only spin-1/2 propagator. If it does, the verdict is INCONCLUSIVE pending lane M.
3. **Flag 2.** Whether the open Kähler–Dirac route, which is non-chiral, undercuts the FAIL. The chirality requirement in the registered mean is what the FAIL leans on.
4. **The class F derivation.**
   - the profile moments;
   - the shell constants √6 and 3√6, and 3/(144a²) = π²/2;
   - the asymptotic R = (π/√2)Dλ_eff/ℓ²;
   - the ARGUED lower bound Var ≥ (1 − C′s/D)·Diag. A first-chaos computation would make it EXACT.
5. **Other profiles.** Whether profiles with deeper layers or BD smearing at a non-locality scale ℓ_k could cut R. Not computed; I expect R ~ Dλ̄/ℓ_k², which needs ℓ_k ~ √(Dλ̄), far above 1e-19 m.
6. **The signed-weight E1′-b step for class E,** and its regularity constant.
7. **The D7 Kähler–Dirac check.** Only D = 40 was run. The physical translation of the λ̄/δ penalty is ARGUED.
8. **The 1+1 claim.** Gallai's theorem and primeness of the sprinkled order. Primeness is ARGUED.
9. **Comparator accuracy.** The survey rests on search excerpts only.

## Files

All files are under `/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/c3/D/`.

**Pre-registration:** `PREREG.md`.

**Scripts** (`scripts/`):
- `D1_weyl_E_vs_F.py`: classes E, F and S, simulation;
- `D1b_quadrature.py`: exact means and diagonal terms;
- `D1c_ratio_law.py`;
- `D5_jw_label_gaps.py`;
- `D6_tables.py`;
- `D7_kd_chain.py`;
- `e1p_core.py`: a copy of the packet's `scripts/E1p/e1p_core.py`;
- `e1p_needle.py`: a copy of the packet's `scripts/E1p/E1p_1_massless_needle.py`.

**Outputs** (`out/`):
- `D1_main.out`, `D1c_ratio_law.out`, `D5_jw_label_gaps.out`, `D6_tables.out`, `D7_kd_chain.out`;
- `D1_D10_s4_w2_u2.npz`, `D1_D40_s8_w4_u4.npz`, `D1_D100_s8_w4_u4.npz`, `D1_D100_s12_w6_u6.npz`, `D1_D200_s8_w4_u4.npz`.

**Downloads:** `lit/` is empty; nothing was downloaded.

**No repository file was edited.**

---

## Adversarial check (Opus 5.5 xhigh)

**Supported:** False

**Corrected verdict:** INCONCLUSIVE, pending lane M and a controlled noise law. The reading's PASS line is not excluded by any no-go the worker proved.

What to record:
- D-T1, D-T2 and D-T3 are EXACT no-gos within their scope. Send them to the referee as no-gos, per the C3 rule.
  - D-T1: an order-only two-point kernel with fixed internal matrices has a Lorentz-scalar mean, so it is never a spinor kernel.
  - D-T2: anything computed from the order alone is parity-even. Chiral or parity-violating matter therefore needs a supplied orientation.
  - D-T3 (BHS type): events cannot carry a frame, null direction, spinor or finite cell structure whose law is Lorentz-invariant.
- Massless leg: two constructions with an order-only (link-only) bulk give the exact Dirac retarded mean.
  - Class E: the frame sits only in the source and detector.
  - Kähler–Dirac 0-form sector: the order-only coboundary of the link field. The codifferential is not needed here, because it vanishes on a 0-form, so Φ = dφ. Its Clifford image γ^μ∂_μφ = S_R·η₀ contains the whole 4×4 retarded kernel, with taste as the source index.
  - Noise for both is ARGUED from the refereed E1′-b bound and CHECKED at accessible sizes.
- Massive leg: for both routes it reduces to lane M's massive scalar kernel, (iγ·∂+m)G_m or (d−m)φ_m. Lane M is M-INCONCLUSIVE.
- Class F: fails, but only by an ARGUED lower bound on its noise.
- Scope note: in class E and the Kähler–Dirac route, the spin-½ content is the apparatus's or Clifford bookkeeping of a scalar link field. The substrate carries no spin degrees of freedom, there is no spin–curvature coupling, and there are 4 tastes. This is a real limit. The fixed PASS and FAIL lines do not test it.
- If the referee rules that "chirality" in the reading means the substrate must tell left from right (Weyl or parity-violating matter), then a FAIL limited to chirality follows from D-T2. That is not the registered Dirac target.

**Issues:** 1. The verdict does not follow from the fixed reading.
- What was proved is narrow: no two-point order-only kernel with internal indices gives a spinor, no order-only quantity has a handedness, and events carry no frame with an invariant law. This does not exclude the PASS line, which asks only for "a construction with the correct mean and a controlled noise law meeting the E1′ bars".
- The run itself produced two massless constructions that meet the mean, both with an order-only or link-only bulk:
  - class E;
  - the Kähler–Dirac 0-form sector, where Φ = (d−δ)Gη₀ = dφ because δφ = 0. It needs no codifferential, and its mean is S_R·η₀.
- PASS is unmet only because of the massive leg, which is lane M's open problem (M-INCONCLUSIVE), and because the noise laws are ARGUED, not controlled.
- A "no-go" that leaves the PASS routes open is not a FAIL for the lane. It is the reading's "otherwise", i.e. INCONCLUSIVE.

2. The chirality leg is aimed at the wrong target.
- TESTS.md:538–546 registers the Dirac retarded propagator, which is parity-symmetric.
- D-T2 is correct, but it excludes only parity-odd structure: handedness, Weyl, parity-violating bulk couplings. The registered target needs none of these.
- The worker's H4 adds the Weyl propagator, and then says the FAIL "rests on the chirality requirement". That reads more into the reading than it says.
- The codifferential δ = ±⋆d⋆ uses two Hodge stars, so it needs the metric but no orientation. D-T2 therefore does not block the Kähler–Dirac codifferential either.

3. D-T1 is too broad as a headline.
- H2 allows only End(V)-valued functionals of the poset with two marked endpoints.
- Outputs that live on chains (cochains) escape it. My v3 check shows the order-only coboundary has a covariant 1-form mean on tilted chains, within 0.5% of the continuum.
- So "no order-only rule has a spin-1/2 propagator as its mean" holds only for two-point kernels with internal indices.
- The first premise of mapping B ("class O excluded in mean") therefore fails for chain-valued order-only rules. B survives only through the chirality leg (issue 2).

4. D-T3 is overextended in "Verdict in detail".
- The claim that the needed frame "is not suppliable by any Lorentz-invariant mark field either" is false for class F.
- Class F's link vectors Δ = x − y form a nonzero mark field on links whose joint law is Poincaré-invariant.
- D-T3's Palm argument needs one, or finitely many, marks per event. Every event has infinitely many links, so the argument does not apply.
- Class F is excluded only by the ARGUED bound Var ≥ (1 − C′s/D)·Diag. Simulations reach only D ≤ 200 and alternative profiles are untested (the worker's own item 5). It is not a "frame on every link" in the D-T3 sense.
- The Kähler–Dirac substrate needs no frame at all, and class E's frame belongs to the apparatus.
- So the second premise of mapping B is not established for F or for Kähler–Dirac.
- In consequence (a), "a gauge-redundant frame … is not a probabilistic record state" is ARGUED but sits inside an item labelled EXACT. Gauge-invariant link-vector data, such as inner products Δ_xy·Δ_xz, is invariant in law.

5. Minor points.
- The Kähler–Dirac noise penalty √2·λ̄/δ is called CHECKED, but rests on two chain lengths at D = 40 only.
- The physical-scale class F figures extrapolate an ARGUED variance bound from D ≤ 200ℓ to about 1e38ℓ. The verdict does not rest on them.
- In the 1+1 control, primeness of the sprinkled order is ARGUED.

6. Correct as stated. The proofs of D-T1 (within its scope), D-T2 and D-T3 (event marks: H³, dS₃, S², spinors, frames, finite neighbour sets, locally finite cell complexes) are sound. The Palm/Slivnyak invariance holds. All the class E and class F numerics I re-checked reproduce.

**Re-runs:** All runs are in /private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/c3/D/verify/, with OMP_NUM_THREADS=2.

(v1) v1_moments.py: profile moments by scipy quadrature.
- ∫Q = 0.0000000000, ∫sQ = −1.0000000000, ∫s²Q = −4.8989794856 (= −√24).
- ∫e^{−m} = √6 and ∫(1+4m)e^{−m} = 3√6.
- 3/(144a²) = π²/2.
- All match the report.

(v2) v2_indep_mc.py: an independent Monte Carlo, written separately from the worker's code.
- It uses an isotropic sprinkling of the full past-cone shell (τ² < 13.54), not the worker's cylinder sampler, and brute-force interval counts.
- D=10, s=4, w=2 (n=1500):
  - links 32.54 against a Campbell value of 32.64;
  - class E mean 0.1303 ± 0.0011, against the worker's quadrature value 0.1297;
  - Var/Diag: E 1.60 (worker 1.613), F 1.59 (worker 1.524 ± 0.045);
  - class F sd/|exact mean| 18.4 (worker 17.98);
  - F/E noise ratio 54.3 (worker 53.2; exact R = 54.7).
- D=40, s=8, w=4 (n=600):
  - Var/Diag: E 1.40 (worker 1.444), F 1.305 (worker 1.307);
  - class F sd/|exact mean| 103.6 (worker 103.6);
  - F/E noise ratio 458 (worker 450; R = 474.9).
- Re-running the worker's D1b quadrature reproduces R = 54.67 and 474.88, and the class means relative to the continuum (1.0165, 1.0021).

(v3) v3_kd_tilted.py: exact Campbell means of the order-only coboundary dN = N(x0) − N(x1) on tilted timelike chains, with x1 a substrate event at D=40.
- E dN against the continuum (φ(x0) − φ(x1))/a, as the ratio of the two, by displacement (dt, dx):
  - (1, 0): 1.0012
  - (1, +0.6): 1.0048
  - (1, −0.6): 1.0002
  - (2, +1.2): 1.0043
  - (2, −1.2): 0.9992
  - (3, 0): 0.9997
  - (0.5, 0): 1.0017
  - (0.05, 0): −5.8. This is the blocking regime the worker reported.
- Conclusion: the order-only, chain-valued functional has a Lorentz-covariant (1-form) mean. D-T1 does not cover it.

No repository files were edited.
