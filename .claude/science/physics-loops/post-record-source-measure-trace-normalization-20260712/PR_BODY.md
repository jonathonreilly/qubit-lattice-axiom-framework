## Summary

- exposes the measure/weight subdivision as a normal transitive helper import;
- links the helper source and cached output from the target note;
- verifies the helper cache's runner path, current source SHA, successful exit,
  and source/trace lane summaries;
- refreshes both runner caches and synchronizes the live inventory to 17
  source-measure rows plus 10 trace rows, 27 total.

## Named repair target

> runner_artifact_issue: include `scripts/frontier_post_record_measure_weight_normalization_subdivision_2026_06_06.py` and its SHA-pinned cache in the restricted packet, then re-audit the row coverage claim.

The finite RN/trace identity remains bounded to supplied finite inputs. This PR
does not assert an audit verdict or derive a physical reference measure, source
law, Born law, selector, or production dynamics. Independent audit remains
required before any effective-status change.

## Trace and review

- [Handoff](.claude/science/physics-loops/post-record-source-measure-trace-normalization-20260712/HANDOFF.md)
- [Trace gate](.claude/science/physics-loops/post-record-source-measure-trace-normalization-20260712/TRACE_GATE.md)
- [Claim-status certificate](.claude/science/physics-loops/post-record-source-measure-trace-normalization-20260712/CLAIM_STATUS_CERTIFICATE.md)
- [Review history](.claude/science/physics-loops/post-record-source-measure-trace-normalization-20260712/REVIEW_HISTORY.md)

Review-loop disposition: PASS WITH BOUNDED CLAIMS.

## Verification

- both changed runners compile and exit zero;
- helper runner: `SUMMARY: PASS=69 FAIL=0`;
- primary runner: `SUMMARY: PASS=55 FAIL=0`;
- both runner caches are fresh and SHA-matched;
- independent exhaustive two-point RN/expectation check passed;
- audit validation pipeline completed with no lint errors;
- generated queue row was `ready: true` with both transitive helper paths;
- generated audit authority files were restored before commit;
- vocabulary lint and `git diff --check` passed.
