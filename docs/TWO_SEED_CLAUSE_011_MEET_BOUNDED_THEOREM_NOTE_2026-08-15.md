---
claim_id: two_seed_clause_011_meet_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Two-seed meetings under the named (0,1,1) hop-cost are scored vs ℓ¹. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/two_seed_clause_011_meet_2026_08_15.py
---

# Two-Seed Meetings Under The Named `(0,1,1)` Hop-Cost

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** two seeds `s0=(0,0,0)` and `s1=(2,0,0)` on the union
`B_4(0) ∪ B_4((2,0,0))`, with fronts grown by the named clause-toggle
`(0,1,1)` using inward weights relative to the seed being grown.
First-meeting sites and the equal-arrival midplane are scored against
unit-cost ℓ¹. Displayed, not adopted.
**Audit-status authority:** independent audit lane only. This note authors
no audit verdict and predicts none.
**Primary runner:**
[`scripts/two_seed_clause_011_meet_2026_08_15.py`](../scripts/two_seed_clause_011_meet_2026_08_15.py)
**Cache:** none. `cache_write: false`.

## Result Up Front

The named support-drop rule `ν = (1,1,1)` has a unique two-seed first
meeting at `(1,0,0)` at time `t=3`. The other named diamond reverser is
the clause-toggle `(0,1,1)`. The residual here is the same two seeds
and the same union: grow a front from each seed by `(0,1,1)`, with
support measured from the seed being grown, and ask whether the first
meeting stays a matching-member front. Uniqueness among hop-costs is
not required.

Write `|σ_s(v)|` for the number of nonzero coordinates of `v-s`. That
integer is the inward weight of `v` relative to the seed `s` being
grown. On a directed nearest-neighbor hop `v → w` still inside the
union, the displayed rule relative to `s` is

`(0,1,1)_s(v→w) = 3` if `(|σ_s(v)|=|σ_s(w)|=1)` or
`|σ_s(w)| < |σ_s(v)|`, else `1`.

The first clause is both inward weights `1`. The second is support
drop. Seed-exit (`|σ_s(v)|=0`) is off, so it costs `1`. Those are the
whole rule.

Let `t0` and `t1` be the least path costs from `s0` and `s1` under
`(0,1,1)` relative to that seed. One pair of Dijkstras on the 195-site
union gives a first-meeting set

`M = { v : t0(v)=t1(v)` and no neighbor is strictly earlier for both `}`.

The lex-first meeting site is `(1,0,0)` at time `t=1`, and `|M|=1`.
The first meeting therefore stays the matching-member front
`{(1,0,0)}`. The cheap seed-exit is what drops the meeting time from
the `ν` value `3` to `1`.

The equal-arrival midplane is `{ v : t0(v)=t1(v) }`. Population
variances of `|v-s0|_2/t0` on each law's own midplane are

`var_(0,1,1) = 0.01142337008814`, `var_ℓ¹ = 0.00995038158264`.

The ℓ¹ variance is strictly smaller. The midplane under `(0,1,1)` has
33 sites; the midplane under ℓ¹ has 25 sites.

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
`(0,1,1)` relative to the seed it grows. Unit-cost ℓ¹ arrival is the
closed form `t_ℓ¹_s(v) = |v-s|_1`; it is not obtained from a third
Dijkstra.

A neighbor `w` of `v` is strictly earlier for both if `t0(w)<t0(v)` and
`t1(w)<t1(v)`. First-meeting sites are the equal-arrival sites with no
such neighbor.

The eight sites

`(0,±2,0)`, `(0,0,±2)`, `(2,±2,0)`, `(2,0,±2)`

lie on the `(0,1,1)` midplane and not on the ℓ¹ midplane `x=1`.

## Theorem 1 — Lex-First Meeting Site

One pair of Dijkstras returns integer arrivals with first-meeting set
`M = { (1,0,0) }`. The lex-first meeting site and its time are

`(1,0,0)` at `t0=t1=1`.

So `|M|=1`. The first meeting stays a matching-member front. Under
unit-cost ℓ¹ the same meeting definition also yields the singleton
`{(1,0,0)}`, at time `1`. Uniqueness is not claimed among hop-costs.

## Theorem 2 — Midplane Variance Of `|v-s0|_2/t0`

On the equal-arrival midplane of each law, let `r(v) = |v-s0|_2 / t0(v)`
and write population variance `(1/n) ∑ (r − mean)^2`. The runner computes

`var_(0,1,1) = 0.01142337008814` on 33 sites,
`var_ℓ¹ = 0.00995038158264` on 25 sites.

So `var_ℓ¹ < var_(0,1,1)`. The cheaper reverser does not tighten the
two-seed midplane ratio below ℓ¹.

## Theorem 3 — Displayed, Not Adopted

The rule `(0,1,1)` is a displayed scoring device on the two-seed union.
It is not written into Admissibility. It is not attached to L1. It is
not a replacement for unit-cost first arrival, and it is not offered as
the unique hop-cost with a two-seed matching-member front.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact integer two-seed arrivals and a midplane population-variance comparison on B_4(0)∪B_4((2,0,0)) for the named (0,1,1) hop-cost. The rule is displayed, not adopted."
trace_class: frontier_discovery
artifact_role: theorem
conditional_surface_status: "exact on the two-seed union for the displayed rule (0,1,1); no Admissibility edit; not attached to L1"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## What This Note Does Not Claim

- Uniqueness of `(0,1,1)` among hop-costs with a matching-member first
  meeting.
- That `(0,1,1)` beats ℓ¹ on two-seed midplane variance.
- Any edit of Lattice, Qubit, Admissibility, or Record.
- Any attachment to L1.
- Any continuum potential, any inverse-power kernel, and any gravitational
  identification.
- Any statement off the union `B_4(0) ∪ B_4((2,0,0))`.
