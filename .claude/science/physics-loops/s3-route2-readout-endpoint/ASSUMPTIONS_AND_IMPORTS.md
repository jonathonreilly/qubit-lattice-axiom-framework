# Assumptions And Imports

## Minimal allowed premise set for block 01

- Exact conditional s3-time family from
  `S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md`:
  `Xi_P(t; c) = (P_R c) tensor V_R(t)`.
- Exact Route-2 slice backbone from
  `QUARK_ROUTE2_EXACT_TIME_COUPLING_NOTE_2026-04-19.md`.
- Exact restricted readout carrier and endpoint family from
  `QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md`.
- T-side candidates as conditional inputs:
  `beta_T/alpha_T = -1` and `alpha_T/alpha_E = -2`.
- Exact endpoint columns:
  `E-shell=(1,0,0,0)`, `E-center=(1,0,1/6,0)`,
  `T-shell=(0,1,0,0)`, `T-center=(0,1,0,1/6)`.
- Exact rational arithmetic and the existing runner APIs.

## Forbidden proof inputs

- Observed quark masses or fitted Yukawa values.
- CKM/J target minimization.
- Nearest-rational selection from live endpoint data.
- Treating the numerical `F_adj = 8/9` match as a typed Route-2 endpoint
  bridge.
- Treating eta-floor endpoint-fitted coefficients as a first-principles
  physical primitive.
- Any audit verdict update or repo-wide authority weaving.

## Import status

The block does not retire the endpoint-triple import. It narrows the import:
future S3-time consumers must supply a non-blind E-center witness value
equivalent to `q_E = 15/8`, `rho_E = 21/4`, or `c_TE = -8/9`.
