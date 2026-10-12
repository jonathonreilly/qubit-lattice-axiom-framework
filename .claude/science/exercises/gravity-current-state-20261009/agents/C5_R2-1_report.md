# C5 R2-1: class II gravity. Can a Z⁴ grid carry an exact gauge identity without being a continuum in disguise?

**Worker.** Claude Opus 5.5 (probe R2-1), same model family as the supervisor and every round-1 probe. **Not refereed.** Run 2026-10-12 from 11:53Z to 12:15Z. No repository file was edited.
**Scratch.** `scratchpad/C5/R2-1/`: this report, plus `scripts/` containing `r21_perfect_remnant.py/.out`, `r21_whitney_blocking.py/.out`, `r21_collision.py/.out` and `r21_collision_d2.py/.out`.
**Read in full.**
- `docs/MINIMAL_AXIOMS_2026-06-29.md`.
- `TESTS.md:2302-2643`: Campaign C5, the round-1 results, and R2-1 at `:2465-2490`.
- `TESTS.md:86-140` (T2 and its referee).
- `agents/C5_O5_synthesis.md`; `SUMMARY.md` §§15–21; `PRICE_NOTE.md` §5 and the v6 delta.
- Referee files: `C4_K1_referee.md`, `C4_K2_referee.md`, `RFW_F1_referee.md`, `RFW_F2_referee.md`, `C4_I1_referee.md`, `C5_O1_referee.md`, and `scripts/T2/referee/REFEREE_VERDICT.md` (Lemma R).

**Labels.** proved (a complete argument is given here) / checked (numerical or symbolic) / suggested / reading / comparator (outside literature, recalled or fetched).

---

## 0. In plain words

- **The grid's gauge identity has two halves.**
  - The graviton's own half is easy. Averaging the continuum metric over links and plaquettes ("blocking") gives an exact, strictly local lattice gauge identity. This is checked symbolically.
  - The matter half is where everything fails. The identity needs a *constant* gauge shift to act on matter as an exact continuous translation. With interacting matter this must hold already at first order in κ.
- **That one requirement decides the question.** An exact continuous translation of an interacting lattice field needs a "momentum" that adds up exactly in every collision. On a grid, any well-behaved momentum is periodic. A periodic function cannot equal k on any patch, and the collisions force it to equal k on a patch.
  - The only way out is for each lattice momentum k to carry an infinite ladder of states k + 2πn: one state for every copy of the Brillouin zone. That ladder *is* the continuum folded into the zone.
- **The Ginsparg–Wilson / perfect-action route does exactly that.** A blocked ("perfect") action has one field per site and couplings that fall off exponentially. Yet its propagator has a pole for every n, and the residues are not suppressed. Its exact remnant translation acts on the n-th pole as the continuum momentum k + 2πn.
  - So it has finitely many fields per site but infinitely many states per cell. The continuum is hidden in its long-range time couplings.
- **Answer to R2-1.** In the class tested, an exact identity exists only on that hidden continuum. A grid with finitely many states per cell cannot carry it once matter interacts.
- **Reading: COLLAPSES-TO-A (bounded).** Set B, when given an exact graviton identity, is set A in lattice coordinates.

---

## 1. Hypotheses (stated before the title), and what the scope excludes

R2-1's setting (`TESTS.md:2472`) is Euclidean Z⁴ at ξ = 1, a W(B4)-covariant law, finitely many fields per site, quasi-local couplings, scalar matter (free, then φ⁴ or Yukawa) and a linearized graviton.

Theorem T (§3) uses only the following:

- **H1 (identity).** Graviton transformations are δh = D(∂)ξ + O(κ), with D translation-covariant and D(q) = iq + O(q²), so D(0) = 0. Matter transformations are δφ = κ ξ^μ T_μ[φ, h] + O(κ²).
  - T may be field-dependent, may mix in auxiliary fields, and may be any Ginsparg–Wilson/Lüscher-modified form.
  - The identity is exact at the order used. For the quantum statement, it is exact up to the Jacobian (trace) term. A "GW relation" whose right-hand side cannot be absorbed into a modified exact symmetry is explicit breaking, not an identity, and is excluded.
- **H2 (interaction).** The matter self-coupling (λ for φ⁴, g for Yukawa) is independent of κ. The tree-level on-shell 2→2 matter amplitude is not identically zero near threshold.
- **H3 (it is gravity).** The constant-ξ charge has nonzero slope on the physical band: ∂τ_j/∂k_j(0) ≠ 0.
  - Equivalently, the graviton couples to rest energy (the t₀ slope is nonzero), and W(B4) carries the slope from the time axis to each spatial axis.
  - A zero-slope "identity" does not couple h to energy-momentum (Lemma W, `C5_O2_referee.md:5`).
- **H4 (asymptotics).** The law is OS-reconstructible (reflection positive), with a physical one-particle band that is isolated near its bottom k = 0, real-analytic, and has a nondegenerate Hessian there. The charge acts additively on asymptotic states (cluster property).
  - Tree-level variant without OS: the symbols are analytic in a strip containing the near-threshold complex shell (for Steps 1–4). For Step 5, the strip must also contain the shell along a path that winds once around a spatial cycle. That holds automatically for finite-range couplings. For quasi-local couplings it needs the strip width to exceed the band's maximum imaginary time-momentum along that path.
- **H5 (finite fibre).** At each spatial momentum k ∈ T³, the matter one-particle space is finite-dimensional, N < ∞. The charge acts on it by a matrix P_j(k) that is real-analytic and periodic in k.
  - *This is not implied by "finitely many fields per site"* when couplings are quasi-local in time (§4).
- **H6.** d = 3 spatial dimensions; more generally d ≥ 2.

**Outside realizations this scope excludes.** These are listed so the title does not exceed the proof.
- (X1) Infinite one-particle fibres (towers): perfect/blocked actions, P10, Kato–Sakamoto–So's "infinitely many flavours".
- (X2) Non-analytic or power-law charges and vertices: SLAC, band-limited Shannon lattices (P14).
- (X3) Free matter (H2 fails). At O(κ²) this is covered only by K2/RFW's bounded results, not by Theorem T.
- (X4) A physical band that is degenerate at its bottom (tastes) without a taste-universal slope. RS S1/S2 cover bounded cases.
- (X5) Non-reflection-positive weights without the strip condition (R2-4 territory).
- (X6) d = 1.

---

## 2. Prior art (each counted once)

**In the repository and packet.**
- **T2** (`TESTS.md:86-140`). Perfect-action kernels C and C′ were tested for TT stiffness. The T2 referee found that box-blocked perfect actions have no positive one-step transfer matrix: alias weights decay polynomially while cosh E grows (`scripts/T2/referee/REFEREE_VERDICT.md` item 4).
  - T2's **Lemma R** (narrowed): it excludes ordinary local, additively momentum-conserving interacting extensions of the relabelling (`TESTS.md:140`).
- **K1** (`C4_K1_referee.md`): 11 = 3 + 8 gauge-restoration directions, and the unique gauge-invariant combination (F1 − 2F2 + 2F3 − F4)/4.
- **K2** (`C4_K2_referee.md`): the free lattice Fierz–Pauli action has an exact linearized identity with K7a placement. Scalar and fermion are exact through O(κ) and fail Killing closure at O(κ²).
- **RFW F2** (`RFW_F2_referee.md`): no C¹-at-q=0 completion with only h and φ, for K2's fixed O(κ) data.
- **RFW F1**: a fixed-field graded FAIL. Off-diagonal and auxiliary routes are open.
- **I1** (`C4_I1_referee.md`): exact Poincaré closure forces a complete reciprocal-lattice tower at the one-particle level.
- **RN L2.** Lemma L2-A (`agents/RN_L2_report.md:45-66`) and its referee (`RN_L2_referee.md:24`): massive NN-KG and tight-binding bands in d ≥ 2 have no odd periodic C¹ collision invariant, and quasi-local dressing cannot rescue them. The referee notes that "matrix-valued degenerate bands and unrestricted conserved operators are not covered".
- **RC C1** (`TESTS.md:1172-1177`): Lemma R, that the C¹ invariants of normal collisions on the lifted zone are λE + b·k + c; and Theorem B1, that no finite-component periodic analytic one-body matrix has an exact SLAC band on an open set.
- **RS S1/S2**: matrix and taste charges, staggered QED. "The obstruction is analyticity plus periodicity, not umklapp" (`agents/RS_S2_report.md:80`).
- **RG G1**: umklapp amplitudes must vanish.
- **O2 Lemma W**: the soft residue is an additive collision invariant (`C5_O2_referee.md:5`).

**Outside (comparators).**
- **Kato, Sakamoto, So**, *Taming the Leibniz rule on the lattice*, [arXiv:0803.3121](https://arxiv.org/pdf/0803.3121). There is no lattice difference operator and product that are both translation-invariant, local, and satisfy the Leibniz rule. A local product forces a non-local difference operator for finitely many flavours. Their proposed escape is "an infinite number of flavors" with a nontrivial site–flavour connection. That is the same tower as here.
  - Their later *cyclic* Leibniz rule ([arXiv:1411.1128](https://pdf.arxiv.org/pdf/1411.1128)) keeps one nilpotent supercharge, not translations.
- **Bergner, Bruckmann, Pawlowski**, *Generalising the Ginsparg–Wilson relation: lattice supersymmetry from blocking transformations*, [arXiv:0807.1110](https://arxiv.org/abs/0807.1110). Blocking a symmetry that contains a derivative leads to SLAC-type non-local derivatives. Locality is regained only for special kernels in solvable quantum mechanics. For interacting theories the blocked action is polynomial "only under special circumstances".
- **Recalled:** Lüscher's GW ⇔ exact modified symmetry; Hasenfratz–Niedermayer and Bietenholz–Wiese perfect actions; Spohn's phonon collision-invariant theorem ([math-ph/0605069](https://arxiv.org/abs/math-ph/0605069)).

**What is new here.**
1. The reduction "any exact identity, GW-modified or not, with interacting matter ⇒ an exact translation symmetry of the matter theory at O(κ)". This makes the prior collision-invariant no-gos decide R2-1.
2. The finite-fibre/tower dichotomy for general analytic dispersions and matrix charges (the determinant step).
3. An explicit perfect-action check that one field per site hides the complete tower, with undiminished on-shell residues.
4. The graviton-sector Whitney blocking and the K1 bookkeeping.

---

## 3. Theorem T (proved under H1–H6): no finite-fibre identity once matter interacts

**Step 1 — reduction (proved).**
- Take δS at order κ¹ and set h = 0.
- Two kinds of term survive: T[φ, 0]·∂S_m/∂φ, and (Dξ)·∂S/∂h at h = 0. The second vanishes for constant ξ, because D(0) = 0.
- Terms in which h transforms into matter (δh ∋ κ U φ or κ V φφ) multiply ∂S/∂h at h = 0 = κ T^{μν}[φ] + (tadpole). They are O(κ²), or they vanish once the tadpole is tuned away.
- So for constant ξ, the full interacting matter action S_m[φ] (λφ⁴ or Yukawa, to all orders in the matter coupling, since λ and g are independent of κ) must be invariant under δφ = ξ·T[φ, 0].
- **The constraint therefore appears at O(κλ), before K2's O(κ²) Killing commutator.**
- At O(λ), with T = T⁽¹⁾φ + λN[φ], the N-variation of S_free is equation-of-motion trivial. What remains is the on-shell condition Σ_i t(p_i) V₄(p_i) = 0 on the 4-point shell incidence with Σp ≡ 0 (mod 2π).

**Step 2 — charge (standard, recalled; needs H4).**
- An exact quasi-local symmetry commutes with the S-matrix. On asymptotic states it acts additively with one-particle action τ_j(k): the eigenvalue of P_j(k) on the band.
- A nonzero 2→2 amplitude therefore makes τ_j a collision invariant wherever the amplitude is nonzero. By analyticity and continuity this extends to the whole connected regular shell, umklapp branches included.

**Step 3 — local lemma (proved, elementary; the same content as RC-C1 Lemma R and Spohn's local step, counted once).**
- Setting: let τ be a C³ collision invariant near (c, c; c, c), for a dispersion ω with nondegenerate Hessian at c, in d ≥ 2.
- Write P = 2c, g(k) = τ(k) + τ(P−k), and h(k) = ω(k) + ω(P−k). Then g is locally constant on the level sets of h. So ∇τ(c+u) − ∇τ(c−u) = λ(u)(∇ω(c+u) − ∇ω(c−u)).
- Expand in u = tû. This gives Hτ(c)û = λ₀(û)Hω(c)û for every direction û. Hence Hω⁻¹Hτ is scalar, i.e. Hτ = λ₀Hω.
- Symmetry of third derivatives forces (∂_lλ₀)Hω_ij = (∂_iλ₀)Hω_lj. If ∇λ₀ ≠ 0, Hω would have rank ≤ 1, which is impossible in d ≥ 2. So λ₀ is constant.
- Therefore τ = aω + b·k + e near c.

**Step 4 — slope.**
- Take c = 0, the band bottom, where ∇ω(0) = 0. H3 gives b_j = ∂τ_j/∂k_j(0) ≠ 0.

**Step 5 — finite fibre ⇒ contradiction (proved).**
- *Isolated analytic band.* f(k) = τ_j(k) − aω(k) − e is real-analytic and periodic on R³, and equals b·k on an open set. So f ≡ b·k everywhere, which is not periodic. Contradiction.
- *Finite fibre with crossings away from k = 0 (H5).* χ(k) = det(P_j(k) − aH₁(k) − e − b·k) is analytic on R³ and vanishes on an open set, so χ ≡ 0. Then for every n ∈ Z³, b·(k + 2πn) is an eigenvalue of the N×N matrix P_j(k) − aH₁(k) − e. Here H₁(k) is the one-particle energy matrix, assumed analytic in H5; it commutes with P_j.
  - Since b ≠ 0, this gives infinitely many distinct eigenvalues, contradicting N < ∞.
  - The fibre must therefore contain the complete ladder {b·(k + 2πn) : n ∈ Z³}: the reciprocal-lattice tower.

**Conclusion (proved under H1–H6).**
- No finite-fibre, quasi-local, Z⁴-translation-covariant law with interacting matter carries an exact linearized-diffeomorphism identity, GW-modified or not, at O(κλ). Hence none carries one through O(κ²).
- The only way past Step 5 is an infinite fibre on which the constant-ξ charge has spectrum k + 2πn. That is a continuum, one-particle momentum space R³, folded into the zone.
- This reaches I1's tower with no boost or Poincaré-closure input: translations plus one nonzero interaction suffice.

**Checks of the steps** (`r21_collision.out`; NN Euclidean KG transfer band, d = 3, m = 0.5, 3000 real 2→2 shell samples):

| Check | Result |
|---|---|
| ω exact invariant | residual 2.2e-15 |
| Lifted k₁ on local non-umklapp collisions | residual 8.9e-16 |
| Sawtooth k₁ on umklapp rows | residual exactly 2π (non-umklapp rows 1.8e-15) |
| Fourier truncations of the sawtooth, R = 1…64 | umklapp RMS rises 3.07 → 4.18, toward the sawtooth's value; the miss never closes |

**A numerical caveat (reported, not hidden).**
- Unit slope at the single point k = 0 is too weak a normalization numerically. Oscillatory charges such as sin(Nk₁)/N have unit slope and small residual (0.42 → 0.031 for R = 1…3, d = 3).
- Requiring τ = k₁ on the whole soft ball |k| < 0.5 gives a residual that still falls with range: d = 2, R = 1…10 gives 1.02 → 0.165 (`r21_collision_d2.out`). It is not saturated at R = 10.
- So *approximate* finite-range charges can push the defect to hard, lattice-scale momenta. Only *exactness* is excluded.
- Reading (not proved): that is the expected pattern. An approximate identity leaves the K1 directions generated by loops that sample the hard region, where the defect is O(1) (§5b).

---

## 4. The Ginsparg–Wilson / perfect route itself (probes a, d, e)

### (a) Construction

**Graviton sector at κ⁰: exact and strictly local (proved; checked symbolically).**
- The blocking is Ξ_n(x) = ∫₀¹ ξ_n(x + s e_n) ds (link average); H_mn = plaquette average of h_mn for m ≠ n; H_nn = ½ × the two-link tent average of h_nn.
- It maps the continuum gauge orbit exactly onto δH_mn = D_mΞ_n + D_nΞ_m and δH_nn = D_nΞ_n, with D the forward difference (`r21_whitney_blocking.out`: all four residuals 0 for a random cubic polynomial plus a trigonometric ξ).
- Transverse smearing commutes with it, so the map can be made W(B4)-covariant. Changing variables in the blocking integral then gives the blocked Fierz–Pauli action an exact local identity: the Whitney/DEC (K7a-type) placement, counted once with K2.
- Gauge-fixing within ker B_ξ is a formal step.

**Free matter: the remnant translation is exact (proved and checked).**
- The remnant translation is T_μ = B∂_μΔBᵀG⁻¹, with symbol t_μ(k) = [Σ_n |B̂(k+2πn)|² i(k+2πn)_μ/((k+2πn)² + m²)]/G(k).
- t is odd and imaginary and G is even and real, so T is G⁻¹-antisymmetric and δS_lat = 0 exactly. Checked: 2.6e-17 (`r21_perfect_remnant.out` §1).
- In GW form: the naive lattice derivative breaks S_lat by a term set by the blocking kernel, while the modified (remnant) transformation is exact.

**Interacting matter.**
- The remnant is the conditional expectation ⟨B δφ⟩ given Φ. It is exact by change of variables (standard, recalled).
- It is non-linear in Φ. Its quasi-locality is **not established**; Bergner–Bruckmann–Pawlowski find a polynomial action only in special cases.

### (d) Locality (checked, free part)

| Quantity | Fitted decay rate per lattice unit (axis, r = 6–17) |
|---|---|
| Perfect action G⁻¹ | 1.35 |
| Remnant translation T₁ | 1.30 |

- Parameters: d = 2 proxy, Gaussian B̂ = e^{−σ|p|²/2}, σ = 0.6, m = 0.5, α = 1.
- The symbols are analytic in a strip, i.e. exponentially local.
- Interacting remnant: open.

### (e) Field content: the tower is hidden in one field per site (proved and checked)

- At fixed spatial k₁, G has a pole in complex k₀ at k₀ = iE_n, with E_n = √(m² + (k₁ + 2πn)²), for **every** n ∈ Z.
- The exact residue is e^{σm²}/(2iE_n). On shell P² = −m², so an O(4)-covariant Gaussian kernel does not suppress the alias states at all.
- 60-digit contour integrals (`r21_perfect_remnant.out` §3) give Res N₁/Res G = i(k₁ + 2πn₁) to all printed digits for n₁ = 0, ±1, 2, and Res N₀/Res G = −E_n.
- So the remnant charge acts on the n-th pole as the continuum momentum and energy.
- The number of poles below energy Λ grows like Λ/π (1, 3, 7, 13 for Λ = 5, 10, 20, 40).
- **This is exactly the infinite fibre that Step 5 requires.** The "finitely many fields per site" of R2-1's setting is the wrong finiteness: quasi-local couplings along the time axis store infinitely many states per cell.
- Suggested, not computed: for the Gaussian kernel, as for T2's box kernel, the undiminished tower likely rules out a positive one-step transfer matrix (cf. T2 referee item 4). This bears on R2-4.

---

## 5. Probes (b), (c), (f)

### (b) Counting the 11 K1 directions

- **Proved:** a linear identity K_L(q)D(q) = 0 with D(q) = iq + O(q²) forces K_L⁽⁰⁾ = 0 (the 3 mass forms), because symmetric q⊗ξ span all symmetric tensors.
- At O(q³) it forces the two-derivative part into the gauge-invariant combination, which K1's referee confirmed is unique (`C4_K1_referee.md:3`). That removes the 8 kinetic forms.
- **So a linear identity fixes all 11 at tree level.** The blocked graviton has one (§4a).
- But K1's directions are generated by matter loops. Protecting them needs the matter identity at O(κ²) (one loop, free matter) and at O(κ²λ) (two loops).
  - In the finite-fibre class Theorem T kills the latter.
  - For free finite-band matter only K2 and RFW's bounded FAILs apply.
- **Net:** in the finite-fibre class, all 11 stay unprotected once matter interacts. On the tower (blocked continuum) all 11 are fixed, inherited from the continuum.
- Reading: approximate finite-range identities leave the defect at hard momenta (§3 caveat). Loops sample the whole zone, so the generated coefficients keep their natural loop size.

### (c) Closure

- On the tower, the remnant generators are the continuum e(4) acting on the folded continuum. Closure is inherited (formally for the interacting case; consistent with I1).
- In the finite-fibre class, closure fails earlier than K2's Killing commutator: the translations themselves cannot be exact at O(κλ).

### (f) Interactions

- Theorem T: no exact identity survives a φ⁴ or Yukawa vertex with additive lattice momentum in any finite-fibre quasi-local law.
- This generalizes T2's narrowed Lemma R and RN L2 to:
  - general analytic dispersions;
  - field-dependent and GW-modified generators;
  - auxiliary fields;
  - matrix charges on a finite fibre with a nondegenerate physical band.
- On the tower, the blocked vertex conserves the continuum momentum k + 2πn. So same-band umklapp amplitudes vanish, which is exactly RG G1's requirement, and the identity survives.

---

## 6. Against the FIXED readings (`TESTS.md:2484-2488`)

| Reading | Status |
|---|---|
| **PASS** | **Not met.** No explicit finite-fibre law exists (Theorem T). The perfect action is not explicit for interacting matter, its interacting quasi-locality is unproved, and it is the blocked continuum supplied as data, which is the COLLAPSES-TO-A clause |
| **FAIL**, as literally worded ("every quasi-local W(B4) law with finitely many fields per site") | **Not established, and false at the free level.** The Gaussian-blocked perfect action is quasi-local, W(B4)-covariant, has one field per site, and its remnant translation is exact (checked). The literal FAIL is refuted at the free level. Whether the interacting blocked law stays quasi-local is open |
| **COLLAPSES-TO-A** | **Reading returned, bounded.** "Only" is proved under H1–H6: every finite-fibre quasi-local law fails at O(κλ). "Exists" holds at the free level (remnant exact and quasi-local, with the complete tower and undiminished residues), and holds formally for the interacting blocked continuum |

**Reading: COLLAPSES-TO-A (bounded).** Record it as *"set B reduces to set A in lattice coordinates"*, with these scope notes:
- The exclusion half is a theorem under H1–H6, with X1–X6 outside it.
- The existence half is checked for free matter and formal for interacting matter.
- Free matter at O(κ²) without self-interaction (X3) is not decided here beyond K2/RFW.
- Degenerate taste bands without a universal slope (X4) and non-reflection-positive weights (X5, see R2-4) are outside the proof.

**Against the expectation** (`TESTS.md:2489-2491`: INCONCLUSIVE, leaning COLLAPSES-TO-A):
- The result is stronger than expected.
- The expectation put the decisive step at O(κ²), in the nonlinear algebra. It actually sits at O(κλ), in the matter translation, as soon as matter interacts.
- The graviton's own gauge structure blocks cleanly and locally.

**What this means for the set choice (reading, not refereed).**
- Set B's price B5 cannot be paid by a lattice identity without importing set A's continuum. B5 is "an exact lattice linearized-diffeomorphism identity, or K1's 11 tunings" (`C5_O5_synthesis.md:358`).
- Set B therefore keeps K1's tunings, or else it becomes A.
- This sharpens P10: the tower is forced by **translations plus any interaction**, without I1's boost input. P10's Qubit price is unchanged: one-particle level only, with the microscopic claim open (`C4_I1_referee.md:15`).

---

## 7. Strong-word check

- "Proved" is used only for:
  - Steps 1, 3, 4 and 5;
  - the free remnant's exactness;
  - the pole and residue formula;
  - the tree-level K1 count;
  - the κ⁰ Whitney identity.
- Step 2 is standard and recalled, conditional on H4.
- "Exactly" refers to exact identities, not to numerical agreement.
- Not claimed:
  - that the interacting perfect action is quasi-local;
  - that Gaussian-blocked actions lack a positive transfer matrix (suggested only);
  - anything about free matter at O(κ²).
- Same family, unrefereed. Under the C5 rules, the bounded no-go part (Theorem T, i.e. the exclusion half) needs the codex referee before it is recorded.
