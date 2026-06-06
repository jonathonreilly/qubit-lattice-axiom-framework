# Handoff

## Summary

This stacked block instantiates the supplied-orientation bridge with three
finite directed examples:

```text
SUPPLIED_DIRECTED_CERTIFICATE_EXAMPLES=TRUE
ARROW_OR_DYNAMICS_BRIDGE_ROWS=28
PRE_RECORD_LAW_CARRIES_PROBABILITY=TRUE
POST_RECORD_SITE_CARRIES_REALIZED_INFORMATION=TRUE
DIRECTED_STATISTICS_REQUIRE_SUPPLIED_ORIENTATION=TRUE
ORIENTATION_DERIVED_FROM_RECORD=FALSE
PHYSICAL_ARROW_DERIVED_FROM_RECORD=FALSE
PRODUCTION_KERNEL_SELECTED=FALSE
```

## Meaning

The result says the dynamics lane can use supplied directed statistics after a
law, orientation, clock, and kernel bridge are named. Counts still do not
orient the arrow, and the examples do not select physical production dynamics.

## Stacking

This PR should target:

```text
physics-loop/post-record-supplied-orientation-bridge-interface-20260606
```

because it is an example layer over PR #2839.

## Files

- `docs/POST_RECORD_DIRECTED_CERTIFICATE_EXAMPLES_2026-06-06.md`
- `scripts/frontier_post_record_directed_certificate_examples_2026_06_06.py`
- `logs/runner-cache/frontier_post_record_directed_certificate_examples_2026_06_06.txt`
- `.claude/science/physics-loops/post-record-directed-certificate-examples-20260606/`

## Next exact action

Closed for campaign purposes. Pivot to a production-kernel selection firewall
for directed certificates while runtime remains.

## PR

```yaml
pr_url: "https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/2850"
base: "physics-loop/post-record-supplied-orientation-bridge-interface-20260606"
initial_mergeable: MERGEABLE
initial_merge_state_status: UNSTABLE
initial_checks: "audit_pipeline in progress at initial verification"
final_mergeable: null
final_merge_state_status: CLEAN
final_checks: "audit_pipeline completed SUCCESS at final verification"
```
