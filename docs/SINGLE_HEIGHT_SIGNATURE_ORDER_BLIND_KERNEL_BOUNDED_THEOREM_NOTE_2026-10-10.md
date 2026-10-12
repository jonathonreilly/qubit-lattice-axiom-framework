---
claim_id: single_height_signature_order_blind_kernel_bounded_theorem_note_2026-10-10
claim_type: open_gate
claim_scope: "On the proper orbit of (1, 2, 3), classify soldered bond-symmetric kernels supported on one reversal class of endpoint heights, with every slice sum equal to 0. There are 21 such classes, each with four bond orbits and kernel dimension 3. A nonzero kernel in this ansatz has every neighbour-product mean equal to 1 exactly when the two heights are opposite. Those six classes are spanned by the eighteen cap-pair kernels. On each of the other fifteen classes the only such kernel is zero. No scale is selected. A sum of two classes is not in this ansatz."
upstream_dependencies:
  - minimal_axioms
  - order_blind_nearest_neighbour_formation_independence_beyond_neighbours_unsoldered_constancy_and_soldered_escape_bounded_theorem_note_2026-09-22
runner: scripts/single_height_signature_order_blind_kernel_2026_10_10.py
---

# One height signature is order-blind only when the heights are opposite

**Date:** 2026-10-10

**Type:** open_gate

**Audit:** unset; independent audit remains a separate lane

**Status:** open_gate

**Status authority:** independent audit only. This source changes no axiom,
primitive, framework rule, or audit verdict.

**Primary runner:**
[`scripts/single_height_signature_order_blind_kernel_2026_10_10.py`](../scripts/single_height_signature_order_blind_kernel_2026_10_10.py)

**Parents:** the [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) and
[the order-blind formation note](ORDER_BLIND_NEAREST_NEIGHBOUR_FORMATION_INDEPENDENCE_BEYOND_NEIGHBOURS_UNSOLDERED_CONSTANCY_AND_SOLDERED_ESCAPE_BOUNDED_THEOREM_NOTE_2026-09-22.md).

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: open_gate
claim_type_reason: "A slice-zero kernel supported on one height signature is order-blind only for opposite heights, and those six kernels are the cap-pair span."
trace_class: negative_route_pruning
target_claim_id: null
target_blocker_text: "Other generic orbits and higher-rank bond spaces are not classified."
source_of_blocker_text: frontier_question
reachability_to_target: prunes
artifact_role: partial_narrowing_proposal
next_trace_action: "Ask whether a soldered order-blind kernel on two height signatures lies outside the eighteen cap-pair kernels. Search first. A negative answer must name the ansatz."
conditional_surface_status: "one proper orbit of (1, 2, 3); one height signature up to reversal; uniform average; one live direction on each opposite signature"
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

The parent note's converse: "Conversely every family with these
properties is order-blind on every window." It leaves the sentence
"Other generic orbits and higher-rank bond spaces are not classified."

## Theorem

**Landing status:** partial narrowing with an incomplete formal no-go packet.
The scoped arguments and exact checks below are preserved for development;
this note does not carry a no-go packet PASS or retained-grade authority.
The missing N1 route packet is distinct from the mathematical validity of
the finite ansatz results.

**Target.** Inside the ansatz of soldered bond-symmetric kernels on the
proper orbit of `(1, 2, 3)` that are supported on one height signature,
decide whether any order-blind kernel lies outside the eighteen
cap-pair kernels.

**Ansatz.** The height signature of a bond `(d, a, b)` is the
reversal-invariant pair of the two heights `a·d` and `b·d`. A kernel in
this ansatz may be nonzero only on the bonds of one signature. It is
unchanged by bond reversal, it transforms by the soldered proper
action, and every slice sums to 0.

**Conclusion.** The orbit carries 21 signatures. Each has four bond
orbits. The slice rows have rank 1 on each signature, so the kernel
dimension is 3. Six signatures have opposite heights `m` and `-m`. The
other fifteen do not: three have equal heights, and twelve have
unequal heights that are not opposites.

On an opposite signature every record activates one direction, and
every pair moment vanishes. Thus

`phi_d(a, b) = 1 + t L_d(a, b)`

has neighbour-product mean 1 for every scale `t`. The eighteen cap and
transverse-cross kernels are supported on these six signatures, are
linearly independent, and span each of the six kernels. Their values
lie in `{-1, 0, 1}`. For `|t| < 1` each of those eighteen families is
positive. The parent converse makes each order-blind on every window.
Every kernel in an opposite signature is a rational combination of
three of them, so it does not leave the cap-pair span.

On each of the twelve unequal signatures the pair-moment quadrics span
all six monomials in the three kernel coordinates. The squares of the
coordinates are therefore moments, and the only common zero is the
origin. On each equal-height signature the moments reduce to

`x^2 + xy + xz - yz = 0`,

`y^2 + xy - xz + yz = 0`,

`z^2 + xy + xz + yz = 0`.

The third polynomial is `(x+z)(y+z)`. If `x = -z`, the second becomes
`y^2 + z^2`, so `y = z = 0` and `x = 0`. If `y = -z`, the first becomes
`x^2 + z^2`, so `x = z = 0` and `y = 0`. Each of the fifteen
non-opposite signatures therefore has only the zero kernel with
vanishing pair moments. No order-blind kernel in this ansatz lies
outside the eighteen.

The witnesses, computed on the row-reduction basis, are the sum `-1`
for signature `(-3, -2)` on directions `-e_x` and `-e_y` at the right
records `(-3, 1, -2)` and `(-3, 2, 1)`, and the sum `1` for signature
`(-3, -3)` on directions `-e_x` and `e_x` at the right record
`(-3, -2, -1)` twice. The uniform averages are `-1/24` and `1/24`.

**Proof.** The runner enumerates the 24 proper rotations and the orbit.
It groups bond orbits by the reversal-invariant height pair, row-reduces
the slice sums, and evaluates the pair moments of each three-dimensional
kernel. Rank 6 of those moments forces the unequal coordinates to
vanish. The equal-height identities and the two substitutions are
checked as polynomial coefficients. The cap line and the matched and
swapped crosses are evaluated on the same orbits; row reduction shows
that they span the six opposite kernels and no other signature. One
live direction makes every product of two or more directions identically
zero, so the slice sums give every neighbour-product mean.

**Obligations.** Proved here: the signature count, the kernel
dimensions, the moment ranks, the equal-height case split, the
witnesses, and the identification of the opposite kernels with the
eighteen cap-pair kernels. Cited from the parent, and not re-proved:
the converse. The strongest missing lemma is whether a kernel supported
on two signatures can leave the eighteen. This note does not classify
that sum.

## What this does not do

- It does not select `t`.
- It does not claim that a sum of two height signatures is order-blind,
  or that every such sum lies in the cap-pair span.
- It does not claim that the 84-dimensional bond space has been
  classified. The slice-zero kernels that meet more than one signature
  stay open.
- It does not cut the normalised bond space on the 48-point alphabet.
- It does not supply a formation site, probability, or rate.

## Runner

`scripts/single_height_signature_order_blind_kernel_2026_10_10.py`
repeats the group, the signatures, the moment ranks, the case split,
and the spanning check.

## Imports

No formation site, probability, rate, or selected scale is imported.
The proper rotations, the height pairs, and the cap and cross values are
enumerated here. Order-blindness of a family that already meets the
product-mean conditions is the parent converse, quoted above.


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
