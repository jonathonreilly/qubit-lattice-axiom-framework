# Handoff

## What Moved

`docs/ANOMALY_FORCES_TIME_THEOREM.md` now routes HY-surface authority to
`GRAPH_FIRST_SU3_INTEGRATION_NOTE.md`, whose selected-axis finite-cube
construction contains the `gl(3)+gl(1)` split and traceless `u(1)` spectrum.
The runner recomputes that spectrum and now guards the source edge.

The parent theorem also no longer names the prior single-clock source path for
B-AXIS provenance. B-AXIS remains declared locally in this theorem; the prior
single-clock source is wording context only.

## What Did Not Move

This does not derive P-HY, P-ABJ, P-COMP, P-REC, or B-AXIS. It does not set an
audit result and does not edit any audit ledger/status/publication files.

## Reviewer Checks

- Confirm no full split-out abelian-surface slug appears in the parent theorem,
  anomaly runner, or runner cache.
- Confirm no full prior single-clock source slug appears in the parent theorem,
  anomaly runner, or runner cache.
- Confirm `GRAPH_FIRST_SU3_INTEGRATION_NOTE.md` is the HY-surface source named
  by the parent theorem.
- Confirm `scripts/frontier_anomaly_forces_time.py` and its cache remain fresh:
  `python3 scripts/cached_runner_output.py scripts/frontier_anomaly_forces_time.py --check-only`.

## Next Science

The high-value remaining physics moves are P-HY, P-REC, P-ABJ, and B-AXIS. This
PR only clears the parent-edge hygiene problem so those premises are easier to
see independently.
