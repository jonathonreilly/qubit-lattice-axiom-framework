# C5 R19-23 report: are the five Ward-violating cone rows physical observables or prescription artefacts?

**Author and provenance.** Claude Opus 5.5 probe (same model family as the supervisor and every C5 worker). Unrefereed. Run 2026-10-13, 06:12Z to about 06:40Z. I edited no repository file and downloaded nothing.

**Paths.** `P/` = `.claude/science/exercises/gravity-current-state-20261009/`; `AX` = `docs/MINIMAL_AXIOMS_2026-06-29.md`; `N0914` = `docs/LOCAL_FINITE_CLOCK_TENSOR_CONSTRAINTS_CUBIC_DISPERSION_AND_LINEAR_GRAVITY_BOUNDARIES_BOUNDED_THEOREM_NOTE_2026-09-14.md`; `S/` = `scratchpad/C5/R19-23/` (this folder); `vR19-19` = `scratchpad/C5/ref_R19-19/REFEREE_VERDICT.md` (appeared during my run).

**Machine use.** `OMP_NUM_THREADS=2`; every run under 3 s.

**What I read.** `AX` in full. `P/TESTS.md`: the C5 method (`:2302-2319`); my item (`:8221-8250`); the entries and verdicts for R9-9 (`:3862-3872`, `:3939-3950`), R13-5 (`:4668-4683`, `:4707-4716`), R16-5 (`:5130-5155`, `:5325-5335`, `:5437-5447`), R17-4 (`:5816-5849`, `:5940-5954`, `:6171-6178`), R19-5 (`:7319-7350`, `:7470-7487`, `:7747-7752`), R19-15 (`:7828-7858`, `:7995-8006`, `:8127-8132`) and R19-19 (`:8008-8046`, `:8133-8143`). `P/agents/C5_R19-19_report.md` in full; `vR19-19`; `P/agents/C5_R9-9_report.md` in full and `C5_R9-9_referee_verdict.md`; `P/agents/C5_R19-15_report.md` (§§0-2) and its verdict. `N0914:40-150`.

**Runners rechecked before use (checked).**
- `P/scripts/C5/R19-19/r1919_gauge.py` (copied to `S/arch19_19/`): output byte-identical to the archive (`r1919_gauge_recheck.out`).
- `P/scripts/C5/R9-9/r99_graviton.py` (copied to `S/arch9_9/`): output identical except the runtime line (`r99_graviton_recheck.out`).
- My shared module `S/kernels.py` rebuilds R19-19's invariant kernel space with the same construction and seed. It reproduces the rows of R19-19's controls: explicit degree-0 tensors lie in the invariant span to ≤ 3.4e-15 and give the expected rows (`r1923_modes.out:1-6`). The EH kernel annihilates gauge directions to 1.8e-15 (`r1923_isolation.out:10`), and its TT block is exactly ω² − q² after normalization (`r1923_isolation.out:2-9`).

**Labels.** proved (complete argument under stated hypotheses; unrefereed) / checked (numerics run here) / suggested (argued, not proved) / reading (interpretation) / comparator (outside reference) / RECALLED (from memory, not verified).

---

## 0. In plain words

1. **Which gauge group (proved; agrees with vR19-19 Finding 1).** R9-9's N-type graviton keeps N0914's vector constraint G_j and its *local* scalar constraint S at every site. Their transformations are spatial diffeos and the time-diffeo action on E (`N0914:56-58`), and R9-9 changes only the derivative symbol (`C5_R9-9_report.md:83`). So the group is the **full** linearized-diffeo group, non-projectable. By Lemma G (confirmed exactly, `vR19-19` item 1), five independent row combinations are Ward violations:
   - μ_E;
   - μ_T2;
   - Ξ_Eg − Ξ_T2g;
   - face2 − Ξ_T2g;
   - face1 − (3Ξ_Eg + Ξ_T2g)/4 (R17-4's K₆ term).

2. **Main result: four of the five are exact pole data of the full theory, whatever the gauge completion (Lemma I; proved by representation theory; checked).**
   - For q along a cubic axis, the 10 components of h_μν split under the little group C₄ᵥ as 4A₁ + B₁ + B₂ + 2E. h_xx − h_yy (E_g TT) is the only B₁ member; h_xy (T₂g TT) is the only B₂ member.
   - For q along a face diagonal (C₂ᵥ), the split is 5A₁ + A₂ + 2B₁ + 2B₂, and face2 = h_ab is the only A₂ member.
   - No gauge direction (p_μξ_ν + p_νξ_μ) lies in B₁, B₂ or A₂.
   - So for **any** O_h × T-covariant response Π(ω, q), the full quadratic action is exactly block-diagonal on these polarizations. This holds whether or not Π is Ward-exact, local or truncated.
   - Their poles are exactly ω² − q² = εΠ_ee(ω, q), with ε = 2/M². This is independent of gauge fixing, Stückelberg completion, constraint projection and field redefinitions, and these modes couple to conserved TT stress.
   - Hence:
     - μ_E and μ_T2 are TT pole masses², m² = εμ;
     - Ξ_Eg − Ξ_T2g is a polarization splitting of the speed along the axes (GW birefringence);
     - face2 − Ξ_T2g is a direction dependence of the T₂g branch's speed.
   - Checked on random kernels: decoupling to ≤ 5.6e-16 (`r1923_isolation.out:13-16`); the coupling tables match the irreps (`:18-40`).
   - **These four rows are PHYSICAL.**

3. **face1 is different (checked).**
   - face1 = h_aa − h_bb shares A₁ with h₀₀, h₀ₙ, h_nn, h_aa + h_bb and with two gauge directions (ξ₀, ξₙ).
   - When Π violates the Ward identity, the face1 pole coefficient is **not** the face1 row. It is the Schur complement of Π over the two A₁ gauge directions, on shell.
   - Six random degree-2 kernels: exact roots of det Q agree with the Schur formula to ≤ 7e-5 relative. They differ from the row by 9–65% and from (3Ξ_Eg + Ξ_T2g)/4 as well (`r1923_modes.out:11-22`).
   - So R17-4's face1 entry (and the K₆ term inside it) is a component of the observable, not the observable itself. It enters the pole with unit coefficient (the Schur correction involves only off-diagonal and gauge-block entries), so it does change a gauge-invariant observable.
   - The physical face1 anisotropy is generically nonzero. Its value for the actual U/UD/VW vertices is **OPEN**, because the non-TT A₁ components of the vacuum response were never computed.

4. **Extra modes (checked in stated classes; suggested beyond).** The answer depends on which Ward violation is present.
   - **Shear rows alone, in "solid" form** (a spatial elastic tensor with no h₀μ terms; this is what a translation-invariant vacuum gives after its one-point part is removed, suggested in §3.3):
     - the kernel keeps an exact residual time-diffeo invariance (`r1923_modes.out:33`);
     - lapse and shift stay Lagrange multipliers (rank Q₂ = 6);
     - there are exactly **2** propagating branches, both with positive norm, at all six (ε, q) points (`r1923_modes.out:31-49`). The same holds with a FULL-Ward degree-2 part added (`:52-77`, inside the EFT range).
     - This is the Lorentz-violating "m₀ = 0" phase, not Fierz–Pauli (comparator, RECALLED: Rubakov 2004; Dubovsky 2004).
     - **No vDVZ discontinuity:** U/U_GR → 1 linearly in m²/q² for mass–mass and mass–light sources (4 laws × 2 directions, `r1923_static.out:11-46, 50-86`). For an isotropic shear mass the static potential is exactly GR (`:20-28`). Deviations are confined to r ≳ 1/m.
   - **Degree-2 (speed-row) Ward violations:** every sample in the generic, momentum-conserving ("class R") and auxiliary-Goldstone classes has extra branches.
     - In class R they are the **time-diffeo Goldstone π⁰**, a scalar graviton: its eigenvectors are pure gauge directions dominated by ξ₀ (non-gauge residual ≤ 1.2e-7, `r1923_static.out:185-200`).
     - Its dispersion is ε-independent. Its stability depends on the sample:
       - one sample is stable, with ω² = 0.42q²;
       - others are tachyonic or complex, with ω² ∝ q, i.e. growth ∝ √q.
     - Its coupling to conserved matter is suppressed: O(ε) relative to the graviton at fixed q (`r1923_static.out:90-99`).
     - Some of these pencils are ill-conditioned, so the stability statements are **suggested**, not class-wide.
5. **Reading: PHYSICAL (worker).**
   - Four rows enter exact, invariant pole positions.
   - The fifth enters the invariant face1 pole, which must replace the row.
   - None is removable by field redefinition or gauge choice.
   - The claim is class-wide (any covariant kernel), so it needs the referee.
   - Reading (ii) fails: the bill does **not** drop to one row by reinterpretation.

---

## 1. Class, hypotheses, exclusions (stated before any title)

- **Theory (R9-9's setting at linear order).**
  - Quadratic symbol: Q(ω, q) = (M²/2)K_EH(ω, q) − Π(ω, q) on the 10 components of h_μν.
  - K_EH is the linearized Einstein–Hilbert kernel, equal to R9-9's N-type in its box, where d(q) = q (`C5_R9-9_report.md:81-96`).
  - Π is the vacuum response, an O_h × T-covariant kernel; R19-19's rows are its Taylor data (`C5_R19-19_report.md:62-69`).
  - Normalization: s·e·K_EH·e = ω² − q² for TT e with e:e = 2, so the TT pole is ω² = q² + εΠ_ee with ε = 2/M² (= 16π at a = ℓ_P; `C5_R9-9_report.md:118-120`).
  - Matter couples as h_μνT^μν with exactly conserved T (exact W1, R19-5 verdict, `TESTS:7747-7750`).
- **Lemma I hypotheses.** Π(ω, q) is any symmetric kernel covariant under O_h × T (P, T even). No polynomial or locality assumption is made, and it holds at any order in derivatives.
- **Numerical class.** The 32-dimensional local invariant kernel space through degree 2 (6 + 26; Lemma G's space, `vR19-19` item 1). Within it:
  - "solid": degree 0 = λ_b(tr h)² + μ_E P_E + μ_T2 P_T, with no h₀μ terms;
  - FULL-Ward degree 2;
  - generic;
  - class R: B^{0νρσ,00} = 0 (no ω² terms in any component with a time index; 23 of 26 dimensions, `r1923_modes.out:334`), with the ω² block on spatial components negative definite (spectral positivity; R9-9 Theorem T step 1, `C5_R9-9_report.md:127`);
  - the auxiliary-Goldstone class (Goldstone quadratic form independent of ω; 17 of 26 dimensions) and the G ≡ 0 class (9 of 26), both in `r1923_goldstone.out:1-12`.
- **Method.**
  - Unitary gauge, with no gauge fixing when Π breaks the Ward identity.
  - Residual invariances are detected and fixed: h₀₀ = 0 for ξ₀, h₀ᵢ = 0 for ξᵢ; roots at ω = 0 are dropped.
  - Exact quadratic eigenvalue problem Q₀ + ωQ₁ + ω²Q₂ (the symbol has degree ≤ 2).
  - Norm sign v·∂_ωQ·v at each real root (TT has +).
  - Static amplitudes T·Q(0, q)⁻¹·T against GR's pseudo-inverse value (GR check: U_ml/U_mm = 2 exactly, `r1923_static.out:9-10`).
- **Excluded.**
  - Nonlinear orders and graviton self-interaction.
  - Finite temperature and FRW.
  - The actual non-TT components of Π_vac for U/UD/VW (never computed; §3.3).
  - Body-diagonal propagation (there the TT pair is an E irrep that shares E with the vector sector, so a Schur complement is needed as for face1; not computed).
  - Roots with |ω| ≳ 1/a. These lie outside the degree-2 EFT; the spurious |ω²|/q² ≳ 1e9 roots in the `.out` files are of this kind.

## 2. Prior art (each counted once)

- **R19-19 + vR19-19.**
  - Lemma G confirmed exactly: under FULL Ward only the line (1, 1, 1, 1, 0, 0) is allowed.
  - "Five rows" means five independent combinations; R9-9 uses the full group (`vR19-19` item 1).
  - The (S\*\*) reading is TAUTOLOGY-OR-CONFLICT. The scoped bill is 4 per class / 10 per species / 2 q²-correlated (`vR19-19` items 3, 5).
  - The pre-crossover tachyon is conditional, among other things on a missing "canonical graviton-mass bridge" (`vR19-19` item 4).
- **R9-9 + verdict.** The N-type box graviton, exact at tree level; Theorem T; the narrow mass FAIL; "general ultralocal polarization-dependent seagulls can cancel the mass split" (`TESTS:3939-3950`).
- **R13-5 + verdict.** W2 is blocked ("the pair terms vanish from H, P and K"), so no gauge-invariant pole split was computed (`TESTS:4707-4716`).
- **R16-5 / R17-5 / R17-8 (W15).** No W2_pf completion for finite-band local matter (`TESTS:5437-5447`; vR17-5 at `TESTS:6179-6197`).
- **R19-5 + verdict.** Exact W1 ≠ W2; exact W1 completions exist for massive species (`TESTS:7747-7752`).
- **R19-15 + verdict.** The shear rows are the full uniform-strain Hessian of the lowest-state energy, so the lattice vacuum is an elastic solid. (S\*) gives STRUCTURAL-ZERO by stipulation (`TESTS:8127-8132`).
- **R17-4 + verdict.** The face1/face2 identities and the K₆ term (`TESTS:6171-6178`).
- **R19-11 verdict.** The SM shear residuals are "catastrophic only if they are identified with a canonically normalized physical graviton mass" (`TESTS:7992`).
- **Comparators (RECALLED).**
  - Fierz–Pauli mass: 5 polarizations and the vDVZ discontinuity. A non-FP mass adds a 6th, ghost mode (Boulware–Deser).
  - Lorentz-violating mass terms m₀²h₀₀² + 2m₁²h₀ᵢ² − m₂²h_ij² + m₃²h_ii² − 2m₄²h₀₀h_ii: with m₀ = 0, only the TT modes propagate, with no ghost and no vDVZ discontinuity (Rubakov 2004; Dubovsky 2004).
  - Gravitons in a solid medium acquire a mass from its shear modulus (solid inflation, Endlich–Nicolis–Wang).
  - The Stückelberg / Arkani-Hamed–Georgi–Schwartz effective field theory of a broken diffeomorphism group.

---

## 3. Results

### 3.1 (a) Which gauge group (proved)

- N0914 imposes G_j = ∂ᵢE_ij and S = tr R(h). They Poisson-commute, and their transformations are h → h + sym∇α and E → E + (ΔI − Hess)β (`N0914:52-58`).
- These are the linearized-ADM spatial-diffeo and Hamiltonian-constraint actions, with four local gauge parameters and lapse/shift as multipliers. That is the full, non-projectable linearized-diffeo group.
- R9-9 keeps every identity when q̂ → d(q) (`C5_R9-9_report.md:83`).
- This agrees with `vR19-19` item 1 and with R19-19's reading (`C5_R19-19_report.md:182`).
- **Caveat (proved, short).** With matter whose second-order coupling is not Ward-complete (W15), the constraints cannot all be imposed consistently, because the total Hamiltonian does not commute with them. The consistent linear theory is the unitary-gauge (or Stückelberg) one analysed below.
- The TT results of §3.2 do not depend on this choice: TT components at q ≠ 0 commute with G and S, so constraint projection does not touch them.

### 3.2 (b) Which rows change gauge-invariant observables

**Lemma I (isolation). Proved by representation theory; checked.**
- **Axis q.** The little group of p = (ω, qẑ) in O_h is C₄ᵥ. The 10 components of h_μν decompose as follows:
  - A₁: h₀₀, h₀z, h_zz, h_xx + h_yy;
  - B₁: h_xx − h_yy;
  - B₂: h_xy;
  - E: (h₀x, h₀y) and (h_xz, h_yz).
- **Face-diagonal q (C₂ᵥ).** With frame (n, a, b):
  - A₁: h₀₀, h₀ₙ, h_nn, h_aa, h_bb;
  - A₂: h_ab;
  - B₁: h₀a, h_na;
  - B₂: h₀b, h_nb.
- The gauge directions p⊗ξ + ξ⊗p transform as ξ: A₁ ⊕ E (axis) and 2A₁ ⊕ B₁ ⊕ B₂ (face). None lies in B₁, B₂ (axis) or A₂ (face).
- By Schur's lemma, any covariant Q(ω, q) is block-diagonal, and the multiplicity-1 blocks are scalars.
- **Checked** (generic 32-parameter kernels, 20 draws, random (ω, |q|)): ‖Qu − (u·Qu)u‖ ≤ 5.6e-16 and u·(gauge directions) = 0 for E_g, T₂g and face2. For face1 the mixing is O(1) (2.8e-1) (`r1923_isolation.out:13-16`). The coupling tables reproduce the irreps (`:18-40`).

**Consequences (proved).** The exact propagator component in each isolated polarization is 1/[(ω² − q²) − εΠ_ee(ω, q)], and its pole is a physical branch coupled to conserved TT stress.
- **μ_E, μ_T2.** At q → 0 along an axis, ω² = εμ_E (B₁) and εμ_T2 (B₂). These are TT pole masses, canonically normalized up to an O(ε) wave-function factor. In R9-9's normalization m²a² = 16πμ at a = ℓ_P.
- **Ξ_Eg − Ξ_T2g.** The two TT polarizations along an axis have c² − 1 = εΞ_Eg and εΞ_T2g. Their difference is velocity birefringence.
- **face2 − Ξ_T2g.** A₂ along (110) and B₂ along (001) are both T₂g-type TT polarizations, so their difference is a direction dependence of that branch's speed.
- **Not removable (proved, short).** Pole positions are invariant under invertible field redefinitions. Gauge transformations act trivially on these blocks (no gauge direction lies in them). A constraint projection leaves them unchanged (§3.1). The ARTEFACT clause therefore fails for these four rows.

**face1 (checked; formula proved at first order).**
- In A₁, K_EH(ω = q) has a 3-dimensional null space: TT face1 plus the two gauge directions ξ₀ and ξₙ. The other two A₁ directions have O(q²) entries.
- First-order degenerate perturbation theory then gives the pole shift as the Schur complement:

  δ(ω²) = ε[Π₁₁ − Π₁G Π_GG⁻¹ Π_G1] at ω = q, with G = {ξ₀, ξₙ}.
- **Checked** (6 random Ward-violating degree-2 kernels, ε = 1e-6 and 1e-7, q = 1e-2; `r1923_modes.out:11-22`):

| trial | exact pole Ξ_face1 | Schur | row face1 | (3Ξ_Eg + Ξ_T2g)/4 |
|---|---|---|---|---|
| 0 | −0.96301 | −0.96301 | −1.50259 | −1.77580 |
| 1 | −1.62867 | −1.62867 | −0.98435 | −0.90871 |
| 2 | +2.76710 | +2.76711 | +3.21807 | +2.10576 |
| 3 | +0.49885 | +0.49885 | +0.44309 | +0.35578 |
| 4 | +0.89321 | +0.89321 | +0.81569 | +0.88098 |
| 5 | +2.03065 | +2.03065 | +1.80988 | +2.20497 |

- The Schur correction is quadratic in the A₁ Ward-violating entries Π₁G, so it vanishes for Ward-exact kernels.
- **Mass analogue (checked).** For the solid kernel, the face-diagonal A₁ TT branch has m² = 0.889ε. Compare the row (3μ_E + μ_T2)/4 = 0.9ε, with μ_E = 1 and μ_T2 = 0.6 (`r1923_modes.out:33-35`: ω²/q² = 9.8929 against 10). So a graviton mass measured along (110) depends on direction even as q → 0. This non-analyticity is the signature of instantaneous (auxiliary) Goldstones (reading).
- **Reading for face1.** The K₆ term enters the invariant face1 pole with unit weight, so it changes an observable. But the observable is the Schur-completed number, which also needs Π_vac's A₁ off-diagonal components. Those were never computed for U, UD or VW (R17-4 and R19-19 evaluate TT components only). Its value for the root laws is OPEN.

### 3.3 (a)/(c) Propagating modes and their coupling to matter

**Why the realistic shear block is "solid" (suggested).**
- With exact W1, T^{0ν}(q = 0) are the conserved H and P. The lowest state is their eigenstate, so connected bubbles with an h₀ν leg vanish at q = 0 for every ω.
- The remaining h₀ν terms at degree 0 are one-point (seagull/tadpole) expectations. (S), P-Tad or (S\*\*) remove them.
- A constant lapse is an exact time rescaling of a continuous-time lattice law, so its second-order response is the one-point term alone.
- What remains at degree 0 is R19-15's elastic tensor (Lemma H, `TESTS:8128`).

**Mode counts (checked; `r1923_modes.out`).**

| class | residual gauge | branches with \|ω\| < 1/a (per q, ω > 0) | norms | ε-scaling |
|---|---|---|---|---|
| S1 solid only (`:31-49`) | ξ₀ exact | 2 (the TT pair, massive) | + + | ω² − q² ∝ ε |
| S2 solid + FULL-Ward degree 2 (`:52-77`) | ξ₀ exact | 2 | + + | same |
| S3 generic degree 2 (`:79-`) | none | 2 TT + up to 8 extra | mixed; complex roots | extra ω²/q² ε-independent |
| S7 class R + solid (`:336-`) | none | 2 TT + π⁰ branches | sample-dependent | extra ε-independent |
| auxiliary / G ≡ 0 classes (`r1923_goldstone.out`) | none | 2 TT + extra | mixed | ill-conditioned (root sets change with (ε, q)) |

- **Proved (short) for S1.** A^{0νρσ} = 0 means the ξ₀ directions (which change only h₀₀ and h₀ᵢ) are exact null directions. The spatial Goldstones πᵢ get only gradient terms A(∂π, ∂π) = q_iq_k A^{ijkl}π_jπ_l and no ω terms, so they are auxiliary.
- **Checked** (S1/S2): exactly two finite branches at six (ε, q) points, both with positive norm.
- **Class R extra branches (checked).**
  - They are the time-diffeo Goldstone: eigenvectors are gauge directions with |ξ₀| dominant and an ξₙ admixture of 0.19–0.26 (`r1923_static.out:185-200`).
  - Sample 1: a stable branch ω² = 0.4176q² (+ norm), plus a complex pair ω² ≈ q²(21.6 ± 743i) at q = 1e-2.
  - Sample 2: tachyonic, ω² = −838q² at q = 1e-2 and −8580q² at q = 1e-3, i.e. ω² ∝ −q.
  - Sample 3: complex, ω² ∝ q.
  - The unstable rates scale as √(qa)/a.
- **Coupling to conserved matter (checked, real branches).** For sample 1's stable π⁰ branch, the residue |T·v|²/|v·∂_ωQ·v| maximized over unit conserved T is:
  - 1.0e-3 at ε = 1e-5 and 1.3e-5 at ε = 1e-7 (q = 1e-2);
  - against 97–100 for the TT pair (`r1923_static.out:90-99`).

  That is O(ε) relative to the graviton at fixed q, as the Stückelberg power counting predicts. Unstable branches would grow from the vacuum regardless of that coupling.
- **Reading.**
  - The Fierz–Pauli expectation ("Ward violation ⇒ extra polarizations") is **wrong for the shear rows** in their realistic form: they give a massive TT pair and nothing else, the m₀ = 0 phase (comparator).
  - Extra modes come from the **degree-2** Ward violations, the same ones that carry Ξ_Eg − Ξ_T2g, face2 − T₂g and K₆. In class R they form a scalar time-diffeo Goldstone with O(1) speed.
  - Whether the true vacuum's π⁰ is healthy is decided by non-TT components of Π_vac that no C5 runner computes. **OPEN, and a candidate new wall** (suggested).

**Static potential (checked; `r1923_static.out:8-86`, `:138-183`).**
- Mass–mass and mass–light amplitudes for static sources at q ∥ z and q ∥ (110).
- For four solid laws, U/U_GR = 1 − c·(ε/q²) with c = O(1). For example, 0.979677 / 0.999797 / 0.999998 at ε/q² = 1e-2 / 1e-4 / 1e-6 (`:11, :14, :17`). Light-to-mass ratios are equally continuous.
- **No vDVZ discontinuity.** Isotropic shear (λ_b = 0, μ_E = μ_T2) gives exactly GR at every q, including m²/q² = 100 (`:20-28`).
- Class R plus solid behaves the same way: 0.843 / 0.9984 / 0.99998 at ε/q² = 0.1 / 1e-3 / 1e-5.
- The modification is an IR effect at r ≳ 1/m. Its form depends on the bulk term and on μ_E − μ_T2 (reading).

### 3.4 (d) Bill consequences (reading)

- **Reading (ii) fails.** The bill does not drop to one row by reinterpretation. Four rows are invariant pole data, and the fifth enters an invariant pole. The physical bill is the one already on record:
  - route A: 11 equalities + window + CC (vR19-12);
  - under (S\*\*): 4 per class / 10 per species / 2 q²-correlated, with (S\*\*) ruled TAUTOLOGY-OR-CONFLICT (`vR19-19` items 3, 5).
- **Correction 1: the face1 row is mis-specified.** It must be its Schur completion over (ξ₀, ξₙ).
  - A placement law that zeroes R17-4/R18-13's diagonal face1 row (w_d, w_o) does not zero the physical face1 speed unless the A₁ Ward mixing Π₁G also vanishes.
  - The count is unchanged (one row), but the R18-13 / R19-12 face1 payments are conditional on the uncomputed A₁ block.
- **Correction 2: the shear rows are canonical TT pole masses** (in the N-type + solid class, flat space, zero temperature, linear order).
  - This supplies the zero-temperature part of the "canonical graviton-mass bridge" that vR19-11 (`TESTS:7992`) and `vR19-19` item 4 called missing.
  - It strengthens R19-19 §3.6 / R19-21's pre-crossover concern, conditional on finite temperature and FRW (not computed). Count it once with R19-21.
- **New candidate wall: Goldstone health** (suggested, not a FAIL).
  - If the speed rows are paid by tuning their TT values while the gauge-block Ward violation remains, the π⁰ branch persists, and its stability is a set of sign conditions (inequalities, not equalities).
  - Under (S\*\*) the defect moves to O(p⁵) (`C5_R19-19_report.md:200`). The Goldstone form then starts at O(p⁶), but its dispersion is set by ratios of coefficients, so its sign conditions persist at any finite subtraction order.
  - Only an exact (non-local, P-R19-15b) Ward completion removes it. This is consistent with vR19-19 item 3's "residual higher-order Bianchi defect".
- **Observable translation of the rows (comparators RECALLED).**
  - μ → the graviton-mass bound (LVK, about 1e-23 eV).
  - Ξ splittings → GW birefringence and speed bounds (GW170817 Δc/c ~ 1e-15 applies to each observed polarization).
  - Unpaid sizes (per species at a = ℓ_P, ~1e-3–1e-2 in c²) remain excluded, as on record.

### 3.5 Prices (named, not adopted)

- **P-R19-23a (new, conditional): the A₁ completion.** The face1 bill row must be paid as the Schur-completed pole. This needs the non-TT A₁ components of each stress vertex's vacuum response, i.e. a stated seagull for h₀₀, h₀ₙ and h_nn.
- **P-R19-23b (new, conditional): π⁰ health.** If degree-2 Ward violation survives in the gauge block, the scalar time-diffeo Goldstone's dispersion must be stable (sign conditions; zero numbers if satisfied).
- No axiom text changes. Dynamics, stress and gravity bridges are downstream (`AX:116-123,187`).

---

## 4. Against the FIXED readings (`TESTS:8246-8249`)

| reading | clause | status |
|---|---|---|
| **PHYSICAL** | the five rows change gauge-invariant observables (polarization-dependent speeds, masses, or extra modes) | **met.** μ_E, μ_T2: TT pole masses. Ξ_Eg − Ξ_T2g: axis birefringence. face2 − Ξ_T2g: direction-dependent T₂g speed. All are exact invariant poles (Lemma I, proved). face1/K₆: enters the invariant face1 pole with unit weight, but the row must be replaced by its Schur completion (checked). Degree-2 Ward violations also bring extra π⁰ branches (checked in samples) |
| | checked | yes (`r1923_isolation.out`, `r1923_modes.out`, `r1923_static.out`) |
| | refereed if class-wide | **class-wide (any covariant kernel), so a referee is needed** |
| **ARTEFACT** | removable, or absent from every gauge-invariant observable at linear order | fails: none of the four isolated rows is removable (pole invariance; no gauge direction in their irreps); K₆ shifts the invariant face1 pole |
| **OPEN** | otherwise | not the outcome. The face1 *value* and π⁰ health are open sub-items |

**Worker reading: PHYSICAL**, with two corrections:
- face1 must be Schur-completed;
- extra modes arise from the degree-2 (not the degree-0) Ward violations.

**Against the expectation (`TESTS:8250`).**
- **Holds:** "PHYSICAL … the bill stands".
- **Does not hold:** "Fierz–Pauli logic". The shear rows give masses without extra polarizations and without vDVZ (the m₀ = 0 phase).
- **New wall:** "a ghost" is not found for the masses. The candidate new wall is instead the π⁰ Goldstone from the speed-row Ward violations, whose stability is sample-dependent and undetermined for the true vacuum.

## 5. Strong-word check

- **"Exact"** is used only for:
  - the block-diagonality of isolated irreps (Schur's lemma; numerically ≤ 5.6e-16);
  - the residual ξ₀ invariance of solid kernels.
- **"Proved"** is used for:
  - the gauge-group identification;
  - Lemma I and its consequences;
  - the first-order Schur formula;
  - S1's auxiliary Goldstones.

  All are short and unrefereed.
- **"Checked"** is used for:
  - the six face1 trials;
  - the mode counts at the listed (ε, q) points;
  - the static ratios;
  - the class-R Goldstone content and couplings.

  The ill-conditioned classes (auxiliary, G ≡ 0, part of S3) support only "extra branches appear"; their stability details are **not** claimed.
- **"No vDVZ"** holds in the solid and class-R samples tested. It is not a universal theorem.
- **"Realistic shear block = solid"** is suggested (W1 + vacuum eigenstate + one-point subtraction), not derived for U/UD/VW.
- **Not claimed:**
  - the actual face1 value or π⁰ stability for any root law;
  - finite temperature or FRW;
  - nonlinear orders;
  - body-diagonal rows.

## 6. For the referee

1. **Lemma I.** The irrep decompositions (C₄ᵥ: 4A₁ + B₁ + B₂ + 2E; C₂ᵥ: 5A₁ + A₂ + 2B₁ + 2B₂) and the absence of gauge directions in B₁, B₂ and A₂. Is "exact invariant pole" correct when T is not in the little group at ω ≠ 0? (It is not needed: C₄ᵥ and C₂ᵥ alone suffice.)
2. **The face1 Schur formula.** Degenerate perturbation theory on the null space {TT, ξ₀, ξₙ} of K_EH(ω = q); `schur_face1` in `r1923_modes.py`.
3. **The S1 mode count and the "solid" argument** (h₀ν terms are one-point only).
4. **The static-amplitude normalization** (GR mass–light/mass–mass ratio = 2, `r1923_static.out:9`) and the no-vDVZ statement.
5. **Whether the π⁰ instabilities in random class-R samples are artefacts** of the degree-2 truncation (ω² ∝ q branches reach |ω| ~ 0.2/a at q = 1e-2).

## 7. Files (`S/`)

- `kernels.py`: R19-19's invariant space (same seed), the EH kernel, the 10×10 symbol, gauge directions, rows.
- `r1923_isolation.py` → `.out`: Lemma I checks and coupling tables.
- `r1923_modes.py` → `.out`: face1 pole vs Schur vs row; mode counts S1–S7 (class R).
- `r1923_static.py` → `.out`: static amplitudes and vDVZ test; branch couplings; Goldstone content.
- `r1923_goldstone.py` → `.out`: Goldstone-form subspaces (G ≡ 0, auxiliary) and their row images; mode counts.
- `arch19_19/` (`r1919_gauge_recheck.out`, identical) and `arch9_9/` (`r99_graviton_recheck.out`, identical except runtime).
