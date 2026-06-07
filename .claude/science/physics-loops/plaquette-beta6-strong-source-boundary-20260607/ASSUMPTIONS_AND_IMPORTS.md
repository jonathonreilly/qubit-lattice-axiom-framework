# Assumptions And Imports

## Explicit Supplied Inputs

- `c_1 = 1`
- `c_4 = 4`
- `c_6 = 24`
- `c_7 = -24`
- `c_8 = 100`
- `u_eval = 1/3`
- `P_MC = 0.5934` as a comparator only

## Retired Hidden Import

The Padé algebra is no longer treated as imported textbook machinery. The
runner solves the Padé system, checks `series * Q - P = O(u^7)`, verifies the
nonzero denominator at the supplied point, and checks the exact rational value.

## Still Open

The coefficient packet, beta-to-`u` convention, and MC comparator remain outside
the row. No retained authority for those physical inputs is introduced here.

