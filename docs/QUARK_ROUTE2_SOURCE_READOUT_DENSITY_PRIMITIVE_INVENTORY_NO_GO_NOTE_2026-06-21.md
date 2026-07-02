# Quark Route-2 Source/Readout Density Primitive Inventory No-Go

**Date:** 2026-06-21
**Claim type:** no_go
**Claim scope:** scoped no-go; source-side review packet only
**Status authority:** independent audit lane only. This source note does not set, claim, or predict an audit outcome.
**Actual current-surface status:** scoped no-go; source-side review packet only
**Trace class:** negative_route_pruning
**Reachability to target:** prunes a Route-2 endpoint escape route; does not derive the endpoint triple.
**Primary runner:** [`scripts/frontier_quark_route2_source_readout_density_primitive_inventory_no_go_2026_06_21.py`](../scripts/frontier_quark_route2_source_readout_density_primitive_inventory_no_go_2026_06_21.py)
**Runner cache:** [`logs/runner-cache/frontier_quark_route2_source_readout_density_primitive_inventory_no_go_2026_06_21.txt`](../logs/runner-cache/frontier_quark_route2_source_readout_density_primitive_inventory_no_go_2026_06_21.txt)
**Authority links:** [QUARK_ROUTE2_QE_COVARIANCE_SCHUR_QUADRATIC_NO_GO_NARROW_NOTE_2026-06-14.md](QUARK_ROUTE2_QE_COVARIANCE_SCHUR_QUADRATIC_NO_GO_NARROW_NOTE_2026-06-14.md), [QUARK_ROUTE2_E_CENTER_BLINDNESS_NO_GO_NOTE_2026-06-17.md](QUARK_ROUTE2_E_CENTER_BLINDNESS_NO_GO_NOTE_2026-06-17.md), [QUARK_ROUTE2_E_CENTER_LIFT_DERIVATION_ATTEMPT_BOUNDED_NOTE_2026-06-12.md](QUARK_ROUTE2_E_CENTER_LIFT_DERIVATION_ATTEMPT_BOUNDED_NOTE_2026-06-12.md), [S3_TIME_READOUT_PRIMITIVE_BRIDGE_ASSESSMENT_BOUNDED_NOTE_2026-06-12.md](S3_TIME_READOUT_PRIMITIVE_BRIDGE_ASSESSMENT_BOUNDED_NOTE_2026-06-12.md), [QUARK_ROUTE2_RCONN_TYPED_BRIDGE_DERIVATION_BOUNDED_NOTE_2026-06-12.md](QUARK_ROUTE2_RCONN_TYPED_BRIDGE_DERIVATION_BOUNDED_NOTE_2026-06-12.md), [QUARK_ROUTE2_T_SIDE_ENDPOINT_THEOREM_ATTEMPT_BOUNDED_NOTE_2026-06-12.md](QUARK_ROUTE2_T_SIDE_ENDPOINT_THEOREM_ATTEMPT_BOUNDED_NOTE_2026-06-12.md), [S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md](S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md), [S3_TIME_BILINEAR_TENSOR_PRIMITIVE_NOTE.md](S3_TIME_BILINEAR_TENSOR_PRIMITIVE_NOTE.md)

## Scope

This note tests the next source/readout target for the Route-2 endpoint triple:

```text
(beta_T/alpha_T, alpha_T/alpha_E, beta_E/alpha_E)
  = (-1, -2, 21/4).
```

The tested primitive is an explicit source/readout density rule equivalent to

```text
q_X ~ w_X^{-2}
```

where the current `O_h` finite-star projector weights are

```text
w_E = 1/3,  w_T = 1/2.
```

This is not an audit verdict and does not edit repo-wide authority surfaces.

## Exact Conditional Support

If an inverse-square source/readout density primitive is supplied, the endpoint
arithmetic is exact:

```text
(1/w_E)/(1/w_T) = 3/2
q_E/q_T = (3/2)^2 = 9/4
q_T = 5/6
q_E = 15/8
rho_E = 6(q_E - 1) = 21/4
c_TE = (-2)(5/6)/(15/8) = -8/9.
```

The runner also checks nearby powers. One inverse-density power gives
`q_E=5/4`, `rho_E=3/2`, and `c_TE=-4/3`, so one power is not enough. The
tested natural powers hit the endpoint target only at exponent `-2`.

## Current-Bank Inventory Result

The current named source/readout authority bank does not supply the
inverse-square density primitive. It names the same object as a missing bridge
or open positive route:

- the covariance Schur note identifies the gap as the missing
  inverse-square-of-projector-weight lift;
- the E-center blindness note says a positive repair must supply an E-center
  lift, source-domain rule, or equivalent readout primitive;
- the E-center lift attempt says the current source bank does not contain an
  exact E-channel row computing `beta_E/alpha_E`;
- the readout primitive bridge assessment leaves map selection open;
- the Rconn typed bridge note keeps `F_adj` untyped as a Route-2 readout;
- the T-side note keeps the first two entries as readout-row selector data;
- the theta-to-slice note localizes the target upstream of time transport;
- the bilinear primitive note leaves physical tensor-primitive identification
  open.

The runner quote-checks these anchors and scans for direct closure phrases
such as a supplied `D_X=A_X/w_X` or supplied inverse-square density primitive.

## Typed Reachability

The current typed graph has the same-domain `O_h` value:

```text
w_T/w_E = 3/2
kappa^2 = 9/4.
```

It also has Route-2 endpoint algebra once `q_E=15/8` or `c_TE=-8/9` is
supplied. But it has no typed edge:

```text
O_h projector weights -> source/readout inverse-square density primitive
```

and no edge:

```text
source/readout inverse-square density primitive -> q_E/q_T = 9/4.
```

Adding those explicit missing edges creates the path to `rho_E=21/4`. Without
them, the current graph has no path from `O_h` weights or the `F_adj=8/9`
count to the endpoint E-row value.

## Claim Boundary

This note proves a scoped inventory no-go only. It does not prove impossibility
over future nonlinear tensor observables, future owner-approved conventions,
or future source/readout theorems. It records that the current named bank does
not yet contain the primitive needed to turn the same-domain `9/4` value into
the Route-2 readout covariance.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_source_readout_density_primitive_inventory_no_go_2026_06_21.py
python3 -m py_compile scripts/frontier_quark_route2_source_readout_density_primitive_inventory_no_go_2026_06_21.py
```

Expected result:

```text
PASS=21 FAIL=0 TOTAL=21
```
