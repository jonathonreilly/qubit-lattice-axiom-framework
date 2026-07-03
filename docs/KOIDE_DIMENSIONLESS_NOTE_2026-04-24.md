# Koide Dimensionless Countermodel No-Go

**Date:** 2026-04-24; narrowed 2026-05-26
**Claim type:** no_go
**Status:** exact countermodel no-go for full dimensionless Koide closure from
the finite two-channel and endpoint algebra alone. This is not a physical
source/readout closure theorem.
**Runner:** `scripts/frontier_koide_dimensionless_objection_closure_review.py`

## Purpose

The prior row mixed useful exact obstruction algebra with broader source-domain
closure language. This repair keeps the exact finite result:

- zero traceless background gives `Q = 2/3`;
- common background does not change `Q`;
- traceless background `z = 1/4` gives `Q = 8/9`;
- opposite traceless background `z = -1/4` gives `Q = 8/15`;
- selected-line endpoint support gives `delta = 2/9`;
- ambient or shifted endpoint source data give countermodels
  `delta = 0`, `1/9`, and `1/3`.

Therefore the finite two-channel plus endpoint algebra does not force full
dimensionless closure. Extra physical source/readout selection would be needed.

The live runner records that boundary with explicit negative closeout labels:

```text
Q_DIMENSIONLESS_OBJECTION_CLOSES_Q=FALSE
DELTA_DIMENSIONLESS_OBJECTION_CLOSES_DELTA=FALSE
FULL_DIMENSIONLESS_OBJECTION_CLOSES_LANE=FALSE
```

The remaining residuals are likewise named explicitly rather than hidden in the
prose:

```text
RESIDUAL_Q=derive_physical_background_source_zero_or_Z_erasure
RESIDUAL_DELTA=derive_selected_line_local_boundary_source_and_based_endpoint
```

## Exact Claim

Let the two-channel source background be

```text
J0 = (s + z, s - z)
```

and define the runner's dimensionless response

```text
Q(s,z) = (1 + y_perp/y_plus)/3
y_plus = 1/(1+s+z)
y_perp = 1/(1+s-z)
```

Then:

```text
Q(0,0) = 2/3
Q(1/5,0) = 2/3
Q(0,1/4) = 8/9
Q(0,-1/4) = 8/15
```

So the exact finite algebra admits countermodels unless a physical law sets
`z = 0`.

For the endpoint channel, with `eta_APS = 2/9`, the runner uses

```text
delta = eta_APS * (1 - spectator) + endpoint_shift
```

and checks:

```text
spectator = 0, endpoint_shift = 0    -> delta = 2/9
spectator = 1, endpoint_shift = 0    -> delta = 0
spectator = 1/2, endpoint_shift = 0  -> delta = 1/9
spectator = 0, endpoint_shift = 1/9  -> delta = 1/3
```

So the exact finite endpoint algebra admits countermodels unless a physical
law selects the line-local endpoint and basepoint.

## Boundary

This row does not claim:

- a derivation of the two-channel physical source carrier;
- a derivation that physical source-free selection sets `z = 0`;
- a derivation of selected-line endpoint source/readout;
- a derivation of the endpoint basepoint;
- charged-lepton scale closure;
- any new axiom or audit verdict.

The row only proves that the finite algebra, by itself, does not force full
dimensionless closure.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_koide_dimensionless_objection_closure_review.py
```
