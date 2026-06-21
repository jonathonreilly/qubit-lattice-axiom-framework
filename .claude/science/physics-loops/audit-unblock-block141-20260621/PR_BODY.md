## Summary

Registers and strengthens the existing runner for the high-priority unaudited
Diamond sensor prediction note.

Before this PR, `diamond_sensor_prediction_note` referenced
`diamond_sensor_prediction_probe.py` in prose, but the audit graph/ledger had
`runner_path: null`. The probe also printed the prediction card without
asserting the toy-law properties.

This PR:

- adds a standard `Runner` metadata line to the note;
- adds deterministic checks to `scripts/diamond_sensor_prediction_probe.py`;
- refreshes the runner cache;
- regenerates the small affected audit surfaces.

Result:

- target claim: `diamond_sensor_prediction_note`
- runner path: `scripts/diamond_sensor_prediction_probe.py`
- audit status remains `unaudited`
- effective status remains `unaudited`
- runner output: `ASSERTIONS: PASS=30 FAIL=0`
- runner classifier: `dominant_class: A`, with `A=3`, `D=1`

## Boundary

- No audit-loop run.
- No `apply_audit.py` run.
- No audit verdicts applied.
- No effective-status promotion.
- No absolute NV detectability claim.
- No source-to-NV coupling map or amplitude/noise bridge added.
- The ideal detector theorem remains a separate dependency row.

## Verification

- `python3 scripts/diamond_sensor_prediction_probe.py` -> `ASSERTIONS: PASS=30 FAIL=0`
- `python3 scripts/diamond_ideal_lockin_detector_theorem.py` -> `ASSERTIONS: PASS`
- `bash docs/audit/scripts/run_pipeline.sh` -> complete, no invalidations
- `python3 scripts/precompute_audit_runners.py --runners scripts/diamond_sensor_prediction_probe.py --check-only --push-mode none --allow-non-main` -> fresh
- `python3 docs/audit/scripts/audit_lint.py --strict` -> OK, no errors
- `python3 -m py_compile scripts/diamond_sensor_prediction_probe.py scripts/diamond_ideal_lockin_detector_theorem.py docs/audit/scripts/build_citation_graph.py docs/audit/scripts/seed_audit_ledger.py docs/audit/scripts/classify_runner_passes.py` -> OK
- `python3 scripts/precompute_audit_runners.py --pr-diff origin/main --check-only --push-mode none --allow-non-main` -> all relevant caches fresh
- `git diff --check` -> OK
