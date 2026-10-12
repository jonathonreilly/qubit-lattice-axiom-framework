# C5 round 12, probe R12-4: one no-go for classical metric records across the CQ classes (worker report)

**Worker.** Claude Opus 5.5, the same family as the supervisor and every C5 worker. **Not refereed.** Run 2026-10-12, 19:30Z to about 20:10Z. No repository file was edited.

**Scratch:** `scratchpad/C5/R12-4/`.
- `scripts/r124_checks.py` and `scripts/r124_checks.out` (sections [1]–[8]) hold every number below. Runtime about 2 s, OMP_NUM_THREADS=2.
- SHA-256: script `5f0252c1…2c91c4`, output `7a57b113…862909`.
- No downloads. Web checks (search results and one abstract) are listed under Sources.

**Paths.** `P/` = `.claude/science/exercises/gravity-current-state-20261009/`; `TESTS` = `P/TESTS.md`; `AX` = `docs/MINIMAL_AXIOMS_2026-06-29.md`; `vR8-3` = `P/agents/C5_R8-3_referee_verdict.md` (and so on); bare `C5_*` files are in `P/agents/`.

**What I read.**
- In full: `AX`; `TESTS:2302-2320` (C5 method and readings); the R12-4 item `TESTS:4447-4461`; the R6-4, R8-3, R9-4, R10-3 and R11-5 registrations and results (`TESTS:3143-3175`, `:3409-3418`, `:3468-3481`, `:3559-3573`, `:3707-3738`, `:3909-3915`, `:3984-3998`, `:4218-4243`, `:4287-4296`, `:4325`, `:4438-4445`).
- In full: `C5_R8-3_report.md`, `vR8-3`; `C5_R9-4_report.md`, `vR9-4`; `C5_R10-3_report.md`, `C5_R10-3_referee.md`, `vR10-3`; `C5_R11-5_report.md`, `vR11-5`; `vR6-4`.
- In part: `C5_R9-4_referee.md:11,33` (the escape list and the dilation gap).

**Labels.** **proved** (derived here under the stated hypotheses); **checked** (a number in `r124_checks.out`); **suggested** (argued, not proved); **reading** (an interpretation); **comparator** (literature: web-checked this run, via an earlier referee, or RECALLED).

---

## Reading against the FIXED rule (`TESTS:4458-4461`)

**Worker reading: DERIVED, pending the referee** (a no-go, so referee required before it is recorded).

| Item | Result |
|---|---|
| Unified no-go | **Theorem U** (§2). The class 𝒰 contains T_E, T_u and R8-3's subclass (§3). Proved in 𝒰. |
| REFUTED attempt | No stationary model in 𝒰 has both finite: the proof is three lines and has no gap I could find (§4). The one explicit stationary model with both finite that I found (**frame friction on classical GWs**, checked [6]) lies outside 𝒰: it drops the standard undamped propagator. So it is an escape, not a refutation. |
| What is left | Listed in §5: finite-time processes; dissipative (damped) classical GW propagation; nonlinear order; spatially structured meters; CQ histories without a stationary non-demolition dilation. **Non-Gaussian and jump records with a linear record→metric map are not escapes** at second order (§2, checked [2]). |
| Minimal price | §6: a preferred frame, plus **one** cone regulator (a start time, or frame-tied GW friction γ ≲ H₀), plus a forced near-cone trade with a profile-independent product bound ∝ L², L ≈ 72–84. |

**Against the expectation.** None was registered. The theorem came out as expected. What I did not expect is how weak its bite is: the divergence is logarithmic in the light-cone direction. Any infrared cut there at the Hubble scale (age or friction) makes both sides finite with a logarithm L ≈ 72–84. So the stationary no-go is exact, but the physical price it forces is structural (a time origin or a dissipative metric), not large. The quantitative constraint is the product bound of §2, Corollary U_L.

---

## 0. In plain words

- A classical metric that is a record has to pay for its pull on matter with noise. That is the decoherence–diffusion trade-off, and it holds for the total noise matter feels, however the noises are correlated.
- Near the light cone, the undamped wave equation amplifies the record's noise by 1/s², where s measures the distance from the cone. It is driving an oscillator exactly at resonance.
- So the product (matter's noise) × (the metric record's noise) is at least a constant times 1/s². Its square root, 1/|s|, has infinite area across the cone. At least one of the two must therefore be infinite near the cone.
- Nothing else is used: not Gaussian statistics, not Markovian memory, not Lorentz invariance, not the absence of correlations. Only three things enter: a stationary state; a record that can be read without disturbing what comes later (Belavkin's non-demolition condition); and an undamped massless wave equation for the metric.
- The infinity is only logarithmic. It comes from the process having run forever. If the universe has an age, or classical gravitational waves are damped even slightly (at the Hubble rate or below), both sides become finite, with a factor of about 75. The trade-off then remains: shrinking one side by a factor ε inflates the other by 1/ε.

---

## 1. Prior art (each counted once)

1. **R8-3** (`TESTS:3559-3573`; `vR8-3:5,11,19`). Lemma 1 (a Lorentz-invariant excitation measure is zero or infinite). Lemma 3 (a cone jump gives ln(1/ε)). The repaired trilemma in the additive, pointwise-trade-off, common-scalar or GR-normalized spin-2 subclass.
2. **R9-4** (`TESTS:3909-3915`; `vR9-4:3,9,11`).
   - (H-T) follows frequency by frequency from a stationary linear non-demolition meter with zero reverse gain. It is **not** a theorem for general CP CQ histories (`C5_R9-4_referee.md:33`).
   - Lemma E: a finite Lorentz-invariant vacuum forces emission-side cancellation (almost everywhere).
   - 1/|s| is not locally finite.
3. **R10-3** (`TESTS:4287-4296`; `vR10-3:9,13,19`).
   - The general correlation bound σ_sum ≥ ħ²|F|²/(2P) (`C5_R10-3_report.md:166-169`).
   - **Lemma Z** (`:173-176`), whose remark already says Lorentz invariance is used only to reduce 4D local finiteness to s-integrability.
   - Theorem P (`:178-189`), refereed correct once positive dispersion and locally finite covariance are explicit (`vR10-3:9`).
   - **Theorem U below is Lemma Z freed of Lorentz invariance, Gaussianity and emission silence. It is not a new mechanism.**
4. **R11-5** (`TESTS:4438-4445`; `vR11-5:6,18,22`). Lemma C in T_u, corrected to D′₀ + a²P_J/s² ≥ a|F|/|s|. A finite frame age is allowed as a named price. A finite-s₀ stationary kernel eventually gives linear record growth.
5. **R6-4** (`TESTS:3409-3418`; `vR6-4:5-25`): the Newtonian least-decoherence floor, and the record-reading prices on all four axioms (`vR6-4:19`).
6. **Repository grep** for "GW damping", "damping rate", "viscous", "Hawking 1966" and "friction" over `P/TESTS.md`, `P/SUMMARY.md` and `P/PRICE_NOTE.md`: no hits. The only "friction" in C5 is R11-5's *matter* drag (`C5_R11-5_report.md:139,208`), a different object. A `docs/` grep for "classical-quantum" or "CQ gravity" hits only unrelated record or instrument notes (for example `docs/proofs/original_microscopic_output_2026_09_30/local_trajectory_and_rotor_limit.md:50`). R10-3 listed "a non-massless or modified G (costs radiation)" as an escape (`C5_R10-3_report.md:205`). §5 quantifies that cost.

---

## 2. The class 𝒰 and Theorem U

### Class 𝒰 (stated before any title)

Linearized CQ gravity on Minkowski space, per spin channel, at second order in the matter coupling (golden-rule / influence-functional order).

- **U1. Stationary and spatially homogeneous.** The (dilated or effective) process is invariant under 4D translations. The kernels may depend on (ω, **k**) in any frame, so the class is Lorentz-invariant or frame-tied. Markovian or not.
- **U2. Classical metric record.** h = G_R·J (+ deterministic mean), with J the classical record and G_R the standard **undamped** massless retarded propagator. Near a regular null point p₀ ≠ 0, |G_R(p)|² = g²/s² off the cone, with g ≠ 0 (GR normalization in the channel).
- **U3. Matter's noise.** Matter couples linearly to the felt field f, with symmetrized noise spectrum σ̄(p) (the Feynman–Vernon noise kernel, which carries decoherence and diffusion). The record has symmetrized spectrum P̄(p). The metric-record covariance is M(p) = |G_R(p)|²P̄(p).
- **U4. Gain.** F(p) is the linear gain from matter's stress to J (Newton fixes F(ω = 0, k → 0) = 1).
- **U5. The felt-field noise–gain bound (H-T_f).** At every p, σ̄(p)·P̄(p) ≥ κ|F(p)|², with κ > 0 fixed. (H-T_f) holds under either of two sufficient conditions:
  - **(a) Lemma K (proved).** In any stationary dilation, Gaussian or not, in which J is a non-demolition record — self-commuting, and [B(t), J(t′)] = 0 for t > t′, i.e. zero reverse gain — and f = B + G̃J for any linear G̃: |C_fJ(p)| = ħ|F(p)| and σ̄_f·P̄ ≥ ħ²|F|²/4.
  - **(b)** The additive form: σ̄ = D + (record part) with (H-T) on D, i.e. P̄·D′₀ ≥ ¼ (R8-3 H3′; R11-5 H3).
- **U6. The cone.** F is continuous at a regular null point p₀ with F(p₀) ≠ 0, forced by Newton plus finite radiation (R8-3 Lemma 3; R9-4 Lemma L, refereed `vR9-4:5`). A **one-sided** lower bound |F| ≥ f₀ > 0 on 0 < ±s < δ suffices.

**Realizations outside 𝒰:** listed in §5.

### Lemma K (felt-field bound for any correlation and any state; proved)

**Setting.** Spectra S_XY(ω) = ∫e^{iωt}⟨X(t)Y(0)⟩, with the spatial Fourier variable implicit. Wightman positivity makes the 2×2 matrix of (f, J) Hermitian and positive semidefinite at every p, for **any** stationary state. Gaussianity is not used.

**Proof.**
1. The commutator spectrum is C_fJ(p) = S_fJ(p) − S_Jf(−p).
2. J self-commuting gives C_JJ = 0, so C_fJ = C_BJ.
3. Zero reverse gain makes ⟨[J(x), B(0)]⟩ purely retarded. That is Kubo's forward gain, so |C_fJ| = ħ|F|.
4. Then |C| ≤ |S_fJ(p)| + |S_fJ(−p)| ≤ √(S_ff(p)P̄) + √(S_ff(−p)P̄) ≤ 2√(σ̄P̄), by Cauchy–Schwarz twice. ∎

**Checks.**
- [1]: 200000 random spectra, minimum ratio 1.013, no violations. Equality is attained (ratio 1.000000000000).
- [2]: a random 7-level **non-Gaussian** stationary system, 1480 frequency bins, minimum ratio 1.0027, no violations.
- [3]: in the QMFS shell, emission-silent f gives ratio 2, which is R10-3's absorption-only value. f = x_a − x_b attains 1.

**Notes.**
- Correlations can push σ̄ far below the *additive* floor |G||C| (checked [1]: 5e-4 of the floor at P = 100). That is R9-4's sub-floor (`C5_R9-4_report.md:162-167`). They cannot push the **product** σ̄P̄ below ħ²|F|²/4.
- **Measure version (proved).** Lemma K holds for Borel sets E with C(E) = iħ∫_E F. Lebesgue differentiation then gives σ̄_ac·P̄_ac ≥ ħ²|F|²/4 almost everywhere. Singular parts only add, so singular spectral weight on or near the cone cannot evade the bound.
- **Belavkin.** The non-demolition principle, stated as past records commuting with all later system Heisenberg operators (Belavkin–Staszewski; comparator, web search this run), is exactly zero reverse gain plus a commuting record. So U5(a) is the definition of a classical record that can be fed back. It is not an extra technical assumption.

### Theorem U (unified cone no-go; proved in 𝒰, referee required)

**Statement.** In 𝒰, near a regular null point p₀ with |F| ≥ f₀ on a one-sided neighbourhood N:

  **σ̄(p)·M(p) ≥ κ g² f₀² / s²**  (almost everywhere on N),

so the matter-noise measure σ̄ and the metric-record covariance M are **not both locally finite** on N. Equivalently, for every a > 0, σ̄ + a²M ≥ 2a√κ g f₀/|s|.

*Proof.*
1. Multiply (H-T_f) by |G_R|² = g²/s².
2. Cauchy–Schwarz gives (∫_N σ̄)(∫_N M) ≥ (∫_N √κ g f₀ / |s|)².
3. Near p₀ ≠ 0, s = ω² − |**k**|² is a smooth local coordinate, with |∇s| = 2|p| ≠ 0 in any frame. So ∫_N d⁴p/|s| = ∞. ∎

[checked [5]: in a frame-tied 4D box around (1, (1,0,0)), the volume fraction with |s| < x is linear in x (density 2.47). The integral of d⁴p/|s| grows as 2 ln(1/η), and Monte Carlo agrees with the shell estimate (0.04860 vs 0.04897).]

**Corollary U_L (regulated product bound; proved).** Suppose the cone is cut at s_* > 0. Either the wave operator is damped, |G|² = g²/(s² + s_*²), or the bound is used only on |s| > s_* (finite time, s_* ~ 2ω/T). Then

  (∫_band σ̄)(∫_band M) ≥ κ g² f₀² · (2 asinh(δ/s_*))², which is ≈ 4κg²f₀² L² with L = ln(2δ/s_*).

[checked [4]: the product over the bound equals 1.000 for the floor split at s_min = 1e-4 to 1e-32. Every other profile (power-law, log-squared, ε-band) exceeds it, and one factor grows without bound. checked [6]: with damping, the saturated split has both integrals equal to κL and g²aL exactly.]

**Reading.** The product bound is profile-independent. Any near-cone suppression of the record by ε (R9-4's P-r9b, R11-5's P-r9b′) inflates matter's near-cone noise by 1/ε, mode by mode. R11-5's e(s) profile is one point on this trade, not a choice that could be improved past it.

---

## 3. Containment: T_E, T_u and R8-3's subclass are in 𝒰

| Class | How it meets 𝒰 | What Theorem U reproduces |
|---|---|---|
| **T_u** (R11-5) | Frame-tied, stationary, standard G_R, continuous non-zero cone gain. Its kernel is additive: K = \|F\|²(D′₀ + \|G\|²P_J) (`C5_R11-5_report.md:90`), with (H-T) P_J·D′₀ ≥ ¼, so U5(b) holds: K·P_J ≥ \|F\|²/4. | K·M ≥ \|F\|²g²/(4s²) gives the referee-corrected Lemma C, D′₀ + a²P_J/s² ≥ a\|F\|/\|s\| (`vR11-5:6`), up to normalization. **proved** |
| **T_E** (R10-3) | Lorentz-invariant stationary linear meter, with a self-commuting record and zero reverse gain, so U5(a) holds by Lemma K. | Under emission silence, σ̄ = ½S_ff(p) ∝ ρ on the timelike side, and (N) with positive dispersion makes ∫ρ locally finite (R10-3 step, `vR10-3:9`). One-sided Theorem U then gives M non-locally-finite: that is Theorem P. **proved** (given R10-3's refereed dispersion step) |
| **R8-3 subclass** | Lorentz-invariant, additive, with pointwise H3′: K = D₀ + c²\|F\|²P_J/s² and P_J·D₀ ≥ \|F\|²/4 (`C5_R8-3_report.md:97-99,125-131`). So U5(b) holds. | (D) ∧ (M) is impossible there too. **But R8-3's own failure is different and stronger:** Lemma 1's boost-orbit infinity of the vacuum rate (`vR8-3:5`). Theorem U does not reproduce it, and a cone regulator does not cure it (§6). **proved** for containment; reading for the comparison |

Also contained, as a bonus: R9-4 (i) (spacelike-only noise). With |F| ≈ 1 on the spacelike side, Theorem U fails on that side alone, independently of Lemma L's ln r (proved, one-sided).

---

## 4. The REFUTED direction (tried; no counterexample in 𝒰)

I tried every way I could see to keep both σ̄ and M locally finite inside 𝒰. Each attempt fails for the reason given:

1. **Correlations, emission cancellation, sub-floor feedback.** Lemma K bounds the product, not σ̄ alone (checked [1]).
2. **Non-Gaussian, jump or counting records.** Wightman positivity alone gives Lemma K (checked [2]). Second-order decoherence depends only on two-point functions.
3. **Singular spectral weight on or near the cone.** The measure version covers it: the off-diagonal C = iħF is absolutely continuous.
4. **Free incoming classical waves, or another Green function** (advanced, symmetric) correlated with J. These live *on* s = 0, while the divergence is the off-cone 1/s², which every Green function of the undamped □ shares.
5. **Fine-tuned F.** If F vanishes near the cone but not on it, there is a jump (ln r radiation; `vR9-4:5`). If it vanishes on the cone, there is no GW emission, against binary-pulsar decay and LIGO (comparator, RECALLED). The one-sided form survives a jump in any case.
6. **Lorentz-invariant dressing of G_R** ([7]):
   - a Maxwell-type stress loop Π ~ s² ln|s| leaves the pole intact (|G|·|s|/g → 1);
   - a field-strength log leaves ∫|G| divergent as ln ln (numeric equals exact, for example 49.997 at ln(1/s_min) = 1474);
   - only a non-zero absorptive threshold, Im Σ(0⁺) ≠ 0, removes the pole. That destroys the 1/r radiation zone, so it fails (R) (suggested; it is also impossible with a local stress coupling, where Im Π ∝ s²).

**Result.** No stationary model in 𝒰 has both finite. **REFUTED does not apply.**

**The explicit stationary model with both finite** (checked [6]) has frame-tied friction on the classical TT metric, G = g/(s + iγω), with the saturated split P̄ ∝ √(s² + γ²ω²). It violates U2. It belongs in §5, not here.

---

## 5. What exactly is left (outside 𝒰)

| Escape | Status | Cost |
|---|---|---|
| **(E1) Finite-time process (a start time)** | OPEN (R11-5 route; allowed as a named price, `vR11-5:18`). | Both sides grow at least as ln T. Their product grows at least as (ln T)² (Corollary U_L). At t_H, L = ln(ωt_H) = 72.3–78.6 for ℓ = 5e-6 to 1e-8 m ([8]), matching R11-5's 72–79 (`vR11-5:15`). |
| **(E2) Dissipative classical GWs (new):** frame-tied friction γ on the TT metric, the Hawking viscous-damping form | **Stationary**, both finite (checked [6]). The dilation is argued only, as R11-5's meter bank; not built. | L = ln(2ω/γ): 73–79 at ℓ = 5e-6 to 1e-8 m for γ = H₀ ([8]). GW amplitude loss at γ = H₀: 0.45% at 40 Mpc, 10.7% at 1 Gpc ([8]). Amplitude damping γ/2c = 1.1e-4 Mpc⁻¹, against a published bound of 6.75e-4 Mpc⁻¹ (95%) from LIGO/Virgo data (comparator, abstract web-checked; whether it is an amplitude or an energy rate is not checked, and either way passes at γ = H₀). Choosing γ = 0.01H₀ adds only 4.6 to L. Phase-velocity shift 1.5e-42 at 100 Hz. **This corrects R10-3's "modified G (costs radiation)" (`C5_R10-3_report.md:205`): the radiation cost is small.** It needs a frame, since no Lorentz-invariant dressing does this (§4.6), and an energy sink for the damped classical GW energy (the hidden meter sector; suggested). |
| **(E3) Nonlinear order** (matter coupling to h², self-gravity of the record) | Not covered by Theorem U. R10-3 flagged a likely nonlinear failure (`C5_R10-3_report.md:232`; suggested). | — |
| **(E4) No stationary non-demolition dilation** | The R9-4 referee's open gap (`C5_R9-4_referee.md:33`). (H-T_f) is a defining wall of 𝒰, not a theorem about CP CQ histories. | — |
| **(E5) Spatially structured meters** (a lattice of meters, set-C-like) | Suggested: Lemma K is convex, so it survives translation-averaging, and Theorem U would then hold for the averaged spectra at k ≪ 1/a. Not proved. | — |
| **(E6) Metric not linear in the record, or a non-stationary frame** (FRW) | Outside. FRW supplies both a frame and an age, with a cone cut at ~H (reading). | — |
| **(E7) Lorentz-invariant models** | Theorem U applies. Separately, Lemma 1 + Lemma E (refereed) force either an infinite vacuum or quantum-bath timelike transfers. A start time does not cure Lemma 1, because the boost orbit is unbounded in frame energy at any age (suggested). | — |

---

## 6. Minimal price for set A's "records are the metric"

Combining the refereed results with Theorem U (proved here, unrefereed):

1. **P-r1, a preferred frame (forced).**
   - Lorentz-invariant stationary records give an infinite vacuum (R8-3 Lemma 1), or emission-silent quantum-bath timelike physics (R9-4 Lemma E; T_E EXCLUDED, `vR10-3:19`). Both are refereed.
   - The cone regulator below also needs a frame or a time origin (§4.6).
2. **One cone regulator (forced by Theorem U).** Either:
   - **P-r11a, a start time** (finite frame age). Axiom text: the record-production law (`AX:185-186`, open gate) acquires a time origin, and "No site is privileged" (`AX:40`) gains a privileged slice. Or:
   - **P-r12a (new), dissipative classical GW propagation** at a frame-tied rate γ ≲ H₀. Stationary. The record stays permanent (`AX:79-80`); the metric becomes a leaky functional of permanent records. It needs an energy sink.
   - **Cost:** either way, a logarithm L ≈ 72–84 at k ~ 1/ℓ.
3. **The near-cone trade (forced, profile-independent by Corollary U_L).** Near-cone record content × near-cone matter noise ≥ 4κg²f₀²L² per mode.
   - R11-5's conditional numbers (ε ~ 1e-11 to 1e-6; a search interval of roughly 4e-7 to 5e-6 m, `vR11-5:12,15`) are one realization of this trade.
   - The lower edge depends on the unresolved premise of whether near-cone TT noise gravitates.
4. **Carried over:** R6-4's P-i1–P-i5 and its (iii) axiom prices on Lattice, Qubit, Admissibility and Record (`vR6-4:19`); P-r11b (driven meters, by Lemma Q, `vR10-3:5`); P-r4 (vacuum photons).

**Which regulator is cheaper (reading).** E2 avoids a start time but adds a dissipative metric and a sink. E1 keeps □ but makes the law non-stationary. Neither is observationally excluded. Both give the same L, to within ln(γt_H).

---

## 7. Strong words checked

- **"Proved"** covers Lemma K (any stationary state, non-demolition record), its measure version, Theorem U, Corollary U_L, and the containments of T_u and R8-3. For T_E, containment relies on R10-3's refereed dispersion step.
- **"Not both locally finite"** means the one-sided 4D neighbourhood integral diverges, logarithmically (|s|⁻¹). **"Infinite"** never means the boost-orbit infinity of R8-3 Lemma 1 in this report.
- **"Every model in 𝒰"** means: U1–U6, second order in the matter coupling, per spin channel.
- **"Non-Gaussian is not an escape"** holds only with a stationary non-demolition dilation and a linear record→metric map.
- **Suggested only:**
  - E2's dilation and energy sink;
  - E5;
  - the "fails (R)" physics of the absorptive threshold in [7](c);
  - the statement that a start time does not cure Lemma 1;
  - the γ ≤ H₀ observational comparison (abstract-level).
- **"DERIVED"** is a worker reading. Theorem U is essentially R10-3's refereed Lemma Z with its scope widened. I claim no new mechanism.

## 8. What would decide it

1. **A referee of Lemma K** (especially the claim that zero reverse gain is Belavkin non-demolition, and the non-Gaussian extension), **Theorem U, Corollary U_L, and the T_E containment.**
2. **For E2:** an explicit stationary dilation with friction γ, including where the GW energy goes, a Bianchi/second-order check, and a fit to standard-siren distance data.
3. **Close E4:** prove or refute that every stationary CP CQ history has a stationary non-demolition dilation.

**Sources.**
- Web search this run:
  - Belavkin's non-demolition principle (Belavkin–Staszewski, [ar5iv quant-ph/0512138](https://ar5iv.arxiv.org/html/quant-ph/0512138); [Nottingham publications](https://www.maths.nottingham.ac.uk/personal/vpb/publications/nwem-pla.pdf));
  - Hawking 1966 viscous GW damping, amplitude factor exp(−8πGηΔ/c³) (via [arXiv:2405.07743](https://export.arxiv.org/pdf/2405.07743) and [arXiv:1708.05576](https://arxiv.org/pdf/1708.05576), search snippets).
- Abstract web-checked: [arXiv:1803.11397](https://arxiv.org/abs/1803.11397), GW damping rate below 6.75e-4 Mpc⁻¹ (95%, LIGO/Virgo combined).
- Via earlier referees: Clerk et al. 0810.4729 Eq. (90); Tsang–Caves PRX 2, 031016; Layton et al. 2307.02557; OWD 2302.07283.
- RECALLED: Diósi/Tilloy least-decoherence (not load-bearing); H₀, t_H; binary-pulsar GW emission.
