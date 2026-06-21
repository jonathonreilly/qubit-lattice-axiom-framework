## Summary

Deletes the 8 verified orphan runner-cache files left after the block130 and
block131 cleanup safety guards.

The deletion set was produced by:

```bash
python3 scripts/precompute_audit_runners.py --cleanup-orphans --all --check-only --allow-non-main
```

After cleanup, the guarded dry run reports:

- `Would delete 0 orphan cache file(s)`
- `fresh: 3123`
- `stale to refresh: 0`
- `missing on disk: 0`

## Boundary

This PR does not audit claims, apply verdicts, edit ledger rows, or assert
retained/proposed-retained status. It only removes unreferenced cache files for
missing runners after the cleanup safety guards.

## Deleted Files

- `logs/runner-cache/cl3_exact_tier_ewitness_2026_05_07_ewitness_pathB3.txt`
- `logs/runner-cache/cl3_exact_tier_ewitness_2026_05_07_ewitness_isotropic.txt`
- `logs/runner-cache/cl3_exact_tier_ewitness_2026_05_07_ewitness_pathB6.txt`
- `logs/runner-cache/cl3_c_iso_su3_nlo_2026_05_08_pathB_xi8_4cubed.txt`
- `logs/runner-cache/cl3_exact_tier_ewitness_2026_05_07_ewitness_pathC.txt`
- `logs/runner-cache/frontier_koide_dimensionless_objection_closure_review_2026_06_07.txt`
- `logs/runner-cache/cl3_exact_tier_ewitness_2026_05_07_ewitness_pathA.txt`
- `logs/runner-cache/cl3_c_iso_su3_nlo_2026_05_08_pathB_xi16_4cubed.txt`

## Verification

- `python3 scripts/precompute_audit_runners.py --cleanup-orphans-dry-run --all --check-only --allow-non-main` before cleanup -> 8 candidates
- `python3 scripts/precompute_audit_runners.py --cleanup-orphans --all --check-only --allow-non-main` -> deleted 8 candidates, `fresh: 3123`, `stale to refresh: 0`, `missing on disk: 0`
- `python3 scripts/precompute_audit_runners.py --cleanup-orphans-dry-run --all --check-only --allow-non-main` after cleanup -> 0 candidates, `fresh: 3123`, `stale to refresh: 0`, `missing on disk: 0`
- `python3 -m unittest docs.audit.scripts.tests.test_audit_pipeline` -> 79 tests passed
- `python3 docs/audit/scripts/audit_lint.py --strict` -> `OK: no errors` with notices only
- `python3 -m py_compile scripts/precompute_audit_runners.py docs/audit/scripts/tests/test_audit_pipeline.py` -> OK
- `git diff --check` -> OK
