# C5 R12-2 report: site creation and Λ. Can a local rule that creates sites track the expansion and fix the vacuum value without tuning?

**Worker.** Claude Opus 5.5 (same family as the supervisor and every C5 worker). Unrefereed. 2026-10-12, 19:06Z to 19:42Z. No repository file was edited.

**Scratch.** `S/` = `.../scratchpad/C5/R12-2/`. Scripts and outputs are in `S/scripts/`. Each runs in under 5 s at `OMP_NUM_THREADS=2`.
- `r122_frw_rules.py/.out`: homogeneous creation laws through a vacuum step: A (algebraic in ρ_tot), U (Ḣ law), E (equation-of-state rule), P (time-derivative/Prony rule), R (vacuum-blind Raychaudhuri law), F (hybrid), GR control. Also the stability of the derivative feedback.
- `r122_ordered_creation.py/.out`: deterministic integrate-and-fire creation with low-discrepancy (quasi-periodic) phases, against random phases and the Yule (Poisson) process (1D).
- `r122_numbers.py/.out`: Lemma CR numbers; dislocation-climb line density; Yule (Poisson) insertion noise and wavefront phase; the mixture estimator (Cauchy–Schwarz); the ΛCDM inverse problem; EW-step sizes, curvature kick and freeze epochs; the cubic Schur check; the grid zero-point under rule E.

**Read.**
- In full: `docs/MINIMAL_AXIOMS_2026-06-29.md` (`AX`); the R12-2 registration (`TESTS.md:4351-4363`); `agents/C5_R11-3_report.md`; the R11-3 referee verdict (`.../C5/ref_R11-3/REFEREE_VERDICT.md`, now recorded at `TESTS.md:4417-4424`); `agents/C5_R10-4_report.md` and its referee verdict.
- In part:
  - `TESTS.md:2302-2420` (C5 method, round 1), `:2847-2858` (R4-5), `:2886-2898` (R5-3), `:2938-2945` (R4-5 result), `:2985-2993` (R5-3 result), `:3106-3130` and `:3420-3428` (R6-3), `:4000-4012` (R10-4), `:4157-4188` (R11-3), `:4297-4332`;
  - `agents/C5_O3_report.md:70-110,180-215` and `C5_O3_referee.md`;
  - `PRICE_NOTE.md:307,367` (P13);
  - `agents/C5_R4-5_report.md:130-150` and `C5_R4-5_referee.md:105-117`.
- Prior art in `docs/` (grep "site creation", "refinement", "lattice growth", "expanding lattice", "growing graph", "graph growth"), listed in §3.

**Labels.** proved / checked (numerics here) / suggested / reading / comparator. A comparator is *verified* if fetched this run, and *RECALLED* if from memory.

**Subtraction rule (`TESTS.md:4074`).** "Vacuum" always names its reference. ρ_v is the time-constant part of the local stress along a site's worldline (V3 with creation keeps the spacing fixed, so the zero-point per site is constant). "Λ_eff" is the late-time limit of 3H² − κρ_nc, where ρ_nc is the true radiation plus matter content. There are no decay or tail clauses.

---

## 0. Verdict against the FIXED readings (`TESTS.md:4360-4363`): **OPEN**

**Not VIABLE.** I found no explicit local rule that gives Friedmann expansion *and* ⟨Λ⟩ = 0 untuned *and* passes every stated check.

The best construction is the **F-law**: a vacuum-blind time-derivative reading of the content, plus a per-site curvature memory (§4.4). It meets most of the checks:
- Λ_eff = 0 untuned across phase transitions (proved, homogeneous sector);
- exact Friedmann expansion for any finite mixture of constant-w components (proved);
- comoving structure growth up to turnaround (proved, as GR's separate universe);
- the rapidity budget is fixed (reading, from R11-3);
- the mean expansion is isotropic (proved).

It stays open, or fails, on four points:
- **(i) Redshift by local insertion.** Poisson-timed insertion is the random-walk foam model, which Chandra data exclude (§4.6). Ordered creation passes: deterministic integrate-and-fire with a quasi-periodic initial phase field has count error O(log N) (Koksma–Hlawka; checked in 1D). But it needs an ordered initial state of unexplained origin, and the 3D defect geometry is not built.
- **(ii) Bound structures.** Turnaround needs site destruction, which Record permanence forbids, so sites must freeze and decouple from collapsing matter. That sector is not computed.
- **(iii) Inhomogeneous vacuum changes.** A constraint-form version is inconsistent with them at linear order: proved around Minkowski given refereed Lemma BR; suggested around FRW (§4.5).
- **(iv) No constant component gravitates.** Observed acceleration therefore needs dynamical dark energy with w ≠ −1.

**Not EXCLUDED.** The exclusions below are bounded to stated classes. None covers every local creation rule, and none is refereed yet.

**Bounded sub-results, each for the referee:**
- **(L-CR) Creation is forced (proved).** Fixed volume per site plus timelike sites plus a homogeneous grid force creation at mean rate exactly 3H per site. Without creation every ball of sites has proper radius below 1/H; the last-scattering sphere had HR = 66.3 at emission.
- **(L-hom) The creation law is the Friedmann equation (proved).** In V3 with creation, FRW leaves a(t) unconstrained by the imposed gravity equations.
- **(PT-s) Laws reading ρ_tot reproduce Lemma PT (proved; checked).** This covers laws algebraic in ρ_tot with a law constant or an inherited per-site C, and the Ḣ law (unimodular). After a vacuum step Δ, Λ_eff shifts by −κΔ (to 1 in 4.6e54 at EW). The branch that would have negative Λ_eff **freezes** instead of crunching, because sites cannot be destroyed.
- **(CS) The equation-of-state rule underestimates mixtures (proved: Cauchy–Schwarz).** It is blind to w = −1 vacua, and H is up to 1.03% low at matter–radiation equality. On the Z³ grid it sees the zero-point (w ≥ 0, R11-3 refereed), which gives H ~ 3/t_P per real scalar.
- **(K) Every continuous-H vacuum-blind law with memory gets a curvature kick (proved; checked).** Each latent-heat release kicks the integration constant by −κΔ/3. At EW this grows to |Ω_K0| ≈ 7.6e23, or the universe freezes at T ≈ 11.5 GeV. EXCLUDED, bounded to that class.
- **(G) Memoryless laws kill structure growth for comoving sites (proved, linear).** δ ∝ a^{−3/2} instead of a.
- **(Foam) Poisson-timed local insertion is the α = 1/2 random-walk foam model (checked; comparator verified).** At z = 1 the optical phase std is 520 rad and the 1 keV X-ray phase std is 2.1e5 rad. EXCLUDED by the Chandra imaging of distant quasars, bounded to independent insertion timing.

**Against the registered framing (`TESTS.md:4352`).** The dichotomy "fixed C brings back Lemma PT, vacuum-tracking C is P13" is **not exhaustive**. There is a third option: the creation law reads only the *time variation* of the local stress along the site worldline. With fixed spacing, every vacuum, including the grid's w ≥ 0 zero-point, is time-constant per site, so it is invisible without any reference value or reference state. It removes the tuning but creates the problems listed above. I name it as a new price, **P-T** (§5).

---

## 1. In plain words

- **Why sites must be created.** If each site always holds the same volume of space (R11-3's V2/V3), space can grow only by adding sites. This is forced, not optional. Without new sites the grid points would have to rush toward one another faster than light anywhere farther apart than the Hubble distance. The patch of sky where the CMB was emitted was 66 Hubble radii across at the time.
- **The rule *is* the expansion law.** On such a grid the remaining gravity equations say nothing about the overall expansion. Whatever rule creates sites *is* the Friedmann equation. So the rule must "know" how much matter and radiation there is.
- **The trap.** If the rule reads the total local energy, it also reads the vacuum's huge energy. Cancelling that with a fixed number fails after the next phase transition (Lemma PT again). Half of all mistuned cases do not crunch: they **freeze**, because sites cannot be removed. That is the owner's "count rises until frozen", but it would have happened at T ≈ 45 GeV.
- **A way out.** On this grid the vacuum's energy per site never changes, because the spacing is fixed. A rule that responds only to how the local energy *changes in time* cannot see the vacuum at all, whatever its value or pressure. With enough time derivatives it can still work out the full matter and radiation content exactly, so the Friedmann expansion comes out right and the vacuum never gravitates. No number is tuned.
- **What breaks.**
  - **(1) Galaxies.** A rule with no memory cannot let overdense regions lag behind the average expansion, so galaxies never form. Adding a per-site memory of local curvature fixes this. But collapsing regions would then need sites removed, which records forbid, so sites must freeze in bound regions.
  - **(2) Light.** If new sites pop in at random places, light from distant quasars arrives with its wavefronts scrambled, and the quasars would not appear sharp in X-ray images. Creation must be ordered, almost like a crystal. A deterministic clock on each site, started in a quasi-periodic pattern, is quiet enough, but someone has to set up that pattern.
  - **(3) Dark energy.** A true cosmological constant is exactly what this rule cannot see. The observed acceleration must come from dark energy that changes in time (w ≠ −1). DESI hints at this, but the size is not explained.
  - **(4) Uneven transitions.** If the vacuum changes unevenly from place to place, the rule's bookkeeping clashes with the other gravity equations (suggested).

---

## 2. Hypotheses and classes (stated before titles)

- **H-V3c (setting).** R11-3's V3: fixed lapse, fixed proper volume v₀ = a³ per site on the slice, with traceless h_ij and shift dynamical. Add a site-creation law. Sites carry the cosmological grid, and a = ℓ_P at every epoch.
  - The imposed gravity equations are R11-3's: E_0i = 0 and E_ij^TL = 0 (`C5_R11-3_report.md:180-185`). Lemma BR is refereed as confirmed with corrections (`TESTS.md:4417-4424`).
  - V2 (free lapse) is covered only where stated.
- **H-hom.** The cosmological site state is statistically homogeneous and isotropic on the homogeneous (cosmic-time) slices of FRW. This is the reading of "no site is privileged" (`AX:40-41`) for the state.
- **H-perm.** Destroying a site that holds a record violates "records are permanent" (`AX:79-80`). So c ≥ 0 wherever sites are recorded. I assume this cosmologically, and call it a reading for unrecorded sites.
- **H-vac.** Vacuum steps are modelled as a change of a time-constant ρ_v with the latent heat going into radiation. This is stated, not derived (R11-3 referee finding 4).
- **H-read.** A creation law may read local expectation values of the stress and their time derivatives along the site worldline. It may also carry finitely many per-site memory variables. Reading T_μν needs a source/action bridge (`AX:186-187`, open gate). That is a price, not a premise.
- **Excluded:**
  - nonlinear inhomogeneous gravity inside bound objects;
  - first-order bubble dynamics (only crossovers and smooth steps are modelled);
  - quantum fluctuations of the creation process, except §4.6;
  - records as a q-charge (R10-4);
  - pairing constructions (R10-5, R12-3).

---

## 3. Prior art (each counted once)

1. **R11-3** [refereed, `TESTS.md:4417-4424`].
   - V2/V3 on fixed sites cannot realize metric FRW expansion, and site creation is an open additional law.
   - V3 absorbs (ρ, p) into C(x), f(t).
   - The worker's numbers: 8.5e184 cells, 3H₀N ≈ 5.6e167 s⁻¹, and the rapidity budget η* = 45.4 fixed with creation (`C5_R11-3_report.md:212-236`).
   - Referee finding 5: the finite-step ratio Δp/Δρ lies in [−0.833, −0.175] across L–G, so the grid step is never w = −1.
2. **R5-3 Lemma PT** [ref] (`TESTS.md:2986-2987`). Also **R10-4 Lemma PT-q** and its §4.5 Bianchi failure for linear-in-q vacuum energy [ref] (`TESTS.md:4297-4301`; `C5_R10-4_report.md:151-177,232-239`).
3. **O3 #5/#12 and P13** [ref] (`C5_O3_report.md:87,97,104`; `PRICE_NOTE.md:367`). A rule removing vacuum gravity must subtract only the state-independent vacuum c-number (EP).
4. **R4-5** [ref]. Lemma C-count (`TESTS.md:2941`; `C5_R4-5_report.md:141`). The referee states that monotone refinement keeps the spatial cap, and that a replaceable 4D event site changes Lattice/Record (`C5_R4-5_referee.md:111-117`).
5. **R6-3** [ref] (`TESTS.md:3420-3428`). Suppressed count noise needs order (V′). This is the same trade-off as §4.6.
6. **Q1** [ref] (`TESTS.md:2415-2419`). Random microstructure seen by coherent waves gives intensity noise. §4.6 is the site-creation instance.
7. **`docs/` grep.**
   - `GROWING_GRAPH_EXPANSION_CARD_NOTE.md` and `GROWING_GRAPH_EXPANSION_SKEPTIC_AUDIT_NOTE.md` (2026-04-05/06). Frontier (boundary) growth of a toy graph, retained as a "graph-distance proxy", with the de Sitter wording demoted. It is boundary growth, not bulk insertion, and has no vacuum or redshift content.
   - `CHIRAL_WALK_SYNTHESIS_2026-04-09.md:172`: "Expanding lattice doesn't stretch separation (walk too localized)". This is a redshift/stretching failure on an older growing lattice, consistent with §4.6's point that stretching needs an encoder.
   - `DARK_ENERGY_EOS_NOTE.md:204`: Model C "volume growth R ~ a^α → w = −1 + 2α/3, ruled out". If Λ = 3/R² with R tied to the site count, creation makes w ≠ −1. The spectral-gap route and site creation conflict unless R is not the grid size. Its falsifier is at `COSMOLOGICAL_CONSTANT_RESULT_2026-04-12.md:106-107`.
   - `historic_intake/HISTORIC_NS_SPECTRAL_TILT_DERIVED_NOTE_INTAKE_NOTE_2026-08-05.md:19`: "lattice growth" n_s. This is an unaudited historic intake, not used.
   - No `docs/` note treats a site-creation law, the value assigned to new sites, or creation noise.
8. **Comparators.**
   - **Verified this run:**
     - Cotler–Strominger, "The Universe as a Quantum Encoder", arXiv:2201.11658: expansion as isometric (non-unitary) evolution adding modes, argued in 1+1D toys.
     - Perlman et al., ApJ 805, 10 (2015), arXiv:1411.7262: Chandra gives α ≳ 0.58, which rules out the random-walk (α = 1/2) foam model; Fermi and TeV data give α ≳ 0.67 and 0.72.
     - DESI DR2 (arXiv:2503.14738; verified by the R10-4 referee, `agents/C5_R10-4_referee_verdict.md:21`).
   - **RECALLED:**
     - Rideout–Sorkin classical sequential growth (gr-qc/9904062): births with label invariance, no embedding lattice;
     - quantum graphity (Konopka–Markopoulou–Severini 2008): a graph cools to a lattice, with no bulk insertion;
     - Bianconi–Rahmede growing network geometries;
     - Jacobson, "Trans-Planckian redshifts and the substance of the space-time river"; Weiss 1987 (fixed physical cutoff: new modes enter in their ground state);
     - Hirth–Lothe on dislocation climb, the crystal-growth mechanism.

---

## 4. Results

### 4.1 Lemma CR: creation is forced, at rate exactly 3H (proved; numbers checked)

**Statement.**
- Assume H-V3c and H-hom on flat FRW with H > 0, using cosmic-time slices. These are the only homogeneous slices, and they have N = 1.
- Let sites move with coordinate velocity V^i, so their proper velocity relative to comoving observers is W = aV, and they are timelike iff |W| < 1. Let c be the creation rate per site.
- Site-number balance at fixed proper density 1/v₀ gives **c = 3H + ∂_iV^i**, exactly.
- **(i) Without creation (c = 0).** Over any comoving ball of proper radius R, the mean inward |W| on the boundary equals HR. Timelike sites therefore need R < 1/H for every ball of sites. Flat FRW slices are unbounded, so this is a contradiction.
- **(ii) With creation.** Under H-hom the flux term has zero mean (an isotropic homogeneous vector field), so **c̄ = 3H**.

**Numbers (checked, `r122_numbers.out` §(a)).**
- At emission, HR = 0.68 at z = 1, 1.00 at z = 1.6 (the past light cone touches the Hubble sphere there), 1.67 at z = 3, and **66.3 at last scattering**.
- 3H₀ = 6.58e-18 s⁻¹ = 3.5e-61 per site per Planck time (matches R11-3, `C5_R11-3_report.md:227`).

**Scope.** This sharpens R11-3's refereed "cannot realize metric FRW expansion" into a rate. For V2 (free lapse), slicings with K ≈ 0 are not covered, and I do not claim it.

### 4.2 Lemma L-hom: the creation law *is* the Friedmann equation (proved)

- In FRW, E_0i ≡ 0 and E_ij^TL ≡ 0 identically by symmetry. So the imposed V3 equations leave a(t) free.
- The nonlinear homogeneous Bianchi identity reads Ẋ + 3H(X + Y) = κ(source), with X = E_00 and Y = f(t) unimposed. It is satisfied for any a(t).
- **So a(t) = (site count)^{1/3} is fixed by the creation law alone.** (a) asks whether a local law can be Friedmann's.

**Mapping to "the value C assigned to new sites".**
- At linear order R11-3 has E_00 = C(x). Here X = 3H² − κρ_tot.
- Specifying C on new sites, as a law constant, inherited from parents, or vacuum-tracking, is equivalent to the algebraic law 3H² = κρ_tot + C (proved by definition).

### 4.3 Laws that read ρ_tot: Lemma PT-s (proved; checked)

**Class A: H² = (κ/3)(ρ_tot − ρ_ref).** ρ_ref = −C/κ is a law constant or is inherited along site lineages, so a transition does not change it.
- Late-time Λ_eff = κ(ρ_v,final − ρ_ref).
- **Checked** (`r122_frw_rules.out`, κ/3 = 1, V0 = 1):
  - ρ_ref tuned for Δ = 0.3 gives X → 0.000000 at Δ = 0.3;
  - the same law at Δ = 0.7 **freezes**.
- If ρ_v,final < ρ_ref, then H² hits 0 while matter remains. GR would turn around (AdS crunch, `C5_R10-4_report.md:194`). Here c ≥ 0 (H-perm), so creation stops and the universe **freezes**.
- At the EW step (`r122_numbers.out` §(e); inputs RECALLED): ΔV = m_H²v²/8 = 1.18e8 GeV⁴ = 4.6e54 ρ_Λ (matches `TESTS.md:2986`). The mistuned branches either become Λ-dominated with H = 2.6e-15 GeV (1/(2.6e-10 s)) or freeze at T ≈ 45 GeV. Both are excluded by BBN (reading).

**Class U: Ḣ = −(κ/2)(ρ + p)_tot.** This is vacuum-blind for w = −1, and it is the homogeneous unimodular law.
- C = H² − κρ_tot/3 is conserved (proved), and checked to 4e-7 through the step (`r122_frw_rules.out`: −0.700000164).
- Late Λ_eff = κρ_v,final + 3C. It is Lemma PT exactly: "vacuum-blind" by ρ + p does not help.

**Class "records-only"** (O3 #12: the creation rate reads record density, which is the axiom-native vacuum-blind reading).
- Permanent records plus new unrecorded sites give n_rec ∝ a^{−3} × (non-decreasing comoving count) (proved from `AX:79-80`).
- So any H² = F(n_rec) with fixed F gives H as a fixed function of the comoving record history. The radiation era (H² ∝ a^{−4}) and the matter era (∝ a^{−3}) need different powers of n_rec. Reproducing both needs a tuned function F that encodes Ω_r/Ω_m (suggested).
- The owner's "records forming on new sites drive the expansion" (`TESTS.md:4353`) therefore does not track Friedmann without tuning (suggested).

### 4.4 Vacuum-blind laws (the third option)

**Rule E (equation of state):** H² = (κ/3)(ρ + p)/(1 + c_s²), with c_s² = dp/dρ.
- Exact for one constant-w component on any w = −1 vacuum (proved).
- For mixtures, **H²_E = (κ/3)(Σ(1+w_i)ρ_i)²/Σ(1+w_i)²ρ_i ≤ (κ/3)Σρ_i**, by Cauchy–Schwarz (proved; sympy identity `r122_numbers.out` §(d)).
- Radiation plus dust: H is low by up to 1.03%, at ρ_m/ρ_r = 4/3 (checked).
- Dust plus dark energy today: the estimator gives 0.38 (w = −0.95), 0.45 (w = −0.9) and 0.66 (w = −0.75) of the true density (checked).
- **No constant-w content reproduces the observed acceleration under E.** By Cauchy–Schwarz such content always gives H²_E ≤ (κ/3)Σρ_i, and a true Λ is invisible.
- Forcing a ΛCDM H(z) under E (inverse problem, checked) needs a dark component with (ρ + p)_D ≈ 0.28–0.34 ρ_c0 over most of the history. Its ρ_D falls by 6.9 ρ_c0 after z = 999, so ρ_D(z = 999) ≥ 7.0 ρ_c0 is needed to keep ρ_D ≥ (ρ + p)_D/2 today.
- That component has time-varying w and a negative adiabatic sound speed. This is not excluded by this computation, but it is contrived (reading). Rule P avoids the issue.
- **On the Z³ grid, E fails outright.** The zero-point has ρ + p = −⟨ε tr A⟩/6 > 0 (R11-3 Identity W and Corollary P, refereed with scope `TESTS.md:4418`). It is 2.07, 1.85 and 1.40 per real scalar in lattice units for L, G and NN, so H ≳ 3/t_P per real scalar (`r122_numbers.out` §(g)). Subtracting it with a law constant fails at the first mass step, since Δp/Δρ ∈ [−0.833, −0.175] (R11-3 referee) gives Δ(ρ + p) ≠ 0. That is Lemma PT per species, unless exact pairing removes the zero-point entirely (O3, R10-5).

**Rule P (time-derivative / Prony):**
- With fixed spacing every vacuum is time-constant per site. So m_k ≡ (−d/d ln a)^k ρ_tot (k ≥ 1) see only the diluting content: m_k = Σ x_i^k ρ_i with x_i = 3(1 + w_i).
- The measure μ = Σ(ρ_i x_i)δ_{x_i} gives zero weight to x = 0. Prony on m_1..m_{2N} recovers μ, and **ρ̂_nc = ∫dμ/x = Σρ_i, exactly, for any N constant-w components** (proved).
- The rule is H² = (κ/3)ρ̂_nc.
- The site knows its own c = 3H, so d/d ln a = (3/c)d/dt is local.
- It is blind to the vacuum's value *and its pressure*, so the grid's w ≥ 0 zero-point is invisible.
- **Checked** (`r122_frw_rules.out`):
  - |H²/ρ_nc − 1| ≤ 2e-7 after the transient;
  - X/ρ_nc = 1.7e-16 at u = 8 for both Δ = 0.3 and 0.7;
  - a Λ-like residual would give ~1e10;
  - **untuned.**
- First-derivative variant (D-rule, H³ = −κρ̇²/(9(ρ̇ + ṗ))): it equals E on the time-varying part. As a feedback H ← (H H_F²)^{1/3} it is stable with slope 1/3 (proved, sympy).

**Lemma G (proved, linear; sites comoving with dust).**
- For any memoryless law c = F(local data) whose homogeneous restriction is Friedmann (F increasing in density), continuity gives δ̇ = −δc.
- For dust, H_loc² = (κ/3)ρ(1 + δ), so δc = (3H/2)δ and δ ∝ a^{−3/2}. GR has δ ∝ a.
- The growing mode is the local curvature, which is an integration constant. Memoryless laws cannot carry it.
- Scope: if sites do not comove (matter flows through sites), growth is set by the non-creation equations. That case is OPEN.

**Lemma K: the curvature kick (proved; checked).**
- Take any vacuum-blind law with memory and continuous H whose late form is H² = (κ/3)ρ_nc + X with X = O(a^{−2}), e.g. the vacuum-blind Raychaudhuri law Ḣ = −H² − (κ/6)(ρ + 3p)_nc. A latent heat Δ entering ρ_nc at fixed H gives **ΔX = −κΔ/3**.
- **Checked** (`r122_frw_rules.out`, R): X a² = −0.286 (Δ = 0.3) and −0.605 (Δ = 0.7) after the step; the smoothed release gives Δ⟨a²⟩. The law then freezes at u = 2.4 and 2.0.
- **EW (inputs RECALLED).** Δ/ρ_r(160 GeV) = 5.1e-3. It grows to **|Ω_K0| = 7.6e23**, against DESI DR2 10³Ω_K = 2.3 ± 1.1 (`TESTS.md:2993`). In practice the closed radiation universe stops at a_max/a_T = 14, i.e. it **freezes at T ≈ 11.5 GeV**.
- **EXCLUDED for this class** (bounded: continuous H, memory carried in X, latent heat into radiation).

**The F-law (hybrid; best candidate):** H² = (κ/3)ρ̂_nc + X, with X a per-site memory obeying Ẋ = −2HX, and c = 3H ≥ 0.
- **(i) Untuned.** ρ̂_nc is memoryless, so latent heat raises H at once. H jumps and X is not kicked (proved; `r122_frw_rules.out` F: X a² = 1.8316e-05 conserved through both steps, trivially by construction).
- **(ii) Exact Friedmann** for constant-w mixtures plus a curvature-type X (proved).
- **(iii) Comoving dust.** H_loc² = (κ/3)ρ_loc + X_loc is GR's separate universe, so the growing mode is present (proved, top-hat level).
- **(iv) Turnaround.** GR needs H_loc < 0, which H-perm forbids. Sites in bound regions freeze (c = 0) and matter then collapses through frozen sites.
  - At linear order around Minkowski, R11-3's Lemma BR uses only the imposed E_0i, E^TL, the Bianchi identity and conserved *full* T. None of these depends on which components are frozen. So δE_00 = δC(x) stays static whatever the creation pattern, and local Newtonian gravity is GR's for δC = 0 (suggested: an extension of refereed Lemma BR, not separately computed).
  - The nonlinear collapse through frozen sites is **not computed** (OPEN).
- Reading: this is a literal "count rises until frozen" for every bound structure, tested only as a hypothesis. It is not specific to black holes.
- **Pre-transition behaviour.** The pre-transition vacuum does not gravitate either. H² before EW lacks GR's +κΔ (0.5% of ρ_r), and before the QCD crossover it lacks the bag term. No current observation measures H at those epochs (reading).

### 4.5 Inhomogeneous vacuum changes: Lemma B-loc (proved around Minkowski, given refereed Lemma BR; the FRW version is suggested, signs for the referee)

- Write E_μν = G_μν − κT^vis_μν, where T^vis excludes the vacuum. Bianchi gives ∇^μE_μν = κJ_ν with J_ν = −∂_νρ_v.
- In V3 with creation, suppose the law *enforces* the vacuum-blind Hamiltonian constraint (δE_00 = 0), with δE_0i = 0 and δE^TL = 0 imposed.
- The ν = j component gives δE_kk = −3κδρ_v + const. The ν = 0 component around FRW gives −H δE_kk ∝ κ δJ_0.
- Together they require δρ̇_v = −3H δρ_v (up to convention signs), a law for the vacuum perturbation. A crossover driven by local temperature does not obey it, and adiabatic δT/T gives δρ_v ∝ ρ̇_v δt(x).
- **A cleaner version around Minkowski.** Lemma BR with conserved full T gives ∂_0δG_00 = κ∂_0δT_00^full. A law enforcing δG_00 = κ(δT_00^full − δρ_v) then forces ∂_0δρ_v = 0. Around FRW, the H-terms let f(t) absorb only the homogeneous part.
- **So a constraint-form vacuum-blind law is inconsistent with spatially non-uniform vacuum changes at linear order.** The homogeneous change is absorbed by f(t), which is why §4.4 works.
- The F-law does not enforce δE_00 = 0, so it escapes this form. But then its local E_00 is an output, and local Newtonian gravity during transitions is not checked. This is the site-creation analogue of R10-4 §4.5's Bianchi failure (`C5_R10-4_report.md:232-239`).

### 4.6 Check (c): redshift, rapidity budget, "no site is privileged"

**Redshift needs an encoder (reading; comparator verified).**
- Excitations must be stretched and new modes must enter in their local vacuum. That is an isometry, not a unitary (Cotler–Strominger 2201.11658, verified).
- The global mode map k → k a₁/a₂ is non-local in position space.
- A *local* insertion (one site at a time) redshifts only on average.

**Local Z³-preserving insertion is dislocation climb (proved, geometry; numbers checked).**
- You cannot add one site to Z³ and keep Z³. The local way is an interstitial (prismatic) dislocation loop: an inserted disc of sites whose rim climbs.
- The lattice is Z³ away from the defect lines, and the lines carry the Burgers vector (torsion).
- Required line density: ρ_L = 3H/(a v_climb). At v = c, the mean spacing is **2.7e-5 m today** and 4.8e-14 m at BBN (`r122_numbers.out` §(b)).
- Global plane insertion keeps exact Z³ but is non-local and anisotropic per event.

**Poisson timing = random-walk foam (checked; comparator verified).**
- Each site splitting at rate H per axis is a Yule process. MC check: variance 797 vs 800 from theory.
- The std of a column's final length is √(ℓ_P D) ≈ 4.1e-5 m for a z = 1 source.
- Columns separated by more than the loop scale (≤ 27 µm) are independent. So the wavefront phase std is 0.026 rad (1 cm radio), **520 rad (optical), 2.1e5 rad (1 keV X-ray)** and 2.1e11 rad (1 GeV).
- This is exactly the α = 1/2 model that Perlman et al. exclude with Chandra (α ≳ 0.58; verified).
- **EXCLUDED, bounded to independent (Poisson-like) insertion timing.**
- An escape needs the per-column insertion-count variance suppressed to ≤ 2.3e-11 of Poisson for X-rays (std ≤ 1.2e25 sites against Poisson's 2.6e30).

**Ordered creation passes (proved in 1D; checked).**
- The rule: each site carries a phase that advances at the local creation rate. When it crosses 1, the site inserts a neighbour along the column, and both restart at 0.
- A site with initial phase φ has D(φ, Φ) = 2^{⌊Φ+φ⌋} descendants: deterministic and monotone in φ.
- By Koksma–Hlawka, a window of N initial sites has count error ≤ V(D)·N·D*_N. For phases frac(iα), α = golden ratio, D*_N = O(log N / N), so the error is O(2^Φ log N), not O(√N).
- **Checked** (`r122_ordered_creation.out`, N = 2e4 per window, 400 windows):
  - at Φ = 6.6, std = 63 (quasi-periodic), 4429 (random phases) and 13932 (Yule);
  - at Φ = 3.3, std = 7.4, 499 and 1213.
- At N ~ 1e60 the error is ~ 2^Φ × 140 sites, far below the 1.2e25 bound.
- **Prices:** a quasi-periodic initial phase field, i.e. an ordered initial *state* (the law privileges nothing, but its origin is unexplained), and a 3D axis-cycling schedule. The 3D version and its dislocation geometry are not built (suggested). With random initial phases, integrate-and-fire is sub-Poisson but still ∝ √N (checked). This is R6-3's order-versus-silence trade-off again (`TESTS.md:3426-3427`).

**Rapidity budget (reading, from R11-3 refereed numbers).** The spacing stays at ℓ_P, so η* = asinh(B/(a m_p)) = 45.4 at every epoch, and "the natural unit equals ℓ_P" (`AX:189-190`) holds as a constant identity. The P/F laws keep this.

**"No site is privileged."**
- The laws are translation- and cubic-covariant (proved): the same rule at every site, with per-site memory as state.
- But local insertion makes dislocation cores structurally distinguished. Then the site set is no longer "the points of Z³" (`AX:37`). That is a Lattice price either way: a dynamical site set with defects, or non-local plane insertion.

### 4.7 Check (d): w(z) and isotropy

**Isotropy (proved; checked).** By Schur, the O_h average of any symmetric rank-2 rate tensor is (tr/3)·I (residual 8.9e-16, `r122_numbers.out` §(f)). A cubic-covariant creation law gives an isotropic *mean* expansion.
- Anisotropy lives at the loop/line scale (≤ 27 µm today) and in the per-event shear of each loop orientation. It is not a cosmological anisotropy (reading).
- The spatial-trace freedom f(t) is homogeneous and isotropic.

**w(z).**
- Under P/F, every time-constant component, Λ included, is invisible. So Λ_eff = 0 exactly (proved).
- Observed acceleration then needs dark energy with w ≠ −1 (for constant w, P/F reproduce wCDM exactly). The prediction is "dark energy is not a cosmological constant". Its size (meV) and its coincidence are not explained.
- DESI DR2 prefers w₀ > −1 at 2.8–4.2σ depending on the SN sample (comparator, verified via the R10-4 referee). It does not exclude w = −1, so this prediction is consistent but untested at 5σ (reading).
- Rule E cannot reproduce ΛCDM-like H(z) with constant-w components (Cauchy–Schwarz, §4.4). Only a contrived dark component with negative adiabatic sound speed works.
- **Tension with the spectral-gap note.** It predicts w = −1 exactly and a fixed R (`DARK_ENERGY_EOS_NOTE.md:204`; falsifier at `COSMOLOGICAL_CONSTANT_RESULT_2026-04-12.md:106-107`). The two cannot both hold (reading).

---

## 5. Prices (named, none adopted)

| # | Price | Axiom text touched |
|---|---|---|
| S1 | Site creation: the site set grows. Either a dynamical defect network (dislocation loops), so sites are not literally Z³, or non-local plane insertion | Lattice, "Physical sites are the points of the cubic lattice Z³" (`AX:37`); "no site is privileged" (`AX:40-41`) |
| S2 | A creation law (rate). The axioms supply no formation or creation rate (`AX:67-69,183-184`) and no dynamics (`AX:116-123`) | Admissibility reading notes; open gates |
| S3 | An isometric encoder: new sites enter in the local vacuum, and existing excitations are stretched | Qubit/Admissibility (no update law supplied, `AX:181-184`) |
| P-T | **Temporal vacuum reference.** The creation law reads only the time variation of the local stress along the site worldline (Prony to order 2N), plus per-site curvature memory X (F-law). This replaces P13's state reference. It is untuned, but it makes every constant component, including a true Λ, non-gravitating for the expansion | Source/action open gate (`AX:186-187`); "A law privileges no states" (`AX:94-95`): P-T privileges time-constancy, not a state (reading) |
| S4 | Deterministic creation clocks with a low-discrepancy (quasi-periodic) initial phase field (from §4.6; constructed in 1D) | Admissibility gives a probability law (`AX:60-73`); a deterministic schedule is a boundary realization (`AX:63-66`) |
| S5 | Freezing of sites in bound regions (c ≥ 0 from permanence), plus a gravity sector for matter collapsing through frozen sites | Record permanence (`AX:79-80`) |
| S6 | Dark energy must be dynamical (w ≠ −1); its scale is a separate input | none (observational price) |

---

## 6. Notes for the referee and the record

**Referee items (FAIL-type, bounded):**
1. Lemma CR (§4.1), including the exactness of c = 3H + ∂_iV^i with W = aV, and the HR = 66.3 number.
2. PT-s for classes A and U, and the freeze branch under H-perm (§4.3).
3. Cauchy–Schwarz underestimate, and rule E failing on the grid zero-point (§4.4).
4. Lemma G (memoryless ⇒ δ ∝ a^{−3/2} for comoving sites).
5. Lemma K (curvature kick −κΔ/3), with its EW numbers and the 11.5 GeV freeze.
6. The foam exclusion of Poisson-timed insertion: Yule variance, per-column independence, and the Perlman α = 1/2 identification. Also the Koksma–Hlawka escape (§4.6).
7. B-loc (§4.5): the Minkowski version rests on Lemma BR; the FRW version is suggested. Please check the linearized Bianchi signs.

**Strong-word check.**
- "Exact" (P-rule): finite mixtures of constant-w components, exact data. Real matter (neutrinos turning non-relativistic) is approximate and Prony is ill-conditioned (suggested).
- "Untuned": the homogeneous sector, smooth (crossover) steps.
- "Forced": Lemma CR under H-V3c and H-hom with cosmic slicing.
- "EXCLUDED": only the bounded classes in §0.

**What would change the picture:**
- a local mechanism that *produces* the low-discrepancy phase field from generic initial data, and its 3D version;
- a computation of collapse through frozen sites in V3;
- a vector or scalar completion that absorbs non-uniform vacuum changes (B-loc);
- a reason for dynamical dark energy at the meV scale.

---

## 7. Files

- Report: `.../scratchpad/C5/R12-2/R12-2_report.md`.
- Scripts and outputs: `.../scratchpad/C5/R12-2/scripts/`:
  - `r122_frw_rules.py/.out`;
  - `r122_ordered_creation.py/.out`;
  - `r122_numbers.py/.out`.
