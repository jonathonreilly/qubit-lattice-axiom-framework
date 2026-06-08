# Route Portfolio

## Selected Route

Add a dedicated live recompute runner whose bare entrypoint is cacheable by the
repo runner-cache harness. The existing source runner now verifies that cache
is present, SHA-fresh, exits zero, reports `SCORECARD PASS=9 FAIL=0`, and
contains the expected drift/seed grid with all row gates passing.

## Rejected Route

Relying on `scripts/NONLABEL_GROWN_DRIFT_BASIN_SWEEP.py --recompute` directly
would not produce a canonical cache with the repo's one-runner-one-cache helper.
It would leave the same audit artifact blocker in place.
