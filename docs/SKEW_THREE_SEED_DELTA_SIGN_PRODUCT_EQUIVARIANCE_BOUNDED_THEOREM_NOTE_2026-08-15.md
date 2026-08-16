---
claim_id: skew_three_seed_delta_sign_product_equivariance_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On the off-axis three-ball star at v=(-1,1,1), whether the claim-delta sign-product labeling is equivariant under the 24 proper cube rotations is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/skew_three_seed_delta_sign_product_equivariance_2026_08_15.py
---

# Claim-Delta Sign-Product Cube Equivariance On The Off-Axis Three-Seed Star (Bounded Theorem)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** the unread six-neighbor star at `v = (−1,1,1)` on
`U = B_2(0) ∪ B_2((2,0,0)) ∪ B_2((1,2,1))`. The displayed claim-delta
sign-product rule of delsgn is scored for commutation with the 24
proper cube rotations acting jointly on slots, seeds, and `δ`. Score
the star at `v` only. Displayed, not adopted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/skew_three_seed_delta_sign_product_equivariance_2026_08_15.py`](../scripts/skew_three_seed_delta_sign_product_equivariance_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md).

## Result Up Front

Investment delsgn rebuilt a complete history tag on this star by the
product of the signs of the nonzero coordinates of each history-tied
claim-delta and reported that the completed 6-tuple fires. Investment
skeweq scored a different map — occupancy `f(n)` — and found that map
commutes for only `1/24` proper rotations. The residual here is not
leftover-char of delsgn (membership of that completed 6-tuple in the
July-3 pair) and not leftover-char of skeweq (different map). It is
whether *this* product-of-`δ`-signs labeling commutes with `G+` on the
star at `v`.

Treat `U` as already locked. The site `v = (−1,1,1)` is unread.
Direction order is

`(+x, −x, +y, −y, +z, −z)`.

Occupancy mask

`m = (1, 0, 1, 1, 0, 1)`.

Seeds are `S = {0, (2,0,0), (1,2,1)}`. For an occupied neighbor `w`,
the nearest seed `s*(w)` is a seed of least ℓ¹ distance; ties take the
lex-first seed. The history kernel `n_hist(w)` is the occupancy dipole
at `w` computed from occupancy in `B_2(s*(w))` only. If `n_hist(w)`
has a unique nonzero coordinate, the label is the sign of that
coordinate. Else `δ = w − s*(w)` and the label is the product of the
signs of the nonzero coordinates of `δ`. Empty stays `0`. On this
star that rule produces

`c = (+,0,+,−,0,−)`.

A rotation `g ∈ G+` acts about `v` on slots, on the three seeds, and
on each claim-delta. Commutation at `g` is the identity

`label(g · w) =` the product rule applied after rotating the seeds
and `w`.

The commutation count on the six slots is

`N_commute = 3`,

so `3/24`. The identity and the two sign-free 3-cycles of the axes
commute. Every other proper rotation rebuilds a different 6-tuple.
In particular `N_commute ≠ 24`, so this firing history tag is not a
cube-covariant Admissibility rule.

Displayed, not adopted. Do not write the product into Admissibility.
Do not attach L1. Do not add a 4th ball. Qubit remains `M_2(C)`. No
axiom edit.

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

Admissibility names neither the 6-tuple `c` nor the product of
claim-delta signs as the framework's fixed rule. The covariance clause
is the test this note applies to that product on this star. Formation
site and rate remain outside the axiom memo. Qubit remains `M_2(C)`.
No axiom edit.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Finite exact ℓ¹ geometry on one unread six-neighbor star and a 24-element commutation count for one displayed claim-delta sign-product rule. Displayed rule only."
trace_class: frontier_discovery
target_claim_id: skew_three_seed_delta_sign_product_equivariance
target_blocker_text: "on the off-axis three-ball star at v=(-1,1,1), whether the claim-delta sign-product labeling commutes with the 24 proper cube rotations"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of N_commute; do not write the product into Admissibility, attach L1, or add a 4th ball"
conditional_surface_status: "exact on the star at v=(-1,1,1); N_commute=3 of 24; displayed, not adopted"
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

For occupied `w`, `s*(w)` is a nearest seed of `w` among `S`, lex-first
if tied. The history occupancy 6-tuple of `w` uses only the indicator
of `B_2(s*(w))`. That 6-tuple determines the dipole

`d_μ = occ_hist(w + e_μ) − occ_hist(w − e_μ)`, `n_hist = d/3`.

If exactly one component of `n_hist` is nonzero, the label of `w` is
the sign of that component. Otherwise the claim-delta is

`δ = w − s*(w)`,

and the label is the product of the signs of the nonzero coordinates
of `δ`. If `|supp δ| = 0`, the empty product is undefined and the
occupied neighbor stays tied. Empty neighbors of `v` stay `0`.

`G+` is the 24 determinant-`+1` signed permutation matrices of the
three axes. A matrix `g` acts about `v`: slot `μ` goes to `gμ`, a
site `x` goes to `v + g(x − v)`, and a vector `δ` goes to `gδ`. The
rotated seeds are `{ v + g(s − v) : s ∈ S }`. The product rule is
then rebuilt on the rotated seeds and the image neighbors of `v`.
Letters move with their slots. Commutation at `g` is

`label(g · w) =` the product rule applied after rotating seeds and `w`

on all six slots. `N_commute` is the number of such `g`.

## Theorem 1 — commutation count on this star

Nearest seeds, history kernels, claim-deltas, and product labels on the
four occupied neighbors are exact:

| neighbor | `s*(w)` | `n_hist` | hist | `δ = w − s*(w)` | product | label |
|---|---|---|---|---|---|---|
| `(0,1,1)` | `(0,0,0)` | `(0, −1/3, −1/3)` | tied | `(0, 1, 1)` | `+` | `+` |
| `(−1,2,1)` | `(1,2,1)` | `(1/3, 0, 0)` | `+` | `(−2, 0, 0)` | unused | `+` |
| `(−1,0,1)` | `(0,0,0)` | `(1/3, 0, −1/3)` | tied | `(−1, 0, 1)` | `−` | `−` |
| `(−1,1,0)` | `(0,0,0)` | `(1/3, −1/3, 0)` | tied | `(−1, 1, 0)` | `−` | `−` |

Empty slots stay `0`. The labeled 6-tuple is therefore

`c = (+,0,+,−,0,−)`.

Enumerating all 24 elements of `G+` and comparing the transported
labeling with the labeling rebuilt from the rotated seeds and image
neighbors gives

`N_commute = 3`

out of 24, written `3/24`. The three commuting rotations are the
identity and the two sign-free 3-cycles of the coordinate axes. Those
three send every unique-axis kernel to another unique-axis kernel of
the same sign and send every two-support claim-delta to a two-support
claim-delta with the same sign product. Every other `g` either flips
an odd number of support signs, moves the unique-axis letter, or
changes the lex-first nearest seed on a tied neighbor, and then
rebuilds a different 6-tuple.

Scoring only the star at `v`. This is not leftover-char of delsgn
(membership): the completed firing 6-tuple is not re-tested as a
July-3 pair member. It is not leftover-char of skeweq (different
map): skeweq scored occupancy `f(n)`, not the product of claim-delta
signs.

## Theorem 2 — the firing history tag is not cube-equivariant

Because `N_commute ≠ 24`, the displayed claim-delta sign-product rule
does not commute with every proper cube rotation of this star. This
firing history tag is not a cube-covariant Admissibility rule.

## Theorem 3 — displayed, not adopted

The product and the commutation count are displayed member data. They
are not the framework's fixed Admissibility rule. This note does not
write the product into Admissibility. Do not write the product into
Admissibility. Do not attach L1. Do not add a 4th ball.
Occupancy-only formation (the `n ≠ 0` gate) is not attached. Qubit
remains `M_2(C)`. No approved primitive is added. No axiom edit.

## Honest-auditor / Boundary

- **What is proved.** On this unread star, the displayed claim-delta
  sign-product rule reproduces `c = (+,0,+,−,0,−)` and commutes with
  `3` of the `24` proper cube rotations.
- **What is displayed only.** The product, the letter identification
  `{+, −}`, and the commutation count are one rival table. They are
  not adopted.
- **What is not claimed.** No attachment of the product to
  Admissibility; no attachment of occupancy-only formation; no axiom
  edit; no formation rate; no lattice-wide dynamics; no claim that
  Admissibility selects `c`; no fourth equal-radius ball; no re-test
  of delsgn pair membership; no occupancy `f(n)` map.
- **Mutation controls.** A rebuilt `c` other than `(+,0,+,−,0,−)`
  fails. `N_commute = 24` would fail the non-covariance report. A note
  that writes the product into Admissibility, attaches L1, or authors
  an audit verdict fails.

This note authors no audit verdict.

## Primary Runner

The primary runner rebuilds `U`, the star at `v`, nearest seeds,
history kernels, claim-deltas, the product rule, the 24 proper cube
rotations acting on slots, seeds, and `δ`, `N_commute`, the current
premise boundary, and the mutation controls. It writes no cache and
authors no audit verdict.
