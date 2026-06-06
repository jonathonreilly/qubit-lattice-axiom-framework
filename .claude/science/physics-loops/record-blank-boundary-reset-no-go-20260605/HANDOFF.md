# Handoff

## Result

Exact negative-boundary block ready for stacked review.

## Main Finding

Clean broadcast from arbitrary old fragment states is many-to-one on the closed
four-qubit space and cannot be unitary. Fanout needs blank fragments, or reset
must export old memory to an explicit sink/environment.

## Boundaries

- Does not derive blank fragments, erasure, thermodynamic reset, sink dynamics,
  physical Hamiltonian, rates, clock, probabilities, or a dial setting.
- Does not apply audit verdicts.

## Next Exact Action

Open stacked PR against
`physics-loop/record-pointer-broadcast-hamiltonian-20260605`, then patch this
loop pack with the PR URL.
