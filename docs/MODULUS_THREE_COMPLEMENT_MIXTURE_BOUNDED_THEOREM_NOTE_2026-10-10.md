---
claim_id: modulus_three_complement_mixture_bounded_theorem_note_2026-10-10
claim_type: bounded_theorem
claim_scope: "On the proper orbit of (1, 2, 3), every rational linear mixture of the modulus-3 complement line with the three signature kernels whose two-neighbour moments all vanish has complement coefficient zero and equal-height block zero. The mixture is then supported on the opposite signatures (-3, 3) and (3, -3), so it lies in the eighteen. No mixture in this ansatz both cancels those moments and leaves the eighteen. The full bond space is not classified. No scale is selected."
upstream_dependencies:
  - minimal_axioms
  - order_blind_nearest_neighbour_formation_independence_beyond_neighbours_unsoldered_constancy_and_soldered_escape_bounded_theorem_note_2026-09-22
  - single_height_signature_order_blind_kernel_bounded_theorem_note_2026-10-10
  - modulus_three_triple_complement_bounded_theorem_note_2026-10-10
runner: scripts/modulus_three_complement_mixture_2026_10_10.py
---

# A mixture of the modulus-3 complement does not leave the eighteen

**Date:** 2026-10-10

**Type:** bounded_theorem

**Audit:** unset; independent audit remains a separate lane

**Status:** proposed_retained

**Status authority:** independent audit only. This source changes no axiom,
primitive, framework rule, or audit verdict.

**Primary runner:**
[`scripts/modulus_three_complement_mixture_2026_10_10.py`](../scripts/modulus_three_complement_mixture_2026_10_10.py)

**Parents:** the [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md),
[the order-blind formation note](ORDER_BLIND_NEAREST_NEIGHBOUR_FORMATION_INDEPENDENCE_BEYOND_NEIGHBOURS_UNSOLDERED_CONSTANCY_AND_SOLDERED_ESCAPE_BOUNDED_THEOREM_NOTE_2026-09-22.md),
the [single height-signature note](SINGLE_HEIGHT_SIGNATURE_ORDER_BLIND_KERNEL_BOUNDED_THEOREM_NOTE_2026-10-10.md),
and the [modulus-3 complement note](MODULUS_THREE_TRIPLE_COMPLEMENT_BOUNDED_THEOREM_NOTE_2026-10-10.md).

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Inside the joint slice kernel, vanishing two-neighbour moments force the complement coefficient and the equal-height block to zero."
trace_class: negative_route_pruning
target_claim_id: null
target_blocker_text: "Other generic orbits and higher-rank bond spaces are not classified."
source_of_blocker_text: frontier_question
reachability_to_target: prunes
artifact_role: theorem
next_trace_action: "Ask whether order-blindness cuts the normalised soldered bond space on the 48-point chiral pair. Do not repeat the dimension count."
conditional_surface_status: "one proper orbit of (1, 2, 3); rational mixtures in the joint slice kernel of signatures (-3, -3), (-3, 3), and (3, -3); two-neighbour moments"
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
```

## Quoted premises

Lattice: "Physical sites are the points of the cubic lattice `Z^3`, with
nearest-neighbor adjacency, standard translations, and proper cubic
rotations about each site."

Admissibility: "There is one fixed nearest-neighbor admissibility rule,
covariant under lattice translations and proper cubic rotations."

Reading note (2), interpretive: "Read with Record, the distribution
concerns which possibility a forming record locks, conditional on
formation at that site; it does not supply the formation site,
probability, or rate."

The parent normalisation: "with phi_d(a, b) = phi_-d(b, a) and
E_r0[prod_{(d, b) in N} phi_d(., b)] = 1 for every N." The parent
converse is not applied. The parent leaves the sentence "Other generic
orbits and higher-rank bond spaces are not classified."

## Theorem

**Target.** Inside the joint slice kernel on the signatures `(-3, -3)`,
`(-3, 3)`, and `(3, -3)`, decide whether a mixture of the complement
line with the three signature kernels can make every two-neighbour
moment vanish and still lie outside the eighteen.

**Ansatz.** The mixture is a rational linear combination of the
complement line and the three signature kernels. That is the whole
joint slice kernel. A two-neighbour moment is the sum, over the
24-point orbit, of the product of the bond values on two distinct
directions at two right-hand records. Cancellation means every such
moment is zero. A kernel outside this joint slice kernel, including
any fourth signature, is not in the ansatz.

**Conclusion.** Every cancelling mixture has complement coefficient
zero and equal-height block zero. Its support lies on the opposite
signatures `(-3, 3)` and `(3, -3)`. By the single-signature note, that
support lies in the eighteen. No mixture in the ansatz both cancels
the two-neighbour moments and leaves the eighteen.

**Proof.** The runner enumerates the proper rotations, the bond orbits,
and the pair moments as quadratic forms on the ten coefficients. Their
span contains the square of the complement coefficient, so that
coefficient is zero at every common rational zero.

The same span, after that coefficient is set to zero, contains nine
forms in the equal-height coordinates `(e0, e1, e2)` and the opposite
blocks `(p0, p1, p2)` and `(q0, q1, q2)`. Six of them are the rows of
`A p` and `B q`, where

```text
A = [[e0, -e2, -(e1+e2)],
     [e1, e0+e1+e2, e1+e2],
     [e2, -e1, e0+e2]]
B = [[e0+e1+e2, e1, e1+e2],
     [-e2, e0, -(e1+e2)],
     [-e1, e2, e0+e2]]
```

Both determinants equal `(e0+e1)((e0+e2)^2+(e1+e2)^2)`. A sum of two
rational squares vanishes only when both squares do, so the second
factor vanishes only on the line `e0 = e1 = -e2`. Over the rationals
the determinants vanish only on the plane `e0+e1 = 0` or on that line.

The other three forms, with the opposite blocks set to zero, are

```text
M1 = e0^2 - 2 e1 e2 - e2^2
M2 = e0 e1 + (1/2) e1^2 + e1 e2 + (1/2) e2^2
M3 = e0 e2 - (1/2) e1^2 + (1/2) e2^2
```

The identity `e1 M3 - e2 M2 = -(1/2)(e1+e2)(e1^2+e2^2)` forces
`e1 = -e2` or `e1 = e2 = 0`. On `e1 = -e2`, `M1` becomes `e0^2+e2^2`.
On `e1 = e2 = 0`, `M1` becomes `e0^2`. Thus the only rational zero with
both opposite blocks zero is the origin. In particular there is no
solution with nonzero determinant, because a nonzero determinant forces
both opposite blocks to zero and then the equal-height block to zero,
which makes the determinant zero.

On the plane `e0+e1 = 0`, away from the origin, the minor `e0^2+e2^2`
of `A` is nonzero, so both matrices have rank 2. The vector
`(-1, -1, 1)` bases each kernel. Substituting those lines into the
three full quadrics forces `e0 = e2 = 0`, a contradiction.

On the line `e0 = e1 = -e2 = s` with `s` nonzero, every `2 x 2` minor
vanishes and the leading entry is `s`, so both matrices have rank 1.
The kernel is spanned by `(-1, 1, 0)` and `(0, 0, 1)`. Substituting
that kernel into the first two quadrics gives `4 s^2`, which is not
zero.

Every cancelling mixture therefore has complement coefficient zero and
equal-height block zero. It is supported on the two opposite
signatures. The cross moments between those two blocks are not solved
here. They are not needed: that support is already inside the eighteen.

**Obligations.** Proved here: the square of the complement coefficient,
the two determinantal factors, both singular loci, and the resulting
vanishing of the equal-height block. Cited from the single-signature
note, and not re-proved: those two opposite signatures lie in the
eighteen. Cited from the complement note, and not re-proved: the line
used as the first basis vector. The parent converse is not applied.
The strongest missing lemma is an order-blindness cut on another
alphabet. This ansatz does not contain one.

## What this does not do

- It does not select a scale.
- It does not solve the cross moments between the two opposite blocks.
- It does not claim that the full bond space has been classified.
- It does not cut the normalised bond space on the 48-point alphabet.
- It does not constrain a kernel that uses a fourth height signature.
- It does not supply a formation site, probability, or rate.

## Runner

`scripts/modulus_three_complement_mixture_2026_10_10.py` repeats the
ten-coefficient moment span, the factored determinants, and both
singular loci. `TOTAL: PASS=12 FAIL=0`.

## Imports

No formation site, probability, rate, or selected scale is imported.
The proper rotations and the pair moments are enumerated here. The
support of the eighteen is the single-signature note. The complement
line is the coordinate vector of the complement note. The parent
converse is not applied.
