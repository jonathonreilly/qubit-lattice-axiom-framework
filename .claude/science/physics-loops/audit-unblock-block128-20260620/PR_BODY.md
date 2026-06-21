## Summary

Refreshes the 11 stale/corrupt full-ledger runner-cache transcripts currently
present on `origin/main` at `81a3eea94`.

Before refresh:

- `python3 scripts/precompute_audit_runners.py --all --check-only --allow-non-main`
  reported `fresh: 3039`, `stale to refresh: 11`, `missing on disk: 0`.

After refresh:

- the same check reports `fresh: 3050`, `stale to refresh: 0`,
  `missing on disk: 0`.

No audit worker was run and no verdict was hand-applied.

## Boundary

This PR is source-side audit infrastructure hygiene only. It does not audit
claims, apply verdicts, edit lane registries, or assert retained/proposed-retained
status.

## Artifacts

- 11 refreshed files under `logs/runner-cache/`
- `.claude/science/physics-loops/audit-unblock-block128-20260620/HANDOFF.md`
- `.claude/science/physics-loops/audit-unblock-block128-20260620/TRACE_GATE.md`
- `.claude/science/physics-loops/audit-unblock-block128-20260620/CLAIM_STATUS_CERTIFICATE.md`
- `.claude/science/physics-loops/audit-unblock-block128-20260620/REVIEW_HISTORY.md`

## Verification

- `python3 scripts/precompute_audit_runners.py --runners <11 paths> --force --push-mode none --allow-non-main` -> 11 OK
- `python3 scripts/precompute_audit_runners.py --all --check-only --allow-non-main` -> `fresh: 3050`, `stale to refresh: 0`, `missing on disk: 0`
- `python3 -m py_compile scripts/precompute_audit_runners.py scripts/runner_cache.py` -> OK
- `python3 -m unittest docs.audit.scripts.tests.test_audit_pipeline` -> 77 tests passed
- `git diff --check` -> OK
