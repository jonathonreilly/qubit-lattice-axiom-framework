---
claim_id: skew_three_seed_delta_sign_product_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On the off-axis three-ball union at unread v=(-1,1,1), whether the product of signs of nonzero coordinates of each tied claim-delta yields a July-3 k=3 pair member is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_covariance_extension_classification_openness_achiral_oriented_frame_minimal_chiral_channel_bounded_theorem_note_2026-07-03
runner: scripts/skew_three_seed_delta_sign_product_2026_08_15.py
---

# Product Of Claim-Delta Signs At The Off-Axis Three-Seed Breaker (Bounded Theorem)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact occupancy on
`U = B_2(0) ∪ B_2((2,0,0)) ∪ B_2((1,2,1))` and the unread six-neighbor
star at `v = (−1,1,1)`. For each occupied neighbor, unique-axis history
labels from the nearest-seed ball, then — when `n_hist` is tied — the
product of the signs of the nonzero coordinates of the claim-delta
`δ = w − s*(w)`. Completed 6-tuple, whether every occupied neighbor is
labeled, and whether that 6-tuple is a July-3 `k = 3` pair member.
Score `U` and the star at `v` only. Displayed, not adopted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/skew_three_seed_delta_sign_product_2026_08_15.py`](../scripts/skew_three_seed_delta_sign_product_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)
and the July-3 classification
[`ADMISSIBILITY_RULE_COVARIANCE_EXTENSION_CLASSIFICATION_OPENNESS_ACHIRAL_ORIENTED_FRAME_MINIMAL_CHIRAL_CHANNEL_BOUNDED_THEOREM_NOTE_2026-07-03.md`](ADMISSIBILITY_RULE_COVARIANCE_EXTENSION_CLASSIFICATION_OPENNESS_ACHIRAL_ORIENTED_FRAME_MINIMAL_CHIRAL_CHANNEL_BOUNDED_THEOREM_NOTE_2026-07-03.md).

## Result Up Front

Investment `#6660` (seedax, unique-axis of `δ`) reported that on this
off-axis triple the three history-tied claim-deltas are two-support:
`(0,1,1)`, `(−1,0,1)`, `(−1,1,0)`. Unique-axis of `δ` therefore fails,
and the 6-tuple remains `(tied, 0, +, tied, 0, tied)`. The residual
here is not leftover-char of seedax (that used the unique nonzero of
`δ`). It is whether the product of the signs of the nonzero
coordinates of each tied `δ` — a displayed two-support scalar —
finishes the labels, and whether the completed 6-tuple is a July-3
`k = 3` pair member.

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
that coordinate. Else let `δ = w − s*(w)`. The label is the product of
the signs of the nonzero coordinates of `δ`. If the support of `δ` is
empty, the empty product is undefined and the slot stays tied. Empty
slots stay `0`.

The completed 6-tuple is

`(+,0,+,−,0,−)`.

Every occupied neighbor is labeled. The three history-tied slots
receive the two-support products `+x → +`, `−y → −`, `−z → −`. The
unique-axis history label at `+y` remains `+`. That slot is not
reassigned by the product (its `δ = (−2, 0, 0)` is unused because
`n_hist` already has a unique axis).

That 6-tuple is a July-3 `k = 3` pair member. It is one of the two
known firing completions of the seedax residual
`(tied, 0, +, tied, 0, tied)`.

The comparison is displayed, not adopted.
Do not write the product rule into Admissibility.
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

Admissibility names neither a product of claim-delta signs of
history-tied neighbors nor the July-3 pair as the framework's fixed
rule. Record permanence is used only to treat the locks on `U` as
already given. Formation site and rate remain outside the axiom memo.
Qubit remains `M_2(C)`. No axiom edit.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Finite exact ℓ¹ geometry on one off-axis three-ball union, nearest-seed history kernels, product of signs of nonzero coordinates of each tied claim-delta, completed 6-tuple, and membership in the reconstructed July-3 k=3 pair. Displayed only."
trace_class: frontier_discovery
target_claim_id: skew_three_seed_delta_sign_product
target_blocker_text: "at unread v=(-1,1,1), whether the product of signs of nonzero coordinates of each tied claim-delta yields a July-3 k=3 pair member"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the completed 6-tuple and pair membership; do not write the product rule into Admissibility, attach L1, or launch a 4th equal-radius ball"
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

the direction from the claiming seed to the neighbor. The label is the
product of the signs of the nonzero coordinates of `δ`. If
`|supp δ| = 0`, the empty product is undefined and the occupied
neighbor stays `tied`. Empty neighbors of `v` stay `0`. This is not
leftover-char of seedax, which used the unique nonzero of `δ`.

The July-3 pair is reconstructed, not imported as a table. Letters
`{0,1,2}` with `0` empty, `1 = +`, and `2 = −` color the six axis
directions. The proper cubic group `G+` is the 24 determinant-`+1`
signed permutation matrices acting on those directions. Spatial
inversion `P = −I` exchanges `+μ` with `−μ`. A `G+`-orbit is chiral
when `P` sends it to a different `G+`-orbit. At three letters there is
exactly one such pair; its two orbits have 24 members each. The
formation predicate `f` is membership in that 48-element set. Do not
overwrite existing locks.

## Theorem 1 — Completed 6-tuple after the product of claim-delta signs

Nearest seeds, history kernels, claim-deltas, and sign products on the
four occupied neighbors are exact:

| neighbor | `s*(w)` | `n_hist` | hist | `δ = w − s*(w)` | `supp δ` | product | label |
|---|---|---|---|---|---|---|---|
| `(0,1,1)` | `(0,0,0)` | `(0, −1/3, −1/3)` | tied | `(0, 1, 1)` | 2 | `(+)(+)=+` | `+` |
| `(−1,2,1)` | `(1,2,1)` | `(1/3, 0, 0)` | `+` | `(−2, 0, 0)` | 1 | unused | `+` |
| `(−1,0,1)` | `(0,0,0)` | `(1/3, 0, −1/3)` | tied | `(−1, 0, 1)` | 2 | `(−)(+)=−` | `−` |
| `(−1,1,0)` | `(0,0,0)` | `(1/3, −1/3, 0)` | tied | `(−1, 1, 0)` | 2 | `(−)(+)=−` | `−` |

The neighbor `(0,1,1)` is ℓ¹-tied between `0` and `(1,2,1)` at
distance 2; lex-first selects `0`. The other three occupied neighbors
have a unique nearest seed.

The product is applied only when `n_hist` is tied. Each of the three
history-tied `δ` is two-support, so unique-axis of `δ` fails and the
label is the displayed two-support scalar: product of the nonzero
signs. The unique-axis history label at `(−1,2,1)` is kept; its
`δ = (−2, 0, 0)` is not used to overwrite that sign.

The completed 6-tuple at `v` is therefore

`(+,0,+,−,0,−)`.

Every occupied neighbor is labeled: all four occupied slots receive a
letter. Empty slots remain `0`.

Scoring only `U` and the star at `v`. The center `v` is not already in
`U`. This is not leftover-char of seedax (unique nonzero of `δ`): the
present object is the product of the signs of the nonzero coordinates
of each tied claim-delta.

## Theorem 2 — The completed 6-tuple is a July-3 `k = 3` pair member

The 6-tuple is fully labeled. The reconstructed July-3 `k = 3` pair
has `N_pair = 48`. The completed coloring

`(+,0,+,−,0,−)`

is a member of that pair. There is one completion of the (now empty)
tie set, and `N_fire = 1`.

## Theorem 3 — Displayed, not adopted

The completed 6-tuple, the claim-delta table, the three two-support
products, and pair membership are displayed member data. They are not
the framework's fixed Admissibility rule.
Do not write the product rule into Admissibility.
Do not attach L1. Failed-bar: no 4th equal-radius ball.
Occupancy-only formation (the `n ≠ 0` gate) is not attached. Qubit
remains `M_2(C)`. No approved primitive is added. No axiom edit.

This note is not leftover-char of seedax (unique nonzero of `δ`),
which asked only whether unique-axis of each claim-delta fully labeled
the star.

## Honest-auditor / Boundary

- **What is proved.** On this `U`, at this unread `v`, the product of
  the signs of the nonzero coordinates of each tied claim-delta
  completes the 6-tuple to `(+,0,+,−,0,−)`. Every occupied neighbor
  is labeled. That 6-tuple is a July-3 `k = 3` pair member.
- **What is displayed only.** The pair, the letter identification
  `{+, −}`, and the product of claim-delta signs are one rival
  comparison. They are not adopted.
- **What is not claimed.** No attachment of the product rule to
  Admissibility; no attachment of occupancy-only formation; no axiom
  edit; no formation rate; no lattice-wide dynamics; no claim that
  Admissibility selects this labeling; no fourth equal-radius ball.
- **Mutation controls.** The completed 6-tuple differing from
  `(+,0,+,−,0,−)` fails. Failure of pair membership fails. A note that
  writes the product rule into Admissibility, attaches L1, or authors
  an audit verdict fails.

This note authors no audit verdict.

## Primary Runner

The primary runner rebuilds `U`, the star at `v`, nearest seeds,
history kernels, claim-deltas, products of nonzero signs, the
completed 6-tuple, the July-3 pair, pair membership, the current
premise boundary, and the mutation controls. It writes no cache and
authors no audit verdict.
