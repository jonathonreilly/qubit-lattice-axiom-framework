# Assumptions And Imports

## Allowed Inputs

- Minimal Record axiom boundary: Record supplies durable realized outcomes,
  finite scalar additivity, and no probability/dynamics/clock content by
  itself.
- Record dynamics layer reconciliation: post-record counts/histories consume
  realized atoms.
- Record Markov-generator embeddability boundary: discrete kernels,
  generators, clocks, and rates are separate gates.
- Record Markov-generator premise classifier: future-record probability,
  pre-record probability origin, generators, clocks, and rates are separate
  premises.

## Constructed Inside This Block

- A one-parameter positive dial family
  `pi(s) = (1, s, s^2) / (1 + s + s^2)` on a three-atom alphabet.
- Explicit reversible Markov generators with `Q(s) pi(s) = 0` for sampled
  positive dial positions.
- A rate-scaling check showing `Q` and `c Q` preserve the stable dial while
  changing off-diagonal rates and nonzero eigenvalues.
- A two-state semigroup check showing the same transition kernel can come from
  different rate/clock pairs with the same dimensionless product.

## Open Imports

- Physical production generator or action.
- Born/IID or equivalent pre-record probability-origin bridge.
- Physical time metric or clock/rate unit.
- Any sector-specific argument selecting a particular generation/Koide dial
  value.

## Forbidden Inputs

- Observed masses or target dial values as proof inputs.
- Claiming Record alone selects a stable dial location.
- Claiming a stationary distribution determines absolute physical rates.
- Treating this branch as a physical dynamics closure.
