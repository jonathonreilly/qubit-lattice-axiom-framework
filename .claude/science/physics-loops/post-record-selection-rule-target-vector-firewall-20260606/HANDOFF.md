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

Commit and push this PR-status checkpoint, then poll PR #2858 until the latest
head is clean/success. After the final PR status is recorded, continue the
campaign while runtime remains.

## PR

```yaml
pr_url: "https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/2858"
base: "physics-loop/post-record-supplied-kernel-selection-rule-interface-20260606"
initial_mergeable: MERGEABLE
initial_merge_state_status: UNSTABLE
initial_checks: "audit_pipeline in progress at initial verification"
final_mergeable: null
final_merge_state_status: null
final_checks: null
```
