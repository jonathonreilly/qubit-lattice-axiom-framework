---
claim_id: two_ball_witness_chiral_mask_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Whether the two-ball unread witness occupancy mask (1,1,1,0,1,0) appears among the July-3 k=3 chiral-pair 6-tuples, and whether any {+,−} labeling of its four occupied slots is a pair member, is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_covariance_extension_classification_openness_achiral_oriented_frame_minimal_chiral_channel_bounded_theorem_note_2026-07-03
runner: scripts/two_ball_witness_chiral_mask_2026_08_15.py
---

# Two-Ball Witness Occupancy Mask Against The July-3 k=3 Chiral Pair

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact occupancy-mask comparison of one unread 6-nearest-neighbor
star against the 48 July-3 `k = 3` chiral-pair 6-tuples, then exact
`{+,−}` filling of the four occupied slots. Displayed, not adopted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/two_ball_witness_chiral_mask_2026_08_15.py`](../scripts/two_ball_witness_chiral_mask_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)
and the July-3 classification
[`ADMISSIBILITY_RULE_COVARIANCE_EXTENSION_CLASSIFICATION_OPENNESS_ACHIRAL_ORIENTED_FRAME_MINIMAL_CHIRAL_CHANNEL_BOUNDED_THEOREM_NOTE_2026-07-03.md`](ADMISSIBILITY_RULE_COVARIANCE_EXTENSION_CLASSIFICATION_OPENNESS_ACHIRAL_ORIENTED_FRAME_MINIMAL_CHIRAL_CHANNEL_BOUNDED_THEOREM_NOTE_2026-07-03.md).

## Result Up Front

Direction order is `(+x, −x, +y, −y, +z, −z)`. The two-ball unread witness
at `v = (1,-1,-1)` for `U = B_2(0) ∪ B_2((2,0,0))` occupies exactly
`(+x, −x, +y, +z)` and leaves `(−y, −z)` empty. Its occupancy mask is

```text
m = (1, 1, 1, 0, 1, 0)
```

with `1` occupied and `0` empty.

July-3 Theorem 3 isolates a unique chiral pair at three condition letters.
Letters here are `{0, +, −}` with `0` empty. The pair is the union of two
`G+` orbits and has `N_pair = 48` members. Every member has empty slots in
exactly two of the six directions.

Of those 48, `N_mask = 4` have empty slots exactly where `m` is `0`. The
mask therefore appears. Among the `16` assignments of `{+, −}` to the four
occupied slots, `N_fire = 4` are pair members. The lex-first firing
labeling, under the letter order `0 < + < −`, is

```text
(+, −, +, 0, −, 0).
```

This is not leftover-char of the two-ball occupied-NN count, which asked
only whether any unread site reaches four occupied neighbors. It is not
leftover-char of the pair occupied-slot census, which asked only the
occupied-slot histogram on the 48 members. The residual here is the mask
and the signed filling of that one 6-NN star at `v`.

The comparison is displayed, not adopted. Do not write the mask into
Admissibility. Do not attach L1.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Finite occupancy-mask match of one 6-NN star against the 48 pair members, and the 16 signed fillings of the occupied slots, are exact; no axiom sentence is rewritten."
trace_class: negative_route_pruning
target_claim_id: two_ball_witness_chiral_mask
target_blocker_text: "whether the two-ball unread witness occupancy mask (1,1,1,0,1,0) appears among the July-3 k=3 pair 6-tuples, and whether any {+,−} labeling of its four occupied slots is a pair member"
source_of_blocker_text: handoff
reachability_to_target: prunes
artifact_role: theorem
conditional_surface_status: "exact on the July-3 named k=3 alphabet and the one two-ball 6-NN star at v; displayed, not adopted"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
next_trace_action: "independent audit of the mask and firing counts; do not write the mask into Admissibility and do not attach L1"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Inputs And Import Boundary

Quoted from the live memo, verbatim:

```text
Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor adjacency, standard translations, and proper cubic rotations about each site.

There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations.

For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.

A site with no record cannot be read.
```

This note does not choose that rule and does not add a mask clause to it.
Letter `0` is the empty/unread letter on the July-3 three-letter model.
Occupied means nonzero. The note does not assign a readout value to
absence.
- **July-3 Theorem 3.** At `k = 3` there is exactly one chiral pair, whose
  members are the handed fully-mixed patterns: every axis bi-colored with
  two distinct values, every value used twice. The runner re-earns the
  pair by enumerating `G+` orbits; it does not import an external list.
- **Two-ball witness, re-earned here.** Only the union `p = (2,0,0)`,
  `r = s = 2` presents four occupied nearest neighbors to an unread site.
  The lex-first such site is `v = (1,-1,-1)`. The runner rebuilds that
  star; it does not import a stored mask.
- **External empirical inputs:** none.
- **Not attached:** L1 is not a premise and is not a conclusion. The
  mask match is not leftover-char of the two-ball count or of the pair
  census.

## Exact Objects

The six nearest-neighbor directions, in the July-3 order, are

```text
(+x, −x, +y, −y, +z, −z).
```

The closed ℓ¹ ball is `B_r(c) = { x in Z^3 : ||x − c||_1 ≤ r }`. The
two-ball occupied set used here is only

```text
U = B_2(0) ∪ B_2((2,0,0)).
```

The unread witness is the single site `v = (1,-1,-1)`. Its 6-NN star is

```text
v + {+e_1, −e_1, +e_2, −e_2, +e_3, −e_3}.
```

Occupancy of a neighbor is membership in `U`. The occupancy mask is the
`{0,1}` 6-tuple in the direction order above. No other site is scored.

A `k = 3` condition 6-tuple is an element of `{0, +, −}^6`. Letter `0` is
empty. The occupancy of a 6-tuple `c` is

```text
occ_mask(c)_i = 0 if c_i = 0 else 1.
```

`G+` is the 24-element proper cubic group of determinant-`+1` signed
permutation matrices. It acts on 6-tuples by the induced permutation of
the six axis directions. Spatial inversion `P = −I` is the central
improper element. A chiral pair is a pair of distinct `G+` orbits
exchanged by `P`. July-3 Theorem 3 states there is exactly one such pair
at `k = 3`. Write `Pair` for the union of those two orbits, and
`N_pair = |Pair|`.

The 16 candidate fillings of the witness star are the 6-tuples that carry
`0` wherever `m` is `0` and a letter from `{+, −}` wherever `m` is `1`.
Letter order for lex comparison is `0 < + < −`.

## Theorem 1 — Mask Count On The Unique Pair

`N_pair = 48`. Exactly `N_mask = 4` members of `Pair` have empty slots
exactly where `m` is `0`.

*Proof.* The 24 proper signed permutation matrices are generated
exhaustively. Their action on the 729 colorings `{0, +, −}^6` partitions
them into 57 `G+` orbits, matching the July-3 Burnside count. Exactly two
of those orbits fail to meet their `P`-images; they form one pair, and
each has size 24, so `N_pair = 48`. Every pair member is fully mixed, so
letter `0` occurs twice and every member has exactly two empty slots.

Independently, the two-ball union `U` is constructed and the six axial
neighbors of `v` are tested for membership in `U`. The occupied neighbors
are `(2,-1,-1)`, `(0,-1,-1)`, `(1,0,-1)`, and `(1,-1,0)`; the empty
neighbors are `(1,-2,-1)` and `(1,-1,-2)`. That is the mask `m`.

Direct comparison of `occ_mask(c)` against `m` on all 48 pair members
yields four matches:

```text
(+, −, +, 0, −, 0)
(+, −, −, 0, +, 0)
(−, +, +, 0, −, 0)
(−, +, −, 0, +, 0).
```

Hence `N_mask = 4`. The occupancy mask appears among the pair members.

## Theorem 2 — Signed Fillings That Fire The Pair

Because `N_mask > 0`, the witness occupancy can host a pair member. Among
the 16 `{+, −}` assignments to the four occupied slots, `N_fire = 4` yield
a pair member. The lex-first firing labeling is `(+, −, +, 0, −, 0)`.

*Proof.* The 16 fillings are enumerated by assigning `{+, −}` independently
to the four occupied directions and leaving `−y` and `−z` empty. A filling
fires if and only if it lies in `Pair`. The four fillings listed in
Theorem 1 are exactly the firing set, so `N_fire = 4`. Under `0 < + < −`
the first of those four is `(+, −, +, 0, −, 0)`.

The remaining 12 fillings fail full mixing: they either repeat a letter
on the `±x` axis or fail the `2/2/2` letter counts. They therefore lie
outside `Pair`.

The witness can host the pair as an occupancy pattern, and four signed
labelings of that pattern are pair members. This is a support-mask
statement on the named `k = 3` model at one 6-NN star. It does not assert
that the physical admissibility rule is the chiral pair, and it does not
identify `{0, +, −}` with a derived physical alphabet.

## Theorem 3 — Displayed, Not Adopted

The mask `m`, the count `N_mask = 4`, and the firing count `N_fire = 4`
are a finite report on the July-3 named alphabet model and one two-ball
star. They are displayed. They are not adopted.

In particular:

- the mask is not written into Admissibility;
- no axiom sentence is edited;
- the comparison is not attached to L1.

Admissibility continues to say only that there is one fixed
nearest-neighbor rule, covariant under translations and proper cubic
rotations, and that the local distribution varies with the
nearest-neighbor conditions. Which occupancy mask a named test alphabet
and a named two-ball star happen to share is not that rule.

## What This Note Does And Does Not Claim

- **It does claim** that the two-ball unread witness occupancy mask
  `(1,1,1,0,1,0)` occurs on exactly four of the 48 July-3 `k = 3` pair
  members, and that four of the sixteen `{+, −}` fillings of its occupied
  slots are pair members, with lex-first firing labeling
  `(+, −, +, 0, −, 0)`.
- **It does not claim** leftover-char of the two-ball occupied-NN count.
  That count only asked whether four occupied neighbors occur. The present
  residual is which four directions they are, and whether that pattern
  sits inside the pair.
- **It does not claim** leftover-char of the pair occupied-slot census.
  That census only asked the occupied-slot histogram `{4: 48}`. The
  present residual is the location of the two empty slots and the signed
  filling.
- **It does not adopt** the mask as Admissibility content and does not
  attach L1.
- **It does not** score any site other than the 6-NN star at `v`, replace
  the six-neighbor stencil, select the physical condition alphabet, or
  decide whether the framework's fixed rule is chiral.

## Machine-Readable Report

```text
N_pair = 48
N_mask = 4
N_fire = 4
mask = (1, 1, 1, 0, 1, 0)
lex_first_firing = (+, -, +, 0, -, 0)
witness_can_host_pair_occupancy = true
displayed_not_adopted = true
attached_to_L1 = false
written_into_admissibility = false
```
