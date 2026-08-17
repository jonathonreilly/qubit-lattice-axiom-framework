---
claim_id: named_hopcost_b6_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On B_6(0), the named equal-weight hop-cost is scored for diamond order at (4,0,0) vs (2,2,2) and for var(|v|_2/t) vs ℓ¹. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/named_hopcost_b6_2026_08_15.py
---

# Named Equal-Weight Hop-Cost Scored On `B_6(0)`

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact integer path costs of one displayed named rule on the
radius-6 nearest-neighbor ball of one seed; diamond order at `(4,0,0)`
versus `(2,2,2)` and population variance of `|v|_2/t(v)` on the 376
nonzero sites. Displayed, not adopted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/named_hopcost_b6_2026_08_15.py`](../scripts/named_hopcost_b6_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

Let `B_6(0)` be the set of sites of `Z^3` reachable from the origin by at
most six nearest-neighbor steps. This is the 377-site ball. One-seed growth
starts at `0`. The occupancy `σ_n` at a site `n` is the 6-bit string whose
direction-`d` bit is set exactly when the neighbor of `n` in direction `d` is
strictly nearer the seed. This is the inward occupation of the one-seed
front.

`G+` is the 24-element group of proper cubic rotations about the seed.
Arrival time `t(n)` is the minimum path cost from `0` to `n` through
`B_6(0)`.

The named rule `ρ` assigns a hop cost on every inward occupancy pair that
appears in `B_6`:

```text
c(σ_v, σ_w) = 3  if |σ_v| = |σ_w| or |σ_v| = 0,
c(σ_v, σ_w) = 1  otherwise.
```

Equal inward weight or seed-exit costs `3`; every other inward pair costs
`1`. The nine inward-weight pairs realized on `B_6(0)` are

```text
(0,1), (1,0), (1,1), (1,2), (2,1), (2,2), (2,3), (3,2), (3,3).
```

This note scores that named rule on `B_6(0)`. It does not rescan the
`3^8 = 6561` fillings. The comparison is not a leftover of the `B_4`
score: the ball is a different ball, and `(2,2,2)` first appears here.

One Dijkstra capped at the 377-site ball gives

```text
t(4,0,0) = 12,  t(6,0,0) = 18,  t(2,2,2) = 14.
```

Diamond reverse at this scale is tested two ways. The explicit scale
inequality `3 t(4,0,0)^2 > 16 t(2,2,2)^2` fails: `432 > 3136` is false.
The same axis/body-diagonal order used on `B_3`, now using `(4,0,0)` and
`(2,2,2)`, is `|v|_2^2`-normalized comparison
`12 t(4,0,0)^2 > 16 t(2,2,2)^2`, equivalently
`t(4,0,0)^2 / 16 > t(2,2,2)^2 / 12`. That also fails: `1728 > 3136` is
false. So diamond does not reverse at this scale.

On the 376 sites of `B_6(0) \ {0}`, write `r(v) = |v|_2 / t(v)` and let
`var` be the population variance

```text
var(r) = (1/376) sum_v (r(v) - mean(r))^2.
```

The named rule has

```text
var_ρ = 0.00067960829822.
```

The ell^1 filling `t(v) = |v|_1` on the same sites has

```text
var_ell1 = 0.01350203761919.
```

So `var_ρ` is strictly below the ell^1 variance. Displayed, not adopted.
The note does not attach ell^1, and it does not attach `ρ`, as a
path-length law.

## Exact Theorems

### Theorem 1

The directed nearest-neighbor edges of `B_6(0)` carry nine inward-weight
pairs of occupancies, the eight pairs already seen on `B_3(0)` together
with the equal-weight pair `(3,3)`. The named rule assigns every pair:
seed-exit `(0,1)` costs `3`, equal-weight pairs cost `3`, and unequal
pairs cost `1`. In particular `ρ(3,3) = 3`.

One Dijkstra on the 377-site ball yields

```text
t(4,0,0) = 12,  t(6,0,0) = 18,  t(2,2,2) = 14.
```

The body-diagonal site `(2,2,2)` is a site of `B_6(0)`
(`|(2,2,2)|_1 = 6`). Diamond reverse at this scale is the pair
`((4,0,0),(2,2,2))`. The explicit test `3 t(4,0,0)^2 > 16 t(2,2,2)^2`
does not hold. The same axis/body-diagonal order used on `B_3`, now using
`(4,0,0)` and `(2,2,2)`, is the comparison of `t^2 / |v|_2^2`; it also
does not reverse. Diamond does not reverse at this scale.

The axis path `0 → (1,0,0) → (2,0,0) → (3,0,0) → (4,0,0) → (5,0,0) → (6,0,0)`
costs `3+3+3+3+3+3 = 18`. The body-diagonal path
`0 → (1,0,0) → (1,1,0) → (1,1,1) → (2,1,1) → (2,2,1) → (2,2,2)` costs
`3+1+1+3+3+3 = 14`.

### Theorem 2

On the 376 nonzero sites of `B_6(0)`, the population variance of
`|v|_2/t(v)` for the named rule is `0.00067960829822`. For the
ell^1 filling `t = |·|_1` on the same sites the same variance is
`0.01350203761919`. The named rule is therefore strictly below
ell^1 on this ball.

The `G+` site-types in `B_6(0)` arrive at

```text
t(1,0,0) = 3,   t(1,1,0) = 4,   t(1,1,1) = 5,
t(2,0,0) = 6,   t(2,1,0) = 7,   t(2,1,1) = 8,
t(2,2,0) = 10,  t(2,2,1) = 11,  t(2,2,2) = 14,
t(3,0,0) = 9,   t(3,1,0) = 10,  t(3,1,1) = 11,
t(3,2,0) = 13,  t(3,2,1) = 14,  t(3,3,0) = 16,
t(4,0,0) = 12,  t(4,1,0) = 13,  t(4,1,1) = 14,
t(4,2,0) = 16,  t(5,0,0) = 15,  t(5,1,0) = 16,
t(6,0,0) = 18.
```

The six axis types satisfy `t = 3 |v|_2` exactly. That is why the variance
remains more than an order of magnitude below ell^1, even though the
body-diagonal type `(2,2,2)` sits off that ratio. The comparison is scored
on `B_6(0)` only. It is not a leftover of the `B_4` score: the balls are a
different ball, and the 376-site list is not the 128-site list. The site
`(2,2,2)` is new.

### Theorem 3

The named rule is displayed as a finite probe on `B_6(0)`. It is
not written into Admissibility. No path-length law is attached. The note
does not attach ell^1 or the displayed rule as a law. The live axiom memo
continues to state that there is one fixed nearest-neighbor admissibility
rule, covariant under translations and proper cubic rotations; that rule is
not replaced by `c(σ_v, σ_w)`. Displayed, not adopted.

## Proof-Obligation Graph

| Obligation | Disposition |
|---|---|
| name `B_6(0)` as the 377-site ball | closed by the nearest-neighbor graph of `Z^3` |
| define inward occupancy of the one-seed front | closed: a bit is set exactly on a strictly nearer neighbor |
| count `G+` | closed: 24 proper cubic rotations |
| name `ρ` on every inward occupancy pair in `B_6` | closed: cost `3` iff equal weight or seed-exit, else `1` |
| report `t(4,0,0)`, `t(6,0,0)`, and `t(2,2,2)` | closed by Theorem 1 |
| report diamond order at `(4,0,0)` vs `(2,2,2)` | closed by Theorem 1; it does not reverse |
| score `var(\|v\|_2/t(v))` versus ell^1 on `B_6(0) \ {0}` | closed by Theorem 2; named rule strictly below ell^1 |
| treat the B_4 score as the B_6 score | refused; different ball, new diagonal |
| rescan all 6561 fillings | refused; one named rule, one Dijkstra |
| write a cost into Admissibility | refused; Theorem 3 |
| attach a path-length law | refused; Theorem 3 |

The obligation graph is acyclic. Every leaf of the bounded comparison is
closed. Adoption of a cost or of a path-length law is not a proof leaf.

## Representative Values

| filling | `t(4,0,0)` | `t(6,0,0)` | `t(2,2,2)` | `var(\|v\|_2/t)` | diamond reverse? |
|---|---:|---:|---:|---:|---|
| ell^1, `t = \|·\|_1` | `4` | `6` | `6` | `0.01350203761919` | no |
| named `ρ` | `12` | `18` | `14` | `0.00067960829822` | no |

The table is an exact illustration of Theorems 1 and 2, not an adopted
dynamics.

## Framework Boundary

Admissibility supplies one fixed nearest-neighbor rule, covariant under
lattice translations and proper cubic rotations, and says that the local
distribution varies with nearest-neighbor conditions. It does not supply a
numerical hop cost on occupancy pairs. This note therefore treats
`c(σ_v, σ_w)` as a displayed probe, not as an axiom clause.

Record is not used. No formation site, formation rate, or readout value is
assigned to an unoccupied site. The seed is a theorem hypothesis for the
one-seed front, not a privileged physical site.

## Imports And Claim Boundary

| Item | Role | Provenance / status |
|---|---|---|
| `Z^3` nearest-neighbor adjacency and proper cubic rotations | ambient lattice | live axiom memo |
| one-seed front from `0` | theorem hypothesis | declared; no site is privileged in the axiom |
| `σ_n` as 6-bit inward occupation | occupancy used by the probe | defined from the one-seed front |
| named rule `ρ` | displayed hop cost on inward weights | mathematical input; not an axiom |
| diamond order on `((4,0,0),(2,2,2))` | the scale test pair on `B_6(0)` | declared; first ball that contains `(2,2,2)` |
| `var(\|v\|_2/t(v))` on `B_6(0) \ {0}` | displayed closeness to `t ∝ \|v\|_2` | computed; not a continuum metric |
| B_4 score of the B_3 8-tuple | context, not a load-bearing parent | different ball; `(2,2,2)` was absent |

There are no measured, fitted, literature, or observational inputs. A
continuum metric, a path-length axiom, and any cost written into
Admissibility remain outside the result.

## Mutations

1. Rescan all 6561 maps on `B_6(0)`: the residual asked only whether this
   named rule reverses the diamond at `(4,0,0)` versus `(2,2,2)` and
   whether its variance stays below ell^1. The runner does not rescan.
2. Treat the B_4 score as already the B_6 score: the balls are a
   different ball; `(2,2,2)` is new; Theorem 2 recomputes the 376-site
   variance.
3. Replace the scale pair by the B_3 pair `((3,0,0),(1,1,1))`: the residual
   asks for diamond order at this scale, now using `(4,0,0)` and
   `(2,2,2)`.
4. Replace population variance by a sample factor `1/375`: the scored set
   is the finite list of 376 sites, so the mean-square deviation uses
   `1/376`.
5. Run more than one Dijkstra or enlarge the graph past `B_6(0)`: the
   residual scores the 377-site ball with one Dijkstra.
6. Write `ρ` into Admissibility or attach a path-length law: the live axiom
   memo still states one fixed covariant nearest-neighbor rule and contains
   no two-end occupancy hop cost.

## What This Does Not Claim

- No cost is written into Admissibility.
- No path-length law is attached.
- The comparison is not scored outside `B_6(0)`.
- The B_6 score is not a leftover of the B_4 score (different ball).
- The note does not attach ell^1 as a law.
- No continuum metric is derived.
- No privileged physical seed is added to the Lattice axiom.
- No Record readout is assigned to a site without a record.
- The 6561-map family is not re-exhausted on this ball.

## No-Go Discipline Gate

The negative claim is only this: on `B_6(0)`, scoring the named
equal-weight hop-cost for diamond order at `(4,0,0)` versus `(2,2,2)` and
for `var(|v|_2/t)` versus ell^1 is not a leftover of the B_4 score, is not
an Admissibility clause, and does not attach a path-length law. It is not
a claim that the named rule belongs in the axiom, nor that it minimizes
any score on `B_6(0)`.

### N1 — materially distinct routes

| Route | Exact attack | Result and authority | Marker |
|---|---|---|---|
| leftover of the B_4 score | Argue that the 128-site 8-tuple score is already the 376-site named-rule score. | Theorem 2: different ball; `(2,2,2)` is new; `var_ρ = 0.00067960829822` is a new number. | **ATTEMPTED** |
| keep the B_3 pair | Treat diamond reverse as `t(3,0,0)` versus `t(1,1,1)` on this ball. | Theorem 1: the scale pair is `((4,0,0),(2,2,2))`; it does not reverse. | **ATTEMPTED** |
| attach ell^1 | Read the smaller named-rule variance as a path-length law. | Theorem 3: ell^1 is a displayed baseline, not attached. | **ATTEMPTED** |
| invent a tenth cost | Fold a pair that does not appear on `B_6(0)` into `ρ`. | Theorem 1: the nine realized weight pairs are all named by `ρ`. | **ATTEMPTED** |
| rescan 6561 fillings | Re-minimize variance on `B_6(0)`. | The residual scores one named rule; the runner does not rescan. | **ATTEMPTED** |
| adopt the named rule | Write `ρ` into Admissibility. | Theorem 3 and the live axiom memo: one fixed covariant nearest-neighbor rule, no hop cost. | **ATTEMPTED** |

### N2 — wall independence and collapse

There is one comparison and one adoption refusal, not a stack of independent
walls. The diamond-order witness and the variance comparison are two
certificates of the same B_6 scoring statement.

| Pair | First closes second? | Second closes first? | Disposition |
|---|---:|---:|---|
| diamond order / variance comparison | no: failure to reverse does not fix the 376-site variance | no: a smaller variance does not decide the scale pair | independent conclusions on one named rule |
| scoring statement / adoption refusal | no: a probe can fail to reverse and still beat ell^1 and still be refused as an axiom | no: refusing adoption does not decide the numbers | independent conclusions |

Path-length attachment is not counted as a third wall: Theorem 3 simply
does not attach one.

### N3 — hidden-condition scan

| Phrase or premise | Classification |
|---|---|
| “one-seed growth from `0`” | explicit theorem hypothesis; the Lattice axiom privileges no site |
| “inward occupation of the one-seed front” | defined from nearer neighbors; not an extra occupancy axiom |
| “named equal-weight hop-cost” | displayed finite probe, not a derived scale |
| “one Dijkstra capped at the 377-site ball” | the definition of `t` through `B_6(0)` |
| “`(2,2,2)` is a site” | exact `ℓ^1` radius `6` versus ball radius `6` |
| “same axis/body-diagonal order as B_3, now using `(4,0,0)` and `(2,2,2)`” | the scale test pair |
| “population variance on 376 sites” | the finite list `B_6(0) \ {0}` |
| “not a leftover” of the B_4 score | Theorems 1 and 2; different ball |
| “Displayed, not adopted” | Theorem 3; no Admissibility edit |

### N4 — citation-to-residual matching

| Evidence path:line | Residual attacked | Residual claimed closed | Match? |
|---|---|---|---:|
| `docs/MINIMAL_AXIOMS_2026-06-29.md:37` | ambient lattice and proper cubic rotations | `Z^3` nearest-neighbor graph and `G+` | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:57` | Admissibility covariance | one fixed covariant nearest-neighbor rule; no hop cost supplied | yes; cost stays displayed |
| `scripts/named_hopcost_b6_2026_08_15.py:300` | size of the scored ball | `B_6(0)` has 377 sites | yes |
| `scripts/named_hopcost_b6_2026_08_15.py:316` | arrival times of the scale sites | `t(4,0,0) = 12`, `t(6,0,0) = 18`, `t(2,2,2) = 14` | yes |
| `scripts/named_hopcost_b6_2026_08_15.py:321` | explicit scale reverse test | `3 t(4,0,0)^2 > 16 t(2,2,2)^2` fails | yes |
| `scripts/named_hopcost_b6_2026_08_15.py:326` | B_3 order on the scale pair | `(4,0,0)` vs `(2,2,2)` also fails to reverse | yes |
| `scripts/named_hopcost_b6_2026_08_15.py:354` | variance versus ell^1 | named rule strictly below ell^1 | yes |
| `scripts/named_hopcost_b6_2026_08_15.py:366` | leftover of the B_4 score | note states different ball | yes |
| `scripts/named_hopcost_b6_2026_08_15.py:374` | adoption of a cost | note and axiom keep the cost out of Admissibility | yes |

No evidence citation is used to claim a path-length axiom, a continuum
metric, or an Admissibility rewrite.

### N5 — rhetoric and resolution audit

| Resolution | Executed? | Narrow negative supported? |
|---|---:|---|
| per element | yes: each directed `B_6(0)` edge | nine named inward-weight pairs |
| per site | yes: `|v|_2/t(v)` on each nonzero site | no other occupancy dictionary is used |
| per mode | yes: the single named rule | the 6561-map family is not re-exhausted |
| per block | yes: diamond order and variance on `B_6(0) \ {0}` | closeness is the stated variance only |
| lattice wide | no | no Admissibility cost and no path-length law are adopted |

The runner prints the same five resolution statements.

### N6 — partial closure and primitive scan

The only dependency used is the registered `minimal_axioms` node. No
approved primitive supplies a two-end occupancy hop cost, and none is
reclassified as an import or wall.

Two partial-closure mechanisms are recorded rather than suppressed. The
B_4 score of the B_3 8-tuple is a strictly smaller-ball statement: it
does not score `B_6(0)` and cannot host `(2,2,2)`. Naming `ρ` on the
finite weight pairs is a strictly weaker statement: it does not decide
diamond order or the 376-site variance. The remaining physical
choice—whether any hop cost belongs in Admissibility—stays explicit and
does not require an axiom edit.

### N7 — hostile steelman

The strongest objection is that transporting the named rule from the B_3
8-tuple to `B_6(0)` is automatic leftover: the same seed-exit cost, the
same equal-weight cost, and the same axis path should make the larger-ball
score a corollary, including a continuing diamond reverse. The objection
correctly identifies that the axis types remain pinned to `t = 3 |v|_2`.
It fails because `B_6(0)` is a different finite list, first contains the
body-diagonal site `(2,2,2)`, and that site arrives at `t = 14`, which
is slower than the axis ratio. The 376-site variance and the failure of
both reverse tests are new certificates, not leftovers.

### N8 — cross-cycle echo

The live axiom memo is the only load-bearing parent. Nearby covariance
language is context.

| Earlier surface | Similar issue | Mechanism considered here |
|---|---|---|
| `docs/MINIMAL_AXIOMS_2026-06-29.md` | proper cubic covariance of the nearest-neighbor rule | used as `G+` equivariance of the displayed cost; the rule itself is not replaced |
| B_4 score of the B_3 8-tuple | same named costs, smaller ball, no `(2,2,2)` | scored as a strictly smaller-ball parent; Theorems 1 and 2 are not leftovers |
| existence of 405 reversing `{1,2,3}` fillings | eight B_3 orbits, existence only | not re-exhausted; this note scores one named rule |

No earlier mechanism retires the B_6 score or the adoption refusal.

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
ball; assigns the named equal-weight hop-cost on every inward occupancy
pair in `B_6`; runs one Dijkstra capped at `B_6(0)`; reports
`t(4,0,0) = 12`, `t(6,0,0) = 18`, and `t(2,2,2) = 14`; reports that
diamond does not reverse at this scale under either the explicit test or
the B_3 axis/body-diagonal order; compares `var(|v|_2/t)` to ell^1 on the
376 nonzero sites; rejects the mutation families, including leftover of
the B_4 score and a 6561 rescan; and verifies that the live axiom memo
does not host the displayed cost. Declared audit inputs are this note and
the axiom memo.
