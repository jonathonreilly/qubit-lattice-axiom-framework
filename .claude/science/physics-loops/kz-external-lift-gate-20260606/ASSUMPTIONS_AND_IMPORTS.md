# Assumptions And Imports

## Allowed Current Inputs

- Active queue item `2026-05-03-pr484-kz-external-lift-gate`.
- PR484 review packet and its success criteria.
- Local Python/CVXPY solver availability.
- Direct SU(3) Cartan-torus single-plaquette calculation used only for the
  no-go witness scale.

## Open Imports

- Explicit `SU(3), beta=6` primary-source bracket for the plaquette
  expectation, or a repo-owned SDP reproduction with cutoff, solver, and
  tolerance specified.

## Forbidden Inputs

- Observed plaquette value or Monte Carlo table as proof input.
- Fitted `beta_eff`.
- Same-surface family argument.
- K-Z `SU(infinity)` benchmark reused as target-regime SU(3) bracket.
- Old PR484 retained/effective-status language.
