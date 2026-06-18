## Summary

Adds a partial exact-support bridge for the audited conditional
`emergent_lorentz_interacting_velocity_rg_attractor_note_2026-06-06` row.

The new theorem proves directly that the leading spatial central-difference
artifact has zero time-channel projection and one `O_h` scalar spatial channel.
This addresses the structural "spatial-only" part of the power-divergent mixing
blocker, while leaving the physical coefficient, one-loop RG derivation,
fixed-point gamma, and LV-bound sufficiency open.

## Trace gate

- Target claim:
  `emergent_lorentz_interacting_velocity_rg_attractor_note_2026-06-06`
- Trace class: `direct_blocker_closure`
- Reachability: `partially_closes`
- Audit/review status: source-side PR only; independent review/audit still owns
  effective status.

## Artifacts

- `docs/EMERGENT_LORENTZ_SPATIAL_BZ_POWER_MIXING_BOUNDARY_THEOREM_NOTE_2026-06-18.md`
- `scripts/frontier_emergent_lorentz_spatial_bz_power_mixing_boundary_2026_06_18.py`
- `logs/runner-cache/frontier_emergent_lorentz_spatial_bz_power_mixing_boundary_2026_06_18.txt`
- `docs/EMERGENT_LORENTZ_INTERACTING_VELOCITY_RG_ATTRACTOR_NOTE_2026-06-06.md`
- `.claude/science/physics-loops/lorentz-spatial-bz-mixing-boundary-20260618/HANDOFF.md`
- `.claude/science/physics-loops/lorentz-spatial-bz-mixing-boundary-20260618/TRACE_GATE.md`
- `.claude/science/physics-loops/lorentz-spatial-bz-mixing-boundary-20260618/CLAIM_STATUS_CERTIFICATE.md`

## Checks

- `python3 scripts/frontier_emergent_lorentz_spatial_bz_power_mixing_boundary_2026_06_18.py`
- `python3 -m py_compile scripts/frontier_emergent_lorentz_spatial_bz_power_mixing_boundary_2026_06_18.py`
- `python3 scripts/frontier_emergent_lorentz_interacting_velocity_rg_attractor_2026_06_06.py`
- `python3 scripts/cached_runner_output.py --refresh scripts/frontier_emergent_lorentz_spatial_bz_power_mixing_boundary_2026_06_18.py`
- `python3 scripts/cached_runner_output.py --check-only scripts/frontier_emergent_lorentz_spatial_bz_power_mixing_boundary_2026_06_18.py`
- `git diff --check`
