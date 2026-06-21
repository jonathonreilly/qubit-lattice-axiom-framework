## Summary

Refreshes the 10 stale/corrupt full-ledger runner-cache transcripts currently
present on `origin/main` at `7fc79bd4`.

Before refresh:

- `python3 scripts/precompute_audit_runners.py --all --check-only --allow-non-main`
  reported `fresh: 3040`, `stale to refresh: 10`, `missing on disk: 0`.

After refresh:

- the same check reports `fresh: 3050`, `stale to refresh: 0`,
  `missing on disk: 0`.

No audit worker was run and no verdict was hand-applied.

## Boundary

This PR is source-side audit infrastructure hygiene only. It does not audit
claims, apply verdicts, edit lane registries, or assert retained/proposed-retained
status.

## Artifacts

- 10 refreshed files under `logs/runner-cache/`
- `.claude/science/physics-loops/audit-unblock-block128-20260620/HANDOFF.md`
- `.claude/science/physics-loops/audit-unblock-block128-20260620/TRACE_GATE.md`
- `.claude/science/physics-loops/audit-unblock-block128-20260620/CLAIM_STATUS_CERTIFICATE.md`
- `.claude/science/physics-loops/audit-unblock-block128-20260620/REVIEW_HISTORY.md`

## Verification

- `python3 scripts/precompute_audit_runners.py --runners <10 paths> --force --push-mode none --allow-non-main` -> 10 OK
- `python3 scripts/precompute_audit_runners.py --all --check-only --allow-non-main` -> `fresh: 3050`, `stale to refresh: 0`, `missing on disk: 0`
- `python3 -m py_compile scripts/precompute_audit_runners.py scripts/runner_cache.py` -> OK
- `python3 -m unittest docs.audit.scripts.tests.test_audit_pipeline` -> 77 tests passed
- `git diff --check` -> OK

After rebasing onto `7fc79bd4`, the same full-ledger cache check still reports
`fresh: 3050`, `stale to refresh: 0`, `missing on disk: 0` on this branch. A
detached `origin/main` check at `7fc79bd4` reports 10 stale/corrupt runner
caches before this PR; `frontier_alpha_s_universal_beta_kernel_2026_06_18.py`
is already fresh on current main and is no longer part of this PR scope.
