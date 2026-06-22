# Quark Route-2 Source-Jet Lift No-Go

**Date:** 2026-06-22
**Type:** no-go / finite readout to same-source Hessian lift obstruction packet
**Actual current-surface status:** no-go for the current exact P_R finite readout surface itself proving the same-source E/T source-Hessian premise
**Trace class:** negative_route_pruning
**Primary runner:** [`scripts/frontier_quark_route2_source_jet_lift_no_go_2026_06_22.py`](../scripts/frontier_quark_route2_source_jet_lift_no_go_2026_06_22.py)
**Cached output:** [`outputs/frontier_quark_route2_source_jet_lift_no_go_2026_06_22.txt`](../outputs/frontier_quark_route2_source_jet_lift_no_go_2026_06_22.txt)

This is not an audit verdict. It does not run audit workers and does not apply
audit outcomes.

## Question

Block96 reduced the `kappa=0` connected-cumulant route to a three-premise
typed parity bridge. The first premise is:

```text
the physical Route-2 E/T readout is a same-source E/T source Hessian.
```

Does the current exact Route-2 `K_R -> P_R` finite readout surface itself prove
that premise?

## Result

No. The current exact readout surface is a finite carrier/readout reduction:

```text
K_R -> P_R -> E/T shell-center readout.
```

It gives endpoint carrier columns and a channelwise linear readout

```text
P_R = [[alpha_E, 0, beta_E, 0],
       [0, alpha_T, 0, beta_T]].
```

A connected source Hessian is a two-jet statement about a source-coupled
partition functional:

```text
W[J] = log Z[J]
D_i D_j W = D_i D_j Z - (D_i Z)(D_j Z).
```

The finite `P_R` surface does not provide:

1. source coordinates `J_A` for the Route-2 physical E/T readout;
2. the raw second source moment `D_A D_B Z`;
3. the one-point product `(D_A Z)(D_B Z)`;
4. the identification that the source used by `P_R/E-T` is the same source
   used by the color/singlet decomposition.

This is not a dimension-count nit. Given any candidate connected Hessian value
`h`, there are infinitely many source two-jets with the same connected value:

```text
D^2 Z = h + (D Z)^2.
```

Conversely, if a finite readout value is treated as a raw second moment, the
connected value still depends on the missing one-point product. Thus finite
readout data alone cannot decide whether the symmetric line is disconnected
and cannot type the physical readout as `D^2 log Z`.

## Missing Primitive

The exact missing primitive is:

```text
Route-2 same-source source-jet lift theorem:

construct source coordinates J_A and a partition functional Z[J] for the
physical Route-2 E/T readout; prove the current P_R/E-T outputs are the
connected source Hessian D_A D_B log Z at zero source; and provide the raw
second-moment and one-point-product split needed to type the symmetric line as
pure disconnected and the antisymmetric line as connected adjoint.
```

No endpoint value is used.

Expected runner result:

```text
TOTAL: PASS=63, FAIL=0
```
