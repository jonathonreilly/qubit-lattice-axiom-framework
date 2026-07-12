# Review History

## Iteration 1 — fix

Three independent review surfaces found five material issues:

- Retyping the existing selector path as `no_go` would launder negative
  authority into its positive downstream consumers because graph edges do not
  carry polarity.
- The no-go's N1–N8 record had to live in the audit-visible source packet.
- The countermodel runner needed actual matrix-unit and spectral-projector
  checks, an explicit base structure, and complete state-neutral laws.
- The KL witnesses had to preserve the native fixed totals, and all synthetic
  countermodel choices had to be inventoried.
- The conditional optimizer had to stop describing its finite-search column
  as unique and had to check constrained-solver termination.

Disposition: `fix`.

## Iteration 2 — one narrow fix

The physics/no-go, import/governance, and code/runner reviewers confirmed the
separate-claim architecture, current-premise theorem, native-total witness,
primitive extensions, optimizer narrowing, solver checks, and cache format.
One remaining runner gate was non-discriminating: covariance plus degeneracy
would also accept a bottom-eigenspace implementation.

Disposition: `fix` on that executable gate; all other surfaces passed.

## Iteration 3 — pass

The repaired spectral gate verifies Hermiticity, idempotence, trace one,
`B P = lambda_plus P`, strict Rayleigh maximality over the complement, unitary
covariance, direct `6 P0 -> P0`, and degeneracy. The no-go runner reports
`PASS=24 FAIL=0`, and the regenerated cache is source-hash fresh.

Final local review-loop disposition: `pass`. Independent audit remains the
only authority that can assign effective retained-grade status.
