# Handoff

## What Changed

The row now has a local runner for the admitted SM bookkeeping table:
`28 + (7/8) * 90 = 106.75`. The runner does not derive the Standard Model
particle spectrum from framework primitives.

## Verification

- `python3 scripts/frontier_sm_relativistic_dof_count_import.py`
- `bash docs/audit/scripts/run_pipeline.sh`
- `python3 docs/audit/scripts/audit_lint.py --strict`
- `python3 scripts/render_controlled_vocabulary.py --check`
- `python3 scripts/vocab_lint.py --report-only docs/SM_RELATIVISTIC_DOF_COUNT_IMPORT_NOTE_2026-05-17.md .claude/science/physics-loops/sm-dof-bounded-import-runner/*.md`
- `git diff --check`
