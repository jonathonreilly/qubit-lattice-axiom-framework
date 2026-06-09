# Assumptions And Imports

## Closed Or Reduced

- The decisive stable-circular-orbit edge no longer needs the full Bertrand
  theorem. The repo support note derives `V(r) = -k/r^(d-2)` from the
  continuum radial Green kernel and checks
  `d^2 V_eff / dr^2 |_(r_c) = k(d-2)(4-d)/r_c^d`.
- For integer `d >= 3`, that sign is positive only at `d = 3`, marginal at
  `d = 4`, and negative for `d >= 5`.

## Still Open

- The full Bertrand closed-orbit theorem remains external context if a later
  claim needs all bounded orbits to be closed.
- The Coulomb route remains bounded companion support only: the scaling lemma
  excludes `d >= 5`, leaves `d = 4` marginal, and does not prove a physical
  hydrogenic `d = 3` spectrum.
- The physical electromagnetic sector, coupling, and full atomic-stability
  theorem remain outside this PR.
- Independent audit owns any effective status change.
