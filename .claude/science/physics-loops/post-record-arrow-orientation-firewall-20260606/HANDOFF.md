# Handoff

## Summary

This stacked block proves a count-only dynamics firewall:

```text
POST_RECORD_COUNTS_ORIENT_PHYSICAL_ARROW=FALSE
COUNT_PUSHFORWARD_REVERSAL_INVARIANT=TRUE
PHYSICAL_ARROW_DERIVED_FROM_RECORD=FALSE
PRODUCTION_KERNEL_SELECTED=FALSE
```

## Meaning

Post-record histories and counts remain valuable realized information. They do
not by themselves orient the physical arrow or select the production kernel.
Any arrow/dynamics row needs a supplied oriented law, boundary condition, clock,
rate, kernel, Hamiltonian, transfer operator, or instrument bridge.

## Stacking

This PR should target:

```text
physics-loop/post-record-stability-dynamics-selector-subdivision-20260606
```

because it consumes the `arrow_or_dynamics_bridge` implication from PR #2837.

## Files

- `docs/POST_RECORD_ARROW_ORIENTATION_FIREWALL_2026-06-06.md`
- `scripts/frontier_post_record_arrow_orientation_firewall_2026_06_06.py`
- `logs/runner-cache/frontier_post_record_arrow_orientation_firewall_2026_06_06.txt`
- `.claude/science/physics-loops/post-record-arrow-orientation-firewall-20260606/`

## Next exact action

Commit, push, and open a stacked PR.

## PR

```yaml
pr_url: null
base: "physics-loop/post-record-stability-dynamics-selector-subdivision-20260606"
mergeable: null
merge_state_status: null
status_check_rollup: null
```
