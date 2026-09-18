# uniqueness-region-up, attempt 2 (worker w-jonathonsmac4f50-j1ba5, model claude-opus-5)

## (1) The statement attempted

Objects of blocks 08 and 28 (PRs #8138, #8172): the six-axis menu `M = {±e₁, ±e₂, ±e₃}`, the rule `φ(a, b) = p, q, r`
for `a = b`, `a = −b`, `a ⊥ b`, here on the line `(p, 1, 2)`; the formation law in level order read as the level
automaton on the level plane: the record at `x` is drawn from

    r(s | a₁, a₂, a₃) = Π_j φ(s, a_j) / Σ_{s'} Π_j φ(s', a_j),        a_j = record at x − e_j,

independently over the sites of a level given the previous level. Block 08 proves one invariant law with exponential
decay when the causal coupling contracts, `3c < 1`, `c` the one-site total-variation sensitivity; block 28 brackets that
criterion on `(p, 1, 2)` between `p = 37/10` (holds) and `p = 19/5` (fails); the executed threshold of memory is `10.5–11`.

**Statement.** Let `ρ` be the ground metric on `M` with `ρ(w, w') = 1` for orthogonal and `ρ(w, w') = α` for antipodal
values, `1 ≤ α ≤ 2`; `𝒜 = {r(· | a) : a ∈ M³}` the achievable one-site laws;
`κ(w, w'; u₁, u₂) = W_ρ(r(·|w, u₁, u₂), r(·|w', u₁, u₂)) / ρ(w, w')`; and
`κ̄ = max_{w ≠ w'} max_{λ₁, λ₂ ∈ 𝒜} Σ λ₁(u₁) λ₂(u₂) κ(w, w'; u₁, u₂)`. If `3κ̄ < 1`, the level automaton has exactly one
invariant law and every initial plane is forgotten exponentially: under the causal coupling
`sup_x E ρ(v_x(t), v'_x(t)) ≤ α (3κ_max)(3κ̄)^{t−1}` (`κ_max = max κ`). At `α = 5/4` the criterion holds exactly at every
`p ∈ {37/10, 38/10, …, 51/10}`; at `p = 51/10`, `3κ̄ = 0.99744869…` (an exact rational). So the proved no-memory region
on `(p, 1, 2)` reaches `p = 51/10` (block 08's criterion stops before `19/5`). The numerical edge of this criterion is near
`p ≈ 5.11`; the located threshold `10.5–11` is not reached.

## (2) Steps

**Step 1 — `ρ` is a metric and `W_ρ` is a metric on laws on `M` (PROVED).** `ρ` takes the values `0, 1, α` with
`α ≤ 2 = 1 + 1`, so every triangle inequality holds. For laws `μ, λ, ν` on the finite set `M` with optimal couplings
`π₁` of `(μ, λ)` and `π₂` of `(λ, ν)`, the glued coupling `π(i, k) = Σ_{j: λ(j) > 0} π₁(i, j) π₂(j, k)/λ(j)` couples
`(μ, ν)`, and `Σ π ρ(i, k) ≤ Σ π₁ ρ(i, j) + Σ π₂ ρ(j, k)` by the triangle inequality of `ρ`. So
`W_ρ(μ, ν) ≤ W_ρ(μ, λ) + W_ρ(λ, ν)`.

**Step 2 — an explicit transport plan (PROVED; CHECKED as E1).** For laws `μ, ν` put the excess `e = (μ − ν)⁺`, the
deficit `d = (ν − μ)⁺` (disjoint supports), `TV = Σ e`. Keep `min(μ, ν)` in place; route a maximum flow `F` from `e` to
`d` along arcs `i → j` with `j ≠ −i` (cost `1` per unit, `i ⊥ j`); route the rest antipodally (cost `α`). This is a
coupling: after a maximum flow, an unrouted excess at `i` and an unmet deficit at some `j ∉ {i, −i}` would give an
augmenting arc, so the remaining excess sits on one point `i` and the remaining deficit on `−i`, of equal mass. Its cost is
`TV + (α − 1)(TV − F)`, an upper bound on `W_ρ(μ, ν)`. `check.py` computes `F` by exact augmenting paths and verifies the
residual structure for every plan it uses.

**Step 3 — the causal coupling (definition, as in block 27's T2 for the sphere).** Given coupled level-`t` records
`(v, v')`, at each site `y` of level `t + 1` draw `(v_y, v'_y)` from an optimal `W_ρ`-coupling of `r(· | v_{pred(y)})` and
`r(· | v'_{pred(y)})`, independently over `y` given level `t`. Put `D_t = sup_x E ρ(v_x(t), v'_x(t))`.

**Step 4 — the averaged one-level recursion (PROVED).** For `t ≥ 1`, `D_{t+1} ≤ 3κ̄ D_t`; for `t = 0`, `D₁ ≤ 3κ_max D₀`.
*Argument.* Fix `y` at level `t + 1` with predecessors `x₁, x₂, x₃` and write `a_j = v_{x_j}`, `a'_j = v'_{x_j}`. By step 1
along the path `a → (a'₁, a₂, a₃) → (a'₁, a'₂, a₃) → a'`,

    E[ρ(v_y, v'_y) | level t] = W_ρ(r(·|a), r(·|a')) ≤ Σ_{j=1}^3 ρ(a_j, a'_j) κ(a_j, a'_j; o_j),

where `o_j` are the two other entries of the `j`-th intermediate pattern: the copy-2 records at `x_i`, `i < j`, and the
copy-1 records at `x_i`, `i > j` (`r` depends only on the multiset of its three arguments, so the slots do not matter).
For `t ≥ 1` the records of level `t` are drawn given level `t − 1`, independently over sites: the coupled pair
`(a_j, a'_j)` at `x_j` is independent of the records at the two other sites given level `t − 1`, and each of those records
has one of the laws `r(· | ·)` of its copy, an element of `𝒜`. Hence
`E[ρ(a_j, a'_j) κ(a_j, a'_j; o_j) | level t − 1] = E[ρ(a_j, a'_j) Σ λ₁(u₁)λ₂(u₂) κ(a_j, a'_j; u₁, u₂) | level t − 1]
≤ κ̄ E[ρ(a_j, a'_j) | level t − 1]`. Take expectations, sum over `j`, take the supremum over `y`. At `t = 0` the initial
records are arbitrary and `κ ≤ κ_max` is used instead.

**Step 5 — symmetry (PROVED; CHECKED at the edge).** Every signed permutation `g` of the six axes preserves `φ`, hence
`r(g s | g a) = r(s | a)`, `ρ(g w, g w') = ρ(w, w')`, `W_ρ(g_*μ, g_*ν) = W_ρ(μ, ν)`, and `g𝒜 = 𝒜`; so the inner maximum
of `κ̄` depends only on whether `w' = −w` or `w' ⊥ w`, and the group is transitive on each kind of ordered pair.
`check.py` uses the two types `(+x, −x)` and `(+x, +y)` on the grid and computes all 30 ordered pairs at `p = 51/10`,
finding exactly two values.

**Step 6 — the exact certificates (CHECKED as E2–E4, fractions throughout).** `check.py` evaluates `κ` through the plan
of step 2 (cost divided by `ρ`), an upper bound on the transport ratio, so every certified `κ̄` below is an upper bound on
the true one and `3κ̄ < 1` is certified with room to spare only in that direction. At `α = 5/4`:

| `p` | 3.7 | 3.8 | 3.9 | 4.0 | 4.2 | 4.4 | 4.6 | 4.8 | 5.0 | 5.1 |
|---|---|---|---|---|---|---|---|---|---|---|
| `3κ̄` | 0.74405 | 0.76887 | 0.79267 | 0.81533 | 0.85687 | 0.89299 | 0.92347 | 0.94834 | 0.97364 | 0.99745 |

(all fifteen grid points `37/10 … 51/10` are below `1`); at `p = 51/10`,
`κ̄ = 52187574259076840991934694/156963184970376094931272779`, `3κ̄ = 0.99744869…`; the first-level constant is
`3κ_max = 1.068206`; the maximizing environment laws are those of the aligned predecessor patterns (`r(·|+x,+x,+x)`
with `r(·|−x,−x,−x)` for the antipodal type, with `r(·|+y,+y,+y)` for the orthogonal type). For comparison, block 08's
`3c` is `0.984995` at `37/10` and `1.011100` at `19/5`, recomputed.

**Step 7 — consequences (PROVED, as in block 27's T2).** With `3κ̄ < 1`, `D_t ≤ α(3κ_max)(3κ̄)^{t−1} → 0` for any two
initial planes. Coupling two invariant laws as initial planes gives laws at level `t` equal to the same two laws, with
per-site distance `≤ D_t → 0`, so their marginals on every finite set coincide: one invariant law. It is invariant under
the signed permutations (the kernel commutes with them), so its one-site law is uniform and the magnetization from any
initial plane tends to zero exponentially (distinct unit vectors of `M` are at Euclidean distance `≤ 2 ≤ 2ρ`, since
`ρ ≥ 1` on distinct values).

## (3) Where the route stops

The criterion saturates at `p ≈ 5.11` (floating-point scan over `α`; not certified beyond `51/10`). The worst achievable
environments are the laws of aligned predecessor patterns pointing in antipodal or orthogonal directions: every level
can present them, so averaging one level of randomness cannot remove them. Nothing here reaches the executed threshold.

## (4) What would push it further

Average two or more levels of randomness (the environment of a site two levels up is drawn from a composed law, less
concentrated than the worst single-level law), with the exact block sensitivity computed by rational arithmetic over the
light cone; or a disagreement-percolation bound with exact small-block enumeration. Both need the ferromagnetic
alignment of the level plane at large `p` to enter the estimate, which a one-site worst case over environments cannot
capture. The grid statement could be made an interval by a Lipschitz bound in `p` for `κ̄` (not attempted).
