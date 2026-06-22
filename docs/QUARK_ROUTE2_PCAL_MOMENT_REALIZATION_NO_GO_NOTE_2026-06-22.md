# Quark Route-2 Pcal Moment-Realization No-Go

**Date:** 2026-06-22
**Type:** no-go / finite moment-realization obstruction packet
**Actual current-surface status:** no-go for exact `P_R` slots determining the Route-2 Pcal product instantiation
**Trace class:** negative_route_pruning
**Primary runner:** [`scripts/frontier_quark_route2_pcal_moment_realization_no_go_2026_06_22.py`](../scripts/frontier_quark_route2_pcal_moment_realization_no_go_2026_06_22.py)
**Cached output:** [`outputs/frontier_quark_route2_pcal_moment_realization_no_go_2026_06_22.txt`](../outputs/frontier_quark_route2_pcal_moment_realization_no_go_2026_06_22.txt)

This is not an audit verdict. It does not run audit workers and does not apply
audit outcomes.

## Question

Block100 showed that generic Pcal/Mobius support does not supply the Route-2
product registry. Could the exact finite `P_R` slot surface itself supply the
missing Pcal moment realization?

## Result

No. The exact `P_R` packet supplies a carrier/readout reduction and four
endpoint slots. It does not supply a probability space, record variables,
reference measure, raw `D_A D_B Z` moments, or one-point `D_A Z` moments.

Even if a Route-2 slot is granted as a raw second moment, the connected
cumulant is still underdetermined. On a two-point finite record space, let
`X=Y` take values `+1` and `-1` with mean `m`. Then

```text
E[XY] = 1
E[X]E[Y] = m^2
connected = E[XY] - E[X]E[Y] = 1 - m^2.
```

The same raw second moment `E[XY]=1` therefore realizes multiple connected
selectors:

```text
m = 0   -> connected = 1   -> kappa = 1
m = 1/3 -> connected = 8/9 -> kappa = 0
m = 2/3 -> connected = 5/9 -> kappa = -3
```

The `m=1/3` realization is the desired disconnected product, but selecting it
without a Route-2 one-point theorem is exactly the missing input.

## Boundary

This block does not say a Route-2 moment realization is impossible. It says
the current exact `P_R` finite slot surface does not determine one. A positive
theorem must construct the record variables and reference source measure, not
choose the one-point product after seeing the desired connected selector.

## Missing Primitive

The exact missing primitive is:

```text
Route-2 Pcal moment-realization theorem:

construct a finite Route-2 record probability space, record variables for the
physical E/T readout, and a reference source measure; prove the exact `P_R`
slots are the raw D_A D_B Z moments; prove the one-point moments D_A Z and
D_B Z on that same source; and prove their product is exactly the symmetric
singlet line whose subtraction leaves the connected adjoint readout.
```

No endpoint value is used.

Expected runner result:

```text
TOTAL: PASS=75, FAIL=0
```
