---
claim_id: cost3_best_reversal_b4_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On B_4(0), the B_3 variance-minimizing reversing filling is scored for diamond order and for var(|v|_2/t) vs ℓ¹. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/cost3_best_reversal_b4_2026_08_15.py
---

# B_3 Variance-Minimizing Reversal Scored On `B_4(0)`

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact integer path costs of one displayed filling on the radius-4
nearest-neighbor ball of one seed; diamond order and population variance of
`|v|_2/t(v)` on the 128 nonzero sites. Displayed, not adopted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/cost3_best_reversal_b4_2026_08_15.py`](../scripts/cost3_best_reversal_b4_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

Let `B_4(0)` be the set of sites of `Z^3` reachable from the origin by at
most four nearest-neighbor steps. This is the 129-site ball. One-seed growth
starts at `0`. The occupancy `σ_n` at a site `n` is the 6-bit string whose
direction-`d` bit is set exactly when the neighbor of `n` in direction `d` is
strictly nearer the seed. This is the inward occupation of the one-seed
front.

`G+` is the 24-element group of proper cubic rotations about the seed. A hop
cost `c(σ_v, σ_w) ∈ {1,2,3}` on a directed nearest-neighbor edge `v → w` is
`G+`-equivariant when it is constant on `G+` orbits of endpoint pairs.
Arrival time `t(n)` is the minimum path cost from `0` to `n` through
`B_4(0)`.

The eight `G+` orbits of inward occupancy pairs used on `B_3(0)`, in the
order used below, are the inward-weight pairs

```text
(0,1), (1,0), (1,1), (1,2), (2,1), (2,2), (2,3), (3,2).
```

The displayed filling is the `B_3(0)` lex-first minimizer of
`var(|v|_2/t(v))` among the 405 diamond-reversing `{1,2,3}` assignments of
those eight orbits,

```text
c = (3, 1, 3, 1, 1, 3, 1, 1).
```

This note scores that same 8-tuple on `B_4(0)`. It does not rescan the
`3^8 = 6561` fillings. The comparison is not a leftover of the `B_3`
minimum: the ball is a different ball.

On this filling, Dijkstra capped at the 129-site ball gives
`t(4,0,0) = 12`. The body-diagonal site `(2,2,2)` is not a site of
`B_4(0)` (`|(2,2,2)|_1 = 6`). The same axis/body-diagonal pair used on
`B_3(0)` remains available and still reverses:

```text
t(3,0,0) = 9,  t(1,1,1) = 5,  3·81 = 243 > 9·25 = 225.
```

On the 128 sites of `B_4(0) \ {0}`, write `r(v) = |v|_2 / t(v)` and let
`var` be the population variance

```text
var(r) = (1/128) sum_v (r(v) - mean(r))^2.
```

The displayed filling has

```text
var_c = 0.00035024862901.
```

The ell^1 filling `t(v) = |v|_1` on the same sites has

```text
var_ell1 = 0.01771035124177.
```

So `var_c` is strictly below the ell^1 variance. Displayed, not adopted. The
note does not attach ell^1, and it does not attach `c`, as a path-length
law.

## Exact Theorems

### Theorem 1

The directed nearest-neighbor edges of `B_3(0)` carry exactly eight `G+`
orbits of endpoint occupancy pairs, with inward-weight representatives as
above. Those eight orbits persist on `B_4(0)`. The 129-site ball also
carries one new orbit, the inward-weight pair `(3,3)`, realized on 48
directed edges joining two weight-3 sites (for example `(1,1,1)` and
`(2,1,1)`). The displayed 8-tuple does not assign that new orbit.

Assigning the eight B_3 costs and omitting the new orbit, or assigning the
new orbit any cost at least `3`, yields the same arrival table on every
site of `B_4(0)`. In particular

```text
t(4,0,0) = 12.
```

The site `(2,2,2)` is not a site of `B_4(0)`, so the comparison
`3 t(4,0,0)^2 > 16 t(2,2,2)^2` is not a statement on this ball. The same
axis/body-diagonal order used on `B_3(0)` is the pair `((3,0,0),(1,1,1))`.
It still reverses: `t(3,0,0) = 9`, `t(1,1,1) = 5`, and
`3 t(3,0,0)^2 > 9 t(1,1,1)^2`.

The axis path `0 → (1,0,0) → (2,0,0) → (3,0,0) → (4,0,0)` costs
`3+3+3+3 = 12`. The body-diagonal path
`0 → (1,0,0) → (1,1,0) → (1,1,1)` costs `3+1+1 = 5`.

### Theorem 2

On the 128 nonzero sites of `B_4(0)`, the population variance of
`|v|_2/t(v)` for the displayed filling is `0.00035024862901`. For the
ell^1 filling `t = |·|_1` on the same sites the same variance is
`0.01771035124177`. The displayed filling is therefore strictly below
ell^1 on this ball.

The `G+` site-types in `B_4(0)` arrive at

```text
t(1,0,0) = 3,  t(1,1,0) = 4,  t(1,1,1) = 5,
t(2,0,0) = 6,  t(2,1,0) = 7,  t(2,1,1) = 8,
t(2,2,0) = 10, t(3,0,0) = 9,  t(3,1,0) = 10,
t(4,0,0) = 12.
```

The four axis types satisfy `t = 3 |v|_2` exactly. That is why the variance
remains two orders of magnitude below ell^1. The comparison is scored on
`B_4(0)` only. It is not a leftover of the `B_3` minimum: the balls are a
different ball, and the 128-site list is not the 62-site list.

### Theorem 3

The filling is displayed as a finite probe on `B_4(0)`. It is
not written into Admissibility. No path-length law is attached. The note
does not attach ell^1 or the displayed 8-tuple as a law. The live axiom memo
continues to state that there is one fixed nearest-neighbor admissibility
rule, covariant under translations and proper cubic rotations; that rule is
not replaced by `c(σ_v, σ_w)`. Displayed, not adopted.

## Proof-Obligation Graph

| Obligation | Disposition |
|---|---|
| name `B_4(0)` as the 129-site ball | closed by the nearest-neighbor graph of `Z^3` |
| define inward occupancy of the one-seed front | closed: a bit is set exactly on a strictly nearer neighbor |
| count `G+` | closed: 24 proper cubic rotations |
| keep the same eight `G+` orbits and the same 8-tuple | closed by Theorem 1 |
| report `t(4,0,0)` and the status of `(2,2,2)` | closed by Theorem 1; `(2,2,2)` is not a site |
| report the B_3 axis/diagonal order on this ball | closed by Theorem 1; it still reverses |
| score `var(\|v\|_2/t(v))` versus ell^1 on `B_4(0) \ {0}` | closed by Theorem 2; filling strictly below ell^1 |
| treat the B_3 minimum as the B_4 score | refused; different ball |
| rescan all 6561 fillings | refused; one displayed 8-tuple |
| write a cost into Admissibility | refused; Theorem 3 |
| attach a path-length law | refused; Theorem 3 |

The obligation graph is acyclic. Every leaf of the bounded comparison is
closed. Adoption of a cost or of a path-length law is not a proof leaf.

## Representative Values

| filling | `t(4,0,0)` | `t(3,0,0)` | `t(1,1,1)` | `var(\|v\|_2/t)` | B_3 diamond? |
|---|---:|---:|---:|---:|---|
| ell^1, `t = \|·\|_1` | `4` | `3` | `3` | `0.01771035124177` | yes |
| displayed `(3, 1, 3, 1, 1, 3, 1, 1)` | `12` | `9` | `5` | `0.00035024862901` | no |

The site `(2,2,2)` is absent from both rows. The table is an exact
illustration of Theorems 1 and 2, not an adopted dynamics.

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
| eight `G+` orbits of occupancy pairs | same orbits as the `B_3` probe | rebuilt here from `B_3(0)` edges |
| `c = (3, 1, 3, 1, 1, 3, 1, 1)` | displayed filling | mathematical input; not an axiom |
| diamond order on `((3,0,0),(1,1,1))` | the B_3 test pair, scored on `B_4(0)` | declared; `(2,2,2)` is not a site |
| `var(\|v\|_2/t(v))` on `B_4(0) \ {0}` | displayed closeness to `t ∝ \|v\|_2` | computed; not a continuum metric |
| B_3 variance minimum | context, not a load-bearing parent | different ball; not a leftover |

There are no measured, fitted, literature, or observational inputs. A
continuum metric, a path-length axiom, and any cost written into
Admissibility remain outside the result.

## Mutations

1. Rescan all 6561 maps on `B_4(0)`: the residual asked only whether this
   displayed 8-tuple still reverses and whether its variance stays below
   ell^1. The runner does not rescan.
2. Treat the B_3 minimum as already the B_4 score: the balls are a
   different ball; Theorem 2 recomputes the 128-site variance.
3. Evaluate `3 t(4,0,0)^2 > 16 t(2,2,2)^2` as a statement on `B_4(0)`:
   `(2,2,2)` is not a site of the 129-site ball.
4. Replace population variance by a sample factor `1/127`: the scored set
   is the finite list of 128 sites, so the mean-square deviation uses
   `1/128`.
5. Assign an unstated ninth cost to the new `(3,3)` orbit and treat it as
   part of the 8-tuple: Theorem 1 records the orbit as unused by `c`.
6. Write `c` into Admissibility or attach a path-length law: the live axiom
   memo still states one fixed covariant nearest-neighbor rule and contains
   no two-end occupancy hop cost.

## What This Does Not Claim

- No cost is written into Admissibility.
- No path-length law is attached.
- The comparison is not scored outside `B_4(0)`.
- The B_4 score is not a leftover of the B_3 minimum (different ball).
- The note does not attach ell^1 as a law.
- No continuum metric is derived.
- No privileged physical seed is added to the Lattice axiom.
- No Record readout is assigned to a site without a record.
- The 6561-map family is not re-exhausted on this ball.

## No-Go Discipline Gate

The negative claim is only this: on `B_4(0)`, scoring the B_3
variance-minimizing reversing filling for diamond order and for
`var(|v|_2/t)` versus ell^1 is not a leftover of the B_3 minimum, is not
an Admissibility clause, and does not attach a path-length law. It is not
a claim that the 8-tuple belongs in the axiom, nor that it minimizes any
score on `B_4(0)`.

### N1 — materially distinct routes

| Route | Exact attack | Result and authority | Marker |
|---|---|---|---|
| leftover of the B_3 minimum | Argue that the 62-site minimizer is already the 128-site score. | Theorem 2: different ball; `var_c = 0.00035024862901` is a new number. | **ATTEMPTED** |
| evaluate `t(2,2,2)` on `B_4(0)` | Treat `3 t(4,0,0)^2 > 16 t(2,2,2)^2` as a B_4 statement. | Theorem 1: `(2,2,2)` is not a site. | **ATTEMPTED** |
| attach ell^1 | Read the smaller filling variance as a path-length law. | Theorem 3: ell^1 is a displayed baseline, not attached. | **ATTEMPTED** |
| invent a ninth cost | Fold the new `(3,3)` orbit into the 8-tuple. | Theorem 1: that orbit is unused by `c`; cost `≥ 3` does not change times. | **ATTEMPTED** |
| rescan 6561 fillings | Re-minimize variance on `B_4(0)`. | The residual scores one displayed filling; the runner does not rescan. | **ATTEMPTED** |
| adopt the filling | Write `c` into Admissibility. | Theorem 3 and the live axiom memo: one fixed covariant nearest-neighbor rule, no hop cost. | **ATTEMPTED** |

### N2 — wall independence and collapse

There is one comparison and one adoption refusal, not a stack of independent
walls. The diamond-order witness and the variance comparison are two
certificates of the same B_4 scoring statement.

| Pair | First closes second? | Second closes first? | Disposition |
|---|---:|---:|---|
| diamond order / variance comparison | no: reversal does not fix the 128-site variance | no: a smaller variance does not decide the B_3 pair | independent conclusions on one filling |
| scoring statement / adoption refusal | no: a probe can reverse and beat ell^1 and still be refused as an axiom | no: refusing adoption does not decide the numbers | independent conclusions |

Path-length attachment is not counted as a third wall: Theorem 3 simply
does not attach one.

### N3 — hidden-condition scan

| Phrase or premise | Classification |
|---|---|
| “one-seed growth from `0`” | explicit theorem hypothesis; the Lattice axiom privileges no site |
| “inward occupation of the one-seed front” | defined from nearer neighbors; not an extra occupancy axiom |
| “same eight G+ orbits and same 8-tuple” | displayed finite probe, not a derived scale |
| “BFS capped at the 129-site ball” | the definition of `t` through `B_4(0)` |
| “`(2,2,2)` is not a site” | exact `ℓ^1` radius `6` versus ball radius `4` |
| “same axis/body-diagonal order as B_3” | the pair `((3,0,0),(1,1,1))` |
| “population variance on 128 sites” | the finite list `B_4(0) \ {0}` |
| “not a leftover” of the B_3 minimum | Theorems 1 and 2; different ball |
| “Displayed, not adopted” | Theorem 3; no Admissibility edit |

### N4 — citation-to-residual matching

| Evidence path:line | Residual attacked | Residual claimed closed | Match? |
|---|---|---|---:|
| `docs/MINIMAL_AXIOMS_2026-06-29.md:37` | ambient lattice and proper cubic rotations | `Z^3` nearest-neighbor graph and `G+` | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:57` | Admissibility covariance | one fixed covariant nearest-neighbor rule; no hop cost supplied | yes; cost stays displayed |
| `scripts/cost3_best_reversal_b4_2026_08_15.py:300` | size of the scored ball | `B_4(0)` has 129 sites | yes |
| `scripts/cost3_best_reversal_b4_2026_08_15.py:321` | arrival time of the axis site | `t(4,0,0) = 12` | yes |
| `scripts/cost3_best_reversal_b4_2026_08_15.py:326` | status of `(2,2,2)` | not a site of the 129-site ball | yes |
| `scripts/cost3_best_reversal_b4_2026_08_15.py:331` | B_3 diamond order on this ball | `t(3,0,0) = 9`, `t(1,1,1) = 5`, still reverses | yes |
| `scripts/cost3_best_reversal_b4_2026_08_15.py:364` | variance versus ell^1 | filling strictly below ell^1 | yes |
| `scripts/cost3_best_reversal_b4_2026_08_15.py:376` | leftover of the B_3 minimum | note states different ball | yes |
| `scripts/cost3_best_reversal_b4_2026_08_15.py:383` | adoption of a cost | note and axiom keep the cost out of Admissibility | yes |

No evidence citation is used to claim a path-length axiom, a continuum
metric, or an Admissibility rewrite.

### N5 — rhetoric and resolution audit

| Resolution | Executed? | Narrow negative supported? |
|---|---:|---|
| per element | yes: each directed `B_4(0)` edge | eight B_3 orbits plus one unused `(3,3)` orbit |
| per site | yes: `|v|_2/t(v)` on each nonzero site | no other occupancy dictionary is used |
| per mode | yes: the single displayed filling | the 6561-map family is not re-exhausted |
| per block | yes: diamond order and variance on `B_4(0) \ {0}` | closeness is the stated variance only |
| lattice wide | no | no Admissibility cost and no path-length law are adopted |

The runner prints the same five resolution statements.

### N6 — partial closure and primitive scan

The only dependency used is the registered `minimal_axioms` node. No
approved primitive supplies a two-end occupancy hop cost, and none is
reclassified as an import or wall.

Two partial-closure mechanisms are recorded rather than suppressed. The
B_3 variance minimum is a strictly smaller-ball statement: it does not
score `B_4(0)`. Existence of 405 reversals on `B_3(0)` is a strictly
weaker statement: it does not select this 8-tuple on `B_4(0)`. The
remaining physical choice—whether any hop cost belongs in
Admissibility—stays explicit and does not require an axiom edit.

### N7 — hostile steelman

The strongest objection is that transporting the B_3 minimizer to `B_4(0)`
is automatic leftover: the same eight costs, the same seed, and the same
axis path should make the larger-ball score a corollary. The objection
correctly identifies that the axis types remain pinned to `t = 3 |v|_2`.
It fails because `B_4(0)` is a different finite list, introduces the new
site-types `(2,1,1)`, `(2,2,0)`, `(3,1,0)`, and `(4,0,0)`, and cannot host
`(2,2,2)`. The 128-site variance and the status of the B_3 test pair are
new certificates, not leftovers.

### N8 — cross-cycle echo

The live axiom memo is the only load-bearing parent. Nearby covariance
language is context.

| Earlier surface | Similar issue | Mechanism considered here |
|---|---|---|
| `docs/MINIMAL_AXIOMS_2026-06-29.md` | proper cubic covariance of the nearest-neighbor rule | used as `G+` equivariance of the displayed cost; the rule itself is not replaced |
| B_3 variance minimum of the same 8-tuple | same filling, smaller ball | scored as a strictly smaller-ball parent; Theorem 2 is not a leftover |
| existence of 405 reversing `{1,2,3}` fillings | same eight orbits, existence only | not re-exhausted; this note scores one displayed filling |

No earlier mechanism retires the B_4 score or the adoption refusal.

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

The companion runner builds the 24 proper cubic rotations, the 129-site
ball, and the eight B_3 occupancy-pair orbits; assigns the displayed
8-tuple; caps Dijkstra at `B_4(0)`; reports `t(4,0,0) = 12` and that
`(2,2,2)` is not a site; reports that the B_3 axis/diagonal pair still
reverses; compares `var(|v|_2/t)` to ell^1 on the 128 nonzero sites;
rejects the mutation families, including leftover of the B_3 minimum and
a 6561 rescan; and verifies that the live axiom memo does not host the
displayed cost. Declared audit inputs are this note and the axiom memo.
