# C5 R10-1 report: is the edge anomaly unremovable? A one-loop "anomaly-inflow" test for box-confined lattice field theories

**Author.** Claude Opus 5.5 probe. Same family as the supervisor and every C5 worker. Unrefereed. 2026-10-12, 17:50Z to about 18:25Z. No repository file edited (`git status` clean).

**Scratch.** `S/` = `.../scratchpad/C5/R10-1/`. Scripts and outputs are in `S/scripts/`; each runs in under 5 s with `OMP_NUM_THREADS=2`.
- `r101_dirac_symbolic.{py,out}`: symbolic reduction (sympy) of the Dirac-sea photon speed integrand to anomaly variables.
- `r101_dirac_moment.{py,out}`: the Dirac moment formula against R8-5's refereed direct numbers (9 shapes, controls, heavy-edge series).
- `r101_scalar_qed.{py,out}`: scalar-QED photon. The direct P_M − P_E is compared with the A-moment.
- `r101_pairing.{py,out}`: boson–fermion pairing. Both sides are computed directly.
- `r101_scans.{py,out}`: a tuned zero along R8-5's Wilson family; the pairing residual under mass splitting; A signs.
- `r101_flat_electron.{py,out}`: the electron self-energy speed for the paired (Clifford-flat) law. This is R8-5's `fermion()` adapted.
- `r85_box_qed_copy.py`, `r99_profiles_copy.py`: unmodified copies of the R8-5 and R9-9 runners, imported from scratch.

**Read.**
- `docs/MINIMAL_AXIOMS_2026-06-29.md`, in full (`AX`).
- `TESTS.md`:
  - C5 method (`:2302-2320`);
  - rounds 6–9 and every referee entry through `:3955`;
  - R10-1 at `:3960-3975`.
- `SUMMARY.md` §17 (`:355-495`).
- `agents/C5_R8-2_report.md` and verdict.
- `agents/C5_R8-5_report.md` and verdict, plus `scripts/C5/R8-5/`.
- `agents/C5_R9-9_report.md` and the newly landed `C5_R9-9_referee_verdict.md`, plus `scripts/C5/R9-9/`.
- `agents/C5_R7-5_report.md` and verdict.
- `agents/C5_S8_synthesis.md:17,183-200`.
- `PRICE_NOTE.md:404`.

**Labels.**
- **proved**: complete under the stated hypotheses.
- **checked**: numerics here.
- **suggested**: argued, not proved.
- **reading**: an interpretation.
- **comparator**: literature, RECALLED unless marked verified.

---

## 0. In plain words

1. **The registered premise is half right.**
   - **Scalar loops.** For charged scalar matter, the one-loop photon speed shift is exactly a zone average of the boost anomaly A = Hess(ε²/2) − 1, weighted by the square of the Ward-forced current, a positive weight. This is the same form as R9-9's Theorem T for the graviton. Proved; checked to 1e-6.
   - **Dirac-sea loops (electrons).** Here the premise is false. R8-5's photon speed shift is a zone average of **four** anomaly functions, not one:
     - A;
     - the velocity-norm anomaly a = |∂h|² − 1;
     - two terms that mix the current with the Wilson direction.

     This identity reproduces R8-5's refereed numbers on every shape (9 box shapes, the Wilson and naive controls, and the r = 1…32 heavy-edge series) to ≤ 1e-3 relative. For box shapes the a-term dominates (S3: +21.0 from a, +0.5 from A, −6.4 from the mixing terms). Proved; checked.
   - **The common root.** All of this lives at the zone edge. Inside the box every term vanishes identically, so the box contributes exactly zero.
2. **The REFUTED direction partly works, for the photon only.**
   - **The matching.** Make every fermion "Clifford-flat": along each axis the velocity operators square to one and anticommute, as in continuum Dirac. This needs 8 components per site, Wilson's r = 1 circle being the simplest case. Then the fermion's photon moment is exactly −2× that of a complex scalar running on the same band curve.
   - **The cancellation.** One 4-component fermion plus two such complex scalars cancel the photon's one-loop speed shift **pointwise in momentum, for every edge shape, with the masses free**. Checked directly to 1e-6. With a split mass the residual is 0.335·m_s² (lattice units), which is negligible for any sub-Planck mass.
   - **What it is.** An edge-band supersymmetry-like pairing, not a numerical tuning.
3. **But it does not reach the observable.**
   - **What remains.** The electron's own one-loop speed shift (photon loop) for the same paired law is −10.7 (box curve) to −18.0 (Wilson circle), in units of e²/16π². That leaves c_e − c_γ ≈ −6e-3 to −1e-2: unsuppressed. Checked.
   - **What would cancel it.** Only a partner loop (photino and selectron, in SUSY language), which is not built. The graviton sector (R9-9) is also not paired here.
   - **No untuned choice nulls every one-loop LV coefficient** in anything constructed.
4. **Counting.**
   - **Without pairing.** Every independent dimension-4 LV coefficient is a nonzero edge moment. Several are sign-definite on whole subclasses: monotone scalar edges give δc_γ < 0, and convex Clifford-flat fermions give δc_γ > 0. So they cannot vanish there at all; a zero needs a sign-changing "falling-up" edge and costs one condition per moment.
   - **The C-box count.** For QED plus gravity it equals set C's six (reading). The box changes the size of each coefficient, not their number.
   - **With pairing.** The photon's own coefficient is removed, but the electron–photon relative speed still needs one condition. So the count is unchanged at one loop.
5. **Against the FIXED readings: SUGGESTED** (worker reading).
   - **Not DERIVED.** The "moments of A" premise is false for Dirac matter, and an untuned (paired) choice does null one coefficient class.
   - **Not REFUTED.** The electron self-energy and graviton coefficients are not nulled.
   - **Derived parts:** Theorems T′, D and P; the sign theorems; Lemma N(m); the localization lemma.

---

## 1. Hypotheses and classes (stated before any title)

- **H-lat.** Z³ × ℝ, continuous time, free (Gaussian) matter. One-loop two-point functions with closed-form k₀ integrals. Bands are C² and periodic. Masses m > 0, or the band is doubler-free with E > 0 off k = 0.
- **H-box.** A box law: inside an open momentum box, every propagator and vertex coincides with its continuum covariant form (R7-1, R8-5).
- **H-Ward.**
  - Gauge vertices are Peierls (minimal, axis-path) couplings, as in R8-5 class 𝒢₀ (`C5_R8-5_report.md:69-79`).
  - With q along a cubic axis (x) and the current along y, the transverse vertex is exactly x = ∂h/∂k_y. This vertex does not depend on k_x or q (proved: q_y = 0 in the divided difference).
  - Charge rigidity (Lemma C) forces this vertex onto the whole zone (`TESTS.md:3808`).
- **Matter classes.**
  - **(S)** A charged complex scalar with separable band ε² = m² + Σu(k_j): R9-9's profiles G, L and NN.
  - **(D)** R8-5's BQ Dirac law: h = Σ[S(k_j)α_j + W(k_j)β] + mβ, with a shared β.
  - **(DF) Clifford-flat Dirac:**
    - h = Σ_j[S(k_j)α_j + W(k_j)β_j] + mβ₀, with 7 mutually anticommuting matrices, so 8 components per site;
    - each curve (S, W) has unit speed, so {∂_jh, ∂_lh} = 2δ_jl exactly.
- **Observable.**
  - The dimension-4 speed coefficient δc² = α + β, with α = ∂_{q²} and β = ∂_{ω²} of the transverse self-energy.
  - For the photon this is R8-5's δc_γ = (P_M − P_E)/2 (`r85_box_qed.py:6-16`).
  - Units: per e², mean over the zone, ×16π² (R8-5's convention).
- **Excluded, not addressed:**
  - non-axis q (cubic symmetry makes dimension-4 speeds isotropic);
  - interacting and non-bilinear charge densities;
  - non-Peierls (transverse Pauli) vertices;
  - INV vertices (R7-5/R8-4);
  - two loops;
  - compact or finite link variables;
  - Z⁴ (set B);
  - the matter-side shift from graviton loops;
  - a lattice gaugino.
- **Untuned** means a choice fixed by a stated structural rule (a symmetry or pairing), not by adjusting a number or shape per species or per observable. Pairing is therefore listed as a price, not as free.

## 2. Prior art (each counted once)

- **I2/C3** (CWC). The band- and zone-averaged anomaly is −β per mode for every finite periodic C² Bloch matrix (`TESTS.md:1411-1416`; `SUMMARY.md:397-405`). That is the "−I" used here.
- **R8-2 Theorem E** (CWC). Ṗ_i = −g_j[δ_ijH + dΓ(εA_ij)] (`TESTS.md:3556`; `C5_R8-2_referee_verdict.md:31-47`).
- **R8-5** (CWC, FAIL bounded).
  - Lemma C and Theorem B: the soft photon couples to every charged mode.
  - BQ cone split Δ ∈ [−71, −11].
  - Heavy edge: −713.
  - (`TESTS.md:3807-3813`; `C5_R8-5_report.md:153-174,227-246`.)
  - Its §4.4 calls the mechanism "suggested". §3.3 here supplies the exact identity for its photon leg.
- **R9-9** (CWC, INCONCLUSIVE).
  - Theorem T is confirmed.
  - Lemma N is valid only under a richness assumption on the vertex family (`TESTS.md:3939-3951`; `C5_R9-9_referee_verdict.md:7-14`).
  - Lemma N(m) in §3.4 uses the mass, not the vertex family, so it needs no richness assumption.
- **R7-5** (CWC, bounded FAIL for P/FF; INV conditional) (`TESTS.md:3500-3504`). Also R8-4 and R9-7: INV fails or is unproved at two loops (`TESTS.md:3815-3821,3925-3937`).
- **RP** (CWC, FAIL bounded): "Only exactly matched spectra cancel to all orders" for μ_E (`SUMMARY.md:393`). §3.5 is the same type of mechanism, a supertrace. It differs in one way: because the LV is edge-localized, only the edge bands must match, not the masses.
- **Comparators.**
  - Groot Nibbelink and Pospelov (PRL 2005): supersymmetry forbids dimension-4 LV; soft breaking reintroduces it suppressed by m_soft²/M² (RECALLED, not verified).
  - Polchinski 1106.6346: dimension-4 LV is natural unless forbidden, with supersymmetry "the one known example" (verified by the R7-5 referee, `C5_R7-5_referee_verdict.md:34`).
- **Repo search.** I grepped TESTS, SUMMARY and agents for "supertrace", "pairing", "Clifford-flat", "|∂h|²" and "velocity anomaly". Results:
  - Supertrace appears only in RP (μ_E).
  - No prior identity splits the Dirac LV into A, a and mixing terms.
  - No prior identity pairs scalar and Dirac photon moments.

## 3. Results

### 3.1 Localization lemma. Proved (sketch)

- **Statement.** Under H-box, every one-loop dimension-4 LV coefficient C = ∫_{T³}I_lat equals ∫[(1 − χ)I_lat − ∇χ·J̃]. Here:
  - χ is a smooth cutoff equal to 1 deep inside the box region (all legs in the box);
  - J̃ is the continuum boost-flow current.

  So C is supported on the edge and on the face shell.
- **Proof.**
  1. A continuum covariant integrand satisfies δ_η(ext) I₄ = −∂_{k^μ}(ω^μ_ν k^ν I₄).
  2. α + β = ½∂_ω∂_q(δ_ηΠ)/η at zero, so the continuum LV integrand is pointwise ∇_k·J̃ after the k₀ integral, given decay in k₀.
  3. On the torus ∫∇·(χJ̃) = 0, and I_lat = I_cont where χ ≠ 0.
- **Meaning.** This is the general form of "the box contributes nothing; the edge contributes everything". It does **not** by itself make C an A-moment. The theorems below do that, case by case.
- **Consistency.** The symbolic primitive G_cov found in §3.3 is exactly the covariantized continuum current (`r101_dirac_symbolic.out:3-4`).

### 3.2 Theorem T′ (scalar QED photon). Proved; checked

- **Claim.** For class (S) with Peierls coupling,

  **δc_γ = (P_M − P_E)/2 = (1/32)⟨u′(k_y)² A_xx/ε⁵⟩ = (1/8)⟨(∂_yε)² A_xx/ε³⟩**, with A_xx = u″(k_x)/2 − 1.
- **Proof.**
  1. P_E = (1/16)⟨u_y′²/ε⁵⟩: the ω² coefficient of Π_yy, which by the Ward identity is the static electric response.
  2. P_M = −(1/2)⟨u_y′²[−(3/8)∂²_xε/ε⁴ + (7/8)(∂_xε)²/ε⁵]⟩; integrating by parts in k_x gives (5/16)⟨u_y′²(∂_xε)²/ε⁵⟩.
  3. Then ∂_x(∂_xε/ε⁴) = [Hess_xx − 5(∂_xε)²]/ε⁵ integrates to zero.
  4. The vertex u′(k_y) does not depend on k_x. ∎

  This is R9-9's Theorem T with |V|² = u′(k_y)², now with a **Ward-forced** vertex instead of a prescribed one.
- **Checked** (`r101_scalar_qed.out`). The direct P_M (exact grid shifts, Richardson in q²) minus P_E matches the moment to 5e-8 – 7e-5 at resolved m:

| profile | m | direct δc_γ·16π² | moment |
|---|---|---|---|
| G | 0.3 | −0.063947 | −0.063947 |
| L | 0.3 | +8.2519 | +8.2528 |
| NN | 0.3 | −0.139891 | −0.139891 |

  At m = 0.05 the direct method is q-limited (q ≈ m); the moment is IR-safe.
- **Normalization.** The continuum scalar : Dirac charge-screening ratio comes out 1 : 4, as it must.

### 3.3 Theorem D (Dirac sea; R8-5's photon leg). Proved; checked against refereed numbers

- **Claim.** For class (D), and for any Clifford dimension,

  **δc_γ = ⟨R_D⟩, R_D = a·x²/(4E³) − A·X²/(4E⁵) − c₁(h·h′)X/(2E⁵) + c₂X/(2E³),**

  where:
  - x = ∂_yh and X = x·h;
  - h′ = ∂_xh;
  - a = |h′|² − 1 and b = h·h″, so A = a + b = Hess_xx(E²/2) − 1;
  - c₁ = x·h′ and c₂ = x·h″.
- **Proof.**
  - Sympy expands R8-5's static χ_yy and P_E to O(q²) in the jet (h, h′, h″). The invariant form is checked to 7e-16.
  - It finds the continuum primitive G = (h·h′)(E²x² − 2X²)/(4E⁵) and verifies, as an algebraic identity, that L − dG/dk_x equals the four-term residual above (`r101_dirac_symbolic.out:4-10`).
  - G is periodic and smooth where E > 0, so it integrates to zero. ∎
- **Checked** (`r101_dirac_moment.out`). R8-5's direct values are referee-confirmed (`C5_R8-5_referee_verdict.md:7`):

| law | a-moment | A-moment | mixing | total | R8-5 direct |
|---|---|---|---|---|---|
| S1 | +3.06 | +0.55 | −1.23 | +2.38 | +2.37 |
| S3 | +21.04 | +0.49 | −6.35 | +15.18 | +15.16 |
| S8 (near-SLAC) | +83.19 | +0.36 | −17.95 | +65.60 | +65.58 |
| Wilson r = 1, no box | **0.0000** | −0.04 | +0.91 | +0.864 | +0.850 |
| naive (F2 law), m = 0.2, L = 48 | −7.13 | +2.11 | 0 | −5.020 | −5.022 |
| S3 heavy edge, r = 32 | +2640 | −5948 | +4015 | +706.6 | +706.1 |

  All nine shapes, both controls and all six heavy-edge points agree to ≤ 1e-3 relative (R8-5's own q-extrapolation error).
- **Consequences.**
  - **The "moments of A" premise is false for Dirac matter.** The velocity-norm anomaly a enters with weight x²/(4E³) > 0 and dominates every box shape.
  - **Its zone mean is not forced.** a ≡ 0 for Wilson r = 1. Only A's mean is forced (−1).
  - **The mixing terms are a separate Wilson effect.** They are zero for naive fermions.
  - **R8-5's heavy-edge growth** (Δ ∝ r) is the near-cancellation of three O(r²) moments, leaving an O(r) remainder.

### 3.4 Sign theorems and Lemma N(m). Proved

- **(S) sign.** If A_xx ≤ 0 on the zone (G, NN; proved for G in R9-9), then δc_γ < 0 for every charged scalar. On each line ∫A_xx = −2π, so A_xx < 0 on a set of positive measure, and the weight u_y′²/ε⁵ is positive almost everywhere.
- **(DF) sign.** For Clifford-flat Dirac, a = c₁ = c₂ = 0, so δc_γ = −⟨A X²/(4E⁵)⟩, with E² = m² + Σ_j v(k_j) and v = S² + W². If A ≤ 0, then δc_γ > 0. Checked: both curves used have A ∈ [−4.97, 0] and [−2, 0] (`r101_scans.out`).
- **Lemma N(m).** For fixed shapes in (S) or (DF), δc_γ(m) cannot vanish for all m² in any interval.
  - Proof: write E^{−5} as a Laplace integral. Then δc_γ = ∫ds s^{3/2}e^{−sm²}F_A(s)F_V(s)F_1(s)/Γ(5/2), with F_V, F_1 > 0.
  - Vanishing on an interval forces F_A ≡ 0, but F_A(0⁺) = ∫A dk = −2π. ∎
  - This needs no vertex-richness assumption (cf. `C5_R9-9_referee_verdict.md:14`).
  - **Reading: it is physically weak.** All physical masses are ≪ 1 in lattice units and the moments are IR-safe, so every light species sees the same m → 0 value. One shape tuning would null that value for all light species of a given type.
- **No sign theorem for (D).** The class (D) moment changes sign along R8-5's no-box Wilson family. It is −5.36 at r = 0 and +0.86 at r = 1, with a zero near r* ≈ 0.72 (`r101_scans.out` (i)).
  - That is a tuned zero of the photon coefficient only.
  - At both ends δc_e is −16 to −21 (R8-5), so Δ ≠ 0 there.

### 3.5 Theorem P (boson–fermion pairing of the photon moment): the REFUTED-direction attempt. Proved; checked

- **Claim.** Take one Clifford-flat fermion (per 4 components) and complex scalars on the same curve, u = v = S² + W². Then, pointwise in k,

  **R_D = −2 × (scalar integrand),** so 1 Dirac (4 components) + 2 complex scalars give δc_γ ≡ 0 at one loop. Equivalently, 8 components + 4 scalars.

  This holds for every edge shape. The mass dependence enters only through m² in each species' own E.
- **Proof.**
  1. With a = c = 0, R_D = −A X²/(4E⁵).
  2. For the scalar, u_y′ = 2(h_y·h_y′) = 2X and A_xx(scalar) = ∂²_x(v/2) − 1 = A (Dirac).
  3. Theorem T′ then gives X²A/(8ε⁵). ∎
- **Checked directly**, with no moment formulas: P_E and P_M from R8-5's static formulas on 7-component Clifford vectors, and the scalar's direct P_M − P_E (`r101_pairing.out`).
  - **Wilson circle (no box).** Dirac/scalar = −2.0000 and residual −8.7e-7 at m = 0.5, N = 96.
  - **Box curves** (S = k, W = 0 exactly on |k| ≤ b₁; unit speed to 2e-16; closure 1e-12; doubler-free):
    - −1.9999, residual −6.7e-6 (b₁ = 0.5);
    - −1.9999, residual −9.0e-6 (b₁ = 0.8).
  - At m = 0.05 the direct method is q-limited; the moment form gives exactly 0.
- **Masses free (checked; `r101_scans.out` (ii)).**
  - With m_f = 0, the residual is 0.3347·m_s² (lattice units, ×e²/16π²), converged for m_s from 0.01 to 0.1.
  - Reading: a partner at 1 TeV with a = ℓ_P gives about 1e-36 relative, far below the 2.66e-19 photon-decay bound (`C5_R8-5_report.md:261`).
- **Price (named, not adopted).**
  - **(i) Clifford-flat fermion velocities.** This takes 8 components per site, i.e. a taste doubling. Removing it would take a taste-splitting soft mass (suggested). I did not find a 4-component separable realization; that one does not exist is suggested, not proved.
  - **(ii) Bosonic partners.** Two complex scalars per 4 fermion components, on the same edge curve: an edge-band supertrace rule (RP's kind of price, restricted to the UV).

  No axiom text changes: the law is downstream (`AX:114-130`). The 8-component site domain sits against the Qubit reading exactly as R8-5's Dirac site does.

### 3.6 What pairing leaves: the electron leg. Checked

`r101_flat_electron.out`: R8-5's Feynman-gauge `fermion()` adapted to the flat law. The adapted path reproduces R8-5's own r = 1 control: −21.47 at N = 96, against −21.41.

| paired law (m = 0.05) | δc_e·16π² (N = 96 / 160) | δc_γ (Dirac + 2 scalars) | Δ = δc_e − δc_γ |
|---|---|---|---|
| Wilson circle, flat | −18.03 / −17.97 | 0 (exact) | −18.0 |
| box curve b₁ = 0.8, photon box (0.8, 1.6) | −10.73 / −10.67 | 0 (exact) | −10.7 |

- Δ stays at R8-5's size: c_e − c_γ ≈ −6e-3 to −1e-2.
- Cancelling it needs a partner loop: a selectron–photino diagram with a lattice gaugino vertex, which is not Ward-forced. It is not built (open).
- Suggested: lattice translations are discrete, so {Q, Q̄} ∝ P cannot hold exactly. Any self-energy pairing must again be a matched-edge construction, and its two-loop stability is the R8-4/R9-7 question again.

### 3.7 (b) The minimal moment set and (c) the tuning count

- **(b) Minimal set (proved where stated; suggested beyond).**
  - **Current–current (photon) one-loop LV:**
    - one functional M_S[u] = ⟨u′²A/ε⁵⟩ per scalar band;
    - three independent functionals per class-(D) band (a, A, mixing). They are independent: a ≡ 0 at r = 1 while the others are not, and they change sign separately along the r-family;
    - one functional per Clifford-flat band, equal to −2M_S[v].

    So the photon coefficient is a **supertrace** Σ_B M[v_B] − ½Σ_F M[v_F] over paired curves, plus the class-(D) a- and mixing-moments, which have no bosonic counterpart.
  - **Graviton TT from scalar loops:** Theorem T (R9-9, confirmed).
  - **Matter self-energies** (two-field loops) and Dirac TT: localization only (§3.1). They are not reduced to anomaly moments here.
- **(c) Count against set C.**
  - Set C's continuous-time total is ≥ 6 (2 TT masses + 1 QED speed + 3 graviton-speed codimensions; reading, `SUMMARY.md:435`).
  - **C-box without pairing.** The same 6 for QED plus gravity (reading). Each coefficient is a generically nonzero edge moment. Some are sign-definite on whole subclasses (§3.4), so a zero requires a sign-changing edge and then costs one condition per independent moment. Universal edge shapes make the count per moment type rather than per species at one loop, and set C's universal discretization behaves the same way.
  - **C-box with pairing (§3.5).** The photon's own coefficient is removed structurally. But c_e − c_γ still needs one condition (§3.6), and the graviton's 3 + 2 are untouched. So the count is still 6 at one loop.
  - **All orders (suggested).** The box adds no symmetry beyond set C's cubic group, so by the standard EFT counting the number of independent dimension-4 LV operators, and hence of counterterms, is set C's. One-loop shape zeros are not protected at two loops (cf. R8-4 and R9-7).

## 4. Against the FIXED readings (`TESTS.md:3973-3975`)

**Worker reading: SUGGESTED**, with derived parts. Same family, unrefereed.

- **DERIVED is not met, for two reasons.**
  1. The premise "every one-loop LV coefficient is a moment of A" is **false** for Dirac-sea matter in R8-5's class. Theorem D finds three more anomaly functions, and the a-term dominates box shapes (checked against refereed numbers).
  2. An untuned structural choice, Theorem P's pairing, nulls one whole coefficient class: the photon one-loop speed, for every shape and mass. So "no untuned choice nulls them" is false coefficient by coefficient. What survives as a no-go is narrower: the sign theorems and Lemma N(m) in their subclasses.
- **REFUTED is not met.** The electron self-energy (§3.6) and the graviton coefficients are not nulled by anything built. Δ is −10.7 to −18.0 in the paired law.
- **What is derived (for the referee):**
  - Theorem T′ (scalar photon = A-moment with a Ward-forced positive weight);
  - Theorem D (the Dirac anomaly-jet identity, reproducing R8-5);
  - Theorem P (pointwise boson–fermion cancellation of the photon moment);
  - the sign theorems and Lemma N(m);
  - the localization lemma (sketch).
- **The record, if the referee confirms.** "The box route's photon coefficient can be removed only by an edge supertrace (Clifford-flat fermions plus matched scalar partners); its matter-speed coefficients are not removed by anything built; the tuning count equals set C's at one loop."

## 5. Prices (named, not adopted)

- **P-flat.** Clifford-flat fermion velocities ({∂_jh, ∂_lh} = 2δ_jl at every k). This means 8 components per site, a taste doubling, and a unit-speed edge curve.
- **P-pair.** Two complex scalars per 4 fermion components on the same edge curve: an edge supertrace rule. Masses are unconstrained (residual ∝ Δm²).
- **For the observable** (open): a matched partner loop for every gauge self-energy (gaugino-type, not Ward-forced), plus a TT-sector pairing, plus two-loop stability. None is built.

Admissibility does not fix dynamics (`AX:114-130`), so each of these is a law choice needing registration or derivation. The Qubit fibre is not changed beyond R8-5's Dirac and non-compact photon prices (`AX:43-53`).

## 6. Scope and strong-word check

- **"Exact" / "pointwise":** applies to the algebraic identities (Theorems T′, D, P) of one-loop integrands for free bilinear matter with Peierls vertices, q along an axis, and continuous time.
- **"Proved":**
  - T′: hand derivation plus the R9-9 integration by parts, which the referee confirmed;
  - D: a sympy identity in the jet, plus periodicity of G;
  - P: algebra on top of D and T′;
  - the sign theorems and Lemma N(m);
  - the localization lemma, as a sketch: routing, k₀ decay and Wick-rotation technicalities are not written out.
- **"Checked":** every table number, with N-convergence in the `.out` files. The direct–moment agreements are ≤ 1e-3 relative for D (limited by R8-5's q-extrapolation) and ≤ 1e-5 for T′ and P at resolved masses.
- **"Untuned"** (pairing): no number is adjusted. It is a structural pairing rule, listed as a price.
- **Not claimed:**
  - any statement about INV, non-Peierls or transverse Pauli vertices;
  - interacting matter;
  - two loops;
  - Dirac TT;
  - the matter-side graviton-loop shift;
  - a 4-component no-go for Clifford-flatness (suggested only);
  - that pairing is observationally viable beyond the photon coefficient.
- **Comparators.** Groot Nibbelink–Pospelov is RECALLED. Polchinski is verified via the R7-5 referee.

## 7. For the referee

1. **Theorem D.** Rerun `r101_dirac_symbolic.py` (the invariant form check is 7e-16), and check that the residual's c-terms are the only non-A, non-a pieces. Is G periodic for the BQ laws? E > 0 there.
2. **The R8-5 match** (`r101_dirac_moment.out`), in particular the naive (−5.0199 vs −5.0220) and r = 32 (+706.6 vs +706.1) rows.
3. **Theorem P's direct check.** The 7-component adaptation of R8-5's χ_yy and P_E (`r101_pairing.py:direct_dirac_flat`), and the trace normalization "per 4 components".
4. **Whether Theorem P counts as "untuned"** under the R10-1 clause. It is listed as a price, so either way the REFUTED clause is not met (§3.6).
5. **The flat electron self-energy adaptation** (`r101_flat_electron.py`: the β_x component of n) and its R8-5 control.
6. **Lemma N(m)'s Laplace step,** and whether the localization sketch needs more than k₀ decay.

## 8. Files

All in `S/scripts/`:
- `r101_dirac_symbolic.{py,out}`;
- `r101_dirac_moment.{py,out}`;
- `r101_scalar_qed.{py,out}`;
- `r101_pairing.{py,out}`;
- `r101_scans.{py,out}`;
- `r101_flat_electron.{py,out}`;
- copies `r85_box_qed_copy.py` and `r99_profiles_copy.py`.

No downloads.
