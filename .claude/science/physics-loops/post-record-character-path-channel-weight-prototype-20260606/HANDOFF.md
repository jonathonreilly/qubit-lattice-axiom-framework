# Handoff

## Summary

This stacked block supplies a finite character/path/channel weight prototype:

```text
CHARACTER_PATH_CHANNEL_WEIGHT_ROWS=10
PHYSICAL_MEASURE_SELECTED=FALSE
PATH_RULE_DERIVED_FROM_RECORD=FALSE
CHARACTER_PACKET_DERIVED_FROM_RECORD=FALSE
CHANNEL_RULE_DERIVED_FROM_RECORD=FALSE
BORN_LAW_DERIVED_FROM_RECORD=FALSE
```

## Meaning

Finite supplied path, channel, and character weights can be normalized and
composed exactly. They are supplied weight semantics, not physical measure
selection or Record-derived dynamics.

## Stacking

This PR should target:

```text
physics-loop/post-record-source-measure-trace-normalization-prototype-20260606
```

because it builds directly on the finite source-measure normalization
prototype.

## Files

- `docs/POST_RECORD_CHARACTER_PATH_CHANNEL_WEIGHT_PROTOTYPE_2026-06-06.md`
- `scripts/frontier_post_record_character_path_channel_weight_prototype_2026_06_06.py`
- `logs/runner-cache/frontier_post_record_character_path_channel_weight_prototype_2026_06_06.txt`
- `.claude/science/physics-loops/post-record-character-path-channel-weight-prototype-20260606/`

## Next exact action

Commit, push, and open the stacked PR.

## PR

```yaml
pr_url: null
base: "physics-loop/post-record-source-measure-trace-normalization-prototype-20260606"
initial_mergeable: null
initial_merge_state_status: null
initial_checks: null
```
