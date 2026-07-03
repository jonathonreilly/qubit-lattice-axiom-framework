# Product-Form Premise Weakens to Outcome-Level Factorization

**Date:** 2026-06-12
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Status:** source proposal; independent audit required.
**Status authority:** independent audit lane only. This source note sets,
predicts, and estimates no audit verdict and edits no registry.
**Primary runner:** `scripts/frontier_product_form_weakens_to_outcome_factorization_2026_06_12.py`
**Runner cache:** `logs/runner-cache/frontier_product_form_weakens_to_outcome_factorization_2026_06_12.txt`

## Boundary

This note proves only L1-L4 below. The weakened premise is named, not
discharged, and not asserted. R-D stays proposed. No cell is selected. r is
never fixed. The occupancy binary stays open.

It does not consume the unaudited unraveling measured results as authority; it
quotes them only to define scope. It does not adopt R-D, select a cell, fix
`r`, decide the outcome-level independence premise, or turn any frame-level
measurement into a quotient-level law.

## The supplied surface

Use a supplied two-outcome partition on `C^3`,
`P_s = |s><s|` and `P_d = |a><a| + |b><b|`, with `P_s + P_d = I`.
For a one-registration state `sigma`, the registered weights are

```text
p_j = Tr(sigma P_j),  j in {s,d}.
```

For two registrations of the same supplied partition, write the four joint
registered weights as `m(j,k)`. The weakened premise is exactly

```text
m(j,k) = p_j p_k  for j,k in {s,d}.
```

This is an outcome-algebra statement. It refers only to the four registered
weights on the partition and not to any joint state representation. The frame
group for the partition is

```text
G_P = { U unitary on C^3 : [U,P_s] = [U,P_d] = 0 }.
```

## Theorem

### L1 - the chain needs less [checked]

Assume only the four outcome weights satisfy `m(j,k)=p_j p_k`. Condition on the
agreement event `A = {(s,s),(d,d)}`. The conditioned outcome weights are

```text
q_i = m(i,i) / (m(s,s) + m(d,d))
    = p_i^2 / (p_s^2 + p_d^2),  i in {s,d}.
```

For the quotient coordinate `x = p_s/p_d`, the agreement-conditioned coordinate
is

```text
x' = q_s/q_d = (p_s^2/p_d^2) = x^2.
```

Thus the wave-10 reduction chain from retained Born form to product composition
to agreement-conditioned flow uses only outcome-level factorization. No joint
state object enters the algebra.

### L2 - strictly weaker than state-level product form [checked]

Let

```text
X = |s><a| + |a><s|
rho = I_9/9 + (X tensor X)/36
```

on `C^3 tensor C^3`. Since the eigenvalues of `X` are `{-1,0,1}`, the
eigenvalues of `rho` are `1/9 + lambda/36` with
`lambda in {-1,0,1}`. Hence `rho >= 0` and `Tr(rho)=1`.

The partition weights are

```text
m(P_s tensor P_s) = 1/9
m(P_s tensor P_d) = 2/9
m(P_d tensor P_s) = 2/9
m(P_d tensor P_d) = 4/9
```

so they factor exactly with `p_s=1/3` and `p_d=2/3`. But the off-partition
coherence observables `A=B=X` give

```text
<A tensor B> - <A><B> = 1/9 != 0.
```

A product state would factor every tensor-product observable expectation, so
this certified correlation proves the state is not product even though the four
registered partition weights factor exactly. Outcome-level factorization is
therefore strictly weaker than state-level product form.

### L3 - frame invariance [checked]

For every `U in G_P`,

```text
Tr(U sigma U^dag P_j)
  = Tr(sigma U^dag P_j U)
  = Tr(sigma P_j),
```

because `U` commutes with the partition projectors. Therefore the registered
weights `p_j` are invariant under all frame motion internal to the supplied
partition sectors. A non-commuting unitary is not protected by this statement
and can change the registered weights.

This is why the measured frame-failure layer is outside the data consumed by
the weakened premise. Scope-only context from
`UNRAVELED_STEP_LAW_BI_INVARIANT_QUASI_STATIONARITY_SPLIT_BOUNDED_THEOREM_NOTE_2026-06-10.md`:
"The stationarity failure is concentrated in the **bi-frame** — the edge's
independent left/right gauge directions — at this size and horizon." Scope-only
context from
`UNRAVELED_RECORD_TRAJECTORIES_SUPPLY_NONDEGENERATE_STEP_DISTRIBUTION_BOUNDED_THEOREM_NOTE_2026-06-10.md`:
"cross-edge independence and convolution structure are not tested here."
These are unaudited measured results in this use; they scope where tests have
and have not been performed, and they are not load-bearing inputs here.

### L4 - the premise relocated [checked]

The wave-10 product-form premise weakens to:

```text
repeated registrations are OUTCOME-INDEPENDENT on the registered partition.
```

That is a quotient-level statement. It is strictly weaker than iid/product
instances by L2, it is untouched by frame motion internal to the partition by
L3, and it is explicitly untested in the unraveled-step scope quoted above.
The premise is named, not discharged.

## Consequence

The occupancy lane's open residue refines again. The remaining named pieces are
outcome-level independence, whose test surface is the unraveling lane's
many-edge residual; the outcome dictionary in its tri-guise form; and the
durability-to-weight coupling. The weakening matters because a future
measurement or theorem need only address the quotient-level law, not the full
frame-level state structure.

## Does-NOT list

- Does not discharge or assert outcome-level independence.
- Does not consume the unaudited unraveling results as authority.
- Does not adopt R-D.
- Does not select a cell.
- Does not fix `r`.
- Does not decide the occupancy binary.
- Does not promote any in-review companion note.

## Dependencies

- [`GLEASON_ON_QUBIT_LATTICE_PROJECTION_LATTICE_NARROW_THEOREM_NOTE_2026-05-20.md`](GLEASON_ON_QUBIT_LATTICE_PROJECTION_LATTICE_NARROW_THEOREM_NOTE_2026-05-20.md)
- [`BUSCH_POVM_EFFECT_GLEASON_QUBIT_AUTHORITY_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md`](BUSCH_POVM_EFFECT_GLEASON_QUBIT_AUTHORITY_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md)
- [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md)

## Context

`UNRAVELED_STEP_LAW_BI_INVARIANT_QUASI_STATIONARITY_SPLIT_BOUNDED_THEOREM_NOTE_2026-06-10.md`
and
`UNRAVELED_RECORD_TRAJECTORIES_SUPPLY_NONDEGENERATE_STEP_DISTRIBUTION_BOUNDED_THEOREM_NOTE_2026-06-10.md`
are used only for the two scope quotes above. Their measured results are
unaudited in this use and not consumed as theorem authority.

`wave-10 reduction note` and `wave-8a anatomy note` are in-review context; their
chains are re-derived inline in L1-L4 rather than imported. The flow context is
`FLAVOR_R_HALF_IS_THE_RECORDS_FLOW_SEPARATRIX_2026-06-02.md` and
`POST_RECORD_FLOW_THERMAL_STABLE_SETTING_CERTIFICATE_2026-06-06.md`; no status
or additional premise is imported from them here.

**No-promotion statement:** this note does not promote, demote, or set the
audit status of any dependency or context note. The independent audit lane is
the single status authority.
