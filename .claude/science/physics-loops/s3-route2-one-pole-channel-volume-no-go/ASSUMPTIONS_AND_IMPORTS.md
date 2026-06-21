# Assumptions And Imports

## Allowed Inputs

- Exact `O_h` channel weights:
  - `w_E=1/3`
  - `w_T=1/2`
  - `w_E/w_T=2/3`
- Granted T-side endpoint value:
  - `q_T=5/6`
- Granted shell ratio used by the endpoint arithmetic:
  - `S_TE=-2`
- Current Route-2 surfaces naming the missing entry:
  - `QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md`
  - `QUARK_ROUTE2_QE_KAPPA_SQUARED_COVARIANCE_SHARPER_NO_GO_NARROW_NOTE_2026-06-10.md`
  - `QUARK_ROUTE2_QE_COVARIANCE_SCHUR_QUADRATIC_NO_GO_NARROW_NOTE_2026-06-14.md`
  - `S3_TIME_BILINEAR_TENSOR_PRIMITIVE_NOTE.md`

## Tested Class

Positive channel-volume cones:

```text
q_X = sum_i a_i w_X^p_i
a_i >= 0
p_i >= -1.
```

This includes polynomial rules and rules with at most one inverse
channel-volume normalization.

## Forbidden Inputs

- No observed quark masses or live endpoint fitting.
- No nearest-rational selector.
- No adopted inverse-square axiom.
- No signed cancellation unless separately derived and policed.
- No claim over all future nonlinear observables.

## Newly Exposed Import

The endpoint needs one of:

- a genuine two-pole inverse-square primitive `p=-2`;
- a derived signed-cancellation mechanism;
- a different E-center/source-readout primitive.
