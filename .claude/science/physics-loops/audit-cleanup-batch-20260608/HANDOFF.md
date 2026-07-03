# Handoff: Audit Cleanup Batch 2026-06-08

## What This PR Does

This PR packages four source-side audit-unblock repairs:

- `docs/NEWTONIAN_DISTANCE_LAW_CONFIRMED.md`: converts the stale historical
  headline row into a local, SHA-pinned pointer to the existing bounded
  wide-tail replay note, runner, frozen raw log, and cache.
- `docs/GATE_B_DYNAMICS_NOTE.md`: narrows Gate B to a generated-geometry
  source index, removes the bold far-field closure overclaim, and converts
  stale machine-local links to repo-relative links.
- `docs/MESOSCOPIC_SURROGATE_ALTERNATE_FAMILY_SCOUT_NOTE.md`: demotes the note
  from bounded theorem metadata to meta/support planning index metadata.
- `docs/lanes/ordered-lattice/README.md`: demotes the README from
  proposed-retained authority-style wording to a historical lane index.

The branch adds two guards:

- `scripts/newtonian_distance_law_confirmed_pointer_guard_2026_06_08.py`
- `scripts/audit_cleanup_scope_guard_2026_06_08.py`

## What It Does Not Do

- It does not edit `docs/audit/**`.
- It does not apply audit verdicts.
- It does not assert new retained or proposed-retained science.
- It does not close the physical Gate B bridge, the mesoscopic objective
  ranking problem, or ordered-lattice per-note authority questions.

## Inspected And Left Alone

`WIDE_LATTICE_H2T_DISTANCE_LAW_NOTE.md` was inspected and not modified. Main
already has the 2026-06-07 verifier repair, fresh cache, and frozen log SHA, so
duplicating that work in this PR would add churn without unlocking more audit.

## Verification

Run before handoff:

```bash
python3 scripts/newtonian_distance_law_confirmed_pointer_guard_2026_06_08.py
python3 scripts/valley_linear_wide_tail_replay.py
python3 scripts/audit_cleanup_scope_guard_2026_06_08.py
python3 scripts/mesoscopic_surrogate_alternate_family_scout.py
python3 scripts/cached_runner_output.py --check-only scripts/newtonian_distance_law_confirmed_pointer_guard_2026_06_08.py
python3 scripts/cached_runner_output.py --check-only scripts/audit_cleanup_scope_guard_2026_06_08.py
python3 scripts/cached_runner_output.py --check-only scripts/valley_linear_wide_tail_replay.py
python3 scripts/cached_runner_output.py --check-only scripts/mesoscopic_surrogate_alternate_family_scout.py
python3 scripts/cached_runner_output.py --check-only scripts/wide_lattice_h2t_distance_replay.py
git diff --check
git diff -- docs/audit
```

The final reviewer should independently decide whether these repairs make the
rows reauditable and whether to extract all four surfaces together or split
them.
