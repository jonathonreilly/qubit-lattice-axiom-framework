---
claim_id: skew_three_seed_history_unique_axis_label_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On the off-axis three-ball union at unread v=(-1,1,1), whether unique-axis labels from each neighbor’s nearest-seed ball form a July-3 k=3 pair member is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_covariance_extension_classification_openness_achiral_oriented_frame_minimal_chiral_channel_bounded_theorem_note_2026-07-03
runner: scripts/skew_three_seed_history_unique_axis_label_2026_08_15.py
---

# Formation-History Unique-Axis Labels At The Off-Axis Three-Seed Breaker (Bounded Theorem)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact occupancy on
`U = B_2(0) ∪ B_2((2,0,0)) ∪ B_2((1,2,1))` and the unread six-neighbor
star at `v = (−1,1,1)`. For each occupied neighbor, the unique-axis
sign of the occupancy kernel computed from that neighbor’s nearest-seed
ball only (formation history), not from the final union `U`. History
6-tuple, whether every occupied neighbor has a unique-axis history
label, and `N_hist_fire` among completions of the tied slots. Score
`U` and the star at `v` only. Displayed, not adopted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/skew_three_seed_history_unique_axis_label_2026_08_15.py`](../scripts/skew_three_seed_history_unique_axis_label_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)
and the July-3 classification
[`ADMISSIBILITY_RULE_COVARIANCE_EXTENSION_CLASSIFICATION_OPENNESS_ACHIRAL_ORIENTED_FRAME_MINIMAL_CHIRAL_CHANNEL_BOUNDED_THEOREM_NOTE_2026-07-03.md`](ADMISSIBILITY_RULE_COVARIANCE_EXTENSION_CLASSIFICATION_OPENNESS_ACHIRAL_ORIENTED_FRAME_MINIMAL_CHIRAL_CHANNEL_BOUNDED_THEOREM_NOTE_2026-07-03.md).

## Result Up Front

Investment `#6658` (skeworb, final `n`) reported that on this off-axis
triple the distinct ambiguous final-`U` kernels at each of the four
`N_uneq` unread 4-occupied-NN sites lie in one `G+` orbit, so any
equivariant `f(n)` is constant on those kernels and cannot assign
opposite letters. The residual here is not leftover-char of skeworb
(final `n`). It is whether unique-axis labels taken from each occupied
neighbor’s *nearest-seed* ball — formation history, not the final
union — fire the July-3 `k = 3` pair at the same unread star
`v = (−1,1,1)`.

Treat `U` as already locked. The site `v = (−1,1,1)` is unread: it
lies in none of the three radius-two ℓ¹ balls. Direction order is

`(+x, −x, +y, −y, +z, −z)`.

The four occupied nearest neighbors of `v` in `U` are `+x`, `+y`,
`−y`, and `−z`. The two empty slots are `−x` and `+z`. Occupancy mask

`m = (1, 0, 1, 1, 0, 1)`.

Seeds are `S = {0, (2,0,0), (1,2,1)}`. For an occupied neighbor `w`,
the nearest seed `s*(w)` is a seed of least ℓ¹ distance; ties take the
lex-first seed. The history kernel `n_hist(w)` is the occupancy dipole
`n = d/3` at `w` computed from occupancy in `B_2(s*(w))` only. The
history label is the unique-axis sign of `n_hist(w)` when
`|supp n_hist(w)| = 1`, and `tied` otherwise. Empty slots stay `0`.

The history 6-tuple is

`(tied, 0, +, tied, 0, tied)`.

Not every occupied neighbor has a unique-axis history label. Exactly
one occupied neighbor, `+y`, is unique-axis (`+`). The three remaining
occupied slots are tied.

There are eight `{+,−}` completions of the three tied slots. Exactly
`N_hist_fire = 2` of them are July-3 pair members:

`(+,0,+,−,0,−)`

and

`(−,0,+,−,0,+)`.

The history 6-tuple itself is not fully labeled, so it is not itself a
pair member. Completions of the ties include two pair members.

The comparison is displayed, not adopted.
Do not write history labels into Admissibility.
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

Admissibility names neither a formation-history unique-axis labeling of
the occupied neighbors nor the July-3 pair as the framework's fixed
rule. Record permanence is used only to treat the locks on `U` as
already given. Formation site and rate remain outside the axiom memo.
Qubit remains `M_2(C)`. No axiom edit.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Finite exact ℓ¹ geometry on one off-axis three-ball union, nearest-seed history kernels on one six-neighbor star, unique-axis versus tied history labels, eight completions of three tied slots, and membership in the reconstructed July-3 k=3 pair. Displayed only."
trace_class: frontier_discovery
target_claim_id: skew_three_seed_history_unique_axis_label
target_blocker_text: "at unread v=(-1,1,1), whether unique-axis labels from each occupied neighbor's nearest-seed ball form a July-3 k=3 pair member"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the history 6-tuple and N_hist_fire; do not write history labels into Admissibility, attach L1, or launch a 4th equal-radius ball"
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

If exactly one component of `n_hist` is nonzero, the history label of
`w` is the sign of that component. Otherwise the occupied neighbor is
`tied`. Empty neighbors of `v` stay `0`. This is not the final-`U`
kernel of skeworb.

The July-3 pair is reconstructed, not imported as a table. Letters
`{0,1,2}` with `0` empty, `1 = +`, and `2 = −` color the six axis
directions. The proper cubic group `G+` is the 24 determinant-`+1`
signed permutation matrices acting on those directions. Spatial
inversion `P = −I` exchanges `+μ` with `−μ`. A `G+`-orbit is chiral
when `P` sends it to a different `G+`-orbit. At three letters there is
exactly one such pair; its two orbits have 24 members each. The
formation predicate `f` is membership in that 48-element set. Do not
overwrite existing locks.

## Theorem 1 — History 6-tuple and unique-axis occupancy

Nearest seeds, history occupancy 6-tuples, and history kernels on the
four occupied neighbors are exact:

| neighbor | `s*(w)` | history 6-tuple | `n_hist` | history label |
|---|---|---|---|---|
| `(0,1,1)` | `(0,0,0)` | `(0,0,0,1,0,1)` | `(0, −1/3, −1/3)` | tied |
| `(−1,2,1)` | `(1,2,1)` | `(1,0,0,0,0,0)` | `(1/3, 0, 0)` | `+` |
| `(−1,0,1)` | `(0,0,0)` | `(1,0,0,0,0,1)` | `(1/3, 0, −1/3)` | tied |
| `(−1,1,0)` | `(0,0,0)` | `(1,0,0,1,0,0)` | `(1/3, −1/3, 0)` | tied |

The neighbor `(0,1,1)` is ℓ¹-tied between `0` and `(1,2,1)` at
distance 2; lex-first selects `0`. The other three occupied neighbors
have a unique nearest seed.

The history 6-tuple at `v` is therefore

`(tied, 0, +, tied, 0, tied)`.

Not every occupied neighbor has a unique-axis history label: three of
the four occupied slots are tied.

Scoring only `U` and the star at `v`. The center `v` is not already in
`U`. This is not leftover-char of skeworb (final `n`): the present
objects are nearest-seed balls and `n_hist`, not the final-union
kernels.

## Theorem 2 — `N_hist_fire` among completions of the ties

The history 6-tuple is not fully labeled, so it is not itself a July-3
pair member. The eight `{+,−}` completions of the three tied slots, and
pair membership, are

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

So `N_hist_fire = 2`. The firing completions are

`(+,0,+,−,0,−)`

and

`(−,0,+,−,0,+)`.

The reconstructed pair has `N_pair = 48`.

## Theorem 3 — Displayed, not adopted

The history 6-tuple, the nearest-seed table, the eight completions, and
the count `N_hist_fire` are displayed member data. They are not the
framework's fixed Admissibility rule.
Do not write history labels into Admissibility.
Do not attach L1. Failed-bar: no 4th equal-radius ball.
Occupancy-only formation (the `n ≠ 0` gate) is not attached. Qubit
remains `M_2(C)`. No approved primitive is added. No axiom edit.

This note is not leftover-char of skeworb (final `n`), which asked only
whether the distinct ambiguous *final-union* kernels at the four
`N_uneq` sites lie in one `G+` orbit.

## Honest-auditor / Boundary

- **What is proved.** On this `U`, at this unread `v`, the history
  6-tuple from nearest-seed balls is `(tied, 0, +, tied, 0, tied)`, not
  every occupied neighbor has a unique-axis history label, and exactly
  two of the eight completions of the tied slots are July-3 `k = 3`
  pair members.
- **What is displayed only.** The pair, the letter identification
  `{+, −}`, the history labels, and the eight completions are one
  rival comparison. They are not adopted.
- **What is not claimed.** No attachment of history labels to
  Admissibility; no attachment of occupancy-only formation; no axiom
  edit; no formation rate; no lattice-wide dynamics; no claim that
  Admissibility selects a firing completion; no fourth equal-radius
  ball.
- **Mutation controls.** The history 6-tuple differing from
  `(tied, 0, +, tied, 0, tied)` fails. `N_hist_fire ≠ 2` fails. A note
  that writes history labels into Admissibility, attaches L1, or
  authors an audit verdict fails.

This note authors no audit verdict.

## Primary Runner

The primary runner rebuilds `U`, the star at `v`, nearest seeds,
history kernels, unique-axis history labels, the eight completions of
the tied slots, the July-3 pair, `N_hist_fire`, the current premise
boundary, and the mutation controls. It writes no cache and authors no
audit verdict.
