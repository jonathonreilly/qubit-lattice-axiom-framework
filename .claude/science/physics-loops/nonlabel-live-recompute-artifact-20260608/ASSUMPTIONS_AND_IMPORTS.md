# Assumptions And Imports

## Allowed Current Inputs

- `scripts/NONLABEL_GROWN_BASIN_TARGETED.py` default frozen-log verifier.
- `scripts/nonlabel_grown_basin_recompute_audit_2026_06_08.py` live recompute artifact.
- `logs/runner-cache/nonlabel_grown_basin_recompute_audit_2026_06_08.txt` completed live recompute cache.

## Imports Not Retired

- The basin is not generalized beyond the three restore rows.
- The result is not promoted to an unbounded family theorem.

## Import Movement

The branch retires the imported-log-only defect by requiring the primary verifier to check the SHA-fresh live recompute cache and exact live rows.
