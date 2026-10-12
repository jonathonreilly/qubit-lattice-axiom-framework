---
claim_id: chiral_pair_first_third_even_dot_family_partner_kernel_bounded_theorem_note_2026-10-10
claim_type: open_gate
claim_scope: "On every ordered height pair, the first-and-third even-dot family is the first and third even generators plus both swapped-dot generators, with the second even generator omitted or included. On the source-same pairs the omitted sum has sign-product coordinate 1, swapped coordinate -5/2, and orthogonal coordinate 3, and the included sum also has parallel coordinate -1 and oblique coordinate 1. On the other three pairs the omitted sum has sign-product coordinate 1, swapped coordinate -2, parallel coordinate 1, oblique coordinate 1, and orthogonal coordinate 2, and the included sum has swapped coordinate -1. Each base image has rank 10. The coefficient pairs compress to 17 rows. The pivot minors at chirality coefficients 0, 1, -1, -1/2, 1/2, 3/2, 5/2, 2, -2, and -2/3 have a nonzero constant gcd, so every chirality coefficient has partner rank 10. The five coefficients 0, 1, -1, -1/2, and 5/2 are not this certificate. A vector with both a nonzero swapped-dot coordinate and a nonzero scaled coordinate is not in this count. The ten-kernel coefficient span is not classified. The full soldered bond space is not classified. No scale is selected."
upstream_dependencies:
  - minimal_axioms
  - chiral_pair_even_span_partner_kernel_bounded_theorem_note_2026-10-10
  - chiral_pair_two_parity_excluded_partner_kernel_bounded_theorem_note_2026-10-10
runner: scripts/chiral_pair_first_third_even_dot_family_partner_kernel_2026_10_10.py
---

# The first-and-third even-dot family keeps partner rank 10

**Date:** 2026-10-11

**Type:** open_gate

**Audit:** unset; independent audit remains a separate lane

**Status:** open_gate

**Status authority:** independent audit only. This source changes no axiom,
primitive, framework rule, or audit verdict.

**Primary runner:**
[`scripts/chiral_pair_first_third_even_dot_family_partner_kernel_2026_10_10.py`](../scripts/chiral_pair_first_third_even_dot_family_partner_kernel_2026_10_10.py)

**Parents:** the [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md),
[the even span](CHIRAL_PAIR_EVEN_SPAN_PARTNER_KERNEL_BOUNDED_THEOREM_NOTE_2026-10-10.md),
and [the two ratio spans](CHIRAL_PAIR_TWO_PARITY_EXCLUDED_PARTNER_KERNEL_BOUNDED_THEOREM_NOTE_2026-10-10.md).

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: open_gate
claim_type_reason: "On every ordered height pair, the first and third even generators plus both swapped-dot generators, with the second even generator omitted or included, have partner rank 10 at every chirality coefficient."
trace_class: negative_route_pruning
target_claim_id: null
target_blocker_text: "Other generic orbits and higher-rank bond spaces are not classified."
source_of_blocker_text: frontier_question
reachability_to_target: prunes
artifact_role: partial_narrowing_proposal
next_trace_action: "Decide whether every chirality coefficient on the sum of both swapped-dot generators and the cap generator of one ratio span has partner rank 10. The first-and-third even-dot family has partner rank 10 at every chirality coefficient. Do not claim the ten-kernel coefficient span is settled."
conditional_surface_status: "every ordered height pair; first and third even generators plus both swapped-dot generators; second even generator omitted or included; every chirality coefficient"
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

**Landing status:** partial narrowing with an incomplete formal no-go packet.
The scoped arguments and exact checks below are preserved for development;
this note does not carry a no-go packet PASS or retained-grade authority.
The missing N1 route packet is distinct from the mathematical validity of
the finite ansatz results.

**Target.** On every ordered height pair, decide whether every chirality
coefficient on the sum of the first and third even generators plus both
swapped-dot generators has partner rank 10, and whether the same count
holds for the sum of all three even generators plus both swapped-dot
generators.

**Ansatz.** The first-and-third even-dot family is the first even
generator plus the third even generator plus the swapped-dot generator
of each ratio span, with the second even generator either omitted or
included, plus an arbitrary chirality coefficient. On the source-same
ordered height pairs the omitted sum has sign-product coordinate `1`,
swapped coordinate `-5/2`, and orthogonal coordinate `3`. The included
sum has those coordinates and also parallel coordinate `-1` and oblique
coordinate `1`. On the other three ordered height pairs the omitted sum
has sign-product coordinate `1`, swapped coordinate `-2`, parallel
coordinate `1`, oblique coordinate `1`, and orthogonal coordinate `2`.
The included sum has swapped coordinate `-1` in place of `-2`. One
pivot-minor gcd covers both members and both coordinate presentations.
The five chirality coefficients `0`, `1`, `-1`, `-1/2`, and `5/2` are
not this certificate. A vector with both a nonzero swapped-dot
coordinate and a nonzero scaled coordinate is not this ansatz. The
ten-kernel coefficient span is not this ansatz. The full soldered bond
space is not classified.

The kernel cross sum on two perpendicular directions is the sum of the
products of the two centre values. This note does not convert that sum
into an alphabet mean.

**Conclusion.** On every ordered height pair, every member of the
family has partner rank 10 at every chirality coefficient, including 0.
The only ten-kernel partner is 0.

**Proof.** The runner enumerates the proper rotations and the alphabet
and builds the ten kernels. The first even generator is the sign
product. On each source-same ordered height pair the third even
generator has swapped coordinate `-1/2` and orthogonal coordinate `1`.
Added to both swapped-dot generators, the omitted sum gives
sign-product coordinate `1`, swapped coordinate `-5/2`, and orthogonal
coordinate `3`. The second even generator has parallel coordinate `-1`
and oblique coordinate `1`, so the included sum adds those coordinates.
On each of the other three ordered height pairs the third even
generator has parallel coordinate `1` and oblique coordinate `1`, and
the second even generator has swapped coordinate `1`. Added to the sign
product and both swapped-dot generators, the omitted sum gives
sign-product coordinate `1`, swapped coordinate `-2`, parallel
coordinate `1`, oblique coordinate `1`, and orthogonal coordinate `2`,
and the included sum gives swapped coordinate `-1`. The base image of
each vector has rank 10, so the partner kernel at chirality coefficient
0 is 0. The coefficient pairs compress to 17 rows. Gaussian elimination
at chirality coefficients `0`, `1`, `-1`, `-1/2`, `1/2`, `3/2`, `5/2`,
`2`, `-2`, and `-2/3` selects ten pivot rows, and the running gcd of
those minors is a nonzero constant. A constant has no root, so the
partner rank stays 10 at every chirality coefficient.

**Obligations.** Proved here: on every ordered height pair, both
members of this family have partner rank 10 at every chirality
coefficient. Cited from the even-span note, and not re-proved: the name
of the even space. Cited from the ratio-span note, and not re-proved:
the names of the two spans. The strongest missing lemma is whether
every chirality coefficient on the sum of both swapped-dot generators
and the cap generator of one ratio span has partner rank 10.

## What this does not do

- It does not select a scale. The vectors are witnesses.
- It does not give a vector with both a nonzero swapped-dot coordinate and a nonzero scaled coordinate this count.
- It does not give every vector in the even space and both spans this count.
- It does not claim that the ten-kernel coefficient span is settled.
- It does not claim that the full soldered bond space is classified.
- It does not apply the order-blind converse.
- It does not convert a kernel cross sum into an alphabet mean.
- It does not repeat the bond-space dimension count.
- It does not return to the modulus-3 triple.
- It does not supply a formation site, probability, or rate.

## Runner

`scripts/chiral_pair_first_third_even_dot_family_partner_kernel_2026_10_10.py`
checks the constant pivot-minor gcd. `TOTAL: PASS=21 FAIL=0`.

## Imports

No formation site, probability, rate, or selected scale is imported.
The proper rotations, the stacked partner kernel, and the pivot-minor
gcd are enumerated here. The even-span note names the even space. The
ratio-span note names the two spans. The order-blind converse is not
applied.


## No-Go Discipline Gate

**Packet status: incomplete; no PASS claimed.** This is a partial narrowing
proposal under the displayed finite ansatz, not a framework-wide exclusion.

- **N1:** The actual routes here are the finite orbit/slice reduction and
  the explicit algebraic argument in the Proof. Related coefficient choices
  are not five independent approach families. The five-family packet is
  absent; no route count or retained prior authority is invented.
- **N2:** The alphabet, covariance, support and coefficient restrictions
  define one ansatz. No count of independent physical walls is asserted.
- **N3:** The uniform finite-record model and any order-blind converse are
  explicit mathematical inputs. They supply no physical selection, formation
  rate, empirical scale or additional framework primitive.
- **N4:** The Imports and Obligations identify which parent result is used.
  A finite kernel rank, a two-centre cross sum and a normalized neighbour
  product are different statements; none is substituted for another.
- **N5:** The primary runner reports the finite resolution it executes.
  Mode spectra, evolving site ensembles and lattice-wide dynamics are not
  computed. Any all-window consequence uses the cited analytical converse
  with strict positivity, not a lattice simulation.
- **N6:** No new axiom is requested or declared necessary. Expanding the
  ansatz is legitimate further work and is not ruled out by these results.
- **N7:** The strongest broader escape is to allow additional support
  signatures or coupled height sectors: cancellation can change when the
  partner domain changes. A full-space classification must derive the joint
  slice and product equations and prove their solution set; the present
  restricted result supplies no such closure. Inside the stated ansatz the
  displayed exact proof, rather than failure to find an escape, is the claim.
- **N8:** The cited parent and companion notes exhibit successive escapes
  from smaller cap and cross spans. Those examples explicitly prohibit
  treating any restricted span classification as closure of the full bond
  space. Historical next-step statements are local frontiers, not evidence
  that later companion results remain unproved.
