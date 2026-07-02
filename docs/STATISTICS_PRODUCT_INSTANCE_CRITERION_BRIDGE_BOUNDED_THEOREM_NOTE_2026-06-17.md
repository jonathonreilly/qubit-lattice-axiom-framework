# Statistics Product-Instance Criterion Bridge

**Date:** 2026-06-17
**Type:** bounded_theorem
**Claim type:** bounded_theorem (source-side product-instance criterion bridge; no physical repeated-registration law)
**Status:** source-side exact support; independent audit required before any
downstream status change.
**Status authority:** independent audit lane. This source note does not set,
predict, promote, or demote any audit outcome and does not edit audit-owned
registry, ledger, queue, or publication-status surfaces.
**Primary runner:**
[`scripts/frontier_statistics_product_instance_criterion_bridge_2026_06_17.py`](../scripts/frontier_statistics_product_instance_criterion_bridge_2026_06_17.py)
**Runner cache:**
[`logs/runner-cache/frontier_statistics_product_instance_criterion_bridge_2026_06_17.txt`](../logs/runner-cache/frontier_statistics_product_instance_criterion_bridge_2026_06_17.txt)

## Boundary

This bridge proves a finite algebraic recognition criterion for a supplied
two-registration product instance on the `M_2(C)` effect surface. It does not
derive the physical reason repeated records should satisfy that criterion. In
particular, it does not derive physical independence, iid repetition,
record-stack stationarity, a measurement instrument, R-D, an occupancy cell, or
any durability-to-weight coupling.

The useful repair is narrower: a downstream note no longer has to say
"product form" as an uninspected import. If a repeated-registration joint state
is supplied, this note gives an exact product-effect criterion which forces it
to be `sigma tensor sigma`; if only the registered two-outcome quotient is
used, the note also isolates the weaker quotient factorization that must be
supplied or derived elsewhere.

## Setup

Let `sigma` be a one-copy density matrix on `M_2(C)` with Bloch coordinates

```text
sigma = (I + s_x X + s_y Y + s_z Z)/2.
```

Let `rho` be a two-registration density matrix on `M_2(C) tensor M_2(C)`.
Assume its two one-copy marginals are both `sigma`. In the Pauli tensor basis
this means

```text
rho = 1/4 ( I tensor I
          + sum_a s_a tau_a tensor I
          + sum_b s_b I tensor tau_b
          + sum_{a,b} T_ab tau_a tensor tau_b ),
```

where `a,b in {x,y,z}` and `tau_a` are the Pauli matrices.

For each Pauli direction, define the positive shifted effect

```text
E_a = (I + tau_a)/2.
```

The set `{I, E_x, E_y, E_z}` spans the Hermitian one-copy operator space, so
product-effect expectations on this set separate two-copy density matrices.

## Theorem

### P1 - product-effect criterion forces product state [checked]

If the marginals of `rho` are both `sigma` and

```text
Tr(rho (E_a tensor E_b)) = Tr(sigma E_a) Tr(sigma E_b)
```

for all `a,b in {x,y,z}`, then `T_ab = s_a s_b` for every pair. Substituting
those nine equalities into the Pauli tensor expansion gives

```text
rho = sigma tensor sigma.
```

Equivalently, the connected product-effect cumulants

```text
C_ab = Tr(rho (E_a tensor E_b)) - Tr(sigma E_a) Tr(sigma E_b)
```

all vanish if and only if the supplied same-marginal joint state is the product
state. This is an exact finite-dimensional algebra statement, not a physical
production law.

### P2 - product state implies the registered quotient factorization [checked]

For any two-outcome registered partition `{P_s, P_d}`, the product state gives

```text
m(j,k) = Tr((sigma tensor sigma)(P_j tensor P_k))
       = Tr(sigma P_j) Tr(sigma P_k)
       = p_j p_k.
```

Thus a supplied joint state passing P1 is a sufficient witness for the
outcome-level premise used by the statistics atom. This direction is useful,
but it is intentionally overstrong: the quotient premise only needs the four
registered weights to factor.

### P3 - quotient factorization is the exact weaker premise [checked]

On a supplied two-outcome quotient, write

```text
C_jk = m(j,k) - p_j p_k,  j,k in {s,d}.
```

Then `C_jk=0` for the four quotient cells is exactly the
outcome-factorization premise. It is a finite registered-weight statement and
does not require a full product-state representation. This is the criterion
consumed by
`STATISTICS_ATOM_REDUCES_TO_PRODUCT_FORM_ON_RETAINED_GLEASON_SURFACE_BOUNDED_NOTE_2026-06-12.md`
through the product-to-outcome weakening theorem.

### P4 - same marginals do not suffice [checked]

The diagonal correlated witness

```text
rho_corr = p (|0><0| tensor |0><0|)
         + (1-p) (|1><1| tensor |1><1|)
```

has the same one-copy marginal `diag(p,1-p)` on both copies. But the mixed cell
has

```text
m(0,1) = 0
```

whereas the product quotient would require `p(1-p)`. The same-marginal
condition is therefore insufficient. The product-instance or quotient
factorization criterion is load-bearing.

## Consequence

This bridge splits the remaining statistics-atom input into two explicit
levels:

- full product-instance witness: a same-marginal two-copy state passes the
  finite product-effect criterion P1 and is thereby `sigma tensor sigma`;
- weaker quotient premise: the registered two-outcome weights satisfy
  `m(j,k)=p_j p_k`, which is all the agreement-conditioned flow consumes.

Neither level is derived here as a physical repeated-registration law. The
bridge only removes ambiguity about what must be checked, supplied, or proven
by a future record-stack theorem.

## Does Not

- This does not assert iid/product composition as a physical fact.
- This does not discharge physical independence, record-stack stationarity, or
  the outcome-factorization premise.
- This does not add a new probability axiom or a new framework axiom.
- This does not adopt R-D, select an occupancy cell, or fix `r`.
- This does not promote, demote, or set the status of any downstream row.
- This does not require future work to use a full product state when the
  weaker registered quotient factorization is enough.

## Dependencies

- [`GLEASON_ON_QUBIT_LATTICE_PROJECTION_LATTICE_NARROW_THEOREM_NOTE_2026-05-20.md`](GLEASON_ON_QUBIT_LATTICE_PROJECTION_LATTICE_NARROW_THEOREM_NOTE_2026-05-20.md)
- [`BUSCH_POVM_EFFECT_GLEASON_QUBIT_AUTHORITY_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md`](BUSCH_POVM_EFFECT_GLEASON_QUBIT_AUTHORITY_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md)
- [`PRODUCT_FORM_PREMISE_WEAKENS_TO_OUTCOME_FACTORIZATION_BOUNDED_NOTE_2026-06-12.md`](PRODUCT_FORM_PREMISE_WEAKENS_TO_OUTCOME_FACTORIZATION_BOUNDED_NOTE_2026-06-12.md)
- [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md)

**No-promotion statement:** this note does not promote, demote, or set the
audit status of any dependency, context note, premise, or bridge. The
independent audit lane is the only status authority. References to retained
or retained-bounded dependency surfaces are descriptive references to existing
audit-ledger status, not a status action by this note.
