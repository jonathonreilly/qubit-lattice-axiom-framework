# Referee: uniqueness-up-2 a2

Worker `w-macbookpro90c72-j00bb` (`grok-4.6`). Author `w-macbookpro90c72-j8469` (`claude-opus-5-5`). The attempt's script is not imported.

## Verdict

Confirmed partial. On `(p, 1, 2)` the two-level Wasserstein constant is an exact upper bound below 1 through `p = 139/25`. The level automaton has one invariant law and forgets its initial plane exponentially on that range. The located threshold 10.5 is not reached.

## What was checked

- **Geometry.** The six grand-predecessors of a site, ordered by `(x₁, x₂)`, are `z₁₁ ≺ z₁₂ ≺ z₁₃ ≺ z₂₂ ≺ z₂₃ ≺ z₃₃`. Adjacent ones share a parent on the level below.
- **The coupling.** `W = TV + (α−1)A`. The stated plan meets both marginals, costs `W`, and has a 1-Lipschitz dual of the same value, on 1333 law pairs and on every plan used in the table. It commutes with all 48 signed permutations (2016 checks). Round 1's constant at `p = 51/10`, `α = 5/4` is the fraction `52187574259076840991934694/156963184970376094931272779`.
- **Environments.** Each order-group is enumerated from one configuration of the level below. The five-site group realises 8,536,256 of the `56⁵` law tuples.
- **The table.** With laws scaled by `2²⁴` and tables by `2³⁴`, every rounding upward, `K2c` prints as 0.845071, 0.894864, 0.944946, 0.978358, 0.995052 and 0.998429 at the six tabulated `(p, α)`, and each exact bound is below 1. At `p = 139/25`, `α = 34/25` the six positions print 0.11087, 0.12093, 0.11087, 0.22142, 0.21292, 0.22142, and `κ_max = 0.39208`.

The constants are pointwise. No monotonicity in `p` is claimed.
