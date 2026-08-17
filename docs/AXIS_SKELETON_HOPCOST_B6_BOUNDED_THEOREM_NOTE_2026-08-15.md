---
claim_id: axis_skeleton_hopcost_b6_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On B_6(0), the named axis-skeleton hop-cost is scored for diamond reverse at (4,0,0) vs (2,2,2) and for var(|v|_2/t) vs ℓ¹. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/axis_skeleton_hopcost_b6_2026_08_15.py
---

# Named Axis-Skeleton Hop-Cost On B_6(0)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** one finite Dijkstra score of a named hop-cost on the closed
nearest-neighbor graph ball `B_6(0)` in `Z^3`. The score is displayed, not
adopted. Uniqueness is not claimed. This note does not attach L1.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/axis_skeleton_hopcost_b6_2026_08_15.py`](../scripts/axis_skeleton_hopcost_b6_2026_08_15.py)

## Result Up Front

On the cubic lattice, write `|σ_v|` for the number of nonzero coordinates of
`v∈Z^3`. The named hop-cost `α` on a nearest-neighbor step `v→w` is

```text
α(v→w) = 3  if |σ_v|=0 or (|σ_v|=|σ_w|=1),
α(v→w) = 1  otherwise.
```

The first clause is the seed exit from the origin. The second clause is the
axis 1-skeleton: both endpoints have weight one. Every other nearest-neighbor
step is cheap. Axis-extension hops therefore stay expensive as hops, while
face and body steps that leave that 1-skeleton are cheap.

Let `B_6(0):={v∈Z^3 : |v|_1 ≤ 6}` be the closed graph ball of radius 6 for
the nearest-neighbor path metric. Let `t(v)` be the `α`-length of a shortest
path from the origin inside this ball, computed by one Dijkstra run. Let
`ℓ¹` be the comparison hop-cost that assigns every nearest-neighbor step the
value `1`, so its arrival time is `|v|_1`.

**Theorem 1.** `t(4,0,0)=8` and `t(2,2,2)=8`. The diamond-reverse test
`12 t(4,0,0)^2 > 16 t(2,2,2)^2` is `768 > 1024`, which is false. The named
rule does not reverse `(4,0,0)` against `(2,2,2)`.

**Theorem 2.** On the 376 nonzero sites of `B_6(0)`, the population variances
of `|v|_2/t` are

```text
var_α = 0.005489876321,
var_ℓ¹ = 0.013502037619.
```

The `α` variance is smaller.

**Theorem 3.** The named rule is displayed, not adopted. It is not written
into Admissibility. Uniqueness is not required and is not claimed.

The rule is not a leftover of the 27 three-slot family (including the
investment rule with no reverse): that family cannot split the face targets
`(1,1,0)` and `(2,2,0)`. Here `t(1,1,0)=4` and `t(2,2,0)=6`.

## Current Premise Boundary

The Lattice and Admissibility premises are quoted from
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md):

Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
adjacency, standard translations, and proper cubic rotations about each site.

There is one fixed nearest-neighbor admissibility rule, covariant under lattice
translations and proper cubic rotations.

For each site, the probability distribution over the possibilities is
determined by, and varies with, the nearest-neighbor conditions.

`α` is not that admissibility rule. The axiom already says there is one fixed
nearest-neighbor admissibility rule. This note does not edit that sentence and
does not add a hop-cost to Admissibility.

The current Record boundary is unused by the score:

When present, a record locks exactly one admissible local possibility.

A readout value is determined by record content alone.

A site with no record cannot be read.

Record supplies no hop-cost, no arrival time, and no Euclidean comparator.

## Machine Status And Trace

```yaml
actual_current_surface_status: displayed
target_claim_type: bounded_theorem
claim_type_reason: "One Dijkstra score of a named hop-cost on B_6(0) for diamond reverse and for population variance of |v|_2/t against ℓ¹. Displayed, not adopted."
trace_class: residual_score
target_claim_id: axis_skeleton_hopcost_b6_bounded_theorem_note_2026-08-15
target_blocker_text: "score the named axis-skeleton hop-cost on B_6(0) for reverse and for variance against ℓ¹"
source_of_blocker_text: handoff
reachability_to_target: scores
artifact_role: theorem
next_trace_action: "Keep α displayed only; do not write it into Admissibility and do not attach L1."
conditional_surface_status: "exact finite score on B_6(0); not adopted"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

Write `0=(0,0,0)` and `e_1,e_2,e_3` for the standard basis of `Z^3`. The open
neighbor set is `N(v)={v±e_1,v±e_2,v±e_3}`. A directed hop is a pair
`(v,w)` with `w∈N(v)` and with both endpoints in `B_6(0)`.

The weight `|σ_v|` is the number of nonzero Cartesian coordinates. Then:

- seed exit: `α(0,e_i)=3` and `α(0,-e_i)=3`;
- axis 1-skeleton: if `|σ_v|=|σ_w|=1`, then `α(v,w)=3`;
- otherwise `α(v,w)=1`.

In particular the axis-extension hops `(n e_i)→((n+1)e_i)` for `n≥1` cost `3`,
while `(e_1)→(e_1+e_2)`, `(e_1+e_2)→(2e_1+e_2)`, and
`(e_1+e_2)→(e_1+e_2+e_3)` each cost `1`. That is the intended cheapening of
`(2,2)` and `(3,3)` face targets without cheapening axis-extension hops.

`t` is the arrival time of one Dijkstra tree for `α` rooted at the origin on
the directed graph just named. The comparison arrival time for `ℓ¹` is
`|v|_1`; on this ball every `ℓ¹` geodesic stays inside, so no second search
is required.

## Theorem 1

The Dijkstra values are `t(4,0,0)=8` and `t(2,2,2)=8`.

An explicit body path of `α`-length `8` is

```text
0 → e_1 → e_1+e_2 → e_1+e_2+e_3 → 2e_1+e_2+e_3 → 2e_1+2e_2+e_3 → 2e_1+2e_2+2e_3
```

with costs `3,1,1,1,1,1`. Any path to `(2,2,2)` has at least six hops and
begins with a seed exit of cost `3`, so `8` is also a lower bound.

An explicit path of `α`-length `8` to `(4,0,0)` is

```text
0 → e_1 → e_1+e_2 → 2e_1+e_2 → 3e_1+e_2 → 4e_1+e_2 → 4e_1
```

with costs `3,1,1,1,1,1`. The direct axis path costs `12`. The off-axis
detour is legal in `B_6(0)` because `(4,1,0)` has ℓ¹-norm `5`. Thus the
shortest-path value `t(4,0,0)` is cheaper than the axis-extension path even
though every axis-extension *hop* still costs `3`.

The diamond test is then `12·8^2=768` against `16·8^2=1024`. Reverse fails.

## Theorem 2

Let `S=B_6(0)\{0}`, so `|S|=376`. The population variance is

```text
var(x) = (1/|S|) ∑_{v∈S} (x(v) - mean(x))^2.
```

The runner evaluates `x_α(v)=|v|_2/t(v)` and `x_ℓ¹(v)=|v|_2/|v|_1` in one
pass over the Dijkstra tree and reports

```text
var_α = 0.005489876321,
var_ℓ¹ = 0.013502037619.
```

So `var_α < var_ℓ¹`. The score is only this finite comparison on `B_6(0)`.

## Theorem 3

`α` is a named displayed hop-cost. It is not adopted as a physical law and is
not written into Admissibility. The axiom text still contains exactly one
fixed nearest-neighbor admissibility rule, and that sentence is unchanged.

Uniqueness is not required. The note does not claim that `α` is the only
hop-cost with a smaller Euclidean-ratio variance than `ℓ¹`, nor that it is
the only hop-cost that splits `(1,1,0)` from `(2,2,0)`.

This note does not attach L1.

## Relation To The 27 Three-Slot Family

A prior 27-member three-slot family, including the investment rule with no
reverse, cannot split `(1,1)` from `(2,2)`. The present named rule is
therefore not a leftover of that family: it marks as expensive only the seed
exit and the axis 1-skeleton, so the two-hop face target `(1,1,0)` and the
four-hop face target `(2,2,0)` receive different arrival times `4` and `6`.
Direct all-expensive accounting would have given `6` and `12`. The same
cheapening produces `t(3,3,0)=8` rather than `18`.

The investment comparison that assigned cost `3` to every seed or equal-weight
hop made a geodesic to `(2,2,2)` use two cheap unequal hops and four expensive
seed or equal hops, for total `14`. Replacing equal-weight expense by
axis-skeleton expense is exactly the change from that comparison to `α`.

## Exact Target And Obligation Graph

| Obligation | Status |
|---|---|
| current Lattice nearest-neighbor graph | quoted; no edit |
| current Admissibility rule | quoted; `α` not written into it |
| current Record boundary | quoted as unused |
| named hop-cost `α` | displayed definition |
| one Dijkstra on `B_6(0)` | executed |
| `t(4,0,0)` and `t(2,2,2)` | exact integers `8,8` |
| diamond reverse `12 t(4,0,0)^2 > 16 t(2,2,2)^2` | false |
| population variance of `|v|_2/t` versus `ℓ¹` | `α` smaller |
| split of `(1,1,0)` from `(2,2,0)` | exact `4` versus `6` |
| uniqueness | not claimed |
| adoption into Admissibility | refused |
| L1 attachment | refused |

The obligation graph is acyclic. Every scored leaf is a finite statement on
`B_6(0)`. Adoption and uniqueness are not proof leaves.

## Boundary And Imports

There are no measured, fitted, literature, or observational inputs. The only
scientific source is the current axiom memo for the cubic nearest-neighbor
graph and the explicit non-adoption of `α` as axiom content.

The score does not select a physical clock, a continuum limit, a Record
readout, a formation rate, or a Newton-lane residual. It does not enlarge
Admissibility.

## Promotion Value Gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It scores one named hop-cost on a declared finite ball for reverse and for variance against `ℓ¹`. |
| V2 | Current main has no landed score of this axis-skeleton rule on `B_6(0)`. |
| V3 | Arrival times are exact integers; the variance comparison is a finite population statistic. |
| V4 | The rule is not a restatement of Admissibility and is not written into it. |
| V5 | Displayed, not adopted. |

## No-Go Discipline Gate

The negative content is narrow: this named rule does not reverse
`(4,0,0)` against `(2,2,2)` on `B_6(0)`. No global hop-cost impossibility is
claimed. Uniqueness is not required.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| direct axis path | use only weight-one hops | cost `12` to `(4,0,0)`; not shortest |
| off-axis detour | leave and rejoin the axis inside `B_6(0)` | shortest `t(4,0,0)=8` |
| body geodesic | six hops, one seed exit, then cheap | shortest `t(2,2,2)=8` |
| `ℓ¹` comparison | unit hops | larger population variance |
| 27 three-slot leftovers | reuse a rule that cannot split `(1,1)` from `(2,2)` | different family; not this rule |
| write `α` into Admissibility | adopt the hop-cost as the axiom rule | refused |
| attach L1 | promote the score as a Newton residual | refused |
