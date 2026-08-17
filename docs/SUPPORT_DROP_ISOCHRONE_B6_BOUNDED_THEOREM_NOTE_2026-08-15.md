---
claim_id: support_drop_isochrone_b6_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On B_6(0), the isochrones of the named support-drop hop-cost are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/support_drop_isochrone_b6_2026_08_15.py
---

# Isochrones Of The Named Support-Drop Hop-Cost On `B_6(0)`

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact integer path costs, the twenty-two `G+` site-type arrival
times, the `|v|_2/t` table, and whether the `t = const` shells are single
Euclidean radii, on the radius-6 nearest-neighbor ball of one seed.
Displayed, not adopted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/support_drop_isochrone_b6_2026_08_15.py`](../scripts/support_drop_isochrone_b6_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.
**Cache:** none. `cache_write: false`.

## Result Up Front

Let `B_6(0) = { v ∈ Z^3 : |v|_1 ≤ 6 }`. Directed edges are the six
nearest-neighbor steps whose both ends lie in the ball. Write `|σ_v|` for
the number of nonzero coordinates of `v`. On a directed hop `v → w` still
inside `B_6(0)`, the named support-drop rule `ν` is

`ν(v→w) = 3` if `|σ_v|=0` or `(|σ_v|=|σ_w|=1)` or `|σ_w| < |σ_v|`,
else `1`.

Those three clauses are the whole rule. Arrival time `t(v)` is the least
sum of `ν` along a directed path from `0` to `v` in that graph. One
Dijkstra from the origin computes every arrival.

`G+` is the 24-element group of proper cubic rotations about the seed. The
376 nonzero sites of `B_6(0)` fall into 22 `G+` site-types, labelled by a
representative with coordinates `a ≥ b ≥ c ≥ 0`. Arrival time is constant
on each type. In particular

`t(4,0,0) = 10`, `t(2,2,2) = 8`.

The twenty-two type times and the ratios `|v|_2 / t` are the table of
Theorem 1. They are not only the two-point arrivals. The `t = const`
shells are **not** all single Euclidean radii: six of the ten arrival
values (`t = 3,4,9,10,11,14`) are single-radius, while four mixed shells
(`t = 5,6,7,8`) each join two or more distinct Euclidean radii.

On the 376 nonzero sites the population variance of `|v|_2 / t` equals the
noshrt figure `0.00590563902870` and is strictly below the ℓ¹ comparator
`0.01350203761919`. So `var_ν < var_ℓ¹`. Displayed, not adopted.

The report is not a leftover of the two-point `10` and `8` times. Naming
`t(4,0,0) = 10` and `t(2,2,2) = 8` does not compute the twenty-two-type
table or decide whether the `t = const` shells are single Euclidean
radii. The rule is not written into Admissibility. It is not attached to
L1.

## Current Premise Boundary

The Lattice and Admissibility premises are quoted from
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md):

Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
adjacency, standard translations, and proper cubic rotations about each site.

There is one fixed nearest-neighbor admissibility rule, covariant under lattice
translations and proper cubic rotations.

Lattice supplies the six-neighbor graph, the ball, and `G+`. Admissibility
supplies none of the hop costs. The integers `3` and `1`, the support-size
clauses, and the arrival function `t` are separately displayed
mathematical inputs. No axiom text is edited.

## Named Rule

Unit-cost ℓ¹ arrival is the closed form `t_ℓ¹(v) = |v|_1`; it is not
obtained from a second Dijkstra. The support-drop hop-cost is the same
named rule scored on `B_6(0)` for diamond reverse and variance. This note
loads that rule as a displayed input and reports its isochrones.

## Theorem 1 — Arrival Time Of Each `G+` Site-Type

`B_6(0)` has 377 sites and 376 nonzero sites. Under `ν`, arrival time is
constant on each of the 22 `G+` site-types in `B_6(0) \ {0}`. The types,
orbit sizes, times, Euclidean radii, and ratios `|v|_2 / t` are

| representative | orbit size | `t` | `|v|_2` | `|v|_2 / t` |
|---|---:|---:|---|---|
| `(1,0,0)` | `6` | `3` | `1` | `1/3` |
| `(1,1,0)` | `12` | `4` | `√2` | `√2 / 4` |
| `(2,0,0)` | `6` | `6` | `2` | `1/3` |
| `(1,1,1)` | `8` | `5` | `√3` | `√3 / 5` |
| `(2,1,0)` | `24` | `5` | `√5` | `√5 / 5` |
| `(3,0,0)` | `6` | `9` | `3` | `1/3` |
| `(2,1,1)` | `24` | `6` | `√6` | `√6 / 6` |
| `(2,2,0)` | `12` | `6` | `2√2` | `√2 / 3` |
| `(3,1,0)` | `24` | `6` | `√10` | `√10 / 6` |
| `(4,0,0)` | `6` | `10` | `4` | `2/5` |
| `(2,2,1)` | `24` | `7` | `3` | `3/7` |
| `(3,1,1)` | `24` | `7` | `√11` | `√11 / 7` |
| `(3,2,0)` | `24` | `7` | `√13` | `√13 / 7` |
| `(4,1,0)` | `24` | `7` | `√17` | `√17 / 7` |
| `(5,0,0)` | `6` | `11` | `5` | `5/11` |
| `(2,2,2)` | `8` | `8` | `2√3` | `√3 / 4` |
| `(3,2,1)` | `48` | `8` | `√14` | `√14 / 8` |
| `(3,3,0)` | `12` | `8` | `3√2` | `3√2 / 8` |
| `(4,1,1)` | `24` | `8` | `3√2` | `3√2 / 8` |
| `(4,2,0)` | `24` | `8` | `2√5` | `√5 / 4` |
| `(5,1,0)` | `24` | `8` | `√26` | `√26 / 8` |
| `(6,0,0)` | `6` | `14` | `6` | `3/7` |

In particular `t(4,0,0) = 10` and `t(2,2,2) = 8`. The ten constant-`t`
shells are

```text
t = 3 : type (1,0,0); single radius 1
t = 4 : type (1,1,0); single radius √2
t = 5 : types (1,1,1), (2,1,0); radii √3 and √5
t = 6 : types (2,0,0), (2,1,1), (2,2,0), (3,1,0); radii 2, √6, 2√2, √10
t = 7 : types (2,2,1), (3,1,1), (3,2,0), (4,1,0); radii 3, √11, √13, √17
t = 8 : types (2,2,2), (3,2,1), (3,3,0), (4,1,1), (4,2,0), (5,1,0);
        radii 2√3, √14, 3√2, 2√5, √26
t = 9 : type (3,0,0); single radius 3
t = 10 : type (4,0,0); single radius 4
t = 11 : type (5,0,0); single radius 5
t = 14 : type (6,0,0); single radius 6
```

There are six single-radius shells and four mixed shells. The mixed
`t = 8` shell includes both `(2,2,2)` and five other types; `(3,3,0)` and
`(4,1,1)` share the common radius `3√2` but sit with three further radii
in the same arrival set. The `t = const` shells are therefore not all
single Euclidean radii. The twenty-two-type table is not only the
two-point times.

## Theorem 2 — Population Variance Of `|v|_2/t`

On the 376 nonzero sites of `B_6(0)`, let `r(v) = |v|_2 / t(v)` and write
population variance `(1/n) ∑ (r − mean)^2`. The runner computes

`var_ν = 0.00590563902870`, `var_ℓ¹ = 0.01350203761919`.

The first figure equals the noshrt population variance and is strictly
below the ℓ¹ figure. So `var_ν < var_ℓ¹`. Unit hop costs recover `|v|_1`
on every site of `B_6(0)`, so the second field is the isochrone ratio of
the constant-`1` filling. The comparison is displayed, not adopted. No
path-length law is attached.

## Theorem 3 — Displayed, Not Adopted

The rule `ν` and its isochrones are a displayed scoring device on
`B_6(0)`. They are not written into Admissibility. They are not attached
to L1. They are not a replacement for unit-cost first arrival, and they
are not offered as the unique hop-cost whose shells match Euclidean
spheres. The live axiom memo continues to state that there is one fixed
nearest-neighbor admissibility rule, covariant under translations and
proper cubic rotations; that rule is not replaced by `ν(v→w)`. Displayed,
not adopted.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact integer arrivals on every G+ site-type of B_6(0) for the named support-drop hop-cost, together with a displayed variance comparison. The rule is displayed, not adopted."
trace_class: frontier_discovery
artifact_role: theorem
conditional_surface_status: "exact on B_6(0) for the displayed rule ν; no Admissibility edit; not attached to L1"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Proof-Obligation Graph

| Obligation | Disposition |
|---|---|
| name `B_6(0)` and the six nearest-neighbor steps | closed by the nearest-neighbor graph of `Z^3` |
| name `ν` by the three support-size clauses | closed; seed-exit, both weights `1`, support drop |
| count `G+` | closed: 24 proper cubic rotations |
| compute `t(v)` on every `G+` site-type | closed by Theorem 1; 22 nonzero types |
| confirm `t(4,0,0) = 10` and `t(2,2,2) = 8` | closed by Theorem 1 |
| report `|v|_2 / t` for each type | closed by Theorem 1 |
| decide whether `t = const` shells are single Euclidean radii | closed by Theorem 1; six single-radius, four mixed |
| treat the table as leftover of the two-point `10` and `8` times | refused; the two times do not report the 22-type shells |
| compare the population variance on the 376 nonzero sites with ℓ¹ | closed by Theorem 2; equals the noshrt figure and strictly below |
| write `ν` into Admissibility | refused; Theorem 3 |
| attach L1 | refused; Theorem 3 |

The obligation graph is acyclic. Every leaf of the bounded comparison is
closed. Adoption of a cost or of a path-length law is not a proof leaf.

## Framework Boundary

Admissibility supplies one fixed nearest-neighbor rule, covariant under
lattice translations and proper cubic rotations, and says that the local
distribution varies with nearest-neighbor conditions. It does not supply a
numerical hop cost on support sizes. This note therefore treats `ν` as a
displayed probe, not as an axiom clause.

Record is not used. No formation site, formation rate, or readout value is
assigned to an unoccupied site. The seed is a theorem hypothesis for the
one-seed front, not a privileged physical site.

## Imports And Claim Boundary

| Item | Role | Provenance / status |
|---|---|---|
| `Z^3` nearest-neighbor adjacency and proper cubic rotations | ambient lattice | live axiom memo |
| one-seed front from `0` | theorem hypothesis | declared; no site is privileged in the axiom |
| named support-drop hop-cost `ν` | displayed `G+`-equivariant hop cost | mathematical input; not an axiom |
| `t(v)` on `B_6(0)` | min path cost under that rule | computed; Theorem 1; one Dijkstra |
| `|v|_2 / t` on the 22 site-types | displayed Euclidean-ratio table | computed; Theorem 1 |
| whether `t = const` shells are single Euclidean radii | displayed isochrone test | computed; not all single |
| `Var(\|v\|_2 / t)` versus ℓ¹ | displayed variance test | computed; Theorem 2; noshrt figure |
| two-point times `t(4,0,0) = 10`, `t(2,2,2) = 8` | context, not a load-bearing parent | identity does not determine the shells |

There are no measured, fitted, literature, or observational inputs. A
continuum metric, a path-length axiom, L1 attachment, and any cost written
into Admissibility remain outside the result.

## Mutations

1. Collapse the twenty-two-type table to the two comparison points
   `(4,0,0)` and `(2,2,2)`: that is the two-point residual, not the
   isochrone residual.
2. Claim every `t = const` shell is a single Euclidean radius: four mixed
   shells (`t = 5,6,7,8`) join several radii.
3. Include the origin in the variance: `t(0) = 0` is excluded by the
   stated domain of 376 nonzero sites.
4. Write `ν` into Admissibility: the live axiom memo still states one
   fixed covariant nearest-neighbor rule and contains no support-drop hop
   cost.
5. Attach L1: Theorem 3 refuses L1 attachment.
6. Replace `ν` by unit-cost ℓ¹: the axis and body-diagonal times become
   `4` and `6`, the diamond does not reverse, and the variance is the
   larger comparator.

## What This Does Not Claim

- No cost is written into Admissibility.
- No path-length law is attached.
- The comparison is not scored outside `B_6(0)`.
- The isochrone table is not a leftover of the two-point `10` and `8`
  times.
- The filling is not claimed to be unique among hop-costs that reverse
  the diamond or beat ℓ¹ variance.
- No continuum Euclidean metric is derived.
- No privileged physical seed is added to the Lattice axiom.
- No Record readout is assigned to a site without a record.
- The rule is not attached to L1.

## No-Go Discipline Gate

The negative claim is only this: on `B_6(0)`, the report of the named
support-drop isochrones is not a leftover of the two-point `10` and `8`
times, is not an Admissibility clause, and is not attached to L1. It is
not a claim about any other hop-cost, any larger ball, or any adopted
dynamics.

### N1 — materially distinct routes

| Route | Exact attack | Result and authority | Marker |
|---|---|---|---|
| two-point leftover | Read `t(4,0,0) = 10` and `t(2,2,2) = 8` as already the isochrone report. | Theorem 1 computes all 22 site-types and the 10 arrival shells. | **ATTEMPTED** |
| two-point ratio test | Compare only `4/10` and `√12 / 8` and declare the Euclidean-ratio table. | Theorem 1 reports `|v|_2 / t` on every type; four shells mix radii. | **ATTEMPTED** |
| force single-radius shells | Treat each `t = const` set as one Euclidean sphere. | Four mixed shells (`t = 5,6,7,8`) join several radii. | **ATTEMPTED** |
| sample variance or include the origin | Change the estimator or divide by `t(0) = 0`. | The stated estimator is the population variance on the 376 nonzero sites. | **ATTEMPTED** |
| write the rule into Admissibility | Treat seed-exit `3`, axis-extension `3`, and support-drop `3` as the covariant rule. | Theorem 3: the live axiom memo still states one fixed nearest-neighbor rule and no hop cost. | **ATTEMPTED** |
| attach L1 | Promote `t` or ℓ¹ to an L1 clause. | Theorem 3 refuses L1 attachment. | **ATTEMPTED** |

### N2 — wall independence and collapse

There is one comparison and one adoption refusal, not a stack of independent
walls. The twenty-two-type table and the variance comparison are two
certificates of the same isochrone report.

| Pair | First closes second? | Second closes first? | Disposition |
|---|---:|---:|---|
| twenty-two-type table / variance comparison | no: the table does not by itself name a variance | no: a variance does not reconstruct the 22 times | independent displayed facts in Theorems 1 and 2 |
| isochrone report / adoption refusal | no: a probe can be tabulated and still refused as an axiom | no: refusing adoption does not compute `t(v)` | independent conclusions |

L1 attachment is not counted as a third wall: Theorem 3 simply does not
attach one.

### N3 — hidden-condition scan

| Phrase or premise | Classification |
|---|---|
| “one-seed growth from `0`” | explicit theorem hypothesis; the Lattice axiom privileges no site |
| “named support-drop hop-cost `ν`” | displayed finite probe, not a derived scale |
| “`G+`-equivariant” | covariance under the axiom's proper cubic rotations |
| “population variance on 376 nonzero sites” | explicit estimator and domain in Theorem 2 |
| “strictly below” the ℓ¹ variance | Theorem 2; displayed, not adopted |
| “not a leftover” of the two-point times | Theorem 1; the 22-type shells are new |
| “Displayed, not adopted” | Theorem 3; no Admissibility edit; not attached to L1 |

### N4 — citation-to-residual matching

| Evidence path:line | Residual attacked | Residual claimed closed | Match? |
|---|---|---|---:|
| `docs/MINIMAL_AXIOMS_2026-06-29.md:37` | ambient lattice and proper cubic rotations | `Z^3` nearest-neighbor graph and `G+` | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:57` | Admissibility covariance | one fixed covariant nearest-neighbor rule; no hop cost supplied | yes; cost stays displayed |
| `scripts/support_drop_isochrone_b6_2026_08_15.py` | named rule `ν` | seed-exit, both weights `1`, support drop | yes |
| `scripts/support_drop_isochrone_b6_2026_08_15.py` | `t(4,0,0)` and `t(2,2,2)` | times `10` and `8` | yes |
| `scripts/support_drop_isochrone_b6_2026_08_15.py` | `t(v)` on every site-type | the 22 orbit times of Theorem 1 | yes |
| `scripts/support_drop_isochrone_b6_2026_08_15.py` | whether shells are single Euclidean radii | six single-radius, four mixed | yes |
| `scripts/support_drop_isochrone_b6_2026_08_15.py` | population variance versus ℓ¹ | noshrt digits, strictly below | yes |
| `scripts/support_drop_isochrone_b6_2026_08_15.py` | adoption of a cost | note and axiom keep the cost out of Admissibility; not attached to L1 | yes |

No evidence citation is used to claim a path-length axiom, a continuum
metric, L1 attachment, or an Admissibility rewrite.

### N5 — rhetoric and resolution audit

| Resolution | Executed? | Narrow negative supported? |
|---|---:|---|
| per element | yes: each directed `B_6(0)` edge | one support-drop hop; no other edge family is classified |
| per site | yes: `t(v)` and `|v|_2 / t` at each of the 376 nonzero sites | no other hop-cost dictionary is used |
| per mode | yes: 22 site-types and the ten arrival shells | other hop-costs and larger balls are untested and unclaimed |
| per block | yes: the population variance on the 376 nonzero sites | closeness is the stated variance test only |
| lattice wide | no | no Admissibility cost and no L1 attachment are adopted |

The runner prints the same five resolution statements.

### N6 — partial-closure and primitive scan

The only dependency used is the registered `minimal_axioms` node. No
approved primitive supplies a support-drop hop cost, an isochrone, or a
Euclidean sphere law, and none is reclassified as an import or wall.

One partial-closure mechanism is recorded rather than suppressed. The
two-point times `t(4,0,0) = 10` and `t(2,2,2) = 8` name the diamond
reverse but do not compute the twenty-two-type table or decide whether
`t = const` shells are single Euclidean radii. The remaining physical
choice—whether any hop cost belongs in Admissibility—stays explicit and
does not require an axiom edit.

### N7 — hostile steelman

The strongest objection is that naming `t(4,0,0) = 10` and `t(2,2,2) = 8`
already is the isochrone report, so a twenty-two-type table is ornament.
The objection correctly notes that those two numbers are part of the
table. It fails because the isochrone residual asks whether every
`t = const` shell is a Euclidean radius. That is a statement about all
22 types: the axis types do not share one arrival, `(1,1,1)` and
`(2,1,0)` share `t = 5` at two radii, and the `t = 8` shell mixes
`(2,2,2)` with five other types. The two-point identity does not exhibit
those shells.

### N8 — cross-cycle echo

The live axiom memo is the only load-bearing parent. Nearby hop-cost
language is context.

| Earlier surface | Similar issue | Mechanism considered here |
|---|---|---|
| `docs/MINIMAL_AXIOMS_2026-06-29.md` | proper cubic covariance of the nearest-neighbor rule | used as `G+` equivariance of the displayed cost; the rule itself is not replaced |
| named support-drop hop-cost on `B_6(0)` | same rule, two-point times and variance | counted as a strictly smaller residual; Theorem 1 reports the 22-type shells |

No earlier mechanism retires the twenty-two-type table, the mixed-shell
classification, the variance comparison, or the adoption refusal.

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

The companion runner builds the 24 proper cubic rotations and the 377-site
ball; applies the named support-drop hop-cost; runs one Dijkstra; computes
`t(v)` on every site-type; reports `|v|_2 / t` and that the `t = const`
shells are not all single Euclidean radii; compares the two population
variances; rejects the mutation families, including the two-point leftover;
and verifies that the live axiom memo does not host the displayed cost.
Declared audit inputs are this note and the axiom memo.
