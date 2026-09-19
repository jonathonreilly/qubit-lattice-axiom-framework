# lightcone-long-range-order — attempt a5

Worker `w-jonathonsmac4f50-ja59c` (model claude-opus-5). Check script: `check.py` in this directory (exact integer, rational and
symbolic arithmetic; one numerical check, labelled; about 3 s).

- **Order of work.** The plan (route (i), with a reflection whose "plane" is the set of vertical edges) was made before any prior
  material was read.
- **Prior material.** No attempt of this problem existed at claim time. Afterwards I read the round-1 referee report on
  `lightcone-formation:a2` (`probes/work/derive/lightcone-formation/referee_w-jonathonsmac4f50-j4e7c/REPORT.md`). It locates the gap
  exactly: the reflections used all map `A` onto `A`, so a maximizing field stays two-valued on `A`, `B`, and the staggered-twist
  bound `Z(t·1_A) ≤ Z(0)` is missing. This attempt supplies that bound and the full Gaussian domination.

## 1. The statement attempted

**Objects (GIVEN).**

- `Γ_L`, `L` even, has vertices `(x, a)` with `x ∈ (Z/L)³`, `a ∈ {0, 1}`, and edges `(x,0)–(y,1)` with `y − x ∈ N7 = {0, ±e₁, ±e₂, ±e₃}`.
- `μ_L` is the sphere (`n = 3`) Heisenberg ferromagnet on `Γ_L`: weight `exp(β Σ_{edges} s_u·s_v)`, uniform a priori measure on `S²`.
- The stationary law `π_L` of the light-cone formation law is the marginal of `μ_L` on layer 0,
  `π_L(s) ∝ Π_x Z(β|S_x(s)|)` (GIVEN, refereed).
- `A = {(x,0) : |x| even} ∪ {(x,1) : |x| odd}` and `B` = the complement are the two classes of the bipartition (layer × spatial parity).
- `m₀ = (1/N) Σ_x s_{(x,0)}`, `N = L³`.

**Claim.** For every even `L` and every `β > 0`,

`⟨|m₀|²⟩_{π_L} ≥ 1 − (3/(2β)) (G_L + H_L)`, where `G_L = (1/N) Σ_{k≠0} 1/E(k)`, `H_L = (1/N) Σ_k 1/(14 − E(k))`,
`E(k) = 6 − 2Σ cos k_j`, and `k` runs over `(2π/L)(Z/L)³`.

Moreover `G_L ≤ I₀ + (3/(4L)) S₂(L/2) + π²/(16L)` and `H_L ≤ I₂ + (3/4)^L/2`, with:

- `I₀ = ∫ d³k/(2π)³ 1/E(k) ∈ [0.250992, 0.254471]`;
- `I₂ = ∫ d³k/(2π)³ 1/(E(k) + 2) ∈ [0.1409314, 0.1409315]`;
- `S₂(K) = Σ_{m₁,m₂=1}^{K} 1/(m₁² + m₂²)`.

Hence, for every `β > β₀ := (3/2)(I₀ + I₂)` with `β₀ ∈ [0.5879, 0.5931]`, the law `π_L` has long-range order
(`⟨|m₀|²⟩ ≥ c(β) > 0`) on every even torus with `L ≥ L₀(β)`. The explicit bound at `β = 1` is `⟨|m₀|²⟩ ≥ 0.093, 0.217, 0.288, 0.337`
at `L = 12, 24, 48, 100`. The executed value is `|m| = 0.76`, i.e. `0.578`.

**The threshold proved.** Long-range order for `β > 0.5931` (the upper end of the bracket), on all sufficiently large even tori.

## 2. Steps

**S1 (GIVEN).** `π_L` is the layer-0 marginal of `μ_L`, and `μ_L` is invariant under every automorphism of `Γ_L`.

**S2 (PROVED; CHECKED G1).** Take a bond plane between `x_j = c` and `c + 1` (on the torus also between `c + L/2` and `c + L/2 + 1`).
Let `ρ` be the spatial reflection through it and set `θ_P(x, a) = (ρ x, 1 − a)`.

- `θ_P` is an involution.
- It is an automorphism: `ρ` acts on differences as a linear reflection, which maps `N7` onto itself, and the layer swap turns an edge
  from layer 0 to layer 1 into one from layer 1 to layer 0.
- It swaps the halves `Λ_± = {x_j` on one side`} × {0, 1}`.
- An edge crossing between the halves joins `(x, a)` and `(x + e_j, 1 − a)` at a plane, and `θ_P(x, a) = (x + e_j, 1 − a)`. So every
  crossing edge is `{u, θ_P u}`.
- `θ_P` maps `A` onto `A`. This is the round-1 obstruction.

*CHECKED:* all these facts exhaustively on `L = 4, 6`, every plane in every direction.

**S3 (PROVED; CHECKED G1).** The layer swap `σ(x, a) = (x, 1 − a)` with halves `(A, B)`.

- `σ` is an involutive automorphism and maps `A` onto `B` (`a + |x|` changes parity).
- A non-vertical edge `(x,0)–(x ± e_j,1)` has both ends in the same class (`|x|` and `1 + |x| ± 1` have equal parity).
- A vertical edge `(x,0)–(x,1)` joins the two classes, and `σ(x, 0) = (x, 1)`.

So the crossing edges of `(A | B)` are exactly the vertical edges, each of the form `{u, σu}`.

*CHECKED:* exhaustively on `L = 4, 6`, including that `σ`'s crossing edges are exactly the vertical ones.

**S4 (PROVED; CHECKED G1).** Every non-vertical edge crosses the plane of some `θ_P`, and every vertical edge crosses `(A | B)`. So
every edge of `Γ_L` crosses some reflection of the family `R = {θ_P} ∪ {σ}`. *CHECKED* on `L = 4, 6`. *Remark (CHECKED):*
`(x, a) ↦ (x, a + |x| mod 2)` maps `Γ_L` isomorphically onto the bilayer `(Z/L)³ × K₂`:

- in these coordinates the `θ_P` are the ordinary bond reflections acting on both layers;
- `σ` is the swap of the two layers.

**S5 (PROVED) Gaussian domination for all fields.** For `h : V → R³` put
`Z(h) = ∫ Π_u dμ₀(s_u) exp(−(β/2) Σ_{⟨uv⟩} |s_u − s_v − (h_u − h_v)|²)`.
Since `|s_u − s_v|² = 2 − 2 s_u·s_v`, `Z(0)` is the partition function of `μ_L` up to a constant.

*(a) Reflection inequality.* Let `θ ∈ R` have halves `Λ_±` with crossing edges `{u, θu}`, `u ∈ ∂Λ_+`. Write `X_u = s_u − h_u` and
`Y_u = s_{θu} − h_{θu}`. A crossing factor is
`exp(−(β/2)|X_u|²) exp(−(β/2)|Y_u|²) exp(β X_u·Y_u)`.
Expanding `exp(β Σ_u X_u·Y_u) = Σ_I c_I X^I Y^I` with `c_I ≥ 0` (Taylor series in the products `X_u^α Y_u^α`) gives
`Z(h) = Σ_I c_I a_I(h|Λ_+) b_I(h|Λ_−)`. Here `a_I` integrates over the `Λ_+` spins, including their internal edges and the
`exp(−(β/2)|X_u|²)`, and `b_I` likewise over `Λ_−`. `θ` is an automorphism and `μ₀` is invariant, so the `Λ_−` integral taken with the
reflected field `h∘θ` equals `a_I`. Cauchy–Schwarz over `I` with weights `c_I` then gives

`Z(h)² ≤ Z(h⁺) Z(h⁻)`, where `h⁺ = h` on `Λ_+` and `h∘θ` on `Λ_−`, and `h⁻` is the mirror construction.

*(b) A maximizer.* `Z` depends only on the gradients `h_u − h_v`. If some gradient `g` has `|g| > 2`, the corresponding factor is at
most `exp(−(β/2)(|g| − 2)²)`, while every other factor is `≤ 1`. So the supremum over fields with `h(u₀) = 0` is attained. Among the
maximizers choose `h*` with the fewest edges of nonzero gradient.

*(c) Counting.* Let `θ ∈ R` and apply (a) to `h*`.

- In `h⁺`, the internal edges of `Λ_−` repeat those of `Λ_+`, and every crossing edge `{u, θu}` has gradient `h*_u − h*_u = 0`. So
  `n(h⁺) = 2 n_+(h*)` and `n(h⁻) = 2 n_−(h*)`.
- From `Z(h*)² ≤ Z(h⁺)Z(h⁻) ≤ Z(h*)²`, both `h⁺` and `h⁻` are maximizers.
- If `h*` had a nonzero gradient on a crossing edge of `θ`, then `min(n(h⁺), n(h⁻)) ≤ n(h*) − n_cross < n(h*)`, a contradiction.

So `h*` has zero gradient on every crossing edge of every `θ ∈ R`, which by S4 is every edge. `h*` is constant and
`Z(h) ≤ Z(h*) = Z(0)` for all `h`.

*The round-1 lemma.* The round-1 gap is the special case `h = t·1_A`. Apply (a) with `θ = σ`: `h⁺ = t` on `A` and `t` on `σ(A) = B`
(constant), and `h⁻ = 0`. So `Z(t 1_A)² ≤ Z(t) Z(0) = Z(0)²`.

*Numerical (N1, labelled):* on the Ising analogue of `Γ` in one dimension (`L = 4, 6`; `β = 0.3, 1, 2`; 40 digits),
`max Z(h)/Z(0) = 0.734` over random fields and `0.985` over staggered twists. Both are `≤ 1`.

*CHECKED (P1):* the Legendre coefficients of `e^{βt}` are positive (`∫ tʲ P_ℓ ≥ 0`, `ℓ ≤ 8`, `j ≤ 24`), so the crossing kernel is
positive definite on `S²`. (a) needs only the Taylor expansion; P1 is the positivity of the unperturbed measure.

**S6 (PROVED; CHECKED S1) The infrared bound.**

- *Second order.* Expanding `Z(εh) ≤ Z(0)` to order `ε²` (the first order vanishes by rotation invariance) gives
  `⟨(s^α, L_Γ φ)²⟩ ≤ (φ, L_Γ φ)/β` for real `φ`, with `L_Γ` the graph Laplacian.
- *Complex test functions.* By real and imaginary parts, `⟨|(s^α, ψ)|²⟩ ≤ (ψ̄, L_Γ^{−1} ψ)/β` for `ψ ⊥ ker L_Γ`.
- *Spectrum.* In Fourier, `L_Γ(k) = [[7, −A(k)], [−A(k), 7]]` with `A = 1 + 2Σ cos k_j`. Its eigenvectors are `v_± = (1, ±1)/√2`, with
  eigenvalues `E(k)` and `14 − E(k)` (CHECKED symbolically; `14 − E(k) = E(k + π) + 2`).
- *The bound.* With `ŝ_±(k) = Σ_{x,a} e^{ik·x} (v_±)_a s_{(x,a)}`: `⟨|ŝ_+(k)|²⟩ ≤ 3N/(β E(k))` for `k ≠ 0`, and
  `⟨|ŝ_−(k)|²⟩ ≤ 3N/(β(14 − E(k)))` for every `k`.

**S7 (PROVED) Long-range order of `π_L`.**

- *Sum rule.* By Parseval over the orthogonal basis `{e^{ik·x} v_±}` with unit spins, `Σ_{k,±} |ŝ_±(k)|² = N · 2N`.
- *Zero mode.* `ŝ_+(0) = (M₀ + M₁)/√2` with `M_a = Σ_x s_{(x,a)}`. So
  `⟨|M₀ + M₁|²⟩/2 ≥ 2N² − (3N/β)[Σ_{k≠0} 1/E + Σ_k 1/(14 − E)]`, i.e.
  `⟨|(M₀ + M₁)/(2N)|²⟩ ≥ 1 − (3/(2β))(G_L + H_L)`.
- *One layer.* `σ` is an automorphism, so `M₀` and `M₁` have the same law. Then `⟨|M₀ + M₁|²⟩ ≤ 2⟨|M₀|²⟩ + 2⟨|M₁|²⟩ = 4⟨|M₀|²⟩`, hence
  `⟨|m₀|²⟩_{π_L} ≥ 1 − (3/(2β))(G_L + H_L)`.

**S8 (PROVED) Finite-volume sums.**

- *`G_L`, points with every coordinate nonzero.* `1/E` decreases in each `|k_j|`. Give each such grid point the cell of side `2π/L`
  toward the origin in every coordinate. The cells are disjoint, and `1/E` on a cell is at least its value at the point. So these
  points contribute at most `I₀`.
- *`G_L`, points with exactly one zero coordinate* (3 planes). Use `2(1 − cos x) ≥ (4/π²)x²`: each plane contributes at most
  `(1/(16L)) Σ_{m≠0} 1/|m|² ≤ S₂(L/2)/(4L)`.
- *`G_L`, points on an axis* (3 axes). Each contributes at most `(1/(16L)) · 2ζ(2)`.
- *`H_L`.* `1/(14 − E) = (1/8) Σ_n (−c/4)^n` with `c = Σ cos k_j`, `|c| ≤ 3`. The torus moments `(1/N) Σ_k cⁿ = 2^{−n} ·` (closed
  torus walks) equal the `Z³` moments for `n < L` and are at most `3ⁿ` in absolute value. So `|H_L − I₂| ≤ (1/8) Σ_{n≥L} (3/4)ⁿ = (3/4)^L/2`.

**S9 (PROVED; CHECKED T1) The integrals.**

- *Series.* With `x = c/3`, `p_{2m} = ∫ x^{2m}` is the return probability of the simple random walk on `Z³` (odd moments vanish). Then
  `I₀ = (1/6) Σ_m p_{2m}` (monotone convergence on `x^{2m}(1 + x) ≥ 0`), and `I₂ = (1/8) Σ_m (9/16)^m p_{2m}` (after `k → k + π`).
- *Exact terms.* `p_{2m} = b_m/36^m`, with `b_m` from the recurrence
  `n³ b_n = 2(2n−1)(10n² − 10n + 3) b_{n−1} − 36(n−1)(2n−1)(2n−3) b_{n−2}`. It is checked exactly against
  `C(2n,n) Σ_k C(n,k)² C(2k,k)` for `n ≤ 30` and used to `m = 2000`.
- *Tail of `I₀`.* `Σ_{m>M} p_{2m} = ∫ x^{2M+2}/(1 − x²)`.
  - This is `2 ∫_{x ≥ 0} …` by `k → k + π`, and `1/(1 − x²) ≤ 1/(1 − x)` there.
  - On `x ≥ 0`, with `u = 1 − x`: `(1 − u)^{2M+2} ≤ e^{−(2M+2)u}`. Extend to the whole torus and write `1/u = ∫₀^∞ e^{−su} ds`.
  - Each coordinate then gives the factor `e^{−A} I₀(A)`, so the tail is at most `6 ∫_{A₀}^∞ (e^{−A} I₀(A))³ dA`, with
    `A₀ = (2M+2)/3`.
  - From `e^{−z} I₀(z) = (1/π) ∫₀² e^{−zt} (t(2−t))^{−1/2} dt`, split at `t = 1` and use convexity of `(1 − t/2)^{−1/2}` on `[0, 1]`:
    `e^{−z} I₀(z) ≤ (2πz)^{−1/2}(1 + (√2 − 1)/(2z)) + e^{−z}/2`. The bound is also CHECKED against mpmath at four points.
  - Result: the tail is at most `≈ 0.0209` at `M = 2000`.
- *Tail of `I₂`.* It is geometric: at most `(1/8)(9/16)^{M+1}/(7/16)`.
- *Result.* `I₀ ∈ [0.250992, 0.254471]` (the classical value `0.2527310` lies inside), `I₂ ∈ [0.14093149, 0.14093149]`, and
  `β₀ ∈ [0.58789, 0.59310]`. *Numerical:* the torus sums at `L = 24, 48` give `(3/2)(G_L + H_L) = 0.5764, 0.5834`.

## 3. Routes (ii) and (iii)

Route (i) closes the gap, so (ii) and (iii) were not needed.

- **Route (ii).** The layer-symmetric infrared bound alone controls only the `E`-band. The sum rule also contains the odd band's total
  weight `(N/2) Σ_x ⟨|s_{(x,0)} − s_{(x,1)}|²⟩`, i.e. the vertical-edge energy, and exchangeability of the layers does not bound it.
  So route (ii) reduces to bounding that energy, which is what S3/S5 supply.
- **Route (iii).** Not attempted.

## 4. What is not claimed, and what would sharpen it

- **Not claimed.**
  - The stationary law's uniqueness, or convergence of the formation process to `π_L`.
  - Anything for the six-axis menu. That is a separate problem (`lightcone-sixaxis-order`), and its identification of the stationary law
    is not established here. S5–S7 use only unit-length records, the Taylor expansion of (a), `⟨s⟩ = 0` on the torus and the sum rule,
    so they may transfer, but that is not checked.
  - Infinite-volume states beyond `⟨|m₀|²⟩ ≥ c` on large tori.
- **Sharpening.** `β₀` is an infrared-bound threshold, not the transition. A sharper tail for `I₀` narrows the bracket to the classical
  `(3/2)(0.2527310 + 0.1409315) = 0.590494`.
- **Other dimensions.** S2–S7 use only that the stencil is symmetric and contains the self-edge, so they hold for the `(2d+1)`-stencil
  light cone in every `d`. The resulting bound is useful only when `G_L` stays bounded, i.e. `d ≥ 3`. In `d = 2`, `G_L ~ log L` and the
  bound gives nothing; no statement about order in `d = 2` is made.
