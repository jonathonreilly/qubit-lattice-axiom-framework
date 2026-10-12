# C5 round 6, probe R6-4: set A. Can the records be the classical metric? (worker report)

**Worker.** Claude Opus 5.5, the same family as the supervisor and every C5 worker. **Not refereed.** Run 2026-10-12, 14:31Z to about 15:00Z. No repository file was edited.

**Scratch.** All files are in `scratchpad/C5/R6-4/`:
- `scripts/r64_checks.py` and `scripts/r64_checks.out`: every number below, in sections [1]–[10].
- `scripts/pdf2txt.py`: extracts PDF text.
- `dl_pdfs/`: copies of two PDFs the R3-4 referee had already downloaded (OSSW 2203.01982 v1 and OWD 2302.07283), read as data only.
- `text/opp2203.txt` and `text/owd2302.txt`: the extracted text.

**Paths.** `P/` = `.claude/science/exercises/gravity-current-state-20261009/`. `AX` = `docs/MINIMAL_AXIOMS_2026-06-29.md`. `TESTS`, `C5_*` are in `P/` and `P/agents/`.

**Read in full.**
- `AX` (all 233 lines).
- `TESTS:2302-3180`: C5 method, rounds 1–6; R6-4 is at `TESTS:3143-3179`.
- `C5_S5_synthesis.md:1-200`, plus a grep of the rest.
- `C5_R3-4_report.md` §4 (E2, lines 220–260).
- `C5_R3-4_referee.md` and `C5_R3-4_referee_verdict.md`.
- `C5_R4-4_referee.md`.
- `C5_R2-3_referee.md`.
- `C5_O4_referee.md`.
- `C5_R4-5_referee_verdict.md:17,23`.
- OSSW 2203.01982 v1: §§III–V and Appendices C and F.

**Read in part.** `C5_R4-4_report.md` (grep for Lemma N, BMV, CQ). The R2-3 and O4 worker reports: not read; their referee files were.

**Labels.**
- **proved:** a derivation given here, under the stated hypotheses.
- **checked:** numerics or arithmetic in `r64_checks.out`.
- **suggested:** argued, not proved.
- **reading:** an interpretation.
- **comparator:** literature. Each is marked "web-checked" (fetched in this run) or "recalled" (from memory).

---

## Prior art (each counted once)

1. **R3-4 E2** (`TESTS:2776`; `C5_R3-4_referee.md:27-29`).
   - Unregulated ultra-local continuous Newtonian classical–quantum (CQ) gravity is EXCLUDED by the published 32-decade empty window.
   - A diffeomorphism-invariant CQ-GR candidate exists.
   - The worker called the non-local and discrete subcases "VIABLE (comparator)" (`C5_R3-4_report.md:249`).
   - `SUMMARY.md:562-563` repeats the 32 decades.
2. **R4-4 Lemma N** (`TESTS:2935`; `C5_R4-4_referee.md:43-49`): a classical c-number channel gives concurrence 0, against 0.156 for quantum coupling.
3. **R2-3 Lemmas B/B′** (`TESTS:2722`; `C5_R2-3_referee.md:5-7`): a decaying stress jump on one surface needs a compensator or a reset rule.
4. **O4 Lemma 1** (`TESTS:2408`; `C5_O4_referee.md:5-9`): V ≤ BC for a permanent, distinguishable record channel.
5. **R4-5 Bianchi gap** (`TESTS:2944`; `C5_R4-5_referee_verdict.md:17`): 17 decades.
6. **No repository derivation** of the least-decoherence floor or of a smeared-coupling window. Grep for "least decoherence" and "Tilloy" finds only R3-4's comparator lines (`C5_R3-4_report.md:236-249`).

## Hypotheses (stated before any title)

- **H1. Newtonian limit.** Non-relativistic matter couples through its mass density operator m(x).
- **H2. The continuous CQ class.**
  - The map is completely positive (CP), trace-preserving, Markovian and Gaussian: the Kramers–Moyal expansion stops at second order.
  - The back-reaction drift is π̇_Φ ∋ −(g*m)(x), where g is a smearing of width ℓ, g̃(k) = e^{−k²ℓ²/2}. Exact Newton is g̃ ≡ 1.
  - Notation: D₀ is the effective Lindblad kernel on m. P_J := 2D̃₂ is the noise power of π̇_Φ.
  - The Newtonian equations are those of OSSW: `text/opp2203.txt:880,924,930` (their Eqs. 36, 39, 40).
- **H3. Homogeneous kernels.** D₀(x−y) and D₂(x−y) are translation-invariant and isotropic. Dependence on a constant background Φ_b is allowed.
- **H4 (H-add).** In the matter's reduced dynamics, the D₀ Lindblad and the potential noise add, with no cross-correlation. This holds in the measurement-and-feedback representation of the continuous class; that equivalence is a comparator (Tilloy–Diósi 2016; Layton–Oppenheim–Weller-Davies; recalled).
- **H5. Point masses.** Matter contains point masses (electrons). Nuclei and nucleons carry Gaussian form factors where needed.
- **H6. Experimental inputs**, as labelled in `r64_checks.out` [4].

**Outside realizations this scope excludes.**
- Discrete (jump) CQ models with matter-dependent D₂. OSSW Table 1 lists them as open by 24 decades (comparator, via the R3-4 referee).
- Field-dependent kernels, for example D₂ ∝ −∇²Φ (OSSW §D3).
- Position-dependent kernels.
- Non-Markovian or coloured noise. This may evade the radiation bound (a 2021 comment found in search; not read).
- Non-Gaussian higher moments.
- The relativistic regime.

---

## 0. In plain words

- **Gravity cannot couple to the exact mass density.** If the classical potential responds to the exact density, every point particle is heated without limit, whatever kernel is chosen. A smearing length ℓ_s in the coupling itself is required.
- **With a smearing ℓ_s, the least damaging choice is the Diósi–Penrose kernel.** Every allowed kernel decoheres and heats matter at least as much as Diósi–Penrose (DP) does with R₀ = ℓ_s.
  - Radiation searches bound DP at R₀ ≳ 4 Å, so ℓ_s ≳ 4 Å.
  - Newton's law, tested down to 52 µm, caps ℓ_s at about 10 µm.
  - Inside this range every stated lab bound passes by 9 to 22 decades: Cs at 70 s, 25 kDa molecules, LISA Pathfinder and torsion balances.
  - **A window exists, from sub-nanometre to about 10 µm. It is not macroscopic.**
- **The covariant candidate as published falls in the excluded case.** Its computed weak-field limit (Layton et al. 2023) is local, with no smearing. A covariant smearing has not been built.
- **Energy and Λ.**
  - The noise has no mean, so there is no Λ-like drift.
  - The energy the noise gives matter is about 16.5 decades too small to act as an everpresent-Λ compensator. This is the same gap R4-5 found for GRW (17 decades).
  - If the diffusing gravitational momentum's kinetic term gravitates and accumulates, as OSSW 2022 assume, every allowed kernel overshoots ρ_Λ by at least 6.7 decades. That premise looks gauge-dependent, so this result is conditional.
- **The trade-off is O4's V ≤ BC, applied to the metric record.**
  - The metric history gives one permanent value per spacetime event, so it is a record set in a block sense.
  - But it is a dense, weak, noisy record of smeared mass, not a lock of one qubit possibility.
  - The Lattice, Qubit, Admissibility and Record texts all change.
- **Correction to prior art.** The published "32 decades" rests on a torsion-balance step that does not follow from the paper's own force-noise formula. It is too strong by about 45 decades. Unregulated ultra-local CQ is still excluded, but by other means: about 6 decades from Cs × LISA Pathfinder, and without limit once point electrons are included.

---

## 1. Lemmas (variant (i), probe (a))

**Lemma T (trade-off).** For the CQ Lindblad on L = (g*m) and drift −L, CP is equivalent to the matrix [[P_J, −½], [−½, D̃₀′]] being positive semidefinite at every k.

In terms of the effective kernel on m, D̃₀ = D̃₀′|g̃|², this reads:

  **P_J(k) · D̃₀(k) ≥ |g̃(k)|² / 4.**

- **[proved; checked [1].]** The 2×2 positivity follows from OSSW Eq. 29 (`text/opp2203.txt`, section IV) with D₁^br = −½ for drift −m.
- Measurement and feedback saturate it: monitoring with strength κ gives record noise 1/(4κ).
- Layton et al. write the same condition as "4D₂ ⪰ D₀⁻¹" (web-checked, arXiv:2307.02557 html, Eqs. 33/54). This agrees with Lemma T under their noise normalization (suggested, not line-checked).

**Lemma F (the least-decoherence floor).** Under H2–H4, the matter's reduced Lindblad kernel is

  K(k) = D̃₀ + (4πG)²|g̃|²P_J/(ħ²k⁴),

the second term being the random-unitary dephasing from the potential noise Φ̃ = 4πG J̃/k². Lemma T and AM–GM give, pointwise in k,

  **K(k) ≥ (4πG/ħ)|g̃|²/k².**

- Equality holds if and only if D̃₀ = (2πG/ħ)|g̃|²/k² and the trade-off is saturated.
- The right-hand side is the DP kernel with R₀ = ℓ (the DP Gaussian convention; mapping uncertain at O(1)).
- **[proved given H2–H4; checked [2]: the minimum of K/floor over 5000 random draws is 1.000000.]**
- **Consequence.** Every positive linear functional of K is at least its DP(R₀ = ℓ) value. That covers:
  - the decoherence rate of any superposition;
  - the energy input per kg, which is (ħ²/2)∫K k² d³k/(2π)³ by the f-sum rule, whatever the structure;
  - first-order spontaneous radiation.
- **Comparator (recalled).** This is Tilloy–Diósi's "principle of least decoherence" in this notation.

**Corollary U (no-go for unsmeared coupling).** Take g̃ ≡ 1, a homogeneous kernel, and any point mass m. Then

  d⟨p²⟩/dt ≥ 4πGħm² ∫d³k/(2π)³ = ∞.

The divergence goes as the cube of any UV cutoff ([3]). **[Proved given H1–H5. A no-go, so referee required.]**

So any continuous Newtonian CQ theory either carries a smearing length in the coupling or heats point particles without limit. Layton et al. note that a cut-off is needed (web-checked text: "theories with a cut-off below" 10⁻¹⁵ m conflict with heating).

## 2. The ℓ_s window for variant (i)

| Bound on ℓ (any kernel in H2–H3) | Value | Source and label |
|---|---|---|
| Radiation: DP R₀ ≳ 4×10⁻¹⁰ m, carried over by Lemma F | **ℓ ≥ 4×10⁻¹⁰ m** | Comparator, web-checked: Figurato et al., *NJP* 26, 113004 (2024), abstract. Donadi et al. 2021 give 0.54 Å (recalled). The bound assumes white, Markovian noise to high frequency |
| Earth heat, 7.9×10⁻¹² W/kg, against Għ/(4√π ℓ³) per kg | ℓ ≥ 5.0×10⁻¹² m | checked [5b] |
| LISA Pathfinder (LPF) alone, against the floor (8π/3)Għ∫\|g̃\|²S_T/M² | ℓ ≥ 5.3×10⁻¹⁴ m | checked [5c]. ASD 1.74 fm s⁻²/√Hz web-checked (Armano et al., *PRL* 120, 061101); 1.928 kg Au–Pt mass recalled |
| Stated bounds only, Cs (1.9 µm, 70 s) × LPF, Cauchy–Schwarz over all kernels | excludes only ℓ < 1×10⁻¹⁹ m | checked [5d]. The interferometers do not bind |
| Inverse-square-law tests to 52 µm. The smearing changes the two-body potential by erfc(r/2ℓ): 2.4×10⁻⁴ at 10 µm, 1.4×10⁻² at 15 µm | **ℓ ≲ 1–1.5×10⁻⁵ m** | suggested. Comparator recalled (Lee et al., *PRL* 2020); no fit to the actual apparatus geometry |

**Window.**
- With the radiation bound: 4×10⁻¹⁰ m ≲ ℓ_s ≲ 1×10⁻⁵ m, about 4.4 decades.
- Using only the own-computed heat bound: 5×10⁻¹² m to 10⁻⁵ m.

**Margins of the least-decoherence kernel** (D̃₀ = γ(2πG/ħ)|g̃|²/k², γ = 1; checked [6]). The closed form for a point mass is Γ = (GM²/ħ)[1/(√π ℓ) − erf(Δ/2ℓ)/Δ]; numerical integration agrees to 4.346e-17.

| ℓ | Cs Γ (allowed 1.4e-2 s⁻¹) | 25 kDa Γ (allowed 1.4e2) | LPF S_a (1.5e-30) | heating (7.9e-12 W/kg) |
|---|---|---|---|---|
| 4e-10 | 4.3e-17 (14.5 dec) | ≤1.5e-12 (14.0) | 6.1e-40 (9.4) | 1.6e-17 (5.7) |
| 1e-8 | 1.7e-18 (15.9) | ≤5.7e-14 (15.4) | 6.1e-40 (9.4) | 9.9e-22 (9.9) |
| 1e-5 | 5.2e-24 (21.4) | ≤3.6e-21 (22.6) | 6.1e-40 (9.4) | 9.9e-31 (18.9) |

- **Ions.** Hyperfine-qubit coherence beyond 1 h involves no spatial mass-density difference, so it does not constrain this class (reading).
- **γ-window.** For a general γ the matter kernel is (γ+1/γ)/2 × DP(ℓ). Allowed γ ([6]; radiation scaled conservatively as ℓ³):

| ℓ | Allowed γ |
|---|---|
| 4 Å | γ = 1 only |
| 1 nm | 0.03–31 |
| 10 nm | 3e-5–3e4 |
| ≥ 1 µm | about 2e-10–5e9 (capped by LPF) |

**Correction to prior art: the published ultra-local margin.**
- **Their step.** OSSW's torsion bound D₂ ≤ 10⁻⁴¹ kg² s m⁻³ comes from their Eqs. F8–F10 (`text/opp2203.txt:1042-1056` and Appendix F1). It treats each nucleus's interior field (Gρr_N)² as uniform over the whole volume V_b ≈ 10¹⁵ m³.
- **Their own formula gives otherwise.** Their F6 with a δ-kernel gives σ_a² = (48π/5)G²D₂/(RT) for a uniform sphere, because a nucleus's field falls as 1/d² and the coherent, body-scale term dominates. For their inputs the two differ by a factor of **9.4×10⁴⁴**; the corrected torsion bound is D₂ ≤ 3.7×10⁵ ([10]). **[suggested; checked arithmetic.]**
- **The published version was not seen.** It could not be fetched (a PMC browser check, and an authentication redirect at nature.com). The R3-4 referee's reading of Table 1 shows the same 10⁻⁴¹ upper end.
- **The exclusion still stands, on other grounds:**
  - with a nucleon-form-factor model and Cs × LPF, the decoherence–noise product exceeds the allowed value by **6.2 decades** ([7]);
  - with point electrons, Corollary U makes it diverge.
- **Recommendation.** Replace "32 decades" (`TESTS:2776`; `SUMMARY:563`) by "≥ 6 decades (Cs × LPF, own); divergent with point electrons". Referee required.
- **The kernel shape is not what fails.** Ultra-local kernels on a smeared density (CSL-like, Gaussian width r) open a window at r ≳ 4×10⁻¹⁰ m. The LPF and Earth-heat bounds cross between 1 and 4 Å, and the DP floor also gives 4 Å ([7]). What "ultra-local excluded" really excludes is the missing regulator.

**Reading for (i): VIABLE**, with these prices named (none adopted):
1. **(P-i1)** Gravity couples to mass density smeared over ℓ_s ∈ [≈4 Å, ≈10 µm]. That is a non-local coupling, and Newton's law changes below ℓ_s.
2. **(P-i2)** Irreducible decoherence and heating of matter at least those of DP(R₀ = ℓ_s), plus a stochastic Newtonian potential. Near ℓ_s = 4 Å only the least-decoherence kernel survives.
3. **(P-i3)** A5 is dropped. Gravity is classical, so there is no graviton. In this variant the theory is Newtonian only, and no light bending or gravitational waves are computed.
4. **(P-i4)** Markovian non-unitary dynamics in a Newtonian time slicing.
5. **(P-i5)** The conditional cosmological overshoot of §4.

**Not established.** Any relativistic completion; non-Markovian versions; the discrete class.

## 3. Variant (ii), probe (b): the covariant candidate (Oppenheim–Weller-Davies)

**A weak-field trade-off has been computed.** Source: Layton, Oppenheim, Russo and Weller-Davies, *JHEP* 08 (2023) 163, arXiv:2307.02557 (comparator, web-checked through the arXiv html; the second half was read only through the fetch tool's summary). They gauge-fix the OWD path integral and find:
- **Ultra-local couplings.** The decoherence term is −(D̃₀/2)(m⁺−m⁻)². The diffusion term is −2D̃₀(∇²Φ/4πG − m̄)². D̃₀ = c⁵D₀(1−β)/4.
- **Saturation.** The trade-off is saturated, 4D₂ = D₀⁻¹. CP needs β ≤ 1.
- **Their own conclusion:** "Non-relativistic versions of these models have already been ruled out."

**Applying the bounds.**
- The limit has g̃ ≡ 1 and homogeneous kernels. By Corollary U, point particles are heated without limit for every (D₀, β).
- With any regulator below 4 Å, Lemma F and the radiation bound exclude it.
- **So the literal candidate is EXCLUDED in its Newtonian limit.** "Literal" means a local T_{μν} coupling with constant or background-dependent couplings. **[proved given H1–H5 plus the comparator radiation bound; referee required.]**

**What a surviving (ii) is missing.**
- A covariant smearing of the T_{μν} coupling at ≥ 4 Å. An e^{ℓ²□}-type form factor is the obvious candidate; its growth at timelike momenta is a known problem in infinite-derivative gravity (comparator, recalled, not checked).
- Or covariant field-dependent kernels whose Newtonian limit has actually been computed.
- And in either case, relativistic checks: c_T, two polarizations, lensing. None was found.
- Grudka et al. (arXiv:2402.17844; abstract web-checked) favour a scale-invariant version on CP grounds. I did not find its Newtonian limit computed.
- **Grossardt's critiques** were not found in two searches. Not verified, not used.

**Reading for (ii): OPEN overall.** Its literal local form is EXCLUDED in the weak-field limit (referee required).

## 4. Energy and momentum: is there a Λ-like drift? (probe (c))

- **First moment: no drift.** The noise has zero mean: OSSW Eq. 40, E[uJ] = 0 (`text/opp2203.txt:930`); Layton Eq. 62, ∇²Φ/4πG = ⟨m̂⟩ + ∫σξ. So the mean Poisson source has no Λ-like term. **[proved within the model.]**
- **Matter-side energy exchange.** The heating floor per kg is Għ/(4√π ℓ³). Multiplied by the cosmic matter density and a Hubble time:
  - at ℓ = 4 Å: **1.75×10⁻²⁶ J m⁻³, 16.5 decades below ρ_Λc²**;
  - at 1 nm: 17.7 decades below;
  - at 1 µm: 26.7 decades below.

  Radiation caps K, so the 4 Å value is about the largest possible. **[checked [8].]**

  This is the size of R4-5's 17-decade gap for GRW heating. CQ diffusion therefore cannot pay for an everpresent-Λ Bianchi compensator through matter either (reading).
- **Gravity side: conditional on H-cosmo.** H-cosmo is OSSW's premise that ⟨π_Φ²⟩ grows by ∫P_J and that the kinetic term −(2πGc²/3)π_Φ² (`text/opp2203.txt`, F25/C10) gravitates and accumulates.
  - Cauchy–Schwarz against the heating limit gives |ε̇| ≥ (2πGc²/3)(ħ²/8h_max)(∫k|g̃| d³k/(2π)³)².
  - **Over a Hubble time:**
    - at least 6.7 decades above ρ_Λc² for any g̃ compatible with the inverse-square-law tests;
    - 14.3 decades above at ℓ = 10 µm;
    - 49.5 decades above at ℓ = 4 Å.

    **[checked [8]; conditional.]**
  - **I judge H-cosmo doubtful (suggested):**
    - the term is the conformal mode, with negative sign;
    - OSSW's C16–C17 give Φ̈ = +(c²k²/3)Φ, an unstable flow (own algebra);
    - Layton et al.'s constrained limit has no π_Φ at all.
  - **If H-cosmo holds, (i) is excluded cosmologically.** If it does not, nothing here excludes it.

## 5. The record reading, variant (iii) (probe (d))

**Lemma R (the trade-off is O4's V ≤ BC).** Take the Gaussian metric-record channel with drift −g*m and noise P_J. For two branches,

  −ln BC = (t/8)∫|g̃ Δm̃|²/P_J ≤ (t/2)∫D̃₀|Δm̃|² = Γt  (by Lemma T).

So V = e^{−Γt} ≤ BC, with equality at saturation. **[proved; checked [9]: the largest ratio over random CP kernels is 0.708 ≤ 1.]**

In plain words, complete positivity is exactly O4 Lemma 1 for the metric record (`TESTS:2408`).

**Block sense (reading).**
- The realized field history gives one value per spacetime event, never revised. So "a site never carries more than one record; records are permanent" (`AX:79-80`) holds if sites are events.
- It fails if sites are persisting spatial sites (Z³). A time-varying value would then be many records per site.

**Axiom texts touched (prices named, not adopted).**
- **Lattice** (`AX:37-41`): sites become events of a continuum. This is already set A's price.
- **Qubit** (`AX:45-53`): the site domain needs a classical commutative factor for the field value, such as M₂(C) ⊗ L^∞(field values). The record content is not an element of the M₂(C) possibility domain.
- **Admissibility** (`AX:57-61`): the record's distribution at an event is set by the joint classical–quantum state within ℓ_s, including the unrecorded matter state through ⟨g*m⟩. Neighbouring conditions alone do not set it. Its support is continuous (Gaussian).
- **Record** (`AX:77-83`):
  - "locks exactly one admissible local possibility" becomes "registers one classical value, an unsharp, noisy reading of smeared mass density";
  - every event carries a record, so "a site with no record cannot be read" becomes vacuous;
  - "Records form" becomes the CQ stochastic law;
  - "Only records are readable" fits as it stands: matter is read only through the metric record, which is O4's category IV.
- **Open gates** (`AX:181-187`): the decoherence mechanism and the record-production dynamics become named content (the DP floor).

**Reading.** Set A changes from sparse records to a dense, information-weak record. "Rare and coarse" (`TESTS:2408-2412`) survives in the information sense: by Lemma R, each event's record gains no more branch information than Γ ≥ DP(ℓ_s), which is about 10⁻¹⁷ s⁻¹ for an atom.

**Falsifier (Lemma N, `TESTS:2935`).**
- In this class the potential noise is classical, and a positive-kernel D₀ Lindblad is a mixture of product local unitaries. So no entanglement is generated. **[suggested; argued, not proved here.]** The Trillo–Navascués counter-claim for DP is disputed (R3-4, comparator).
- **A positive BMV-type gravity-mediated-entanglement result would exclude (i)–(iii).**
- A DP-floor excess in radiation or heating at R₀ ≈ ℓ_s would be the positive signature.

## 6. Readings against the FIXED rule (`TESTS:3170-3173`)

| Variant | Reading | Basis | Referee needed for |
|---|---|---|---|
| (i) Newtonian CQ, smearing ℓ_s | **VIABLE**: ℓ_s ≈ 4×10⁻¹⁰ m to ≈ 1×10⁻⁵ m; stated bounds pass by 9–22 decades; prices P-i1 to P-i5. Conditionally excluded cosmologically if H-cosmo holds | Lemmas T and F, the table in §2, [5]–[7] | Corollary U (no-go); the ultra-local margin correction |
| (ii) OWD covariant CQ-GR | **OPEN.** The literal local form is EXCLUDED in its weak-field limit | Layton et al. 2023 plus Corollary U | the literal EXCLUDED |
| (iii) metric history as the record set | **Reading with prices** on Lattice, Qubit, Admissibility and Record. Lemma R: CP equals V ≤ BC | §5 | none |

**Against the expectation.**
- (i): VIABLE, but the window is sub-nanometre to micron, not macroscopic.
- (ii): OPEN, as expected.
- (iii): a reading with prices, as expected, with Record priced and Qubit and Admissibility too.

**Strong words checked.**
- "Every", "any" and "kernel-independent" mean every kernel within H2–H3, never beyond.
- "Proved" is used only for Lemmas T, F and R, Corollary U, and the first-moment statement.
- The radiation lower end depends on comparator DP bounds; their Gaussian-convention mapping is uncertain at O(1).
- The upper end depends on a recalled inverse-square-law bound.

**What would decide it.**
1. A relativistic, covariant smeared CQ coupling, and its Newtonian limit.
2. A gauge-invariant treatment of the π_Φ energy, which settles H-cosmo.
3. The discrete (jump) CQ class tested the same way. It is the class closest to "records form" as discrete events.
4. BMV.
5. A dedicated DP-radiation re-analysis at R₀ = ℓ_s.

**Sources (web-checked this run).**
- arXiv:2307.02557 (Layton et al.; html).
- arXiv:2406.18494 (Figurato et al.; abstract).
- arXiv:2402.17844 (Grudka et al.; search summary).
- Armano et al., *PRL* 120, 061101 (search).
- Panda et al., *Nature* 631, 515 (search; the source-mass result only).
- OSSW arXiv:2203.01982 v1 and OWD 2302.07283: PDF text (copies of the R3-4 referee's downloads).
