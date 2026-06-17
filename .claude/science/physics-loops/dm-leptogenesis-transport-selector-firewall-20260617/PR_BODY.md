## Summary

Source-side repair for `dm_leptogenesis_pmns_transport_extremal_source_candidate_note_2026-04-16`.

The prior audit classified the row as `audited_numerical_match` because the
exact `eta/eta_obs = 1` point came from interpolation against `ETA_OBS`, not
from an independently retained source selector.  This PR preserves the useful
bounded interval witness but makes the crossing root explicitly diagnostic.

## Science Change

- Updates the parent note to state that the interpolated `lambda_*` root is not
  a physical selector or retained prediction.
- Adds `DM_LEPTOGENESIS_PMNS_TRANSPORT_SELECTOR_FIREWALL_NOTE_2026-06-17.md`.
- Adds a deterministic selector-firewall runner proving that interval crossing
  is target-defined unless a separate selector theorem supplies the endpoint or
  interpolation parameter.
- Updates the registered parent runner to enforce the new source boundary.

## Trace Gate

- Trace class: `direct_blocker_closure`
- Target: `dm_leptogenesis_pmns_transport_extremal_source_candidate_note_2026-04-16`
- Blocker addressed: the interpolated equality point was load-bearing as a
  numerical match to `ETA_OBS`.
- Result: bounded interval support is preserved; physical selector closure
  remains open.

## Checks

```bash
python3 scripts/frontier_dm_leptogenesis_pmns_transport_selector_firewall_2026_06_17.py
# PASS=12 FAIL=0

python3 scripts/frontier_dm_leptogenesis_pmns_transport_extremal_source_candidate.py
# PASS=16 FAIL=0

python3 scripts/cached_runner_output.py --refresh scripts/frontier_dm_leptogenesis_pmns_transport_selector_firewall_2026_06_17.py
# status: ok

python3 scripts/cached_runner_output.py --refresh scripts/frontier_dm_leptogenesis_pmns_transport_extremal_source_candidate.py
# status: ok
```

## Review Notes

No audit verdicts, ledger rows, queue rows, front-door status files, or
publication effective-status files are changed.  Review-loop is reviewer-owned
per current workflow.
