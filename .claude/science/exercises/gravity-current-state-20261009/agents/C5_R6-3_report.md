# C5 R6-3: Lemma V. Count fluctuations of the Lorentz-random lattice, and lensing silence against Poisson-size Λ fluctuation

**Worker.** Claude Opus 5.5, the same family as the supervisor and the other C5 probes. **Not refereed.** It reports a SUB-VOLUME reading and a REFUTED clause, so the codex referee is required before anything is recorded. Run 2026-10-12, 14:19Z to about 15:20Z. No repository file was edited.

**Scratch.** `scratchpad/C5/R6-3/scripts/`:
- `r63_formfactor.py/.out`: closed-form Fourier transforms of the sharp diamond and the truncated past cone, checked against quadrature, plus phase-averaged tail forms. Also the shell integral J(M).
- `r63_Jtable.py/.out` and `r63_Jtable.npz`: J(M) for 10⁻³ ≤ |M| ≤ 10⁹, both signs. Also the Plancherel check and the asymptotics.
- `r63_siegel_dual.py/.out` and `r63_Cstar.npy`: Siegel shell densities C*_t of the reciprocal lattice, with a counting cross-check.
- `r63_variance.py/.out`: the exact Haar-average variance from the shell sum, from T = 6 to T = 5×10⁶⁰, compared with the R4-5 Monte Carlo.
- `r63_misc.py/.out`: four things.
  - A check of the bound in the proof.
  - The null-vector density of the isotropic Z⁴ (the counterexample).
  - Fits with and without a T⁴ term.
  - The Λ numbers.
- `r63_mc216.py` with `r63_mc_eta1.5.out` and `r63_mc_eta2.5.out`: my own diamond Monte Carlo at T = 54, 108, 216 and 432.
- `r63_mc432.py` with `r63_mc432_pooled.out`, and `r63_mc_diamond_tail.py` with `r63_mc_diamond_tail_T54.out`: extra T = 432 seeds, and the per-frame tail check.
- `r63_mc_cone.py`, `r63_mc_cone_tail.py`, `r63_cone_trim.py`, `r63_cone_frame_check.py`, each with its `.out`: past-cone checks (heavy tail, aligned/typical split, single-frame Parseval).

**Read.**
- `docs/MINIMAL_AXIOMS_2026-06-29.md`, in full.
- `TESTS.md`:
  - §Campaign C5 (2302–2320);
  - rounds 1–5 and their results (2321–3000);
  - Round 6, with R6-3 at 3106–3139;
  - E2/E3 and Lemma P (225–263).
- `agents/C5_S5_synthesis.md`: the R6-3 rows at 182, 235, 318–323 and 442–470.
- `agents/C5_R4-5_report.md`, `C5_R4-5_referee.md` §§4–6, and `C5_R4-5_referee_verdict.md`.
- R4-5 scripts: `r45_checks.py`, `r45_checks2.py/.out` and `r45_lattice_count.py`.
- `agents/C5_R4-1_report.md` §§1–3: Siegel C_m, the sampling, and the automorphic-mode mechanism.
- `scratchpad/C5/ref_R2-2/R2-2_referee.md` §§2–4: P-L′, cocompactness, reciprocal lattice and gap.
- `agents/C5_O5_synthesis.md:447-453` (O5 remark 1).

**Labels.**
- **proved:** a complete argument here (same family, unrefereed).
- **proved mod RECALLED:** complete except for a named standard theorem.
- **derived (asymptotic):** a leading-order computation that is not fully rigorous.
- **checked:** a numerical check in the scripts.
- **suggested:** argued only.
- **reading:** an interpretation.
- **comparator:** outside literature. "Verified" means checked by web search this run; "from memory" means not checked.

---

## 0. Verdict against the FIXED readings (`TESTS.md:3130-3135`)

### LRL count: SUB-VOLUME (worker reading; referee required)

**Sharp causal diamonds.** Var N(D_T) = O(T² ln T) is proved (§3, Theorem D).
- The exact Haar asymptotic is Var = 0.1665 T² ln T + O(T²). This is derived (asymptotic) and checked to T = 5×10⁶⁰.
- It reproduces R4-5's Monte Carlo at T = 13–108 within its error bars, and my own Monte Carlo at T = 216 (0.973 ± 0.046 against 0.980).
- At T = 432 the Monte Carlo is tail-limited: pooled about 1.25 ± 0.2, against 1.096.
- R4-5's apparent "T^2.2" is T² ln T.
- There is no T⁴ term. F = 0 exactly, by the bound.

**Truncated past cones** (flat spacelike base). Var N(P_T) = O(T³). The proof is a sketch at the same level as Theorem D. The exact Haar mean is 0.4847 T³ (checked).
- That mean is carried by rare frames, in which the base is Bragg-aligned with a timelike reciprocal vector within an angle of about 1/T. The per-frame distribution is heavy-tailed (checked).
- In typical frames the count variance is smaller (suggested: about T² ln T).

**Smoothed windows** w(x/T), w ∈ C_c^∞: Var = O(T⁻ⁿ) for every n (proved).

**DIVERGENT is not returned.** The shell sum converges for sharp diamonds (proved) and for past cones (sketch plus checked).

**Record proposed for the referee:** "everpresent-Λ magnitude excluded on LRL under the three premises" (R4-5's H1, H2, H4: unimodular conjugacy, count-volume bridge, Planck density).
- Under those premises, ΔΛ/Λ_obs ≈ 1.4×10³⁰ for the flat-based past cone (ensemble-mean variance).
- It is ≈ 1.4×10⁵⁹ for a diamond of equal 4-volume.
- The fluctuation is too large, not too small: a sharper volume means a less sharp Λ.

### (d) Trade-off lemma (derivation)

**As literally stated: REFUTED** (proved; referee required). The hypothesis is "no structure-factor support for 0 < |q²| < c", which allows null-cone support.
- **Counterexample:** the Lorentz-random isotropic lattice X = g(Z⁴ + u), with g Haar on SO⁺(1,3)/SO⁺(1,3;ℤ), a finite-volume, non-cocompact quotient.
- It is stationary, Lorentz-invariant in law and mean-ergodic, with finite local second moments.
- It has no reciprocal vectors with 0 < |q²| < (2π)².
- But it has null reciprocal vectors with Siegel density b = 0.0217, which gives **Var N(D_T) ≥ 0.042 T⁶**. That is super-volume (§5.2).

**Corrected statement: DERIVED** (proved, with the form-factor bound of §3; same family). Hypotheses:
- the gap includes the punctured null cone, i.e. Γ = 0 on {q ≠ 0 : |q²| < c}, which is exactly LRL's property (`TESTS.md:2716`);
- mean ergodicity (no extra atom at q = 0);
- finite local second moments.

Conclusions: Var N(D_T) = O(T² ln T), Var N(P_T) = O(T³), and smooth windows give O(T⁻ⁿ).

**Lensing silence in its strict sense: OPEN.** That is a gap only at spacelike and null q, which is all that 1→1 on-shell scattering sees.
- A volume law would then need timelike Bartlett weight accumulating at q² → 0⁻ (proved).
- No classical point process with that property was constructed or excluded.
- Partial results (proved):
  - thinning, Cox modulation and independent superposition always add white spacelike weight;
  - a finite-variance Lorentz-invariant random displacement field is constant.

### Against the expectation (`TESTS.md:3136-3139`)

- **Smooth windows:** SUB-VOLUME (DERIVED), as expected, and stronger: O(T^(−∞)).
- **Sharp windows:** SUB-VOLUME rather than "OPEN, leaning SUB-VOLUME". The growth is boundary-dominated: the waist for diamonds, the flat base for past cones.
- **(d):** split.
  - Literal: REFUTED, by null weight.
  - Two-sided gap: DERIVED.
  - One-sided (lensing) gap: open.

---

## 1. In plain words

**The Lorentz-random grid is far too regular to carry everpresent Λ.**
- Take the grid's points in a causal diamond of size T. Their number fluctuates only like T² ln T: like the area of the diamond's waist (the 2-sphere where the past and future light cones meet), not like its 4-volume T⁴.
- For a past light cone cut off by a flat "big bang" slice, the average fluctuation is like T³. That comes from the flat slice, and mostly from rare orientations in which the slice lines up with a row of grid planes.
- For smoothly weighted regions the fluctuation goes to zero.

**Under Sorkin's premises, a quieter count means a louder Λ.**
- A count that is too sharp pins the 4-volume too well, so Λ comes out 10³⁰ to 10⁵⁹ times too large.

**General version.**
- Any Lorentz-invariant random point pattern with no Fourier weight at small invariant momentum, including the light cone, has the same sub-volume behaviour.
- If null (light-cone) Fourier weight is allowed, the opposite happens: a Lorentz-random version of the ordinary 4D grid fluctuates like T⁶.
- Whether a pattern can be silent to light (no weight at spacelike and null momenta) yet carry a volume-law count through timelike weight alone is still open.

---

## 2. Setting, hypotheses, outside realizations

**(S1) LRL** (`C5_R2-2_referee.md:9`; `TESTS.md:2716`).
- X = g(L₇ + u), with L₇ = diag(√7,1,1,1)ℤ⁴ and ρ = 1/√7.
- (g, u) is Haar on ISO⁺(1,3)/(L₇ ⋊ Γ_L), with Γ_L cocompact.
- Reciprocal lattice: G = 2π diag(1/√7,1,1,1)m, with G² = c·t, c = (2π)²/7 and t = Q*(m) = −m₀² + 7|m⃗|². The form is ⟨−1,7,7,7⟩, anisotropic, so |t| ≥ 1 (`R2-2_referee.md:124-147`).

**(S2) Windows.**
- D_T: a causal diamond of proper height T.
- P_T = J⁻(0) ∩ {t′ ≥ −T}: a past cone cut by a flat spacelike slice of a frame. The slice is the flat-space proxy for the big-bang surface.
- Both are sharp. Smooth windows are w(x/T) with w ∈ C_c^∞.
- Frames are Haar-random relative to the lattice.

**(S3) Variance.** Var = E_g Var_u N, the variance over translations and frames. Since E_u N = ρ|W| for every g (Lorentz preserves volume), there is no between-frame term.

**(S4) Conventions.** The pairing is q·x = −ωt + k·x, and Ŵ(q) = ∫W e^{−iq·x}. The shell measure is μ_M = δ(q² − M)d⁴q, over both sheets for M < 0, with signature (−+++).

**Excluded outside realizations:**
- curved or FRW embeddings of LRL (R3-3: defects needed);
- per-realization (fixed-g) statements, except where noted;
- records on LRL sites. B′+ (Bernoulli inert records) is untouched: thinning restores the volume law (R4-5 §4.5, `TESTS.md:2939-2943`);
- quantum (non-commuting) counts;
- non-flat truncations of the past cone.

---

## 3. (a)–(b) Variance formula and shell asymptotics

### 3.1 Variance formula (proved mod RECALLED)

Parseval on the torus R⁴/gL₇ gives Var_u N(W) = ρ² Σ_{G≠0} |Ŵ(gG)|².

Averaging over g ∈ SO⁺(1,3)/Γ_L uses three ingredients:
- **Unfolding over each Γ_L-orbit.** Stabilizers are finite for timelike shells and lattices in SO⁺(1,2) for spacelike ones.
- **Finitely many orbits per shell.**
- **Siegel's formula with class number one.** This is RECALLED. The genus of ⟨−7,1,1,1⟩ has one class (`TESTS.md:2905`), hence so does its dual.

The result:

  **Var N(W_T) = ρ² Σ_{t≠0} C*_t ∫_{q²=ct} |Ŵ_T|² dμ = ρ² T⁶ Σ_{t≠0} C*_t J_W(c t T²),**

  where **J_W(M) = ∫_{q²=M} |Ŵ₁(q)|² dμ_M**.

The scaling used is Ŵ_T(q) = T⁴Ŵ₁(Tq) and μ_{ct}(q) = T⁻²μ_{ctT²}(p). Tonelli justifies exchanging the sum and the average.

**Shell densities.**
- Formula: C*_t = cρ*∏_p α_p(t), with ρ* = √7/(2π)⁴. For p ∤ 14t, α_p = 1 − χ(p)/p² with χ = (−7/·). α₂ and α₇ come from exact counts modulo p^r.
- Checks:
  - Direct counting of reciprocal vectors in the lattice frame (|m₀| ≤ 3000) agrees to within 0.5% on 15 shells, both signs (`r63_siegel_dual.out:6-21`).
  - The mean over |t| ≤ 60 is 9.64e-3, against cρ* = 9.57e-3.
  - Shells with t = 1, 2, −3, −5, … are empty, for local reasons.

This is S in the pre-registration's form: the Haar average of the Bragg combs is Σ_t (2π)⁴ρ²C*_t μ_{ct}.

### 3.2 Closed forms (proved; checked to 6e-7 against quadrature, `r63_formfactor.out:2-3`)

**Diamond D₁ = {|x| ≤ t ≤ 1 − |x|}.**

  |D̂₁(ω,k)| = (8π/(k|ω|))·|F|,  F = ½[G(k+ω) − G(k−ω)],  G(β) = ∫₀^{1/2} u cos(k/2 + β(u − ½)) du.

**Past cone P₁.**

  P̂₁ = (4π/(ikω))[∫₀¹ r sin(kr)e^{−iωr} dr − e^{−iω}(sin k − k cos k)/k²].

The second term is exactly the flat base: −e^{−iω}B̂₁(k)/(iω).

### 3.3 Theorem D (form-factor bound for the sharp diamond): proved, elementary

For |M| ≥ 64, **J_D(M) ≤ K (1 + ln|M|)/M²**, with an absolute K. Numerically K ≤ 1.7×10⁴ suffices (`r63_misc.out:3-10`).

**The proof** uses three elementary inequalities, then a split of the η-integral into three regions.

The inequalities:
- (i) **|G(β)| ≤ g(β) := min(1/8, 1/|β|).** Integrate by parts once: |G| ≤ 1/(2|β|) + 2/β².
- (ii) **|G′(β)| ≤ 2/β².** The weight u(u − ½) vanishes at both ends, so integrate by parts twice. Hence |D̂₁| ≤ 64π/k³ whenever |ω| ≤ k/2.
- (iii) **|D̂₁| ≤ (8π/(k|ω|))·½[g(k+ω) + g(|k−ω|)].** Checked on 2×10⁵ random points: the maximum ratio is 0.982 (`r63_misc.out:2`).

Parametrise:
- timelike: (ω,k) = √m(cosh η, sinh η), with weight 4πm sinh²η dη;
- spacelike: (ω,k) = √m(sinh η, cosh η), with weight 4πm cosh²η dη.

Note that k ± ω = √m e^{±η}. The three regions:
- **η ≤ 1.** Bound (iii) gives integrand ≤ 256π³/m². For spacelike shells, bound (ii) handles |ω| ≤ k/2.
- **1 ≤ η ≤ ½ ln m.** Here g(k−ω) ≤ e^η/√m, so the integrand is ≤ 1024π³/((1 − e⁻²)²m²) per unit η. This region produces the logarithm.
- **η ≥ ½ ln m** (the null region). Here g ≤ 1/8, so the integrand is ≤ C e^{−2η}/m. That integrates to O(1/m²).

So the slow decay along null directions (the pre-registration's worry) costs only O(1/m²). J_D(0) = 1.938 is finite (`r63_Jtable.out:4`). ∎

### 3.4 Exact asymptotics (derived (asymptotic) + checked)

**Diamond, both signs: J_D(M) = 16π³ ln|M|/M² + B/M².**
- Fitted A = 496.4 (timelike) and 493.4 (spacelike), against 16π³ = 496.1 (`r63_Jtable.out:36-37`). B ≈ −611.
- **Origin.** Phase-average the fast phase k/2. Then ⟨F²⟩ = |e^{iβ₋/2}P₊ + Q₊ − g_h(β₋)|²/8, with β₋ = k − ω. In the window 1 ≪ |β₋| ≪ √m, g_h ≈ e^{iβ₋/2}/(2iβ₋): this is the endpoint u = ½, i.e. the **waist 2-sphere**. That makes the integrand 32π³/m² per unit η over ½ ln m units.
- So the logarithm is the waist seen at all intermediate boosts. The null cones themselves contribute O(1/m²).

**Past cone.**
- Timelike: J_P(M) → (2π)³|B₁|/|M|^{3/2} = 1039.03/|M|^{3/2}. The value 1040.8 at |M| = 10⁸ comes from the base term, ∫d³k |B̂₁|²/ω³.
- Spacelike: J_P(M) ≈ 32π³ ln M/M². Fitted: 992.
- (`r63_Jtable.out:44-71`; `r63_variance.out:2-3`.)

**Plancherel checks.** ∫J dM = (2π)⁴|W| to 4e-4 (diamond) and 1.4e-4 (past cone).

### 3.5 Shell-sum convergence and the T-laws

Σ_t C*_t (1 + ln|t|)/t² and Σ_t C*_t/|t|^{3/2} converge, since C*_t = O(log log |t|). Hence:

| Window | Exact Haar variance (checked) | Bound |
|---|---|---|
| Sharp diamond D_T | **0.1665 T² ln T + O(T²)**. Var/T² = 0.505, 0.633, 0.749, 0.865, 0.980, 1.096 at T = 13, 27, 54, 108, 216, 432; 1.62 at 10⁴; 23.4 at 5×10⁶⁰ | O(T² ln T), proved |
| Past cone P_T (flat base) | **0.4847 T³** (0.566 at T = 13; 0.501 at 108) | O(T³), sketch |
| Smooth w(x/T) | O(T⁻ⁿ) for all n | proved: Ŵ is Schwartz and \|q\|_E ≥ √\|q²\| ≥ √c on every shell |

**Past-cone sketch.** The base piece gives a timelike bound of ≤ (2π)³|B₁||M|^{−3/2} exactly. For spacelike shells it gives ≤ 64π³|M|^{−3/2}, using h(r) = r(e^{−iωr} − e^{−iω})/ω, which vanishes at both ends, integrated by parts twice. The cone-surface piece is handled as in Theorem D.

**Fixed-width mollification of D_T** (suggested). The waist terms near the rest point survive, so Var stays at order T², with a smaller coefficient.

---

## 4. (c) Numerics

### 4.1 Diamonds

**Exact Haar shell sum against Monte Carlo** (Var/T²):

| T | Exact (`r63_variance.out:6-15`) | R4-5 MC, η_max 1.5 / 3.0 | Mine, η_max 1.5 | Mine, η_max 2.5 |
|---|---|---|---|---|
| 13 | 0.505 | 0.518 / 0.592 (±4%) | | |
| 27 | 0.633 | 0.646 / 0.631 | | |
| 54 | 0.749 | 0.719 / 0.778 | 0.792 ± 0.048 | 0.796 ± 0.044 |
| 108 | 0.865 | 0.880 / 0.825 | 0.803 ± 0.037 | 0.847 ± 0.034 |
| 216 | 0.980 | | 0.973 ± 0.046 | (stopped) |
| 432 | 1.096 | | 0.852 ± 0.089 (n = 250); 1.556 ± 0.318 (n = 330, three more seeds, `r63_mc432_pooled.out`). Pooled ≈ 1.25 ± 0.2 | |

**Notes on the Monte Carlo.**
- The bootstrap errors understate the true scatter at large T, because rare aligned frames create a tail. A per-frame tail check at T = 54 (`r63_mc_diamond_tail_T54.out`) gives:
  - mean 0.737 ± 0.018, against the exact 0.749;
  - median 0.669;
  - top 1% of frames carrying 6% of the mean.

  So the diamond mean is carried by typical frames.
- The η_max = 2.5 run was stopped at T = 216.

- The shell sum is the exact quotient-Haar average, modulo the RECALLED Siegel formula. **No sampling is involved.** This answers the referee's sampling objection (`C5_R4-5_referee.md:155-176`).
- The ball-averaged Monte Carlo agrees, so it did approximate the quotient average. That is consistent with equidistribution of large balls: Eskin–McMullen, comparator from memory.

**Fits** (`r63_misc.out` (3)). On the exact values for T ≤ 108:
- F + A/T² returns **F = 2.0e-3**. This reproduces the referee's "F ~ 1e-4–2e-3" (`C5_R4-5_referee_verdict.md:13`).
- F + (a + b ln T)/T² returns **F = −3e-5**.
- Over T ≤ 10⁴ the two forms give 6.8e-4 and −7e-6.

So the apparent volume term was the logarithm, and Theorem D makes F = 0 exact.

### 4.2 Past cones

- **The single-frame Parseval step is checked.** At η = 0.4 and T = 13, Monte Carlo gives Var_u = 135714 ± 1357, against a reciprocal sum of 133970 (R = 60, still rising slowly) (`r63_cone_frame_check.out`).
- That frame happens to be nearly aligned with the timelike reciprocal vector m = (7,1,0,0), at rapidity 0.397. So its Var/T³ = 62, against an ensemble mean of 0.57.

**The ensemble is heavy-tailed** (`r63_mc_cone_tail_T13.out`, `_T20.out`):

| T | Frames × shifts | Mean | Median | q99 | Max | Top 1% share of the mean |
|---|---|---|---|---|---|---|
| 13 | 6000 × 24 | 0.34 ± 0.06 | 0.109 | 1.90 | 243 | 58% |
| 20 | 4000 × 24 | 0.20 ± 0.03 | 0.080 | | 85 | 46% |

All values are Var_u/T³. The exact means are 0.566 and about 0.55.

- At η_max = 1.5 with one shift per frame (`r63_mc_cone_eta1.5.out`), Var/T³ = 0.165, 0.117, 0.24 ± 0.20 and 0.023 ± 0.011 at T = 27, 54, 108 and 216. In units of T² that is about 4.5, 6.3 and 5.1 at T = 27, 54 and 216. These are typical-frame values, consistent with order T² (ln T) growth (suggested).
- The Monte Carlo means fall short because the rarest, largest frames are undersampled. The bootstrap errors do not capture that.
- `r63_cone_trim.out` shows the mechanism. The share of the T³ coefficient from frames with a timelike reciprocal vector within |k| < K/T of the cone axis is 0.17, 0.37 and 0.42 (of 0.485) for K = 2, 4, 8. The remainder decays like 1/K.
- **Reading.** The T³ mean is a Bragg-alignment effect, with probability of order T⁻³ per frame. For the actual cosmic frame, typical-frame variance applies (suggested: of order T² ln T). The past-cone Monte Carlo is therefore **not a confirmation of 0.4847**; it is consistent in direction and in mechanism.

---

## 5. (d) The trade-off lemma

### 5.1 Corrected Lemma V′ (proved, given §3; same family, unrefereed)

**Hypotheses.** X is a stationary random measure on R^{1,3} with:
- an SO⁺(1,3)-invariant law;
- intensity ρ > 0;
- finite local second moments;
- Bartlett spectrum Γ with Γ({0}) = 0 (mean-ergodic);
- **Γ({q ≠ 0 : |q²| < c}) = 0**, a two-sided gap that includes the punctured null cone.

**Conclusion.** Var N(D_T) ≤ K T² ln T, Var N(P_T) ≤ K T³ (the latter given the §3.5 sketch), and Var N(w(·/T)) = O(T⁻ⁿ).

**Proof.**
1. **Parseval for indicators.** Var N(1_A) = (2π)⁻⁴ ∫|1̂_A|² dΓ for bounded A. Mollify with Gaussians: \hat φ_n ↑ 1 gives monotone convergence on the right. On the left, convergence is dominated, because E N(∂A) = 0 and N(A₁) is in L². (Proved.)
2. **Decomposition.** Restricted to q ≠ 0, Γ = ∫ν(dM)μ_M + b₊μ₀⁺ + b₋μ₀⁻, by uniqueness of invariant measures on Lorentz orbits (RECALLED). The gap gives b± = 0 and supp ν ⊂ {|M| ≥ c}.
3. **Linear growth.** Γ is translation-bounded: Γ(B(q,r)) ≤ E[N(|f|)²]/δ uniformly in q (standard; argument in the notes). Balls placed at the rest points of the hyperboloids, where μ_{M′}(B) ≳ r³/√|M|, give ν(|M| ≤ X) ≤ K₁(1 + X).
4. **Assemble.** Var ≤ (2π)⁻⁴T⁶∫ν(dM)K(1 + ln(|M|T²))/(M²T⁴) ≤ K′T² ln T · ∫(1 + ln|M|)M⁻²ν(dM). The integral is finite by step 3. ∎

**What this covers.** It is Lemma V of R4-5 (`C5_R4-5_report.md:195-202`), with the missing form-factor proof and shell-sum control supplied. It answers the referee's points in `C5_R4-5_referee.md:181-195`.

### 5.2 The literal (d) is REFUTED (proved; referee required)

**The counterexample: the Lorentz-random isotropic lattice.**
- Γ_Z = SO⁺(1,3) ∩ GL(4,ℤ) for the form −x₀² + x₁² + x₂² + x₃². It is an arithmetic lattice of finite covolume (Borel–Harish-Chandra; RECALLED) and non-cocompact.
- Non-null reciprocal vectors have |q²| ≥ (2π)².
- **Null vectors.**
  - #{n : n₁² + n₂² + n₃² = n₀², |n₀| ≤ X}/μ₀ = 0.866, 0.856, 0.859, 0.857 and 0.858 at X = 100, 200, 400, 800 and 1500.
  - So there is no logarithm, as Heath-Brown's quaternary asymptotic predicts for a non-square discriminant (comparator, verified).
  - Unfolding over the cusp stabilizers (lattices in E(2)) gives a finite Haar density, b = 0.0217 in q-units.
- **Variance.** Var N(D_T) ≥ b·J_D(0)·T⁶ = **0.042 T⁶** (`r63_misc.out:11-17`).
- **Second moments are finite.** The rest of the shell sum is O(T² ln T) by Theorem D. Equivalently, the cusp contributes E_g Var_u ~ ∫y·y⁻³dy < ∞.

**Reading.** Null Bragg weight produces super-volume growth: light-cone-aligned lattice planes enter and leave the diamond whole. The hypothesis must include the null cone. Lensing silence needs that anyway, since null transfer is collinear light scattering.

### 5.3 What lensing silence actually requires: OPEN

**What 1→1 on-shell scattering needs.** It needs transfer q = k′ − k with q² ≥ 0. So strict lensing silence is a gap on {0 ≤ q² < c, q ≠ 0} only. Timelike in-band weight is allowed.

**Proved.**
- From 5.1 step 4, a volume law (Var ≥ FρT⁴ along a sequence T → ∞) forces liminf_ε of T²∫_{|M|<ε}ν J(MT²) > 0 for every ε. That is weight accumulating at q² → 0. Under strict silence that weight is timelike.
- **Positivity rules out the soft constructions.**
  - Independent thinning gives S → p²S + p(1−p)ρ.
  - A Cox process gives S = ρ + ρ²σ.
  - Superposition adds spectra.

  Each puts white weight in the spacelike band. A silent process must cancel the self-term ρ there, which takes rigidity.
- **A stationary Lorentz-invariant random displacement field u with E|u|² < ∞ is a.s. constant.** Its spectral measure is a finite invariant measure, and every orbit other than {0} has infinite invariant measure. So "LRL plus a timelike-spectrum displacement" is not available as a pointwise construction.

**Not settled.** Whether a rigid classical process has a spacelike-and-null gap together with timelike weight of density ~dM at M → 0⁻.
- O5 remark 1 (`C5_O5_synthesis.md:447-453`) is the quantum analogue: a forward-cone spectral measure gives an exact volume law.
- N-Q′ (`TESTS.md:2711`) forbids such counts in a positive-energy vacuum, so that analogue is not a classical point process.

**Answer to "is there a general trade-off?"**
- **Yes** for two-sided gaps (LRL type): derived.
- **Not established** for strict lensing silence: open, with the constraints above.

---

## 6. (e) Λ size under R4-5's three premises (`TESTS.md:2939`)

**The premises:**
- H1: ΔΛ·ΔV ≈ κ_u ℓ̄_P², with κ_u = 1;
- H2: ΔV = √Var/ρ;
- H4: ρ = ℓ̄_P⁻⁴.

Scaling Poisson's 1.389 (refereed, `TESTS.md:2939`), with V_lc = 6.389×10²⁴² ℓ_P⁴ (`r63_misc.out` (4)):

| Region | T (lattice units) | Var/(ρV) | ΔΛ/Λ_obs |
|---|---|---|---|
| Past cone, flat base, ensemble-mean variance | 1.26×10⁶⁰ | 9.7×10⁻⁶¹ | **1.4×10³⁰** |
| Diamond of equal 4-volume | 2.13×10⁶⁰ | 1.0×10⁻¹¹⁸ | **1.4×10⁵⁹** |

- Typical cosmic frames (§4.2) and smoothed windows push ΔΛ higher still.
- **Epoch scaling.** ΔΛ ∝ T^{−3/2} (cone) or ∝ 1/(T√ln T) (diamond), against H² ∝ T⁻². So the "everpresent" tracking also fails. This confirms R4-5's suggested row at `C5_R4-5_report.md:124`.

**Reading, for the referee.** "Everpresent-Λ magnitude excluded on LRL **sites** under H1, H2 and H4." Three scope points:
- it excludes by being too large;
- it says nothing about ⟨Λ⟩ (R5-3);
- it does not touch B′+, inert Bernoulli records on LRL. There thinning restores the volume law; that is R4-5's surviving construction.

---

## 7. Prior art (each counted once)

- **R4-5 numerics and Lemma V** (`TESTS.md:2943`; `C5_R4-5_referee_verdict.md:13,15`).
  - Numerics reproduced exactly by the shell sum.
  - Lemma V proved in corrected form.
  - The referee's F-degeneracy explained.
- **P-L′** (`TESTS.md:2712`). Consistent: LRL's spacelike weight sits on shells with q² ≥ 3c.
- **R2-2 gap and null-free reciprocal lattice** (`TESTS.md:2716`). Used, and essential: §5.2 shows that the null condition is load-bearing.
- **O5 remark 1** (`C5_O5_synthesis.md:447`). Used as the quantum comparator in §5.3.
- **E2/E3 and Lemma P** (`TESTS.md:249-263`). Contrast: SL/AN-invariant laws are white (c ≥ 1), while Lorentz-invariant laws can be gapped. Nothing here contradicts Lemma P, because SO(1,3) is not SL(4).
- **Siegel densities** (`TESTS.md:2905`). R4-1's method is reused for the dual form ⟨−1,7,7,7⟩, which is new here. R4-1's automorphic-mode mechanism (`C5_R4-1_report.md:41-46`) concerns per-realization operators, not counts, so there is no overlap.
- **Docs grep.** No repository doc treats hyperuniformity of Lorentzian point sets. The "everpresent" hits are R4-5's only (`C5_R4-5_report.md:14`).

**Comparators.**
- Torquato–Stillinger, PRE 68, 041113 (2003). Window number variance and hyperuniformity; verified (search; abstract-level). The Euclidean surface law T^{d−1} is the analogue that the Lorentzian average turns into T² ln T.
- Bombelli–Henson–Sorkin, gr-qc/0605006. No equivariant frame map for sprinklings; verified (abstract). Not used load-bearing.
- Heath-Brown (1996), Crelle 481. Quaternary zero counts carry no logarithm for a non-square discriminant; verified (search snippet).
- From memory: Siegel's mean-value and Siegel–Weil; Borel–Harish-Chandra; Eskin–McMullen; Daley–Vere-Jones (Bartlett spectrum).

---

## 8. Strong-word check and points for the referee

1. **"Exact Haar average."** Exact modulo the RECALLED Siegel/unfolding formula. Class number one for the dual is inherited from L₇. Siegel densities are checked by counting to 0.5%.
2. **Theorem D constants.** K is not optimized. The η ≤ 1 spacelike region uses bound (ii). Small |M| < 64 shells are covered by finiteness: J_D ≤ 2.4 numerically, and an explicit bound follows from the same estimates.
3. **Past-cone bound.** It is a sketch, so it needs writing out. The T³ coefficient is a heavy-tailed ensemble mean (§4.2), which makes the Monte Carlo inconclusive on its own value.
4. **The §5.2 counterexample.** Check:
   - finiteness of the Haar density b for non-cocompact Γ_Z (unfolding at cusps, plus the Σn⁻² over multiples);
   - finite second moments;
   - that the literal (d) hypothesis admits null weight. As written it does (`TESTS.md:3125`).
5. **§5.1 step 3** (translation-bounded ⇒ ν grows linearly). The argument is sketched.
6. **"Excluded" in §6.** Conditional on H1, H2 and H4, which are themselves heuristics (`TESTS.md:2939`).

**Not done.**
- An FRW or curved past cone.
- A rigorous typical-frame (median) law for past cones.
- Strict lensing silence with timelike weight (open, §5.3).
- Per-realization statements.
