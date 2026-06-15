# Handoff

This PR registers direct anomaly verifiers for two pending critical anomaly notes:

- `SU2_WITTEN_Z2_ANOMALY_THEOREM_NOTE_2026-04-24.md` -> `scripts/frontier_su2_witten_z2_anomaly.py`
- `SU3_CUBIC_ANOMALY_CANCELLATION_THEOREM_NOTE_2026-04-24.md` -> `scripts/frontier_su3_cubic_anomaly_cancellation.py`

Local regeneration confirmed those exact `runner_path` values in the ledger. Generated audit/publication outputs were restored before commit.

The PR does not broaden either anomaly claim and does not alter audit verdicts.
