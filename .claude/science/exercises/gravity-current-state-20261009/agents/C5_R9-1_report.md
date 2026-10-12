# C5 R9-1 report: edge-sector population (harmless, observable, or dark-matter-like?)

**Author.** Claude Opus 5.5 probe. Same family as the supervisor and every C5 worker. Unrefereed. 2026-10-12, 16:38Z to about 17:05Z. No repository file edited.
**Scratch.** `S/` = `.../scratchpad/C5/R9-1/`.
- `S/scripts/r91_edge_population.py` → `.out` (4.5 s, `OMP_NUM_THREADS=2`): parts A–E below.
- `S/scripts/r91_qed_checks.py` → `.out`: QED, free-fall and inflation arithmetic.
**Read.**
- `docs/MINIMAL_AXIOMS_2026-06-29.md` in full (`AX`).
- `TESTS.md`: C5 method and round 1 (`:2302-2440`); results through "Round 7–8 referee results, part 3" (`:2706-3573`; round-6 prereg `:3009-3240` skimmed); R9-1 (`:3600-3639`).
- `agents/C5_R8-2_report.md` and `C5_R8-2_referee_verdict.md` in full.
- `agents/C5_S8_synthesis.md` (`:1-120`, plus grep hits).
- `SUMMARY.md` §§21–23 (`:534-606`) and `:395-410`.
- `C5_R7-1_report.md:55-120,217-274` and `C5_R7-1_referee_verdict.md:50-58,212-219`.
- `C5_O2_report.md:112-135` (Lemma F).
- R8-2's script `scripts/C5/R8-2/r82_edge.py` (band and symbol definitions, reused).
- Pending worker R8-5 (`scratchpad/C5/R8-5/R8-5_report.md:1-80,150-250`), as an **unrefereed worker claim only**.
**Labels.**
- **proved**: an argument given here, complete under its stated hypotheses.
- **checked**: numerics here.
- **suggested**: argued, not proved.
- **reading**: an interpretation.
- **comparator**: literature. V = verified by web this run; RECALLED = from memory, not verified.

**Comparators verified this run (V).**
- MICROSCOPE: η(Ti, Pt) = [−1.5 ± 2.3 ± 1.5]e-15 (PRL 129, 121102; arXiv 2209.15487), as cited at `C5_R8-2_referee_verdict.md:66`. Registered bar 1e-15.
- Planck 2018: Ω_c h² = 0.120 ± 0.001 and N_eff = 2.99 ± 0.17 (arXiv 1807.06209).
- Dark-matter EP bounds:
  - Kesden–Kamionkowski (astro-ph/0608095; Kesden 0903.4458): extra DM–DM force ≲ 10% of gravity, from the Sgr stream symmetry. Contested by Keselman–Nusser–Peebles 2009.
  - Cowsik et al. (arXiv 1808.09925): torsion-balance η_DM(Al, SiO₂) ~ 1e-5 toward Galactic DM (version-dependent).
- BK18: r₀.₀₅ < 0.036 (95%), PRL 127, 151301.
- Electron moment: a_e = 0.00115965218059(13) (Fan et al., PRL 130, 071801, 2023).

**RECALLED** (PDG; not verified this run):
- Γ_Z = 2495.2 ± 2.3 MeV and Γ(Z→ee) = 83.91 MeV;
- the a_e same-mass vacuum-polarization coefficient 119/36 − π²/3;
- α⁻¹(M_Z) ≈ 128.95;
- the Parker / Chung–Kolb–Riotto gravitational-production scalings.

---

## 0. In plain words

1. **The gravitating edge forces the doublers to carry the same charges as the particle (new, proved).** Take R8-2's universal stress. Its density is continuous and positive on the diagonal (refereed). Gravity's energy density must also commute with electric (or colour) charge, or charge is not conserved in a gravitational field. Together these force every mode of the band, box and edge alike, to carry the same charge (Lemma Q).
   - So the gauge case **G-in (photon vertex only on the box) is unavailable for any charged species** once gravity is universal.
   - This is independent of R8-5's gauge-side Lemma C (unrefereed), and agrees with it.
2. **Literal profile (L): EXCLUDED** for Standard-Model content, in both gauge cases. The 7 corner copies of the electron have exactly the electron's mass (Finding D, refereed) and its charge (Lemma Q). The Z would decay into them: +587 MeV of width against a measured total of 2495 ± 2.3 MeV. They also shift a_e by 5.9e-7, about 4.6e6 times the experimental error. These numbers hold for every a, b, b₂, m.
3. **What would survive in L.** Only species that carry no gauge charge, or the priced variants below. For these, the doublers are gravity-only, cold copies of mass m, which fall correctly (weight 1 − O((pa)²) ~ 1 − 1e-40).
   - **The only production channel is two-body gravitational scattering with lattice momentum π/a.** It goes as (T/M_P)⁷ per Hubble time (computed).
   - **The resulting relic abundance depends on T_max:**
     - below Ω_DM for T_max ≲ 1.0–1.8e17 GeV;
     - equal to Ω_DM for T_max ≈ 1.0–1.9e17 GeV (a dark-matter lead);
     - overclosing above.
   - **The lead needs a universe hotter than standard inflation allows.** BK18 caps the reheating temperature at about 5.8e15 GeV; at that T_max, Ω_D h² ≈ 4e-12.
4. **Gapped profile (G): population HARMLESS** for T_max ≲ 3.5e17 GeV (a = ℓ_P, b = 2), i.e. T_max ≲ E_e/68, in either gauge case.
   - The edge sits at Planck energy, its equilibrium population is Boltzmann-suppressed, and no static or lab process reaches it.
   - Any relic is hot (w ≈ 1/3), so there is no dark-matter candidate.
   - **This does not rescue G.** Under G-out the edge acts virtually, not through population. Combining R8-5's unrefereed one-loop electron speed shift with O2's Lemma F gives a composition-dependent free-fall weight of η ~ 2–5e-7 for Ti/Pt (suggested). That is about 1e8 times the MICROSCOPE bar.
5. **Momentum balance (proved; checked semiclassically).** The lattice crystal momentum is exactly conserved, and gravity pushes on it with weight equal to energy. So active mass, and the passive "charge", equal energy.
   - Theorem E's extra term is an **inertial** anomaly: the map from momentum to velocity.
   - Consequence: a bound pair of a box body and an edge quantum has a self-accelerating energy centroid, d²(Σεx)/dt² = F·A_edge. The gravitating momentum ∫T⁰ⁱ is not conserved.
   - Momentum does not go into the field.

---

## 1. Hypotheses and class (stated before titles)

- **H-law.** R7-1/R8-2's free law in d = 3 (`C5_R7-1_report.md:63-71`; `C5_R8-2_report.md:25-28`), with b = 2.0, b₂ = 3.1.
  - **Profile L:** ε² = m² + Σ s(k_i)², with s = ρk + (1 − ρ) sin k.
  - **Profile G:** ε² = m² + Σ u(k_i), with u monotone on [0, π].
- **H-grav.** R8-2's Construction A (`C5_R8-2_report.md:73-90`; refereed `C5_R8-2_referee_verdict.md:5-21`):
  - F^{00}(k′, k) is continuous on T³ × T³, with F^{00}(k, k) = ε(k) > 0;
  - first-moment lapse coupling;
  - Newtonian exchange with the lattice Poisson symbol |D(q)|² of R8-2 (`r82_edge.py:120-127`), which has no zero at the corners (|D(π)|² = 4).
  - The graviton's own lattice kinetic symbol is a **choice (reading)**. R8-2 fixes D only as the stress's divergence symbol.
- **H-int.** Interactions are box-supported and number-conserving (R7-1 BT; R8-1 pending). Box-supported interactions leave edge particles free (proved, elementary: the support argument of `C5_R7-1_referee_verdict.md:50-58`).
- **H-gauge.**
  - **G-in:** gauge vertices are box-supported.
  - **G-out:** point-local Peierls coupling with a Dirac sea (R8-5's BQ class 𝒢₀; `R8-5_report.md:84-94`, unrefereed).
- **H-charge.** A conserved charge Q = dΓ(c(k)), with a one-body symbol c(k) diagonal in k (a translation-covariant on-site charge density). The coupled system needs [T^{00}(q), Q] = 0, i.e. exact charge conservation in a gravitational field, as required for Gauss-law consistency with a dynamical gauge field.
- **Physical scale.** a = ℓ_P = 1/M_P with M_P = 1.221e19 GeV (**reading**, `AX:187-190`). Results are also given in units of 1/a.
- **Excluded.**
  - Pair-creating non-gauge vertices (R8-4).
  - The interacting stress (R9-2).
  - FRW beyond linear order: redshift of lattice momentum is not modelled.
  - N ≥ 3.
  - Set B / LRL.

## 2. Prior art (each counted once)

- **R8-2 and its referee** (`TESTS:3550-3557`):
  - Finding D: exactly 2^d − 1 mass-m corner valleys (`C5_R8-2_referee_verdict.md:49-51`);
  - Construction A (`:5-21`);
  - Lemma U, with the referee's correction that near-face states couple with small q (`:25-29`);
  - Theorem E and its scope (`:31-47`): the arbitrary-k acceleration is semiclassical (`:45`);
  - the gap ceiling (`:53-58`);
  - η = 0 only as a proxy (`:60-66`);
  - R8-2's own suggested η-channels (`C5_R8-2_report.md:181-185`): Planck-transfer dressing ~ (m_N/M_P)², and gauge/loop risk ~ 1e-6.
- **R7-1:**
  - the inert-edge reading (`C5_R7-1_report.md:221-225`);
  - the suggestion that gauge coupling reaches all modes (`:230`);
  - the referee's universality price (`C5_R7-1_referee_verdict.md:212-219`).
- **O2 Lemma F** (`C5_O2_report.md:118-131`): β_B = Hess(E_B²/2)|₀; the EP tests a common β.
- **I2/C3 zone average** (`SUMMARY.md:403-405`).
- **R8-5 (pending worker, unrefereed)**:
  - Lemma C, charge rigidity in class 𝒢 (`R8-5_report.md:155-166`);
  - Theorem B, no box-confined vertex (`:168-174`);
  - BQ one-loop δc_e·16π² = −5.6 to −13.3 (`:225-238`).
  - Used below only where labelled.
- **Repository taste–dark-matter lane (historic)**: `docs/historic_intake/HISTORIC_DM_CLEAN_DERIVATION_NOTE_INTAKE_NOTE_2026-08-05.md:22,36`. Staggered tastes were proposed as dark matter. Its 2026-09-30 corrigendum finds that "no taste state is a gauge singlet" in the base × fibre embedding. Different construction (staggered Z³ tastes, not R7-1 corners); counted once. Lemma Q below reaches the same conclusion for R7-1's band from the gravity side.
- **Literature comparators:**
  - Nielsen–Ninomiya / Hamiltonian naive fermions with 2^d tastes (RECALLED);
  - Parker 1969; Chung–Kolb–Riotto 1998 (RECALLED);
  - the dark-matter EP bounds above (V).

---

## 3. Results

### 3.1 Lemma Q: universal gravity forces equal charge on box and edge. Proved (elementary); illustrated

- **Claim.** Assume H-grav and H-charge, with c(k) taking values in a discrete set. Then c is constant on T³.
- **Proof.**
  1. [T^{00}(q), Q] = Σ_k F^{00}(k+q, k)(c(k) − c(k+q)) a†_{k+q} a_k, so its vanishing requires F^{00}(k′, k)(c(k) − c(k′)) = 0 for all k, k′.
  2. Continuity and F^{00}(k, k) > 0 give a neighbourhood of every (k, k) where F^{00} ≠ 0. On it, c(k′) = c(k).
  3. So c is locally constant, hence constant on the connected torus. ∎
  - The same argument applies to a matrix-valued (non-abelian) one-body charge: F intertwines the representations, which are locally constant, hence constant.
- **Illustration** (`r91_edge_population.out`, part B). For a box-only charge, the commutator element across the face is F^{00} = 2.0543, 2.0543 and 2.0543 at δ = 0.05, 0.01 and 0.001, for both profiles. It does not vanish.
- **Consequence 1. G-in is unavailable for charged species.**
  - Gauge invariance (the Ward–Takahashi identity at zero transfer) pins a soft gauge vertex to the mode's charge. That is standard, and it is R8-5's Theorem B in lattice form (unrefereed).
  - So a box-supported vertex means a neutral edge. Lemma Q then forbids a neutral edge under universal gravity with exact charge conservation.
  - Every Standard-Model massive species carries hypercharge, weak isospin or colour. So for SM content, G-in collapses to G-out in both profiles.
- **The three exits (prices), named and not adopted:**
  - **(i)** non-universal gravity: R7-1's χ-cut stress, the refereed universality violation (`C5_R7-1_referee_verdict.md:212-219`);
  - **(ii)** a discontinuous F^{00} across the face: a non-quasi-local stress, with power-law real-space tails (suggested);
  - **(iii)** charge non-conservation in gravitational fields, with Gauss-law inconsistency for the gauge field.

### 3.2 Band facts in d = 3. Proved / checked (`.out` part A)

- **Flat edge mean (proved).** A = 0 on the box, because ε² = m² + k² there, and the zone mean of A is −I (Theorem E, refereed). Hence ∫_edge A = −(2π)³ I, and the flat edge mean of A_ii is exactly −1/f_edge, with f_edge = 1 − (b/π)³.
  - Checked: −1.35278 against −1/f_edge = −1.35278 (G), and −1.35285 (L, grid). This explains R8-2's "edge mean −1.35" (`C5_R8-2_report.md:140`) and shows it is profile-independent.
- **Group speeds (checked).**
  - L's edge has superluminal states, with max |v| = 4.12 (m = 0.3) and 4.17 (m = 0.05), in the descent region between k* and b₂.
  - G's edge is subluminal: max |v| = 0.997 (m = 0.3) and 1.000 (m = 0.05, at the face).
  - The box has max |v| < 1.
- **Thermal population (number-conserving Boltzmann; checked).**
  - **L.** f_edge → 7/8: 0.873 at T = 0.02/a, m = 0.3; 0.875 analytic. Each corner valley has exactly the box partition function up to O((Ta)²), because s = sin k on |k| ≥ b₂ gives ε² = m² + Σ sin²δ_i (proved, elementary).
  - **G.** f_edge = 8.9e-38, 4.9e-15, 1.9e-7, 1.2e-3 and 0.14 at T = 0.02, 0.05, 0.1, 0.2 and 0.5 (/a; m = 0.3).
- **Free-fall weight of what is populated (checked).**
  - **G.** The thermal edge population sits just outside the face, where A → 0 (C^∞ continuation of the box). Its energy-weighted ⟨tr A/3⟩ is −1e-4, −7e-3, −0.09, −0.39 and −0.86 at T = 0.02, 0.05, 0.1, 0.2 and 0.5. The equation of state is w = ⟨v²⟩/3 = 0.33 to 0.24, i.e. radiation-like.
  - **L doublers.** A_ii = cos 2δ_i − 1 = −2 sin²δ_i (proved; Finding D's weight 1 at rest, refereed). For physical momentum p, A ≈ −2(pa)². A halo top-doubler at v = 1e-3 has |A| ~ 4e-40.

### 3.3 Production (a)

**(i) Gravitational box → edge transitions (Lemma U), lab and thermal.**
- **G profile.**
  - In a static field, first-order real transitions conserve energy. Edge states have ε ≥ E_e ≈ √(m² + b²)/a (refereed ceiling; equality for the monotone G profile). So a body of box matter at E ≪ E_e cannot populate the edge (proved at linear order).
  - Lemma U's small-q couplings act only on states already within O(q) of the face, at energy ≈ E_e. Smooth forces move k continuously (k̇ = −ε∇Φ), so "entering the edge" means being accelerated to Planck energy.
  - The thermal fraction near the face is e^{−E_e/T} (part A). At T = 1 TeV with a = ℓ_P, this is e^{−2.4e16}.
  - The virtual admixture from Planck-transfer Newtonian exchange inside matter is of order (m/M_P)⁴(ℓ_P/r)³ ~ 1e-136 per nucleon pair. Suggested estimate; it refines R8-2's (m_N/M_P)².
- **L profile.**
  - Low-energy box → doubler conversion needs lattice-momentum transfer Q ∈ {0, π}³ \ {0}.
  - A single particle cannot convert: the graviton at Q costs |D(Q)|/a ≥ 2/a.
  - The two-body process X(k₁) + X′(k₂) → X_Q(k₁ + Q) + X′_Q(k₂ − Q) is kinematically open, since −Q ≡ Q. It proceeds by Newtonian exchange with the contact strength V_Q = 4πG F₁F₂ a²/|D(Q)|² (dust-kernel F^{00} = ½(ε + ε′) ≈ ε; `C5_R8-2_report.md:77`).
  - **Lab rate (computed):** inside a nucleus, Γ ~ 4e-132 s⁻¹ per nucleon. That gives a conversion fraction < 2e-114 over the age of the universe. The doublers fall with weight 1 anyway.

**(ii) Thermal equilibrium and freeze-in at T_max (L; computed).**
- **Cross-section.** With the golden rule in the CM frame, massless legs and lapse coupling: σ = (π/16) G² a⁴ s³ S_Q, where S_Q = Σ_Q |D(Q)|⁻⁴ = 3/16 + 3/64 + 1/144 = 0.24132 (checked).
- **Thermal average.** ⟨s³(1 − cos θ)⟩ = 9.22e4 T⁶ (Boltzmann; MC 9.228e4 against analytic 9.216e4; Fermi–Dirac 1.07e5).
- **Rate.** With n_tot = 11.6 T³ (SM degrees of freedom) and g* = 106.75: Γ/H = 2953 (T/M_P)⁷.
  - Doublers equilibrate (Γ = H) at T = 0.32 M_P = 3.9e18 GeV.
  - The freeze-in fraction is f_D = (Γ/H)/7 at T_max.
  - The full spin-2 head-on bound (κ = 8) gives Γ/H = 1.89e5 (T/M_P)⁷, with equilibrium at 0.18 M_P.
- **Abundance.** With doublers of mass m equal to the parent (the band-mass reading; see the variant below) and the SM spectrum:
  - Ω_D h² = 1.15e9 f_D (fermions), or 1.78e9 f_D (with W, Z, H).
  - Ω_D = Ω_c at T_max = 1.81–1.93e17 GeV (lapse) or 1.00–1.07e17 GeV (κ = 8).
  - Composition: top (62%), W (19%), Z (11%), H (5%).
  - At the BK18 inflationary reheating cap T_RH ≲ 5.8e15 GeV (computed from r < 0.036, A_s = 2.1e-9, instant reheating; `r91_qed_checks.out`): Ω_D h² = 4e-12 (lapse) to 3e-10 (κ = 8).
  - Equilibrium (T_max ≳ 3e18 GeV): f_D → 7, Ω_D h² ~ 1e10. Overclosure.
- **Variant L-Y.** If masses come from box-supported Yukawa vertices, the doublers are massless. Then ΔN_eff = 2.85 f_D, which is harmless until f_D ~ 0.1, i.e. T_max ≈ 0.3 M_P.
- **Scope.** Order-of-magnitude rate: one-graviton contact exchange, massless legs, Boltzmann statistics, SM degrees of freedom held up to 1e17 GeV, the graviton's lattice symbol a choice. The T_max values scale as (coefficient)^{−1/7}, so they are robust to O(1) factors (a factor of 64 in rate moves T by 1.8).

**(iii) Gravitational production in an expanding background.**
- **Proved (elementary).** In the number-conserving class every term of H is normal-ordered a†a or a†a†aa. So the empty vacuum stays empty for any time-dependent h_{μν}(t): production is exactly 0.
- **Comparator (RECALLED; with a Dirac sea).** Parker / Chung–Kolb–Riotto production of mass M ≫ H_inf is suppressed by roughly exp(−O(M/H_inf)). With E_e ~ 1e19 GeV and H_inf < 4.7e13 GeV (computed from BK18), it is negligible for G. For light L-doublers with a sea, production is like their parents', which is already covered by G-out.

**(iv) G-out gauge production.**
- **L.** The doublers are charged (Lemma Q; R8-5 Lemma C). With a sea they are pair-produced exactly like the parent.
  - **Z → each doubler pair (computed):** 7 × Γ(Z→ee) = +587 MeV, against Γ_Z = 2495.2 ± 2.3 MeV (RECALLED). That is about 255σ.
  - **Virtual effects, parameter-free (computed from RECALLED coefficients):**
    - δa_e = 7 × (119/36 − π²/3)(α/π)² = 5.9e-7, against σ = 1.3e-13 (V): 4.6e6σ;
    - α⁻¹(M_Z) → about 112, against about 128.95.
  - **Without a sea** (number-conserving G-out), conversion is the Coulomb-contact analogue of (ii), with Γ/H ≈ 6.5e-4 (T/M_P)³ (computed; it uses all-species n_tot, so it is an overestimate). The doublers are still charged mass-m electrons, and their abundance is then set by initial conditions. Not used for the exclusion.
- **G.** Gauge production of edge pairs needs √s ≥ 2E_e. Thermal production is ∝ e^{−E_e/T}, as in part D.

### 3.4 Fall, clustering and relics (b)

- **(1) Admixture η in test bodies.**
  - **Population channels:**
    - G: zero at linear order in static fields (3.3(i)); the virtual Newtonian admixture is ~1e-136 (suggested).
    - L: conversion ≤ 2e-114, with weight 1 − O((pa)²).
    - All far below 1e-15.
  - **Virtual gauge channel (G-out, both profiles; suggested, conditional).** O2's Lemma F gives β = Hess(E²/2)|₀ = c² for a dressed band. R8-5's unrefereed BQ loop gives δc_e·16π² = −5.6 to −13.3, so β_e − 1 = −6.5e-3 to −1.5e-2.
    - The Ti–Pt difference in electron mass fraction is 3.3e-5. With nucleons at β ≠ β_e, η ≈ 2–5e-7 from the electron share alone (`r91_qed_checks.out`).
    - The sector-additive reading is O2's, SUGGESTED (`C5_R8-2_report.md:35`). It needs R8-5's referee.
    - This is R8-2's "η ~ 1e-6 possible" (`C5_R8-2_report.md:185`), made definite. Unpopulated edges still act through loops, and the gap does not decouple them (R8-5 `:241-248`, worker).
- **(2) Relic gas.**
  - **L-doublers** (only in a priced or gauge-singlet variant): cold (w → 0 below T ~ m), collisionless, gravity-only. They fall with weight 1 to 1e-40, so they would cluster like CDM (suggested). Dark-matter EP bounds (10% for KK, 1e-5 for Cowsik et al.; V) pass by about 35 decades.
  - **G-edge relics:** hot (w = 0.33 at production; part A). Their near-face weight anomaly is small (|⟨A⟩| ≤ 0.09 for T ≤ 0.1/a). Deep-edge quanta fall up or anisotropically: A_ii down to −3.2 at the edge top (R8-2, refereed rerun).
    - Whether they survive expansion is OPEN. Gravitational decay at Planck energy is kinematically open for large-q transitions, because |D(q)| < |q| near π. If lattice momentum redshifts, edge quanta flow back into the box (suggested; FRW is outside the linear setting).
    - Part D's yields therefore assume stability and are upper bounds.
    - **G bound (computed, part D):** stable edge relics with equilibrium yield at T_max have log₁₀ Ω_edge h² = −57.3, −14.1, +0.25 and +11.6 at T_max = 0.01, 0.02, 0.03 and 0.05 /a. So Ω_edge h² < 0.12 for T_max ≲ 0.03/a ≈ 3.5e17 GeV (a = ℓ_P).
    - Charged-relic searches at Planck mass are not checked (RECALLED: none apply directly).
- **(3) Doublers under G-in** as gravity-only mass-m copies of every species. This configuration is **not available for gauge-charged species** (Lemma Q). It applies only to gauge singlets (none massive in the SM; sterile ν if present), or under exits (i)–(iii). Its DM-EP status is as in (2).

### 3.5 Momentum balance (c). Proved (semiclassical); operator part proved; checked

- **Exact, proved.** The full linear-order law, matter plus Newtonian lapse exchange V = Σ T^{00} G T^{00}, is lattice-translation invariant. So the total crystal momentum (mod 2π) is conserved.
- **Semiclassically:** k̇_i = −ε_i∇Φ_j. The push on crystal momentum is energy × field, equal and opposite for the two bodies. Active mass is the source ∫T^{00} = H (Construction A, refereed), and the passive "charge" is energy. Both are universal.
- **Theorem E's extra term is inertial.** p = ∇(ε²/2) = εv, and dp/dt = Hess(ε²/2)·k̇. The term dΓ(εA) is the anomaly in the k → v map (inertia), not in gravitational charge (proved from Theorem E's identity, `C5_R8-2_referee_verdict.md:33-43`).
- **Where the momentum goes.** It does not go into the static field: the field carries no momentum at this order. Crystal momentum is conserved. The gravitating momentum J_E = ∫T⁰ⁱ (the energy current, which sources gravitomagnetism) is not conserved: d(J_E,1 + J_E,2)/dt = F(A₂ − A₁) along the line of centres. The energy centroid of a box + edge pair self-accelerates.
- **Checked** (part E, d = 1, RK4, separation 60, G·ε₁ε₂ U):
  - total k drift ≤ 1.4e-13 in every run;
  - d²(ε₁x₁ + ε₂x₂)/dt² = −1.2069e-6 against F·A₁ = −1.2069e-6 (gapped edge top, A₁ = −3.20);
  - −9.62e-6 against −9.58e-6 (literal s-maximum, A₁ = −31.3);
  - ≈ 3e-13 for box + box and doubler + box (A₁ = 0).
- **Reading.** A non-conserved ∫T⁰ⁱ in an external field is the W3/W4 failure seen from the source side. Linearized GR's next-order (Bianchi) consistency needs ∂_μT^{μν} = −ΓT with A = 0, so the edge is incompatible with consistent second-order coupling. This is suggested; the local-lapse algebra W4 is open (`TESTS:3405`).

---

## 4. Against the FIXED readings (`TESTS.md:3632-3634`)

| profile / gauge | population | worker reading |
|---|---|---|
| **L, G-out** | 7 charged mass-m copies per charged species, for every a, b, b₂, m. Z width +587 MeV (255σ); a_e +5.9e-7 (4.6e6σ); α⁻¹(M_Z) ≈ 112 | **EXCLUDED** (referee required). Matches the expectation (`TESTS:3638`) |
| **L, G-in** (as posed, SM content) | Inconsistent: universal gravity plus charge conservation forces a charged edge (Lemma Q), so G-in collapses to G-out | **EXCLUDED** for gauge-charged species (referee required). Departs from the expectation "OPEN leaning HARMLESS" (`TESTS:3639`) |
| **L, G-in, priced** (gauge singlets; or exits (i)–(iii)) | Gravity-only cold copies; f_D = 422 (T_max/M_P)⁷ (lapse) | **HARMLESS** for T_max ≤ 1.0e17 GeV (both couplings; a = ℓ_P), Ω_D h² < 0.12, checked. **DARK-CANDIDATE (lead, not adopted)** for T_max ≈ 1.0–1.9e17 GeV: Ω_D = Ω_c, DM-EP passes by about 35 decades, cold. **EXCLUDED (overclosure)** for T_max ≳ 2e17 GeV |
| **G, G-out** | Boltzmann-suppressed. Stable-relic upper bound Ω_edge h² < 0.12 for T_max ≲ 0.03/a (3.5e17 GeV); lab population 0 at linear order | **HARMLESS** for T_max ≲ 3.5e17 GeV (checked); **OPEN** above. Not DARK-CANDIDATE: the relic is hot, with stability and redshift OPEN. **Caveat:** the virtual-loop η ~ 2–5e-7 (suggested; conditional on R8-5 plus O2 Lemma F) fails MICROSCOPE independently of population |
| **G, G-in** | Collapses to G-out for charged species (Lemma Q). For singlets, as G-out without the loop caveat | as G-out |

**The DARK-CANDIDATE lead carries prices:**
- one of exits (i)–(iii), or gauge-singlet species only;
- a hot phase at T_max ~ 1e17 GeV, about 17 times the BK18 instant-reheating cap: no standard single-field inflation after it;
- doubler masses equal to band masses (not Yukawa-generated).

The amount is tuned through T_max; the composition (t : W : Z : H ≈ 62 : 19 : 11 : 5) would be a prediction.

**Expectation check.**
- G: HARMLESS for T_max ≪ E_e, and OPEN near Planckian T. As expected.
- L/G-out: EXCLUDED. As expected.
- L/G-in: the expected OPEN/HARMLESS is replaced by Lemma Q's collapse to EXCLUDED for charged content. The computed DARK-CANDIDATE survives only in the priced variant.

## 5. Prices (named, not adopted)

- **P-R9a** (for any surviving L): a gauge-singlet matter content, or exits (i), (ii) or (iii) of §3.1.
  - (i) is R7-1's refereed universality violation.
  - (ii) is a non-quasi-local stress.
  - (iii) is gravitational charge non-conservation.
- **P-R9b** (DARK-CANDIDATE): T_max ≈ 1–2e17 GeV with no BK18-compatible inflation afterwards; band-parameter masses.
- **P-R9c** (G): the population is harmless, but G-out loops reach the edge virtually. Passing MICROSCOPE then needs a per-species speed counterterm at about 1e-8 relative (η budget 1e-15 against the electron share 3.3e-5 × 2δc_e), or R8-5's unbuilt custodial vertex structure. Suggested; conditional on R8-5's referee.
- No axiom text changes. Admissibility fixes no dynamics, stress or charge (`AX:114-130`), and source and gauge bridges are outside the axioms (`AX:173-190`).

## 6. Strong-word check

- **"Proved":**
  - Lemma Q: continuity plus a positive diagonal plus a discrete charge;
  - the flat-edge-mean identity;
  - the 7/8 limit;
  - zero vacuum production in the number-conserving class;
  - no lab population for G at linear order in static fields;
  - crystal-momentum conservation;
  - the inertial reading of Theorem E's term.
- **"Collapses to G-out"** additionally uses the WT identity at zero transfer (standard; R8-5 Theorem B, unrefereed).
- **"Computed"** rates are order-of-magnitude golden-rule estimates, with their approximations stated in §3.3(ii). T_max thresholds are insensitive (power 1/7).
- **"EXCLUDED" for L/G-out** uses RECALLED SM numbers (Γ_Z, Γ_ee, the VP coefficient) and verified a_e. It assumes a Dirac sea (BQ class). Without a sea, see §3.3(iv).
- The **η ~ 1e-7 loop channel** is suggested. It rests on R8-5's unrefereed δc_e, O2's suggested sector additivity, and Lemma F.
- The **two-body centroid result** is semiclassical. Theorem E's arbitrary-k acceleration is semiclassical per its referee (`C5_R8-2_referee_verdict.md:45`).
- **"a = ℓ_P"** is a reading throughout.

## 7. For the referee

1. Lemma Q's hypotheses: is [T^{00}(x), Q] = 0 the right requirement? Does R8-2's F^{00} meet continuity (Construction A, glued kernel)?
2. The step "box-supported gauge vertex ⇒ neutral edge" (WT at q → 0).
3. The conversion cross-section normalization: CM golden rule, v_rel = 2, Møller factor 1 − cos θ, S_Q.
4. Whether the L/G-out exclusion counts as "computed population" (Z → doublers) under the fixed clause.
5. Whether the G-out loop channel should change G's reading from HARMLESS to EXCLUDED once R8-5 is refereed.

## 8. Files

- `S/scripts/r91_edge_population.py`, `.out`:
  - (A) band geometry, thermal fractions, A and w;
  - (B) Lemma Q illustration;
  - (C) doubler conversion and Ω_D(T_max);
  - (D) G-edge relic bound;
  - (E) two-body momentum balance.
- `S/scripts/r91_qed_checks.py`, `.out`: QED, free-fall and inflation arithmetic.

**Sources (web, this run).**
- [MICROSCOPE final, arXiv 2209.15487](https://arxiv.org/abs/2209.15487)
- [Planck 2018 VI, arXiv 1807.06209](https://arxiv.org/abs/1807.06209)
- [Kesden & Kamionkowski, astro-ph/0608095](https://arxiv.org/abs/astro-ph/0608095)
- [Kesden 2009, arXiv 0903.4458](https://pdf.arxiv.org/pdf/0903.4458)
- [Cowsik et al., arXiv 1808.09925](https://arxiv.org/pdf/1808.09925)
- [BK18, arXiv 2110.00483](https://arxiv.org/pdf/2110.00483.pdf)
- [Fan et al. 2023, arXiv 2209.13084](https://ar5iv.labs.arxiv.org/html/2209.13084)
