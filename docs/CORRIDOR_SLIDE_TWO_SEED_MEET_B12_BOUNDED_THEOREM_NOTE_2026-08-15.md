---
claim_id: corridor_slide_two_seed_meet_b12_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Two-seed meeting-set arrival-speed variance under the named corridor-slide hop-cost on B_12(0)∪B_12((2,0,0)) is compared to ℓ¹. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/corridor_slide_two_seed_meet_b12_2026_08_15.py
---

# Two-Seed Meeting-Set Variance Under Corridor-Slide On The B_12 Union

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** the named corridor-slide hop-cost `μ`, grown from each of two
seeds on the finite union `B_12(0)∪B_12((2,0,0))`, the first-meeting set of
the two arrival fields, and the population variance of `|v-s0|_2/t0` on
that set versus the unit-cost comparison. No hop-cost is written into
Admissibility. L1 is not attached.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/corridor_slide_two_seed_meet_b12_2026_08_15.py`](../scripts/corridor_slide_two_seed_meet_b12_2026_08_15.py)
**Cache:** none. `cache_write: false`.

## Result Up Front

The named corridor-slide hop-cost `μ` is the already scored support-drop
rule `ν` plus cost `3` on a `2→2` hop whose destination has least nonzero
absolute coordinate equal to `1` (an axis-hugging face slide). On one seed,
`μ` is the rounder same-`k` reverser among the previously displayed scores.
The radius-`6` two-seed meeting set on the same seeds is a singleton with
both arrival-speed variances `0`. The residual here is whether `|M|>1` on
the union of radius-`12` balls about `(0,0,0)` and `(2,0,0)`, and whether
`μ` then beats `ℓ¹` on that meeting set. Uniqueness is not claimed.
Uniqueness not required.

Two Dijkstras, one from each seed, with hop-costs grown from each seed,
produce identical first-meeting data for `μ`:

lex-first meeting site `(1,0,0)`, arrival `t=3`, `|M|=1`.

So `|M|>1` is false. The unit-cost comparison `ℓ¹` has the same first-meeting
site `(1,0,0)` at `t=1`, again with `|M|=1`. On a singleton meeting set the
arrival-speed variance is exactly `0` under both scores. The two displayed
variances therefore tie. Ordered by the names `l1` then `mu`, the lex-first
minimizer is `ℓ¹`. The scores are displayed, not adopted. Do not write `μ`
into Admissibility. Do not attach L1.

The `μ` meeting time `3` is not a leftover of the unit-cost time `1`. The
site `(12,0,0)` lies in this union and is absent from the radius-`6` union,
so the table is not leftover of the smaller-ball singleton.

## Current Premise Boundary

The Lattice and Admissibility premises are quoted from
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md):

Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
adjacency, standard translations, and proper cubic rotations about each site.

There is one fixed nearest-neighbor admissibility rule, covariant under lattice
translations and proper cubic rotations.

For each site, the probability distribution over the possibilities is
determined by, and varies with, the nearest-neighbor conditions.

The axiom does not supply hop-cost values. It does not
supply the formation site, probability, or rate.

The current Record boundary is:

When present, a record locks exactly one admissible local possibility.

A readout value is determined by record content alone.

A site with no record cannot be read.

None of Record is used to select a hop-cost.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Two finite seed-relative Dijkstras and the first-meeting-set arrival-speed variances on B_12(0)∪B_12((2,0,0)) are exact; no hop-cost is adopted and L1 is not attached."
trace_class: frontier_discovery
target_claim_id: corridor_slide_two_seed_meet_b12
target_blocker_text: "compare two-seed meeting-set arrival-speed variance of μ versus ℓ¹ on B_12(0)∪B_12((2,0,0))"
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Keep the meeting-set scores displayed. Do not write μ into Admissibility. Do not attach L1."
conditional_surface_status: "exact for the named hop-cost and the unit-cost comparison on the induced union graph; no physical law is selected"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

Write `s0=(0,0,0)` and `s1=(2,0,0)`. The executed domain is the union

`B_12(0)∪B_12((2,0,0)) = { v ∈ Z^3 : |v|_1 ≤ 12 or |v-s1|_1 ≤ 12 }`.

This set has 3203 sites. Each separate ball has 2625 sites. The executed graph
is the induced nearest-neighbor graph on the union: a directed hop `v→w`
exists when `w-v` is a signed axis unit and `w` lies in the union.

The coordinate support is `σ_v={i : v_i ≠ 0}`. Its cardinality is the
weight. On a hop `v→w` measured from the seed being grown:

- seed-exit means `|σ_v|=0`,
- both-weights-1 means `|σ_v|=|σ_w|=1`,
- support-drop means `|σ_w| < |σ_v|`,
- corridor-slide means `|σ_v|=|σ_w|=2` and the least nonzero `|w_i|` equals `1`.

The named cost `μ`, grown from seed `s`, prices the hop `v→w` by the
already scored one-seed rule on the translated points `v-s` and `w-s`:

`μ_s(v→w) = 3` if `|σ_{v-s}|=0` or `(|σ_{v-s}|=|σ_{w-s}|=1)` or
`|σ_{w-s}| < |σ_{v-s}|` or `(|σ_{v-s}|=|σ_{w-s}|=2` and the least nonzero
`|(w-s)_i|` equals `1)`, else `1`.

The unit-cost comparison `ℓ¹` prices every executed hop at `1`. Its arrivals
are the taxicab norms from each seed; no third or fourth Dijkstra is run.

Arrival times `t0` and `t1` are the least path costs from `s0` and `s1`
under the named rule. The meeting set is

`M = { v : t0(v)=t1(v) and no neighbor w is strictly earlier for both }`,

where "strictly earlier for both" means `t0(w)<t0(v)` and `t1(w)<t1(v)`.
Uniqueness of a meeting site is not required.

The compared statistic on `M` is the population variance of `|v-s0|_2/t0`.
On a singleton this variance is `0`. Equivalently the second moment
`Q = |v-s0|_2^2 / t0^2` is reported. This note does not attach L1.

## Theorem 1 — Lex-First Meeting Site, Arrival, And `|M|`

Every union site is reached from both seeds under `μ`. The equal-arrival
set has `713` sites under `μ` and `265` sites under `ℓ¹`, but every
equal-arrival site other than `(1,0,0)` has a neighbor strictly earlier
for both clocks. Therefore

`M_μ = {(1,0,0)}`,

the lex-first meeting site is `(1,0,0)`, its arrival is `t=3`, and
`|M|=1`.

A witness walk of cost `3` from `s0` is the seed-exit hop
`(0,0,0) → (1,0,0)`. A witness walk of cost `3` from `s1` is the
seed-exit hop `(2,0,0) → (1,0,0)`. Those walks are witnesses, not a
uniqueness claim among paths.

Under `ℓ¹` the same definition yields `M_ℓ¹ = {(1,0,0)}` at `t=1`. The
midplane `|x|=|x-2|` is the plane `x=1`, and every other site of that
plane has a neighbor strictly earlier for both taxicab clocks.

## Theorem 2 — Meeting-Set Arrival-Speed Variance

Because `|M|=1`, both displayed population variances are `0`. No
`|M|≥2` comparison of `var(|v-s0|_2/t0)` is available on this union.

On `M_μ` the single speed is `|s0-offset|_2 / 3 = 1/3`, so the second
moment is `1/9` and the population variance is `0`.

On `M_ℓ¹` the single speed is `1/1 = 1`, so the second moment is
`1` and the population variance is `0`.

Both meeting-set variances are therefore `0`. The score `μ` does not beat
`ℓ¹` on `M`. The lex-first minimizer among the names `l1` and `mu` is
`ℓ¹`. The comparison is displayed, not adopted.

The pair is not a leftover of one-seed variance: the first-meeting front
under the stated neighbor test is a singleton for both named costs, so the
rounder-reverser distinction on a one-seed ball does not survive as a
variance gap on this two-seed meeting set. Enlarging the union from radius
`6` to radius `12` grows the equal-arrival set to `713` sites under `μ`
and does not enlarge `M`.

## Theorem 3 — No Admissibility Write, L1 Not Attached

Do not write `μ` into Admissibility. The current admissibility rule remains
the quoted nearest-neighbor distribution constraint. The corridor-slide
clauses and the unit-cost comparison are scoring rules on the finite union,
not a replacement of that axiom.

Do not attach L1. No formation law, occupancy member, or locked-set filling
rule is identified with either hop-cost.

## Promotion Value Gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers whether two-seed meeting-set variance under μ beats ℓ¹ on the B_12 union. |
| V2 | Current main has no landed two-seed meeting-set variance for corridor-slide on B_12. |
| V3 | The two Dijkstras, the meeting set, and the singleton variances are finite and exact. |
| V4 | The comparison is not an axiom rewrite: Admissibility is left unchanged. |
| V5 | Displayed scores are not a physical hop-cost or formation law. |

## No-Go Discipline Gate

The negative content is narrow: these two meeting-set scores are compared
on the stated union and are not adopted. No uniqueness of a physical law
is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| `μ` | seed-relative corridor-slide | executed; `|M|=1`, `var=0`, `t=3` |
| `ℓ¹` | unit hop-cost | executed; `|M|=1`, `var=0`, `t=1`; lex-first name |
| other meeting tests | keep the whole equal-arrival midplane | different residual; not this `M` |
| unrestricted `Z^3` paths | leave the union and return | outside the declared domain |
| adopt a score | write `μ` into Admissibility | forbidden; not executed |
| attach L1 | identify a score with a formation member | forbidden; not executed |

### N2 — wall independence

Union restriction, seed-relative hop-cost, the first-meeting test, the
speed statistic, and axiom non-adoption are distinct. This note claims no
complete wall collection.

### N3 — hidden-condition scan

The union, the induced graph, seed-relative `μ`, the neighbor test for
`M`, population variance, and lex-first among the two names are declared.
No continuum limit, no physical clock, and no formation rate are assumed.

### N4 — source residual matching

The axiom memo supplies the cubic nearest-neighbor substrate and the
distribution sentence. It does not name hop-cost clauses. The residual is
a finite comparison on that substrate, not an axiom edit.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | each of the 3203 union sites | no other union |
| per site | two arrivals under `μ`, taxicab under `ℓ¹` | no physical tick identification |
| per mode | no spectral calculation | no mode exhaustion |
| per block | two Dijkstras and two singleton variances | no law selection |
| lattice wide | checked and not executed | no infinite-volume score |

### N6 — live partial-closure paths

Live routes are a derived hop-cost, a reason to adopt one of the two
scores, a still larger-radius union, and a separately derived formation
law. None is closed here.

### N7 — hostile steelman

**Steelman:** Because the radius-`6` meeting set was a singleton, the
radius-`12` union should admit `|M|>1` and then a strictly smaller
arrival-speed variance under `μ` than under `ℓ¹`.

**Answer:** Under the stated neighbor test both first-meeting fronts remain
the singleton `{(1,0,0)}`. Population variance on a singleton is `0` for
every positive arrival. The one-seed roundness gap does not appear as a
meeting-set variance gap here, and enlarging the ball does not enlarge `M`.

### N8 — cross-cycle echo

The one-seed corridor-slide reverse at `k=7` is not reused as a lemma.
The radius-`6` singleton is not copied as a substitute for the two
Dijkstras on this union. The two scores are computed here. L1 remains
unattached.

**Gate disposition:** PASS for the reported meeting site, `|M|`, the two
variances, the displayed lex-first minimizer `ℓ¹`, and the refusal to
adopt a hop-cost or attach L1. FAIL / DO NOT SHIP for writing `μ` into
Admissibility, attaching L1, or claiming a unique physical law.

## What This Note Does Not Claim

- Uniqueness of `μ` among hop-costs with this meeting set.
- Any edit of Lattice, Qubit, Admissibility, or Record.
- Any attachment to L1.
- Any continuum potential, any inverse-power kernel, and any gravitational
  identification.
- Any statement off `B_12(0)∪B_12((2,0,0))`.
- Any adoption of the one-seed reverse as a two-seed variance gap.
- Any claim that `|M|>1` on this union.

## Primary Runner

The primary runner rebuilds the union, runs the two seed-relative
Dijkstras, rebuilds the unit-cost meeting set from taxicab norms,
recomputes the second moments and singleton variances, checks the
lex-first minimizer, and pins the current axiom wording together with the
non-adoption sentences. It authors no audit verdict.
