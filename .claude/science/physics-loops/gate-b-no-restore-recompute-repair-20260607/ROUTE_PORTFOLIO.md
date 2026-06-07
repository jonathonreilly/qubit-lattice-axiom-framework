# Route Portfolio

## Route A: completed recompute certificate

Run the live one-seed replay, write a deterministic recompute certificate,
refresh stale source rows exposed by the recompute, update the default verifier
to compare the source log against it, and refresh the cache.

Disposition: executed.

## Route B: broaden tolerance only

Accept the old Born residuals under a loose tolerance.

Disposition: rejected; the recompute exposed real source-row drift, so the
source rows were refreshed instead.

## Route C: audit ledger retag

Directly update the audit row.

Disposition: forbidden for this PR; the science branch only queues re-audit.
