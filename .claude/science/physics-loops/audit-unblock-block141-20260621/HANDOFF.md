# Handoff

## Summary

Block141 registers and strengthens the Diamond sensor prediction note's runner.

The target row:

```text
diamond_sensor_prediction_note
```

now has:

```text
runner_path = scripts/diamond_sensor_prediction_probe.py
audit_status = unaudited
effective_status = unaudited
```

The runner now checks the printed toy-law properties and reports:

```text
ASSERTIONS: PASS=30 FAIL=0
```

The runner classifier records `dominant_class: A` with `A=3`, `D=1`, and
`assert_count=7`.

## Boundary

- No audit-loop run.
- No `apply_audit.py` run.
- No verdict or effective-status promotion.
- No absolute NV detectability claim.
- No source-to-NV coupling or amplitude/noise bridge added.
- Ideal detector theorem remains a separate dependency.

## Verification

- `python3 scripts/diamond_sensor_prediction_probe.py` -> `ASSERTIONS: PASS=30 FAIL=0`.
- `python3 scripts/diamond_ideal_lockin_detector_theorem.py` -> `ASSERTIONS: PASS`.
- `bash docs/audit/scripts/run_pipeline.sh` -> complete, no invalidations.
- `python3 scripts/precompute_audit_runners.py --runners scripts/diamond_sensor_prediction_probe.py --check-only --push-mode none --allow-non-main` -> fresh.
- `python3 docs/audit/scripts/audit_lint.py --strict` -> OK.
- `python3 -m py_compile scripts/diamond_sensor_prediction_probe.py scripts/diamond_ideal_lockin_detector_theorem.py docs/audit/scripts/build_citation_graph.py docs/audit/scripts/seed_audit_ledger.py docs/audit/scripts/classify_runner_passes.py` -> OK.
- `python3 scripts/precompute_audit_runners.py --pr-diff origin/main --check-only --push-mode none --allow-non-main` -> all relevant caches fresh.
- `git diff --check` -> OK.

## Next Exact Action

Open PR for block141, then continue to the next unaudited runner-registration
miss. Do not refresh older PR branches onto `main`.
