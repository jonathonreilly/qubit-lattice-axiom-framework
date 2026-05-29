# Assumptions And Imports

## PMNS TM2 Row

Used only standard PMNS parametrization algebra already present in the row.
The repair adds the missing nonsingular chamber condition
`c12 s12 s13 != 0`, equivalently `0 < sin^2(theta_13) < 2/3` under the TM2
sum rule. No observed PMNS values are used as proof input.

## Planck Coframe Row

Used the existing accepted-premise packet (P1) and retained bounded
`CL3_COMPLEXIFICATION_SPLIT` dependency. The repair does not add a new
framework axiom or new retained premise. It narrows the daggered CAR statement
to the Pauli-realized compatible Hermitian representative and adds a
nonunitary-similarity boundary check showing why (P1) alone does not determine
fixed-background-dagger CAR.

## Imports Retired Or Exposed

- Retired for PMNS: hidden division by `c12 s12 s13` without excluding the
  singular endpoint.
- Exposed for Planck: fixed-background daggered CAR remains non-invariant
  without choosing a compatible Hermitian representative.
