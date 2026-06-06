# Handoff

PR purpose:

Repair the audited conditional source blocker on the I12 right-handed-neutrino
thermal-exclusion note. The branch corrects the numeric margin at `T = 100 GeV`
and replaces O(1)-only route language with the actual threshold condition
`y_nu >= y_thr`.

Files changed:

- `docs/SM_GSTAR_I12_NUR_THERMAL_EXCLUSION_BOUNDED_NOTE_2026-05-29.md`
- `scripts/frontier_sm_gstar_i12_nur_thermal_exclusion_2026_05_29.py`
- `logs/runner-cache/frontier_sm_gstar_i12_nur_thermal_exclusion_2026_05_29.txt`
- `.claude/science/physics-loops/gstar-i12-threshold-wording-20260606/`

Verification:

- Runner passes with `PASS=66 FAIL=0`.
- Runner cache is fresh.
- `git diff --check` passes.
- `git diff -- docs/audit --exit-code` passes.

Audit boundary:

No `docs/audit/**` files are modified. This PR does not set audit verdicts or
claim an effective status change. It is intended for Codex reviewer extraction
and independent re-audit.

Remaining blocker after this PR:

The note still depends on the empirical small-neutrino-mass observation. A full
unbounded closure would need a framework-native neutrino-mass derivation or a
separate retained bridge that retires that import.
