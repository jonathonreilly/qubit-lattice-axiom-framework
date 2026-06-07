# Route Portfolio

## Route A: Boundary Check Repair

Status: executed.

The runner label already stated the intended boundary: cluster decomposition is
not usable as a positive retained primitive to close P1. The boolean check was
too strict because it treated `retained_bounded` as a failure. The repair
distinguishes positive retained closure from bounded context.

## Route B: Promote P1 Closure

Status: rejected.

The note and runner continue to state that operator-algebraic primitives do not
retire P1; they only give multiplicative factorization and counterexamples to
additivity.
