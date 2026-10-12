---
claim_id: chiral_pair_one_swapped_dot_twice_same_cap_partner_kernel_bounded_theorem_note_2026-10-10
claim_type: open_gate
claim_scope: "On every ordered height pair, one swapped-dot generator plus twice the cap of the same ratio span lies in that span. The plus sum has transverse-sign coordinate -2, sign-product coordinate -2, matched coordinate 4, swapped coordinate -1, swapped-dot coordinate 1, orthogonal coordinate 1, and scaled coordinate 4. The minus sum has transverse-sign coordinate 2, sign-product coordinate 2, and swapped-dot coordinate -1, with the same matched, swapped, orthogonal, and scaled coordinates. Chirality coefficient 0 has partner rank 7. The partner kernel is that span on pairs (1, 2), (2, 1), (2, 3), and (3, 2), and the other span on (1, 3) and (3, 1). The 14-row pencil has maximal-minor gcd equal to a nonzero multiple of the cube of the chirality coefficient, so every nonzero chirality coefficient has partner rank 10. Twice the cap of the other span is not in this count. The ten-kernel coefficient span is not classified. The full soldered bond space is not classified. No scale is selected."
upstream_dependencies:
  - minimal_axioms
  - chiral_pair_even_span_partner_kernel_bounded_theorem_note_2026-10-10
  - chiral_pair_two_parity_excluded_partner_kernel_bounded_theorem_note_2026-10-10
runner: scripts/chiral_pair_one_swapped_dot_twice_same_cap_partner_kernel_2026_10_10.py
---

# One swapped-dot generator plus twice the same-span cap

**Date:** 2026-10-11

**Type:** open_gate

**Audit:** unset; independent audit remains a separate lane

**Status:** open_gate

**Status authority:** independent audit only. This source changes no axiom,
primitive, framework rule, or audit verdict.

**Primary runner:**
[`scripts/chiral_pair_one_swapped_dot_twice_same_cap_partner_kernel_2026_10_10.py`](../scripts/chiral_pair_one_swapped_dot_twice_same_cap_partner_kernel_2026_10_10.py)

**Parents:** the [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md),
[the even span](CHIRAL_PAIR_EVEN_SPAN_PARTNER_KERNEL_BOUNDED_THEOREM_NOTE_2026-10-10.md),
and [the two ratio spans](CHIRAL_PAIR_TWO_PARITY_EXCLUDED_PARTNER_KERNEL_BOUNDED_THEOREM_NOTE_2026-10-10.md).

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: open_gate
claim_type_reason: "On every ordered height pair, one swapped-dot generator plus twice the cap of the same span has partner rank 7 only at chirality coefficient 0."
trace_class: negative_route_pruning
target_claim_id: null
target_blocker_text: "Other generic orbits and higher-rank bond spaces are not classified."
source_of_blocker_text: frontier_question
reachability_to_target: prunes
artifact_role: partial_narrowing_proposal
next_trace_action: "Decide whether every chirality coefficient on the sum of one swapped-dot generator and twice the cap of the other ratio span has partner rank 10. Do not claim the ten-kernel coefficient span is settled."
conditional_surface_status: "every ordered height pair; one swapped-dot generator plus twice the cap of the same ratio span"
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
coefficient on the sum of one swapped-dot generator and twice the cap
of the same ratio span has partner rank 10.

**Ansatz.** There are two sums. The plus sum is the swapped-dot generator
of the first ratio span plus twice its cap. It has transverse-sign
coordinate `-2`, sign-product coordinate `-2`, matched coordinate `4`,
swapped coordinate `-1`, swapped-dot coordinate `1`, orthogonal
coordinate `1`, and scaled coordinate `4`. The minus sum uses the second
ratio span and has transverse-sign coordinate `2`, sign-product
coordinate `2`, and swapped-dot coordinate `-1`, with the same matched,
swapped, orthogonal, and scaled coordinates. Each lies in its own span
and not in the other. Twice the cap of the other span is not this
ansatz. The ten-kernel coefficient span is not this ansatz. The full
soldered bond space is not classified.

The kernel cross sum on two perpendicular directions is the sum of the
products of the two centre values. This note does not convert that sum
into an alphabet mean.

**Conclusion.** On every ordered height pair, chirality coefficient 0 has
partner rank 7, and every nonzero chirality coefficient has partner rank
10.

**Proof.** The runner enumerates the proper rotations and the alphabet
and builds the ten kernels. Each sum lies in its span. The base image
has rank 7. On pairs `(1, 2)`, `(2, 1)`, `(2, 3)`, and `(3, 2)` the
partner kernel is that span. On `(1, 3)` and `(3, 1)` it is the other
span. The coefficient pairs compress to 14 rows. The gcd of the
10-by-10 minors is a nonzero multiple of the cube of the chirality
coefficient, so the only root is 0 and every nonzero chirality
coefficient has partner rank 10. At heights 1 and 2 the bond on `-e_x`
and `-e_y` has lefts `(-1, -2, -3)` and `(-1, -2, 3)`. The plus sum at
chirality coefficient 1, against the matched-oblique generator of its
span, has rights `(1, -3, -2)` and `(-1, 2, -3)`, centre pairs `(-9, 0)`
and `(-1, 2)`, and kernel cross sum `-2`. The minus sum at chirality
coefficient 1 has rights `(1, -3, -2)` and `(-1, 2, 3)`, centre pairs
`(1, 2)` and `(-1, 0)`, and kernel cross sum `2`.

**Obligations.** Proved here: one swapped-dot generator plus twice the
cap of the same span, on every ordered height pair, for every chirality
coefficient. Cited from the even-span note, and not re-proved: the name
of the even space. Cited from the ratio-span note, and not re-proved:
the names of the two spans. The strongest missing lemma is whether
every chirality coefficient on the sum of one swapped-dot generator and
twice the cap of the other ratio span has partner rank 10.

## What this does not do

- It does not select a scale. The vectors are witnesses.
- It does not give twice the cap of the other span this count.
- It does not give one swapped-dot generator plus one cap this count.
- It does not claim that the ten-kernel coefficient span is settled.
- It does not claim that the full soldered bond space is classified.
- It does not apply the order-blind converse.
- It does not convert a kernel cross sum into an alphabet mean.
- It does not repeat the bond-space dimension count.
- It does not return to the modulus-3 triple.
- It does not supply a formation site, probability, or rate.

## Runner

`scripts/chiral_pair_one_swapped_dot_twice_same_cap_partner_kernel_2026_10_10.py`
checks the degree-3 maximal-minor gcd. `TOTAL: PASS=6 FAIL=0`.

## Imports

No formation site, probability, rate, or selected scale is imported.
The proper rotations, the stacked partner kernel, and the maximal-minor
gcds are enumerated here. The even-span note names the even space. The
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
