---
claim_id: ridge_slide_var_vs_mu_nu_b12_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Arrival-speed variance under ridge-slide, corridor-slide, and support-drop on B_12(0) is compared. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/ridge_slide_var_vs_mu_nu_b12_2026_08_15.py
---

# Named Ridge-Slide Versus μ Versus ν Arrival-Speed Variance On B_12(0)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** three named directed nearest-neighbor hop-costs on the finite
ℓ¹-ball `B_12(0)`, their Dijkstra arrival times from the origin, and the
population variance of `|v|_2/t` on the 2624 nonzero sites. No hop-cost is
written into Admissibility. L1 is not attached.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/ridge_slide_var_vs_mu_nu_b12_2026_08_15.py`](../scripts/ridge_slide_var_vs_mu_nu_b12_2026_08_15.py)
**Cache:** none. `cache_write: false`.

## Result Up Front

The named ridge-slide hop-cost `ρ3` is the already scored corridor-slide
rule `μ` plus cost `3` on those `3→3` hops whose destination has exactly
two absolute coordinates equal to `1`. The named corridor-slide hop-cost
`μ` is the support-drop rule `ν` plus cost `3` only on those `2→2` hops
whose destination has least nonzero absolute coordinate equal to `1`.
The investment is that ridge-slide taxes the `μ` axis corridor. The
residual here is whether `ρ3` is rounder or worse than `μ` on `B_12(0)`.
Uniqueness is not claimed.

The executed order of arrival-speed variances on `B_12(0)` is

`var_ρ3 < var_μ < var_ν`.

So `ρ3` is strictly rounder than both `μ` and `ν` on `B_12(0)`. The
lex-first minimizer among the three displayed names is `ρ3`. The scores
are displayed, not adopted. Do not write `ρ3`, `μ`, or `ν` into
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
claim_type_reason: "Three finite Dijkstra scores and their population arrival-speed variances on B_12(0) are exact; no hop-cost is adopted and L1 is not attached."
trace_class: upstream_support
target_claim_id: ridge_slide_var_vs_mu_nu_b12
target_blocker_text: "compare arrival-speed variance of ρ3, μ, and ν on B_12(0)"
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Keep the three scores displayed. Do not write ρ3, μ, or ν into Admissibility. Do not attach L1."
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
- ridge-slide means `|σ_v|=|σ_w|=3` and exactly two `|w_i|` equal `1`.

The three named costs are:

- `ρ3`: cost `3` if `μ` would be `3` or ridge-slide, else `1`. Written
  `ρ3(v→w) = 3` if `|σ_v|=0` or `(|σ_v|=|σ_w|=1)` or `|σ_w| < |σ_v|` or
  `(|σ_v|=|σ_w|=2` and the least nonzero `|w_i|` equals `1)` or
  `(|σ_v|=|σ_w|=3` and exactly two `|w_i|` equal `1)`, else `1`.
- `μ`: cost `3` if `ν` would be `3` or corridor-slide, else `1`. Written
  `μ(v→w) = 3` if `|σ_v|=0` or `(|σ_v|=|σ_w|=1)` or `|σ_w| < |σ_v|` or
  `(|σ_v|=|σ_w|=2` and the least nonzero `|w_i|` equals `1)`, else `1`.
- `ν`: cost `3` if seed-exit or both-weights-1 or support-drop, else `1`.

On the ridge hop `(1,1,1) → (2,1,1)` one has `|σ| : 3 → 3` and exactly
two `|w_i| = 1`, so `ν = μ = 1` while `ρ3 = 3`. On the non-ridge body
hop `(2,2,1) → (3,2,1)` one has `|σ| : 3 → 3` and only one `|w_i| = 1`,
so all three names stay at cost `1`. On the axis-hugging hop
`(1,1,0) → (2,1,0)` one has `|σ| : 2 → 2` and least nonzero `|w_i| = 1`,
so `ν = 1` while `ρ3 = μ = 3`. The leave-axis hop `(0,-1,0) → (1,-1,0)`
stays at cost `1` under all three names. Therefore neither `μ` nor `ν`
prices the ridge clause, and the `ρ3` scores below are not a leftover of
either comparator.

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

`Q_ρ3 = 8080835149812247289/37031456927424960000`,

`Q_μ = 81461329283517896329/284940228576113510400`,

`Q_ν = 775884178398451/2344690585036800`.

The population variances, truncated to 18 decimal digits, are

`var_ρ3 = 0.005047718614862020`,

`var_μ = 0.005601692188543646`,

`var_ν = 0.006660738070183863`.

Thus all three variances are reported. The ridge-slide rule `ρ3` is
strictly rounder than `μ` on `B_12(0)`, and `μ` remains strictly
rounder than `ν`.

## Theorem 2 — Lex-First Minimizer

Order the three names as the strings `mu`, `nu`, and `rho3`. The
variance-minimizing score among those three is `ρ3`, and it is the unique
minimum of the three displayed numbers. Therefore the lex-first
minimizer among the three is `ρ3`. Uniqueness among hop-costs outside this
triple is not required and is not claimed.

The minimizer is displayed, not adopted.

## Theorem 3 — No Admissibility Write, L1 Not Attached

Do not write `ρ3`, `μ`, or `ν` into Admissibility. The current admissibility
rule remains the quoted nearest-neighbor distribution constraint. The three
clause families are scoring rules on `B_12(0)`, not a replacement of that
axiom.

Do not attach L1. No formation law, occupancy member, or locked-set filling
rule is identified with any of the three hop-costs.

## Promotion Value Gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers whether ρ3 is rounder or worse than μ and ν on B_12(0). |
| V2 | Current main has no landed ρ3/μ/ν variance comparison on B_12(0). |
| V3 | The three Dijkstras and the 2624-site population variances are finite and exact. |
| V4 | The comparison is not an axiom rewrite: Admissibility is left unchanged. |
| V5 | Displayed scores are not a physical hop-cost or formation law. |

## No-Go Discipline Gate

The negative content is narrow: these three scores are compared on `B_12(0)`
and are not adopted. No uniqueness of a physical law is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| `ρ3` | all `μ` clauses plus ridge `3→3` hops expensive | executed; lex-first variance minimizer |
| `μ` | all `ν` clauses plus hugging `2→2` expensive | executed; between `ρ3` and `ν` |
| `ν` | seed-exit, both-weights-1, and support-drop expensive | executed; largest variance |
| other clause triples | drop the ridge family or price every `3→3` | different named family; not this residual |
| unrestricted `Z^3` paths | leave `B_12(0)` and return | outside the declared ball |
| adopt a score | write `ρ3`, `μ`, or `ν` into Admissibility | forbidden; not executed |
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

**Steelman:** Because `μ` already restores the axis corridor that ridge
paths sit on, taxing those remaining `3→3` hops whose destination has
exactly two unit coordinates should stretch the arrival-speed field and
make `ρ3` worse-round than `μ` on `B_12(0)`.

**Answer:** Pricing the ridge clause changes the whole arrival field. On
`B_12(0)` the executed variances are strictly ordered
`var_ρ3 < var_μ < var_ν`. The extra ridge clause is rounder, not worse,
than both `μ` and `ν` on this ball.

### N8 — cross-cycle echo

The corridor-slide same-`k` restore and the ridge-slide same-`k` scores
are not reused as lemmas. The three scores are computed on `B_12(0)`.
L1 remains unattached.

**Gate disposition:** PASS for the three reported variances, the displayed
lex-first minimizer `ρ3`, and the refusal to adopt a hop-cost or attach L1.
FAIL / DO NOT SHIP for writing `ρ3`, `μ`, or `ν` into Admissibility,
attaching L1, or claiming a unique physical law.

## Primary Runner

The primary runner rebuilds `B_12(0)`, runs the three Dijkstras, recomputes
the second moments and population variances, checks the reported order and
lex-first minimizer, and pins the current axiom wording together with the
non-adoption sentences. It authors no audit verdict.
