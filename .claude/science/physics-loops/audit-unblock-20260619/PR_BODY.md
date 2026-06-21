# PR Body

## Summary

This PR unblocks the ready audit row for
`one_parameter_reduced_shell_law_helpers_umbrella_note_2026-04-13`.

On current `origin/main`, direct execution of
`scripts/frontier_one_parameter_reduced_shell_law.py` failed its
source-boundary firewall: the auto-generated `docs/repo/FRONT_DOOR_STATUS.md`
queue snapshot listed the ready row without the helper-wrapper qualifier, so
the runner reported `PASS=16 FAIL=1` even though the committed runner cache was
stale at `PASS=17 FAIL=0`.

The fix keeps the claim boundary narrow:

- `docs/ONE_PARAMETER_REDUCED_SHELL_LAW_HELPERS_UMBRELLA_NOTE_2026-04-13.md`
  now states that generated queue snapshots are not source-claim citations for
  this firewall.
- `scripts/frontier_one_parameter_reduced_shell_law.py` skips
  `docs/repo/FRONT_DOOR_STATUS.md`, matching the existing skip for generated
  audit/publication surfaces.
- The target runner cache was refreshed and now records
  `PASS=17 FAIL=0 TOTAL=17`.

After rebasing onto current `main` at `678b38ce7`, the branch is intentionally
narrowed to the source firewall repair, the refreshed target runner cache, and
the branch-local loop packet. Generated audit, publication, and front-door
surfaces are excluded from this PR.

## Boundary

- No audit-loop run.
- No audit verdicts applied.
- No effective-status promotion.
- This is a source-side runner/firewall repair for an already-ready unaudited
  bounded row.

## Current queue snapshot

- claim_type: `bounded_theorem`
- audit_status: `unaudited`
- effective_status: `unaudited`
- criticality: `critical`
- load_bearing_score: `10.353`
- direct_in_degree: `2`
- transitive_descendants: `653`
- deps: `coarse_grained_exterior_law_helper_note_2026-04-14`, `lattice_laplacian_shell_localization_identity_bounded_theorem_note_2026-06-16`
- helper_runner_paths: `6`
- ready: `true`

## Verification

- `python3 -m py_compile scripts/frontier_one_parameter_reduced_shell_law.py`
- Direct runner before patch: `PASS=16 FAIL=1`
- `python3 scripts/frontier_one_parameter_reduced_shell_law.py` -> `PASS=17 FAIL=0 TOTAL=17`
- `python3 scripts/precompute_audit_runners.py --runners scripts/frontier_one_parameter_reduced_shell_law.py --check-only --push-mode none --allow-non-main` -> `fresh: 1`, `stale to refresh: 0`, `missing on disk: 0`
- `python3 scripts/precompute_audit_runners.py --pr-diff origin/main --check-only --allow-non-main` -> `fresh: 1`, `stale to refresh: 0`, `missing on disk: 0`
- `python3 -m py_compile scripts/frontier_one_parameter_reduced_shell_law.py scripts/precompute_audit_runners.py scripts/runner_cache.py` -> OK
- `git diff --check` -> OK
