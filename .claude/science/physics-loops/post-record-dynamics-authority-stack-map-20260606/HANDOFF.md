# Handoff

## Summary

This stacked block maps the current dynamics authority stack:

```text
POST_RECORD_DYNAMICS_AUTHORITY_STACK_MAP=TRUE
DYNAMICS_AUTHORITY_LAYERS=5
PRODUCTION_KERNEL_SELECTED_WITHOUT_RULE=FALSE
SELECTION_RULE_DERIVED_FROM_RECORD=FALSE
TARGET_VECTOR_DERIVED_FROM_RECORD=FALSE
SAMPLE_IS_PROBABILITY_LAW=FALSE
```

## Meaning

The stack now separates supplied, admitted, blocked, exact-support, and no-go
classes for dynamics work. It is a handoff map, not an audit verdict.

## Stacking

This PR should target:

```text
physics-loop/post-record-admitted-sample-target-vector-interface-20260606
```

because it summarizes the stack through PR #2861.

## Files

- `docs/POST_RECORD_DYNAMICS_AUTHORITY_STACK_MAP_2026-06-06.md`
- `scripts/frontier_post_record_dynamics_authority_stack_map_2026_06_06.py`
- `logs/runner-cache/frontier_post_record_dynamics_authority_stack_map_2026_06_06.txt`
- `.claude/science/physics-loops/post-record-dynamics-authority-stack-map-20260606/`

## Next exact action

Commit and push this PR-status checkpoint, then poll PR #2864 until the latest
head is clean/success. After final PR status is recorded, close out the
campaign if runtime is exhausted.

## PR

```yaml
pr_url: "https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/2864"
base: "physics-loop/post-record-admitted-sample-target-vector-interface-20260606"
initial_mergeable: MERGEABLE
initial_merge_state_status: UNSTABLE
initial_checks: "audit_pipeline in progress at initial verification"
final_mergeable: null
final_merge_state_status: null
final_checks: null
```
