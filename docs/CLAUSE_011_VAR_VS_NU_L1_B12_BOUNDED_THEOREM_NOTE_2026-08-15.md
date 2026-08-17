---
claim_id: clause_011_var_vs_nu_l1_b12_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Arrival-speed variance under (0,1,1), support-drop, and ℓ¹ on B_12(0) is compared. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/clause_011_var_vs_nu_l1_b12_2026_08_15.py
---

# Clause (0,1,1) Versus ν Versus ℓ¹ Arrival-Speed Variance On B_12(0)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** three named directed nearest-neighbor hop-costs on the finite
ℓ¹-ball `B_12(0)`, their Dijkstra arrival times from the origin, and the
population variance of `|v|_2/t` on the 2624 nonzero sites. No hop-cost is
written into Admissibility. L1 is not attached.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/clause_011_var_vs_nu_l1_b12_2026_08_15.py`](../scripts/clause_011_var_vs_nu_l1_b12_2026_08_15.py)

## Result Up Front

On `B_8(0)`, the executed order of arrival-speed variances is
`var_ν < var_(0,1,1) < var_ℓ¹`. The same three scores are now evaluated on
`B_12(0)`, the radius at which the named support-drop rule ν already fails
the doubled-pair reverse `12 t(8,0,0)^2 > 16 t(4,4,4)^2`. Uniqueness is
not required. The executed order is

`var_ν < var_(0,1,1) < var_ℓ¹`.

The cheaper rival stays worse-round. The lex-first minimizer among the
three displayed scores is ν. The scores are displayed, not adopted.

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
target_claim_id: clause_011_var_vs_nu_l1_b12
target_blocker_text: "compare arrival-speed variance of (0,1,1), ν, and ℓ¹ on B_12(0)"
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Keep the three scores displayed. Do not write (0,1,1) or ν into Admissibility. Do not attach L1."
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
- support-drop means `|σ_w| < |σ_v|`.

The three named costs are:

- `(0,1,1)`: cost `3` if both-weights-1 or support-drop, else `1`. Seed-exit
  is cheap.
- `ν=(1,1,1)`: cost `3` if seed-exit or both-weights-1 or support-drop, else
  `1`.
- `ℓ¹`: every executed hop costs `1`.

Arrival time `t(v)` is the Dijkstra cost from `0` under the named rule.
The compared statistic on `B_12(0)\{0}` is the population variance

`var(|v|_2/t) = (1/N) Σ_v (|v|_2/t(v) - μ)^2`,

with `N=2624` and `μ=(1/N) Σ_v |v|_2/t(v)`. Equivalently,
`var = Q - μ^2` where the second moment `Q=(1/N) Σ_v |v|_2^2 / t(v)^2` is
rational. Three Dijkstras are run, one per cost.

This note does not attach L1. The `ℓ¹` score is only the unit-cost comparison
on the same directed graph.

## Theorem 1 — Three Variances

Every nonzero site is reached under each of the three costs. Under `ℓ¹`,
`t(v)=|v|_1`. The exact second moments on the 2624 nonzero sites are

`Q_(0,1,1) = 884017798061/1774744171200`,

`Q_ν = 775884178398451/2344690585036800`,

`Q_ℓ¹ = 337/656`.

The population variances, truncated to 18 decimal digits, are

`var_(0,1,1) = 0.007725513804812077`,

`var_ν = 0.006660738070183863`,

`var_ℓ¹ = 0.009447425719061308`.

Thus all three variances are reported. The cheaper rival `(0,1,1)` remains
strictly worse-round than ν, and both named clause scores remain strictly
below the unit-cost score.

## Theorem 2 — Lex-First Minimizer

Order the three names as the strings `(0,1,1)`, `l1`, and `nu`. The
variance-minimizing score among those three is ν, and it is the unique
minimum of the three displayed numbers. Therefore the lex-first
minimizer among the three is ν. Uniqueness among hop-costs outside this
triple is not required and is not claimed.

The minimizer is displayed, not adopted.

## Theorem 3 — No Admissibility Write, L1 Not Attached

Do not write `(0,1,1)` or ν into Admissibility. The current admissibility
rule remains the quoted nearest-neighbor distribution constraint. The two
clause triples and the unit-cost comparison are scoring rules on `B_12(0)`,
not a replacement of that axiom.

Do not attach L1. No formation law, occupancy member, or locked-set filling
rule is identified with any of the three hop-costs.

## Promotion Value Gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers whether the cheaper B_8 rival stays worse-round on B_12(0). |
| V2 | Current main has no landed (0,1,1)/ν/ℓ¹ variance comparison on B_12(0). |
| V3 | The three Dijkstras and the 2624-site population variances are finite and exact. |
| V4 | The comparison is not an axiom rewrite: Admissibility is left unchanged. |
| V5 | Displayed scores are not a physical hop-cost or formation law. |

## No-Go Discipline Gate

The negative content is narrow: these three scores are compared on `B_12(0)`
and are not adopted. No uniqueness of a physical law is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| `(0,1,1)` | cheap seed-exit, expensive axis-1 and support-drop | executed; worse-round than ν |
| ν | all three clauses expensive | executed; lex-first variance minimizer |
| `ℓ¹` | unit hop-cost | executed; largest variance |
| other clause triples | enable seed-exit only, or drop support-drop | different named family; not this residual |
| unrestricted `Z^3` paths | leave `B_12(0)` and return | outside the declared ball |
| adopt a score | write `(0,1,1)` or ν into Admissibility | forbidden; not executed |
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
distribution sentence. It does not name hop-cost triples. The residual is
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

**Steelman:** Because `(0,1,1)` is cheaper at the seed, and because ν
already fails the doubled-pair reverse on this ball, the cheaper rival
should at least match ν in arrival-speed variance on `B_12(0)`.

**Answer:** Cheap seed-exit changes the whole arrival field. On `B_12(0)`
the executed variances remain strictly ordered `var_ν < var_(0,1,1)`.
Cheaper is not rounder, even at the radius where ν reverse already fails
the doubled pair.

### N8 — cross-cycle echo

The B_8 investment that ν is rounder than `(0,1,1)` is not reused as a
lemma. The three scores are recomputed on `B_12(0)`. L1 remains unattached.

**Gate disposition:** PASS for the three reported variances, the displayed
lex-first minimizer ν, and the refusal to adopt a hop-cost or attach L1.
FAIL / DO NOT SHIP for writing `(0,1,1)` or ν into Admissibility, attaching
L1, or claiming a unique physical law.

## Primary Runner

The primary runner rebuilds `B_12(0)`, runs the three Dijkstras, recomputes
the second moments and population variances, checks the reported order and
lex-first minimizer, and pins the current axiom wording together with the
non-adoption sentences. It authors no audit verdict.
