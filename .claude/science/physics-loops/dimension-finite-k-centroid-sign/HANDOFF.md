# Handoff

## Result

Added a finite-k centroid-sign bridge for the dimension-selection lower-bound
runner.

## Review Surface

- `docs/DIMENSION_SELECTION_FINITE_K_CENTROID_SIGN_BRIDGE_NOTE_2026-05-25.md`
- `scripts/frontier_dimension_selection_finite_k_centroid_sign_bridge.py`
- `outputs/dimension_selection_finite_k_centroid_sign_bridge_2026-05-25.json`

## Verification

- `python3 scripts/frontier_dimension_selection_finite_k_centroid_sign_bridge.py`
- `python3 scripts/frontier_dimension_selection.py`
- `python3 -m py_compile scripts/frontier_dimension_selection_finite_k_centroid_sign_bridge.py scripts/frontier_dimension_selection.py`
- `git diff --check`

## Remaining Blockers

- all-d potential/Coulomb law authority;
- upper-bound Bertrand/Coulomb conditional dependencies;
- possible interval proof over finite `M` if audit requires more than
  derivative plus direct finite-M replay.
