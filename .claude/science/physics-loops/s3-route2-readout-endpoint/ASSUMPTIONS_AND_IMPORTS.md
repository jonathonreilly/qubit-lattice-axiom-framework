# Assumptions And Imports

## Minimal Allowed Premises

- The exact Route-2 readout reduction:
  `docs/QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md`.
- The six-arm `O_h` star and its exact `A1 (+) E (+) T1` decomposition.
- Character arithmetic for symmetric squares and tensor products.
- The target rationals as comparison targets already named by the exact
  readout map, not as proof inputs.

## Forbidden Inputs

- Observed quark masses or fitted CKM/CP data.
- Nearest-rational selection from live numerical endpoints.
- Any endpoint selector that inserts `rho_E = 21/4`.
- Treating the existence of a mixed nonseparable map as a coefficient
  selection theorem.

## Newly Exposed Import

The nonseparable quadratic route needs a new primitive selecting reduced
coefficients inside

```text
Hom_Oh(Sym^2(E (+) T1), E (+) T1).
```

That space has dimension `3`, so symmetry alone leaves the endpoint ratio
underdetermined.
