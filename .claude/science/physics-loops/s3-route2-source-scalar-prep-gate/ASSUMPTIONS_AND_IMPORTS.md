# Assumptions And Imports

## Allowed Current-Surface Inputs

- Exact restricted Route-2 carrier columns from
  `docs/QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md`.
- Restricted bright readout form
  `P_R = [[alpha_E,0,beta_E,0],[0,alpha_T,0,beta_T]]`.
- Endpoint algebra
  `q_E = 1 + (beta_E/alpha_E)/6` and
  `q_T = 1 + (beta_T/alpha_T)/6`.
- Conditional time family
  `Xi_P(t;c) = (P_R c) tensor V_R(t)`.
- Schur-frame weights `w_E=1/3`, `w_T=1/2` used only to test the candidate
  inverse channel scaling.

## Forbidden Inputs

- Observed quark masses or fitted Yukawa entries.
- Nearest-rational selection from live endpoint data.
- Treating a channel normalization as a center-excess theorem.
- Treating this branch-local packet as an audit verdict.

## New Import Exposed

A source-preparation theorem that moves the E-center endpoint must be
center-excess nonuniform:

```text
S = diag(a_E, a_T, b_E, b_T)
```

and must derive the ratio

```text
rho_E * (b_E/a_E) = 21/4.
```
