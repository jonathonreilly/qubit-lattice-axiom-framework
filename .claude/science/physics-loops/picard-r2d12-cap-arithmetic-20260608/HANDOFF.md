# Handoff

Target claim: `plaquette_v1_picard_fuchs_ode_rank_exclusion_r2_d12_narrow_theorem_note_2026-05-17`

Remote branch: `physics-loop/picard-r2d12-cap-arithmetic-20260608`

## What Changed

- Corrected the `ORDER=52` cap display from `min(47,47)=47` to `min(47,48)=47`.
- Left the exact-rational runner unchanged because it already computes the full-rank matrix.

## Verification

- `python3 scripts/audit_companion_plaquette_v1_picard_fuchs_ode_rank_exclusion_r2_d12_narrow_2026_05_17.py`
- `python3 scripts/cached_runner_output.py --check-only scripts/audit_companion_plaquette_v1_picard_fuchs_ode_rank_exclusion_r2_d12_narrow_2026_05_17.py`
- `python3 -m py_compile scripts/audit_companion_plaquette_v1_picard_fuchs_ode_rank_exclusion_r2_d12_narrow_2026_05_17.py`
- `git diff --check`

## Remaining Blockers

None for this bounded row after reviewer extraction. All-order Picard-Fuchs minimality remains a separate lane.
