## Summary

Registers and strengthens the existing Diamond/NV protocol probe for `diamond_sensor_protocol_note`.

This is source-side audit-unblock work only. The target remains:

- `audit_status: unaudited`
- `effective_status: unaudited`
- `claim_type: bounded_theorem`

The runner classification is intentionally D-heavy because the note preserves real open gaps: no source-to-NV coupling map and no calibrated absolute amplitude/noise budget.

## Artifacts

- Source note: `docs/DIAMOND_SENSOR_PROTOCOL_NOTE.md`
- Runner: `scripts/diamond_sensor_protocol_probe.py`
- Runner cache: `logs/runner-cache/diamond_sensor_protocol_probe.txt`
- Loop pack: `.claude/science/physics-loops/audit-unblock-block144-20260621/`
- Generated surfaces:
  - `docs/audit/AUDIT_LEDGER.md`
  - `docs/audit/AUDIT_QUEUE.md`
  - `docs/audit/data/audit_ledger.json`
  - `docs/audit/data/audit_queue.json`
  - `docs/audit/data/citation_graph.json`
  - `docs/audit/data/runner_classification.json`

## Verification

- `python3 scripts/diamond_sensor_protocol_probe.py`
  - `SUMMARY: PASS=11 FAIL=0`
- `python3 scripts/diamond_ideal_lockin_detector_theorem.py`
  - `ASSERTIONS: PASS`
- `bash docs/audit/scripts/run_pipeline.sh`
  - completed with no invalidations
- `python3 scripts/precompute_audit_runners.py --runners scripts/diamond_sensor_protocol_probe.py --push-mode none --allow-non-main`
  - refreshed runner cache
- `python3 scripts/precompute_audit_runners.py --runners scripts/diamond_sensor_protocol_probe.py --check-only --push-mode none --allow-non-main`
  - all relevant caches fresh
- `python3 docs/audit/scripts/audit_lint.py --strict`
  - `3474 rows checked`; `139 notices`; `OK: no errors`
- `python3 -m py_compile scripts/diamond_sensor_protocol_probe.py scripts/diamond_ideal_lockin_detector_theorem.py docs/audit/scripts/build_citation_graph.py docs/audit/scripts/seed_audit_ledger.py docs/audit/scripts/classify_runner_passes.py`
  - pass
- `python3 scripts/precompute_audit_runners.py --pr-diff origin/main --check-only --push-mode none --allow-non-main`
  - all relevant caches fresh
- `git diff --check`
  - pass

## Audit Boundary

No audit verdicts are authored here. This PR did not run `audit-loop` or `docs/audit/scripts/apply_audit.py`; independent review/audit remains required.
