# Physics Loop Handoff

## Status

`exact-support`; independent audit required before any retained status
movement.

## Claim moved

`gauge_vacuum_plaquette_residual_environment_all_weight_convolution_identification_narrow_theorem_note_2026-05-17`

## Blocker addressed

The conditional audit says the row hard-coded positive `a_(p,q)` symbols
rather than deriving nonvanishing, and upgraded finite/per-weight Schur
algebra into an all-weight boundary class function without convergence,
distribution, or formal-series authority.

## What this PR does

- Adds an I4 bridge deriving strict all-weight Wilson coefficient positivity.
- Adds the formal central character-distribution dictionary for arbitrary
  all-weight diagonal data on finite-character test vectors.
- Updates the parent note to consume I4 without claiming I4 is already
  retained.
- Updates the parent runner to verify the I4 bridge packet and cache.
- Leaves `docs/audit/**` untouched.

## Verification

```bash
python3 -m py_compile scripts/audit_companion_gauge_wilson_su3_all_weight_positive_coefficient_formal_bridge_2026_06_07.py scripts/audit_companion_gauge_vacuum_plaquette_residual_environment_all_weight_convolution_identification.py
PYTHONPATH=scripts python3 scripts/cached_runner_output.py --check-only scripts/audit_companion_gauge_wilson_su3_all_weight_positive_coefficient_formal_bridge_2026_06_07.py
PYTHONPATH=scripts python3 scripts/cached_runner_output.py --check-only scripts/audit_companion_gauge_vacuum_plaquette_residual_environment_all_weight_convolution_identification.py
git diff --check
git diff --name-only -- docs/audit
```

## Loop packet

`.claude/science/physics-loops/gauge-all-weight-formal-bridge-20260607/`
