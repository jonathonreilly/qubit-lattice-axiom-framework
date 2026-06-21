# Route Portfolio

## Selected Route: Runner-Cache Evidence Refresh

Score: high landability, low blast radius, direct audit-unblock value.

The main obstacle for this target was not a failing runner; it was an unhelpful cache record:
the cache said `status: ok` but did not preserve the runner stdout needed for review. Running
the precompute path under the runner's declared timeout produced a full transcript with
`PASS = 46`, `FAIL = 0`.

## Rejected Route: Source Rewrite For Runtime

Score: unnecessary.

The runner completed under its declared timeout. A source rewrite would add risk without
retiring a current blocker.

## Included Route: Queue/Ledger Refresh

Score: required for strict-lint cleanliness.

The narrow cache-only diff passed cache freshness and whitespace checks, but strict audit lint
failed on stale retained-grade ledger hashes already present on the base. Running the canonical
pipeline regenerated the audit queue, ledger, helper-dependency map, publication effective-status
views, and front-door status. These are generated support surfaces, not hand-applied audit
verdicts.

## Rejected Route: Audit Verdict Application

Score: forbidden by user instruction.

The user explicitly asked not to audit. Independent audit remains responsible for any verdict.
