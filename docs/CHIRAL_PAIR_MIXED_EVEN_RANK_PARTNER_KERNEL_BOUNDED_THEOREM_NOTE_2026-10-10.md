---
claim_id: chiral_pair_mixed_even_rank_partner_kernel_bounded_theorem_note_2026-10-10
claim_type: open_gate
claim_scope: "On the ordered height pairs (1, 3), (2, 3), and (3, 2), the second even generator plus both swapped-dot generators is the kernel vector with swapped coordinate -1 and orthogonal coordinate 2. Its base image has rank 7 and contains every chirality row. The projected pivot minors at chirality coefficients 0 and -1 have a nonzero constant gcd, so every chirality coefficient has partner rank 7. The same coefficients on the other three ordered height pairs are not in this rank-7 count. The ten-kernel coefficient span is not classified. The full soldered bond space is not classified. No scale is selected."
upstream_dependencies:
  - minimal_axioms
  - chiral_pair_even_span_partner_kernel_bounded_theorem_note_2026-10-10
  - chiral_pair_two_parity_excluded_partner_kernel_bounded_theorem_note_2026-10-10
runner: scripts/chiral_pair_mixed_even_rank_partner_kernel_2026_10_10.py
---

# An even-space block mixed with both ratio spans keeps partner rank 7

**Date:** 2026-10-11

**Type:** open_gate

**Audit:** unset; independent audit remains a separate lane

**Status:** open_gate

**Status authority:** independent audit only. This source changes no axiom,
primitive, framework rule, or audit verdict.

**Primary runner:**
[`scripts/chiral_pair_mixed_even_rank_partner_kernel_2026_10_10.py`](../scripts/chiral_pair_mixed_even_rank_partner_kernel_2026_10_10.py)

**Parents:** the [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md),
[the even span](CHIRAL_PAIR_EVEN_SPAN_PARTNER_KERNEL_BOUNDED_THEOREM_NOTE_2026-10-10.md),
and [the two ratio spans](CHIRAL_PAIR_TWO_PARITY_EXCLUDED_PARTNER_KERNEL_BOUNDED_THEOREM_NOTE_2026-10-10.md).

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: open_gate
claim_type_reason: "On three ordered height pairs, one vector that meets both ratio spans and has a nonzero even-space block component has partner rank 7 at every chirality coefficient."
trace_class: negative_route_pruning
target_claim_id: null
target_blocker_text: "Other generic orbits and higher-rank bond spaces are not classified."
source_of_blocker_text: frontier_question
reachability_to_target: prunes
artifact_role: partial_narrowing_proposal
next_trace_action: "Decide whether every chirality coefficient on the source-same form of the second even generator plus both swapped-dot generators has partner rank 10. On (1, 3), (2, 3), and (3, 2) those coefficients have partner rank 7 at every chirality coefficient. Do not claim the ten-kernel coefficient span is settled."
conditional_surface_status: "ordered height pairs (1, 3), (2, 3), and (3, 2); second even generator plus both swapped-dot generators; every chirality coefficient"
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

**Decomposition convention.** Here an even-space block component means the
coefficient component in the displayed direct sum of the even space, the
ratio spans present in the ansatz, and (when present) the chirality line.
It does not mean the parity-even projection of the total kernel. Ratio-span
generators may themselves contribute to that parity-even projection.

**Target.** On the 48 signed permutations of `(1, 2, 3)`, decide whether
every nonzero chirality coefficient, on every vector that meets both
ratio spans and has a nonzero even-space block component, has partner rank 10.

**Ansatz.** The second even generator plus the swapped-dot generator of
each ratio span, plus an arbitrary chirality coefficient. All three
block coefficients are nonzero. On the ordered height pairs `(1, 3)`,
`(2, 3)`, and `(3, 2)`, the summed kernel vector has swapped coordinate
`-1` and orthogonal coordinate `2`. The same coefficients on the other
three ordered height pairs are not in this rank-7 count. The ten-kernel
coefficient span is not this ansatz. The full soldered bond space is
not classified.

The kernel cross sum on two perpendicular directions is the sum of the
products of the two centre values. This note does not convert that sum
into an alphabet mean.

On these three pairs the total pencil is
`2 (orthogonal - swapped/2) + c chi`, which is purely odd in the
parity decomposition. Its rank 7 therefore agrees with the general
odd-space result; it is not a counterexample to the mixed-parity theorem.

**Conclusion.** On `(1, 3)`, `(2, 3)`, and `(3, 2)`, every chirality
coefficient, including 0, has partner rank 7. A nonzero chirality
coefficient on a vector that meets both spans and has a nonzero even-space block
component therefore need not have partner rank 10.

**Proof.** The runner enumerates the proper rotations and the alphabet
and builds the ten kernels. On each ordered height pair outside the
source-same set, the second even generator is the swapped generator.
Added to both swapped-dot generators, it gives swapped coordinate `-1`
and orthogonal coordinate `2`. The base image of that vector has rank 7,
so the kernel of the base rows has dimension 3. Every chirality row of
the pencil is orthogonal to that kernel, and therefore lies in the base
image. Every chirality coefficient keeps the partner image inside that
7-dimensional space. The coefficient pairs compress to 14 rows. Gaussian
elimination on their base parts selects seven pivot columns, and those
columns are an isomorphism on the image. The pivot rows at chirality
coefficients `0` and `-1` give 7-by-7 minors whose running gcd is a
nonzero constant. A constant has no root, so the projected rank stays 7,
and the partner rank stays 7, at every chirality coefficient.

**Obligations.** Proved here: on three ordered height pairs, this mixed
vector has partner rank 7 at every chirality coefficient. Cited from the
even-span note, and not re-proved: the name of the even space. Cited
from the ratio-span note, and not re-proved: the names of the two
spans. The strongest missing lemma is whether every chirality
coefficient on the source-same form of these coefficients has partner
rank 10.

## What this does not do

- It does not select a scale. The mixed vector is a witness.
- It does not give the source-same height pairs this rank-7 count.
- It does not give every mixed vector partner rank 7.
- It does not claim that the ten-kernel coefficient span is settled.
- It does not claim that the full soldered bond space is classified.
- It does not apply the order-blind converse.
- It does not convert a kernel cross sum into an alphabet mean.
- It does not repeat the bond-space dimension count.
- It does not return to the modulus-3 triple.
- It does not supply a formation site, probability, or rate.

## Runner

`scripts/chiral_pair_mixed_even_rank_partner_kernel_2026_10_10.py`
checks the constant projected gcd. `TOTAL: PASS=15 FAIL=0`.

## Imports

No formation site, probability, rate, or selected scale is imported.
The proper rotations, the stacked partner kernel, and the projected
minor gcd are enumerated here. The even-span note names the even space.
The ratio-span note names the two spans. The order-blind converse is
not applied.


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
