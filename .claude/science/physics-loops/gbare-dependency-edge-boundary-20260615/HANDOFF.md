# Handoff

## Summary

This branch is a clean focused replacement for the g_bare part of the older
dirty conditional-cleanup PRs. It repairs the two dependency rows that gate
`g_bare_derivation_note` by making the missing Wilson inputs explicit scoped
premises rather than hidden retained dependencies.

## Verification

```bash
python3 scripts/frontier_g_bare_rescaling_conditional_algebra_check.py
python3 scripts/frontier_g_bare_constraint_surface_check.py
python3 scripts/precompute_audit_runners.py --runners scripts/frontier_g_bare_rescaling_conditional_algebra_check.py,scripts/frontier_g_bare_constraint_surface_check.py --check-only
```

Expected summaries:

- rescaling runner: `SUMMARY: PASS = 15, FAIL = 0`
- constraint runner: `SUMMARY: PASS = 12, FAIL = 0`

## Audit Boundary

No audit verdicts, generated audit data, publication effective-status files, or
repo front-door status files are edited. Independent audit remains required.
