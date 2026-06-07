# Physics Loop Handoff

## Status

`exact-support`; independent audit required before retained movement.

## Claim moved

`generation_localization_momentum_corner_delta_ji_protected_narrow_theorem_note_2026-06-06`

## Blocker addressed

The conditional audit says the row needs a retained bridge from the
retained-bounded open-cubic mediator authority to the periodic
translation-invariant plane-wave density-density kernel and normalization.

## What this PR does

- Adds a finite periodic torus plane-wave density-kernel bridge theorem.
- Adds a bridge runner and cache.
- Updates the parent generation note to cite the bridge packet.
- Updates the parent runner to verify bridge path/source/cache freshness.
- Leaves `docs/audit/**` untouched.

## Verification

```bash
python3 -m py_compile scripts/audit_companion_generation_periodic_plane_wave_density_kernel_bridge_2026_06_07.py scripts/generation_localization_corner_protected_delta_runner.py
PYTHONPATH=scripts python3 scripts/cached_runner_output.py --check-only scripts/audit_companion_generation_periodic_plane_wave_density_kernel_bridge_2026_06_07.py
PYTHONPATH=scripts python3 scripts/cached_runner_output.py --check-only scripts/generation_localization_corner_protected_delta_runner.py
git diff --check
git diff --name-only -- docs/audit
```

## Loop packet

`.claude/science/physics-loops/generation-periodic-mediator-bridge-20260607/`
