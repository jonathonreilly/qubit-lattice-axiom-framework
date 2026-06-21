# Route Portfolio

## Selected Route: Typed-Edge Cut Certificate

Status: delivered as a narrow no-go.

The current source bank cannot reach the Route-2 E-center readout nodes. The
runner proves that weak scalar, sign, selector, and slot additions fail unless
they include a typed Route-2 readout landing edge.

## Positive Route Left Open

Target one of the equivalent typed readout edges:

```text
su3_R_conn_8_9 -> route2_center_TE_minus_8_9
su3_R_conn_8_9 -> route2_q_E_15_8
su3_R_conn_8_9 -> route2_rho_E_21_4
```

or the two-edge split:

```text
su3_R_conn_8_9 -> scalar_signed_minus_8_9
scalar_signed_minus_8_9 -> route2_center_TE_minus_8_9
```

## Rejected Routes

- Fresh numeric matching to `8/9`: already insufficient without a typed
  landing edge.
- T-side sign-only repair: does not supply E-center magnitude.
- Physical selector shortcut: separate context and still not a Route-2 center
  endpoint ratio.
