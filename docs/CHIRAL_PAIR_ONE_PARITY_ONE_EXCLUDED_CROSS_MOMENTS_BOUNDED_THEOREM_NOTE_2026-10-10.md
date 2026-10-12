---
claim_id: chiral_pair_one_parity_one_excluded_cross_moments_bounded_theorem_note_2026-10-10
claim_type: open_gate
claim_scope: "On the 48 signed permutations of (1, 2, 3), take one kernel from the parity span and one kernel from the excluded span. If the two kernels are not the matched oblique dot and the matched transverse cross, a vector with both coefficients nonzero has every kernel cross sum against a ten-kernel partner equal to 0 exactly when the partner is 0. In the oblique-matched plane the matched coefficient over the oblique coefficient has a partner kernel exactly at the ratios plus and minus 1, where that kernel has dimension 3. On height pairs (1, 2) and (2, 3) the ratio plus 1 has basis matched plus oblique, minus swapped plus swapped-dot plus orthogonal, and minus the transverse sign minus the sign product plus twice matched plus twice scaled. The ratio minus 1 has basis minus matched plus oblique, minus swapped minus swapped-dot plus orthogonal, and the transverse sign plus the sign product plus twice matched plus twice scaled. On the height pair (1, 3) those two bases are exchanged. Oblique plus matched at heights 1 and 2 has every cross sum equal to 0 against itself. The same vector at heights 1 and 3 has witness cross sum -4. Chirality plus matched against the chirality cap has witness cross sum 2. Oblique plus twice matched against oblique has witness cross sum -1. A sum of two parity kernels is outside this ansatz. The ten-kernel coefficient span is not classified. The full soldered bond space is not classified. No scale is selected."
upstream_dependencies:
  - minimal_axioms
  - chiral_pair_excluded_kernel_span_cross_moments_bounded_theorem_note_2026-10-10
  - chiral_pair_cross_height_parity_span_cross_moments_bounded_theorem_note_2026-10-10
  - chiral_pair_scaled_cross_dot_bases_opposite_height_ansatz_bounded_theorem_note_2026-10-10
runner: scripts/chiral_pair_one_parity_one_excluded_cross_moments_2026_10_10.py
---

# One parity kernel plus one excluded kernel

**Date:** 2026-10-10

**Type:** open_gate

**Audit:** unset; independent audit remains a separate lane

**Status:** open_gate

**Status authority:** independent audit only. This source changes no axiom,
primitive, framework rule, or audit verdict.

**Primary runner:**
[`scripts/chiral_pair_one_parity_one_excluded_cross_moments_2026_10_10.py`](../scripts/chiral_pair_one_parity_one_excluded_cross_moments_2026_10_10.py)

**Parents:** the [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md),
[the excluded-span note](CHIRAL_PAIR_EXCLUDED_KERNEL_SPAN_CROSS_MOMENTS_BOUNDED_THEOREM_NOTE_2026-10-10.md),
[the parity-span note](CHIRAL_PAIR_CROSS_HEIGHT_PARITY_SPAN_CROSS_MOMENTS_BOUNDED_THEOREM_NOTE_2026-10-10.md),
and the [scaled cross-dot basis note](CHIRAL_PAIR_SCALED_CROSS_DOT_BASES_OPPOSITE_HEIGHT_ANSATZ_BOUNDED_THEOREM_NOTE_2026-10-10.md).

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: open_gate
claim_type_reason: "In each plane spanned by one parity kernel and one excluded kernel, the partner kernel is known: it is zero except on the oblique-matched plane at ratios plus and minus 1."
trace_class: negative_route_pruning
target_claim_id: null
target_blocker_text: "Other generic orbits and higher-rank bond spaces are not classified."
source_of_blocker_text: frontier_question
reachability_to_target: prunes
artifact_role: partial_narrowing_proposal
next_trace_action: "Decide whether a vector with two or more nonzero parity-kernel coefficients and a nonzero excluded coefficient can pair with a nonzero ten-kernel vector and still have every cross moment equal to 0. Do not claim the ten-kernel coefficient span is settled."
conditional_surface_status: "48 signed permutations of (1, 2, 3); one parity kernel plus one excluded kernel; witness directions (-1, 0, 0) and (0, -1, 0)"
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

**Target.** On the 48 signed permutations of `(1, 2, 3)`, decide which
vectors that use one parity-span kernel and one excluded kernel have
every kernel cross sum equal to 0 against a ten-kernel partner.

**Ansatz.** The parity kernels are the chirality cap, the transverse-sign
cap, their sign product, the swapped transverse cross, the parallel
transverse dot, the matched oblique dot, and the orthogonal swapped
cross. The excluded kernels are the matched transverse cross, the
swapped transverse dot, and the scaled cross-dot kernel. The ansatz is
one plane spanned by one kernel from each list. There are 21 such
planes. A sum of two parity kernels lies outside every one of them. A
vector with parity coefficient 0 lies in the excluded span and is not
re-proved here. The ten-kernel coefficient span is not this ansatz.
The full soldered bond space is not classified.

The kernel cross sum on two perpendicular directions is the sum of the
products of the two centre values. This note does not convert that sum
into an alphabet mean.

**Conclusion.** Let `P` be one parity kernel, let `E` be one excluded
kernel, and let `x = s P + t E` with `s` and `t` rational and both
nonzero. Let `y` be any ten-kernel vector at the other height. This
holds for every ordered pair of heights among `{1, 2, 3}`.

If `{P, E}` is not the matched oblique dot together with the matched
transverse cross, every kernel cross sum vanishes if and only if `y`
is 0.

If `P` is the matched oblique dot and `E` is the matched transverse
cross, write `r = t / s`. The partner rank is 7 when `r` is `1` or
`-1`, and it is 10 for every other rational `r`. Thus a nonzero
partner exists exactly at those two ratios. At each of them the
partner kernel has the following basis. On the unordered height pairs
`{1, 2}` and `{2, 3}`, and in both orders, the ratio `1` has basis

- matched plus oblique,
- minus swapped, plus swapped-dot, plus orthogonal,
- minus the transverse sign, minus the sign product, plus twice
  matched, plus twice scaled.

The ratio `-1` has basis

- minus matched plus oblique,
- minus swapped, minus swapped-dot, plus orthogonal,
- the transverse sign plus the sign product plus twice matched plus twice scaled.

The cap generator retains its positive twice-matched coefficient. On
the unordered height pair `{1, 3}`, in both orders, those two bases
are exchanged.

In particular, oblique plus matched at height 1 against the same
vector at height 2 has every kernel cross sum equal to 0. The same
pair of vectors at heights 1 and 3 does not. On `-e_x` and `-e_y`,
the lefts are `(-1, -3, -2)` and `(-1, -3, 2)`, the rights are
`(1, -3, -2)` and `(-1, 3, -2)`, the centre values are `(0, 0)` and
`(-2, 2)`, and the kernel cross sum is `-4`.

Chirality plus matched at height 1, against the height-2 chirality
cap, fails on `-e_x` and `-e_y`. The lefts are `(-1, -2, -3)` and
`(-1, -2, 3)`. The rights are `(1, -3, -2)` and `(-3, 2, -1)`. The
centre values are `(1, 1)` and `(-1, -1)`. The kernel cross sum is
`2`.

Oblique plus twice matched, against oblique, fails on the same
directions at heights 1 and 2. The lefts are `(-1, -2, -3)` and
`(-1, -2, 3)`. The rights are `(1, -2, -3)` and `(-1, 2, -3)`. The
centre values are `(0, 0)` and `(-1, 1)`. The kernel cross sum is
`-1`.

**Proof.** The runner enumerates the proper rotations and the alphabet
and builds the ten kernels. For each ordered height pair and each of
the 21 planes it selects ten bonds whose rows are independent at a
generic ratio, and it computes the determinant of `P + r E` on those
bonds. A drop of the partner rank below 10 would make that determinant
vanish. For the twenty planes other than oblique plus matched, every
rational root at which the numeric rank is below 10 is `r = 0`. Both
coefficients are nonzero only for `r` nonzero, so the partner rank is
10 and the only partner is 0.

For oblique plus matched the same determinant, pivoted at ratio 2, has
rational roots exactly `1` and `-1`. The numeric rank is 7 at both
roots and 10 at ratio 2. The three named vectors are linearly
independent and lie in the kernel, so they are a basis. The runner
checks both orders of each height pair, with the two bases exchanged
on `{1, 3}`. The zero scan and the three witness bonds are direct
centre sums.

**Obligations.** Proved here: the twenty full-rank planes, the two
special ratios, the two kernel bases and the height pair that exchanges
them, the zero scan at heights 1 and 2, and the witness sums `2`,
`-4`, and `-1`. Cited from the parity-span note, and not re-proved:
those seven kernels are the parity span. Cited from the excluded-span
note, and not re-proved: a vector in the excluded span pairs with a
ten-kernel vector only when one of them is 0. Cited from the basis
note, and not re-proved: the ten named kernels are a basis of one
opposite-height ansatz. The strongest missing lemma is whether a
vector with two or more nonzero parity-kernel coefficients and a
nonzero excluded coefficient can pair with a nonzero ten-kernel vector
and still have every cross moment equal to 0.

## What this does not do

- It does not select a scale. The coefficients are witnesses.
- It does not take a sum of two parity kernels.
- It does not re-prove the excluded span or the parity span.
- It does not claim that the ten-kernel coefficient span is settled.
- It does not claim that the full soldered bond space is classified.
- It does not apply the order-blind converse.
- It does not convert a kernel cross sum into an alphabet mean.
- It does not repeat the bond-space dimension count.
- It does not return to the modulus-3 triple.
- It does not supply a formation site, probability, or rate.

## Runner

`scripts/chiral_pair_one_parity_one_excluded_cross_moments_2026_10_10.py`
checks the twenty planes, the two special ratios, and the witnesses.
`TOTAL: PASS=10 FAIL=0`.

## Imports

No formation site, probability, rate, or selected scale is imported.
The proper rotations, the partner determinants, and the witness sums
are enumerated here. The parity-span note names the seven parity
kernels. The excluded-span note settles a vector with parity
coefficient 0. The basis note supplies the ten-kernel basis. The
order-blind converse is not applied.


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
