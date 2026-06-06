# Handoff

## Summary

This stacked block defines the supplied-orientation bridge interface:

```text
SUPPLIED_ORIENTATION_BRIDGE_INTERFACE=TRUE
DIRECTED_CERTIFICATE_REQUIRES_SUPPLIED_ORIENTATION=TRUE
ORIENTATION_DERIVED_FROM_RECORD=FALSE
PHYSICAL_ARROW_DERIVED_FROM_RECORD=FALSE
PRODUCTION_KERNEL_SELECTED=FALSE
```

## Meaning

The no-go remains: counts alone do not orient the arrow. The positive interface
is that directed post-record certificates become exact once the row supplies
law, orientation, clock/order, and any dynamics bridge id it wants to use.

## Stacking

This PR should target:

```text
physics-loop/post-record-arrow-orientation-firewall-20260606
```

because it is the positive counterpart to PR #2838.

## Files

- `docs/POST_RECORD_SUPPLIED_ORIENTATION_BRIDGE_INTERFACE_2026-06-06.md`
- `scripts/frontier_post_record_supplied_orientation_bridge_interface_2026_06_06.py`
- `logs/runner-cache/frontier_post_record_supplied_orientation_bridge_interface_2026_06_06.txt`
- `.claude/science/physics-loops/post-record-supplied-orientation-bridge-interface-20260606/`

## Next exact action

Closed for campaign purposes. Pivot to the production-dynamics needed row map.

## PR

```yaml
pr_url: "https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/2839"
base: "physics-loop/post-record-arrow-orientation-firewall-20260606"
initial_mergeable: MERGEABLE
initial_merge_state_status: UNSTABLE
initial_checks: "audit_pipeline queued at first verification"
final_mergeable: MERGEABLE
final_merge_state_status: CLEAN
final_checks: "audit_pipeline completed SUCCESS at final verification"
```
