# uniqueness-up-2: derivation attempt 3 of 4

Worker `w-jonathonsmac4f50-j96fc` (claude-opus-5), unit `J-derive-uniqueness-up-2-a3`.

Objects are those of blocks 08 and 28 (PRs #8138, #8172), as restated in round 1's criterion `probes/work/derive/uniqueness-region-up/w-jonathonsmac4f50-j1ba5/ATTEMPT.md`:
- the six-axis menu `M = {±e₁, ±e₂, ±e₃}` with `φ = p, q, r` for equal, antipodal and orthogonal pairs, here on `(p, 1, 2)`;
- the level automaton `r(s | a₁, a₂, a₃) = Π_j φ(s, a_j)/Z`, with the records of a level drawn independently given the previous level;
- the ground metric `ρ = 1` (orthogonal) and `α` (antipodal), with `1 ≤ α ≤ 2`;
- `κ(w, w'; u₁, u₂) = W_ρ(r(·|w, u₁, u₂), r(·|w', u₁, u₂))/ρ(w, w')`;
- the 56 achievable laws `𝒜`.

**Provenance and independence.** The averaged-Wasserstein criterion that this attempt refines is my model family's own round-1 attempt (`j1ba5`, refereed as a partial by grok, `jeff4`). grok's round-1 attempt a1 extended it to `p = 5.11`, and a claude-opus-5 referee (`j7b64`) re-checked that. So this attempt builds on a same-family result. No other round-2 attempt was on `origin/ai/probes` when I started.

## 1. The statement attempted

**The constants.**
- `κ_max = max κ`.
- `κ̄₁ = max_{λ₁, λ₂ ∈ 𝒜} E_{u₁~λ₁, u₂~λ₂} κ(w, w'; u₁, u₂)`, maximized over `w ≠ w'`. This is round 1's constant.
- `κ̄_s = max E κ(w, w'; u₁, u₂)` over `w ≠ w'`, `z ∈ M` and multisets `{b₁, b₂}`, `{c₁, c₂}`, with `u₁ ~ r(·|z, b₁, b₂)` and `u₂ ~ r(·|z, c₁, c₂)`. The two environment laws share a predecessor value.

**Theorem.** Put `a = 3κ̄_s` and `b = min(α, 3κ_max)(κ̄₁ − κ̄_s)`. Under the causal coupling of any two initial planes:
- `D_{t+1} ≤ a D_t + b D_{t−1}` for `t ≥ 1`, and `D₁ ≤ 3κ_max D₀`, where `D_t = sup_x E ρ(v_x(t), v'_x(t))`;
- if `C := a + b < 1`, the level automaton has exactly one invariant law, and every initial plane is forgotten exponentially at rate `λ = (a + √(a² + 4b))/2 < 1`.

**Certificates (exact, `α = 27/20`).** `C < 1` at `p = 511/100, 513/100, 515/100, …, 525/100` and at `526/100`:

| `p` | 5.11 | 5.15 | 5.19 | 5.23 | 5.25 | 5.26 |
|---|---|---|---|---|---|---|
| `C` | 0.96721 | 0.97573 | 0.98421 | 0.99266 | 0.99687 | 0.99897 |

- `C > 1` at `5.27` (`1.00107`) and at `5.30`.
- Round 1's `3κ̄₁ ≥ 1` at every one of these points at this `α`.
- The largest certified `p` is `263/50 = 5.26`; round 1 certified up to `5.11`.

## 2. Steps

**S1 (PROVED; CHECKED `W1`). Closed form of `W_ρ`.** For laws `μ, ν` on `M`, let `e = (μ − ν)⁺`, `d = (ν − μ)⁺` and `TV = Σ e`. Then `W_ρ(μ, ν) = TV + (α − 1) M` with `M = max_i (e_i + d_{−i} − TV)⁺`. At most one `i` is positive, because two would need `e_i + e_j + d_{−i} + d_{−j} > 2 TV`.
- **Upper bound.** Round 1's plan keeps `min(μ, ν)` in place and routes a maximal non-antipodal flow. Its value is `TV − M`, since the only obstruction is the pair `(i, −i)`. The rest goes antipodally at cost `α`.
- **Lower bound (weak duality).** Let `i*` attain `M > 0`. Define `f` as follows:
  - `f(i*) = α` and `f(−i*) = 0`;
  - `f = 1` on the other excess points and on the points with no excess or deficit;
  - `f = α − 1` on the other deficit points.
  - `f` is 1-Lipschitz for `ρ`, since every difference is at most `1` except `|f(i*) − f(−i*)| = α = ρ(i*, −i*)`.
  - Then `Σ f(μ − ν) = TV + (α − 1)(e_{i*} + d_{−i*} − TV)`, and every coupling costs at least `Σ f(μ − ν)`.
- Checked against exhaustive exact transport on 180 random integer-mass instances.

**S2 (GIVEN, round 1 steps 1 and 3).** `ρ` and `W_ρ` are metrics. The causal coupling draws each site of level `t + 1` from an optimal `W_ρ` coupling given level `t`, independently over sites.

**S3 (PROVED). The geometry of siblings.** Let `y` be a site with predecessors `x_j = y − e_j`.
- Two of them, `x_i` and `x_k`, share exactly one predecessor, `z = y − e_i − e_k`.
- `z` is not a predecessor of the third, `x_j`, whose predecessors are `y − e_j − e_m`.

**S4 (PROVED). The recursion.** Use round 1's path through intermediate patterns: `W_ρ(r(·|a), r(·|a')) ≤ Σ_j ρ(a_j, a'_j) κ(a_j, a'_j; o_j)`. Condition on level `t − 1`, with `t ≥ 1`. The pair `(a_j, a'_j)` is independent of the environment records `o_j` given level `t − 1`, so `E[ρκ | t − 1] = Σ_{w,w'} π(w, w') ρ(w, w') E[κ(w, w'; o_j) | t − 1]`. The environment records of `o_j` sit at `x_i` and `x_k`.
- **First and last step of the path.** Both environment records come from one copy. Their laws are `r(·|v_z, ·, ·)` and `r(·|v_z, ·, ·)` with the same value `v_z` (S3), so `E[κ | t − 1] ≤ κ̄_s`.
- **Middle step.** One record comes from copy 2 and one from copy 1.
  - If `v_z = v'_z`, the bound is `κ̄_s` as above; otherwise it is `κ̄₁`.
  - So `E[ρ(a_j, a'_j) κ | t − 1] ≤ κ̄_s E[ρ(a_j, a'_j) | t − 1] + (κ̄₁ − κ̄_s) E[ρ(a_j, a'_j) | t − 1] 1{v_z ≠ v'_z}`.
  - `E[ρ(a_j, a'_j) | t − 1] = W_ρ(r(·|v_{pred x_j}), r(·|v'_{pred x_j}))`. This is at most `α`, and also at most `κ_max Σ_{i ∈ pred x_j} ρ(v_i, v'_i)`.
  - By S3, `z ∉ pred x_j`. Taking expectations, the extra term is at most `min(α, 3κ_max)(κ̄₁ − κ̄_s) D_{t−1}`.
- Summing the three steps and taking the supremum over `y` gives `D_{t+1} ≤ 3κ̄_s D_t + b D_{t−1}`.
- **At `t = 0`.** The environment is arbitrary, so `D₁ ≤ 3κ_max D₀`. For `t = 1` the level-1 records are drawn given the fixed level 0, so the argument applies.

**S5 (PROVED; CHECKED `C2`). Symmetry.** Signed permutations reduce the maximization to the ordered-pair types `(+x, −x)` and `(+x, +y)` (round 1 step 5). At `p = 526/100` all 30 ordered pairs give exactly two values of the shared constant: antipodal `0.324388` and orthogonal `0.325748`.

**S6 (CHECKED `C1`, `W2`). Exact constants.**
- `κ̄₁` is recomputed with S1's formula. At `p = 51/10`, `α = 5/4` it equals round 1's exact value `52187574259076840991934694/156963184970376094931272779`.
- The `C` values are those in the table of §1. At `p = 526/100`, `C = 101742123434848535989198503256177583297484225264/101846828471981561903500313276312611907960100913`.

**S7 (PROVED). Consequences.**
- For nonnegative `a, b` with `a + b < 1`, the recursion gives `D_t ≤ K λ^t`, where `λ` is the larger root of `λ² = aλ + b` and lies below 1.
- Coupling two invariant laws as initial planes forces equal finite-dimensional marginals, so there is one invariant law. It is invariant under the signed permutations, and the magnetization from any plane decays exponentially (round 1 step 7).

**INFO (numerical, not claimed).**
- A hybrid bound helps a little more. It averages the first and last steps also over the level-`(t − 1)` randomness of the environment's non-shared predecessors: condition on level `t − 2` plus `x_j`'s three predecessors, which are independent of the environment's other level-`(t − 1)` sites. It keeps S4's bound for the middle step.
- It gives a floating-point edge near `p ≈ 5.33`. The α-scan of the criterion in S4, also in floating point, has its optimum near `α = 1.35` and its edge near `p ≈ 5.265`.

## 3. Where the route stops

`C` crosses 1 between `p = 5.26` and `5.27`.

The maximizing environment is a wall between `w` and `w'`. One sibling's predecessors are `(w, w, w)`. The other's are `(w, w', w')`, sharing the `w`-valued predecessor `z`. Every level can present this configuration. So single-site averaging, even with the sharing constraint and one more level of averaging, saturates near `5.3`.

The executed threshold `10.5` is out of reach of one-site criteria.

## 4. What would push further

- **Route (i) with real blocks.** Measure disagreement on `2 × 2` (or larger) blocks of the level plane over two levels, and optimize the block metric by exact LP. Wall configurations then enter with their block-level weight, instead of as a worst case at every site.
- **Route (ii).** A disagreement-percolation domination whose open probability is the maximal-coupling failure rate at a site, with exact enumeration over the two-level cone.
- **Route (iii).** Cone mixing.

Any of these needs the ferromagnetic alignment of the level plane at large `p` to enter the estimate. The one-site constant cannot see it.
