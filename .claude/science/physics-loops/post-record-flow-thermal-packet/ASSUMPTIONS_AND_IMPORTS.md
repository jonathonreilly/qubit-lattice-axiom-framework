# Assumptions And Imports

## Current Structured Inputs

- `docs/audit/data/audit_ledger.json` is read but not modified.
- `scripts/frontier_post_record_stability_dynamics_selector_subdivision_2026_06_06.py`
  is statically imported by the flow/thermal runner.
- Through the parent helper, the selector/dial helper is visible as a
  transitive helper.
- `outputs/post_record_flow_thermal_stable_setting_slice_2026_06_07.json`
  records the current 60-row flow/thermal slice.

## Out Of Scope

- No audit verdicts are applied.
- No selected dial value is claimed.
- No physical flow, score, thermal rule, production dynamics, arrow, clock, or
  rate is derived from Record.
