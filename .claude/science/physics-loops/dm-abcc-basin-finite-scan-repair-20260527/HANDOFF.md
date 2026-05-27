# Handoff

This branch repairs the DM A-BCC finite-search support row by replacing the
primary hard-coded chart wrapper with a live finite-scan certificate.

Key movement:

- New runner:
  `scripts/frontier_dm_abcc_basin_independent_finite_scan.py`
- Cache:
  `logs/runner-cache/frontier_dm_abcc_basin_independent_finite_scan.txt`
- Result:
  `TOTAL: PASS=16 FAIL=0`
- Pipeline state:
  `dm_abcc_basin_finite_search_support_note_2026-04-30` is reset to
  `audit_status=unaudited`, `effective_status=unaudited`, `ready=true`.

The repaired claim is bounded finite-scan support only. Do not extract this as
global basin exhaustiveness. The remaining hard science target is a genuine
interval/root-isolation proof for all possible basins.
