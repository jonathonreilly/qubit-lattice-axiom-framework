# C4 lane RL4: closing RL3's two lemmas (worker report)

**Worker:** Claude Opus 5.5 (probe RL4), the same model family as the exercise authors. **Unrefereed.** Worked 20:23–21:15Z (machine clock) on 2026-10-11. OMP_NUM_THREADS=2; every run under 1 minute. No repository file was edited.

**Read in full:** TESTS.md lines 1–12, "C4 ninth wave / Lane RL3", "C4 results recorded 20:23Z", "C4 tenth wave / Lane RL4" (fixed readings); `C4_RL3_report.md`, `C4_RL3_referee.md`; `C4_RL3b_report.md`, `C4_RL3b_referee.md`. **Read in part:** `C4_RL2_report.md` (source definition, B.1); `rl2_core.py` (operator coefficients); RL3's stored Volterra arrays (used only as a sanity comparison, never inside a bound). I did not read the `_full` referee files for RL3/RL3b (not present in `agents/`; the referee summaries were enough).

## Verdict (worker)

| item | status | content |
|---|---|---|
| **Lemma U′** (replaces Lemma U) | **PROVED** (constants computer-evaluated, not interval-certified) | On the Lorentz-invariant set A_k (all legs τ ∈ W = [0.1, 0.6], every consecutive-leg rapidity ≥ θ* = 10.75), the full chaos kernel obeys \|F_k\| ≥ (1−2δ)^k \|F_k^nn\| for **every k**, with δ = 0.044 / 0.045 / 0.046 (op0/1/2). |
| RL3b's literal Lemma U (\|Λ_c(z₀)\| ≤ 7.9e4) | **not proved; not needed** | U′ plus the positivity of the chaos series gives the lower bound without bounding the signed irreducible kernel K_c. |
| **Rate lemma** (RL3's "Tauberian" step) | **PROVED** for the limsup rate; liminf via a standard local limit theorem | No inverse-Laplace step is needed. Lorentz invariance and nonnegativity of the Palm variance convert divergence of the restricted ladder's transform into a pointwise rate. |
| **Palm two-point variance** V_ε(τ) = Var[H_P(x,y)/ε] | **PROVED** | lim inf_{τ→∞} τ⁻¹ ln V_ε(τ) ≥ c_low √ε, with c_low = 0.628 / 0.670 / 0.712. c_low/c_fail = 64 / 69 / 73 at s = 10 km. |
| **Lemma T′** (extended source with a spacelike past edge and regular turn-on) | **PROVED** for the end factor (explicit). Geometric step: **PROVED** for a planar edge (Blackwell renewal theorem); finite source **ARGUED** (standard local CLT, polynomial prefactor only) | The end factor is ≥ ½(1−2δ)h₀\|J(z_k)\| > 0 for z_k in a layer of thickness a₀ = 0.30–0.36 ℓ_k above the edge. |
| **Lemma T for an edgeless source** (e.g. Gaussian-tailed J > 0 everywhere) | **NOT PROVED**; obstruction identified | The one-legged end response diverges logarithmically in absolute value. It is finite only through the moment condition M₀ = 0, so an absolute bound cannot work there. |

**Worker reading against the FIXED readings: FAIL (bounded),** or INCONCLUSIVE leaning FAIL if the referee does not accept the bounded scope.
- Both lemmas are proved in the forms U′ and T′.
- The bound covers:
  - the Palm two-point variance (complete);
  - extended sources whose support has a spacelike past edge with a regular turn-on.
- It does not cover sources with no past edge (Gaussian tails, or an infinite past).
- I did not prove the literal form of RL3b's Lemma U. The FAIL route does not need it.

**Plain summary.**
- **The noise variance is a sum of squares, so we may throw terms away.** RL3 proved that the variance is a sum of nonnegative pieces, one per number of added events. Keeping only the "ladder" configurations, where every added event sits on a chain with short steps that turn sharply, gives a lower bound.
- **Inside the kept configurations, the dangerous signed terms are now controlled multiplicatively.** These are the terms where an added event sits inside a hop instead of on the chain.
  - RL3's sketch only gave a bound when the number of added events k was much smaller than e^{θ*}. Here, a renewal over the positions of the added events shows that each sharp turn costs at most a factor (1−2δ) ≈ 0.91, for every k.
  - Every input is now rigorous except computer-evaluated envelope integrals. In particular, the sup of the mean kernel on short proper times comes from an analytic chain-volume bound, not RL1's Volterra numerics.
- **From a pole to a pointwise rate.** The variance between two points depends only on their proper time and is ≥ 0. So if its Laplace transform diverges, the variance itself must grow at least that fast along some sequence of τ. A local limit theorem upgrades this to all large τ.
- **The end factor.** If the source switches on across a spacelike surface (any real source that starts at some time), the last added event can be placed just after the switch-on. Its past then holds almost no source, every correction is O(a⁴), and the end factor is J(z_k)h(leg) ≠ 0.
- **Number.** The proved rate constant is 0.63–0.71 against the 0.0098 needed to fail the 1e-19 m bar. That is 64–73 standard-deviation e-folds at 10 km, 1 Gpc.
  - This is weaker than the node-ladder candidate 2.73–3.25, because of the window and cap restrictions.
  - It is still a factor 64–73 in the constant and about 0.6 decades in ℓ_k.

## 1. Setting (RL1/RL2/RL3 conventions)

- **Units and weights.** ℓ_k = 1, ρε = 1, f(m) = e^{−m}Σ_n C_n m^n/n! with m = πτ⁴/24. C for op0/1/2 are taken from `rl2_core.OPS` (massless-renormalized).
- **Mean kernel.** h = f + f∗h; M = δ + h.
- **Observables.**
  - Palm two-point: V_ε(τ) = Var_ε[H_P(x,y)/ε], with τ = τ(y,x).
  - Extended source: φ(x) = Σ_{y∈P} H_P(x,y) J(y), with mean field Ψ = MJ.
- **Theorem 1 (RL3, referee-confirmed).** Var = Σ_{k≥1} (ε^k/k!) ∫ F_k², with ε-independent kernels F_k given by RL3's D^k formula.
  - Insertions are either nodes of a chain, or interior to a hop. A hop containing g inserted points carries the factor f^{(g)}(vol).
  - P-nodes are integrated with Lebesgue measure.

## 2. Lemma U′: multiplicative control of interior insertions (PROVED)

### 2.1 Exact transfer structure (PROVED)

Fix chain-ordered z_0 = x ≻ z_1 ≻ … ≻ z_k ≻ z_{k+1} = y. For a < b define Step_{a,b} as the sum over chains from z_a to z_b whose hops contain all of z_{a+1}, …, z_{b−1}, each hop weighted by f^{(g)} of its interval volume. Then:

- Step_{a,a+1} = h(z_a, z_{a+1}).
- F_k = G_{k+1}, where G_0 = 1 and G_n = Σ_{a<n} G_a Step_{a,n}.

**Proof.** In RL3's D^k formula, group each chain by its set T of node-insertions. Between consecutive T-nodes, the inserted points lie in hop intervals. Each hop containing a block of consecutive inserted points is "special".

The P-chain between two consecutive special hops, from v_i down to u_{i+1}, lies in the open diamond I(u_{i+1}, v_i). The z's are totally ordered, and block i lies strictly above v_i while block i+1 lies strictly below u_{i+1}. So that diamond contains no inserted point.

Its weight sum is therefore unrestricted, and equals M(v_i, u_{i+1}). This gives

Step_{a,b} = Σ_{blocks} ∫ M(z_a,u₁) f^{(g₁)}(u₁,v₁) M(v₁,u₂) ⋯ f^{(g_s)}(u_s,v_s) M(v_s,z_b).

The localizations are:
- u_i ∈ Ī(z_{p_i}, z_{p_i−1});
- v_i ∈ Ī(z_{q_i+1}, z_{q_i});

where block i = {z_{p_i}, …, z_{q_i}}. Every integration point lies in a **leg diamond** D_j = Ī(z_j, z_{j−1}) of proper time T_j ∈ W. ∎

Normalize: G̃_n = G_n / Π_{i<n} h(ℓ_{i+1}) and ρ_{a,n} = Step_{a,n} / Π_{i=a}^{n−1} h(ℓ_{i+1}), with ρ_{n−1,n} = 1. Then G̃_n = G̃_{n−1} + Σ_{a≤n−2} G̃_a ρ_{a,n}.

### 2.2 The index-renewal inequality (PROVED)

**Claim.** If |ρ_{a,n}| ≤ δ^{n−a−1} for all n − a ≥ 2 and δ ≤ 0.1, then |G̃_n| ≥ (1−2δ)|G̃_{n−1}| for every n. Hence |F_k| ≥ (1−2δ)^k Π_{i=0}^{k} |h(ℓ_{i+1})| = (1−2δ)^k |F_k^nn|.

**Proof.** By induction, |G̃_a| ≤ |G̃_{n−1}|(1−2δ)^{−(n−1−a)}. Then

|G̃_n − G̃_{n−1}| ≤ |G̃_{n−1}| Σ_{j≥1} (δ/(1−2δ))^j = |G̃_{n−1}| δ/(1−3δ) ≤ 1.43δ|G̃_{n−1}| ≤ 2δ|G̃_{n−1}|. ∎

**This is the step RL3 lacked.** It is uniform in k: no condition k ≪ e^{θ*} and no ε-window. So the bound survives the τ → ∞ limit at fixed ε.

### 2.3 Local bound |ρ_{a,b}| ≤ δ^{b−a−1} (PROVED; constants in `rl4_A`)

Hypotheses on A_k: every leg T_j ∈ W = [τ₁, τ₂] = [0.1, 0.6], and every interior vertex z_j has relative leg rapidity θ_j ≥ θ*.

1. **Rigorous h on short proper times.** h − f = Σ_{n≥2} f^{∗n}, and the n-chain volume in a diamond of volume V is ≤ V^{n−1}/(n−1)!. Hence
   - |h(τ) − f(τ)| ≤ F(e^{FV(τ)} − 1), with F = sup_{[0,τ]}|f|.
   - On [0, 0.6] this band is ≤ 0.0175 / 0.0200 / 0.0228. f is decreasing there.
   - So h_∞ := sup_{[0,τ₂]}|h| ≤ 1.028 / 1.101 / 1.176 and h₀ := inf_W h ≥ 0.769 / 0.821 / 0.872.
   - The Volterra arrays lie inside the band. Only h on [0, τ₂] enters the bound, because every M factor joins two points of one leg diamond.
2. **Rapidity inequality (RL3, re-derived).** Take w = u − z_j ∈ I(0, ℓ_j) and w′ = z_j − v ∈ I(0, ℓ_{j+1}). Then:
   - τ_w e^{ζ(w,ℓ_j)} ≤ 2T_j;
   - the hyperbolic triangle inequality gives θ(w,w′) ≥ θ_j − ζ − ζ′;
   - so τ(v,u)² ≥ 2w·w′ ≥ e^{θ_j} A B / (4T_jT_{j+1}), with A = τ_w², B = τ_{w′}².
3. **Product measure in a leg diamond.** For p ∈ D_j, take A = τ(z_j,p)² and B̃ = τ(p,z_{j−1})². Then d⁴p = (πr/T_j) dA dB̃ ≤ (π/2) dA dB̃, since the Jacobian of (p⁰, r) ↦ (A, B̃) is 4rT_j and r ≤ T_j/2.
   - This is what makes shared endpoints harmless. The point v_i = u_{i+1} (the δ-part of M) has its two coordinates used by two different hops, under a product measure.
4. **Singleton block {z_j}.** |f′(m)| ≤ ψ(c_j A B), with:
   - ψ(x) = Φ₁(x²) and Φ₁(m) = sup_{m′≥m}|f′(m′)|;
   - c_j = √(π/24) e^{θ_j}/(4T_jT_{j+1}).

   Each end is either a node (point mass at T²) or integrated (Lebesgue on [0, T²]). The worst of the three cases is:
   - Q_LL ≤ (Ψ₁/c)(1 + ln(cT²T′²ψ(0)/Ψ₁));
   - Q_PL ≤ 4(τ₂/τ₁)Ψ₁ e^{−θ}/√(π/24);
   - Q_PP = ψ(√(π/24) e^θ τ₁²/4), which is negligible.

   Here Ψ₁ = ∫₀^∞ ψ = 6.30 / 6.73 / 7.29 and ψ(0) = sup|f′| = 13.9 / 14.8 / 15.9.
5. **Pair block {z_p, z_{p+1}}.** τ(v,u)² ≥ max(e^{θ_p} A T_{p+1}/(2T_p), e^{θ_{p+1}} B T_{p+1}/(2T_{p+2})), with A = τ(z_p,u)² and B = τ(v,z_{p+1})², since every cross term of future-timelike vectors is positive.
   - Using Φ₂(max) ≤ √(Φ₂(m₁)Φ₂(m₂)), each end gives E₂ ≤ (2τ₂/τ₁) e^{−θ} S₂, with S₂ = ∫√Φ₂(πx²/24) dx = 18.3–19.0.
   - So the pair pays one suppression **per vertex**. This answers the referee's grouped-hop objection.
6. **Blocks with g ≥ 3.** The hop contains a zig-zag with (g−2) two-legged vertices inside, so τ(v,u)² ≥ (g−2)τ₁² e^{θ*}.
   - With |f^{(g)}(m)| ≤ 2^g · 6 max|C| · e^{−m}(1+m)^5, the factor is below e^{−10⁸}. It is far below δ^g for every g.
7. **Bookkeeping.**
   - Leg weights:
     - an inner leg carries ω = π/2 + h_∞(π/2)²τ₂⁴ ≤ 1.95 (the δ-part plus the h-part of M);
     - an end leg carries 1 + e, with e = h_∞(π/2)τ₂² ≤ 0.67;
     - there are at most 2^{n−1} block compositions.
   - With q = max(Q, E₂, q_{g≥3}):

     |ρ_{a,b}| ≤ K (2 max(1,ω) q/h₀)^n =: δ^n, where K = max(1, (1+e)²/(2max(1,ω)h₀)).
   - **Result.** At θ* = 10.75: δ = 0.0443 / 0.0449 / 0.0463. At θ* = 12.75, δ ≈ 0.006.

## 3. From the restricted ladder to a pointwise rate (PROVED; liminf via a standard LCLT)

**Cap restriction.** Take the lab caps S_± = {τ ∈ W, lab rapidity η ≥ η*, ±n·e ≥ ½}, with legs alternating between the two caps.
- Then n₁·n₂ ≤ ½. So cosh θ ≥ ½ cosh η₁ cosh η₂, and θ ≥ 2η* − ln 8.
- With η* = (θ* + ln 8)/2 = 6.42, every A_k^cap ⊂ A_k.

**Laplace bound.** By Theorem 1 and Lemma U′:

V_ε(τ(X)) ≥ L(X) := Σ_k (ε(1−2δ)²)^k (q₊∗q₋∗⋯)(X), with q_± = h² 1_{S_±} ≥ 0.

By Tonelli, ∫ e^{−zt} L = Σ_k (ε(1−2δ)²)^k ĝ(z)^{k+1}. Here:

ĝ(z) = π ∫_W τ³h² ∫_{η*}^∞ sinh²η e^{−zτ cosh η} dη dτ ≥ (π I_W / z²)(1 − err),

with err = 2e^{−2η*} + zτ₂e^{−η*}/2 + (zτ₂e^{η*})²/8. This uses sinh²η ≥ (e^{2η}/4)(1 − 2e^{−2η*}), cosh η ≤ e^η/2 + e^{−η*}/2, and (1+y)e^{−y} ≥ 1 − y²/2.

So the transform diverges for every z ≤ z_c, where z_c ≥ (1−2δ)√(π I_W ε (1 − err)).

**limsup (PROVED).** V depends only on τ (Poincaré invariance in law) and is locally bounded, so

∫ e^{−zt} V = 4π ∫ τ³ V(τ) K₁(zτ)/(zτ) dτ.

If V(τ) ≤ C e^{aτ} held with a < z_c, this would converge on (a, z_c). Hence lim sup τ⁻¹ ln V ≥ z_c.

**liminf (standard theorem).** At z = z_c the tilted alternating pair-walk satisfies the hypotheses of the multidimensional local limit theorem for densities:
- iid pairs;
- a bounded density;
- exponential moments;
- mean (2μ_t, 0⃗);
- a nonsingular covariance.

Summing the LCLT density over the √T window of step numbers gives L(T, 0⃗) ≥ c T^{−3/2} e^{z_c T}. Hence lim inf τ⁻¹ ln V ≥ z_c.

**Numbers (`rl4_A`).**
- **Window integral.** I_W ≥ 0.1511 / 0.1727 / 0.1961. This is a rigorous lower band from the h-band; the Volterra values are 0.155 / 0.177 / 0.201.
- **Correction.** err = 5e-6 at physical ε.
- **Rate constant.** c_low = (1−2δ)√(πI_W(1−err)) = **0.628 / 0.670 / 0.712**.
- **Comparison at s = 10 km.** c_fail = 0.00975, so c_low/c_fail = **64 / 69 / 73**, i.e. ≥ 64–73 sd e-folds.
- **Comparison at s = 12 km.** The ratio is 71–80.
- **Other window.** W = [0.15, 0.5] gives 0.53–0.60, with ratio 55–62.

## 4. Lemma T: the extended source

### 4.1 Reduction (PROVED)

On A_k with z_1, …, z_{k−1} two-legged:

F_k^J = Σ_{a=0}^{k} G_a E_a.

- E_k = Ψ(z_k) is the node end.
- E_a (a < k) has z_{a+1}, …, z_k interior, with z_k **one-legged**: the hop containing z_k ends at a free point v ≺ z_k, followed by Ψ(v).

### 4.2 Obstruction for an edgeless source (DERIVED)

For |Ψ(v)| ≥ const on the whole past of z_k:
- ∫_v |f′(m(v,u))| ~ (π/2A) ∫ s²|f′| ds, with A = τ(z_k,u)²;
- ∫_{D_k} dA/A diverges logarithmically.

The signed leading coefficient is ∝ ∫ s² f′(πs²/24) ds ∝ M₀ = ∫f ds = 0 (rl2_core: M₀ = M₁ = M₂ = 0). So E_{k−1} is finite only by cancellation, and **no absolute-value bound can prove Lemma T for Gaussian-tailed or infinite-past sources.** A proof there must use the moment conditions. I did not find one.

### 4.3 Lemma T′ (end factor PROVED; constants in `rl4_B`)

**Hypotheses.**
- supp J ⊂ {N·y ≥ 0}, i.e. the source switches on across a spacelike plane Σ. Every compact source that starts at some time satisfies this.
- Turn-on regularity: on a patch of the layer 0 < N·z ≤ a, |J(y)| ≤ κ_J |J(z)| for y ∈ C(z) := J⁻(z) ∩ {N·y ≥ 0}. This holds for any J = g(t)w(x⃗) with g ≥ 0 nondecreasing near the edge and w continuous and nonzero. Jumps and finite- or infinite-order zeros are allowed.

**Proof.** C(z_k) has volume (π/3)t⁴ ≤ (π/3)a⁴. Every v with Ψ(v) ≠ 0 and v ≺ z_k lies in C(z_k). Hence:
- |Ψ(z_k) − J(z_k)| ≤ h_∞ κ_J (π/3)a⁴ |J(z_k)|.
- |Ψ(v)| ≤ κ′|J(z_k)| on C(z_k).
- |E_{k−1}| ≤ (1 + h_∞(π/24)τ₂⁴) ψ(0) (π/3)a⁴ κ′ |J(z_k)|.
- For a ≤ k−2, |E_a| / Π|h| ≤ δ^{k−1−a} C_end a⁴ |J(z_k)|. This uses §2.3 for the two-legged vertices; for a last pair-block it uses only the top-end suppression, (2τ₂/τ₁) e^{−θ} ∫Φ₂.

Together with §2.2:

|F_k^J| ≥ |G_{k−1}| |J(z_k)| [(1−2δ)h₀(1 − O(a⁴)) − O(a⁴)] ≥ ½(1−2δ)h₀ |G_{k−1}| |J(z_k)|

for a ≤ a₀ = **0.36 / 0.36 / 0.36** (κ_J = 1) or **0.31 / 0.30 / 0.30** (κ_J = 2). This is the nonzero end factor. ∎

### 4.4 Geometric step

Var φ(x) ≥ Σ_k ε^k (1−2δ)^{2k−2} (½h₀)² ∫ Π_{i<k} h(ℓ_i)² J(z_k)² 1[ℓ_k ∈ W ∩ cap, z_k ∈ layer]. This is a positive ladder with a positive end weight.

- **Planar edge (J's turn-on translation-invariant along Σ): PROVED.** Integrating the endpoint over the layer gives a 1D renewal in the N-time t_x of the observer above Σ, with interarrival transform ĝ. The tilted interarrival law has a density and a finite mean, so **Blackwell's renewal theorem** gives Var φ(x) ≥ c e^{z_c t_x} as t_x → ∞. Here t_x is exactly the proper time from Σ to x.
- **Finite source (the physical 10 km, 1 Gpc configuration): ARGUED.** The same tilted walk is used, with the 4D LCLT in the frame where x − z* = (τ, 0⃗) for a layer point z*. The finite target (layer ∩ patch) costs only a polynomial factor in τ, so the rate is unchanged. If the patch is chosen on the far side of the source, the proper time from the source's past edge to x is ≳ √(2Ds) for any source that switched on no later than the emission window, so RL3's translation is conservative.

## 5. Against the FIXED readings (TESTS.md, Lane RL4)

- **PASS:** not applicable.
- **FAIL ("both lemmas are proved, so the RL3 lower bound holds and the 1e-19 m bar fails"):**
  - Lemma U is proved in the chaos form U′. RL3b's kernel form is bypassed, not proved.
  - Lemma T is proved as T′ for sources with a spacelike past edge and regular turn-on. For the planar edge this includes the pointwise step; for a finite source the geometric step is a standard-LCLT argument.
  - The resulting rate constant 0.63–0.71 exceeds c_fail = 0.0098 by 64–73×.
- **Worker reading: FAIL (bounded)** to:
  - the Palm two-point variance;
  - edge sources (T′);
  - the rate reading (asymptotic in τ at fixed ε, polynomial prefactor not controlled).
- **Fallback.** If the referee requires Lemma T for edgeless, smooth, everywhere-positive sources, or a written-out LCLT step for the finite source: **INCONCLUSIVE, leaning FAIL**.
- **Against the supervisor's expectation:**
  - "U likely provable with 60 decades of slack": yes. The slack actually used is a factor (1−2δ) per rung with θ* ≈ 11, not 60 decades.
  - "T harder": yes. It closes only for edge sources.

## 6. Flags for the referee

1. **Constants are floating point.** The envelope sups Φ₁ and Φ₂ are grid running-maxima with a Lipschitz pad, and I_W is a trapezoid. None is interval-certified. Margins: δ ≤ 0.05 against the 0.1 needed; c_low/c_fail ≈ 64.
2. **Step factorization (§2.1).** Check that the inter-special-hop P-sums are unrestricted, i.e. that their diamonds contain no inserted point. Also check the δ-identifications u₁ = z_a, v_s = z_b, v_i = u_{i+1}.
3. **Pair-block bound (§2.3.5).** Check the cross-term positivity and the min ≤ geometric-mean step.
4. **Liminf.** It cites the LCLT for densities (iid alternating pairs). The limsup needs no citation.
5. **Lemma T′'s class.** It excludes Gaussian-tailed sources such as RL2's MC source. Whether the physical source has a past edge in the model is a modelling question for the supervisor.
6. **Scope.** Fixed ε, τ → ∞, and exponent and constant only. RL3's flag 3 (prefactor at the physical point) is untouched.
7. **The bound is loose, and consistent with RL3's data (`rl4_C`).**
   - At θ = 4–8 the per-vertex bound is dominated by the crude g ≥ 3 envelope, giving q ≈ 2–60. It is far above RL3-B's measured \|rest/node\| of 1e-3 to 1e-5. This is consistent (bound ≥ data) but not sharp.
   - At θ* = 10.75 the single-vertex ratio bound is ≈ 0.04, against RL3-B's extrapolated ~1e-6.
   - Nothing in the proof needs sharpness. A larger θ* only adds O(e^{−2η*}) to err.

## Files (scratch: `/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C4/RL4/`)

| script | output | content |
|---|---|---|
| `rl4_A_lemmaU_constants.py` | `rl4_A_lemmaU_constants.out` | rigorous h-band on [0, τ₂]; Φ envelopes; Q, E₂, q_{g≥3}; δ(θ*); I_W lower band; c_low; c_fail; two windows |
| `rl4_B_endfactor_turnon.py` | `rl4_B_endfactor_turnon.out` | Lemma T′ end-factor constants and layer thickness a₀ (κ_J = 1, 2) |
| (inline) | `rl4_C_bound_vs_RL3B.out` | per-vertex bound at θ = 4, 5, 6, 8 (comparison with RL3-B) |
| `rl2_core.py` | — | copy of RL2's operator module (coefficients only) |
