---
claim_id: equal_weight_hopcost_b12_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On B_12(0), the named equal-weight hop-cost is scored for diamond reverse and for var vs ν. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/equal_weight_hopcost_b12_2026_08_15.py
---

# Named Equal-Weight Hop-Cost Scored On `B_12(0)`

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact integer path costs of one displayed named rule `ρ` on the
radius-12 nearest-neighbor ball of one seed; diamond reverse at `(4,0,0)`
versus `(2,2,2)`, the doubled pair `(8,0,0)` versus `(4,4,4)`, and
population variance of `|v|_2/t(v)` on the 2624 nonzero sites against the
named support-drop rule `ν`. Displayed, not adopted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/equal_weight_hopcost_b12_2026_08_15.py`](../scripts/equal_weight_hopcost_b12_2026_08_15.py)
**Cache:** none. `cache_write: false`.
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

Let `B_12(0)` be the set of sites of `Z^3` reachable from the origin by at
most twelve nearest-neighbor steps. This is the 2625-site ball. One-seed
growth starts at `0`. The occupancy `σ_n` at a site `n` is the 6-bit string
whose direction-`d` bit is set exactly when the neighbor of `n` in
direction `d` is strictly nearer the seed. This is the inward occupation of
the one-seed front. On this lattice the inward weight `|σ_n|` equals the
number of nonzero coordinates of `n`.

`G+` is the 24-element group of proper cubic rotations about the seed.
Arrival time `t(n)` is the minimum path cost from `0` to `n` through
`B_12(0)`.

The named rule `ρ` assigns a hop cost on every inward occupancy pair:

```text
c_ρ(σ_v, σ_w) = 3  if |σ_v| = |σ_w| or |σ_v| = 0,
c_ρ(σ_v, σ_w) = 1  otherwise.
```

Equal inward weight or seed-exit costs `3`; every other inward pair costs
`1`. The nine inward-weight pairs realized on `B_12(0)` are the same nine
already seen on `B_6(0)`:

```text
(0,1), (1,0), (1,1), (1,2), (2,1), (2,2), (2,3), (3,2), (3,3).
```

The comparison rule `ν` is the named support-drop hop-cost already scored
on this ball: seed-exit, both weights `1`, or support drop costs `3`, else
`1`. Uniqueness is not claimed.

Two Dijkstras, both capped at the 2625-site ball, give

```text
t_ρ(4,0,0) = 12,  t_ρ(2,2,2) = 14,  t_ρ(8,0,0) = 24,  t_ρ(4,4,4) = 32.
```

Diamond reverse at this scale is the `|v|_2^2`-normalized comparison
`12 t_ρ(4,0,0)^2 > 16 t_ρ(2,2,2)^2`. Substituting gives `1728 > 3136`,
which fails. So `ρ` still fails reverse at `(4,0,0)` versus `(2,2,2)` on
`B_12(0)`. The doubled pair `12 t_ρ(8,0,0)^2 > 16 t_ρ(4,4,4)^2` is
`6912 > 16384`, which also fails.

On the 2624 sites of `B_12(0) \ {0}`, write `r(v) = |v|_2 / t(v)` and let
`var` be the population variance

```text
var(r) = (1/2624) sum_v (r(v) - mean(r))^2.
```

The two Dijkstras give

```text
var_ρ = 0.00094819117290,  var_ν = 0.00666073807018.
```

So `var_ρ < var_ν`. The named equal-weight rule is still strictly below `ν`
on this ball. Displayed, not adopted. Do not write `ρ` or `ν` into
Admissibility. Do not attach L1.

The comparison is not a leftover of the `B_6` score: the ball is a
different ball, `(4,4,4)` first appears here, the variance is the 2624-site
list rather than the 376-site list, and the baseline is `ν` rather than
unit-cost first arrival.

## Current Premise Boundary

The Lattice and Admissibility premises are quoted from
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md):

Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
adjacency, standard translations, and proper cubic rotations about each site.

There is one fixed nearest-neighbor admissibility rule, covariant under lattice
translations and proper cubic rotations.

For each site, the probability distribution over the possibilities is
determined by, and varies with, the nearest-neighbor conditions.

Lattice supplies the six-neighbor graph and the ball. Admissibility supplies
none of the hop costs. The integers `3` and `1`, the inward-weight clauses,
the support-drop clauses, and the arrival functions `t_ρ` and `t_ν` are
separately displayed mathematical inputs. No axiom text is edited.

## Exact Theorems

### Theorem 1

The directed nearest-neighbor edges of `B_12(0)` carry nine inward-weight
pairs of occupancies. The named rule `ρ` assigns every pair: seed-exit
`(0,1)` costs `3`, equal-weight pairs cost `3`, and unequal pairs cost
`1`. In particular `ρ(3,3) = 3`. The named rule `ν` assigns seed-exit,
both-weights-`1`, and support drop the cost `3`, and every other hop the
cost `1`. Those two assignments differ on equal-weight hops of inward
weight at least `2`: `ρ` costs `3` there and `ν` costs `1`.

One Dijkstra for `ρ` on the 2625-site ball yields

```text
t_ρ(4,0,0) = 12,  t_ρ(2,2,2) = 14,  t_ρ(8,0,0) = 24,  t_ρ(4,4,4) = 32.
```

The body-diagonal site `(4,4,4)` is a site of `B_12(0)`
(`|(4,4,4)|_1 = 12`). Diamond reverse at this scale is the pair
`((4,0,0),(2,2,2))`. The test `12 t_ρ(4,0,0)^2 > 16 t_ρ(2,2,2)^2` does
not hold: `1728 > 3136` is false. Diamond does not reverse under `ρ` at
this scale.

Witnessing paths of those `ρ`-costs exist. The axis walk

`0 → (1,0,0) → (2,0,0) → (3,0,0) → (4,0,0)`

has hop-costs `3+3+3+3` and sum `12`. Extending that walk through
`(5,0,0)`, `(6,0,0)`, `(7,0,0)` to `(8,0,0)` has eight costs `3` and
sum `24`. The body-diagonal walk

`0 → (1,0,0) → (1,1,0) → (1,1,1) → (2,1,1) → (2,2,1) → (2,2,2)`

has hop-costs `3+1+1+3+3+3` and sum `14`. Extending that walk through
`(3,2,2)`, `(3,3,2)`, `(3,3,3)`, `(4,3,3)`, `(4,4,3)` to `(4,4,4)` has
the same two cost-`1` hops and ten cost-`3` hops and sum `32`.

The `B_6(0)` arrivals `t_ρ(4,0,0) = 12` and `t_ρ(2,2,2) = 14` therefore
survive the larger ball: no cheaper in-ball detour exists on `B_12(0)`.
That is a new certificate, not a leftover, because the search graph is the
2625-site graph rather than the 377-site graph.

### Theorem 2

On the 2624 nonzero sites of `B_12(0)`, the population variance of
`|v|_2/t(v)` for the named equal-weight rule is `0.00094819117290`. For
the named support-drop rule `ν` on the same sites the same variance is
`0.00666073807018`. So `var_ρ < var_ν`. The named equal-weight rule is
therefore still strictly below `ν` on this ball.

The axis types under `ρ` satisfy `t_ρ = 3 |v|_2` exactly, because every
axis hop is either seed-exit or equal inward weight `1`. That is why the
variance remains more than a factor of six below `ν`, even though the
body-diagonal types sit off that ratio (`t_ρ(2,2,2) = 14` and
`t_ρ(4,4,4) = 32`). The comparison is scored on `B_12(0)` only. It is not
a leftover of the `B_6` score: the balls are a different ball, the
2624-site list is not the 376-site list, and the baseline is `ν`.

### Theorem 3

The named rules `ρ` and `ν` are displayed as finite probes on `B_12(0)`.
Do not write `ρ` or `ν` into Admissibility. Do not attach L1. No
path-length law is attached. The live axiom memo continues to state that
there is one fixed nearest-neighbor admissibility rule, covariant under
translations and proper cubic rotations; that rule is not replaced by
`c_ρ(σ_v, σ_w)` or by the support-drop clauses of `ν`. Displayed, not
adopted. Uniqueness is not claimed.

## Proof-Obligation Graph

| Obligation | Disposition |
|---|---|
| name `B_12(0)` as the 2625-site ball | closed by the nearest-neighbor graph of `Z^3` |
| define inward occupancy of the one-seed front | closed: a bit is set exactly on a strictly nearer neighbor |
| name `ρ` on every inward occupancy pair in `B_12` | closed: cost `3` iff equal weight or seed-exit, else `1` |
| name `ν` as in the prior support-drop score | closed: seed-exit, both-weights-`1`, or support drop costs `3` |
| report `t_ρ(4,0,0)`, `t_ρ(2,2,2)`, `t_ρ(8,0,0)`, `t_ρ(4,4,4)` | closed by Theorem 1 |
| report whether `12 t_ρ(4,0,0)^2 > 16 t_ρ(2,2,2)^2` | closed by Theorem 1; it fails |
| score `var(\|v\|_2/t(v))` for `ρ` versus `ν` on `B_12(0) \ {0}` | closed by Theorem 2; `ρ` strictly below `ν` |
| treat the B_6 score as the B_12 score | refused; different ball, new sites, new baseline |
| write `ρ` or `ν` into Admissibility | refused; Theorem 3 |
| attach L1 | refused; Theorem 3 |
| claim uniqueness | refused; uniqueness is not claimed |

The obligation graph is acyclic. Every leaf of the bounded comparison is
closed. Adoption of a cost or of a path-length law is not a proof leaf.

## Representative Values

| filling | `t(4,0,0)` | `t(2,2,2)` | `t(8,0,0)` | `t(4,4,4)` | `var(\|v\|_2/t)` | diamond reverse? |
|---|---:|---:|---:|---:|---:|---|
| named `ν` | `10` | `8` | `14` | `14` | `0.00666073807018` | yes |
| named `ρ` | `12` | `14` | `24` | `32` | `0.00094819117290` | no |

The table is an exact illustration of Theorems 1 and 2, not an adopted
dynamics. The `ν` arrivals are the prior `B_12(0)` support-drop table,
recomputed here by the second Dijkstra.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact integer arrivals and a population-variance comparison on the finite ball B_12(0) for the displayed equal-weight hop-cost versus the displayed support-drop hop-cost. The rules are displayed, not adopted."
trace_class: frontier_discovery
artifact_role: theorem
conditional_surface_status: "exact on B_12(0) for the displayed rules ρ and ν; no Admissibility edit; not attached to L1"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Framework Boundary

Admissibility supplies one fixed nearest-neighbor rule, covariant under
lattice translations and proper cubic rotations, and says that the local
distribution varies with nearest-neighbor conditions. It does not supply a
numerical hop cost on occupancy pairs. This note therefore treats
`c_ρ(σ_v, σ_w)` and the support-drop clauses of `ν` as displayed probes,
not as axiom clauses.

Record is not used. No formation site, formation rate, or readout value is
assigned to an unoccupied site. The seed is a theorem hypothesis for the
one-seed front, not a privileged physical site.

## Imports And Claim Boundary

| Item | Role | Provenance / status |
|---|---|---|
| `Z^3` nearest-neighbor adjacency and proper cubic rotations | ambient lattice | live axiom memo |
| one-seed front from `0` | theorem hypothesis | declared; no site is privileged in the axiom |
| `σ_n` as 6-bit inward occupation | occupancy used by `ρ` | defined from the one-seed front |
| named rule `ρ` | displayed hop cost on inward weights | mathematical input; not an axiom |
| named rule `ν` | displayed support-drop hop cost | mathematical input; not an axiom |
| diamond order on `((4,0,0),(2,2,2))` | the scale test pair | declared |
| `var(\|v\|_2/t(v))` on `B_12(0) \ {0}` | displayed closeness to `t ∝ \|v\|_2` | computed; not a continuum metric |
| B_6 score of `ρ` | context, not a load-bearing parent | different ball; `(4,4,4)` was absent |

There are no measured, fitted, literature, or observational inputs. A
continuum metric, a path-length axiom, and any cost written into
Admissibility remain outside the result.

## Mutations

1. Treat the B_6 score as already the B_12 score: the balls are a
   different ball; `(4,4,4)` is new; Theorem 2 recomputes the 2624-site
   variance against `ν`.
2. Replace the scale pair by `((8,0,0),(4,4,4))` as the only test: the
   residual asks whether reverse still fails at `(4,0,0)` versus
   `(2,2,2)`. Both pairs fail under `ρ`; the original pair is the stated
   test.
3. Replace population variance by a sample factor `1/2623`: the scored set
   is the finite list of 2624 sites, so the mean-square deviation uses
   `1/2624`.
4. Run one Dijkstra only, or enlarge the graph past `B_12(0)`: the residual
   scores the 2625-site ball with two Dijkstras, one for `ρ` and one for
   `ν`.
5. Compare `var_ρ` to unit-cost first arrival instead of to `ν`: the
   residual asks whether `var` is still below `ν`.
6. Write `ρ` or `ν` into Admissibility, or attach L1: the live axiom memo
   still states one fixed covariant nearest-neighbor rule and contains no
   two-end occupancy hop cost.

## What This Does Not Claim

- No cost is written into Admissibility.
- No path-length law is attached.
- L1 is not attached.
- The comparison is not scored outside `B_12(0)`.
- The B_12 score is not a leftover of the B_6 score (different ball).
- Uniqueness among hop-costs is not claimed.
- No continuum metric is derived.
- No privileged physical seed is added to the Lattice axiom.
- No Record readout is assigned to a site without a record.

## No-Go Discipline Gate

The negative claim is only this: on `B_12(0)`, scoring the named
equal-weight hop-cost for diamond reverse at `(4,0,0)` versus `(2,2,2)` and
for `var(|v|_2/t)` versus `ν` is not a leftover of the B_6 score, is not
an Admissibility clause, and does not attach L1. It is not a claim that
the named rule belongs in the axiom, nor that it minimizes any score on
`B_12(0)`.

### N1 — materially distinct routes

| Route | Exact attack | Result and authority | Marker |
|---|---|---|---|
| leftover of the B_6 score | Argue that the 376-site named-rule score is already the 2624-site score. | Theorem 2: different ball; `(4,4,4)` is new; `var_ρ = 0.00094819117290` is a new number against `ν`. | **ATTEMPTED** |
| keep only the doubled pair | Treat diamond reverse as `t(8,0,0)` versus `t(4,4,4)` only. | Theorem 1: the residual pair is `((4,0,0),(2,2,2))`; it does not reverse. | **ATTEMPTED** |
| attach L1 | Read the smaller named-rule variance as a path-length law. | Theorem 3: L1 is not attached. | **ATTEMPTED** |
| invent a tenth cost | Fold a pair that does not appear on `B_12(0)` into `ρ`. | Theorem 1: the nine realized weight pairs are all named by `ρ`. | **ATTEMPTED** |
| adopt the named rule | Write `ρ` or `ν` into Admissibility. | Theorem 3 and the live axiom memo: one fixed covariant nearest-neighbor rule, no hop cost. | **ATTEMPTED** |
| claim uniqueness | Read the smaller variance as a unique hop-cost. | Uniqueness is not claimed. | **ATTEMPTED** |

### N2 — wall independence and collapse

There is one comparison and one adoption refusal, not a stack of independent
walls. The diamond-order witness and the variance comparison are two
certificates of the same B_12 scoring statement.

| Pair | First closes second? | Second closes first? | Disposition |
|---|---:|---:|---|
| diamond order / variance comparison | no: failure to reverse does not fix the 2624-site variance | no: a smaller variance does not decide the scale pair | independent conclusions on one named rule |
| scoring statement / adoption refusal | no: a probe can fail to reverse and still beat `ν` and still be refused as an axiom | no: refusing adoption does not decide the numbers | independent conclusions |

L1 attachment is not counted as a third wall: Theorem 3 simply does not
attach it.

### N3 — hidden-condition scan

| Phrase or premise | Classification |
|---|---|
| “one-seed growth from `0`” | explicit theorem hypothesis; the Lattice axiom privileges no site |
| “inward occupation of the one-seed front” | defined from nearer neighbors; not an extra occupancy axiom |
| “named equal-weight hop-cost” | displayed finite probe, not a derived scale |
| “two Dijkstras capped at the 2625-site ball” | the definition of `t_ρ` and `t_ν` through `B_12(0)` |
| “`(4,4,4)` is a site” | exact radius `12` versus ball radius `12` |
| “population variance on 2624 sites” | the finite list `B_12(0) \ {0}` |
| “not a leftover” of the B_6 score | Theorems 1 and 2; different ball |
| “Displayed, not adopted” | Theorem 3; no Admissibility edit |

### N4 — citation-to-residual matching

| Evidence path:line | Residual attacked | Residual claimed closed | Match? |
|---|---|---|---:|
| `docs/MINIMAL_AXIOMS_2026-06-29.md:37` | ambient lattice and proper cubic rotations | `Z^3` nearest-neighbor graph and `G+` | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:57` | Admissibility covariance | one fixed covariant nearest-neighbor rule; no hop cost supplied | yes; cost stays displayed |
| `scripts/equal_weight_hopcost_b12_2026_08_15.py:251` | size of the scored ball | `B_12(0)` has 2625 sites | yes |
| `scripts/equal_weight_hopcost_b12_2026_08_15.py:261` | arrival times of the scale sites | `t_ρ(4,0,0) = 12`, `t_ρ(2,2,2) = 14` | yes |
| `scripts/equal_weight_hopcost_b12_2026_08_15.py:281` | diamond reverse test | `12 t_ρ(4,0,0)^2 > 16 t_ρ(2,2,2)^2` fails | yes |
| `scripts/equal_weight_hopcost_b12_2026_08_15.py:306` | variance versus `ν` | named rule strictly below `ν` | yes |
| `scripts/equal_weight_hopcost_b12_2026_08_15.py:246` | two Dijkstras | `DIJKSTRA_CALLS == 2` | yes |
| `scripts/equal_weight_hopcost_b12_2026_08_15.py:194` | adoption of a cost | note keeps `ρ` and `ν` out of Admissibility | yes |
| `scripts/equal_weight_hopcost_b12_2026_08_15.py:199` | attachment to L1 | note does not attach L1 | yes |

No evidence citation is used to claim a path-length axiom, a continuum
metric, or an Admissibility rewrite.

### N5 — rhetoric and resolution audit

| Resolution | Executed? | Narrow negative supported? |
|---|---:|---|
| per element | yes: each directed `B_12(0)` edge | nine named inward-weight pairs |
| per site | yes: `|v|_2/t(v)` on each nonzero site | no other occupancy dictionary is used |
| per mode | yes: the two named rules | uniqueness is not claimed |
| per block | yes: diamond order and variance on `B_12(0) \ {0}` | closeness is the stated variance only |
| lattice wide | no | no Admissibility cost and no L1 attachment |

The runner prints the same five resolution statements only as the bounded
score on `B_12(0)`.

### N6 — partial closure and primitive scan

The only dependency used is the registered `minimal_axioms` node. No
approved primitive supplies a two-end occupancy hop cost, and none is
reclassified as an import or wall.

Two partial-closure mechanisms are recorded rather than suppressed. The
B_6 score of `ρ` is a strictly smaller-ball statement: it does not score
`B_12(0)` and cannot host `(4,4,4)`. Naming `ρ` on the finite weight pairs
is a strictly weaker statement: it does not decide diamond order or the
2624-site variance. The remaining physical choice—whether any hop cost
belongs in Admissibility—stays explicit and does not require an axiom
edit.

### N7 — hostile steelman

The strongest objection is that transporting the named rule from `B_6(0)`
to `B_12(0)` is automatic leftover: the same seed-exit cost, the same
equal-weight cost, and the same axis path should make the larger-ball score
a corollary, including a continuing failure to reverse. The objection
correctly identifies that the axis types remain pinned to `t_ρ = 3 |v|_2`
and that `t_ρ(4,0,0)` and `t_ρ(2,2,2)` numerically match the B_6 table.
It fails because `B_12(0)` is a different finite search graph, first
contains `(4,4,4)`, recomputes variance on 2624 sites against `ν` rather
than against unit-cost first arrival, and could in principle have admitted
a cheaper detour onto `(2,2,2)`. The two Dijkstras close that possibility.

### N8 — cross-cycle echo

The live axiom memo is the only load-bearing parent. Nearby covariance
language is context.

| Earlier surface | Similar issue | Mechanism considered here |
|---|---|---|
| `docs/MINIMAL_AXIOMS_2026-06-29.md` | proper cubic covariance of the nearest-neighbor rule | used as `G+` equivariance of the displayed cost; the rule itself is not replaced |
| B_6 score of `ρ` | same named costs, smaller ball, no `(4,4,4)` | scored as a strictly smaller-ball parent; Theorems 1 and 2 are not leftovers |
| B_12 score of `ν` | same ball, different hop-cost | used only as the variance baseline; not adopted |

No earlier mechanism retires the B_12 `ρ` score or the adoption refusal.

No-Go Discipline disposition: **PASS** for the bounded comparison and the
adoption boundary stated at the start of this section.

## Live Parent Quotes

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

> No site is privileged. Sites are distinguished by the supplied lattice
> structure alone.

> There is one fixed nearest-neighbor admissibility rule, covariant under lattice
> translations and proper cubic rotations.

> For each site, the probability distribution over the possibilities is
> determined by, and varies with, the nearest-neighbor conditions.

## Runner Contract

The companion runner builds the 2625-site ball; assigns the named
equal-weight hop-cost on every inward occupancy pair in `B_12`; assigns
the named support-drop hop-cost `ν`; runs two Dijkstras capped at
`B_12(0)`; reports `t_ρ(4,0,0) = 12`, `t_ρ(2,2,2) = 14`,
`t_ρ(8,0,0) = 24`, and `t_ρ(4,4,4) = 32`; reports that diamond does not
reverse at `(4,0,0)` versus `(2,2,2)`; compares `var(|v|_2/t)` for `ρ`
versus `ν` on the 2624 nonzero sites; rejects leftover of the B_6 score;
and verifies that the live axiom memo does not host the displayed costs.
Declared audit inputs are this note and the axiom memo.
