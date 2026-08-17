---
claim_id: cost3_best_reversal_isochrone_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On B_3(0), the isochrones of the variance-minimizing diamond-reversing {1,2,3} two-end occupancy cost are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/cost3_best_reversal_isochrone_2026_08_15.py
---

# Isochrones Of The Variance-Minimizing Diamond-Reversing `{1,2,3}` Two-End Cost On `B_3(0)`

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact integer path costs, the six `G+` site-type arrival times,
and a displayed variance comparison on the radius-3 nearest-neighbor ball
of one seed. Displayed, not adopted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/cost3_best_reversal_isochrone_2026_08_15.py`](../scripts/cost3_best_reversal_isochrone_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

Let `B_3(0)` be the set of sites of `Z^3` reachable from the origin by at
most three nearest-neighbor steps. One-seed growth starts at `0`. The
occupancy `σ_n` at a site `n` is the 6-bit string whose direction-`d` bit is
set exactly when the neighbor of `n` in direction `d` is strictly nearer the
seed. This is the inward occupation of the one-seed front.

`G+` is the 24-element group of proper cubic rotations about the seed. A hop
cost `c(σ_v, σ_w) ∈ {1,2,3}` on a directed nearest-neighbor edge `v → w` is
`G+`-equivariant when it is constant on `G+` orbits of endpoint pairs.
Arrival time `t(n)` is the minimum path cost from `0` to `n` through
`B_3(0)`.

The eight `G+` orbits of inward occupancy pairs, written as inward-weight
pairs `(|σ_v|, |σ_w|)`, are

```text
(0,1), (1,0), (1,1), (1,2), (2,1), (2,2), (2,3), (3,2).
```

The lex-first variance-minimizing diamond-reversing filling of those orbits
is

```text
c = (3, 1, 3, 1, 1, 3, 1, 1).
```

On `B_3(0)` this filling realizes `t(3,0,0) = 9` and `t(1,1,1) = 5`. The
six `G+` site-types in `B_3(0) \ {0}` have distinct constant arrival times.
Each `t = const` shell is therefore a single `G+` site-type, hence a single
Euclidean radius: the shells are the Euclidean-ratio table of `|v|_2 / t`,
not only the two-point axis and diagonal times. Among the 62 nonzero sites
the population variance of `|v|_2 / t` is `0.00017588571746`, strictly
below the ell^1 comparator `0.02073945514155`. The comparison is reported
on `B_3(0)` only. Displayed, not adopted.

The report is not a leftover of the minimizer identity. Naming
`c = (3, 1, 3, 1, 1, 3, 1, 1)` and the two-point times `t(3,0,0) = 9`,
`t(1,1,1) = 5` does not compute the six-type table or decide whether the
`t = const` shells are the Euclidean-ratio table. It is not a leftover of
the wrong map: the lex-first reversal `c = (1, 1, 3, 1, 1, 1, 1, 1)` mixes
`(1,1,1)` and `(2,1,0)` into one shell and is not this filling.

## Exact Theorems

### Theorem 1

`B_3(0)` has 63 sites and 228 directed nearest-neighbor edges. Under the
variance-minimizing filling, arrival time is constant on each of the six
`G+` site-types in `B_3(0) \ {0}`. The six types, their times, and the
ratio `|v|_2 / t` are

| representative | orbit size | `t` | `|v|_2` | `|v|_2 / t` |
|---|---:|---:|---|---|
| `(1,0,0)` | `6` | `3` | `1` | `1/3` |
| `(1,1,0)` | `12` | `4` | `√2` | `√2 / 4` |
| `(1,1,1)` | `8` | `5` | `√3` | `√3 / 5` |
| `(2,0,0)` | `6` | `6` | `2` | `1/3` |
| `(2,1,0)` | `24` | `7` | `√5` | `√5 / 7` |
| `(3,0,0)` | `6` | `9` | `3` | `1/3` |

In particular `t(1,0,0) = 3`, `t(1,1,0) = 4`, `t(2,0,0) = 6`,
`t(2,1,0) = 7`, `t(1,1,1) = 5`, and `t(3,0,0) = 9`. The six seed-exit
edges occupy orbit `(0,1)` of cost `3`. Both axis extensions occupy orbit
`(1,1)` of cost `3`. The axis path `0 → (1,0,0) → (2,0,0) → (3,0,0)`
costs `3+3+3 = 9`. The body-diagonal path
`0 → (1,0,0) → (1,1,0) → (1,1,1)` costs `3+1+1 = 5`.

The constant-`t` shells are therefore

```text
t=3 : 6 sites of type (1,0,0)
t=4 : 12 sites of type (1,1,0)
t=5 : 8 sites of type (1,1,1)
t=6 : 6 sites of type (2,0,0)
t=7 : 24 sites of type (2,1,0)
t=9 : 6 sites of type (3,0,0)
```

Every shell is a single `G+` site-type, hence a single Euclidean radius.
The six shells are the Euclidean-ratio table. They are not only the
two-point `(3,0,0)` and `(1,1,1)` times. The three axis types share the
common ratio `1/3`.

### Theorem 2

Let `S` be the 62 nonzero sites of `B_3(0)`. Write `|v|_2` for the
ordinary Euclidean radius `√(x^2+y^2+z^2)`. The population variance

```text
Var(a) = (1/|S|) Σ_{v in S} (a(v) - mean(a))^2
```

on the displayed ratio field is

```text
Var(|v|_2 / t(v))     = 0.00017588571746
Var(|v|_2 / |v|_1)    = 0.02073945514155
```

The first figure equals the minkbest population variance and is strictly
below the ell^1 figure. Unit hop costs recover `|v|_1` on every site of
`B_3(0)`, so the second field is the isochrone ratio of the constant-`1`
filling (the ell^1 comparator). The comparison is displayed, not adopted.
No path-length law is attached.

### Theorem 3

The variance-minimizing filling and its isochrones are displayed as a
finite probe on `B_3(0)`. They are not written into Admissibility. No
path-length law is attached; do not attach graph radius, Euclidean radius,
ell^1, or the filling `c` as an axiom clause. The live axiom memo
continues to state that there is one fixed nearest-neighbor admissibility
rule, covariant under translations and proper cubic rotations; that rule
is not replaced by `c(σ_v, σ_w)`. Displayed, not adopted.

## Proof-Obligation Graph

| Obligation | Disposition |
|---|---|
| name `B_3(0)` and the six direction bits | closed by the nearest-neighbor graph of `Z^3` |
| define inward occupancy of the one-seed front | closed: a bit is set exactly on a strictly nearer neighbor |
| count `G+` | closed: 24 proper cubic rotations |
| name the eight pair orbits and the variance-minimizing filling | closed by Theorem 1; `c = (3, 1, 3, 1, 1, 3, 1, 1)` |
| compute `t(v)` on every `G+` site-type | closed by Theorem 1; six nonzero types |
| confirm `t(3,0,0) = 9` and `t(1,1,1) = 5` | closed by Theorem 1 |
| report `|v|_2 / t` for each type and whether shells are the Euclidean-ratio table | closed by Theorem 1; each shell is one type |
| compare the population variance on the 62 nonzero sites with ell^1 | closed by Theorem 2; strictly below |
| treat the table as leftover of the minimizer identity | refused; identity does not report the six-type shells |
| treat the table as leftover of the wrong map | refused; the lex-first reversal is a different filling |
| write `c` into Admissibility | refused; Theorem 3 |
| attach a path-length law | refused; Theorem 3 |

The obligation graph is acyclic. Every leaf of the bounded comparison is
closed. Adoption of a cost or of a path-length law is not a proof leaf.

## Representative Values

| site type | `t` | `|v|_2 / t` | `|v|_2 /` graph radius |
|---|---:|---|---|
| `(1,0,0)` | `3` | `1/3` | `1` |
| `(1,1,0)` | `4` | `√2 / 4` | `√2 / 2` |
| `(1,1,1)` | `5` | `√3 / 5` | `√3 / 3` |
| `(2,0,0)` | `6` | `1/3` | `1` |
| `(2,1,0)` | `7` | `√5 / 7` | `√5 / 3` |
| `(3,0,0)` | `9` | `1/3` | `1` |

The table is an exact illustration of Theorems 1 and 2, not an adopted
dynamics.

## Framework Boundary

Admissibility supplies one fixed nearest-neighbor rule, covariant under
lattice translations and proper cubic rotations, and says that the local
distribution varies with nearest-neighbor conditions. It does not supply a
numerical hop cost on occupancy pairs. This note therefore treats
`c(σ_v, σ_w) ∈ {1,2,3}` as a displayed probe, not as an axiom clause.

Record is not used. No formation site, formation rate, or readout value is
assigned to an unoccupied site. The seed is a theorem hypothesis for the
one-seed front, not a privileged physical site.

## Imports And Claim Boundary

| Item | Role | Provenance / status |
|---|---|---|
| `Z^3` nearest-neighbor adjacency and proper cubic rotations | ambient lattice | live axiom memo |
| one-seed front from `0` | theorem hypothesis | declared; no site is privileged in the axiom |
| `σ_n` as 6-bit inward occupation | occupancy used by the probe | defined from the one-seed front |
| variance-minimizing `c = (3, 1, 3, 1, 1, 3, 1, 1)` | displayed `G+`-equivariant hop cost | mathematical input; not an axiom |
| `t(v)` on `B_3(0)` | min path cost under that filling | computed; Theorem 1 |
| `|v|_2 / t` on the six site-types | displayed Euclidean-ratio table | computed; Theorem 1 |
| `Var(\|v\|_2 / t)` versus ell^1 | displayed isochrone test | computed; Theorem 2 |
| minimizer identity of `c` | context, not a load-bearing parent | identity does not determine the shells |
| lex-first reversing map | context, the wrong map | a different filling; mixed `t = 3` shell |

There are no measured, fitted, literature, or observational inputs. A
continuum metric, a path-length axiom, and any cost written into
Admissibility remain outside the result.

## Mutations

1. Collapse the six-type table to the two comparison points `(3,0,0)` and
   `(1,1,1)`: that is the minimizer-identity residual, not the isochrone
   residual.
2. Replace the variance-minimizing filling by the lex-first reversal
   `(1, 1, 3, 1, 1, 1, 1, 1)`: that is the wrong map; it mixes two
   site-types into one shell.
3. Claim the `t = const` shells are not the Euclidean-ratio table: each
   shell is one `G+` site-type.
4. Include the origin in the variance: `t(0) = 0` is excluded by the
   stated domain of 62 nonzero sites.
5. Write `c` into Admissibility: the live axiom memo still states one
   fixed covariant nearest-neighbor rule and contains no two-end occupancy
   hop cost.
6. Attach a path-length law: Theorem 3 refuses ell^1, graph radius, and
   Euclidean radius as axiom clauses.

## What This Does Not Claim

- No cost is written into Admissibility.
- No path-length law is attached.
- The comparison is not scored outside `B_3(0)`.
- The isochrone table is not a leftover of the minimizer identity.
- The isochrone table is not a leftover of the wrong map.
- The filling is not claimed to be re-derived here as a minimizer.
- No continuum Euclidean metric is derived.
- No privileged physical seed is added to the Lattice axiom.
- No Record readout is assigned to a site without a record.

## No-Go Discipline Gate

The negative claim is only this: on `B_3(0)`, the report of the
variance-minimizing reversing isochrones is not a leftover of the
minimizer identity, is not a leftover of the wrong map, is not an
Admissibility clause, and does not attach a path-length law. It is not a
claim about any other filling, any larger ball, or any adopted dynamics.

### N1 — materially distinct routes

| Route | Exact attack | Result and authority | Marker |
|---|---|---|---|
| minimizer-identity leftover | Read `c` and the two-point times `t(3,0,0) = 9`, `t(1,1,1) = 5` as already the isochrone report. | Theorem 1 computes all six site-types and the six distinct shells. | **ATTEMPTED** |
| wrong-map leftover | Reuse the lex-first reversal isochrones as this table. | That map is `(1, 1, 3, 1, 1, 1, 1, 1)` with mixed `t = 3`; this filling is `(3, 1, 3, 1, 1, 3, 1, 1)`. | **ATTEMPTED** |
| two-point ratio test | Compare only `3/9` and `√3 / 5` and declare the Euclidean-ratio table. | Theorem 1 reports `|v|_2 / t` on every type; the shells are six radii. | **ATTEMPTED** |
| sample variance or include the origin | Change the estimator or divide by `t(0) = 0`. | The stated estimator is the population variance on the 62 nonzero sites. | **ATTEMPTED** |
| write the filling into Admissibility | Treat seed-exit `3` and axis-extension `3` as the covariant rule. | Theorem 3: the live axiom memo still states one fixed nearest-neighbor rule and no hop cost. | **ATTEMPTED** |
| attach a path-length law | Promote `t` or ell^1 to an axiom-level length. | Theorem 3 refuses both; do not attach either. | **ATTEMPTED** |

### N2 — wall independence and collapse

There is one comparison and one adoption refusal, not a stack of independent
walls. The six-type table and the variance comparison are two certificates of
the same isochrone report.

| Pair | First closes second? | Second closes first? | Disposition |
|---|---:|---:|---|
| six-type table / variance comparison | no: the table does not by itself name a variance | no: a variance does not reconstruct the six times | independent displayed facts in Theorems 1 and 2 |
| isochrone report / adoption refusal | no: a probe can be tabulated and still refused as an axiom | no: refusing adoption does not compute `t(v)` | independent conclusions |

Path-length attachment is not counted as a third wall: Theorem 3 simply
does not attach one.

### N3 — hidden-condition scan

| Phrase or premise | Classification |
|---|---|
| “one-seed growth from `0`” | explicit theorem hypothesis; the Lattice axiom privileges no site |
| “inward occupation of the one-seed front” | defined from nearer neighbors; not an extra occupancy axiom |
| “variance-minimizing `c = (3, 1, 3, 1, 1, 3, 1, 1)`” | displayed finite probe, not a derived scale |
| “`G+`-equivariant” | covariance under the axiom's proper cubic rotations |
| “population variance on 62 nonzero sites” | explicit estimator and domain in Theorem 2 |
| “strictly below” the ell^1 variance | Theorem 2; displayed, not adopted |
| “not a leftover” of the minimizer identity or of the wrong map | Theorem 1; the six-type shells are new |
| “Displayed, not adopted” | Theorem 3; no Admissibility edit |

### N4 — citation-to-residual matching

| Evidence path:line | Residual attacked | Residual claimed closed | Match? |
|---|---|---|---:|
| `docs/MINIMAL_AXIOMS_2026-06-29.md:37` | ambient lattice and proper cubic rotations | `Z^3` nearest-neighbor graph and `G+` | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:57` | Admissibility covariance | one fixed covariant nearest-neighbor rule; no hop cost supplied | yes; cost stays displayed |
| `scripts/cost3_best_reversal_isochrone_2026_08_15.py:319` | eight pair orbits and the named filling | weights and `c = (3, 1, 3, 1, 1, 3, 1, 1)` | yes |
| `scripts/cost3_best_reversal_isochrone_2026_08_15.py:329` | `t(3,0,0)` and `t(1,1,1)` | times `9` and `5` | yes |
| `scripts/cost3_best_reversal_isochrone_2026_08_15.py:334` | `t(v)` on every site-type | the six orbit times of Theorem 1 | yes |
| `scripts/cost3_best_reversal_isochrone_2026_08_15.py:366` | population variance versus ell^1 | minkbest digits, strictly below | yes |
| `scripts/cost3_best_reversal_isochrone_2026_08_15.py:388` | adoption of a cost | note and axiom keep the cost out of Admissibility | yes |

No evidence citation is used to claim a path-length axiom, a continuum
metric, or an Admissibility rewrite.

### N5 — rhetoric and resolution audit

| Resolution | Executed? | Narrow negative supported? |
|---|---:|---|
| per element | yes: each directed `B_3(0)` edge | one inward occupancy pair; no other edge family is classified |
| per site | yes: `t(v)` and `|v|_2 / t` at each of the 62 nonzero sites | no other occupancy dictionary is used |
| per mode | yes: six site-types and the one variance-minimizing filling | other fillings and larger balls are untested and unclaimed |
| per block | yes: the population variance on the 62 nonzero sites | closeness is the stated variance test only |
| lattice wide | no | no Admissibility cost and no path-length law are adopted |

The runner prints the same five resolution statements.

### N6 — partial-closure and primitive scan

The only dependency used is the registered `minimal_axioms` node. No
approved primitive supplies a two-end occupancy hop cost, an isochrone, or
a Euclidean sphere law, and none is reclassified as an import or wall.
The scale-reference primitive is a units conversion only. The
kinetic-isotropy primitive supplies `c_t = c_s` as a graining ratio, not a
spatial isochrone. The realized-state primitive supplies pointwise
evaluation of a realized state, not a hop cost.

Two partial-closure mechanisms are recorded rather than suppressed. The
minimizer identity names `c` and the two-point times but does not compute
the six-type Euclidean-ratio table. The lex-first reversal isochrones are
a different filling (the wrong map) and mix two site-types into one shell.
The remaining physical choice—whether any hop cost belongs in
Admissibility—stays explicit and does not require an axiom edit.

### N7 — hostile steelman

The strongest objection is that naming the variance-minimizing filling and
the two-point times `t(3,0,0) = 9`, `t(1,1,1) = 5` already is the
isochrone report, so a six-type table is ornament. The objection correctly
notes that those two numbers are part of the table. It fails because the
isochrone residual asks whether every `t = const` shell is a Euclidean
radius. That is a statement about all six types: the axis types share
ratio `1/3`, while `(1,1,0)`, `(1,1,1)`, and `(2,1,0)` occupy distinct
shells at `√2 / 4`, `√3 / 5`, and `√5 / 7`. The two-point identity does
not exhibit those shells, and the wrong map mixes two of them.

### N8 — cross-cycle echo

The live axiom memo is the only load-bearing parent. Nearby covariance
language is context.

| Earlier surface | Similar issue | Mechanism considered here |
|---|---|---|
| `docs/MINIMAL_AXIOMS_2026-06-29.md` | proper cubic covariance of the nearest-neighbor rule | used as `G+` equivariance of the displayed cost; the rule itself is not replaced |
| minimizer identity of `c = (3, 1, 3, 1, 1, 3, 1, 1)` | same filling, two-point times | counted as a strictly smaller residual; Theorem 1 reports the six-type shells |
| lex-first reversal isochrones | same eight orbits, wrong map | a different filling; mixed shell; not this table |

No earlier mechanism retires the six-type Euclidean-ratio table, the
variance comparison, or the adoption refusal.

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

The companion runner builds the 24 proper cubic rotations, the 63-site ball,
and the 228 directed edges; applies the variance-minimizing filling
`(3, 1, 3, 1, 1, 3, 1, 1)`; computes `t(v)` on every site-type; reports
`|v|_2 / t` and that the `t = const` shells are the Euclidean-ratio table;
compares the two population variances; rejects the mutation families,
including the minimizer-identity leftover and the wrong-map leftover; and
verifies that the live axiom memo does not host the displayed cost.
Declared audit inputs are this note and the axiom memo.
