# Route Portfolio

## Route 1: Inline Bridge Repair

Chosen. Add a bridge lemma to the existing theorem note deriving:

- temporal-gauge mixed kernel as a tensor product over spatial links;
- exactly four marked plaquette boundary links;
- trivial-channel identity on non-marked links after normalization;
- dual-orientation equality for inverse boundary links;
- final `a_(p,q)^4` compression.

This is the smallest repair that addresses the audit blocker without creating
a new claim row.

## Route 2: New Upstream Theorem Note

Deferred. A separate bridge theorem note would be audit-cleaner in some repos,
but it creates another row and dependency edge when the missing derivation is
short enough to inline.

## Route 3: Scope Demotion

Fallback only. Narrowing to a purely algebraic `a_(p,q)^4` witness would be
honest but would not unlock the downstream local/environment factorization
claim.

## Route 4: Runner-Only Repair

Rejected. The audit blocker was an operator-level bridge, not just a missing
finite witness. The runner was enhanced, but the source note also needed the
derivation.
