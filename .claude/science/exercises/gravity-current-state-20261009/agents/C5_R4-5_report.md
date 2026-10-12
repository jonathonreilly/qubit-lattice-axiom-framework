# C5 R4-5: Λ from the record count (everpresent Λ)

**Worker.** Claude Opus 5.5 (same family as the supervisor and the other C5 probes). Not refereed. Run 2026-10-12, 13:09Z to about 13:50Z. No repository file was edited.
**Scratch.** `scratchpad/C5/R4-5/`. Scripts and outputs are in `scripts/`:
- `r45_numbers.py/.out`: magnitudes with explicit factors, per set.
- `r45_lattice_count.py/.out`: count variance of lattice substrates in 3+1 causal diamonds.
- `r45_checks.py/.out` and `r45_checks2.py/.out`: the aligned-row formula, Bernoulli thinning, small misalignment, and the boost-averaged (LRL-ensemble) variance.

**Read.**
- In full: `docs/MINIMAL_AXIOMS_2026-06-29.md`; `TESTS.md` §§"Campaign C5" through "C5 Round 4" (2302–2851); `agents/C5_O5_synthesis.md`; `SUMMARY.md` §§15–21; `PRICE_NOTE.md` §§1, 5, 6 and the v6 delta.
- Prior art: `docs/COSMOLOGICAL_CONSTANT_RESULT_2026-04-12.md` (and its 05-17 audit-prep note), `COSMOLOGICAL_CONSTANT_SPECTRAL_GAP_IDENTITY_THEOREM_NOTE.md`, `COSMOLOGICAL_CONSTANT_VACUUM_ENERGY_AUDIT_NOTE.md`, `UNIVERSAL_GR_INDUCED_COSMOLOGICAL_CONSTANT_BOUNDED_THEOREM_NOTE_2026-06-08.md`, `UNIVERSAL_GR_LAMBDA_BYPASS_NOTE.md`, `DARK_ENERGY_EOS_NOTE.md` (head), `OMEGA_LAMBDA_DERIVATION_NOTE.md` (head), `COSMOLOGY_SCALE_IDENTIFICATION_AND_REDUCTION_NOTE.md` ("Honest Remaining Gap").
- Packet items: `agents/C5_O3_report.md:80-120` (row 7); `agents/E1_report.md:50-66`; `agents/supervisor_thread.md:45-60,140-160`; `TESTS.md:150-160`.
- Referee files: the Λ/unimodular passages of `C5_R2-3_report.md` and `C5_R2-3_referee.md`, `C5_R3-4_referee.md:13,37`, `C5_R2-5_referee.md:53` and `C5_R3-2_referee.md`. `C5_O3_referee.md` has no Λ-specific line.
- **Docs grep.** No repository doc mentions everpresent Λ or Sorkin's count argument. The "Sorkin" hits in `docs/` are the I₃ = 0 Born-rule work, which is unrelated.

**Labels.**
- **proved:** a complete argument under the stated hypotheses.
- **checked:** a numerical or arithmetic check, in the scripts.
- **suggested:** argued, not proved.
- **reading:** an interpretation.
- **comparator:** outside literature. "Verified" means checked by web fetch this run; "from memory" means not checked.

---

## 0. Verdict against the FIXED readings (`TESTS.md:2846-2849`): **INCONCLUSIVE**

**Not PASS.**
- **No set does it as literally defined in the item.** None of A (records only), B or LRL (lattice sites), or C (a 3D grid with ticks) gives the observed |Λ| from its own count.
- **The construction that does reach the observed order** is a Planck-density layer of records that form at random and steer nothing, with Λ conjugate to their count (§3, rows A+ and B′+). It needs new prices.
- **⟨Λ⟩ = 0 is not derived in any set** (§5). It is the old cosmological-constant problem, relocated to an integration constant or a tuning.
- **The CMB data are not passed as stated** (§6).

**Not FAIL.**
- The random-record variants give the observed order without fine tuning: one O(10⁻²–1) coefficient, which is not derived.
- The data cited disfavour the published count-based Model 1 against the CMB, but they do not exclude everpresent-Λ histories as a class (§6).
- A crystal's own site count is frame-dependent in this heuristic, not uniquely "wrong order" (§4.3).

**Bounded sub-results** (these are FAIL-type, so they need the codex referee before they are recorded):
- **(i) Set A, records only:** |ΔΛ| ≤ 5e-73 Λ_obs (checked arithmetic, under H1–H3).
- **(ii) Set C, under Record as written:** |ΔΛ| ≤ 4e-28 Λ_obs (proved bound from the axiom text, under H1–H3).
- **(iii) LRL site count:** there is no volume law in Lorentz-averaged causal diamonds at T ≤ 108 lattice units (checked). The asymptotic claim is suggested.

---

## 1. In plain words

**Sorkin's idea.**
- In one form of gravity (unimodular), Λ and the amount of spacetime behind us are a conjugate pair, like position and momentum.
- If spacetime is made of countable elements at about one per Planck 4-volume, sprinkled at random, then the count fixes the volume only to within ±√N.
- So Λ is uncertain by about 1/√N, and 1/√N comes out at today's observed value.

**What this probe found.**
- **The magnitude needs three things of the count:**
  - it must be dense, near the Planck scale;
  - it must be random, so that its spread grows like √volume;
  - it must live in real (Lorentzian) spacetime.
- **The literal sets fail at least one of these:**
  - **A's records are far too rare.** Interference experiments forbid more. The result is about 72 or more decades too small.
  - **C's records are capped by the rule "one record per site".** The site count measures space, not spacetime. The result is at least 27 decades too small.
  - **A crystal's own site count is not random.** How much it spreads depends on how the observer moves through the crystal.
  - **The Lorentz-random lattice (LRL) is too regular.** Its count spreads far less than √volume.
- **What works.** Records forming at random at about one per Planck 4-volume, and steering nothing, give the right size. That is Sorkin's mechanism with records as the elements.
- **What it costs:**
  - a new rule, that the volume is the record count;
  - records that steer light not at all, or the lensing noise returns;
  - a way for Λ to change without breaking energy conservation;
  - and nothing explains why Λ averages to zero.
- **The data are mixed.** The published versions fit supernovae but strain against the CMB.

---

## 2. The mechanism, its hypotheses and its magnitude (explicit factors)

### Hypotheses

None of these is derived in any set. Each is a comparator heuristic or a price.
- **H1 (unimodular conjugacy; comparator, Sorkin).** S ⊃ −(Λ/8πG)·V, so V and Λ/(8πG) are conjugate. The heuristic saturates ΔΛ·ΔV ≈ κ_u ℓ̄_P², with ℓ̄_P² = 8πGħ/c³. κ_u = 1 is the Sorkin and ZAS form; κ_u = ½ is minimal Gaussian uncertainty.
- **H2 (volume is the count).** The substrate fixes the count N in the past region, and V is known only to ΔV = √Var(N)/ρ. This is a new rule in every set, i.e. a price.
- **H3 (volume law).** Var(N | region) = F ρ V, with F = O(1), for every region shape and every observer.
- **H4 (density).** ρ ≈ ℓ̄_P⁻⁴ × O(10⁻²–1).
- **H5 (mean).** ⟨Λ⟩ = 0.
- **H6 (Lorentzian region).** The past region of here-now (its past light cone) is a region of a Lorentzian spacetime that contains the counted elements.

**Formula.** ΔΛ = κ_u ℓ̄_P² ρ/√Var(N). Under H3 and H4 this is ΔΛ = κ_u (ℓ̄_P/ℓ_e)²/√(F V), with ρ = ℓ_e⁻⁴.

### Magnitudes (checked, `r45_numbers.out:1-32`)

**Inputs.**
- Λ_obs = 3Ω_Λ H₀²/c² = 1.090e-52 m⁻² (H₀ = 67.4, Ω_m = 0.3153). That is 2.85e-122 ℓ_P⁻² and 7.16e-121 ℓ̄_P⁻².
- The past-light-cone 4-volume of here-now in ΛCDM is V_lc = 4.36e103 m⁴ = 6.39e242 ℓ_P⁴. For comparison, (c/H₀)⁴ = 5.20e243 ℓ_P⁴.

**Poisson count at the Planck density (F = 1):**

| ℓ_e | κ_u | V | ΔΛ/Λ_obs |
|---|---|---|---|
| ℓ̄_P | 1 | V_lc | **1.39** |
| ℓ̄_P | 1 | (c/H₀)⁴ | 0.49 (reproduces `C5_O3_report.md:99` "0.49 ρ_Λ") |
| ℓ̄_P | ½ | V_lc | 0.70 |
| ℓ_P | 1 | V_lc | 34.9 |
| ℓ_P | ½ | (c/H₀)⁴ | 6.1 |

So the observed order comes out with a coefficient anywhere from 0.24 to 35, depending only on conventions.

**Epoch scaling (checked).** Λ_S/(3H²/c²) = 2.7 in the radiation era, 1.5–1.8 in the matter era and 0.95 today. The mechanism tracks H² at all epochs with an O(1) coefficient; this is the "everpresent" property.

**The coefficient is not derived** (comparator, verified). The published implementations need:
- β ≈ 0.01–0.02 in Model 1 (ADGS 2004, as quoted by ZAS);
- α = 0.88 rms of a tanh-compressed Ω̂_de in Model 2 (ZAS).

Taking κ_u = 1 at face value, β ≈ 0.01–0.02 corresponds to ℓ_e ≈ 7–10 ℓ̄_P (35–50 ℓ_P). That is a mild choice, not a fine tuning.

---

## 3. Per set

ΔΛ is under H1, with the forced identification of the count where a set does not supply one.

| Set | What is counted | Does H2–H6 hold? | ΔΛ / Λ_obs | Label |
|---|---|---|---|---|
| **A** (continuum + rare record flashes) | Flashes, at rates inside the refereed F7 budget | H2 fails: the 4-volume is a continuum, and the flash count tracks matter (n_b λ), not volume. Forced H2 violates H4 | GRW (λ = 1e-16 s⁻¹): **2.6e-81**. O4 Earth-heat maximum (5.3e-11 s⁻¹): 1.9e-78. All photons, neutrinos and baryons at 1e-9 s⁻¹: **4.6e-73** | checked (`r45_numbers.out:34-38`); conditional on H1 |
| **A+** (A plus an inert Poisson record layer at the Planck density) | Inert records that lock only their own occurrence | H2 by a new rule; H3 holds (Poisson); H4 by choice; H6 holds | **0.24–35** (§2) | the comparator mechanism; prices Λ1–Λ4 below |
| **B** (Euclidean Z⁴, whole law hypercubic) | Euclidean sites, or records in the block | **H6 fails.** The sites are Euclidean, and OS reconstruction gives no map from lattice sites to Lorentzian events. "The past light cone of here-now" has no lattice content | **no prediction** | reading |
| **B, Lorentzian crystal reading** (and C's site-tick count) | Sites of Z⁴ (or Z³ × τZ) in a causal diamond | **H3 fails: the spread depends on the frame and the region shape** (§4.3). For C there is also a mismatch: fixed comoving sites in FRW count ∫d³x dt, not the physical 4-volume ∫a³d³x dt (reading) | aligned observer: F = 0.60 for Z⁴, so 1.29 × Sorkin. Any real observer moving relative to the crystal: no universal law | checked at T ≤ 108; the aligned-row term proved analytically and checked |
| **B′, LRL sites** | Points of an LRL realization | H6 holds. **H3 fails:** the Lorentz-averaged spread is sub-volume, Var ≈ 0.5–0.9 T^{~2.2} at T = 13–108 (§4.4) | Wrong epoch scaling (ΔΛ falls more slowly than H²). Magnitude not claimed, since it would need an extrapolation (`TESTS.md:8`) | checked to T ≤ 108; asymptotics suggested |
| **B′+** (LRL plus records that form Bernoulli(p), independently per site, and steer nothing) | Inert records on LRL sites | Thinning restores H3: Var = p(1−p)ρV + p²Var_sites (checked, §4.5). H4 holds if a ≈ ℓ̄_P and p = O(1) | **≈ 0.4–1 × Sorkin**, with effective density pρ/(1−p) | checked (thinning); prices Λ1–Λ4 |
| **C** (Z³ + ticks; Record as written) | Records | **Proved cap** (Lemma C-count, §4.1): the records in J⁻(here-now) number at most 8.2e184, against V_lc/ℓ_P⁴ = 6.4e242 | **≤ 4.0e-28** (comoving spacing ℓ_P today). ≤ 8e-52 at a 1e-19 m spacing | proved bound under H1–H3; arithmetic checked (`r45_numbers.out:40-45`) |
| **E** (Poisson events; comparator) | Events | All of H2–H6 hold | **0.24–35** | comparator. Route E is excluded if its events steer light (RZ/RL4, refereed; `SUMMARY.md` §18) |

---

## 4. New results

### 4.1 Lemma C-count (proved, from the axiom text)

**Statement.** Assume the sites are the points of Z³ (`MINIMAL_AXIOMS_2026-06-29.md:37`) and that "A site never carries more than one record; records are permanent" (`:79-80`). Then the number of records in any past region is at most the number of site worldlines that region meets. A record count therefore measures a 3-volume, never a 4-volume.

**Numbers (checked).**
- With comoving spacing ℓ_P today and a comoving particle horizon of 4.36e26 m, N_rec(J⁻(p)) ≤ 8.24e184.
- Each record's 4-volume share is then at least 6.4e242 / 8.2e184. The mean formation density is at most 1.3e-58 per ℓ_P⁴, close to t_P·H₀ = 1.2e-61 times a geometric factor.
- Under H1–H3 with the forced H2, |ΔΛ| ≤ 4.0e-28 Λ_obs.
- Allowing site creation at a fixed physical spacing of ℓ_P does not raise the cap. The number of distinct sites that ever enter J⁻(p) is at most (4π/3)χ_p³/ℓ_P³ = 8.2e184. That count is a reading of the geometry, not a separate check.

**Consequence.** In set C the owner's "count rises until frozen" saturates at the 3-volume count. It cannot be the unimodular clock.

### 4.2 Set A bound (checked arithmetic)

The flash density is bounded by the refereed F7 budgets: Earth heat 5.3e-11 s⁻¹ per nucleon (`TESTS.md:2410`) and the IGM bound of about 1e-9 s⁻¹ (`C5_R2-3_report.md:188`). Under H1–H3 with the forced H2, ΔΛ/Λ_obs ≤ 4.6e-73 even when every photon, neutrino and baryon flashes at 1e-9 s⁻¹.

### 4.3 Crystal counts in causal diamonds depend on the frame

**Aligned-row formula** (proved at leading order in T; the next jumps, in A‴, give O(T²) corrections to Var; checked).
- In a crystal with time-row spacing s and density ρ, take a diamond of height T whose axis is the crystal's time axis.
- The cross-section volume A(t) = (4π/3)min(t, T−t)³ has a slope jump ΔA′ = −2πT² at the waist. So |χ̂(2πn e₀/s)| ≈ 2πT²/q².
- Summing over the time row gives Var = ρ²T⁴s⁴π²/180, i.e. **Var/(ρV) = (2π/15) ρ s⁴**. That is a volume law.
- **Checked against the count:** L₇ prediction 7.757, measured 7.4–7.8 for T = 6–76 (`r45_lattice_count.out` L7 η = 0). Z⁴ measured 0.60 flat at T = 6–76. The time row alone gives 0.42; the remainder is other rows, not analysed.

**Misalignment** (checked).
- With a spatial wavenumber k = M sinh δη, the row term picks up a factor sinc²(MδηT/2).
- **Checked:** L₇ at δη = 0.05 falls from 6.7 to 4e-3 between T = 6 and 108, tracking the formula (`r45_checks2.out`, part (a)).
- For any real observer the row term is gone. For example, the Sun against the CMB has δη = 1.2e-3, so MδηT/2 = 6e57 at T = c·t₀ and the suppression is about 1e-116 (`r45_numbers.out`, last lines). This uses the analytic formula, not an extrapolated fit.

**Boosted Z⁴** (which has null lattice vectors) is erratic.
- Var/(ρV) varies between 0.06 and 3.7 at T ≤ 76.
- The fitted slope is T^{4.2–4.6}.
- No universal law is visible.

**Reading.** In this heuristic, a crystal's own count gives a Λ that depends on the observer's velocity relative to the crystal. That is a preferred-frame effect, not a prediction.

### 4.4 The LRL ensemble is sub-volume (checked to T ≤ 108; asymptotics suggested)

**Method.**
- Boosts are drawn with density ∝ sinh²η on [0, η_max] in an isotropic direction, with a fresh translation for each sample.
- This approximates the SO⁺(1,3)/Γ_L average by large hyperbolic balls.
- The fundamental domain itself was not constructed.

**Results.**
- At η_max = 1.5, Var/(ρV) = 6.2e-2, 1.8e-2, 5.0e-3 and 1.5e-3 at T = 13, 27, 54 and 108. That is Var ∝ T^{2.2}, with Var/T² rising from 0.52 to 0.88.
- At η_max = 3.0, Var/(ρV) = 7.1e-2, 1.8e-2, 5.4e-3 and 1.4e-3 at the same T, i.e. Var ∝ T^{2.17}, with Var/T² rising from 0.59 to 0.82. This is stable against η_max.
- At η_max = 1.0, Var ∝ T^{2.29}. At η_max = 2.0, Var ∝ T^{2.38}. These two runs reach only T ≤ 38.
- The analytic estimate (suggested) is the row term averaged over misalignment: ∫d³δη · 4π²T⁴ sinc²/M⁴ gives about T²/M⁶ per orbit, so Var ∝ T² up to logarithms.
- So the gap that makes LRL quiet for lensing (R2-2, refereed: no Bragg support for 0 < |q²| < (2π)²/7) also removes the volume law.

### 4.5 Random formation restores the volume law (checked)

**Identity.** With Bernoulli(p) records on sites, Var(N_rec) = p(1−p)⟨N⟩ + p²Var(N_sites). This is exact, a standard binomial identity.

**Check.** On L₇ at η = 0.7, T = 27:
- p = 0.3: Var(N_rec)/(pρV) = 0.70;
- p = 0.7: Var(N_rec)/(pρV) = 0.31.

Both equal 1 − p (`r45_checks.out`, part 2).

**Reading.** Hyperuniformity of the sites is irrelevant once formation is random. It is the record count, not the site count, that can carry Sorkin's magnitude.

### 4.6 Lemma V: a volume law forces in-band weight (suggested; sketch plus the numbers above)

**Setting.** For a stationary, Lorentz-invariant-in-law count with structure factor S (a Lorentz-invariant positive measure), Var N(D_T) = (2π)⁻⁴ ∫ S(dq) |χ̂_{D_T}(q)|² = (2π)⁻⁴ T⁶ ∫ ν(dm²) J(|m|T), where J is the diamond's form factor integrated over the hyperboloid of mass m.

**Two directions:**
- If ν has a density at m² → 0, the shells |m| < 1/T give Var ∝ T⁴, a volume law.
- If ν vanishes on 0 < |m²| < c (the LRL gap), then Var = o(T⁴), provided J(X) = O(X^{−2−ε}). The data in §4.4 indicate J ~ X⁻⁴; this is **not proved**.

**Consequence (suggested).**
- The elements whose count sets an everpresent Λ must carry Poisson-size spacelike weight in band.
- By RZ/RL4 and P-L′ (refereed), if those same elements steer propagation, lensing noise follows.
- So the Λ-count must steer nothing. The LRL's lensing silence and an everpresent Λ cannot come from the same elements.
- The count also cannot be a local integer observable of a positive-energy vacuum: N-Q′ (R2-2, refereed; `TESTS.md:2711`) makes every such count annihilate the vacuum. It has to be a classical record layer, i.e. a mixed state, which is what A+ and B′+ assume.

### 4.7 Bianchi consistency (suggested; uses the refereed Lemma B scope)

**The constraint.** Unimodular gravity tolerates only ∂_νΛ = 8πG J_ν (`C5_R2-3_report.md:112`; scope confirmed at `C5_R2-3_referee.md:23`). A classical Λ(x) that varies by about ρ_crit per Hubble time therefore needs an energy exchange of order ρ_Λc² per Hubble time, about 5e-10 J m⁻³.

**Size.** Cosmic GRW heating is 5.4e-27 J m⁻³ per Hubble time, about 17 decades below ρ_Λ (`C5_R3-4_referee.md:37`).

**Conflict.** Inert records, which are needed by §4.6, exchange nothing. So either:
- (a) the records carry an energy channel at the ρ_crit level, i.e. they are not inert in energy; or
- (b) everpresent Λ is not a classical field obeying the trace-free Einstein equation. It would be a quantum uncertainty, with the stochastic Λ(t) only a phenomenological model.

Whether DNY part I addresses this is unverified.

---

## 5. Where ⟨Λ⟩ = 0 comes from, set by set (it is not derived in any)

- **Comparator.** DNY (verified) state it as an assumption: "thanks to a yet-unknown solution to the old cosmological constant problem" (Das–Nasiri–Yazdi, arXiv:2307.13743).
- **A, A+ and B′/B′+ (Lorentzian, unimodular).**
  - Vacuum energy decouples from the trace-free equations. Λ is an integration constant that is radiatively stable but has no fixed value (`C5_O3_report.md:98`, row 6).
  - The mean is a choice of initial or global datum, made to about 1e-123 in Planck units. That is a tuning relocated, not removed.
- **B (Euclidean Z⁴).**
  - The vacuum tadpole is an O(1), SO(4)-isotropic lattice coupling (`UNIVERSAL_GR_INDUCED_COSMOLOGICAL_CONSTANT_BOUNDED_THEOREM_NOTE_2026-06-08.md:34-41`). K1 counts it as a separate cosmological-tadpole tuning (`SUMMARY.md:418`).
  - Under a unimodular "one site = one volume unit" rule the tadpole is a constant in each fixed-N sector, so it drops out (suggested). The mean is then set by whatever weights the N-sectors.
  - Baum–Hawking's e^{3π/GΛ} peak at Λ → 0⁺ is a possible Euclidean source (comparator, from memory, contested). If taken literally it would also suppress the fluctuations.
- **C.** Tuning (`C5_O5_synthesis.md:315`; C1's Λ ≈ 1.1e-123) or the unimodular rule. Either way it is a premise.

---

## 6. Data (comparator)

- **Zwane–Afshordi–Sorkin, CQG 35, 194002 (2018); arXiv:1703.06265** (verified via ar5iv).
  - Model 2, a Gaussian process in log a with a tanh-compressed Ω_de, α = 0.88 and μ = 0.98, fits as well as ΛCDM: χ² 11335.2 against 11334.6.
  - It eases the H₀ and Lyman-α BAO tensions.
  - It does not solve the ultramassive-black-hole and lithium problems.
  - Model 2 is phenomenological. It is not computed from a count.
- **Ahmed–Dodelson–Greene–Sorkin, PRD 69, 103523 (2004)** (verified abstract). The fluctuating Λ is "always of order the ambient density". The Model 1 range 0.01 < β < 0.02 is as quoted in ZAS.
- **Das–Nasiri–Yazdi, arXiv:2307.13743 (v2, Oct 2024)** (verified abstract).
  - Model 1, which is closer to the count origin, beats ΛCDM on SN Ia only for a few random seeds.
  - For the CMB it "struggles": suppressing Λ near last scattering helps, but χ² stays much larger than ΛCDM's.
  - The favoured fluctuations are smaller than typical everpresent-Λ amplitudes.
- **Barrow, PRD 75, 067301 (2007)** (verified abstract). CMB isotropy strongly constrains the stochastic Λ fluctuations: those allowed by COBE/WMAP are too small to dominate at z < 1000.
- **DESI DR2 (2025)** (verified only as press summaries). There is a hint of evolving dark energy when DESI is combined with CMB and SN data. No test of everpresent Λ against DR2 was found.
- **Reading against "consistent with CMB/BAO as stated".** Not established. The count-derived model is CMB-disfavoured, and the model that fits is not derived from a count.

---

## 7. The owner's thought ("the record count rises"), tested as a hypothesis

**Reading.** In unimodular gravity the clock conjugate to Λ is the past 4-volume ("unimodular time"). "Time = record creation" is therefore exactly the right variable for Sorkin's mechanism, provided the record count measures 4-volume.

**What survives:** a count that rises like the past 4-volume, at Planck density, with independent formation.
- In C it saturates (Lemma C-count).
- In A it is too sparse and follows matter.
- In B′ it works only with random, inert formation, and then the mean and Bianchi questions stay open.

So the thought survives as Sorkin's mechanism with records as the elements, and only under the prices below.

---

## 8. Relation to prior art

- **`COSMOLOGICAL_CONSTANT_RESULT_2026-04-12.md`** (Λ = 3/R², R = c/H_inf supplied; ratio 1.44 at H₀, `:24,33`).
  - **What is shared:** both routes give Λ ~ H².
  - **What differs:**
    - The spectral gap needs R supplied (conditional) and gives a fixed Λ.
    - Everpresent Λ supplies the H² scaling from the count, but with a random sign and size.
    - The spectral-gap route says w = −1 exactly (`DARK_ENERGY_EOS_RETAINED_COROLLARY_THEOREM_NOTE.md:27,78`).
  - **Consequence.** The two are incompatible as stated. Adopting everpresent Λ triggers that note's own falsifier, "if `w != -1` … the fixed spectral-gap identification fails" (`COSMOLOGICAL_CONSTANT_RESULT_2026-04-12.md:106`).
- **`COSMOLOGICAL_CONSTANT_SPECTRAL_GAP_IDENTITY_THEOREM_NOTE.md`.** An R-identity only; unaffected. This result does not supply R.
- **`COSMOLOGICAL_CONSTANT_VACUUM_ENERGY_AUDIT_NOTE.md`** (finite lattice sums do not suppress, `:14,59`). Consistent: everpresent Λ addresses the size of the fluctuation, not the mean, so the audit's negative stands.
- **`UNIVERSAL_GR_INDUCED_COSMOLOGICAL_CONSTANT_BOUNDED_THEOREM_NOTE_2026-06-08.md`.** It left unimodular and record routes open (`:25,59,94`). This probe takes the unimodular route: it decouples the tadpole but turns the mean into a premise (§5). It closes nothing in that note.
- **`OMEGA_LAMBDA_DERIVATION_NOTE.md`.** Arithmetic on supplied Ω_b and R. Everpresent Λ makes Ω_Λ today a random O(1) draw, not 0.69 derived.
- **`UNIVERSAL_GR_LAMBDA_BYPASS_NOTE.md`.** Its λ is the phase-lift parameter, not Λ. Unrelated.
- **`C5_O3_report.md:99`, row 7.** "~H₀²M̄² = 0.49 ρ_Λ" is reproduced (0.487 with (c/H₀)⁴; 1.39 with the actual past-cone volume).
  - The row's "needs #6" is confirmed: the mechanism needs unimodular conjugacy.
  - The row's "Lattice → countable random events" is sharpened: the counted elements must be random, volume-law and inert. A lattice's own sites do not qualify (§4.3–4.4).
- **`E1_report.md:58`.** The count does not see TT strain at fixed det g, so there is no counting-level graviton mass. This probe is the trace-sector partner: the count sees only det g, i.e. Λ. Consistent.
- **`supervisor_thread.md:53`.** "δΛ ~ 1/√V_Hubble ~ 1e-122" is checked: 1/√((c/H₀)⁴/ℓ_P⁴) = 1.39e-122, against Λ_obs ℓ_P² = 2.85e-122.
- **`supervisor_thread.md:149`.** "Reads naturally with the record count rises" holds only under §7's conditions.
- **`TESTS.md:159`.** That comparator is now tested, with the result above.

---

## 9. Prices named (none adopted)

| # | Price | Axiom text touched |
|---|---|---|
| Λ1 | **Volume is the record count.** A unimodular bridge: the past 4-volume is defined as N_rec/ρ, and Λ is its conjugate | A new primitive; source/action is an open gate (`MINIMAL_AXIOMS_2026-06-29.md:187`) |
| Λ2 | **Planck-density random formation of inert records.** Records lock only their occurrence, never matter branch data (P4 reconciliation, `B_referee.md:185-190`, as cited in PRICE_NOTE P4). They steer no propagation (§4.6) | Record (`:77-80`); the formation rate is downstream (`:184`) |
| Λ3 | **An energy channel for Λ(x) variation** (∂Λ = 8πG J), or a non-classical Λ (§4.7) | none, or a new primitive |
| Λ4 | **⟨Λ⟩ = 0,** as a premise or a tuned integration constant | none |
| Λ5 (C only) | Site creation, or 4D sites. Without it, Lemma C-count caps the count at the 3-volume | Lattice (`:37`) |

---

## 10. For the referee

1. **Lemma C-count.** Check the J⁻(p) site cap, including the site-creation reading.
2. **Aligned-row formula.** Check Var/(ρV) = (2π/15)ρs⁴ and its sinc² misalignment factor; the numerics are in `r45_lattice_count.out` and `r45_checks2.out`.
3. **LRL averaging.** Is the hyperbolic-ball average a fair proxy for the SO⁺(1,3)/Γ_L average? Is the T^{~2.2} law asymptotic? The proof of J(X) = O(X^{−2−ε}) is the missing step of Lemma V.
4. **Model 1 coefficient.** Whether β ≈ 0.01–0.02 in ADGS Model 1 is a rms or a feedback-amplified coefficient; I did not resolve this.
5. **Bianchi tension.** Whether the §4.7 tension is already treated in DNY part I.

**Not done.**
- The fundamental domain of Γ_L.
- Crystal variance for the actual FRW past-cone region; only diamonds were computed.
- An everpresent-Λ fit to DESI DR2.

Sources: [ZAS arXiv:1703.06265](https://arxiv.org/abs/1703.06265), [ar5iv text](https://ar5iv.arxiv.org/html/1703.06265), [DNY arXiv:2307.13743](https://arxiv.org/abs/2307.13743), [ADGS astro-ph/0209274](https://arxiv.org/abs/astro-ph/0209274), [Barrow gr-qc/0612128](https://arxiv.org/abs/gr-qc/0612128), [DESI DR2 summary (CERN Courier)](https://cerncourier.com/a/desi-hints-at-evolving-dark-energy/).
