---
claim_id: chiral_pair_mixed_parity_partner_kernel_bounded_theorem_note_2026-10-10
claim_type: open_gate
claim_scope: "On the 48 signed permutations of (1, 2, 3), a parity vector whose odd part and even part are both nonzero has partner rank 10, so the only ten-kernel partner is 0. The orthogonal cross lies in the parity span and in neither the odd space nor the even space. At heights 1 and 2 it is half the swapped cross plus the even generator given by the orthogonal cross minus half the swapped cross. On the bond along -e_x and -e_y, the lefts are (-1, -2, -3) and (-1, -2, 3) and the rights are (1, -3, -2) and (-1, 2, -3). Against the sign product the centre pairs are (0, -1) and (-1, -1) and the kernel cross sum is 1. Against the chirality cap the centre pairs are (0, -1) and (-1, 1) and the kernel cross sum is -1. Against the matched cross the centre pairs are (0, 0) and (-1, 1) and the kernel cross sum is -1. A vector with a nonzero excluded coefficient is not in this count. The ten-kernel coefficient span is not classified. The full soldered bond space is not classified. No scale is selected."
upstream_dependencies:
  - minimal_axioms
  - chiral_pair_cross_height_parity_span_cross_moments_bounded_theorem_note_2026-10-10
  - chiral_pair_odd_space_partner_kernel_bounded_theorem_note_2026-10-10
runner: scripts/chiral_pair_mixed_parity_partner_kernel_2026_10_10.py
---

# A mixed parity vector pairs only with zero

**Date:** 2026-10-11

**Type:** open_gate

**Audit:** unset; independent audit remains a separate lane

**Status:** open_gate

**Status authority:** independent audit only. This source changes no axiom,
primitive, framework rule, or audit verdict.

**Primary runner:**
[`scripts/chiral_pair_mixed_parity_partner_kernel_2026_10_10.py`](../scripts/chiral_pair_mixed_parity_partner_kernel_2026_10_10.py)

**Parents:** the [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md),
[the parity span](CHIRAL_PAIR_CROSS_HEIGHT_PARITY_SPAN_CROSS_MOMENTS_BOUNDED_THEOREM_NOTE_2026-10-10.md),
and [the odd space](CHIRAL_PAIR_ODD_SPACE_PARTNER_KERNEL_BOUNDED_THEOREM_NOTE_2026-10-10.md).

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: open_gate
claim_type_reason: "A parity vector with both an odd part and an even part has partner rank 10, so the only ten-kernel partner is 0."
trace_class: negative_route_pruning
target_claim_id: null
target_blocker_text: "Other generic orbits and higher-rank bond spaces are not classified."
source_of_blocker_text: frontier_question
reachability_to_target: prunes
artifact_role: partial_narrowing_proposal
next_trace_action: "Decide whether a vector with a nonzero coefficient on the swapped transverse dot or the scaled cross-dot kernel has a ten-kernel partner other than 0. A mixed parity vector pairs only with 0. Do not claim the ten-kernel coefficient span is settled."
conditional_surface_status: "48 signed permutations of (1, 2, 3); parity span; witness directions (-1, 0, 0) and (0, -1, 0)"
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
a vector with both an odd part and an even part has a ten-kernel partner
other than 0.

**Ansatz.** The parity span is the direct sum of the odd space and the
even space of the source height. A vector in this span is mixed when
both parts are nonzero. The orthogonal cross is one mixed vector. At
heights 1 and 2 it is half the swapped cross plus the even generator
whose swapped coefficient is `-1/2` and whose orthogonal coefficient is
`1`. A vector with a nonzero coefficient on the matched cross, the
swapped transverse dot, or the scaled cross-dot kernel is not in this
ansatz. The ten-kernel coefficient span is not this ansatz. The full
soldered bond space is not classified.

The kernel cross sum on two perpendicular directions is the sum of the
products of the two centre values. This note does not convert that sum
into an alphabet mean.

**Conclusion.** For every ordered pair of heights among `{1, 2, 3}`, a
mixed parity vector has partner rank 10. The only ten-kernel partner is
0.

The orthogonal cross lies in the parity span and in neither summand, so
both of its parts are nonzero. The sum of the chirality cap and the sign
product is another mixed vector, and it also has partner rank 10.

At heights 1 and 2, the bond on `-e_x` and `-e_y` has lefts
`(-1, -2, -3)` and `(-1, -2, 3)`. The rights are `(1, -3, -2)` and
`(-1, 2, -3)`. The orthogonal values are `0` and `-1`. Against the sign
product the centre pairs are `(0, -1)` and `(-1, -1)`. The first left
contributes 0. The second left contributes `1`. The kernel cross sum is
`1`. Against the chirality cap the centre pairs are `(0, -1)` and
`(-1, 1)`. The second left contributes `-1`. The kernel cross sum is
`-1`. Against the matched cross the centre pairs are `(0, 0)` and
`(-1, 1)`. The second left contributes `-1`. The kernel cross sum is
`-1`.

**Proof.** The runner enumerates the proper rotations and the alphabet
and builds the ten kernels. On each ordered height pair the odd basis
has dimension 4, the even basis has dimension 3, and the two together
have rank 7. Both bases have excluded coefficients 0. The orthogonal
cross does not raise that rank, and it lies in neither basis. At heights
1 and 2 it equals half the swapped cross plus the third even generator.

Let `M_1` through `M_4` be the partner maps of the odd generators, and
let `N_1` through `N_3` be the partner maps of the even generators. Let
`S` send `(u_1, u_2, u_3, u_4, v_1, v_2, v_3)` to the sum of `M_i u_i`
and `N_j v_j`. The runner row-reduces `S` and finds rank 46, so the
kernel has dimension 24. Every kernel vector has its four odd blocks in
the even space of the partner height and its three even blocks in the
odd space of the partner height. Those spaces have dimensions 3 and 4
and meet only at 0, so the tuples of that form are 24-dimensional and
equal the kernel.

For odd coefficients `a` and even coefficients `b`, the partner equation
is `S(a_1 w, a_2 w, a_3 w, a_4 w, b_1 w, b_2 w, b_3 w) = 0`. This holds
if and only if every `a_i w` lies in the partner even space and every
`b_j w` lies in the partner odd space. If both `a` and `b` are nonzero,
then `w` lies in both spaces, so `w` is 0. The partner rank is 10. The
runner checks the chirality-sign mixture and the orthogonal cross on
every ordered height pair. The witness bond is a direct centre sum.

**Obligations.** Proved here: both parts of the orthogonal cross are
nonzero, the joint rank is 46, every mixed parity vector has partner
rank 10, and the cross sums are `1`, `-1`, and `-1`. Cited from the
parity-span note, and not re-proved: the names of the odd and even
bases. The pure odd and pure even partner kernels are not the claim of
this note. The strongest missing lemma is whether a vector with a
nonzero coefficient on the swapped transverse dot or the scaled
cross-dot kernel has a ten-kernel partner other than 0.

## What this does not do

- It does not select a scale. The coefficients are witnesses.
- It does not give a mixed parity vector a nonzero ten-kernel partner.
- It does not take a vector with a nonzero excluded coefficient.
- It does not restate the pure odd or pure even partner kernel as this claim.
- It does not claim that the ten-kernel coefficient span is settled.
- It does not claim that the full soldered bond space is classified.
- It does not apply the order-blind converse.
- It does not convert a kernel cross sum into an alphabet mean.
- It does not repeat the bond-space dimension count.
- It does not return to the modulus-3 triple.
- It does not supply a formation site, probability, or rate.

## Runner

`scripts/chiral_pair_mixed_parity_partner_kernel_2026_10_10.py` checks
the mixed membership, the joint rank, and the witness bond.
`TOTAL: PASS=8 FAIL=0`.

## Imports

No formation site, probability, rate, or selected scale is imported.
The proper rotations, the joint partner kernel, and the witness sums
are enumerated here. The parity-span note names the odd and even bases.
The odd-space note names the odd partner kernel. The order-blind
converse is not applied.


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
