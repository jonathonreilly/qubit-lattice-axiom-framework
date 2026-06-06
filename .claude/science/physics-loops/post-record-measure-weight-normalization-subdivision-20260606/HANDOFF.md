# Handoff

## Summary

This stacked block subdivides the measure/weight/normalization rows:

```text
MEASURE_WEIGHT_NORMALIZATION_ROWS=41
SOURCE_MEASURE_OR_RN_BRIDGE_ROWS=14
CHARACTER_PATH_CHANNEL_WEIGHT_ROWS=10
TRACE_NORMALIZATION_REFERENCE_ROWS=8
SELECTOR_TANGENT_READOUT_WEIGHT_ROWS=5
GENERIC_MEASURE_WEIGHT_IMPORT_ROWS=4
NORMALIZED_MEASURE_SELECTS_DIAL=FALSE
```

## Meaning

Finite supplied weights can be normalized exactly. That gives a normalized
measure under the supplied rule, not selector authority.

## Stacking

This PR should target:

```text
physics-loop/post-record-selector-dial-bucket-subdivision-20260606
```

because it builds directly on the `measure_weight_normalization` row split.

## Files

- `docs/POST_RECORD_MEASURE_WEIGHT_NORMALIZATION_SUBDIVISION_2026-06-06.md`
- `scripts/frontier_post_record_measure_weight_normalization_subdivision_2026_06_06.py`
- `logs/runner-cache/frontier_post_record_measure_weight_normalization_subdivision_2026_06_06.txt`
- `.claude/science/physics-loops/post-record-measure-weight-normalization-subdivision-20260606/`

## Next exact action

Open the stacked PR and verify GitHub merge/check status.

## PR

```yaml
pr_url: null
base: "physics-loop/post-record-selector-dial-bucket-subdivision-20260606"
initial_mergeable: null
initial_merge_state_status: null
initial_checks: null
```
