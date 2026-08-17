---
claim_id: height_ridge_var_vs_rho3_mu_b12_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Arrival-speed variance under height-ridge, ridge-slide, and corridor-slide on B_12(0) is compared. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/height_ridge_var_vs_rho3_mu_b12_2026_08_15.py
---

# Height-Ridge Versus ρ3 Versus μ Arrival-Speed Variance On B_12(0)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** three named directed nearest-neighbor hop-costs on the finite
ℓ¹-ball `B_12(0)`, their Dijkstra arrival times from the origin, and the
population variance of `|v|_2/t` on the 2624 nonzero sites. No hop-cost is
written into Admissibility. L1 is not attached.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/height_ridge_var_vs_rho3_mu_b12_2026_08_15.py`](../scripts/height_ridge_var_vs_rho3_mu_b12_2026_08_15.py)

## Result Up Front

The ridge-slide rule ρ3 is rounder than the corridor-slide rule μ on
`B_12(0)`. The new clause ζ taxes height-`m` ridges for `m ≥ 2`. The same
three scores are now evaluated on `B_12(0)`. Uniqueness is not required.
The executed order is

`var_ρ3 < var_ζ < var_μ`.

ζ is worse-round than ρ3. The lex-first minimizer among the three
displayed scores is ρ3. The scores are displayed, not adopted.

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
target_claim_id: height_ridge_var_vs_rho3_mu_b12
target_blocker_text: "compare arrival-speed variance of ζ, ρ3, and μ on B_12(0)"
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Keep the three scores displayed. Do not write ζ, ρ3, or μ into Admissibility. Do not attach L1."
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

The coordinate support is `σ_v={i : v_i ≠ 0}`. Write `|σ_v|` for its
cardinality. On a hop `v→w`:

- `ν(v→w)=3` if `|σ_v|=0` or (`|σ_v|=|σ_w|=1`) or `|σ_w|<|σ_v|`, else `1`.
- `μ(v→w)=3` if ν would be `3` or (`|σ_v|=|σ_w|=2` and the least nonzero
  `|w_i|` equals `1`), else `1`.
- `ρ3(v→w)=3` if μ would be `3` or (`|σ_v|=|σ_w|=3` and exactly two `|w_i|`
  equal `1`), else `1`.
- `ζ(v→w)=3` if ρ3 would be `3` or (`|σ_v|=|σ_w|=3` and exactly two `|w_i|`
  equal `m` and `m=min_j |w_j|` and `m≥2`), else `1`.

Corridor-slide is μ. Ridge-slide is ρ3. Height-ridge is ζ: it taxes the
same hops as ρ3 and, in addition, the 3→3 hops whose destination is a
height-`m` ridge for `m≥2`.

Arrival time `t(v)` is the Dijkstra cost from `0` under the named rule.
The compared statistic on `B_12(0)\{0}` is the population variance

`var(|v|_2/t) = (1/N) Σ_v (|v|_2/t(v) - mean)^2`,

with `N=2624` and `mean=(1/N) Σ_v |v|_2/t(v)`. Equivalently,
`var = Q - mean^2` where the second moment `Q=(1/N) Σ_v |v|_2^2 / t(v)^2` is
rational. Three Dijkstras are run, one per cost.

This note does not attach L1.

## Theorem 1 — Three Variances

Every nonzero site is reached under each of the three costs. The exact
second moments on the 2624 nonzero sites are

`Q_ζ = 7935966931146340589/37031456927424960000`,

`Q_ρ3 = 8080835149812247289/37031456927424960000`,

`Q_μ = 81461329283517896329/284940228576113510400`.

The population variances, truncated to 18 decimal digits, are

`var_ζ = 0.005394463770340473`,

`var_ρ3 = 0.005047718614862020`,

`var_μ = 0.005601692188543646`.

Thus all three variances are reported. Height-ridge ζ remains strictly
worse-round than ridge-slide ρ3, and ρ3 remains strictly rounder than
corridor-slide μ.

## Theorem 2 — Lex-First Minimizer

Order the three names as the strings `mu`, `rho3`, and `zeta`. The
variance-minimizing score among those three is ρ3, and it is the unique
minimum of the three displayed numbers. Therefore the lex-first
minimizer among the three is ρ3. Uniqueness among hop-costs outside this
triple is not required and is not claimed.

The minimizer is displayed, not adopted.

## Theorem 3 — No Admissibility Write, L1 Not Attached

Do not write ζ, ρ3, or μ into Admissibility. The current admissibility
rule remains the quoted nearest-neighbor distribution constraint. The
three named hop-costs are scoring rules on `B_12(0)`, not a replacement
of that axiom.

Do not attach L1. No formation law, occupancy member, or locked-set filling
rule is identified with any of the three hop-costs.

## Promotion Value Gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers whether the height-ridge tax is rounder or worse than ρ3 on B_12(0). |
| V2 | Current main has no landed ζ/ρ3/μ variance comparison on B_12(0). |
| V3 | The three Dijkstras and the 2624-site population variances are finite and exact. |
| V4 | The comparison is not an axiom rewrite: Admissibility is left unchanged. |
| V5 | Displayed scores are not a physical hop-cost or formation law. |

## No-Go Discipline Gate

The negative content is narrow: these three scores are compared on `B_12(0)`
and are not adopted. No uniqueness of a physical law is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| ζ | ρ3 plus height-`m` ridge tax for `m≥2` | executed; worse-round than ρ3 |
| ρ3 | μ plus unit-ridge 3→3 tax | executed; lex-first variance minimizer |
| μ | ν plus axis-hugging 2→2 tax | executed; largest variance of the three |
| other height clauses | tax all-equal body hops or only one `m` | different named family; not this residual |
| unrestricted `Z^3` paths | leave `B_12(0)` and return | outside the declared ball |
| adopt a score | write ζ, ρ3, or μ into Admissibility | forbidden; not executed |
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

**Steelman:** Because leftover body paths are hypothesized to use
height-2 ridges, taxing those ridges should at least match ρ3 in
arrival-speed variance on `B_12(0)`.

**Answer:** The extra 3→3 tax changes the whole arrival field. On
`B_12(0)` the executed variances remain strictly ordered
`var_ρ3 < var_ζ`. The height-ridge clause is not rounder than ρ3.

### N8 — cross-cycle echo

The investment that ρ3 is rounder than μ is not reused as a lemma. The
three scores, including the first display of ζ variance, are computed on
`B_12(0)`. L1 remains unattached.

**Gate disposition:** PASS for the three reported variances, the displayed
lex-first minimizer ρ3, and the refusal to adopt a hop-cost or attach L1.
FAIL / DO NOT SHIP for writing ζ, ρ3, or μ into Admissibility, attaching
L1, or claiming a unique physical law.

## Primary Runner

The primary runner rebuilds `B_12(0)`, runs the three Dijkstras, recomputes
the second moments and population variances, checks the reported order and
lex-first minimizer, and pins the current axiom wording together with the
non-adoption sentences. It authors no audit verdict.
