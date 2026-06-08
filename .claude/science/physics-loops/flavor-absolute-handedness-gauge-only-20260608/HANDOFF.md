# Handoff

Target claim: `flavor_absolute_handedness_is_gauge_relative_is_physical_narrow_theorem_note_2026-06-08`

Remote branch: `physics-loop/flavor-absolute-handedness-gauge-only-20260608`

## What Changed

- Narrowed the note from "magnitude and relative orientations are physical" to "absolute handedness is gauge; magnitude and relative-orientation readouts remain open."
- Removed runner dependence on the audit ledger.
- Added source-boundary checks that explicitly keep the `2/9` physical readout and CP/mixing relative-orientation bridge open.
- Refreshed the runner cache with `TOTAL: PASS=17 FAIL=0`.

## Verification

- `python3 scripts/frontier_flavor_absolute_handedness_is_gauge.py`
- `python3 scripts/cached_runner_output.py --refresh scripts/frontier_flavor_absolute_handedness_is_gauge.py --timeout-sec 120`

## Remaining Blockers

- Prove a physical charged-lepton single-summand readout bridge for `2/9`, or keep it outside this theorem.
- Prove a multi-sector shared-axis/readout bridge that identifies relative orientation with CP or mixing, or keep it as an invariant candidate.
