---
claim_id: two_ball_all_4nn_unique_axis_agree_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On U=B_2(0)∪B_2((2,0,0)) inside the radius-6 box, whether any unread 4-occupied-NN site has a July-3 pair member agreeing with that site’s unique-axis labels is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_covariance_extension_classification_openness_achiral_oriented_frame_minimal_chiral_channel_bounded_theorem_note_2026-07-03
runner: scripts/two_ball_all_4nn_unique_axis_agree_2026_08_15.py
---

# All 4-NN Unread Sites Of Two-Ball U Versus Unique-Axis Agreement

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact census, on the radius-6 box, of every unread site of
`U = B_2(0) ∪ B_2((2,0,0))` with four occupied six-neighbors, scored
against July-3 `k = 3` pair membership and occupancy-kernel unique-axis
labels. Displayed, not adopted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/two_ball_all_4nn_unique_axis_agree_2026_08_15.py`](../scripts/two_ball_all_4nn_unique_axis_agree_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)
and the July-3 classification
[`ADMISSIBILITY_RULE_COVARIANCE_EXTENSION_CLASSIFICATION_OPENNESS_ACHIRAL_ORIENTED_FRAME_MINIMAL_CHIRAL_CHANNEL_BOUNDED_THEOREM_NOTE_2026-07-03.md`](ADMISSIBILITY_RULE_COVARIANCE_EXTENSION_CLASSIFICATION_OPENNESS_ACHIRAL_ORIENTED_FRAME_MINIMAL_CHIRAL_CHANNEL_BOUNDED_THEOREM_NOTE_2026-07-03.md).

## Result Up Front

Direction order is `(+x, −x, +y, −y, +z, −z)`. Occupied set

```text
U = B_2(0) ∪ B_2((2,0,0))
```

is scored only inside the box `|x|,|y|,|z| ≤ 6`. An unread site is a box
point not in `U`. Occupied-NN count is how many of its six axial neighbors
lie in `U`.

Exactly `N_4 = 4` unread box sites have occupied-NN count `4`. They are
`(1,-1,-1)`, `(1,-1,1)`, `(1,1,-1)`, and `(1,1,1)`. For each, the occupancy
mask, the number of July-3 pair fillings `N_fire`, the number of
unambiguous unique-axis labels `N_unique_axis`, and the agreement count
`N_agree` are

| `v` | mask | `N_fire` | `N_unique_axis` | `N_agree` |
|---|---|---:|---:|---:|
| `(1,-1,-1)` | `(1,1,1,0,1,0)` | 4 | 2 | 0 |
| `(1,-1,1)` | `(1,1,1,0,0,1)` | 4 | 2 | 2 |
| `(1,1,-1)` | `(1,1,0,1,1,0)` | 4 | 2 | 2 |
| `(1,1,1)` | `(1,1,0,1,0,1)` | 4 | 2 | 0 |

`N_pos = 2` of those sites have `N_agree > 0`. The lex-first such site is
`v = (1,-1,1)`. One agreeing 6-tuple there is `(+, −, −, 0, 0, +)`.
Unique-axis therefore does not forbid firing at every 4-NN unread site of
this `U`.

The lex-first 4-NN unread site `(1,-1,-1)` still has `N_agree = 0`. The
present residual is not leftover-char of the one-witness unique-axis
agreement on that lex-first 4-NN unread site. The census does not stop at
the lex-first witness.

The comparison is displayed, not adopted. Do not write a site list into Admissibility. Do not attach L1.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Finite agreement census of every 4-NN unread site of one two-ball U against unique-axis labels is exact; no axiom sentence is rewritten."
trace_class: negative_route_pruning
target_claim_id: two_ball_all_4nn_unique_axis_agree
target_blocker_text: "whether any unread 4-occupied-NN site of U=B_2(0)∪B_2((2,0,0)) has N_agree>0"
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
conditional_surface_status: "exact on the July-3 named k=3 alphabet, this U, and the radius-6 box; displayed, not adopted"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
next_trace_action: "independent audit of N_pos; do not write a site list into Admissibility and do not attach L1"
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

This note does not choose that rule and does not add a unique-axis clause
or a site list to it. Letter `0` is the empty/unread letter on the July-3
three-letter model. Occupied means membership in the constructed set `U`.
The note does not assign a readout value to absence.
- **July-3 Theorem 3.** At `k = 3` there is exactly one chiral pair, whose
  members are the handed fully-mixed patterns: every axis bi-colored with
  two distinct values, every value used twice. The runner re-earns the
  pair by enumerating `G+` orbits; it does not import an external list.
- **Two-ball occupied set, re-earned here.** `U = B_2(0) ∪ B_2((2,0,0))`
  is constructed as the union of two closed ℓ¹ balls. Unread sites are
  enumerated in the radius-6 box only.
- **Unique-axis label.** On the same `U`, the occupancy kernel `n = d/3`
  of an occupied neighbor has a unique axis when exactly one component is
  nonzero. The label is the sign of that unique nonzero component, or
  ambiguous. Ambiguous slots are free in the agreement count.
- **External empirical inputs:** none.
- **Not attached:** L1 is not a premise and is not a conclusion. The
  census is not leftover-char of the one-witness unique-axis agreement.

## Exact Objects

The six nearest-neighbor directions, in the July-3 order, are

```text
(+x, −x, +y, −y, +z, −z).
```

The closed ℓ¹ ball is `B_r(c) = { x in Z^3 : ||x − c||_1 ≤ r }`. The
occupied set is only

```text
U = B_2(0) ∪ B_2((2,0,0)).
```

Scoring is restricted to the finite box `|x|,|y|,|z| ≤ 6`. A site `v` in
that box is unread when `v ∉ U`. Occupancy of a neighbor is membership in
`U`. The occupancy mask of `v` is the `{0,1}` 6-tuple of those memberships
in the direction order above.

A `k = 3` condition 6-tuple is an element of `{0, +, −}^6`. Letter `0` is
empty. `G+` is the 24-element proper cubic group of determinant-`+1` signed
permutation matrices. It acts on 6-tuples by the induced permutation of
the six axis directions. Spatial inversion `P = −I` is the central
improper element. A chiral pair is a pair of distinct `G+` orbits
exchanged by `P`. July-3 Theorem 3 states there is exactly one such pair
at `k = 3`. Write `Pair` for the union of those two orbits, and
`N_pair = |Pair|`.

For an unread `v` with exactly four occupied neighbors, `N_fire(v)` is the
number of members of `Pair` whose occupancy mask equals the mask of `v`.
Equivalently, it is the number of `{+, −}` fillings of those four occupied
slots that lie in `Pair`.

The occupancy 6-tuple of a site `w` inside `U` is `c(w)_i = 1` if
`w + e_i ∈ U` and `0` otherwise. The dipole and kernel are
`d_μ = c_{+μ} − c_{−μ}` and `n = d/3`. The unique-axis label of an
occupied neighbor is the sign of the unique nonzero component of `n`, or
ambiguous when `|supp n| ≠ 1`. `N_unique_axis(v)` is the number of
occupied neighbors of `v` that receive a unique-axis label.

`N_agree(v)` is the number of pair members on `v`'s mask that match every
unique-axis label. Ambiguous slots are free. `N_4` is the number of unread
box sites with occupied-NN count `4`. `N_pos` is how many of those have
`N_agree > 0`.

## Theorem 1 — Four Unread 4-NN Sites

`N_4 = 4`. The four unread box sites with occupied-NN count `4`, together
with their masks, fire counts, unique-axis counts, and agreement counts,
are the rows of the table in the Result Up Front.

*Proof.* The 24 proper signed permutation matrices are generated
exhaustively. Their action on the 729 colorings `{0, +, −}^6` partitions
them into 57 `G+` orbits, matching the July-3 Burnside count. Exactly two
of those orbits fail to meet their `P`-images; they form one pair, and
each has size 24, so `N_pair = 48`. Every pair member is fully mixed:
every axis is bi-colored and each letter occurs twice.

Independently, `U` is constructed as the union of the two radius-`2` ℓ¹
balls. Every site of the box `|x|,|y|,|z| ≤ 6` outside `U` is tested for
how many of its six axial neighbors lie in `U`. Exactly four sites reach
count `4`: `(1,-1,-1)`, `(1,-1,1)`, `(1,1,-1)`, and `(1,1,1)`. Each has
`|U| = 43` as the same occupied set.

For each such `v`, the occupancy mask is read off membership of the six
neighbors in `U`. The sixteen `{+, −}` fillings of the four occupied slots
are enumerated; a filling is a fire if and only if it lies in `Pair`.
Direct membership yields `N_fire = 4` at every one of the four sites.

The occupancy kernel of each occupied neighbor is computed on the same
`U`. In every case the two `±x` neighbors have two nonzero kernel
components and are ambiguous, while the two remaining occupied neighbors
each have a single nonzero component. Hence `N_unique_axis = 2` at every
site. Matching pair members against those two labels yields

```text
N_agree(1,-1,-1) = 0
N_agree(1,-1,1)  = 2
N_agree(1,1,-1)  = 2
N_agree(1,1,1)   = 0.
```

The unique-axis fragments and the agreeing 6-tuples are

| `v` | unique-axis 6-tuple | agreeing pair members |
|---|---|---|
| `(1,-1,-1)` | `(*, *, +, 0, +, 0)` | none |
| `(1,-1,1)` | `(*, *, −, 0, 0, +)` | `(+, −, −, 0, 0, +)`, `(−, +, −, 0, 0, +)` |
| `(1,1,-1)` | `(*, *, 0, +, −, 0)` | `(+, −, 0, +, −, 0)`, `(−, +, 0, +, −, 0)` |
| `(1,1,1)` | `(*, *, 0, −, 0, −)` | none |

At `(1,-1,-1)` the two unique-axis labels force `+y = +` and `+z = +`.
Full mixing on that mask then requires both `±x` slots to be `−`, so the
`x` axis fails to be bi-colored and no pair member survives. The opposite
corner `(1,1,1)` is the same obstruction with both unique-axis labels `−`.
The two mixed-sign corners leave a bi-colored `x` axis free, and two pair
members survive at each.

## Theorem 2 — Two Sites Have N_agree > 0

`N_pos = 2`. Unique-axis does not forbid firing at every 4-NN unread site
of this `U`. The lex-first site with `N_agree > 0` is `v = (1,-1,1)`, and
one agreeing 6-tuple there is `(+, −, −, 0, 0, +)`.

*Proof.* Theorem 1 lists `N_agree` at the four sites. Exactly two values
are positive, so `N_pos = 2`. Among those two sites, the lexicographic
minimum is `(1,-1,1)`. At that site the unique-axis fragment is
`+y = −` and `−z = +`, with `±x` ambiguous. Of the four firing 6-tuples
on mask `(1,1,1,0,0,1)`, the two that carry those signs are
`(+, −, −, 0, 0, +)` and `(−, +, −, 0, 0, +)`. The first of those in
lexicographic letter order is `(+, −, −, 0, 0, +)`.

Because `N_pos > 0`, it is not the case that unique-axis forbids firing at
every 4-NN unread site of this `U`. The lex-first 4-NN unread site
`(1,-1,-1)` remains a zero-agreement witness; the other three sites are
part of the same residual and are not optional extras.

## Theorem 3 — Displayed, Not Adopted

The four-site census and the count `N_pos = 2` are a finite report on the
July-3 named alphabet model and one two-ball occupied set inside the
radius-6 box. They are displayed. They are not adopted.

In particular:

- the unique-axis labels are not written into Admissibility;
- no site list is written into Admissibility;
- no unique-axis clause is written into Admissibility;
- no axiom sentence is edited;
- the comparison is not attached to L1.

Admissibility continues to say only that there is one fixed
nearest-neighbor rule, covariant under translations and proper cubic
rotations, and that the local distribution varies with the
nearest-neighbor conditions. Which unread 4-NN sites of a displayed
two-ball union agree with occupancy-kernel unique-axis labels is not that
rule.

## What This Note Does And Does Not Claim

- **It does claim** that this `U` has exactly four unread 4-NN sites in
  the radius-6 box, that their masks, fire counts, unique-axis counts, and
  agreement counts are the rows of Theorem 1, that `N_pos = 2`, and that
  the lex-first positive site is `(1,-1,1)` with agreeing 6-tuple
  `(+, −, −, 0, 0, +)`.
- **It does not claim** leftover-char of the one-witness unique-axis
  agreement on the lex-first 4-NN unread site. It is not leftover-char of
  the one-witness unique-axis agreement. That residual scored only
  `v = (1,-1,-1)`. The present residual enumerates every 4-NN unread site
  of the same `U`.
- **It does not adopt** a unique-axis rule or a site list as Admissibility
  content and does not attach L1.
- **It does not** open a larger box than `|x|,|y|,|z| ≤ 6`, replace the
  six-neighbor stencil, select the physical condition alphabet, or decide
  whether the framework's fixed rule is chiral.

## Machine-Readable Report

```text
N_pair = 48
N_4 = 4
sites = [(1, -1, -1), (1, -1, 1), (1, 1, -1), (1, 1, 1)]
masks = [(1, 1, 1, 0, 1, 0), (1, 1, 1, 0, 0, 1), (1, 1, 0, 1, 1, 0), (1, 1, 0, 1, 0, 1)]
N_fire = [4, 4, 4, 4]
N_unique_axis = [2, 2, 2, 2]
N_agree = [0, 2, 2, 0]
N_pos = 2
lex_first_positive = (1, -1, 1)
one_agreeing = (+, -, -, 0, 0, +)
unique_axis_forbids_every_4nn = false
displayed_not_adopted = true
attached_to_L1 = false
written_into_admissibility = false
site_list_written_into_admissibility = false
```
