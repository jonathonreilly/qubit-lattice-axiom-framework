# Handoff

## Summary

This stacked block defines admitted-sample target-vector semantics:

```text
ADMITTED_SAMPLE_TARGET_VECTOR_INTERFACE=TRUE
ADMITTED_SAMPLE_EMPIRICAL_VECTOR_EXACT=TRUE
SAMPLE_IS_PROBABILITY_LAW=FALSE
WEIGHTS_DERIVED_FROM_SAMPLE=FALSE
SELECTION_RULE_DERIVED_FROM_SAMPLE=FALSE
PRODUCTION_KERNEL_SELECTED_BY_SAMPLE_ALONE=FALSE
```

## Meaning

Realized post-record samples can provide exact empirical vectors when admitted
as observation data. They do not become probability laws and do not select
weights, rules, or kernels.

## Stacking

This PR should target:

```text
physics-loop/post-record-selection-rule-target-vector-firewall-20260606
```

because it is the positive admitted-sample companion to PR #2858.

## Files

- `docs/POST_RECORD_ADMITTED_SAMPLE_TARGET_VECTOR_INTERFACE_2026-06-06.md`
- `scripts/frontier_post_record_admitted_sample_target_vector_interface_2026_06_06.py`
- `logs/runner-cache/frontier_post_record_admitted_sample_target_vector_interface_2026_06_06.txt`
- `.claude/science/physics-loops/post-record-admitted-sample-target-vector-interface-20260606/`

## Next exact action

Commit, push, open the stacked PR, record PR status, then continue or close the
campaign based on remaining runtime.

## PR

```yaml
pr_url: null
base: "physics-loop/post-record-selection-rule-target-vector-firewall-20260606"
initial_mergeable: null
initial_merge_state_status: null
initial_checks: null
final_mergeable: null
final_merge_state_status: null
final_checks: null
```
