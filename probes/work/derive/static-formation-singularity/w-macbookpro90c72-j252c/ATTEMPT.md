# J:derive:static-formation-singularity:a2 — w-macbookpro90c72-j252c

**Provenance.** This attempt was written by three sessions holding this claim:
- `check.py` part 1 (S0–S2, lines 1–236) was written by an earlier claude-opus-5 session;
- the plan for part 2 was written by a claude-opus-5-5 session;
- `check.py` part 2 (S3–S8, lines 237–853) and this file were written by claude-opus-5-5.

`python3 check.py` prints 11 `ok` lines with `FAIL` empty, and exits 0 in about 13 s. Every finite claim below is
an exact integer or `Fraction` identity or inequality in it. Floats (numpy) are used only to locate positive test
vectors and to pick a starting `L`; the inequalities built on them are then checked exactly.

**Definitions** are those of the census note on `main`,
`docs/ADMISSIBILITY_FORMATION_ORDER_MENU_ORDER_MIXTURE_MONOTONE_BOX_AND_CUBE_CENSUS_BOUNDED_THEOREM_NOTE_2026-09-13.md`
(Premises, lines 91–150; Theorem 2, line 312):
- the six-value menu with antipode `s ↦ s^1`;
- the class-(P) rule at `(p,q,r) = (3,1,2)`, i.e. `φ(s,t) = 3` equal, `1` antipodal, `2` orthogonal;
- the static law `μ(v) = W(v)/Z`, with `W = ∏_{edges} φ`;
- the formation law of an order `σ`, `ν_σ(v) = ∏_k r(v_{x_k} | recorded neighbours)`, with
  `r(s|A) = ∏_{y∈A} φ(s,v_y) / Nf(v|A)` and `Nf(A) = Σ_s ∏_{t∈A} φ(s,t)`;
- the monotone-box class: linear extensions of the product order from a corner.

An **adapted** law chooses the next site as any function of the values already formed, as in round 1 and in
a1 §0. `H` is the closed convex hull of the adapted laws on the window. On a finite window there are finitely many
deterministic adapted strategies, so `H` is a polytope. Randomised strategies and mixtures of orders lie in `H`.

`Nf(∅) = 6` and `Nf({t}) = 12`. The pair value `N₂(a,b) = Nf({a,b})` is 26 if `a = b`, 24 if orthogonal and 22 if
antipodal.

`TV` is total variation, `BC(P,Q) = Σ √(PQ)` the Bhattacharyya coefficient and `KL` the relative entropy.

## 1. Statement attempted

**(a) Total variation to the hull, growing with the number of cycles.**
1. **(S3)** On the `2×2` plaquette:
   - `TV(μ, H) = 30457/2431728` exactly;
   - `1_E` is an optimal `[0,1]`-valued test, where `E` = {one diagonal pair equal, the other not antipodal}.
2. **(S8)** On the `2×3` ladder:
   - `TV(μ, H) = 4120449306433/238517136000000` exactly;
   - this is strictly smaller (< 0.874×) than `TV(μ, conv{ν_σ : all 720 fixed orders}) = TV(μ, monotone hull) = 812090431/41067000000`;
   - so value-dependent orders come strictly closer to the static law than every mixture of fixed orders. On the
     `2×2` they do not.
3. **(S4)** On `m` disjoint plaquettes:
   - for every nondecreasing `G : {0,1}^m → [0,1]`, `sup_{H_m} E_ν G(1_E(copy_1),…,1_E(copy_m)) = Ĝ(q,…,q)`, where `q = 1619/5616` and `Ĝ` is the multilinear extension of `G`;
   - hence `TV(μ^m, H_m) ≥ TV(Bin(m,p), Bin(m,q)) ≥ 1 − β^m`, with `p = 521/1732` and `1 − β ≥ 9.43777·10⁻⁵`;
   - `TV ≥ 1/2` at `m = 2410`, while `TV < 1/2` for every `m ≤ 952`. The threshold lies in `[953, 2410]`; a1 had `[496, 9268]`.

**(b) Relative entropy and singularity for corner (monotone) orders on strips and the tube.**
- Windows: the `w×L` strips (`w = 2, 3`) and the `2×2×L` tube.
- Exact certificates: `BC(μ_L, ν_L)² ≤ K·r2^{L−1}`, with the certified `1 − r2` and `K` in the table below. Hence:
  - `KL(μ_L‖ν_L) ≥ (L−1)(1−r2) − log K` for each corner law;
  - `TV ≥ 1/2` against the whole monotone hull for `L ≥ 4624, 2272, 1019`;
  - on the half-infinite strip and tube, every static Gibbs law is mutually singular to every corner-order formation law, with KL density at least `(1−r2)/w` per site (`w = 4` for the tube).
- `Z²` and `Z³` themselves are not redone here; see a3 and a1 (§3).

**(c) The most distinguishing observable.**
- On the `2×2`, the optimal test against the full hull is `1_E`, a function of the two diagonal (next-nearest-neighbour) relations.
  The plaquette four-point function, 81/3464 against 9/416, is 7.16× weaker (a1).
- On the `2×2×2` cube:
  - one corner law has `TV = 1182193085/23402354976` (a1's value);
  - the all-equal event has `μ = 177147/387917824` against `ν = 6561/22497280`;
  - the TV-closest point of the monotone hull is the uniform mixture of the 8 corner laws, at
    `TV = 3205622113713065/81441318629518848`;
  - that TV is attained by `E₈ = {μ > ν̄₈}`, with `μ(E₈) = 278186119/581876736` and `ν_k(E₈) = 377272857433/859933780992` for every corner `k`.

**Route no-go (S7).** The pointwise envelope `ν ≤ W/Ŷ` is valid for all of `H`, but on `2×L` strips the bound it gives
tends to 0. It therefore cannot give a uniform full-hull bound on long strips.

## 2. Steps

### Tools (PROVED; each proof is complete)
- **T1.** `TV ≥ 1 − BC`. Since `1 − TV = Σ min(P,Q)` and `min(a,b) ≤ √(ab)`.
- **T2.** `TV ≤ √(1 − BC²)` (Le Cam's inequality).
  - `TV = ½Σ|√P−√Q|(√P+√Q)`.
  - By Cauchy–Schwarz this is at most `½·√(2−2BC)·√(2+2BC)`.
- **T3.** `BC` is multiplicative on products: `Σ_{x,y} √(P(x)P'(y)Q(x)Q'(y)) = BC(P,Q)·BC(P',Q')`.
- **T4.** `BC(μ, Σλ_kν_k) ≤ Σ_k √λ_k·BC(μ,ν_k) ≤ √K·max_k BC(μ,ν_k)`.
  - The first inequality is `√(Σa_k) ≤ Σ√a_k`, applied termwise.
  - The second is Cauchy–Schwarz: `Σ√λ_k ≤ √(KΣλ_k)`.
- **T5.** `KL(P‖Q) ≥ −2 log BC(P,Q)`.
  - By Jensen, `−KL = 2E_P log √(Q/P) ≤ 2 log E_P √(Q/P)`.
  - All laws here are strictly positive (`φ ≥ 1`), so no support issue arises.
- **T6.** The Bellman sup over the hull, for any `f ≥ 0`.
  - Set `V(v) = f(v)` on complete configurations, and `V(π) = max_x Σ_s r(s|π,x)·V(π+x:s)` on a partial state `π`.
    Here `r(s|π,x) = ∏_{formed y∼x} φ(s,v_y)/Nf(formed neighbour values)`.
  - Upper bound. Take any strategy, randomised or history-dependent. For every choice `x`,
    `E[V(π_{t+1}) | history] = Σ_s r·V(π_t+x:s) ≤ V(π_t)`. So `E_ν f = E V(π_n) ≤ V(∅)`.
  - Attainment. The argmax strategy attains `V(∅)`.
  - `ν ↦ E_ν f` is linear, so `sup_H E_ν f = V(∅)`.
  - Hence for every `ν ∈ H` and every test `f` with values in `[0,1]`: `TV(μ,ν) ≥ E_μ f − V(∅)`.
- **T7.** Symmetric mixtures.
  - Setting: a group `Γ` of window automorphisms fixes `μ` and permutes the laws `{ν_k}` transitively.
  - Claim: the uniform mixture `ν̄` minimises `TV(μ,·)` on `conv{ν_k}`.
  - Proof: `TV(μ, ν∘g) = TV(μ,ν)`. Averaging over `Γ` maps every `Σλ_kν_k` to `ν̄`. `TV(μ,·)` is convex.
- **T8.** Initial segments.
  - Setting: `D` is an initial segment of `σ`.
  - Claim: the marginal of `ν_σ` on `D` is the formation law of `σ|_D` on the window `D`.
  - Proof: sum out the later sites from last to first; each kernel sums to 1, and no kernel of a site in `D` reads a later site.
  - For a corner order, the first `L` columns of a strip form such a segment.

### S0 — constants. CHECKED (part 1)
`Z1 = 12`; `N₂ ∈ {22, 24, 26}`; `N₃ ∈ [44, 60]`; `N₄ ∈ [80, 146]`.

### S1 — the likelihood identity. PROVED; CHECKED (part 1)
- `ν_σ(v) = W(v)/Y_σ(v)`, with `Y_σ(v) = ∏_k Nf(v|A_k)`.
  - Each edge's `φ` enters exactly once, at its later endpoint (a1 S1).
  - CHECKED on all 24 orders of the 4-cycle, with `Σ_v W/Y = 1`.
- Over fixed orders, `min TV(μ,ν_σ) = 455/31176` (a3's value) and `max = 37/1299`.

### S1b — the identity for adapted laws. PROVED; CHECKED (part 1)
- Along `v`, an adapted strategy realises an order `σ(v)`, so `ν(v) = W(v)/Y_{σ(v)}(v)`.
- CHECKED for 4 value-dependent strategies on the 4-cycle and on the `2×3` ladder: numerator `= W` and `Σ_v W/Y = 1`.

### S2 — forests. PROVED; CHECKED (part 1)
- On a tree with a connected order, every non-root site has exactly one recorded neighbour. So `Y = 6·12^{n−1} = Z` and `ν = μ`.
  - CHECKED on path3, P4, star4, tree5 and comb6.
- A non-connected order breaks this: star4 leaves-first gives `TV = 5/144`.
- Hence every separation needs cycles.

### S3 — exact TV to the full hull on the `2×2`. CHECKED; conclusion PROVED
Setup:
- Sites `0=(0,0)`, `1=(0,1)`, `2=(1,1)`, `3=(1,0)`.
- The diagonal pair values are `N1 = N₂(v0,v2)` and `N2 = N₂(v1,v3)`.
- The corner laws are `ν_A` (corners 0 and 2, `Y_A = 864·N2`) and `ν_B` (corners 1 and 3, `Y_B = 864·N1`).
  CHECKED, including that opposite corners give equal `Y`.

Class weights by `(rel(v0,v2), rel(v1,v3))`: 876, 2688 ×2, 492 ×2, 9216, 1920 ×2, 492. CHECKED; the sum is 20784.

With `ν̄ = ½(ν_A+ν_B)`:
- `E = {μ > ν̄} = {1/N1 + 1/N2 < 1728/20784} = {N1,N2 ∈ {26,26}, {26,24}}` (unordered). CHECKED.
- `μ(E) = 521/1732` and `ν_A(E) = ν_B(E) = 1619/5616`. CHECKED.
- `TV(μ, ν̄) = 30457/2431728 = μ(E) − ν̄(E)`, by the full `6⁴` sum. CHECKED.
- The Bellman recursion of T6 over the `7⁴` partial states gives `sup_H ν(E) = V(∅) = 1619/5616`. CHECKED:
  - exactly, via `V(π)·L^{#unformed} ∈ ℤ`;
  - with the Bellman equality re-verified at every state.

**Conclusion (PROVED).**
- `TV(μ,ν) ≥ μ(E) − 1619/5616 = 30457/2431728` for every `ν ∈ H` (T6).
- `ν̄ ∈ H` attains it.
- So `TV(μ, H_{2×2}) = 30457/2431728`, and `1_E` is an optimal test among all `[0,1]`-valued tests.

Relation to a1: a1 had this `E` and this lower bound (a1 S7), and the bracket `[30457/2431728, 455/31176]`. The
attainment by `ν̄`, which closes the bracket, is new. Optimality of `1_E` therefore holds among all tests, not only
among the 64 events measurable in the diagonal statistic.

### S4 — `m` disjoint plaquettes. PROVED; numbers CHECKED
`H_m` is the hull of adapted laws on the disjoint union. A strategy may interleave the copies and read every formed
value.

**Multi-affine Bellman (PROVED).**
- Let `q(·)` be the single-copy value function of T6 for `f = 1_E`, so `q(∅) = q = 1619/5616`.
- Take `G` nondecreasing, and put `V(π) = Ĝ(q(π_1),…,q(π_m))`.
- `Ĝ` is affine in each argument and nondecreasing on `[0,1]^m`:
  - `∂_cĜ` is the multilinear extension of `G(…,1,…) − G(…,0,…) ≥ 0`.
- Forming a site `x` in copy `c` uses a kernel that reads only `π_c`, because the copies are disjoint. So
  `Σ_s r·V(π+x:s) = Ĝ(…, Σ_s r·q(π_c+x:s), …) ≤ Ĝ(…, q(π_c), …) = V(π)`:
  - the equality uses affinity and `Σ_s r = 1`;
  - the inequality uses the single-copy Bellman inequality and monotonicity of `Ĝ`.
- At complete states `V = G(indicators)`. So `sup_{H_m} E_ν G ≤ Ĝ(q,…,q)`, as in T6.
- Equality holds: run copy 1's optimal strategy to completion, then copy 2's, and so on. The indicators are then
  i.i.d. Bernoulli(`q`).

**Consequences.**
1. Tail tests. For `G = 1{Σ ≥ k}`: `sup_{H_m} ν(#E ≥ k) = P(Bin(m,q) ≥ k)`. Under `μ^m`, `#E ~ Bin(m,p)`.
2. The best tail test (PROVED). The ratio `Bin(m,p)(j)/Bin(m,q)(j)` is increasing in `j` because `p > q`. Hence
   `max_k [P(Bin(m,p)≥k) − P(Bin(m,q)≥k)] = TV(Bin(m,p),Bin(m,q))`, attained at `k* = min{j : Bin_p(j) ≥ Bin_q(j)}`.
   So `TV(μ^m, H_m) ≥ TV(Bin(m,p), Bin(m,q))`.
3. The exact threshold of this bound (CHECKED).
   - At `m = 2410`, `k* = 710` and the difference is `≥ 1/2`.
   - At `m = 2409` the difference at `k*` is `< 1/2`.
   - All tails are exact integers, via `T_{j−1} = T_j·j·(c−a)/((m−j+1)·a)`.
   - Every comparison is cross-multiplied.
4. Closed form (PROVED; β CHECKED).
   - By T1, `TV(Bin,Bin) ≥ 1 − BC_b^m`, with `BC_b = √(pq) + √((1−p)(1−q))` (binomial theorem).
   - An exact ceiling gives `BC_b ≤ β` with `1 − β ≥ 9.43777·10⁻⁵`.
   - This closed form alone reaches `1/2` from `m = 7345`.
5. Monotonicity in `m` (PROVED).
   - Let `ν ∈ H_{m+1}`. Its marginal on the first `m` copies is the law of a randomised adapted strategy on `m` copies.
   - That strategy simulates copy `m+1` with private randomness. Condition on a pre-drawn random table to make it deterministic.
   - So the marginal lies in `H_m`, and `TV(μ^{m+1}, H_{m+1}) ≥ TV(μ^m, H_m)`.
6. Converse. `ν̄^{⊗m} ∈ H_m`, as a uniform mixture of the `2^m` concatenated corner orders.
   - By T2 and T3, `TV(μ^m, H_m) ≤ √(1 − BC(μ,ν̄)^{2m})`.
   - Here `BC(μ,ν̄) = Σ_classes W·√((N1+N2)/(1728·Z·N1·N2))`.
   - Exact floor and ceiling square roots at `10^{−30}` give:
     - `BC^{1904} > 3/4`, so `TV < 1/2` for all `m ≤ 952`;
     - `BC^{1906} ≤ 3/4`, so this route stops at 953.
7. **Result.**
   - `TV(μ^m, H_m) ≥ 1/2` iff `m ≥ m*` (by 5), with `953 ≤ m* ≤ 2410`.
   - a1 had `[496, 9268]`; a3 had 80237 for the upper end.
   - a1's product lemma (S3(i)) and a3's DP product lemma are the special cases `G = ∏ h(b_i)` and `θ^{Σb_i}`.

### S5 — corner orders on strips and the tube. PROVED; numbers CHECKED
**Setup.** A `w×L` strip with `site = w·i + j` (column `i`, row `j`), in the column-major corner order from site 0.
For a column transition `t → s`:
- `T[t][s] = intra(s)·∏_j φ(t_j,s_j)`, with `intra(s) = ∏_j φ(s_{j−1},s_j)`;
- `den(t,s) = ∏_{j≥1} N₂(t_j, s_{j−1})`.

Then:
- `W = intra(col 0)·∏ T`, so `Z_L = u₀ᵀT^{L−1}1` with `u₀ = intra`;
- `Y = 6·12^{w−1}·∏_{i≥1} 12·den`.

This representation is CHECKED against the generic `predlist` computation on every configuration of the `2×2`,
`2×3` and `3×2` windows. The initial-segment fact T8 is CHECKED once: the `2×3` corner law, summed over its last
column, is the `2×2` corner law.

**The tube** (`2×2×L`, `site = 4i+2a+b`, slice order `00, 01, 10, 11`):
- the first slice gives `Y₀ = 864·N₂(s01,s10)`;
- each later slice gives `12·N₂(s00,t01)·N₂(s00,t10)·N₃(s01,s10,t11)`;
- the corner order's recorded-neighbour sets are CHECKED to be exactly the lower neighbours on the `2×2×3` tube.

**BC formula (PROVED).** Write `T̃ = T/√den` entrywise and `ũ₀ = u₀` (for the tube, `intra/√den0`). Then
`BC(μ_L, ν_L)² = (ũ₀ᵀT̃^{L−1}1)² / (const0·12^{L−1}·u₀ᵀT^{L−1}1)`, with `const0 = 6·12^{w−1}` (864 for the tube).

**Certificate (PROVED).** Take positive integer vectors `u, v`.
- Set `λ_low = min_t (Tu)_t/u_t`. Then `u₀ᵀT^{L−1}1 ≥ λ_low^{L−1}(u₀·u)/umax`.
- Set `ρ̃_up = max_t (Ãv)_t/(D·v_t)`, where `Ã = ⌈D·T̃⌉` entrywise and `D = 10^15`. Then `T̃ ≤ Ã/D`, so
  `ũ₀ᵀT̃^{L−1}1 ≤ ρ̃_up^{L−1}(ũ₀·v)/vmin`.
- So `BC² ≤ K·r2^{L−1}`, with `r2 = ρ̃_up²/(12λ_low)` rounded up at `10^{−12}` and
  `K = [(ũ₀·v)/vmin]²·umax/(const0·(u₀·u))`.
- Sanity (CHECKED): `w = 1` is a path, and there `r2 = 1` and `K = 1` exactly.

**Numbers (CHECKED).**

| window | `1 − r2 ≥` | `K ≤` | certificate gives `TV ≥ ½` vs one corner law, from `L =` | vs the monotone hull, from `L =` | `TV ≥ 0.99` vs the hull, from `L =` |
|---|---|---|---|---|---|
| `2×L` | `6.05795792·10⁻⁴` | 1.0289 | 2336 | 4624 | 17535 |
| `3×L` | `1.245343112·10⁻³` | 1.0583 | 1159 | 2272 | 8551 |
| `2×2×L` | `3.511679839·10⁻³` | 1.1224 | 428 | 1019 | 3244 |

- Each `L` is the first at which the exact certificate passes; `L − 1` fails.
- The hull column uses T4 with `K_h = 4` corners (8 for the tube):
  - `TV ≥ 1 − BC ≥ 1 − √K_h·BC_1`, so `TV ≥ ½` when `BC_1² ≤ 1/(4K_h)`;
  - `BC_k = BC_1` for every corner `k`, because the reflections of the window fix `μ` and permute the corners transitively.
- The cycle rank is `(w−1)(L−1)` for strips and `4L−3` for the tube. So these are `TV` bounds, against the whole
  monotone hull, that grow with the number of independent cycles.

**KL (PROVED from T5).**
- `KL(μ_L‖ν_L) ≥ −log(K·r2^{L−1}) ≥ (L−1)(1−r2) − log K`.
- So the density is at least `(1−r2)/w` per site. For comparison, on `Z²` a3 had `1.38·10⁻⁶` per site and a1 had
  `min D = 537719/129443808050`. Strips are not `Z²`: §3.

**Infinite volume (PROVED).** Work on the half-infinite strip or tube, with ν the corner order from the finite end
(column-major). The order is ω-type, since every site has finitely many predecessors.
1. `ν` restricted to the first `L` columns is `ν_L` (T8).
2. Let `μ^∞` be any Gibbs (DLR) law of `W`. Condition on the configuration beyond the first `L` columns; the conditional
   marginal on the first `L` columns is `∝ W_L(v)·h(v_{L−1})`.
   - Here `h(t) = Σ_x M[t][x]·g(x)`, with `g ≥ 0` and `M = T` or `M = ∏_jφ(t_j,x_j)`.
   - `M[t][x]/M[t'][x] ≤ 3^w`, so `h(t)/h(t') ≤ 3^w`.
   - Hence `μ^∞|_L ≤ 3^w·μ_L` (`3⁴` for the tube). No uniqueness or Perron–Frobenius theorem is needed.
3. So `BC(μ^∞|_L, ν_L) ≤ 3^{w/2}·√(K·r2^{L−1})`, which is summable in `L`.
4. Let `A_L = {μ^∞|_L > ν_L}`, a cylinder event. Then `μ^∞(A_L^c) ≤ BC` and `ν(A_L) ≤ BC`, since on each set the
   smaller law is `≤ √(μν)`.
5. By Borel–Cantelli (`P(limsup B_L) ≤ Σ_{L≥N} P(B_L) → 0` when `Σ_L P(B_L) < ∞`):
   - `μ^∞(liminf A_L) = 1`, because `A_L^c` occurs only finitely often `μ^∞`-a.s.;
   - `ν(liminf A_L) ≤ ν(limsup A_L) = 0`.
   - So `μ^∞ ⊥ ν`.
6. The same holds for every mixture of the corner laws at the finite end: 2 corners for strips, 4 for the tube.
7. `liminf_L KL(μ^∞|_L‖ν_L)/(wL) ≥ (1−r2)/w`.

### S6 — the `2×2×2` cube. CHECKED; hull statement PROVED
- The lex order is the corner order. Its recorded-neighbour sets are `1:{0}`, `2:{0}`, `3:{1,2}`, `4:{0}`, `5:{1,4}`,
  `6:{2,4}`, `7:{3,5,6}`. CHECKED.
- `Y = 10368·N₂(v1,v2)·N₂(v1,v4)·N₂(v2,v4)·N₃(v3,v5,v6)` and `Z = 6982520832`.
  - Sum out `v0` (giving `N₃(v1,v2,v4)`) and `v7` (giving `N₃(v3,v5,v6)`).
  - `Σ ν = 1` and `TV = 1182193085/23402354976` = a1's value. Both are exact over `6⁶` terms, grouped by `Y`.
- All-equal event: `μ = 177147/387917824` against `6561/22497280`.
- The 8 coordinate reflections `a ↦ a ⊕ m` fix `μ` and act simply transitively on the corner laws, so
  `ν_m(v) = W(v)/Y(v∘g_m)`. By T7 the uniform mixture `ν̄₈` is the TV-closest point of the monotone hull. There is also
  a direct certificate: `ν_k(E₈)` is the same for all 8 corners, so every mixture `ν` has `ν(E₈) = ν_1(E₈)` and
  `TV(μ,ν) ≥ μ(E₈) − ν̄₈(E₈)`.
- The exact values, computed in int64 over the `6⁷` configurations with `v0 = 0` (times 6 by value symmetry), grouped
  by the 8-tuple of `Y`'s:
  - `TV(μ, monotone hull) = 3205622113713065/81441318629518848 ≈ 0.0394`, against `≈ 0.0505` for one corner law;
  - `μ(E₈) = 278186119/581876736`;
  - `ν_k(E₈) = 377272857433/859933780992`.

### S7 — the pointwise envelope: the step that fails. PROVED; CHECKED
**The bound (PROVED).**
- Every `ν ∈ H` satisfies `ν(v) ≤ W(v)/Ŷ(v)`, where `Ŷ` is the minimum of `Y_σ(v)` over all orders (S1b). Mixtures preserve this.
- Hence `TV(μ,H) ≥ E_μ(1 − Z/Ŷ)^+`.
- `Ŷ` comes from the subset DP `g(S) = min_x g(S∖x)·Nf(v on N(x)∩(S∖x))`.

**On small windows (CHECKED).**
- On the `2×2`, `Ŷ = min(36n², 864n)` at `n = min(N1,N2)`, and the envelope is `2555/810576 < 30457/2431728`. So it is lossy.
- On the `2×3`, `Ŷ(all equal) = 7008768 > Z = 6000000`, so the envelope is positive.

**No-go on `2×L`.**
- Choosing per column the cheaper of the two row orders gives
  `Ŷ ≤ Ŷ_col = 72·∏_{i≥1} 12·min(N₂(t₁,s₀), N₂(t₀,s₁))`.
- `(1−x)^+ ≤ 1/x`, so envelope `≤ E_μ[Ŷ_col/Z_L] = 72·u₀ᵀ(T∘G)^{L−1}1/Z_L²`.
- The S5 machinery certifies `ρ_up(T∘G) < 0.980098·λ_low²` exactly. So the envelope is `≤ C·0.980098^{L−1} → 0`.

**This is the first step that fails** for a full-hull bound on long strips (§3).

### S8 — the `2×3` ladder: monotone, fixed-order and full adapted hulls. CHECKED; conclusions PROVED
**Monotone hull.**
- The 4 corner laws are images of `ν_0` under the 4 reflections; by the census note's Theorem 2(b), `ν_0 = ν_5`.
- `ν̄₄` = the uniform mixture. `TV(μ, ν̄₄) = 812090431/41067000000 = μ(E₄) − ν̄₄(E₄)`, with `E₄ = {μ > ν̄₄}`. CHECKED.

**Fixed-order hull.**
- `max` over all 720 orders (98 distinct recorded-neighbour structures) of `ν_σ(E₄)` is `1007405/2628288 = ν̄₄(E₄)`. CHECKED.
- Hence every mixture of fixed orders has `TV ≥ μ(E₄) − ν̄₄(E₄)`, and `TV(μ, conv{fixed orders}) = 812090431/41067000000` (PROVED).

**Full adapted hull.**
- *Upper bound* (CHECKED). Each of 19 strategies works as follows:
  - it forms row 0 as the path `0,1,2`, with factor `6·12·12`;
  - it then chooses the first site `k` of row 1 from `(v0,v1,v2)`, and the second from `(v0,v1,v2,v_k)`;
  - `Y` is then one of `12·N₂(v1,v3)N₂(v2,v4)`, `144·N₃(v1,v3,v5)`, `12·N₂(v0,v4)N₂(v2,v4)` or `12·N₂(v1,v5)N₂(v0,v4)`, times 864.

  The strategies are tabulated in `CODES`, one entry per class of `(v0,v1,v2)` under the 48 value maps.
  - Each choice reads formed values only, so each is an adapted strategy.
  - check.py computes each law exactly along the order it realises, and checks `Σ W/Y = 1`.

  The mixture `ν* = Σ λ_i·¼Σ_g ν_i∘g` uses the weights `LAM` (positive, summing to 1), with `g` running over the 4
  reflections. It is in `H` and has `TV(μ,ν*) = 4120449306433/238517136000000`.
- *Lower bound* (CHECKED). Define the test `f*`:
  - `f* = 1` on `{μ > ν*}` and `0` on `{μ < ν*}`;
  - on the 29 classes where `μ = ν*`, `f*` takes the listed values in `[0,1]` (18 of them fractional).

  The exact Bellman DP of T6 over the `7⁶` states gives `sup_H E_ν f* = 6053681639/15265096704`, and
  `E_μ f* − sup_H E_ν f* = 4120449306433/238517136000000`.
- **Conclusion (PROVED).**
  - `TV(μ, H_{2×3}) = 4120449306433/238517136000000 ≈ 0.017275`, strictly below the fixed-order value `≈ 0.019775`.
  - So value-dependent orders come strictly closer to the static law than every mixture of the 720 fixed orders.
  - On the `2×2` the two values coincide (S3).
- *How the data were found* (not part of the claim):
  - a float double-oracle: an LP over mixtures, alternated with an exact-structure Bellman best response, converged in 49 rounds;
  - an exact solve of the primal and dual square systems on its support.

  The certificate is self-contained: any error in `CODES`, `LAM` or the tied values would make the two exact bounds
  differ, and check.py would FAIL.

## 3. Where the route fails

The goal behind (a) is a full-hull TV bound that grows with the number of cycles on connected windows. This route
reaches it only for disjoint cycles (S4). **The first step that fails is S7.**
- The only full-hull tool that applies to every window, the pointwise envelope, gives a bound that tends to 0 on `2×L` strips.
- S8 shows why the monotone-hull certificates of S5 do not transfer: on the `2×3` the full hull is strictly closer to
  `μ` than any mixture of fixed orders. Any full-hull bound on strips must therefore beat value-dependent strategies.
  Symmetry and corner mixtures are not enough.

Part (b) is proved here only on quasi-one-dimensional windows (strips and the tube) and for corner orders. For `Z²`
and `Z³`:
- a3 gives `h ≥ c₂/3` with `c₂ = 19/4604256`, and `h ≥ c₃/4`;
- a1 gives `min D = 537719/129443808050` on `Z²`, and 21.4× a3's rate on `Z³`.

The strip densities of S5 (`3.0·10⁻⁴` to `8.8·10⁻⁴` per site) are about two orders of magnitude above those `Z²`
bounds. This suggests the `Z²` constants are far from sharp, but proves nothing about `Z²`.

## 4. What would finish it
- **Full hull on strips.** Needed: a Bellman supersolution with a transfer structure, for overlapping plaquettes.
  - Whether the full-hull TV on `2×L` tends to 1 is open. S8 fixes what such a route must beat.
  - An exact `2×4` or `3×3` value by the S8 method (double-oracle, then an exact certificate) would show the trend.
- **Uniform-in-width certificates.** The S5 transfer bound with `w → ∞`, or a block/spacing argument, would give `Z²`
  and `Z³` densities of the strip order.
- **Closing `[953, 2410]`.** The E-count tests reach `TV(Bin(m,p),Bin(m,q))`; tests that use more than the `E`
  indicators, or a converse mixture closer than `ν̄^{⊗m}`, would narrow it.
- **The cube's full hull.** The Bellman DP over `7⁸` states: the S8 method with value symmetry.

## Credits (paths on `origin/ai/probes`)
- a1 = `w-macbookpro90c72-je8fe` (issue #8517):
  - log `logs/probes/J:derive:static-formation-singularity:a1/w-macbookpro90c72-je8fe__4b07929d__20260920T134144Z.json`;
  - attempt `probes/work/derive/static-formation-singularity/w-macbookpro90c72-je8fe/ATTEMPT.md`.
- a3 = `w-jonathonsmac4f50-ja5a1` (issue #8481):
  - log `logs/probes/J:derive:static-formation-singularity:a3/w-jonathonsmac4f50-ja5a1__24777d06__20260919T201444Z.json`;
  - attempt `probes/work/derive/static-formation-singularity/w-jonathonsmac4f50-ja5a1/ATTEMPT.md`.
