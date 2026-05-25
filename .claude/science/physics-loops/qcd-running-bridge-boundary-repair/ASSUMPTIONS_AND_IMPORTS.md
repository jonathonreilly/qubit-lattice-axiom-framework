# Assumptions And Imports

## Load-Bearing Inputs

No repository source note is load-bearing after the repair.

The running kernel uses external standard-infrastructure inputs:

- admitted `alpha_s(v) = 0.103304`;
- admitted electroweak boundary scale `v = 246.282818290129 GeV`;
- PDG `M_Z`, quark-mass thresholds, and alpha_s comparator values;
- Machacek-Vaughn / Arason two-loop SM RGE coefficients.

## Removed As One-Hop Repo Dependencies

- `plaquette_self_consistency_note`: upstream alpha_s(v) derivation remains
  conditional and is no longer bundled into this kernel row.
- `gauge_vacuum_plaquette_rho_pq6_wilson_environment_bounded_note_2026-05-09`:
  upstream finite coefficient support is not part of the running-kernel claim.

## Axioms

No new axioms are introduced.
