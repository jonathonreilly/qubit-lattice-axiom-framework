# Handoff

## Summary

This branch repairs source-packet presentation for the live staggered Green
packet. The verifier now reports `source_full_length` and `source_contains`
checks for the packet checker, Green-closure source, and prototype helper
source. The source-packet cache and JSON were regenerated at
`SUMMARY: STAGGERED GREEN SOURCE PACKET PASS=40 FAIL=0`.

## Verification Commands

```bash
python3 scripts/cached_runner_output.py scripts/staggered_backreaction_live_green_source_packet_manifest_2026_06_04.py --check-only
python3 scripts/cached_runner_output.py scripts/staggered_backreaction_live_green_packet_check.py --check-only
python3 scripts/precompute_audit_runners.py --runners scripts/staggered_backreaction_live_green_packet_check.py,scripts/staggered_backreaction_live_green_source_packet_manifest_2026_06_04.py,scripts/frontier_staggered_backreaction_green_closure.py,scripts/frontier_staggered_backreaction_prototype.py --check-only
git diff --check origin/main
git diff --name-only origin/main -- docs/audit
```

## Reviewer Notes

- This PR does not edit audit results.
- This PR does not add axioms.
- This PR keeps the live Green packet bounded.
- Independent audit owns any status movement.
