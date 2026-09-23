# J:derive:uniqueness-up-2:a2

Worker `w-macbookpro90c72-j8469` (claude-opus-5-5). This is attempt 2 of 4.

**Independence.** At claim time the tool printed the summary lines of attempts a3 (`w-jonathonsmac4f50-j96fc`) and a4 (`w-jonathonsmac4f50-j5c56`), both claude-opus-5 and unrefereed. So I knew that:
- a3 certified `p` up to about 5.25 with a one-level "shared-predecessor" bound;
- a4 estimated route (ii).

I formed and built the route below before opening their files. It is a different route: two levels of the automaton, not one. I read a3 and a4 afterwards, only to place the result.
- The one idea the two routes share is that records of one copy agree on a shared predecessor. a3 uses it with a correction term. Here it enters through whole groups of environment sites, with no correction term.
- I use round 1's refereed definitions, and reproduce its exact constant (A1).

## (1) Exact statement

### Objects

These are the objects of blocks 08 and 28 (PRs #8138, #8172), as restated by round 1 (`probes/work/derive/uniqueness-region-up/w-jonathonsmac4f50-j1ba5`, refereed twice).
- **Menu and rule.** The menu is `M = {±e₁, ±e₂, ±e₃}`. The rule is `φ(s, a) = p, 1, 2` for `s = a`, `s = −a`, `s ⊥ a`.
- **The level automaton.**
  - Level `t` is the plane `Λ_t = {x ∈ Z³ : x₁ + x₂ + x₃ = t}`.
  - The predecessors of `y ∈ Λ_{t+1}` are `P(y) = {y − e₁, y − e₂, y − e₃}`.
  - Given level `t`, the records of level `t + 1` are independent, with laws `r(s | a₁, a₂, a₃) = Π_j φ(s, a_j)/Z`.
  - `r` depends only on the multiset of its arguments. `𝒜` is the set of its 56 laws.
- **Metric.** `ρ = 0, 1, α` on equal, orthogonal and antipodal values, with `1 ≤ α ≤ 2`. `W` is the Wasserstein distance for `ρ`.
- **The cone.** The six *grand-predecessors* of `y` are `z_{ij} = y − e_i − e_j` (`i ≤ j`).
  - The three **corners** `z_{ii}` each lie below one predecessor of `y`.
  - The three **edges** `z_{ij}` (`i < j`) each lie below two.

### Claim

The six-axis level automaton on `(p, 1, 2)` has exactly one invariant law, and forgets every initial plane exponentially, at:

| `p` | `α` | `K2c` (upper bound) |
|---|---|---|
| `51/10` | `27/20` | 0.845071 |
| `21/4` | `27/20` | 0.894864 |
| `27/5` | `27/20` | 0.944946 |
| `11/2` | `27/20` | 0.978358 |
| `111/20` | `27/20` | 0.995052 |
| `139/25` | `34/25` | 0.998429 |

Here `K2c` is the two-level constant of steps 4–5. Each entry is an exact rational upper bound, printed to six digits, and each is below 1.

The largest certified `p` is **`139/25 = 5.56`**. There the six positions give:
- corners `z₁₁`, `z₂₂`, `z₃₃`: 0.11087, 0.12093, 0.11087;
- edges `z₁₂`, `z₁₃`, `z₂₃`: 0.22142, 0.21292, 0.22142;
- `κ_max = 0.39208`.

The certificates are pointwise: no monotonicity in `p` is claimed. Round 1 certified up to 5.1, and a3 up to 5.26. The numerical edge of this criterion lies between 5.56 and 5.57; the located threshold 10.5 is not reached.

## (2) Steps

1. **PROVED (an optimal, symmetric plan). CHECKED A1, A2.**
   - **Setup.** For laws `μ, ν` on `M`, let `e = (μ − ν)⁺`, `d = (ν − μ)⁺`, `TV = Σe` and `A = max_i (e_i + d_{−i} − TV)⁺`.
   - **At most one `i` is positive.** Two such `i` would need `e_i + e_j + d_{−i} + d_{−j} > 2TV` (the case `j = −i` gives 0).
   - **The plan `Π(μ, ν)`:**
     1. keep `min(μ, ν)` in place;
     2. send `A` from the critical `i*` to `−i*`;
     3. route the rest between different axes. Let `E_k, D_k` be the remaining excess and deficit on axis `k`. Take the axis-level transport `F` (zero diagonal, rows `E`, columns `D`) at the midpoint of its feasible set, which is a segment. Split `F_{kl}` within the axes proportionally to `e` and `d`.
   - **Feasibility.**
     - After step 2, `e'_i + d'_{−i} ≤ TV'` for every `i`. At `i*` this holds with equality. For `i ≠ ±i*` it is `≤ 2TV − (TV + A)`. At `i = −i*` both terms vanish.
     - Supports are disjoint, so `E_k + D_k ≤ TV'` for every axis.
     - That makes every lower bound of `s = F₁₂` (namely `0`, `D₂ − E₃`, `D₁ + D₂ − E₂ − E₃`) at most every upper bound (`E₁`, `D₂`, `D₁ + D₂ − E₃`).
   - **Cost.** All residual mass moves between axes at cost 1. So the cost is `TV + (α − 1)A`.
   - **Optimality.** The 1-Lipschitz witness `f` has `Σ f(μ − ν)` equal to this cost. Take `f(i*) = α`, `f(−i*) = 0`, `f = α − 1` on the other deficit points and `f = 1` elsewhere. When `A = 0`, take `f = 0` on deficits and `1` elsewhere. So `W(μ, ν) = TV + (α − 1)A` and `Π` is optimal.
   - **Symmetry.** Every step commutes with the 48 signed permutations `g`: the critical `i*` is unique, and the midpoint of the segment is intrinsic. So `Π(gμ, gν) = g_* Π(μ, ν)`.
   - **CHECKED.**
     - A1: marginals, cost and dual witness on 1333 pairs of laws, and on every plan used in A4.
     - A1: round 1's exact `κ̄` at `p = 51/10`, `α = 5/4` is reproduced.
     - A2: equivariance on every pair used, for all 48 `g` (2016 checks).

2. **PROVED (the coupled process).** Fix on every level the lexicographic order `≺` of `(x₁, x₂)`. On the six grand-predecessors of every `y` it reads `z₁₁ ≺ z₁₂ ≺ z₁₃ ≺ z₂₂ ≺ z₂₃ ≺ z₃₃`.
   - **Level 0:** any coupling of the two initial planes.
   - **Odd levels:** `(V_y, V'_y) ~ Π(r(·|V_{P(y)}), r(·|V'_{P(y)}))`, independently over `y`.
   - **Even levels `t ≥ 2`:** for `x` with `P(x) = {q₁ ≺ q₂ ≺ q₃}`, let `h^m` be the triple with copy 2 on `q₁..q_m` and copy 1 on the rest. Draw a chain `A⁰, …, A³`:
     - `A⁰ ~ r(·|h⁰)`;
     - `A^m` given `A^{m−1}` follows the conditional of `Π(r(·|h^{m−1}), r(·|h^m))`;
     - independently over `x`. Set `V_x = A⁰` and `V'_x = A³`.
   - **Each copy is a version of the automaton.**
     - Copy 1 at `x` is `A⁰ ~ r(·|V_{P(x)})`.
     - For copy 2, the last marginal of the glued chain is `r(·|h³) = r(·|V'_{P(x)})`, whatever the intermediate triples are.
     - In both cases the draws are independent over `x` and depend on the past only through that copy's previous level.
   - **When nothing changes.** If `V_q = V'_q`, the step's two laws coincide. `Π` is then diagonal, so the chain does not move.

3. **PROVED (two-level telescoping).** Let `t + 1` be odd, `t ≥ 2`, and `y ∈ Λ_{t+1}`. List its grand-predecessors as `z_1 ≺ … ≺ z_6`.
   - For `x ∈ P(y)`, let `H^k_x = A^{m(x,k)}_x`, where `m(x,k)` is the number of `z_1..z_k` in `P(x)`. So `H⁰ = V_{P(y)}` and `H⁶ = V'_{P(y)}`.
   - Level `t + 1` is optimally coupled, so the triangle inequality for `W` gives
     `E[ρ(V_y, V'_y) | 𝓕_t] = W(r(·|H⁰), r(·|H⁶)) ≤ Σ_k W(r(·|H^{k−1}), r(·|H^k))`.

4. **PROVED (the single-switch function).**
   - **Which predecessors move at step `k`.** Given `𝓕_{t−1}`, the `k`-th term involves one step of the chain at each child of `z_k` in `P(y)`: one child for a corner, two for an edge. That step is `Π`-coupled with the child's other predecessors at their hybrid values. The other `x ∈ P(y)` do not move; each carries one value with law `r(·|hybrid predecessors)`. All of these are independent.
   - **Hybrid values.** The hybrid value at `z_i` is `V'_{z_i}` if `z_i ≺ z_k`, and `V_{z_i}` if `z_i ≻ z_k`.
   - **The function `F`.** Hence `E[k-th term | 𝓕_{t−1}] = F_{pos}(V_{z_k}, V'_{z_k}; u)`, where `u` is the tuple of hybrid values at the other five grand-predecessors. `F` is exactly computable:
     - **corner** (`z = z_ii`; `j, k` the other two directions; `u = (u_ij, u_ik, u_jj, u_jk, u_kk)`):
       `F = Σ Π(r(·|w, u_ij, u_ik), r(·|w', u_ij, u_ik))(a, a') · r(b | u_ij, u_jj, u_jk) · r(c | u_ik, u_jk, u_kk) · W(r(·|a, b, c), r(·|a', b, c))`;
     - **edge** (`z = z_ij`; `u = (u_ii, u_ik, u_jj, u_jk, u_kk)`): the plans at both children, the law `r(·|u_ik, u_jk, u_kk)`, and `W(r(·|a, b, c), r(·|a', b', c))`.
   - `F(w, w; u) = 0`.

5. **PROVED (averaging with group-consistent environments).** Condition on `𝓕_{t−2}`, with level `t − 1` odd.
   - **Independence.** The pairs `(V_z, V'_z)` at level `t − 1` are independent over `z`. So the pair at `z_k` is independent of the hybrid environment `u`, whose entries are independent with laws `λ_{z_i}`:
     - `λ_{z_i} = r(·|V'_{P(z_i)})` for `z_i ≺ z_k` (group *before*);
     - `λ_{z_i} = r(·|V_{P(z_i)})` for `z_i ≻ z_k` (group *after*).
   - **The key point.** Within a group, all the laws come from one configuration of level `t − 2`: copy 2's or copy 1's. Two sites of a group that share a predecessor see the same value there.
   - **The bound.** Let `S_B` and `S_A` be the tuples of laws (pattern multisets) that one configuration can produce on each group. Then
     `E[k-th term | 𝓕_{t−2}] = Σ_{w≠w'} Π_{z_k}(w, w') E_λ F(w, w'; u) ≤ κ2c(z_k) · E[ρ(V_{z_k}, V'_{z_k}) | 𝓕_{t−2}]`,
     with `κ2c(z_k) = max_{w≠w'} max_{(λ_B, λ_A) ∈ S_B × S_A} E_λ F(w, w'; u)/ρ(w, w')`.
     - Across the two groups, a shared predecessor may differ between the copies. The product `S_B × S_A` allows that.
     - Step 1's symmetry reduces the maximum over `(w, w')` to `(+x, −x)` and `(+x, +y)`.
   - **Result.** Summing over `k` and taking expectations, `D_{t+1} ≤ K2c D_{t−1}`, where `K2c = Σ_{k=1}^6 κ2c(z_k)` and `D_t = sup_x E ρ(V_x(t), V'_x(t))`.

6. **PROVED (consequences).**
   - **The first levels.** The one-level bound (round 1's step 4, with `κ_max` in place of the average) holds at odd levels. At even levels it holds through the chain's triangle inequality. It gives `D₁ ≤ 3κ_max D₀` and `D_{2k} ≤ 3κ_max D_{2k−1}`.
   - **Decay.** With step 5, `D_t ≤ α max(1, 3κ_max)² K2c^{⌊(t−1)/2⌋}`.
   - **Uniqueness.** Couple two invariant laws as the initial planes. Each copy keeps its law at every level. On a finite window `B`, the two copies differ with probability at most `|B| D_t → 0`. So the laws are equal, and every initial plane is forgotten exponentially.

7. **CHECKED (A3–A5, exact).**
   - A3: the realisable sets `S_B`, `S_A` are enumerated exhaustively for every group of the six splits. For example, the five-site group realises 8,536,256 of the `56⁵ = 550,731,776` tuples.
   - A4: every table entry is an exact Fraction. The maxima over `S_B × S_A` are taken in integers with every rounding upward: tables × `2³⁴`, laws × `2²⁴`, a ceiling after each contraction, all terms nonnegative. So every `κ2c` printed is an upper bound, and `K2c < 1` holds exactly at the rows of the table.
   - A5: `κ_max` is computed.

### INFO (floating point, not claimed)

- **Without step 5's consistency.** With independent environment laws in `𝒜`, the two-level constant `K2` is:
  - 0.8983 at `p = 5.1`, `α = 5/4` (round 1's bound squared is 0.9949);
  - 0.9917 at `p = 5.4`, `α = 1.35`.

  Its edge is near `5.42`.
- **The choice of plan does not matter at the worst case.**
  - The worst case is unchanged, to six digits, if the plan at the children is replaced by the LP-optimal coupling for the actual two-level cost: 0.113565 in both cases, at `p = 5.4`, `α = 1.35`.
  - An independent-excess coupling is much worse (`K2 = 1.026`).
- **The order does not matter.** All 12 orders of the six grand-predecessors that a linear functional induces give the same multiset of split classes: two corners with one full group, one corner split 3|2, two edges split 1|4, one edge split 2|3. So `K2c` does not depend on the order.
- **The edge of `K2c`.** It lies between 5.56 and 5.57.
  - At `p = 5.57`: `K2c = 1.0044` (`α = 1.33`) and `1.0018` (`α = 1.36`).
  - At `p = 5.6`: `K2c = 1.0255, 1.0131, 1.0163` at `α = 1.3, 1.4, 1.5`.
  - The best `α` is near 1.35–1.37: the antipodal and orthogonal worst cases cross there.

### ASSUMED

Only the definitions of blocks 08 and 28, as round 1 restates them. Everything else is argued above.

## (3) Where the route stops

`K2c` crosses 1 between `p = 5.56` and `5.57`.
- The maximising environments are domains of `w` and `w'` meeting along a wall. For example, at `p = 5.4` the full-group corner maximum, in floating point, has patterns realised by a `−x` region on three of the nine sites and `+x` elsewhere. These are realisable inside each group, so the consistency constraint does not exclude them.
- Averaging two levels and imposing consistency within groups removes the incoherent worst cases of the one-level criteria, but not the coherent walls.
- The located threshold 10.5 is out of reach for this route.

## (4) What would push further

- **Three levels.** Switch a site three levels below and average over the ten-site cone. The obstacle is the maximum over nine environment laws. The trie over configurations of one group used here would have to run over the 15-site cone.
- **Block metrics (route (i)).** Weight disagreements of `2 × 2` blocks, so that a coherent wall is charged once rather than at every site.
- **A referee from another model family.** Blocks 08 and 28, round 1, a3, a4 and this attempt are all the same model family.
