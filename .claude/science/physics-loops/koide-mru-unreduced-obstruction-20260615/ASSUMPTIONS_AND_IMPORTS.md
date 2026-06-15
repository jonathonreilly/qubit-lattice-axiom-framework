# Assumptions And Imports

## Retained dependency used

- `koide_dweh_cyclic_compression_note_2026-04-18`: supplies the cyclic
  compression surface `span_R{I, C+C^2, i(C-C^2)}` and the associated
  three-channel carrier.

## Load-bearing algebra in this branch

- Lagrange multiplier calculation for
  `S_{mu,nu} = mu log(E_+) + nu log(E_perp)` at fixed total block power.
- Projector determinant calculation
  `det(alpha P_+ + beta P_perp) = alpha beta^2` with ranks `(1, 2)`.

## Explicitly not imported as proof

- No physical scalar-lane `SO(2)` quotient theorem is imported.
- No `cos(3 arg b)` decoupling theorem is imported.
- No observed charged-lepton values, fitted selectors, or new axioms are used.

The reduced carrier calculation is kept only as context and is not a
load-bearing premise for the bounded theorem claim.
