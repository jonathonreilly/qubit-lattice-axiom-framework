# Handoff

## Summary

This stacked block proves the target/weight firewall:

```text
SELECTION_RULE_TARGET_VECTOR_FIREWALL=TRUE
SAME_TARGET_DIFFERENT_WEIGHTS_SELECT_DIFFERENT_KERNELS=TRUE
TARGET_VECTOR_DERIVED_FROM_RECORD=FALSE
SELECTION_WEIGHTS_DERIVED_FROM_RECORD=FALSE
PRODUCTION_KERNEL_SELECTED_WITHOUT_RULE=FALSE
```

## Meaning

The supplied selection-rule interface needs supplied target vectors and weights.
Different supplied weights can select different kernels from the same candidate
family and target vector.

## Stacking

This PR should target:

```text
physics-loop/post-record-supplied-kernel-selection-rule-interface-20260606
```

because it is the firewall companion to PR #2856.

## Files

- `docs/POST_RECORD_SELECTION_RULE_TARGET_VECTOR_FIREWALL_2026-06-06.md`
- `scripts/frontier_post_record_selection_rule_target_vector_firewall_2026_06_06.py`
- `logs/runner-cache/frontier_post_record_selection_rule_target_vector_firewall_2026_06_06.txt`
- `.claude/science/physics-loops/post-record-selection-rule-target-vector-firewall-20260606/`

## Next exact action

Commit, push, open the stacked PR, record PR status, then continue the campaign
while runtime remains.

## PR

```yaml
pr_url: null
base: "physics-loop/post-record-supplied-kernel-selection-rule-interface-20260606"
initial_mergeable: null
initial_merge_state_status: null
initial_checks: null
final_mergeable: null
final_merge_state_status: null
final_checks: null
```
