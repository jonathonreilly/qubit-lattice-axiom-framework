---
claim_id: no_shortcut_support_drop_hopcost_b4_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On B_4(0), the named support-drop hop-cost is scored for small-ball reverse and for variance vs ℓ¹. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/no_shortcut_support_drop_hopcost_b4_2026_08_15.py
---

# Support-Drop Hop-Cost On B_4(0): Small-Ball Reverse And Variance Versus ℓ¹

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact first-arrival times under the named support-drop hop-cost on
the closed ℓ¹ ball `B_4(0)`, the small-ball reverse test at `(3,0,0)` versus
`(1,1,1)`, and the population variance of `|v|_2/t` on `B_4(0)\{0}` versus
unit ℓ¹ arrival. No occupancy step is run. No hop-cost is written into
Admissibility. The comparison is displayed, not adopted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/no_shortcut_support_drop_hopcost_b4_2026_08_15.py`](../scripts/no_shortcut_support_drop_hopcost_b4_2026_08_15.py)

## Result Up Front

Lattice names nearest-neighbor adjacency on `Z^3` and proper cubic rotations
about each site. Write `σ_v` for the set of nonzero coordinates of `v∈Z^3`
and `|σ_v|` for its cardinality. The named support-drop hop-cost on an
oriented nearest-neighbor step `v→w` is the positive integer

`ν(v→w) = 3` if `|σ_v|=0` or `(|σ_v|=|σ_w|=1)` or `|σ_w|<|σ_v|`, else `1`.

That is a local function of the two endpoint weights. Seed exit, the axis
1-skeleton, and every support-decreasing step cost `3`. Support-increasing
and same-weight off-axis steps cost `1`. First arrival `t(v)` is shortest-path
cost from the origin through `B_4(0)` only. The rule is scored independently
on this ball. An arrival table from a larger ball is not imported.

On `B_4(0)` the arrivals are

`t(3,0,0)=9`, `t(1,1,1)=5`, `t(4,0,0)=12`.

The small-ball reverse test is the displayed comparison

`3 t(3,0,0)^2 > 9 t(1,1,1)^2`,

equivalently `t(3,0,0)^2/|(3,0,0)|_2^2 > t(1,1,1)^2/|(1,1,1)|_2^2`. It holds:
`3·81=243` and `9·25=225`. The same pair under unit ℓ¹ arrival `t=|v|_1`
gives `27` versus `81` and does not reverse.

Population variance of `|v|_2/t` on the `128` nonzero sites of `B_4(0)` is

`var_ν = 0.004721240258`, `var_{ℓ¹} = 0.017710351242`.

The named rule has the smaller variance. Displayed, not adopted. Do not write `ν` into Admissibility. Do not attach ℓ¹.

## Current Premise Boundary

The Lattice and Admissibility premises are quoted from
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md):

Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
adjacency, standard translations, and proper cubic rotations about each site.

There is one fixed nearest-neighbor admissibility rule, covariant under lattice
translations and proper cubic rotations.

For each site, the probability distribution over the possibilities is
determined by, and varies with, the nearest-neighbor conditions.

Those sentences supply the six-neighbor graph and the proper-cube covariance
used to name a hop-cost. They do not name `ν`, a first-arrival clock, a
variance score, or a reverse test. This note does not edit them.

Record is unused. The current Record boundary remains:

When present, a record locks exactly one admissible local possibility.

A readout value is determined by record content alone.

A site with no record cannot be read.

No occupancy is grown on a new patch. The ball `B_4(0)` is an enumeration
domain for an already-named local hop-cost, not a new spatial construction.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "First arrivals under the named support-drop hop-cost on the 129-site ball B_4(0), the small-ball reverse inequality at (3,0,0) versus (1,1,1), and the two population variances of |v|_2/t are finite exact statements. The rule is displayed, not adopted."
trace_class: negative_route_pruning
target_claim_id: no_shortcut_support_drop_hopcost_b4
target_blocker_text: "score the named support-drop hop-cost on B_4(0) for small-ball reverse and for var(|v|_2/t) versus unit ell^1 arrival"
source_of_blocker_text: handoff
reachability_to_target: prunes
artifact_role: theorem
next_trace_action: "Do not write the hop-cost into Admissibility and do not attach unit ell^1 arrival; later work that wants a clock must add structure that is not scored here."
conditional_surface_status: "exact for the named positive-integer hop-cost on B_4(0); no adopted clock or axiom edit"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

`B_4(0) = {v∈Z^3 : |v|_1 ≤ 4}` is the closed taxicab ball of radius `4` about
the origin. It has `129` sites. The comparison domain for ratios is the
nonzero subset, with `128` sites. The site `(2,2,2)` has taxicab weight `6`
and is not in `B_4(0)`.

A path is a finite walk along the six nearest-neighbor directions that stays
inside `B_4(0)`. Its `ν`-cost is the sum of `ν` along oriented steps. First
arrival `t(v)` is the minimal such cost; `t(0)=0`. Unit ℓ¹ arrival on the
same graph is the hop-count `|v|_1`. Both arrivals are displayed comparators.

The Euclidean comparator is `|v|_2 = sqrt(v_1^2+v_2^2+v_3^2)`. Population
variance of a finite list `x_1,…,x_n` is

`(1/n) Σ_i (x_i - mean)^2`.

Here `n=128` and `x(v)=|v|_2/t(v)` with the indicated arrival.

## Theorem 1 — Arrivals And Small-Ball Reverse

Dijkstra on the `129`-site graph with the named rule yields

`t(3,0,0)=9`, `t(1,1,1)=5`, `t(4,0,0)=12`.

Explicit witnessing paths of those costs exist. The on-axis walk

`0 → (1,0,0) → (2,0,0) → (3,0,0)`

has hop-costs `3,3,3` and sum `9`. The body-diagonal walk

`0 → (1,0,0) → (1,1,0) → (1,1,1)`

has hop-costs `3,1,1` and sum `5`. The on-axis walk

`0 → (1,0,0) → (2,0,0) → (3,0,0) → (4,0,0)`

has hop-costs `3,3,3,3` and sum `12`. Every in-ball neighbor of `(3,0,0)`
other than the inner axis site has weight `2`, so a last step off a face
costs `3` and cannot undercut the axis sum `9`. The same last-step price
keeps `t(4,0,0)=12` on this ball: a long off-axis continuation through
`(4,1,0)` leaves `B_4(0)`.

The small-ball reverse inequality holds:

`3 t(3,0,0)^2 = 243 > 225 = 9 t(1,1,1)^2`.

Under unit ℓ¹ arrival the same pair is `3·3^2=27` versus `9·3^2=81` and does
not reverse. The comparison is displayed, not adopted.

## Theorem 2 — Variance Of `|v|_2/t` Versus ℓ¹

On the `128` nonzero sites the population variances are

`var_ν = 0.004721240258`, `var_{ℓ¹} = 0.017710351242`.

The named rule is smaller. Axis sites keep the ratio `1/3`. Off-axis sites
receive cheaper hops once they leave the 1-skeleton, which compresses the
spread of `|v|_2/t` relative to unit ℓ¹ arrival, whose axis ratios equal `1`
and whose body-diagonal ratio is `sqrt(3)/3`. Both numbers are computed from
the same `128` sites. Displayed, not adopted.

## Theorem 3 — Displayed, Not Adopted

The named rule is a scored hop-cost on `B_4(0)`, not a clause of
Admissibility. Do not write `ν` into Admissibility. Unit ℓ¹
arrival is a displayed comparator only. Do not attach ℓ¹. No uniqueness
claim is made among hop-costs that reverse the small-ball pair or that beat
the ℓ¹ variance. No axiom is edited.

## Exact Target And Obligation Graph

| Obligation | Disposition |
|---|---|
| quote current Lattice nearest-neighbor and proper-cube wording | source-bound |
| quote current Admissibility covariance wording | source-bound |
| name the support-drop hop-cost on oriented 6-NN steps | closed by the local formula |
| compute `t(3,0,0)`, `t(1,1,1)`, `t(4,0,0)` on `B_4(0)` | closed by one shortest-path search |
| decide `3 t(3,0,0)^2 > 9 t(1,1,1)^2` | closed; `243>225` |
| report both population variances and the order | closed; `ν` smaller |
| write `ν` into Admissibility | outside the claim |
| attach unit ℓ¹ arrival as a clock | outside the claim |
| import a larger-ball arrival table | not executed |
| grow occupancy on a new patch | not executed |
| edit Lattice or Admissibility | `hypothetical_axiom_status: no edit` |

The obligation graph is acyclic. Every leaf of the bounded comparison is
closed. Adoption of a physical clock is not a proof leaf because it is
expressly not part of the target.

## Imports And Non-Claims

Only the current axiom memo is imported. The hop-cost is named in this note
by a local weight formula. No occupancy construction and no axiom edit is
imported. The small-ball reverse test and the two variances are displayed
comparators on `B_4(0)`.

The theorem does not say that this hop-cost is the unique reversing rule, or
that it is a physical clock. It says that on `B_4(0)` the named rule gives
the three reported arrivals, passes the small-ball reverse test, and has
smaller `|v|_2/t` variance than unit ℓ¹ arrival.

## Value Gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It isolates the named support-drop hop-cost on `B_4(0)` as a finite scored object with an explicit reverse test and an explicit variance comparison. |
| V2 | Current main names nearest-neighbor adjacency and proper cubic rotations, but does not score this hop-cost on `B_4(0)`. |
| V3 | Ball cardinality, shortest-path arrivals, the integer reverse inequality, and both variances are independently finite and exact. |
| V4 | The result is more than a restatement of Lattice because it names a two-point hop-cost and compares the implied arrival to two explicit tests. |
| V5 | The comparisons remain displayed; the note does not install a clock or edit Admissibility. |

## No-Go Discipline Gate

The claim is restricted to the named hop-cost on `B_4(0)` and to the two
displayed tests. No global uniqueness of hop-costs and no physical clock
selection is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| named support-drop hop-cost on `B_4(0)` | Dijkstra first arrival | executed; `t(3,0,0)=9`, `t(1,1,1)=5`, reverse holds |
| unit ℓ¹ hops | cost `1` on every 6-NN step | executed as comparator; reverse fails; larger variance |
| axis 1-skeleton only | stay on weight `1` | costs `9` and `12` on axis, but is not the scored rule |
| leave `B_4(0)` | use `(4,1,0)` or `(2,2,2)` | different domain; not scored |
| write `ν` into Admissibility | enlarge the axiom | forbidden; `no edit` |
| attach ℓ¹ as a clock | name unit taxicab arrival | forbidden; displayed only |
| occupancy on a new patch | grow a spatial configuration | not executed |

### N2 — wall independence

The hop-cost formula, the ball `B_4(0)`, the small-ball pair, and the
variance predicate are distinct inputs. The note claims no complete wall
collection beyond this scored class.

### N3 — hidden-condition scan

The hop set, the local formula for `ν`, the shortest-path arrival, the
radius-`4` domain, the reverse predicate, and the population-variance
predicate are declared. Occupancy, an axiom edit, and a larger-ball table
are not silently assumed.

### N4 — source residual matching

The current axiom memo supplies nearest-neighbor adjacency and proper cubic
rotations, and an Admissibility rule covariant under those rotations. It does
not name this hop-cost. The residual scored here is the named rule on
`B_4(0)`, not an imported arrival table from a larger ball.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | named hops and the sites `(3,0,0)`, `(1,1,1)`, `(4,0,0)` | no continuum spacetime classification |
| per site | first arrival from the origin on `B_4(0)` | no occupancy field |
| per mode | no mode calculation | no spectral exhaustion |
| per block | the `129`-site ball | no new spatial patch |
| lattice wide | checked and not executed | no global clock derivation |

### N6 — live partial-closure paths

A later construction may change the hop-cost, enlarge the ball, or add
structure that is not a support-drop hop-cost. Those are different objects.
They are not scored here and are not filled by writing `ν` into
Admissibility or by attaching ℓ¹.

### N7 — hostile steelman

**Steelman:** An off-axis detour inside `B_4(0)` could undercut `t(3,0,0)=9`
or flip the reverse inequality, so the integer report is only a path upper
bound.

**Answer:** First arrival is a shortest-path minimum on the finite graph, not
a single path. Every in-ball last step onto `(3,0,0)` from a weight-`2` site
costs `3`. Dijkstra on all `129` sites returns `9`, `5`, and `12`, and the
reverse comparison uses those minima.

### N8 — cross-cycle echo

This note does not attach a named arrival kernel and does not treat the
`B_4(0)` score as leftover character of a larger-ball arrival table. It
scores only the named local hop-cost on this ball.

**Gate disposition:** PASS for the three arrivals, the small-ball reverse,
and the variance order versus ℓ¹. FAIL / DO NOT SHIP for “`ν` is written
into Admissibility,” “ℓ¹ is attached as a clock,” or “occupancy was grown
on a new patch.”

## Primary Runner

The primary runner enumerates `B_4(0)`, applies the named hop-cost on every
in-ball nearest-neighbor step, computes first arrival by one Dijkstra search,
tests the small-ball reverse inequality, and reports both population
variances. It authors no audit verdict.
