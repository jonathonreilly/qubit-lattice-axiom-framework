# Goal

Finish a branch-local, read-only subdivision of the
`stability_or_dynamics_selector` bucket produced by the selector/dial
subdivision block.

The target movement is exact support for dispatching rows into two queues:

- `flow_or_thermal_stability`: rows whose next useful work is a supplied flow,
  map, fixed point, attractor, separatrix, thermal branch, entropy rule, or
  stability certificate.
- `arrow_or_dynamics_bridge`: rows whose next useful work is a physical arrow,
  Hamiltonian, transfer, kernel, instrument, decoherence, measurement, clock,
  or rate bridge.

The block must preserve the user's dial constraint: stable settings may be
recorded as stable settings, but they are not selected dials.

## Non-goals

- No audit data edits.
- No audit verdict application.
- No row promotion.
- No forced generation or Koide dial.
- No claim that Record derives a physical arrow, kernel, Hamiltonian,
  instrument, clock, or rate.
- No physical selector claim from keyword membership alone.
