# Handoff

This PR repairs the audited conditional product-grading eta-sector row by
narrowing T3 to the exact half-integer cutoff family.

The note now gives the floor formula
`eta_delta(A(a)) = floor(Lambda-a)+1-floor(Lambda+a)` for `a in (0,1/2)`,
states the fixed-twist condition `a <= frac(Lambda) < 1-a`, and claims the
uniform interval theorem only for `Lambda in Z>=0+1/2`.

The runner now checks:
- the original label table at `Lambda=20.5`;
- the floor formula against direct spectral counts;
- sampled half-integer cutoffs;
- excluded non-half-integer counterexamples `Lambda=20.25` and `20.75`.

No audit ledger, queue, status, or verdict files were edited.
