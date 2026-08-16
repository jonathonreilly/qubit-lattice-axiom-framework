---
claim_id: weight4_occupancy_three_ball_realization_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Among weight-4 occupancies that admit a Stab-invariant July-3 pair member, whether a 3-ball union realizes one at an unread site is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/weight4_occupancy_three_ball_realization_2026_08_15.py
---

# Weight-4 Occupancy Three-Ball Realization (Bounded Theorem)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** the 15 weight-4 occupancy masks on the six-neighbor star, the
July-3 pair and `G+` of the maskstab census, and 3-ball unions
`U = B_2(s1) ∪ B_2(s2) ∪ B_2(s3)` with distinct centers in `[−2,2]³`
together with unread sites `v ∉ U` in the box `||v||_∞ ≤ 3`. Score
3-ball unions and stars only. Displayed, not adopted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/weight4_occupancy_three_ball_realization_2026_08_15.py`](../scripts/weight4_occupancy_three_ball_realization_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md).

## Result Up Front

Investment maskstab lists which weight-4 occupancy masks have
`N_stab_ok > 0` (fair pair candidates). Investment staborb/orbfire
scores one named three-ball occupancy. Investment 3ball scores tied-`n`
geometry only. The residual here is not leftover of staborb/orbfire
(one mask) or 3ball (tied-n geometry only). It is whether any
Stab-ok weight-4 mask appears as the 6-NN occupancy of an unread site
on a 3-ball union.

Direction order is

`(+x, −x, +y, −y, +z, −z)`.

`G+` is the 24 proper cube rotations acting on slots. The July-3
`k = 3` chiral pair is the unique pair of `G+` orbits of handed
fully-mixed 6-tuples; it has 48 members. Same pair and `G+` as
maskstab.

Weight-4 masks are the 15 bitstrings in `{0,1}^6` with four `1`s.
For each mask `σ`, `Stab(σ)` is the stabilizer in `G+`,
`N_pair_support` is the number of pair members with that support, and
`N_stab_ok` is the number of those members fixed by every element of
`Stab(σ)`.

**Theorem 1.** Rebuild `N_ok_masks` (same census as maskstab). The
15-row census has `N_stab_ok = 0` on every row, so

`N_ok_masks = 0`.

There is no lex-first ok-mask. Because `N_ok_masks = 0`, set
`N_real = 0` and stop the search.

**Theorem 2.** `N_real` is the number of ok-masks realized by some
3-ball `U` and unread `v` in the box above. With no ok-mask to
realize,

`N_real = 0`.

There is no lex-first realizing `(centers, v, σ)`.

**Theorem 3.** Displayed, not adopted. Do not write a realizing U into
Admissibility. Do not attach L1. Do not add a 4th ball. Qubit remains
`M_2(C)`. No axiom edit.

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

Admissibility names neither a weight-4 occupancy mask nor a realizing
3-ball union as the framework's fixed rule. Formation site and rate
remain outside the axiom memo. Qubit remains `M_2(C)`. No axiom edit.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Finite exact census of the 15 weight-4 occupancy masks against the July-3 pair, then a gated 3-ball realization count. Displayed counts only."
trace_class: frontier_discovery
target_claim_id: weight4_occupancy_three_ball_realization
target_blocker_text: "among weight-4 occupancies that admit a Stab-invariant July-3 pair member, whether a 3-ball union realizes one at an unread site"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of N_ok_masks and N_real; do not write a realizing U into Admissibility, attach L1, or add a 4th ball"
conditional_surface_status: "exact on the 15 weight-4 masks and the gated 3-ball search; N_ok_masks=0; N_real=0; displayed, not adopted"
hypothetical_axiom_status: "not proposed; no axiom or approved primitive is added"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

Slots are `(+x, −x, +y, −y, +z, −z)`. Occupancy at an unread site `v`
relative to a locked set `U` is the 6-bit indicator

`σ(U, v)_μ = 1` if and only if `v + e_μ ∈ U`.

Weight is the number of occupied slots. The 15 weight-4 masks are every
element of `{0,1}^6` with four ones.

`G+` is the 24 determinant-`+1` signed permutation matrices of the three
axes. A matrix `g` permutes the six axis directions: the bit (or letter)
at slot `μ` moves to slot `gμ`. The occupancy stabilizer is

`Stab(σ) = { g in G+ : g · σ = σ }`.

The July-3 `k = 3` chiral pair is reconstructed by enumerating the 24
proper rotations on `{0,1,2}^6` (57 orbits) and retaining the unique pair
of orbits exchanged by spatial inversion. It has 48 members. Fully mixed
means every axis is bi-colored and each letter is used twice. Support of
a 6-tuple is the slots with a nonzero letter.

`N_pair_support` is the number of pair members whose support equals `σ`.
`N_stab_ok` is the number of those members `c` with `g · c = c` for every
`g` in `Stab(σ)`. `N_ok_masks` is the number of weight-4 masks with
`N_stab_ok > 0`.

Write `B_2(c) = { x ∈ Z^3 : |x − c|_1 ≤ 2 }`. A 3-ball union is

`U = B_2(s1) ∪ B_2(s2) ∪ B_2(s3)`

with distinct `si` in `[−2,2]³`. An unread site is `v ∉ U` with
`||v||_∞ ≤ 3`. A realization of a mask `σ` is a pair `(U, v)` with
`σ(U, v) = σ` and `wt(σ) = 4`. `N_real` is the number of ok-masks that
admit at least one such pair. Short-circuit after the first hit per
ok-mask. Score 3-ball unions and stars only.

## Theorem 1 — rebuild `N_ok_masks`

The 15 weight-4 masks, in lex order, have the rebuilt census

| `σ` | `|Stab(σ)|` | `N_pair_support` | `N_stab_ok` |
|---|---|---|---|
| `(0, 0, 1, 1, 1, 1)` | 8 | 0 | 0 |
| `(0, 1, 0, 1, 1, 1)` | 2 | 4 | 0 |
| `(0, 1, 1, 0, 1, 1)` | 2 | 4 | 0 |
| `(0, 1, 1, 1, 0, 1)` | 2 | 4 | 0 |
| `(0, 1, 1, 1, 1, 0)` | 2 | 4 | 0 |
| `(1, 0, 0, 1, 1, 1)` | 2 | 4 | 0 |
| `(1, 0, 1, 0, 1, 1)` | 2 | 4 | 0 |
| `(1, 0, 1, 1, 0, 1)` | 2 | 4 | 0 |
| `(1, 0, 1, 1, 1, 0)` | 2 | 4 | 0 |
| `(1, 1, 0, 0, 1, 1)` | 8 | 0 | 0 |
| `(1, 1, 0, 1, 0, 1)` | 2 | 4 | 0 |
| `(1, 1, 0, 1, 1, 0)` | 2 | 4 | 0 |
| `(1, 1, 1, 0, 0, 1)` | 2 | 4 | 0 |
| `(1, 1, 1, 0, 1, 0)` | 2 | 4 | 0 |
| `(1, 1, 1, 1, 0, 0)` | 8 | 0 | 0 |

The three same-axis empty masks have `|Stab| = 8` and
`N_pair_support = 0`: a fully mixed pair member cannot place both empty
letters on one axis. The remaining twelve masks have `|Stab| = 2` and
`N_pair_support = 4`. On each of those twelve the nontrivial stabilizer
element swaps the two slots of the fully occupied axis, so it cannot fix
a bi-colored pair member. Therefore every row has `N_stab_ok = 0`, and

`N_ok_masks = 0`.

There is no lex-first ok-mask. If `N_ok_masks = 0`, set `N_real = 0` and
stop the search. That clause is triggered.

This is the same census as maskstab. It is not leftover of
staborb/orbfire (one mask): those notes score
`σ = (1, 0, 1, 1, 0, 1)` only. It is not leftover of 3ball (tied-n
geometry only): that note does not census Stab-ok pair members.

## Theorem 2 — `N_real` on the gated box

`N_real` is the number of ok-masks realized by some 3-ball union
`U = B_2(s1) ∪ B_2(s2) ∪ B_2(s3)` with distinct centers in `[−2,2]³`
and an unread site `v ∉ U` with `||v||_∞ ≤ 3`. The search, if run,
short-circuits after the first hit per ok-mask and would report the
lex-first realizing `(centers, v, σ)`.

Because Theorem 1 gives `N_ok_masks = 0`, the search is not run and

`N_real = 0`.

There is no lex-first realizing `(centers, v, σ)`. No weight-4
occupancy that admits a Stab-invariant July-3 pair member is available
to realize, so no such mask appears as the 6-NN occupancy of an unread
site on a 3-ball union in the box.

## Theorem 3 — displayed, not adopted

The census, the count `N_ok_masks = 0`, and the gated count
`N_real = 0` are displayed member data. They are not the framework's
fixed Admissibility rule. This note does not write a realizing U into
Admissibility. Do not write a realizing U into Admissibility. Do not
attach L1. Do not add a 4th ball. Occupancy-only formation is not
attached. Qubit remains `M_2(C)`. No approved primitive is added. No
axiom edit.

## Honest-auditor / Boundary

- **What is proved.** On the 15 weight-4 occupancy masks, `N_ok_masks = 0`.
  The realization search therefore stops and `N_real = 0`.
- **What is displayed only.** The 15-row census and the two counts are
  one rival table. They are not adopted.
- **What is not claimed.** No attachment of a realizing union to
  Admissibility; no attachment of occupancy-only formation; no axiom
  edit; no formation rate; no lattice-wide dynamics; no fourth
  equal-radius ball; no leftover of staborb/orbfire (one mask); no
  leftover of 3ball (tied-n geometry only); no compiler no-go.
- **Mutation controls.** A rebuilt row with `N_stab_ok > 0` fails the
  `N_ok_masks = 0` report and would require running the 3-ball search.
  A note that writes a realizing U into Admissibility, attaches L1, or
  authors an audit verdict fails.

This note authors no audit verdict.

## Primary Runner

The primary runner rebuilds `G+`, the July-3 pair, the 15 weight-4
occupancy-mask census, `N_ok_masks`, the gated 3-ball realization
count `N_real`, the current premise boundary, and the mutation
controls. It writes no cache and authors no audit verdict.
