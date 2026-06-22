# Quark Route-2 Hessian To E-Center Bridge Gate Note

**Date:** 2026-06-21
**Status:** no-go / conditional support boundary.
**Primary runner:** `scripts/frontier_quark_route2_hessian_e_center_bridge_gate_2026_06_21.py`
**Output:** `outputs/frontier_quark_route2_hessian_e_center_bridge_gate_2026_06_21.txt`

## Claim Boundary

The prior Route-2 reductions leave one live positive shape:

```text
C_X proportional to w_X^-2,
w_E = 1/3,
w_T1 = 1/2,
C_E/C_T = 9/4.
```

If the Route-2 readout lift obeyed

```text
q_X proportional to C_X,
```

then the granted T-side value `q_T = 5/6` would force

```text
q_E = (5/6)(9/4) = 15/8,
rho_E = 6(q_E - 1) = 21/4,
c_TE = -8/9.
```

This block asks whether the current bank supplies that Hessian-to-E-center
readout law.

## Result

It does not. The current bank supports the conditional arithmetic above, but
does not select the map from a Hessian coefficient to the Route-2 readout lift.

The obstruction is exact: the same positive Hessian coefficients and the same
T-side calibration admit several simple readout maps. Only one returns the
target:

| Map from Hessian coefficient to lift | T-side calibration | Resulting `q_E` | Resulting `rho_E` |
|---|---:|---:|---:|
| `q_X = (q_T/C_T) C_X` | `q_T=5/6` | `15/8` | `21/4` |
| `q_X = 1 + ((q_T-1)/C_T) C_X` | `q_T=5/6` | `5/8` | `-9/4` |
| `rho_X = (rho_T/C_T) C_X` | `rho_T=-1` | `5/8` | `-9/4` |
| `q_X = q_T (C_T/C_X)` | `q_T=5/6` | `10/27` | `-34/9` |

So the Hessian ratio alone is not the readout theorem. A positive theorem must
prove the specific proportional-lift law `q_X proportional to C_X`, including
its normalization and sign convention, not merely exhibit an inverse-square
Hessian coefficient.

## Current-Surface Firewall

The checked current bank contains nearby but insufficient facts:

- the observable-Hessian route is scalar-only and does not supply the missing
  tensor/time-coupling law;
- the measured E-center calibration is stack-internal comparator evidence and
  leaves exact infinite-volume identification open;
- the readout primitive bridge assessment reaches membership, not unique
  selection of `P_R`;
- the E-center blindness no-go still requires a genuine E-center lift,
  source-domain rule, or equivalent readout primitive.

Therefore this block does not close the parent endpoint triple. It sharpens
the remaining theorem target to:

```text
derive q_X proportional to the selected Route-2 channel Hessian coefficient,
and show that this proportional lift is the E-center readout map.
```

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_hessian_e_center_bridge_gate_2026_06_21.py
```

Expected result:

```text
TOTAL: PASS=26, FAIL=0
```
