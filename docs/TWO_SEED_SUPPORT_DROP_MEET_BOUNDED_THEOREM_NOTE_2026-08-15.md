---
claim_id: two_seed_support_drop_meet_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Two-seed meetings under the named support-drop hop-cost are scored vs ℓ¹. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/two_seed_support_drop_meet_2026_08_15.py
---

# Two-Seed Meetings Under The Named Support-Drop Hop-Cost

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** two seeds `s0=(0,0,0)` and `s1=(2,0,0)` on the union
`B_4(0) ∪ B_4((2,0,0))`, with fronts grown by the named support-drop
hop-cost `ν` using inward weights relative to the seed being grown.
First-meeting sites and the equal-arrival midplane are scored against
unit-cost ℓ¹. Displayed, not adopted.
**Audit-status authority:** independent audit lane only. This note authors
no audit verdict and predicts none.
**Primary runner:**
[`scripts/two_seed_support_drop_meet_2026_08_15.py`](../scripts/two_seed_support_drop_meet_2026_08_15.py)
**Cache:** none. `cache_write: false`.

## Result Up Front

The one-seed support-drop rule `ν` reversed the diamond and beat ℓ¹
variance on a single ball. The residual here is two-seed: grow a front
from each seed by the same named rule, with support measured from the
seed being grown, and ask whether first-meeting sites sit closer to a
common ratio `|x-s|_2/t` than under ℓ¹.

Write `|σ_s(v)|` for the number of nonzero coordinates of `v-s`. On a
directed nearest-neighbor hop `v → w` still inside the union, the
displayed rule relative to the seed `s` being grown is

`ν_s(v→w) = 3` if `|σ_s(v)|=0` or `(|σ_s(v)|=|σ_s(w)|=1)` or
`|σ_s(w)| < |σ_s(v)|`, else `1`.

The first clause is seed-exit. The second is both inward weights `1`.
The third is support drop. Those three clauses are the whole rule.

Let `t0` and `t1` be the least path costs from `s0` and `s1` under `ν`
relative to that seed. One pair of Dijkstras on the 195-site union
gives a first-meeting set

`M = { v : t0(v)=t1(v)` and no neighbor is strictly earlier for both `}`.

The lex-first meeting site is `(1,0,0)` at time `t=3`, and `|M|=1`.

The equal-arrival midplane is `{ v : t0(v)=t1(v) }`. Population
variances of `|v-s0|_2/t0` on each law's own midplane are

`var_ν = 0.00405294265643`, `var_ℓ¹ = 0.00995038158264`.

The `ν` variance is strictly smaller. The midplane under `ν` has 33
sites; the midplane under ℓ¹ has 25 sites. The comparison is two-seed:
it uses both arrivals, so it is not a leftover of one-seed variance on
a single ball.

The rule is displayed, not adopted. It is not written into Admissibility.
It is not attached to L1.

## Current Premise Boundary

The Lattice and Admissibility premises are quoted from
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md):

Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
adjacency, standard translations, and proper cubic rotations about each site.

There is one fixed nearest-neighbor admissibility rule, covariant under lattice
translations and proper cubic rotations.

Lattice supplies the six-neighbor graph and the two balls. Admissibility
supplies none of the hop costs. The integers `3` and `1`, the seed-relative
support-size clauses, and the two arrival functions are separately
displayed mathematical inputs. No axiom text is edited.

## Named Rule And Domain

Let `B_4(s) = { v ∈ Z^3 : |v-s|_1 ≤ 4 }`. The host is the union
`B_4(0) ∪ B_4((2,0,0))`, which has 195 sites. Directed edges are the
six nearest-neighbor steps whose both ends lie in the union.

For the seed `s0`, inward weight is `|σ_{s0}(v)|`. For the seed `s1`,
inward weight is `|σ_{s1}(v)|`. Each Dijkstra uses only the copy of
`ν` relative to the seed it grows. Unit-cost ℓ¹ arrival is the closed
form `t_ℓ¹_s(v) = |v-s|_1`; it is not obtained from a third Dijkstra.

A neighbor `w` of `v` is strictly earlier for both if `t0(w)<t0(v)` and
`t1(w)<t1(v)`. First-meeting sites are the equal-arrival sites with no
such neighbor.

The eight sites

`(0,±2,0)`, `(0,0,±2)`, `(2,±2,0)`, `(2,0,±2)`

lie on the `ν` midplane and not on the ℓ¹ midplane `x=1`. Equal arrival
under `ν` is therefore not the one-seed leftover of the geometric
midplane of ℓ¹, and it is not the one-seed leftover of a single-ball
`|v|_2/t` census.

## Theorem 1 — Lex-First Meeting Site

One pair of Dijkstras returns integer arrivals with first-meeting set
`M = { (1,0,0) }`. The lex-first meeting site and its time are

`(1,0,0)` at `t0=t1=3`.

So `|M|=1`. Under unit-cost ℓ¹ the same meeting definition also yields
the singleton `{(1,0,0)}`, at time `1`.

## Theorem 2 — Midplane Variance Of `|v-s0|_2/t0`

On the equal-arrival midplane of each law, let `r(v) = |v-s0|_2 / t0(v)`
and write population variance `(1/n) ∑ (r − mean)^2`. The runner computes

`var_ν = 0.00405294265643` on 33 sites,
`var_ℓ¹ = 0.00995038158264` on 25 sites.

So `var_ν < var_ℓ¹`. First-meeting and later equal-arrival sites under
`ν` lie closer to a common ratio than the ℓ¹ midplane does. Uniqueness is not claimed.

## Theorem 3 — Displayed, Not Adopted

The rule `ν` is a displayed scoring device on the two-seed union. It is
not written into Admissibility. It is not attached to L1. It is not a
replacement for unit-cost first arrival, and it is not offered as the
unique hop-cost with a tighter two-seed midplane ratio.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact integer two-seed arrivals and a midplane population-variance comparison on B_4(0)∪B_4((2,0,0)) for one named hop-cost. The rule is displayed, not adopted."
trace_class: frontier_discovery
artifact_role: theorem
conditional_surface_status: "exact on the two-seed union for the displayed rule ν; no Admissibility edit; not attached to L1"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## What This Note Does Not Claim

- Uniqueness of `ν` among hop-costs that tighten two-seed midplane
  variance below ℓ¹.
- Any edit of Lattice, Qubit, Admissibility, or Record.
- Any attachment to L1.
- Any continuum potential, any inverse-power kernel, and any gravitational
  identification.
- Any statement off the union `B_4(0) ∪ B_4((2,0,0))`.
- That the midplane comparison is a leftover of one-seed variance.
