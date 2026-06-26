# Quark Route-2 Cubic-Axis Readout Support

**Date:** 2026-06-26
**Type:** exact-support / abstract cubic-axis signed readout theorem
**Actual current-surface status:** exact-support for an abstract `S3`-covariant cubic-axis signed readout theorem; not current-surface Route-2 closure
**Trace class:** upstream_support
**Primary runner:** [`scripts/frontier_quark_route2_cubic_axis_readout_support_2026_06_26.py`](../scripts/frontier_quark_route2_cubic_axis_readout_support_2026_06_26.py)
**Cached output:** [`outputs/frontier_quark_route2_cubic_axis_readout_support_2026_06_26.txt`](../outputs/frontier_quark_route2_cubic_axis_readout_support_2026_06_26.txt)

This is not an audit verdict. It does not run audit workers and does not apply
audit outcomes. It does not propose a new framework primitive.

## Question

Block152 showed that cubic record geometry alone does not force the Route-2
same-source product selector. It also isolated the positive shape:

```text
uniform three-axis record + selected-axis one-vs-two signed collapse
  -> E[X]=E[Y]=+/-1/3, E[XY]=1
  -> kappa=0.
```

This block asks whether that positive shape can be made exact without endpoint
values.

## Exact Axis-Source Theorem

Let the abstract axis-record source be

```text
A = {0, 1, 2}
```

with the unique normalized `S3`-invariant law

```text
P0(a) = 1/3.
```

Given a selected axis `mu in A`, define the signed one-vs-two readout

```text
chi_mu(a) = +1  if a = mu,
          = -1  if a != mu.
```

The sign-reversed readout `-chi_mu` is the same product theorem with the
opposite one-point sign. For either sign choice, set

```text
X = Y = +/- chi_mu.
```

Then the exact moments are:

```text
E[X] = E[Y] = +/- 1/3,
E[X]E[Y] = 1/9,
E[XY] = 1,
E[XY] - E[X]E[Y] = 8/9,
kappa = 0.
```

The construction is `S3`-covariant:

```text
chi_{g mu}(g a) = chi_mu(a).
```

Thus, once a selected axis is supplied, the signed one-vs-two axis readout is
canonical on this abstract axis-record source.

## Relation To Existing Support

The graph-first selector theorem supplies a selected axis on the canonical
cube-shift surface. The graph-first `SU(3)` theorem then supplies the selected
axis, residual swap, and color-rank support on the graph/taste surface.

This Block153 theorem is the exact finite axis-source theorem that Block152
asked for. It turns the positive shape into a reusable support theorem.

## Transfer Boundary

This block still does not close Route-2. The current framework and Route-2
surfaces do not yet prove that the abstract axis-source readout is the
physical `P_R/E-T` readout.

The remaining transfer theorem must supply:

```text
T1. a physical Route-2 source space Omega_R with an axis-record quotient A;
T2. a normalized `S3`-invariant reference law P0 on that quotient;
T3. the graph-first selected axis as the Route-2 selected axis mu;
T4. physical readouts X,Y for P_R/E-T identified with +/- chi_mu on that same
    source;
T5. raw same-source moment E[XY]=1 and connected-subtraction typing;
T6. source/readout unit calibration mu_readout=1;
T7. post-selector orientation sign only after kappa=0.
```

Without those transfer clauses, the theorem remains exact upstream support.
The current `P_R/E-T` finite labels are still carrier/readout labels, not
proved axis-record outcomes. The selected-axis graph/color support still lives
on the graph/taste carrier, not on the Route-2 cubic `l=2` `E/T2`
center-response readout.

No endpoint value is used as an input. This block does not import `rho_E`,
`q_E`, observed quark values, fitted source weights, finite-box comparators,
or endpoint-value reversal.

Expected runner result:

```text
TOTAL: PASS=203, FAIL=0
```
