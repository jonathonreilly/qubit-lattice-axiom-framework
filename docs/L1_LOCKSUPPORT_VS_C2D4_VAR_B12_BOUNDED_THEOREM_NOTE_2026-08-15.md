---
claim_id: l1_locksupport_vs_c2d4_var_b12_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Arrival-speed variance on B_12(0) under unit ℓ¹ versus named c2d4 is compared. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/l1_locksupport_vs_c2d4_var_b12_2026_08_15.py
---

# Unit ℓ¹ Lock-Support Versus Named c2d4 Arrival-Speed Variance On B_12(0)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** two named directed nearest-neighbor hop-costs on the finite
ℓ¹-ball `B_12(0)`, their Dijkstra arrival times from the origin, and the
population variance of `|v|_2/t` on the 2624 nonzero sites. No hop-cost is
written into Admissibility. L1 is not attached.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/l1_locksupport_vs_c2d4_var_b12_2026_08_15.py`](../scripts/l1_locksupport_vs_c2d4_var_b12_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.
**Cache:** none. `cache_write: false`.

## Result Up Front

Write `|σ_v|` for the number of nonzero coordinates of `v ∈ Z^3`. Native unit
ℓ¹ on the cubic 6-NN graph prices every remaining hop at cost `1`. That unit
graph is the lock-support cone of the origin: Record locks at a site, and the
native nearest-neighbor support spreads at unit hop cost. Named `c2d4` is a
separately displayed hop-cost. The parent clauses `ν`, `μ`, and `ρ3` are those
of the ridge-slide scoring on this ball:

- `ν(v→w) = 3` if `|σ_v|=0` or `(|σ_v|=|σ_w|=1)` or `|σ_w| < |σ_v|`, else `1`;
- `μ(v→w) = 3` if `ν` would be `3` or `(|σ_v|=|σ_w|=2` and the least nonzero
  `|w_i|` equals `1)`, else `1`;
- `ρ3(v→w) = 3` if `μ` would be `3` or `(|σ_v|=|σ_w|=3` and exactly two
  `|w_i|` equal `1)`, else `1`;
- `c2d4(v→w) = 3` if `ρ3` would be `3`, else `2` if (`|σ_v|=|σ_w|=2` and
  `max_i |w_i| > max_i |v_i|` and `max_i |v_i| ≥ 4`), else `1`.

The extra `c2d4` clause is a max≥4 out-face hop priced at `2`: support stays
`2`, the destination max absolute coordinate grows, and the source max is
already at least `4`. It is displayed, not adopted. Uniqueness is not required.

The investment is that same-k reverse bits of unit ℓ¹ and named `c2d4`
disagree. The residual here is the first display of arrival-speed variance of
native ℓ¹ lock-support versus displayed `c2d4` on `B_12(0)`. Uniqueness is not
claimed.

The finite host is scored independently. Two Dijkstras from the origin are run
on this ball, unit ℓ¹ first, then `c2d4`. The ball is not leftover of a
larger-ball table.

The executed order of arrival-speed variances on `B_12(0)` is

`var_ℓ¹ > var_c2d4`.

So native ℓ¹ lock-support is strictly less round than displayed `c2d4` on
`B_12(0)`. The scores are displayed, not adopted. Do not write hop-costs into
Admissibility. Do not attach L1.

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
claim_type_reason: "Two finite Dijkstra scores and their population arrival-speed variances on B_12(0) are exact; no hop-cost is adopted and L1 is not attached."
trace_class: upstream_support
target_claim_id: l1_locksupport_vs_c2d4_var_b12
target_blocker_text: "compare arrival-speed variance of unit ℓ¹ lock-support versus named c2d4 on B_12(0)"
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Keep the two scores displayed. Do not write hop-costs into Admissibility. Do not attach L1."
conditional_surface_status: "exact for the two named hop-costs on the induced B_12(0) graph; no physical law is selected"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

Write `0=(0,0,0)` and `B_12(0)={v∈Z^3 : |v|_1 ≤ 12}`. This set has 2625 sites.
The executed graph is the induced nearest-neighbor graph on that set: a
directed hop `v→w` exists when `w-v` is a signed axis unit and `w∈B_12(0)`.

The coordinate support is `σ_v={i : v_i ≠ 0}`. Its cardinality is the
weight. On a hop `v→w`:

- seed-exit means `|σ_v|=0`,
- both-weights-1 means `|σ_v|=|σ_w|=1`,
- support-drop means `|σ_w| < |σ_v|`,
- corridor-slide means `|σ_v|=|σ_w|=2` and the least nonzero `|w_i|` equals `1`,
- ridge-slide means `|σ_v|=|σ_w|=3` and exactly two `|w_i|` equal `1`,
- out-face means `|σ_v|=|σ_w|=2` and `max_i |w_i| > max_i |v_i|`,
- max≥4 out-face means out-face and `max_i |v_i| ≥ 4`.

The two named costs are:

- unit ℓ¹: cost `1` on every remaining 6-NN hop. Written `ℓ¹(v→w) = 1`.
- `c2d4`: cost `3` if `ρ3` would be `3`, else `2` if max≥4 out-face,
  else `1`. Written `c2d4(v→w) = 3` if `|σ_v|=0` or `(|σ_v|=|σ_w|=1)`
  or `|σ_w| < |σ_v|` or `(|σ_v|=|σ_w|=2` and the least nonzero `|w_i|`
  equals `1)` or `(|σ_v|=|σ_w|=3` and exactly two `|w_i|` equal `1)`,
  else `2` if `|σ_v|=|σ_w|=2` and `max_i |w_i| > max_i |v_i|` and
  `max_i |v_i| ≥ 4`, else `1`.

On the seed-exit hop `(0,0,0) → (1,0,0)` one has `|σ_v|=0`, so unit ℓ¹
costs `1` and `c2d4` costs `3`. On the axis hop `(1,0,0) → (2,0,0)` both
weights are `1`, so unit ℓ¹ costs `1` and `c2d4` costs `3`. On the max≥4
out-face hop `(4,2,0) → (5,2,0)` one has `|σ| : 2 → 2`, `max |w_i| = 5 >
max |v_i| = 4`, and source max already `4`, so unit ℓ¹ costs `1` and
`c2d4` costs `2`. On the max≥3 out-face hop `(3,2,0) → (4,2,0)` source max
is `3`, so unit ℓ¹ costs `1` and `c2d4` costs `1`. On the ridge hop
`(1,1,1) → (2,1,1)` one has `|σ| : 3 → 3` and exactly two `|w_i| = 1`, so
unit ℓ¹ costs `1` and `c2d4` costs `3`. On the axis-hugging hop
`(1,1,0) → (2,1,0)` one has `|σ| : 2 → 2` and least nonzero `|w_i| = 1`,
so unit ℓ¹ costs `1` and `c2d4` costs `3` by corridor-slide. The
three-unit enter hop `(1,1,0) → (1,1,1)` stays at cost `1` under both
names. The leave-axis hop `(0,-1,0) → (1,-1,0)` stays at cost `1` under
both names. Therefore named `c2d4` is not the unit-ℓ¹ clause, and the
`c2d4` scores below are not a leftover of lock-support occupancy.

Arrival time `t(v)` is the Dijkstra cost from `0` under the named rule.
Under unit ℓ¹ that arrival equals the coordinate-sum `|v|_1`. The compared
statistic on `B_12(0)\{0}` is the population variance

`var(|v|_2/t) = (1/N) Σ_v (|v|_2/t(v) - mean)^2`,

with `N=2624` and `mean=(1/N) Σ_v |v|_2/t(v)`. Equivalently,
`var = Q - mean^2` where the second moment `Q=(1/N) Σ_v |v|_2^2 / t(v)^2` is
rational. Two Dijkstras are run, one per cost.

This note does not attach L1. The comparison uses only the two named
clause families on the same directed graph.

## Theorem 1 — Two Variances

Every nonzero site is reached under each of the two costs. The exact
second moments on the 2624 nonzero sites are

`Q_ℓ¹ = 337/656`,

`Q_c2d4 = 12586016761121881939/63482497589871360000`.

The population variances, truncated to 18 decimal digits, are

`var_ℓ¹ = 0.009447425719061308`,

`var_c2d4 = 0.003574941366936777`.

Thus both variances are reported.

## Theorem 2 — Variance Order; Displayed, Not Adopted

On `B_12(0)` one has

`var_ℓ¹ > var_c2d4`.

Native unit ℓ¹ lock-support is therefore strictly less round than displayed
`c2d4` on this ball. Equality does not hold. The opposite inequality does
not hold.

Displayed, not adopted. Do not write hop-costs into Admissibility. Do not
attach L1.

The current admissibility rule remains the quoted nearest-neighbor
distribution constraint. The two clause families are scoring rules on
`B_12(0)`, not a replacement of that axiom. No formation law, occupancy
member, or locked-set filling rule is identified with either hop-cost.
Uniqueness among hop-costs outside this pair is not required and is not
claimed.

## Promotion Value Gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers whether native ℓ¹ lock-support is rounder or less round than displayed c2d4 on B_12(0). |
| V2 | Current main has no landed unit-ℓ¹ versus c2d4 variance comparison on B_12(0). |
| V3 | The two Dijkstras and the 2624-site population variances are finite and exact. |
| V4 | The comparison is not an axiom rewrite: Admissibility is left unchanged. |
| V5 | Displayed scores are not a physical hop-cost or formation law. |

## No-Go Discipline Gate

The negative content is narrow: these two scores are reported on `B_12(0)`
and are not adopted. No uniqueness of a physical law is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| unit ℓ¹ | cost `1` on every remaining 6-NN hop | executed; larger variance |
| `c2d4` | all `ρ3` clauses plus max≥4 out-face `2→2` hops at cost `2` | executed; smaller variance |
| other clause pairs | tax every out-face at `3`, or drop the source-max floor | different named family; not this residual |
| unrestricted `Z^3` paths | leave `B_12(0)` and return | outside the declared ball |
| adopt a score | write hop-costs into Admissibility | forbidden; not executed |
| attach L1 | identify a score with a formation member | forbidden; not executed |

### N2 — wall independence

Ball restriction, hop-cost clauses, the speed statistic, and axiom
non-adoption are distinct. This note claims no complete wall collection.

### N3 — hidden-condition scan

The ball, the induced graph, the two cost clauses, and population variance
are declared. No continuum limit, no physical clock, and no formation rate
are assumed.

### N4 — source residual matching

The axiom memo supplies the cubic nearest-neighbor substrate and the
distribution sentence. It does not name hop-cost clauses. The residual is
a finite comparison on that substrate, not an axiom edit.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | each nonzero site of `B_12(0)` | no other ball |
| per site | one arrival time per named cost | no physical tick identification |
| per mode | no spectral calculation | no mode exhaustion |
| per block | two Dijkstras and one variance pair | no law selection |
| lattice wide | checked and not executed | no `Z^3` or infinite-volume score |

### N6 — live partial-closure paths

Live routes are a derived hop-cost, a reason to adopt one of the two
scores, a comparison on a larger ball, and a separately derived formation
law. None is closed here.

### N7 — hostile steelman

**Steelman:** Because unit ℓ¹ is the native lock-support cone, its
arrival-speed field should be at least as round as named `c2d4` on
`B_12(0)`, so the displayed comparison should report `var_ℓ¹ < var_c2d4`
or equality.

**Answer:** Pricing every hop at `1` leaves axis sites at Euclidean speed
`1` and body-diagonal sites near `1/√3`. Named `c2d4` prices seed-exit and
axis hops at `3`, which slows those high-speed sites. On `B_12(0)` the
executed variances satisfy `var_ℓ¹ > var_c2d4`. Native ℓ¹ lock-support is
strictly less round than displayed `c2d4` on this ball.

### N8 — cross-cycle echo

The same-k reverse-bit comparison of unit ℓ¹ versus `c2d4` and the
already-scored `c2d4` variance against other named hop-costs are not
reused as lemmas. The two scores are computed on `B_12(0)`. L1 remains
unattached.

**Gate disposition:** PASS for the two reported variances, the displayed
order `var_ℓ¹ > var_c2d4`, and the refusal to adopt a hop-cost or attach L1.
FAIL / DO NOT SHIP for writing hop-costs into Admissibility, attaching L1,
or claiming a unique physical law.

## What This Does Not Claim

- Uniqueness is not required.
- No physical identification of `t` as a clock, mass, or force law is made.
- No claim is made that Record locks these arrival times.
- Independent leftovers on larger balls are not used as parents.
- The roundness comparison on this ball is not a no-go against named
  hop-costs elsewhere.

These are scope boundaries, not impossibility or route-exhaustion claims.
Accordingly, no no-go verdict is authored here.

## Live Parent Quotes

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

> There is one fixed nearest-neighbor admissibility rule, covariant under lattice
> translations and proper cubic rotations.

> A site with no record cannot be read.

Their dependency role is limited to the repository's site graph and the
refusal to treat a named hop-cost as axiom content.

## Primary Runner

The primary runner rebuilds `B_12(0)`, runs the two Dijkstras, recomputes
the second moments and population variances, checks the reported order,
and pins the current axiom wording together with the non-adoption
sentences. It authors no audit verdict.
