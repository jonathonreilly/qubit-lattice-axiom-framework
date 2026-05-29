# Gauge-Vacuum Plaquette Beta=6 Scalar-Value Insufficiency

**Date:** 2026-04-17
**Date of scope repair:** 2026-05-29
**Type:** no_go
**Claim type:** no_go
**Status authority:** independent audit lane only.
**Status:** bounded formal no-go candidate: one scalar value does not determine
an `N >= 3` positive normalized class-sector vector.
**Primary runner:** `scripts/gauge_vacuum_plaquette_scalar_underdetermination_formal.py`

## 2026-05-29 Audit Repair

The audit verdict was `audited_conditional` because the previous row mixed a
valid scalar-underdetermination lemma with broader beta=6 Wilson/Haar kernel,
rim-lift, compression, and compressed-evaluation identifications that were not
retained one-hop authorities. The audit offered this repair route:

```text
narrow this note to the formal scalar-underdetermination lemma only.
```

This revision takes that route. The binding claim below is only the elementary
finite-dimensional statement that a single scalar constraint does not determine
an `N >= 3` positive normalized vector. The beta=6 plaquette language is context
for why the lemma matters; it is not a load-bearing physical/PF closure claim.

## Formal Question

If a retained lane later supplies one scalar value `L(v) = c`, does that scalar
value by itself determine the full positive normalized class-sector vector
`v`?

## Answer

No.

## Formal No-Go

Let

```text
V_n = {v in R^n : v_i > 0, sum_i v_i = 1}
```

with `n >= 3`. Let `L(v) = ell . v` be one nonconstant scalar linear observable
whose level set intersects `V_n` in more than one point. Then fixing one scalar
value

```text
L(v) = c
```

does not determine a unique vector `v in V_n`.

Equivalently, there can be distinct positive normalized vectors

```text
v^(A) != v^(B)
```

with

```text
L(v^(A)) = L(v^(B)),
```

while another statistic or boundary evaluation `M(v)` separates them:

```text
M(v^(A)) != M(v^(B)).
```

This is a formal underdetermination lemma. It does not require a Wilson/Haar
kernel, a rim-lift theorem, a compressed class-function theorem, or a physical
plaquette framework-point evaluation.

## Explicit Witness

In `R^3`, use the normalized positive vectors

```text
v^(A) = (1/5, 3/5, 1/5),
v^(B) = (7/20, 3/10, 7/20).
```

For

```text
L(v) = 0 v_0 + 1 v_1 + 2 v_2,
```

both vectors give

```text
L(v^(A)) = L(v^(B)) = 1.
```

For

```text
M(v) = 0 v_0 + 1 v_1 + 4 v_2,
```

they differ:

```text
M(v^(A)) = 7/5,
M(v^(B)) = 17/10.
```

The null direction

```text
w = (1, -2, 1)
```

satisfies `sum_i w_i = 0` and `L(w) = 0`, but `M(w) != 0`. Therefore a
small positive segment `v^(A) + eps w` stays in the simplex, preserves the
same scalar `L`, and changes `M`.

## Consequence For Beta=6 Context

If a later retained beta=6 construction supplies only one scalar plaquette
value, that one scalar value is not enough to recover a full class-sector
coefficient vector, coefficient list, or boundary function. More information,
such as enough independent evaluations or a separate retained structural
theorem, is needed.

This consequence is only a formal warning. It does not assert that the beta=6
Wilson/Haar kernel, rim lift, compressed evaluation bridge, or physical PF seam
has already been retained.

## What This Closes

- one scalar constraint does not determine an `N >= 3` positive normalized
  vector;
- the displayed witness has equal `L` and unequal `M`;
- a scalar plaquette value alone cannot be treated as full class-sector data.

## What This Does Not Close

- the beta=6 Wilson/Haar kernel;
- any rim-lift or compression theorem;
- any compressed boundary class-function theorem;
- explicit coefficients `rho_(p,q)(6)`;
- explicit plaquette PF data;
- the global sole-axiom PF selector theorem.

## Verification

```bash
python3 scripts/gauge_vacuum_plaquette_scalar_underdetermination_formal.py
# THEOREM PASS=12 SUPPORT=0 FAIL=0
```
