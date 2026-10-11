# Lane RZ, probe Z2: noise spectrum with a carrier source, finite-τ normalization, and the physical translation (worker report)

**Worker:** Claude Opus 5.5 (probe Z2), the same model family as the exercise authors. **Unrefereed.** Worked 21:39–22:05Z on 2026-10-11. OMP_NUM_THREADS=2; every run under 8 minutes. No repository file was edited.

**Read in full:** TESTS.md lines 1–12; "Lane RZ" (fixed readings, expectation); "C4 result recorded 21:28Z (Y1)"; "C4 result recorded 21:01Z (RL4)"; "C4 sixth wave / RL2"; "C4 ninth wave / RL3"; "C4 results recorded 19:41Z and 20:23Z". `C4_Y1_report.md` and `C4_Y1_referee.md`; `C4_RL2_report.md`; `C4_RL4_referee.md`. Scripts `rl2_core.py`, `rl2_B_smeared_mc.py`, `rl2_C_ladder_rates.py`, `RL1_B_bd_mean_volterra.py` (solver), `rl3b_B_h_and_roots.out`. **Read in part:** `C4_RL3b_report.md` (lines 1–140); `C4_RL4_report.md` (lines 120–244).

**Labels:**
- **PROVED:** complete argument here, or in a refereed RL file (scope stated).
- **DERIVED:** leading-order asymptotics of an exact formula, with the uniform bound ARGUED.
- **CHECKED:** my numerics, with the scripts below.
- **ARGUED:** a standard step, not written out.
- **SUGGESTED:** a heuristic.

## Verdict (worker)

**The noise is not multiplicative on the carrier. It is broadband. Its in-band fraction is small only by a power law, about e^{−106} (optical) to e^{−131} (VLBI channel), not exponentially. Against the proved e-fold budget, that leaves lensed light noise-dominated by at least 4.4×10⁴ e-folds. Reading: FAIL (controlled, not proved).**

| item | status | result |
|---|---|---|
| Is the noise multiplicative on the carrier? | **CHECKED** (MC: ε = 1, ½, ¼, ⅛; ω₀ = 0, 0.1, 0.3, 1, 2, 4 /ℓ_k). Within the node ladder, **PROVED** structure | **No.** The normalized two-time correlation \|ρ(δ)\| falls to ≤ 0.15 by δ = 0.2 ℓ_k at every ε and every ω₀. Its phase does not follow the carrier: arg ρ/(−ω₀δ) is erratic, from −0.7 to ≫ 1, never ≈ 1 over a range of δ. Of the noise power, 38–47% lies at \|ω\| > 10/ℓ_k and only 4–7% at \|ω\| < 1/ℓ_k. In the node ladder, the observer's time enters only through the top rung, so the spectral shape does not depend on the carrier. |
| Low-frequency PSD | **DERIVED** (node ladder, exact formula at each ε); **CHECKED** (z2_B; MC) | S(ω)/V is nonzero and flat for ω ≪ 1/ℓ_k. Small-ε law: **S(0)/V = κ√ε ℓ_k**, κ = πW²/k_h = 0.054–0.067 (op0–op2; W = ∫h dσ). The exact node-ladder value tends to the law: ratio 0.98–1.10 at ε = 10⁻⁴. The MC at ε ≥ ⅛ gives S(ω₀)/V = 0.13–0.28 ℓ_k, which is 2–5× **above** the node-ladder value. It does not depend on τ within errors, and it changes by at most a factor 1.4 over ω₀ ≤ 4/ℓ_k. |
| In-band fraction (real field, band ω₀ ± Δω) | DERIVED; physical numbers CHECKED | **f = 2Δk (S/V)/π = 2κ Δk √ε ℓ_k/π.** At ℓ_k = 7.9e-20 m: optical V band 1.2e-46 (e^{−106}); 1 nm filter e^{−110}; radio 1 GHz with 100 MHz band e^{−119}; 1 MHz channel e^{−124}; 1 kHz channel e^{−131}. |
| Finite-τ normalization | **CHECKED** | Fixing p = −3/2 (the finite-target LCLT form), the fit V = A τ^{p} e^{γτ} gives γ = 4.87, 2.95, 1.75, 1.10. The exact ladder root (node plus same-hop variance, RL3b) is 4.98, 2.94, 1.72, 1.05: agreement within 2–5%. ln A = −3.20, −3.63, −3.51, −3.57 at ε = 1 … ⅛, ε-independent within ±0.3. The carrier lowers ln A by at most 1.3 (at ω₀ = 4/ℓ_k, ε = ⅛) and leaves γ unchanged. |
| Physical: lensed quasar or radio source, D = 1–5 Gpc | CHECKED arithmetic; polynomial budget ARGUED | Pay ln f, the τ^{−3/2} factor and a 1000-e-fold allowance for the remaining polynomial prefactors. Then ln(N_in/S) ≥ **4.4×10⁴** (optical or radio) for emission only 1 s before the retarded time at 1 Gpc; 2.7×10⁶ for 1 h; 2.5×10⁸–5.7×10⁸ for 1 yr. The threshold emission depth is Δt* ≈ 6 μs (no allowance) to 0.6 ms (1000 e-folds) at 1 Gpc. |
| Physical: 1 h lab lamp at 1 m | CHECKED / SUGGESTED | γτ = 0.36 (proved rate) or 1.56 (derived), so the growth regime is not reached. In-band relative noise ≲ e^{−100}: **no observable effect**. The threshold for a source at 1 m is 12 days (no allowance) to 130 days (1000 e-folds) of continuous emission. |

**Reading against the FIXED RZ readings: FAIL (controlled, not proved).** Bounded to:
- RL4 T′: edged emission events;
- Y1's phase average, referee-confirmed;
- the stable scalar layer readout;
- a photon ℓ_k ≤ 7.9e-20 m, shared with matter (X1).

**What would make it INCONCLUSIVE.** The in-band fraction is a DERIVED leading-order value, CHECKED numerically, not a proved lower bound. The missing step is a Fourier version of RL4's Lemma U′ for the top rung (Lemma F, §6). If the referee requires Lemma F to be proved, the reading is **INCONCLUSIVE, leaning FAIL by ≥ 4.4×10⁴ e-folds.** Nothing found here points toward PASS: PASS needs suppression by more than about 4.5×10⁴ e-folds, and the fraction costs only 106–131.

**Against the supervisor's expectation.**
- Expected: "multiplicative on the carrier, in-band fraction O(1)." **The mechanism is wrong.**
  - Each node's contribution reaches the observer as a pulse of duration about ℓ_k²/r (r = distance along the observer's past cone). The noise is therefore a white multiplier on the carrier, with bandwidth about 1/(κ√ε ℓ_k).
  - So the in-band fraction is power-law small: about 2κΔk√ε ℓ_k/π.
- The expected **reading (FAIL) still follows**, because the exponent budget (≥ 4.5×10⁴) exceeds the fraction's cost (≤ 131) by a factor of more than 300.

**Plain summary.**
- **The noise is fast flicker, not a slow wobble of the carrier.** The extra noise on the light is made of extremely short blips, each lasting about the time light takes to cross a Planck-scale-squared-over-ℓ_k distance. It is not a slow random change of the wave's brightness and phase.
- **A narrow-band detector sees only a sliver of it.** Optical or radio detectors catch a fraction of about e^{−106} to e^{−131} of that flicker.
- **The sliver is still far too big.** The flicker's total power grows by about 45,000 e-folds even when the light was emitted only one second before the light we see, at 1 Gpc. After paying for the narrow band and every other plausible prefactor, the in-band noise still exceeds the signal by at least e^{44,000}.
- **A lab lamp that has been on for an hour is fine.** Its growth has not started (0.36 e-folds). Trouble would begin only for sources running continuously for weeks to months.

## 1. Setting

- Units ℓ_k = 1, ρ = 1/ε, N(x,y) = ε g_ε(n(y,x)) with exact binomial thinning (RL2_B). The mean operator is ε-independent. Operator op0 throughout the MC; op0–op2 in the ladder calculations.
- **Carrier source with a past edge:** J(y) = w(y⃗) e^{iω₀t_y} Θ(t_y). Here w is a Gaussian (σ = 0.4) centred at x⃗_s = (2,0,0) and truncated at R₀ = 1.2, so ∫w ≈ 1.
  - The cos and sin columns are solved together, giving φ = φ_c + iφ_s.
  - |J| = w is continuous and nonzero at the edge, so this J is in RL4's T′ class (whose hypotheses involve only |J|).
- **Sprinkling region:** Ω = J⁺(supp J) ∩ J⁻(x_T). This is exact for the observable, because every interval between points of Ω lies in Ω.
- **Observer worldline:** x⃗ = 0, times t_k on a grid of step 0.025 from 1 to T. Each observer is its own Palm point, not added to the sprinkling:
  φ(x_k) = Σ_z N(x_k,z) u(z), with u = (I − N)⁻¹J on the sprinkled points.
- **Runs** (`z2_A`, 470 s each):

| ε | T | ⟨n⟩ | realizations R |
|---|---|---|---|
| 1 | 10 | 1929 | 3139 |
| ½ | 9 | 2615 | 1637 |
| ¼ | 8 | 3398 | 960 |
| ⅛ | 7 | 4173 | 594 |

- **Envelope.** The noise grows as e^{γt}. All spectral quantities therefore use the envelope-normalized process η(t)/√V(t): ρ(t,t+δ) = C(t,t+δ)/√(V V′), and S(ω)/V = 2 Re∫₀^∞ ρ(δ)e^{iωδ}dδ. This is the white-level-to-variance ratio. For a complex carrier the in-band fraction is f = Δω S/(πV); for a real field it is f = 2Δω S/(πV).

## 2. MC results (CHECKED; `z2_C_analyse.out`, `z2_E_tau_dependence.out`)

### 2.1 Spectral weight at the carrier

The late window is the last 2 ℓ_k. The bootstrap sd uses 30 resamples.

| ε | S(0)/V | S(ω₀=1)/V | S(ω₀=4)/V | early-window S(0)/V | node ladder S_n(0)/V (z2_B) | MC/node |
|---|---|---|---|---|---|---|
| 1 | 0.216 ± 0.023 | 0.217 ± 0.026 | 0.188 ± 0.013 | 0.211 ± 0.027 | 0.099 | 2.2 |
| ½ | 0.276 ± 0.017 | 0.257 ± 0.011 | 0.189 ± 0.009 | 0.264 ± 0.011 | 0.069 | 4.0 |
| ¼ | 0.218 ± 0.011 | 0.213 ± 0.011 | 0.155 ± 0.007 | 0.221 ± 0.011 | 0.047 | 4.6 |
| ⅛ | 0.156 ± 0.009 | 0.167 ± 0.009 | 0.128 ± 0.009 | 0.143 ± 0.009 | 0.032 | 4.9 |

- **No dependence on τ.** Early (τ ≈ 3.5–6.7) and late (τ ≈ 5.7–8.8) windows agree within errors.
- **Weak dependence on the carrier.** S(ω₀)/S(0) = 0.6–1.0 for ω₀ ≤ 4/ℓ_k.
- **Falls toward the √ε law at small ε.** Between ¼ and ⅛ the ratio is 0.72; √½ = 0.71.
- **Discretization.** The unresolved part at δ < dt is ρ(0.025) ≈ 0.80–0.88, so the trapezoid error on S/V is ≤ 0.004.

**In-band fraction at accessible ε** (complex carrier, one band of half-width Δω, f = ΔωS/(πV)):
- Δω = 0.05: f = 2–4×10⁻³.
- Δω = 0.1: f = 4–9×10⁻³.
- Δω = 0.3: f = 1.2–2.6×10⁻².

**Periodogram on a 3.5–4 ℓ_k window (resolution 1.6–1.8), fraction of power:**
- within |ω − ω₀| < 1: 0.04–0.10;
- at |ω| < 1: 0.04–0.07;
- at |ω| > 10: 0.38–0.47;
- at |ω| > 20: 0.14–0.26.

The noise power at −ω₀ (the mirror band) is as large as at +ω₀ (0.04–0.10). The noise does not know which side the carrier is on.

### 2.2 Correlation shape

**Re ρ(δ) in the late window (ε = ⅛):**

| δ | 0.05 | 0.1 | 0.2 | 0.3 | 0.5 | 0.75 | 1.0 |
|---|---|---|---|---|---|---|---|
| MC | 0.73 | 0.45 | −0.01 | −0.18 | −0.01 | 0.06 | 0.01 |
| node ladder | 0.62 | 0.15 | −0.23 | −0.19 | −0.01 | 0.02 | −0.005 |

- At ε = 1 there is no dip: 0.39 at δ = 0.1, 0.15 at 0.2, 0.07 at 0.3.
- So the MC shape moves toward the node-ladder shape as ε falls. The anticorrelation dip near δ ≈ 0.3 is reproduced at ε = ⅛.

**Carrier tracking.** With multiplicative noise on a slow multiplier, ρ would be ≈ e^{−iω₀δ}·(slow decay), with |ρ| ≈ 1 out to δ ~ 1/ω₀. Instead |ρ| < 0.06 at δ ≥ 0.3 for every ω₀, and arg ρ does not follow −ω₀δ.

### 2.3 Finite-τ fits of V(τ), with τ = √(t² − d²)

The window is the late part of the series: τ from about 3–6 up to 6.7–9.8.

| ε | γ (p = 0) | ln A (p = 0) | γ (p = −3/2) | ln A (p = −3/2) | free p | exact roots: node / node + hop-var / k_h√ε (RL3b) | RL2 MC (2 × sd rate) |
|---|---|---|---|---|---|---|---|
| 1 | 4.67 ± 0.04 | −4.73 | **4.87** | −3.20 | 5.5 (ill-conditioned) | 1.62 / **4.98** / 2.73 | 4.07 / 3.86 |
| ½ | 2.72 ± 0.02 | −4.93 | **2.95** | −3.63 | −1.4 | 1.27 / **2.94** / 1.93 | 2.59 / 2.69 |
| ¼ | 1.47 ± 0.01 | −4.52 | **1.75** | −3.51 | −1.2 | 0.98 / **1.72** / 1.37 | 1.37 / 1.18 |
| ⅛ | 0.78 ± 0.01 | −4.34 | **1.10** | −3.57 | +0.5 | 0.75 / **1.05** / 0.97 | 0.81 / 0.85 |

- **Fixed p = −3/2 (RL4's finite-target LCLT form).** The rate matches the exact ladder root including the same-hop count variance to 2–5% at all four ε.
- **Pure exponential (p = 0, Blackwell's planar-edge form).** Rates are 6–26% low.
- **Free p.** Ill-conditioned over windows of 4 ℓ_k: p ranges from −1.9 to +5.5 across ω₀ and ε.
- **Carrier at ε = ⅛** (p = −3/2):

| ω₀ | 0 | 1 | 2 | 4 |
|---|---|---|---|---|
| γ | 1.10 | 1.09 | 1.09 | 1.11 |
| ln A | −3.57 | −3.68 | −4.03 | −4.84 |

  The carrier changes only the prefactor. This matches RL4 T′, whose lower bound sees only |J(z_k)| on the turn-on patch, so it does not depend on ω₀ for a complex carrier (PROVED there).
- **Relative variance at accessible ε.** Only ε = ⅛ resolves the mean: |Ψ| = 0.062 (median |mean|/sem = 2.0–2.4). There, V/|Ψ|² ≈ 1.4×10² (late median), and V/|Ψ|² ≈ e^{2.0}·τ^{−3/2}·e^{1.10τ}.

**Normalization law at accessible ε (CHECKED for this source):**

  **V(τ) ≈ A τ^{−3/2} e^{γ_root(ε) τ}, with ln A = −3.5 ± 0.3 for ε ∈ [⅛, 1]**

The source has unit charge, size 0.4 ℓ_k and distance 2 ℓ_k.

## 3. Why the noise is white at the carrier (node ladder; `z2_B`)

### 3.1 Structure (PROVED within the node ladder)

**The top rung is the only place the observer's time enters.** The k-th chaos amplitude of φ(x) at leading order is εᵏ h(x−z₁) h(z₁−z₂)⋯Ψ(z_k), with every factor ≥ 0 after squaring (RL3b Theorem 1, RL4). The observer's time t enters only through the top factor h(x_t − z₁). So for the envelope-normalized process (planar edge, renewal M(z) ∝ e^{γ t_z}):

  **S_n(ω) = ε ∫ 4πr² dr |ĥ_r(γ/2 − iω)|²,  ĥ_r(q) = ∫₀^∞ τ dτ h(τ) e^{−q√(τ²+r²)}/√(τ²+r²).**

- Its integral ∫ S_n dω/2π equals Λ_node(γ) = 1 at the root. Numerically this is 0.989–0.991 up to ω ≤ 200 (CHECKED).
- The carrier enters only through the bottom-end weight |Ψ(z_k)|². So the spectral shape is carrier-independent, and the noise cannot be concentrated at ω₀.

### 3.2 Flatness at low frequency (DERIVED)

**Far field.** For r ≫ ℓ_k, ĥ_r(q) → e^{−qr} W/(2r), where W = ∫h dσ = 1/(2πc₂) by the 4D symbol. So |ĥ_r|² = e^{−γr}W²/(4r²) **does not depend on ω**.
- This is on-shell, Lorentz-invariant propagation: the pulse from a node at distance r lasts about ℓ_k²/r, but its area is exactly W/(2r).
- Frequency dependence enters only from the near zone (r ~ ℓ_k), on the scale ω ~ 1/ℓ_k.

**Small-ε law.** The far field dominates (r ~ 1/γ ≫ ℓ_k), giving

  **S(0)/V → επW²/γ = (πW²/k_h)√ε ℓ_k.**

**Frame independence (PROVED, elementary).** For an observer moving with rapidity β relative to the rest frame of (x − y_edge), the zero-frequency weight is

  ε∫dΩ ∫ e^{−γr}W²/(4r²D(θ)²) r² dr/(4π)·… ∝ ∫dΩ/D(θ)² = 4π,

with D(θ) = cosh β − sinh β cos θ. So S(0)/V is the same in every frame. The Y1 beaming (γ_b = √(D/2s)) changes only where the flat range ends. For the forward nodes it pushes that end to lower ω, by e^{β}.

### 3.3 Numbers (CHECKED; `z2_B_ladder_spectrum.out`)

**op0, node root γ and S_n(0)/V:**

| ε | node root γ | S_n(0)/V |
|---|---|---|
| 1 | 1.623 | 0.0988 |
| ½ | 1.267 | 0.0692 |
| ¼ | 0.979 | 0.0474 |
| ⅛ | 0.748 | 0.0320 |

**Spectrum shape.** S_n(ω)/S_n(0) at ω = 0.5, 1, 2, 4, 8 is 1.03, 1.10, 1.32, 2.2, 5.3 (ε = ⅛). The spectrum is flat at low ω and rises toward 1/ℓ_k: the power sits at high frequency. The low-frequency fraction F(|ω| < 1) is 1.1–3.3%.

**Approach to the law, S_n(0)/(V√ε):**

| operator | ε = 10⁻² | ε = 10⁻³ | ε = 10⁻⁴ | law (Volterra W) | ratio at ε = 10⁻⁴ |
|---|---|---|---|---|---|
| op0 | 0.0741 | 0.0673 | 0.0665 | 0.0675 | 0.985 |
| op1 | — | — | 0.0615 | — | 1.05 |
| op2 | — | — | 0.0541 | — | 1.10, still converging |

- **W.** Two values of W exist: the Volterra grid gives 0.2419 (op0), the 4D symbol gives 0.2299 (op0). Across op0–op2 and both W choices, κ = 0.054–0.067. Its effect on ln f is under 0.2.
- **MC versus node ladder.** At accessible ε the MC's S/V is 2–5× the node-ladder value. The extra terms (same-hop count variance and interior insertions, which dominate the rate there; RL3b's "node + hopvar" root) add low-frequency weight rather than cancelling it. The ratio grows from 2.2 to 4.9 as ε falls from 1 to ⅛, with no trend toward cancellation.

## 4. Finite-distance normalization: what is measured, what is proved, what is extrapolated

**Proved (RL4, refereed, fixed physical ε, no ε-extrapolation).** lim inf τ⁻¹ ln V ≥ c_low√ε/ℓ_k, with c_low = 0.628. The LCLT gives L(T) ≥ c(ε) T^{−3/2} e^{z*T} with c(ε) > 0.

**Is physical τ asymptotic?** The relevant expansion parameter is the number of renewals, γτ:
- physical cases: 4.5×10⁴ (1 s at 1 Gpc) to 5.7×10⁸ (1 yr at 5 Gpc);
- LCLT relative corrections: O((γτ)^{−1/2}) ≤ 0.5%.

So the physical point is deep in the asymptotic regime of the proved theorem. That is not an extrapolation in ε.

**Measured at accessible ε (CHECKED, §2.3).**
- The τ^{−3/2} form with γ = the exact root fits to 2–5%.
- ln A = −3.5 ± 0.3, flat over ε ∈ [⅛, 1].
- The carrier moves ln A by at most 1.3.

**Not measured; this would be a long extrapolation, which I do not do.** The prefactor c(ε) at ε = 1.75×10⁻⁶³, and its dependence on the emitter's geometry.

**What I do instead (ARGUED): bound its log.** Every ingredient is polynomial:
- the chaos weights εᵏ, which are absorbed in the root;
- the LCLT density, ∝ z^{5/2}(zT)^{−3/2}, which gives ≈ −181 for the z^{5/2} part at physical ε;
- the per-emitter incoherent-cell factor ℓ_k³/v: −63 for an atom, −132 for a 1 m³ antenna;
- D²/ℓ_k² from the 1/D² mean: +202 at 1 Gpc;
- the angular acceptance of the imaging beam within the 1/γ_b noise cone: ≈ −5 to −20;
- the emission-history integral (N sums over all emitters in J⁻(x), S only over the on-cone ones; Y1 §2.3): +ln(T/(t_coh γτ)) > 0.

**Allowance.** I allow B = 1000 e-folds for all of these together. Only −1.5 ln(τ/ℓ_k) = −125 to −139 is taken explicitly.

**The finite-distance law used:**

  **ln(N_in/S) ≥ c_low√ε τ/ℓ_k − 1.5 ln(τ/ℓ_k) + ln f(Δk) − B,  τ = √(2D·cΔt + (cΔt)²),  f = 2κΔk√ε ℓ_k/π.**

**What is extrapolated:** only B. It would take B ≳ 4.4×10⁴ to change the 1 s case, and B ≳ 2.5×10⁸ to change the 1 yr case.

**First chaos alone (pure shot noise of the mean wave; SUGGESTED, closed form).** The in-band relative variance is

  ΔkεW²π²D/2 (ℓ_k units), using ∫d³z/(z²|z−s|²) = π³/|s|.

That is 4.5×10⁻⁵⁸ for the lab at 1 m and 1.4×10⁻³² at 1 Gpc. It is negligible everywhere. Only the renewal growth matters.

## 5. Physical translation (ℓ_k = 7.9e-20 m; CHECKED arithmetic in `z2_D_translate.out`)

**Base quantities.**
- ε = 1.75×10⁻⁶³, √ε/ℓ_k = 5.30×10⁻¹³ m⁻¹.
- γ = 3.33×10⁻¹³ m⁻¹ (proved, c_low) or 1.45×10⁻¹² m⁻¹ (derived, k_h).
- S(0)/V = 2.0–2.2×10⁻⁵² m = 7×10⁻⁶¹ s. The noise bandwidth is about 1/(κ√ε ℓ_k), i.e. about 10⁵¹ m⁻¹, far above the Planck frequency (flag 4).

| case | γτ (proved / derived) | ln f (optical V / radio 100 MHz) | ln(N_in/S) ≥ (B = 1000) |
|---|---|---|---|
| lensed source, 1 Gpc, emission 1 s before the retarded time | 4.53e4 / 1.97e5 | −106 / −119 | **4.40e4** |
| 1 Gpc, 1 h | 2.72e6 / 1.18e7 | same | 2.71e6 |
| 1 Gpc, 1 yr (quasar baselines) | 2.54e8 / 1.11e9 | same | 2.54e8 |
| 3 Gpc, 1 s / 1 yr | 7.84e4 / 4.40e8 (proved) | same | 7.7e4 / 4.4e8 |
| 5 Gpc, 1 s / 1 yr | 1.01e5 / 5.69e8 (proved) | same | 1.0e5 / 5.7e8 |
| VLBI 1 GHz, 1 kHz channel, 1 Gpc, 1 s | 4.53e4 | −131 | 4.40e4 |
| lab lamp at 1 m, on for 1 h | 0.36 / 1.56 | −106 / −119 | pre-asymptotic: in-band ≲ e^{−100} (first chaos 4.5e-58) |
| lab lamp at 1 m, on for 1 day | 8.6 / 37.5 | same | < 0 (safe) |
| lab source at 1 m, on for 1 yr | 3.2e3 / 1.4e4 | same | +1.9e3 (would be noise-dominated) |

**Threshold emission depth Δt\*** (proved rate): the depth where γτ pays |ln f| + B.

| allowance | 1 Gpc | 5 Gpc | source at 1 m |
|---|---|---|---|
| B = 0 | 5.5–7 μs | 1.1–1.4 μs | 12–14 days |
| B = 300 | 81–86 μs | 16–17 μs | 47–49 days |
| B = 1000 | 0.60–0.61 ms | 0.12 ms | 128–130 days |

Each range spans optical V band to radio 100 MHz.

**Observational allowance.** These are Y1's recalled figures, not fetched:
- lensed-image flux ratios agree with smooth models to 10–20%;
- quasar time delays come from correlated variability;
- VLBI fringes on lensed components are strong.

Each needs N_in/S ≲ 1, i.e. ln ≲ 0. The table gives ln ≥ 4.4×10⁴ for any emission depth ≥ 1 s. Real lensed quasars and radio sources have been seen for decades, so by Y1 §2.3 their emission depth is ≥ T_obs.

## 6. Map to the FIXED readings (TESTS.md, lane RZ)

**PASS** ("the in-band fraction is exponentially suppressed by more than the e-fold budget"): **not met.**
- The fraction is power-law small: ln f = −106 to −131.
- The budget is ≥ 4.5×10⁴. The derivation (§3) shows no mechanism for exponential suppression: the far-field top-rung amplitude is exactly flat in ω.
- The MC finds more low-frequency weight than the node ladder, not less.

**FAIL** ("a proved (or controlled) positive lower bound on the in-band fraction, times the finite-distance variance, exceeds ≳ 1 for at least one real observation class"): **met at the "controlled" level.**
- **Finite-distance variance.** The proved rate (RL4) is applied deep in its asymptotic regime (γτ ≥ 4.5×10⁴). The prefactor's τ-power is fitted (p = −3/2, matching the exact root to 2–5%) and its amplitude measured at accessible ε (ln A = −3.5 ± 0.3). The remaining polynomial prefactors are bounded by an argued allowance of 1000 e-folds, against a margin of 4.4×10⁴.
- **In-band fraction.**
  - The exact node-ladder formula is computed at each ε, and its small-ε law is checked to converge within 2–10%.
  - The structural reason is PROVED within the node ladder: time enters only the top rung, and the far field is flat by on-shell propagation.
  - The full MC at accessible ε has 2–5× more low-frequency weight than the node ladder.
  - **Not proved:** that the non-node (interior-insertion) part of the top rung cannot cancel the node part after the time-Fourier integral.
- **Worker reading: FAIL (controlled), bounded to:**
  - (i) RL4 T′, edged emission events, applied per emitter (Y1 §2.3, ARGUED);
  - (ii) the independent-phase average (Y1 §2.1, referee-confirmed);
  - (iii) the stable scalar layer readout standing in for the photon;
  - (iv) photon ℓ_k ≤ 7.9e-20 m (X1, unrefereed);
  - (v) the argued polynomial allowance B ≤ 1000. Even B = 4×10⁴ leaves the 1 s case failing, and B ≤ 2.5×10⁸ the 1 yr case.

**INCONCLUSIVE:** applies if the referee requires a proved Fourier lower bound. The statement needed is:

> **Lemma F:** for top rungs in the far field r ≫ ℓ_k, |∫dt e^{iωt} F_k(x_t; z)| ≥ (1 − 2δ′) |∫dt e^{iωt} F_k^nn(x_t; z)| uniformly in k.

RL3b's power counting (displaced or interior terms are O(z²) relative) makes it plausible: SUGGESTED. If Lemma F is not supplied, the reading is **INCONCLUSIVE, leaning FAIL by ≥ 4.4×10⁴ e-folds.**

## 7. Flags for the referee

1. **The MC geometry is a finite edged source at d = 2 ℓ_k with a fixed observer worldline, not the Gpc null geometry.** By Poincaré invariance in law (RL2 B.1) the noise depends on the proper time to the edge. The low-frequency weight S(0)/V is frame-independent (§3.2), and the beaming of Y1 only changes where the flat range ends.
2. **Short windows.** The windows are 3.5–4 ℓ_k long, so frequency resolution is only 1.6–1.8/ℓ_k. That is why S(ω)/V is estimated through the correlation integral ∫ρ e^{iωδ}, which needs only δ ≲ 1. The periodogram fractions are resolution-limited.
3. **The fits** are over 4 ℓ_k of τ. Free-p fits are ill-conditioned; the p = −3/2 choice is motivated by RL4's LCLT and supported by the root agreement, not derived for this geometry.
4. **The variance V is dominated by trans-Planckian frequencies** (bandwidth ~ 1/(κ√ε ℓ_k) = ℓ_k/(κℓ_P²)): boosted ℓ_k-scale structure, allowed by Lorentz invariance in law. The verdict uses only the in-band part. Whether the total-variance energy budget (backreaction) is itself a separate problem was not examined.
5. **The polynomial allowance B ≤ 1000 is ARGUED** from the explicit factors listed in §4, not computed at physical ε. It enters only additively in the exponent.
6. **Photon versus scalar.** A tensor or vector layer readout could differ in κ by O(1). That changes ln f by less than 1.
7. **Real carrier versus complex carrier.** The MC used e^{iω₀t}. For cos(ω₀t) the turn-on patch (thickness ≤ 0.36 ℓ_k ≪ 1/ω₀) has |J| ≈ w, so T′ is unchanged. The fraction for a real field doubles: f = 2Δk S/(πV), as used.

## Files (scratch: `/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/RZ/Z2/`)

| script | output | content |
|---|---|---|
| `z2_A_carrier_mc.py` | `z2_A_e{1,05,025,0125}.out`, `.npz` | carrier MC, observer time series, all ω₀ per realization |
| `z2_B_ladder_spectrum.py` | `z2_B_ladder_spectrum.out`, `z2_B_res.npy` | node-ladder S_n(ω), roots, ρ(δ), far-field law (op0–op2; ε = 1 … 10⁻⁴) |
| `z2_C_analyse.py` | `z2_C_analyse.out` | mean, V(τ) fits (p = 0, free, −3/2), \|ρ(δ)\|, S(ω)/V, periodogram fractions |
| `z2_E_tau_dependence.py` | `z2_E_tau_dependence.out` | early/late S(ω₀)/V with bootstrap, signed ρ versus node ladder, in-band fractions |
| `z2_D_translate.py` | `z2_D_translate.out` | physical fractions, e-fold budgets, thresholds Δt* |
| `rl2_core.py`, `RL1/` | — | copies of RL2's operator module and RL1's Volterra solver and coefficients |
