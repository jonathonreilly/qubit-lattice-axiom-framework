---
claim_id: chiral_pair_chi_ts_matched_span_partner_kernel_bounded_theorem_note_2026-10-10
claim_type: open_gate
claim_scope: "On the 48 signed permutations of (1, 2, 3), the chirality, transverse-sign, and matched span is the rational span of the chirality cap, the transverse-sign cap, and the matched transverse cross. That span is 3-dimensional. Its intersection with either ratio span of the oblique-matched plane is 0. For every ordered pair of absolute heights among 1, 2, and 3, a nonzero vector in the span has partner rank 10 exactly when its matched coefficient is nonzero, and then the only ten-kernel partner is 0. When the matched coefficient is 0 and the vector is nonzero, the partner rank is 7 and the partner kernel is the even space of the partner height relative to the source height. On source-partner pairs (1, 2), (2, 1), and (1, 3) that space is spanned by the sign product, the oblique dot minus the parallel dot, and the orthogonal cross minus half the swapped cross. On pairs (3, 1), (2, 3), and (3, 2) it is spanned by the sign product, the swapped cross, and the parallel dot plus the oblique dot. The chirality cap pairs with the sign product. At heights 1 and 2 the bond on -e_x and -e_y has lefts (-1, -2, -3) and (-1, -2, 3), rights (1, -2, -3) and (-3, 2, -1), centre pairs (-1, 1) and (1, 1), and kernel cross sum 0. The chirality cap plus the matched cross on the same bond has centre pairs (-1, 1) and (0, 1) and kernel cross sum -1. A vector with a nonzero coefficient outside these three kernels is not in this count. The ten-kernel coefficient span is not classified. The full soldered bond space is not classified. No scale is selected."
upstream_dependencies:
  - minimal_axioms
  - chiral_pair_cross_height_parity_span_cross_moments_bounded_theorem_note_2026-10-10
  - chiral_pair_twice_chi_ts_matched_line_cross_moments_bounded_theorem_note_2026-10-10
runner: scripts/chiral_pair_chi_ts_matched_span_partner_kernel_2026_10_10.py
---

# The chirality, transverse-sign, and matched span

**Date:** 2026-10-11

**Type:** open_gate

**Audit:** unset; independent audit remains a separate lane

**Status:** open_gate

**Status authority:** independent audit only. This source changes no axiom,
primitive, framework rule, or audit verdict.

**Primary runner:**
[`scripts/chiral_pair_chi_ts_matched_span_partner_kernel_2026_10_10.py`](../scripts/chiral_pair_chi_ts_matched_span_partner_kernel_2026_10_10.py)

**Parents:** the [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md),
[the parity span](CHIRAL_PAIR_CROSS_HEIGHT_PARITY_SPAN_CROSS_MOMENTS_BOUNDED_THEOREM_NOTE_2026-10-10.md),
and [the doubled chirality line](CHIRAL_PAIR_TWICE_CHI_TS_MATCHED_LINE_CROSS_MOMENTS_BOUNDED_THEOREM_NOTE_2026-10-10.md).

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: open_gate
claim_type_reason: "In the chirality, transverse-sign, and matched span, a nonzero vector has partner rank 10 exactly when its matched coefficient is nonzero. Otherwise the partner kernel is the even space of the partner height."
trace_class: negative_route_pruning
target_claim_id: null
target_blocker_text: "Other generic orbits and higher-rank bond spaces are not classified."
source_of_blocker_text: frontier_question
reachability_to_target: prunes
artifact_role: partial_narrowing_proposal
next_trace_action: "Decide whether the sign product has a ten-kernel partner outside the odd space of the partner height. The chirality cap and the transverse-sign cap have partner kernel equal to the even space, whose excluded coefficients are 0. Do not claim the ten-kernel coefficient span is settled."
conditional_surface_status: "48 signed permutations of (1, 2, 3); coefficients on the chirality cap, the transverse-sign cap, and the matched cross; witness directions (-1, 0, 0) and (0, -1, 0)"
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
every nonzero rational combination of the chirality cap, the
transverse-sign cap, and the matched transverse cross has partner rank
10, or exhibit a combination that pairs with a nonzero ten-kernel vector.

**Ansatz.** The chirality, transverse-sign, and matched span is the
rational span of those three kernels. A vector in the span has
coefficients `(a, b, c)` on the chirality cap, the transverse-sign cap,
and the matched transverse cross, and coefficient 0 on the other seven
kernels. The chirality cap and the transverse-sign cap are parity
kernels. The matched transverse cross is an excluded kernel. The sign
product, the swapped cross, the parallel dot, the oblique dot, and the
orthogonal cross are the remaining parity kernels used to name the
partner. Both ratio spans of the oblique-matched plane meet this span
only at 0. A vector with a nonzero coefficient outside the three
kernels is not in the span. The ten-kernel coefficient span is not this
ansatz. The full soldered bond space is not classified.

The kernel cross sum on two perpendicular directions is the sum of the
products of the two centre values. This note does not convert that sum
into an alphabet mean.

**Conclusion.** For every ordered pair of heights among `{1, 2, 3}`,
and for every rational `(a, b, c)` not all 0, the partner kernel is 0
when `c` is not 0, and it is the even space `E` of the partner height
relative to the source height when `c` is 0. In the first case the
partner rank is 10. In the second case the partner rank is 7.

On source-partner pairs `(1, 2)`, `(2, 1)`, and `(1, 3)`, `E` is the
rational span of the sign product, the oblique dot minus the parallel
dot, and the orthogonal cross minus half the swapped cross. On pairs
`(3, 1)`, `(2, 3)`, and `(3, 2)`, `E` is the rational span of the sign
product, the swapped cross, and the parallel dot plus the oblique dot.
Each generator has excluded coefficients 0. These are the even bases
named for the reversed ordered pair in the parity-span note.

The chirality cap is the combination `(1, 0, 0)`. It pairs with the
sign product, which is a nonzero ten-kernel vector, and with every
vector of `E`. At heights 1 and 2, the bond on `-e_x` and `-e_y` has
lefts `(-1, -2, -3)` and `(-1, -2, 3)`. The rights are `(1, -2, -3)`
and `(-3, 2, -1)`. Against the sign product the centre pairs are
`(-1, 1)` and `(1, 1)`. The first left contributes `-1`. The second
left contributes `1`. The kernel cross sum is 0. The chirality cap plus
the matched cross, the combination `(1, 0, 1)`, has centre pairs
`(-1, 1)` and `(0, 1)` on the same bond. The second left now contributes
0. The kernel cross sum is `-1`.

**Proof.** The runner enumerates the proper rotations and the alphabet
and builds the ten kernels. The three unit vectors on the chirality
cap, the transverse-sign cap, and the matched cross are independent.
Adjoining either ratio span raises the rank from 3 to 6, so each
intersection is 0.

Fix an ordered height pair. Let `M_chi`, `M_ts`, and `M_matched` be the
partner maps of the three kernels, and let `S` send `(u, v, w)` to
`M_chi u + M_ts v + M_matched w`. The partner equation for coefficients
`(a, b, c)` is `S(a w, b w, c w) = 0`. The runner row-reduces `S` and
finds rank 24, so the kernel has dimension 6. Every kernel vector has
matched block 0, and its chirality block and transverse-sign block lie
in `E`. The space `E` is 3-dimensional, so the triples `(u, v, 0)` with
`u` and `v` in `E` form a 6-dimensional space and equal the kernel.

Thus `S(a w, b w, c w) = 0` if and only if `c w = 0` and both `a w` and
`b w` lie in `E`. If `c` is not 0, then `w = 0` and the partner rank is
10. If `c = 0` and `(a, b)` is not `(0, 0)`, then `w` lies in `E`, every
vector of `E` occurs, and the partner rank is 7. The runner checks the
two caps directly. Each has partner rank 7, and each named generator of
`E` annihilates every partner row. It also checks the triples
`(2, -3, 5)` and `(2, -3, 0)` on every ordered height pair. The first
has partner rank 10. The second has partner rank 7. The witness bonds
are direct centre sums.

**Obligations.** Proved here: the span is 3-dimensional and meets each
ratio span only at 0, the partner rank is 10 exactly when the matched
coefficient is nonzero, the partner kernel is the named even space when
that coefficient is 0, the excluded coefficients of that space are 0,
and the cross sums are 0 and `-1`. Cited from the parity-span note, and
not re-proved: the cross-moment criterion inside the parity span, and
the names of the even bases on each ordered pair. Cited from the
doubled chirality note, and not re-proved: the five lines through these
three kernels have partner rank 10. Those lines sit in the nonzero
matched part of this span. The strongest missing lemma is whether the
sign product has a ten-kernel partner outside the odd space of the
partner height.

## What this does not do

- It does not select a scale. The coefficients are witnesses.
- It does not claim that every nonzero combination has partner rank 10. The matched-zero plane does not.
- It does not take a vector with a nonzero coefficient outside these three kernels.
- It does not re-prove the five lines or the parity-span cross-moment criterion.
- It does not claim that the ten-kernel coefficient span is settled.
- It does not claim that the full soldered bond space is classified.
- It does not apply the order-blind converse.
- It does not convert a kernel cross sum into an alphabet mean.
- It does not repeat the bond-space dimension count.
- It does not return to the modulus-3 triple.
- It does not supply a formation site, probability, or rate.

## Runner

`scripts/chiral_pair_chi_ts_matched_span_partner_kernel_2026_10_10.py`
checks the span, the six partner kernels, the stacked rank, and the
witness bonds. `TOTAL: PASS=8 FAIL=0`.

## Imports

No formation site, probability, rate, or selected scale is imported.
The proper rotations, the partner kernels, the stacked rank, and the
witness sums are enumerated here. The parity-span note names the even
bases. The doubled chirality note names the five lines. The order-blind
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
