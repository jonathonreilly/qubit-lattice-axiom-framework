# Blocks117-118: PR230 invariant-data and Schur pole-derivative boundaries

## Summary

Adds two PR230 campaign artifacts on the stacked review branch into PR #230:

- Block117 narrows the top-Yukawa blocker to the minimal same-surface
  source-reparametrization invariant data packet.
- Block118 proves that the complete finite Schur A/B/C packet does not
  determine strict Schur/Feshbach `K'(pole)` or residue.

## Status

- `proposal_allowed=false`
- `actual_current_surface_status`: exact negative boundary
- no retained or `proposed_retained` wording

## Files

- `docs/YT_PR230_BLOCK117_SOURCE_REPARAM_INVARIANT_MINIMAL_DATA_NOTE_2026-05-17.md`
- `scripts/frontier_yt_pr230_block117_source_reparam_invariant_minimal_data.py`
- `outputs/yt_pr230_block117_source_reparam_invariant_minimal_data_2026-05-17.json`
- `docs/YT_PR230_BLOCK118_SCHUR_FINITE_PACKET_POLE_DERIVATIVE_NONIDENTIFIABILITY_NOTE_2026-05-17.md`
- `scripts/frontier_yt_pr230_block118_schur_finite_packet_pole_derivative_nonidentifiability.py`
- `outputs/yt_pr230_block118_schur_finite_packet_pole_derivative_nonidentifiability_2026-05-17.json`
- `.claude/science/physics-loops/pr230-retained-closure-campaign-20260517/`

## Verification

```text
python3 -m py_compile scripts/frontier_yt_pr230_block117_source_reparam_invariant_minimal_data.py
python3 scripts/frontier_yt_pr230_block117_source_reparam_invariant_minimal_data.py
# SUMMARY: PASS=14 FAIL=0

python3 -m py_compile scripts/frontier_yt_pr230_block118_schur_finite_packet_pole_derivative_nonidentifiability.py
python3 scripts/frontier_yt_pr230_block118_schur_finite_packet_pole_derivative_nonidentifiability.py
# SUMMARY: PASS=10 FAIL=0

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
