---
claim_id: skew_three_seed_local_n_equivariance_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On the off-axis three-ball star at v=(-1,1,1), whether the firing local-in-n labeling is equivariant under the 24 proper cube rotations is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/skew_three_seed_local_n_equivariance_2026_08_15.py
---

# Local-In-`n` Firing Map Cube Equivariance On The Off-Axis Three-Seed Star (Bounded Theorem)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** the unread six-neighbor star at `v = (−1,1,1)` on
`U = B_2(0) ∪ B_2((2,0,0)) ∪ B_2((1,2,1))`. The displayed firing
local-in-`n` map of `#6655` is scored for commutation with the 24
proper cube rotations acting jointly on slots and on `n`. Score the
star at `v` only. Displayed, not adopted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/skew_three_seed_local_n_equivariance_2026_08_15.py`](../scripts/skew_three_seed_local_n_equivariance_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md).

## Result Up Front

Investment `#6656` (skewrun execution) ran the local-in-`n` 6-tuple
`c = (−,0,+,−,0,+)` at unread `v = (−1,1,1)` and reported a fire.
Investment slotn displayed a different rule — a slot-odd tie-break —
that fired and commuted for only `3/24` proper rotations. The residual
here is not leftover-char of skewrun (execution) and not leftover-char
of slotn (different rule). It is whether *this* `f(n)` labeling
commutes with `G+` on the star at `v`.

Treat `U` as already locked. The site `v = (−1,1,1)` is unread. Direction
order is

`(+x, −x, +y, −y, +z, −z)`.

Occupancy mask

`m = (1, 0, 1, 1, 0, 1)`.

The displayed local-in-`n` map labels an occupied neighbor `w` by the
dipole `n = d/3` at `w`: unique-axis sign where `|supp n| = 1`;
otherwise the letter that map assigns to that `n` (shared kernel
`n = (1/3, 0, −1/3) → −`, and `n = (1/3, −1/3, 0) → +`). Empty stays
`0`. On this star that map produces

`c = (−,0,+,−,0,+)`.

A rotation `g ∈ G+` acts on slots and on `n`. The commutation count on
the six slots is

`N_commute = 1`,

so `1/24`. Only the identity keeps every rotated two-support kernel
inside the displayed table and reproduces the transported letters. In
particular `N_commute ≠ 24`, so the firing local-in-`n` map is not a
cube-covariant Admissibility rule.

The two two-support kernels lie in one `G+` orbit and receive opposite
letters. No function of `n` alone that assigns those two letters can
commute with every proper cube rotation.

Displayed, not adopted. Do not write the map into Admissibility. Do not
attach L1. Do not add a 4th ball. Qubit remains `M_2(C)`. No axiom edit.

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

Admissibility names neither the 6-tuple `c` nor the displayed local-in-`n`
table as the framework's fixed rule. The covariance clause is the test
this note applies to that table on this star. Formation site and rate
remain outside the axiom memo. Qubit remains `M_2(C)`. No axiom edit.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Finite exact ℓ¹ geometry on one unread six-neighbor star and a 24-element commutation count for one displayed local-in-n table. Displayed map only."
trace_class: frontier_discovery
target_claim_id: skew_three_seed_local_n_equivariance
target_blocker_text: "on the off-axis three-ball star at v=(-1,1,1), whether the firing local-in-n labeling commutes with the 24 proper cube rotations"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of N_commute; do not write the map into Admissibility, attach L1, or add a 4th ball"
conditional_surface_status: "exact on the star at v=(-1,1,1); N_commute=1 of 24; displayed, not adopted"
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

At a site `w`, the occupancy 6-tuple of its neighbors inside `U`
determines the dipole

`d_μ = occ(w + e_μ) − occ(w − e_μ)`, `n = d/3`.

The displayed local-in-`n` map `f` on a kernel is:

- empty slot: `f = 0`;
- `|supp n| = 1`: `f` is the sign of the unique nonzero component;
- `n = (1/3, 0, −1/3)` (the shared kernel on this star): `f = −`;
- `n = (1/3, −1/3, 0)`: `f = +`;
- any other occupied kernel is outside the displayed table.

`G+` is the 24 determinant-`+1` signed permutation matrices of the
three axes. A matrix `g` sends slot `μ` to `gμ` and sends a kernel `n`
to the vector `g n`. Letters move with their slots. Commutation at `g`
is the identity

`label(g · slot, g · n) = g · label(slot, n)`

on all six slots. `N_commute` is the number of such `g`.

## Theorem 1 — commutation count on this star

The occupancy dipoles on the four occupied neighbors are exact:

| neighbor | `n` | `f(n)` |
|---|---|---|
| `(0,1,1)` | `(1/3, 0, −1/3)` | `−` |
| `(−1,2,1)` | `(1/3, 0, 0)` | `+` |
| `(−1,0,1)` | `(1/3, 0, −1/3)` | `−` |
| `(−1,1,0)` | `(1/3, −1/3, 0)` | `+` |

Empty slots stay `0`. The labeled 6-tuple is therefore

`c = (−,0,+,−,0,+)`.

Enumerating all 24 elements of `G+` and comparing the transported
labeling with the labeling rebuilt from the transported kernels gives

`N_commute = 1`

out of 24, written `1/24`. The identity commutes. Every non-identity
`g` either sends a two-support kernel off the two-row displayed table
or rebuilds a different 6-tuple. The two two-support kernels are
`G+`-related: a proper rotation carries `(1/3, 0, −1/3)` to
`(1/3, −1/3, 0)`, while the displayed table assigns those two vectors
opposite letters.

Scoring only the star at `v`. This is not leftover-char of skewrun
(execution): the fire at `v` is not re-run. It is not leftover-char of
slotn (different rule): slot-odd uses the slot name, not only `n`.

## Theorem 2 — the firing map is not cube-equivariant

Because `N_commute ≠ 24`, the displayed local-in-`n` map does not
commute with every proper cube rotation of this star. The firing
local-in-`n` map is not a cube-covariant Admissibility rule.

The obstruction is already visible in the table: a cube-covariant
function of `n` cannot send two `G+`-images of one kernel to opposite
letters.

## Theorem 3 — displayed, not adopted

The map and the commutation count are displayed member data. They are
not the framework's fixed Admissibility rule. This note does not write
the map into Admissibility. Do not write the map into Admissibility.
Do not attach L1. Do not add a 4th ball. Occupancy-only formation
(the `n ≠ 0` gate) is not attached. Qubit remains `M_2(C)`. No approved
primitive is added. No axiom edit.

## Honest-auditor / Boundary

- **What is proved.** On this unread star, the displayed local-in-`n`
  map reproduces `c = (−,0,+,−,0,+)` and commutes with `1` of the `24`
  proper cube rotations.
- **What is displayed only.** The map, the letter identification
  `{+, −}`, and the commutation count are one rival table. They are
  not adopted.
- **What is not claimed.** No attachment of a local-in-`n` labeling to
  Admissibility; no attachment of occupancy-only formation; no axiom
  edit; no formation rate; no lattice-wide dynamics; no claim that
  Admissibility selects `c`; no fourth equal-radius ball; no re-run of
  the skewrun fire; no slot-odd rule.
- **Mutation controls.** A rebuilt `c` other than `(−,0,+,−,0,+)`
  fails. `N_commute = 24` would fail the non-covariance report. A note
  that writes the map into Admissibility, attaches L1, or authors an
  audit verdict fails.

This note authors no audit verdict.

## Primary Runner

The primary runner rebuilds `U`, the star at `v`, the displayed
local-in-`n` table, the 24 proper cube rotations, `N_commute`, the
current premise boundary, and the mutation controls. It writes no
cache and authors no audit verdict.
