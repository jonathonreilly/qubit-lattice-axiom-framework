# Handoff

## What Changed

- R4-2 now computes `C3` central projector ranks `(1,2)` and checks per-DOF versus equal-block readings.
- R4-3 now checks that the same two central idempotents admit multiple positive `C3`-invariant metric ratios, so K0 block count does not fix energy weights.
- Runner verdict text is narrowed to round-4 executable support.
- The note records that rounds 1-3 still need one-hop authority coverage.

## Checks

- `PYTHONPATH=scripts python3 scripts/flavor_find_J_round4_consolidation_kappa_is_input_2026_06_02.py`
- `python3 scripts/cached_runner_output.py --refresh scripts/flavor_find_J_round4_consolidation_kappa_is_input_2026_06_02.py`
- `python3 scripts/cached_runner_output.py --check-only scripts/flavor_find_J_round4_consolidation_kappa_is_input_2026_06_02.py`
- `python3 -m py_compile scripts/flavor_find_J_round4_consolidation_kappa_is_input_2026_06_02.py`
- `git diff --check`

## Remaining Blocker

Rounds 1-3 need separate authority repair before the full four-round consolidation can request a clean audit.
