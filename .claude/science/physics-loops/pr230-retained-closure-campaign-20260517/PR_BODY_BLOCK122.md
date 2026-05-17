# Block122: PR230 Hamming-Axis Action/LSZ Normalization Gap

## Summary

Adds a stacked PR230 campaign artifact on top of Blocks120-121.  Base Block118
selects the finite Hamming-Dirichlet taste-radial `O_H` axis as exact support,
and base Block119 adds a native finite Dirichlet action/LSZ support probe.
Block122 proves that these finite supports do not determine accepted action,
scalar LSZ metric, source-overlap normalization, contact subtraction, or
strict source-Higgs pole rows.

## Status

- `proposal_allowed=false`
- `actual_current_surface_status`: exact negative boundary
- no retained or `proposed_retained` wording

## Files

- `docs/YT_PR230_BLOCK122_HAMMING_AXIS_ACTION_LSZ_NORMALIZATION_GAP_NOTE_2026-05-17.md`
- `scripts/frontier_yt_pr230_block122_hamming_axis_action_lsz_normalization_gap.py`
- `outputs/yt_pr230_block122_hamming_axis_action_lsz_normalization_gap_2026-05-17.json`
- `.claude/science/physics-loops/pr230-retained-closure-campaign-20260517/`

## Verification

```text
python3 -m py_compile scripts/frontier_yt_pr230_block122_hamming_axis_action_lsz_normalization_gap.py
python3 scripts/frontier_yt_pr230_block122_hamming_axis_action_lsz_normalization_gap.py
# SUMMARY: PASS=11 FAIL=0

python3 scripts/frontier_yt_pr230_full_positive_closure_assembly_gate.py
# SUMMARY: PASS=200 FAIL=0

python3 scripts/frontier_yt_retained_closure_route_certificate.py
# SUMMARY: PASS=325 FAIL=0

python3 scripts/frontier_yt_pr230_positive_closure_completion_audit.py
# SUMMARY: PASS=79 FAIL=0

python3 scripts/frontier_yt_pr230_campaign_status_certificate.py
# SUMMARY: PASS=440 FAIL=0

python3 scripts/frontier_yt_pr230_assumption_import_stress.py
# SUMMARY: PASS=123 FAIL=0

python3 scripts/frontier_yt_fh_lsz_target_timeseries_full_set_checkpoint.py
# SUMMARY: PASS=9 FAIL=0

python3 scripts/frontier_yt_pr230_schur_higher_shell_chunk_checkpoint.py --chunk-index 63
# SUMMARY: PASS=15 FAIL=0

git diff --check
# clean
```
