# Handoff

PR: https://github.com/jonathonreilly/cl3-lattice-framework/pull/1935

## What Changed

The primary Fam1 seed-0 runner now contains the load-bearing growth, wave,
`prop_beam`, and `cz` implementations directly. The generated citation graph
therefore records no helper paths for the row, and the row is ready for
re-audit without relying on a truncated helper excerpt.

The source note now scopes the exact bounded claim to the Fam1 seed-0
`H = 0.25` control ladder only; cross-family closure remains downstream.

## Verification

- `python3 scripts/precompute_audit_runners.py --runners scripts/wave_direct_dm_h025_fam1_seed0_control_batch.py --allow-non-main`
- `docs/audit/scripts/run_pipeline.sh`
- `python3 docs/audit/scripts/audit_lint.py`
- `python3 scripts/render_controlled_vocabulary.py --check`
- `python3 scripts/vocab_lint.py --report-only docs/WAVE_DIRECT_DM_H025_FAM1_SEED0_CONTROL_NOTE.md .claude/science/physics-loops/wave-fam1-seed0-helper-packet/*.md`
- `python3 -m py_compile scripts/wave_direct_dm_h025_fam1_seed0_control_batch.py`
- `python3 scripts/precompute_audit_runners.py --runners scripts/wave_direct_dm_h025_fam1_seed0_control_batch.py --allow-non-main --check-only`
- `git diff --check`
