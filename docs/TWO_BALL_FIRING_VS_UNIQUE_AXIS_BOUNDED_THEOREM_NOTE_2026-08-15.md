---
claim_id: two_ball_firing_vs_unique_axis_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Among the 4 July-3 pair members on the two-ball witness mask, how many agree with unique-axis labels +y=+ and +z=+ is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_covariance_extension_classification_openness_achiral_oriented_frame_minimal_chiral_channel_bounded_theorem_note_2026-07-03
runner: scripts/two_ball_firing_vs_unique_axis_2026_08_15.py
---

# Two-Ball Firing 6-Tuples Versus Unique-Axis Signs

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact census of the four July-3 `k = 3` pair members on the
two-ball witness occupancy mask `(1,1,1,0,1,0)` against the unique-axis
fragment `+y = +` and `+z = +`. Displayed, not adopted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/two_ball_firing_vs_unique_axis_2026_08_15.py`](../scripts/two_ball_firing_vs_unique_axis_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)
and the July-3 classification
[`ADMISSIBILITY_RULE_COVARIANCE_EXTENSION_CLASSIFICATION_OPENNESS_ACHIRAL_ORIENTED_FRAME_MINIMAL_CHIRAL_CHANNEL_BOUNDED_THEOREM_NOTE_2026-07-03.md`](ADMISSIBILITY_RULE_COVARIANCE_EXTENSION_CLASSIFICATION_OPENNESS_ACHIRAL_ORIENTED_FRAME_MINIMAL_CHIRAL_CHANNEL_BOUNDED_THEOREM_NOTE_2026-07-03.md).

## Result Up Front

Direction order is `(+x, −x, +y, −y, +z, −z)`. The two-ball unread witness
occupancy mask on that order is

```text
m = (1, 1, 1, 0, 1, 0)
```

with `1` occupied and `0` empty. Occupied slots are `+x`, `−x`, `+y`, and
`+z`. Empty slots are `−y` and `−z`.

July-3 Theorem 3 isolates a unique chiral pair at three condition letters.
Letters are `{0, +, −}` with `0` empty. The pair is the union of two `G+`
orbits and has `N_pair = 48` members. Exactly four `{+, −}` fillings of
`m` are pair members. Those four firing 6-tuples are

```text
(+, −, +, 0, −, 0)
(+, −, −, 0, +, 0)
(−, +, +, 0, −, 0)
(−, +, −, 0, +, 0).
```

The occupancy-kernel unique-axis fragment on the two unambiguous occupied
neighbors of the witness is `+y = +` and `+z = +`. Among the four firing
6-tuples, `N_agree = 0` have both of those signs. Unique-axis labels on
those two neighbors already exclude every firing labeling.

This is not leftover-char of the full occupancy-kernel 6-tuple, which
scored one full kernel labeling with `*` on the two ambiguous `±x` slots.
The residual here is only the four-member firing census against the two
unambiguous signs.

The comparison is displayed, not adopted. Do not write a tie-break into Admissibility. Do not attach L1.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Finite agreement count of the four firing pair members on one witness mask against two unique-axis signs is exact; no axiom sentence is rewritten."
trace_class: negative_route_pruning
target_claim_id: two_ball_firing_vs_unique_axis
target_blocker_text: "among the 4 firing 6-tuples on the two-ball witness mask, how many have +y=+ and +z=+"
source_of_blocker_text: handoff
reachability_to_target: prunes
artifact_role: theorem
conditional_surface_status: "exact on the July-3 named k=3 alphabet and the one two-ball 6-tuple census; displayed, not adopted"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
next_trace_action: "independent audit of N_agree; do not write a tie-break into Admissibility and do not attach L1"
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
or a tie-break to it. Letter `0` is the empty/unread letter on the July-3
three-letter model. Occupied means nonzero. The note does not assign a
readout value to absence.
- **July-3 Theorem 3.** At `k = 3` there is exactly one chiral pair, whose
  members are the handed fully-mixed patterns: every axis bi-colored with
  two distinct values, every value used twice. The runner re-earns the
  pair by enumerating `G+` orbits; it does not import an external list.
- **Two-ball witness mask, re-earned here.** The union
  `U = B_2(0) ∪ B_2((2,0,0))` at unread `v = (1,-1,-1)` occupies
  `(+x, −x, +y, +z)` and leaves `(−y, −z)` empty. The runner rebuilds
  that mask and the four pair fillings; it does not import a stored list.
- **Unique-axis fragment.** On the same `U`, the occupancy kernel
  `n = d/3` of an occupied neighbor has a unique axis when exactly one
  component is nonzero. The two unambiguous occupied neighbors of `v`
  are the `+y` and `+z` sites; both receive label `+`. The `±x`
  neighbors have no unique axis and are not used as constraints here.
- **External empirical inputs:** none.
- **Not attached:** L1 is not a premise and is not a conclusion. The
  agreement count is not leftover-char of the full kernel 6-tuple with
  `*`.

## Exact Objects

The six nearest-neighbor directions, in the July-3 order, are

```text
(+x, −x, +y, −y, +z, −z).
```

The closed ℓ¹ ball is `B_r(c) = { x in Z^3 : ||x − c||_1 ≤ r }`. The
occupied set used to rebuild the mask is only

```text
U = B_2(0) ∪ B_2((2,0,0)).
```

The unread witness is the single site `v = (1,-1,-1)`. Occupancy of a
neighbor is membership in `U`. The occupancy mask is the `{0,1}` 6-tuple
in the direction order above.

A `k = 3` condition 6-tuple is an element of `{0, +, −}^6`. Letter `0` is
empty. `G+` is the 24-element proper cubic group of determinant-`+1` signed
permutation matrices. It acts on 6-tuples by the induced permutation of
the six axis directions. Spatial inversion `P = −I` is the central
improper element. A chiral pair is a pair of distinct `G+` orbits
exchanged by `P`. July-3 Theorem 3 states there is exactly one such pair
at `k = 3`. Write `Pair` for the union of those two orbits, and
`N_pair = |Pair|`.

The four firing 6-tuples are the members of `Pair` whose occupancy mask
equals `m`, equivalently the `{+, −}` fillings of the four occupied slots
of `m` that lie in `Pair`.

The occupancy 6-tuple of a site `w` inside `U` is `c(w)_i = 1` if
`w + e_i ∈ U` and `0` otherwise. The dipole and kernel are
`d_μ = c_{+μ} − c_{−μ}` and `n = d/3`. The unique-axis fragment used here
is only the pair of signs of the unique nonzero components at the `+y`
and `+z` neighbors of `v`. Those signs are both `+`.

`N_agree` is the number of firing 6-tuples whose `+y` slot is `+` and
whose `+z` slot is `+`.

## Theorem 1 — Four Firing 6-Tuples And N_agree

The four firing 6-tuples on `m` are

```text
(+, −, +, 0, −, 0)
(+, −, −, 0, +, 0)
(−, +, +, 0, −, 0)
(−, +, −, 0, +, 0).
```

Exactly `N_agree = 0` of them have `+y = +` and `+z = +`.

*Proof.* The 24 proper signed permutation matrices are generated
exhaustively. Their action on the 729 colorings `{0, +, −}^6` partitions
them into 57 `G+` orbits, matching the July-3 Burnside count. Exactly two
of those orbits fail to meet their `P`-images; they form one pair, and
each has size 24, so `N_pair = 48`. Every pair member is fully mixed:
every axis is bi-colored and each letter occurs twice.

Independently, `U` is constructed and the six axial neighbors of `v` are
tested for membership in `U`. The occupied neighbors are `(2,-1,-1)`,
`(0,-1,-1)`, `(1,0,-1)`, and `(1,-1,0)`; the empty neighbors are
`(1,-2,-1)` and `(1,-1,-2)`. That is the mask `m`.

The 16 `{+, −}` fillings of the four occupied slots are enumerated. A
filling is a firing 6-tuple if and only if it lies in `Pair`. Direct
membership yields exactly the four 6-tuples listed above.

Slotwise, those four have `(+y, +z)` equal to `(+, −)`, `(−, +)`,
`(+, −)`, and `(−, +)` respectively. None equals `(+, +)`. Hence
`N_agree = 0`.

The same vanishing is forced by full mixing on this mask. If `+y` and
`+z` were both `+`, the two `+` letters would already be used, the two
`0` letters would already occupy `−y` and `−z`, and both `±x` slots would
have to be `−` to use `−` twice. The `x` axis would then fail to be
bi-colored, so the 6-tuple would lie outside `Pair`.

## Theorem 2 — Unique-Axis Fragment Excludes Every Firing Labeling

Because `N_agree = 0`, unique-axis labels on the two unambiguous occupied
neighbors already exclude every firing labeling.

*Proof.* On the same `U`, the occupancy kernels of the four occupied
neighbors of `v` are

| neighbor of `v` | `w` | `n = d/3` | `|supp n|` | label |
|---|---|---|---:|---|
| `+x` | `(2,-1,-1)` | `(0, 1/3, 1/3)` | 2 | no unique axis |
| `−x` | `(0,-1,-1)` | `(0, 1/3, 1/3)` | 2 | no unique axis |
| `+y` | `(1,0,-1)` | `(0, 0, 1/3)` | 1 | `+` |
| `+z` | `(1,-1,0)` | `(0, 1/3, 0)` | 1 | `+` |

The unique-axis fragment is therefore `+y = +` and `+z = +`. By
Theorem 1, no firing 6-tuple carries both of those signs. Any labeling
that respects the unique-axis fragment on the two unambiguous neighbors
fails to be a pair member on this mask.

The two ambiguous `±x` slots are not used as a further constraint. The
present census does not score a full kernel 6-tuple with `*`.

## Theorem 3 — Displayed, Not Adopted

The four firing 6-tuples and the count `N_agree = 0` are a finite report
on the July-3 named alphabet model and one two-ball mask. They are
displayed. They are not adopted.

In particular:

- the unique-axis fragment is not written into Admissibility;
- no tie-break is written into Admissibility;
- no unique-axis clause is written into Admissibility;
- no axiom sentence is edited;
- the comparison is not attached to L1.

Admissibility continues to say only that there is one fixed
nearest-neighbor rule, covariant under translations and proper cubic
rotations, and that the local distribution varies with the
nearest-neighbor conditions. Which unique-axis fragment a displayed
occupancy kernel assigns on a named two-ball star is not that rule.

## What This Note Does And Does Not Claim

- **It does claim** that the four July-3 pair members on the two-ball
  witness mask are the 6-tuples listed in Theorem 1, that `N_agree = 0`
  of them have `+y = +` and `+z = +`, and that the unique-axis fragment
  on those two unambiguous neighbors therefore excludes every firing
  labeling.
- **It does not claim** leftover-char of the full occupancy-kernel
  6-tuple with `*`. It is not leftover-char of the full occupancy-kernel
  6-tuple. That residual scored one assembled labeling of all
  four occupied slots. The present residual is only whether the two
  unambiguous signs already meet any firing 6-tuple.
- **It does not adopt** a unique-axis tie-break as Admissibility content
  and does not attach L1.
- **It does not** open a new spatial patch, replace the six-neighbor
  stencil, select the physical condition alphabet, or decide whether the
  framework's fixed rule is chiral.

## Machine-Readable Report

```text
N_pair = 48
N_fire = 4
mask = (1, 1, 1, 0, 1, 0)
firing = [(+, -, +, 0, -, 0), (+, -, -, 0, +, 0), (-, +, +, 0, -, 0), (-, +, -, 0, +, 0)]
unique_axis_plus_y = +
unique_axis_plus_z = +
N_agree = 0
unique_axis_excludes_every_firing = true
displayed_not_adopted = true
attached_to_L1 = false
written_into_admissibility = false
tie_break_written_into_admissibility = false
```
