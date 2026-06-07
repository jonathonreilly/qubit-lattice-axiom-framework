# Route Portfolio

## Route A: all-weight positivity plus formal distribution bridge

Status: executed.

This directly attacks the audit blocker while avoiding an unsupported L2
upgrade. The proof is short: every `(p,q)` appears at finite word length
`p+q` inside powers of `3 direct_sum 3bar`, so the Wilson exponential has a
strict positive coefficient for `beta>0`.

## Route B: prove full L2/bounded-operator decay for the residual sequence

Status: deferred.

This would be stronger but requires a real asymptotic estimate for
`r_(p,q)^env(beta)`, not just Wilson one-link positivity.

## Route C: compute beta=6 Perron data

Status: deferred.

This is a separate parent-gate computation and would broaden the branch.
