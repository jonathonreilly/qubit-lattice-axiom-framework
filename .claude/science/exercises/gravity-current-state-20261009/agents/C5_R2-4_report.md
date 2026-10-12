# C5 R2-4: set B's weight. Is Admissibility's probability clause satisfiable on Z⁴ with chiral fermions and gravity?

**Worker.** Claude Opus 5.5 (same family as O1–O5 and the supervisor). **Unrefereed.** Run 2026-10-12, 11:53Z to about 12:30Z. No repository file was edited.
**Scratch.** `scratchpad/C5/R2-4/`: ten scripts and their `.out` files (listed in §8).
**Read in full.** `docs/MINIMAL_AXIOMS_2026-06-29.md`; `TESTS.md` "Campaign C5", round-1 results and round 2 (lines 2302–2643); `agents/C5_O5_synthesis.md`; `SUMMARY.md` §§15–21; `PRICE_NOTE.md` v5 and the v6 delta; `C4_K2_referee.md`, `C4_K2_referee_full.md`; `C3_D_referee.md`; `C5_O1_referee.md`. Also read: the relevant parts of `C5_O1_report.md` (Lemmas B–E), `C4_K2_report.md` (§4, transfer matrix), the candidate pack's `TEST_LOG.md` (K7a, K2a, G0), and the repo prior-art notes listed in §1.

---

## 0. In plain words

**The question.** In set B, the axiom's "probability distribution at each site, fixed by the neighbours" becomes the conditional of a Euclidean 4D grid weight. Is that weight a real probability once the content includes (i) Standard-Model-like chiral fermions and (ii) gravity? If not, what is the smallest change to the axiom text?

**What I found.**
1. **Gravity: no.** This is the decisive result, and it does not depend on the grid.
   - Take any probability weight in which stress sources couple locally to a real quantity. The long-range response to those sources is a variance, so it can never be negative.
   - Einstein gravity's response is negative along one direction, the "conformal" source. That is the Euclidean conformal-factor problem.
   - The sign is fixed by an observation. The relative weight of the trace coupling is set by light bending (γ = 1, Cassini). Every positive weight gives γ ≤ ½.
   - So a positive probability weight with local couplings cannot carry the observed graviton. Einstein gravity is still reflection positive (I checked), so the price is "probability distribution" → "reflection-positive weight". RP itself is not what fails.
   - The only way to keep a true probability is to make the constraint (Newtonian/conformal) part of gravity an instantaneous action-at-a-distance term. That is power-law non-local, and it is the canonical-reduction picture.
2. **Chiral fermions: not shown for chirality itself. Shown for CP violation.**
   - A positive weight forces an exact, site-local time-reversal-type symmetry on the reconstructed theory (Lemma K, proved).
   - The observed CP violation in the weak sector (the CKM phase) then has to be spontaneous, i.e. in the state, not the law. Otherwise the weight must be complex.
   - Chirality with CP conserved is not excluded by anything I could prove. The complex phase of the chiral determinant is a fact about one choice of variables.
3. **Nearest-neighbour versus quasi-local.**
   - Exact lattice chiral symmetry of Ginsparg–Wilson type cannot be nearest-neighbour or hypercube-range. Exact algebra, d = 2, 3, 4, for every polynomial R in that class.
   - The overlap operator is exponentially local only.
   - But mirror-gapping (symmetric-mass-generation) constructions are nearest-neighbour compatible and open. So "nearest-neighbour → quasi-local" is **not** forced by chirality as such.
   - Separately: read literally (positive, neighbour-determined site conditionals on Z⁴), Admissibility allows only pair interactions (Hammersley–Clifford). Plaquette gauge actions and Grassmann fermions are already outside the literal text, chiral or not.

**Against the fixed readings.**
- (ii): **DERIVED**, under stated hypotheses (W1–W3), in a stronger form than registered: no positive nearest-neighbour **or quasi-local** weight, on any lattice. The only positivity-keeping escape is power-law non-locality (canonical reduction), which is SUGGESTED and not built here.
- (i): **DERIVED** only in its CP-violating form, with spontaneous CP violation as the named escape (hypotheses K1–K4). For chirality per se: **SUGGESTED**.
- Not REFUTED.
- **Price:** "probability distribution" → "weight" (reflection-positive, complex allowed).
  - The alternative for gravity is Π-NL: keep the probability and accept power-law non-locality in the constraint sector.
  - "Nearest-neighbour" → "quasi-local" is suggested, not derived.
- Neither change brings back a preferred tensor (Lemma C) or a law-level arrow (Lemma E).

---

## 1. Hypotheses, scope, prior art (counted once)

**The setting (from `TESTS.md:2563-2581`).**
- Z⁴ at ξ = 1, with a W(B4)-covariant law; first nearest-neighbour, then quasi-local.
- "Positive, normalizable, reflection-positive Gibbs weight" means a nonnegative measure μ on a configuration space Ω = ∏ₓ Ωₓ, finite total mass in finite volume, and OS reflection positivity for Θ(F) = conj(F∘θ), with θ a configuration map covering a lattice hyperplane reflection.
- Fermions enter either as Grassmann fields (then "positive" can refer only to the bosonic marginal) or as emergent from bosonic site variables.

**Excluded outside realizations** (the scope does not cover these):
- real-time stochastic substrates, which have no Euclidean measure (routes E and A);
- non-Gibbsian "weights" defined only through a Hilbert space (that is already the price);
- gravity whose coupling field is not a real observable of the measure: complexified or rotated conformal variables, which is the named escape, or purely relational or holographic readouts;
- spontaneously broken phases, which are named as escapes where they matter.

**Prior art, each counted once.**
- **K7a** (`TEST_LOG.md:31-33`):
  - unreduced Euclidean gravity form indefinite (255 negative eigenvalues at L = 4);
  - 4D staggered fermions have 4 tastes;
  - the referee's open point "a positive physical transfer matrix after constraints, gauge reduction or a contour prescription is open" (`TEST_LOG.md:52`).
- **K2** (`C4_K2_referee_full.md:32-36`):
  - TT transfer positive, (s₄² + q̂²)/4 per polarization;
  - the unreduced DeWitt form is indefinite;
  - joint graviton–matter RP is uncomputed.
  - Also `C4_K2_report.md:186-202`: Gibbons–Hawking–Perry as comparator; staggered two-step positivity.
- **K2a** (`TEST_LOG.md:74,92`): no Weyl selector in the hypercubic form; the "left–right or one speed" tension.
- **Repo RP notes.** `docs/AXIOM_FIRST_RP_TWO_STEP_TRANSFER_MATRIX_POSITIVITY_NOTE_2026-05-28.md:25-33`: single-step staggered transfer not positive; two-step positive (free). `docs/AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM_NOTE_2026-04-29.md` (staggered-only narrowing).
- `docs/NAIVE_LATTICE_FERMION_TWO_POWER_D_SPECIES_COUNT_NARROW_THEOREM_NOTE_2026-05-10.md:1-7` (16 species at d = 4).
- `docs/P2_EUCLIDEAN_VS_LORENTZIAN_FORK_2026-06-05.md:41` ("OS reconstruction authority" listed as an implicit assumption).
- `kinetic_isotropy_primitive` (OS0 kinetic normalization on Z³ × Z_τ; `PRIMITIVE_REGISTRY_CHECK.md:63-71`).
- C3 D: chiral event matter needs an orientation or selector plus spin transport (`C3_D_referee.md:48-50`).
- O1 referee: "a coupled reflection-positive chiral matter-plus-gravity construction has not been exhibited" (`C5_O1_referee.md:44`).
- **No repo hits** for convexity of log Z, the γ_PPN link to the conformal mode, Horváth's ultralocality theorem, or Lüscher's chiral construction. Hits for "Ginsparg", "overlap" and "Nielsen–Ninomiya" are ABJ/taste notes, with no GW-locality result.

**Labels.**
- **PROVED:** proof given here, under the stated hypotheses.
- **CHECKED:** numerical or exact-algebra run in scratch.
- **COMPARATOR:** a published result, recalled from memory and not re-derived. Citations are unverified unless marked.
- **SUGGESTED:** argued, not proved.
- **READING:** an interpretation.

---

## 2. Probe (b) first: gravity (the decisive part)

### G1. The Euclidean linearized EH weight on real h is not normalizable, for any Faddeev–Popov gauge fixing (CHECKED; K7a/K2 prior art)

**Setup.** K7a's lattice symbol is O(4)-covariant in s_μ = 2 sin(k_μ/2) (K7a referee, via `TEST_LOG.md`). Its quadratic form is
  K(h,h) = ½s²h·h − (s·h)² + (ss:h) tr h − ½s²(tr h)².

**Results** (`r24_graviton_quotient.out`):
- Exact gauge invariance: max |KG| = 1.3e-14.
- Spectrum s²{−1, 0×4, ½×5}, reproducing the K7a referee.
- On the gauge quotient: (5+, 1−) at 400/400 random momenta.
- The negative direction is exactly the transverse-trace (conformal) mode: overlap 1.000000.
- For any lattice symbol whose small-momentum limit is EH, the quotient form divided by s² tends to EH's (½×5, −1). By continuity the negative direction persists at small s (PROVED). The |s|-scaling lines in the output only confirm homogeneity for this symbol.

**Why no gauge fixing helps** (PROVED, elementary). Faddeev–Popov factorization gives
  ∫dh e^{−K−|F h|²} = const · ∫_quotient e^{−K}.
The right side diverges, so K + FᵀF is indefinite for every linear F with F|_gauge invertible.
- CHECKED: 2400 of 2400 gauge fixings (random F plus de Donder) are indefinite.

**G2. A natural escape fails** (CHECKED, `r24_unimodular.out`). Impose the local hard constraint tr h = 0 (linearized unimodular gravity), with gauge reduced to transverse diffeos. The quotient is then (5+, 1−), with the negative eigenvalue at −¼s² at all 300 momenta. A longitudinal scalar takes the conformal mode's place.

### G4. Lemma W: convexity. No positive local weight carries GR's source response (PROVED; numbers CHECKED)

**Hypotheses.**
- **(W1)** A positive measure e^{−S(φ,J)} on any configuration space. The variables and the lattice are arbitrary, and normalizability is not needed beyond existence of second moments.
- **(W2) Locality of the source coupling.** Real symmetric test stress sources J_μν enter S as a real, **local** functional (finite or exponentially decaying range), for example S − ∫J·h with h a real local or quasi-local observable. Inserted sources gravitate like matter (equivalence principle).
- **(W3)** The long-range response W(J,J) = 1/p² part of ∂²_J log Z on conserved real J (p·J = 0) has the observed isotropic form (J·J − a (tr J)²)/p², with a = γ/(1+γ).
  - This is gauge invariant: gauge modes pair to zero with conserved J.
  - Newtonian sources give (1 − a)ρρ′. Light (traceless T) gives ρE. Bending/Newton = 1/(1 − a) = 1 + γ.
  - The Euclidean continuation keeps a: T_E^{44} = −T^{00} and tr_E = η_μν T^{μν}.

**Proof.**
- ∂²_J log Z = Var_J(∂_J S) − ⟨∂²_J S⟩_J.
- The variance is ≥ 0, because the tilted measure is positive.
- The seagull term is local (W2), so its symbol is bounded as p → 0 and contributes nothing to the 1/p² part.
- So the 1/p² part is PSD on conserved real J. By Bochner, the covariance of a stationary real field is a PSD matrix measure in p, so the coefficient of 1/p² is PSD for each direction p̂. For linear coupling the response is exactly Cov(h, h).
- At each p, J = θ = 1 − pp/p² is conserved, and θ·θ − a(tr θ)² = 3 − 9a.
- Hence a ≤ ⅓, i.e. γ ≤ ½. ∎

**Observation.** γ − 1 = (2.1 ± 2.3)e-5 (Cassini; COMPARATOR, Bertotti–Iess–Tortora 2003, recalled). That gives a = 0.500005 ± 0.000006, against the bound a ≤ ⅓.

**What each corner costs.** Dropping one hypothesis at a time:
- **Drop W1 (positivity), keep locality and GR.** Use a complex or rotated conformal variable (COMPARATOR: Gibbons–Hawking–Perry). This is price Π-W.
- **Drop W2 (locality), keep positivity and GR.** Solve the constraints canonically:
  - the TT modes stay real fluctuating fields, with a positive transfer (K2);
  - the spin-0 and constraint sector becomes a deterministic **non-local** (instantaneous 1/∇²) real term in the weight, which is bounded below by the positive-energy theorem (COMPARATOR: Schoen–Yau/Witten);
  - the description singles out a time slicing (temporal or Coulomb-type gauge).
  - This is price Π-NL (§5). SUGGESTED: not constructed on Z⁴ here.
- **Drop W3 (GR), keep positivity and locality.** Every positive long-range covariance (P2 + cP0s)/p² with c ≥ 0 gives a = (1 − c)/3 ≤ ⅓, so γ ≤ ½. GR has c = −½. Excluded by Cassini.

**CHECKED** (`r24_source_convexity.out`, two momenta).
- **GR (B):** a = 0.500000, γ = 1.000000, W(θ)·p²/norm = −1.500000, i.e. negative. GR's Euclidean graviton response is not a variance.
- **The positive 4D-TT Gaussian (A, c = 0):** a = ⅓, γ = ½. This is the vDVZ structure (COMPARATOR: van Dam–Veltman, Zakharov 1970).
- **Locality note.** A is positive **and** local: the local EH form restricted by the local hard linear constraints p·h = 0 and tr h = 0.
  - At two derivatives the only local gauge-invariant form is EH, with its spin-0 coefficient fixed at the negative GR value (K1: 1 of 9 forms survives).
  - So a positive local graviton needs constraints like A's, and then it predicts γ = ½.

### G3. GR is reflection positive. Model A is too, but it is not GR (CHECKED)

`r24_conformal_rp.out` uses exact residues and the OS matrix M[(a,t),(b,t′)] = r_a C_ab(t+t′) over 21 linearized-Riemann components × 12 times = 252.
- **GR:** min eigenvalue −3.4e-16 against max 1.15, so PSD. GR is OS-positive on gauge-invariant observables.
- **Model A:** also PSD at q = e₁.
- **Generic spatial momentum (3/5, −2/5, 1/3)** (`r24_conformal_rp_generic.out`): both are PSD again (min −2.2e-16 and −1.7e-16, against max 0.657).
- **The two OS matrices really differ** (`r24_conformal_rp_diff.out`): ‖M_A − M_B‖/‖M_B‖ = 0.28 at q = e₁. So both theories are RP, and they are different theories.

But A is a different theory (`r24_conformal_rp2.out`):
- its Ricci–Ricci correlators are non-contact in 55 of 55 entries, against 0 of 55 for GR;
- 171 of 231 Riemann pairs differ from GR by non-contact terms;
- and γ = ½, which is excluded.

**READING.** The Euclidean conformal-mode sign is not a gauge artefact that a clever **local** positive variable choice could remove. It is the Euclidean image of the observed light-bending-to-Newton ratio. GR satisfies RP but is not a positive measure. That is exactly the gap between Admissibility's "probability distribution" and set B's B3 ("conditional of an RP Gibbs specification", `C5_O5_synthesis.md:356`).

### Known lattice-gravity phases (COMPARATOR, recalled; not re-derived)

- **Regge calculus.** The Euclidean EH action is unbounded below. The conformal problem reappears and is handled by measure and R² terms (Hamber–Williams).
- **Euclidean DT.** Weights are positive with a bounded action at fixed N, but the phases are crumpled and branched-polymer, with no extended 4D phase. DT also changes the Lattice axiom, since it is not Z⁴.
- **CDT.** Wick rotation uses the proper-time foliation and gives a de Sitter phase. The foliation is a preferred u⊗u, so CDT sits in class I (`TESTS.md:2576`; O1 counts, `C5_O1_referee.md:7`).
- **Continuum.** Gibbons–Hawking–Perry rotate the conformal contour. Mazur–Mottola and Schleich show the physical (reduced) measure is positive. This is consistent with K2's positive TT transfer and with G3.

All of these either complexify the conformal variable, reduce to constrained or non-local variables, or add a foliation. In this packet's terms, each pays "weight", "non-local or gauge-fixed description", or "preferred tensor".

---

## 3. Probe (a): chiral fermions

### A1. Nielsen–Ninomiya in the free class (COMPARATOR, with a proof sketch; CHECKED count)

**Hypotheses.** Quadratic Grassmann action on Z⁴; translation-covariant; Weyl block W(p) continuous on T⁴; exact on-site chiral symmetry.
- These cover nearest-neighbour **and** every exponentially local symbol. W(B4) is not needed.

**Statement.** The local indices of the zeros of det W (the windings in π₃(GL_n(C))) sum to zero, so the spectrum is vector-like.

**Sketch.** Excise small balls around the zeros. W is invertible on the compact remainder, and Stokes applied to the closed winding 3-form makes the boundary windings sum to 0.

**CHECKED** (`r24_overlap_and_doublers.out`). The naive nearest-neighbour W(B4) symbol has 16 zeros with signed index sum 0 (8 + 8). Staggered: 4 tastes, vector-like (K7a prior art).

**What this does and does not decide.** The obstruction in this class comes from exact on-site chirality plus continuity. It does not come from nearest-neighbour range. Nearest-neighbour versus quasi-local does not decide (i) here.

### A2. No ultralocal Ginsparg–Wilson operator in the hypercube-range W(B_d) class (CHECKED, exact)

**Class.**
- D = a(p) + iγ·b(p), with a multilinear and symmetric in c_μ = cos p_μ.
- b_μ = sin p_μ times a multilinear symmetric polynomial in the other c_ν. That covers every coupling inside the unit hypercube, nearest-neighbour included.
- GW with R = r(p)·1 is the identity a = r(a² + |b|²).
- Physical conditions: a(0) = 0; b ≈ p; D invertible at every doubler corner (Rabinowitsch variable).

**Results.**
- Canonical r = ½ (`r24_gw_ultralocal.out`): 0 solutions for d = 2, 3, 4. The d = 1 control finds 1D Wilson with r = 1.
- General multilinear r(p) (`r24_gw_generalR.out`): the Gröbner basis is {1} for d = 2, 3, 4, i.e. there is no solution even over C. The d = 1 control has solutions.

**COMPARATOR.** Horváth (1998) proved the canonical-R ultralocal no-go in d ≥ 2. Extensions to general ultralocal R are recalled with unverified attribution. This check reproduces the result in a bounded class. It does not prove the full theorem: tensor Clifford terms σ_μν t_μν are excluded by the class, as they are by C.

### A3. The overlap operator is exponentially local, not ultralocal (CHECKED; COMPARATOR Hernández–Jansen–Lüscher)

**Free overlap at M₀ = 1 on 32⁴** (`r24_overlap_and_doublers.out`):
- canonical GW holds to 6.7e-16;
- there is a single zero, and every doubler sits at a = 2;
- the kernel is nonzero on 992,831 of 1,048,576 sites;
- the axis decay rate is ≈ 0.9–1.1 per spacing.

With gauge fields, exponential locality is proved only for fields obeying the plaquette ("admissibility") bound ‖1 − U_p‖ < ε (COMPARATOR).

**RP of overlap or domain-wall fermions in physical time: not established, as far as I know** (SUGGESTED). Lüscher's chiral gauge construction gives an exactly gauge-invariant measure whose phase is fixed by integrability. It is proved for U(1); for non-abelian groups it holds to all orders in perturbation theory (COMPARATOR). The weight is complex.

### A4. When the phase can be made positive

**Pseudo-real, paired content: yes** (PROVED, elementary; COMPARATOR for RP).
- SU(2)_L alone, with the SM's 12 left-handed doublets, is vector-like in disguise, since 2 ≅ 2̄ via ε. It is 6 Dirac doublets.
- Wilson fermions (r = 1) with the Wilson gauge action are nearest-neighbour, W(B4)-covariant and RP (Osterwalder–Seiler).
- γ₅-hermiticity makes det D real, and the even power makes det⁶ ≥ 0.
- The cost is one additive Wilson-mass tuning.
- But the positivity is that of the gauge marginal, and that marginal is a non-local functional of U.

**Complex representations (SU(2)×U(1)_Y): the gauge-marginal phase is P-odd and physical** (COMPARATOR: η-invariant / Dai–Freed / Witten; one-loop P-odd neutral triple-gauge couplings f₅). It cannot be removed **in those variables**. I found no variable-independent obstruction for CP-conserving chirality (see A5).

**Explicit CP violation: an obstruction in every variable choice** (Lemma K below).

### A5. Lemma K: a positive weight forces a site-local time-reversal symmetry (PROVED)

**Hypotheses.**
- **(K1)** μ is a real (in particular positive) measure on Ω = ∏ₓΩₓ.
- **(K1′)** RP holds with Θ(F) = conj(F∘θ), where θ is a configuration map, and μ is Θ-invariant.

**Claim.** F ↦ conj F descends to an antiunitary involution K on the OS Hilbert space. K commutes with the transfer semigroup and with every configuration-map symmetry (translations, rotations). So K P K⁻¹ = −P and K J K⁻¹ = −J. K preserves the support of local observables.

**Proof.** μ is real, so ⟨Θ conj F, conj G⟩ = conj⟨ΘF, G⟩. Hence K preserves the null space and is anti-isometric. Configuration maps commute with complex conjugation. ∎

**Corollary K′** (PROVED). For real μ, Θ-invariance makes θ itself a symmetry of μ. Combined with B4⁺ (which contains R₄₁(π)), the spatial reflection θ₁ is also a symmetry. So the law carries a unitary parity-type symmetry P′ = (spatial reflection) ∘ (an internal map).

**Corollary K″** (DERIVED under hypotheses).
- **(K2)** Exact lattice symmetries survive into the continuum limit.
- **(K3)** K is not spontaneously broken.
- **(K4)** The IR is the SM with Jarlskog invariant J ≠ 0. Internal unitaries range over the SM's flavour, gauge and C transformations.

**Argument.**
- Set U := (CPT)⁻¹K. It is unitary, reverses P, commutes with J and H, i.e. it is a parity-type symmetry P·V with V internal.
- With C internal, that would be a CP·V′ symmetry.
- J ≠ 0 excludes every CP·V′ for V′ a flavour basis change (COMPARATOR: Jarlskog).

Then no real, and in particular no positive, RP weight carries the observed weak sector.
- **Escape (K3 dropped):** spontaneous CP violation (COMPARATOR: Nelson–Barr), with domain walls to be inflated away.
- **READING:** a positive law also forces θ_QCD ∈ {0, π} at law level.

**Scope.** Lemma K does **not** exclude P-violating, CP-conserving chiral content. P′ can be CP, and emergent fermions can carry T² = −1 by symmetry fractionalization even though K² = +1 (SUGGESTED). It does not apply to Grassmann weights, which are not measures.

### A6. Hammersley–Clifford: what "nearest-neighbour" allows (PROVED from COMPARATOR HC)

**Claim.** Read literally, Admissibility on Z⁴ (strictly positive, site conditionals depending only on nearest neighbours) is a Gibbs field with **single-site and pair potentials only**. The Z⁴ graph is bipartite, so its cliques are vertices and edges.

**Consequences.**
- Grassmann fermions (not a measure), Wilson plaquette actions (4-link cliques) and the fermion-determinant marginal (non-local) are all outside the literal text **before** chirality enters.
- Gauge structure must be emergent from pair-interacting M₂(C)-valued site variables, or "nearest-neighbour" must at least mean "finite-range cliques".
- **Positive nearest-neighbour bosonic models can carry emergent fermions:** the 2D Ising model is a Majorana fermion (COMPARATOR).
- No 4D positive pair model with emergent chiral (or even Dirac) fermions is known to me. This is open, not excluded.

### A7. Interacting escape (open; COMPARATOR, recalled, unverified)

**Mirror fermions with symmetric mass generation.**
- Proposals: Eichten–Preskill; Wang–Wen; Catterall 2020 (reduced staggered fermions); Butt–Catterall–Hasenfratz 2021 (a 4D symmetric massive phase).
- These are nearest-neighbour compatible on Z⁴ and evade Nielsen–Ninomiya, which is a free-field theorem.
- None is proved to give a chiral gauge theory. Golterman–Shamir raise objections.

**Repo prior art.** K2a's Spin(10) quartic on P̄_R works only in the continuous-time form (`TEST_LOG.md:74`).

---

## 4. Probe (c): RP for (a) and (b) together

**What is known.**
- Wilson fermions with the Wilson gauge action: RP (COMPARATOR).
- Staggered fermions: two-step RP only (repo, free).
- Overlap or domain-wall fermions: RP not established (§A3).
- Gravity: RP on gauge-invariant Riemann correlators, CHECKED for the free graviton (G3, B). Not as a positive measure (G4).
- Joint coupled graviton–matter RP: still uncomputed. Nothing here changes K2's statement (`C4_K2_referee_full.md:36`; `PRICE_NOTE.md:366`).

**Added by this probe.**
1. A positive joint weight would carry Lemma K's T-type symmetry, so it cannot carry explicit CP violation.
2. By Lemma W, no positive joint weight with local or quasi-local couplings can carry the observed graviton. Π-NL is the non-local exception, and it is SUGGESTED only.

So the only open joint question is RP of a **complex or rotated** weight. That is SUGGESTED to be feasible (the θ-term precedent: complex weight, RP with Θ = θ∘conj; COMPARATOR). It is not shown.

---

## 5. Probe (d): wording and price, against `MINIMAL_AXIOMS_2026-06-29.md:57-73`

**Text (`:57-61`):** "There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations. For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions."

Set B already pays B2 and B3 (`C5_O5_synthesis.md:355-356`). R2-4's extra prices, named only and not adopted:

| # | Price | Text touched | Status | Forced by |
|---|---|---|---|---|
| Π-W | "probability distribution" → "**weight** (real or complex), reflection-positive under Θ = θ∘conj; probabilities are the Born weights of the OS-reconstructed state" | `:60-61`; reading note (3) at `:70-73` ("a probability measure on the local possibility domain") | **DERIVED as necessary** for the observed graviton with a local or quasi-local law (Lemma W + Cassini, under W1–W3). The alternative is Π-NL. Also needed for explicit CP violation (K″, under K1–K4) | G4; A5 (unless CP is spontaneous) |
| Π-NL (alternative to Π-W for (ii)) | Keep a positive probability weight; the graviton's constraint (spin-0) sector becomes a deterministic **power-law non-local** term (instantaneous 1/∇²), with the TT modes as local fluctuating fields | `:57`, `:61` ("nearest-neighbor" → non-local, worse than quasi-local); time metric and slicing are an open gate (`:185`) | SUGGESTED escape (canonical reduction plus the positive-energy theorem, COMPARATOR); not constructed on Z⁴ | G4, corner "drop W2" |
| Π-CP (alternative to Π-W for (i) only) | Keep positive weights; CP violation sits in the state (spontaneous), like B4's arrow; θ_QCD ∈ {0, π} in the law | none (a physics price: a Nelson–Barr-type sector, domain walls) | escape, not tested | A5 |
| Π-QL | "nearest-neighbor" → "**quasi-local** (exponentially decaying)" | `:57`, `:61` | **SUGGESTED** for chirality. DERIVED only if exact GW lattice chirality is required (A2). The SMG route is nearest-neighbour compatible and open (A7) | A2, A3 |
| Π-FR | "nearest-neighbor" read as "finite-range cliques" (plaquette or hypercube), not pair-only | `:57`, `:61`; Lattice adjacency `:37-38` | PROVED needed for **any** lattice gauge action or fermion hopping with links, independent of chirality (A6) | A6 (HC) |

**Not forced:** no Qubit change. A fermion-carrying positive formulation would need emergent fermions from M₂(C) pair models, which is open (G0/G0b prior art: one qubit per site fails in the product-dressing class).

---

## 6. Do the prices bring back a preferred tensor (Lemma C) or a law-level arrow (Lemma E)?

**Π-W (complex RP weight).**
- **No tensor** (PROVED, elementary). B4⁺ still acts linearly; only improper elements act with conjugation. So O1's refereed counts (V, S₂) = (0, 1) for B4⁺ are unchanged (`C5_O1_referee.md:7`).
- **No arrow.** The law is invariant under B4⁺ ∋ R₄ⱼ(π), which reverses x₄, so no time orientation is preserved and Lemma E (`C5_O1_referee.md:21`) is not triggered.
- Θ = CRT is kept. Π-W gives up only K and P′, i.e. it allows explicit T- and CP-violation. That is not an arrow.

**Π-CP (positive weight, spontaneous CP).** The law keeps K (time reversal) and P′: no tensor and no arrow. **The law is maximally time-symmetric**, which is consistent with B4. T-violation then sits in the state, next to the arrow. READING: positivity and B4 point the same way.

**Π-QL.** The overlap kernel is W(B4)-covariant. Summable couplings still give a finite point group (Lemma C′), so protection is unchanged. No tensor, no arrow.

**Gravity alternatives to Π-W.**
- **GHP contour rotation:** covariant, no tensor or arrow. But the conformal component becomes imaginary, which is Π-W in another form.
- **Π-NL (canonical reduction, positive):** the slicing singles out e₄, so V₂^tl ≠ 0 **in the law's description**. Gauge-invariant physics stays covariant, so there is no preferred tensor that matter can feel (SUGGESTED). No arrow: the slicing is time-reflection symmetric. Its real cost is power-law non-locality. A purely local TT-gauge restriction without the non-local constraint term is model A-like and gives the wrong γ.
- **CDT foliation:** a preferred tensor, class I.
- **Positive 4D-TT Gaussian:** covariant and RP on Riemann, but γ = ½, excluded.

---

## 7. Verdict against the FIXED readings (`TESTS.md:2582-2589`)

- **(ii) graviton: DERIVED.**
  - Hypotheses W1–W3. Statement: no positive measure with a **local or quasi-local** real coupling of stress sources reproduces linearized GR's long-range response, because positivity forces a ≤ ⅓ (γ ≤ ½) and Cassini needs a = ½.
  - It is stronger than registered: it holds for any lattice, any variable choice, quasi-local as well as nearest-neighbour, and with or without normalizability.
  - Its one escape keeping positivity is power-law non-locality (Π-NL, SUGGESTED).
  - The bounded companion G1 (real-contour EH, any FP gauge fixing, non-normalizable) is CHECKED on K7a's symbol.
  - Expectation was SUGGESTED. **Exceeded.**
- **(i) chiral fermions: DERIVED in its CP-violating form; SUGGESTED for chirality per se.**
  - DERIVED part: Lemma K + K″ under K1–K4, with escape K3 (spontaneous CP violation).
  - Expectation "DERIVED for nearest-neighbour (Nielsen–Ninomiya plus tastes)": **NOT met as stated.**
    - Nielsen–Ninomiya excludes only the free, exact-on-site-chirality class, at any locality, so it is not a nearest-neighbour result.
    - The nearest-neighbour-specific no-go (A2) covers only the GW route.
    - Interacting SMG is open.
  - Expectation "chiral phase SUGGESTED": met, with the sharpening that the phase is variable-dependent unless CP is violated.
- **Not REFUTED.** No explicit positive RP W(B4) weight carries (i) and (ii). (ii) is now excluded for positive weights.
- **Net:** on the gravity side set B pays Π-W ("probability distribution" → "reflection-positive weight") or, alternatively, Π-NL (keep the probability, give up locality for the constraint sector). Π-QL is suggested only. The O5 expectation "set B pays an extra Admissibility price" is confirmed, for a different main reason than registered: the conformal mode as fixed by light bending, not chirality.

**Strong-word check.**
- "Every positive weight" in G4 means W1–W3: a local or quasi-local real coupling of stress sources, and an isotropic GR-like IR form with a fixed by γ.
- "No positive measure" does **not** cover power-law non-local laws (Π-NL).
- "Any variables" excludes coupling through non-real observables, which is the escape.
- "Proved" for Lemma K assumes μ real and Θ given by conj ∘ (configuration map).
- A2 is "no solution in the class", not Horváth's full theorem.
- Every literature item is recalled and unverified.

**Needs codex referee:** G4/Lemma W (a no-go, and the main result), Lemma K and K″, A2's class statement, and the price table.

---

## 8. Files (all in `scratchpad/C5/R2-4/`)

| Script | Output | Checks |
|---|---|---|
| `r24_graviton_quotient.py` | `.out` | G1: gauge invariance, quotient (5+,1−), conformal mode, 2400 gauge fixings |
| `r24_unimodular.py` | `.out` | G2: tr h = 0 + transverse diffeos still (5+,1−) |
| `r24_source_convexity.py` | `.out` | G4: a = ½ (GR) vs ⅓ (positive), W(θ) = −1.5, γ |
| `r24_conformal_rp.py` | `.out` | G3: OS matrices (252×252) on Riemann, GR vs positive 4D-TT, q = e₁ |
| `r24_conformal_rp_generic.py` | `.out` | G3 at a generic spatial momentum |
| `r24_conformal_rp2.py` | `.out` | G3: Ricci/Riemann contact versus non-contact, A vs B |
| `r24_overlap_and_doublers.py` | `.out` | A1 doubler index sum; A3 overlap GW identity, locality, decay |
| `r24_gw_ultralocal.py` | `.out` | A2 canonical R, d = 1..4 (sympy solve) |
| `r24_gw_generalR.py` | `.out` | A2 general multilinear R, Gröbner, d = 1..4 |
| `r24_conformal_rp_diff.py` | `.out` | G3: the A and B OS matrices differ by 28% (Frobenius) |

**Note on a diagnostic line.** The line "eigen-check (A) … False" in the G3 outputs tests a normalization identity that does not hold in plain (non-√2) components. It is not used. The covariance used is V(VᵀKV)⁻¹Vᵀ, which is correct for any basis V.
