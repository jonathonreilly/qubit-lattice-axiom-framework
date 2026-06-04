# Assumptions And Imports

## Used Natively

- Finite Cl(3) site algebra gives finite single-term operator norm at
  canonical normalization.
- Finite-range local rule on a finite cubic block gives finite
  per-site touch count and finite interaction adjacency degree.
- Duhamel iteration and operator-norm submultiplicativity give the
  per-site sum `J_* = max_z sum_{X contains z} ||h_X||`.

## Not Claimed

- No new axiom.
- No derivation of a transfer gap.
- No unconditional spatial cluster decomposition.
- No continuum Yang-Mills or thermodynamic-limit claim.

## External Math Discipline

The LR-series shape is standard textbook mathematical physics, but the
load-bearing constants are applied inside the framework:

- source proof defines `J_*` and `D_int`;
- runner computes the corrected nearest-neighbour representative
  constants and checks `J <= J_*` with strict inequality.
