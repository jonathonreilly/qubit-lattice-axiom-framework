---
claim_id: chiral_pair_opposite_height_basis_mixtures_product_means_bounded_theorem_note_2026-10-10
claim_type: open_gate
claim_scope: "On the 48 signed permutations of (1, 2, 3), every rational mixture of the ten slice-zero bond-symmetric soldered kernels on one opposite-height pair has every neighbour-product mean equal to 1. The supports of the six directions are disjoint, and every left slice of each basis kernel sums to 0, so the identity is linear and covers the whole rational span. The mixture with all ten coefficients equal to 1/32 is strictly positive, with values 29/32, 15/16, 31/32, 1, 33/32, 17/16, and 19/16. Its one-neighbour mean on e_z at far end (1, 2, -3) is 1, and its two-neighbour mean on -e_x and e_z at far ends (2, 1, 3) and (1, 2, -3) is 1. Every one-neighbour condition and every two-direction partner pair has mean 1. Coefficient 2 on the chirality cap alone takes values -1, 1, and 3, so it is not strictly positive, and those same means remain 1. The integer coefficients 1 through 10 are a moment check, not a bound on the span. A sum across heights is not in this ansatz. The 300-dimensional affine space is not classified. No scale is selected."
upstream_dependencies:
  - minimal_axioms
  - order_blind_nearest_neighbour_formation_independence_beyond_neighbours_unsoldered_constancy_and_soldered_escape_bounded_theorem_note_2026-09-22
  - chiral_pair_scaled_cross_dot_bases_opposite_height_ansatz_bounded_theorem_note_2026-10-10
  - chiral_pair_bond_factor_dimension_bounded_theorem_note_2026-10-10
runner: scripts/chiral_pair_opposite_height_basis_mixtures_product_means_2026_10_10.py
---

# Every rational mixture of one opposite-height basis has product mean 1

**Date:** 2026-10-10

**Type:** open_gate

**Audit:** unset; independent audit remains a separate lane

**Status:** open_gate

**Status authority:** independent audit only. This source changes no axiom,
primitive, framework rule, or audit verdict.

**Primary runner:**
[`scripts/chiral_pair_opposite_height_basis_mixtures_product_means_2026_10_10.py`](../scripts/chiral_pair_opposite_height_basis_mixtures_product_means_2026_10_10.py)

**Parents:** the [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md),
[the order-blind formation note](ORDER_BLIND_NEAREST_NEIGHBOUR_FORMATION_INDEPENDENCE_BEYOND_NEIGHBOURS_UNSOLDERED_CONSTANCY_AND_SOLDERED_ESCAPE_BOUNDED_THEOREM_NOTE_2026-09-22.md),
[the opposite-height basis note](CHIRAL_PAIR_SCALED_CROSS_DOT_BASES_OPPOSITE_HEIGHT_ANSATZ_BOUNDED_THEOREM_NOTE_2026-10-10.md),
and the [chiral-pair bond note](CHIRAL_PAIR_BOND_FACTOR_DIMENSION_BOUNDED_THEOREM_NOTE_2026-10-10.md).

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: open_gate
claim_type_reason: "Every rational mixture of the ten opposite-height basis kernels has neighbour-product mean 1, and the equal-coefficient mixture at 1/32 is a strictly positive witness."
trace_class: negative_route_pruning
target_claim_id: null
target_blocker_text: "Other generic orbits and higher-rank bond spaces are not classified."
source_of_blocker_text: frontier_question
reachability_to_target: prunes
artifact_role: partial_narrowing_proposal
next_trace_action: "Decide which rational mixtures of two opposite-height bases, at two distinct absolute heights, have every neighbour-product mean equal to 1. Do not claim the 300-dimensional affine space is classified."
conditional_surface_status: "48 signed permutations of (1, 2, 3); one opposite-height pair; rational mixtures of its ten basis kernels; equal coefficients 1/32"
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

Theorem 2 of the parent: "with phi_d(a, b) = phi_-d(b, a) and
E_r0[prod_{(d, b) in N} phi_d(., b)] = 1 for every N. Conversely every
family with these properties is order-blind on every window." The parent
leaves the sentence "Other generic orbits and higher-rank bond spaces
are not classified."

## Theorem

**Landing status:** partial narrowing with an incomplete formal no-go packet.
The scoped arguments and exact checks below are preserved for development;
this note does not carry a no-go packet PASS or retained-grade authority.
The missing N1 route packet is distinct from the mathematical validity of
the finite ansatz results.

**Target.** On the 48 signed permutations of `(1, 2, 3)`, decide which
rational mixtures of the ten basis kernels on one opposite-height pair
have every neighbour-product mean equal to 1.

**Ansatz.** Fix an absolute height `h`. The ten kernels are the
chirality cap, the transverse-sign cap, their sign product, the matched
transverse cross, the swapped transverse cross, the parallel
transverse-dot sign, the matched oblique transverse-dot sign, the
swapped transverse-dot sign, the orthogonal swapped cross, and the
scaled cross-dot kernel. Each is supported on bonds with `a·d = h` and
`b·d = -h`. A rational mixture has coefficients `c_i` and factor
`phi_d(a, b) = 1 + sum_i c_i K_{i,d}(a, b)`. The same statement at the
other two heights is a separate family. A sum across heights is not in
this ansatz. The 300-dimensional affine space is not classified.

**Conclusion.** Every such mixture is bond-symmetric and soldered.
Every left slice sums to 0, and each record meets at most one live
direction. Every neighbour product therefore has mean 1. The identity
covers the whole rational span. It is not restricted to an integer box.

The witness with every coefficient equal to `1/32` takes the values
`29/32`, `15/16`, `31/32`, `1`, `33/32`, `17/16`, and `19/16`. All are
strictly positive. Every far-end sum of the kernel mixture is 0, so
every far-end sum of the factor is 48. The uniform mean on `e_z` at far
end `(1, 2, -3)` is 1. The uniform mean on `-e_x` and `e_z` at far ends
`(2, 1, 3)` and `(1, 2, -3)` is 1. At height 1, the bond on `-e_x` from
`(-1, -3, -2)` to `(1, -3, 2)` has chirality value `1` and scaled value
`-2`, while the bond from `(-1, -3, -2)` to `(1, -3, -2)` has chirality
value `-1` and scaled value `0`. The witness is not a scalar multiple of
either kernel.

Coefficient `2` on the chirality cap, with the other nine coefficients
0, takes the values `-1`, `1`, and `3`. It is not strictly positive.
Its one-neighbour means and its two-direction means are still 1. The
integer coefficients `1` through `10`, in the kernel order above, have
the same means equal to 1. That box is a check. The slice argument
already covers every rational tuple.

If the sum of the nine absolute unit-kernel coefficients and twice the
absolute scaled coefficient is strictly less than 1, then every factor
value lies in `(0, 2)`. The equal mixture meets the bound, since
`11/32 < 1`. The bound is sufficient, not a description of the whole
positive cone. Theorem 2's converse applies to every strictly positive
mixture, including this witness. It is not applied to the coefficient-2
cap.

**Proof.** The runner enumerates the proper rotations and the alphabet.
Each basis kernel is unchanged by every proper rotation and by reversing
the bond. The nine unit kernels take values in `{-1, 0, 1}`, and the
scaled kernel takes values in `{-2, -1, 0, 1, 2}`. For each fixed far
end, the sum over the 48 centres is 0. Across the union of the ten
supports, each record meets at most one direction. A record has one
coordinate of each modulus, so the direction `a·d = h` is unique, and
every kernel vanishes off that cap pair.

A neighbour condition names at most one far end in each direction. At a
centre, at most one factor differs from 1. The product minus 1 is the
mixture on that live direction, or 0 if the condition does not use it.
Summing over the centre, each coefficient multiplies a left slice. Every
left slice is 0, so the mean is 1. Bond symmetry of the kernels gives
bond symmetry of the mixture. Soldered covariance is linear, so the
mixture is soldered. Reversing the bond identifies a far-end sum with a
left slice in the opposite direction, so every far-end kernel sum is 0
and every far-end factor sum is 48.

The value set, the two sample means, and the far-end sums of the equal
mixture are computed directly. So are all `864` one-neighbour conditions
and all `103680` two-direction partner pairs of that mixture, of the
coefficient-2 cap, and of the integer box. The overlap bond and the
split bond are the two height-1 bonds named above.

**Obligations.** Proved here: soldered covariance, bond symmetry, the
value ranges, the left slices, the one-live-direction bound on the union
of the ten supports, the product-mean identity for every rational
mixture, the seven witness values, the two sample means, the far-end
sums, the overlap and split bonds, the coefficient-2 values, and the
integer-box means. Cited from Theorem 2, and not re-proved: bond
symmetry together with every product mean equal to 1 makes a family
order-blind on every window. The converse is applied only where the
factor is strictly positive. Cited from the opposite-height basis note,
and not re-proved: these ten kernels are a basis of the ansatz. Cited
from the chiral-pair bond note, and not re-proved: far-end sum 1 is the
normalisation of that bond space. The strongest missing lemma is which
rational mixtures of two such bases, at two distinct absolute heights,
have every neighbour-product mean equal to 1.

## What this does not do

- It does not select a scale. The coefficient `1/32` is a witness.
- It does not describe the whole strictly positive cone. The coefficient
  bound is sufficient only.
- It does not put a sum across heights inside the ansatz.
- It does not claim that the 300-dimensional affine space is classified.
- It does not treat the integer box `1` through `10` as the span.
- It does not re-derive the basis.
- It does not repeat the bond-space dimension count.
- It does not return to the modulus-3 triple.
- It does not supply a formation site, probability, or rate.

## Runner

`scripts/chiral_pair_opposite_height_basis_mixtures_product_means_2026_10_10.py`
repeats the covariance comparison, the slice sums, the live-direction
bound, and the three moment checks. `TOTAL: PASS=8 FAIL=0`.

## Imports

No formation site, probability, rate, or selected scale is imported.
The proper rotations, the ten kernels, the slices, and the moment sums
are enumerated here. Theorem 2's converse is applied to each strictly
positive mixture. The opposite-height basis note supplies the basis.
The chiral-pair bond note supplies the meaning of far-end sum 1.


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
