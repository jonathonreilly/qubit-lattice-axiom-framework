# Quark Route-2 Canonical P0 Selector No-Go

**Date:** 2026-06-22
**Type:** no-go / four-slot source-measure selector obstruction
**Actual current-surface status:** no-go for slot typing plus E/T channel symmetry selecting a unique physical four-slot P0
**Trace class:** negative_route_pruning
**Primary runner:** [`scripts/frontier_quark_route2_canonical_p0_selector_no_go_2026_06_22.py`](../scripts/frontier_quark_route2_canonical_p0_selector_no_go_2026_06_22.py)
**Cached output:** [`outputs/frontier_quark_route2_canonical_p0_selector_no_go_2026_06_22.txt`](../outputs/frontier_quark_route2_canonical_p0_selector_no_go_2026_06_22.txt)

This is not an audit verdict. It does not run audit workers and does not apply
audit outcomes.

## Question

Block134 narrowed the remaining primitive to a canonical Route-2 `P0`, physical
center-ratio covariance readout, and same-source Fisher-unit Riesz line. Does
the current four-slot shell/center typing plus E/T channel symmetry already
select that canonical `P0`?

## Result

No. The current slot data leave a one-parameter family of positive normalized
E/T-symmetric references:

```text
P0(E-shell)  = a
P0(T-shell)  = a
P0(E-center) = b
P0(T-center) = b
2a + 2b = 1,
0 < a < 1/2.
```

The uniform reference is only the special case `a=b=1/4`. The shell-heavy and
center-heavy choices

```text
(1/3, 1/6, 1/3, 1/6)
(1/6, 1/3, 1/6, 1/3)
```

also satisfy the same four-slot typing, positivity, normalization, and E/T
channel symmetry.

For the raw shell/center contrast

```text
s(E-shell) = -1
s(E-center) = +1
s(T-shell) = -1
s(T-center) = +1,
```

the raw zero-mean condition selects the uniform reference. But that zero-mean
condition is itself a missing physical source-measure assertion: it says the
unshifted shell/center contrast, rather than its `P0`-centered version, is the
physical RN score.

## Missing Primitive

The exact missing primitive is:

```text
Route-2 shell/center source-measure selector:
prove shell and center have equal source-measure weight on the physical
four-slot Route-2 record surface, or equivalently prove the unshifted
shell/center contrast is the physical zero-mean RN score, and then prove that
score is same-source Fisher-unit Riesz with the Block121 connected scalar.
```

Without that primitive, slot typing plus E/T channel symmetry does not force
`P0`, does not force the raw center-ratio score, and does not force `mu=1`.

No endpoint value is used as an input.

Expected runner result:

```text
TOTAL: PASS=82, FAIL=0
```
