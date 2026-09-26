# Referee: the delayed clock and the pair law, attempt 1

Attempt `w-macbookpro9927a-j0e51`. The Green function, the separation walk, and the first-order moment solution are recomputed here. The attempt's script is not imported. The direct simulation was not rebuilt.

The records hop on their own clocks. The field relaxes by the supplied clause `du/dt = Γ w ⊙ (M u + λ(n − n̄))`, with `λ = log κ` and departure timing `a = 1`, `W = 1`. Well-posedness (A0) and differentiability at `λ = 0` (A1) are assumptions of the attempt.

## Verdicts

**Invariant.** Along the flow, `d/dt Σ e^{−u}` cancels because `M` has zero column sums and the occupations sum to `N`. Jumps do not move `u`. On ring 5 this cancellation is an identity in the field values.

**Separation.** One record's direction is uniform on the neighbours, whatever the field, so the jump chain is simple random walk and the trail acts only through waiting times. For two records, every nonzero separation on rings 3–6, the `3×3`, `4×4` and `3³` steps onto each nonzero neighbour exactly once. The separation's jump chain is simple random walk on the torus minus the origin, at every `Γ` and `λ`.

**First order.** With `r0 = 1/(2q)`, the factor `γ = Γ/(Γ + r0 q)` is `2Γ/(2Γ+1)`. The conditional mean `m(C) = π0 γ φ*(C)`, `φ* = q Σ_r G(·−r)`, solves the moment equations in 54 cases: rings 5–7, the `3×3` and the `3³`, several record counts, rates `1/3, 1, 5/2`, and timings `1, 1/2, 0`. The slaved value `γ = 1` and the wrong rate `Γ/(Γ+1)` fail in all 36 controls. On ring 5 with two records the moment operator has rank one less than its dimension, so the solution is the constants plus this particular solution, fixed by mean zero. The `O(λ)` record law is block 95's at coupling `γλ`. On ring 6 the pair weights are `−1/3, 1/6, 1/3` times `γλ` at distances `1, 2, 3`, and `q G(0) = 35/36`. On the `3³`, `q G(0) = 88/81`.

**Product law and reversibility.** Under A0, the averaged Lyapunov derivative forces a product law's field measure onto the line of equilibria of the mean occupation. A linear test then forces every supported configuration to share that occupation, and a positive escape rate contradicts stationarity on one configuration. So no stationary product exists when `λ ≠ 0` and `0 < Γ < ∞`. Reversibility would force the vector field to vanish, hence a single occupation, which the same escape rate forbids. The drift identity on that line was checked symbolically.

**Sojourn.** `ΔG2 = G` gives the arrival sum `Σ (G2(D′)−G2(D)) = −G(D) − [D adjacent] G(0)/q`. On ring 6 at distance 2 the arrival values of `G2` are `−265/864` and `119/864`. On the `3³` at `(0,0,1)` they are `−19/8748` and `23/2187`. The forward sojourn depends on the arrival neighbour, so the observed separation is not reversible at order `λ/Γ`.

**Quasi-static threshold.** The uniform field is unstable for `λ` below `V μ1`: `−3` on ring 6, `−27/2` on the `3³`, and `−64/3` on the `4³`.

## What stays open

A0 and A1 were not proved. The direct simulation, the exact-in-`λ` integral `J(λ)`, and the second order in `λ` were not rebuilt.

## Result

HIT: confirmed. At finite `Γ` and `log κ ≠ 0` there is no stationary product of a record law and a field law, and no stationary law is reversible, both under A0. The separation is a simple random walk off the origin. At first order in `log κ` the conditional mean field is the slaved field times `2Γ/(2Γ+1)`.
