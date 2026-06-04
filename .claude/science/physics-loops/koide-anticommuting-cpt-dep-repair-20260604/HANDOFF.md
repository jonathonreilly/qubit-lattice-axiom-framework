# Handoff

## What Changed

- Removed `CPT_EXACT_REAL_ANTI_HERMITIAN_D_NARROW_THEOREM_NOTE_2026-05-10.md`
  from the load-bearing authority list.
- Added a dated repair note explaining that CPT is not used by this finite
  reconciliation.

## Why It Matters

The row was blocked because it named a CPT authority with a separate spectral
sign issue as load-bearing. The reconciliation itself only compares two Koide
readout routes and the runner checks those directly. Removing the unused
authority closes the dependency-surface defect without touching the separate
CPT packet.

## Verification

- `PYTHONPATH=scripts python3 scripts/frontier_koide_anticommuting_eigenvector_vs_eigenvalue_readout_reconciliation.py`
- `python3 scripts/cached_runner_output.py --check-only scripts/frontier_koide_anticommuting_eigenvector_vs_eigenvalue_readout_reconciliation.py`
- `python3 -m py_compile scripts/frontier_koide_anticommuting_eigenvector_vs_eigenvalue_readout_reconciliation.py`
- `git diff --check`

## Remaining Blocker

- Physical readout-class selection remains open.

## Next Action

Open the review PR, then continue to sibling CPT-dependency rows if useful.
