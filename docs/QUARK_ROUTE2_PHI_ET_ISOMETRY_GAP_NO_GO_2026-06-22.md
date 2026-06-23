# Quark Route-2 Phi_ET Isometry Gap No-Go

**Date:** 2026-06-22
**Type:** no-go / typed source-readout map to unit-isometry obstruction
**Actual current-surface status:** no-go for typed `Phi_ET` existence alone proving source-readout isometry or `mu=1`
**Trace class:** negative_route_pruning
**Primary runner:** [`scripts/frontier_quark_route2_phi_et_isometry_gap_no_go_2026_06_22.py`](../scripts/frontier_quark_route2_phi_et_isometry_gap_no_go_2026_06_22.py)
**Cached output:** [`outputs/frontier_quark_route2_phi_et_isometry_gap_no_go_2026_06_22.txt`](../outputs/frontier_quark_route2_phi_et_isometry_gap_no_go_2026_06_22.txt)

This is not an audit verdict. It does not run audit workers and does not apply
audit outcomes.

## Question

Block127 isolated a sufficient source-readout isometry theorem:

```text
typed Phi_ET + source norm + readout norm + unit preservation => mu=1.
```

Suppose a future construction supplies the typed map `Phi_ET`. Does the typed
map alone force the unit-preserving source/readout isometry, and hence
`mu=1`?

## Result

No. Typing and isometry are separate clauses.

Even after a typed map is supplied,

```text
Phi_ET : Block121 source-Hessian components -> finite P_R E/T output rows,
```

the rescaled family

```text
Phi_ET^(lambda) = lambda Phi_ET
```

preserves:

- source-Hessian domain typing;
- finite `P_R` E/T row codomain typing;
- same-source labels;
- channel assignment;
- the connected/disconnected source subtraction already done upstream.

But it changes the source-to-readout magnitude coupling:

```text
mu(lambda) = lambda,
c_TE(lambda) = -lambda * (8/9).
```

Rational choices such as:

```text
lambda = 1/2, 1, 3/2
```

are endpoint-free. The typed map alone does not select `lambda=1`.

## Distinction From Earlier No-Go Packets

This block does not repeat Block125. Block125 says finite `P_R` row labels do
not construct `Phi_ET`.

This block assumes a typed `Phi_ET` for the sake of the countermodel and shows
that typing alone still does not prove the Block127 isometry clause.

This block also does not repeat Block126. Block126 says equal source-unit
weights alone do not fix physical `mu=1`.

This block says a typed source-readout map alone does not fix physical `mu=1`
unless the source/readout metrics and pullback normalization are proven.

## Missing Primitive

The exact missing primitive is:

```text
Route-2 source/readout metric-isometry theorem:

construct the source metric on the Block121 connected scalar line, construct
the physical readout metric on the finite P_R/E-T center-ratio scalar line,
and prove Phi_ET^* g_readout = g_source on the normalized line. Equivalently,
prove that the typed map has unit operator norm on the scalar line consumed by
Block123 C4.
```

No endpoint value is used.

Expected runner result:

```text
TOTAL: PASS=93, FAIL=0
```
