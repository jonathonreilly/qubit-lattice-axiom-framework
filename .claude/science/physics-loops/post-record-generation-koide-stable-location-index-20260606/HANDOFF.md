# Handoff

## Summary

This stacked block indexes the generation/Koide dial lane as stable-location
support only:

```text
KOIDE_OR_GENERATION_SELECTOR_ROWS=104
GENERATION_OR_KOIDE_STABLE_FEATURE_ROWS=2
GENERATION_KOIDE_STABLE_LOCATION_INDEX_ROWS=106
GENERATION_OR_KOIDE_DIAL_SELECTED=FALSE
STABLE_LOCATION_SELECTS_DIAL=FALSE
KOIDE_CLOSED=FALSE
```

## Meaning

Stable-location evidence can sit on the dial under supplied rules. It does not
select, force, or derive the dial value.

## Stacking

This PR should target:

```text
physics-loop/post-record-flow-thermal-stable-setting-certificate-20260606
```

because it builds directly on the supplied stable-setting certificate.

## Files

- `docs/POST_RECORD_GENERATION_KOIDE_STABLE_LOCATION_INDEX_2026-06-06.md`
- `scripts/frontier_post_record_generation_koide_stable_location_index_2026_06_06.py`
- `logs/runner-cache/frontier_post_record_generation_koide_stable_location_index_2026_06_06.txt`
- `.claude/science/physics-loops/post-record-generation-koide-stable-location-index-20260606/`

## Next exact action

Poll PR #2844 until `audit_pipeline` completes, then record the final clean PR
state if the check succeeds.

## PR

```yaml
pr_url: "https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/2844"
base: "physics-loop/post-record-flow-thermal-stable-setting-certificate-20260606"
initial_head: "ad1ff5c9fa34a63243448b9b1e9d82e5873e4855"
initial_mergeable: MERGEABLE
initial_merge_state_status: UNSTABLE
initial_checks: "audit_pipeline QUEUED"
```
