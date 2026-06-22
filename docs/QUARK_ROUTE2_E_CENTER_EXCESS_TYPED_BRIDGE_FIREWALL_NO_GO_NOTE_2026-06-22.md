# Quark Route-2 E-Center Excess Typed-Bridge Firewall No-Go

**Date:** 2026-06-22
**Claim type:** no_go
**Actual current-surface status:** no-go for same-rational E-center excess import
**Trace class:** negative_route_pruning
**Runner:** `scripts/frontier_quark_route2_e_center_excess_typed_bridge_firewall_no_go_2026_06_22.py`

Actual current-surface status: no-go for same-rational E-center excess import.

## Scope

The direct E-center readout target can be written as an excess:

```text
q_E - 1 = 7/8.
```

This block asks whether existing nearby `7/8` constants can be reused as that
Route-2 E-center excess without an additional typed bridge.

This is not an audit verdict. It does not close the parent
[`S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md`](S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md)
row.

## Exact Target Algebra

The Route-2 target chain is:

```text
e_E := q_E - 1 = 7/8
q_E = 1 + e_E = 15/8
rho_E = 6 e_E = 21/4
gamma_T(center)/gamma_E(center) = -2 * (5/6)/(15/8) = -8/9
```

So a theorem proving `e_E = 7/8` in the Route-2 E-center readout slot would
close the E-center part of the endpoint chain, conditional on the already
named T-side candidates. A theorem merely producing the rational number `7/8`
in another context does not supply that slot.

## Firewall Result

The runner classifies candidate same-rational appearances:

| Candidate | Numeric relation | Result |
|---|---|---|
| Route-2 E-center excess | `7/8` | Sufficient only if typed as `q_E - 1`. |
| APBC fourth-power factor | `7/8` | Same rational; not an E-center readout. |
| APBC fourth root | `x^4 = 7/8` | Different algebraic object; using `7/8` as the root is false. |
| Taste weight | `7/18` | Gives `rho_E = 7/3`, not `21/4`. |
| `R_conn = 8/9` | Center-ratio route, not an excess route | Exact only if a typed bridge gives `c_TE=-R_conn`. |
| Generic low-rational reuse | includes `7/8` | Selects target only by naming the target slot. |

The firewall is:

```text
same rational number != same typed Route-2 readout theorem.
```

## Remaining Positive Target

One of these would move the endpoint:

```text
derive e_E = q_E - 1 = 7/8 from a Route-2 E-center readout theorem;
derive c_TE = -8/9 from a typed source-domain bridge;
derive rho_E = 21/4 directly in the restricted readout family.
```

Without one of those typed statements, the `7/8` appearances are context
matches, not proof inputs.

This note does not rule out future E-center theorems or the `R_conn` typed
bridge. It only blocks same-rational reuse as a hidden import.

## Validation

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_e_center_excess_typed_bridge_firewall_no_go_2026_06_22.py
```

Expected result:

```text
TOTAL: PASS=38, FAIL=0
```
