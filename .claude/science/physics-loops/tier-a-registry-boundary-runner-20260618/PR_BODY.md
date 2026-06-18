## Summary

Adds a source/machine-registry boundary runner and cache for `admitted_input_registry_tier_a_note_2026-05-23`, which is a high-load meta row with no runner path on current `main`.

## What changed

- Adds `scripts/admitted_input_registry_tier_a_boundary_check.py`.
- Adds `logs/runner-cache/admitted_input_registry_tier_a_boundary_check.txt`.
- Adds primary runner/cache pointers to `docs/ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23.md`.
- Adds branch-local physics-loop handoff/certificate files.

## Boundary

This PR does not audit the row, retag the ledger, change effective status, add/remove/regrade any admission, or promote Tier-A dependents to unbounded retained.

## Verification

- `python3 scripts/admitted_input_registry_tier_a_boundary_check.py`
- `python3 scripts/cached_runner_output.py --refresh scripts/admitted_input_registry_tier_a_boundary_check.py`
- `python3 -m py_compile scripts/admitted_input_registry_tier_a_boundary_check.py`
- `git diff --check`
- forbidden-path guard for audit/publication/status surfaces
