---
claim_id: born_weight_in_unit_interval_is_not_record_count_i_bounded_theorem_note_2026-08-13
claim_type: bounded_theorem
claim_scope: "At one M_2(C) site, the supplied-grading Born pairing Tr(rho P) takes the exact value 3/5 on the displayed diagonal witness, which lies in (0,1) and is not an integer. A unit-lock Record pattern has I in Z_>=0 with I(empty)=0 and I(one lock)=1, so I is a cardinality. These are different types: a Q-valued pairing versus a Z-valued count. Identifying them requires an extra dictionary that this note displays and does not adopt. The result does not say the Born form is false, does not force r=1/2, and does not adopt L_phys."
upstream_dependencies:
  - minimal_axioms
  - born_form_from_binary_ternary_scaled_projector_frame_lift_bounded_theorem_note_2026-08-09
runner: scripts/born_weight_in_unit_interval_is_not_record_count_i_2026_08_13.py
---

# Born Weight In The Unit Interval Is Not Record Count I

**Date:** 2026-08-13
**Type:** bounded_theorem
**Scope:** exact one-site type comparison of a supplied-grading Born pairing
with a unit-lock Record count.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/born_weight_in_unit_interval_is_not_record_count_i_2026_08_13.py`](../scripts/born_weight_in_unit_interval_is_not_record_count_i_2026_08_13.py)

## Result Up Front

Take the exact one-site matrices

`P = diag(1, 0)`, `rho = diag(3/5, 2/5)`.

Then

`Tr(rho P) = 3/5`.

The value `3/5` lies in the open unit interval and is not an integer. A
unit-lock Record pattern has `I in Z_>=0`, with `I(empty)=0` and
`I(one lock)=1`. Therefore `Tr(rho P)` is not equal to any unit-lock `I`.

The August 9 parent supplies a Born form `Tr(rho E)` on a supplied grading.
The current Record axiom supplies a scalar readout that is additive on
pairwise-disjoint records with `I(empty)=0`. On unit locks that readout is a
cardinality. These are different types: a `Q`-valued pairing versus a
`Z`-valued count. Identifying them requires an extra dictionary. This note
displays the mismatch and does not adopt the dictionary.

The argument uses only exact rational matrix arithmetic and the unit-lock
cardinality convention. It does not use Bessel functions, Haar measure, or
four-dimensional plaquettes. It does not say that the Born form is false. It
does not force `r=1/2` and does not adopt `L_phys`.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The witness Tr(rho P)=3/5 is exact, 3/5 is not an integer, and unit-lock I is a cardinality; the extra identification dictionary is displayed and not adopted."
trace_class: type_separation
target_claim_id: born_weight_in_unit_interval_is_not_record_count_i
target_blocker_text: "a Born weight in (0,1) is not a Record count I"
source_of_blocker_text: handoff
reachability_to_target: closes
artifact_role: theorem
conditional_surface_status: "exact for the displayed witness and the unit-lock cardinality reading; no dictionary is adopted"
hypothetical_axiom_status: "none; no axiom edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

Work at one site with possibility presentation `M_2(C)` from
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md).

Let

`P = diag(1, 0)`, `rho = diag(3/5, 2/5)`.

Both matrices are Hermitian. `P` is a rank-one projector. `rho` is a density
matrix: it is positive semidefinite and `Tr(rho)=1`. The Born pairing on this
pair is the exact rational

`Tr(rho P) = 3/5`.

The parent
[`BORN_FORM_FROM_BINARY_TERNARY_SCALED_PROJECTOR_FRAME_LIFT_BOUNDED_THEOREM_NOTE_2026-08-09.md`](BORN_FORM_FROM_BINARY_TERNARY_SCALED_PROJECTOR_FRAME_LIFT_BOUNDED_THEOREM_NOTE_2026-08-09.md)
supplies, on a supplied grading `w` and an eligible low-arity menu family, a
unique density matrix with

`w(E) = Tr(rho E)`

on the scaled-projector domain. The present note uses only that typed pairing.
It does not re-prove the parent theorem and does not add a grading-selection
law.

The current Record axiom states that records form, that a present record locks
exactly one admissible local possibility, and that

> Only records are readable. A readout value is determined by record content
> alone. For any finite collection of pairwise-disjoint records, scalar readout
> `I` is additive, with `I(empty)=0`.

A **unit-lock Record pattern** is a finite collection of pairwise-disjoint
records in which each lock is assigned the same unit increment. Additivity and
`I(empty)=0` then make `I` a cardinality: `I in Z_>=0`, `I(empty)=0`, and
`I(one lock)=1`. This is a reading of the existing additive readout on unit
locks, not an axiom edit.

## Theorem 1 — The displayed pairing is not an integer

`Tr(rho P) = 3/5`. The integer condition `q in Z` for a rational `q=a/b` in
lowest terms is `b=1`. Here `b=5`, so

`3/5 notin Z`.

A unit-lock `I` takes values in `Z_>=0`. Therefore `Tr(rho P)` is not equal to
any unit-lock `I`. In particular the predicate "`Tr(rho P)` is an integer"
fails on this witness.

## Theorem 2 — The two objects have different types

Quote Record: `I` is additive on pairwise-disjoint records with `I(empty)=0`.
For unit locks it is a cardinality.

Quote August 9: the Born form is `Tr(rho E)` on a supplied grading.

The first object is `Z`-valued. The second is a `Q`-valued pairing of a
density matrix with an effect. They are different types. The displayed values
are

`born(rho, P) = 3/5`, `record_I(0) = 0`, `record_I(1) = 1`.

The predicate "`I(one lock)=3/5`" fails.

## Theorem 3 — Identification requires an extra dictionary

Any identification of `Tr(rho P)` with `I` must supply an extra dictionary
that converts a pairing in `[0,1]` into a count in `Z_>=0`, or that converts
a count into a pairing. The witness `3/5` versus `{0,1,2,...}` is already a
type mismatch, so no such dictionary is implied by the current objects.

This note displays the mismatch. It does not adopt a dictionary, a rounding
rule, a frequency typicality map, or a large-`N` replacement of `I` by
`N Tr(rho P)`.

## Theorem 4 — Independence and non-refutation

The argument does not use Bessel functions, Haar measure, or four-dimensional
plaquettes. Those constructions are outside this block.

The argument does not say that the Born form is false. The parent pairing
`Tr(rho E)` remains the typed Born object on a supplied grading. The claim is
only that this pairing is not the unit-lock Record count.

## Theorem 5 — No forced equal weight and no `L_phys`

The witness uses `rho = diag(3/5, 2/5)`, not a forced equal-weight
`r=1/2` mixture. The note does not force `r=1/2`.

The note does not adopt `L_phys`. No physical length, cell scale, or continuum
path length is introduced.

## Mutation Predicates

The following hostile predicates fail on the displayed objects:

1. "`Tr(rho P)` is an integer" fails, because `born(rho, P)=3/5`.
2. "`I(one lock)=3/5`" fails, because `record_I(1)=1`.

Identity gates for those objects call `born(rho, P)` and `record_I(nlocks)`.

## What Is Not Claimed

- No canonical axiom is edited.
- The parent low-arity uniqueness theorem is not re-proved.
- No physical registration of the displayed `P` or `rho` is claimed.
- Born is not declared false.
- Bessel, Haar, and four-dimensional plaquette constructions are not used.
- `r=1/2` is not forced.
- `L_phys` is not adopted.
- No extra dictionary from pairing to count is adopted.

## Runner Contract

The companion runner computes `Tr(rho P)` by exact `Fraction` matrix
arithmetic, evaluates `record_I` as the unit-lock cardinality, and checks the
two mutation predicates. It reads this note, the August 9 parent, and the
axiom memo. It writes no runner cache.
