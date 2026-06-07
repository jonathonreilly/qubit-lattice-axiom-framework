# Route Portfolio

## Route A: Cache Refresh

Status: executed for 18 runners.

This is the smallest safe unblock: update stale cache headers and bodies for
audited rows whose current runners exit successfully.

## Route B: Include Failing Internal Scorecard

Status: rejected for this clean batch.

`frontier_observable_principle_p1_bridge_operator_algebraic_external_narrow.py`
refreshes as a process but reports `TOTAL: PASS=28, FAIL=1`. That belongs in a
repair PR, not a clean cache-refresh batch.

## Route C: Recreate Missing Runners

Status: deferred.

Rows with missing runner files need source reconstruction or ledger/source
repair and should be handled one at a time.
