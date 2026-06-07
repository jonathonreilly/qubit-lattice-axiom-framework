# Handoff

Changed:

- `docs/VALLEY_LINEAR_WIDE_TAIL_NOTE.md`
- `scripts/valley_linear_wide_tail_replay.py`
- `logs/runner-cache/valley_linear_wide_tail_replay.txt`

Verification:

- `python3 -m py_compile scripts/valley_linear_wide_tail_replay.py`
- `python3 scripts/valley_linear_wide_tail_replay.py`
- `python3 scripts/precompute_audit_runners.py --runners scripts/valley_linear_wide_tail_replay.py --force --push-mode=none`
- Runner/cache result: `SCORECARD PASS=9 FAIL=0`

No `docs/audit/**` files are changed.
