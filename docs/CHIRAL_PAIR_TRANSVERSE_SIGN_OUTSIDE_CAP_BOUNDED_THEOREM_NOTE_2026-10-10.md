---
claim_id: chiral_pair_transverse_sign_outside_cap_bounded_theorem_note_2026-10-10
claim_type: open_gate
claim_scope: "On the 48 signed permutations of (1, 2, 3), the transverse-sign cap phi_d(a, b) = 1 + (1/2) S_d(a) S_{-d}(b) is bond-symmetric and soldered. S_d is the sign of the product of the two coordinates transverse to d when a·d = 3, and 0 otherwise. All 729 partner patterns have product mean 1, the values are 1/2, 1, and 3/2, and every far-end sum equals 48. The bonds e_z from (1, 2, 3) and from (-2, 1, 3) to (1, 2, -3) have transverse products +1 and -1 against one chiral product -1, so no scale of the exhibited chiral cap matches. The order-blind subset is not classified. No scale is selected."
upstream_dependencies:
  - minimal_axioms
  - order_blind_nearest_neighbour_formation_independence_beyond_neighbours_unsoldered_constancy_and_soldered_escape_bounded_theorem_note_2026-09-22
  - chiral_pair_bond_factor_dimension_bounded_theorem_note_2026-10-10
runner: scripts/chiral_pair_transverse_sign_outside_cap_2026_10_10.py
---

# A transverse-sign cap on the chiral pair lies off the chiral-cap line

**Date:** 2026-10-10

**Type:** open_gate

**Audit:** unset; independent audit remains a separate lane

**Status:** open_gate

**Status authority:** independent audit only. This source changes no axiom,
primitive, framework rule, or audit verdict.

**Primary runner:**
[`scripts/chiral_pair_transverse_sign_outside_cap_2026_10_10.py`](../scripts/chiral_pair_transverse_sign_outside_cap_2026_10_10.py)

**Parents:** the [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md),
[the order-blind formation note](ORDER_BLIND_NEAREST_NEIGHBOUR_FORMATION_INDEPENDENCE_BEYOND_NEIGHBOURS_UNSOLDERED_CONSTANCY_AND_SOLDERED_ESCAPE_BOUNDED_THEOREM_NOTE_2026-09-22.md),
and the [chiral-pair bond note](CHIRAL_PAIR_BOND_FACTOR_DIMENSION_BOUNDED_THEOREM_NOTE_2026-10-10.md).

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: open_gate
claim_type_reason: "The transverse-sign cap at coefficient 1/2 is strictly positive, every partner pattern has mean 1, and two bonds forbid every scale of the chiral cap."
trace_class: negative_route_pruning
target_claim_id: null
target_blocker_text: "Other generic orbits and higher-rank bond spaces are not classified."
source_of_blocker_text: frontier_question
reachability_to_target: prunes
artifact_role: partial_narrowing_proposal
next_trace_action: "Ask whether a strictly positive order-blind factor on the 48-point chiral pair lies outside both the chiral-cap line and the transverse-sign cap. Do not repeat the dimension count."
conditional_surface_status: "48 signed permutations of (1, 2, 3); transverse-sign cap; coefficient 1/2; uniform partner patterns"
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

**Target.** On the 48 signed permutations of `(1, 2, 3)`, decide whether
a strictly positive order-blind factor lies outside the exhibited
chiral-cap line.

**Ansatz.** Let `S_d(a)` be the sign of the product of the two
coordinates transverse to an axis step `d` when `a·d = 3`, and 0
otherwise. The family is

```text
phi_d(a, b) = 1 + (1/2) S_d(a) S_{-d}(b)
```

The exhibited chiral-cap line uses orbit chirality in place of `S`:
`+1` on the proper orbit of `(1, 2, 3)` and `-1` on the other orbit,
again only on the cap `a·d = 3`. A factor off both lines is not
classified here.

**Conclusion.** The transverse-sign factor is bond-symmetric and
soldered. Its six supports are disjoint and each sign has mean 0. All
729 partner patterns have uniform product mean 1. The values are
`1/2`, `1`, and `3/2`. Every far-end sum equals 48, so the quotient by
48 lies in the normalised space. The parent converse makes the family
order-blind on every window. On `e_z`, the bonds from `(1, 2, 3)` and
from `(-2, 1, 3)` to `(1, 2, -3)` have transverse products `+1` and
`-1`, while both chiral products are `-1`. No rational scale of the
chiral cap matches both bonds.

**Proof.** The runner enumerates the proper rotations and the alphabet.
`(1, 2, -3)` lies in the second proper orbit, and `(-2, 1, 3)` lies in
the first. The sign `S` itself changes under some rotations; the product
`S_d(a) S_{-d}(b)` does not. Direct comparison gives bond symmetry.
Each coordinate axis meets the cap condition in disjoint sets, and each
sign sums to 0. Every 6-tuple with entries in `{-1, 0, 1}` therefore
has product mean 1, which covers every neighbour condition. The two
named bonds give the products above, so the tensors are not
proportional.

**Obligations.** Proved here: soldered covariance of the product, bond
symmetry, disjoint mean-zero supports, the 729 means, the three values,
the far-end sums, and the two-bond obstruction. Cited from Theorem 2,
and not re-proved: bond symmetry together with every product mean equal
to 1 makes the family order-blind on every window. Cited from the
chiral-pair bond note, and not re-proved: far-end sum 1 is the
normalisation of that bond space. The dimension count is not repeated.
The chiral-cap line is the comparison tensor, not a re-derivation of
its order-blindness. The strongest missing lemma is a strictly positive
order-blind factor outside both lines.

## What this does not do

- It does not select a scale. The coefficient `1/2` is a witness.
- It does not classify the order-blind subset.
- It does not re-derive the order-blindness of the chiral cap.
- It does not repeat the bond-space dimension count.
- It does not return to the modulus-3 triple.
- It does not supply a formation site, probability, or rate.

## Runner

`scripts/chiral_pair_transverse_sign_outside_cap_2026_10_10.py` repeats
the product covariance, the 729 means, and the two-bond obstruction.
`TOTAL: PASS=10 FAIL=0`.

## Imports

No formation site, probability, rate, or selected scale is imported.
The proper rotations, the transverse signs, and the partner means are
enumerated here. Theorem 2's converse is applied to this family. The
chiral-pair bond note supplies the meaning of far-end sum 1.


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
