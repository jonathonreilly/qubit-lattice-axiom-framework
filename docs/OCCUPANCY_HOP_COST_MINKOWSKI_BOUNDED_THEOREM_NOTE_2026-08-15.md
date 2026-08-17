---
claim_id: occupancy_hop_cost_minkowski_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On B_3(0), whether G+-equivariant occupancy-dependent hop costs can match Minkowski better than ℓ¹ is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/occupancy_hop_cost_minkowski_2026_08_15.py
---

# Occupancy-Only Hop Costs Stay Diamond On The Radius-3 Ball

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact one-seed front on `B_3(0)` whose 6-NN hop cost may depend on
the occupancy of the arrival site, restricted to `G+`-equivariant maps
`c:{0,1}^6→{1,2}`. Displayed comparison to the Minkowski sample
`x^2+y^2+z^2 = c t^2`. No physical clock, boost, or Wick map is selected.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/occupancy_hop_cost_minkowski_2026_08_15.py`](../scripts/occupancy_hop_cost_minkowski_2026_08_15.py)

## Result Up Front

Lattice names nearest-neighbor adjacency on `Z^3` and proper cubic rotations
about each site. Admissibility says the local rule is determined by
nearest-neighbor conditions. A leftover after constant cube-covariant hop
costs is therefore still NN-determined: the cost of a hop into `v` may depend
on the 6-bit occupancy `σ` of `N(v)`.

Grow a one-seed front from the origin on the induced graph of the integer
ball `B_3(0)={v∈Z^3 : |v|_1 ≤ 3}`. Arrival time is the first time the front
reaches a site; each hop into `v` costs `c(σ)∈{1,2}`, where `σ` is read from
already-arrived neighbors of `v`. The map `c` is required to be
`G+`-equivariant.

For constant `c=1` the front is ordinary graph distance, so isochrones are
`ℓ¹` spheres. On the sphere `|v|_1=3` the 6 axis sites have `|v|_2^2=9` and
the 8 body-diagonal sites have `|v|_2^2=3`. The Minkowski sample
`|v|_2^2 = c t^2` would require those two classes to share a common ratio
`t^2/|v|_2^2`. They do not: both arrive at `t=3`, so the ratios are `1` and
`3`.

Every `G+`-equivariant `c:{0,1}^6→{1,2}` is scored, including every cost that
depends only on the weight of `σ` and every cost that depends only on whether
the arrival axis is already occupied. In all `1024` equivariant maps the axis
tips still arrive no later, per Euclidean radius, than the body-diagonal
tips: `t(3,0,0)^2 / 9 ≤ t(1,1,1)^2 / 3`. No map reverses that order. Therefore
occupancy-only hop costs stay diamond.

The comparison is displayed, not adopted. Do not write a cost into
Admissibility. Do not attach a named arrival kernel.

## Current Premise Boundary

The Lattice and Admissibility premises are quoted from
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md):

Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
adjacency, standard translations, and proper cubic rotations about each site.

There is one fixed nearest-neighbor admissibility rule, covariant under lattice
translations and proper cubic rotations.

For each site, the probability distribution over the possibilities is
determined by, and varies with, the nearest-neighbor conditions.

Those sentences supply the six-neighbor graph, the proper-cube covariance, and
the license to let a displayed hop cost depend on nearest-neighbor occupancy.
They do not name a hop-cost, a first-arrival clock, a null cone, a boost, or a
Wick map. This note does not edit them.

Record is unused. The current Record boundary remains:

When present, a record locks exactly one admissible local possibility.

A readout value is determined by record content alone.

A site with no record cannot be read.

The scored domain is only `B_3(0)`. No larger ball is grown.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Constant-c=1 ell^1 isochrones, the axis/body Euclidean mismatch at ell^1=3, and the 1024-map G+ occupancy census on B_3(0) are finite exact statements. Minkowski light is a displayed comparator, not an adopted law."
trace_class: negative_route_pruning
target_claim_id: occupancy_hop_cost_minkowski
target_blocker_text: "score whether G+-equivariant occupancy-dependent 6-NN hop-costs on a one-seed B_3(0) front can match a Minkowski sample better than ell^1"
source_of_blocker_text: handoff
reachability_to_target: prunes
artifact_role: theorem
next_trace_action: "Do not attach a named arrival kernel; a later route that wants isotropic c must change the hop set, drop G+ equivariance, enlarge the cost alphabet, or add structure that is not occupancy-only on B_3(0)."
conditional_surface_status: "exact for G+-equivariant occupancy hop-costs in {1,2} on the induced B_3(0) one-seed front; no adopted clock or axiom edit"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

Write `e_1=(1,0,0)`, `e_2=(0,1,0)`, `e_3=(0,0,1)`, and

`A = {±e_1, ±e_2, ±e_3}`.

A proper cube matrix is a `3×3` monomial signed-permutation matrix with
exactly one nonzero entry `±1` in each row and column and determinant `+1`.
The proper cube group `G+` is the set of all such matrices. It has order `24`
and acts on occupancy configurations `σ∈{0,1}^A` by permuting the six
neighbor slots.

The comparison domain is

`B_3(0) = {v∈Z^3 : |v|_1 ≤ 3}`.

It has `63` sites. The induced 6-NN graph is used; sites with `|v|_1=4` are
never occupied. The seed is the origin. Occupancy of an arrival site `v` is
the 6-bit pattern of which neighbors in `A` have already arrived. A hop into
`v` costs `c(σ)∈{1,2}`. First arrival is the one-seed front time, which is the
minimum path cost among paths whose hop costs are evaluated against the
already-arrived set.

`G+`-equivariance means `c(gσ)=c(σ)` for every `g∈G+`. The action has ten
orbits on `{0,1}^6`, so there are `2^{10}=1024` equivariant maps to `{1,2}`.
Two named subfamilies are included in that census:

- weight-only maps, `c(σ)=f(|σ|)`;
- arrival-axis maps, `c` depending on whether the far neighbor along the
  incoming hop is already occupied.

The taxicab and Euclidean quadratic forms are the displayed comparators

`|v|_1 = |v_1|+|v_2|+|v_3|`,

`|v|_2^2 = v_1^2+v_2^2+v_3^2`.

The Minkowski sample is the displayed relation `|v|_2^2 = c t^2`, or
equivalently constancy of `t^2/|v|_2^2` on a nonzero sample.

## Theorem 1 — Constant Cost Recovers ℓ¹ Isochrones

If `c` is the constant function `1`, every hop costs `1`. The one-seed front
on the induced ball is ordinary graph distance, so

`t(v)=|v|_1`

on `B_3(0)`. Isochrones are `ℓ¹` spheres.

On the sphere `|v|_1=3` there are `6` axis sites `(±3,0,0)` and permutations,
each with `|v|_2^2=9`, and `8` body-diagonal sites `(±1,±1,±1)`, each with
`|v|_2^2=3`. All fourteen sites arrive at `t=3`. The displayed ratios are

`t(3,0,0)^2 / 9 = 1`, `t(1,1,1)^2 / 3 = 3`.

That is the `ℓ¹` versus Euclidean mismatch on this sample. It is not a
leftover of a constant direction-only hop cost: the same numbers appear here
as the occupancy-independent baseline against which occupancy-dependent maps
are scored.

## Theorem 2 — Occupancy-Only Maps Stay Diamond

Let `c:{0,1}^6→{1,2}` be `G+`-equivariant. Grow the one-seed front on
`B_3(0)` and write `t_axis=t(3,0,0)` and `t_body=t(1,1,1)`. Cube covariance
forces these values to be constant on the `6` axis tips and on the `8` body
tips respectively.

The Euclidean-radius comparison is the exact integer inequality

`t_axis^2 · 3 ≤ t_body^2 · 9`,

which says that the axis sites still arrive no later than the body diagonals
at the same Euclidean radius (smaller or equal `t^2/|v|_2^2`).

The `1024` maps produce only the six ordered pairs

`(t_axis,t_body) ∈ {(3,3),(3,4),(3,5),(6,4),(6,5),(6,6)}`.

Each pair satisfies the inequality. The first reversing map in lexicographic
orbit order does not exist. Weight-only maps produce the same six pairs.
Arrival-axis maps produce only `(3,3)` and `(6,6)`.

On the induced ball the unique in-ball neighbor of `(3,0,0)` is `(2,0,0)`, so
every axis-tip hop has weight `1` and `t_axis=3 c(wt=1)`. Body-diagonal sites
can see up to three already-arrived face-adjacent neighbors, so occupancy can
split the raw times. Even the most body-favoring pair `(6,4)` still has

`6^2 / 9 = 4 < 16/3 = 4^2 / 3`.

Axes remain the fast Euclidean directions. Therefore occupancy-only hop costs
stay diamond.

## Theorem 3 — Displayed, Not Adopted

The Minkowski sample and the occupancy hop-cost are displayed comparison
objects. They are not written into Lattice or Admissibility. No cost law is
adopted. No arrival kernel is attached. A Wick map is not selected.

Displayed, not adopted. Do not write a cost into Admissibility.

## Exact Target And Obligation Graph

| Obligation | Disposition |
|---|---|
| quote current Lattice nearest-neighbor and proper-cube wording | source-bound |
| quote current Admissibility covariance and NN-condition wording | source-bound |
| enumerate `G+` and the ten occupancy orbits | closed by finite listing |
| constant `c=1` recovers `t=|v|_1` on `B_3(0)` | closed by the one-seed front |
| report the `|v|_1=3` axis/body Euclidean mismatch | closed: `|v|_2^2=9` versus `|v|_2^2=3` |
| census every `G+`-equivariant `c` to `{1,2}` | closed: `1024` maps, six pairs |
| axis still no later per Euclidean radius, or name the first reversal | closed: no reversal |
| write a cost into Admissibility | outside the claim |
| attach a named arrival kernel | outside the claim |
| edit Lattice or Admissibility | `hypothetical_axiom_status: no edit` |

The obligation graph is acyclic. Every leaf of the bounded comparison is
closed. Adoption of a physical light law is not a proof leaf because it is
expressly not part of the target.

## Imports And Non-Claims

Only the current axiom memo is imported. Occupancy is the one-seed arrived
set on the induced `B_3(0)` graph, not a new spatial patch and not a Record
content map. The Minkowski sample is a displayed comparator on that finite
ball.

The theorem does not say that isotropic light is impossible in every later
construction. It says that `G+`-equivariant occupancy-dependent hop-costs
with values in `{1,2}` on this one-seed front stay diamond.

## Value Gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It isolates occupancy dependence of a still-NN hop cost as the leftover after constant cube-covariant costs, and scores it on `B_3(0)`. |
| V2 | Current main names nearest-neighbor conditions but does not score occupancy hop-costs against the displayed Minkowski sample. |
| V3 | Group order, orbit count, the `63`-site ball, and the `1024`-map census are independently finite and exact. |
| V4 | The result is more than a restatement of constant hop-costs because occupancy is allowed to vary with the arrival 6-tuple. |
| V5 | The comparisons remain displayed; the note does not install Minkowski structure or a clock. |

## No-Go Discipline Gate

The negative claim is restricted to `G+`-equivariant occupancy hop-costs in
`{1,2}` on the one-seed front in `B_3(0)`, and to the displayed Minkowski
sample on the `ℓ¹=3` axis/body sites. No global impossibility of isotropic
light is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| constant occupancy-blind cost | `c=1` | executed; `t=|v|_1`; mismatch `1` versus `3` |
| weight-only occupancy cost | `c=f(|σ|)` in `{1,2}` | executed; six pairs; diamond order holds |
| arrival-axis occupancy cost | cost from the far-axis bit | executed; pairs `(3,3)` and `(6,6)` only |
| every `G+`-equivariant `c` | `1024` maps `{0,1}^6→{1,2}` | executed; no Euclidean-radius reversal |
| drop `G+` equivariance | unequal costs on one orbit | lives only after dropping cube covariance |
| larger hop set | add face diagonals or longer steps | different member; not 6-NN |
| enlarge the cost alphabet | values outside `{1,2}` | different object; not scored |
| write a cost into Admissibility | enlarge the axiom | forbidden; `no edit` |

### N2 — wall independence

Cube covariance, the six-neighbor hop set, the `{1,2}` occupancy cost type,
the one-seed front, and the displayed Minkowski sample are distinct inputs.
The note claims no complete wall collection beyond this scored class.

### N3 — hidden-condition scan

The hop set, the group `G+`, occupancy of already-arrived neighbors, the
induced `B_3(0)` domain, layer-synchronous front arrival, and the
Euclidean-radius predicate are declared. A Wick map, a boost, and an axiom
edit are not silently assumed.

### N4 — source residual matching

The current axiom memo supplies nearest-neighbor adjacency, proper cubic
rotations, and an Admissibility rule determined by nearest-neighbor
conditions. It does not name Minkowski light. The residual scored here is
occupancy dependence of an NN hop-cost, not leftover constancy of a
direction-only member.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | ten occupancy orbits and the named axis/body tips | no continuum spacetime classification |
| per site | one-seed front arrival on `B_3(0)` | no Record content map |
| per mode | no mode calculation | no spectral exhaustion |
| per block | `B_3(0)` only | no larger spatial patch |
| lattice wide | checked and not executed | no global light-law derivation |

### N6 — live partial-closure paths

A later construction may change the hop set, drop cube covariance, enlarge
the cost alphabet, or add structure that is not an occupancy-only 6-NN hop
cost on `B_3(0)`. Those are different objects. They are not scored here and
are not filled by writing a cost into Admissibility.

### N7 — hostile steelman

**Steelman:** Making singleton hops expensive and crowded arrivals cheap
should fill body diagonals first and restore a Euclidean sphere.

**Answer:** That law is included. It produces `(t_axis,t_body)=(6,4)`, which
splits the raw `|v|_1=3` sphere. The Euclidean-radius order still holds,
`4 < 16/3`, so axes remain faster per Euclidean radius. Occupancy-only hop
costs stay diamond.

### N8 — cross-cycle echo

This note does not attach a named arrival kernel and does not treat the
comparison as leftover character of a constant direction-only hop-cost. It
scores occupancy dependence on the arrival 6-tuple, which that constant-cost
census did not run.

**Gate disposition:** PASS for constant-`c=1` `ℓ¹` isochrones, the
`|v|_1=3` Euclidean mismatch, and the occupancy census with no
Euclidean-radius reversal. FAIL / DO NOT SHIP for “Minkowski is adopted,”
“Admissibility now contains a hop-cost,” “a Wick map is selected,” or
“occupancy-only costs match the Minkowski sample better than `ℓ¹`.”

## Primary Runner

The primary runner enumerates `G+` and the occupancy orbits, grows the
one-seed front on `B_3(0)` for every equivariant cost, checks the constant-`c`
isochrones and the axis/body mismatch, and confirms that no scored map
reverses the Euclidean-radius diamond order. It authors no audit verdict.
