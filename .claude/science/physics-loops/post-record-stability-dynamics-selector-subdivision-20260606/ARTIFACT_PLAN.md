# Artifact Plan

## Created

- `docs/POST_RECORD_STABILITY_DYNAMICS_SELECTOR_SUBDIVISION_2026-06-06.md`
- `scripts/frontier_post_record_stability_dynamics_selector_subdivision_2026_06_06.py`
- `logs/runner-cache/frontier_post_record_stability_dynamics_selector_subdivision_2026_06_06.txt`
- `.claude/science/physics-loops/post-record-stability-dynamics-selector-subdivision-20260606/`

## Runner requirements

- Verify source anchors in this note and upstream notes.
- Recompute the 64-row stability/dynamics selector scope from the current
  ledger.
- Split into exactly 36 `flow_or_thermal_stability` rows and 28
  `arrow_or_dynamics_bridge` rows.
- Verify representative rows in both sub-buckets.
- Verify the audit ledger hash is unchanged.
- Verify no audit-data write, audit verdict, row promotion, stable-dial
  selection, generation/Koide selection, or Record-derived physical arrow flag
  is set.

## Review requirements

- Runner summary is `SUMMARY: PASS=25 FAIL=0`.
- `py_compile` passes.
- Cached summary is present.
- ASCII scan is clean.
- Overclaim scan is clean.
- Loop pack contains 13 files.
- `git diff --check` passes.
