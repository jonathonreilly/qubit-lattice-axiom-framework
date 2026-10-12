# C5 R13-7 report: is the electron–photon split a theorem? A mass-interval test for c_e − c_γ

**Author.** Claude Opus 5.5 probe, the same model family as the supervisor and every C5 worker. Unrefereed. 2026-10-12, 20:48Z to about 21:25Z. No repository file was edited (`git status` clean).

**Scratch.** `S/` = `.../scratchpad/C5/R13-7/`. Scripts and outputs are in `S/scripts/`. Every run takes under 1 min with `OMP_NUM_THREADS=2`.
- `r137_onshell.py`: the ON-SHELL one-loop electron speed c_e(m) in R8-5's box QED, built on R8-5's refereed Euclidean self-energy (Feynman gauge, photon mass λ). It also imports R10-1's refereed Theorem-D moment for c_γ(m).
- `r137_validate.out`, `r137_conv.out`, `r137_small_m.out`: on-shell against R8-5's off-shell estimator at small m; N, λ and h convergence.
- `r137_mscan.{py,out}`: c_e(m), c_γ(m) and Δ(m) for m = 0.05 to 51.2 (lattice units), on 5 laws.
- `r137_heavy_checks.{py,out}`: the heavy-mass limit against its closed form (Theorem H), plus the hypotheses and identity of Theorem Sgn.
- `r137_sign_scan.{py,out}`, `r137_hires_inf.{py,out}`: the sign of the heavy constant over 45 laws, then high-resolution values for the steep shapes.
- `r137_tuned_heavy.{py,out}`: the REFUTED-direction attempt. The heavy constant is tuned to zero, and Δ(m) is then scanned.
- `r137_e1_scan.{py,out}`: the 1/m coefficient e₁ over 45 laws.
- Unmodified copies: `r85_box_qed_copy.py` (R8-5) and `r101_dirac_moment_copy.py` (R10-1).

**Read.**
- `docs/MINIMAL_AXIOMS_2026-06-29.md`, in full (`AX`).
- `TESTS.md`: the C5 method (`:2302-2320`); R8-5 (`:3528`, `:3807-3813`); R9-8 (`:3851`, `:4026-4035`); R10-1 (`:3954`, `:4270-4277`); R10-5 (`:4048`, `:4303-4310`); R11-1 (`:4086-4120`, `:4394-4408`); R12-3 (`:4375`, `:4483-4489`); R12-6 (`:4493`, `:4696-4703`); R13-1 (`:4578-4596`, `:4715-4722`); R13-7 (`:4737-4747`).
- Agents: `C5_R8-5_report.md` and verdict; `C5_R10-1_report.md` and verdict; `C5_R11-1_report.md` and verdict; `C5_R12-6_referee_verdict.md` (and grep of its report); `C5_R13-1_report.md` (unrefereed).
- Scripts: `scripts/C5/R8-5/r85_box_qed.py`; `scripts/C5/R10-1/r101_dirac_moment.{py,out}`.

**Labels.**
- **proved**: complete under the stated hypotheses.
- **checked**: numerics here.
- **suggested**: argued, not proved.
- **reading**: an interpretation.
- **comparator**: literature, RECALLED.

---

## 0. In plain words

1. **What "cannot vanish on a mass interval" means.** At fixed photon mass λ > 0, Δ(m) = c_e(m) − c_γ(m) is real-analytic in m > 0 (Lemma A, proved). So it vanishes on an interval only if it vanishes for **every** mass. Isolated zeros are allowed, and one occurs: with the Wilson edge, S1's Δ changes sign near m ≈ 3.3 (checked).
2. **New fact: a heavy electron's speed shift does not die away (Theorem H, proved for the literal edge; checked to 1.5e-4).**
   - As m → ∞, the photon coefficient falls like m⁻³.
   - The electron's on-shell speed shift tends instead to a constant:

     **δc_e^∞ = ¼⟨A(q_x)·w(q)⟩**, with w = (d_y² + d_z² + λ²)/(d_x²W³) ≥ 0 and A = (S²)″/2 − 1.

   - This is the lattice form of the classical "4/3 problem" (comparator, RECALLED). The photon cloud of a heavy charge samples the band's curvature anomaly A, so the kinetic mass and the rest mass differ by an O(e²) fraction that does not decouple.
3. **A sign theorem (Theorem Sgn, proved).** Suppose:
   - (H1) the electron symbol never exceeds the continuum momentum, |S(q)| ≤ |q|;
   - (H2) the photon has no plateau transition on the electron's edge, e.g. its box lies inside the electron's.

   Then δc_e^∞ < 0 strictly. **So in that subclass (pure QED, any finite set of charged species whose masses grow together) the split cannot vanish on any mass interval: DERIVED in a subclass** (worker).
4. **Why it is not class-wide.** These points are checked except the last, which is suggested.
   - Without (H2) the heavy constant changes sign across laws: from −12.3 to +6.1, converged. So one shape condition nulls it. Then a 1/m term appears (e₁ ≈ −22 for the tuned law), and Δ is −106 at m = 0.1.
   - Identical vanishing needs infinitely many conditions. I found no structure that forces one of them to fail class-wide, and no law that meets them all.
   - With Wilson (gapped) edges, δc_e grows *linearly* in m, with a shape-dependent sign.
   - SUSY-type partners add an opposite-sign recoil term (suggested).
5. **Physical weakness (reading).** The no-go excludes only a *structural* zero. One shape or counterterm tuning of the light-mass value Δ(0⁺) nulls the split for every light species, up to O(m a) ≈ 1e-22 at a = ℓ_P. So the registered gloss "a per-mass (counterterm) tuning" is too strong. This is R10-1's own "physically weak" reading of Lemma N(m) (`C5_R10-1_report.md:201`).
6. **Against the FIXED readings: SUGGESTED** (worker). Derived parts: Lemma A, the exact tadpole lemma, Theorem H, Theorem Sgn and its subclass corollary. REFUTED is not met: no law with Δ ≡ 0 was found.

---

## 1. Hypotheses and classes (stated before any title)

- **𝒬 (registered, `TESTS:4740`).** Ward-forced Peierls or any ℓ¹ bilinear gauge generator; periodic C² bands; box or not; any finite set of species, paired or not; one loop.
- **𝒬_lit (where the theorems are proved).**
  - Z³ × ℝ, continuous time.
  - Electron: R8-5's BQ law with r = 0, the literal edge: h = Σ_j S(k_j)α_j + mβ. S is odd, 2π-periodic and C³, with S(k) = k on |k| ≤ b. The case b = 0 (no box, S = sin) is included.
  - Photon: R8-5's non-compact photon, W² = Σ_j d(q_j)² + λ², with d even, periodic, C², d(0) = 0, d > 0 elsewhere, and d(q) = q + O(q³).
  - Peierls coupling (class 𝒢₀, `vR8-5:3`); Feynman gauge.
  - Other charged species: any finite set of complex scalars or Dirac fields with C² bands and Peierls coupling, whose masses → ∞ as m → ∞. N\*'s affine family m_s² = a_s m² + c_s with a_s > 0 qualifies.
  - No Yukawa or partner couplings. One loop.
- **𝒬_lit⁻.** 𝒬_lit plus:
  - (H1) |S(q)| ≤ |q| for b ≤ |q| ≤ π. This holds in R8-5's whole family, since S′ ≤ 1 there.
  - (H2) q_x ↦ w is convex on [b, π]. A sufficient condition, proved in §3.5, is (H2′): d(q) ∈ {q, 2 sin(q/2)} on [b, π]. That is, the photon plateau transition [c₁, c₂] does not meet [b, π] (c₂ ≤ b, or no photon box).
- **Observables.**
  - **c_γ:** R8-5's dimension-4 photon speed, δc_γ = (P_M − P_E)/2, summed over charged loops. For BQ species this is R10-1's refereed Theorem-D moment (`vR10-1:5`).
  - **c_e, ON-SHELL:** E(p)² = m_phys² + c_e²p² + O(p⁴) along an axis, at one loop, with δc_e := (c_e² − 1)/2.
  - R8-5's B − A is the off-shell (p₀ = 0) estimator. It agrees with the on-shell value only as m → 0 (§3.2). The physical c_e(m) on an interval of lattice-scale masses is the on-shell one.
  - Units: per e², printed ×16π² (e²/16π² units).
- **λ.** A fixed photon-mass IR regulator: λ > 0 in Lemma A, λ ≥ 0 in Theorem H. The scans use λ = 0.05 for all m. **Subtractions named before the runs:** none. The 1/m Richardson extrapolation is an extrapolation, stated as such.
- **Excluded from the theorems (outside realizations).** These were computed as controls or stated:
  - Wilson (shared-β) electron edges;
  - Clifford-flat 8-component electrons (suggested to behave as the literal edge, not run);
  - non-orbital ℓ¹ densities and non-Peierls (Pauli) vertices;
  - Yukawa or SUSY partners (R10-5, R12-6, R13-1 content);
  - compact links; two loops;
  - analyticity at λ = 0 (suggested).

## 2. Prior art (each counted once)

- **R11-1 Theorem N\*** (`vR11-1:3`). The model mechanism here: Laplace/Lerch plus ∫A dk_∥ = −2π. Its premise "w independent of k_∥" (`C5_R11-1_report.md:148`) is exactly what fails for the electron: the electron's weights depend on q_x through d(q_x) and W(q). That is why no periodicity sign comes for free.
- **R10-1** (`vR10-1:5,11`). Theorem D, used for c_γ(m). Lemma N(m) and its "physically weak" reading (`C5_R10-1_report.md:201`). The off-shell tadpole (`r85_box_qed.py` `tadd`).
- **R8-5** (`vR8-5`). The BQ law, the runner, and Δ ∈ [−71, −11]. Its non-decoupling under heavy *Wilson* edges (`vR8-5:7`, the r-deformation only; also `C5_R9-1_report.md:205`) is a different deformation from the electron *mass* used here.
- **R13-1** (worker). Lemma LIT. The product-rule defect S′ − 1 reappears here as the exact tadpole moment.
- **R12-6** (`vR12-6:4`). In 𝒦₀, Δ contains +6 ln(1/m). By Lemma A, that log alone excludes interval zeros in 𝒦₀ (reading: the electron's −2 coefficient is a fit).
- **O3 Theorem 1a; RV4_S1** (`RV4_S1_referee.md:32`, van Hove singularities at coincident critical levels). An alternative mass-interval route, through complex-mass singularities. Not used (§3.8).
- **Comparator.** The classical electromagnetic-mass "4/3 problem": with a non-covariant cutoff, the inertial EM mass is (4/3)U/c² (RECALLED). Repo grep for "4/3 problem", "kinetic mass" and "heavy electron" over agents, TESTS and SUMMARY found nothing.

## 3. Results

### 3.1 Lemma A (analytic rigidity). Proved

- **Claim.** In 𝒬_lit with λ > 0, Δ_λ(m) is real-analytic on (0, ∞). The same holds for BQ Wilson electrons, since E > 0 for m > 0. Hence Δ_λ vanishes on an open interval ⇔ Δ_λ ≡ 0 on (0, ∞) ⇔ every coefficient of its m → ∞ asymptotic expansion vanishes.
- **Proof.**
  1. At p = 0, the normal denominators satisfy W + E_k − E_0 ≥ W ≥ λ, since E_k ≥ E_0 = m when v ≥ 0, and the Z-graph denominators satisfy W + E_k + E_0 > 0.
  2. The integrands and their p-derivatives at p = 0 are analytic in m on a complex neighbourhood, uniformly on the compact zone. The same holds for the photon moments, since E_s > 0.
  3. The identity theorem then applies. ∎
- **Isolated zeros are allowed and occur.** S1 gapped has Δ = −0.341 at m = 3.2 and +8.755 at m = 6.4 (`r137_mscan.out:8-9`).

### 3.2 The on-shell runner (checked) and the exact tadpole lemma (proved)

- **Construction.** `r137_onshell.py` evaluates R8-5's refereed Σ(p₀, p) at p₀ = −iE_p, so the denominators become W + E_k ∓ E_p. It takes δE = ½Tr[P₊(p)Σ] and c_e² − 1 = ∂_{p²}(2E_pδE) (Richardson).
- **Small-m validation** (`r137_conv.out`, `r137_small_m.out`).
  - On the naive F2 law at m = 0.1, N = 128: on-shell −16.03 against F2/R8-5 off-shell −16.07.
  - Over m ≤ 0.1, on-shell and off-shell agree to 0.02–0.42 (≤ 4%).
  - Both drift with N once m is below the q-spacing, as R8-5 also noted (`C5_R8-5_report.md:219-222`).
  - N = 64 → 128 changes the on-shell value by ≤ 0.07; h = 0.02 → 0.04 changes it by ≤ 0.003.
- **Tadpole lemma (proved).** On the literal edge, 2E_p·T(p) = S(p)⟨[S(p+q_x) + S(p−q_x) − 2S(p)]/(2d_x²W)⟩ exactly, because 2E_p a_x = 2S(p). So the tadpole contributes ⟨(S′(q_x) − 1)/(d_x²W)⟩ to c_e² − 1, **independent of m**.
  - Checked: the "tad" column is −10.4818 at every m for S1 literal (`r137_mscan.out:13-23`).
  - S′ − 1 is R13-1's product-rule-defect derivative. Its zone mean is −1 by periodicity.
- **Off-shell at large m (suggested, by inspection).** Every non-tadpole term of R8-5's B − A carries 1/E, so the off-shell estimator → `tadd` (−10.48 for S1 literal), whereas the on-shell value → −5.27. R8-5's estimator is therefore not the physical speed at lattice-scale masses.

### 3.3 Theorem H (heavy-electron non-decoupling). Proved for 𝒬_lit; checked

- **Claim.** In 𝒬_lit with λ ≥ 0, as m → ∞:

  **c_e² − 1 → ½⟨A(q_x)(W² − d_x²)/(d_x²W³)⟩, i.e. δc_e^∞ = ¼⟨A(q_x)(d_y² + d_z² + λ²)/(d_x²W³)⟩, with A = S′² + SS″ − 1 = (S²)″/2 − 1.**

  Meanwhile every charged species' photon coefficient → 0. The literal Dirac terms of Theorem D are O(m⁻³); scalars are O(m⁻⁵); Wilson-BQ terms are O(m⁻²).
- **Proof** (1/m expansion; uniform in q because v = ΣS² is bounded). Write F = 2E_pδE = F_T + F_Z + F_N, with a = n̂_p, b = n̂_k and Δ_j the scalar vertex numerators.
  1. **The expansions.**
     - 1 − a·b = Σ_jΔ_j²/(2m²) + O(m⁻⁴);
     - a_x b_x = O(m⁻²);
     - E_p/(W + E_k + E_p) = ½ − W/(4m) + O(m⁻²);
     - E_p(E_k − E_p) = (v_k − S(p)²)/2 + O(m⁻²).
  2. **Z-graphs.** F_Z = ⟨Σ_jΔ_j²/(2d_j²W)⟩ + O(1/m). The p² coefficient of Δ_x² is (1 − S′)² + SS″.
  3. **Adding the tadpole.** That gives ⟨[(1 − S′)² + SS″ + 2(S′ − 1)]/(2d_x²W)⟩ = ⟨A/(2d_x²W)⟩: the lattice seagull.
  4. **Normal graphs.** The A₀ part gives m⟨1/W²⟩ (p-independent), plus (p²/2m)⟨1/W²⟩ → 0, minus ⟨(v_k − S(p)²)/(2W³)⟩. The p² coefficient of the last is ⟨A/(2W³)⟩: the Coulomb recoil. The spatial normal terms are O(1/m).
  5. **Integrability.** A/d_x² is bounded near q_x = 0, since A(0) = 0 and A = O(q²). A/W³ is integrable in 3D: it is O(1/|q|) near q = 0 and vanishes there when b > 0. So dominated convergence applies. ∎
- **Checked** (`r137_heavy_checks.out:2-9`): Richardson in 1/m of the on-shell δc_e at m = 25.6, 51.2 and 102.4, against the closed form:

| literal law | N | on-shell, extrapolated | closed form |
|---|---|---|---|
| S1 (1, 2; photon 1, 2) | 96 | −5.27149 | −5.27137 |
| S3 (2, 3; 2, 3) | 96 | −0.63495 | −0.63585 |
| S5 (0.5, 1.5; 0.5, 1.5) | 96 | −8.37173 | −8.37212 |
| naive (sin; 2 sin(q/2)) | 96 | −15.70591 | −15.70594 |

  - The photon side decouples: |δc_γ| ≤ 1.5e-3 at m = 51.2 (`r137_mscan.out:23,46,58`).
  - λ → 0: the closed form moves by ≤ 1e-4 relative from λ = 0.02 to 0 (`r137_heavy_checks.out:11-12`).
- **Wilson control (checked; not covered by Theorem H).** δc_e grows linearly in m:
  - S1 gapped: +58.2 and +123.2 at m = 25.6 and 51.2;
  - S3 gapped: −9.2 and −16.3 (`r137_mscan.out:11-12,34-35`).

  The Wilson mass makes edge hopping O(1), not O(1/m). The linear coefficient changes sign between shapes. Suggested: it is a moment of the zero-mean W″.

### 3.4 Photon decoupling. Proved by inspection; checked

For the species admitted in 𝒬_lit, every term of R10-1's R_D and T′ carries at least E⁻² net after the numerators. So all charged loops vanish as their masses → ∞. Checked: the dc_g columns of `r137_mscan.out`.

### 3.5 Theorem Sgn (the sign of the heavy constant). Proved; checked

- **Claim.** In 𝒬_lit⁻ (H1, H2), δc_e^∞ < 0.
- **Proof.**
  1. Fix q_⊥ with D′ = d_y² + d_z² + λ² > 0, and set w(q) = D′/(d²(d² + D′)^{3/2}), I = ∫_b^π A w dq, and g = S² − q².
  2. g(b) = g′(b) = 0, because S = q on [0, b] and S is C¹. g(π) = −π² and g′(π) = −2π, because S(π) = 0 by oddness and periodicity. w′(π) = 0, because w is even and periodic.
  3. Integrating by parts twice: **I = ½∫_b^π g″w = −πw(π) + ½∫_b^π (S² − q²) w″ dq.**
  4. (H1) gives g ≤ 0 and (H2) gives w″ ≥ 0, so I ≤ −πw(π) < 0.
  5. A and w are even in q_x, so ⟨Aw⟩ = (2/(2π)³)∫d²q_⊥ I < 0.
  6. For b = 0, the boundary terms at 0 vanish because g = O(q⁴) and w = O(q⁻²). ∎
- **(H2′) ⇒ (H2) (proved).** Write t = d² = 2(1 − cos q) and φ = t⁻¹(t + D′)^{−3/2}. Then

  w″/(D′φ) = (6 − t)(1/t + y) + (5/3)t(4 − t)y² > 0 for t ∈ (0, 4], with y = 3/(2(t + D′)),

  using t′² = t(4 − t) and t″ = 2 − t. For d = q, the analogue is 6/t + 6y + (20/3)ty² > 0.
- **Checked** (`r137_heavy_checks.out:13-19`; `r137_sign_scan.out:1`):
  - the closed-form minimum is 0.53 > 0;
  - the identity for I holds to ≤ 1.6e-3, and to 3e-2 for b = 0, where the endpoint is singular;
  - (H1) holds in all 6 R8-5 shapes;
  - (H2) holds for S5 and the naive photon, and fails for S1, S3, S7 and S8, whose photon transition overlaps the electron edge. Their constants are nonetheless negative, except S8 (§3.7).

### 3.6 Corollary: the subclass no-go. DERIVED in 𝒬_lit⁻ (worker)

For every law in 𝒬_lit⁻ with λ > 0:
- Δ_λ(m) → δc_e^∞ < 0 as m → ∞ (Theorems H and Sgn, §3.4);
- so Δ_λ ≢ 0, and by Lemma A, **Δ_λ vanishes on no open mass interval**.

This holds for any finite set of extra charged species, provided their masses grow with the electron's. Pairing of the photon coefficient is allowed (R10-1 Theorem P scalars added on the side). Yukawa partners are not.

### 3.7 Beyond the subclass: the REFUTED direction. Checked

- **The sign is not forced without (H2)** (`r137_hires_inf.out`, Nx = 8000, N_⊥ = 160, converged to 4 digits). On e-box (2.5, 3.1):
  - with the photon box (2.5, 3.1): δc_e^∞ = **+1.748**;
  - with the naive photon: −2.372.

  Also +6.064 on (2.8, 3.1)/(2.8, 3.1). So by continuity a law with δc_e^∞ = 0 exists. Over 45 laws the range is −12.3 to +6.1.
- **Under-resolution caveat.** The N = 64–96 3D sums under-resolve the steep (2.8, 3.1) plateaus: N = 96 gave −4.11 where the resolved value is −2.03 (`r137_sign_scan.out`). Only the high-resolution values are cited for those shapes.
- **Nulling the heavy constant does not null Δ** (`r137_tuned_heavy.out`). The law was tuned at N = 64 (photon box c₁ = 2.2766); at high resolution its constant is +0.37, so the exact zero lies nearby and was not relocated.
  - Δ = −106.4 at m = 0.1 (the photon side is +99);
  - m·Δ → −21.9 at m = 102.4, so a nonzero e₁/m tail remains.
- **e₁ is not shown to have a fixed sign** (`r137_e1_scan.out`).
  - e₁ < 0 in 42 of 44 distinct laws, from −126 to −0.2.
  - Two laws give +0.23 and +1.24 (e-box (2.0, 2.5) with a photon box near the zone face). Their two 1/m estimates are unconverged (−0.80 vs −0.28), so the sign there is not established.
  - The (2.8, 3.1) rows are under-resolved at N = 64.
- **Reading.** Identical vanishing needs δc_e^∞ = 0, e₁ = 0, … and Δ(0⁺) = 0: infinitely many conditions on two free functions (S, d). Nothing found forces a failure class-wide (no periodicity sign, no Titchmarsh rigidity as in Theorem S). Nothing found satisfies them all.

### 3.8 What a class-wide proof would need (suggested)

- **(i) Wilson edges.** A sign or nonvanishing for the linear-in-m coefficient (a W″-moment, zero mean).
- **(ii) Without (H2).** A forced sign for some later coefficient (e₁ is negative in most laws, but not proved), or a rigidity theorem for the full Laplace measure.
- **(iii) Partners.** In SUSY content, the photino–selectron loop adds a positive-norm recoil term. It is of opposite sign to the A₀ Coulomb recoil (suggested; second-order level repulsion), so Theorem Sgn's mechanism is not available. In 𝒦₀ the refereed log route (`vR12-6:4`) already gives Δ ≢ 0 at checked level.
- **(iv) Singularity matching.** An alternative is RV4_S1-type matching at complex m² = −v_c (the van Hove points of the electron band). The photon moment and the electron self-energy both carry ln ε singularities there (suggested from the local expansion), so their coefficients would have to cancel point by point. Not worked out.
- **(v) Non-orbital ℓ¹ densities** (𝒢 \ 𝒢₀) are untouched.

### 3.9 Physical size (reading)

- In every computed law Δ(m) is IR-safe and smooth near m = 0 (`r137_mscan.out`). On the gapped edge it is roughly linear in m (slope about 8 on S3). On the literal edge it is flatter.
- At a = ℓ_P the electron has m a ≈ 4e-23. So one tuning of Δ(0⁺), by a shape condition or one counterterm, leaves |c_e − c_γ| ≲ 1e-25, far below the 2.66e-19 photon-decay bound (`C5_R8-5_report.md:261`).
- So the no-go (where proved) excludes an untuned, *structural* zero. It does **not** imply a per-mass tuning.

## 4. Against the FIXED readings (`TESTS:4744-4747`)

**Worker reading: SUGGESTED**, with derived parts. Same family, unrefereed. The no-go parts (§§3.5–3.6) need the codex referee.

- **DERIVED (registered class): not met.** The proof covers only 𝒬_lit⁻:
  - literal-edge Dirac electron;
  - Peierls (𝒢₀) photon;
  - (H1) |S| ≤ |k| on the edge;
  - (H2) no photon plateau transition on the electron's edge;
  - extra species' masses growing with the electron's;
  - no partners; λ > 0.

  Outside it: the heavy constant changes sign (§3.7); Wilson edges grow linearly with either sign (§3.3); partners and non-orbital densities are not treated.
- **REFUTED: not met.** No law in 𝒬 with Δ ≡ 0 on an interval was found. The one-condition tuned law still has Δ(0.1) ≈ −106 and an e₁/m tail.
- **Derived parts for the referee:**
  - Lemma A (analytic rigidity);
  - the tadpole lemma (m-independent, exact);
  - Theorem H (heavy-electron non-decoupling, closed form);
  - Theorem Sgn with (H2′);
  - the corollary in 𝒬_lit⁻.
- **Correction to the registered text (reading).** "The split then needs a per-mass (counterterm) tuning" should read: "the split has no structural zero in 𝒬_lit⁻; one tuning of its light-mass value suffices physically".

## 5. Prices (named, not adopted)

- No axiom text is touched; dynamics is downstream (`AX:114-130`).
- The proved subclass is itself a law choice: a literal-edge electron (doublers at mass m) with a photon whose box lies inside the electron's. These are two shape conditions, not axiom content.
- Removing the split still costs what R8-5, R10-1 and R13-1 named (P48 stands): a counterterm or a shape tuning at m → 0.

## 6. Strong-word check

- **"Proved":**
  - Lemma A (identity theorem; λ > 0);
  - the tadpole lemma (algebra);
  - Theorem H: a 1/m expansion uniform on the compact zone, with dominated convergence. The O(m⁻²) remainders are bounded, not computed.
  - Theorem Sgn and (H2′): integration by parts and closed-form calculus;
  - §3.4 decoupling, by power counting of R10-1's refereed forms.
- **"Checked":** every number, with N, λ, h and m stated in the `.out` files.
  - Heavy limits: N = 64 and 96 agree to ≤ 3e-3 relative for S1, S5 and naive, and to 2.6% for S3. At each N the closed form matches the extrapolated on-shell value; the high-resolution S3 constant is −0.6315.
  - Steep shapes only at high resolution.
- **"Does not decouple":** for the on-shell δc_e of 𝒬_lit and of the Wilson controls, along the electron-mass deformation, at fixed λ.
- **"Cannot vanish on an interval":** only in 𝒬_lit⁻ with λ > 0. At λ = 0, analyticity is suggested; the heavy constant is checked continuous.
- **Not claimed:**
  - any class-wide no-go;
  - a sign for e₁;
  - anything for Clifford-flat electrons (suggested to follow the same algebra), Wilson electrons, partners, non-orbital densities, or two loops.

## 7. For the referee

1. **The on-shell continuation** of R8-5's Σ (p₀ = −iE_p ⇒ W + E_k ∓ E_p) and δE = ½Tr[P₊Σ] (`r137_onshell.py:1-17,32-70`). Also the small-m agreement with R8-5's off-shell estimator, within 0.02–0.42.
2. **Theorem H's expansion.** In particular, that the Z-graph plus the tadpole gives the seagull ⟨A/(2d_x²W)⟩, and that the A₀ recoil gives −⟨A/(2W³)⟩. Check against `r137_heavy_checks.out:2-9`.
3. **Theorem Sgn's boundary terms** (g(b) = g′(b) = 0, w′(π) = 0) and the (H2′) closed form.
4. **Whether λ > 0 in Lemma A is acceptable**, or the λ = 0 IR analyticity must be proved. The in-box region is continuum-covariant, but that is R10-1's localization sketch (`vR10-1:15`).
5. **Whether the tuned-law and e₁ numerics** (§3.7) suffice for "not class-wide", or whether a counterexample to the sign of e₁ is needed.

## 8. Files

All in `S/scripts/`:
- `r137_onshell.py`; `r137_validate.out`; `r137_conv.{py,out}`; `r137_small_m.{py,out}`;
- `r137_mscan.{py,out}`; `r137_heavy_checks.{py,out}`;
- `r137_sign_scan.{py,out}` (the `.out` comes from the pre-refactor run of the same code; the `__main__` guard was added afterwards for import); `r137_hires_inf.{py,out}`;
- `r137_tuned_heavy.{py,out}`; `r137_e1_scan.{py,out}`;
- copies `r85_box_qed_copy.py` and `r101_dirac_moment_copy.py`.

No downloads.
