# Referee report: J:derive:uniqueness-region-up:a2

Author: `w-jonathonsmac4f50-j1ba5` (claude-opus-5). Referee: `w-macbookpro90c72-jeff4` (grok-4.6).
Problem: enlarge the proved no-memory region of the six-axis formation law on `(p,1,2)` toward the executed threshold `10.5–11` (block 08 stops at `3c < 1`, which holds at `p = 37/10` and fails at `19/5`).

## Does the attempt prove that statement?

It proves a strictly weaker but new exact partial: uniqueness and exponential memory loss at every `p ∈ {37/10, …, 51/10}` via an averaged `W_ρ` contraction with `α = 5/4`, not the located threshold. That is a legitimate PARTIAL for this task (a block/two-level criterion that moves the proved edge from `3.7` past `3.8` to `5.1`). It does not claim `10.5–11`.

## Step-by-step

**Step 1 (`ρ` and `W_ρ` are metrics) — holds.** `α ≤ 2` makes the three-point inequalities on `{0,1,α}` work. Independent T1: triangle on all `6³` triples at `α = 5/4`. The gluing of optimal couplings is the standard Wasserstein triangle inequality on a finite set.

**Step 2 (orthogonal-then-antipodal plan) — holds as an upper bound.** Excess/deficit are disjoint; max-flow on non-antipodal arcs; leftover mass, if any, sits on one antipodal pair (otherwise a cheap augmenting arc). Cost `TV + (α−1)(TV−F) ≥ W_ρ`. Independent: the plan is feasible on every call used, and its cost is `≥` the true min-cost transport (Fractions, successive shortest paths). At the maximizers the two costs agree, so the stated `κ̄` equals the true ratio, not a loose bound.

**Step 3 (causal coupling) — holds as a definition**, the block-27 T2 pattern with `W_ρ` in place of TV.

**Step 4 (averaged recursion) — holds.** Lipschitz of the kernel along the three single-coordinate paths; for `t ≥ 1` the three predecessors on a level are independent given the previous level, so the mixed copy-1/copy-2 environments are product laws in `𝒜 × 𝒜`. Taking `max_{λ1,λ2 ∈ 𝒜}` is a valid worst-case. At `t = 0` the environment need not lie in `𝒜`, hence `κ_max`. Then `D_t ≤ α (3κ_max)(3κ̄)^{t−1}`. Independent: at `p = 51/10`, `3κ_max = 1.068206 > 1 > 3κ̄ = 0.99744869`, so the first step may expand and then contracts.

**Step 5 (cube symmetry) — holds.** Independent T4: all 30 ordered pairs at `p = 51/10` take exactly two values (antipodal vs orthogonal).

**Step 6 (certificates) — holds.** Independent true-`W` grid: `3κ̄ < 1` at every `p = 37/10,…,51/10`, matching the author's five-decimal table and the exact edge
`κ̄ = 52187574259076840991934694 / 156963184970376094931272779`.
Block 08 `3c = 0.984995` at `37/10` and `1.011100` at `19/5`, recomputed.

**Step 7 (uniqueness and forgetting) — holds.** Two invariant laws as initial planes stay put and have per-site (hence finite-window) distance `≤ D_t → 0`. Magnetization from an arbitrary plane vanishes because distinct menu vectors are at Euclidean distance `≤ 2 ≤ 2ρ`.

## Classic failure modes

- Quantifier: the grid is the statement (`p` in that finite set), not an interpolation to an interval. The author says the numerical edge is `≈ 5.11` and does not certify beyond `51/10`.
- Bound only at checked sizes: `𝒜` is enumerated (`6³` laws), all 30 pairs at the edge, all `u1,u2`. No sample.
- Outside theorems: Wasserstein triangle (sketched); coupling uniqueness (standard, as in T2). No appeal to unproved percolation bounds.
- Circular: none. The located threshold is not used.
- Neighbouring statement: this is not a re-proof of `3c < 1`; averaging over `𝒜` is what crosses `19/5`.

## Verdict

The PARTIAL claim survives. First failing step: none. The route correctly stops short of `10.5–11`.

`HIT: confirmed` — see `check.py`.
