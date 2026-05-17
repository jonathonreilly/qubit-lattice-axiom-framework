# Block117: source-reparametrization invariant minimal-data boundary

## Summary

Adds a PR230 Block117 artifact that narrows the retained top-Yukawa blocker to
the minimal same-surface invariant data packet.  It verifies that current raw
source slopes, finite source aliases, W/Z mass-plus-response dictionaries,
finite Schur packets, and neutral H1/H2 support do not supply retained closure.

## Status

- `proposal_allowed=false`
- `actual_current_surface_status`: exact negative boundary
- no retained or `proposed_retained` wording

## Files

- `docs/YT_PR230_BLOCK117_SOURCE_REPARAM_INVARIANT_MINIMAL_DATA_NOTE_2026-05-17.md`
- `scripts/frontier_yt_pr230_block117_source_reparam_invariant_minimal_data.py`
- `outputs/yt_pr230_block117_source_reparam_invariant_minimal_data_2026-05-17.json`
- `.claude/science/physics-loops/pr230-retained-closure-campaign-20260517/`

## Verification

```text
python3 -m py_compile scripts/frontier_yt_pr230_block117_source_reparam_invariant_minimal_data.py
python3 scripts/frontier_yt_pr230_block117_source_reparam_invariant_minimal_data.py
# SUMMARY: PASS=14 FAIL=0

python3 scripts/frontier_yt_pr230_full_positive_closure_assembly_gate.py
# SUMMARY: PASS=200 FAIL=0

python3 scripts/frontier_yt_retained_closure_route_certificate.py
# SUMMARY: PASS=325 FAIL=0

python3 scripts/frontier_yt_pr230_positive_closure_completion_audit.py
# SUMMARY: PASS=79 FAIL=0

python3 scripts/frontier_yt_pr230_campaign_status_certificate.py
# SUMMARY: PASS=436 FAIL=0

python3 scripts/frontier_yt_pr230_assumption_import_stress.py
# SUMMARY: PASS=119 FAIL=0

git diff --check
# clean
```

