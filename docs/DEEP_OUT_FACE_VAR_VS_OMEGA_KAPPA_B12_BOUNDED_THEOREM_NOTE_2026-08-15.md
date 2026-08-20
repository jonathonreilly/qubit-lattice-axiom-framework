---
claim_id: deep_out_face_var_vs_omega_kappa_b12_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Arrival-speed variance under deep-out-face, out-face, and ridge-enter on B_12(0) is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/deep_out_face_var_vs_omega_kappa_b12_2026_08_15.py
---

# Named Deep-Out-Face Versus ω Versus κ Arrival-Speed Variance On B_12(0)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** three named directed nearest-neighbor hop-costs on the finite
ℓ¹-ball `B_12(0)`, their Dijkstra arrival times from the origin, and the
population variance of `|v|_2/t` on the 2624 nonzero sites. No hop-cost is
written into Admissibility. L1 is not attached.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/deep_out_face_var_vs_omega_kappa_b12_2026_08_15.py`](../scripts/deep_out_face_var_vs_omega_kappa_b12_2026_08_15.py)
**Cache:** none. `cache_write: false`.

## Result Up Front

The named deep-out-face hop-cost `df` is the already scored ridge-slide
rule `ρ3` plus cost `3` on those `2→2` hops whose destination has a
strictly larger max absolute coordinate than the source and whose source
max absolute coordinate is at least `2`. That extra clause skips the
unit-out-face hop, for example `(1,1,0)→(2,1,0)`, and still fires on
`(2,2,0)→(3,2,0)`. The named out-face hop-cost `ω` is `ρ3` plus cost `3`
on those `2→2` hops whose destination has a strictly larger max absolute
coordinate than the source, including the unit-out-face hop. The named
ridge-enter hop-cost `κ` is `ρ3` plus cost `3` on those `2→3` hops whose
destination has exactly two absolute coordinates equal to `1`. The
investment is that `df` skips unit-out-face. The residual here is the
first display of arrival-speed variance of `df` versus `ω` and `κ` on
`B_12(0)`. Uniqueness is not claimed.

On the induced nearest-neighbor graph of `B_12(0)` the unit-out-face skip
is already priced by the corridor-slide clause of `ρ3`. Every cubic
`2→2` hop that grows the box max from a source of max `1` still has a
destination coordinate of absolute value `1`, so it is already cost `3`
under `ρ3`, under `ω`, and under `df`. Therefore `df` and `ω` agree on
every induced hop of `B_12(0)`.

The executed order of arrival-speed variances on `B_12(0)` is

`var_df = var_ω < var_κ`.

So `df` ties `ω` and both are strictly rounder than `κ` on `B_12(0)`.
The lex-first minimizer among the three displayed names is `df`. The
scores are displayed, not adopted. Do not write `df`, `ω`, or `κ` into
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
target_claim_id: deep_out_face_var_vs_omega_kappa_b12
target_blocker_text: "report arrival-speed variance of df, ω, and κ on B_12(0)"
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Keep the three scores displayed. Do not write df, ω, or κ into Admissibility. Do not attach L1."
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
- ridge-enter means `|σ_v|=2` and `|σ_w|=3` and exactly two `|w_i|` equal `1`,
- out-face means `|σ_v|=|σ_w|=2` and `max_i |w_i| > max_i |v_i|`,
- deep-out-face means `|σ_v|=|σ_w|=2` and `max_i |w_i| > max_i |v_i|` and
  `max_i |v_i| ≥ 2`.

The three named costs are:

- `df`: cost `3` if `ρ3` would be `3` or deep-out-face, else `1`. Written
  `df(v→w) = 3` if `|σ_v|=0` or `(|σ_v|=|σ_w|=1)` or `|σ_w| < |σ_v|` or
  `(|σ_v|=|σ_w|=2` and the least nonzero `|w_i|` equals `1)` or
  `(|σ_v|=|σ_w|=3` and exactly two `|w_i|` equal `1)` or
  `(|σ_v|=|σ_w|=2` and `max_i |w_i| > max_i |v_i|` and `max_i |v_i| ≥ 2)`,
  else `1`.
- `ω`: cost `3` if `ρ3` would be `3` or out-face, else `1`. Written
  `ω(v→w) = 3` if `|σ_v|=0` or `(|σ_v|=|σ_w|=1)` or `|σ_w| < |σ_v|` or
  `(|σ_v|=|σ_w|=2` and the least nonzero `|w_i|` equals `1)` or
  `(|σ_v|=|σ_w|=3` and exactly two `|w_i|` equal `1)` or
  `(|σ_v|=|σ_w|=2` and `max_i |w_i| > max_i |v_i|)`, else `1`.
- `κ`: cost `3` if `ρ3` would be `3` or ridge-enter, else `1`. Written
  `κ(v→w) = 3` if `|σ_v|=0` or `(|σ_v|=|σ_w|=1)` or `|σ_w| < |σ_v|` or
  `(|σ_v|=|σ_w|=2` and the least nonzero `|w_i|` equals `1)` or
  `(|σ_v|=|σ_w|=3` and exactly two `|w_i|` equal `1)` or
  `(|σ_v|=2` and `|σ_w|=3` and exactly two `|w_i|` equal `1)`, else `1`.

On the deep-out-face hop `(2,2,0) → (3,2,0)` one has `|σ| : 2 → 2` and
`max |w_i| = 3 > max |v_i| = 2 ≥ 2`, so `κ = 1` while `df = ω = 3`. On
the ridge-enter hop `(2,1,0) → (2,1,1)` one has `|σ| : 2 → 3` and exactly
two `|w_i| = 1`, so `df = ω = 1` while `κ = 3`. On the ridge hop
`(1,1,1) → (2,1,1)` one has `|σ| : 3 → 3` and exactly two `|w_i| = 1`,
so all three names cost `3`. On the axis-hugging unit-out-face hop
`(1,1,0) → (2,1,0)` one has `|σ| : 2 → 2`, least nonzero `|w_i| = 1`,
and a growing max from source max `1`, so the extra deep-out-face clause
does not fire, the extra out-face clause would fire if `ρ3` did not, and
`ρ3` already costs `3`; therefore all three names cost `3`. The
three-unit enter hop `(1,1,0) → (1,1,1)` stays at cost `1` under all
three names. The leave-axis hop `(0,-1,0) → (1,-1,0)` stays at cost `1`
under all three names. Therefore neither `ω` nor `κ` prices a hop that
`df` leaves cheap on this graph: the skip of unit-out-face is already
absorbed by corridor-slide.

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

`Q_df = 2697928722329275408991/14234892042902154624000`,

`Q_ω = 2697928722329275408991/14234892042902154624000`,

`Q_κ = 8065845471432407489/37031456927424960000`.

The population variances, truncated to 18 decimal digits, are

`var_df = 0.004242786759120176`,

`var_ω = 0.004242786759120176`,

`var_κ = 0.005030477616848010`.

Thus all three variances are reported. The deep-out-face rule `df` ties
the out-face rule `ω` on `B_12(0)`, and both remain strictly rounder
than `κ`.

## Theorem 2 — Lex-First Minimizer

Order the three names as the strings `df`, `kappa`, and `omega`. The
variance-minimizing scores among those three are `df` and `ω`, which
are equal. The lexicographically earlier of those two names is `df`.
Therefore the lex-first minimizer among the three is `df`. Uniqueness
among hop-costs outside this triple is not required and is not claimed.

The minimizer is displayed, not adopted.

## Theorem 3 — No Admissibility Write, L1 Not Attached

Do not write `df`, `ω`, or `κ` into Admissibility. The current admissibility
rule remains the quoted nearest-neighbor distribution constraint. The three
clause families are scoring rules on `B_12(0)`, not a replacement of that
axiom.

Do not attach L1. No formation law, occupancy member, or locked-set filling
rule is identified with any of the three hop-costs.

## Promotion Value Gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers whether df is rounder or worse than ω and κ on B_12(0). |
| V2 | Current main has no landed df/ω/κ variance report on B_12(0). |
| V3 | The three Dijkstras and the 2624-site population variances are finite and exact. |
| V4 | The comparison is not an axiom rewrite: Admissibility is left unchanged. |
| V5 | Displayed scores are not a physical hop-cost or formation law. |

## No-Go Discipline Gate

The negative content is narrow: these three scores are reported on `B_12(0)`
and are not adopted. No uniqueness of a physical law is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| `df` | all `ρ3` clauses plus deep-out-face `2→2` hops expensive | executed; lex-first variance minimizer; ties `ω` |
| `ω` | all `ρ3` clauses plus out-face `2→2` hops expensive | executed; identical arrival field to `df` on this graph |
| `κ` | all `ρ3` clauses plus ridge-enter `2→3` hops expensive | executed; strictly larger variance |
| other clause triples | drop the deep-out-face family or tax every `2→2` | different named family; not this residual |
| unrestricted `Z^3` paths | leave `B_12(0)` and return | outside the declared ball |
| adopt a score | write `df`, `ω`, or `κ` into Admissibility | forbidden; not executed |
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

**Steelman:** Skipping the unit-out-face hop should split `df` from `ω`
and stretch or compress the arrival-speed field relative to `ω` on
`B_12(0)`.

**Answer:** On cubic nearest-neighbor hops the unit-out-face `2→2` already
has a destination coordinate of absolute value `1`, so corridor-slide
already prices it at `3`. The skip is vacuous on the induced graph of
`B_12(0)`. The executed variances satisfy `var_df = var_ω < var_κ`.

### N8 — cross-cycle echo

The deep-out-face same-`k` scores and the out-face and ridge-enter
variance scores are not reused as lemmas. The three scores are computed
on `B_12(0)`. L1 remains unattached.

**Gate disposition:** PASS for the three reported variances, the displayed
lex-first minimizer `df`, and the refusal to adopt a hop-cost or attach L1.
FAIL / DO NOT SHIP for writing `df`, `ω`, or `κ` into Admissibility,
attaching L1, or claiming a unique physical law.

## Primary Runner

The primary runner rebuilds `B_12(0)`, runs the three Dijkstras, recomputes
the second moments and population variances, checks the reported order and
lex-first minimizer, and pins the current axiom wording together with the
non-adoption sentences. It authors no audit verdict.
