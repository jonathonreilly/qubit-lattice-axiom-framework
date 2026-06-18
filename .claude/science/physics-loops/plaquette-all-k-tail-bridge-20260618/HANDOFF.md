# Handoff

This PR adds bounded source-side support for the plaquette word-count all-k
remainder blocker.

Changed source packet:

- Adds `GAUGE_VACUUM_PLAQUETTE_WORD_COUNT_RESCALED_TAIL_SUPPORT_NOTE_2026-06-18.md`.
- Adds `scripts/gauge_vacuum_plaquette_word_count_rescaled_tail_support_2026_06_18.py`
  and its runner cache.
- Wires the existing all-k remainder note to the new support artifact.
- Leaves the analytic monotone/Neumann tail proof open.

Verification:

```text
python3 scripts/gauge_vacuum_plaquette_word_count_rescaled_tail_support_2026_06_18.py
TOTAL: PASS=14, FAIL=0

python3 scripts/cached_runner_output.py --check-only scripts/gauge_vacuum_plaquette_word_count_rescaled_tail_support_2026_06_18.py
fresh logs/runner-cache/gauge_vacuum_plaquette_word_count_rescaled_tail_support_2026_06_18.txt

python3 -m py_compile scripts/gauge_vacuum_plaquette_word_count_rescaled_tail_support_2026_06_18.py
git diff --check
```

Reviewer focus:

- Confirm the branch does not claim the full all-k theorem is closed.
- Confirm the runner actually exposes the k=20 double-cancellation issue.
- Confirm the parent note keeps the remaining analytic uniform-tail proof open.
- Confirm no audit/status/publication authority surfaces are included.
