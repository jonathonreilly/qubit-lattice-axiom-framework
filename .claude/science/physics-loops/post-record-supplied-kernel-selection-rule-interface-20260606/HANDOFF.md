# Handoff

## Summary

This stacked block defines the positive supplied-rule interface:

```text
SUPPLIED_KERNEL_SELECTION_RULE_INTERFACE=TRUE
SUPPLIED_RULE_UNIQUE_MINIMUM=TRUE
WEAK_RULE_UNDERSELECTS_KERNEL=TRUE
SELECTION_RULE_DERIVED_FROM_RECORD=FALSE
CANDIDATE_FAMILY_DERIVED_FROM_RECORD=FALSE
PRODUCTION_KERNEL_SELECTED_WITHOUT_RULE=FALSE
```

## Meaning

Kernel selection is allowed only inside a supplied finite candidate family and
supplied selection rule. A weak rule underselects. Record does not derive the
rule or candidate family.

## Stacking

This PR should target:

```text
physics-loop/post-record-directed-certificate-kernel-selection-firewall-20260606
```

because it is the positive supplied-rule companion to PR #2853.

## Files

- `docs/POST_RECORD_SUPPLIED_KERNEL_SELECTION_RULE_INTERFACE_2026-06-06.md`
- `scripts/frontier_post_record_supplied_kernel_selection_rule_interface_2026_06_06.py`
- `logs/runner-cache/frontier_post_record_supplied_kernel_selection_rule_interface_2026_06_06.txt`
- `.claude/science/physics-loops/post-record-supplied-kernel-selection-rule-interface-20260606/`

## Next exact action

Commit and push this PR-status checkpoint, then poll PR #2856 until the latest
head is clean/success. After the final PR status is recorded, continue the
campaign while runtime remains.

## PR

```yaml
pr_url: "https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/2856"
base: "physics-loop/post-record-directed-certificate-kernel-selection-firewall-20260606"
initial_mergeable: MERGEABLE
initial_merge_state_status: UNSTABLE
initial_checks: "audit_pipeline in progress at initial verification"
final_mergeable: null
final_merge_state_status: null
final_checks: null
```
