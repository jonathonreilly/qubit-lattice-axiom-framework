# Handoff

## Summary

This stacked block supplies a finite source-measure trace/RN normalization
prototype:

```text
SOURCE_TRACE_PROTOTYPE_ROWS=22
SOURCE_MEASURE_OR_RN_BRIDGE_ROWS=14
TRACE_NORMALIZATION_REFERENCE_ROWS=8
PHYSICAL_REFERENCE_IDENTIFIED=FALSE
NORMALIZED_MEASURE_SELECTS_DIAL=FALSE
BORN_LAW_DERIVED_FROM_RECORD=FALSE
```

## Meaning

The prototype certifies finite measure/RN semantics under supplied reference
and source weights. It does not identify the physical pre-record reference,
derive Born law, or select a dial.

## Stacking

This PR should target:

```text
physics-loop/post-record-measure-weight-normalization-subdivision-20260606
```

because it builds directly on the measure/weight subdivision companion.

## Files

- `docs/POST_RECORD_SOURCE_MEASURE_TRACE_NORMALIZATION_PROTOTYPE_2026-06-06.md`
- `scripts/frontier_post_record_source_measure_trace_normalization_prototype_2026_06_06.py`
- `logs/runner-cache/frontier_post_record_source_measure_trace_normalization_prototype_2026_06_06.txt`
- `.claude/science/physics-loops/post-record-source-measure-trace-normalization-prototype-20260606/`

## Next exact action

Commit, push, and open the stacked PR.

## PR

```yaml
pr_url: null
base: "physics-loop/post-record-measure-weight-normalization-subdivision-20260606"
initial_mergeable: null
initial_merge_state_status: null
initial_checks: null
```
