---
claim_id: chiral_pair_cap_sum_chirality_scale_partner_kernel_bounded_theorem_note_2026-10-10
claim_type: bounded_theorem
claim_scope: "On the 48 signed permutations of (1, 2, 3), the sign product plus both cap generators has scaled coefficient 4. The coefficient pairs of that vector and the chirality cap compress to 17 rows. A running gcd of their 10-by-10 minors is a nonzero constant, so every chirality coefficient has partner rank 10. The swapped-dot vector is not in this all-scale count. The ten-kernel coefficient span is not classified. The full soldered bond space is not classified. No scale is selected."
upstream_dependencies:
  - minimal_axioms
  - chiral_pair_even_span_partner_kernel_bounded_theorem_note_2026-10-10
  - chiral_pair_two_parity_excluded_partner_kernel_bounded_theorem_note_2026-10-10
runner: scripts/chiral_pair_cap_sum_chirality_scale_partner_kernel_2026_10_10.py
---

# The cap sum keeps partner rank 10 at every chirality scale

**Date:** 2026-10-11

**Type:** bounded_theorem

**Audit:** unset; independent audit remains a separate lane

**Status:** proposed_retained

**Status authority:** independent audit only. This source changes no axiom,
primitive, framework rule, or audit verdict.

**Primary runner:**
[`scripts/chiral_pair_cap_sum_chirality_scale_partner_kernel_2026_10_10.py`](../scripts/chiral_pair_cap_sum_chirality_scale_partner_kernel_2026_10_10.py)

**Parents:** the [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md),
[the even span](CHIRAL_PAIR_EVEN_SPAN_PARTNER_KERNEL_BOUNDED_THEOREM_NOTE_2026-10-10.md),
and [the two ratio spans](CHIRAL_PAIR_TWO_PARITY_EXCLUDED_PARTNER_KERNEL_BOUNDED_THEOREM_NOTE_2026-10-10.md).

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Every chirality coefficient on the scaled coefficient 4 vector has partner rank 10."
trace_class: negative_route_pruning
target_claim_id: null
target_blocker_text: "Other generic orbits and higher-rank bond spaces are not classified."
source_of_blocker_text: frontier_question
reachability_to_target: prunes
artifact_role: theorem
next_trace_action: "Decide whether every chirality coefficient on the swapped-dot coefficient 1 vector has partner rank 10. Coefficient 0 and coefficient 1 both have partner rank 10. The scaled coefficient 4 vector has partner rank 10 at every chirality coefficient. Do not claim the ten-kernel coefficient span is settled."
conditional_surface_status: "48 signed permutations of (1, 2, 3); sign product plus both cap generators; every chirality coefficient"
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

**Target.** On the 48 signed permutations of `(1, 2, 3)`, decide whether
every nonzero chirality coefficient on the scaled coefficient 4 vector
has partner rank 10.

**Ansatz.** The sign product plus both cap generators, plus an arbitrary
chirality coefficient. The scaled coordinate is 4 and the swapped-dot
coordinate is 0. The even coefficient and both cap coefficients stay
nonzero. The swapped-dot vector is not in this all-scale count. The
ten-kernel coefficient span is not this ansatz. The full soldered bond
space is not classified.

The kernel cross sum on two perpendicular directions is the sum of the
products of the two centre values. This note does not convert that sum
into an alphabet mean.

**Conclusion.** For every ordered height pair and every chirality
coefficient, including 0, the partner rank is 10.

**Proof.** The runner enumerates the proper rotations and the alphabet
and builds the ten kernels. On each ordered height pair it forms the
partner rows of the scaled coefficient 4 vector and of the chirality
cap. Those coefficient pairs span 17 dimensions. A running gcd of the
10-by-10 minors of the pencil is a nonzero constant. Those minors
therefore have no common root, so the projected rank stays 10 at every
chirality coefficient.

**Obligations.** Proved here: every chirality coefficient on the scaled
coefficient 4 vector has partner rank 10. Cited from the even-span note,
and not re-proved: the name of the even space. Cited from the ratio-span
note, and not re-proved: the names of the two spans. The strongest
missing lemma is whether every chirality coefficient on the swapped-dot
coefficient 1 vector has partner rank 10.

## What this does not do

- It does not select a scale. The cap sum is a witness.
- It does not give the swapped-dot vector this all-scale count.
- It does not classify every vector in the even space and both spans.
- It does not claim that the ten-kernel coefficient span is settled.
- It does not claim that the full soldered bond space is classified.
- It does not apply the order-blind converse.
- It does not convert a kernel cross sum into an alphabet mean.
- It does not repeat the bond-space dimension count.
- It does not return to the modulus-3 triple.
- It does not supply a formation site, probability, or rate.

## Runner

`scripts/chiral_pair_cap_sum_chirality_scale_partner_kernel_2026_10_10.py`
checks the constant minor gcd. `TOTAL: PASS=13 FAIL=0`.

## Imports

No formation site, probability, rate, or selected scale is imported.
The proper rotations, the stacked partner kernel, and the minor gcd are
enumerated here. The even-span note names the even space. The ratio-span
note names the two spans. The order-blind converse is not applied.
