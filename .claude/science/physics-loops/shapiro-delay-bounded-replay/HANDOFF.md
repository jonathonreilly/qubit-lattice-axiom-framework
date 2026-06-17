# Handoff

This PR repairs `shapiro_delay_note` as a bounded finite replay:

- the note no longer claims retained/proposed-retained status;
- failed archived Shapiro bridge/rendering notes are removed from the live
  artifact chain;
- the primary runner recomputes the table from `scripts/shapiro_delay_portable.py`
  instead of hard-coding rows;
- the cache records PASS gates for exact zero control, family spread below
  `2.5e-4 rad`, monotone phase, bounded source status, static-cone no-go
  boundary, and exclusion of lab/field-speed claims.

Checks run:

- `python3 scripts/shapiro_phase_lag_probe.py --format text`
- `python3 scripts/cached_runner_output.py scripts/shapiro_phase_lag_probe.py --refresh --timeout-sec 600`
- `python3 scripts/cached_runner_output.py scripts/shapiro_phase_lag_probe.py --check-only`
- `python3 -m py_compile scripts/shapiro_phase_lag_probe.py`
- `git diff --check`

No audit loop was run, no audit data was edited, and no main landing was done.
