# Quark Route-2 Source-Readout Unit Calibration No-Go

**Date:** 2026-06-22
**Type:** no-go / source-unit to physical readout-unit calibration obstruction
**Actual current-surface status:** no-go for Block121 equal source-unit weights alone fixing the physical readout coupling `mu=1`
**Trace class:** negative_route_pruning
**Primary runner:** [`scripts/frontier_quark_route2_source_readout_unit_calibration_no_go_2026_06_22.py`](../scripts/frontier_quark_route2_source_readout_unit_calibration_no_go_2026_06_22.py)
**Cached output:** [`outputs/frontier_quark_route2_source_readout_unit_calibration_no_go_2026_06_22.txt`](../outputs/frontier_quark_route2_source_readout_unit_calibration_no_go_2026_06_22.txt)

This is not an audit verdict. It does not run audit workers and does not apply
audit outcomes.

## Question

Block121 fixes equal unit weights inside the endpoint-free source extension:

```text
R_conn = 8 / (8 + 1) = 8/9.
```

Does that internal source normalization also fix the physical readout-unit
calibration:

```text
mu = 1
```

from the internal connected fraction to the Route-2 center-ratio magnitude?

## Result

No. Internal source-unit equality is a statement inside the source domain. The
physical readout-unit calibration is a map from that source domain into the
Route-2 scalar output domain.

With the same internal source jet and the same endpoint orientation sign, the
family

```text
c_TE(mu) = -mu * (8/9)
```

keeps the internal `kappa=0` source algebra unchanged while changing the
physical output magnitude. Generic rational choices such as:

```text
mu = 1/2, 1, 3/2
```

are all endpoint-free. The source algebra alone does not select one of them.

## Missing Primitive

The exact missing primitive is:

```text
Route-2 source-readout unit calibration theorem:

prove that the physical center-ratio readout unit is the same unit as the
Block121 normalized connected source fraction, so the source-to-readout
coupling is mu=1. The proof must come from framework source/readout typing,
not an endpoint target value or a fitted scalar calibration.
```

No endpoint value is used.

Expected runner result:

```text
TOTAL: PASS=55, FAIL=0
```
