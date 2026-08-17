---
claim_id: support_drop_mixed_shells_b12_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Mixed t=const shells under the named support-drop hop-cost on B_12(0) are named. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/support_drop_mixed_shells_b12_2026_08_15.py
---

# Mixed t=const Shells Of The Named Support-Drop Hop-Cost On B_12(0)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** one named nearest-neighbor hop-cost on the ℓ¹ ball `B_12(0)`,
scored only for which arrival values mix more than one Euclidean squared
radius and for whether the reverse-critical body diagonal sits among them.
**Audit-status authority:** independent audit lane only. This note authors
no audit verdict and predicts none.
**Primary runner:**
[`scripts/support_drop_mixed_shells_b12_2026_08_15.py`](../scripts/support_drop_mixed_shells_b12_2026_08_15.py)
**Cache:** none. `cache_write: false`.

## Result Up Front

The same named support-drop hop-cost `ν` already scored on `B_8(0)` is
scored independently on `B_12(0)`. Mixed `t=const` shells are not leftover
of the radius-`8` mixed list: that list is six arrival values
`5,6,7,8,9,10`, while `B_12(0)` adds four further mixed arrivals
`11,12,13,14`. The site `(4,4,4)` is not in `B_8(0)` at all.

Write `|σ_v|` for the number of nonzero coordinates of `v ∈ Z^3`. On a
directed nearest-neighbor hop `v → w` still inside `B_12(0)`, the displayed
rule `ν` is

`ν(v→w) = 3` if `|σ_v|=0` or `(|σ_v|=|σ_w|=1)` or `|σ_w| < |σ_v|`,
else `1`.

The first clause is seed-exit. The second is both weights `1`. The third is
support drop. Those three clauses are the whole rule. Uniqueness is not claimed.

One Dijkstra from the origin on `B_12(0)` (2625 sites; 2624 nonzero) names
exactly ten mixed arrival values on `B_12(0) \ {0}`:

| `t` | distinct `|v|_2^2` | site count |
|---:|---:|---:|
| `5` | `2` | `32` |
| `6` | `4` | `66` |
| `7` | `4` | `96` |
| `8` | `5` | `140` |
| `9` | `8` | `198` |
| `10` | `10` | `258` |
| `11` | `10` | `326` |
| `12` | `13` | `402` |
| `13` | `15` | `486` |
| `14` | `15` | `578` |

The reverse-critical body diagonal `(2,2,2)` arrives at `t=8`, which is
mixed. The doubled body diagonal `(4,4,4)` arrives at `t=14`, which is
mixed. Both sit in mixed shells.

The census is displayed, not adopted. Do not write `ν` into Admissibility.
Do not attach L1.

## Current Premise Boundary

The Lattice and Admissibility premises are quoted from
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md):

Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
adjacency, standard translations, and proper cubic rotations about each site.

There is one fixed nearest-neighbor admissibility rule, covariant under lattice
translations and proper cubic rotations.

For each site, the probability distribution over the possibilities is
determined by, and varies with, the nearest-neighbor conditions.

Lattice supplies the six-neighbor graph and the ball. Admissibility supplies
none of the hop costs. The integers `3` and `1`, the support-size clauses,
and the arrival function `t` are separately displayed mathematical inputs.
No axiom text is edited.

## Named Rule

Let `B_12(0) = { v ∈ Z^3 : |v|_1 ≤ 12 }`. Directed edges are the six
nearest-neighbor steps whose both ends lie in the ball. For `v ∈ B_12(0)`,
`t(v)` is the least sum of `ν` along a directed path from `0` to `v` in
that graph.

A `t=const` shell is mixed when the sites of that arrival carry more than
one value of `|v|_2^2`. The six mixed arrivals on `B_8(0)` remain mixed
here with the same site counts. The four new mixed arrivals exist only
because sites with `|v|_1 > 8` are present; on `B_8(0)` the values
`t=11,12,13` are single-radius six-site shells and `t=14` does not occur.

## Theorem 1 — Mixed Arrival Values

One origin Dijkstra on `B_12(0)` returns sixteen positive arrival values.
The ten listed in the opening table are exactly those whose shells contain
more than one `|v|_2^2`. The remaining six arrivals `3,4,15,16,17,20` are
single-radius.

The first six mixed rows copy the `B_8(0)` mixed list. The last four rows
are new. In particular `t=11` now mixes ten squared radii across 326
sites, and `t=14` mixes fifteen squared radii across 578 sites. The
`B_12(0)` mixed list is therefore not leftover of the `B_8(0)` mixed list.

## Theorem 2 — Body Diagonals Sit In Mixed Shells

The same Dijkstra gives `t(2,2,2) = 8` and `t(4,4,4) = 14`. Both values
appear in the mixed list of Theorem 1.

The `t=8` shell has five squared radii `{12,14,18,20,26}` and 140 sites.
The reverse-critical body diagonal `(2,2,2)` contributes the radius `12`
orbit of size `8`; it shares the shell with `(3,2,1)`, `(3,3,0)`,
`(4,1,1)`, `(4,2,0)`, and `(5,1,0)` (and their cubic images). So the
reverse-critical body diagonal sits in a mixed shell.

The `t=14` shell has fifteen squared radii and 578 sites. The doubled body
diagonal `(4,4,4)` contributes the radius `48` orbit of size `8`; it shares
the shell with, among others, `(8,0,0)` at radius `64`. So `(4,4,4)` also
sits in a mixed shell.

Both facts are displayed, not adopted.

## Theorem 3 — Displayed, Not Adopted

The rule `ν` is a displayed scoring device on `B_12(0)`. Do not write `ν`
into Admissibility. Do not attach L1. The mixed-shell census is not offered
as a unique hop-cost property and is not a replacement for unit-cost first
arrival.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact mixed t=const census on the finite ball B_12(0) for one named hop-cost. The rule is displayed, not adopted."
trace_class: frontier_discovery
artifact_role: theorem
conditional_surface_status: "exact on B_12(0) for the displayed rule ν; no Admissibility edit; not attached to L1"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## What This Note Does Not Claim

- Uniqueness of `ν` among hop-costs with mixed `t=const` shells.
- Any edit of Lattice, Qubit, Admissibility, or Record.
- Any attachment to L1.
- Any continuum potential, any inverse-power kernel, and any gravitational
  identification.
- Any statement off `B_12(0)`.
- Any reuse of the `B_8(0)` mixed list as a substitute for the radius-`12`
  Dijkstra.
