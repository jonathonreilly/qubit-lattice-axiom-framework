# S3 Endpoint Axis-Readout Transfer Classification

**Date:** 2026-06-26
**Type:** exact finite classification / transfer obstruction
**Actual current-surface status:** exact-support for a four-slot transfer
classification; no current endpoint closure
**Trace class:** upstream_support with a negative boundary for the current
finite endpoint surface alone
**Primary runner:**
[`scripts/frontier_s3_endpoint_axis_readout_transfer_classification_2026_06_26.py`](../scripts/frontier_s3_endpoint_axis_readout_transfer_classification_2026_06_26.py)
**Cached output:**
[`outputs/frontier_s3_endpoint_axis_readout_transfer_classification_2026_06_26.txt`](../outputs/frontier_s3_endpoint_axis_readout_transfer_classification_2026_06_26.txt)

This is not an audit verdict. It does not run audit workers and does not apply
audit outcomes. It proposes no new framework primitive.

## Question

Block153 proved the abstract support theorem:

```text
normalized S3 three-axis source
+ selected-axis one-vs-two signed readout on the same source
  -> E[X]E[Y] = 1/9
  -> E[XY] = 1
  -> connected value 8/9
  -> kappa = 0.
```

The remaining endpoint question is whether the current finite endpoint surface
already supplies the physical transfer into that abstract source/readout
theorem.

## Four-Slot Surface

The live finite endpoint labels are:

```text
E-shell, E-center, T-shell, T-center.
```

The live carrier/readout reduction is channelwise:

```text
P_R = [[alpha_E, 0, beta_E, 0],
       [0, alpha_T, 0, beta_T]].
```

The currently isolated source-measure family from slot typing plus E/T
symmetry is:

```text
P0(E-shell)  = a
P0(T-shell)  = a
P0(E-center) = b
P0(T-center) = b
a + b = 1/2
0 < a,b < 1/2.
```

This is a four-label shell/center surface, not yet a physical three-axis source.

## Classification Theorem

Let `q` be a total surjective quotient from the four endpoint labels to three
axis labels `{0,1,2}`. Require the push-forward of the E/T-symmetric law above
to be the normalized S3 axis law:

```text
q_* P0(axis 0) = q_* P0(axis 1) = q_* P0(axis 2) = 1/3.
```

Then exactly the following finite transfers are possible:

1. `q` identifies the two shell labels and leaves the two center labels as
   singletons. The required source weights are:

   ```text
   a = 1/6, b = 1/3.
   ```

2. `q` identifies the two center labels and leaves the two shell labels as
   singletons. The required source weights are:

   ```text
   a = 1/3, b = 1/6.
   ```

No quotient that identifies a mixed shell/center pair works. The uniform
four-slot law `a=b=1/4` also cannot push forward under any total surjective
four-to-three quotient to the uniform three-axis law.

There are twelve labeled witnesses: choose which axis receives the same-type
pair, choose whether the pair is shell or center, and assign the two remaining
opposite-type labels to the two remaining axes.

## Consequence For The Signed Readout

For any one of the twelve finite witnesses above, if a physical endpoint theorem
also identifies the endpoint readouts `X,Y` with the same signed axis variable

```text
chi_mu(axis) = +1 when axis=mu, and -1 otherwise
```

or its sign reverse on the same source, then the Block153 algebra applies
without importing an endpoint value:

```text
E[X] = E[Y] = +/- 1/3
E[X]E[Y] = 1/9
E[XY] = 1
E[XY] - E[X]E[Y] = 8/9
kappa = 0.
```

This is conditional support only. The current endpoint surface does not yet
prove the physical quotient `q`, does not select one of the two non-uniform
source laws, and does not identify `P_R/E-T` readouts with `chi_mu` on the same
source.

## Current Boundary

The current endpoint files supply:

- the four finite endpoint labels;
- the exact carrier/readout reduction;
- the E/T-symmetric one-parameter source-measure family;
- prior no-gos showing that color-marginal, multi-record, and canonical-P0
  transfer shortcuts are not already present.

They do not supply:

- a physical endpoint source space with a total quotient to three S3 axes;
- a theorem selecting `a=1/6,b=1/3` or `a=1/3,b=1/6`;
- a physical reason to pair the two shell labels or the two center labels;
- a same-source readout theorem identifying `X,Y` with `+/- chi_mu`;
- connected-cumulant typing and unit readout calibration on the physical
  endpoint source.

Therefore the current finite endpoint surface reaches a precise transfer
blocker, not endpoint closure.

## Exact Remaining Theorem

The exact remaining theorem target is:

```text
S3 endpoint axis-readout transfer theorem:
derive a physical endpoint source law, a total same-type-pair quotient
q: {E-shell,E-center,T-shell,T-center} -> {0,1,2}, and same-source endpoint
readouts X,Y = +/- chi_mu(q(.)) with connected-subtraction typing and unit
calibration, using no endpoint value as an input.
```

This theorem would use the finite classification above and the Block153
signed-axis support theorem. Without it, the endpoint bridge remains open.

## Validation

Run:

```bash
python3 -m py_compile scripts/frontier_s3_endpoint_axis_readout_transfer_classification_2026_06_26.py
PYTHONPATH=scripts python3 scripts/frontier_s3_endpoint_axis_readout_transfer_classification_2026_06_26.py
```

Expected result:

```text
TOTAL: PASS=489, FAIL=0
```
