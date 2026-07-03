# Record Function Finite Sector Algebra

**Date:** 2026-06-05
**Claim type:** positive_theorem
**Status authority:** independent audit lane only; effective status is
pipeline-derived after audit. This note does not set, predict, or propose an
audit outcome.
**Primary runner:** [`scripts/record_function_finite_sector_algebra_2026_06_05.py`](../scripts/record_function_finite_sector_algebra_2026_06_05.py)
(sympy + finite subset checks; **SCORECARD 21 PASS / 0 FAIL**).
**Cached log:** [`logs/runner-cache/record_function_finite_sector_algebra_2026_06_05.txt`](../logs/runner-cache/record_function_finite_sector_algebra_2026_06_05.txt).

## Scope and honesty

This note isolates the algebra that follows from the 2026-06-05 **Record**
axiom:

```text
Given a supplied finite record-sector decomposition, scalar readout is
finitely additive over disjoint records.
```

The resulting object is a finite **record function**: a sector readout vector.
This is useful because many downstream claims need ratios, normalized
coordinates, coarse-grainings, and stability coordinates. But this note does
not turn record readout into Born probability, dynamics, source/action,
occupancy, or a value selector.

## Theorem

Let a supplied finite record decomposition have sectors

```text
R_0, ..., R_(n-1)
```

and scalar readouts

```text
v_i = I(R_i).
```

Then the record function is the finite vector

```text
v = (v_0, ..., v_(n-1)).
```

For any finite union of sectors `A`, with indicator vector `chi_A`,

```text
I(A) = chi_A . v.
```

If `A` and `B` are disjoint, then

```text
I(A union B) = I(A) + I(B).
```

The runner verifies this for all `81` ordered disjoint pairs of subsets of a
four-sector test decomposition.

## Coarse-graining

A finite coarse-graining is an incidence matrix `C`. The coarsened record
function is

```text
w = C v.
```

If the coarse-graining is a partition of the original sectors, each original
sector appears in exactly one coarse block, equivalently

```text
1_m C = 1_n.
```

Then total readout is preserved:

```text
sum_j w_j = sum_i v_i.
```

Repeated coarse-graining composes associatively:

```text
D(Cv) = (DC)v.
```

This is the finite algebraic content that Record makes available for later
dynamics. It is not yet a probability calculus.

## Ratios and normalized coordinates

For a two-sector record function

```text
v = (u, d),     u+d != 0,
```

the normalized coordinates

```text
p_0 = u/(u+d),     p_1 = d/(u+d)
```

sum to one and are invariant under global readout scaling. The raw ratio

```text
rho = d/u
```

is also scale-invariant. These are structural readout coordinates. Calling
them probabilities requires a separate normalization/Born gate.

Finite additivity leaves the normalized coordinate arbitrary: for any supplied
`p` in `(0,1)`, choosing

```text
d = p u / (1-p)
```

gives `d/(u+d)=p`. Thus Record alone cannot select a value.

## Generation-dial specialization

For the generation two-sector readout, the sector powers are

```text
singlet readout = a^2,
doublet readout = 2|b|^2.
```

With

```text
r = |b|^2/a^2,
rho = doublet/singlet,
```

we have

```text
rho = 2r.
```

The exact dial coordinate is therefore

```text
s = log2(rho) = log2(2r).
```

For the named `Q` endpoint entries, the finite generation readout packet uses
the standard three-slot Koide structural coordinate attached to the supplied
`C3`/`K`-real generation context:

```text
Q = (sum_k lambda_k^2) / (sum_k lambda_k)^2.
```

Here the `K`/CPT-real `C3`-equivariant square-root readout has the finite
character form

```text
lambda_k = a + 2|b| cos(theta + 2 pi k/3),     k=0,1,2.
```

The `C3` character sums give, exactly,

```text
sum_k lambda_k     = 3a,
sum_k lambda_k^2   = 3a^2 + 6|b|^2.
```

Therefore this packet derives the displayed generation-coordinate formula
before substituting endpoints:

```text
Q = (3a^2 + 6|b|^2)/(3a)^2 = 1/3 + (2/3)r.
```

Equivalently, in the two-block record-function notation above,

```text
Q = (singlet readout + doublet readout)/(3 singlet readout).
```

This is a structural coordinate on the supplied generation readout, not a
probability, dynamics, occupancy selector, or measured-mass assertion.

The named endpoints are:

```text
rho=1 -> s=0 -> r=1/2 -> Q=2/3
rho=2 -> s=1 -> r=1   -> Q=1
```

The runner verifies these identities exactly and verifies that `rho` remains a
free readout ratio until a weighting or dynamics gate is supplied.

## What this unlocks

This is the small reusable row that the dynamics push needs:

1. Record gives finite additive sector vectors.
2. Coarse-grainings are incidence matrices.
3. Ratios and normalized coordinates are valid structural coordinates.
4. No probability or dynamics is implied.

Downstream dynamics claims can now cite this instead of smuggling in a hidden
Born or source/action premise. It also gives a clean basis for rewriting older
observable-principle rows: if a row only needs finite additive sector readout,
it can depend on record-function algebra; if it needs weights, probability, or
time evolution, that extra gate must be named.

## Runner coverage

The runner verifies:

- finite additivity over all ordered disjoint subset pairs in a four-sector
  model;
- singleton decomposition and empty-union readout;
- coarse-graining by incidence matrix;
- total preservation for partition coarse-grainings;
- associative composition of coarse-grainings;
- scale invariance of normalized coordinates and ratios;
- arbitrariness of two-sector normalized coordinates under Record alone;
- generation specialization `rho=2r`, `s=log2(rho)`, and the two named
  endpoints;
- the finite `C3`/`K`-real power-sum definition of the generation `Q`
  coordinate, deriving `Q = 1/3 + (2/3)r` before endpoint substitution.

## Net

Record-function algebra is a retained-candidate scaffold, not a physical
selection principle. It is exactly the algebra needed to talk cleanly about
record-sector dials and dynamics without overclaiming probability or value
selection.
