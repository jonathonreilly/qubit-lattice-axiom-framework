# Assumptions And Imports

## Allowed Minimal Premises

- Exact source-domain color support: `F_adj = (N_c^2 - 1) / N_c^2 = 8/9` at
  `N_c = 3`.
- Positive-lift Route-2 domain: `rho_E > -6`.
- Granted T-side values for the local reduction: `q_T = 5/6` and `s_TE = -2`.
- Endpoint algebra:

```text
|c_TE| = (5/3) / q_E
q_E = 1 + rho_E/6
```

- Existing quote-derived typed-edge inventory from the source-domain bridge
  runner.
- Exact rational arithmetic.

## Forbidden Proof Inputs

- Observed masses.
- Fitted Yukawa, CKM, or J targets.
- Live endpoint nearest-rational selection.
- Physical connected-trace selector.
- A hidden scalar-to-Route-2 unit normalization.

## New Import Exposed

The block exposes one missing theorem:

```text
unit typecast normalization: nu = 1
```

Equivalently, the current bank must supply one of:

```text
scalar magnitude 8/9 -> Route-2 |c_TE| = 8/9
su3_R_conn_8_9 -> route2_center_TE_minus_8_9
su3_R_conn_8_9 -> route2_q_E_15_8
su3_R_conn_8_9 -> route2_rho_E_21_4
```

Block25 shows that the current parents do not already provide any of these
typed landings.
