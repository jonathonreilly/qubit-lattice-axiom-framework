# C5 R5-5: the ensemble-only LRL law as a superposition over lattice frames

**Worker.** Claude Opus 5.5 (probe R5-5), the same model family as every C5 worker and the supervisor. **Not refereed.** It reports a FAIL, so it needs the codex referee before anything is recorded. Run 2026-10-12, 14:17Z to about 14:39Z. No repository file was edited. Nothing was downloaded; three web searches were used only to verify citations.

**Scratch** (`scratchpad/C5/R5-5/scripts/`):
- `r55_A_frame_structure.py` → `.out`: how fast R4-1's per-realization deviation changes with the frame. It replays R4-1's frame RNG, checks the frames against the saved η's, and loads R4-1's saved shell sums with `allow_pickle=False`.
- `r55_B_mean_law_stability.py` → `.out`, plus `r55_B2_zero_locations.py` → `.out`: whether the ensemble-mean law is stable. It counts zeros of the mean symbol in the cut plane and locates them.
- `r55_C_which_frame_numbers.py` → `.out`: the which-frame phase one quantum writes, under the stated bridges.
- `r55_D_toy_frame.py` → `.out`: exact finite toy checks of Theorem F, Corollary F′ and the gapped-frame contrast.
- `r55_E_pointwise_check.py` → `.out`: per-frame, finite-ℓ illustration behind Lemma AE.
- `r55_B3_resolution_check.py` → `.out`: contour-resolution recheck of the (B) zero counts.

**Read.** `docs/MINIMAL_AXIOMS_2026-06-29.md` in full; `TESTS.md:2302-2999` (the C5 method, rounds 1–5; R5-5 is at `:2987-2999`); `SUMMARY.md` §§21–22; `C5_R4-1_report.md`, `C5_R4-1_referee.md`; `C5_Q1_report.md`, `C5_Q1_referee.md`; `C5_O4_report.md` §§0–3, `C5_O4_referee.md`; `C5_R4-3_referee.md`; `C5_R5-1_referee_verdict.md` and `C5_R5-1_report.md` §5.3; the R5-2 worker report (unrefereed; its referee is still running); `ROUTES.md:36`.

**Labels.**
- *proved*: complete argument here (same family, unrefereed).
- *proved mod RECALLED*: complete except for named standard theorems.
- *checked*: numerical, in the scratch files.
- *suggested*: argued only.
- *reading*: interpretation.
- *comparator*: outside literature, web-verified where marked, otherwise from memory.

---

## 0. In plain words

- **The idea under test.** One copy of the random-frame lattice (LRL) has no good long-distance wave law (R4-1, refereed). The average over copies does. So put the lattice's frame into a quantum superposition, and hope that only the average law is what we see.
- **Why it does not work.** Matter that lives on the lattice moves by that copy's law in each branch of the superposition. Everything we can measure is made of such matter. So every measured statistic is a **weighted mixture of single-copy predictions**, whatever the frame's phases (Theorem F, proved). The quantum superposition behaves exactly like not knowing which copy we are in.
  - The average law could be what we see only if every copy already predicts the same thing for the states we observe (Corollary F′, proved). In that case the superposition is not needed.
  - This is the frame version of Q1's result for sprinklings (`C5_Q1_report.md:76-86`, refereed).
- **How fast the frame gets "picked".** A propagating quantum whose single-copy behaviour depends on the frame becomes correlated with the frame. Using R4-1's deviation as the coupling, one quantum pins the frame to a tiny neighbourhood, a hyperbolic distance of 1e-27 or less, in every listed experiment. The bridges are stated in §6; the numbers are checked arithmetic. The deviation changes over a frame distance of about 0.4–0.6 (checked).
- **The obstruction then returns in the realized copy, almost surely.** I strengthen R4-1 from a statement about the average of squares over copies to one that holds for **almost every** copy (Lemma AE, proved mod RECALLED). So the copy the frame lands on has the R4-1 obstruction with probability one.
- **Could the frame be held rigid by an energy gap?** In a toy, yes: a gapped frame in its symmetric state makes the matter see the average law (checked). But in any Poincaré-covariant theory the frame's orientation states all carry zero energy-momentum (Lemma P0, proved). So no Poincaré-covariant gap exists. A gap needs a preferred time in the law, which is what LRL was built to avoid.
  - The Bragg gap protects only the frame's *translation* states. Those carry reciprocal-lattice momenta. It does not protect the *orientation* states.
- **The only clean way to make the average law physical is to change what matter is.** The average operator sums the field over whole hyperboloids, so matter must be a field on a continuum (Lemma C, proved). That is set A, with LRL supplying only a non-local kernel.
  - For that version I checked stability. Smooth-profile mean kernels on shells 1–96 have no growing modes in the checked region (checked). The four-shell mean kernels have growing modes with e-folding times of 0.6–0.9 lattice times (checked). This parallels the 4D Benincasa–Dowker (BD) instability (comparator).
- **Records make it permanent.** Once any record forms whose odds depend on the frame, O4's Lemma 1 (with its H0 reading) bounds the frame's coherence for ever. So "undo it later" (Q1's final-state projection, or a tuned joint unitary) is closed after the first frame-sensitive record.
- **Worker reading: FAIL (bounded)** in the stated class (§1, §2).

---

## 1. Against the FIXED readings (`TESTS.md:2996-2999`)

| Clause | Finding | Label |
|---|---|---|
| **PASS:** "the frame stays coherent for all observed propagation (decoherence rate below stated bounds), so the ensemble □ is the observed law, with prices named" | **Not met in the class.** The observed law is a mixture of single-realization laws whatever the frame's coherence (Thm F). The frame stays coherent on a set of frames only if all their laws agree on the observed states (Cor. F′). Then the "ensemble □" is just the common single-realization law, and the superposition does no work. Even at amplitude level the mean propagator E[G_X] is not B̄⁻¹ (§3.4) | proved |
| **FAIL:** "propagation decoheres the frame within observed scales, so per-realization physics, and the R4-1 obstruction, return" | **Met in the class (§2).** (i) Per-realization physics is what is observed: proved (Thm F), with no bridge. (ii) The R4-1 obstruction holds in Haar-almost every realization, so with Born probability one in the realized frame: Lemma AE, proved mod RECALLED. (iii) "Within observed scales": one quantum resolves the frame to d₁ ≤ 1e-27 in every listed experiment, against a frame correlation length of about 0.5 (A). This step is checked arithmetic **under Bridge B1/B2**, which maps R4-1's off-shell operator deviation to on-shell phases | (i) proved; (ii) proved mod RECALLED; (iii) checked given the bridge |
| **INCONCLUSIVE** | Not returned for the class. Outside the class the route is not an independent escape. It reduces to R5-2's open per-realization question, or collapses to set A (Lemma C), or needs a non-Poincaré time (Lemma P0) or a non-unitary/erasure step closed by Record permanence under H0 (§7) | reading |

**Worker reading: FAIL (bounded).** The class:
- frame-diagonal coupling (decomposable over realizations), with orthogonal realization labels, any frame wave-function (the Poincaré-invariant one included), and unitary quantum mechanics for unrecorded degrees of freedom;
- every observable built from matter on the realization (decomposable);
- per-realization law in R4-1's class (fixed, linear, retarded, scalar, finitely many Γ_L-orbits, at least one nonzero off-site orbit).

Step (iii) is conditional on Bridge B. The FAIL's substance is (i) + (ii), and both are bridge-free.

**Against the expectation implicit in R5-2's price (iv)** (`R5-2_report.md:236`). "Ensemble-only law" is **not an independent price** in the decomposable class. It either reduces to price (i) or (iii), or it means matter on a continuum (set A).

---

## 2. Setting and hypotheses (stated before titles)

- **(F1) Realization space.** Y = 𝒫/(Γ_L ⋉ L₇), with 𝒫 the proper orthochronous Poincaré group acting on realizations X = g(L₇ + u) by X ↦ hX. Y carries a finite 𝒫-invariant measure dX, since Γ_L is cocompact in SO⁺(1,3) (R2-2 referee) and L₇ is cocompact in R⁴.
  - The frame Hilbert space is H_F = L²(Y, dX), with orthogonal (δ-normalized) labels |X⟩ and the geometric 𝒫 action.
  - **Orientation sector:** the u-independent functions, H_F⁰ ≅ L²(SO⁺(1,3)/Γ_L).
- **(F2) Frame-diagonal ("decomposable") law.** The joint Hilbert space is the direct integral ∫^⊕ H_M(X) dX, where H_M(X) is the matter space of realization X. The joint evolution is U = ∫^⊕ U_X dX, with U_X the realization-X law. The same holds for CPTP per-realization maps.
- **(F3) Decomposable observables.** Every physically realizable observable or instrument is decomposable over Y. This is automatic when observers, apparatus and records are matter living on the realization under a frame-diagonal law.
- **(F4) Unrecorded degrees of freedom obey unitary QM** (O4's H1, `C5_O4_report.md` §0). Where records are used: O4's H0 reading (record contents orthogonal). The O4 referee marks H0 as a reading, not axiom content (`C5_O4_referee.md:3`).
- **(F5) The per-realization law** is in R4-1's class, as corrected by its referee (`C5_R4-1_referee.md:116-126,151-153`).

**Outside realizations this scope excludes:**
- non-decomposable laws (realization-changing dynamics), §7.1;
- frame Hamiltonians outside the Poincaré generators, §4;
- non-unitary final-state laws, §7.2;
- spacetime-dependent frame fields (polycrystals), §7.4;
- infinite-orbit kernels, which reduce to R5-2 (§7.5);
- curved realizations;
- tensor, spinor and nonlinear operators.

---

## 3. Theorem F: the observed law is a mixture of per-realization laws (proved)

### 3.1 Statement and proof
**Theorem F.** Under (F1)–(F3), let the initial joint state be Ψ₀ = ∫^⊕ ψ(X)χ_X dX, with any complex frame amplitude ψ ∈ L²(Y) and per-realization matter states χ_X. Then for every decomposable observable O = ∫^⊕ O_X and every time:

⟨O⟩ = ∫ |ψ(X)|² ⟨U_Xχ_X | O_X | U_Xχ_X⟩ dX.

This holds equally for multi-time, multi-particle and sequential instruments, provided each is decomposable.

*Proof.* U and O are decomposable, so ⟨Ψ₀|U†OU|Ψ₀⟩ = ∫ |ψ(X)|²⟨χ_X|U_X†O_XU_X|χ_X⟩ dX. The direct-integral inner product is diagonal in X. Sequential instruments compose decomposably. ∎

**Consequences.**
- The phases of ψ are unobservable. A coherent frame superposition and the classical mixture |ψ|²dX give identical statistics for every matter observer. The frame is effectively superselected.
- Q1's Theorem A (`C5_Q1_report.md:76-86`; referee: "exact for orthogonal configuration labels and configuration-diagonal coupling", `C5_Q1_referee.md:5`) is the special case with Poisson configurations and a common H_M.
- For a common H_M with identical initial χ:
  - the matter's reduced state is ρ_M = ∫|ψ|² U_Xρ U_X† dX (Q1 Thm A form);
  - the frame's reduced kernel is ρ_F(X, X′) = ψ(X)ψ*(X′)·D(X, X′), with **D(X, X′) = ⟨U_X′χ|U_Xχ⟩**.
  - Frame decoherence and matter dephasing are therefore one quantity.
  - An interferometer's visibility is the |ψ|²-average of e^{iΔΦ_X}.

**Checked** (`r55_D_toy_frame.out`; 64 frames on the 1+1 analog's quotient circle, a two-arm matter system, random frame phases):
- |ρ_M − mixture| ≤ 6.2e-17 at T = 0.5, 2, 8, 32;
- the visibility equals |E e^{−iΔω T}| to 6 digits (0.846287, 0.320188, 0.188701, 0.109980);
- the frame coherence between u₀ and u₁₆ equals the matter overlap |D| to 6 digits.

### 3.2 Corollary F′: frame coherence is redundant (proved)
- On a set S ⊂ supp ψ the frame stays coherent (|D(X, X′)| = 1 for X, X′ ∈ S and every populated χ) **if and only if** U_X = e^{iθ_X}U on the populated subspace, for all X ∈ S.
  - *Proof.* Equality in Cauchy–Schwarz gives U_Xχ = e^{iθ_X(χ)}U_X′χ. Applying this to χ₁ + χ₂ forces θ_X to be the same for all populated χ. ∎
- In that case every per-realization law already gives the observed law U, and the frame superposition contributes nothing.
- In every other case the matter carries which-frame information, and the observed law is the mixture (Thm F).
- **So no frame superposition in this class turns a failing per-realization law into a working one.**

### 3.3 Prior art (counted once)
- `ROUTES.md:36` (F1a, frozen random sites): "Ensemble-only protection is not viable: per realization there is a random TT tadpole and stiffness…". Same structure, different substrate.
- Lemma H (R5-1, refereed, `C5_R5-1_report.md:184-198`): frame-picking cannot be restored by invariant averaging. Here the invariant state on Y exists (finite volume), but Thm F shows that averaging over it is only a mixture.

### 3.4 The "ensemble □" is not even the amplitude-level law (proved identity, formal)
- In the class, the matter's mean amplitude is E[U_X]χ (for sourced fields, E[G_X]J), the mean of propagators.
- R4-1's ensemble □ is B̄ = E[B_X], the mean of operators.
- With Δ_X = B_X − B̄ and E Δ_X = 0:

  E[G_X] = B̄⁻¹ + B̄⁻¹ E[Δ_X B̄⁻¹ Δ_X G_X]

  This is the standard second-order self-energy term. It vanishes only if Δ_X B̄⁻¹Δ_X G_X averages to zero. Since R_ℓ ≫ 1 at observed ℓ, the series is not even perturbative.
- So "the mean law is observed at amplitude level", as in RL2's Poisson mean, does not hold for B̄ either.

---

## 4. Lemma P0: no Poincaré-covariant gap protects the frame (proved); the gapped toy (checked)

**Lemma P0.** On H_F = L²(Y):
- (a) Translations act on the Fourier component e^{iG*·u} (G* ∈ L₇*) of a frame function as multiplication by e^{−i(gG*)·a}.
  - The orientation sector (G* = 0) carries **P^μ = 0 exactly**.
  - The translation sector carries 4-momenta gG* on the hyperboloids Q*(G*) ≠ 0, so |q²| ≥ (2π)²/(7a²), which is the Bragg gap.
- (b) The only 𝒫-invariant vector is the constant. Translation invariance forces G* = 0, and SO⁺(1,3) acts transitively on G/Γ_L.
- (c) So in any Poincaré-covariant joint dynamics, where time evolution is the time-translation P⁰, every orientation state is degenerate with the invariant frame state: P⁰ = 0 on all of H_F⁰.
  - Transitions from the invariant state to orientation-excited states, which are exactly the which-frame correlations, cost no energy-momentum. They are kinematically open at every matter energy.
  - A frame Hamiltonian with a gap above the invariant state cannot be a Poincaré generator. It is a preferred time.

*Proof.* (a) X + a = g(L₇ + u + g⁻¹a). Then Fourier-expand in u ∈ R⁴/L₇. (b), (c) follow directly. ∎

**Reading.**
- The Bragg gap that silences in-band scattering (R2-2) protects the frame's translation sector: an umklapp needs q = gG*.
- It gives no protection to the orientation sector, where the R4-1 deviation lives (it is a function of the observer's lattice-frame velocity u).
- Which-frame writing is "forward", with q = 0: elastic dephasing.

**Contrast, the gapped toy (checked, `r55_D_toy_frame.out` part (3)).** Add H_F = E_F(1 − |c⟩⟨c|), with |c⟩ the invariant state. This is not a Poincaré generator, by Lemma P0. Then the matter sees the **mean law** plus the second-order shift −s²Var(ε)/E_F, and the frame stays in |c⟩.
- E_F = 30: visibility 0.9989, frame fidelity 0.9992, relative phase 2.9756 against the mean-law-plus-second-order value 2.9755.
- E_F = 10: phase 2.2963 against 2.2928.
- E_F = 0: visibility 0.110, fidelity 0.023.
- This is the only mechanism found that makes the average law physical with the frame coherent (adiabatic elimination; comparator: Born–Oppenheimer and motional narrowing). Its price is a gapped, non-Poincaré frame dynamics, i.e. a law-level preferred time.

---

## 5. Lemma AE: R4-1's obstruction holds in almost every realization (proved mod RECALLED)

**Statement.** For R4-1's class (F5) and Haar-almost every u ∈ 𝒳 = Γ_L∖H³:

limsup_{ℓ→∞} |Δ_ℓ(u)|/ℓ > 0, possibly +∞, hence limsup_ℓ R_ℓ(u)·(a/ℓ)³ > 0.

So if decoherence selects the frame with a Born law |ψ|²dX, which is absolutely continuous, then the realized frame has the obstruction **with probability one**. This answers the R4-1 referee's caveat that the theorem is "not a proof that every realization …" (`C5_R4-1_referee.md:126`) up to a null set.

**Proof.**
1. **Finite Dirichlet polynomials.** f has finite support, so each D_j(s) = Σ_m f_m Ψ_j(m)m^{−s} is a finite Dirichlet polynomial. The Mellin representation of R5-2 §2.2 (closed form checked there to 1e-11; worker, unrefereed) then gives c_j(ℓ) as residue terms at s = ½ ± ir_j/2 − k plus a remainder.
   - Its leading term is R4-1's referee-confirmed additive asymptotic (`C5_R4-1_referee.md:71-78`).
   - Its coefficient carries Γ(½ + ir_j/2), with |Γ(½ + ir/2)| = (π/cosh(πr/2))^{½} ~ √(2π)e^{−πr/4}.
2. **Uniform convergence.** RECALLED: sup-norm |ψ_j|_∞ ≲ r_j on a compact 3-orbifold, and Weyl's law #{r_j ≤ R} ~ cR³. Then |A_j| ≤ Σ_m |f_m|m^{−½}|Ψ_j(m)| ≲ r_j, a finite sum of point values. So Σ_j |ψ_j(u)|·|lead_j| < ∞ uniformly in u.
   - Hence, for each u, Δ_ℓ(u)/ℓ equals a uniformly convergent trigonometric series in t = ln 2ℓ (a Bohr almost-periodic function), plus finitely many threshold (ℓ log ℓ) or exceptional (ℓ^{1+τ}) terms, plus o(1).
3. **Eigenfunction coefficients.** Group by distinct eigenvalue. The coefficient of e^{irt} at u is κ_r·E_r(u), with E_r := Σ_{r_j=r} A_jψ_j and κ_r ≠ 0.
   - E_r is a Laplace eigenfunction, real-analytic on the orbifold (RECALLED: elliptic regularity, applied locally on the Γ-cover).
   - If E_r ≢ 0, its zero set has Haar measure zero.
4. **Some coefficient is nonzero.** R4-1 (iv), referee-confirmed (`C5_R4-1_referee.md:104-116`), gives a tempered j with A_j ≠ 0, so E_{r_j} ≢ 0.
5. **Conclusion.** Outside that null set the almost-periodic part has a nonzero Bohr coefficient, so it does not tend to 0 (RECALLED: Bohr mean value). Any threshold or exceptional term with a nonzero coefficient at u only increases the growth. ∎

**Finite-ℓ illustration (checked, `r55_E_pointwise_check.out`).** Take R4-1's own frames (48 at η ≤ 1, 30 at η ≤ 0.6) and kernels {1,2,3,4} and {1,2,4,7}. Then max over ℓ ∈ [6, 19 or 24] of |B_gφ − B̄φ|/ℓ has a minimum over frames of 1.8, 0.20, 10.5 and 0.83, against medians of 7.3, 0.94, 14.1 and 1.4. No frame falls below 1% of the median. This is consistent with Lemma AE, which is asymptotic; it does not test it.

**Scope.**
- It is an off-shell operator statement on R4-1's Gaussian family, exactly R4-1's own form.
- The torsion points are assumed harmless, as in R5-2 §2.3 and R4-1's referee §4.4.

---

## 6. How fast propagation picks the frame

### 6.1 Frame correlation length of the deviation (checked, `r55_A_frame_structure.out`)
- The structure function is SF(d) = ⟨(ε(u) − ε(u′))²⟩/(2Var ε), with ε R4-1's relative deviation. It is computed from R4-1's own frames (48 at η ≤ 1, 30 at η ≤ 0.6; frames replayed and asserted against the saved η's).
- **Results:**
  - SF(d < 0.25) = 0.15–0.44 (η ≤ 1 sample) and 0.39–0.75 (η ≤ 0.6 sample).
  - SF reaches about 1 (0.8–1.9) by d ≈ 0.5–1. The pattern is the same across the 4-shell {1,2,3,4}, 4-shell {1,2,4,7} and smooth L = 2, 3 kernels at ℓ = 4–24.
  - Fitted ξ_F (SF ≈ (d/ξ_F)² for d < 0.5): 0.46–0.63 and 0.34–0.45 in the two samples.
- **Reading.** The deviation is dominated by low automorphic modes. For d ≪ ξ_F the rms difference between frames is ≈ √2 R_ℓ d/ξ_F ≈ 3R_ℓ d.
- **Caveats:** H³ distances are upper bounds on quotient distances, and the samples are local balls (R4-1 referee §3).

### 6.2 Bridges (stated; not derived)
R4-1's deviation is an off-shell operator test, "not yet a direct observable" (`C5_R4-1_referee.md:54`).
- **B1 (massless, eikonal).** A quantum of wavenumber k (ℓ = 1/k) acquires the branch-phase difference Φ(d) ≈ 3dR_ℓ·kcT/2.
  - **Caveat:** Lemma Z (refereed) makes any *regular* null per-realization dispersion Lorentz-invariant (`C5_R4-3_referee.md:25-27`). If photons have a regular per-realization dispersion, they write no which-frame phase this way, and the B1 rows drop out.
- **B2 (massive, rest-frame phase).** Φ(d) ≈ 3dR_{λ_C}·Mc²τ/(2ħ), with ℓ = λ_C, summed over constituents. The timelike, mass-like sector is exactly the one Lemma Z leaves open (`C5_R4-3_referee.md:27`).
- **Inputs:** R_ℓ = P(ℓ/a)³, with P from R4-1's measured prefactors: 4-shell 4.2, smooth L = 3 2.0e-3, flat L = 4 5.9e-4. These are finite-window, log-periodic fits, and R4-1's theorem is a limsup.

### 6.3 Numbers (checked arithmetic, `r55_C_which_frame_numbers.out`)
d₁ is the frame distance resolved by one quantum (Φ = 1 rad).

| quantum | a = ℓ_P, flat L=4 | a = ℓ_P, 4-shell | a = 1e-19 m, flat L=4 |
|---|---|---|---|
| optical photon, 1 m arm (B1) | 7.5e-88 | 1.1e-91 | 1.8e-40 |
| optical photon, 1 Gpc (B1) | 2.4e-113 | 3.4e-117 | 5.8e-66 |
| electron, 1 ns (B2) | 1.1e-76 | 1.5e-80 | 2.5e-29 |
| neutron, 0.1 ms (B2) | 3.6e-75 | 5.1e-79 | 8.5e-28 |
| Cs-133, 70 s (B2) | 3.9e-83 | 5.4e-87 | 9.2e-36 |
| 25 kDa molecule, 7 ms (B2) | 2.1e-81 | 2.9e-85 | 4.9e-34 |

- Every entry is ≥ 27 decades below ξ_F ≈ 0.5. One quantum leaves the frame localized far inside the region where per-realization physics is constant, so "per-realization physics returns" at once.
- The R_{λ_C} values for a nucleon (1e54–1e58 at a = ℓ_P) mean the single-realization law has no nucleon-like mass shell at all. That is R4-1's obstruction restated on-shell through B2.
- **Illustration only** (R4-1's P ∝ L^{−4.5} fit over L ≤ 4; extrapolation barred, `TESTS.md:5-9`). For one quantum *not* to resolve frames 0.5 apart, the kernel scale would have to be ℓ_k ~ 1e-18 to 1e-15 m. For the gamma-ray and Cs rows that is ≳ the quantum's own scale, where the bridge fails.
- **Comparator** (web-verified: Pikovski, Zych, Costa, Brukner, Nat. Phys. 11, 668 (2015), arXiv:1311.1095). In time-dilation decoherence the branch phase rate per unit rest energy is gΔx/c² ≈ 1e-22 (Δx = 1 µm). Here, under B2, it is 3R_{λ_C}d ≈ 4e54 per unit frame distance (nucleon, a = ℓ_P, flat kernel).
  - The mechanism is the same: proper-time phases record a variable. Diósi's frame-dependence critique (arXiv:1507.05828, seen in search results) has a direct analogue here: the "which-frame" variable is relational (u).

---

## 7. Escapes outside the class (trying to make it work)

### 7.1 Non-decomposable law: the mean operator acting on matter. Lemma C: collapses to set A (proved)
- B̄φ(x) = cφ(x) + Σ_m g_m ∫_{H_m⁺} φ(x − v)dμ_m(v), with H_m⁺ the future hyperboloid.
- For B̄ to act on fields over a configuration set S, S must contain x − H_m⁺ (μ_m-a.e.) for each x ∈ S and each m with g_m ≠ 0.
- Then S ⊇ x − (H_m⁺ + H_m⁺), and H_m⁺ + H_m⁺ = {v future timelike, −v² ≥ 4m} is open.
- So S contains open sets: matter must live on a continuum, never on one realization's countable point set.
- **Reading:** "only the frame-averaged law is physical" means set A (continuum matter field) with LRL entering only as a Lorentz-invariant non-local kernel supported on discrete proper-time shells. This is a causal-set-type non-local continuum theory (comparator: Belenchia–Benincasa–Liberati; Aslanbeigi–Saravani–Sorkin).
- **Stability of that mean law** (checked, `r55_B_mean_law_stability.out`, `r55_B2_zero_locations.out`). A growing mode of (B̄ − μ²)φ = 0 is a zero of B̄(z) − μ² for z = p² in C∖(−∞, 0]; the forward tube maps onto this cut plane.
  - **Four-shell mean kernels: unstable.**
    - Argument-principle counts in 1e-5 < |z| < 1e4 are 14, 4 and 16 zeros for {1,2,3,4}, {1,2,4,7}, {2,3,5,6}. They are independent of δ (1e-6, 1e-3), of μ² ∈ {0, 1e-4, 1e-2}, and of contour resolution (20k and 60k points per segment, `r55_B3_resolution_check.out`).
    - The located zeros include w₀ = √z₀ = 1.594 ± 5.396i ({1,2,3,4}), an e-folding time of 0.63a.
    - On the real axis z = κ² > 0 there is no sign change: B̄ < 0 throughout. The instability is complex, as for 4D BD (web-verified: Aslanbeigi, Saravani, Sorkin, JHEP 06 (2014) 024, arXiv:1403.1622: evidence that the original 4D causal-set d'Alembertian is unstable and the 2D one stable).
  - **Smooth-profile mean kernels on shells 1–96** (f = e^{−m/L²}·cubic, L = 2, 3; finitely supported, like R4-1's own smooth families): **no zeros** in 1e-5 < |z| < 1e6 (count 0.000 at R = 1e4 and 1e6, and at 60k points per segment). Stable in the checked region. Near 0, h ≈ −z − μ²; at large |z|, h → c ≠ 0.
  - Only the cut-plane criterion was checked. Real-axis zeros off the mass shell (extra real poles or ghosts) were not examined.
- **Price (named, not adopted).** Set A's price (a continuum base) plus the choice of a smooth kernel. Discreteness then survives only as the shell structure of a non-local kernel.

### 7.2 Final-state projection or tuned erasure. Closed by Record permanence once a frame-sensitive record forms (proved under H0)
- Projecting the frame back onto ψ gives E[U_X]χ, with success probability 1 − E‖U_Xχ − EUχ‖². This is Q1's Theorem B identity (`C5_Q1_report.md:118`) with X in place of P.
  - With branch states nearly orthogonal (§6), the probability is ≈ the mean overlap, i.e. tiny.
  - The output is the mean propagator, not e^{−iH̄t} (§3.4).
- **Record link.**
  - Suppose any record forms whose distribution depends on the frame, p_X ≠ p_X′. Then O4's Lemma 1 (refereed with H0 as hypothesis, `C5_O4_referee.md:3`) bounds the frame coherence: |ρ_F(X, X′)| ≤ |ψψ*|·BC(p_X, p_X′).
  - "Records are permanent" (`MINIMAL_AXIOMS_2026-06-29.md:79-80`) makes the bound hold for ever.
  - So recombination and tuned erasure are excluded after the first frame-sensitive record.
  - Under the B2 numbers, every recorded measurement involving massive matter is frame-sensitive. That last step is conditional on the bridge.
- **Open:** a world in which every record is exactly frame-blind. By Cor. F′ that needs every single-realization law to agree on everything recorded.

### 7.3 Quantum reference frames (comparator; reading)
- In the QRF formalism (web-verified: Giacomini, Castro-Ruiz, Brukner, Nat. Commun. 10, 494 (2019), arXiv:1712.07207), a "superposition of frames" is a change of perspective: physics is covariant under quantum frame changes.
- Here the R4-1 deviation is already relational. It depends on u, the observer's velocity relative to the lattice, which is invariant under global 𝒫.
- So a superposition of lattice frames, seen from the lattice, is a superposition of lab velocities. It supplies no average over the law, only a mixture over u (Thm F).
- Bartlett–Rudolph–Spekkens (RMP 79, 555 (2007), from memory): bounded-size frames only add decoherence.

### 7.4 Spacetime-dependent frame fields: polycrystal or motional narrowing (suggested; outside)
- If the frame varies over a correlation length ξ, phases could random-walk and narrow, with dephasing ~ Lk²ξε(ξ)².
- **Obstacles:**
  - a Lorentz-invariant random frame field with compact domains is problematic: correlations along the light cone extend to arbitrary Euclidean distance (cf. Bombelli–Henson–Sorkin, `C5_R5-1_report.md:93`);
  - grain boundaries are defects that bring back RZ-type random noise (R3-3 defect model, `TESTS.md:2770-2772`).
- Not tested.

### 7.5 Infinite-orbit kernels: reduce exactly to R5-2
- By Cor. F′, the frame superposition helps iff the per-realization law already works on observed states.
- So for R5-2's open infinite-orbit class, R5-5 adds nothing. Its prices (i) and (iii) stand (`R5-2_report.md` §7), and (iv) is not independent.

---

## 8. Relation to Q1, O4 and R5-1

- **Q1** (refereed CWC; FAIL proved for orthogonal labels, configuration-diagonal coupling and fixed Poisson weights, `C5_Q1_referee.md:5,13`).
  - Thm F is the same identity, generalized to a direct integral of matter spaces and to all decomposable instruments.
  - The differences:
    - the LRL "noise" is a smooth automorphic function of the frame, not white;
    - the realization space is a finite-volume homogeneous space with a unique invariant state;
    - Q1's noise-free route (a positive-energy vacuum cannot absorb spacelike momentum, `C5_Q1_report.md:202-218`) has the *opposite* sign here. Orientation excitations need zero momentum, so they are always open (Lemma P0).
- **O4.** Lemma 1 (V ≤ BC) is used in §7.2 with the frame as the system and records as the which-way detector. Permanence turns frame selection into an irreversible fact.
- **R5-1.** Lemma H (no frame-picking state is restored in law) is compatible: the invariant state on Y exists, but it is observationally a mixture (Thm F).

## 9. Scope, hypotheses, outside realizations; strong words

**Proved:**
- Thm F and Cor. F′ (any frame amplitude, decomposable class);
- Lemma P0;
- Lemma C;
- the §3.4 identity (formal: assumes the inverses exist).

**Proved mod RECALLED:**
- Lemma AE (sup-norm, Weyl, analyticity of eigenfunctions and nodal sets, Bohr almost-periodic theory, plus R5-2's Mellin closed form, which is unrefereed but checked there).

**Checked:**
- toy identities (D);
- frame correlation length (A);
- mean-law cut-plane zero counts and locations (B, B2): five kernels; the smooth-profile ones are finitely supported on m ≤ 96 (R4-1's construction), not infinite-orbit kernels;
- arithmetic (C).

**Conditional:** §6 numbers, on Bridges B1/B2.

**Outside, open:**
- non-decomposable laws other than B̄-on-continuum;
- non-Poincaré frame dynamics;
- exactly frame-blind record sets;
- polycrystal frames;
- infinite-orbit kernels (= R5-2);
- curved, tensor, spinor and nonlinear operators;
- the on-shell form of R4-1's deviation (B1/B2).

**Strong words.**
- "Every" and "whatever the phases" are used only inside Thm F's decomposable class.
- "No Poincaré-covariant gap" applies to the geometric frame representation (F1).
- "With probability one" is for Born laws absolutely continuous with respect to Haar (ψ ∈ L²).
- "Unstable" and "stable" in §7.1 refer to cut-plane zeros in the checked |z| ranges only.
- Fitted values (ξ_F, P) are finite-window and log-periodic; read them as orders of magnitude.

## 10. Prior art (counted once)

- **Repository grep** (docs/ and the packet; 14:35Z): "Pikovski", "superposition of frames", "frame superposition", "superposed frame", "Anderson tower", "Giacomini", "time dilation decoher": no hits.
  - "quantum reference frame": one unrelated hit (`docs/work_history/.../CYCLE18_NOTE_2026-07-14.md:657`, Głowacki, operational frames).
  - "ensemble-only": `ROUTES.md:36` (F1a: ensemble-only protection not viable per realization) and the C5 R3-1, R4-1 and R5-1 scope lists.
- **Packet results used:**
  - R4-1 and its referee (coupling and spectral expansion);
  - Q1 (Thm A/B structure);
  - O4 (Lemma 1, H0);
  - R4-3 referee (Lemma Z scope);
  - R5-1 (Lemma H);
  - R2-2 (Bragg gap, cocompactness);
  - R5-2 (worker; Mellin closed form, price list).
- **Comparators:**
  - web-verified: Pikovski et al. 2015; Diósi arXiv:1507.05828 (title seen only); Giacomini et al. 2019; Aslanbeigi–Saravani–Sorkin 2014;
  - from memory: Bartlett–Rudolph–Spekkens 2007; Anderson-tower / spontaneous-symmetry-breaking decoherence of order parameters (van Wezel–van den Brink–Zaanen 2005); Belenchia–Benincasa–Liberati non-local field theory from causal sets; Bohr almost-periodic functions; Hörmander sup-norm bounds.

## 11. Prices (named; none adopted)

- **P-F1 (set A collapse).** Matter is a continuum field whose law is the LRL mean operator B̄ (Lemma C). Requires a smooth kernel: the four-shell mean laws are unstable at the lattice rate; the smooth ones are stable in the checked region.
- **P-F2 (gapped frame).** A frame Hamiltonian outside the Poincaré generators (Lemma P0): a law-level preferred time. This contradicts the reason for LRL (O1, R2-2).
- **P-F3 (non-unitary recombination or erasure).** Q1's final-state costs. Closed after the first frame-sensitive record, by Record permanence (under H0).
- **For set B′ (LRL):** price (iv) of R5-2 is withdrawn as an independent escape in the decomposable class. What remains is R5-2's (i) (infinitely many arithmetic identities) or (iii) (a mesoscale), or a move to set A.

## 12. Needs codex referee

1. Thm F and Cor. F′ in the direct-integral form: the decomposability assumption (F3) and whether it is the right reading of "only the frame-averaged law is physical".
2. Lemma P0: the translation action on L²(Y), and P⁰ = 0 on the orientation sector.
3. Lemma AE:
   - uniform convergence of the leading series (sup-norm and Weyl);
   - use of R5-2's Mellin form for finite support;
   - the nodal-set and Bohr step;
   - torsion points.
4. Lemma C (support and open-set generation).
5. The B/B2 zero counts. Contour resolution: 20,000 points per segment. Check that the smooth-profile kernels have no zeros near the cut at |z| > 1e6, and whether the infinite-support versions behave the same.
6. Whether Bridges B1/B2 are acceptable, or whether FAIL should rest on (i) + (ii) alone.
7. The reading: FAIL (bounded), the class as in §1.
