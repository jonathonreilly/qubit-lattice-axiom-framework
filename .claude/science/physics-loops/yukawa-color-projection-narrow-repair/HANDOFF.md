# Handoff

## What Changed

This PR follows the existing judicial audit repair target for
`YUKAWA_COLOR_PROJECTION_THEOREM.md`: narrow the claim text to only the exact
adjoint representation-dimension fraction.

The source now distinguishes:

- `f_adj,dim = 8/9`: representation-dimension fraction, in scope.
- `F_adjoint(M)`: matrix-dependent trace fraction, out of scope.
- `R_conn`: lattice connected-trace observable, out of scope.

## Audit Queue Result

After regeneration, `yukawa_color_projection_theorem` is queue rank 1,
critical, `ready: Y`, with 978 descendants.

## Verification

- `python3 -m py_compile scripts/frontier_ew_current_fierz_channel_decomposition.py scripts/audit_companion_ew_fierz_general_n_c_exact.py`
- `python3 scripts/frontier_ew_current_fierz_channel_decomposition.py`
- `python3 scripts/audit_companion_ew_fierz_general_n_c_exact.py`
- `bash docs/audit/scripts/run_pipeline.sh`
- `python3 docs/audit/scripts/audit_lint.py --strict`
- `git diff --check`
- `python3 scripts/render_controlled_vocabulary.py --check`
- `python3 scripts/vocab_lint.py --report-only docs/YUKAWA_COLOR_PROJECTION_THEOREM.md .claude/science/physics-loops/yukawa-color-projection-narrow-repair`

PR: https://github.com/jonathonreilly/cl3-lattice-framework/pull/1764
