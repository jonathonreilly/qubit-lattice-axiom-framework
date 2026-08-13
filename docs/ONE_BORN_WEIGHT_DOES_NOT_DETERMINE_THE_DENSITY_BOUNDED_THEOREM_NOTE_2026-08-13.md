---
claim_id: one_born_weight_does_not_determine_the_density_bounded_theorem_note_2026-08-13
claim_type: bounded_theorem
claim_scope: "At one M_2(C) site, a single Born weight Tr(ρP) on one fixed rank-one projector does not recover the density matrix. An exact two-density witness with a=3/5 shares that weight and differs in the off-diagonal. Reconstructing a state needs the full density or enough independent weights. A Record lock of a P-outcome is not either density, and an Admissibility distribution over possibilities is not a density matrix without an identification. The note does not claim the Born form is false, does not replace the 2026-08-09 low-arity uniqueness theorem, and does not adopt ρ as axiom content."
upstream_dependencies:
  - minimal_axioms
  - born_form_from_binary_ternary_scaled_projector_frame_lift_bounded_theorem_note_2026-08-09
runner: scripts/one_born_weight_does_not_determine_the_density_2026_08_13.py
---

# One Born Weight Does Not Determine The Density

**Date:** 2026-08-13
**Type:** bounded_theorem
**Scope:** exact one-site finite-dimensional algebra on one projector and two
explicit densities. No frame-function uniqueness argument is launched.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/one_born_weight_does_not_determine_the_density_2026_08_13.py`](../scripts/one_born_weight_does_not_determine_the_density_2026_08_13.py)

## Result Up Front

A single number `Tr(ρ P)` does not pick `ρ`.

On `H=C^2`, the rank-one projector `P=diag(1,0)` returns only the `(0,0)`
entry of a density. Two distinct positive trace-one operators share the value
`3/5` and differ by a nonzero off-diagonal. Therefore a predicate
“`Tr(ρ P)` recovers `ρ`” fails on that pair.

This is independent of which projector is later selected as a menu member and
independent of any update map on a declared resolution of the identity. The
August 9 parent already gives uniqueness after a menu-independent grading on
every binary and ternary scaled-projector menu. That parent is left in place.
The present block only displays that one weight on one projector is not that
input.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: negative_route_pruning
target_claim_id: one_born_weight_does_not_determine_the_density
target_blocker_text: "a single number Tr(ρP) does not pick ρ"
source_of_blocker_text: handoff
reachability_to_target: closes
artifact_role: theorem
campaign_native_target_reachability: advances
next_trace_action: "Keep the extra reconstruction object as the full density or enough independent weights; do not treat one lock or one weight as ρ."
conditional_surface_status: "exact two-density witness on one projector; uniqueness on a full low-arity menu family remains the August 9 parent"
hypothetical_axiom_status: "no axiom edit; density is not adopted as axiom content"
admitted_observation_status: null
claim_type_reason: "The two-density witness is exact finite algebra; it does not derive a physical identification of Admissibility with a density matrix."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

Work at one site, with `H=C^2`. Fix the rank-one projector

`P = diag(1, 0)`.

A density has the Hermitian trace-one form

`ρ = [[a, c], [c̄, 1−a]]`

with `a` rational, `0 ≤ a ≤ 1`, and `|c|² ≤ a(1−a)`. The last inequality is
the principal-minor form of positive semidefiniteness.

Direct multiplication gives

`Tr(ρ P) = a`.

The extra object for a state is the full density (or enough independent weights).
One diagonal entry does not determine the off-diagonal.

## Theorem 1 — Two Densities, One Weight

Take `a = 3/5`. Display the two-density witness

- `ρ0 = diag(3/5, 2/5)`, off-diagonal `0`. Then `|0|² = 0 ≤ 6/25`, so `ρ0`
  is positive semidefinite. Its principal minors are `3/5 > 0` and
  `det(ρ0) = 6/25 ≥ 0`.
- `ρ1 = [[3/5, 1/5], [1/5, 2/5]]`. Then `|1/5|² = 1/25 ≤ 6/25`, so `ρ1` is
  positive semidefinite. Its principal minors are `3/5 > 0` and
  `det(ρ1) = (3/5)(2/5) − 1/25 = 6/25 − 1/25 = 1/5 > 0`.

Both are Hermitian and have trace one. Therefore both are densities. The
Born weights on the fixed projector agree and the matrices do not:

`Tr(ρ0 P) = Tr(ρ1 P) = 3/5`, and `ρ0 ≠ ρ1` (off-diagonal).

## Theorem 2 — One Weight Does Not Recover The Density

A single Born weight on one projector does not recover `ρ`.

Any map that sends the number `Tr(ρ P)` to a unique density fails on
`{ρ0, ρ1}`: both inputs produce `3/5`, and the outputs differ. Recovering a
state on this algebra requires the full density matrix or a list of
independent weights large enough to fix the remaining Hermitian parameters.
That reconstruction statement is not an axiom change.

## Theorem 3 — A Lock And A Distribution Are The Wrong Types

The current Record wording in
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)
states that a record locks exactly one admissible local possibility, and that
for any finite collection of pairwise-disjoint records the scalar readout `I`
is additive with `I(empty)=0`. In that wording, a lock is one admissible
possibility; `I` is a count.

A lock of a P-outcome is not `ρ0` or `ρ1`. The locked object is one
admissible possibility. The two displayed densities are candidate operators
used to form Born weights. They are not that locked possibility.

The current Admissibility wording states that for each site the probability
distribution over the possibilities is determined by, and varies with, the
nearest-neighbor conditions, and that the distribution is a probability
measure on the local possibility domain. A distribution over possibilities is not a density matrix without an identification.
This note supplies no such identification.

## Theorem 4 — Born, August 9, And The Axiom Surface Stay Put

This note does not claim the Born form is false. The witness uses the Born
weight `Tr(ρ P)` as the evaluation map and shows only that one such number
underdetermines `ρ`.

This note does not replace
[`BORN_FORM_FROM_BINARY_TERNARY_SCALED_PROJECTOR_FRAME_LIFT_BOUNDED_THEOREM_NOTE_2026-08-09.md`](BORN_FORM_FROM_BINARY_TERNARY_SCALED_PROJECTOR_FRAME_LIFT_BOUNDED_THEOREM_NOTE_2026-08-09.md).
That parent still supplies uniqueness of a density after a menu-independent
grading on every binary and ternary scaled-projector menu. The present
hypothesis is one weight on one projector, which is a strictly smaller input.

This note does not adopt `ρ` as axiom content. The four axioms are unchanged.
The two-density witness is displayed only as finite algebra on supplied
matrices.

## Theorem 5 — No Half-Trace Specialization And No Frame Relaunch

The witness uses `a = 3/5`, not `1/2`. This note does not force `r=1/2`.

This note does not launch a frame-function uniqueness on all projectors.
Gleason and the August 9 low-arity lift already live elsewhere. Their
hypotheses are a nonnegative normalized frame function, or a menu-independent
grading on every binary and ternary scaled menu. One number `Tr(ρ P)` is not
that input, and this block does not re-prove those theorems.

## Mutation

Let `R` be the predicate “`Tr(ρ P)` recovers `ρ`” on a finite family of
densities: `R` holds when each Born weight on the fixed `P` is produced by
exactly one member of the family. Then `R` fails on `{ρ0, ρ1}`.

## Cited Surfaces

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) — Record lock
  and count; Admissibility distribution on the local possibility domain.
- [`BORN_FORM_FROM_BINARY_TERNARY_SCALED_PROJECTOR_FRAME_LIFT_BOUNDED_THEOREM_NOTE_2026-08-09.md`](BORN_FORM_FROM_BINARY_TERNARY_SCALED_PROJECTOR_FRAME_LIFT_BOUNDED_THEOREM_NOTE_2026-08-09.md)
  — uniqueness after a full low-arity grading; not replaced here.
