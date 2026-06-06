# Handoff

## Summary

This stacked block subdivides the 210 selector/dial rows from the row-bucketing
companion:

```text
koide_or_generation_selector: 104
stability_or_dynamics_selector: 64
measure_weight_normalization: 41
generic_selector_rule: 1
```

## Meaning

The subdivision gives the campaign a practical next queue. It does not select a
dial, force Koide, or apply an audit verdict.

## Stacking

This PR should target:

```text
physics-loop/post-record-audit-evidence-ladder-row-bucketing-20260606
```

because it subdivides the row-bucketing output from PR #2835.

## Files

- `docs/POST_RECORD_SELECTOR_DIAL_BUCKET_SUBDIVISION_2026-06-06.md`
- `scripts/frontier_post_record_selector_dial_bucket_subdivision_2026_06_06.py`
- `logs/runner-cache/frontier_post_record_selector_dial_bucket_subdivision_2026_06_06.txt`
- `.claude/science/physics-loops/post-record-selector-dial-bucket-subdivision-20260606/`

## Next exact action

Commit, push, open the stacked PR, record PR status, then pivot to the next
campaign lane.
