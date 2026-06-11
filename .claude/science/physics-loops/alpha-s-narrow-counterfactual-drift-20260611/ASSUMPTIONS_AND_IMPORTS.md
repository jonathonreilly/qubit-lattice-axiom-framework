# Assumptions And Imports

## Closed Inputs

- `alpha_bare` and `u_0` are abstract positive real symbols.
- The retained abstract tadpole-power authority supplies
  `alpha_LM = alpha_bare/u_0` and `alpha_s(v) = alpha_bare/u_0^2`.

## Not Imported

- No `u_0` value is used.
- No plaquette evaluation, low-energy running bridge, or observed
  `alpha_s` value is used.
- No new axiom is introduced.
- No audit verdict or ledger status is modified.

## Repair Point

For the counterfactual powers `(1,1)`, the exact difference is
`alpha_bare^2*(1 - u_0)/u_0^2`. Equality would force the special boundary
`u_0 = 1`, not `alpha_bare = u_0`.
