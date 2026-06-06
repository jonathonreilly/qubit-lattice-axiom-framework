# Handoff

## Summary

This stacked block proves the kernel-selection firewall:

```text
DIRECTED_CERTIFICATE_KERNEL_SELECTION_FIREWALL=TRUE
SAME_DIRECTED_CERTIFICATE_DISTINCT_KERNELS=TRUE
PRODUCTION_KERNEL_SELECTED=FALSE
PRODUCTION_KERNEL_DERIVED_FROM_DIRECTED_CERTIFICATE=FALSE
ORIENTATION_DERIVED_FROM_RECORD=FALSE
PHYSICAL_ARROW_DERIVED_FROM_RECORD=FALSE
```

## Meaning

Directed certificates can audit supplied dynamics bridges. They do not select
the production kernel. The kernel or selection rule remains a separate supplied
input.

## Stacking

This PR should target:

```text
physics-loop/post-record-directed-certificate-examples-20260606
```

because it is the firewall companion to PR #2850.

## Files

- `docs/POST_RECORD_DIRECTED_CERTIFICATE_KERNEL_SELECTION_FIREWALL_2026-06-06.md`
- `scripts/frontier_post_record_directed_certificate_kernel_selection_firewall_2026_06_06.py`
- `logs/runner-cache/frontier_post_record_directed_certificate_kernel_selection_firewall_2026_06_06.txt`
- `.claude/science/physics-loops/post-record-directed-certificate-kernel-selection-firewall-20260606/`

## Next exact action

Commit, push, open the stacked PR, record PR status, then continue the campaign
while runtime remains.

## PR

```yaml
pr_url: null
base: "physics-loop/post-record-directed-certificate-examples-20260606"
initial_mergeable: null
initial_merge_state_status: null
initial_checks: null
final_mergeable: null
final_merge_state_status: null
final_checks: null
```
