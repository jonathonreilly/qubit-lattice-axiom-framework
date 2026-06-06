# Handoff

## Summary

This stacked block subdivides the 64 `stability_or_dynamics_selector` rows from
the selector/dial subdivision companion:

```text
flow_or_thermal_stability: 36
arrow_or_dynamics_bridge: 28
```

## Meaning

The subdivision gives the dynamics campaign two different next queues:

- stable-setting work under supplied flow, thermal, fixed-point, attractor, or
  separatrix surfaces;
- physical-arrow and production-dynamics bridge work for rows that need a
  Hamiltonian, transfer, kernel, instrument, decoherence, measurement, clock,
  or rate import.

stable setting is not selected dial.

## Stacking

This PR should target:

```text
physics-loop/post-record-selector-dial-bucket-subdivision-20260606
```

because it subdivides the selector/dial output from PR #2836.

## Files

- `docs/POST_RECORD_STABILITY_DYNAMICS_SELECTOR_SUBDIVISION_2026-06-06.md`
- `scripts/frontier_post_record_stability_dynamics_selector_subdivision_2026_06_06.py`
- `logs/runner-cache/frontier_post_record_stability_dynamics_selector_subdivision_2026_06_06.txt`
- `.claude/science/physics-loops/post-record-stability-dynamics-selector-subdivision-20260606/`

## Next exact action

Commit, push, and open a stacked PR.

## PR

```yaml
pr_url: null
base: "physics-loop/post-record-selector-dial-bucket-subdivision-20260606"
mergeable: null
merge_state_status: null
status_check_rollup: null
```
