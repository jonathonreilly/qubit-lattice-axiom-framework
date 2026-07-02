# No-Go Ledger

## Block30

Route:

```text
kappa_EW=0 -> endpoint target
```

Verdict: no-go for the route unless W1 is also supplied.

Reason:

- W2-only reaches `su3_R_conn_8_9`.
- W2-only does not type `su3_R_conn_8_9` as
  `route2_center_TE_minus_8_9`.
- W1-only reaches the endpoint target chain from the color scalar but does not
  prove the physical selector.
- W1 and W2 are independent gates.

## Prior Campaign Memory

- E-center-blind constraints leave `rho_E` free.
- E-center-visible endpoint-matrix selectors land the target only when they
  supply a bridge-equivalent statement.
- Scalar-bypass routes constrain support but do not select `P_R`.
- Source-domain typecasts leave a scale or typed-edge gap unless the signed
  center-ratio bridge is supplied.
