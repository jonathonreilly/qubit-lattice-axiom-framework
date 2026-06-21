## Summary

Refreshes the canonical runner cache for
`scripts/frontier_dm_neutrino_source_surface_perturbative_uniqueness_theorem.py`.

On `origin/main`, the cache recorded `status: ok` but did not preserve useful stdout. This PR
recomputes the cache through `scripts/precompute_audit_runners.py` and records the full transcript:
`PASS = 46`, `FAIL = 0`, under the runner's declared `1800` second timeout.

After rebasing onto current `main` at `678b38ce7`, the branch is intentionally
narrowed to the runner transcript plus branch-local loop metadata. Broader
audit-support regeneration is handled in later PRs.

## Boundary

This PR does not audit the claim, apply a verdict, or assert retained/proposed-retained status.
It does not hand-edit audit ledgers, queues, publication matrices, lane registries, active review
queues, or repo-wide status boards.

The target row remains unaudited and not ready because these dependencies remain unresolved:

- `neutrino_dirac_z3_support_trichotomy_note`
- `dm_neutrino_dirac_bridge_theorem_note_2026-04-15`

## Artifacts

- `logs/runner-cache/frontier_dm_neutrino_source_surface_perturbative_uniqueness_theorem.txt`
- `.claude/science/physics-loops/audit-unblock-block126-20260620/HANDOFF.md`
- `.claude/science/physics-loops/audit-unblock-block126-20260620/TRACE_GATE.md`
- `.claude/science/physics-loops/audit-unblock-block126-20260620/CLAIM_STATUS_CERTIFICATE.md`
- `.claude/science/physics-loops/audit-unblock-block126-20260620/REVIEW_HISTORY.md`

## Verification

- `python3 scripts/precompute_audit_runners.py --runners scripts/frontier_dm_neutrino_source_surface_perturbative_uniqueness_theorem.py --check-only --push-mode none --allow-non-main` -> `fresh: 1`, all relevant caches fresh
- `python3 scripts/precompute_audit_runners.py --pr-diff origin/main --check-only --allow-non-main` -> `fresh: 0`, `stale to refresh: 0`, `missing on disk: 0`
- `python3 -m py_compile scripts/precompute_audit_runners.py scripts/runner_cache.py scripts/frontier_dm_neutrino_source_surface_perturbative_uniqueness_theorem.py` -> OK
- `git diff --check` -> OK
