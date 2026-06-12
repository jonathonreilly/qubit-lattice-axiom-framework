# Record Period Sample-Scope Repair Handoff

## Target

`record_conditional_law_period_scaling_l3_to_l4_bounded_theorem_note_2026-06-11`

Prior audit blocker:

```text
scope_too_broad: either narrow the null-cleared/no-MC language to the fixed 300-permutation deterministic sample or add an exact/certified permutation-null p95 computation, then re-audit.
```

## Repair Summary

The note now states that the permutation-null statistic is a fixed, seeded,
300-permutation sampled-null p95. It explicitly does not claim an exhaustive
permutation-null p95, a certified finite-sample upper confidence bound, or an
MC-free null theorem.

The runner stdout labels now use sampled-null language, and the runner adds
two source-note checks confirming that the note declares the sampled-null
boundary.

## Verification

```text
python3 -m py_compile scripts/frontier_record_conditional_law_period_scaling_2026_06_11.py
python3 scripts/frontier_record_conditional_law_period_scaling_2026_06_11.py
python3 scripts/precompute_audit_runners.py --runners scripts/frontier_record_conditional_law_period_scaling_2026_06_11.py --force --concurrency 1 --push-mode none --allow-non-main
python3 scripts/cached_runner_output.py scripts/frontier_record_conditional_law_period_scaling_2026_06_11.py
git diff --check
git diff --name-only -- docs/audit/data
```

No audit-ledger files should be changed by this PR.
