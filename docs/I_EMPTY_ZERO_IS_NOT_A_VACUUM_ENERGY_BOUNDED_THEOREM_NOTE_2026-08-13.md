---
claim_id: i_empty_zero_is_not_a_vacuum_energy_bounded_theorem_note_2026-08-13
claim_type: bounded_theorem
claim_scope: "The Record sentence I(empty)=0 is the additive identity of the readout, a count of locks in the empty collection. A putative vacuum energy is a law-level rational E0 attached to the empty history and is not that count: the trial values E0=1 and E0=1/2 are well-defined and unequal to I(empty). Realized-state evaluation is pointwise with no averaging, so a history-independent law-level vacuum number is not a Record readout of the empty collection. The extra object is displayed at E0=1 and is not adopted; it is not identified with r, w, or G_N, and no cosmological claim is made."
upstream_dependencies:
  - minimal_axioms
  - realized_state_primitive_note_2026-06-11
runner: scripts/i_empty_zero_is_not_a_vacuum_energy_2026_08_13.py
---

# I(empty)=0 Is Not A Vacuum Energy

**Date:** 2026-08-13
**Type:** bounded_theorem
**Scope:** exact additive identity of the Record readout versus a law-level
constant attached to the empty history. No cosmological constant is installed.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/i_empty_zero_is_not_a_vacuum_energy_2026_08_13.py`](../scripts/i_empty_zero_is_not_a_vacuum_energy_2026_08_13.py)

## Result Up Front

`I(empty)=0` is a count identity, not a law-level energy.

The current Record wording supplies a finitely additive scalar readout of
pairwise-disjoint record collections and names the empty collection as the
additive identity. That number is the number of locks in the empty collection.
It is not a selectable vacuum energy sitting in every history.

A putative vacuum energy is a different object: a law-level rational `E0`
attached to the empty history, constant rather than a count of locks. The
trial values `E0=1` and `E0=1/2` are well-defined rationals and are not equal
to `I(empty)`. The extra object is displayed at `E0=1` and is not adopted.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: negative_route_pruning
target_claim_id: i_empty_zero_is_not_a_vacuum_energy
target_blocker_text: "I(empty)=0 is a count identity, not a law-level vacuum energy"
source_of_blocker_text: handoff
reachability_to_target: closes
artifact_role: theorem
next_trace_action: "Keep E0 as an extra law-level constant if it is displayed; do not identify it with I(empty), r, w, or G_N, and do not install a cosmological constant."
conditional_surface_status: "exact additive-identity algebra on the empty collection; no vacuum-energy law is derived or adopted"
hypothetical_axiom_status: "no axiom edit; E0 is not adopted as axiom content"
admitted_observation_status: null
claim_type_reason: "The identity I(empty)=0 is the Record additive identity recomputed from empty ∪ empty; unequal trial constants are exact rationals. No cosmological identification is claimed."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

Work with finite collections of pairwise-disjoint records. The current Record
wording in
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)
states that a readout value is determined by record content alone, and that
for any finite collection of pairwise-disjoint records the scalar readout `I`
is additive, with `I(empty)=0`.

Write `empty` for the empty collection. Then `empty ∪ empty = empty`, and
the two copies are pairwise disjoint, so additivity applies.

A putative vacuum energy is a law-level number `E0 ∈ Q` attached to the empty
history: a constant, not a count of locks. Two trial values are used:

- `E0 = 1`
- `E0 = 1/2`

The value `E0 = 0` is also a well-defined rational. Numerical equality of
that one trial with the count `I(empty)` does not make `E0` a Record readout.

## Theorem 1 — I(empty)=0 By The Axiom Sentence

The axiom sentence already states `I(empty)=0`. The same value is the unique
solution of the additivity identity on the empty collection.

Recompute only:

`I(empty ∪ empty) = I(empty) + I(empty)`.

Because `empty ∪ empty = empty`, this is `I(empty) = I(empty) + I(empty)`,
hence `I(empty) = 0` in `Q`.

That is the additive identity of the readout. It is a count of locks in the
empty collection.

## Theorem 2 — Trial Constants Are Not I(empty)

A constant `E0 = 1` is a well-defined rational and is not equal to
`I(empty)`. A constant `E0 = 1/2` is likewise unequal to `0`.

So

`E0 = 1 ≠ I(empty) = 0`,

and

`E0 = 1/2 ≠ I(empty) = 0`.

Both trial values are extra numbers. Neither is the additive identity of `I`.

## Theorem 3 — A History-Independent Law Number Is Not The Empty Readout

The realized-state primitive in
[`REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md`](REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md)
states that derivations may evaluate at the realized state, pointwise, and
that nothing more is supplied: no averaging over alternatives, no typical or
generic claim, and no quoting a number that would differ had another
law-admissible state been realized.

A law-level vacuum number that would be the same in every history is not a
Record readout of the empty collection. That readout is `0`, a count
identity, not a selectable energy. Pointwise evaluation at a realized empty
collection still returns the count identity. Averaging is not used.

## Theorem 4 — Display E0=1 As Extra; Do Not Adopt It

The extra object for a vacuum energy is a law-level constant `E0`,
independent of `I`. Display `E0=1` as extra. Do not adopt it.

This note does not install a cosmological constant. It does not claim cosmology.
The four axioms are unchanged. The displayed constant is not axiom content.

## Theorem 5 — Do Not Identify E0 With r, w, Or G_N

Do not identify `E0` with `r`, `w`, or `G_N`.

Those symbols are already in use as a registered sector dial, a formation
weight, and Newton's constant. The trial constant `E0` is a separate extra
object. This note does not force `r=1/2`.

## Mutation

Let `P1` be the predicate “`I(empty)=1`”. Then `P1` fails: `I(empty)=0`.

Let `P½` be the predicate “`I(empty)` selects `E0=1/2`”. Then `P½` fails:
the empty readout is the count identity `0` and does not select the trial
constant `1/2`.

## Cited Surfaces

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) — Record
  additivity and the sentence `I(empty)=0`.
- [`REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md`](REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md)
  — pointwise evaluation; no averaging over alternatives.
