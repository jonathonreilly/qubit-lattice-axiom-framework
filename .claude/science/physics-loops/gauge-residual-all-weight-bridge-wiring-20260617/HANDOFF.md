# Gauge Residual All-Weight Bridge Wiring Handoff

## Target

The audited gauge-vacuum residual/environment prompts still name the bridge

```text
stripped residual source-sector operator equals normalized convolution by
the actual compressed unmarked spatial Wilson environment boundary character
```

as open. Current `origin/main` already has a narrow all-weight formal
convolution bridge plus a symbolic companion runner, but the row was not
easy for the audit machinery to discover and the two parent finite-packet
notes did not cite it.

## Change

- Adds plain inline primary-runner and runner-cache metadata to
  `GAUGE_VACUUM_PLAQUETTE_RESIDUAL_ENVIRONMENT_ALL_WEIGHT_CONVOLUTION_IDENTIFICATION_NARROW_THEOREM_NOTE_2026-05-17.md`.
- Wires both parent finite-packet notes to the all-weight bridge as
  structural formal-convolution support only.
- Extends the symbolic companion runner so it fails if that metadata or
  parent wiring disappears.
- Refreshes the runner cache.

## Honest Boundary

This does not compute the beta=6 unmarked spatial Wilson environment
coefficients from the full unmarked DOF integral. It does not assert
normalized `kappa_(0,0)=1` closure and does not promote either parent row.

The movement is narrower: the formal Peter-Weyl diagonal-convolution
dictionary for the already-stripped residual eigenvalue sequence is now
explicitly source-wired and mechanically checked.

## Verification

```bash
python3 scripts/audit_companion_gauge_vacuum_plaquette_residual_environment_all_weight_convolution_identification.py
python3 scripts/cached_runner_output.py --refresh scripts/audit_companion_gauge_vacuum_plaquette_residual_environment_all_weight_convolution_identification.py
python3 scripts/cached_runner_output.py --check-only scripts/audit_companion_gauge_vacuum_plaquette_residual_environment_all_weight_convolution_identification.py
python3 -m py_compile scripts/audit_companion_gauge_vacuum_plaquette_residual_environment_all_weight_convolution_identification.py
git diff --check
git diff -- docs/audit docs/publication docs/repo/FRONT_DOOR_STATUS.md --stat
```
