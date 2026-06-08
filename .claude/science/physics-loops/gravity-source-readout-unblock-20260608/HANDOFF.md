# Gravity Source/Readout Unblock Handoff

## Repair

Updated `docs/GRAV_DECOHERENCE_DERIVED_NOTE.md` with a 2026-06-08
dependency split. The row now directly cites existing bounded support for:

- density-operator position readout (`rho_grav(x)=<x|rho|x>`);
- canonical mass-linearity once the source map is supplied;
- weak-field response under canonical `V_grav=m phi(x)` coupling.

The runner firewall now checks that the source note contains this split.

## Verification

- `python3 scripts/frontier_grav_decoherence_derived.py`
- `python3 scripts/cached_runner_output.py --refresh scripts/frontier_grav_decoherence_derived.py`

## Remaining Science

This does not close the decoherence row beyond companion arithmetic. Remaining
bridges are physical source coupling in a superposed matter configuration,
Penrose-Diosi `E_G/hbar`, SI normalization, Planck pin, and BMV geometry/cutoff.
