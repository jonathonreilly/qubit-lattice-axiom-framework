# Handoff

## Summary

This stacked block provides a finite evidence ladder for bounded/conditional
audit rows.

The runner verifies nine representative row types:

- append/count row -> exact support candidate;
- exact finite p-value row -> conditional audit ready;
- concentration certificate row -> conditional audit ready;
- expectation-only p-value row -> blocked expectation-only;
- simulation-only p-value row -> support-only, not calibrated;
- stable dial row -> stable setting support;
- selected dial from stability only -> blocked missing selector;
- bounded production dynamics row -> bounded support with open imports;
- branch-local audit verdict row -> independent audit only.

## Meaning

The ladder is a guardrail for using the Record/dynamics stack. It lets a row
claim only the evidence rung it reaches.

## Stacking

This PR should target:

```text
physics-loop/post-record-supplied-concentration-certificate-interface-20260606
```

because it uses the concentration-certificate interface from PR #2833.

## Files

- `docs/POST_RECORD_CONDITIONAL_AUDIT_EVIDENCE_LADDER_2026-06-06.md`
- `scripts/frontier_post_record_conditional_audit_evidence_ladder_2026_06_06.py`
- `logs/runner-cache/frontier_post_record_conditional_audit_evidence_ladder_2026_06_06.txt`
- `.claude/science/physics-loops/post-record-conditional-audit-evidence-ladder-20260606/`

## Next exact action

Commit, push, open the stacked PR, record PR status, then pivot to the next
campaign lane.
