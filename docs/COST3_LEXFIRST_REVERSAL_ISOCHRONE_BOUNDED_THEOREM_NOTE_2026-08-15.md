---
claim_id: cost3_lexfirst_reversal_isochrone_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On B_3(0), the isochrones of the lex-first diamond-reversing {1,2,3} two-end occupancy cost are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/cost3_lexfirst_reversal_isochrone_2026_08_15.py
---

# Isochrones Of The Lex-First Diamond-Reversing `{1,2,3}` Two-End Cost On `B_3(0)`

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact integer path costs and a displayed variance comparison on the
radius-3 nearest-neighbor ball of one seed. Displayed, not adopted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/cost3_lexfirst_reversal_isochrone_2026_08_15.py`](../scripts/cost3_lexfirst_reversal_isochrone_2026_08_15.py)
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

The lex-first diamond-reversing filling of those orbits is constructed by
the named rule seed-exit `1`, axis-extension `3`, else `1`:

```text
c = (1, 1, 3, 1, 1, 1, 1, 1).
```

On `B_3(0)` this filling realizes `t(3,0,0) = 7` and `t(1,1,1) = 3`. The
seven `G+` site types have constant arrival times, listed in Theorem 1.
Among the 62 sites with `t(v) > 0`, the population variance of
`|v|_2 / t(v)` is `0.022275669698`, while the same variance with the
`ℓ¹` radius `|v|_1` (graph radius) in place of `t` is `0.020739455142`.
The graph-radius variance is smaller. The `t = const` shells of this
filling are therefore not closer to Euclidean spheres, by this displayed
ratio test, than the `ℓ¹` shells. The comparison is reported on `B_3(0)` only.
Displayed, not adopted.

The report is not a leftover of the existence of a reversing filling. That
existence names 405 maps and one lex-first witness. It does not compute
`t(v)` on every site or compare isochrones to graph-radius shells.

## Exact Theorems

### Theorem 1

`B_3(0)` has 63 sites and 228 directed nearest-neighbor edges. Under the
lex-first filling, arrival time is constant on each `G+` orbit of sites.
The seven orbits and their times are

| representative | orbit size | `t` | `|v|_2` | graph radius |
|---|---:|---:|---|---:|
| `(0,0,0)` | `1` | `0` | `0` | `0` |
| `(1,0,0)` | `6` | `1` | `1` | `1` |
| `(1,1,0)` | `12` | `2` | `√2` | `2` |
| `(2,0,0)` | `6` | `4` | `2` | `2` |
| `(1,1,1)` | `8` | `3` | `√3` | `3` |
| `(2,1,0)` | `24` | `3` | `√5` | `3` |
| `(3,0,0)` | `6` | `7` | `3` | `3` |

In particular `t(1,0,0) = 1`, `t(1,1,0) = 2`, `t(2,0,0) = 4`,
`t(2,1,0) = 3`, `t(1,1,1) = 3`, and `t(3,0,0) = 7`. The six seed-exit
edges occupy orbit `(0,1)` of cost `1`. Both axis extensions occupy orbit
`(1,1)` of cost `3`. The three-step body-diagonal path uses only cost-`1`
hops. The unique in-ball neighbor of `(3,0,0)` is `(2,0,0)`, so
`t(3,0,0) = t(2,0,0) + 3 = 7`. The face site `(2,1,0)` is reached by
`0 → (1,0,0) → (1,1,0) → (2,1,0)` at total cost `3`.

The constant-`t` shells are therefore

```text
t=1 : 6 sites of type (1,0,0)
t=2 : 12 sites of type (1,1,0)
t=3 : 32 sites, 8 of type (1,1,1) and 24 of type (2,1,0)
t=4 : 6 sites of type (2,0,0)
t=7 : 6 sites of type (3,0,0)
```

Every shell except `t = 3` is a single `G+` site type, hence a single
Euclidean radius. The mixed `t = 3` shell carries two radii, `√3` and `√5`.

### Theorem 2

Let `S` be the 62 sites of `B_3(0)` with `t(v) > 0`. Write `|v|_2` for the
ordinary Euclidean radius `√(x^2+y^2+z^2)`. The population variance

```text
Var(a) = (1/|S|) Σ_{v in S} (a(v) - mean(a))^2
```

on the two displayed ratio fields is

```text
Var(|v|_2 / t(v))     = 0.022275669698
Var(|v|_2 / |v|_1)    = 0.020739455142
```

The graph-radius variance is smaller. Unit hop costs recover `|v|_1` on
every site of `B_3(0)`, so the second field is the isochrone ratio of the
constant-`1` filling (the `ℓ¹` comparator). By this displayed test the
lex-first reversing cost does not make the `t = const` shells closer to
Euclidean spheres than the `ℓ¹` shells.

The axis overshoot is visible in the ratios themselves: `(3,0,0)` has
`|v|_2 / t = 3/7`, while `(1,0,0)` has ratio `1`. Graph radius keeps every
axis site at ratio `1` and the body diagonal at `√3/3`. Reversal of the
diamond order at the two comparison points is therefore not the same as a
closer Euclidean shell. Displayed, not adopted.

### Theorem 3

The lex-first filling and its isochrones are displayed as a finite probe on
`B_3(0)`. They are not written into Admissibility. No path-length law is
attached; do not attach graph radius, Euclidean radius, or the filling `c`
as an axiom clause. The live axiom memo continues to state that there is
one fixed nearest-neighbor admissibility rule, covariant under translations
and proper cubic rotations; that rule is not replaced by `c(σ_v, σ_w)`.
Displayed, not adopted.

## Proof-Obligation Graph

| Obligation | Disposition |
|---|---|
| name `B_3(0)` and the six direction bits | closed by the nearest-neighbor graph of `Z^3` |
| define inward occupancy of the one-seed front | closed: a bit is set exactly on a strictly nearer neighbor |
| count `G+` | closed: 24 proper cubic rotations |
| name the eight pair orbits and the lex-first filling | closed by Theorem 1; `c = (1, 1, 3, 1, 1, 1, 1, 1)` |
| compute `t(v)` on every site | closed by Theorem 1; seven site types, 63 sites |
| confirm `t(3,0,0) = 7` and `t(1,1,1) = 3` | closed by Theorem 1 |
| compare the two population variances on `{t > 0}` | closed by Theorem 2; graph-radius variance is smaller |
| treat the table as leftover of reversal existence | refused; existence does not compute the 63-site table |
| write `c` into Admissibility | refused; Theorem 3 |
| attach a path-length law | refused; Theorem 3 |

The obligation graph is acyclic. Every leaf of the bounded comparison is
closed. Adoption of a cost or of a path-length law is not a proof leaf.

## Representative Values

| site type | `t` | `|v|_2 / t` | `|v|_2 /` graph radius |
|---|---:|---|---|
| `(1,0,0)` | `1` | `1` | `1` |
| `(1,1,0)` | `2` | `√2 / 2` | `√2 / 2` |
| `(2,0,0)` | `4` | `1/2` | `1` |
| `(1,1,1)` | `3` | `√3 / 3` | `√3 / 3` |
| `(2,1,0)` | `3` | `√5 / 3` | `√5 / 3` |
| `(3,0,0)` | `7` | `3/7` | `1` |

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
| lex-first `c = (1, 1, 3, 1, 1, 1, 1, 1)` | displayed `G+`-equivariant hop cost | mathematical input; not an axiom |
| `t(v)` on `B_3(0)` | min path cost under that filling | computed; Theorem 1 |
| `Var(\|v\|_2 / t)` versus `Var(\|v\|_2 /` graph radius`)` | displayed isochrone test | computed; Theorem 2 |
| existence of a reversing filling | context, not a load-bearing parent | existence does not determine the isochrones |

There are no measured, fitted, literature, or observational inputs. A
continuum metric, a path-length axiom, and any cost written into
Admissibility remain outside the result.

## Mutations

1. Collapse the 63-site table to the two comparison points `(3,0,0)` and
   `(1,1,1)`: that is the existence residual, not the isochrone residual.
2. Replace the lex-first filling by another of the 405 reversing maps: the
   named filling is seed-exit `1`, axis-extension `3`, else `1`.
3. Claim the `t = const` shells are closer to Euclidean spheres: the
   graph-radius variance is smaller.
4. Include the origin in the variance: `t(0) = 0` is excluded by the
   stated domain `{v : t(v) > 0}`.
5. Write `c` into Admissibility: the live axiom memo still states one
   fixed covariant nearest-neighbor rule and contains no two-end occupancy
   hop cost.
6. Attach a path-length law: Theorem 3 refuses both graph radius and
   Euclidean radius as axiom clauses.

## What This Does Not Claim

- No cost is written into Admissibility.
- No path-length law is attached.
- The comparison is not scored outside `B_3(0)`.
- The isochrone table is not a leftover of reversal existence.
- The lex-first filling is not claimed to minimize the displayed variance.
- No continuum Euclidean metric is derived.
- No privileged physical seed is added to the Lattice axiom.
- No Record readout is assigned to a site without a record.

## No-Go Discipline Gate

The negative claim is only this: on `B_3(0)`, the report of the lex-first
reversing isochrones is not a leftover of reversal existence, is not an
Admissibility clause, does not attach a path-length law, and does not make
the `t = const` shells closer to Euclidean spheres than graph-radius
shells by the displayed variance test. It is not a claim about any other
filling, any larger ball, or any adopted dynamics.

### N1 — materially distinct routes

| Route | Exact attack | Result and authority | Marker |
|---|---|---|---|
| existence leftover | Read `t(3,0,0) = 7` and `t(1,1,1) = 3` as already the isochrone report. | Theorem 1 computes all seven site types; the mixed `t = 3` shell is invisible at those two points. | **ATTEMPTED** |
| two-point ratio test | Compare only `3/7` and `√3/3` and declare Euclidean closeness. | Theorem 2 uses all 62 positive-`t` sites; graph-radius variance is smaller. | **ATTEMPTED** |
| drop the axis overshoot | Ignore `(2,0,0)` and `(3,0,0)` because the other types agree with graph radius. | Those six-plus-six sites are in `S`; they drive `|v|_2 / t` down to `1/2` and `3/7`. | **ATTEMPTED** |
| sample variance or include the origin | Change the estimator or divide by `t(0) = 0`. | The stated estimator is the population variance on `{t > 0}`; the origin is excluded. | **ATTEMPTED** |
| write the filling into Admissibility | Treat seed-exit `1` and axis-extension `3` as the covariant rule. | Theorem 3: the live axiom memo still states one fixed nearest-neighbor rule and no hop cost. | **ATTEMPTED** |
| attach a path-length law | Promote `t` or graph radius to an axiom-level length. | Theorem 3 refuses both; do not attach either. | **ATTEMPTED** |

### N2 — wall independence and collapse

There is one comparison and one adoption refusal, not a stack of independent
walls. The 63-site table and the variance comparison are two certificates of
the same isochrone report.

| Pair | First closes second? | Second closes first? | Disposition |
|---|---:|---:|---|
| 63-site table / variance comparison | no: the table does not by itself name a variance | no: a variance does not reconstruct the seven times | independent displayed facts in Theorems 1 and 2 |
| isochrone report / adoption refusal | no: a probe can be tabulated and still refused as an axiom | no: refusing adoption does not compute `t(v)` | independent conclusions |

Path-length attachment is not counted as a third wall: Theorem 3 simply
does not attach one.

### N3 — hidden-condition scan

| Phrase or premise | Classification |
|---|---|
| “one-seed growth from `0`” | explicit theorem hypothesis; the Lattice axiom privileges no site |
| “inward occupation of the one-seed front” | defined from nearer neighbors; not an extra occupancy axiom |
| “lex-first `c = (1, 1, 3, 1, 1, 1, 1, 1)`” | displayed finite probe, not a derived scale |
| “`G+`-equivariant” | covariance under the axiom's proper cubic rotations |
| “population variance on `{t > 0}`” | explicit estimator and domain in Theorem 2 |
| “graph-radius variance is smaller” | Theorem 2; displayed, not adopted |
| “not a leftover” of reversal existence | Theorem 1; the 63-site table is new |
| “Displayed, not adopted” | Theorem 3; no Admissibility edit |

### N4 — citation-to-residual matching

| Evidence path:line | Residual attacked | Residual claimed closed | Match? |
|---|---|---|---:|
| `docs/MINIMAL_AXIOMS_2026-06-29.md:37` | ambient lattice and proper cubic rotations | `Z^3` nearest-neighbor graph and `G+` | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:57` | Admissibility covariance | one fixed covariant nearest-neighbor rule; no hop cost supplied | yes; cost stays displayed |
| `scripts/cost3_lexfirst_reversal_isochrone_2026_08_15.py:313` | eight pair orbits and the named filling | weights and `c = (1, 1, 3, 1, 1, 1, 1, 1)` | yes |
| `scripts/cost3_lexfirst_reversal_isochrone_2026_08_15.py:323` | `t(3,0,0)` and `t(1,1,1)` | times `7` and `3` | yes |
| `scripts/cost3_lexfirst_reversal_isochrone_2026_08_15.py:328` | `t(v)` on every site type | the seven orbit times of Theorem 1 | yes |
| `scripts/cost3_lexfirst_reversal_isochrone_2026_08_15.py:351` | which variance is smaller | graph-radius variance is smaller | yes |
| `scripts/cost3_lexfirst_reversal_isochrone_2026_08_15.py:368` | adoption of a cost | note and axiom keep the cost out of Admissibility | yes |

No evidence citation is used to claim a path-length axiom, a continuum
metric, or an Admissibility rewrite.

### N5 — rhetoric and resolution audit

| Resolution | Executed? | Narrow negative supported? |
|---|---:|---|
| per element | yes: each directed `B_3(0)` edge | one inward occupancy pair; no other edge family is classified |
| per site | yes: `t(v)` at each of the 63 sites | no other occupancy dictionary is used |
| per mode | yes: seven site types and the one lex-first filling | other fillings and larger balls are untested and unclaimed |
| per block | yes: the two variances on the 62 positive-`t` sites | closeness is the stated variance test only |
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

Two partial-closure mechanisms are recorded rather than suppressed.
Existence of a reversing filling names the lex-first witness but does not
compute the 63-site table or the variance comparison. Unit hop costs
recover graph radius, which is used as the displayed comparator and is not
promoted to a path-length law. The remaining physical choice—whether any
hop cost belongs in Admissibility—stays explicit and does not require an
axiom edit.

### N7 — hostile steelman

The strongest objection is that diamond reversal at `(3,0,0)` versus
`(1,1,1)` already forces the `t = const` shells closer to Euclidean
spheres, so a 62-site variance is ornament. The objection correctly notes
that those two points move toward a common Euclidean radius in the
reversed order. It fails because the same filling sends `(2,0,0)` to
`t = 4` and `(3,0,0)` to `t = 7`, so the axis ratios drop to `1/2` and
`3/7`, while graph radius keeps every axis ratio at `1`. The 62-site
population variance is the hostile check of that overshoot, and
graph-radius variance is smaller.

### N8 — cross-cycle echo

The live axiom memo is the only load-bearing parent. Nearby covariance
language is context.

| Earlier surface | Similar issue | Mechanism considered here |
|---|---|---|
| `docs/MINIMAL_AXIOMS_2026-06-29.md` | proper cubic covariance of the nearest-neighbor rule | used as `G+` equivariance of the displayed cost; the rule itself is not replaced |
| existence of a reversing `{1,2,3}` filling | same eight orbits, same lex-first witness | counted as a strictly smaller residual; Theorems 1 and 2 compute the isochrones |
| unit hop costs / graph radius | constant-`1` isochrones | used as the displayed comparator; not attached as a path-length law |

No earlier mechanism retires the 63-site table, the variance comparison, or
the adoption refusal.

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
and the 228 directed edges; constructs the lex-first filling from seed-exit
`1` and axis-extension `3`; computes `t(v)` on every site; compares the two
population variances; rejects the mutation families, including the existence
leftover; and verifies that the live axiom memo does not host the displayed
cost. Declared audit inputs are this note and the axiom memo.
