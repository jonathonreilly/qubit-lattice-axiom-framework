# Route Portfolio

## Route A: completed recompute certificate

Run the live replay, write a deterministic recompute certificate, update the
default verifier to compare frozen rows against it, and refresh the cache.

Disposition: executed.

## Route B: independent analytic derivation

Derive the three finite propagation rows without using the runner implementation.

Disposition: not needed for this blocker; the auditor allowed a completed
`--recompute` audit run or cached recompute certificate.

## Route C: audit ledger retag

Directly update the audit row.

Disposition: forbidden for this PR; the science branch only queues re-audit.
