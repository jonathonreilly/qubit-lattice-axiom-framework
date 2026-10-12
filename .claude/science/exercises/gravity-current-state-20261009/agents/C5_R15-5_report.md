# C5 R15-5: producing the graviton at strong coupling — does a Gu–Wen-type qubit model escape the Gaussian exclusions?

**Worker.** Claude Opus 5.5 (same family as the supervisor and every C5 worker). 2026-10-12, 22:10Z to about 22:30Z. **Unrefereed.** I edited no repository file. Scripts and outputs: `S/scripts/` (s1, s2, s3; each run under 10 s on 2 threads). One untrusted download (the Gu–Wen PDF) sits unread in `S/downloads/`; it could not be rendered, so the literature points below come from tool summaries of the arXiv abstract and ar5iv HTML pages. They are labelled comparator.

**Paths.**
- `P/` = `.claude/science/exercises/gravity-current-state-20261009/`.
- `TESTS` = `P/TESTS.md`. The R15-5 registration is at `TESTS:5010-5023`.
- `AX` = `docs/MINIMAL_AXIOMS_2026-06-29.md`.
- `N0914` = `docs/LOCAL_FINITE_CLOCK_TENSOR_CONSTRAINTS_CUBIC_DISPERSION_AND_LINEAR_GRAVITY_BOUNDARIES_BOUNDED_THEOREM_NOTE_2026-09-14.md`.
- `vX` = `P/agents/C5_X_referee_verdict.md`. `R15-3` = `P/agents/C5_R15-3_report.md`.
- `S` = `scratchpad/C5/R15-5/`.

**Labels.**
- proved = a derivation made here (unrefereed);
- checked = numerics run here;
- suggested = an argument, not a proof;
- reading = an interpretation;
- comparator = literature (fetched as untrusted text and summarized by a tool, or RECALLED).

---

## 0. Plain words

- **The question.** Every graviton no-go so far covers ordinary "free-field" (Gaussian) models. Gu and Wen proposed qubit models in which gauge constraints, rather than energy, remove the unwanted graviton partners. Does that escape work, and does it give light-speed gravitons that pull on matter like gravity?
- **(a) What the escape is (proved, checked).** In the exact-constraint N-type theory (linearized gravity in Hamiltonian form on Z³), the partners are not gapped; they are *not states at all*. They are gauge directions removed by two exact constraints. The theory breaks two hypotheses of every Gaussian no-go:
  - its energy on the full set of fields is not positive (a negative "conformal" direction on each side);
  - its physical fields form a bundle that jumps at k = 0. That jump is exactly the discontinuity that marks the edge of R15-3's Theorem C.

  So the gauge escape and R15-3's "discontinuous symbol" escape are the same thing, seen two ways.
- **(b) The count.** With ordinary continuous (CCR) fields, exactly two physical branches survive in every direction. Both are linear (ω = |k| at small k) and carry the helicity-±2 characters on axes, face diagonals and body diagonals. There is no doubler, and the static pull from a scalar source is attractive and goes like 1/r (checked, s1, s3).
- **But qubits can't hold that theory in the controlled regime.** The light-speed graviton and the 1/r pull both come from **one term**, h:R(h) (the linearized Einstein–Hilbert term). That term is gauge-invariant only as a whole: it is not built from gauge-invariant local pieces. A compact variable can only carry gauge-invariant periodic pieces ("characters"), so the term needs the h side to be noncompact. The ladder (proved as a corollary of the 09-14 note's lemma; checked):
  - continuous fields on both sides: z = 1, 1/r;
  - h integer, E compact: z = 2, 1/r;
  - E integer, h compact: z = 2, contact force only;
  - qubits or clocks on both sides: z = 3, contact force only.

  Strong-penalty perturbation theory to **any finite order** stays on the qubit rung (proved sketch, Lemma W). That closes the "higher-order returning words" gap the R12-5 referee left open, inside its hypotheses.
- **(c) Coupling to matter (proved; standard structure, checked on the lattice symbols).** If the two constraints carry matter sources, keeping them true in time forces two things:
  - the source of the momentum constraint is the *current* of the source of the scalar constraint;
  - it is locally conserved.

  With energy as the scalar source, matter's energy flux must equal its momentum density, as an exact collision invariant. That is the relativistic condition T⁰ⁱ = Tⁱ⁰. On any non-constant periodic band it fails for generically interacting matter (proved under a stated hypothesis). The box band meets it only inside the box. So the N-type graviton does not escape the matter-side boost wall; it inherits it. Gu–Wen's own "masses" are scalar-constraint defects, not the energy of arbitrary matter (comparator), so universality is not supplied.
- **Reading: INCONCLUSIVE.**
  - No qubit model passes.
  - The only window left is non-perturbative: penalties comparable to the other couplings, high-harmonic or aliasing words, or a singular semiclassical limit. That is Gu–Wen's own uncontrolled regime.
  - The decisive missing computation is named in §8.

---

## 1. Hypotheses, classes, excluded realizations

**Fields.**
- Six canonical pairs per cell, q = h, p = E, symmetric tensors (N0914:87-92), with midpoint symbols q̂_i = 2 sin(k_i/2) (N0914:200-201).
- Vector constraint G E = q̂_i E_ij.
- Scalar constraint S h = q̂_iq̂_jh_ij − q̂² tr h.
- Curvature R(h) = ε ε ∂∂ h.
- Scalar-gauge-invariant E-character content C(E) = ε∂(E − δ trE/2) (N0914:52-55).

**Classes used.**
- **𝒩 (exact-constraint N-type, CCR).** H_N = J/2[E:E − ½(trE)²] + g/2 h:R(h) on the quotient {G E = 0, S h = 0}/gauge (N0914:70-76). Real-valued fields.
- **Ladder variants.** The same constraints, with one or both sides compact, so that the compact side's energy is built only from gauge-invariant characters (N0914:186-215).
- **𝒲 (strong-penalty finite-slot).** Z_N clocks with exact commuting stabilizer constraints (N0914:85-160), perturbation V = finite sum of Weyl characters, penalty U ≫ ‖V‖ (Schrieffer–Wolff convergent). Words obey the integer-lifting bound (N0914:218-222). The small-field expansion of the effective Hamiltonian is regular (N0914's summability, :239-252).

**Excluded realizations.** These are not covered by any negative statement here:
- penalties comparable to the other couplings (U ~ J ~ g, Gu–Wen's regime) where 1/U series need not converge;
- high-harmonic or aliasing words (word length ~ N);
- singular semiclassics or Berry structures;
- non-abelian or field-dependent constraint algebras;
- gapless matter that is integrated out;
- fermionic slots;
- nonlinear gravity, Λ.

---

## 2. Prior art (each counted once)

1. **Lane R** (`TESTS:692-767`).
   - Strong-class S, S-tl, V and V-tl have 5, 4, 3 and 2 modes, with dispersions k, k, k², k³ (`TESTS:752`).
   - Scalar charge gives linear TT only with partners (`:753`).
   - **Exact-constraint weak VS/N-type: two positive linear TT modes and an attractive 1/r response to a supplied source; open: the lattice stress/source bridge and a compact realization** (`:759`).
   - My s1/s3 recheck this, so count it once. My new content is §§3–5's location of the escape, the ladder, Lemma W and Lemma T.
2. **N0914.**
   - The H_L/H_N comparators (ω² = Jgk⁶ and Jgk², `:66-76`).
   - H_N's energy is not periodic in compact coordinates (`:79-84`).
   - **Character lemma:** every local h-character is O(k²) and every E-character is O(k), so frequencies are O(k³) (`:186-215`); it survives eliminating gapped auxiliaries (`:254-259`).
   - Finite penalties give det K = −J²/2 (`:262-278`).
   - Static source: contact for H_L, −g|ρ|²/(4k²) for H_N (`:282-296`).
   - Gu–Wen N-type uncontrolled (`:374-375`).
   - My ladder is a direct corollary of the character lemma. The rotor rungs are, as far as my grep found, not written there. N0914 names compact/compact and CCR/CCR only.
3. **R11-2 X1 (refereed).** Finite-slot exact N-type constraints in the regular lifted class give O(k³) (`TESTS:4407-4409`). WW binds only when all its premises hold, and a gauge graviton has no covariant conserved stress (`vR11-2:5`).
4. **R12-5 (refereed OPEN).**
   - DW-q removes non-invariant characters at *first order* only.
   - It does "not control higher-order returning words … or non-Gaussian strong-coupling phases" (`vR12-5:5,17`).
   - Gu–Wen is outside X1 because its constraints are energetic with U ~ J ~ g (`vR12-5:11`).
   - Lemma W below addresses the returning words inside 𝒲 only.
5. **R13-2 X-G** (`vR13-2:25`) and **R14-4 G-mix** (`vR14-4:40`). Both are PSD Gaussians on six pairs. Both list "indefinite exact-constraint theories, and non-Gaussian phases" as outside.
   - R13-2's sign lemma X-S: the N-type has no sign-free product-basis Euclidean form; the sign problem sits in the trace/conformal sector (`TESTS:4758-4772`; `vR13-2:5-9`).
6. **R15-3 Theorem C** (worker, unrefereed; `R15-3:95-133`).
   - Class 𝒜: PSD, finitely many pairs, O-covariant, symbol continuous at k = 0.
   - Its own table names "flat partners accepted as gauge: needs exact constraints or an indefinite IR (lane R N-type, Gu–Wen, P-N3″)" as outside 𝒜 (`R15-3:223`).
   - X2, discontinuous at k = 0, is the only exhibit with exactly two branches (`R15-3:190-192`).
   - **Rechecked here:**
     - the per-irrep inequality by hand from the O character table: A1 0+1, A2 1+0, E 1+1, T1 0+1, T2 1+2, as stated (`R15-3:118-119`);
     - the TT stabilizer characters (s1 (4)).
   - I rely on nothing else from R15-3.
7. **Comparators.**
   - **Gu–Wen, arXiv:0907.1203** (abstract; ar5iv text summarized by a tool, untrusted).
     - L-type: only helicity ±2 gapless, ε ∝ k³, semiclassical "reliable".
     - N-type: "no reliable approach".
     - The lattice N-type imposes the scalar constraint η = R^ii = 0 and the vector constraint ∂_iE^ij = 0 by cosine penalties on compact link variables. Its low-energy H is J/2[E² − ½(trE)²] + g/2 a_ij R^ij, gauge-invariant only up to a total derivative.
     - Reported reason for unreliability: the N-type terms do not commute with the penalty terms. Their quadratic "quantum-freeze" treatment is "an uncontrolled approximation".
     - Scalar defects are interpreted as mass and vector defects as momentum. The N-type force is attractive for like signs ∝ m₁m₂/r²; the L-type force is repulsive, ∝ |x|⁻⁴.
   - **Xu, cond-mat/0602443** (abstract): a stable algebraic Bose liquid with "soft graviton" ω ∝ k².
   - **Xu–Hořava, 1003.0009** (abstract): an fcc boson model with emergent gravity at a Gaussian z = 3 Lifshitz point, and a z = 2 phase by tuning.
   - **Rasmussen–You–Xu 1601.08235; Pretko 2017** (via `R15-3:90-91`, not re-fetched).
   - **Jenkins 0904.0453, the gauge-stress WW loophole** (via `vR11-2:5`).

---

## 3. (a) Which Gaussian assumption each Gu–Wen-type model breaks

**Lemma E (location of the escape; proved by linear algebra, checked s1).** For 𝒩 at every k ≠ 0 on the lattice zone:
- **(E1) The extended Hessian is indefinite.** The E side has eigenvalues (−½, 1, 1, 1, 1, 1)J, the negative one on tr E. The h side has (−1, 0, 0, 0, 1, 1)gq̂², the negative one on the transverse trace. (s1 (1); matches `N0914:262-267`, `TESTS:4758-4772`.)
  - This breaks the PSD hypothesis of Lemma P (`vR13-2:11`), Theorem G (`vR13-2:15`), G-mix (`vR14-4:40`) and Theorem C (`R15-3:46`).
- **(E2) The physical phase space is the quotient.** It is V(k) = ker G ∩ ker S (because S Gᵀ = 0, range Gᵀ ⊂ ker S, and (range Gᵀ)^⊥ = ker G), of dimension 2 at every k ≠ 0 (s1 (2), (5): never ≠ 2 on a 16³ grid).
  - H_N restricted to V is the reduced Hamiltonian. That is legitimate because R Gᵀ = 0 exactly, and K is scalar-gauge invariant on G = 0: P_kerG K Sᵀ = 0 to 1e-16 (s1 (1); `N0914:57-59,75`).
  - On V, K|_V = 1 and R|_V/q̂² = 1 over the whole zone (s1 (5)). So the reduced theory is positive, with no doubler.
- **(E3) The physical bundle is discontinuous at k = 0.** ‖P_V(εẑ) − P_V(εx̂)‖₂ = 1.0000 for ε = 1e-2, 1e-4, 1e-6 (s1 (6)).
  - Written as a theory on the six pairs with the unphysical directions removed, its symbol is of R15-3's X2 type, which is discontinuous at k = 0 (`R15-3:190-192`).
  - **The constraint quotient is how a local Hamiltonian realizes Theorem C's excluded discontinuous symbol.** Locality is kept because the discontinuity sits in the constraint (Gauss law), not in the Hamiltonian.

**Per model** (proved for 𝒩 and the ladder; reading for the Gu–Wen lattice model).

| Model | PSD on extended fields? | Exact constraints? | Physical branches (small k) | Hypothesis of the Gaussian no-gos it breaks |
|---|---|---|---|---|
| Continuum/lattice N-type, CCR (𝒩) | no (E1) | yes, two (G on E, S on h) | 2, z = 1, helicity ±2 | PSD (E1); continuity of the physical bundle (E3); "every pair physical" |
| L-type / H_L (N0914:66-71; Gu–Wen L) | yes (sum of squares of invariants) | yes | 2, z = 3 | only "every pair physical" (E2/E3). It keeps PSD, so Theorem G's conclusion (z ≥ 2 when partners are flat) holds, and it is z = 3 |
| Gu–Wen lattice N-type (cos penalties, compact links, U ~ J ~ g) | no: its quadratic expansion is the finite-penalty Gaussian with det K = −J²/2 (`N0914:262-270`) | no, energetic, and the other terms do not commute with the penalties (comparator; `vR12-5:11`) | claimed 2, z = 1 (uncontrolled) | none in a controlled sense. Its semiclassical expansion is not in 𝒢/𝒜 because it is indefinite and dynamically unstable (Jordan chain, `N0914:272-278`). The graviton claim rests on an unproved non-perturbative projection onto the constraint surface plus a non-periodic IR energy |
| Xu soft-graviton / Xu–Hořava (bosons, z = 2, 3) | yes (Maxwell-like, comparator) | emergent, energetic | z = 2 or 3 | the same as L-type; consistent with the ladder in §4 (reading) |

**So, precisely (proved for 𝒩, reading for Gu–Wen):**
- The escape is the pair (indefinite extended energy, exact first-class constraints).
- PSD plus exact vector-gauge flatness already forces z ≥ 2 (X-G, Theorem G, `vR13-2:15`).
- So **a linear helicity-2 branch with no physical partner needs the indefinite h:R(h)**. It is the unique O(k²) vector-gauge-invariant h-form (`R13-2:104`, s2(i) there).
- That in turn needs the **second exact constraint** (the scalar, or Hamiltonian, constraint) to remove its negative direction. This is the N-type, and only the N-type.

---

## 4. (b) Branch count, helicities, and why qubits cannot hold the N-type in the controlled regime

**Checked (s1 (2)–(5)).** In 𝒩 along ẑ, (110), (111), (1,2,5) and (2,1,3):
- dim V = 2;
- ω/|k| = 0.999996–0.999998 at |k| = 1e-2 and 1.000000 at 1e-3 (both branches; isotropic, ω² = Jg q̂²);
- stabilizer eigenvalues on V: C4 (−1, −1), C3 (ω, ω̄), C2′ (+1, +1). These are exactly the helicity-±2 characters (`R15-3:56-59`).

So the low-energy sector has exactly the two helicity-±2 gapless modes: no partner, no doubler.

**Lemma L (the compactness ladder; proved as a corollary of N0914:199-215, checked s1 (8)).** Let the two exact constraints act, and let each side be either real (CCR), integer (rotor), or compact. Energy on a compact side must be a sum of gauge-invariant characters (summable moments).
- **On the compact h side:** gauge invariance under continuous λ (generated by an integer G E) forces each h-character to be O(k²) (`N0914:203-205`). So H_hh = O(k⁴). The one O(k²) form, h:R(h), is invariant only as a whole: no factorization into analytic gauge-invariant characters exists (R15-3 s3: transverse polynomial fields start at degree 2).
- **On the compact E side:** each E-character is O(k) (`N0914:205-207`), so H_EE = O(k²).
- **On a real or integer side:** the weakly invariant quadratic forms survive exactly. K is invariant under integer Sᵀ shifts on G = 0. h:R(h) is invariant under integer Gᵀλ shifts because R Gᵀ = 0.

Hence the TT frequencies:

| E side | h side | TT dispersion (checked s1 (8): exponent along (1,2,5)) | static scalar-source energy (checked s3) |
|---|---|---|---|
| real | real (CCR) | z = 1.000 | −ρ²/(4q̂²): attractive 1/r |
| integer (rotor) | compact | z = 2.000 | +ρ²/4, k-independent: contact only |
| compact | integer (dual rotor) | z = 2.000 | −ρ²/(4q̂²): attractive 1/r |
| compact | compact (clocks, qubits; H_L) | z = 3.000 | contact only (`N0914:282-288`) |

**Two consequences (proved).**
1. **One term carries both.** The linear graviton and the Newtonian 1/r come from the same single term, g/2 h:R(h). It needs a noncompact h, and z = 1 additionally needs a noncompact E.
2. **The axioms' qubit cannot reach z = 1 in the regular class.** One finite site per point (`AX:47`) makes both sides compact.
   - Rotor rungs need an infinite-dimensional slot per site, a Qubit price like P-N1.
   - Even then they give z = 2, which LIGO and GW170817 timing excludes (reading: at a = ℓ_P the group velocity is ~ ℓ_P k ≪ 1).

**Lemma W (strong-penalty returning words; proved sketch).**
- **Setting.** In 𝒲, let P project onto the sharp zero-syndrome sector of the commuting stabilizers. Let R = Q(E₀ − H_U)⁻¹Q.
- **Step 1.** R is a function of the syndromes alone.
- **Step 2.** A Weyl character W shifts every syndrome by a fixed amount, so R W = W R′, where R′ is R with shifted argument.
- **Step 3.** Every order-n Schrieffer–Wolff word P W₁RW₂R…RW_nP therefore equals c·P(W₁⋯W_n)P, with a scalar c fixed by the intermediate syndromes.
- **Step 4.** It is non-zero only if the product commutes with every stabilizer, i.e. is a gauge-invariant Weyl character (mod N).
- **Conclusion.** Under the lifting bound (word exponents below the N0914:110-111 threshold) it is an exactly gauge-invariant character. So the order-n effective Hamiltonian lies in the class of N0914's character lemma, and if its small-field expansion is regular, **every frequency is O(k³) at every finite order**.
- **What this does.** It extends DW-q (first order, `vR12-5:5`) to all finite orders, inside 𝒲.
- **What it does not cover:**
  - non-convergent U ~ J ~ g;
  - words long enough to alias, of length ~ N;
  - resummation;
  - singular semiclassics.

  These are the excluded realizations of §1.

**Large-N clocks imitating CCR (suggested, not shown).** Making a Z_N clock "noncompact on both sides" for |n| ≪ N needs diagonal quadratic functions such as E² and h:R(h). Their periodic extension has a kink at the wrap, so their Fourier series contains harmonics up to N/2. Those harmonics alias, so the integer lift fails. Gauge orbits in the invariant sector run through the wrap, so the weak invariances (K on G = 0, h:R(h) under Gᵀλ) are broken there. This is the "high harmonics / winding with N" escape that N0914:218-222 lists. Whether the breaking is irrelevant in some phase is not decided.

---

## 5. (c) Coupling to matter: 1/r, universality, Weinberg–Witten

**1/r (checked).**
- In 𝒩 with a supplied scalar source S h = ρ, the minimal field energy is −ρ²/(4q̂²) at |k| = 0.3, 0.1 and 0.03, in every direction tested (s1 (7), s3). This is attractive between like signs and is 1/r in real space. It reproduces `N0914:291-292` and `TESTS:759`.
- The attraction comes from the negative transverse-trace (conformal) direction of h:R(h). The positive |R|² of the compact-h rungs gives only a contact term.

**Lemma T (source consistency; proved, standard Bianchi/Ward structure on the lattice symbols, checked s2).**
- **Two identities.** S K = q̂ᵀG exactly (s2: residual 5e-15, λ = q̂ with c = 1.000000), and G R = 0 exactly (4e-15).
- **The sourced constraints.** With sources, S h = κρ and G E = j, and with matter coupled as ½ h:T. Keeping them true in time requires:
  - (T1) κ ρ̇ = J q̂·j: the vector-constraint source is the current of the scalar source;
  - (T2) j̇ = −½ q̂_i T_ij: it is locally conserved, with the h-coupled stress as its flux.
- **With energy density as the scalar source** (the Newtonian coupling), (T1) says j is the energy current (up to a transverse piece and normalization). (T2) says the energy current is a conserved density whose flux is the stress. That is T⁰ⁱ = Tⁱ⁰ with ∂_tT⁰ⁱ + ∂_jTʲⁱ = 0: the Ward identity of linearized GR, now forced on the matter.

**Corollary T′ (proved under a stated hypothesis; checked in 1D).**
- **Hypothesis.** The interacting matter's only additive collision invariants are particle number, energy and crystal momentum.
- **Statement.** For a species with a smooth periodic band ε(k) > 0, the per-mode energy-current symbol is ε ε′ = (ε²/2)′. For (T2), the total energy current must be conserved in collisions, so ε ε′ ∈ span{1, ε, k}.
- **Proof.**
  - k is not periodic, so its coefficient is 0.
  - From ε ε′ = a + bε we get ε′ = a/ε + b. At the band maximum and minimum, ε′ = 0, so a/ε_max = a/ε_min = −b. Hence either ε_max = ε_min, or a = b = 0 (and then ε′ = 0).
  - Either way ε is constant. ∎
- **Check (s2).** On a cosine band, 1160 non-trivial 2→2 events (with crystal momentum and energy conserved) violate energy-current conservation with median |Δ| = 1.13. A smooth box-type band shows violations, but all of them come from processes leaving the box. In 1D, equal-mass in-box processes are trivial exchanges, so the in-box exactness (where p = k and ε ε′ = k) could not be exercised there.
- **Reading.** The N-type's universal coupling needs relativistic matter (T⁰ⁱ = Tⁱ⁰ as an exact collision invariant). That is the matter-side boost wall (the cos k factor, `TESTS:2241`; R8-2 Theorem E, the edge anomaly, `SUMMARY:619-621`). The box route satisfies it inside the box, consistent with R9-9's exact tree-level Ward coupling to number-conserving box stress (`TESTS:3940-3944`), and loses it at the edge. **The N-type graviton does not escape the walls on the matter side; it inherits them.**

**Gu–Wen's own matter (comparator, reading).**
- In Gu–Wen, masses are scalar-constraint defects, quantized topological charges with "mass quanta". Their N-type force law is attractive between like defects.
- Nothing makes an arbitrary excitation carry defect charge equal to its energy. The equivalence principle, the "universal 1/r coupling" of the PASS clause, is not supplied.
- By Lemma T, a source that is not the energy density with its current would be inconsistent with the constraint algebra once it moves.

**Weinberg–Witten (reading, using `vR11-2:5`).**
- WW does not bind here. Lorentz invariance is not exact on the lattice, and the gauge graviton has no gauge-invariant covariant local stress (Jenkins' loophole, as in GR).
- Lemma T shows what replaces WW on the lattice: the constraint algebra itself demands a symmetric, locally conserved matter stress. That is the content WW's premises would have supplied.

---

## 6. The PASS direction: what was tried

1. **CCR N-type (𝒩).**
   - Gives: exactly 2 linear helicity-±2 branches, positive on the whole zone, no doubler, attractive 1/r (checked).
   - Fails: it is not a qubit model (P-N1, `AX:47`), and universal coupling needs T⁰ⁱ = Tⁱ⁰ (Lemma T).
2. **Rotor N-type** (E integer, h compact; exact integer Gauss law G E = 0, sharp e^{iSh} = 1; H = J/2 Σ K(E) + g Σ(1 − cos R(h)), integer stencils as in N0914:133-140).
   - Gives exactly 2 helicity-±2 gapless branches at z = 2 (checked spin-wave), the comparator of Xu's soft graviton.
   - Bounded below once the conserved uniform trace of E is superselected (proved: tr E₀ commutes with H, since R and the characters have no k = 0 component). Without that superselection, Lemma U's −(1/6)(trE₀)² per site is unbounded below (`vR13-2:5`).
   - Fails: z = 2, contact force only, not qubits.
3. **Dual rotor** (h integer, E compact; H = g/2 h:R(h) + J Σ(1 − cos 2C(E))).
   - Gives exactly 2 helicity-±2 branches at z = 2 and an attractive 1/r from integer, quantized scalar sources (checked).
   - Fails: z = 2, not qubits. Of the regular models found, this is the nearest miss.
4. **Finite-slot, any finite strong-penalty order** (Lemma W): z = 3.
5. **Induced Einstein–Hilbert term (Sakharov) from integrated-out matter.**
   - With gapped matter coupled by periodic phases: no; it stays in the character class (`N0914:254-259`).
   - With matter whose vector-gauge action is a *translation*, the continuum Sakharov route: this needs a local generator of continuous translations, which finite sites lack (O2, `SUMMARY:538`). The box supplies one inside the box only.
   - Even then the coupling must be non-periodic in h, which sends h back to noncompact (P-N1) (suggested).
6. **Large-N clocks imitating CCR:** weak invariance breaks at the wrap (suggested, §4).

---

## 7. Prices (named, never adopted)

| Price | Axiom touched | Buys |
|---|---|---|
| P-N1 (supplied CCR tensor pairs, = P41/P49) | Qubit `AX:45-53` (M₂(C), `:47`) | exactly 2 linear helicity-±2 branches and 1/r at tree level (checked) |
| **P-r15-5a** (one integer slot per site on the h side: dual rotor) | Qubit `AX:47` | 2 helicity-±2 branches and 1/r, but z = 2, observationally excluded |
| **P-r15-5b** (exact first-class constraint pair G E = 0, S h = 0 as a redundancy among possibilities; lane R price) | not in the axioms. Admissibility `AX:57` supplies no redundancy (lane R R1, `TESTS:740`) | removes the partners as gauge (Lemma E) |
| **P-r15-5c** (matter supplies a symmetric, locally conserved stress, T⁰ⁱ = Tⁱ⁰ as an exact collision invariant) | source/action gate `AX:187`; this is the boost wall | universal linear coupling (Lemma T); unmet on periodic bands (T′); met in-box only |
| P-N3″ (non-perturbative phase with an indefinite IR and emergent exact constraints; unbuilt) | none named; a dynamical hypothesis | possibly z = 1 on qubits. Outside Lemma W; sign-problematic for product-basis QMC (X-S) |

---

## 8. Readings against the FIXED clauses (`TESTS:5021-5023`)

- **PASS: no.**
  - No qubit model with local terms only was shown to have exactly the two helicity-±2 gapless modes **plus** a universal 1/r coupling.
  - The model that has the right spectrum and the 1/r pull is CCR (𝒩): not qubits, and its coupling is not universal without P-r15-5c.
  - Gu–Wen's lattice N-type is uncontrolled by its authors' own account (comparator; `N0914:374-375`; `vR12-5:11`).
  - Every controlled qubit route found gives z = 3 (Lemma W with X1), and rotor routes give z = 2.
- **FAIL: no.**
  - No referee has seen any of this.
  - Lemma W is a no-go candidate in 𝒲, but it extends **X1 (dispersion)**, not Theorem C (partner count): inside 𝒲 the partners *are* removed and it is the dispersion that fails.
  - No partner-count extension of Theorem C to non-Gaussian phases was found. An attempted Bijl–Feynman (single-mode) version needs continuous static structure factors at k = 0, which is exactly what Coulomb-phase pinch points violate (suggested). So it cannot cover the gauge escape.
- **INCONCLUSIVE: yes.** The decisive missing computation:
  - **Strong-coupling stiffness.** A controlled, non-perturbative computation, *not* product-basis QMC (sign problem, X-S), on a finite-slot N-type model in its non-convergent regime U ~ J ~ g. It must establish whether the sharp-constraint ground state has an **O(k²) Einstein–Hilbert stiffness on TT**: a static TT susceptibility χ_TT(k) ∝ 1/k², versus 1/k⁴ or 1/k⁶ for the rotor and qubit rungs. Equivalently, whether the weakly invariant form h:R(h), which no lifted regular character can be, is generated non-perturbatively through aliasing words or a singular semiclassical limit. The same computation should check that the scalar-channel static response is 1/k², not contact (the 1/r test).
  - **Feasibility.** Tensor-network or ED studies at minimal N, or a large-N clock with controlled wrap-breaking. ED is likely infeasible at ≥ 140 logical qubits (`vR12-5`, worker figure, RECALLED from `C5_S14_synthesis.md:104`).
  - **Matter-side condition (needed for PASS even if the above succeeds).** A local matter law with T⁰ⁱ = Tⁱ⁰ as an exact collision invariant on the whole zone (Lemma T and T′). That is the boost wall, which no route has crossed without the box's edge.
- **Expectation check.** The registration expected nothing explicit. The most likely outcome was INCONCLUSIVE, and that is the outcome.

---

## 9. Strong-word check and scope

- **"Exactly two" (§4)** holds for 𝒩 and its ladder variants on the physical quotient at k ≠ 0. Gauge directions are not states there. Under R15-3's strict N1 counting on the extended space, the gauge directions would be flat "branches". The registration's "low-energy sector" is the physical one, so I use the quotient.
- **"Proved":**
  - Lemma E;
  - Lemma L (a corollary of N0914's refereed-in-repo-review character lemma; its Taylor and moment hypotheses are inherited);
  - Lemma T (linear constraint algebra; standard in the continuum);
  - T′ (under its collision-invariant hypothesis; integrable matter with extra invariants is not covered);
  - Lemma W (sketch: syndrome-commutation step plus N0914's lemma; it needs convergence, lifting and a regular expansion);
  - rotor superselection.
- **"Checked":** s1 (spectra, characters, positivity on a 16³ grid, bundle jump, static energies), s2 (identities to 5e-15; 1D collision test), s3 (static energies). All in midpoint-symbol models. Face-centred phase details are absorbed into q̂, as in N0914:200-201.
- **Not covered:**
  - the strongly coupled finite-slot phase itself;
  - aliasing and resummation;
  - non-abelian or field-dependent constraint algebras;
  - gapless integrated-out matter;
  - fermions;
  - nonlinear gravity;
  - Λ.
- **Literature points are tool summaries of untrusted pages**, not verbatim checks. The Gu–Wen PDF could not be rendered and was not executed.

## Files (`S/`)

- `scripts/s1_ntype_reduced.py/.out`:
  - extended vs reduced spectra;
  - stabilizer characters;
  - zone positivity;
  - bundle discontinuity;
  - static source;
  - the ladder exponents.
- `scripts/s2_source_consistency.py/.out`: S K = q̂ᵀG and G R = 0 (Lemma T); the 1D collision test (T′).
- `scripts/s3_ladder_static.py/.out`: static scalar-source energy for h:R(h) vs |R(h)|².
- `downloads/GuWen_0907.1203v3.pdf`: untrusted, unrendered, not executed.
