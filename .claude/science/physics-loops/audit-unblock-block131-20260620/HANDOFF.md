# Handoff

## Summary

Block131 fixes another orphan runner-cache cleanup safety issue.

After block130, cleanup dry run reported 9 candidates. One was still unsafe to
delete because it is linked by a live note:

- cache: `logs/runner-cache/chsh_structural_bound_narrow_2026_05_17.txt`
- note: `docs/CHSH_STRUCTURAL_BOUND_NARROW_THEOREM_NOTE_2026-05-17.md`

This PR makes cleanup scan repository text references outside
`logs/runner-cache/` and preserve matching cache files. After the fix, the
full-ledger cleanup dry run reports 8 candidates instead of 9:

- `fresh: 3120`
- `stale to refresh: 0`
- `missing on disk: 0`

## Boundary

This is a methodology/tooling safety PR. It does not audit any claim, apply a
verdict, delete cache files, or assert retained status.

## Verification

- `python3 -m unittest docs.audit.scripts.tests.test_audit_pipeline.PrecomputeAuditRunnersTest` -> OK, 2 tests.
- `python3 scripts/precompute_audit_runners.py --cleanup-orphans-dry-run --all --check-only --allow-non-main` -> OK, 8 candidates.
- `python3 -m py_compile scripts/precompute_audit_runners.py docs/audit/scripts/tests/test_audit_pipeline.py` -> OK.
- `python3 -m unittest docs.audit.scripts.tests.test_audit_pipeline` -> 79 tests passed.
- `python3 docs/audit/scripts/audit_lint.py --strict` -> OK, notices only.
- `git diff --check` -> OK.

## Next Exact Action

Commit, push, and open a stacked PR against
`physics-loop/audit-unblock-block130-20260620`.
