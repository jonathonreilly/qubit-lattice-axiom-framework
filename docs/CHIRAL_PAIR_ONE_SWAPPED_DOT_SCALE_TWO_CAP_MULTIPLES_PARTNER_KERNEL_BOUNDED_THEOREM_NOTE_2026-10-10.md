---
claim_id: chiral_pair_one_swapped_dot_scale_two_cap_multiples_partner_kernel_bounded_theorem_note_2026-10-10
claim_type: open_gate
claim_scope: "On every ordered height pair, and for every triple of positive integers (t, r, s), t times one swapped-dot generator plus r times the plus cap and s times the minus cap has swapped-dot coordinate t or -t, swapped coordinate -t, orthogonal coordinate t, transverse-sign coordinate s-r, sign-product coordinate s-r, matched coordinate 2r+2s, and scaled coordinate 2r+2s. The two sums are linearly independent for every positive integer t. Each lies in neither ratio span and outside the even space. The partner rows are homogeneous of degree 1, so the matrix at (t, r, s, c) is t times the matrix at (1, r/t, s/t, c/t). Exact positive-parameter root-branch certificates prove rank 10 at every chirality coefficient. The ten-kernel coefficient span and full soldered bond space remain unclassified. No scale is selected."
upstream_dependencies:
  - minimal_axioms
  - chiral_pair_even_span_partner_kernel_bounded_theorem_note_2026-10-10
  - chiral_pair_two_parity_excluded_partner_kernel_bounded_theorem_note_2026-10-10
runner: scripts/chiral_pair_one_swapped_dot_scale_two_cap_multiples_partner_kernel_2026_10_10.py
---

# One positive scale of a swapped-dot generator plus two cap multiples

**Date:** 2026-10-12

**Type:** open_gate

**Audit:** unset; independent audit remains a separate lane

**Status:** open_gate

**Status authority:** independent audit only. This source changes no axiom,
primitive, framework rule, or audit verdict.

**Primary runner:**
[`scripts/chiral_pair_one_swapped_dot_scale_two_cap_multiples_partner_kernel_2026_10_10.py`](../scripts/chiral_pair_one_swapped_dot_scale_two_cap_multiples_partner_kernel_2026_10_10.py)

**Parents:** the [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md),
[the even span](CHIRAL_PAIR_EVEN_SPAN_PARTNER_KERNEL_BOUNDED_THEOREM_NOTE_2026-10-10.md),
and [the two ratio spans](CHIRAL_PAIR_TWO_PARITY_EXCLUDED_PARTNER_KERNEL_BOUNDED_THEOREM_NOTE_2026-10-10.md).

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: open_gate
claim_type_reason: "On every ordered height pair, t times one swapped-dot generator plus every pair of positive cap multiples has partner rank 10 at every chirality coefficient, for every positive integer t."
trace_class: negative_route_pruning
target_claim_id: null
target_blocker_text: "Other generic orbits and higher-rank bond spaces are not classified."
source_of_blocker_text: frontier_question
reachability_to_target: prunes
artifact_role: partial_narrowing_proposal
next_trace_action: "Decide whether every triple of positive integers (t, r, s) gives partner rank 10, at every chirality coefficient, for t times both swapped-dot generators plus r times the plus cap and s times the minus cap. The case t = 1 is settled. Do not claim the ten-kernel coefficient span is settled."
conditional_surface_status: "every ordered height pair; t times one swapped-dot generator plus every pair of positive cap multiples"
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

**Target.** On every ordered height pair, decide whether every triple of
positive integers `(t, r, s)` gives partner rank 10 at every chirality
coefficient on the sum of `t` times one swapped-dot generator, `r` times
the plus cap, and `s` times the minus cap.

**Ansatz.** There are two sums. The plus-dot sum has swapped-dot
coordinate `t`. The minus-dot sum has swapped-dot coordinate `-t`. Each
has swapped coordinate `-t`, orthogonal coordinate `t`, transverse-sign
coordinate `s-r`, sign-product coordinate `s-r`, matched coordinate
`2r+2s`, and scaled coordinate `2r+2s`. The two sums are linearly
independent for every positive integer `t`. Each lies in neither ratio
span and outside the even space. Both swapped-dot generators are not
this ansatz. The ten-kernel coefficient span is not this ansatz. The
full soldered bond space is not classified.

The kernel cross sum on two perpendicular directions is the sum of the
products of the two centre values. This note does not convert that sum
into an alphabet mean.

**Conclusion.** On every ordered height pair, every triple of positive
integers `(t, r, s)` gives partner rank 10 at every chirality
coefficient, for each of the two sums.

**Proof.** The runner enumerates the proper rotations and the alphabet
and builds the ten kernels. The coordinate identity is linear, so the
three parameter axes determine it, and the point `(2, 3, 5)` agrees.
Membership in each ratio span, and in the even space of each ordered
height pair, is the vanishing of linear forms in `(t, r, s)`. Those
forms have no strictly positive rational zero, so each sum lies outside
for every positive integer triple. Each compressed partner row is the
linear form `t` times the swapped-dot row plus `r` times the plus-cap
row plus `s` times the minus-cap row plus `c` times the chirality row.
For `t` nonzero, the row at `(t, r, s, c)` equals `t` times the row at
`(1, r/t, s/t, c/t)`. Every maximal minor therefore scales by `t^10`.
The runner checks the row identity on every compressed row at
`(2, 3, 5, 1)`, and checks that one nonzero maximal minor scales by
`2^10`. The rank certificate uses the full selected family of maximal minors,
not a resultant of two original minors. The runner factors the first
nonzero minor into factors linear in chirality `c`. For each factor
`a(r,s)c+b(r,s)`, it verifies that either `a` or `b` is nonzero on the
strictly positive parameter domain by exact factorization and
same-sign coefficients. If `a = 0`, a nonzero `b` excludes this branch;
otherwise it substitutes `c = -b/a` into every selected minor and
finds one whose reduced numerator is a product of factors with
strictly same-sign nonzero coefficients. That minor cannot vanish on
this branch for positive `r,s`. Chirality-independent factors of the
first minor are checked nonzero in the same way. This exhausts every
possible zero of the first minor, so the selected minors have no common
chirality zero. The argument holds for positive real parameters;
in particular it applies to the positive rational parameters `r/t,s/t`
used in the scaling argument when present. The exact interpolated
minor identities and the row-scaling identity supply the matrix link.
The legacy elimination expression remains a diagnostic: taking a
polynomial gcd before specialization does not by itself exclude extra
common roots after specialization. No claim that two original maximal
minors have a nonzero resultant is made. At heights 1 and 2 the bond on `-e_x` and `-e_y` has lefts
`(-1, -2, -3)` and `(-1, -2, 3)`. Against the chirality cap, each sum
has rights `(1, -3, -2)` and `(-3, 2, -1)`. The partner centre pair is
`(1, -1)`. For the plus-dot sum the source centres are `-2t-4r` and
`0`, so the centre pairs are `(-2t-4r, 1)` and `(0, -1)` and the kernel
cross sum is `-2t-4r`. For the minus-dot sum the source centres are
`-4r` and `0`, so the centre pairs are `(-4r, 1)` and `(0, -1)` and
the kernel cross sum is `-4r`. Neither cross sum depends on `s`. The
plus-dot cross sum does not vanish for positive integers `t` and `r`.
The minus-dot cross sum does not vanish for a positive integer `r`.

**Obligations.** Proved here: `t` times one swapped-dot generator plus
`r` times the plus cap and `s` times the minus cap, for every triple of
positive integers `(t, r, s)`, on every ordered height pair, for every
chirality coefficient, for each of the two generators. Cited from the
even-span note, and not re-proved: the name of the even space. Cited
from the ratio-span note, and not re-proved: the names of the two
spans. The strongest missing lemma is whether every triple of positive
integers `(t, r, s)` gives partner rank 10, at every chirality
coefficient, for `t` times both swapped-dot generators plus `r` times
the plus cap and `s` times the minus cap.

## What this does not do

- It does not select a scale. The vectors are witnesses.
- It does not put both swapped-dot generators into this count.
- It does not claim that the pivot gcd degree is independent of `t`, `r`, and `s`.
- It does not claim that this resultant is the monic generator of least degree.
- It does not claim that the ten-kernel coefficient span is settled.
- It does not claim that the full soldered bond space is classified.
- It does not apply the order-blind converse.
- It does not convert a kernel cross sum into an alphabet mean.
- It does not repeat the bond-space dimension count.
- It does not return to the modulus-3 triple.
- It does not supply a formation site, probability, or rate.

## Runner

`scripts/chiral_pair_one_swapped_dot_scale_two_cap_multiples_partner_kernel_2026_10_10.py`
checks the coordinate identity, the span obstructions, the scale
identity, and the positive-parameter branch certificates and diagnostic elimination polynomials. `TOTAL: PASS=10 FAIL=0`.

## Imports

No formation site, probability, rate, or selected scale is imported.
The proper rotations, the stacked partner kernel, and the elimination
polynomials are enumerated here. The even-span note names the even
space. The ratio-span note names the two spans. The order-blind
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

## Review correction: parameter specialization

The original proof called a gcd-based derived expression the resultant
of two maximal minors. Those minors can share a quadratic factor.
The runner now requires the exact branch certificate above before
accepting its diagnostic expression. This repairs the proof without
extending the ansatz or the no-go packet status.
