# No-Go Ledger

## Distance-Law Quick Timeout Bump

An exploratory refresh of
`scripts/distance_law_wide_continuum.py` with `--timeout-sec 600` was stopped
after more than six minutes without completion.  This lane should not be
packaged as a simple timeout-cache repair.

## Status Overclaim

This block does not claim the two source notes are audit-clean.  It only
removes the stale timeout-cache blocker by proving the runners complete under
an appropriate declared timeout.
