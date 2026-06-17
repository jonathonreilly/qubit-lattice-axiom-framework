# Handoff

Branch: `codex/audit-runner-breakage-staleness-20260617`

What changed:

- Added a deterministic guard for the `timeout` and `nonzero_exit` portions of
  `docs/audit/data/runner_breakage_inventory.json`.
- The guard reads current SHA-pinned caches and fails if any runtime-failure
  inventory entry is not cache-fresh with `status=ok` and `exit_code=0`.
- The audit data itself is not edited.

Expected audit effect:

- The 39 runtime-failure entries in the current inventory should no longer be
  treated as live compute blockers without re-checking the fresh cache evidence.
- Missing-runner path entries remain out of scope here and are handled by the
  separate path-canonicalization PR.

Next exact action:

- Reviewer/auditor can inspect
  `logs/runner-cache/audit_runner_runtime_breakage_staleness_guard_2026_06_17.txt`
  or rerun `python3 scripts/audit_runner_runtime_breakage_staleness_guard_2026_06_17.py`.
