# C4 lane RL2: curved mean and physical variance of the three stable 6-layer operators (worker report)

**Worker:** Claude Opus 5.5 (probe RL2), the same model family as the exercise authors. **Unrefereed.** Worked 18:46–19:20Z on 2026-10-11. OMP_NUM_THREADS=2; every run under 8 minutes. No repository file was edited.

**Read in full:** `docs/MINIMAL_AXIOMS_2026-06-29.md`; TESTS.md "C4 results recorded 18:47Z" and "C4 sixth wave / Lane RL2" (plus the E1, E1′ settings and the header rules); `C4_RL1_report.md`, `C4_RL1_referee.md`, `C4_RL1_referee_full.md`; `C3_G-L_report.md`, `C3_G-L_referee.md`; `E1p_b_referee.md`; RL1 scripts B, C, F4b, F5, F6, G, I.

## Verdict (worker): INCONCLUSIVE, leaning FAIL (the noise clause is still not controlled; the mean clause now passes)

| operator (RL1_F4b row) | curved mean, needle order: (W_lens/W_flat)/√Δ as p→0 | noise: small-ε rate constant k (z_var ℓ_k = k√ε) | fixed-source MC / ladder rate | ℓ_k needed for ≤ 1 sd e-fold, 1 Gpc, source extent s = 1.2e4 m |
|---|---|---|---|---|
| op0 (row 0 ≡ row 3) | mid 1.0063 → fit 0.998; quarter 1.0048 → fit 0.999 | bare 2.84, node-only 2.73 | 0.68–0.91 (ε = 1 … ⅛) | 6.9e-19 m (bar 1e-19 m) |
| op1 (row 1 ≡ row 4) | mid 1.0061 → 0.998; quarter 1.0047 → 0.999 | bare 3.03, node-only 2.83 | 0.85–0.86 (ε = ¼) | 7.0e-19 m |
| op2 (row 2 ≡ row 5) | mid 1.0058 → 0.998; quarter 1.0046 → 0.999 | bare 3.33, node-only 3.25 | 0.84–0.98 (ε = ¼) | 7.2e-19 m |

(Mean column: the value at the smallest computed smearing, p = 2.5×10⁻⁴ ℓ⁻², then the free-intercept p → 0 fit. GR = 1; the one-hop link would give 0.486 (mid) / 0.543 (quarter).)

**Plain summary.**
- **Mean: yes, all three operators focus like GR.** I computed the average of the per-sprinkling inverse on the G-L lens exactly, in the needle (Penrose-limit) geometry that governs the cone at high density. Its magnification goes to GR's √Δ, not to the link's ν^{-1/2}. The error falls as the smearing in the cone-normal direction grows relative to ℓ: it is 14% at p = 0.03 ℓ⁻², 1.8% at 10⁻³ and 0.6% at 2.5×10⁻⁴. Fits extrapolate to 0.998–1.000. On the plane-wave reduction the answer is exactly density-independent, so this error is the only mismatch, and it vanishes in the continuum. The reason is exact and simple: the sum over chains carries the Van Vleck chain rule in its measure, which the single link does not.
- **Noise: still almost certainly too large, but not by the margin RL1 claimed, and still not controlled.**
  - The growth is in proper time, not distance. For a source of extent s at null distance D, the relevant proper time is √(2Ds), about 9×10¹⁴ m for 1 Gpc, not 3×10²⁵ m. This is exact, from Lorentz invariance in law.
  - With the ladder rate law, the bound needs ℓ_k ≳ 7×10⁻¹⁹ m (10 km source) to 8×10⁻¹⁸ m (100 s of emission), against the bar of 10⁻¹⁹ m. RL1 said 2×10⁻¹⁵ m.
  - At the bar, the noise is about e^{300}. It is bounded only out to about 10 kpc.
  - A fixed-source Monte Carlo at ε = 1, ½, ¼, ⅛ tracks the ladder rate at 0.7–0.9 of it, with no trend toward the cancellation a PASS would need. A PASS needs the true rate to be 300 times below the ladder law, or the ε-exponent to be ≥ 0.54 instead of ½.
  - But that law is still an extrapolation from ε ≥ 1/8 to ε ≈ 7×10⁻⁶⁴. The rule bars that, so the noise clause stays open.

## A. The curved mean (task 1)

### A.1 Reduction to a one-dimensional equation (derived here; exact on plane waves)

**Setting.** Plane wave ds² = −2du dv − xᵀK(u)x du² + dx², with y, x on the axis (Heisenberg isometries make this general for non-conjugate pairs). Write s = τ² = −2σ, Λ = u_x − u_y, and Δ(·,·), ν(·,·) for the Van Vleck determinant and G-L's needle factor of sub-segments.

1. **Measure.** In Brinkmann coordinates σ(y,z) and σ(z,x) are linear in v_z and quadratic in x_z, with matrices u·P_y and (Λ−u)·P_x. Eliminating v_z and integrating the ellipse in x_z gives
   d⁴z = 2π du dσ₁ dσ₂ / (Δu₁Δu₂ √det Q) = (2π/Λ)·g·du dσ₁ dσ₂, with g = √(Δ(y,x)/(Δ(y,z)Δ(z,x))).
   This uses G-L's refereed det Q = det J(Λ)/(det J det K). The region in (σ₁, σ₂) is exactly flat space's: σ₁, σ₂ ≤ 0 and Δu₂σ₁ + Δu₁σ₂ ≥ (Δu₁Δu₂/Λ)σ_yx.
   - **Check:** this reproduces V = (π/24)τ⁴⟨g⟩_w, and ⟨g⟩_w = ν. Numerically, for the A = 3 mid, A = 3 quarter and A = 1 lenses, the two independent formulas (sub-segment Van Vleck in affine u; G-L's ⟨Ω⁴⟩_w/⟨Ω²⟩² in flat t) agree to 3×10⁻¹⁴ (`rl2_F`).
2. **Mean inverse.** By the exact Palm identity (RL1, referee-confirmed), H̄(x,y) = h(u_y, u_x, s) solves H̄ = f̄ + ρ f̄ ∗ H̄ with f̄(z,x) = f(ρ(π/24)s₂²ν(u_z,u_x)) (G-L's volume law is exact on plane waves).
3. **Laplace in s.** The flat-form region is a triple convolution in the rescaled variables s₁Λ/u and s₂Λ/(Λ−u), so the Laplace transform factorizes. Writing k(Λ,q) = ĥ(Λ, p = q/Λ), the recursion closes at fixed q (with ρ = 1):

   k(Λ,q) = ν(0,Λ)^{-1/2} f̂(q/(Λ√ν(0,Λ))) + (π/2q) ∫₀^Λ du g(u;Λ) ν(u,Λ)^{-1/2} f̂(q/((Λ−u)√ν(u,Λ))) k(u,q),

   where f̂(p) = ∫e^{-ps} f(πs²/24) ds = −M₃p³/6 + ….

   This is a 1D Volterra equation in the affine parameter for each q.
4. **Density independence (PROVED).** The plane-wave homothety (u, v, x) → (u, λ²v, λx) maps a ρ-sprinkling to a λ⁻⁴ρ one. So the plane-wave answer depends on p only in units of ℓ⁻², and its p → 0 limit is exactly density-independent.
5. **Direct (δ(s)) coefficient:** W(y,x) = lim_{p→0} ĥ. The comparators are GR (scalar Hadamard; Huygens on plane waves, R = 0), giving W/W_flat = Δ^{1/2}, and the one-hop link, giving ν^{-1/2}.
6. **Needle order for the conformal lens (ARGUED).** For x in the cone layer of y, every chain lies in I(y,x), a needle of volume O(ℓ⁴). That needle sits exactly in the Penrose scaling (u ~ 1, x⊥ ~ ℓ, v ~ ℓ²). So the cone-layer mean inverse, at leading order in ℓ, is that of the ray's Penrose-limit plane wave. For the G-L conformal lens (Weyl = 0) that wave is isotropic. Its Δ, ν are G-L's exact needle-order values, which I used via u = ∫Ω²dt.
   - Finite-ℓ corrections beyond the Penrose limit (O(ℓ/w) or smaller) were **not computed**.

### A.2 Operators (CHECKED; `rl2_core`)

**Renormalization.** The three distinct stable operators are RL1_F4b rows 0, 1, 2; rows 3–5 are their antipodal duplicates, as the referee noted. Each was renormalized so that the 4D symbol has f̃(0) = (π/2)∫s ln s f ds = 1 exactly.
- RL1 normalized at z = 10⁻³. That left f̃(0) − 1 ≈ 5×10⁻⁷, a tiny mass term.
- The correction factor is 0.9999995.

**c₂ coefficient.** The symbol is S(z) = f̃ − 1 = −c₂z² + O(z⁴ ln z), with c₂ = −(π/16)∫s² ln s f ds.
- Check: for BD this gives c₂ = 0.612372 = √6/4 (exact); the direct symbol gives 0.608 at z = 0.05.
- For op0, op1, op2: c₂ = 0.6922, 0.6609, 0.6311. So the flat targets are W = 1/(2πc₂) = 0.22993, 0.24083, 0.25218.
- **Correction to RL1 F5:** it compared its W(τ) to BD's 0.25990, which is the wrong target for these operators.

### A.3 Flat check (CHECKED; `rl2_A_flat.out`)

Solving the 1D Volterra equation with the flat geometry gives ĥ₀(p):
- op0: 0.3226 (p = 1), 0.2559 (0.1), 0.2329 (0.01), 0.2304 (0.005, grid q/40).
- This approaches 1/(2πc₂) = 0.2299, which comes from the 4D symbol and is independent of the reduction. Same for op1 and op2.
- Absolute grid error grows as p falls (≈ 2% at p = 0.005 with step q/20; ≈ 0.6% with q/40). It is common-mode, and it cancels in lens/flat ratios to < 4×10⁻⁴ (q/10 against q/20).

### A.4 Lens results (CHECKED; `rl2_A_*.out`, `rl2_E`)

**Lens and comparators.** Conformal lens A = 3, w = 10, R = 100, with u_obs = 153.17:
- GR √Δ = 1.5317 (mid) and 1.5272 (quarter);
- link ν^{-1/2} = 0.7440 and 0.8286;
- G-L link/GR = 0.4857 and 0.5426, reproduced.

**Ratio M(p) = (ĥ_lens/ĥ_flat)/√Δ, Richardson in the grid:**

| p (ℓ⁻²) | 0.03 | 0.01 | 0.005 | 0.002 | 0.001 | 5e-4 † | 2.5e-4 † |
|---|---|---|---|---|---|---|---|
| mid, op0 / op1 / op2 | 1.1416 / 1.1388 / 1.1361 | 1.0832 / 1.0811 / 1.0789 | 1.0548 / 1.0533 / 1.0517 | 1.0296 / 1.0287 / 1.0278 | 1.0178 / 1.0173 / 1.0167 | 1.0108 / 1.0105 / 1.0102 | 1.0063 / 1.0061 / 1.0058 |
| quarter, op0 / op1 / op2 | 1.0738 / 1.0730 / 1.0723 | 1.0506 / 1.0495 / 1.0484 | 1.0351 / 1.0342 / 1.0333 | 1.0200 / 1.0194 / 1.0188 | 1.0125 / 1.0121 / 1.0117 | 1.0079 / 1.0076 / 1.0074 | 1.0048 / 1.0047 / 1.0046 |

- The mean magnification is GR's, not the link's: at p = 0.001 it is 1.559 (mid) against GR 1.532 and link 0.744.
- † Grid q/10 only. The lens/flat ratio is grid-insensitive (q/10 vs q/20: 4×10⁻⁴ at p = 10⁻³), but the absolute flat value at these p is off by more than 50% (a discrete kernel mass defect compounding over ~1/p renewals). The ratio rests on common-mode cancellation: the lens and flat runs use the same number of steps and renewals. **Checked:** at p = 5×10⁻⁴, q/20 gives 1.01059 / 1.01026 / 1.00992 against q/10's 1.01083 / 1.01051 / 1.01018 (mid). The ratio moved by 2.4×10⁻⁴ while the absolute flat value moved from 0.088 to 0.181 (`rl2_A_mid_tinyp_q20.out`).
- The excess M − 1 falls with local log-slope 0.34–0.48 at large p, rising to 0.71–0.80 at the smallest p.
- Free-intercept fits over the four smallest p (M₀ + a√p + bp; M₀ + a p^α; M₀ + a√p + b p ln p) give M₀ = 0.998 (mid) and 0.999 (quarter), with fit spread ±0.001, for all three operators. With only the Richardson points (p ≥ 10⁻³) the same fits give 0.990–0.992.
- So M₀ = 1 holds to about 0.2–1%, depending on whether the q/10 points are accepted, and the analytic argument (A.5) gives exactly 1.

### A.5 Why the mean focuses as √Δ (PROVED identity; limit ARGUED)

**The identity.** The Van Vleck chain rule g(u;Λ)·Δ^{1/2}(0,u) = Δ^{1/2}(0,Λ)/Δ^{1/2}(u,Λ) is exact and checked in `rl2_F`. It implies that k = Δ^{1/2}(y,x)·κ exactly, where κ obeys the **flat-form** equation with only two changes:
- its kernel carries the *last hop's* factor (Δν)^{-1/2}(u,Λ), with ν in the f̂ argument;
- its source term is divided by Δ^{1/2}, which is O(p³).

**The limit.** As p → 0 the kernel concentrates on last hops of affine length ~q = pΛ, where Δν − 1 = O(R_kk q²). The kernel's long tail ~ (q/w)³/q adds O(q² ln(Λ/q)) per renewal, over ~Λ/q renewals. So κ → κ_flat, and the magnification → Δ^{1/2}, with a correction of order R_kk Λ² p ln(1/p). The limit interchange is ARGUED.

**Why links differ.** The one-hop link has no chain measure and therefore no g factor. That is why it keeps ν^{-1/2}.

**Tiny-p check.** At p = 5×10⁻⁴ and 2.5×10⁻⁴ the excess keeps falling (A.4). Its local slope approaches 0.7–0.8, consistent with a p ln(1/p) leading term setting in.

### A.6 Scope of the mean result
- Scalar, retarded, the flat-normalized mean of the realization inverse (exact Palm identity). Lens: the G-L conformal lens at mid and quarter, at needle order (Penrose limit). Pre-caustic.
- **Not done:**
  - finite-ℓ corrections beyond the Penrose limit in the actual conformal lens;
  - stability of the mean inverse on curved backgrounds beyond what the plane-wave Volterra solution shows (it stayed bounded and smooth for all p run);
  - BD (its flat mean is unstable);
  - tensor and tails.

## B. The physical variance (task 2)

### B.1 The growth variable is proper time (PROVED from exact Poincaré invariance in law)

**Statement.** The sprinkling law is Poincaré invariant (E1, exact). So E[φ(x)φ(x)] for φ = Σ H(x,y)J(y) is a double integral over source points of a covariance kernel that depends only on the invariants of (x, y, y′).
- For a source of rest-frame extent s at null distance D, every source event y ≺ x has τ(y,x)² ≤ (δ + 2s)(2D + δ) ≲ 6Ds. I write τ_max = √(2Ds) below; the O(1) factor moves ℓ_k by at most 6^{1/6} = 1.35.
- So any growth law e^{zτ} of the kernel gives at most e^{z√(2Ds)} for the field, not e^{zD}.
- Why this holds:
  - E[H(x,y)²] is a function of τ(y,x) alone.
  - Cauchy–Schwarz gives |E[H(x,y)H(x,y′)]| ≤ √(E H(x,y)² · E H(x,y′)²).
  - Hence, by Mecke, Var φ ≤ E φ² ≤ (ρ∫|J| √(E H²) dy)² + ρ∫J² E H² dy. Both terms are controlled by the largest τ in the source.

**Consequence for RL1.** RL1 (§4.5, `RL1_I`) used τ = D = 1 Gpc. That overstated the e-fold count by a factor D/√(2Ds) ≈ 3.5×10¹⁰ for s = 1.2×10⁴ m, the E1′-b source scale, s/D = 4×10⁻²². This changes the required ℓ_k from 2.25×10⁻¹⁵ m to 6.9×10⁻¹⁹ m.

### B.2 Rate law at small ε: two ladders (CHECKED numerically; exponent SUGGESTED)

**Bare shared-path ladder (RL1; rung ε²E[g_ε(n)²]).** Small-ε law z_var ℓ_k = √(4πI₁ε):

| operator | I₁ | k = √(4πI₁) |
|---|---|---|
| op0 | 0.644 | 2.84 |
| op1 | 0.730 | 3.03 (new: RL1 F5 analysed rows 0, 3, 5, i.e. two distinct operators) |
| op2 | 0.885 | 3.33 |

The exact ladder root over the law is 1.75 → 1.22 → 1.07 → 0.97 for ε = 1, ¼, ⅛, 0.01 (`rl2_C`).

**Exact chaos structure.** Var φ = Σₖ (1/k!)ρᵏ ∫ (E Dᵏφ)², every term ≥ 0 (Last–Penrose). For chain-ordered insertions, the amplitude is a product of mean inverses H̄ (a node insertion) and interval-count derivative weights ε²f′ (an interior insertion).
- **Node-only renormalized ladder (rung ρH̄² = ερ_k h_k²).** k_h = √(4π∫τ h_k² dτ) = 2.73, 2.83, 3.25, within 4–7% of the bare constants (`rl2_C`; h_k from RL1's Volterra, τ ≤ 16).
- **Scaling (SUGGESTED, not proved).** In the limit ε → 0 at fixed √ε τ/ℓ_k, node and interior insertions each cost O(ε) per rung and carry the hyperboloid factor 1/z². So z ∝ √ε/ℓ_k with an O(1) constant, unless the node and interior amplitudes cancel pointwise.
- **Not bounds.** Neither ladder is a bound. The node and interior amplitudes add inside each chaos term before squaring.

### B.3 Fixed-source Monte Carlo at ε < 1 (CHECKED; `rl2_B_*`, `rl2_D`)

**Setup.**
- op0, ε-smeared weights εg_ε(n) (exact binomial thinning), ℓ_k = 1, ρ = 1/ε.
- Observer at the top tip of the diamond. A FIXED Gaussian source (width 0.4ℓ_k, centred at (0.8,0,0,0)) that does not scale with T. T = 3–9.
- The mean operator is ε-independent in ℓ_k units (exact), so the rates are directly comparable across ε.

| ε | MC sd rate of φ (per ℓ_k of proper time; last 4 / last 3 T) | bare-ladder sd prediction | MC / ladder |
|---|---|---|---|
| 1 | 2.03 / 1.93 | 2.49 | 0.82 / 0.78 |
| 0.5 | 1.30 / 1.34 | 1.47 | 0.88 / 0.91 |
| 0.25 | 0.68 / 0.59 | 0.87 | 0.79 / 0.68 |
| 0.125 | 0.40 / 0.42 | 0.54 | 0.75 / 0.79 |
| 0.25, op1 | 0.78 / 0.77 | 0.90 | 0.86 / 0.85 |
| 0.25, op2 | 0.80 / 0.93 | 0.95 | 0.84 / 0.98 |

- The fixed-source field grows exponentially at every ε, at 0.7–0.9 of the ladder rate. There is no trend in the ratio over a factor 8 in ε.
- Samples are small (R = 20–300) and heavy-tailed, and ε = 0.125 is the least asymptotic. These are rates, not bounds.

### B.4 Physical translation (`rl2_D`; ℓ = ℓ_P, D = 1 Gpc)

**Formula.** sd e-folds n = k ℓ_P² τ/(2ℓ_k³), with τ = √(2Ds + s²). Bounded (n ≤ 1) needs ℓ_k ≥ (kℓ_P²τ/2)^{1/3}. Values for k = 2.84 (other operators within 2%):

| s | τ | n at ℓ_k = 1e-19 m | ℓ_k needed |
|---|---|---|---|
| RL1 (τ = D) | 3.1e25 m | 1.1e13 | 2.25e-15 m |
| 1.2e4 m (E1′-b source scale) | 8.7e14 m | 3.2e2 | 6.9e-19 m |
| 3e6 m (one 100 Hz cycle) | 1.4e16 m | 5.1e3 | 1.7e-18 m |
| 3e10 m (100 s of emission) | 1.4e18 m | 5.1e5 | 8.0e-18 m |

- At the bar, noise stays ≤ 1 sd e-fold only for τ ≤ 2.7×10¹² m, i.e. D ≤ 3×10²⁰ m ≈ 10 kpc for s = 1.2×10⁴ m.
- **For PASS at the bar,** the true small-ε constant k_true would need to be ≤ k/323. Equivalently, the asymptotic rate would need to scale as ε^{α} with α ≥ 0.54 instead of ½: ε^{0.04} ≈ 1/323 at ε = 6.8×10⁻⁶⁴.

### B.5 What is and is not controlled
- **Controlled:**
  - the growth variable (B.1);
  - the ladder constants (B.2);
  - the MC rates over ε ∈ [⅛, 1] with a fixed source (B.3).
- **Not controlled:**
  - the variance law at ε ~ 10⁻⁶⁴. The exponent ½ is a scaling argument, and the constant comes from ladders that are not bounds.
  - The margin is now thin in exponent space (Δα ≈ 0.04), so no extrapolation from accessible ε can settle it. Only a theorem can: a lower bound on Var with the hyperboloid factor, for example a chaos-term lower bound that keeps both node and interior amplitudes.

## C. Against the FIXED readings

- **PASS:** "≥ 1 stable operator has mean magnification → √Δ with density-independent mismatch → 0, and noise bounded at physical parameters (ℓ_k ≤ 1e-19 m over 1 Gpc)."
  - The mean half holds for all three. Needle order: CHECKED to about 0.2–1% by extrapolation; PROVED-identity plus ARGUED limit.
  - The noise half is not shown. All evidence says unbounded: e^{~300} at the bar for a 10 km source, more for longer emission.
  - PASS is not met.
- **FAIL:** "each operator: O(1) mean mismatch, or unbounded noise at physical parameters."
  - The mean does not fail.
  - Unbounded noise rests on the small-ε law, which is extrapolated over 63 decades in ε. TESTS.md:5–9 ("No verdict rests on long extrapolation") bars it.
  - FAIL is not established.
- **Worker reading: INCONCLUSIVE, leaning FAIL.**
  - RL1 left the mean open and the noise open. RL2 closes the mean (passes) and narrows the noise.
  - The exclusion margin shrinks from 4 decades in ℓ_k (RL1) to 0.8–1.9 decades (RL2), because the growth variable is proper time.
- **Against the supervisor's expectation:**
  - "Mean passes" is confirmed, by computation rather than by the locality argument.
  - "Noise fails at 1e-19 m" is supported, with a smaller margin than RL1's.
  - "INCONCLUSIVE if small-ε variance cannot be controlled" is what obtains.

## D. Flags for the referee
1. The 1D reduction (A.1) is new. Check the measure 2π g/Λ and the closure at fixed q = pΛ. The flat limit reproduces the 4D-symbol value 1/(2πc₂), and ⟨g⟩_w = ν to 10⁻¹⁴.
2. The Penrose-limit claim (A.1, item 6) is the step that transfers the plane-wave result to the conformal lens at needle order. Finite-ℓ lens corrections were not computed.
3. With p ≥ 10⁻³ only, the fitted intercepts are 0.990–0.992. Adding the q/10 points at 5×10⁻⁴ and 2.5×10⁻⁴ brings them to 0.998–1.000. Those points rely on common-mode cancellation of a large absolute grid error (A.4 †); the grid check at p = 5×10⁻⁴ (q/20 against q/10) moves the ratio by only 2.4×10⁻⁴. A better quadrature (exact kernel mass per step) would remove the caveat entirely.
4. B.1 changes RL1's translation materially. It applies to RL1's arithmetic as well (`RL1_I`).
5. The MC uses the tip-to-tip diamond and a timelike observer. By B.1 that is the invariant content of a null-separated fixed source, but the mean there is the small tail, so I report rates, not relative noise.
6. The node-only ladder uses RL1's Volterra h_k (τ ≤ 16), whose tail accuracy was questioned (RL1 F6). I_h is dominated by τ ≤ 5, so this matters little.

## Files (scratch: `/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C4/RL2/`)

| script | output | content |
|---|---|---|
| `rl2_core.py` | `rl2_core.out` | operators (renormalized), c₂, f̂ tables, BD check |
| `rl2_A_planewave_mean.py` | `rl2_A_flat.out`, `rl2_A_mid.out`, `rl2_A_quarter.out`, `*_smallp.out`, `*_tinyp.out`, `rl2_A_mid_tinyp_q20.out` | 1D Volterra for the curved mean |
| `rl2_E_extrapolate_mean.py` | `rl2_E_extrapolate_mean.out` | p → 0 fits |
| `rl2_F_measure_check.py` | `rl2_F_measure_check.out` | ⟨g⟩_w = ν check |
| `rl2_B_smeared_mc.py` | `rl2_B_op0_eps{1,0.5,0.25,0.125}.out`, `rl2_B_op{1,2}_eps0.25.out` | fixed-source smeared MC |
| `rl2_C_ladder_rates.py` | `rl2_C_ladder_rates.out` | bare and node ladder constants, all three operators |
| `rl2_D_rates_and_translation.py` | `rl2_D_rates_and_translation.out` | MC rate fits; proper-time translation |
