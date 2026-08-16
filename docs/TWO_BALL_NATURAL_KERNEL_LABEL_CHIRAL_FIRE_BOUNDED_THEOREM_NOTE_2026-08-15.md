---
claim_id: two_ball_natural_kernel_label_chiral_fire_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On U=B_2(0)∪B_2((2,0,0)) at unread v=(1,−1,−1), whether occupancy-kernel unique-axis labels of the four occupied neighbors form a July-3 k=3 pair member is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_covariance_extension_classification_openness_achiral_oriented_frame_minimal_chiral_channel_bounded_theorem_note_2026-07-03
runner: scripts/two_ball_natural_kernel_label_chiral_fire_2026_08_15.py
---

# Natural Occupancy-Kernel Labels At The Two-Ball Witness Versus The July-3 k=3 Pair

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact occupancy-kernel unique-axis labels of the four occupied
nearest neighbors of one unread 6-nearest-neighbor star on
`U = B_2(0) ∪ B_2((2,0,0))`, compared to the 48 July-3 `k = 3`
chiral-pair 6-tuples. Displayed, not adopted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/two_ball_natural_kernel_label_chiral_fire_2026_08_15.py`](../scripts/two_ball_natural_kernel_label_chiral_fire_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)
and the July-3 classification
[`ADMISSIBILITY_RULE_COVARIANCE_EXTENSION_CLASSIFICATION_OPENNESS_ACHIRAL_ORIENTED_FRAME_MINIMAL_CHIRAL_CHANNEL_BOUNDED_THEOREM_NOTE_2026-07-03.md`](ADMISSIBILITY_RULE_COVARIANCE_EXTENSION_CLASSIFICATION_OPENNESS_ACHIRAL_ORIENTED_FRAME_MINIMAL_CHIRAL_CHANNEL_BOUNDED_THEOREM_NOTE_2026-07-03.md).

## Result Up Front

Direction order is `(+x, −x, +y, −y, +z, −z)`. Scoring is only the occupied
set `U = B_2(0) ∪ B_2((2,0,0))` and the 6-NN star at the unread witness
`v = (1,-1,-1)`. No new spatial patch is opened.

The four occupied neighbors of `v` are `(2,-1,-1)`, `(0,-1,-1)`,
`(1,0,-1)`, and `(1,-1,0)`. The two unread neighbors are `(1,-2,-1)` and
`(1,-1,-2)`. Occupancy mask of the star is `(1, 1, 1, 0, 1, 0)`.

For a site `w ∈ U`, write `c(w) ∈ {0,1}^6` for the occupancy 6-tuple of
its six axial neighbors inside `U`. The occupancy dipole and kernel are

```text
d_μ = c_{+μ}(w) − c_{−μ}(w),    n = d/3.
```

If `|supp n| = 1`, the unique-axis label of `w` is the sign of that unique
nonzero `n_μ`. If `n` has any other support, `w` has no unique axis. Empty
slots of the star at `v` stay the empty letter `0`.

The natural 6-tuple assembled at `v` is

```text
c = (*, *, +, 0, +, 0),
```

where `*` means no unique axis. Not every occupied neighbor has a
unique-axis label: the `±x` neighbors each have `n = (0, 1/3, 1/3)`.

July-3 Theorem 3 isolates a unique chiral pair at three condition letters.
Letters are `{0, +, −}` with `0` empty. The pair is the union of two `G+`
orbits and has `N_pair = 48` members. The natural 6-tuple `c` is not a
letter 6-tuple, so it is not a pair member: the pair does not fire. The
Hamming distance to the lex-first firing labeling `(+, −, +, 0, −, 0)`,
counting `*` as a distinct symbol, is `3`.

This is not leftover-char of the two-ball occupied-NN count, which asked
only whether any unread site reaches four occupied neighbors. It is not
leftover-char of the existence of some `{+,−}` labeling of the witness
mask: some signed fillings are pair members, but the occupancy-kernel
unique-axis rule is not one of them.

The comparison is displayed, not adopted. Do not write the kernel labeling
into Admissibility. Do not attach L1.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Finite occupancy-kernel unique-axis labels of one 6-NN star, and the exact Hamming comparison to the July-3 k=3 pair, are exact; no axiom sentence is rewritten."
trace_class: negative_route_pruning
target_claim_id: two_ball_natural_kernel_label_chiral_fire
target_blocker_text: "whether occupancy-kernel unique-axis labels of the four occupied neighbors of the two-ball unread witness form a July-3 k=3 pair member"
source_of_blocker_text: handoff
reachability_to_target: prunes
artifact_role: theorem
conditional_surface_status: "exact on U and the 6-NN star at v against the July-3 named k=3 alphabet; displayed, not adopted"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
next_trace_action: "independent audit of the natural 6-tuple and Hamming distance; do not write the kernel labeling into Admissibility and do not attach L1"
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

This note does not choose that rule and does not add a kernel-label clause
to it. Letter `0` is the empty/unread letter on the July-3 three-letter
model. Occupied means membership in `U`. The note does not assign a
readout value to absence.
- **July-3 Theorem 3.** At `k = 3` there is exactly one chiral pair, whose
  members are the handed fully-mixed patterns: every axis bi-colored with
  two distinct values, every value used twice. The runner re-earns the
  pair by enumerating `G+` orbits; it does not import an external list.
- **Two-ball witness, re-earned here.** Only the union `p = (2,0,0)`,
  `r = s = 2` is used. The unread witness is `v = (1,-1,-1)`. The runner
  rebuilds `U` and the star; it does not import a stored mask.
- **Occupancy kernel, displayed here.** `d_μ = c_{+μ} − c_{−μ}` and
  `n = d/3` are computed from occupancy of `U` at each occupied neighbor
  of `v`. The unique-axis rule uses only the support and signs of `n`.
- **External empirical inputs:** none.
- **Not attached:** L1 is not a premise and is not a conclusion. The
  kernel labeling is not leftover-char of the two-ball count or of the
  existence of some signed filling of the mask.

## Exact Objects

The six nearest-neighbor directions, in the July-3 order, are

```text
(+x, −x, +y, −y, +z, −z).
```

The closed ℓ¹ ball is `B_r(c) = { x in Z^3 : ||x − c||_1 ≤ r }`. The
occupied set used here is only

```text
U = B_2(0) ∪ B_2((2,0,0)).
```

The unread witness is the single site `v = (1,-1,-1)`. Its 6-NN star is

```text
v + {+e_1, −e_1, +e_2, −e_2, +e_3, −e_3}.
```

No other site is scored.

A `k = 3` condition 6-tuple is an element of `{0, +, −}^6`. Letter `0` is
empty. `G+` is the 24-element proper cubic group of determinant-`+1` signed
permutation matrices. It acts on 6-tuples by the induced permutation of
the six axis directions. Spatial inversion `P = −I` is the central
improper element. A chiral pair is a pair of distinct `G+` orbits
exchanged by `P`. July-3 Theorem 3 states there is exactly one such pair
at `k = 3`. Write `Pair` for the union of those two orbits, and
`N_pair = |Pair|`.

The occupancy 6-tuple of a site `w` inside `U` is

```text
c(w)_i = 1 if w + e_i ∈ U else 0,
```

in the direction order above. The dipole and kernel are `d_μ = c_{+μ} −
c_{−μ}` and `n = d/3`. Support is `{ μ : n_μ ≠ 0 }`. The unique-axis
label is `sign(n_μ)` when that set is a singleton, and is the symbol `*`
otherwise. The natural 6-tuple at `v` puts `0` on unread neighbors of `v`
and the unique-axis label on occupied neighbors.

Hamming distance between two 6-tuples over the extended alphabet
`{0, +, −, *}` is the number of slots where the symbols differ. The
lex-first firing labeling of the witness mask, under letter order
`0 < + < −` among `{0, +, −}` fillings that lie in `Pair`, is
`(+, −, +, 0, −, 0)`.

## Theorem 1 — Natural 6-Tuple And Unique-Axis Coverage

The natural 6-tuple at `v` is `c = (*, *, +, 0, +, 0)`. Not every
occupied neighbor has a unique-axis label.

*Proof.* The two-ball union `U` is constructed and the six axial
neighbors of `v` are tested for membership in `U`. The occupied
neighbors are `(2,-1,-1)`, `(0,-1,-1)`, `(1,0,-1)`, and `(1,-1,0)`; the
empty neighbors are `(1,-2,-1)` and `(1,-1,-2)`. Each occupied neighbor
`w` is scored by its occupancy 6-tuple inside `U`:

| neighbor of `v` | `w` | occupancy `c(w)` | `d` | `n = d/3` | `|supp n|` | label |
|---|---|---|---|---|---:|---|
| `+x` | `(2,-1,-1)` | `(0,0,1,0,1,0)` | `(0,1,1)` | `(0, 1/3, 1/3)` | 2 | `*` |
| `−x` | `(0,-1,-1)` | `(0,0,1,0,1,0)` | `(0,1,1)` | `(0, 1/3, 1/3)` | 2 | `*` |
| `+y` | `(1,0,-1)` | `(1,1,0,0,1,0)` | `(0,0,1)` | `(0, 0, 1/3)` | 1 | `+` |
| `−y` | `(1,-2,-1)` | unread | — | — | — | `0` |
| `+z` | `(1,-1,0)` | `(1,1,1,0,0,0)` | `(0,1,0)` | `(0, 1/3, 0)` | 1 | `+` |
| `−z` | `(1,-1,-2)` | unread | — | — | — | `0` |

The `+y` and `+z` neighbors each have a unique nonzero kernel component,
so the unique occupied-axis rule supplies the signs `+` and `+`. The
`±x` neighbors each have two nonzero components, so they have no unique
axis. Assembling in direction order gives `c = (*, *, +, 0, +, 0)`.
Therefore it is false that every occupied neighbor has a unique-axis
label.

## Theorem 2 — The Pair Does Not Fire

The natural 6-tuple `c` is not one of the 48 July-3 `k = 3` pair members.
The pair does not fire. The Hamming distance to the lex-first firing
labeling `(+, −, +, 0, −, 0)` is `3`.

*Proof.* The 24 proper signed permutation matrices are generated
exhaustively. Their action on the 729 colorings `{0, +, −}^6` partitions
them into 57 `G+` orbits, matching the July-3 Burnside count. Exactly two
of those orbits fail to meet their `P`-images; they form one pair, and
each has size 24, so `N_pair = 48`. Every pair member is fully mixed, so
letter `0` occurs twice and every member lies in `{0, +, −}^6`.

The symbol `*` is not a letter of that alphabet, so `c ∉ Pair`. Among
the 16 `{+, −}` fillings of the four occupied slots of the witness mask,
exactly four lie in `Pair`. Under `0 < + < −` the lex-first of those four
is `(+, −, +, 0, −, 0)`. Slotwise comparison against `c` differs in the
`+x`, `−x`, and `+z` slots and agrees in the other three, hence Hamming
distance `3`.

Existence of some signed filling that lies in `Pair` is a different
residual. The occupancy-kernel unique-axis rule is not such a filling.

## Theorem 3 — Displayed, Not Adopted

The natural 6-tuple `c`, the failure of unique-axis coverage, the report
that the pair does not fire, and the Hamming distance `3` are a finite
report on the July-3 named alphabet model and one two-ball star. They are
displayed. They are not adopted.

In particular:

- the kernel labeling is not written into Admissibility;
- no axiom sentence is edited;
- the comparison is not attached to L1.

Admissibility continues to say only that there is one fixed
nearest-neighbor rule, covariant under translations and proper cubic
rotations, and that the local distribution varies with the
nearest-neighbor conditions. Which unique-axis labels a displayed
occupancy kernel assigns on a named two-ball star is not that rule.

## What This Note Does And Does Not Claim

- **It does claim** that on `U = B_2(0) ∪ B_2((2,0,0))` at unread
  `v = (1,-1,-1)`, the occupancy-kernel unique-axis labels of the four
  occupied neighbors assemble to `c = (*, *, +, 0, +, 0)`, that not every
  occupied neighbor has a unique-axis label, that `c` is not a July-3
  `k = 3` pair member, and that the Hamming distance to
  `(+, −, +, 0, −, 0)` is `3`.
- **It does not claim** leftover-char of the two-ball occupied-NN count.
- **It does not claim** leftover-char of the existence of some `{+,−}`
  labeling of the witness mask.
- **It does not adopt** the kernel labeling as Admissibility content and
  does not attach L1.
- **It does not** score any site other than `U` and the 6-NN star at `v`,
  replace the six-neighbor stencil, select the physical condition
  alphabet, or decide whether the framework's fixed rule is chiral.

## Machine-Readable Report

```text
N_pair = 48
natural_c = (*, *, +, 0, +, 0)
every_occupied_neighbor_has_unique_axis = false
pair_fires = false
hamming_to_lex_first = 3
lex_first_firing = (+, -, +, 0, -, 0)
displayed_not_adopted = true
attached_to_L1 = false
written_into_admissibility = false
```
