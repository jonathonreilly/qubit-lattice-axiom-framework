# C4 lane RL3: the noise exponent theorem for the event route (worker report)

**Worker:** Claude Opus 5.5 (probe RL3), the same model family as the exercise authors. **Unrefereed.** Worked 19:19–19:51Z on 2026-10-11. OMP_NUM_THREADS=2; every run under 2 minutes. No repository file was edited.

**Read in full:** `docs/MINIMAL_AXIOMS_2026-06-29.md`; TESTS.md lines 1–12, "C4 sixth wave / Lane RL2", "C4 ninth wave / Lane RL3"; the RL2 worker report and its scripts `rl2_core`, `rl2_B`, `rl2_C`, `rl2_D`; `C4_RL1_report.md`, `C4_RL1_referee.md`; `E1_referee.md`; `supervisor_thread.md`; `C3_LemmaL_referee.md`. **Read in part:** RL1's Volterra solver (`RL1_B`) and its grid check (`RL1_F6.out`).

## Verdict (worker): FAIL against the fixed (rate) reading, with one bookkeeping step of the lower-bound proof sketched rather than written out (flag 1)

| | status | result (op0 / op1 / op2) |
|---|---|---|
| **Theorem 1.** Var_ε[(GJ)(x)] = Σ_{k≥1} ε^k a_k, with every a_k ≥ 0 and **independent of ε** (ℓ_k units) | **PROVED** (exact, all ε ∈ (0,1]); **CHECKED** sharply (D) | — |
| **Lemma S.** An insertion that sits inside a hop, instead of on the chain, is suppressed by e^{−θ} when its two legs differ in rapidity by θ | single vertex: **PROVED** (needs only sup\|H\|); multi-vertex product bound: **SKETCHED**; **CHECKED** (B, E) | measured \|rest/node\| ≈ (10–100)·e^{−1.8θ} |
| **Theorem 3 (a).** Lower bound γ_var(ε) ≥ c_low √ε/ℓ_k, in the window ε^{−1/2} ≪ τ/ℓ_k ≪ ε^{−3/2} (the physical point lies inside it) | **PROVED in outline**: steps (i)–(iv) proved, (v)–(vi) sketched | c_low = 1.18 / 1.33 / 1.52 (window \|H\| ≥ 0.3); 0.72 / 0.77 / 0.82 (window τ ≤ 0.6) |
| **Theorem 2.** The exact constant: γ_var = c*√ε/ℓ_k (1 + O(ε ln²(1/ε))), with c* = √(4π I_h) and I_h = ∫τ H̄_k² dτ | lower half as in Theorem 3; upper half **ARGUED** | c* = 2.732 / 2.835 / 3.253 |
| FAIL threshold c_fail (≥ 1 sd e-fold at ℓ_k = 1e-19 m, 1 Gpc, 10 km source, τ = √(2Ds)) | arithmetic | **c_fail = 0.0089** |
| (c) margin | | c_low/c_fail = 81–171; c*/c_fail = 307–366. ℓ_k needed ≥ 4.3–5.6×10⁻¹⁹ m (from c_low) or 6.7–7.2×10⁻¹⁹ m (from c*) |

**Plain summary.**
- **The key fact is exact and simple.** On a Poisson sprinkling, the variance of the realization-inverse field is a power series in the smearing ε, and every coefficient is a fixed, nonnegative number that does not depend on ε (in units of ℓ_k). Each coefficient is the squared size of the field's k-th order response to adding k points.
  - So no extrapolation in ε is needed. Small ε just weights the same fixed numbers differently.
  - The growth rate at small ε is set by how these fixed numbers grow with distance. That growth is a property of ε-independent integrals.
- **Two kinds of response, and only one survives at long range.** Adding a point either inserts a new step into a chain (a "node"), or changes the count inside an existing step (an "interior" insertion). RL2 flagged that these add with signs inside each term.
  - I prove that the interior insertion is pinned between its two neighbours' causal diamonds. It pays a factor e^{−θ}, where θ is the rapidity between its two legs.
  - In the configurations that carry the growth, consecutive legs are boosted relative to each other by θ ≈ ln(1/ε) ≈ 145 at physical ε. So the interior terms are suppressed by about ε, and the variance is the node ladder: rung H̄², constant c* = √(4π∫τH̄²) = 2.73 for op0.
  - This is exactly RL2's "node-only renormalized ladder". It is now the asymptotically exact law, not an estimate.
- **The bar fails by a wide margin in the constant.** The rate is c√ε/ℓ_k with exponent exactly ½. Avoiding FAIL at ℓ_k = 1e-19 m would need c ≤ 0.0089. The proved lower bound (with deliberately crude choices) is 0.72–1.52, and the exact constant is 2.73–3.25.
  - In ℓ_k this is still only about 0.6–0.85 decades, because ℓ_k ∝ c^{1/3}.
- **Caveat on the physical reading (flag 3).** The pre-registered criterion counts e-folds of the rate. The power-law prefactor at the physical point is worth about −150 e-folds of variance. With c* the noise stays enormous; with the crudest proved c_low (window τ ≤ 0.6) it would be marginal. This needs the prefactor, which I did not prove.

## 1. Setting (RL1/RL2 conventions; ℓ_k = 1, ρ_k = ερ = 1)

- **Sprinkling and weights.** Poisson sprinkling P of density ρ = 1/ε in a bounded causal region. The hop weight is h(n) = ε g_ε(n), where g_ε(n) = Σ_j C_j Binom(n, j; ε) and n = |P ∩ I(y,x)|. Operator B = I − N, with N(x,y) = h(n(y,x)) for y ≺ x.
- **Field.** φ(x) = Σ_{y∈P} H_P(x,y) J(y), with H_P = (I − N)⁻¹ − I, i.e. the sum over chains of at least one hop. This is RL2's `rl2_B` observable exactly.
- **Mean quantities.** f(m) = e^{−m}Σ C_j m^j/j!, with m = (π/24)τ⁴, and f^{(a)} = d^a f/dm^a.
  - The mean inverse is H̄ = εH̄_k, with H̄_k = f + f∗H̄_k (RL1's Volterra equation). I write H for H̄_k, and M = δ + H.
  - Ψ = MJ is the mean field. It does not depend on ε, by RL1/RL2's exact Palm identity.
- **Two exact Poisson facts used throughout:**
  - E g_ε(Poi(μ)) = f(εμ), by thinning;
  - E Δ^a g(Poi(μ)) = d^a/dμ^a E g(Poi(μ)).
  - Together: E Δ^a h(Poi(μ)) = ε^{a+1} f^{(a)}(εμ).

## 2. Theorem 1: the exact ε-power series (PROVED; CHECKED)

**Statement.** Var_ε φ(x) = Σ_{k≥1} ε^k a_k, where a_k = (1/k!)∫ F_k(z₁…z_k)² dz₁…dz_k ≥ 0. The kernels F_k depend only on f, its m-derivatives, J and x, and not on ε.

For the kernel between two added points, H_P(x,y₀): Var[H_P/ε] = Σ ε^k a_k as well, with E[H_P/ε] = H(τ) exactly.

**Proof.**
1. **Chaos expansion.** F ∈ L² on a bounded region: the weights are bounded and the number of chains is ≤ 2^{|P|}. Last–Penrose then gives Var F = Σ_k (ρ^k/k!)∫(E D^k_{z₁..z_k}F)².
2. **Expanding D^k F.** D^k F = Σ_{S⊆[k]}(−1)^{k−|S|} F(P ∪ z_S). Expand each F(P ∪ z_S) over chains, and group the chains by the set T ⊆ S of inserted points they use as nodes.
   - The hop intervals of a chain are pairwise disjoint open intervals, and they contain no chain node.
   - So each inserted point outside T lies in at most one hop interval.
   - In the alternating sum over S ⊇ T, a point lying in no hop interval cancels. A point in a hop interval turns that hop's weight into a forward difference.
   - Result: D^k F = Σ_T Σ_{chains through z_T} Π_hops Δ^{a_hop}h(n_P(hop)) · 1[every z_j ∉ T lies in a hop] · J(end).
3. **Expectation.** The multivariate Mecke formula handles the P-nodes; disjoint intervals give independent Poisson counts. Each hop with a inserted interior points contributes ε^{a+1}f^{(a)}.
   - A chain with r P-nodes has r + |T| hops (+1 for the kernel case), and Σa = k − |T|.
   - So the term carries ρ^r ε^{r+|T|+k−|T|} = ε^k (ρε = 1). Hence E D^k F = ε^k F_k (ε^{k+1}F_k for the kernel).
   - Therefore ρ^k(E D^k F)² = ε^k F_k². ∎

**Corollaries (PROVED).**
- (C1) Var_ε/ε is nondecreasing in ε, and Var_ε ≤ (ε/ε₀)Var_{ε₀} for ε ≤ ε₀.
- (C2) The growth rate γ(ε) is nondecreasing in ε.
- (C3) Any small-ε statement about γ is a statement about the large-τ growth of the fixed sequence a_k(τ). The rule against long extrapolation (TESTS.md:5–9) is met by construction, provided the asymptotics of the a_k are derived and not fitted.
- (C4, reading) F_k = δ^kΦ/δρ_k(z₁)…δρ_k(z_k), the Taylor coefficients of the mean field in an inhomogeneous event density (Margulis–Russo). Noise is the mean field's response to density fluctuations.

**CHECK (D, `rl3_D_first_chaos_check.out`).** Kernel case, op0. a₁(T) is computed independently by quadrature of the exact one-insertion kernel Γ = N + (interior) + (grouped), and compared with the Monte Carlo limit of Var[H_P/ε]/ε at ε = ½ … 1/64 (R = 40000 … 6000).

| T | a₁ quadrature (all insertions) | node-only part ∫N² | MC Var/ε at ε = 1/32, 1/64 | MC quadratic ε→0 intercept |
|---|---|---|---|---|
| 1.0 | 3.941 ± 0.009 | 0.100 | 4.50, 4.09 | 3.89 |
| 1.5 | 3.011 ± 0.031 | 0.243 | 3.10, 3.02 | 3.00 |

- The MC mean is ε-independent and equals H(T) (−0.148 against −0.145; −0.103 against −0.102).
- The series structure and the interior/grouped kernels are confirmed at the 1–2% level.
- At these short separations the interior terms are 97% / 92% of a₁. The node-only ladder is **not** a lower bound term by term; it becomes the law only at large rapidity (§3).

## 3. Lemma S: interior and grouped insertions die with leg rapidity

**(i) Confinement (PROVED).** Take inserted points ordered along a chain, x = z₀ ≻ z₁ ≻ … ≻ z_k (≻ y₀).
- Every P-node of every contributing chain lies in a diamond I(z_j, z_{j−1}).
- If z_j is interior to a hop (u, v), then u ∈ I(z_j, z_{j−1}) ∪ {z_{j−1}} and v ∈ I(z_{j+1}, z_j) ∪ {z_{j+1}}.
- When several points share one hop, the hop's ends lie in the diamonds adjacent to the group.
- Proof: total order along the chain.

**(ii) Rapidity inequality (PROVED).**
- If u ∈ I(0, a), then τ_u e^{ζ(u,a)} ≤ 2τ_a. Proof: cosh ζ ≤ (τ_a² + τ_u²)/(2τ_aτ_u).
- Hence, for u ∈ I(0, a) and −v ∈ I(0, b), where the legs a, b have relative rapidity θ:

  τ(v,u)² ≥ 2u·(−v) ≥ τ_u τ_v e^{θ−ζ_u−ζ_v} ≥ e^θ τ_u²τ_v²/(4τ_aτ_b).

**(iii) One-vertex bound (PROVED, given sup|H| < ∞).**
- The set {u ∈ I(0,a): τ_u ≤ t} has measure ≤ π τ_a² t². Then (ii) and the super-exponential decay of f′ give the four exact pieces:
  - z interior to a hop leaving z_prev directly: ≤ C_d e^{−θ};
  - the same hop reached through a mean chain: ≤ C_H (1+θ) e^{−θ};
  - z inside a hop that ends at z_next: ≤ C_G e^{−θ}, or super-exponentially small when the hop is direct.
- The constants involve sup|H| (1.011 / 1.081 / 1.153), the diamond sizes, and ∫Φ(y²)dy with Φ the decreasing envelope of |f′|.
- Grouped hops holding several inserted points pay at least the same factor, via τ(v,u)² ≥ 2(u − z_j)·(z_j − z_{j+1}).

**(iv) Multi-vertex product bound (SKETCHED).** On configurations where every step proper time lies in a window W with |H| ≥ h₀ and every consecutive leg rapidity is ≥ θ*, each assignment with interior set S is bounded by

  |F^{(S)}| ≤ |F^{nn}| Π_{j∈S} Ĉ(1+θ_j)e^{−θ_j},

where F^{nn} = Π H(steps)·Ψ is the all-node term.
- Neighbours of an interior vertex trade H(τ_j) for at most sup|H|, which costs a factor sup|H|/h₀.
- The number of groupings is ≤ c^{|S|}.
- Large groups are not dangerous. On A_k a hop holding g ≥ 2 consecutive inserted points must contain a zig-zag of g − 1 steps with mutual rapidities ≥ θ*. Its interval volume grows with g, so f^{(g)} is super-exponentially small there; each group still pays at least one factor e^{−θ*}.
- Hence |F_k| ≥ ½|F_k^{nn}| whenever k Ĉ(1+θ*)e^{−θ*} ≤ 0.4.
- I have not written out the constant Ĉ in full (flag 1).

**CHECK (B, `rl3_B_op{0,1,2}.out`).** The exact one-vertex pieces were computed by MC at legs (τ₁, τ₂) = (0.6, 0.6), (1, 1), (0.6, 1.4), for θ = 0 … 6.
- At θ = 0, rest/node = −2.7 … −14: interior terms dominate when the legs are aligned.
- At θ = 4, 5, 6: (0.85, 0.11, 0.018)×10⁻³; (37, 7.3, 1.2)×10⁻³; (2.4, 0.5, 0.05)×10⁻³ (op0).
- The other operators agree within a factor 1.5. The decay is ≈ e^{−1.8θ}, faster than the proved e^{−θ}.

**CHECK (E, `rl3_E_first_chaos_largeT.out`).** The exact first-chaos coefficient a₁(T), kernel case op0, two-cone parametrization (d⁴z = (πr/T) dτ₁² dτ₂²), legs τ ≤ 3.
- The share of a₁ not carried by the node term falls: 0.92 (T = 1.5), 0.80 (2), 0.13 (3), 0.005 (5), 0.003 (8), 0.000 (12), 0.001 (16). The MC noise at T ≥ 5 is ≈ 0.003 (inner MC n = 40000; the n = 3000 run gave the same trend with noise ≈ 0.03).
- Over the same range the node-weighted mean leg rapidity rises 2.3 → 5.
- The node part tends to its exact large-T value 2πI_h² = 2.216 (2.04 at T = 12).

## 4. Theorem 3: the explicit lower bound (part a)

**Statement.**
- Fix a window W on which |H| ≥ h₀ > 0 and c_low(W) := √(π I_h[W]), with I_h[W] = ∫_W τH² dτ.
- Then for ε → 0 and τ/ℓ_k in [ε^{−1/2−δ}, ε^{−3/2+δ}], the variance grows at least like exp[c_low √ε τ/ℓ_k (1 − o(1))], up to a power-law prefactor.
- Shown for the Lorentz-invariant kernel case; for a fixed smooth source, through Ψ² ≥ 0 at the last insertion.

**Proof outline.**

| step | content | status |
|---|---|---|
| (i) | Var ≥ Σ_k ε^k (1/k!)∫_{A_k}F_k² for any regions A_k (Theorem 1: every term ≥ 0) | proved |
| (ii) | A_k = chain-ordered configurations whose k+1 steps have τ ∈ W, lab rapidity ≥ η*, and spatial direction alternating between the caps n·e ≥ ½ and n·e ≤ −½; then every consecutive leg rapidity θ ≥ 2η* − ln 4 =: θ* | proved |
| (iii) | Lemma S (i)–(iii) | proved |
| (iv) | product bound ⇒ \|F_k\| ≥ ½\|F_k^{nn}\| on A_k for k ≤ 0.4e^{θ*}/(Ĉ(1+θ*)) | sketched |
| (v) | restricted node ladder: alternating-cap renewal. Rung transform ĝ_c(z) = π∫_Wτ³H²∫_{η*}^∞ sinh²η e^{−zτcoshη} ≥ π I_h[W]/z² − O(ln(1/z) + e^{2η*}) (uses ∫₀^∞ sinh²η e^{−x coshη}dη = K₁(x)/x; each cap is ¼ of the sphere). Pole at z² = πI_h[W]ε(1 − O(ε ln(1/ε) + ε e^{2η*})) | proved (the Laplace step); the capped-sum-to-pointwise (Tauberian) step is sketched |
| (vi) | choose e^{θ*} between k ≈ √ε τ and 1/ε. This is possible exactly when τ ≪ ε^{−3/2}. At the physical point, √ετ/ℓ_k = 225 and ε^{−1} = 1.5×10⁶³, so e^{θ*} ≈ 10⁴⁰ makes both error terms ≲ 10⁻²³ | arithmetic |

**Values (`rl3_C`).**
- c_low = 1.176 / 1.331 / 1.521 (W: |H| ≥ 0.3), or 0.717 / 0.767 / 0.818 (W: τ ≤ 0.6, where H ∈ [0.80, 1.01]).
- The cap alternation costs a factor 2 in c. A positive-operator argument without it would give √(4πI_h[W]) (ARGUED).

**No extrapolation.** Every constant is an ε-independent convergent integral.
- I_h converges: the grid change moves it by 1.5×10⁻³ relative, and the cutoff change 12 → 16 adds 0.2%.
- The large-τ tail of the Volterra H is numerically noisy at the 10⁻³ level (RL1 F6). It enters I_h at below 0.5%.
- The ε-window condition holds at the physical point with 60 decades of room.

## 5. Theorem 2 and the upper bound (part b): ARGUED

**Exact constant.** In the hyperboloid regime the node ladder's rung is g = H² with ĝ(z) = 4πI_h/z² + O(ln(1/z)). Its pole is z* = √(4πI_hε)(1 + O(ε ln ε)).
- Lemma S, used in absolute value, bounds the remaining Bethe–Salpeter kernel. Aligned configurations (θ = O(1)), where rest/node is 10–100, occupy a fraction O(z²) of the rung measure, giving relative corrections O(A ε ln²(1/ε)) with A ~ 10²–10⁴.
- So γ_var = c*√ε/ℓ_k with c* = √(4πI_h) = 2.732 / 2.835 / 3.253: both bounds have the same constant, and the exponent is exactly ½.
- The upper half needs the absolute-value Lemma S over all configurations, including large-τ hop tails. That is not written (flag 2).
- **Consistency with RL2's MC.** At ε = ⅛ the MC sd rate is 0.40–0.42, against the node law's 0.483: a ratio of 0.83–0.87. With A ~ 10–100, the O(Aε ln) correction is O(1) at ε ≥ ⅛, so the MC is pre-asymptotic. This explains why it sits below both ladders without contradicting the law.
- **Corrections to RL2.** RL2's "bare" constants (2.84/3.03/3.33) are not the asymptotic law; the node constants are. RL2's statement that both ladders are "not bounds" is resolved: the node ladder is the exact asymptotic, and the bare ladder is not.

## 6. Physical translation (part c; `rl3_C`)

**Inputs.** ℓ = ℓ_P, D = 1 Gpc, s = 1.2×10⁴ m, τ = √(2Ds + s²) = 8.61×10¹⁴ m. At the bar, ε = 6.8×10⁻⁶⁴ and √ε τ/ℓ_k = 224.8.
- sd e-folds: n = (c/2)·224.8.
- c_fail = 0.00890.

| constant | n at the bar (sd e-folds) | ℓ_k needed for n ≤ 1 |
|---|---|---|
| c* (op0 / op1 / op2) | 307 / 319 / 366 | 6.75 / 6.83 / 7.15 ×10⁻¹⁹ m |
| c_low, W: \|H\| ≥ 0.3 | 132 / 150 / 171 | 5.09 / 5.31 / 5.55 ×10⁻¹⁹ m |
| c_low, W: τ ≤ 0.6 | 81 / 86 / 92 | 4.32 / 4.42 / 4.51 ×10⁻¹⁹ m |

- ℓ_k ≤ 1e-19 m is not viable over 1 Gpc for a 10 km source under the pre-registered rate count.
- The exclusion is 0.64–0.85 decades in ℓ_k, but 80–370 times in the rate constant.

**Prefactor (SUGGESTED, flag 3).** From the renewal pole, Var ≈ Λ m^{1/2} e^{mτ}/(4π√(2π)τ^{3/2}), with m = c√ε. At the physical point:
- c*: ln Var ≈ 614 − 154 = 460 (≈ 230 sd e-folds);
- c_low = 1.18: ≈ 108 (54 sd);
- c_low = 0.72: ≈ 3 (2 sd).

These are on the unit scale of the ℓ_k-normalized kernel. The physical comparison is against the signal, which is much smaller (about ℓ_k/D for the null configuration), so the relative noise is larger still. The rate criterion is what was pre-registered.

## 7. Against the FIXED readings

- **PASS** ("rate exponent > ½, or constant small enough that ℓ_k ≤ 1e-19 m bounds the noise"): **excluded**.
  - The exponent is exactly ½ in structure: Theorem 1 plus the 1/z² rung.
  - The constant is bounded below by c_low ≥ 0.72, against the 0.0089 PASS would need.
- **FAIL** ("a proof that the rate is at least c√ε/ℓ_k with c large enough that the bar fails"): **met**, with c_low = 0.72–1.52 against c_fail = 0.0089.
  - The proof's skeleton is proved: the exact series, confinement, the rapidity inequality, the one-vertex bound, and the restricted-ladder pole.
  - Two routine estimates are sketched: the multi-vertex product constant Ĉ, and the capped-sum Tauberian step. Their slack is a factor e^{θ*} ≈ 10⁴⁰.
- **Worker reading: FAIL**, conditional on the referee accepting (iv)–(v) as written. If the referee requires them in full, the reading is INCONCLUSIVE, leaning FAIL. Either way, the gap is no longer an extrapolation in ε.
- **Against the supervisor's expectation:**
  - "Exponent ½ exactly, constant ≈ ladder": confirmed, and the ladder is identified as the node ladder (2.73), not the bare one (2.84).
  - "A provable lower bound gives FAIL by about 1 decade": 0.64–0.85 decades in ℓ_k.

## 8. Flags for the referee
1. **Step (iv).** The multi-vertex product bound on A_k: the explicit Ĉ, including grouped hops and interior vertices adjacent to the observer and source ends. Also step (v)'s capped-sum Tauberian step.
2. **Upper bound (part b).** It is ARGUED only: the absolute-value Lemma S over all configurations, including aligned ones and H's large-τ tail.
3. **Prefactor.** The fixed reading counts rate e-folds. At the physical point the power-law prefactor costs about 150 variance e-folds. The FAIL survives with c* and with c_low (|H| ≥ 0.3), but it is marginal on the unit scale with the crudest window (τ ≤ 0.6). The physical null-configuration translation, τ = √(2Ds), is RL2's B.1 mapping; for the lower bound it enters only through Ψ² ≥ 0 at the last insertion (ARGUED).
4. **Numerical inputs.** sup|H| and the windowed I_h come from RL1's Volterra solution, which is not interval-certified. They are robust to grid (≤ 0.15%), and the margins are 80×+.
5. **Theorem 1 is general.** It holds for every ε ∈ (0, 1] and every count-dependent retarded operator with ε-thinned weights. It answers the RL1/RL2 question "do positive ladders bound the variance?": the chaos orders are the positive sub-sums, and the node ladder is not one of them. It becomes the law only through Lemma S.

## Files (scratch: `/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C4/RL3/`)

| script | output | content |
|---|---|---|
| `rl3_A_Ih.py` | `rl3_A_Ih.out`, `rl3_H_op{0,1,2}.npz` | H̄_k (Volterra), I_h grid and cutoff convergence, c* |
| `rl3_B_vertex_suppression.py` | `rl3_B_op{0,1,2}.out` | exact one-vertex pieces vs leg rapidity (Lemma S check) |
| `rl3_C_window_and_translate.py` | `rl3_C_window_and_translate.out` | windowed constants, c_fail, translation, prefactor estimate |
| `rl3_D_first_chaos_check.py` | `rl3_D_first_chaos_check.out` (`_v0_mislabelled.out`: first run, kernel normalization printed wrongly; superseded) | Theorem 1 check: a₁ quadrature vs MC ε → 0 |
| `rl3_E_first_chaos_largeT.py` | `rl3_E_first_chaos_largeT.out` (`_n3000.out`: lower-statistics run) | Lemma S inside the exact a₁(T), T = 1.5–16 |
| `rl2_core.py` | — | copy of RL2's operator module (renormalized ops) |
