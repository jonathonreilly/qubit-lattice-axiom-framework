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

- `fresh: 3050`
- `stale to refresh: 0`
- `missing on disk: 0`

The branch is restacked on PR #4500 at `eab9c843d`.

## Boundary

This is a methodology/tooling safety PR. It does not audit any claim, apply a
verdict, delete cache files, or assert retained status.

## Verification

- `python3 -m unittest docs.audit.scripts.tests.test_audit_pipeline.PrecomputeAuditRunnersTest` -> OK, 2 tests.
- `python3 scripts/precompute_audit_runners.py --cleanup-orphans-dry-run --all --check-only --allow-non-main` -> OK, 8 candidates.
- `python3 -m py_compile scripts/precompute_audit_runners.py scripts/runner_cache.py docs/audit/scripts/tests/test_audit_pipeline.py` -> OK.
- `python3 -m unittest docs.audit.scripts.tests.test_audit_pipeline` -> 79 tests passed.
- `git diff --check` -> OK.

## Next Exact Action

Run targeted verification, force-push the restacked branch, update PR #4501
body, then continue to the next stacked cleanup PR.

## PR

- https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/4501
