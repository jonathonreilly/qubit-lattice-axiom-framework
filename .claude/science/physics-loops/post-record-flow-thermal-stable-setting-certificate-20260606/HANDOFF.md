# Handoff

## Summary

This stacked block defines the supplied stable-setting certificate:

```text
FLOW_OR_THERMAL_STABILITY_ROWS=36
STABLE_SETTING_SELECTS_DIAL=FALSE
GENERATION_OR_KOIDE_DIAL_SELECTED=FALSE
SELECTED_DIAL_DERIVED_FROM_STABILITY=FALSE
```

## Meaning

A stable feature may be certified under a supplied flow, score, or thermal rule.
That is a stable setting on a dial, not a selected dial value.

## Stacking

This PR should target:

```text
physics-loop/post-record-stability-dynamics-selector-subdivision-20260606
```

because it builds directly on the `flow_or_thermal_stability` row split.

## Files

- `docs/POST_RECORD_FLOW_THERMAL_STABLE_SETTING_CERTIFICATE_2026-06-06.md`
- `scripts/frontier_post_record_flow_thermal_stable_setting_certificate_2026_06_06.py`
- `logs/runner-cache/frontier_post_record_flow_thermal_stable_setting_certificate_2026_06_06.txt`
- `.claude/science/physics-loops/post-record-flow-thermal-stable-setting-certificate-20260606/`

## Next exact action

Open the stacked PR and verify GitHub merge/check status.

## PR

```yaml
pr_url: null
base: "physics-loop/post-record-stability-dynamics-selector-subdivision-20260606"
initial_mergeable: null
initial_merge_state_status: null
initial_checks: null
```
