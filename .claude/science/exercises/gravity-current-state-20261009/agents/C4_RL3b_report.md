# C4 lane RL3, probe RL3b: exact second-moment renewal for the stable layer inverses, and its small-ε root (worker report)

**Worker:** Claude Opus 5.5 (probe RL3b), the same model family as the exercise authors. **Unrefereed.** Worked 19:40–20:20Z on 2026-10-11. OMP_NUM_THREADS=2; every run under 9 minutes. No repository file was edited. I did not read the parallel RL3 probe's files, so the two methods stay independent.

**Read in full:** `docs/MINIMAL_AXIOMS_2026-06-29.md`; TESTS.md lines 1–12, "C4 sixth wave", "C4 ninth wave / Lane RL3" (fixed readings) and "C4 results recorded 19:41Z"; `C4_RL2_report.md`, `C4_RL2_referee.md`, `C4_RL2_referee_full.md`; `C3_LemmaL_referee.md`; `E1_referee.md`; the S1 lines of `supervisor_thread.md`; RL2 scripts `rl2_core`, `rl2_B`, `rl2_C`, `rl2_D`; RL1's Volterra solver.

## Verdict (worker): INCONCLUSIVE, leaning FAIL much more strongly than RL2

The exponent is now derived, not extrapolated. The FAIL is held back by one uniform bound and one source-transfer step, both stated in section 7.

| operator | I_h = ∫τ h² dτ (exact momentum identity) | k_h = √(4π I_h): variance rate γ ℓ_k = k_h √ε (1 + O(ε ln 1/ε)) | sd e-folds at the bar (D = 1 Gpc, s = 10 km) | ℓ_k needed for ≤ 1 sd e-fold |
|---|---|---|---|---|
| op0 | 0.595189 | 2.7348 | 281 | 6.6e-19 m |
| op1 | 0.639705 | 2.8353 | 291 | 6.6e-19 m |
| op2 | 0.842548 | 3.2539 | 334 | 6.9e-19 m |

**Plain summary.**
- **The second moment obeys an exact renewal equation (PROVED).** Cut each pair of chains at the points they share; the pieces in between are statistically independent. This gives M2 = K + ρ K∗M2 exactly. K is the sum over pairs of chains that share no interior point. Its part H̄² is exactly the positive "both copies pass through the same point" ladder. Everything else in K comes from the random interval counts: one copy's point sitting inside the other copy's hop, or two hops sharing counted points.
- **Only the shared-point rungs survive as ε → 0 (DERIVED; one uniform bound ARGUED).** The growth rate is the root of a characteristic equation. The large factor 1/z² that drives the growth comes from integrating over the infinite hyperboloid of boosts. That factor appears only when both copies leave from **the same point** and arrive at **the same point**.
  - If the endpoints are displaced by any nonzero Δ, the pair integral is O(1/(z|Δ⃗|)), not O(1/z²). This bound is PROVED in closed form and CHECKED numerically.
  - Interval-count (interior) insertions always displace the two copies, so they are suppressed by at least a power of z ~ √ε.
- **Result.**
  - The exponent is exactly ½.
  - The constant is the node ladder's k_h = √(4π∫τh²dτ). This is a convergent, ε-independent integral, evaluated here by an exact momentum-space identity with no tail truncation.
  - k_h is 4% below RL2's bare constant. The bare ladder is not the right leading term; the node ladder is.
- **Physical consequence.** At ℓ_k = 1e-19 m, a 10 km source at 1 Gpc gives 281–334 sd e-folds. A PASS would need the true constant to be 281 times smaller than derived, or the exponent to be ≥ 0.539. The derivation excludes both, provided the bound in section 7 holds.
- **MC check.** RL2's fixed-source MC rates at ε = 1 … ⅛ lie above the node-ladder root, and their ratio to it falls monotonically toward 1: 2.4, 2.1, 1.3, 1.1. The one correction I computed exactly (the same-hop count variance) is positive and scales as 7–8 ε at every ε. The MC is consistent with corrections that vanish as ε → 0.

## 1. Setting and the mean (from RL1/RL2, exact)

**Units and weights.**
- Units ℓ_k = 1, sprinkling density ρ = 1/ε.
- The weight is N(x,y) = ε g_ε(n(y,x)) for y ≺ x, where n is the count in the open interval and g_ε(n) = Σ_j C_j Bin(n,j) ε^j (1−ε)^{n−j}.
- G = (I−N)⁻¹ = I + H, with H(x,y) = Σ_chains Π N.

**Mean (Palm/Mecke, exact).** H̄ = εh, where h = f + f∗h is ε-independent and f(τ) = f_C(πτ⁴/24).

**A finite-difference identity used below (PROVED).**
- Adding m points inside a hop interval changes the weight by an m-th finite difference.
- Since g_ε(n) = E C(Bin(n,ε)) and Poisson thinning gives Poi(V), we get E_n[Δ^m g_ε(n)] = ε^m f^{(m)}(V) exactly, where f(V) = Σ C_j e^{−V} V^j/j!.

## 2. The exact equation for the second moment (PROVED)

**Theorem 1.** Let M2(x,y) = E_{x,y}[H(x,y)²] (Palm at x, y). Then

  **M2(x,y) = K(x,y) + ρ ∫_{I(y,x)} K(x,z) M2(z,y) d⁴z,**  

where K(x,y) = E Σ_{(c,c′)} w_c w_{c′}, summed over ordered pairs of chains from y to x with **no common interior vertex**. K and M2 depend only on τ(y,x).

**Proof.**
- Each pair (c,c′) has a unique set of common interior vertices z₁ ≺ … ≺ z_r. The order is the same in both chains, because both chains are causally ordered (Lemma L's argument).
- Apply multivariate Mecke to all distinct vertices. In segment i, every hop interval of either chain lies inside the open interval I(z_i, z_{i+1}).
- These segment intervals are pairwise disjoint. They contain no vertex of any other segment and no common vertex, because consecutive open intervals of an ordered chain are disjoint.
- So the weights in segment i depend only on η ∩ I(z_i, z_{i+1}) and on that segment's own private vertices. Poisson independence then factorizes the expectation over segments.
- Summing the private configurations segment by segment gives K(z_{i+1}, z_i), hence M2 = Σ_r ρ^r K^{∗(r+1)}. Poincaré invariance in law gives the τ-dependence. ∎

**The equation is closed.** No higher moment couples in. All the difficulty is moved into the explicit kernel K, which is itself an exact sum over interior-disjoint pairs.

**Decomposition (PROVED).** Write K = H̄² + K_c.
- **H̄² is exact.** The factorial moment measure of distinct Poisson points is a product measure, so the interior-disjoint pairs with independent weights give exactly (EH)².
- **K_c is the covariance part.** It contains exactly three effects:
  - (a) same-hop count variance: c = c′ = one hop, giving ε² Var g_ε. It is exactly computable.
  - (b) node–interior: a private vertex of one chain lies inside a hop interval of the other. This shifts the count by 1, a finite difference ε² f′ + ….
  - (c) interior–interior: two hops whose intervals overlap share Poisson counts. The leading covariance is ε³ f′f′ V(I∩I′).

**Which parts are ladder-like and positive.**
- The node–node rung ρ H̄² = ε h² ≥ 0 is the exact positive ladder.
- K_c is signed. It is the correction.
- For deterministic weights K_c ≡ 0 and Theorem 1 reduces to C3's Lemma L.

**Truncations.**
- K → H̄² is exact at leading order in ε for the rate (section 4). It is not a pointwise bound.
- Truncating the exact chaos series below is a lower bound at fixed (x,y).

**By-product: the exact chaos form (PROVED, Mecke plus the identity in section 1).**
- E D^k_{u₁…u_k} H(x,y) = ε^{1+k} A_k(x; u; y), with A_k ε-independent: a sum over node and interior placements of the u's, built from h and the derivatives f^{(m)}.
- Hence Var H(x,y) = ε² Σ_{k≥1} (ε^k/k!) ‖A_k‖², and every coefficient is nonnegative and ε-independent.
- So the whole ε-dependence is explicit. The exponent question reduces to the large-k, large-T growth of fixed functions. No ε-extrapolation enters.

## 3. Lorentz reduction and the characteristic equation (PROVED)

**Transform.** With the hyperboloid–Laplace transform F̂(z) = ∫_{J⁺} e^{−zt} F(τ) d⁴X = 4π ∫ τ³ F(τ) K₁(zτ)/(zτ) dτ, causal convolution becomes a product. So

  M̂2(z) = K̂(z)/(1 − Λ(z)),  Λ(z) := ρ K̂(z).

**Growth rate.**
- The growth rate γ(ε) of M2(τ) is the largest real root of **Λ(γ) = 1**.
- It is also the growth rate of Var = M2 − H̄², because h does not grow: the operators are stable.
- The rightmost zero is real for the positive leading kernel, and stays real under the small signed K_c.

**Leading part (PROVED).**
- Λ_node(z) = 4πε ∫ τ³ h² K₁(zτ)/(zτ) dτ = (4πε I_h / z²)[1 + O(z² ln(1/z))].
- This uses K₁(a)/a = a⁻² + ½ ln(a/2) + O(1) and ∫τ³h² < ∞.

**I_h by an exact momentum identity (PROVED identity; CHECKED; `rl3b_A`).**
- Parseval with e^{−zt} split across the two factors gives the exact expression; the 1/z² term comes from the pinch at large on-shell relative momenta. The result is

  **I_h = (1/16π⁴) ∫₀^∞ b db ∫_ℝ dσ |Φ(σ − ib)|²,  Φ = f̃/(1 − f̃),**

  with f̃ the 4D symbol continued off the real axis (the K₁ formula, principal √w).
- The integrand is ~ 1/(c₂²|w|²) near w = 0 and ~ 1/|w|⁴ at infinity, so the integral converges absolutely.
- **Test.** On h = e^{−τ⁴}, the identity reproduces √(π/8)/2 to 1.3e-6.
- **Values.** For op0, op1, op2: I_h = 0.595189, 0.639705, 0.842548.
- **Cross-checks.**
  - The position-space values at τ ≤ 16 (RL2) are 0.593730, 0.639439, 0.841831, consistent with a 0.03–0.25% tail beyond τ = 16.
  - min|1 − f̃|/min(|w|,1) = 0.05 on the lower-half-plane grid, so there are no zeros there (stability consistent).

## 4. Small-ε asymptotics of the root (DERIVED; one uniform bound ARGUED)

**Lemma D, the displaced pair propagator.** Define W(Δ;z) = ∫ d⁴X e^{−zt} h(X+Δ) h(X).
- **Exact axial reduction (PROVED).** With σ = τ²(X), the reduction is W = (π/2|Δ⃗|) ∫dt e^{−zt} ∫dσ h̃(σ) [Hc(s₀ + 2r|Δ⃗|) − Hc(s₀ − 2r|Δ⃗|)], where Hc = ∫h̃, s₀ = σ + 2tΔ⁰ + Δ², and r = √(t² − σ).
- **Bound.** Hence **|W(Δ;z)| ≤ π ‖h̃‖₁ sup|Hc| / (|Δ⃗| z)**, i.e. O(1/z), against 4πI_h/z² at Δ = 0. For timelike Δ, W = O(ln 1/z).
- **CHECKED (`rl3b_C`, op0).**
  - Δ = 0: z²W = 5.77, 6.69, 7.15, 7.34, 7.41 for z = 0.4 … 0.025, approaching 4πI_h = 7.46.
  - Δ = (0,1): z²W falls 0.041 → 0.002, while zW → 0.085. The predicted limit is (π/2)(∫h̃)² ≈ 0.083–0.092.
  - Δ = (0, 0.5), (0.5, 1) and null (1,1): zW bounded, z²W → 0.
  - Timelike: z²W → 0.

**Power counting for Λ_c.**
- **Every K_c term displaces the copies.**
  - (b) and (c) always leave the two copies at different points at the rung, because an interior point is strictly inside the hop interval.
  - The displacement co-moves with the incoming segment, which is a compact diamond in that segment's frame.
  - So the outgoing pair segment carries Lemma D's 1/(z|Δ⃗_lab|) with |Δ⃗_lab| ~ e^{η}. After the boost integral, an isolated non-node rung costs a relative factor O(z²) against a node rung (up to logs).
- **Order of each term.**
  - K_c with one correlation and coincident ends gives Λ_c ~ ε² ln(1/z)/z².
  - Term (a) is the same order.
  - Chains of m displaced rungs give O(ε^{1+m}/z^{m+1}).
  - At z ~ √ε, all of these are O(ε ln 1/ε) relative to the leading term.
- **Hence:**

  **γ(ε) ℓ_k = √(4π I_h ε) · [1 + O(ε ln 1/ε)],  α = ½ exactly,  c = k_h.**

**Status of the ingredients.**
- PROVED:
  - the exact equation (Theorem 1);
  - the leading term Λ_node;
  - I_h;
  - the single-segment bound (Lemma D).
- ARGUED, not proved: the uniform all-orders bound on Λ_c, including the co-moving step and rare configurations where an interior point sits near a hop's light cone.

**Needed for the FAIL is far weaker than the asymptotic.** The bar fails if Λ(z₀) ≥ 1 at z₀ = c_crit √ε, where c_crit = 0.00975 (s = 10 km). Since Λ_node(z₀) ≈ 4πI_h/c_crit² ≈ 7.9e4, it suffices to prove |Λ_c(z₀)| ≤ 7.9e4. Power counting gives |Λ_c| ~ 1e4·ε ~ 1e-59.

**Exponent margin.** RL2's PASS route needed α ≥ 0.539. The derivation gives α = ½ with an analytic O(ε ln 1/ε) correction. At ε = 7e-64 that correction is about 1e-61.

## 5. Check against RL2's Monte Carlo, ε = 1 … ⅛ (CHECKED; `rl3b_B`, `rl3b_E`)

**Roots of the exact-K₁ characteristic equation, op0** (variance rate per ℓ_k; sd rate = half):

| ε | node only Λ_node = 1 | node + exact same-hop variance (a) | small-ε law √(4πI_hε) | RL2 MC sd ×2 | MC / node (sd) |
|---|---|---|---|---|---|
| 1 | 1.623 | 4.976 | 2.735 | 4.07 / 3.86 | 2.51 / 2.38 |
| ½ | 1.267 | 2.938 | 1.934 | 2.59 / 2.69 | 2.05 / 2.12 |
| ¼ | 0.979 | 1.724 | 1.367 | 1.37 / 1.18 | 1.40 / 1.21 |
| ⅛ | 0.748 | 1.049 | 0.967 | 0.81 / 0.85 | 1.08 / 1.13 |
| 0.05 | 0.515 | 0.599 | 0.612 | — | — |
| 0.01 | 0.254 | 0.262 | 0.274 | — | — |
| 0.001 | 0.0849 | 0.0852 | 0.0865 | — | — |

**op1 and op2 at ε = ¼.** MC/node is 1.48 and 1.42–1.65.

**Readings.**
- The node root approaches the law with node/law = 0.59, 0.77, 0.93, 0.98 at ε = 1, ⅛, 0.01, 0.001. That is the O(z² ln z) K₁ correction.
- The exact same-hop variance term shifts z² by +8.4ε, 8.8ε, 8.4ε, 7.7ε, 7.1ε, 6.8ε, 7.1ε. It is cleanly linear in ε, as section 4 predicts for a coincident-end correction.
- The MC sits between the two roots. Its excess over the node root, (z²_MC/z²_node − 1)/ε, is 5.3/4.7, 6.4/7.0, 3.8/1.8 and 1.3/2.3 at ε = 1, ½, ¼, ⅛. So the remaining K_c terms (b), (c) are negative and also shrink with ε.
- **The data are consistent with the theorem.** MC → node ladder as ε falls, and the bare ladder (RL1/RL2) is not the limit.
- **The data cannot fix the order of the correction** (O(ε) against O(√ε)): samples are small and heavy-tailed, and this is a fixed-source field rather than the Palm two-point function.
- **Note.** At ε = 1, node + same-hop variance reproduces RL2's bare-ladder root, 4.9757. At large z only small τ matters, where h ≈ f.

## 6. Physical translation (`rl3b_D`)

**Formula.** sd e-folds n = k_h ℓ_P² τ/(2ℓ_k³), with τ = √(2Ds + s²), D = 1 Gpc = 3.0857e25 m. ε = (ℓ_P/1e-19 m)⁴ = 6.82e-64.

| source extent s | τ | n at ℓ_k = 1e-19 m (op0/op1/op2) | ℓ_k needed (op0 … op2) | k_h / c_crit |
|---|---|---|---|---|
| 1.0e4 m (10 km) | 7.86e14 m | 281 / 291 / 334 | 6.55–6.94e-19 m | 281–334 |
| 1.2e4 m (E1′-b) | 8.61e14 m | 307 / 319 / 366 | 6.75–7.15e-19 m | 307–366 |
| 3e6 m (100 Hz cycle) | 1.36e16 m | 4860 / 5039 / 5783 | 1.69–1.79e-18 m | ~5e3 |
| 3e10 m (100 s) | 1.36e18 m | 4.9e5 / 5.0e5 / 5.8e5 | 7.9–8.3e-18 m | ~5e5 |

**Source transfer (referee finding 3; ARGUED, node level).** Theorem 1's cutting also applies to two different source points y, y′. Cut at the **first common vertex** z₁.
- Upstream: the two interior-disjoint chains from y and y′ give, at node level, Σ_{y,y′} J J′ H̄(z₁,y) H̄(z₁,y′) = φ̄(z₁)². This is the square of the mean field.
- Downstream: the same renewal M2 applies.
- So Var φ(x) ≈ ε ∫ d⁴z φ̄(z)² R(x,z), with R the positive node-ladder resolvent, R ~ e^{γ τ(z,x)}.
- This structure is positive, like Lemma L's modulus-square ends. Its exponent is γ · max τ(z,x) over the support of φ̄², which by the reverse triangle inequality is ≤ τ_max ~ √(2Ds).
- This replaces RL2's unproved Cauchy–Schwarz step by the same pole γ. It is not yet a theorem including the K_c parts.

## 7. Against the FIXED readings

- **PASS** needs a proof that the exponent is > ½ (e.g. ≥ 0.54) or that the constant is small enough. **Not met.** The exponent is derived to be exactly ½, and the constant is k_h = 2.73–3.25, 281–334 times too large. PASS is excluded at the level of this derivation.
- **FAIL** needs "a proof that the rate is at least c√ε/ℓ_k with c large enough that the bar fails" (c_crit = 0.0098 at s = 10 km). **Not fully met.** What is proved:
  - the exact renewal;
  - the exact leading term and its constant (a convergent integral, no extrapolation);
  - the single-segment suppression lemma.

  Two steps are not proved:
  - (P1) a uniform bound |Λ_c(c_crit√ε)| ≤ 7.9e4. This is a crude bound with a 5-decade margin over the power-counting estimate.
  - (P2) the transfer from the Palm two-point variance to the extended-source field including K_c. At node level it is derived (section 6).
- **Worker reading: INCONCLUSIVE, leaning FAIL.**
  - The extrapolation objection that held RL2 at INCONCLUSIVE no longer applies: nothing is extrapolated in ε.
  - The remaining gap is two named lemmas, not a 63-decade fit. If a referee accepts the section 4 power counting as proof, the reading becomes **FAIL (bounded to the scalar Palm/node-transfer level)**.
- **Against the supervisor's expectation.** The ladder structure gives rate ∝ √ε with a convergent S1-type coefficient: exponent exactly ½, as expected. The constant is the node ladder's (2.73), not the bare ladder's (2.84). The bare ladder is not the limit; it is the ε = 1 face of the same equation.

## 8. Flags for the referee

1. Theorem 1's factorization needs every hop interval of segment i to lie inside I(z_i, z_{i+1}) and to contain no other segment's vertex. Check this, including Palm endpoints.
2. The momentum identity for I_h. Check the pinch step and the analytic continuation of f̃ to the lower half w-plane (retarded transform, analytic off the real axis).
3. The co-moving argument in section 4. It is the only place where the boost structure of an interior rung enters. Configurations with an interior point near its hop's light cone were not bounded.
4. Section 5 compares Palm-kernel roots with a fixed-source MC on a timelike diamond, as RL2 did. The comparison is a trend check, not a fit.
5. The chaos by-product (Var = ε² Σ ε^k ‖A_k‖²/k! with ε-independent A_k) is a second exact route to the exponent. It overlaps with the RL3 lane's method.

## Files (scratch: `/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C4/RL3b/`)

| script | output | content |
|---|---|---|
| `rl3b_A_Ih_momentum.py` | `rl3b_A_Ih_momentum.out` | exact momentum identity for I_h; test on e^{−τ⁴}; zero scan |
| `rl3b_B_h_and_roots.py` | `rl3b_B_h_and_roots.out`, `rl3b_h_op{0,1,2}.npz` | h(τ) via RL1 Volterra; finite-ε roots (node; node + same-hop variance); MC comparison |
| `rl3b_C_displaced_segment.py` | `rl3b_C_displaced_segment.out` | Lemma D check, W(Δ;z) for coincident, spacelike, null and timelike Δ |
| `rl3b_D_translate.py` | `rl3b_D_translate.out` | physical translation; c_crit; α needed for PASS |
| (inline) | `rl3b_E_finite_eps_shifts.out` | relative z² shifts / ε |
| `rl2_core_copy.py`, `RL1in/` | — | self-contained copies of RL2's operator core and RL1's solver/coefficients (byte-identical inputs) |
