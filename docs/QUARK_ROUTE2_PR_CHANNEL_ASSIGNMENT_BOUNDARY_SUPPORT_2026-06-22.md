# Quark Route-2 P_R Channel-Assignment Boundary Support

**Date:** 2026-06-22
**Type:** exact-support / finite `P_R` E/T channel-assignment boundary
**Actual current-surface status:** exact-support for finite `P_R` E/T channel labels; not source-Hessian readout-coupling closure
**Trace class:** upstream_support
**Primary runner:** [`scripts/frontier_quark_route2_pr_channel_assignment_boundary_support_2026_06_22.py`](../scripts/frontier_quark_route2_pr_channel_assignment_boundary_support_2026_06_22.py)
**Cached output:** [`outputs/frontier_quark_route2_pr_channel_assignment_boundary_support_2026_06_22.txt`](../outputs/frontier_quark_route2_pr_channel_assignment_boundary_support_2026_06_22.txt)

This is not an audit verdict. It does not run audit workers and does not apply
audit outcomes.

## Scope

Block123 split the minimal readout-coupling contract into clauses C1-C5. The
current block isolates the finite `P_R` contribution to C3:

```text
C3. channel_assignment:
    the E and T scalar outputs are assigned to the physical Route-2 channels
    before a scalar ratio is formed.
```

The exact readout-map authority already supplies a finite E/T channel
assignment on the restricted carrier class:

```text
E-shell  = (1, 0, 0,   0)
E-center = (1, 0, 1/6, 0)
T-shell  = (0, 1, 0,   0)
T-center = (0, 1, 0, 1/6)
```

and every admissible bright-preserving linear readout has block form:

```text
P_R = [[alpha_E, 0, beta_E, 0],
       [0, alpha_T, 0, beta_T]].
```

That is exact finite channel-label support.

## Boundary

This finite channel assignment is not the full C3 source-Hessian clause and
does not supply C2 or C4.

The same block-diagonal channel assignment permits different coefficient maps:

```text
target-like:
  alpha_E = 1, beta_E = 21/4, alpha_T = -2, beta_T = 2

orientation-only:
  alpha_E = 1, beta_E = 0, alpha_T = -1, beta_T = 0
```

Both preserve the finite E/T row assignment. They give different center-ratio
outputs. Therefore:

```text
finite P_R E/T channel labels
!= same-source source-Hessian readout-coupling theorem.
```

## Result

This block marks one sub-piece as exact support:

```text
finite E/T row labels and disjoint carrier columns are available.
```

The remaining Route-2 readout-coupling work is narrower:

```text
1. prove the Block121 source Hessian is the same source/readout as finite P_R;
2. prove the finite E/T rows are the physical source-Hessian output channels;
3. prove the coefficient normalization fixes mu=1.
```

No endpoint value is used.

Expected runner result:

```text
TOTAL: PASS=66, FAIL=0
```
