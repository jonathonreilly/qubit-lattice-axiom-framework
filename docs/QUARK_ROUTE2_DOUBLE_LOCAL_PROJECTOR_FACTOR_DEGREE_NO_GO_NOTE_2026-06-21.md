# Route-2 Double-Local Projector Factor-Degree No-Go

**Date:** 2026-06-21  
**Claim type:** no-go / exact support boundary  
**Actual current-surface status:** no-go  
**Trace class:** negative_route_pruning  
**Reachability to target:** prunes zero-factor and one-factor source/readout/Schur normalization routes for the open Route-2 endpoint; leaves the exact two-factor primitive open.  
**Primary runner:** [`scripts/frontier_quark_route2_double_local_projector_factor_degree_no_go_2026_06_21.py`](../scripts/frontier_quark_route2_double_local_projector_factor_degree_no_go_2026_06_21.py)  
**Runner cache:** `logs/runner-cache/frontier_quark_route2_double_local_projector_factor_degree_no_go_2026_06_21.txt`

## Boundary

This note does not derive `rho_E = 21/4`, does not close the Route-2 endpoint
triple, does not update an audit verdict, and does not claim a unique exact
`Theta_R -> Lambda_R` theorem.

It sharpens the positive target from the current no-go stack:

```text
q_X proportional to w_X^-2.
```

The result is a factor-degree gate. Zero or one reciprocal local
projector-weight factors cannot close the endpoint. Two reciprocal factors are
necessary and sufficient inside the integer reciprocal-degree grammar. Those
two reciprocal factors remain an open primitive on the current surface.

No observed masses, fitted targets, PDG values, nearest-rational selection, or
live endpoint fit is used.

## Current Inputs

The exact six-arm `O_h` star gives per-arm projector weights

```text
w_A1 = 1/6,   w_E = 1/3,   w_T1 = 1/2,
kappa = w_T1 / w_E = 3/2.
```

The endpoint target after granting the T-side entries is

```text
q_T = 5/6,
q_E = 15/8,
lambda = q_E / q_T = 9/4,
rho_E = 6(q_E - 1) = 21/4,
center T/E = -2 q_T / q_E = -8/9.
```

The current source/readout notes still leave the endpoint coefficient theorem
open:

- `S3_TIME_TENSOR_PRIMITIVE_PROTOTYPE_NOTE.md` defines a staging object under
  named admitted inputs and says it does not derive those inputs.
- `S3_TIME_CONSTRUCTED_SUPPORT_TENSOR_PRIMITIVE_NOTE.md` gives a bounded
  response Jacobian, not an exact tensor observable or exact endpoint
  coefficient theorem.
- `S3_TIME_BILINEAR_TENSOR_PRIMITIVE_NOTE.md` defines the bilinear carrier
  under named inputs and explicitly does not derive a physical tensor primitive.
- `QUARK_ROUTE2_QE_COVARIANCE_SCHUR_QUADRATIC_NO_GO_NARROW_NOTE_2026-06-14.md`
  already shows the inverse-square law is the sharp gap and says no named
  functional supplies it.

## Factor-Degree Gate

Let `d` count reciprocal local projector-weight factors. The induced covariance
is

```text
lambda(d) = (w_T1 / w_E)^d = (3/2)^d.
```

The endpoint consequences are

```text
q_E(d)      = lambda(d) q_T,
rho_E(d)    = 6(q_E(d) - 1),
center T/E  = -2 q_T / q_E(d).
```

The first degrees are:

| reciprocal degree `d` | `lambda(d)` | `q_E(d)` | `rho_E(d)` | center `T/E` |
|---:|---:|---:|---:|---:|
| 0 | `1` | `5/6` | `-1` | `-2` |
| 1 | `3/2` | `5/4` | `3/2` | `-4/3` |
| 2 | `9/4` | `15/8` | `21/4` | `-8/9` |
| 3 | `27/8` | `45/16` | `87/8` | `-16/27` |
| 4 | `81/16` | `135/32` | `615/32` | `-32/81` |

Therefore:

- zero reciprocal factors miss;
- one reciprocal factor misses;
- two reciprocal factors close conditionally;
- within integer reciprocal degrees `|d| <= 6`, `d = 2` is the unique endpoint
  degree.

## Stuck Fan-Out

The first-principles fan-out now has five exact frames:

| frame | reciprocal degree | result |
|---|---:|---|
| raw carrier/readout degree | 0 | misses |
| source-normalized single reciprocal | 1 | misses |
| readout-normalized single reciprocal | 1 | misses |
| Schur-dual single reciprocal | 1 | misses |
| source times readout reciprocal | 2 | closes conditionally |

This prunes the tempting "one normalization is enough" route. A positive proof
must derive two independent reciprocal local projector-weight factors, or an
exactly equivalent nonseparable center-shell covariance primitive.

## Net

The block does not prove the double-local primitive. It makes the remaining
target stricter:

```text
current exact star weights + one reciprocal normalization
  -> lambda = 3/2
  -> rho_E = 3/2
  -> wrong endpoint.
```

The endpoint needs:

```text
source/readout or dual/dual factorization with total reciprocal degree 2
  -> lambda = 9/4
  -> q_E = 15/8
  -> rho_E = 21/4.
```

So the next positive route is not "find a normalization." It is:

> derive two independent reciprocal local projector-weight factors from named
> Route-2 source/readout/tensor structure, or derive an equivalent primitive
> that has the same total factor degree.

## Validation

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_double_local_projector_factor_degree_no_go_2026_06_21.py
```

Expected result:

```text
PASS=14 FAIL=0
```
