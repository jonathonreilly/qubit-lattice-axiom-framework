---
claim_id: chiral_pair_ratio_span_sum_partner_kernel_bounded_theorem_note_2026-10-10
claim_type: open_gate
claim_scope: "On the 48 signed permutations of (1, 2, 3), the two ratio spans meet only at 0 and their sum is 6-dimensional. The swapped transverse dot sits only on the swapped-orthogonal generator, with opposite signs on the two spans, and the scaled cross-dot kernel sits only on the cap generator, with coefficient 2 on both spans. A nonzero vector in the sum has a nonzero ten-kernel partner if and only if it lies in exactly one span. The partner is then the three-dimensional ratio span of that height pair: the same span on pairs (1, 2), (2, 1), (2, 3), and (3, 2), and the other span on (1, 3) and (3, 1). A vector with a nonzero part in each span has partner rank 10. The chirality cap lies outside the sum. Adding a nonzero multiple of it to a nonzero vector of the sum gives partner rank 10. On -e_x and -e_y, the lefts are (-1, -2, -3) and (-1, -2, 3). The swapped-orthogonal generator of the first span plus the oblique-matched generator of the second, against the oblique-matched generator of the first, has rights (1, -2, -3) and (-1, 2, -3), centre pairs (0, 0) and (2, 2), and kernel cross sum 4. The chirality cap plus the swapped-orthogonal generator, against the sign product, has rights (1, -3, -2) and (-1, 2, -3), centre pairs (-1, -1) and (-1, -1), and kernel cross sum 2. A vector outside the span of the chirality cap and the two ratio spans is not in this count. The ten-kernel coefficient span is not classified. The full soldered bond space is not classified. No scale is selected."
upstream_dependencies:
  - minimal_axioms
  - chiral_pair_two_parity_excluded_partner_kernel_bounded_theorem_note_2026-10-10
  - chiral_pair_odd_space_partner_kernel_bounded_theorem_note_2026-10-10
runner: scripts/chiral_pair_ratio_span_sum_partner_kernel_2026_10_10.py
---

# A sum of the two ratio spans pairs only on one span

**Date:** 2026-10-11

**Type:** open_gate

**Audit:** unset; independent audit remains a separate lane

**Status:** open_gate

**Status authority:** independent audit only. This source changes no axiom,
primitive, framework rule, or audit verdict.

**Primary runner:**
[`scripts/chiral_pair_ratio_span_sum_partner_kernel_2026_10_10.py`](../scripts/chiral_pair_ratio_span_sum_partner_kernel_2026_10_10.py)

**Parents:** the [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md),
[the two ratio spans](CHIRAL_PAIR_TWO_PARITY_EXCLUDED_PARTNER_KERNEL_BOUNDED_THEOREM_NOTE_2026-10-10.md),
and [the odd space](CHIRAL_PAIR_ODD_SPACE_PARTNER_KERNEL_BOUNDED_THEOREM_NOTE_2026-10-10.md).

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: open_gate
claim_type_reason: "In the sum of the two ratio spans, a nonzero ten-kernel partner occurs exactly on one span, and the chirality cap does not create another one."
trace_class: negative_route_pruning
target_claim_id: null
target_blocker_text: "Other generic orbits and higher-rank bond spaces are not classified."
source_of_blocker_text: frontier_question
reachability_to_target: prunes
artifact_role: partial_narrowing_proposal
next_trace_action: "Decide whether a vector outside the span of the chirality cap and the two ratio spans, with a nonzero coefficient on the swapped transverse dot or the scaled cross-dot kernel, has a ten-kernel partner other than 0. Inside that span, such a partner exists exactly on one ratio span. Do not claim the ten-kernel coefficient span is settled."
conditional_surface_status: "48 signed permutations of (1, 2, 3); sum of the two ratio spans and the chirality cap; witness directions (-1, 0, 0) and (0, -1, 0)"
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

**Target.** On the 48 signed permutations of `(1, 2, 3)`, decide whether
a vector with a nonzero coefficient on the swapped transverse dot or the
scaled cross-dot kernel has a ten-kernel partner other than 0.

**Ansatz.** The two ratio spans are the spans named by the ratio-span
note. They meet only at 0, so their sum is 6-dimensional. The swapped
transverse dot appears only on the swapped-orthogonal generator, with
coefficient `1` on the first span and `-1` on the second. The scaled
cross-dot kernel appears only on the cap generator, with coefficient `2`
on both spans. The chirality cap is one further direction outside the
sum. A vector outside the span of that cap and the two ratio spans is
not in this ansatz. The ten-kernel coefficient span is not this ansatz.
The full soldered bond space is not classified.

The kernel cross sum on two perpendicular directions is the sum of the
products of the two centre values. This note does not convert that sum
into an alphabet mean.

**Conclusion.** Write a vector of the sum as `s1, s2, s3` on the first
span and `t1, t2, t3` on the second. Its swapped-dot coefficient is
`s2 - t2`, and its scaled coefficient is `2(s3 + t3)`. For every ordered
height pair, a nonzero vector of this form has a nonzero ten-kernel
partner if and only if one coefficient group vanishes and the other does
not. The partner is
then the whole partner span: the same ratio span on height pairs
`(1, 2)`, `(2, 1)`, `(2, 3)`, and `(3, 2)`, and the other ratio span on
`(1, 3)` and `(3, 1)`. If both groups are nonzero, the partner rank is
10 and the only ten-kernel partner is 0.

Thus, inside the sum, a nonzero swapped-dot or scaled coefficient has a
ten-kernel partner other than 0 exactly when the vector lies in one
ratio span. The chirality cap adds no further partner. For any nonzero chirality coefficient and any nonzero sum part,
the partner rank is 10. At chirality coefficient zero the single-span
rank-7 cases above remain; the zero coefficient is not excluded by
adding a chirality coordinate to the ansatz.

At heights 1 and 2, the bond on `-e_x` and `-e_y` has lefts
`(-1, -2, -3)` and `(-1, -2, 3)`. The swapped-orthogonal generator of
the first span plus the oblique-matched generator of the second has
values `0` and `2`. Against the oblique-matched generator of the first
span, the rights are `(1, -2, -3)` and `(-1, 2, -3)`, the centre pairs
are `(0, 0)` and `(2, 2)`, and the kernel cross sum is `4`. The first
left contributes 0. The second left contributes `4`.

The chirality cap plus the swapped-orthogonal generator has values `-1`
and `-1` on the same lefts. Against the sign product, the rights are
`(1, -3, -2)` and `(-1, 2, -3)`, the centre pairs are `(-1, -1)` and
`(-1, -1)`, and the kernel cross sum is `2`.

**Proof.** The runner enumerates the proper rotations and the alphabet
and builds the ten kernels. Each ratio span has rank 3, and the two
together have rank 6. The chirality cap raises that rank to 7. The
stated supports of the swapped transverse dot and the scaled kernel are
read off the six generators.

On each ordered height pair, let `P+` and `P-` be the partner spans,
exchanged on `(1, 3)` and `(3, 1)`. They meet only at 0. Let `S` send
`(u1, u2, u3, v1, v2, v3)` to the sum of the partner maps of the six
generators. The runner row-reduces `S` and finds rank 42, so the kernel
has dimension 18. Every kernel vector has its first three blocks in
`P+` and its last three blocks in `P-`. Those spaces are 3-dimensional,
so the tuples of that form are 18-dimensional and equal the kernel.

For coefficients `s` and `t`, the partner equation is
`S(s1 y, s2 y, s3 y, t1 y, t2 y, t3 y) = 0`. This holds if and only if
every `si y` lies in `P+` and every `tj y` lies in `P-`. One nonzero
group forces `y` into that partner span, and every vector of the span
occurs, so the partner rank is 7. Both groups nonzero force `y` into
the intersection, so `y` is 0 and the partner rank is 10. The runner
checks one vector from each single span and two vectors that meet both
spans, on every ordered height pair.

The same count with the chirality cap adjoined has rank 49 and nullity
21. The chirality block lies in the even space of the partner height,
and the six sum blocks lie in `P+` and `P-` as before. The even space
meets each partner span only at 0. A nonzero cap coefficient therefore
forces `y` into the even space. A nonzero sum coefficient forces `y`
into `P+` or `P-`. Both force `y` to 0. The runner checks the chirality
cap plus the swapped-orthogonal generator on every ordered height pair.
The two witness bonds are direct centre sums.

**Obligations.** Proved here: the two spans meet only at 0, the excluded
coordinates sit on the named generators, the six-generator kernel is the
product of the partner spans, a vector in both spans has partner rank
10, a vector in one span has partner rank 7, the chirality cap lies
outside the sum and does not restore a partner, and the cross sums are
`4` and `2`. Cited from the ratio-span note, and not re-proved: the
names of the two spans and the exchange of their partners. Cited from
the odd-space note, and not re-proved: the name of the even space. The
strongest missing lemma is whether a vector outside the span of the
chirality cap and the two ratio spans, with a nonzero swapped-dot or
scaled coefficient, has a ten-kernel partner other than 0.

## What this does not do

- It does not select a scale. The coefficients are witnesses.
- It does not give a vector that meets both spans a nonzero partner.
- It does not give the chirality cap plus a nonzero sum vector a partner.
- It does not take a vector outside the span of the chirality cap and the two ratio spans.
- It does not restate the partner kernel of one ratio span as a new construction.
- It does not claim that the ten-kernel coefficient span is settled.
- It does not claim that the full soldered bond space is classified.
- It does not apply the order-blind converse.
- It does not convert a kernel cross sum into an alphabet mean.
- It does not repeat the bond-space dimension count.
- It does not return to the modulus-3 triple.
- It does not supply a formation site, probability, or rate.

## Runner

`scripts/chiral_pair_ratio_span_sum_partner_kernel_2026_10_10.py` checks
the span sum, the two stacked kernels, and the witness bonds.
`TOTAL: PASS=8 FAIL=0`.

## Imports

No formation site, probability, rate, or selected scale is imported.
The proper rotations, the stacked partner kernels, and the witness sums
are enumerated here. The ratio-span note names the two spans. The
odd-space note names the even space. The order-blind converse is not
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
