# Nonlabel Drift Recompute Artifact Handoff

## Claim

`nonlabel_grown_drift_basin_note`

## Repair

Added `scripts/nonlabel_grown_drift_basin_recompute_audit_2026_06_08.py`,
which reruns the live grown-row geometry-sector calculation for all nine
drift/seed rows in the source note. The runner checks exact zero-source and
neutral-pair gates, sign orientation, double-charge sign, and charge-exponent
tolerance.

`scripts/NONLABEL_GROWN_DRIFT_BASIN_SWEEP.py` now checks the SHA-fresh
recompute cache in its default verifier path, so the restricted packet no
longer relies only on the frozen transcript.

## Evidence

- `logs/runner-cache/nonlabel_grown_drift_basin_recompute_audit_2026_06_08.txt`
  has `status: ok`, `exit_code: 0`, `timeout_sec: 420`, and
  `SCORECARD PASS=9 FAIL=0`.
- `logs/runner-cache/NONLABEL_GROWN_DRIFT_BASIN_SWEEP.txt` has
  `SCORECARD PASS=10 FAIL=0`, counting the nine frozen rows plus the live
  recompute artifact.

## Boundary

This does not widen the theorem beyond the stated finite drift/seed grid at
fixed `restore = 0.70`. It does not add a new axiom and does not edit
`docs/audit/**`.
