# Review History

Local verification:

- `python3 scripts/diamond_sensor_prediction_probe.py` -> `ASSERTIONS:
  PASS=30 FAIL=0`.
- `python3 scripts/diamond_ideal_lockin_detector_theorem.py` -> `ASSERTIONS:
  PASS`.
- Parser probe -> `scripts/diamond_sensor_prediction_probe.py`.
- `bash docs/audit/scripts/run_pipeline.sh` completed; no invalidations.
- `python3 scripts/precompute_audit_runners.py --runners scripts/diamond_sensor_prediction_probe.py --check-only --push-mode none --allow-non-main` -> fresh.
- `python3 docs/audit/scripts/audit_lint.py --strict` -> OK, no errors.
- `python3 -m py_compile scripts/diamond_sensor_prediction_probe.py scripts/diamond_ideal_lockin_detector_theorem.py docs/audit/scripts/build_citation_graph.py docs/audit/scripts/seed_audit_ledger.py docs/audit/scripts/classify_runner_passes.py` -> OK.
- `python3 scripts/precompute_audit_runners.py --pr-diff origin/main --check-only --push-mode none --allow-non-main` -> all relevant caches fresh.
- `git diff --check` -> OK.

Review-loop is deferred to the reviewer lane per the user's instruction that
the review skill will take PRs and cherry-pick useful science/tooling.
