---
claim_id: skew_three_seed_claim_axis_label_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On the off-axis three-ball union at unread v=(-1,1,1), whether claim-axis tie-breaks of history-tied neighbors yield a July-3 k=3 pair member is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_covariance_extension_classification_openness_achiral_oriented_frame_minimal_chiral_channel_bounded_theorem_note_2026-07-03
runner: scripts/skew_three_seed_claim_axis_label_2026_08_15.py
---

# Claim-Axis Labels Of History-Tied Neighbors At The Off-Axis Three-Seed Breaker (Bounded Theorem)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact occupancy on
`U = B_2(0) ∪ B_2((2,0,0)) ∪ B_2((1,2,1))` and the unread six-neighbor
star at `v = (−1,1,1)`. For each occupied neighbor, unique-axis history
labels from the nearest-seed ball, then claim-axis tie-break
`δ = w − s*(w)` on remaining ties. Completed 6-tuple or remaining
ties, whether every occupied neighbor is labeled, and (if not fully
labeled) `N_fire` among remaining completions against the July-3
`k = 3` pair. Score `U` and the star at `v` only. Displayed, not
adopted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/skew_three_seed_claim_axis_label_2026_08_15.py`](../scripts/skew_three_seed_claim_axis_label_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)
and the July-3 classification
[`ADMISSIBILITY_RULE_COVARIANCE_EXTENSION_CLASSIFICATION_OPENNESS_ACHIRAL_ORIENTED_FRAME_MINIMAL_CHIRAL_CHANNEL_BOUNDED_THEOREM_NOTE_2026-07-03.md`](ADMISSIBILITY_RULE_COVARIANCE_EXTENSION_CLASSIFICATION_OPENNESS_ACHIRAL_ORIENTED_FRAME_MINIMAL_CHIRAL_CHANNEL_BOUNDED_THEOREM_NOTE_2026-07-03.md).

## Result Up Front

Investment `#6659` (histlab, unique-axis) reported that on this
off-axis triple the nearest-seed history kernels leave three slots
tied at `v = (−1,1,1)`, and that 2 of 8 completions of those ties fire
the July-3 pair. The residual here is not leftover-char of histlab
(that stopped at unique-axis). It is whether, when `n_hist` is tied,
the claim-axis vector `δ = w − s*(w)` — the direction from the
claiming seed to the neighbor — supplies a unique-axis sign, whether
that fully labels the star, and whether the completed 6-tuple is a
July-3 `k = 3` pair member.

Treat `U` as already locked. The site `v = (−1,1,1)` is unread: it
lies in none of the three radius-two ℓ¹ balls. Direction order is

`(+x, −x, +y, −y, +z, −z)`.

The four occupied nearest neighbors of `v` in `U` are `+x`, `+y`,
`−y`, and `−z`. The two empty slots are `−x` and `+z`. Occupancy mask

`m = (1, 0, 1, 1, 0, 1)`.

Seeds are `S = {0, (2,0,0), (1,2,1)}`. For an occupied neighbor `w`,
the nearest seed `s*(w)` is a seed of least ℓ¹ distance; ties take the
lex-first seed. The history kernel `n_hist(w)` is the occupancy dipole
`n = d/3` at `w` computed from occupancy in `B_2(s*(w))` only. If
`n_hist(w)` has a unique nonzero coordinate, the label is the sign of
that coordinate. Else let `δ = w − s*(w)`. If `δ` has a unique nonzero
coordinate, the label is the sign of that coordinate. Else the slot
stays tied. Empty slots stay `0`.

The completed 6-tuple is still

`(tied, 0, +, tied, 0, tied)`.

Not every occupied neighbor is labeled. Claim-axis breaks none of the
three history ties: each of those `δ` has two nonzero coordinates.
The unique-axis history label at `+y` remains `+`. That slot is not
reassigned by claim-axis (its `δ = (−2, 0, 0)` is unused because
`n_hist` already has a unique axis).

There are eight `{+,−}` completions of the three remaining tied slots.
Exactly `N_fire = 2` of them are July-3 pair members:

`(+,0,+,−,0,−)`

and

`(−,0,+,−,0,+)`.

The 6-tuple is not fully labeled, so it is not itself a pair member.

The comparison is displayed, not adopted.
Do not write claim-axis into Admissibility.
Do not attach L1. Failed-bar: no 4th equal-radius ball.

## Current Premise Boundary

The Lattice, Admissibility, Record, and Qubit sentences used here are quoted
from [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md):

Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
adjacency, standard translations, and proper cubic rotations about each site.

There is one fixed nearest-neighbor admissibility rule, covariant under lattice
translations and proper cubic rotations.

For each site, the probability distribution over the possibilities is
determined by, and varies with, the nearest-neighbor conditions.

it does not supply the formation site, probability,
or rate.

The full one-site possibility domain has algebraic presentation `M_2(C)`.

When present, a record locks exactly one admissible local possibility.

A site never carries more than one record; records are permanent.

A readout value is determined by record content alone.

A site with no record cannot be read.

Admissibility names neither a claim-axis labeling of history-tied
neighbors nor the July-3 pair as the framework's fixed rule. Record
permanence is used only to treat the locks on `U` as already given.
Formation site and rate remain outside the axiom memo.
Qubit remains `M_2(C)`. No axiom edit.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Finite exact ℓ¹ geometry on one off-axis three-ball union, nearest-seed history kernels, claim-axis vectors w − s*(w) on history-tied neighbors, remaining ties, eight completions, and membership in the reconstructed July-3 k=3 pair. Displayed only."
trace_class: frontier_discovery
target_claim_id: skew_three_seed_claim_axis_label
target_blocker_text: "at unread v=(-1,1,1), whether claim-axis tie-breaks of history-tied neighbors yield a July-3 k=3 pair member"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the remaining 6-tuple and N_fire; do not write claim-axis into Admissibility, attach L1, or launch a 4th equal-radius ball"
conditional_surface_status: "exact on U=B_2(0)∪B_2((2,0,0))∪B_2((1,2,1)) at unread v=(-1,1,1); displayed, not adopted"
hypothetical_axiom_status: "not proposed; no axiom or approved primitive is added"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

Write `0 = (0,0,0)`, `p = (2,0,0)`, and `q = (1,2,1)`. The closed ℓ¹
ball of radius two is

`B_2(c) = { x ∈ Z^3 : |x − c|_1 ≤ 2 }`.

The locked set is the already-given union

`U = B_2(0) ∪ B_2((2,0,0)) ∪ B_2((1,2,1))`.

The three balls each have 25 sites. Pairwise overlaps are 7, 4, and 4,
and the triple overlap has 2 sites, so `|U| = 62`. The unread site is

`v = (−1,1,1)`.

Then `|v|_1 = 3`, `|v − p|_1 = 5`, and `|v − q|_1 = 3`, so `v ∉ U`.

The six nearest neighbors, in the declared order, are

| slot | neighbor | in `U` |
|---|---|---|
| `+x` | `(0,1,1)` | yes |
| `−x` | `(−2,1,1)` | no |
| `+y` | `(−1,2,1)` | yes |
| `−y` | `(−1,0,1)` | yes |
| `+z` | `(−1,1,2)` | no |
| `−z` | `(−1,1,0)` | yes |

Occupancy mask at `v`:

`m = (1, 0, 1, 1, 0, 1)`.

Letters are `{0, +, −}` with `0` empty/unread.

For occupied `w`, `s*(w)` is a nearest seed of `w` among `S`, lex-first
if tied. The history occupancy 6-tuple of `w` uses only the indicator
of `B_2(s*(w))`. That 6-tuple determines the dipole

`d_μ = occ_hist(w + e_μ) − occ_hist(w − e_μ)`, `n_hist = d/3`.

If exactly one component of `n_hist` is nonzero, the label of `w` is
the sign of that component. Otherwise the claim-axis vector is

`δ = w − s*(w)`,

the direction from the claiming seed to the neighbor. If exactly one
component of `δ` is nonzero, the label is the sign of that component.
Otherwise the occupied neighbor stays `tied`. Empty neighbors of `v`
stay `0`. This is not leftover-char of histlab, which stopped at
unique-axis of `n_hist`.

The July-3 pair is reconstructed, not imported as a table. Letters
`{0,1,2}` with `0` empty, `1 = +`, and `2 = −` color the six axis
directions. The proper cubic group `G+` is the 24 determinant-`+1`
signed permutation matrices acting on those directions. Spatial
inversion `P = −I` exchanges `+μ` with `−μ`. A `G+`-orbit is chiral
when `P` sends it to a different `G+`-orbit. At three letters there is
exactly one such pair; its two orbits have 24 members each. The
formation predicate `f` is membership in that 48-element set. Do not
overwrite existing locks.

## Theorem 1 — Completed 6-tuple after claim-axis

Nearest seeds, history kernels, and claim-axis vectors on the four
occupied neighbors are exact:

| neighbor | `s*(w)` | `n_hist` | hist | `δ = w − s*(w)` | label |
|---|---|---|---|---|---|
| `(0,1,1)` | `(0,0,0)` | `(0, −1/3, −1/3)` | tied | `(0, 1, 1)` | tied |
| `(−1,2,1)` | `(1,2,1)` | `(1/3, 0, 0)` | `+` | `(−2, 0, 0)` | `+` |
| `(−1,0,1)` | `(0,0,0)` | `(1/3, 0, −1/3)` | tied | `(−1, 0, 1)` | tied |
| `(−1,1,0)` | `(0,0,0)` | `(1/3, −1/3, 0)` | tied | `(−1, 1, 0)` | tied |

The neighbor `(0,1,1)` is ℓ¹-tied between `0` and `(1,2,1)` at
distance 2; lex-first selects `0`. The other three occupied neighbors
have a unique nearest seed.

Claim-axis is applied only when `n_hist` is tied. Each of the three
history-tied `δ` has two nonzero coordinates, so none receives a
claim-axis sign. The unique-axis history label at `(−1,2,1)` is kept;
its `δ = (−2, 0, 0)` is not used to overwrite that sign.

The completed 6-tuple at `v` is therefore

`(tied, 0, +, tied, 0, tied)`.

Not every occupied neighbor is labeled: three of the four occupied
slots remain tied.

Scoring only `U` and the star at `v`. The center `v` is not already in
`U`. This is not leftover-char of histlab (unique-axis): the present
objects are the claim-axis vectors `w − s*(w)` on history-tied
neighbors.

## Theorem 2 — Not fully labeled; `N_fire` among remaining completions

The 6-tuple is not fully labeled, so it is not itself a July-3 pair
member. The eight `{+,−}` completions of the three remaining tied
slots, and pair membership, are

| completion | pair member |
|---|---|
| `(+,0,+,+,0,+)` | no |
| `(+,0,+,+,0,−)` | no |
| `(+,0,+,−,0,+)` | no |
| `(+,0,+,−,0,−)` | yes |
| `(−,0,+,+,0,+)` | no |
| `(−,0,+,+,0,−)` | no |
| `(−,0,+,−,0,+)` | yes |
| `(−,0,+,−,0,−)` | no |

So `N_fire = 2`. The firing completions are

`(+,0,+,−,0,−)`

and

`(−,0,+,−,0,+)`.

The reconstructed pair has `N_pair = 48`.

## Theorem 3 — Displayed, not adopted

The completed 6-tuple, the claim-axis table, the eight remaining
completions, and the count `N_fire` are displayed member data. They
are not the framework's fixed Admissibility rule.
Do not write claim-axis into Admissibility.
Do not attach L1. Failed-bar: no 4th equal-radius ball.
Occupancy-only formation (the `n ≠ 0` gate) is not attached. Qubit
remains `M_2(C)`. No approved primitive is added. No axiom edit.

This note is not leftover-char of histlab (unique-axis), which asked
only whether unique-axis signs of `n_hist` fully labeled the star.

## Honest-auditor / Boundary

- **What is proved.** On this `U`, at this unread `v`, claim-axis
  tie-breaks of the three history-tied neighbors leave the 6-tuple
  `(tied, 0, +, tied, 0, tied)`. Not every occupied neighbor is
  labeled. Exactly two of the eight remaining completions are July-3
  `k = 3` pair members.
- **What is displayed only.** The pair, the letter identification
  `{+, −}`, the claim-axis labels, and the eight completions are one
  rival comparison. They are not adopted.
- **What is not claimed.** No attachment of claim-axis to
  Admissibility; no attachment of occupancy-only formation; no axiom
  edit; no formation rate; no lattice-wide dynamics; no claim that
  Admissibility selects a firing completion; no fourth equal-radius
  ball.
- **Mutation controls.** The completed 6-tuple differing from
  `(tied, 0, +, tied, 0, tied)` fails. `N_fire ≠ 2` fails. A note that
  writes claim-axis into Admissibility, attaches L1, or authors an
  audit verdict fails.

This note authors no audit verdict.

## Primary Runner

The primary runner rebuilds `U`, the star at `v`, nearest seeds,
history kernels, claim-axis vectors, remaining ties, the eight
completions of those ties, the July-3 pair, `N_fire`, the current
premise boundary, and the mutation controls. It writes no cache and
authors no audit verdict.
