# Handoff

PR: https://github.com/jonathonreilly/cl3-lattice-framework/pull/1929

## What Changed

The note now binds only the primary runner's direct Born-safe gravity maximum:
`family=asym`, `threshold=0.05`, `scale=1.0`, `N = 100`,
`grav_ln = +2.297 +/- 0.486`, `born_max = 6.66e-16`, `ok = 6`.

The mass-response fit comparison and source-note dependency edges for that
removed comparison are no longer binding.

## Verification

- `python3 scripts/precompute_audit_runners.py --runners scripts/hard_geometry_gravity_window.py --allow-non-main --check-only`
- `bash docs/audit/scripts/run_pipeline.sh`
- `python3 docs/audit/scripts/audit_lint.py --strict`
- `python3 scripts/render_controlled_vocabulary.py --check`
- `python3 scripts/vocab_lint.py --report-only docs/HARD_GEOMETRY_GRAVITY_WINDOW_NOTE.md .claude/science/physics-loops/hard-geometry-direct-gravity-narrow/*.md`
- `python3 -m py_compile scripts/hard_geometry_gravity_window.py`
- `git diff --check`
