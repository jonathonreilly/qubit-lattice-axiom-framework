---
claim_id: unequal_radius_tick_not_l1_neighbor_datum_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On the lex-first unequal-radius breaker, whether displayed L1 neighbor data equals the lock-tick 4-tuple is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/unequal_radius_tick_not_l1_neighbor_datum_2026_08_15.py
---

# Unequal-Radius Lock-Tick Is Not A Displayed L1 Neighbor Datum (Bounded Theorem)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** the uneqrad lex-first unequal-radius breaker
`U = B_2((−2,−2,−2)) ∪ B_1((−2,−2,−1)) ∪ B_3((−2,−2,1))` at
`v = (−3,−3,−1)`. Occupied slots carry
`t = (1, 1, 3, 2)` on `(+x, +y, +z, −z)`. Whether any displayed L1
neighbor datum on those four sites equals that 4-tuple is reported.
Displayed, not adopted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/unequal_radius_tick_not_l1_neighbor_datum_2026_08_15.py`](../scripts/unequal_radius_tick_not_l1_neighbor_datum_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md).

## Result Up Front

Investment uneqrec: `M_2` Record does not supply `t`. That residual is one
common `M_2` lock on every occupied neighbor. The residual here is not
leftover of uneqrec (one `M_2` lock). New residual: on this star, none of
the displayed L1 neighbor data — `n`, Bloch from occupancy, `k`,
formation-count of the union — equals the 4-tuple `t`. That names the
extra as not a theorem of displayed L1.

`U`, `v`, and `t` are the uneqrad lex-first breaker. Occupancy `σ` is the
6-bit nearest-neighbor indicator of `U` at `v`. The four occupied
neighbors are `+x`, `+y`, `+z`, and `−z`. Comparators are the displayed
L1 lists at those four sites only.

**Theorem 1.** `t` is not equal to any of those four-site L1 lists.

**Theorem 2.** Therefore `t` is not a theorem of displayed L1 on this
star.

**Theorem 3.** Displayed, not adopted. Do not write `t` into L1 or
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

The full one-site possibility domain has algebraic presentation `M_2(C)`.

When present, a record locks exactly one admissible local possibility.

Only records are readable. A readout value is determined by record content
alone.

A site with no record cannot be read.

Admissibility names neither lock-ticks nor any displayed L1 neighbor list
as a supplier of `t`. Lattice names cubic sites and six-neighbor
adjacency; it does not name the 4-tuple `t`. Record locks one admissible
local possibility in `M_2(C)` and supplies no integer formation-count of
a union. Qubit remains `M_2(C)`. No axiom edit.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "On the uneqrad lex-first star the occupied lock-tick 4-tuple equals none of the displayed four-site L1 lists (occupancy bits, n from each neighbor six-star, Bloch from occupancy, k, formation-count of U). So t is not a theorem of displayed L1 on this star. Displayed, not adopted."
trace_class: negative_route_pruning
target_claim_id: unequal_radius_tick_not_l1_neighbor_datum
target_blocker_text: "whether displayed L1 neighbor data equals the lock-tick 4-tuple on the lex-first unequal-radius breaker"
source_of_blocker_text: handoff
reachability_to_target: prunes
artifact_role: theorem
next_trace_action: "independent audit of the four-site list comparison on this star; do not write t into L1 or Admissibility or attach L1"
conditional_surface_status: "exact on the uneqrad lex-first 6-star; t equals none of the displayed L1 lists; displayed, not adopted"
hypothetical_axiom_status: "not proposed; no axiom or approved primitive is added"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

Write `B_r(c) = { x ∈ Z^3 : ‖x − c‖_1 ≤ r }`. The host is the uneqrad
lex-first breaker

`U = B_2((−2,−2,−2)) ∪ B_1((−2,−2,−1)) ∪ B_3((−2,−2,1))`,
radii `(2, 1, 3)`,
`v = (−3,−3,−1)`.

Slots are the six directions

`(+x, −x, +y, −y, +z, −z)`.

A neighbor `w = v + e` is occupied when `w ∈ U`. Occupancy and ticks are

`σ = (1, 0, 1, 0, 1, 1)`,
`t = (1, ·, 1, ·, 3, 2)`.

So `v ∉ U` and the four occupied neighbors carry mixed clocks `{1, 1, 3, 2}`.
The occupied 4-tuple, in slot order `(+x, +y, +z, −z)`, is

`t_occ = (1, 1, 3, 2)`.

The four occupied sites are

`w_{+x} = (−2, −3, −1)`,
`w_{+y} = (−3, −2, −1)`,
`w_{+z} = (−3, −3, 0)`,
`w_{−z} = (−3, −3, −2)`.

Displayed L1 comparators at those four neighbors:

- occupancy bits (all 1): `σ_occ = (1, 1, 1, 1)`;
- `n_μ` from the six-star of each neighbor if defined, with dipole
  `d_μ(w) = occ(w + e_μ) − occ(w − e_μ)` and `n(w) = d(w)/3` when
  defined from that six-star:
  `n_occ = ((0, 1/3, 0), (1/3, 0, 0), (1/3, 1/3, 1/3), (1/3, 1/3, 0))`;
- Bloch `I_2/2` (Bloch vector `(0, 0, 0)` at each occupied site) or the
  occupancy map `(1, 1, 1, 1)`;
- `k(w)` the occupied-NN count of the six-star at `w`:
  `k_occ = (3, 3, 3, 2)`;
- Formation-count of `U` is one integer `|U| = 81`, not a 4-tuple.

These lists are occupancy geometry of `U` on the six-neighbor graph.
They are not Record content and not an Admissibility rule.

## Theorem 1 — `t` is not equal to any of those four-site L1 lists

Direct comparison on this star:

`t_occ = (1, 1, 3, 2)`,

`σ_occ = (1, 1, 1, 1) ≠ t_occ`,

`n_occ` is a 4-tuple of 3-vectors, not the integer 4-tuple `t_occ`,

Bloch `I_2/2` is four copies of `(0, 0, 0)`, not `t_occ`,

the occupancy map is `(1, 1, 1, 1) ≠ t_occ`,

`k_occ = (3, 3, 3, 2) ≠ t_occ`,

and the formation-count of the union is the single integer `81`, not a
4-tuple.

So `t` is not equal to any of those four-site L1 lists.

## Theorem 2 — `t` is not a theorem of displayed L1 on this star

The displayed L1 menu on this star is occupancy bits, `n` from each
neighbor six-star, Bloch from occupancy, `k`, and the formation-count of
`U`. Theorem 1 says none of those objects equals `t_occ`. Therefore `t`
is not a theorem of displayed L1 on this star.

This is not leftover of uneqrec (one `M_2` lock). uneqrec showed that the
same `M_2` projector on every occupied neighbor cannot send one Bloch
vector to both `1` and `3`. The present comparison does not use that
lock. It uses only the named L1 neighbor lists.

## Theorem 3 — displayed, not adopted

The four-site comparison is displayed star data. It is not the
framework's fixed Lattice, Record, or Admissibility content.
Displayed, not adopted. Do not write `t` into L1 or Admissibility.
Do not attach L1. Occupancy-only formation is not attached. Qubit remains
`M_2(C)`. No approved primitive is added. No axiom edit.

## Honest-auditor / Boundary

- **What is proved.** On the uneqrad lex-first unequal-radius breaker,
  the occupied lock-tick 4-tuple equals none of the displayed four-site
  L1 lists. Therefore `t` is not a theorem of displayed L1 on this star.
- **What is displayed only.** The lists `σ_occ`, `n_occ`, Bloch from
  occupancy, `k_occ`, and `|U|` are one rival table. They are not
  adopted.
- **What is not claimed.** No writing of `t` into L1 or Admissibility;
  no attachment of L1; no axiom edit; no formation rate; no lattice-wide
  dynamics; no leftover of uneqrec (one `M_2` lock); no compiler no-go.
- **Mutation controls.** A rebuilt `t_occ` other than `(1, 1, 3, 2)`
  fails. A rebuilt list among occupancy, `n`, Bloch, `k`, or
  formation-count that equals `t_occ` fails. A note that writes `t` into
  L1 or Admissibility, attaches L1, or authors an audit verdict fails.

This note authors no audit verdict.

## Primary Runner

The primary runner rebuilds the uneqrad lex-first host, the occupancy,
the lock-ticks, the four-site L1 lists, the current premise boundary,
and the mutation controls. It writes no cache and authors no audit
verdict. It scores the uneqrad star only.
