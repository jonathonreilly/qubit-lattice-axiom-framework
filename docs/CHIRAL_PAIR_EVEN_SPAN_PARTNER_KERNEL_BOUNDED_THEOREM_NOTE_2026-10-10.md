---
claim_id: chiral_pair_even_span_partner_kernel_bounded_theorem_note_2026-10-10
claim_type: open_gate
claim_scope: "On the 48 signed permutations of (1, 2, 3), the even span of an ordered height pair is the rational span of the even basis of the source height. It is 3-dimensional, its excluded coefficients are 0, and it meets the three excluded axes only at 0. For every ordered pair of absolute heights among 1, 2, and 3, every nonzero vector in that span has partner rank 6, and the partner kernel is the odd space of the partner height. On source-partner pairs (1, 2), (2, 1), and (1, 3) that odd space is spanned by the chirality cap, the transverse-sign cap, the swapped cross, and the parallel dot plus the oblique dot. On pairs (3, 1), (2, 3), and (3, 2) it is spanned by the chirality cap, the transverse-sign cap, the oblique dot minus the parallel dot, and the orthogonal cross minus half the swapped cross. The sign product lies in every even span. It pairs with the chirality cap and with no vector outside the odd space. At heights 1 and 2 the bond on -e_x and -e_y has lefts (-1, -2, -3) and (-1, -2, 3), rights (1, -3, -2) and (-1, 2, -3), centre pairs (1, -1) and (1, 1) against the chirality cap, and kernel cross sum 0. Against the matched cross the centre pairs are (1, 0) and (1, 1) and the kernel cross sum is 1. A vector outside the even span is not in this count. The ten-kernel coefficient span is not classified. The full soldered bond space is not classified. No scale is selected."
upstream_dependencies:
  - minimal_axioms
  - chiral_pair_cross_height_parity_span_cross_moments_bounded_theorem_note_2026-10-10
  - chiral_pair_chi_ts_matched_span_partner_kernel_bounded_theorem_note_2026-10-10
runner: scripts/chiral_pair_even_span_partner_kernel_2026_10_10.py
---

# The even span and its odd partner

**Date:** 2026-10-11

**Type:** open_gate

**Audit:** unset; independent audit remains a separate lane

**Status:** open_gate

**Status authority:** independent audit only. This source changes no axiom,
primitive, framework rule, or audit verdict.

**Primary runner:**
[`scripts/chiral_pair_even_span_partner_kernel_2026_10_10.py`](../scripts/chiral_pair_even_span_partner_kernel_2026_10_10.py)

**Parents:** the [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md),
[the parity span](CHIRAL_PAIR_CROSS_HEIGHT_PARITY_SPAN_CROSS_MOMENTS_BOUNDED_THEOREM_NOTE_2026-10-10.md),
and [the chirality, transverse-sign, and matched span](CHIRAL_PAIR_CHI_TS_MATCHED_SPAN_PARTNER_KERNEL_BOUNDED_THEOREM_NOTE_2026-10-10.md).

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: open_gate
claim_type_reason: "Every nonzero vector in the even span has partner rank 6, and the partner kernel is the odd space of the partner height."
trace_class: negative_route_pruning
target_claim_id: null
target_blocker_text: "Other generic orbits and higher-rank bond spaces are not classified."
source_of_blocker_text: frontier_question
reachability_to_target: prunes
artifact_role: partial_narrowing_proposal
next_trace_action: "Decide whether the swapped cross has a ten-kernel partner outside the even space of the partner height. The even span pairs only with the odd space. Do not claim the ten-kernel coefficient span is settled."
conditional_surface_status: "48 signed permutations of (1, 2, 3); even basis of the source height; witness directions (-1, 0, 0) and (0, -1, 0)"
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
the sign product has a ten-kernel partner outside the odd space of the
partner height.

**Ansatz.** For an ordered height pair, the even span is the rational
span of the even basis of the source height. On source heights paired
with `(1, 2)`, `(2, 1)`, and `(3, 1)`, that basis is the sign product,
the oblique dot minus the parallel dot, and the orthogonal cross minus
half the swapped cross. On `(1, 3)`, `(2, 3)`, and `(3, 2)`, it is the
sign product, the swapped cross, and the parallel dot plus the oblique
dot. The sign product lies in every one of these spans. Each generator
has excluded coefficients 0. The odd space of the partner height is the
4-dimensional space named below. A vector outside the even span, including
a vector with a nonzero odd part, is not in this ansatz. The ten-kernel
coefficient span is not this ansatz. The full soldered bond space is not
classified.

The kernel cross sum on two perpendicular directions is the sum of the
products of the two centre values. This note does not convert that sum
into an alphabet mean.

**Conclusion.** For every ordered pair of heights among `{1, 2, 3}`,
every nonzero vector in the even span has partner rank 6. The partner
kernel is the odd space of the partner height relative to the source
height. No excluded kernel lies in that partner.

On source-partner pairs `(1, 2)`, `(2, 1)`, and `(1, 3)`, the odd space
is spanned by the chirality cap, the transverse-sign cap, the swapped
cross, and the parallel dot plus the oblique dot. On pairs `(3, 1)`,
`(2, 3)`, and `(3, 2)`, it is spanned by the chirality cap, the
transverse-sign cap, the oblique dot minus the parallel dot, and the
orthogonal cross minus half the swapped cross. These are the odd bases
named for the reversed ordered pair in the parity-span note.

The sign product is the combination with coefficient 1 on the first even
generator. It pairs with the chirality cap and with every vector of the
odd space, and with no vector outside that space. At heights 1 and 2,
the bond on `-e_x` and `-e_y` has lefts `(-1, -2, -3)` and
`(-1, -2, 3)`. The rights are `(1, -3, -2)` and `(-1, 2, -3)`. Against
the chirality cap the centre pairs are `(1, -1)` and `(1, 1)`. The first
left contributes `-1`. The second left contributes `1`. The kernel cross
sum is 0. Against the matched cross the centre pairs are `(1, 0)` and
`(1, 1)`. The first left contributes 0. The second left contributes `1`.
The kernel cross sum is `1`.

**Proof.** The runner enumerates the proper rotations and the alphabet
and builds the ten kernels. On each of the two even shapes, the three
generators are independent, their excluded coefficients are 0, and
adjoining the three excluded axes raises the rank from 3 to 6.

Fix an ordered height pair. Let `M_1`, `M_2`, and `M_3` be the partner
maps of the three even generators, and let `S` send `(u, v, w)` to
`M_1 u + M_2 v + M_3 w`. The partner equation for even coefficients
`(a, b, c)` is `S(a w, b w, c w) = 0`. The runner row-reduces `S` and
finds rank 18, so the kernel has dimension 12. Every kernel vector has
its three blocks in the odd space `O`. That space is 4-dimensional, so
the triples with all three blocks in `O` form a 12-dimensional space and
equal the kernel.

Thus `S(a w, b w, c w) = 0` if and only if `a w`, `b w`, and `c w` all
lie in `O`. If `(a, b, c)` is not `(0, 0, 0)`, then `w` lies in `O`,
every vector of `O` occurs, and the partner rank is 6. The runner checks
each even generator directly. Each has partner rank 6, and each named
generator of `O` annihilates every partner row. Those generators have
excluded coefficients 0. It also checks the coefficient triples
`(1, 0, 0)` and `(1, 1, 1)` on every ordered height pair. Both have
partner rank 6. The first is the sign product. The witness bonds are
direct centre sums.

**Obligations.** Proved here: the even span is 3-dimensional and meets
the excluded axes only at 0, every nonzero vector has partner rank 6,
the partner kernel is the named odd space, and the cross sums are 0 and
`1`. Cited from the parity-span note, and not re-proved: the
cross-moment criterion inside the parity span, and the names of the odd
and even bases. Cited from the chirality, transverse-sign, and matched
note, and not re-proved: that span splits on the matched coefficient.
The strongest missing lemma is whether the swapped cross has a
ten-kernel partner outside the even space of the partner height.

## What this does not do

- It does not select a scale. The coefficients are witnesses.
- It does not give the sign product a partner outside the odd space.
- It does not take a vector outside the even span.
- It does not re-prove the parity-span cross-moment criterion or the chirality, transverse-sign, and matched span.
- It does not claim that the ten-kernel coefficient span is settled.
- It does not claim that the full soldered bond space is classified.
- It does not apply the order-blind converse.
- It does not convert a kernel cross sum into an alphabet mean.
- It does not repeat the bond-space dimension count.
- It does not return to the modulus-3 triple.
- It does not supply a formation site, probability, or rate.

## Runner

`scripts/chiral_pair_even_span_partner_kernel_2026_10_10.py` checks the
even span, the six partner kernels, the stacked rank, and the witness
bonds. `TOTAL: PASS=8 FAIL=0`.

## Imports

No formation site, probability, rate, or selected scale is imported.
The proper rotations, the partner kernels, the stacked rank, and the
witness sums are enumerated here. The parity-span note names the odd
and even bases. The chirality, transverse-sign, and matched note names
that span. The order-blind converse is not applied.


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
