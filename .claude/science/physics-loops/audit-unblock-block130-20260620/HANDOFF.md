# Handoff

## Summary

Block130 fixes an orphan runner-cache cleanup false-positive class.

Before this fix, `cleanup_orphans()` treated a cache as safe to delete when:

1. its stem was not in the known ledger runner set, and
2. `scripts/<stem>.py` did not exist.

That missed valid nested runner paths recorded in cache headers. The observed
false positives were:

- `logs/runner-cache/yt_p1_delta_r_corrected_bound_memsafe.txt`
- `logs/runner-cache/yt_p1_fermion_regulator_verification_memsafe.txt`

Both headers name existing runners under `scripts/corrections/`.

After the fix, full-ledger cleanup dry run reports 9 candidates instead of 11,
and the full-ledger runner cache check remains clean:

- `fresh: 3123`
- `stale to refresh: 0`
- `missing on disk: 0`

## Boundary

This is a methodology/tooling safety PR. It does not audit any claim, apply a
verdict, delete cache files, or assert retained status.

## Verification

- `python3 -m unittest docs.audit.scripts.tests.test_audit_pipeline.PrecomputeAuditRunnersTest` -> OK.
- `python3 scripts/precompute_audit_runners.py --cleanup-orphans-dry-run --all --check-only --allow-non-main` -> OK, 9 candidates.
- `python3 -m py_compile scripts/precompute_audit_runners.py scripts/runner_cache.py docs/audit/scripts/tests/test_audit_pipeline.py` -> OK.
- `python3 -m unittest docs.audit.scripts.tests.test_audit_pipeline` -> 78 tests passed.
- `python3 docs/audit/scripts/audit_lint.py --strict` -> OK, notices only.
- `git diff --check` -> OK.

## Next Exact Action

Monitor PR #4500 audit-lane check, then continue to the next audit-unblock
target.

## PR

- https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/4500
