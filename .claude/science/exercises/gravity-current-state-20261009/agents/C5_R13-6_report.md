# C5 round 13, probe R13-6: set A, route E1, an explicit start-time CQ dilation (worker report)

**Worker.** Claude Opus 5.5. This is the same model family as the supervisor and every C5 worker.
- **Not refereed.**
- Run 2026-10-12, 20:14Z to about 20:50Z.
- No repository file was edited.

**Scratch:** `scratchpad/C5/R13-6/`.
- `scripts/r136_checks.py` and `scripts/r136_checks.out` (sections [1]–[11]) hold every number below.
- Runtime is about 20 s with OMP_NUM_THREADS=2.
- SHA-256: script `70ef0c37…c1cacf`, output `0f6fa55f…62df`.
- No downloads and no web fetches in this run. Comparators are either via earlier referees or RECALLED.

**Paths.**
- `P/` = `.claude/science/exercises/gravity-current-state-20261009/`.
- `TESTS` = `P/TESTS.md`; `AX` = `docs/MINIMAL_AXIOMS_2026-06-29.md`.
- `vR11-5` = `P/agents/C5_R11-5_referee_verdict.md` (and so on). Bare `C5_*` files are in `P/agents/`.
- `out:[n]` = section n of `scripts/r136_checks.out`.

**What I read.**
- In full:
  - `AX`; `TESTS:2302-2320` (C5 method); `TESTS:4560-4694` (round 13; R13-6 at `:4682-4692`);
  - `C5_S14_synthesis.md` (grep plus §1.5, §3, §5);
  - `SUMMARY.md:534-675` (§§21–25);
  - `C5_R11-5_report.md`, `vR11-5`, the full referee report `scratchpad/C5/ref_R11-5/C5_R11-5_referee.md`;
  - `C5_R12-4_report.md`, `C5_R12-4_referee.md`, `vR12-4`;
  - `C5_R6-4_report.md`, `vR6-4`;
  - `C5_R10-3_referee.md`, `vR10-3`;
  - `C5_R12-7_report.md`. This is the comparison partner; it is unrefereed and used as a worker claim.
- Scripts: `scripts/C5/R11-5/r115_checks.{py,out}`; `scripts/C5/R12-7/r127_checks.py:100-294` and its output; `ref_R11-5/scripts/r115_referee_checks.out` (the L_eff roots).

**Labels.**
- **proved:** derived here under the stated hypotheses.
- **checked:** a number in `r136_checks.out`.
- **suggested:** argued, not proved; order of magnitude unless stated.
- **reading:** an interpretation.
- **comparator:** literature, via an earlier referee, or RECALLED.

**Subtraction rule (`TESTS:4566`).** Every growth, decay or tail clause below concerns a positive spectral density, a positive energy, or a probability. So nothing is subtracted ("subtraction: none"). There are three exceptions:
- the finite-start correction to lab kernels is measured against the stationary kernel;
- the drag of §5.2 is the odd-in-ω part of the gain. The even part is not subtracted; it exerts no force on a symmetric body;
- the waveform check is measured against F = 1.

Each script section prints its subtraction.

**Order rule (`TESTS:4566`).** The exactness conditions hold at these orders:
- **linear order in G (mean field):** γ = 1, c_T = c, the static limit, and the zero first-order delay of the repaired gain;
- **second order in the matter–meter coupling (Gaussian, golden-rule):** saturation (P·D = |F|²/4) and complete positivity, which holds at every order for the Gaussian dilation;
- **second order in the metric noise:** the noise-fed PPN term.

---

## Reading against the FIXED rule (`TESTS:4688-4691`)

**Worker reading: EXCLUDED for the class as literally specified.** This is a no-go, so a **referee is required**. In the repaired class, the reading is **OPEN**.

**1. The literal class is excluded.** The literal class is R11-5's 𝒦_ε with its gain F_u = e^{−k²ℓ²/2}(1 − iωτ)^{−n}, τ = ℓ/c, integer n ≥ 3 (`C5_R11-5_report.md:156`).
- **Lemma D (§5.2)** shows the following. This causal gain delays the mean field by δ = nτ in the CMB frame. So every moving body is pulled back by its own lagging field, at rate Γ = (4πG/3)δ∫ρ²/M.
- For the double-pulsar neutron stars this dissipates orbital energy: Ṗ_b/P_b = −3Γ.
- The measured agreement with GR (1.3e-4) needs δ < 3.7e-29 s, which means ℓ < 4e-21 m. The class has δ = 3ℓ/c ≥ 4e-18 s across R6-4's window. **Every ℓ_s is violated, by factors 1e11 to 1e15** (checked [10], [11]).
- The failure is in the mean-field gain, not in the start time. So it equally hits R11-5's stationary kernel and R12-7's E2, which carries the same F_u (`C5_R12-7_report.md:153`).

**2. The repaired class is OPEN.** The repair is the same gain with a zero first moment: (1 − inωτ)(1 − iωτ)^{−n}, n ≥ 4. This is a named price, P-r13b.
- **Probe (a): done**, at the level of transfer functions and Gaussian covariances, per frame mode, for the scalar channel. The pieces are:
  - an exact causal spectral factor;
  - a single-port, exactly saturated meter;
  - the finite-start state and covariance in closed form;
  - complete positivity (CP).
- **Probe (b): done.** Record growth is ε·ln t on the whole domain t − t₀ ≤ t_H for the explicit network (coherence time ≥ t_H). In the s₀ = 0 limit it is ε·ln t forever and never becomes linear.
- **Probe (c):** the stated list passes, including the noise-fed term, by ≥ 50 decades (suggested normalization).
- **Probe (d): not closed**, so VIABLE is not reached:
  - Strictly in 𝒦_ε (τ = ℓ/c), the energy budget still needs R11-5's near-cone suppression ε(ℓ), and so R11-5's assumed coefficients.
  - A decoupled gain scale τ_c removes ε entirely. But its window is bounded above by the residual neutron-star drag and depends on the neutron-star density profile (suggested).
- The spin-2, conserved-noise assembly is not built. This is the same gap as R12-7's.

| Clause (`TESTS:4686`) | Status |
|---|---|
| (a) positive synthesis measure | **R11-5's displayed profile has none** for cone-centred Lorentzian lines (proved; checked [2]). Its Stieltjes density is negative on t ∈ (ε², ε). Two positive measures are given instead: the arcsine measure of the causal factor (checked [1]), and a Stieltjes member of the family (checked [2]). |
| (a) causal spectral factor | **Ĥ = (Ω² − (ω+i0)²)^{−1/2} ↔ θ(τ)J₀(Ωτ)**, with Ĥ² = G_R. Both Ĥ and 1/Ĥ are causal. The suppression factor e_± is explicit and rational (proved; checked [1], [2]). |
| (a) finite-start state and covariance | At t₀ the meter is in vacuum and h = ḣ = 0. The record side is exact: Var h_k(t) = ½∫₀^{t−t₀}J₀²(Ωτ)dτ = (ln 8ΩT + γ_E)/(2πΩ) + o(1) (proved; checked [4] to 6 digits). The quantum backaction is explicit for finite networks with Γ_min ≤ 1/t_H. The exact s₀ = 0 network is a limit, suggested only (§3.4). |
| (a) exact map bank → spectra | Single-port network: gain g = H_x and post-filter R = F/g. This gives D = \|F\|²D′₀ and P_J = 1/(4D′₀) **exactly** (proved; checked [3]). A parallel bank cannot be causally saturated without an all-pass whose delay is about 16/Γ_min, which is Hubble-scale (proved; checked [3]). |
| (a) CP | Proved for every finite age: a unitary dilation, a homodyne instrument on commuting outputs, and record-conditioned causal feedback. The irrational factor is a limit of finite networks on [t₀, t]. |
| (b) record growth | With s₀ = 0, the slope is dE/dln T = ε up to T = 1e14/Ω. With s₀ > 0, growth becomes linear for T ≫ 1/s₀, which lies beyond t_H when s₀ ≤ 1/t_H (checked [4]). Size at t_H: §4. |
| (c) R11-5's tests + noise-fed PPN | Pass for the repaired gain (table §5.1). **New test (Lemma D): FAIL for the literal gain at every ℓ** (§5.2). |
| (d) ℓ_s interval | Literal class: none. Repaired, strict τ = ℓ/c: the stated list passes on 4e-10 to 5e-6 m. With the energy budget, R11-5's conditional interval of about 4e-7 to 5e-6 m stands (`vR11-5:12`). Repaired with τ_c: §6. |
| (e) prices | §7. |

**Against the expectation (`TESTS:4692`).** The expectation was "OPEN, leaning VIABLE near 4e-7 to 5e-6 m; the noise-fed PPN term is the likeliest failure."
- The noise-fed PPN term passes by more than 50 decades (suggested).
- The start time itself costs nothing observable.
- What fails is something no earlier C5 probe computed: the record gain's causal delay drags moving bodies toward the CMB frame. R11-5 checked the same delay only against GW170817's 1.74 s (`C5_R11-5_report.md:185`). That is the wrong test by about 30 orders of magnitude.

---

## 0. In plain words

- **The start-time model can be written down exactly.** The cheapest record that keeps matter's noise as low as Newton allows has a precise form. Its metric noise is white noise passed through the "square root" of the wave equation's response.
  - In time, that square root is a Bessel function J₀(c|k|t). It never dies off exponentially, so it has no steady state with finite noise.
  - Switch it on at a start time and everything is finite. The metric noise grows only as the logarithm of the age.
- **No hidden bank of oscillators is needed** to get the right spectra exactly. A single-channel meter whose response is that square root does it, with no wasted noise.
  - R11-5 proposed a bank of separate meters instead. Its exact profile cannot be built from cone-centred single-mode lines with positive weights.
  - A bank of separate meters can only be made noise-optimal by delaying the record by about 16/Γ_min, which is Hubble-scale.
- **A start time does not change any lab, Solar System or GW test.** At today's age the start-time corrections are below 1e-15 at Solar-System scales and smaller, and about 2e-7 at kiloparsec scales.
- **But the smearing in time breaks something new.** R11-5's form makes gravity respond with a tiny delay (3ℓ/c, at most 5e-14 s) in the cosmic rest frame.
  - A moving star then feels its own gravity lagging slightly behind it. That is a brake toward the cosmic rest frame.
  - Neutron stars are so dense that the brake is strong. At the smallest smearing length a neutron star would lose its speed through the cosmic frame in about 50–80 years. The double pulsar's measured orbital decay rules it out at every smearing length, by 11 to 15 orders of magnitude.
  - R12-7's friction route uses the same smearing, so it has the same problem.
- **The fix is cheap.** Use a time filter whose average delay is zero (it "extrapolates" slightly). The brake then drops by (vτ/R)², to about 1e-29 s⁻¹, far below the bound.
- **With the fix, the start time passes every stated test.** What stays open is the energy budget of the record's own gravitational waves.
  - With R11-5's smearing time τ = ℓ/c this needs R11-5's near-cone suppression and its unmeasured coefficients.
  - Choosing a separate gain time τ_c of about 0.6–8 ps removes the suppression altogether. Its upper limit comes from the leftover neutron-star brake and depends on the star's density profile.

---

## 1. Prior art (each counted once)

1. **R11-5 and verdict** (`vR11-5:6,9,15,18,22`).
   - Lemma C, with the corrected |F|.
   - The four-stage chain is confirmed (CP, saturated, χ_FF = 0).
   - Missing pieces: the positive synthesis measure, the causal factor, the finite-start covariance and the exact map. These are this item's probe (a).
   - Log growth needs the non-locally-finite limit; a finite s₀ gives linear growth (`vR11-5:6`).
   - A finite frame age is allowed as a price (`vR11-5:18`).
   - Premise-(ii) roots of about 1.73–4.02e-7 m with L_eff ≈ 50–53 (`vR11-5:15`; `ref_R11-5/scripts/r115_referee_checks.out:52-54`).
2. **R12-4 and verdict** (`vR12-4:5-19`).
   - Theorem U and Corollary U_L (regulator-dependent L²).
   - A start time is a temporal boundary, not a breach of `AX:40` (`vR12-4:15`).
   - The E1 row (`C5_R12-4_report.md:162`).
3. **R6-4** (`vR6-4:7,19`): the least-decoherence floor; the window 4e-10 to 5e-6 m; the record-reading prices.
4. **R10-3** (`vR10-3:5,13`): Lemma Q (driven meters); a non-locally-finite covariance is not a stationary record.
5. **R8-3 and R9-4.**
   - R8-3 introduced the causal smearing F_u.
   - Its lag was compared only with GW170817 (`C5_R8-3_report.md:203,212`; `C5_R11-5_report.md:185,220`).
   - R9-4 (`vR9-4:11`): n ≥ 3.
6. **R12-7** (worker, unrefereed). It is the comparison partner, not prior art for E1's construction.
   - It uses a parallel bank with X ∈ [1, 2.47] (`C5_R12-7_report.md:79-86`).
   - Its frame drag formula for E2-h is at `:145`.
7. **Repository grep.**
   - Searched `P/TESTS.md`, `P/SUMMARY.md`, `P/PRICE_NOTE*`, `P/agents/` and `docs/` for: "aberration", "speed of gravity", "Laplace's", "group delay", "minimum phase", "outer function".
   - No hits in the sense used here. "Laplace" hits are all "Laplacian". "Paley" hits are RG/RC lattice notes.
   - "Spectral factor" hits only `vR11-5`, S14, R12-7 and R5-4's verdict, in a different object.
   - "Stieltjes" hits R10-3's dispersion step and others, in different objects.
   - **There is no prior computation of a self-drag or an orbital aberration from the record gain's delay.**

## 2. Hypotheses: class ℰ₁ (stated before any title)

- **E1-H1.** Linearized Gaussian CQ gravity on Minkowski space with mean GR coupling: h = G_R·J, and matter feels h through ½h_μν(g*T^μν) (spatial smearing g, as `C5_R11-5_report.md:143`). Fixed CMB frame u.
- **E1-H2.** Per frame mode k and spin channel, the record is J = F·(T + ξ) with the noise split of 𝒦_ε: D′₀·P_J = ¼ (saturated). The profile e(s) can have ε ∈ (0, 1], and **s₀ = 0** (no coherence-time regulator).
- **E1-H3 (start).** At frame time t₀ the following hold:
  - the meters are in their vacuum (a product state with matter);
  - h(t₀) = ḣ(t₀) = 0;
  - all couplings switch on.

  Every statement is for t − t₀ = T ≤ t_H.
- **E1-H4.** The gain is F = e^{−k²ℓ²/2}·F_t(ω) with F_t causal. Two choices:
  - **literal:** F_t = (1 − iωτ)^{−n}, τ = ℓ/c, n ≥ 3;
  - **repaired:** F_t = P(−iωτ)(1 − iωτ)^{−n} with a polynomial P chosen to zero the first (or first and third) moment of the impulse response, n ≥ 4 (or 5). The variant τ = τ_c ≠ ℓ/c is stated separately.
- **E1-H5.** Golden-rule (second) order in the matter–meter coupling. Newtonian mean field for the drag tests.

**Excluded realizations.**
- GW friction (R12-7).
- Non-Gaussian and jump records.
- A dynamical frame.
- Non-linear gravity beyond the noise-fed second-order estimate.
- The full spin-2 conserved-noise assembly. This is not built; see §8.

---

## 3. Probe (a): the explicit finite-start construction

### 3.1 Lemma S: the causal spectral factor of the saturated split (proved; checked [1])

Per frame mode, let Ω = c|k| and s = ω² − Ω². The least-decoherence split of R9-4 and R11-5 (`C5_R11-5_report.md:157-159`, with ε = 1) is

  D′₀ = 1/(2|s|),  P_J = |s|/2,  D′₀·P_J = ¼.

**Statement.** Let Ĥ(ω) := (Ω² − (ω + i0)²)^{−1/2}. Then:
- |Ĥ|² = 1/|s| on the real axis, and Ĥ² = G_R.
- Ĥ and 1/Ĥ are both analytic in the upper half plane, so both are causal. 1/Ĥ grows at most like |ω|, so it is a causal distribution of order 1 by Paley–Wiener–Schwartz (comparator, RECALLED).
- In time, Ĥ ↔ θ(τ)J₀(Ωτ).

*Proof.*
- ∫₀^∞ J₀(Ωτ)e^{−pτ}dτ = (p² + Ω²)^{−1/2} for Re p > 0, with p = −iω + 0.
- (p² + Ω²)^{±1/2} has no zeros or branch points for Re p > 0.
- (J₀ * J₀)(τ) = sin(Ωτ)/Ω is the Laplace convolution theorem. ∎

**Checks.**
- The Laplace identity holds to 1.7e-15 at 12 points.
- |Ĥ|²·|s| = 1 at ω = 0.5, 0.99, 1.01, 3.
- An upper-half-plane scan (Im ω ∈ [1e-6, 1e2]) gives 9.99e-3 ≤ |Ĥ| ≤ 707: no zeros or poles.
- J₀*J₀ = sin to 8 digits at τ = 1, 5, 20.

**Consequence.** The saturated record is exactly realizable at the transfer-function level:
- backaction transfer H_x = √2·F·Ĥ;
- gain g = H_x;
- post-filter R = F/g = Ĥ^{−1}/√2 (causal).

The metric-record noise is then **h_noise = Ĥ·ξ**: white noise passed through the "half-retarded propagator". Its stationary covariance |Ĥ|²/2 = 1/(2|s|) is exactly Theorem U's non-locally-finite object. With a start time it is a well-defined process (§3.4).

### 3.2 The suppression factor (proved; checked [2])

e(s) = ε + (1 − ε)s²/(s² + δ²) = (s² + εδ²)/(s² + δ²).

**Outer factor in ω.** Let ω_b = √(Ω² − ib) (Re > 0, Im < 0). Then |s + ib| = |(ω − ω_b)(ω + ω_b*)| on the real axis, and both roots lie in the lower half plane. So the outer factor of e is

  e_+(ω) = [(ω − ω_{εδ})(ω + ω*_{εδ})]/[(ω − ω_δ)(ω + ω*_δ)],

with |e_+|² = e to 1.7e-13 (checked).
- Zeros sit at Im = −εδ/(2Ω).
- Poles sit at Im = −δ/(2Ω).
- e_+ and 1/e_+ are both rational and outer.

The referee's plateau correction is reproduced: e(ε) ≈ 2ε and e(√ε) ≈ ½ (`vR11-5:15`).

**The full suppressed factor** is H_x = F·√2·Ĥ·e_+^{−1}·(…). The post-filter R = e_+·Ĥ^{−1} is causal.

### 3.3 Positive synthesis measures (proved; checked [1], [2])

**(i) R11-5's displayed profile admits no positive cone-centred Lorentzian measure.**
- In the baseband x = u², D′₀ ∝ f(x) = x^{−1/2}(x + ε)/(x + ε²).
- A positive superposition of cone-centred single-mode lines, ∫dμ(Γ)Γ/(Γ²/4 + u²), is exactly a Stieltjes function of x.
- f's Stieltjes density is (1/π)t^{−1/2}[1 + (ε − ε²)/(ε² − t)]. **This is negative on t ∈ (ε², ε)**: down to −1.3e5 at ε = 1e-2 (checked).
- A non-negative least-squares fit with 200 widths misses by 48%.
- So `C5_R11-5_report.md:170` ("a positive superposition of lines centred on ω = c|k|") is false for single-mode (Lorentzian) lines.
- Scope: this is proved for s₀ = 0 and Lorentzian lines. Lines with other shapes, such as the four-stage chain's ω^{−8} line, are not tested.

**(ii) The causal factor has a positive measure.** J₀(Ωτ) = ∫cos(ω′τ)dμ(ω′), with the arcsine measure dμ = dω′/(π√(Ω² − ω′²)) ≥ 0 on |ω′| < Ω (checked to 10 digits).
- So Ĥ is a positive superposition of **undamped** modes at frequencies inside the cone.
- That is legitimate only with a start time, because undamped elements have no stationary state with white-noise drive.
- **This is E1's price made concrete (P-r13a).**

**(iii) A Stieltjes member of the family exists** if a bank is preferred:
- D′₀ = (1/2|u|)[1 + (1/ε − 1)(2/π)arctan(b/|u|)], with measure ρ(t) = (1/π)t^{−1/2}[1 + (1/ε − 1)·1(t < b²)] ≥ 0 (checked: quadrature vs closed form 6e-4).
- It suppresses P_J by ε for |u| ≪ b (checked: 1.00e-4 at ε = 1e-4).
- Its transition is slower than e(s): Lorentzian wings reach out to |u| ~ b/ε.

### 3.4 The finite-start state and covariance (proved; checked [4], [5])

**Two levels of explicitness (stated before the formulas).**
- **The record side is exact and classical.** The homodyne output noise ñ of a stable single-port network in its vacuum or steady state is exactly white (S = ½) from t₀ on. Everything that turns it into h is a classical causal filter, G_R·R = Ĥ/√2: the J₀ kernel. So the metric-record covariance below is exact for any network whose gain is g = √2FĤ.
- **The quantum backaction side is explicit only for rational approximants.** A finite stable network with outer gain g_N → √2FĤ has a smallest pole Γ_min > 0, which acts as R11-5's s₀ ≈ Γ_min.
  - Choose Γ_min ≤ 1/t_H and start the network in its vacuum (its steady state) at t₀.
  - Its backaction is then stationary from t₀, with a bounded, locally finite spectrum.
  - Its record grows as ε·ln T on the whole domain t − t₀ ≤ t_H. Growth would turn linear only after T ≈ 1/Γ_min > t_H (checked [4], third row).
  - **So the explicit model is the approximant with a meter coherence time ≥ t_H.** This is R11-5's T_* ≥ t_H, now with every element written down.
  - The exact s₀ = 0 network (memory longer than any age) is the limit. Its quantum initial-state treatment is suggested only. In the arcsine (undamped-mode) realization of §3.3(ii), the initial vacuum adds a bounded term, because the measure has total mass J₀(0) = 1.

**State.** At t₀, the state is ρ_matter ⊗ |0⟩⟨0|_meter, with classical h(t₀) = ḣ(t₀) = 0. For t > t₀:
- the record is J(t) = ∫_{t₀}^t r(t − t′)I(t′)dt′, with r the kernel of R;
- the metric is h(t) = ∫_{t₀}^t G_R(t − t′)J(t′)dt′.

Because R, G_R and Ĥ are causal convolution operators and the inputs start at t₀, compositions on [t₀, ∞) obey the frequency-domain algebra exactly. So **h_noise(t) = ∫_{t₀}^t ĥ_h(t − t′)ξ(t′)dt′**, where:
- ĥ_h = J₀ for ε = 1;
- ĥ_h = the inverse transform of Ĥ·e_+ for ε < 1.

**Exact covariance:** C_h(t, t′) = ½∫_{t₀}^{min(t,t′)} ĥ_h(t − τ)ĥ_h(t′ − τ)dτ.

**Checks (ε = 1, per mode, in units of Ω).**
- Var h(T) = ½∫₀^T J₀² = 1.155374 / 1.522253 / 1.888685 / 2.255158 at T = 1e2 to 1e5. The asymptote (ln 8T + γ_E)/(2π) agrees to about 4e-4 at T = 1e2 and 6e-6 at T = 1e4.
- Var ḣ/Ω² grows with the same slope.
- **Finite at every age; logarithmic.**

**Matter side (checked [5]).**
- Take a matter transition exactly on the cone, driven by the finite-start backaction. P(T) = ½∫₀^T dt′|∫₀^{T−t′}J₀e^{iτ}dτ|² = **T²/(2π)** (0.1592·T² at T = 50, 200, 800). This is finite at every age. The stationary version is infinite.
- Off-cone transfers converge to the stationary golden-rule rate: P/T = 0.5513 → 0.5495 (subtraction: the stationary rate).
- The finite-start correction to off-cone lab kernels at age t_H is ≤ 1/(Ωt_H) (subtraction: the stationary kernel):
  - 7.7e-33 for k = 1/µm;
  - 1.1e-15 for k = 1/AU;
  - 2.4e-7 for k = 1/kpc.

### 3.5 Single port vs bank, and the exact map (proved; checked [3])

- **Single port.** Take a cascade of single-mode QND elements (one input and one output line). Then |gain| = |H_x| at every u, to 7e-16 (checked for three elements). So S_imp·S_FF = |gain|²/4 exactly (Lemma K with equality).
  - With g = H_x outer, R = F/g is causal.
  - The map is exact: D = |F|²D′₀, the record's T-referred imprecision is P_J, and K = |F|²(D′₀ + |G|²P_J), which is R11-5's kernel.
  - For an irrational target (Ĥ), use rational outer approximants realized as quantum-mechanics-free-subsystem (QMFS) networks (Tsang–Caves, comparator via `vR10-3:5`). On [t₀, t] these converge in L² of the impulse response, so the Gaussian covariances converge.
- **Parallel bank (independent ports).** Saturation needs R_i ∝ conj(g_i) pointwise. With causal R_i this forces the common factor to carry B(u) = Π(Γ_j/2 + iu)/(Γ_j/2 − iu).
  - B is an all-pass with group delay Σ4/Γ_j ≈ 16/Γ_min (checked: 1.6e4, 1.6e7, 1.6e10 for Γ_min = 1e-3, 1e-6, 1e-9).
  - For Γ_min ~ 1/t_H this is a Hubble-time record delay. So a bank is either unsaturated (R12-7's X ≤ 2.47 at `:84`) or acausal in effect.
  - **The single-port factor is strictly better on both counts** (reading).

### 3.6 Complete positivity at every finite age (proved)

Discretize [t₀, t] into steps dt. One step is the composition of five maps:
1. a unitary on matter ⊗ network ⊗ input-line segment;
2. a homodyne measurement of the commuting output quadrature (a Gaussian instrument, Kraus operators A_r with Σ A_r†A_r = 1);
3. a unitary exp(−i dt H_fb[r_{≤t}]) controlled by past records only. G_R(0) = 0, and R and F are causal, so no present record enters;
4. a partial trace;
5. initial appending of the vacuum at t₀.

Each map is CP and trace-preserving, so the composition is too. Pointwise limits of CP maps are CP, which covers dt → 0. CP is proved for every finite stable network, including all the approximants of Ĥ. For the s₀ = 0 limit, CP is proved only if the Gaussian covariances converge on [t₀, t]. That holds on the record side; on the backaction side it is suggested (§3.4).

This proof covers the whole finite-start 𝒦_ε process. It extends `vR11-5:8`, which confirmed the chain, to every single-port network.
- **Not covered:** the spin-2 conserved-noise assembly (§8).

---

## 4. Probe (b): record growth and its size at t_H

**Growth law (checked [4]).** E(T) = 2∫du P(u)sin²(uT/2)/u² near the cone (subtraction: none):

| Profile | E(T) for T = 1e4 … 1e14 (units 1/Ω) | dE/dln T |
|---|---|---|
| ε = 1, s₀ = 0 | 9.79, 14.4, 19.0, 23.6, 28.2, 32.8 | 1.00 at every decade |
| ε = 1e-4, s₀ = 0 | 4.607 (flat) | 1.00e-4 at every decade from 1e6 |
| ε = 1e-4, s₀ = 1e-10 | 4.61 … 6.18 | 1.0e-4 → 3.4e-3 → 0.34 |

**What this means for E1.** The referee's point (`vR11-5:6`) is that logarithmic growth belongs to the non-locally-finite limiting kernel. Two statements follow:
- **Ideal limit (s₀ = 0).** The start time alone regulates, and growth is ε·ln t forever, never linear. The record side of this limit is exact (§3.4). Its quantum backaction side is suggested.
- **Explicit finite network (s₀ ≈ Γ_min ≤ 1/t_H).** The growth is ε·ln t on the stated domain t − t₀ ≤ t_H, and would turn linear only beyond about 1/Γ_min. **The start time is what makes this a complete model.** A stationary version of the same network has infinite record covariance (Theorem U), because the record noise at the cone is finite while M ~ P/s².

**Size at t_H** (R11-5 normalization: O(1) tensor weights, Isaacson premise; suggested).
- ρ_GW(t_H) ≈ [ε·L_eff + (non-secular forced part ≈ ½ln(1/ε), premise (ii))]·ħc/(π³ℓ⁴), with L_eff = ln(εct_H/ℓ).
- ρ_GW < ρ_Λ (checked [6]A) needs:

| ℓ | ε needed | L_eff |
|---|---|---|
| 1e-8 m | 1.2e-16 | 42 |
| 2e-7 m | 1.6e-11 | 51 |
| 1e-6 m | 9.3e-9 | 56 |
| 5e-6 m | 5.4e-6 | 60 |

These agree with `vR11-5:15` to within the L definition. Corollary U_L's product then gives matter a 1/ε near-cone noise. E1 does not change this trade; it only fixes L.

**With a decoupled gain scale τ_c ≫ ℓ/c (repaired gain, n = 4, ε = 1; checked [6]B).** The near-cone record content is cut at k ~ 1/(cτ_c) by |F(cone)|², with no trade, because both sides of Corollary U_L carry |F|².

| cτ_c | ρ_GW(t_H), log variant | quasi-static TT (ω < 0.5c\|k\|, R11-5's weight), ℓ = 4e-10 / 1e-6 / 5e-6 m |
|---|---|---|
| 1e-4 m | 7.5 ρ_Λ | 1.4e4 / 5.6 / 1.0 ρ_Λ |
| 1e-2 m | 7.0e-8 ρ_Λ | 1.4e-2 / 5.7e-6 / 1.1e-6 ρ_Λ |

- The sum of both is below ρ_Λ for cτ_c > 1.7e-4 m at ℓ = 5e-6 m, and for cτ_c > 2.4e-3 m at ℓ = 4e-10 m.
- **This needs no ε, no f_cone and no A′.**
- Vacuum-photon injection is also cut: timelike transfers need ω > c|k| and ω < 1/τ_c (suggested).
- The chain-only variant (bounded D′₀, linear growth) needs cτ_c > 91 m (checked). That is excluded by §5.2's residual drag unless the gain is compensated to higher order (suggested).

---

## 5. Probe (c): the tests

### 5.1 R11-5's list plus the noise-fed term (repaired gain)

| Test | Result | Label |
|---|---|---|
| Cs-133 (1.9 µm, 70 s), LISA Pathfinder (LPF), corrected torsion | The static kernel equals R6-4's floor (F(0, k) = e^{−k²ℓ²/2}). At lab frequencies, \|F_t\|² − 1 ~ n(n−1)(ωτ)² ≤ 1e-20, and finite-start corrections are ≤ 1e-15. R6-4's margins of 9–22 decades carry over (`vR6-4:7`; `vR11-5:12`, conditional scope). | checked (inheritance) |
| Cassini | γ = 1 at linear static mean-field order. | proved, as `vR11-5:12` |
| GW170817 | c_T = c (G_R untouched; front speed c). The repaired gain has no first-order lag. At 1 kHz, \|F\| − 1 ≤ 2.4e-4 and arg F ≤ 5e-6 rad even at τ_c = 1e-6 s; at the τ_c window (≤ 8e-12 s) the corrections are below 1e-12. | checked [8] |
| PPN α₁, α₂ (linear) | F_c(k·w, k) → 1 as k → 0. With the first moment zero, there is no first-order frame displacement of the field centre. The even term is ~ (wτ/r)² ≲ 1e-41 at 1 AU. | proved / checked |
| **Noise-fed second order** | ⟨h²⟩ ≲ 2e-59 (quasi-static least-decoherence noise, ℓ ≥ 4e-10 m, cτ_c ≥ 1 cm). The frame-dependent part is β²⟨h²⟩ ≲ 4e-65, against α̂₂ < 1.6e-9. The Isaacson fluid at rest in the frame, with ρ ≤ ρ_Λ, gives ≤ 1e-33 at 1 AU. Order 2m in the noise scales as ⟨h²⟩^m. | suggested (power counting; normalization as R6-4 Lemma F) |
| Binary-pulsar orbital aberration (new) | §5.3. | checked |
| **Self-drag (new; Lemma D)** | §5.2. Literal gain: **FAIL at every ℓ**. Repaired strict family (τ = ℓ/c): Γ = 5.6e-29 s⁻¹ at ℓ = 5e-6 m, against 6.1e-21: pass. | proved + checked |

### 5.2 Lemma D: self-drag from the record's causal delay (proved at Newtonian mean-field order; no-go part, referee required)

**Setting.**
- Mean field h̄ = G_R·F·⟨T⟩, with a frame-tied causal gain F(ω, k) = g̃(k)F_t(ω). Write Im F_t(ω) = δω + c₃(ωτ)³ + c₅(ωτ)⁵ + …, where δ = ∫τf(τ)dτ is the first moment of the impulse response f.
- A body with density ρ (spherically symmetric) moves uniformly at v ≪ c through the frame.

**Statement.** The body feels a net self-force

  F_self = −4πG∫d³k/(2π)³ k Im F(k·v)|ρ̃(k)|²/k²
  = −(4πG/3)·δ·(∫ρ²d³x)·v − (4πG c₃τ³/5)|v|²(∫|∇ρ|²)v − ….

*Proof.*
- Φ_eff(k) = −4πG F(k·v, k)ρ̃(k)/k² for a source moving uniformly (ω = k·v).
- The self-force is F_i = −∫ρ∂_iΦ_eff. Only the part odd in k survives against |ρ̃|², and that is i·Im F.
- Expand Im F and use ⟨k_ik_j⟩ = δ_ijk²/3 and ⟨μ⁴⟩ = 1/5. ∎

**Plain reading.** The field is centred where the body was a time δ ago. The body is pulled back toward that point.

**Checks [10].**
- For a Gaussian body, the exact integral with F_t = (1 − iωτ)^{−3} reproduces the first-order formula: 2.2448e-5 vs 2.2448e-5.
- The repaired n = 4 gain reduces the drag by 6(vτ/a)².

**Consequences for the literal gain** (δ = nτ = 3ℓ/c):
- Neutron star (n = 1 polytrope, 1.3 M_☉, R = 12 km): (4πG/3)∫ρ²/M = 1.64e8 s⁻². Γ = 1.64e8·δ: at ℓ = 4e-10 m, Γ = 4e-10 to 7e-10 s⁻¹ (uniform sphere to polytrope), an e-fold in about 50–80 years (checked [10], [11]).
- **Double pulsar J0737−3039A/B.**
  - The drag on orbital velocities dissipates orbital energy at −2ΓK, so Ṗ_b/P_b = −3Γ (circular orbit; the CM velocity drops out because Σm_iu_i = 0).
  - Ṗ_b agrees with GR to 1.3e-4 (95%; comparator, web-checked by R12-7, `C5_R12-7_report.md:129`). So Γ < 6.1e-21 s⁻¹, δ < 3.7e-29 s (polytrope) or 6.2e-29 s (uniform), and ℓ < 4e-21 m.
  - The literal class has ℓ ≥ 4e-10 m. **Every ℓ_s is excluded, by factors of about 1e11 to 1e15.**
- Earth at ℓ = 5e-6 m: Γ = 7.7e-20 s⁻¹, a 3% loss of CMB-frame velocity over t_H. That is also large against Solar-System ephemeris secular bounds (RECALLED, not used for the verdict).

**Scope ("every").**
- It holds for every member of the literal 𝒦_ε: any n ≥ 3 and τ = ℓ/c > 0, because δ = nτ > 0.
- More generally, it holds for **any frame-tied causal gain whose impulse response, in frame time, has a positive first moment**. That covers every non-negative causal temporal smearing in the frame.
- **It does not cover Lorentz-invariant gains F(s).** A uniformly moving body has spacelike transfers (ω = k·v, |ω| < c|k|). There a retarded F(s) such as R8-3's 1/(1 − ℓ²□)_ret is real, so Im F = 0 and there is no drag, as relativity requires. Those gains fail elsewhere (R8-3 Lemma 1, `vR8-3:5`).
- It does not depend on the noise, on ε, or on the regulator (start time or friction).
- Hypotheses: Newtonian mean field, uniform (or quasi-static orbital) motion, symmetric bodies, v ≪ c.

**Unavoidable but suppressible (proved).**
- Kramers–Kronig: a causal F that is real on the real axis must be constant. So Im F ≢ 0, and some drag always remains.
- Odd moments can be zeroed one at a time with signed impulse responses (checked [11]):
  - P(z) = 1 + 4z with n = 4 gives Im F = 20x³ − 84x⁵ + …;
  - P(z) = 1 + 5z + 8z² with n = 5 gives Im F = 56x⁵ + …. Then |F|² ≤ 2.83, with high-ω slope −6, so the UV test still holds.
- **Residual drag with the first moment zero:**
  - strict τ = ℓ/c: Γ = 5.6e-29 s⁻¹ at ℓ = 5e-6 m, far below the 6.1e-21 s⁻¹ bound;
  - τ_c variant: the double pulsar needs τ_c < 7.9e-12 s (cτ_c < 2.4e-3 m) at v = 300 km/s for the smooth polytrope.
- With the first and third moments zero, the interior estimate allows cτ_c up to about 10 m. But the polytrope's surface kink makes the Taylor coefficient diverge, so the real bound is set by surface structure at scale vτ ≈ 1 cm (suggested only).

### 5.3 Orbital aberration (Laplace type; checked [7])

The same delay makes star 2 fall toward star 1's position a time δ earlier. That gives dE/dt = +(4μ/M)Ω²δ|E|.
- Double pulsar: δ < 2.4e-14 s, so ℓ < 2.4e-6 m for the literal gain.
- Hulse–Taylor: δ < 1.8e-12 s.
- This effect is subdominant to Lemma D for neutron stars, by (4πGρ/3)/Ω² ~ 3e14. It is the only effect for point-like orbiting bodies.
- The repaired gain removes it at first order. The residual τ_c bound is < 1.3e-3 s.

---

## 6. Probe (d): the ℓ_s interval

| Class | Interval | Basis |
|---|---|---|
| Literal 𝒦_ε (F_u, τ = ℓ/c, n ≥ 3), with E1 or any regulator | **none** | Lemma D + double pulsar (referee required) |
| Repaired, strict τ = ℓ/c (n = 4, first moment zero), stated list only | 4e-10 to 5e-6 m | R6-4's conservative window (`vR6-4:7`); §5.1 |
| Repaired, strict, with the record budget | conditional search interval of about 4e-7 to 5e-6 m (premise (ii)); about 4e-8 to 5e-6 m (premise (i)) | `vR11-5:12,15`. E1 only fixes L_eff = 42–60. Needs A′, f_cone and the Isaacson premise. |
| Repaired, τ_c variant (ε = 1, n = 4) | ℓ ∈ (≈4.3e-10, 5e-6] m with cτ_c ∈ [≈1.7e-4 m (larger at small ℓ: 2.4e-3 at 4e-10), 2.4e-3 m] | budget [6]B (O(1) tensor weights, Isaacson, suggested); drag [11] (smooth-polytrope neutron star, suggested). The window is a factor of about 12–14 in τ_c at ℓ ≳ 1e-8 m and closes near ℓ ≈ 4.3e-10 m. Higher-order compensation would widen it (suggested). |

**Reading.** In every repaired variant the upper end is R6-4's inherited 5e-6 m. The literal F_u had an extra orbital-aberration cap of 2.4e-6 m, which the repair removes.

## 7. Probe (e): prices (named, not adopted)

- **P-r11a, a start time** (finite frame age t₀).
  - It is a temporal boundary, not a privileged site (`AX:40`; `vR12-4:15`).
  - The open gate `AX:185` ("arrow, record-production dynamics, … time metric") gains a time origin, at which every meter starts in its vacuum.
- **P-r13a (new), a half-retarded meter channel per frame mode.** Its backaction transfer is (Ω² − (ω+i0)²)^{−1/2}, a J₀ impulse response.
  - Equivalently, it is a positive arcsine superposition of **undamped** meter modes inside the cone.
  - It has no stationary state with locally finite noise. It exists only because of P-r11a, and it carries a memory as long as the age.
  - It replaces R11-5's argued "bank" (P-r9b′'s realization) and its T_* ≥ t_H.
- **P-r13b (new; forced by Lemma D for every frame-tied causal gain).** The record gain's impulse response must have a vanishing first moment.
  - So it must be signed: the classical filter extrapolates the source.
  - It needs n ≥ 4 (or ≥ 5 for the third-moment version) to keep the UV test.
  - The drag is suppressed but never zero (Kramers–Kronig).
  - *Axiom text:* nothing in `AX` supplies a filter. This is content of the record-production law (`AX:185`).
- **P-r13c (optional), a gain time scale τ_c ≈ 0.6–8 ps**, decoupled from ℓ/c. It removes P-r9b′ (ε) and the near-cone heating, and cuts vacuum photons. Its upper end is set by the residual neutron-star drag.
- **Carried over:**
  - P-r1 (a preferred frame, in the meter and in the gain);
  - P-r11b (driven meters; an energy input to record production, `AX:185`; Lemma Q, `vR10-3:5`);
  - P-r3 (R6-4's P-i1 to P-i5, including conditional H-cosmo);
  - P-r4 (vacuum photons);
  - P-r9b′ (ε suppression), in the strict variant only;
  - R6-4 (iii)'s Qubit, Admissibility and Record prices (`vR6-4:19`).
- **Record** (`AX:77-80`) is unaffected. Records form from t₀ on and are permanent. The metric is a linear functional of the records since t₀.

## 8. E1 versus E2 on equal terms (for the owner's question 1)

| | **E1** (this report) | **E2** (R12-7, worker, unrefereed) |
|---|---|---|
| Regulator | a start time t₀; G_R untouched | friction γ on h̄ (E2-h); stationary except the sink energy (`C5_R12-7_report.md:108`) |
| Meter | single port, exactly saturated; Ĥ = G_R^{1/2} (J₀) or rational outer approximants | parallel bank, X ∈ [1, 2.47] (`:84`) |
| Memory | J₀ tail: as long as the age (P-r13a) | linewidths down to γ ~ H₀ (`:91`) |
| Extra sector | none beyond driven meters | a noiseless T = 0 outgoing-only classical sink that gravitates, with frame recoil (`:151`) |
| Near-cone budget | the same ε trade under τ = ℓ/c; L_eff = 42–60 | the same, plus the sink (γ/3H)ρ_GW (`:37`) |
| **Self-drag from the gain (Lemma D)** | literal F_u fails; repaired by P-r13b | **the same F_u is carried (`:153`): fails the same way, and needs the same repair** |
| Self-drag from the regulator | none (G_R untouched) | E2-h drags at 2γ\|U\|/(3Mc²) (`:145`): neutron star 2.2e-19 s⁻¹ at γ = H₀. That entry calls the effect "common-mode" for binaries. But the drag acts on each star's orbital velocity, so Ṗ_b/P_b = −3Γ = −6.6e-19 s⁻¹, against 1.8e-20. **This suggests γ ≲ 0.03H₀** (suggested; R12-7's formula, my orbital mapping). |
| Stated tests | pass after the repair | pass (worker) |
| Reading | OPEN (repaired); literal EXCLUDED | OPEN (worker) |

**Reading.** The start time costs nothing observable. Its price is a beginning (P-r11a) and an age-long meter memory (P-r13a). E2 trades the beginning for a sink, frame recoil and its own frame drag. Both need P-r13b.

## 9. Strong words checked

- **"Exactly saturated"** is the single-port network at second order in the coupling. The irrational Ĥ is reached as a limit of rational approximants on finite intervals.
- **"Every ℓ_s" (Lemma D)** holds within the literal 𝒦_ε, where δ = nℓ/c > 0. The double-pulsar input is a comparator via R12-7's web check (1.3e-4 at 95%). The bound is robust: the violation is ×1e11 even at ℓ = 4e-10 m. It is a **no-go: referee required**.
- **"Never linear"** holds for s₀ = 0 (checked to T = 1e14/Ω).
- **"Passes"** for noise-fed PPN is power counting with R6-4's normalization (suggested).
- The **τ_c window** depends on O(1) tensor weights, the Isaacson premise, and a smooth neutron-star profile at scale vτ ~ µm–cm (suggested).
- **"No positive measure"** applies to R11-5's profile with cone-centred Lorentzian lines and s₀ = 0.
- **Not built:**
  - the spin-2 channel with conserved noise (∂·ξ = 0). A double-curl potential is the obvious route (suggested). This is the same gap as R12-7's (`:93`);
  - a physical simulation of the QMFS approximants.
- **"EXCLUDED"** and **"OPEN"** are worker readings.

## 10. What would decide it

1. **A referee of Lemma D**, especially whether R11-5's F_u, as R8-3 and R11-5 wrote it, is "the class" or only one member of it. Also check the orbital mapping Ṗ_b/P_b = −3Γ, and the same mapping for R12-7's E2-h drag.
2. **Accept or reject P-r13b** (zero-first-moment gain) as within 𝒦_ε. If accepted, E1 is OPEN, with probe (a) complete for the scalar channel.
3. **Build the spin-2 conserved-noise assembly**, then recompute the O(1) tensor weights of the budget.
4. **A neutron-star drag calculation** with a realistic crust and envelope profile and the third-moment-compensated gain. This fixes the τ_c window's upper end.
5. As in R11-5: A′, f_cone and the gravitating status of near-cone TT noise. This applies only to the strict τ = ℓ/c variant.

**Sources.**
- Via earlier referees: double pulsar 1.3e-4 (arXiv:2112.06795, R12-7); α₁, α₂ (`vR11-5:12`); Cassini; GW170817; Tsang–Caves QMFS (`vR10-3:5`).
- RECALLED:
  - Laplace (1805) aberration argument;
  - Paley–Wiener–Schwartz; Kramers–Kronig;
  - ∫₀^∞J₀(t)e^{−pt}dt = (1 + p²)^{−1/2} (checked numerically here);
  - neutron-star mass and radius (1.3 M_☉, 12 km);
  - ρ_crit, ρ_Λ and t_H, as R11-5.
