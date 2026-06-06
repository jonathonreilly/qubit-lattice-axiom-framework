# Handoff

This PR adds a narrow exact-support bridge for
`H_staggered_chirality = epsilon(x) Omega_global`.

The core theorem is that the scalar nearest-neighbor edge-flip grading on the
`Z^3` coordinate graph is unique up to global sign and equals
`epsilon(x)=(-1)^(x_1+x_2+x_3)`. Multiplying by the A1 central pseudoscalar
`sigma_1 sigma_2 sigma_3=iI` gives the local staggered chirality sign field.

Reviewer focus:

- Decide whether this bridge is enough to re-audit the 2026-06-03
  Kawamoto-Smit rescoping companion cleanly.
- Decide whether the lattice Noether row can now move past the specific
  KS phase/chirality sign-surface packet gap.
- Preserve the boundary: this PR does not close the full staggered-Dirac
  realization gate or species-label bridge.

No audit verdicts or audit ledger rows are changed in this branch.
