# Handoff

## Summary

This branch repairs the C3 artifact issue for
`sm_anomaly_closure_retained_anchors_decoupled_bounded_theorem_note_2026-06-08`.

The audit ledger said the load-bearing no-`nu_R` theorem is genuine, but the
runner/source scorecard overstated C3: the old printed example only checked
`Tr[Y]`, not the full cubic anomaly family. This branch changes the runner to
verify the family

```text
y_u = 4/3 + t,  y_d = -2/3 - t,  y_e = -2 - t,  y_nu = t
```

at `t=1/2`, checking `SU(3)^2Y = 0`, `Tr[Y] = 0`, and `Tr[Y^3] = 0`.

## Changed Files

- `docs/SM_ANOMALY_CLOSURE_RETAINED_ANCHORS_DECOUPLED_BOUNDED_THEOREM_NOTE_2026-06-08.md`
- `scripts/audit_companion_sm_anomaly_closure_retained_anchors_2026_06_08.py`
- `logs/runner-cache/audit_companion_sm_anomaly_closure_retained_anchors_2026_06_08.txt`

## Boundary

No matter-content derivation is claimed. The minimal RH completion remains an
admitted premise, and the `nu_R` branch remains an admitted/open branch rather
than a selected framework consequence.
