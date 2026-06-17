## Summary

Adds a source-side boundary for the quark CP-carrier completion's
small-correction residual.

- proves the shipped fitted `xi_u`, `xi_d` pair is non-perturbative relative to
  the Schur `1-3` base (`101.9x` up-sector, `6.64x` down-sector)
- adds a bounded capped-carrier parent-slice scan showing common caps `R <= 5`
  do not recover the parent `J` target
- updates the parent note to treat the small-correction route as negatively
  closed for the current fit while preserving the bounded numerical-match
  status

## Trace

- Loop pack:
  `.claude/science/physics-loops/quark-cp-small-correction-bound-20260617/HANDOFF.md`
- Trace gate:
  `.claude/science/physics-loops/quark-cp-small-correction-bound-20260617/TRACE_GATE.md`
- Certificate:
  `.claude/science/physics-loops/quark-cp-small-correction-bound-20260617/CLAIM_STATUS_CERTIFICATE.md`

## Honest Status

This is exact-support / bounded-support boundary work. It does not derive
`xi_u`, `xi_d`, the comparator targets, or a framework-native
non-perturbative carrier normalization. It does not claim retained/promoted
status and does not edit audit results.

## Checks

```bash
python3 scripts/frontier_quark_cp_small_correction_boundary.py
python3 scripts/frontier_quark_cp_carrier_completion.py
python3 scripts/cached_runner_output.py scripts/frontier_quark_cp_small_correction_boundary.py --refresh
python3 scripts/cached_runner_output.py scripts/frontier_quark_cp_small_correction_boundary.py --check-only
python3 -m py_compile scripts/frontier_quark_cp_small_correction_boundary.py
git diff --check
```

