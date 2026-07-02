# Assumptions And Imports

## Allowed Current-Surface Inputs

- Exact restricted Route-2 readout endpoint algebra from
  `docs/QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md`.
- Schur weights `w_E=1/3`, `w_T=1/2` and inverse-square gap markers from
  `scripts/frontier_quark_route2_qe_covariance_schur_quadratic_no_go_2026_06_14.py`.
- Conditional T-side values `rho_T=-1` and shell T/E `=-2`.
- Exact rational endpoint arithmetic.

## Conditional Premise

The block assumes a one-power readout premise:

```text
q_E/q_T = (w_E/w_T)^-1 = 3/2.
```

With `q_T=5/6`, this gives `q_E=5/4` and `rho_E=3/2`.

## Forbidden Inputs

- Observed quark masses or fitted Yukawa entries.
- Nearest-rational selection from live endpoint data.
- Treating `b_E/a_E=7/2` as already derived.
- Treating this packet as an audit verdict.

## Open Import

The source theorem still missing is:

```text
b_E/a_E = 7/2
```

for an endpoint-normalized source map `S=diag(a_E,a_T,b_E,b_T)` with
`a_T/a_E=1` and `b_T/a_T=1`.
