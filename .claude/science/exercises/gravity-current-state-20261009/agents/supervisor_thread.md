# Supervisor's own thread (Claude Opus 5.5)

Written before any route agent reported, so the comparison stays fair: the skill's standing rule is that the supervisor runs its own thread on farmed-out work.

## The smallest object (CHECKED, exact; `scripts/S0_ir_cone_cutoff_identity.py`)

Take one massless field in a constant, volume-preserving metric g = exp(−tε), with ε symmetric traceless and tr ε² = 1. Its vacuum energy's second derivative in t at t = 0 is:

| Cutoff | Bosonic mode | Weyl sea |
|---|---|---|
| window fixed in **label** space, \|k\| < K₀ | **+K₀⁴/(120π²)** | **−K₀⁴/(60π²)** |
| window fixed in **proper** space | **0** | **0** |

- The value is the same for axis, face and generic shears.
- The Weyl value matches the W1 referee's independent number.
- Reading: in the IR-cone approximation, the transverse-traceless (TT) modulus is exactly the cutoff geometry. Nothing else enters.

## An observation to test: bosons and fermions enter with opposite sign

- **At the free IR-cone level,** the modulus is ∝ (n_B − 2 n_Weyl)·K₀⁴/(120π²), a supertrace. A boson–fermion-balanced content cancels the leading K₀⁴ term exactly. This is the TT twin of the SUSY cancellation of the quartic vacuum-energy divergence (suggested).
- **With mass splittings** the cancellation stops at subleading orders, K₀²·STr m² and STr m⁴·log (suggested). With modulus ~ STr m⁴ and m_g² ~ modulus/M_P², a TeV splitting gives m_g ~ TeV²/M_P ~ 1e-4 eV. That is far above the LIGO bound of about 1e-23 eV.
- So balance can remove the Planck-scale part but not reach the bound. This mirrors the cosmological constant: SUSY leaves about TeV⁴ against the observed meV⁴ (suggested, order of magnitude).
- **Beyond the IR cone,** lattice band structure enters: K3a″'s free part is O(0.1) per cell with signs that depend on the coupling. Whether a lattice supertrace cancels the *whole* free-level modulus is a cheap check, not run.

## My candidate routes (for comparison with the agents)

| # | Route | Premise challenged | First test |
|---|---|---|---|
| C1 | **A liquid vacuum.** A substrate whose neighbour structure rearranges has no static shear modulus, so the low-energy cutoff follows the geometry | L1 (fixed adjacency), S4 | In a model whose bonds can rewire (or whose defects proliferate), does the field theory living on it have zero static TT modulus? Compare crystal and melt |
| C2 | **A protected emergent graviton.** An exact lattice constraint forbids the TT mass, as Gauss's law protects the photon | S2, S5 | Is a rank-2 exact constraint compatible with a linear (ω ∝ q) TT mode? The 09-29 probes say exact slides give ω ~ q², so this is likely wounded |
| C3 | **One mechanism for two problems.** The trace part of the cutoff's vacuum response is the cosmological constant; the TT part is this modulus | S6, H2 | Does any known CC-relaxation mechanism also zero a **second** derivative, not just the first? Equilibrium self-tuning (Volovik) zeroes pressure (the tadpole), not a modulus (suggested) |
| C4 | **The price lemma.** For any local field theory regulated by a fixed label-space cutoff, the static TT modulus is generically nonzero and cancels only by supertrace balance or tuning | L1 | Generalize the IR-cone identity to the lattice band structure and to O(e²); state it as a lemma |

**Lean (a reading).** C1 and C4 together are the honest core. The stiffness face says a fixed crystal substrate makes the vacuum rigid against shear. Gravitational waves are massless, so the substrate must flow (C1), unless something cancels the modulus exactly, which in the known cases is supersymmetry, and that cancellation is broken in nature. This is a layman-simple candidate price: **"space is not a fixed crystal"**. Still to be weighed against the agents' independent routes.

## Follow-up: records as spacetime events (written before E1 reports; 2026-10-09)

**Power count (suggested).**
- **Static white disorder in 3D:** the random mass² averaged over a region λ³ is about √W·λ^(−3/2). Relative to k² ~ λ⁻², that grows like λ^½. It is **relevant**, and F1a died of it.
- **Spacetime white disorder in 4D:** averaged over λ⁴, the ratio to k² is about σ, independent of λ. It is **marginal**.

**A crude gravitational-wave phase-noise estimate (suggested).**
- Along a path of length D there are about D/λ independent coherence regions, each adding a phase of about σ. So δφ ~ σ·√(D/λ).
- For LIGO waves (λ ~ 1e6 m) over D ~ 1e25 m, δφ ~ 3e9·σ, so we need σ ≲ 3e-10.
- Smearing over a 4D region of size ℓ averages (ℓ/l_P)⁴ events, so σ_eff ~ σ₀(l_P/ℓ)². That needs ℓ ≳ 6e4·l_P ≈ 1e-30 m, far below the LHC locality bar of 1e-19 m.
- **On this count E1 would PASS.**

**Caveats that could reverse it.**
- **The cone.** The Benincasa–Dowker operator sums over the past light cone, whose volume near the cone is infinite (the Lorentz group is non-compact). The known result is that its pointwise fluctuations *grow* with density unless smeared. The true scaling of σ_eff with ℓ may therefore be much worse than (l_P/ℓ)².
- **Swerves.** These bounds add an independent constraint.
- **The mediator.** Whether a graviton exists on such a substrate at all is not tested here.

**The trace twin.** Everpresent Λ: δΛ ~ 1/√V_Hubble ~ 1e-122 in Planck units, the observed order (COMPARATOR, Sorkin). The analogous TT fluctuation over the Hubble volume would be δm_g² ~ H², i.e. m_g ~ 1e-33 eV, below LIGO's 1e-23 eV (suggested).

## Follow-up: why a fixed spatial substrate cannot be both shape-blind and quiet (2026-10-09, written while E2/E3 ran)

**Timing, for honesty.** I wrote this after glimpsing one line of E2's progress ("pooled fits within 2 SE of white noise"). I had seen no E3 result. The lemma is a proof, not a forecast, so it stands or falls on its own; the referee checks it with E2/E3.

**Lemma P (proved, same-family; to be refereed).**
- **Setting:** a stationary simple point process X in R^d, d ≥ 2, with intensity ρ and finite second moments.
- **Claim:** if its law is invariant under SL(d) (all volume-preserving linear maps), then its pair correlation g₂ is constant: g₂ ≡ c ≥ 1, with c = 1 exactly when X is (mean-)ergodic. So for every window W,

  Var N(W) = ρ|W| + ρ²(c − 1)|W|² ≥ ρ|W|,

  and S(k) = 1 for every k ≠ 0. The density noise is white; no such set is hyperuniform.
- **Proof:**
  - For A ∈ SL(d), AX has the same intensity, and its reduced second factorial moment measure is the push-forward by A.
  - Invariance in law makes that measure an SL(d)-invariant Radon measure on R^d∖{0}. SL(d) acts transitively there for d ≥ 2, and an invariant measure on a homogeneous space is unique up to scale, so it is c·ρ·Lebesgue. A simple process puts no mass at 0, so g₂ ≡ c.
  - Var N(W) ≥ 0 for large W forces c ≥ 1. Mean ergodicity, i.e. N(W)/|W| → ρ in L², forces c = 1. ∎
- **The same holds for the smallest group that matters.** The upper-triangular Iwasawa subgroup AN acts simply transitively on unimodular metrics, so invariance under AN alone already makes the mean energy shape-blind to all orders. AN has two open orbits in R^d, the half-spaces x_d > 0 and x_d < 0. Parity swaps them and g₂ is even, so g₂ is still constant almost everywhere.

**Corollary for E2/E3 (suggested; the readings are the tests').** In a frozen spatial substrate, mean TT shape-blindness that comes from the symmetry of the substrate's law (R1 Lemma L, R2 Lemma A) and suppressed long-wavelength density noise exclude each other.
- **Diluted Z³, quasicrystals and stealthy hyperuniform sets** have quiet or crystalline density, but their law keeps only finite or rotational symmetry. Their mean TT stiffness is therefore not protected by symmetry: it has one number for icosahedral or decagonal order, two for cubic. It vanishes only by tuning.
- **Poisson-type sets, frozen or growing,** are protected in mean, but their density noise is white. That was F1a's failure.
- So no frozen spatial pattern escapes by being cleverer. The choice is between a symmetric law (white noise) and quiet order (an unprotected mean).

**What the lemma does not cover.**
1. **The stiffness field is a nonlinear local functional of the configuration.** White density noise generically gives white stiffness noise. A stiffness density that is exactly a divergence, a coboundary, would be quiet even on a Poisson set. That is F1a's one reopen condition, and it stays open.
   - Related: for a *pair-sum* energy, a stealthy set with a band-limited kernel is exactly shape-blind in every realization. But Z³ is the extreme stealthy set, and this is T2's free-level relabelling again: non-local, and it does not survive interactions (Lemma R).
2. **Spacetime.** The Lorentz group is not transitive on R⁴∖{0}; its orbits are hyperboloids. So Lorentz invariance in law forces only g₂(x) = G(x·x), not a constant, and E1 is not touched by this lemma. The spacetime Poisson sprinkling itself has S ≡ 1 (white in 4D). Whether that white noise is harmless (marginal) is exactly E1's quantitative question.

**Prior art inside this packet (my miss, caught by the E2/E3 worker).**
- `kill_F1a.md:24` already had the pair-theory version as a READING: R3's necessity lemma (`R3_price.md:34`, ρ₂ = a + b/r³ ⇒ b = 0) means a pair-level zero mean forces Poisson pair statistics, which rules out a hyperuniform density.
- Lemma P reaches the same exclusion from the law's symmetry (SL(d), or AN alone) rather than from a pair-potential functional. That makes it independent of the energy functional, and it gives the variance identity.
- I did not grep the packet before writing it.

**Lemma P after the referee (codex sol, CONFIRMED WITH CORRECTIONS; `agents/E23_referee.md` §6).**
- "c = 1 iff ergodic" becomes **c = 1 iff density averages converge in L²**. Translation ergodicity is sufficient, not necessary; a Haar-random unimodular lattice has c = 1.
- For c > 1 the spectrum is white at k ≠ 0 plus an atom at k = 0, not simply "white".
- **The AN step needed more:** a contraction diag(t, …, t, t^{−(d−1)}) removes singular mass on x_d = 0, and pair exchange, not parity, equates the two half-spaces. "Smallest group" is withdrawn.
- **Withdrawn as too strong:** the corollary's "white density ⇒ white stiffness", and "not protected ⇒ stiffness nonzero". What survives is that SL/AN law protection and ensemble-hyperuniform density exclude each other.
- **Spacetime:** Lorentz orbits include null cones with possible singular measures, so g₂ = G(x²) needs an absolutely continuous density.

## E1 outcome against my pre-registered expectation (2026-10-09, after the referee)

- **My headline ("on this count E1 would PASS") was a coarse-grained phase-noise count.** That row does pass in E1.
- **My first caveat was the one that mattered.** It said the BD sum runs over the whole past light cone, whose volume is infinite, so per-realization fluctuations could scale much worse. They do: the row noise gain diverges with the size of the past (EXACT), and the naive evolution is exponentially unstable at the tested ε. Only the extrapolation to physical ε keeps this from a FAIL.
- **S1** had the coefficient right for a slab past. The referee's "missing Jacobian" was a region convention, slab against diamond (S1b, CHECKED).
- **Reading (not tested).** Waves need signed weights in any step-by-step rule (block 122, on main as `docs/ADMISSIBILITY_RULE_WAVES_NEED_SIGNED_WEIGHTS_..._2026-09-24.md`; PR #9176 closed after owner integration). On a Poisson substrate, signed weights turn the substrate's noise into a gain that grows with the size of the past. A rule that moves influence only along links, with positive weights (Johnston's massless path sum), avoids the cancellations, but it is a propagator from sources, not an initial-value evolution. Whether the instability is BD-specific is therefore the natural next question. Prior art on path sums: the event era's complex-phase path sums on DAGs, dropped for rank-1 collapse.

## Follow-up 2: my own backward derivation (written 2026-10-09 after launching E1′, B1 and B2, before any of them reported)

**Labels:** comparator (literature), proved or checked (this packet), suggested (argument), reading. Each step names the theorem's hypotheses.

**Step 1. Universality comes free (comparator: Weinberg 1964 soft theorem).**
- **Statement:** in a Lorentz-invariant S-matrix with a massless spin-2 particle, the particle's soft couplings must all be equal, which is the equivalence principle.
- **Hypotheses:** exact low-energy Lorentz invariance, a massless spin-2 pole, a local S-matrix.
- **Consequence:** the substrate does not need a separate mechanism for universal coupling. It needs (i) a massless helicity-2 mode and (ii) Lorentz invariance in the infrared, accurate to the LV bounds.
- **Completion (comparator: Deser/Feynman self-coupling).** Once those two hold, the low-energy theory is GR.

**Step 2. The graviton cannot be an ordinary composite (comparator: Weinberg–Witten).**
- **Statement:** a Lorentz-covariant theory with a conserved, Lorentz-covariant stress tensor has no massless helicity-2 particle that carries energy.
- **Escapes, each a hypothesis failing:**
  - (a) a gauge redundancy, so the graviton's stress is not gauge-covariant: diffeomorphisms;
  - (b) the substrate theory does not live in the same spacetime: holographic emergence;
  - (c) no UV Lorentz invariance, which Step 3 makes costly.
- **Consequence (suggested):** the graviton is either the substrate's own geometry, carried by a redundancy, or holographic.

**Step 3. One light cone without tuning (comparator: Collins et al.; checked here: T1).**
- A UV preferred frame feeds infrared speed splits at O(g²/16π²) unless a symmetry protects them.
- T1 found two sufficient protections: exact Lorentz invariance in law, or a hypercubic symmetry that treats time like space (Z⁴).
- **Consequence:** time and space must be treated alike. An absolute "now" carried by the substrate is ruled out unless tuned.

**Step 4. No labels that resist shear (comparator: Rubakov–Tinyakov, Dubovsky; proved here: Lemma R; checked here: K3a″, W1).**
- A medium whose points carry physical labels gives the graviton a mass equal to its shear stiffness. Three things protect against this:
  - (i) a gauge redundancy (the labels are unphysical);
  - (ii) no spatial labels at all;
  - (iii) a fluid's relabelling symmetry.
- **Excluded:**
  - (iii) by F1b's kill (refereed): flat space forces ρ + p = 0, which removes the phonon kinetic term, and the fluid's frame splits speeds;
  - a fixed Z³ or Z⁴ has physical labels and only discrete translations, so Lemma R applies;
  - K7a's gauge-invariant linear graviton on Z⁴ needs an exactly conserved interacting stress, which a fixed lattice does not supply (K3a, bounded).
- **Consequence (suggested):** the points of the substrate must be gauge, i.e. physics depends only on relations. Alternatively there are no spatial points at all.

**Step 5. One frozen random pattern is too noisy (proved here: Lemma P, corrected; checked here: E2, E3, F1a).**
- If shape-blindness comes from the symmetry of the substrate's law, a frozen spatial realization has white noise. Quiet orders are not protected.
- **Consequence:** the substrate is not one frozen spatial configuration. It is a spacetime structure (E1: marginal by power count, but BD dynamics amplifies the noise), or a quantum sum over configurations (not tested anywhere here), or both.

**Step 6. Lorentz-invariant discreteness has unbounded valency (comparator: Bombelli–Henson–Sorkin).**
- No Lorentz-invariant rule picks finitely many neighbours from a sprinkling.
- **Consequence:** under the exact-Lorentz option of Step 3, "nearest-neighbour adjacency" with finite valency must go. Under the Z⁴ option, labels come back and Step 4 bites.
- **The fork:** keep finite neighbourhoods and pay a redundancy that a fixed grid lacks, or keep Lorentz invariance and accept unbounded valency.

**Step 7. Stability and locality (checked here: E1, E2, E3; E1′ running).**
- Rules that move influence step by step need signed weights to carry waves (block 122, on main).
- On a random substrate, signed weights amplify the substrate's noise (E1, inconclusive at physical scales).
- Massless influence passed along links has no signed recursion (E1′ tests this).

**Step 8. Λ (comparator: Sorkin's everpresent Λ).** A spacetime substrate with N elements predicts δΛ ~ N^(−1/2), about the observed magnitude. This is a positive for spacetime randomness. It reads naturally with "the record count rises".

**Intersection (suggested).** The substrate must be:
- a **dynamical, relational structure**, in which only the pattern of which elements neighbour which is physical, and labels or positions are gauge;
- one that treats **time and space alike** (Lorentz in law or hypercubic);
- one whose **graviton is the pattern's own ripple**, protected by an exact constraint (the redundancy);
- one whose **realization noise is removed by the dynamics** (a quantum sum over patterns, or a stable propagation rule), not by freezing.

GR satisfies this in the continuum. Causal sets, CDT, spin foams and group field theory are partial discrete examples; each lacks something (a dynamics with a continuum limit, exact Lorentz, or an exact redundancy). Holography is the other escape.

**Reading of the owner's thought** ("the sites are just the substrate; the neighbourhood can move across it, including the qubits"):
- If physics depends only on the moving neighbourhood pattern and never on which underlying site it sits on, then the underlying sites are a gauge redundancy, which is exactly escape (i) of Step 4. A sheared pattern is just another pattern with the same intrinsic relations, so the shear stiffness tied to fixed labels is gone.
- The questions this leaves:
  - Step 6: the moving neighbourhood cannot be a fixed finite set if Lorentz invariance is exact;
  - Step 5: the pattern must be quantum-summed, not frozen, to kill the noise;
  - the graviton should be the ripple of the neighbourhood pattern itself, with a constraint that keeps it massless.

**Cheapest discriminating tests (suggested).**
1. In a small relational model where only the pattern is physical (a 2D causal set or CDT with a BD-type action), does the quantum sum over patterns suppress the per-realization noise that a single frozen pattern has?
2. Can a record-formation rule produce Lorentz-invariant-in-law event sets, or must the order be supplied (A36)?
3. Does the pattern's linearized dynamics have a massless TT mode protected by an exact constraint?

## Campaign C3: supervisor's expectations (written 2026-10-10 ~01:00Z, after launch, before any result)

**G-A (the order as the graviton).**
- **Mean:** expected exactly mass-free and exactly gauge-blind in law, because the Poisson law is invariant under volume-preserving maps and order functionals transform covariantly. For the BD action I expect linearized Einstein–Hilbert at O(k²) (comparator: BD 2010).
- **Per realization:** I expect the crackle to dominate. Pairs crossing nullness flip with probability ∝ ε, so the variance is ∝ ε·N_near-null, against a mean signal ∝ ε²k²N. The noise wins below ε ~ (k²N)^(−1/3)-type thresholds, which are hopeless at h ~ 1e-21 for a single realization.
- **Expected verdict:** FAIL, or INCONCLUSIVE if the crackle averages over the detector volume in a controlled way. The physically relevant question becomes whether gravity is a coarse-grained order statistic. That is G-C.

**G-B (a tensor on links).**
- I expect PASS. The non-TT admixture is set by counting noise: relative ~ √(F/N̄), ~1e-29.
- The mean is exactly the linearized-GR retarded field, since G₀'s mean commutes with derivatives.
- Scope: this is not protection.

**G-C (protection).**
- I expect INCONCLUSIVE.
- "Diffeomorphisms act trivially on the abstract order" is true but empty: it does not define a per-realization graviton.
- A quantum sum over orders is the only candidate mechanism, and its continuum limit is unsolved.

**M-A (Johnston, packet plus detector).**
- I expect M-INCONCLUSIVE, leaning FAIL for heavy particles.
- Regeneration along the trip probably adds variance roughly linearly in proper time, at a rate set by the m²ℓ gain, giving decoherence lengths ~ (m²ℓ)⁻¹ in proper time.
- That is ~10 km of proper time for a proton (boosted lab distances are longer), and ~3e10 m for an electron.
- That would put M-PASS at 1 km within reach, if a controlled bound exists.

**M-B (unitary matter on links).** I expect a FAIL-type no-go for a strictly Lorentz-invariant, frame-free unitary rule, because unbounded valency and varying antichain sizes leave no fixed Hilbert space. The escape is SJ-type constructions, which are not step-by-step.

**M-C (mass without signed weights).** The proper-time (Schwinger) representation G_m = ∫dτ e^{−m²τ}·(heat kernel) is positive only in Euclidean signature. In Lorentzian signature the phases e^{−im²s} return. So I expect no positive-weight route for real-time massive propagation. A composite or bound-state route might work but would need an interaction.

**K (keep the grid).** I expect FAIL: some non-gauge-invariant form ≥ 1e-4. K3a showed no conserved interacting stress in the tested class, so W(B4) alone cannot force the five forms to zero.

**X1.** I expect FAIL: white in the direct spectra as well. **X2.** I expect FAIL: n ≤ 1.
