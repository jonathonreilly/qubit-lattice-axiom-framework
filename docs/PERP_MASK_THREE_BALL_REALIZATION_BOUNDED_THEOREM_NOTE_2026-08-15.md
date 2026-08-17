---
claim_id: perp_mask_three_ball_realization_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Among the 12 perpendicular weight-4 masks, how many are realized as unread 6-NN occupancy of a 3-ball union is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/perp_mask_three_ball_realization_2026_08_15.py
---

# Perpendicular Weight-4 Mask Three-Ball Realization (Bounded Theorem)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** the 12 perpendicular weight-4 occupancy masks on the six-neighbor
star, and 3-ball unions `U = B_{r1}(s1) ∪ B_{r2}(s2) ∪ B_{r3}(s3)` with
distinct centers in `[−2,2]³`, radii `ri ∈ {1,2,3}` not all equal, together
with unread sites `v ∉ U` in the box `‖v‖_∞ ≤ 4`. Score a prefix plus
existence per mask. Displayed, not adopted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/perp_mask_three_ball_realization_2026_08_15.py`](../scripts/perp_mask_three_ball_realization_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md).

## Result Up Front

Investment bitname: `f` is named on all 12 perp masks. Investment bitfire:
`f` fires on the uneqrad star (one mask). The residual here is not leftover
of uneqrad (one mask). Among the 12, how many appear as the 6-NN occupancy
of an unread site on a 3-ball union in the uneqrad box (radii in `{1,2,3}`)?

Direction order is

`(+x, −x, +y, −y, +z, −z)`.

A weight-4 mask is perpendicular when the two emptied slots lie on two
distinct axes. There are exactly 12 such masks. Centers are distinct sites
of `Z^3` in the cube `[−2,2]³`. Radii run over the 24 triples in `{1,2,3}³`
that are not all equal. Lex order is on the canonical tuple
`(s1,s2,s3, r1,r2,r3, v)` with `s1 < s2 < s3` in coordinate lex order.
An unread site is scored only when `wt(σ(U,v)) = 4`. Stop at the first
realization per mask. Also report the 2000-star prefix.

**Theorem 1.** `N_real = 12`. All 12 perpendicular weight-4 masks are
realized as unread 6-NN occupancy of a 3-ball union in the uneqrad box.

On the lex-first 2000 weight-4 stars,

`N_prefix = 2000`, `N_prefix_real = 12`.

**Theorem 2.** The lex-first host `(centers, radii, v)` of each realized
mask is the first unread weight-4 star in the uneqrad enumeration whose
occupancy equals that mask. Every mask has such a host; none is empty.

**Theorem 3.** Displayed, not adopted. Do not write a host into
Admissibility. Do not attach L1. Qubit remains `M_2(C)`. No axiom edit.

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

Admissibility names neither a perpendicular weight-4 occupancy mask nor a
realizing 3-ball union as the framework's fixed rule. Formation site and
rate remain outside the axiom memo. Qubit remains `M_2(C)`. No axiom edit.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Finite exact census of the 12 perpendicular weight-4 occupancy masks as unread 6-NN occupancy of uneqrad 3-ball unions, with a 2000-star prefix and a lex-first host per mask. Displayed counts only."
trace_class: frontier_discovery
target_claim_id: perp_mask_three_ball_realization
target_blocker_text: "among the 12 perpendicular weight-4 masks, how many are realized as unread 6-NN occupancy of a 3-ball union"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of N_real and the lex-first hosts; do not write a host into Admissibility or attach L1"
conditional_surface_status: "exact on the 12 perpendicular weight-4 masks in the uneqrad box; N_real=12; N_prefix=2000; N_prefix_real=12; displayed, not adopted"
hypothetical_axiom_status: "not proposed; no axiom or approved primitive is added"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

Slots are `(+x, −x, +y, −y, +z, −z)`. Occupancy at an unread site `v`
relative to a locked set `U` is the 6-bit indicator

`σ(U, v)_μ = 1` if and only if `v + e_μ ∈ U`.

Weight is the number of occupied slots. A weight-4 mask is perpendicular
when the two emptied slots lie on two distinct axes. The 12 perpendicular
masks, in lex order, are

`(0, 1, 0, 1, 1, 1)`,
`(0, 1, 1, 0, 1, 1)`,
`(0, 1, 1, 1, 0, 1)`,
`(0, 1, 1, 1, 1, 0)`,
`(1, 0, 0, 1, 1, 1)`,
`(1, 0, 1, 0, 1, 1)`,
`(1, 0, 1, 1, 0, 1)`,
`(1, 0, 1, 1, 1, 0)`,
`(1, 1, 0, 1, 0, 1)`,
`(1, 1, 0, 1, 1, 0)`,
`(1, 1, 1, 0, 0, 1)`,
`(1, 1, 1, 0, 1, 0)`.

The three same-axis empty weight-4 masks are not scored.

Write `B_r(c) = { x ∈ Z^3 : ‖x − c‖_1 ≤ r }`. A 3-ball union in the
uneqrad box is

`U = B_{r1}(s1) ∪ B_{r2}(s2) ∪ B_{r3}(s3)`

with distinct `si` in `[−2,2]³` and `(r1,r2,r3) ∈ {1,2,3}³` not all
equal. An unread site is `v ∉ U` with `‖v‖_∞ ≤ 4`. A star in the prefix
is such a `v` with `wt(σ(U,v)) = 4`. A realization of a perpendicular
mask `σ` is a pair `(U, v)` with `σ(U, v) = σ`. `N_real` is the number
of the 12 masks that admit at least one such pair. Short-circuit after
the first hit per mask. `N_prefix` is the number of weight-4 unread
stars in the lex-first 2000. `N_prefix_real` is how many of the 12
appear in that prefix.

## Theorem 1 — `N_real = 12`

Every one of the 12 perpendicular weight-4 masks appears as the 6-NN
occupancy of an unread site on some uneqrad 3-ball union in the box, so

`N_real = 12`.

The census lists all 12. On the lex-first 2000 weight-4 stars the same
12 already appear:

`N_prefix = 2000`, `N_prefix_real = 12`.

The last first-hit in that prefix is star 1410. This is not leftover of
uneqrad (one mask): uneqrad scores lock-tick Stab shrink on one breaker
star; bitfire scores whether `f` fires on that one star. The present
count is occupancy realization of each of the 12 masks.

## Theorem 2 — lex-first host per mask

The lex-first host is the first `(centers, radii, v)` in the uneqrad
enumeration whose unread 6-NN occupancy equals the mask. The twelve
hosts are

| `σ` | lex-first `(centers, radii, v)` |
|---|---|
| `(0, 1, 0, 1, 1, 1)` | `(((-2, -2, -2), (-2, -2, -1), (-2, -2, 0)), (2, 1, 2), (-1, -1, -1))` |
| `(0, 1, 1, 0, 1, 1)` | `(((-2, -2, -2), (-2, -2, -1), (-2, -2, 0)), (2, 1, 2), (-1, -3, -1))` |
| `(0, 1, 1, 1, 0, 1)` | `(((-2, -2, -2), (-2, -2, -1), (-2, 0, -2)), (1, 1, 2), (-1, -1, -1))` |
| `(0, 1, 1, 1, 1, 0)` | `(((-2, -2, -2), (-2, -2, -1), (-2, 0, -2)), (1, 2, 1), (-1, -1, -2))` |
| `(1, 0, 0, 1, 1, 1)` | `(((-2, -2, -2), (-2, -2, -1), (-2, -2, 0)), (2, 1, 2), (-3, -1, -1))` |
| `(1, 0, 1, 0, 1, 1)` | `(((-2, -2, -2), (-2, -2, -1), (-2, -2, 0)), (2, 1, 2), (-3, -3, -1))` |
| `(1, 0, 1, 1, 0, 1)` | `(((-2, -2, -2), (-2, -2, -1), (-2, 0, -2)), (1, 1, 2), (-3, -1, -1))` |
| `(1, 0, 1, 1, 1, 0)` | `(((-2, -2, -2), (-2, -2, -1), (-2, 0, -2)), (1, 2, 1), (-3, -1, -2))` |
| `(1, 1, 0, 1, 0, 1)` | `(((-2, -2, -2), (-2, -2, -1), (0, -2, -2)), (1, 1, 2), (-1, -1, -1))` |
| `(1, 1, 0, 1, 1, 0)` | `(((-2, -2, -2), (-2, -2, -1), (0, -2, -2)), (1, 2, 1), (-1, -1, -2))` |
| `(1, 1, 1, 0, 0, 1)` | `(((-2, -2, -2), (-2, -2, -1), (0, -2, -2)), (1, 1, 2), (-1, -3, -1))` |
| `(1, 1, 1, 0, 1, 0)` | `(((-2, -2, -2), (-2, -2, -1), (0, -2, -2)), (1, 2, 1), (-1, -3, -2))` |

No mask is unrealized. The first weight-4 star of the box is itself a
perpendicular mask: `σ = (1, 0, 1, 0, 1, 1)` at
`((-2, -2, -2), (-2, -2, -1), (-2, -2, 0)), (2, 1, 2), (-3, -3, -1)`.

## Theorem 3 — displayed, not adopted

The count `N_real = 12`, the prefix counts, and the twelve lex-first
hosts are displayed member data. They are not the framework's fixed
Admissibility rule. This note does not write a host into Admissibility.
Do not write a host into Admissibility. Do not attach L1. Occupancy-only
formation is not attached. Qubit remains `M_2(C)`. No approved primitive
is added. No axiom edit.

## Honest-auditor / Boundary

- **What is proved.** On the 12 perpendicular weight-4 occupancy masks,
  `N_real = 12`. Each mask has a lex-first uneqrad host. The 2000-star
  prefix already contains all 12, so `N_prefix = 2000` and
  `N_prefix_real = 12`.
- **What is displayed only.** The twelve hosts and the two prefix counts
  are one rival table. They are not adopted.
- **What is not claimed.** No attachment of a realizing union to
  Admissibility; no attachment of occupancy-only formation; no axiom
  edit; no formation rate; no lattice-wide dynamics; no leftover of
  uneqrad (one mask); no leftover of bitname or bitfire; no compiler
  no-go.
- **Mutation controls.** A rebuilt `N_real` other than 12 fails. A
  rebuilt empty host on any of the 12 masks fails. A rebuilt prefix
  with `N_prefix_real` other than 12 fails. A note that writes a host
  into Admissibility, attaches L1, or authors an audit verdict fails.

This note authors no audit verdict.

## Primary Runner

The primary runner rebuilds the 12 perpendicular weight-4 occupancy
masks, the uneqrad 3-ball box, the 2000-star prefix, `N_real`, the
lex-first host of each mask, the current premise boundary, and the
mutation controls. It scores a prefix plus existence per mask. It
writes no cache and authors no audit verdict.
