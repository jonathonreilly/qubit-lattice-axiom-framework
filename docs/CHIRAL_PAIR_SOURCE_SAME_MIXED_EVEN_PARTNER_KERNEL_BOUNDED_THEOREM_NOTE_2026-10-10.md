---
claim_id: chiral_pair_source_same_mixed_even_partner_kernel_bounded_theorem_note_2026-10-10
claim_type: bounded_theorem
claim_scope: "On the ordered height pairs (1, 2), (2, 1), and (3, 1), the second even generator plus both swapped-dot generators is the kernel vector with swapped coordinate -2, parallel coordinate -1, oblique coordinate 1, and orthogonal coordinate 2. Its base image has rank 10. The coefficient pairs compress to 17 rows. The monic pivot minor at chirality coefficient 1 is (c - 2)^2, and the monic pivot minor at chirality coefficient 2 is c^3(c - 1). Their gcd is a nonzero constant, so every chirality coefficient has partner rank 10. The other three ordered height pairs are not in this rank-10 count. The ten-kernel coefficient span is not classified. The full soldered bond space is not classified. No scale is selected."
upstream_dependencies:
  - minimal_axioms
  - chiral_pair_even_span_partner_kernel_bounded_theorem_note_2026-10-10
  - chiral_pair_two_parity_excluded_partner_kernel_bounded_theorem_note_2026-10-10
runner: scripts/chiral_pair_source_same_mixed_even_partner_kernel_2026_10_10.py
---

# A source-same mixed vector keeps partner rank 10

**Date:** 2026-10-11

**Type:** bounded_theorem

**Audit:** unset; independent audit remains a separate lane

**Status:** proposed_retained

**Status authority:** independent audit only. This source changes no axiom,
primitive, framework rule, or audit verdict.

**Primary runner:**
[`scripts/chiral_pair_source_same_mixed_even_partner_kernel_2026_10_10.py`](../scripts/chiral_pair_source_same_mixed_even_partner_kernel_2026_10_10.py)

**Parents:** the [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md),
[the even span](CHIRAL_PAIR_EVEN_SPAN_PARTNER_KERNEL_BOUNDED_THEOREM_NOTE_2026-10-10.md),
and [the two ratio spans](CHIRAL_PAIR_TWO_PARITY_EXCLUDED_PARTNER_KERNEL_BOUNDED_THEOREM_NOTE_2026-10-10.md).

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "On the three source-same ordered height pairs, the second even generator plus both swapped-dot generators has partner rank 10 at every chirality coefficient."
trace_class: negative_route_pruning
target_claim_id: null
target_blocker_text: "Other generic orbits and higher-rank bond spaces are not classified."
source_of_blocker_text: frontier_question
reachability_to_target: prunes
artifact_role: theorem
next_trace_action: "Decide whether every chirality coefficient on the sign product plus both swapped-dot generators has partner rank 10. On the source-same pairs, the second even generator plus both swapped-dot generators has partner rank 10 at every chirality coefficient. Do not claim the ten-kernel coefficient span is settled."
conditional_surface_status: "ordered height pairs (1, 2), (2, 1), and (3, 1); second even generator plus both swapped-dot generators; every chirality coefficient"
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

## Theorem

**Target.** On the source-same ordered height pairs `(1, 2)`, `(2, 1)`,
and `(3, 1)`, decide whether every chirality coefficient on the second
even generator plus both swapped-dot generators has partner rank 10.

**Ansatz.** The second even generator plus the swapped-dot generator of
each ratio span, plus an arbitrary chirality coefficient. On these three
pairs the summed kernel vector has swapped coordinate `-2`, parallel
coordinate `-1`, oblique coordinate `1`, and orthogonal coordinate `2`.
The same coefficients on `(1, 3)`, `(2, 3)`, and `(3, 2)` are not in
this rank-10 count. The ten-kernel coefficient span is not this ansatz.
The full soldered bond space is not classified.

The kernel cross sum on two perpendicular directions is the sum of the
products of the two centre values. This note does not convert that sum
into an alphabet mean.

**Conclusion.** On `(1, 2)`, `(2, 1)`, and `(3, 1)`, every chirality
coefficient, including 0, has partner rank 10. The only ten-kernel
partner is 0.

**Proof.** The runner enumerates the proper rotations and the alphabet
and builds the ten kernels. On each source-same ordered height pair, the
second even generator is the parallel-oblique generator. Added to both
swapped-dot generators, it gives swapped coordinate `-2`, parallel
coordinate `-1`, oblique coordinate `1`, and orthogonal coordinate `2`.
The base image of that vector has rank 10, so the partner kernel at
chirality coefficient 0 is 0. The coefficient pairs compress to 17 rows.
Gaussian elimination at chirality coefficients `1` and `2` selects ten
pivot rows. The monic pivot minor at coefficient `1` is `(c - 2)^2`.
The monic pivot minor at coefficient `2` is `c^3(c - 1)`. Those two
polynomials have no common root, and their running gcd is a nonzero
constant. A constant has no root, so the partner rank stays 10 at every
chirality coefficient.

**Obligations.** Proved here: on the three source-same ordered height
pairs, this mixed vector has partner rank 10 at every chirality
coefficient. Cited from the even-span note, and not re-proved: the name
of the even space. Cited from the ratio-span note, and not re-proved:
the names of the two spans. The strongest missing lemma is whether
every chirality coefficient on the sign product plus both swapped-dot
generators has partner rank 10.

## What this does not do

- It does not select a scale. The mixed vector is a witness.
- It does not give `(1, 3)`, `(2, 3)`, or `(3, 2)` this rank-10 count.
- It does not give every mixed vector partner rank 10.
- It does not give the sign product plus both swapped-dot generators this count.
- It does not claim that the ten-kernel coefficient span is settled.
- It does not claim that the full soldered bond space is classified.
- It does not apply the order-blind converse.
- It does not convert a kernel cross sum into an alphabet mean.
- It does not repeat the bond-space dimension count.
- It does not return to the modulus-3 triple.
- It does not supply a formation site, probability, or rate.

## Runner

`scripts/chiral_pair_source_same_mixed_even_partner_kernel_2026_10_10.py`
checks the constant pivot-minor gcd. `TOTAL: PASS=16 FAIL=0`.

## Imports

No formation site, probability, rate, or selected scale is imported.
The proper rotations, the stacked partner kernel, and the pivot-minor
gcd are enumerated here. The even-span note names the even space. The
ratio-span note names the two spans. The order-blind converse is not
applied.
