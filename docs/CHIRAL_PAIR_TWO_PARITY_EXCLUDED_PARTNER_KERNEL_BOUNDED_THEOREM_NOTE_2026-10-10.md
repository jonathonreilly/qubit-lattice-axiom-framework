---
claim_id: chiral_pair_two_parity_excluded_partner_kernel_bounded_theorem_note_2026-10-10
claim_type: open_gate
claim_scope: "On the 48 signed permutations of (1, 2, 3), let V+ be the rational span of the matched cross plus the matched oblique dot, of minus the swapped transverse cross plus the swapped transverse dot plus the orthogonal swapped cross, and of minus the transverse-sign cap minus the sign product plus twice the matched cross plus twice the scaled cross-dot kernel. Let V- be spanned by minus the matched cross plus the matched oblique dot; minus the swapped transverse cross minus the swapped transverse dot plus the orthogonal swapped cross; and the transverse-sign cap plus the sign product plus twice the matched cross plus twice the scaled cross-dot kernel. Each span has dimension 3. A nonzero vector in either span has two or more nonzero parity-kernel coefficients and a nonzero excluded coefficient exactly when it is not on that span's oblique-matched line. For every ordered pair of absolute heights among 1, 2, and 3, every nonzero vector in V+ or in V- has a three-dimensional partner kernel. On height pairs (1, 2), (2, 1), (2, 3), and (3, 2) the partner kernel of each span is itself. On height pairs (1, 3) and (3, 1) the two spans exchange. In particular, minus the swapped cross plus the swapped transverse dot plus the orthogonal cross at height 1 has every kernel cross sum equal to 0 against the matched-plus-oblique vector at height 2. On -e_x and -e_y the lefts are (-1, -2, -3) and (-1, -2, 3), the rights are (1, -3, -2) and (-1, 2, -3), and the centre pairs are (-2, 0) and (0, 2). The same vectors at heights 1 and 3 have centre pairs (0, 0) and (-2, 2) and kernel cross sum -4. A vector outside both spans is not in this count. The ten-kernel coefficient span is not classified. The full soldered bond space is not classified. No scale is selected."
upstream_dependencies:
  - minimal_axioms
  - chiral_pair_one_parity_one_excluded_cross_moments_bounded_theorem_note_2026-10-10
  - chiral_pair_cross_height_parity_span_cross_moments_bounded_theorem_note_2026-10-10
  - chiral_pair_scaled_cross_dot_bases_opposite_height_ansatz_bounded_theorem_note_2026-10-10
runner: scripts/chiral_pair_two_parity_excluded_partner_kernel_2026_10_10.py
---

# Two parity kernels plus an excluded kernel

**Date:** 2026-10-11

**Type:** open_gate

**Audit:** unset; independent audit remains a separate lane

**Status:** open_gate

**Status authority:** independent audit only. This source changes no axiom,
primitive, framework rule, or audit verdict.

**Primary runner:**
[`scripts/chiral_pair_two_parity_excluded_partner_kernel_2026_10_10.py`](../scripts/chiral_pair_two_parity_excluded_partner_kernel_2026_10_10.py)

**Parents:** the [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md),
[the one-parity plane note](CHIRAL_PAIR_ONE_PARITY_ONE_EXCLUDED_CROSS_MOMENTS_BOUNDED_THEOREM_NOTE_2026-10-10.md),
[the parity-span note](CHIRAL_PAIR_CROSS_HEIGHT_PARITY_SPAN_CROSS_MOMENTS_BOUNDED_THEOREM_NOTE_2026-10-10.md),
and the [scaled cross-dot basis note](CHIRAL_PAIR_SCALED_CROSS_DOT_BASES_OPPOSITE_HEIGHT_ANSATZ_BOUNDED_THEOREM_NOTE_2026-10-10.md).

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: open_gate
claim_type_reason: "Inside the two named three-dimensional spans, every nonzero vector has a three-dimensional partner kernel, and that kernel is the same span or the other span according to the height pair."
trace_class: negative_route_pruning
target_claim_id: null
target_blocker_text: "Other generic orbits and higher-rank bond spaces are not classified."
source_of_blocker_text: frontier_question
reachability_to_target: prunes
artifact_role: partial_narrowing_proposal
next_trace_action: "Decide whether the sum of the chirality cap, the transverse-sign cap, and the matched transverse cross can pair with a nonzero ten-kernel vector and still have every cross moment equal to 0. That vector lies outside both spans. Do not claim the ten-kernel coefficient span is settled."
conditional_surface_status: "48 signed permutations of (1, 2, 3); the two ratio spans of the oblique-matched plane; witness directions (-1, 0, 0) and (0, -1, 0)"
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
a vector with two or more nonzero parity-kernel coefficients and a
nonzero excluded coefficient can pair with a nonzero ten-kernel vector
and still have every kernel cross sum equal to 0.

**Ansatz.** The parity kernels are the chirality cap, the transverse-sign
cap, their sign product, the swapped transverse cross, the parallel
transverse dot, the matched oblique dot, and the orthogonal swapped
cross. The excluded kernels are the matched transverse cross, the
swapped transverse dot, and the scaled cross-dot kernel. The ansatz is
two rational spans. `V+` is spanned by

- the matched cross plus the matched oblique dot,
- minus the swapped transverse cross, plus the swapped transverse dot,
  plus the orthogonal swapped cross,
- minus the transverse-sign cap, minus the sign product, plus twice
  the matched cross, plus twice the scaled cross-dot kernel.

`V-` is spanned explicitly by

- minus the matched cross plus the matched oblique dot,
- minus the swapped transverse cross, minus the swapped transverse dot,
  plus the orthogonal swapped cross,
- the transverse-sign cap plus the sign product, plus twice the matched
  cross and twice the scaled cross-dot kernel.

The matched coefficient in the third generator remains `+2`. A global
matched-coordinate sign reversal would define a different, incorrect span.
Each span has dimension 3. A vector outside both spans is not in this
count. The ten-kernel coefficient span is not this ansatz. The full
soldered bond space is not classified.

The kernel cross sum on two perpendicular directions is the sum of the
products of the two centre values. This note does not convert that sum
into an alphabet mean.

**Conclusion.** Write a vector of either span as `s1` times the
oblique-matched generator, plus `s2` times the swapped-orthogonal
generator, plus `s3` times the cap generator. For a nonzero vector, two
or more parity-kernel coefficients are nonzero and some excluded
coefficient is nonzero if and only if `s2` or `s3` is nonzero. That is
exactly the complement of the oblique-matched line.

Let `x` be any nonzero vector in `V+` or in `V-`, and let the other
height be any of the two heights different from its own, among
`{1, 2, 3}`. The ten-kernel vectors `y` with every kernel cross sum
equal to 0 form a three-dimensional space. On the ordered pairs
`(1, 2)`, `(2, 1)`, `(2, 3)`, and `(3, 2)`, that space is the span
containing `x`. On the ordered pairs `(1, 3)` and `(3, 1)`, it is the
other span.

In particular, minus the swapped cross plus the swapped transverse dot
plus the orthogonal cross has two nonzero parity coefficients and one
nonzero excluded coefficient. At height 1, every kernel cross sum
against the matched-plus-oblique vector at height 2 is 0. On `-e_x`
and `-e_y`, the lefts are `(-1, -2, -3)` and `(-1, -2, 3)`, the rights
are `(1, -3, -2)` and `(-1, 2, -3)`, and the centre pairs are
`(-2, 0)` and `(0, 2)`. The same two vectors at heights 1 and 3 do not
pair. The lefts are `(-1, -3, -2)` and `(-1, -3, 2)`, the rights are
`(1, -2, 3)` and `(-1, 3, -2)`, the centre pairs are `(0, 0)` and
`(-2, 2)`, and the kernel cross sum is `-4`.

**Proof.** The runner enumerates the proper rotations and the alphabet
and builds the ten kernels. The three generators of each span are
independent. Their parity supports are disjoint: the oblique-matched
line meets only the oblique dot, the swapped-orthogonal generator meets
only the swapped cross and the orthogonal cross, and the cap generator
meets only the transverse-sign cap and the sign product. The swapped
transverse dot appears only on the swapped-orthogonal generator, and
the scaled kernel appears only on the cap generator. A coefficient
`s2` therefore makes both of those parity entries and the swapped-dot
entry nonzero, and a coefficient `s3` makes both cap entries and the
scaled entry nonzero. The matched coefficient is `s1 + 2 s3` on `V+`
and `-s1 + 2 s3` on `V-`, so it can vanish while `s3` does not. The
vectors with `(s1, s2, s3) = (-2, 0, 1)` on `V+` and `(2, 0, 1)` on
`V-` have matched coefficient 0 and still meet the pattern. The only
nonzero vectors that miss the pattern are the oblique-matched lines.

On each ordered height pair, the live bonds of either span fall into
two kinds. In the first kind the oblique-matched partner row is
nonzero, the swapped-orthogonal partner row is 0, and the cap partner
row is `2` or `-2` times the oblique-matched row. In the second kind
the oblique-matched row is 0 and the cap row is `2` or `-2` times the
swapped-orthogonal row. Both signs occur in both kinds. The nonzero
rows use eight directions in the ten-kernel coordinate space. Those
eight directions have rank 7, and each of the four kind-and-sign
classes contains all eight.

A combination with coefficients `(s1, s2, s3)` therefore has partner
row `(s1 + 2 ε s3)` times the oblique-matched row on a first-kind bond
of sign `ε`, and `(s2 + 2 ε s3)` times the swapped-orthogonal row on a
second-kind bond of sign `ε`. The four scalars are the image of a
`4` by `3` matrix of rank 3, so they vanish together only at the zero
coefficient vector. A nonzero combination makes at least one scalar
nonzero. That class contributes all eight directions, and the partner
rank is 7. The kernel dimension is 3, and every nonzero vector in the
span has this same kernel.

On height pairs `(1, 2)`, `(2, 1)`, `(2, 3)`, and `(3, 2)`, the three
generators of the same span are orthogonal to those eight directions.
On height pairs `(1, 3)` and `(3, 1)`, the three generators of the
other span are the orthogonal triple. In each case the direct partner
rows of the swapped-orthogonal generator have rank 7 and annihilate
that triple, so the triple is the partner kernel. The two witness
bonds are direct centre sums.

**Obligations.** Proved here: the two spans, the parity-and-excluded
pattern off each oblique-matched line, the four bond classes and the
eight directions, the partner kernel on every ordered height pair, and
the centre pairs `(-2, 0)`, `(0, 2)`, `(0, 0)`, and `(-2, 2)` with
cross sums `0` and `-4`. Cited from the parity-span note, and not
re-proved: the seven kernels named above are the parity span, and the
other three are outside it. Cited from the basis note, and not
re-proved: those ten kernels are a basis of one opposite-height
ansatz. Cited from the one-parity plane note, and not re-proved: these
two triples are the partner kernels of the oblique-matched plane at
ratios `1` and `-1`. The strongest missing lemma is whether the sum of
the chirality cap, the transverse-sign cap, and the matched transverse
cross can pair with a nonzero ten-kernel vector and still have every
cross moment equal to 0. That vector lies outside both spans.

## What this does not do

- It does not select a scale. The coefficients are witnesses.
- It does not take a vector outside `V+` and `V-`.
- It does not re-prove the parity span, the excluded span, or the
  one-parity planes.
- It does not claim that the ten-kernel coefficient span is settled.
- It does not claim that the full soldered bond space is classified.
- It does not apply the order-blind converse.
- It does not convert a kernel cross sum into an alphabet mean.
- It does not repeat the bond-space dimension count.
- It does not return to the modulus-3 triple.
- It does not supply a formation site, probability, or rate.

## Runner

`scripts/chiral_pair_two_parity_excluded_partner_kernel_2026_10_10.py`
checks the two spans, the bond classes, the partner kernels, and the
two witness bonds. `TOTAL: PASS=10 FAIL=0`.

## Imports

No formation site, probability, rate, or selected scale is imported.
The proper rotations, the bond classes, and the witness sums are
enumerated here. The parity-span note names the seven parity kernels.
The basis note supplies the ten-kernel basis. The one-parity plane note
names these two triples as partner kernels of the oblique-matched
plane. The order-blind converse is not applied.


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
