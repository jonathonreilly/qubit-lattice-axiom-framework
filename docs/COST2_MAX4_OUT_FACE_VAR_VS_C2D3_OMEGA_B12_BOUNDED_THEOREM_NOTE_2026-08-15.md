---
claim_id: cost2_max4_out_face_var_vs_c2d3_omega_b12_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Arrival-speed variance under cost-2 max≥4 out-face, cost-2 max≥3 out-face, and out-face on B_12(0) is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/cost2_max4_out_face_var_vs_c2d3_omega_b12_2026_08_15.py
---

# Named Cost-2 Max≥4 Out-Face Versus c2d3 Versus ω Arrival-Speed Variance On B_12(0)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** three named directed nearest-neighbor hop-costs on the finite
ℓ¹-ball `B_12(0)`, their Dijkstra arrival times from the origin, and the
population variance of `|v|_2/t` on the 2624 nonzero sites. No hop-cost is
written into Admissibility. L1 is not attached.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/cost2_max4_out_face_var_vs_c2d3_omega_b12_2026_08_15.py`](../scripts/cost2_max4_out_face_var_vs_c2d3_omega_b12_2026_08_15.py)
**Cache:** none. `cache_write: false`.

## Result Up Front

The named cost-2 max≥4 out-face hop-cost `c2d4` is the already scored
ridge-slide rule `ρ3` except that those `2→2` hops whose destination has
a strictly larger max absolute coordinate than the source, and whose
source max is already at least `4`, cost `2` rather than `1`. The named
cost-2 max≥3 out-face hop-cost `c2d3` is the same except that the source-max
floor is `3`. The named out-face hop-cost `ω` is `ρ3` plus cost `3` on
every `2→2` hop whose destination has a strictly larger max absolute
coordinate than the source, with no source-max floor. The investment is
that `c2d4` restores k=14 and holds face k=1..8, and that `c2d3` is
rounder than `ω`. The residual here is the first display of arrival-speed
variance of `c2d4` versus `c2d3` and `ω` on `B_12(0)`. Uniqueness is not claimed.

The executed order of arrival-speed variances on `B_12(0)` is

`var_c2d4 < var_c2d3 < var_ω`.

So `c2d4` is strictly rounder than both `c2d3` and `ω` on `B_12(0)`, and
`c2d3` is strictly rounder than `ω`. The lex-first minimizer among the
three displayed names is `c2d4`. The scores are displayed, not adopted.
Do not write `c2d4`, `c2d3`, or `ω` into Admissibility. Do not attach L1.

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
claim_type_reason: "Three finite Dijkstra scores and their population arrival-speed variances on B_12(0) are exact; no hop-cost is adopted and L1 is not attached."
trace_class: upstream_support
target_claim_id: cost2_max4_out_face_var_vs_c2d3_omega_b12
target_blocker_text: "compare arrival-speed variance of c2d4, c2d3, and ω on B_12(0)"
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Keep the three scores displayed. Do not write c2d4, c2d3, or ω into Admissibility. Do not attach L1."
conditional_surface_status: "exact for the three named hop-costs on the induced B_12(0) graph; no physical law is selected"
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
- max≥3 out-face means out-face and `max_i |v_i| ≥ 3`,
- max≥4 out-face means out-face and `max_i |v_i| ≥ 4`.

The three named costs are:

- `c2d4`: cost `3` if `ρ3` would be `3`, else `2` if max≥4 out-face,
  else `1`. Written `c2d4(v→w) = 3` if `|σ_v|=0` or `(|σ_v|=|σ_w|=1)`
  or `|σ_w| < |σ_v|` or `(|σ_v|=|σ_w|=2` and the least nonzero `|w_i|`
  equals `1)` or `(|σ_v|=|σ_w|=3` and exactly two `|w_i|` equal `1)`,
  else `2` if `|σ_v|=|σ_w|=2` and `max_i |w_i| > max_i |v_i|` and
  `max_i |v_i| ≥ 4`, else `1`.
- `c2d3`: cost `3` if `ρ3` would be `3`, else `2` if max≥3 out-face,
  else `1`. Written `c2d3(v→w) = 3` if `|σ_v|=0` or `(|σ_v|=|σ_w|=1)`
  or `|σ_w| < |σ_v|` or `(|σ_v|=|σ_w|=2` and the least nonzero `|w_i|`
  equals `1)` or `(|σ_v|=|σ_w|=3` and exactly two `|w_i|` equal `1)`,
  else `2` if `|σ_v|=|σ_w|=2` and `max_i |w_i| > max_i |v_i|` and
  `max_i |v_i| ≥ 3`, else `1`.
- `ω`: cost `3` if `ρ3` would be `3` or out-face, else `1`. Written
  `ω(v→w) = 3` if `|σ_v|=0` or `(|σ_v|=|σ_w|=1)` or `|σ_w| < |σ_v|` or
  `(|σ_v|=|σ_w|=2` and the least nonzero `|w_i|` equals `1)` or
  `(|σ_v|=|σ_w|=3` and exactly two `|w_i|` equal `1)` or
  `(|σ_v|=|σ_w|=2` and `max_i |w_i| > max_i |v_i|)`, else `1`.

On the max≥4 out-face hop `(4,2,0) → (5,2,0)` one has `|σ| : 2 → 2`,
`max |w_i| = 5 > max |v_i| = 4`, and source max already `4`, so
`ω = 3` and `c2d4 = c2d3 = 2`. On the max≥3 out-face hop
`(3,2,0) → (4,2,0)` one has `|σ| : 2 → 2`, `max |w_i| = 4 > max |v_i| = 3`,
and source max `3`, so `ω = 3`, `c2d3 = 2`, and `c2d4 = 1`. On the
deep-out hop `(2,2,0) → (3,2,0)` one has `|σ| : 2 → 2` and a growing max,
but source max `2`, so `ω = 3` while `c2d4 = c2d3 = 1`. On the ridge hop
`(1,1,1) → (2,1,1)` one has `|σ| : 3 → 3` and exactly two `|w_i| = 1`,
so all three names cost `3`. On the axis-hugging hop `(1,1,0) → (2,1,0)`
one has `|σ| : 2 → 2`, least nonzero `|w_i| = 1`, and a growing max, so
all three names cost `3` by corridor-slide. The three-unit enter hop
`(1,1,0) → (1,1,1)` stays at cost `1` under all three names. The
leave-axis hop `(0,-1,0) → (1,-1,0)` stays at cost `1` under all three
names. Therefore neither `c2d3` nor `ω` is the cost-2 max≥4 out-face
clause, and the `c2d4` scores below are not a leftover of either
comparator.

Arrival time `t(v)` is the Dijkstra cost from `0` under the named rule.
The compared statistic on `B_12(0)\{0}` is the population variance

`var(|v|_2/t) = (1/N) Σ_v (|v|_2/t(v) - mean)^2`,

with `N=2624` and `mean=(1/N) Σ_v |v|_2/t(v)`. Equivalently,
`var = Q - mean^2` where the second moment `Q=(1/N) Σ_v |v|_2^2 / t(v)^2` is
rational. Three Dijkstras are run, one per cost.

This note does not attach L1. The comparison uses only the three named
clause families on the same directed graph.

## Theorem 1 — Three Variances

Every nonzero site is reached under each of the three costs. The exact
second moments on the 2624 nonzero sites are

`Q_c2d4 = 12586016761121881939/63482497589871360000`,

`Q_c2d3 = 2273856763058868971/11694144292871040000`,

`Q_ω = 2697928722329275408991/14234892042902154624000`.

The population variances, truncated to 18 decimal digits, are

`var_c2d4 = 0.003574941366936777`,

`var_c2d3 = 0.003682635284982629`,

`var_ω = 0.004242786759120176`.

Thus all three variances are reported. The cost-2 max≥4 out-face rule
`c2d4` is strictly rounder than `c2d3` on `B_12(0)`, and `c2d3` remains
strictly rounder than `ω`.

## Theorem 2 — Lex-First Minimizer

Order the three names as the strings `c2d3`, `c2d4`, and `omega`. The
variance-minimizing score among those three is `c2d4`, and it is the
unique minimum of the three displayed numbers. Therefore the lex-first
minimizer among the three is `c2d4`. Uniqueness among hop-costs outside
this triple is not required and is not claimed.

The minimizer is displayed, not adopted.

Displayed, not adopted.

## Theorem 3 — No Admissibility Write, L1 Not Attached

Do not write `c2d4`, `c2d3`, or `ω` into Admissibility. The current
admissibility rule remains the quoted nearest-neighbor distribution
constraint. The three clause families are scoring rules on `B_12(0)`, not
a replacement of that axiom.

Do not attach L1. No formation law, occupancy member, or locked-set filling
rule is identified with any of the three hop-costs.

## Promotion Value Gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers whether c2d4 is rounder or worse than c2d3 and ω on B_12(0). |
| V2 | Current main has no landed c2d4/c2d3/ω variance comparison on B_12(0). |
| V3 | The three Dijkstras and the 2624-site population variances are finite and exact. |
| V4 | The comparison is not an axiom rewrite: Admissibility is left unchanged. |
| V5 | Displayed scores are not a physical hop-cost or formation law. |

## No-Go Discipline Gate

The negative content is narrow: these three scores are reported on `B_12(0)`
and are not adopted. No uniqueness of a physical law is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| `c2d4` | all `ρ3` clauses plus max≥4 out-face `2→2` hops at cost `2` | executed; lex-first variance minimizer |
| `c2d3` | all `ρ3` clauses plus max≥3 out-face `2→2` hops at cost `2` | executed; between `c2d4` and `ω` |
| `ω` | all `ρ3` clauses plus every out-face `2→2` hop at cost `3` | executed; largest variance |
| other clause triples | tax every out-face at `3` only, or drop the source-max floor to `3` | different named family; not this residual |
| unrestricted `Z^3` paths | leave `B_12(0)` and return | outside the declared ball |
| adopt a score | write `c2d4`, `c2d3`, or `ω` into Admissibility | forbidden; not executed |
| attach L1 | identify a score with a formation member | forbidden; not executed |

### N2 — wall independence

Ball restriction, hop-cost clauses, the speed statistic, and axiom
non-adoption are distinct. This note claims no complete wall collection.

### N3 — hidden-condition scan

The ball, the induced graph, the three cost clauses, population variance,
and lex-first among the three names are declared. No continuum limit, no
physical clock, and no formation rate are assumed.

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
| per block | three Dijkstras and one variance triple | no law selection |
| lattice wide | checked and not executed | no `Z^3` or infinite-volume score |

### N6 — live partial-closure paths

Live routes are a derived hop-cost, a reason to adopt one of the three
scores, a comparison on a larger ball, and a separately derived formation
law. None is closed here.

### N7 — hostile steelman

**Steelman:** Because `c2d3` taxes every max≥3 out-face hop at `2`,
including the source-max `3` hops that `c2d4` leaves at `1`, the
arrival-speed field of `c2d3` should be at least as round as `c2d4` on
`B_12(0)`, so the displayed minimum among the three names should be
`c2d3` rather than `c2d4`.

**Answer:** Pricing only the max≥4 out-face hop at `2`, and leaving the
source-max `3` out-face hop at `1`, changes the whole arrival field.
On `B_12(0)` the executed variances are strictly ordered
`var_c2d4 < var_c2d3 < var_ω`. The cost-2 max≥4 out-face clause is
strictly rounder than both `c2d3` and `ω` on this ball.

### N8 — cross-cycle echo

The cost-2 max≥4 same-`k` scores, the cost-2 max≥3 variance scores, and
the out-face variance scores are not reused as lemmas. The three scores
are computed on `B_12(0)`. L1 remains unattached.

**Gate disposition:** PASS for the three reported variances, the displayed
lex-first minimizer `c2d4`, and the refusal to adopt a hop-cost or attach L1.
FAIL / DO NOT SHIP for writing `c2d4`, `c2d3`, or `ω` into Admissibility,
attaching L1, or claiming a unique physical law.

## Primary Runner

The primary runner rebuilds `B_12(0)`, runs the three Dijkstras, recomputes
the second moments and population variances, checks the reported order and
lex-first minimizer, and pins the current axiom wording together with the
non-adoption sentences. It authors no audit verdict.
