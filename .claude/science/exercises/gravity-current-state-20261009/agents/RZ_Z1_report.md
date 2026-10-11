# Lane RZ, probe Z1: the frequency spectrum of the event-route readout noise (worker report)

**Worker:** Claude Opus 5.5 (probe Z1), the same model family as the exercise authors. **Unrefereed.** Worked 21:39–22:00Z on 2026-10-11. OMP_NUM_THREADS=2; every run under 3 minutes. No repository file was edited.

**Read in full:** TESTS.md lines 1–12, "Lane RZ", "C4 result recorded 21:28Z (Y1)", "C4 result recorded 21:01Z (RL4)", "C4 ninth wave / RL3", "C4 results recorded 20:23Z"; `C4_Y1_report.md`, `C4_Y1_referee.md`; `C4_RL4_report.md`, `C4_RL4_referee.md`; `C4_RL3b_report.md`, `C4_RL3b_referee.md`; `C4_RL2_report.md`. The `_full` referee files named in the task do not exist in `agents/` for Y1 and RL4; the summaries were used. Code reused: RL3b's `rl2_core_copy.py`, its K₁ symbol routine, and `RL1in/`.

**Labels:** PROVED (complete argument here, scope stated); CHECKED (numerics, scripts below); ARGUED (standard step, not written out in full); SUGGESTED (heuristic).

## Verdict (worker)

**The noise is not multiplicative on the carrier.** The node ladder carries the source's *intensity* (DC), not its phase. The noise reaches the observer through the last rung as radiation from instantaneous point scatterers, so its spectrum is **white**. It is flat from DC up to ~1/(γℓ_k), with no feature at ω₀. The in-band fraction is therefore **polynomially small, not exponentially small**: it costs 97–155 e-folds, against an e-fold budget of ≥ 2.2e4 at a 1 s baseline at 1 Gpc.

| item | status | content |
|---|---|---|
| Top-rung factorization of the two-time covariance | **PROVED** (exact, all chaos orders) | Cov[φ(x), φ(x′)] depends on the observation points only through source-independent, Lorentz-invariant top kernels. The source enters only through weights that are invariant under a common time translation. |
| Node-level two-time covariance | **PROVED** (exact identity for the node-only chaos sum) | C(x,x′) = ∫d⁴z h(x−z) h(x′−z) S(z), with S(z) = ε[\|Ψ(z)\|² + V(z)] and V(z) = C(z,z). The source's phase cancels in \|Ψ\|². |
| Carrier transport through the ladder | **PROVED** (node level, leading order) | The deep rungs pass only the DC intensity. An intensity modulation at frequency Ω is passed with relative weight \|Λ(γ+iΩ)\| = γ²/(γ²+Ω²). For the 2ω₀ beat of a real field this is ~1e-39 (optical). |
| Spectrum for exponential S (the asymptotic form) | **PROVED** identity; **CHECKED** | p(σ) = (2π)⁻⁴ ∫d³k \|Φ(k + iγN/2)\|² = G(γσ)/(8π³γ). G(0⁺) = π/c₂² is fixed by the IR pole residue, and ∫G = 16π⁴I_h. The spectrum is flat from σ = 0 to σ ~ 1/γ, peaks at 12.8× near γσ ≈ 2.4, then falls as 1/(γσ)². |
| Observer boosted relative to the growth direction | **PROVED** (pole part); **CHECKED** to 3e-4 | The low-frequency level is multiplied by η_b/sinh η_b. The angular density is ∝ 1/D(θ): log-uniform in angle between 1/γ_b and ~1 rad around the source direction. |
| In-band fraction, node level | **PROVED** (exact as t → ∞; planar edge) | f_B = εΔω̃/(4π²c₂²γ̃)·η_b/sinh η_b = √ε Δω̃ η_b /(4π²c₂² c sinh η_b), with γ̃ = c√ε and Δω̃ = Δω ℓ_k/c (band half-width). It does not depend on ω₀. |
| Lower bound on the in-band variance, full model | **PROVED** given one **ARGUED** lemma (filtered U′ for the top hop) | Var φ_B(x) ≥ (1−2δ′)² · [√ε Δω̃/(4π²c₂² c_low)] · [η_b/sinh η_b] · L(x) · (1−o(1)). L is RL4's restricted-ladder lower bound (rate c_low√ε). |
| Numbers at ℓ_k = 7.9e-20 m | **CHECKED** | Band penalty Λ_B = 97–137 e-folds (X-ray to a 1 Hz radio channel), plus a boost penalty of 1.4–16 (quasar age to 1 s baseline). In-band variance e-folds n_B ≥ 4.5e4 (1 s), 7.7e6 (8 h), 2.5e8 (1 yr), 8e11 (quasar), all at the proved rate c_low. |

**Reading against the FIXED RZ readings (Z1's half): the band-fraction obstacle is removed. Z1 alone: INCONCLUSIVE pending Z2's finite-distance normalization, leaning FAIL.**
- **PASS needs exponential suppression of the in-band fraction. Excluded at node level:** the fraction is an explicit power of ε and Δω (exact formula). In the full model the suppression is at most 155 e-folds, given filtered U′.
- **FAIL needs** (in-band lower bound) × (finite-distance variance) ≳ the signal. Z1 supplies the first factor at rate level: n_B ≥ n_var − Λ_B with Λ_B ≤ 155. The prefactor relative to the signal |Ψ_B(x)|² at physical D is Z2's job (section 7).
- **Against the supervisor expectation:** the conclusion (in-band noise is not small enough to save the route) holds, but the stated mechanism and the O(1) fraction do not.
  - The noise is white, not concentrated at ω₀.
  - The fraction is e^{−97} to e^{−155}, not O(1).
  - It is still irrelevant against budgets of 10⁴–10¹² e-folds.

**Plain summary.**
- **The sprinkled points are events, not objects.** Each one exists for an instant. When the wave passes such a point, the point re-emits a flash: the local field value times a short, sharp response. A flash at an instant contains all frequencies equally. So the noise it adds is white, whatever the carrier frequency of the light that excited it.
- **The chain of shared points (the ladder) carries brightness, not phase.** Deeper points pass on how strong the wave was, averaged over time. The carrier's phase drops out, because both copies in the variance see the same random point.
- **The noise at the telescope is therefore white noise from DC to absurdly high frequencies.** It is spread evenly over about 10³²–10³⁴ times the bandwidth of any real detector band. Only a fraction ~e^{−100} to e^{−155} of it lands in any given band.
- **That fraction does not rescue the theory.** The noise grows by at least 45,000 e-folds for one second of emission seen at 1 Gpc, and by much more for real sources. Losing 155 e-folds to the band leaves 45,000.
- **What still has to be shown is the absolute normalization** (Z2): how large the noise is at physical distance relative to the signal, not just how fast it grows.
- **A side finding.** In the GW setting of RL4 (a 10 km source at 1 Gpc, the LIGO band, the 1e-19 m bar), the band penalty of 152 e-folds exceeds the proved 129 variance e-folds. That RL4 FAIL is therefore not observationally robust at its own source scale with the proved constant. It is robust with the node-ladder constant (408 e-folds left), or with the inspiral as the source extent (Y1 §6.2).

## 1. Setting (RL1–RL4 conventions)

- **Units.** ℓ_k = 1, ρ = 1/ε. The mean is H̄ = εh, with M = δ + h, Φ = f̃/(1 − f̃) the 4D symbol of h, and 1 − f̃(w) = c₂w(1 + O(w ln w)) as w → 0 (Euclidean-sign invariant w = −k²).
- **Field and mean.** φ(x) = Σ_{y∈P} H_P(x,y) J(y) (plus the identity term), with mean Ψ = MJ.
- **Chaos.** The exact chaos expansion (RL3, referee-confirmed) is linear in the observable. So for any two readouts, or any filtered readout φ_B = ∫b(t)φ(t,x⃗)dt:

  Cov[φ(x), φ(x′)] = Σ_k (ε^k/k!) ∫ F_k^J(x; z) F_k^J(x′; z)* dz,  Var φ_B = Σ_k (ε^k/k!) ∫ |∫b(t) F_k^J((t,x⃗); z) dt|² dz.

  Every term of the second series is ≥ 0, so any restriction of it is a lower bound.
- **Source.** J(y) = j(y⃗)e^{−iω₀y⁰}, switched on across a spacelike edge (RL4 T′). Or a stationary random-phase source J = j(y⃗)ζ(y⁰), with ζ stationary, band-limited near ω₀ and independent of P.

## 2. The two-time covariance

### 2.1 Top-rung factorization, all orders (PROVED)

Group each chaos kernel by its top hop, using RL4 §2.1's step factorization read from the top:

F_k^J(x; z_1..z_k) = Σ_{b=1}^{k} Step_{0,b}(x; z_1..z_b) Q_b(z_b; z_{b+1}..z_k) + (top hop containing every z, ending at a free point v with weight Ψ(v)).

- **Step_{0,b}** is the hop structure from x to the node z_b with z_1..z_{b−1} interior to its hops. It is built from h and f^{(g)} only, so it is **source-independent and Poincaré-invariant**.
- **Q_b** is the response at the node z_b to the remaining insertions and the source.

**Consequences.**
- The observation point enters F_k only through the Step kernels. So the dependence of Cov[φ(x), φ(x′)] on (x⁰, x′⁰) is entirely in Step_{0,b}(x;·)Step_{0,b′}(x′;·)*.
- For a stationary source, a common time translation of all z multiplies every Q_b by the same phase e^{−iω₀T}. So the weights Q_bQ_{b′}* are translation-invariant and carry no observation-time dependence.
- **The observed spectrum is a superposition of the spectra of the source-independent top kernels.** The carrier can shape it only through the z-dependence of those weights.

### 2.2 Node level (PROVED, exact for the node-only sum)

For the node part, Step_{0,1} = h(x − z_1) and Q_1 = F_{k−1}^{J,nn}(z_1; z_2..). Summing the deep part:

**C_nn(x,x′) = ∫ d⁴z h(x−z) h(x′−z) S(z),  S(z) = ε[|Ψ(z)|² + V_nn(z)],  V_nn(z) = C_nn(z,z).**

- This is the renewal of RL3b Theorem 1, now with **two different top endpoints over one shared bottom**.
- The bottom weight is |Ψ(z_k)|², so the carrier phase e^{−iω₀z_k⁰} cancels exactly.
- So S is the noise-source intensity per unit 4-volume. It is time-independent for a monochromatic source, apart from the slow e^{γt} growth.

### 2.3 Real fields and modulated intensity (PROVED at node level, leading order in γ)

- **Real fields.** For a real J the bottom weight is Ψ² = |ψ|²[1 + cos(2ω₀t + 2 arg ψ)]/2. The 2ω₀ part enters S as a modulation e^{±2iω₀t}.
- **One rung passes a modulation at frequency Ω with factor Λ(γ+iΩ).** Here Λ(z) = 4πεI_h/z² · (1+O(z² ln z)) is the node characteristic function of RL3b, continued analytically to Re z > 0.
- **Size of the factor.** Relative to the growing DC mode it is |Λ(γ+iΩ)| = γ²/(γ²+Ω²). For Ω = 2ω₀ this is ≈ (γ̃/2ω̃₀)²:
  - ~1e-40 to 3e-39 optical;
  - ~1e-30 to 4e-29 at 5 GHz (c_low to k_h).

  So the ladder is a low-pass integrator of intensity with cutoff ~γ. Its DC output is half the real-field intensity.
- **Random-phase source.** For a stationary random-phase or incoherent source the same holds, with |Ψ|² replaced by the mean intensity E_ζ|Ψ|². For independent emitters it is Y1's sum of mean noise powers.

### 2.4 Why the supervisor's multiplicative picture fails (PROVED content, plain statement)

- A sprinkled point is an **event**: it scatters the field at one instant.
- The noise it injects at z is the field value Ψ(z) times a compensated Poisson count dÑ(z), which is δ-correlated in spacetime. Multiplying a δ-correlated noise by e^{−iω₀z⁰} leaves it δ-correlated, so the carrier is forgotten at the injection point.
- The injected noise then reaches the observer through one mean propagator h. That is the retarded Green function at low k, and it weights all on-shell frequencies equally.
- A persistent scatterer (a worldline) would give carrier-locked, multiplicative noise. A Lorentz-invariant point process has no worldlines.

## 3. The spectrum

### 3.1 Identity (PROVED)

**The setup.** Take S(z) = S(x)e^{γN·(z−x)}. This is the asymptotic form in the growth frame N. For the planar edge it is exact up to the Blackwell renewal limit. For a finite source it holds by linearizing τ(w,z) about x: over the relevant depths the relative error is ≤ 2e-5 (§3.3).

**Parseval.** Put e^{−γN·w/2} on each factor and use h real, so Φ(−k*) = Φ(k)*. This gives

  C(x, x−Δe) = S(x) e^{−γN·eΔ/2} ∫ d⁴k/(2π)⁴ |Φ(k + iγN/2)|² e^{−ik·eΔ}.

**PSD.** At fixed x⃗, the power spectral density in observer frequency σ is

  **p(σ) = (2π)⁻⁴ ∫ d³k |Φ(w)|²,  w = |k⃗|² − σ² + γ²/4 − iγ k·N.**

**Growth frame (N = e₀).**
- For γ → 0 at fixed b = γσ, k⃗-integration across the shell gives p(σ) = G(γσ)/(8π³γ), with G(b) = b∫du |Φ(u − ib)|².
- **Pole residue:** G(0⁺) = π/c₂², so the white level is **p₀ = 1/(8π²c₂²γ)**. It holds at σ = 0 as well (direct k-integral: 4π∫k²dk/(c₂²(k²+γ²/4)²) = 2π²/(c₂²γ)).
- **Total:** ∫p dσ = (1/4π³γ²)∫₀^∞ G db = 4πI_h/γ². This is RL3b's momentum identity.

### 3.2 Numbers (CHECKED; `z1_A_spectrum.out`, `z1_B_direct_and_boost.out`)

| op | c₂ | ∫G db / 16π⁴I_h | effective one-sided bandwidth ∫G/G(0⁺) (in units of 1/γ) | G/G(0⁺) at b = 1e-4, 1e-3, 0.1, 2.4, 43, 2000 |
|---|---|---|---|---|
| op0 | 0.69218 | 0.99999 | 141.47 (analytic 16π³c₂²I_h = 141.47) | 1.0025, 1.027, 3.1, 12.8 (peak), 0.5, 4e-5 |
| op1 | 0.66087 | 0.99999 | 138.60 | same shape |
| op2 | 0.63112 | 0.99999 | 166.49 | same shape |

- **Direct 3D-k check** of p(σ)·8π²c₂²γ at finite γ with the exact Φ:
  - γ = 1e-2: 1.0095 at σ = 0, 1e-3, 1e-2, 0.1.
  - γ = 1e-3: 1.0046 / 1.0040 / 1.0006 / 1.0010 / 1.0010 / 1.0028 at σ = 0 … 1; then 3.10, 10.97, 5.83 at σ = 100, 1e3, 1e4. These match G(γσ).
- **Spectrum shape.** Flat within 3% from DC to γσ ~ 1e-3 (within 25% to 1e-2), then a broad hump, then a 1/(γσ)² tail; large-b log-slope −2.001. Physical bands sit at γσ ~ 1e-44, deep in the flat part.
- **Numerical note.** RL3b's log s-grid starts at s = 1e-9. That leaves M₀_grid = −1.0e-9, which adds a spurious 2πM₀/w pole and dominates |Φ| for |w| ≲ 1e-4. I removed it analytically (`z1_A_spectrum.py`, `Phi`); with it removed, 1/(c₂wΦ) = 1 ± 3e-3 down to |w| = 1e-6. RL3b's I_h is unaffected, because the small-|w| region carries negligible weight.

### 3.3 Boosted observer and angular distribution (PROVED pole part; CHECKED)

**Setting.** Let the observer move with rapidity η_b relative to N. For a source edge at null distance D and emission T before the retarded time, γ_b = cosh η_b = (D + cT)/τ ≈ √(D/2cT) (Y1 geometry).

**The level.** Near the shell Im w = −γσD(θ), with D(θ) = cosh η_b − cos θ sinh η_b and θ measured from the source direction. So

  p_obs(σ) = p₀ · (1/4π)∫dΩ/D(θ) = p₀ · η_b/sinh η_b.

**CHECKED** (`z1_B`, γ = 1e-6, σ = 1e-3):

| η_b | p_obs/p_rest | η_b/sinh η_b |
|---|---|---|
| 0.5 | 0.95934 | 0.95952 |
| 1 | 0.85067 | 0.85092 |
| 2 | 0.55123 | 0.55144 |
| 4 | 0.14650 | 0.14657 |
| 6 | 0.02972 | 0.02975 |

**Total variance.** It is a Lorentz scalar. The boost moves power to higher observer frequencies in the forward direction.

**Angle (PROVED at node level; numbers in `z1_D_angular.out`).**
- The in-band noise per solid angle is ∝ 1/D(θ). That is flat inside 1/γ_b of the source direction and then log-uniform in angle out to ~1 rad. It appears as the source image plus a halo.
- Fraction inside a PSF:

| case | within 1 mas | within 0.05″ | within 1″ |
|---|---|---|---|
| T = 1 s (1/γ_b = 0.9 mas) | 2% | 20% | 35% |
| T = 1 yr (1/γ_b = 5″) | — | 4e-6 | 1.7e-3 |
| 1e7-yr quasar (1/γ_b = 4.5°) | — | 1.5e-12 | 6e-10 |

  These are ≤ 35 e-folds. They change where the noise appears, not whether it is observable.

**Validity of the exponential S along the past cone.**
- z = x − r(1,n̂) gives τ(w,z)² = τ² − 2rτD(θ), exactly for a point-like edge.
- The decay depth is 1/(γD) ≤ 2γ_b/γ. For 1 Gpc and 1 s that is 1.4e21 m ≪ D.
- So the linearization error is ≤ 2γ_b/(γD) ~ 5e-5. Transverse curvature corrections are ~2e-5.

### 3.4 In-band fraction (PROVED at node level, planar edge, t → ∞)

For an analytic band filter with b̂ = 1 on [ω₀−Δω, ω₀+Δω] (‖b‖² = Δω/π), and with S = εV at large V:

**f_B = Var φ_B / Var φ = 2Δω p_obs/∫p = εΔω̃ / (4π²c₂²γ̃) · η_b/sinh η_b = √ε Δω̃ η_b / (4π²c₂² c sinh η_b),**

where c is the rate constant (γ̃ = c√ε) and Δω̃ = Δωℓ_k/c_light.

**Equivalent position-space form.**
- The band-filtered top rung from z at distance r on the observer's past cone is h_B(z) = b(z⁰+r)·m₁/r · (1 + o(1)), with m₁ = ∫τh dτ = 1/(4πc₂) (the same pole residue).
- So B = εm₁²‖b‖²∫dΩ∫dr V(x − r(1,n̂)): **radiation from white noise of intensity εV spread over the past light cone to depth 1/(γD).**

**Properties.**
- **No ω₀.** Every band of the same width gets the same noise, from radio to X-ray and DC.
- **Correlation time.** The two-time correlation C(Δ)/C(0) = ∫G(b)cos(bΔ/γ)db / 16π⁴I_h decays on Δ ~ γℓ_k/c_light ≈ 7e-60 s (growth frame).

## 4. Lower bound in the full model (Prop. 4)

**Proposition 4.** Assume RL4 T′'s hypotheses, with a planar past edge of normal N. Let x be at N-time t, and b an analytic band filter with envelope β > 0 and b̂ = 1 on the band. Then

**Var φ_B(x) ≥ (1−2δ′)² · [√ε Δω̃ / (4π²c₂² c_low)] · [η_b/sinh η_b] · L(t) · (1 − o(1)),**

where L(t) ≥ c e^{z_c t}, z_c ≥ c_low√ε, is RL4's restricted alternating-cap ladder lower bound (Blackwell).

**Proof (steps).**
1. **Positivity** (§1): restrict the chaos sum to configurations with z_1 at distance r on the past cone of the worldline (t, x⃗) and z_2, …, z_k in RL4's set A_{k−1}.
   - Choose the cap axis per direction: e = −n̂, where n̂ is the top-rung direction.
   - Then the turn rapidity at z_1 is θ ≥ η_top + η₂ − ln 4 ≥ θ*, since η_top ≈ ln(2r) ≈ 70 and η₂ ≥ η* = 6.42.
2. **Top-hop split.** Split F_k^B = h_B(z_1)Q_1 + Σ_{b≥2} Step^B_{0,b} Q_b.
   - **Filtered U′ (ARGUED):** |Σ_{b≥2} Step^B_{0,b}Q_b| ≤ 2δ′ |h_B(z_1) Q_1| on this set.
   - This is the same geometry as RL4 §2.3: each interior insertion in the top hop pays e^{−θ}. The t-integration only replaces the pointwise top factor by its filtered value, at the same e^{−θ} order. That value is ≤ ‖β‖_∞(1/r)∫τ|f^{(g)} …|dτ, against h_B = β·m₁/r with m₁ ≠ 0.
   - Not written out: the δ′ constants, and the set where β(z_1⁰+r₁) and β(z_2⁰+r₂) differ, which arises when the second leg's null projection exceeds 1/Δω̃.
3. **Deep part.** RL4 U′ + T′ give |Q_1| ≥ (1−2δ)^{k−1}|Q_1^{nn}| with a nonzero end factor. Summed over the deep configurations, this gives L at z_1 (PROVED, RL4, refereed).
4. **Top factor.** h_B(z_1) = β(z_1⁰ + r)m₁/r · (1 + O((ω₀/r) ln(r/ω₀))), with m₁ = 1/(4πc₂) ≠ 0. This needs only ∫τ|h|dτ < ∞ and the pole residue (PROVED).
5. **Cone integral.** ∫dΩ∫dr L(t_N(x − r(1,n̂))) = L(t) · 4πη_b/(c_low√ε sinh η_b) · (1 − o(1)). L(t) ~ Ce^{z_c t} (Blackwell); z_c ≥ c_low√ε only makes the depth shorter, and the bound uses 1/c_low conservatively against the true root. Multiply by εm₁²‖b‖². ∎

**Finite source.** The finite-source version uses RL4's LCLT step (ARGUED in RL4, polynomial factor only) and the linearization of §3.3.

**Status.** Prop. 4 is PROVED except for step 2 (ARGUED) and the finite-source LCLT (RL4's ARGUED step). Without step 2, the node-level statement (§3.4) is exact.

## 5. Numbers (CHECKED; `z1_C_translate.out`; op0, ℓ_k = 7.9e-20 m, ε = 1.75e-63, √ε = 4.19e-32)

**Band penalty Λ = −ln f_B before the boost (c_low / k_h):**

| band | Δω̃ | Λ (c_low) | Λ (k_h) |
|---|---|---|---|
| radio 1 Hz channel | 8.3e-28 | 137.1 | 138.6 |
| maser 1 kHz channel | 8.3e-25 | 130.2 | 131.6 |
| 5 GHz continuum, 500 MHz | 4.1e-19 | 117.1 | 118.5 |
| optical 0.1 nm channel | 9.9e-17 | 111.6 | 113.0 |
| optical V band | 7.2e-14 | 105.0 | 106.5 |
| X-ray 0.5–2 keV | 3.0e-10 | 96.7 | 98.1 |
| LIGO 20–1000 Hz | 8.1e-25 | 130.2 | 131.7 |

op1 and op2 agree within 0.2.

**Cases.** n_B = n_var − Λ_B, with Λ_B = band penalty + boost penalty.

| case | τ (m) | boost penalty | n_var (c_low / k_h) | n_B, worst band (1 Hz radio) | n_B, V band |
|---|---|---|---|---|---|
| lensed, 1 Gpc, 1 s | 1.36e17 | 16.2 | 4.53e4 / 1.97e5 | 4.51e4 / 1.97e5 | 4.51e4 |
| lensed, 1 Gpc, 8 h | 2.31e19 | 11.4 | 7.68e6 / 3.34e7 | 7.68e6 | 7.68e6 |
| lensed, 1 Gpc, 1 yr | 7.64e20 | 8.2 | 2.54e8 / 1.11e9 | 2.54e8 | 2.54e8 |
| lensed, 5 Gpc, 1 yr | 1.71e21 | 8.9 | 5.69e8 / 2.48e9 | 5.69e8 | 5.69e8 |
| quasar, 1 Gpc, 1e7 yr | 2.42e24 | 1.4 | 8.05e11 / 3.50e12 | 8.05e11 | 8.05e11 |
| on-cone radio emitter, s = 3 m | 1.36e13 | 25.1 | 4.5 / 19.7 | −158 / −144 | −126 / −112 |
| maser emitter, s = 1 km | 2.48e14 | 22.3 | 83 / 360 | −77 / +199 | −45 / +231 |
| lab lamp, 1 m, on 1 h | 1.08e12 | 0 | 0.36 / 1.56 | −137 | −105 |
| lab lamp, 1 m, on 1 day | 2.59e13 | 0 | 8.6 / 37.5 | −129 / −101 | −96 / −69 |

- **Crossover (1 Gpc).** In-band n_B ≥ 0 once emission began more than T* before the retarded time:
  - T* = 7.9 μs (c_low) / 0.43 μs (k_h), V band;
  - 9.4 μs / 0.52 μs, 5 GHz continuum.
- **Same picture at ℓ_k = 1e-19 m.** At 1 s, n_B = 2.2e4 (c_low).
- **Consequence for the RL4 GW setting** (1 Gpc, s = 10 km, LIGO band; boost penalty 21.2):
  - At ℓ_k = 1e-19 m: n_var = 129 / 561 and Λ_B = 151.6 / 153.1, so **n_B = −23 (c_low) / +408 (k_h)**.
  - At 7.9e-20 m: n_B = +110 / +986.
  - So, with the proved constant at the E1 bar, RL4's all-frequency FAIL does not survive band filtering at s = 10 km. It survives with the node-ladder constant, and with any inspiral extent of a year or more (n_B ≈ 1.25e8 at the bar).
  - RL4's recorded reading was a rate statement and is unaffected. Its observational gloss "fails for edged sources over 1 Gpc" needs this qualifier.

## 6. Map to the FIXED RZ readings

- **PASS** ("the in-band fraction is exponentially suppressed by more than the e-fold budget"): **excluded at node level.** f_B is an explicit polynomial in ε and Δω̃: e^{−97} to e^{−155} including the boost. In the full model it is the same, given filtered U′. This is ≥ 140 times smaller in the exponent than the budget at a 1 s baseline.
- **FAIL** ("a proved or controlled positive lower bound on the in-band fraction, times the finite-distance variance, exceeds what observation allows for at least one real observation class"):
  - Z1 supplies the first factor: Prop. 4 (one ARGUED lemma), and the exact node-level f_B.
  - At rate level, n_B ≥ 4.5e4 for any lensed source seen for 1 s at 1 Gpc in any band.
  - The finite-distance prefactor is not supplied here. Neither is the onset at physical D.
- **Z1's reading: INCONCLUSIVE pending Z2, leaning FAIL.** It becomes FAIL if Z2 supplies a controlled normalization whose log-prefactor is ≲ 4e4 e-folds below the RL4 rate at the 1 s, 1 Gpc point. Y1 estimated ≲ 1e3; the band penalty is ≤ 155 of the budget.

## 7. What Z2 must supply

1. **Finite-distance normalization.** The ratio V(x)/|Ψ_B(x)|² at physical τ and D, i.e. the prefactor of RL4's L(t) relative to the signal. That means:
   - the LCLT constant (polynomial in 1/ε);
   - the end factor;
   - the 1/D² dilution of the signal, which the τ-only noise kernel does not share.

   Z1's input to this is: in-band noise = f_B × total, with f_B as in §3.4 (use c = the measured or proved rate consistently in both).
2. **A numerical check of the white spectrum at accessible ε.** Use a carrier source in RL2's fixed-source MC, at ε = ¼ … ⅛, with an ω₀ well below 1/ℓ_k.
   - Measure the PSD of φ(t) at fixed x⃗ over a window.
   - Prediction: the PSD is flat at level V·γ/(16π³c₂²I_h) per unit σ (two-sided density p/V), with no excess at ω₀.
   - At these ε, γ ~ 1, so "flat" means flat to σ ~ 1e-3/γ (25% rise by 1e-2/γ), then the G(b) hump. Compare with G(γσ)/G(0⁺) from `z1_A_spectrum.out`.
3. **A check of filtered U′.** Compare the node-only and full filtered chaos (or MC) in-band variances at the same ε. Prop. 4 needs the ratio ≥ (1−2δ′)² ≈ 0.8. Any O(1) ratio suffices for the reading.
4. **The real-field 2ω₀ beat.** Confirm in MC that no line appears at 2ω₀ (prediction: suppressed by γ²/(4ω₀²)).

## 8. Flags for the referee

1. **§2.1.** The top-hop grouping reads RL4's step factorization from the top instead of from the bottom. Check that the free-endpoint term (top hop containing every z) is source-dependent only through Ψ(v), with v below z_k.
2. **§3.1.** The analytic continuation k → k + iγN/2 uses Φ analytic in the forward tube (retarded h, exponential bound e^{γt} on S). The sign of Im w, and the use of Φ(−k*) = Φ(k)* for real h, give |Φ|² symmetric in σ.
3. **§3.4.** The exact node-level f_B uses S = εV (V ≫ |Ψ|²), and the asymptotic exponential form of V (Blackwell for the planar edge). For a finite source, the linearization error is quantified in §3.3.
4. **Step 2 of Prop. 4 (filtered U′)** is the one ARGUED step. Without it the full-model statement rests on the same power counting as RL3b's P1, but with the top-hop geometry RL4 already controls.
5. **Numerics.** The spurious-pole removal (M₀_grid = −f(0)·1e-9) is exact to O(1e-9). G(0⁺) = π/c₂² is analytic; the numerics reach 1.0025 at b = 1e-4.
6. **Translation.** Flat-space τ (FRW changes O(1) in τ), the Δω half-width convention, and η_b from Y1's geometry. The angular fractions affect only where the noise appears (image or halo), at a cost of ≤ 35 e-folds.

## Files (scratch: `/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/RZ/Z1/`)

| script | output | content |
|---|---|---|
| `z1_A_spectrum.py` | `z1_A_spectrum.out` (all ops), `z1_A_spectrum_op0.out` (first run, before the spurious-pole fix) | G(b) = b∫\|Φ(u−ib)\|²du; G(0⁺) = π/c₂²; ∫G = 16π⁴I_h; spectral shape |
| `z1_B_direct_and_boost.py` | `z1_B_direct_and_boost.out` | direct 3D-k PSD at γ = 1e-2, 1e-3 (flat from DC); boosted-observer factor η_b/sinh η_b |
| `z1_C_translate.py` | `z1_C_translate.out` | band penalties, boost penalties, n_B for physical cases at ℓ_k = 7.9e-20 and 1e-19 m; crossover T*; RL4 GW setting |
| `z1_D_angular.py` | `z1_D_angular.out` | fraction of in-band noise within 1 mas, 0.05″, 1″, 1 rad of the source |
| `rl2_core_copy.py`, `RL1in/` | — | copies of RL2's operator core and RL1's coefficients (byte-identical inputs) |
