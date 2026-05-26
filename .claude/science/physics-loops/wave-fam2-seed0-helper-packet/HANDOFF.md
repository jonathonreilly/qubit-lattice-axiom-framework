# Handoff

PR: https://github.com/jonathonreilly/cl3-lattice-framework/pull/1933

## What Changed

The primary Fam2 seed-0 runner now contains the load-bearing growth, wave,
`prop_beam`, and `cz` implementations directly.  The generated citation graph
therefore records no helper paths for the row, and the row is ready for
re-audit without relying on a truncated helper excerpt.

## Verification

- `python3 scripts/precompute_audit_runners.py --runners scripts/wave_direct_dm_h025_fam2_seed0_control_batch.py --allow-non-main`
- `bash docs/audit/scripts/run_pipeline.sh`
- `python3 docs/audit/scripts/audit_lint.py --strict`
- `python3 scripts/render_controlled_vocabulary.py --check`
- `python3 scripts/vocab_lint.py --report-only docs/WAVE_DIRECT_DM_H025_FAM2_SEED0_CONTROL_NOTE.md .claude/science/physics-loops/wave-fam2-seed0-helper-packet/*.md`
- `python3 -m py_compile scripts/wave_direct_dm_h025_fam2_seed0_control_batch.py`
- `python3 scripts/precompute_audit_runners.py --runners scripts/wave_direct_dm_h025_fam2_seed0_control_batch.py --allow-non-main --check-only`
- `git diff --check`
