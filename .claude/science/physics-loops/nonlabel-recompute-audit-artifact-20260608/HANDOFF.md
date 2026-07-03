# Nonlabel Recompute Audit Artifact Handoff

## Claim

`nonlabel_grown_basin_note`

## Repair

Added `scripts/nonlabel_grown_basin_recompute_audit_2026_06_08.py`, which
reruns the live grown-row geometry-sector calculation for restore values
`0.60`, `0.70`, and `0.80`, then checks the row gates and exponent arithmetic.

## Verification

- `python3 scripts/nonlabel_grown_basin_recompute_audit_2026_06_08.py`
- `python3 scripts/cached_runner_output.py --refresh scripts/nonlabel_grown_basin_recompute_audit_2026_06_08.py --timeout-sec 180`
- `python3 scripts/cached_runner_output.py --check-only scripts/nonlabel_grown_basin_recompute_audit_2026_06_08.py`
- `python3 scripts/NONLABEL_GROWN_BASIN_TARGETED.py`
- `git diff --check`
- `git diff -- docs/audit`

## Remaining Science

This does not derive a wider restore interval, a continuum nonlabel theorem, or
an unbounded family statement.  It only removes the audit artifact blocker for
the three-row bounded basin already claimed by the source note.
