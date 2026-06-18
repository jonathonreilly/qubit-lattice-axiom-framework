## Summary

Adds a source-boundary runner/cache for `scale_reference_primitive`, which is a high-load meta primitive row with no runner path on current `main`.

## What changed

- Adds `scripts/scale_reference_primitive_boundary_check.py`.
- Adds `logs/runner-cache/scale_reference_primitive_boundary_check.txt`.
- Adds primary runner/cache pointers to `docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md`.
- Adds a branch-local physics-loop handoff/certificate under `.claude/science/physics-loops/scale-reference-primitive-runner-20260618/`.

## Boundary

This PR does not audit the row, retag the ledger, change effective status, add an axiom, derive `a/l_P = 1`, or supply any dimensionless physics. It only packages the existing owner-approved primitive boundary for re-audit.

## Verification

- `python3 scripts/scale_reference_primitive_boundary_check.py`
- `python3 scripts/cached_runner_output.py --refresh scripts/scale_reference_primitive_boundary_check.py`
- `python3 -m py_compile scripts/scale_reference_primitive_boundary_check.py`
- `python3 docs/audit/scripts/check_axiom_premise_clean.py`
- `git diff --check`
- forbidden-path guard for audit/publication/status surfaces
