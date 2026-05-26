# Handoff

PR: pending

## What Changed

The DM/PMNS stationary-classification row now advertises only the bounded
algebraic parity/KKT residual and sampled dominant-pair action-gap diagnostic.
Global branch enumeration, unique physical selector status, and physical
off-seed source-law claims are removed from both prose and runner stdout.

## Verification

- `python3 scripts/precompute_audit_runners.py --runners scripts/frontier_dm_leptogenesis_pmns_analytic_stationary_classification_theorem.py --allow-non-main`
- `python3 scripts/frontier_dm_leptogenesis_pmns_analytic_stationary_classification_theorem.py`
- `bash docs/audit/scripts/run_pipeline.sh`
- `python3 docs/audit/scripts/audit_lint.py --strict`
- `python3 scripts/render_controlled_vocabulary.py --check`
- `python3 scripts/vocab_lint.py --report-only docs/DM_LEPTOGENESIS_PMNS_ANALYTIC_STATIONARY_CLASSIFICATION_THEOREM_NOTE_2026-04-16.md .claude/science/physics-loops/dm-pmns-stationary-diagnostic-narrow/*.md`
- `python3 -m py_compile scripts/frontier_dm_leptogenesis_pmns_analytic_stationary_classification_theorem.py`
- `git diff --check`

