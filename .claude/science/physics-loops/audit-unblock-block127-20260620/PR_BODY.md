## Summary

Refreshes the canonical runner cache for `scripts/frontier_frozen_stars_rigorous.py`.

On `origin/main`, the cache recorded `status: ok` but did not preserve useful stdout. This PR
recomputes the cache through `scripts/precompute_audit_runners.py` and records the full transcript
under the runner's declared `1800` second timeout.

After rebasing onto current `main` at `678b38ce7`, the branch is intentionally
narrowed to the runner transcript plus branch-local loop metadata. Broader
audit-support regeneration and packet-helper fixes are handled in later PRs.

## Boundary

This PR does not audit the claim, apply a verdict, or assert retained/proposed-retained status.
It does not hand-edit audit ledgers, queues, publication matrices, lane registries, active review
queues, or repo-wide status boards.

The target row remains unaudited and not ready because these dependencies remain unresolved:

- `gw_echo_null_result_note`
- `work_history.gw_echo_timing_route_note`

This is a leaf-scope evidence unblock; it does not move a load-bearing retained chain.

## Artifacts

- `logs/runner-cache/frontier_frozen_stars_rigorous.txt`
- `.claude/science/physics-loops/audit-unblock-block127-20260620/HANDOFF.md`
- `.claude/science/physics-loops/audit-unblock-block127-20260620/TRACE_GATE.md`
- `.claude/science/physics-loops/audit-unblock-block127-20260620/CLAIM_STATUS_CERTIFICATE.md`
- `.claude/science/physics-loops/audit-unblock-block127-20260620/REVIEW_HISTORY.md`

## Verification

- `python3 scripts/precompute_audit_runners.py --runners scripts/frontier_frozen_stars_rigorous.py --force --push-mode none --allow-non-main` -> `OK`, elapsed `387.4s`
- `python3 scripts/precompute_audit_runners.py --runners scripts/frontier_frozen_stars_rigorous.py --check-only --push-mode none --allow-non-main` -> `fresh: 1`, all relevant caches fresh
- `python3 scripts/precompute_audit_runners.py --pr-diff origin/main --check-only --allow-non-main` -> `fresh: 0`, `stale to refresh: 0`, `missing on disk: 0`
- `python3 -m py_compile scripts/frontier_frozen_stars_rigorous.py scripts/precompute_audit_runners.py scripts/runner_cache.py` -> OK
- `git diff --check` -> OK
