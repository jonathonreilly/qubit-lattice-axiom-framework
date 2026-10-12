# C5 round 11, probe R11-5: a regulated preferred-frame CQ kernel and its window (worker report)

**Worker.** Claude Opus 5.5, the same family as the supervisor and every C5 worker. **Not refereed.** Run 2026-10-12, 18:36Z to about 19:20Z. No repository file was edited.

**Scratch:** `scratchpad/C5/R11-5/`.
- `scripts/r115_checks.py` and `scripts/r115_checks.out` (sections [1]–[13]) hold every number below. Runtime about 5 s, OMP_NUM_THREADS=2.
- SHA-256: script `ebb0ca71…c58c8f`, output `3ec1ae36…643773`.
- No downloads. Web checks are listed under Sources.

**Paths.** `P/` = `.claude/science/exercises/gravity-current-state-20261009/`; `TESTS` = `P/TESTS.md`; `AX` = `docs/MINIMAL_AXIOMS_2026-06-29.md`; `vR9-4` = `P/agents/C5_R9-4_referee_verdict.md` (and so on); bare `C5_*` files are in `P/agents/`.

**What I read.**
- In full: `AX`; the C5 header `TESTS:2302-2320`; the R11 block `TESTS:4062-4282`, with R11-5 at `:4218-4244`; `C5_R9-4_report.md`, `C5_R9-4_referee.md`, `vR9-4`; `C5_R8-3_report.md`, `vR8-3`, `C5_R8-3_referee.md:180-272`; `C5_R6-4_report.md`, `vR6-4`, `C5_R6-4_referee.md:60-135`; `SUMMARY.md:534-635` (§§21–24).
- In part: the R6-4, R8-3 and R9-4 registrations and results (`TESTS:3143-3180`, `:3405-3418`, `:3466-3481`, `:3555-3573`, `:3700-3738`, `:3905-3916`); `C5_S11_synthesis.md:1-60,120-135,226-251,300-330`; `scripts/C5/R9-4/r94_checks.{py,out}` §[7]; `scripts/C5/R8-3/r83_checks.py` §§[5],[9].
- Read only for overlap: `vR10-3` (refereed after S11; Lemma Q and the "stationary record" finding are counted once below). The R10-3 worker report was **not** used for content.

**Labels.**
- **proved:** derived here under the stated hypotheses.
- **checked:** a number in `r115_checks.out`.
- **suggested:** argued, not proved; order-of-magnitude unless stated.
- **reading:** an interpretation.
- **comparator:** literature, marked web-checked (this run), via an earlier referee, or RECALLED.

**Subtraction rule (`TESTS:4074`).** Every decay or tail clause in this report concerns a positive spectral density or a positive energy integrand, so no channel limit is subtracted ("subtraction: none"). The single exception is the velocity effect in §4, which is measured against the same kernel at v = 0 (the subtraction is the rest-frame static kernel). Each script section prints its subtraction.

---

## Reading against the FIXED rule (`TESTS:4239-4242`)

**Worker reading: VIABLE, in a restricted-domain (finite frame age) form only. Referee requested.**

| Clause | Status |
|---|---|
| Explicit regulated kernel | 𝒦_ε (§2): kernel formulas are explicit; D′₀ is a bounded function, so locally finite. CP is proved by a dilation for the low-frequency meter (checked [1]). The near-cone meter bank is argued, with its algebra proved (§2.3). |
| Passes every stated test (`TESTS:4233-4237`) | Yes, for every ℓ_s in R6-4's window: Cs-133 for 70 s, LPF, corrected torsion, Cassini, GW170817, PPN α₁ and α₂. Velocity effects are O(β²) = 1.5e-6 relative, with annual modulation 4.8e-7 (§4). |
| Allowed ℓ_s interval | Stated tests only: R6-4's 4e-10 to 5e-6 m (true lower end about 1e-10 m). Adding the computed vacuum and cosmological consequences, which are not stated tests and are order of magnitude: **about 2–4e-7 to 5e-6 m** under the conservative premise (ii), and about 4e-8 to 5e-6 m under premise (i). The core, roughly 5e-7 to 5e-6 m, survives an O(10³) error in any coefficient. |
| Prices | Named in §6. They include a new one: **the law has a start time** (a finite frame age), because of Lemma C. |

**The decisive new fact (proved; a no-go, so referee required): Lemma C, the cone lemma (§1).** Take any kernel tied to a frame that is stationary in that frame and satisfies (H-T), with the standard retarded propagator and with F continuous and non-zero at a regular point of the light cone. Then the matter decoherence measure D′₀ and the classical metric record's covariance M cannot both be locally finite there.

So **no stationary version exists** in which both the classical record and the matter decoherence are well defined. A regulated kernel exists only as a finite-time process. The record's on-shell gravitational-wave (GW) content then grows over the frame's age: at the minimal rate ε·ln t if P_J vanishes linearly at the cone, and linearly in t if D′₀ is bounded there.

- If the referee does **not** accept a finite frame age as a "restricted domain" (`C5_R9-4_referee.md:81` lists "a finite-time, restricted-domain, or regulated prescription"), the reading falls to: EXCLUDED as a stationary record-metric model within class 𝒯_u (Lemma C), and OPEN outside 𝒯_u.
- This matches the R10-3 referee's finding for the emission-cancelled corner: "a non-locally-finite positive covariance does not define the stipulated stationary classical record" (`vR10-3:13`). Counted once.

**Against the expectation (`TESTS:4243`).**
- The interval lands inside the expected 2e-7 to 5e-6 m.
- The expected "new risk" (velocity-dependent heating and its annual modulation) is negligible: O(β²), with no O(β) drag term in the construction.
- The real risk turned out to be the cone itself (Lemma C). It forces near-cone noise suppression ε(ℓ) ~ 1e-11 to 1e-6, and a law with a start time.

---

## 0. In plain words

- **The kernel can be built.** Picture a quantum "meter" that watches the smeared stress of matter, continuously and gently, at every point of the cosmic rest frame. The meter writes a classical record, and the record is fed back to matter as the classical metric. That process is automatically a legitimate quantum operation. A chain of four coupled resonators gives the meter's kick noise the steep high-frequency fall (ω⁻⁸) needed to keep the empty-space photon output finite. The chain is also arranged so the meter kicks without dragging: moving bodies feel no friction against the cosmic frame.
- **The averaged metric is exactly Einstein's**, with the source blurred over ℓ_s. So light bending, Shapiro delay, gravitational-wave speed and the preferred-frame PPN parameters all come out as in GR, up to corrections that fall away beyond ℓ_s.
- **Moving through the cosmic frame barely matters.** Earth moves at 370 km/s relative to the CMB frame. That changes every lab decoherence and heating rate by about one part in a million, with a yearly wobble of 5 parts in 10 million. The lab margins are 9 to 22 decades.
- **The light cone is the hard part.** Classical gravity has to pay for its pull with noise. Near the light cone that noise either decoheres matter without limit, or keeps pumping classical gravitational waves into space. There is no in-between. The minimal option pumps slowly, logarithmically in time. So the theory needs a start time (the universe's age), and its leftover gravitational-wave energy must be squeezed by a factor ε of about 1e-11 to 1e-6.
- **What survives.** Smearing lengths from about 0.2–0.4 µm up to 5 µm pass everything computed, if the noise's gravitational-wave energy counts as gravitating. Down to about 0.04 µm pass if only freely travelling waves count. Below that, the squeezing heats matter (or makes too many vacuum photons) beyond what Earth's heat flow allows.

---

## Prior art (each counted once)

1. **R6-4** (`TESTS:3409-3418`; `vR6-4:5-25`).
   - The Newtonian least-decoherence floor K ≥ (4πG/ħ)|g̃|²/k²; the VIABLE window 4e-10 to 5e-6 m (true lower end about 1e-10 m).
   - Corollary U; H-cosmo conditional (`C5_R6-4_referee.md:210-216`).
   - The ISL endpoint needs a geometry fit (`C5_R6-4_referee.md:113-125`).
2. **R8-3** (`TESTS:3559-3573`; `vR8-3`).
   - Lemma 1 (boost-orbit infinity); Lemma 3 (cone jump → ln).
   - The preferred-frame ansatz and its EBL estimate Ė ≈ A′ħc²ℓ_P²/ℓ⁷ (`C5_R8-3_report.md:197-231`), with A′ in [1e-4, 1].
   - μ is non-minimal (`C5_R8-3_referee.md:217-225`).
3. **R9-4** (`TESTS:3909-3915`; `vR9-4:11`).
   - n ≥ 3 (integer).
   - D′₀ ∝ 1/|s| is not locally finite.
   - The 2e-7 to 5e-6 m search target with L = 10 and the ε^(−1/7) joint solution (`C5_R9-4_report.md:197-228`).
   - The (H-T) meter derivation (`C5_R9-4_referee.md:17-33`).
4. **R4-4 Lemma N** (`TESTS:2935`): a positive BMV result excludes every variant. The construction below predicts zero BMV entanglement (§2.2).
5. **R10-3 referee** (`vR10-3:5,13`).
   - Lemma Q: a ground-state meter cannot write an informative record at non-zero four-momentum.
   - A non-locally-finite record covariance does not define a stationary classical record.
   - Both are used here, counted once. Our meters are driven, not in a ground state, consistent with Lemma Q.
6. **Lane RF** (`TESTS:1295-1310`). The preferred-foliation lane lists PPN α₁/α₂ and GW170817 as the frame tests. It concerns a dynamical foliation in the gravity sector; here the frame is a fixed background in the noise only (a different question; counted once).
7. **Repository grep** for "back-action evading" (0 files), "quantum-mechanics-free"/"Tsang" (only R10-3 files and two unrelated docs), "Isaacson" (only `C5_R9-4_report.md`), and "khronon"/"aether" (lane RF and C4 only). There is no repository construction of a frame-tied CQ dilation.

## Hypotheses: class 𝒯_u (stated before any title)

- **H1.** Linearized CQ gravity on Minkowski space. The classical metric is h = G_R·(F·T + ξ), with the standard massless retarded G_R. Matter feels h through the same F (symmetric coupling, R8-3's H1′).
- **H2.** A fixed frame u^μ, taken as the CMB rest frame. Every kernel (F, P_J, D′₀) is translation-invariant and, in the theorem, stationary in frame time. It depends on (ω, |k|) in the frame, per spin channel.
- **H3 (H-T).** At every frame momentum, [[P_J, F/2], [F*/2, D′₀]] ≥ 0. This uses R8-3's convention: P_J·D′₀ ≥ ¼ on the smeared operator, and K = D′₀|F|² + c²|F|²P_J/s² on matter. (H-T) holds for the stationary linear-meter dilations used here (`C5_R9-4_referee.md:17-33`).
- **H4.** F is continuous at s = 0, with F(cone) ≈ 1 at low |k|. This is forced by Lemma 3 together with GW emission (R8-3, R9-4).
- **H5.** Gaussian statistics; golden-rule order for vacuum rates.

**Excluded realizations.**
- Correlated, emission-cancelled histories (R10-3).
- Trace-only kernels (`TESTS:3911-3912`).
- A dynamical frame field: the frame is a fixed background here.
- Jump or non-Gaussian CQ.
- Non-linear gravity.

---

## 1. Lemma C: the cone lemma (proved; no-go part, referee required)

**Statement.** Under H1–H4, at every frame momentum near a regular cone point where F ≠ 0,

  D′₀ + c²M ≥ c/|s| (for every c > 0), where M ≡ |G_R|²P_J = P_J/s².

Since ∫ds/|s| diverges at s = 0, **D′₀ and M cannot both be locally finite measures** across the cone.

*Proof.* AM–GM gives D′₀ + c²P_J/s² ≥ 2c√(P_J·D′₀)/|s| ≥ c/|s|, by (H-T). ∎

- [proved; checked [2]: the minimum of the ratio over 20000 draws is 1.000022. ∫_{d<|s|<1} ds/|s| = 9.2, 18.4, 36.8, 73.7 at d = 1e-2, 1e-4, 1e-8, 1e-16.]
- This sharpens the R9-4 referee's point (`vR9-4:11`). Making D′₀ locally finite pushes the non-integrable weight into the classical metric record.

**Finite-time meaning (checked [3]).** Write P_J ≈ σ|u|^α near the cone, with u = ω − c|k|. The on-shell (free) GW energy after time T is ∫du P_J sin²(uT/2)/u² (subtraction: none). Its growth depends on α:
- **α = 0** (D′₀ bounded): grows linearly in T (14.7, 156, 1570).
- **α = 1**: grows logarithmically, by 2.30 per decade (2.93, 5.19, 7.48).
- **α = 2**: saturates (1.05, 1.01, 1.00), but then D′₀ ~ 1/u² and matter's near-null decoherence grows like T.

So the minimal secular growth is logarithmic, at α = 1. **Every regulated member of 𝒯_u is a finite-time process with growing on-shell record content** (proved for the stationary-kernel class; the growth exponents are checked).

**Consequence for the fixed setting (reading).** The "regulator or restricted domain at the cone" (`TESTS:4223`) must in the end be a restricted domain in **time**: the frame's age. A bounded D′₀ (a "regulator" in the narrow sense) is allowed, but then M is not locally finite, and the record's on-shell content grows over the age.

---

## 2. Probe (a): the construction 𝒦_ε

### 2.1 The low-frequency meter: an explicit dilation, with CP proved

**Model.** Per frame mode and spin channel, the matter observable is A = (g_ℓ*T). It couples to a resonant (rotating-frame), driven chain of N modes:

  H = λ A X₁ + g Σ_j (X_jX_{j+1} + P_jP_{j+1}).

Mode N leaks at rate κ into a line whose X output is homodyned. The quadratures split into two closed sets, {P₁, X₂, P₃, X₄, …} (driven by A) and {X₁, P₂, X₃, P₄, …} (which carries the backaction X₁).

- **χ_FF = 0** (proved from the split; checked [1]: |dX₁/dA| = 0). Consequences:
  - [X₁(t), X₁(t′)] = 0, so the backaction is a commuting, classical-like noise;
  - there is no friction and no meter-mediated coherent A–A interaction;
  - the noise is symmetric in ±ω.
- **Quantum limited at every ω** (checked [1]): S_II·S_FF/(|gain|²/4) = 1 to 7e-16 at all eight test frequencies, from 0 to 100.
- **Backaction falloff is ω^(−2N)** (checked [1]: slope −8.000 for N = 4).
- **CP (proved).** The process alternates a Gaussian homodyne instrument on matter ⊗ chain ⊗ line with unitaries controlled by the record. Discretize time: the averaged map is Σ_r A_r ρ A_r† with Σ A_r†A_r = 1. The feedback H_fb(t) = −½∫h_μν[J_{≤t}](g*T^μν) uses only past records, since G_R is retarded and the post-filter R is causal.
- The meter is driven, not in its ground state, consistent with R10-3's Lemma Q (`vR10-3:5`).
- **Mean field (proved).** E[J] = R·gain·⟨A⟩ = F_u⟨T⟩, so h̄ = G_R F_u⟨T⟩. F_u commutes with ∂, so the smeared source is conserved and the Bianchi identity holds (R8-3 §4).
- **No entanglement (proved within the model).** Matter sees (i) commuting backaction noise, which is a mixture of product unitaries, and (ii) record-conditioned feedback, which is LOCC. So the model predicts **zero BMV entanglement**. R4-4 Lemma N's falsifier stands.
- **UV (checked [4]).** The photon-pair vacuum energy injection converges if and only if the total backaction falls faster than ω⁻⁶:
  - (1+ω²)⁻²: diverges (46 → 5e7);
  - (1+ω²)⁻³: logarithmic (1.57, 3.86, 6.16, 8.46);
  - (1+ω²)⁻⁴: converges (0.1667).

  Equivalently, 1/|s| × (1+ω²τ²)^(−n) with n ≥ 3, as in R9-4. **N ≥ 4 chain stages.** Subtraction: none.

### 2.2 The kernel 𝒦_ε (explicit formulas, units c|k| = 1 per mode)

- F = F_u = e^{−k²ℓ²/2}(1 − iωτ)^{−n}, with n = 3 and τ = ℓ/c (R8-3's form; n corrected to 3).
- D′₀(s) = c/(2e(s)√(s² + s₀²)) and P_J(s) = e(s)√(s² + s₀²)/(2c), where e(s) = ε + (1 − ε)s²/(s² + δ²), δ = √ε, and s₀ = 2c|k|/T_*.
  - T_* ≥ t_H is a meter coherence time. Equivalently, take the frame age as a restricted domain.
  - Outside the cone band this is the R9-4 optimizer.
- **Checks ([9]):**
  - P_J·D′₀ = ¼ to 3e-17 everywhere (saturated).
  - sup D′₀ = 2.5e13 at ε = 1e-6, so D′₀ is bounded and locally finite.
  - The static kernel equals R6-4's least-decoherence floor exactly (K/floor = 1.000000 at ω = 0).
  - The photon-pair weight ∫s²D′₀ ds = 0.2500, the same as without suppression. So the narrow band does **not** multiply the vacuum photon output by 1/ε (this corrects R9-4's broadband assumption, `C5_R9-4_report.md:214`, for premise (i)).
- **Secular free-GW growth is suppressed by ε** (analytic: P_J ≈ ε|s|/2c inside |s| < δ). Numerically the slope dE/dlnT is ≤ 1.2e-2, the quadrature's resolution, against 1 unsuppressed.
- A **non-secular forced near-cone TT part** of about ½ln(1/ε) (6.9 to 11.5) remains unless the suppression is broadband. This is the premise (i)/(ii) split in §5.

### 2.3 The near-cone meter bank (algebra proved; physical element argued)

The near-cone profile 1/(e(s)√(s² + s₀²)) is a positive superposition of lines centred on ω = c|k|. Each line comes from a two-quadrature modulated meter: coupling λA[cos Ωt X^c + sin Ωt X^s] to two independent copies of the §2.1 chain, with Ω = c|k|.

- **Stationarity (proved).** ⟨F_ba(t)F_ba(t′)⟩ = λ²S(t − t′)cos Ω(t − t′), and the backaction still commutes.
- **(H-T) holds (proved by Cauchy–Schwarz).** Saturation holds near the line centre up to O((bandwidth/2Ω)^{2N}).
- **Combining independent saturated meters with optimal record weights preserves saturation (proved):** P_eff = 1/(4ΣD_i), so P_eff·ΣD_i = ¼.
- The two-tone backaction-evading element is standard (comparator, RECALLED: Clerk–Marquardt–Jacobs two-tone BAE; Tsang–Caves QMFS, title confirmed by R10-3). It was **not simulated** here (suggested).

**Reading.** To make the classical record finite, the meter must contain a light-cone-resonant quantum sector in the frame. Its backaction is still a commuting classical noise, so "records are the metric" holds. But the near-cone part of gravity's cost is paid by a hidden, frame-tied, light-like meter field.

---

## 3. Probe (b): γ, c_T, the vacuum rate

- **γ = 1 and Shapiro (proved, as R8-3 §4).** The mean field is linearized GR with source F_u⟨T⟩, and for static dust h₀₀ and h_ij carry the same smeared Φ. The deflection deficit is e^{−b²/2ℓ²}, e^{−9.7e27} or smaller at the solar limb (R8-3 [4]).
- **c_T = c exactly (proved).** The vacuum wave operator is untouched.
- **GW emission at 100–1000 Hz.** 1 − |F_u| ≤ 2e-20, and the lag nτ is ≤ 5e-14 s against GW170817's 1.74 s ([6]; R8-3 [6] rescaled to n = 3).
- **Vacuum excitation in the frame.** It is finite: Ė ≈ A′ħc²ℓ_P²/ℓ⁷ in photons of about ħc/ℓ (R8-3's estimate, now with n = 3). This gives ℓ ≳ 4.6e-9 / 8.9e-9 / 1.7e-8 m for A′ = 1e-4 / 1e-2 / 1 against the whole EBL ([8]; suggested; A′ still R8-3's bracket).
- **On-shell record content (classical GWs at frequency ~c/ℓ)** ([7]; suggested, O(1) tensor weights, Isaacson premise):
  - **Bounded D′₀ with P_J(cone) at the static floor** (the §2.1 meter alone): dρ/dt ≈ 0.067ħc²/ℓ⁵. That is ρ_GW(t_H) ≈ 1e35 ρ_crit at 5e-6 m and 4e38 ρ_crit at 1e-6 m. It would need ℓ > 55 m. **The §2.1 meter alone is excluded** whenever free GWs gravitate. That is why the §2.3 bank is needed.
  - **𝒦_ε**: ρ_GW ≈ εLħc/(π³ℓ⁴), with **L = ln(c t_H/ℓ) = 72–79** (R9-4 used 10). ρ_GW < ρ_Λ needs ε < 6.6e-17, 1.1e-11, 7.0e-9, 4.5e-6 at ℓ = 1e-8, 2e-7, 1e-6, 5e-6 m.

## 4. Probe (b): matter moving at 370 km/s through the frame, and annual modulation

- **Velocity (web-checked).** v = 369.82 ± 0.11 km/s (Planck 2018), β = 1.2336e-3.
  - The dipole direction, computed from (l, b) = (264.02°, 48.25°), is RA, Dec = 167.94°, −6.94° and ecliptic latitude −11.15° ([5]).
- **Static lab kernel for moving matter.** K_lab(ω′ ≈ 0, k) = K_frame(k·v, k) (subtraction: the rest-frame static kernel). Checked [5]:

| kℓ | Direction-averaged δK/K | Along v |
|---|---|---|
| 0.1 | +4.9e-7 | +1.5e-6 |
| 1 | −1.0e-6 | −3.0e-6 |
| 3 | −1.3e-5 | −4.0e-5 |

  All are O(β²(1 + n(kℓ)²)).
- **Annual modulation.** Earth's orbital velocity projects at most 29.22 km/s on the dipole. That gives a δK/K amplitude of **4.8e-7** (kℓ = 1, along v; [5]).
- **No O(β) term (proved within 𝒦_ε).**
  - Every kernel is even in ω: the classical record noise is symmetric, and χ_FF = 0 makes the backaction symmetric.
  - Every kernel is smooth at ω = 0 for k ≠ 0.
  - So there is no frame drag (quantum friction) and no first-order heating asymmetry. A ground-state equilibrium bath would give drag. The QND chain is what removes it.
- **Heating and diffusion** (the f-sum rule; the Earth-heat, LPF and torsion comparisons) all evaluate K at lab frequencies ≪ c|k|. Their values equal R6-4's least-decoherence numbers × (1 + O(1e-6)), with lab-frequency corrections ω²/(c²k²) ≲ 1e-20. **R6-4's margins (9–22 decades) carry over unchanged** (proved for the kernel; the numbers are R6-4's).

## 5. Probe (c): comparisons

| Test | Result | Basis |
|---|---|---|
| Cs-133, 1.9 µm, 70 s (Panda et al., *Nature* 631, 515 (2024); web-checked) | pass by 14.5–21 decades across the window | R6-4 table × (1 + 1e-6); §4 |
| LISA Pathfinder, (1.74 ± 0.05) fm s⁻²/√Hz above 2 mHz (Armano et al., *PRL* 120, 061101 (2018); web-checked) | pass; LPF is a γ = 1 prediction (`vR6-4:7`) | as above |
| Torsion, σ_a² = (48π/5)G²D₂/(RT) | pass (an ω → 0 statement; R6-4's corrected integration) | as above |
| Cassini γ − 1 = (2.1 ± 2.3)e-5 | γ = 1 exactly; deficit e^{−10^27} | §3 |
| GW170817 | c_T = c exactly; lag ≤ 5e-14 s | §3 |
| PPN α₁: \|α̂₁\| < ~4e-5 (PSR J1738+0333, Shao & Wex 2012); α₂: \|α̂₂\| < 1.6e-9 (Shao et al. 2013); weak-field α₂ < 4e-7 (solar spin; web-checked) | The mean field gives α₁ = α₂ = 0 at r ≫ ℓ. A moving source sees F_u(k·w, k) → 1 as k → 0, for every w. The frame-dependent terms are a lag nτ ≤ 5e-14 s (a displacement ≤ 1.9e-8 m) and a dipole correction ~nβℓ/r ≤ 1.2e-19 at 1 AU ([6]). Both are short-range, not 1/r PPN terms. | proved (linear order); checked |
| PPN via the noise at second order | The noise feeds the mean metric only through its own energy: a homogeneous radiation-like TT fluid at rest in the CMB frame, with ρ ≤ ρ_Λ by the §3 constraint. Its frame effects on orbits are of order (ρ_GW/ρ_crit)(H₀r/c)²β, negligible. | suggested |
| ISL (Lee et al., *PRL* 124, 101101 (2020): 52 µm, Yukawa λ < 38.6 µm at α = 1; web-checked) | Every mass pair in that apparatus is ≥ 52 µm apart. The smeared point-pair force deficit there is 1.1e-11 at ℓ = 5e-6 m, against 0.61 for the excluded Yukawa. So 5e-6 m is safe pairwise; a net-torque statement still needs the geometry (`C5_R6-4_referee.md:113-125`). | checked [8]; suggested for the torque |

**Additional computed tests (not on the stated list; order of magnitude).**

1. **Vacuum photons.** ℓ ≳ 0.5–1.7e-8 m (§3).
2. **On-shell GW content.** This fixes ε(ℓ) (§3).
3. **Near-cone matter heating.** The 1/ε-enhanced D′₀ near the cone can excite matter at ħω ≈ ħc/ℓ (electronic UV at small ℓ, vibrational IR at large ℓ). Estimate ([10]; suggested): heating_cone/heating_static ~ f_cone·L/ε. Against Earth's 7.9e-12 W/kg:
   - FAIL at 1e-8 m (1.9e-7 W/kg);
   - marginal at 4e-8 m;
   - pass at 2e-7 m (8.5e-16), 1e-6 m (1e-17) and 5e-6 m (1e-22).

   The crossover is about **4.2e-8 m** (a factor 100 in f_cone moves it by 1.9).
4. **Premise (ii) (R9-4's broadband treatment, with L = ln(c t_H/ℓ)).** Joint lower ends: **1.8 / 2.7 / 4.1e-7 m** for A′ = 1e-4 / 1e-2 / 1 ([11]). At 1e-6 m the margin is photons/EBL = 6e-5 even with ×1/ε ([12]).
5. **Quasi-static TT noise energy** ([13]). The ω < 0.5c|k| region carries 0.049 units: 6.6e4 ρ_crit at 1e-6 m and 110 ρ_crit at 5e-6 m, if it gravitates. Restricting it to ω < 0.01c|k| leaves 3.3e-7 units (0.44 and 7e-4 ρ_crit). So a suppression band reaching down to 0.01c|k| suffices. That is still ≫ lab frequencies (c|k| ≳ 6e13 s⁻¹), so the lab kernels are untouched (suggested).
6. **H-cosmo** (R6-4's conformal-mode π_Φ energy). If it gravitates and accumulates, R6-4's ≥ 6.7-decade overshoot applies to this class too. As in R6-4, it is unproved and does not exclude (`C5_R6-4_referee.md:210-216`).

## 6. Probe (d): the ℓ_s interval and the prices

**Allowed interval (worker reading).**

| Basis | ℓ_s |
|---|---|
| Stated tests only | 4e-10 m (true about 1e-10) to 5e-6 m |
| Premise (i): only free (secular) GWs gravitate | ≈ 4e-8 to 5e-6 m (lower end from near-cone heating; photon EBL gives 0.5–1.7e-8) |
| Premise (ii): near-cone TT noise gravitates, broadband suppression | ≈ 1.8–4.1e-7 to 5e-6 m |
| Robust core: survives A′ ∈ [1e-4, 1], f_cone ± 1e2, and both premises | ≈ 5e-7 to 5e-6 m |

The upper end everywhere is R6-4's conservative 5e-6 m.

**Prices (named, not adopted).**
- **P-r1.** A preferred frame (the CMB frame) in the noise kernels and the smearing. It is a fixed background; a dynamical frame field is not built. *Axiom text:* Lattice `AX:37-41` supplies a frame only in sets C and C-box; set A is a continuum (as R8-3).
- **P-r2′.** A temporal smearing τ = ℓ/c with integer n ≥ 3. The meter has N ≥ 4 resonant stages: causal, non-Markovian memory.
- **P-r3.** R6-4's P-i1 to P-i5: non-local coupling, irreducible DP-floor decoherence, no graviton, Markovian-in-frame dynamics, conditional cosmology.
- **P-r4.** Vacuum photon creation at about A′ħc²ℓ_P²/ℓ⁷.
- **P-r9b′ (refines R9-4's P-r9b).** Near-cone suppression ε(ℓ) ≈ 1e-11 to 5e-6. It is realized by a bank of frame-resonant driven QND meters: a hidden light-like quantum sector in the frame. The matter cost is a 1/ε-enhanced decoherence at near-null transfers (the §5 heating).
- **P-r11a (new; forced by Lemma C).** **The law has a start time.** The classical metric record is a finite-age process with on-shell content growing as ε·ln t, or a meter coherence time T_* ≥ t_H. A stationary version does not exist in 𝒯_u. *Axiom text:* Record (`AX:77-80`) "Records form… records are permanent" is unaffected, but the record-production law (open gate, `AX:185-186`) acquires a time origin. Lattice `AX:40` ("No site is privileged") gains a privileged time slice.
- **P-r11b (new).** Driven meters (not in a ground state; Lemma Q). An energy source is supplied to the record-writing process. *Axiom text:* the record-production dynamics (`AX:185-186`) becomes named content with an energy input.
- **Qubit, Admissibility and Record prices** are as R6-4 (iii) (`vR6-4:19`).

## 7. Strong words checked

- **"No stationary version"** means within 𝒯_u: H1–H4, (H-T) per frame momentum, the standard retarded G_R, and F continuous and non-zero at a regular cone point. It is proved by AM–GM and is a no-go: **referee required.**
- **"CP (proved)"** covers the §2.1 chain dilation with record-conditioned causal feedback. The §2.3 modulated element is argued (its stationarity and (H-T) algebra proved), not simulated.
- **"Exactly"** (γ, c_T) is at linear mean-field order.
- **"No O(β) term"** holds within 𝒦_ε (χ_FF = 0, kernels even and smooth in ω). It is not a class-wide statement.
- Every cosmological number (A′, O(1) tensor weights, f_cone, the Isaacson premise, L) is suggested and order of magnitude. That is why the interval is quoted per premise, with a robust core.
- **"VIABLE"** is a worker reading for the restricted-domain form. It is not a refereed verdict.

## 8. What would decide it

1. **A referee of Lemma C**, and of whether a finite frame age (or T_* ≥ t_H) counts as the "restricted domain" the fixed setting allows.
2. **Simulate the two-tone modulated QND element** (§2.3) and confirm the bank reproduces e(s)√(s² + s₀²) with near-saturation.
3. **Compute A′** from the Maxwell ⟨TT⟩ spectral coefficient, and f_cone from measured optical and IR absorption. That fixes the lower end to better than a factor of 2.
4. **Settle the gravitating status** of the forced near-cone TT noise (premise (i) vs (ii)) and of H-cosmo.
5. **Fit the Lee et al. geometry** for the upper end.

**Sources.**
- Web-checked this run:
  - [Planck 2018 I, arXiv:1807.06205](https://arxiv.org/pdf/1807.06205) (369.82 ± 0.11 km/s).
  - [Shao & Wex 2012, arXiv:1209.4503](https://ar5iv.labs.arxiv.org/html/1209.4503) and [arXiv:1209.5171](https://web3.arxiv.org/abs/1209.5171) (α̂₁ = −0.4^{+3.7}_{−3.1}e-5).
  - [Shao et al. 2013, arXiv:1211.6558](https://ar5iv.arxiv.org/html/1211.6558) (|α̂₂| < 1.6e-9).
  - [Will, Living Reviews (2014)](https://www.maths.tcd.ie/EMIS/journals/LRG/Articles/lrr-2014-4/fn_1.html) (solar-alignment α₂ < 4e-7, search snippet).
  - [Lee et al., arXiv:2002.11761](https://arxiv.org/abs/2002.11761) (52 µm; λ < 38.6 µm).
  - [Armano et al., PRL 120, 061101](https://spiral.imperial.ac.uk/bitstream/10044/1/57430/4/PhysRevLett.120.061101.pdf) (1.74 ± 0.05 fm s⁻²/√Hz).
  - [Panda et al., Nature 631, 515 (2024)](https://ideas.repec.org/a/nat/nature/v631y2024i8021d10.1038_s41586-024-07561-3.html) (Cs, 70 s).
- Via earlier referees: Cassini; GW170817; Clerk et al. RMP Eq. (90); Tsang–Caves (title).
- RECALLED: ρ_crit, ρ_Λ, t_H, u_EBL; the Galactic-to-ICRS matrix (the output reproduces the known dipole RA/Dec); two-tone BAE; Isaacson.
