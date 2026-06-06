# Handoff

## Summary

This stacked block maps the current production-dynamics-needed rows:

```text
PRODUCTION_DYNAMICS_NEEDED_ROWS=6
BOUNDARY_PHASE_FINITE_SCAN_ROWS=1
PERSISTENT_OBJECT_READOUT_KERNEL_ROWS=2
PERSISTENT_RECORD_PRODUCTION_OVERLAP_ROWS=3
PRODUCTION_DYNAMICS_DERIVED=FALSE
PRODUCTION_KERNEL_SELECTED=FALSE
PHYSICAL_ARROW_DERIVED_FROM_RECORD=FALSE
```

## Meaning

The six rows have bounded evidence, but retained-unbounded or
physical-dynamics movement needs supplied bridge data. Post-record records carry
realized information; production laws, kernels, clocks, rates, instruments, and
orientation bridges remain supplied imports.

## Stacking

This PR should target:

```text
physics-loop/post-record-supplied-orientation-bridge-interface-20260606
```

because the row map uses that parent interface for orientation/kernel bridge
language.

## Files

- `docs/POST_RECORD_PRODUCTION_DYNAMICS_NEEDED_ROW_MAP_2026-06-06.md`
- `scripts/frontier_post_record_production_dynamics_needed_row_map_2026_06_06.py`
- `logs/runner-cache/frontier_post_record_production_dynamics_needed_row_map_2026_06_06.txt`
- `.claude/science/physics-loops/post-record-production-dynamics-needed-row-map-20260606/`

## Next exact action

Wait for the final pushed head's `audit_pipeline` to complete, then record the
clean final PR/check state.

## PR

```yaml
pr_url: "https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/2840"
base: "physics-loop/post-record-supplied-orientation-bridge-interface-20260606"
initial_mergeable: MERGEABLE
initial_merge_state_status: UNSTABLE
initial_checks: "audit_pipeline in progress at first verification"
final_mergeable: null
final_merge_state_status: null
final_checks: null
```
