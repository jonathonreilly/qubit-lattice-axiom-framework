# Handoff

## Summary

This PR repairs `exponent_derivation` by replacing a positive dimensional
exponent derivation with a bounded boundary note grounded in the retained
matched 2D/4D replay.

## Claim Movement

- Before: the row proposed `alpha ~ 1/d_spatial` with 5D/6D predictions.
- After: the row says the path-count/mixing argument is heuristic, and the
  retained matched replay does not support a clean dimension-only law.
- Remaining: a positive theorem needs an actual DAG path-measure derivation or
  a broader matched-dimensional sweep controlling topology/connectivity.

## Verification

- `python3 scripts/frontier_exponent_derivation_scope_repair.py`
- `python3 scripts/vocab_lint.py --report-only docs/EXPONENT_DERIVATION.md .claude/science/physics-loops/exponent-derivation-scope-repair-20260527/*.md`
- `bash docs/audit/scripts/run_pipeline.sh`
- `git diff --check`

## Next Action

Open as a draft PR. If review accepts the demotion, independent audit can
re-audit the row as a bounded boundary rather than a positive exponent
mechanism.
