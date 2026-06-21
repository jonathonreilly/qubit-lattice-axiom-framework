# Assumptions And Imports

## Minimal Allowed Premises

- The exact Route-2 readout reduction:
  `docs/QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md`.
- The six-arm octahedral star with `O_h` signed-permutation action.
- The exact projector decomposition `A1 (+) E (+) T1` on the six arms.
- The prior same-domain covariance and quadratic no-go packets on current
  `main`.
- The target rationals as comparison targets already named by the exact
  readout map, not as proof inputs.

## Forbidden Inputs

- Observed quark masses or CKM/CP fitted values.
- Nearest-rational selection from live numerical endpoints.
- Any live endpoint selector that fixes `rho_E = 21/4` by fit.
- Treating `lambda = 9/4` as adopted because it equals `kappa^2`.
- Treating a chosen channel metric normalization as canonical without a
  theorem deriving the `E:T1` scalar ratio.

## Newly Exposed Import

The channel-metric route requires an additional primitive:

```text
c_E / c_T = (w_T / w_E)^2 = 9/4.
```

`O_h` invariance, positivity, and Schur block decomposition leave this ratio
free.
