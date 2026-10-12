# C5 round 15, probe R15-2: set A E1, the spin-2 conserved-noise assembly for the repaired gain (worker report)

**Worker.** Claude Opus 5.5, the same model family as the supervisor and every C5 worker. **Not refereed.** Run 2026-10-12, 21:40Z to about 22:08Z. No repository file was edited.

**Scratch:** `scratchpad/C5/R15-2/`.
- `scripts/r152_checks.py` and `scripts/r152_checks.out` hold every number below (sections [1]–[9]). Runtime about 35 s with OMP_NUM_THREADS=2.
- SHA-256: script `be3d556b627b171470fb5dc9dfa6d67df25c46b15e6b75969428e313cb1e71bc`, output `002294d895ba5fd601293217b842420cff837231429a28f34092eb89b91b023b`.
- No downloads, no web fetches. One comparator read from an earlier untrusted text extraction of OWD 2302.07283 (`scratchpad/C5/ref_R6-4/text/owd2302.txt`, read as data only).

**Paths.** `P/` = `.claude/science/exercises/gravity-current-state-20261009/`; `TESTS` = `P/TESTS.md`; `AX` = `docs/MINIMAL_AXIOMS_2026-06-29.md`; `vR13-6` = `P/agents/C5_R13-6_referee_verdict.md` (and so on); `R13-6:n` = `P/agents/C5_R13-6_report.md:n` (and so on); `out:n` = line n of `scripts/r152_checks.out`; `OWD:n` = line n of the OWD text extraction above.

**What I read.** In full: `AX`; `TESTS:2302-2320` (C5 method); the set-A entries `TESTS:3143-3180, 3405-3418, 3466-3481, 3559-3573, 3707-3738, 3905-3915, 3984-3998, 4218-4243, 4285-4296, 4320-4330, 4436-4462, 4515-4560, 4682-4732, 4815-4893` and round 15 `TESTS:4925-4960`; `C5_R13-6_report.md`, `vR13-6`; `C5_R14-2_report.md`; `C5_R11-5_report.md:100-260`; `C5_R8-3_report.md:60-200`; `C5_R6-4_report.md:144-160` (γ-window); `OWD:590-660`. Scripts: `scripts/C5/R13-6/r136_checks.py` ([6], [9]); `scripts/C5/R11-5/r115_checks.py` ([7]).

**Labels.** **proved** (derived here under the stated hypotheses); **checked** (a number in `r152_checks.out`); **suggested** (argued, not proved); **reading** (interpretation); **comparator** (literature, via earlier referees or the local untrusted text).

**Subtraction rule.** Every variance, energy density and spectral density below is positive; subtraction: none. The Bianchi defects in [2]–[3] are measured against zero; the TT weight in [6] is measured against R13-6's formula. **Order rule.** Linear order in G for the mean field and the Bianchi identity; Gaussian (second order in the matter–meter coupling) for CP and decoherence; second order in the metric noise for the energy budget and the PPN shift.

---

## Reading against the FIXED readings (`TESTS:4940-4951`)

**Worker reading: OPEN.** No no-go is claimed, so no referee is mandatory. A referee is recommended for §3.3 (Lemma B), §4.5 (the constraint-channel energy) and §4.3 (the weight ¼).

- **Not EXCLUDED.** The example the item names, "conserved spin-2 noise is impossible with the repaired gain", is **false**. §3 builds conserved spin-2 noise with the repaired gain and a finite start, exactly, path by path (proved; checked out:2, 11). The repaired gain is in fact the smoothness that makes it work: f(0) = f′(0) = 0.
- **Not VIABLE**, for two reasons:
  1. **The budget fails on one of its own premises.** The assembly exposes a budget term no earlier E1 or E2 table counted: the stationary field energy of the record noise in the **constraint channels** (Newtonian scalar and gravitomagnetic vector). If non-radiative metric noise gravitates (premise (iii), the analogue for constraint fields of the Isaacson premise used for TT), this term exceeds ρ_Λ across most of the window, by 1.2× at ℓ = 5e-6 m up to 1e12× at 4e-10 m at the drag ceiling (checked out:66-69). R6-4's γ-trade rescues ℓ ≳ 5e-8 m in the τ_c variant and ℓ ≳ 2.5e-7 m in the strict variant (suggested; out:91-102). Under premise (i) (only free GWs gravitate) the term is absent.
  2. **The second-order PPN bound is power counting** with checked ⟨h²⟩ ≤ 1.4e-49. The margin is ≥ 39 decades, but the coefficient is not computed, so the test is suggested, not checked.

| Stated test (`TESTS:4943-4947`) | Result | Label |
|---|---|---|
| CP | Every channel is a Gaussian instrument with causal record feedback. The exact irrational TT limit is CP: positive-real (outer) arcsine-quadrature approximants converge in trace norm (relative error 1.5e-4 at N = 2048). This closes the referee's conditional (`vR13-6:27-31`). | proved; checked out:39-44 |
| Bianchi (conserved noise source) | TT noise is conserved identically. S/V noise is conserved path by path from t₀, with J^{0ν}(t₀) = 0. **New: R13-6's start (h = ḣ = 0, couplings switched on) violates the Bianchi identity of the mean field** whenever matter is present at t₀ (Lemma B). An exact conserved initial-memory term repairs it, and the repair is transient only because the first moment is zero. | proved; checked out:2, 11-12, 18-21 |
| TT weights vs the assumed O(1) | The exact weight is **¼** of R11-5/R13-6's normalization (0.2524 including the log constant). Only TT carries secular near-cone content; S and V carry none. ḣ is regular (finite variance) once the gain is included. | proved; checked out:28-35, 47-48 |
| PPN α₁, α₂ at second order | ⟨h_ij h_ij⟩_TT ≤ 1.4e-49 and ⟨φ²⟩_S ≤ 8e-59. The noise-fluid term is ≤ 1.6e-33 × ρ_n/ρ_crit at 1 AU. Passes by ≥ 39 decades. | ⟨h²⟩ checked out:74-80; coefficient suggested |
| Budget | **TT:** ε limits relax ×3.8–3.9; the τ_c window reopens down to ℓ ≈ 4.3e-10 m (R14-2 had 1–2e-9 m). **Constraint channels:** a conditional overshoot (above). | TT checked out:50-61; S/V checked magnitude out:64-69, γ-trade suggested out:91-102 |

---

## 0. In plain words

- **Gravity's noise has six parts, and only two of them are waves.** A conserved source in linearized gravity splits, in the CMB frame, into two wave polarizations (TT), two "gravitomagnetic" parts and two scalar parts.
  - Only the waves travel at the speed of light.
  - The other four respond instantly, like Newton's potential (checked exactly, out:2-7).
  - The light-cone trouble that forces a start time (R11-5 Lemma C, R12-4 Theorem U) is therefore confined to the two wave polarizations. The other channels can be stationary.
- **Conserved noise is easy, and the repaired gain is exactly smooth enough.** Pick the noise's energy and transverse-momentum densities freely, pass them through the gain, and get the remaining components from time derivatives.
  - This needs the gain's impulse response to start flat (f(0) = f′(0) = 0). The repaired gain does (out:6).
  - The noise then switches on smoothly at the start and is conserved at every instant.
- **But the start itself had a hole.** R13-6's start ("meters in vacuum, metric zero, switch on") breaks energy-momentum conservation of the recorded matter during the first few gain times, whenever matter already exists at the start.
  - The fix is an initial record of matter's energy and momentum at t₀, which the gain then forgets.
  - It forgets completely only because the repaired gain's average delay is zero. The original gain would keep a frozen spurious energy density forever (out:21).
- **The gravitational-wave budget is 4× easier than assumed.** The "order-one tensor weights" overestimated the wave content by a factor 4. The allowed gain time scale widens, and the window that R14-2 found closing near 1–2 nm closes at 0.4 nm instead.
- **A new budget item appears.** The Newtonian part of the record noise is a fluctuating potential everywhere in space. If its field energy gravitates, as the wave energy is assumed to, it acts like a vacuum energy of size ħ/(ℓ³τ). That is far above the dark-energy density at small smearing lengths.
  - It can be pushed down by recording the Newtonian channel less precisely, at the cost of more matter decoherence (R6-4's γ-trade).
  - That works only above about 50 nm (gain-time variant) or about 250 nm (strict variant).

---

## 1. Prior art (each counted once)

1. **R13-6 and its referee** (`vR13-6:3-43`).
   - Lemma D, the literal gain EXCLUDED.
   - P-r13b repair: (1 − 4ix)(1 − ix)^{−4}, a changed OPEN model.
   - Lemma S (Ĥ = (Ω² − (ω+i0)²)^{−1/2} ↔ θJ₀).
   - The ḣ white-noise boundary term and the conditional exact-limit CP (`vR13-6:27-31`).
   - The spin-2 assembly is unbuilt (`R13-6:164, 468-470`; double-curl route suggested).
   - Budget at "O(1) tensor weights" (`R13-6:311`; `r136_checks.py` [6]).
2. **R14-2** (worker, unrefereed).
   - E1 OPEN, for four reasons (`R14-2:26`).
   - The τ_c ceiling with V_CMB is 1.49e-3 m (`R14-2:168-176`).
   - The window closes at 1–2e-9 m (`R14-2:175, 227-238`).
3. **R11-5** (`vR11-5`; `R11-5:145`): mean field h̄ = G_R F_u⟨T⟩, conserved because F commutes with ∂; budget formula with O(1) tensor weights (`R11-5:187, 267`); H-cosmo conditional (`R11-5:236`).
4. **R8-3** (`R8-3:184`): F·T is conserved, so the Bianchi identity holds for the mean field. The no-go is posed in the spin-2 channel with the photon's spin-2 spectral weight (`R8-3:104, 140-159`).
5. **R12-4 Theorem U** (`TESTS:4518-4524`). Its class needs "an undamped massless 1/s pole" (`TESTS:4521`). That is used in §3.1 to place the S/V channels outside it.
6. **R6-4** (`R6-4:144-160`): the least-decoherence floor (4πG/ħ)|g̃|²/k²; lab margins; the γ-window (allowed γ down to 2e-10 at ℓ ≥ 1 µm, 3e-5 at 10 nm, 0.03 at 1 nm, 1 at 4 Å); H-cosmo conditional (`TESTS:3415`).
7. **Comparator (untrusted local text): OWD 2302.07283.**
   - The covariant diffusion matrix is the generalized DeWitt metric. It is "not positive semi-definite", and is required to be positive only on physical local degrees of freedom; scalar and tensor two-point functions are shown positive elsewhere (`OWD:604-621`).
   - "The challenge … is to obtain the transverse parts of the Einstein equation, which are the constraints" (`OWD:601-603`).
   - §3.1 below meets the indefiniteness as the indefinite scalar block, and handles it by a positive noise covariance per channel.
8. **Repository grep** of `P/agents/` and `P/TESTS.md` for "Poisson gauge", "Bardeen", "constraint channel", "initial-memory", "Riesz", "DeWitt": no derivation of the constraint-channel noise energy or of the finite-start mean-field defect. `docs/` was not grepped.

## 2. Hypotheses: class ℰ₁₅ (stated before any title)

- **H1.** Linearized Gaussian CQ gravity on Minkowski space, preferred CMB frame u, as R13-6's E1-H1–H5 (`R13-6:144-157`), with three changes:
  - the noise is a symmetric tensor ξ^{μν};
  - matter couples through ½h_μνT^{μν} with conserved T;
  - the gain is P-r13b, F = e^{−k²ℓ²/2}(1 − 4iωτ)(1 − iωτ)^{−4}, the same scalar for every component, with τ = ℓ/c (strict) or τ_c.
- **H2.** Per frame mode and channel c, the trade-off P_J^c D₀^c ≥ |F|²/4 (ħ units, Lemma T form), with the least-decoherence split unless stated.
- **H3′ (start, corrected in §3.3).** At t₀ the meters are in vacuum, the TT metric and its rate are zero, and the record carries the initial-memory term B[T^{0ν}(t₀)].
- **H4.** The Isaacson premise for TT energy. Premise (iii), that non-radiative (constraint-channel) metric noise gravitates through its static field energy, is stated separately wherever it is used.
- **Excluded realizations:** GW friction (E2); non-Gaussian and jump records; nonlinear completions (Bianchi holds here at linear order only); dynamical frames.

## 3. The assembly

### 3.1 Lemma A: channel decomposition for conserved sources (proved; checked out:1-7)

Take p = (ω, 0, 0, k) and conserved T (p_μT^{μν} = 0). The free data are:
- ρ = T^{00} (S);
- T^{0a}, a ∈ {x, y} (V, 2 components);
- T^{ab} = TT (2) plus the transverse trace T_⊥ (S).

The rest is determined: T^{z0} = (ω/k)ρ, T^{za} = (ω/k)T^{0a}, T^{zz} = (ω/k)²ρ.

The Lorenz-gauge exchange 16πG[T′·T − ½T′T]/(k² − ω²) equals exactly

  16πG { T′^{TT}:T^{TT}/(k² − ω²) − 2T′^{0a}T^{0a}/k² + ½ρ′ρ(k² − ω²)/k⁴ + ½(ρ′T_⊥ + T′_⊥ρ)/k² }

(200 random pairs, relative error 3.2e-15, out:2).

- **Only TT has the cone pole.** The V and S blocks are instantaneous: finite at ω → ck (out:5).
- The S block is **indefinite** (det = −1/4k⁴). This is the comparator's DeWitt indefiniteness (`OWD:615-621`).

**Consequence (proved, given Theorem U's class, `TESTS:4521`).** Theorem U and Lemma C need a massless 1/s pole in the metric response. They therefore bind only the two TT polarizations.
- With least-decoherence noise the S and V channels have locally finite D₀ and metric covariance (K_c = |F|²|G_c|/ħ, G_c ∝ 1/k²). They may be stationary.
- **The start time (P-r11a) is needed by the TT channel alone.**

### 3.2 The explicit model

- **TT (2 polarizations).**
  - S_int = Σ_λ h_λT_λ, with h^{TT}_ij = Σh_λe^λ_ij, e:e = 2 and T_λ = ½e^λ:T. The response is g = 16πG/(c⁴s).
  - Least decoherence gives the floor K_TT = 16πG|F|²/(ħc⁴|s|) and the metric noise S_h,λ = 8πGħ|F|²e(s)/(c²|Ω² − ω²|) (Ω = ck).
  - Realization: R13-6's single-port meter per polarization, gain √2FĤ e_+^{−1}, post-filter R = F/g. So h_λ = √(8πGħ/c²)·(f ⋆ J₀(Ω·)) ⋆ ξ (proved, as `R13-6:170-197`, with GR's TT normalization).
  - ξ^{TT}_ij is spatial, transverse and traceless, so ∂_μξ^{μν} = 0 identically. It enters no constraint.
- **V (2 components).** Response 32πG/(c⁴k²) per component. Least-decoherence imprecision ∝ k² and white up to the gain cutoff. Instantaneous gravitomagnetic potential.
- **S (ρ, T_⊥).**
  - The ρρ floor 4πG|k² − ω²/c²|/(ħc⁴k⁴) is attained at any chosen ω with **anticorrelated** pressure-record noise (P_ρ⊥ = −P_⊥⊥g₁₂/g₁₁) and finite K_⊥⊥ (proved by Cauchy–Schwarz; checked out:83-85). At ω = 0 this is exactly R6-4's floor.
  - Enforcing it up to the cone makes K_⊥⊥ diverge there (out:85). An isotropic choice keeps K = O(G/ħk²) everywhere.
  - Choice used: the correlated optimum at |ω| ≪ ck, interpolated to the bounded choice near the cone (reading).
- **Lemma CU: one gain for all channels** (proved from Lemma A).
  - The record's mean field is E_F = F_TT·E_Lorenz + (F_V − F_TT)V/k² + (F_S − F_TT)S.
  - Each remainder is an instantaneous spatial kernel times a causal temporal filter. Its response to a changing source is nonzero outside the light cone, so it signals superluminally unless F_S = F_V = F_TT.
  - So the channel meters must all deliver the same F (R_c g_c = F). They do here.
  - Noise and decoherence may differ by channel, because they are independent of matter.
- **The gauge of the record (reading, P-r15b).** The metric record is held in the frame's Poisson gauge, or only gauge-invariant content is recorded.
  - In Lorenz gauge the S/V noise reappears as pure-gauge h̄ components with covariance ∝ S_ξ/s². That is non-integrable at the cone and grows secularly with a start (proved: G_R acting on non-vanishing S/V noise at s = 0).
  - In Poisson gauge, Φ, Ψ and S_i are instantaneous and stationary, and only h^{TT} grows (as ε ln t).
- **Locality (reading).** Channel-adapted meters couple to the projections Π^c(F·T). These are instantaneous Riesz-type, spatially non-local functionals.
  - The alternative is one local tensor meter with the TT spectral shape in every channel, projected on the record side (a classical post-filter).
  - That alternative gives S/V near-cone decoherence ∝ 1/|s|, R11-5's toy situation, with γ = ¼ at lab frequencies.
  - Either way the backaction is commuting (χ_FF = 0) and independent of matter. Matter's influence on matter goes only through the mean field, which is causal by Lemma CU (suggested; no-signalling not computed beyond this).

### 3.3 Bianchi compatibility with a finite start

**(a) Conserved S/V noise from t₀ (proved; checked out:9-15).**
- Set J^{00} = f ⋆_{t₀} ξ_ρ and J^{0a} = f ⋆_{t₀} ξ_a.
- The derived components are J^{z0} = (i/k)∂_tJ^{00} = (i/k) f′ ⋆ ξ_ρ, J^{zz} = −k^{−2} f″ ⋆ ξ_ρ, and J^{za} = (i/k) f′ ⋆ ξ_a.
- Conservation is exact if and only if f(0) = 0 and f′(0) = 0. The repaired gain f = e^{−x}x²(4 − x)/(2τ) has both (out:6).
- Checks:
  - J^{0ν}(t₀) = 0 (out:11);
  - finite-difference residual 1.3e-4 (discretization);
  - Var J^{zz} = ∫f″²/k⁴ (0.168 sampled vs 0.159).
- With f′(0) ≠ 0 (literal n = 2), J^{zz} carries white noise (Var 31 vs 0.08, out:12).
- So the constraints hold at t₀ with zero S/V noise, and every component has finite variance.

**(b) Lemma B: a finite-start defect of the mean field (proved; checked out:17-23).**
- For conserved matter present at t₀, the causal record J = f ⋆_{t₀} T has

  ∂_μJ^{μν}(t) = f(t − t₀)·T^{0ν}(t₀) ≠ 0

  (checked: defect 0.915 = prediction 0.915, out:18). So R13-6's H3 (`R13-6:148-151`) is not Bianchi-compatible for t − t₀ ~ τ.
- **Exact repair (proved):** add

  B^{00} = ψ(t − t₀)T^{00}(t₀) − Ψ₁(t − t₀)∂_iT^{0i}(t₀), B^{0i} = ψ(t − t₀)T^{0i}(t₀), B^{ij} = 0,

  with ψ(s) = ∫_s^∞ f and Ψ₁(s) = ∫_0^s ψ.
- J + B is exactly conserved (residual 3.6e-4, discretization; out:19). Also J^{0ν}(t₀⁺) = T^{0ν}(t₀), so the initial metric is the constraint solution for matter at t₀, not h = 0.
- **B decays to zero if and only if Ψ₁(∞) = ∫t f = 0**, the first moment. For the repaired gain Ψ₁(∞) = 7e-13 τ. For the literal n = 3 gain it is 3τ: a frozen spurious energy density 3τ·∂_tT^{00}(t₀) for ever (out:21).
- So P-r13b, introduced for Lemma D's drag, is also what makes a finite start Bianchi-clean.
- **Price P-r15a (named):** an initial-value record of T^{0ν}(t₀), a one-shot measurement at t₀ with its own imprecision and backaction (a one-time decoherence at t₀).

## 4. The tests

### 4.1 CP (proved; checked out:37-44)

- **Each channel.** The construction is R13-6 §3.6 per channel (`R13-6:281-292`): a unitary dilation, a Gaussian homodyne instrument, feedback controlled only by past records, and a partial trace. The correlated S block is a two-port Gaussian instrument (CP regardless; saturation of the matrix trade-off by a two-mode QND meter is suggested, comparator RECALLED). The record-side projection is classical post-processing.
- **The exact irrational TT limit** (closing `vR13-6:31`):
  - Approximants J₀_N(t) = N^{−1}Σcos(Ω cos θ_j t)e^{−Γt} (Gauss–Chebyshev nodes of the arcsine measure, Γ = 1/(NT)).
  - Their transfer functions are sums of positive-real terms, hence outer (min Re > 0 on Re p ≥ 0 in every sample, smallest 1.6e-5). So the post-filters F/g_N are causal.
  - With the gain, A_N(t, u) = (f ⋆ J₀_N)(t − u) converges to A in Hilbert–Schmidt norm on [t₀, t]. C_N = A_NA_N* → C in trace norm; the relative bound falls 2.4e-3 → 6.1e-4 → 1.5e-4 for N = 128, 512, 2048 (out:41-43).
  - Gaussian dephasing maps with trace-norm-convergent covariances converge pointwise. Pointwise limits of CP maps are CP.
- **Initial state.** The approximants' internal vacua contribute a bounded term (arcsine mass J₀(0) = 1), as in `R13-6:245`.
- **ḣ regularity (closing `vR13-6:27-31`; checked out:26-31).**
  - With F included, K = f ⋆ J₀ has K(0) = K′(0) = 0. So ḣ = K′ ⋆ ξ has no white-noise term.
  - Var ḣ grows as |F(Ω)|²/π per ln T (0.3551 vs 0.3548 predicted at Ωτ = 0.1; 0.3388 vs 0.3382 at Ωτ = 1).
  - The referee's term ξ − Ω(J₁ ⋆ ξ) belongs to the unfiltered kernel F = 1.

### 4.2 Bianchi

- **Proved at linear order:** §3.3 (noise exact; mean field exact with B).
- **Not covered:** covariant conservation ∇_μJ^{μν} = 0 at second order. In a nonlinear completion the noise acquires a correction ξ^{(2)} ~ −∂^{−1}(Γ_noise ξ) with nonzero mean. That is the interaction-energy term of §4.5 (suggested).

### 4.3 TT weights vs the assumed O(1) (proved; checked out:31-35, 47-48)

- Per polarization the secular ⟨ḣ_λ²⟩ = (8πGħ/c²)Ω|F|²ε(ln ΩT + c₁)/π, with c₁ = ln 8 + γ_E − 2 = 0.657 (out:31).
- With ρ_GW = (c²/32πG)⟨ḣ_ijḣ_ij⟩, e:e = 2 and two polarizations:

  **ρ_GW = (ħc/2π³)∫dk k³ε|F|²[ln(ckt) + c₁]**, against R11-5/R13-6's (2ħc/π³)∫dk k³ε|F|² ln(ckt) (`R11-5:187`; `r136_checks.py` [6]).

- The ratio is **¼ at leading log**, and 0.2524 numerically at L ≈ 76 (out:47-48).
- The quasi-static TT term (`R13-6:326-331`) has the same normalization, so it is also ×¼.
- The S/V channels contribute **no secular near-cone record content**: no 1/s pole.

### 4.4 PPN α₁, α₂ at second order (⟨h²⟩ checked; coefficient suggested)

- **First order.** As R13-6 (`R13-6:347`): the universal repaired gain gives no first-order frame displacement. The even part is ~ (wτ/r)², short-range, not of PPN form.
- **Second order in the noise.** The averaged metric shift has two structures (suggested; it needs the nonlinear completion):
  1. a homogeneous noise fluid at rest in the CMB frame, effect ~ (ρ_n/ρ_crit)(H₀r/c)²β = 1.6e-33·ρ_n/ρ_crit at 1 AU (out:80). Even at the strict-variant constraint energy (ρ_n ~ 1e19 ρ_Λ at 4e-10 m) this is ≲ 1e-14 ≪ 1.6e-9;
  2. a local dressing of the body's field ∝ ⟨h²⟩, with the noise covariance anisotropic at O(w²/c²) in the body frame.
- **⟨h²⟩ at t_H** (out:74-79): ⟨h_ijh_ij⟩_TT = 1.4e-49 (ℓ = 4e-10 m, strict) down to 2e-62 (cτ_c = 1.49e-3 m); ⟨φ²⟩_S ≤ 8e-59.
- So α₁, α₂ ≲ C·1.4e-49 against α̂₂ < 1.6e-9 and |α̂₁| ≲ 4e-5 (comparators via `R14-2:191`). The pass needs C < 1e40. A term growing as (r/ℓ)² would be the fluid term (1), which is bounded separately by ρ_n.
- **Label: passes, suggested** (the coefficient is not computed).

### 4.5 Budget

**(a) TT, Isaacson premise (checked).**
- **Strict τ = ℓ/c:** ε needed is 4.7e-16, 6.3e-11, 3.6e-8, 2.1e-5 at ℓ = 1e-8, 2e-7, 1e-6, 5e-6 m. That is ×3.82–3.87 looser than R13-6/R14-2's (`R13-6:315-320`; out:50-53).
- **τ_c variant (ε = 1), against R14-2's ceiling cτ_c ≤ 1.49e-3 m:**

| ℓ [m] | 4e-10 | 1e-9 | 2e-9 | 1e-8 | 1e-6 | 5e-6 |
|---|---|---|---|---|---|---|
| lower cτ_c, exact weight [m] | 1.53e-3 | 1.13e-3 | 8.9e-4 | 5.2e-4 | 1.40e-4 | 1.21e-4 |
| R14-2 (assumed weight; reproduced) | 2.43e-3 | 1.79e-3 | 1.42e-3 | 8.3e-4 | 2.09e-4 | 1.74e-4 |
| window factor to 1.49e-3 m | closed | 1.3 | 1.7 | 2.8 | 10.6 | 12.3 |

- **The TT-only window closes at ℓ ≈ 4.3e-10 m** (out:61), not at 1–2e-9 m (`R14-2:175`). This is a correction to R14-2's τ_c closure, inheriting its drag ceiling (smooth polytrope, suggested).

**(b) Constraint channels (S, V): a new term (magnitude checked; gravitating status = premise (iii)).**
- At the least-decoherence split, a channel with instantaneous response g/k² carries metric noise S_φ = ħg|F|²/(2k²). Its static field energy is then (proved)

  |u₁| = (1/2g)⟨|∇φ|²⟩ = (ħ/4)∫d³k dω/(2π)⁴|F|² = ħ I_F/(32π^{3/2}ℓ³τ),

  with I_F = 21/32 for the repaired gain (out:64-65).
- **It does not depend on G.** It is the record noise's own "zero-point" energy at scale ℓ and bandwidth 1/τ. It is stationary (no accumulation): the S/V channels are instantaneous with finite covariance.
- **Size** (out:66-69): |u₁|/ρ_Λ is

| ℓ [m] | strict | cτ_c = 1.49e-3 m (drag ceiling) |
|---|---|---|
| 4e-10 | 8.6e18 | 2.3e12 |
| 1e-8 | 2.2e13 | 1.5e8 |
| 1e-6 | 2.2e5 | 150 |
| 5e-6 | 350 | 1.2 |

- **Sign (suggested):** the S (attractive Newtonian) binding energy is negative. The V (gravitomagnetic, like currents repel) energy is positive. No cancellation is enforced, so the total is O(1–3)|u₁|.
- **Under premise (iii) the budget fails at least-decoherence** everywhere in the window, except within ×1.2 at ℓ = 5e-6 m in the τ_c variant.
- This is R6-4's H-cosmo (`TESTS:3415`; `R11-5:236`) made explicit for E1: bandwidth-limited by the gain, stationary, and computable.
- **The escape: R6-4's γ-trade** (record the S/V channels less precisely, P_J → γP_opt; matter kernel ×(γ + 1/γ)/2). With R6-4's allowed γ interpolated log-log (`R6-4:151-160`), the allowed region under premise (iii) is ℓ ≥ 4.5–5.5e-8 m (τ_c variant) and ℓ ≥ 2.2–2.6e-7 m (strict), for 1–3 channels (suggested; out:89-102).

**Combined (worker reading).**
- Premise (i), only free GWs gravitate: the TT budget passes for ℓ ∈ (≈4.3e-10, 5e-6] m with cτ_c ∈ [lower(ℓ), 1.49e-3] m.
- Premise (iii): ℓ ∈ [≈5e-8, 5e-6] m (τ_c variant, with γ_{S,V} ≤ γ_req(ℓ), out:93-100) or [≈2.5e-7, 5e-6] m (strict).
- These are search regions, not VIABLE: premise-dependent and partly suggested.

## 5. Prices (named, not adopted)

- **New: P-r15a.** An initial-value record of matter's energy-momentum density at t₀ (the term B). It is forced by Lemma B for any finite start with a gain of nonzero memory.
  - It is transient only with P-r13b.
  - *Axiom text:* Record (`AX:77-80`) is unaffected. The record-production gate (`AX:185`) gains an initial measurement at the time origin.
- **New: P-r15b (reading).** The metric record is gauge-fixed in the CMB frame's Poisson gauge, or records only gauge-invariant content. This rides on P-r1.
- **New, conditional on premise (iii): P-r15c.** Under-recorded constraint channels (γ_{S,V} ≪ 1), raising matter decoherence and heating by up to 1/γ. *Axiom text:* the same Admissibility/Record prices as R6-4 (iii) (`vR6-4:19`), with a channel-dependent record precision.
- **Lemma CU** is a constraint, not a price: a single gain for every channel.
- **Locality:** either channel-adapted meters with instantaneous non-local (Riesz) couplings, or a local tensor meter with near-cone S/V decoherence (reading).
- **Carried over:** P-r1, P-r11a (now needed by TT alone), P-r11b, P-r13a (per TT polarization), P-r13b, P-r13c or P-r9b′ (ε now ×3.8 looser), P-r3, P-r4, and R6-4 (iii)'s four-axiom prices (`R14-2:252-260`).

## 6. Strong words checked

- **"Exactly conserved":**
  - the noise for t ≥ t₀ at linear order, given f(0) = f′(0) = 0 (the n = 4 repaired gain; literal n ≥ 3 also has it);
  - the mean field only with B.
  - The finite-difference residuals (1e-4) are discretization (out:11, 19).
- **"Only TT has the cone pole":** linearized GR, conserved sources, CMB-frame decomposition. Exact identity, checked to 3e-15.
- **"Weight ¼":** least-decoherence split per polarization, Isaacson energy t₀₀ = (c²/32πG)⟨ḣḣ⟩, leading log. The constant c₁ makes it 0.2524 at L ≈ 76.
- **"CP in the exact limit":** at the level of Gaussian covariances on finite [t₀, t], via trace-norm convergence of positive-real approximants (checked to N = 2048). The quantum initial-state term is bounded, not computed in closed form.
- **"Independent of G" for |u₁|:** at the least-decoherence split only. Under the γ-trade it scales as γ.
- **"Budget fails under (iii)":** premise (iii) is not proved. It is the constraint-field analogue of the Isaacson premise that every E1/E2 budget already uses. The sign bookkeeping is suggested, and γ_min is interpolated from R6-4's table.
- **"PPN passes":** suggested (power counting), with ⟨h²⟩ checked.
- **"Not EXCLUDED":** the item's named EXCLUDED example is refuted constructively. No other inconsistency was found in ℰ₁₅.

## 7. What would decide it

1. **The gravitating status of constraint-channel record noise** (premise (iii)), from a nonlinear completion: GR with a covariantly conserved stochastic source. This is now the deciding budget question for set A's E1, and equally for E2, which has the same S/V channels.
2. **A referee** of Lemma B, of the weight ¼ and of |u₁|. If they hold, update the E1/E2 tables of R13-6 and R14-2.
3. **R6-4's γ-window** recomputed for channel-dependent γ, with the heating integral weighted at the gain bandwidth rather than interpolated.
4. **The second-order PPN coefficient** in a nonlinear completion (it is needed only to turn suggested into checked; the margin is ≥ 39 decades).

**Sources.**
- Via earlier referees or reports: double-pulsar drag ceiling (`R14-2:168-176`); α̂₁, α̂₂ (`R14-2:191`); R6-4's γ-window and margins (`R6-4:144-160`).
- Local untrusted text: OWD 2302.07283 (`OWD:601-621`).
- RECALLED:
  - the Bardeen/Poisson-gauge split of linearized GR (only h^{TT} radiative);
  - the Isaacson energy;
  - Gauss–Chebyshev quadrature for the arcsine measure;
  - positive-real functions have no zeros in Re p > 0;
  - ρ_crit, ρ_Λ and t_H as R11-5.
