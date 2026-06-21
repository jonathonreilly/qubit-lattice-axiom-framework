# [physics-loop] audit-unblock block153: bounded Diamond protocol runner registration

Registers an executable bounded runner for `diamond_sensor_protocol_note`.

## Scope

- Adds `scripts/diamond_sensor_protocol_bounded_probe.py`.
- Adds runner metadata to `docs/DIAMOND_SENSOR_PROTOCOL_NOTE.md`.
- Adds fresh runner cache: `logs/runner-cache/diamond_sensor_protocol_bounded_probe.txt`.
- Regenerates audit ledger/queue/citation/runner-classification surfaces.
- Adds branch-local handoff pack under `.claude/science/physics-loops/audit-unblock-block153-20260621/`.

## Claim Boundary

This PR keeps the row `bounded_theorem` / `unaudited` / `effective_status: unaudited`.
It does not apply audit verdicts, does not update repo-wide lane/status authority
surfaces, and does not claim a closed Diamond/NV protocol or calibrated lab
detectability. The source-to-NV coupling map and calibrated absolute
amplitude/noise budget remain open.

## Verification

- `python3 scripts/diamond_sensor_protocol_bounded_probe.py`
  - `SUMMARY: PASS=17 FAIL=0`
- `python3 scripts/diamond_sensor_protocol_probe.py`
- `python3 scripts/diamond_ideal_lockin_detector_theorem.py`
  - `ASSERTIONS: PASS`
- `bash docs/audit/scripts/run_pipeline.sh`
- `python3 scripts/precompute_audit_runners.py --runners scripts/diamond_sensor_protocol_bounded_probe.py --push-mode none --allow-non-main`
- `python3 scripts/precompute_audit_runners.py --runners scripts/diamond_sensor_protocol_bounded_probe.py --check-only --push-mode none --allow-non-main`
- `python3 docs/audit/scripts/audit_lint.py --strict`
  - `OK: no errors` with the existing 139 notices
- `python3 -m py_compile scripts/diamond_sensor_protocol_bounded_probe.py scripts/diamond_sensor_protocol_probe.py scripts/diamond_ideal_lockin_detector_theorem.py docs/audit/scripts/build_citation_graph.py docs/audit/scripts/seed_audit_ledger.py docs/audit/scripts/classify_runner_passes.py`
- `git diff --check`

## Row Check

`diamond_sensor_protocol_note` now has:

- `claim_type`: `bounded_theorem`
- `audit_status`: `unaudited`
- `effective_status`: `unaudited`
- `runner_path`: `scripts/diamond_sensor_protocol_bounded_probe.py`
- runner classification: dominant `B`, `assert_count: 1`
