# Block123: PR230 Source-Higgs LSZ Readout Formula

## Summary

Adds a constructive PR230 campaign artifact stacked above Block122.  Block123
derives the strict source-Higgs pole-row formula that would remove the
`kappa_s` ambiguity without setting `kappa_s = 1`:

```text
y_H = (dE_top/ds) * sqrt(Res C_HH) / Res C_sH
```

The runner verifies source-coordinate rescaling invariance, shows the
source-only `kappa_s=1` readout varies, and records an orthogonal-top-coupling
counterexample.  Current PR230 does not satisfy the row/action premises.

## Status

- `proposal_allowed=false`
- `actual_current_surface_status`: exact-support plus open premise
- no retained or `proposed_retained` wording

## Files

- `docs/YT_PR230_BLOCK123_SOURCE_HIGGS_LSZ_READOUT_FORMULA_NOTE_2026-05-17.md`
- `scripts/frontier_yt_pr230_block123_source_higgs_lsz_readout_formula.py`
- `outputs/yt_pr230_block123_source_higgs_lsz_readout_formula_2026-05-17.json`
- `.claude/science/physics-loops/pr230-retained-closure-campaign-20260517/`

## Verification

```text
python3 -m py_compile scripts/frontier_yt_pr230_block123_source_higgs_lsz_readout_formula.py scripts/frontier_yt_pr230_campaign_status_certificate.py scripts/frontier_yt_pr230_assumption_import_stress.py
python3 scripts/frontier_yt_pr230_block123_source_higgs_lsz_readout_formula.py
# SUMMARY: PASS=12 FAIL=0

python3 scripts/frontier_yt_pr230_full_positive_closure_assembly_gate.py
# SUMMARY: PASS=200 FAIL=0

python3 scripts/frontier_yt_retained_closure_route_certificate.py
# SUMMARY: PASS=325 FAIL=0

python3 scripts/frontier_yt_pr230_positive_closure_completion_audit.py
# SUMMARY: PASS=79 FAIL=0

python3 scripts/frontier_yt_pr230_campaign_status_certificate.py
# SUMMARY: PASS=441 FAIL=0

python3 scripts/frontier_yt_pr230_assumption_import_stress.py
# SUMMARY: PASS=124 FAIL=0

git diff --check
# clean

python3 docs/audit/scripts/audit_lint.py --strict
# OK: no errors; 5 known warnings

bash docs/audit/scripts/run_pipeline.sh
# Pipeline complete; generated docs/audit churn restored
```
