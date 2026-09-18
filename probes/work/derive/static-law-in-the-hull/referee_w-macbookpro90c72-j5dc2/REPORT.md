# Referee report: J:derive:static-law-in-the-hull:a1

Author: `w-jonathonsmac4f50-j0546` (claude-opus-5). Referee: `w-macbookpro90c72-j5dc2` (grok-4.6).
Problem: is the static law in the convex hull of adapted (value-dependent) sequential formation laws, on the 2×3 rectangle and the cube, for the six-axis rule at rational weights; a separating functional that works for every weight would be a theorem (block 16 X4).

## Does the attempt prove that statement?

Yes, and a stronger one: on every finite window of `Z³` whose nearest-neighbour graph contains a cycle, for every positive six-axis product rule that is not constant, the static law is not in the convex hull of adapted formation laws. The separating functional is `f = 1[constant pattern]`. The 2×3 rectangle and the cube at `(3,1,2)`, `(5,2,4)`, `(7,3,5)` are instances. This is X4, not a neighbouring forest/value-blind statement (block 16 already closed value-blind mixtures). A path of three sites is a negative control: `Z = D` and some order has every `k_x ≤ 1`.

## Step-by-step

**Step 1 (representation) — holds.** `μ_S(v) = Σ_σ ρ_S(σ | v) μ_σ(v)` with `Σ_σ ρ_S(σ | v) = 1` for each fixed `v`. The formed neighbours of `σ_j` at its formation are exactly `A_{σ_j}(σ)` (a function of the order, not of the values). `ρ` may depend on `v`; that is why this is not a value-blind mixture of measures, but it is a convex combination of the numbers `μ_σ(v)` at each pattern. Independent check R4: on the plaquette, a value-dependent greedy policy, all `6^4` patterns, the sequential simulation equals `Σ_σ ρ(σ|v) μ_σ(v)`.

**Step 2 (constant patterns) — holds.** `r(b | ∅) = 1/6`, `r(b | A)` with all recorded neighbours `b` equals `p^k / N_k`, `Σ_x k_x(σ) = |E|`, so `μ_σ(v^b) = p^{|E|} / D_σ` and `μ_stat(v^b) = p^{|E|} / Z_Λ`. Independent: along a min-`D` order the product of those conditionals equals `p^{|E|}/D_σ`.

**Step 3 (Hölder / AM-GM) — holds at the scope used.** The inequality `Π_i x_i ≤ (1/k) Σ_i x_i^k` is AM-GM on `{x_i^k}`; the author did not tag it ASSUMED. That is a cosmetic gap, not a failing step: (i) for `k = 2` it is `(x-y)^2 ≥ 0`; (ii) on `Z³` one has `k_x ≤ 6`, and enumerating every tuple in `M^k` for `k ≤ 6` at five rules (including `q > p` and `p = q`) gives `Σ_s Π_i φ(s, a_i) ≤ N_k`, with equality iff the functions `φ(·, a_i)` coincide, which is all `a_i` equal, or (only when `p = q`) all in one antipodal pair. Orthogonal records are strict for every non-constant rule, including `p = q ≠ r`. Independent check R1 (dot-product `φ`, not the author's `a ^ 1` encoding).

**Step 4 (`Z_Λ ≤ D_σ`, strict if some `k_x ≥ 2`) — holds.** Expanding `Π_edges φ` along the order, the inner sum over the newly formed record is `N_k` for `k ≤ 1` and `≤ N_k` for `k ≥ 2` by Step 3. Strictness uses orthogonal records on two already-formed neighbours (positive weight because `φ > 0`), not merely “not all equal”: when `p = q` an antipodal pair would saturate Hölder, but orthogonal pairs still do not, and they exist on every window that has a site with `k ≥ 2`.

**Step 5 (cycle ⇒ some `k_x ≥ 2` in every order) — holds.** The last vertex of a cycle in the order has both cycle-neighbours already formed. Independent: min over orders of `max_x k_x` is `2` on the plaquette, 2×3 and 3×3, `3` on the cube, and `1` on the path of 3.

**Step 6 (main inequality) — holds.** Pointwise convex combination plus `D_σ ≥ D_Λ` gives `μ_S(v^b) ≤ p^{|E|}/D_Λ`; Steps 4–5 give `Z_Λ < D_σ` for every order, hence `Z_Λ < D_Λ`, hence the constant-pattern mass is strictly below the static mass. Independent R3: `Z < D` on every cyclic window/rule pair checked; `Z = D` on the path; author’s table rows recomputed with Python ints and a forward subset DP.

**Step 7 (hull and `f`) — holds.** Any convex combination of adapted laws still has `E f ≤ 6 p^{|E|}/D_Λ < 6 p^{|E|}/Z_Λ = E_stat f`. The bound on `f` is attained by the value-blind min-`D` order (an adapted scheme that ignores values). Value-dependence cannot raise the constant-pattern mass above `p^{|E|}/D_Λ`.

**Step 8 (numbers) — holds as CHECKED.** Independent recomputation matches the author’s `Z` and `D` on the plaquette, 2×3, cube (five rules) and 3×3 at `(3,1,2)` and `(2,2,1)`. Cube min-`D` orders have a site with `k = 3` (not merely `2`).

## Classic failure modes

- Quantifier swap: none. The argument is uniform in the scheme, the cyclic window and the non-constant positive rule; the table is not the proof.
- Induction at the wrong level: the `G_j` recurrence is on the formation prefix of a fixed window, not on window size.
- Bound only at checked sizes: `k ≤ 6` is the full degree range on `Z³`; Hölder is enumerated there. `Z < D` is proved, not fitted.
- Outside theorem beyond hypotheses: AM-GM is used for all `k ≥ 1` on nonnegative reals; closed at the used scope as above. No appeal to block 16’s flip lemma (which does not apply to `P(σ | v)`).
- Circular use of the statement: none. Forests are correctly excluded (Step 5).

## Verdict

The claim survives. First failing step: none.

`HIT: confirmed` — see `check.py` (independent machinery).
