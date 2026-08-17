---
claim_id: named_equal_weight_hopcost_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "The named rule cost=3 iff equal inward weight or seed-exit reproduces the minkbest 8-tuple and names the B_4 (3,3) orbit. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/named_equal_weight_hopcost_2026_08_15.py
---

# Named Equal-Weight Hop-Cost Versus The Minkbest 8-Tuple

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact comparison of one named local-in-weights hop-cost with the
displayed eight-orbit filling on the radius-4 nearest-neighbor ball of one
seed. Displayed, not adopted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/named_equal_weight_hopcost_2026_08_15.py`](../scripts/named_equal_weight_hopcost_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

Let `B_4(0)` be the set of sites of `Z^3` reachable from the origin by at
most four nearest-neighbor steps. This is the 129-site ball. One-seed growth
starts at `0`. The occupancy `σ_n` at a site `n` is the 6-bit string whose
direction-`d` bit is set exactly when the neighbor of `n` in direction `d` is
strictly nearer the seed. This is the inward occupation of the one-seed
front. Write `w_n = |σ_n|` for that Hamming weight.

`G+` is the 24-element group of proper cubic rotations about the seed. A hop
cost on a directed nearest-neighbor edge `v → w` is `G+`-equivariant when it
is constant on `G+` orbits of endpoint pairs. Arrival time `t(n)` is the
minimum path cost from `0` to `n` through `B_4(0)`.

The eight `G+` orbits of inward occupancy pairs used on `B_3(0)`, in the
order used below, are the inward-weight pairs

```text
(0,1), (1,0), (1,1), (1,2), (2,1), (2,2), (2,3), (3,2).
```

The displayed minkbest filling of those eight orbits is

```text
c = (3, 1, 3, 1, 1, 3, 1, 1).
```

`B_4(0)` grows one new orbit, the inward-weight pair `(3,3)`, realized on
48 directed edges. That ninth orbit is not named by the 8-tuple.

The named local-in-weights rule `rho` is the member clause

```text
cost 3 if w_v = w_w or w_v = 0, else cost 1.
```

Equal inward weight or seed-exit therefore costs 3; every other pair costs
1. This is a finite named rule on weights, not a per-radius leftover of the
8-tuple.

On the eight orbits, `rho` returns exactly `c`. In particular the new orbit
is named by `rho(3,3) = 3`. Uniqueness of `rho` is not claimed.

On `B_4(0)`, filling the eight orbits by `rho` and the new `(3,3)` orbit by
`rho(3,3) = 3` yields the same arrival table as omitting `(3,3)` or assigning
it any cost at least `3`. In particular `t(4,0,0) = 12`. The same
axis/body-diagonal pair used on `B_3(0)` still reverses:

```text
t(3,0,0) = 9,  t(1,1,1) = 5,  3·81 = 243 > 9·25 = 225.
```

Displayed, not adopted. The note does not attach ell^1, and it does not
attach `rho`, as a path-length law. The named rule is not written into
Admissibility.

## Exact Theorems

### Theorem 1

The directed nearest-neighbor edges of `B_3(0)` carry exactly eight `G+`
orbits of endpoint occupancy pairs, with inward-weight representatives as
above. Evaluating `rho` on those eight weight pairs gives

```text
rho(0,1) = 3,  rho(1,0) = 1,  rho(1,1) = 3,  rho(1,2) = 1,
rho(2,1) = 1,  rho(2,2) = 3,  rho(2,3) = 1,  rho(3,2) = 1,
```

which is the minkbest 8-tuple `(3, 1, 3, 1, 1, 3, 1, 1)`. The 129-site ball
adds the inward-weight pair `(3,3)` on 48 directed edges joining two
weight-3 sites (for example `(1,1,1)` and `(2,1,1)`). The named rule assigns
`rho(3,3) = 3` because the inward weights are equal. The 8-tuple does not
name that orbit; the member clause does.

The evaluation is local in the two inward weights. It does not scan a
radius-dependent leftover table. Uniqueness of `rho` among all maps that
extend `c` is not claimed.

### Theorem 2

On `B_4(0)`, assign the eight B_3 orbits by `rho` and either omit the new
`(3,3)` orbit or assign it any cost at least `3`. These fillings share the
same arrival table on every site of the 129-site ball. In particular the
named assignment `rho(3,3) = 3` is one of those fillings, and

```text
t(4,0,0) = 12.
```

The same axis/body-diagonal order used on `B_3(0)` is the pair
`((3,0,0),(1,1,1))`. It still reverses: `t(3,0,0) = 9`, `t(1,1,1) = 5`, and
`3 t(3,0,0)^2 > 9 t(1,1,1)^2`.

The axis path `0 → (1,0,0) → (2,0,0) → (3,0,0) → (4,0,0)` uses the
same-weight or seed-exit orbits and costs `3+3+3+3 = 12`. The body-diagonal
path `0 → (1,0,0) → (1,1,0) → (1,1,1)` costs `3+1+1 = 5`.

The bound `3` on the unused orbit is sharp on this ball: assigning cost `1`
or `2` to `(3,3)` changes 24 arrival times (the `(2,1,1)` type). Those
cheaper fillings are not the named rule.

### Theorem 3

The named rule is displayed as a finite probe. It is not written into
Admissibility. No path-length law is attached. The note does not attach
ell^1 or `rho` as a law. Uniqueness of `rho` is not claimed. The live axiom
memo continues to state that there is one fixed nearest-neighbor
admissibility rule, covariant under translations and proper cubic rotations;
that rule is not replaced by `rho(w_v, w_w)`. Displayed, not adopted.

## Proof-Obligation Graph

| Obligation | Disposition |
|---|---|
| name `B_4(0)` as the 129-site ball | closed by the nearest-neighbor graph of `Z^3` |
| define inward occupancy and inward weight | closed: a bit is set exactly on a strictly nearer neighbor; `w = |σ|` |
| count `G+` | closed: 24 proper cubic rotations |
| evaluate `rho` on the eight orbits | closed by Theorem 1; equals `(3, 1, 3, 1, 1, 3, 1, 1)` |
| name the new `(3,3)` orbit | closed by Theorem 1; `rho(3,3) = 3` |
| compare omit versus any cost at least `3` | closed by Theorem 2; same arrival table |
| report `t(4,0,0)` and the B_3 diamond pair | closed by Theorem 2; `12`, and it still reverses |
| treat `rho` as a per-radius leftover | refused; it is a member clause on weights |
| claim uniqueness of `rho` | refused; Theorem 3 |
| write `rho` into Admissibility | refused; Theorem 3 |
| attach a path-length law | refused; Theorem 3 |

The obligation graph is acyclic. Every leaf of the bounded comparison is
closed. Adoption of a cost or of a path-length law is not a proof leaf.

## Representative Values

| filling | `t(4,0,0)` | `t(3,0,0)` | `t(1,1,1)` | B_3 diamond? |
|---|---:|---:|---:|---|
| omit `(3,3)` | `12` | `9` | `5` | no |
| `rho`, including `rho(3,3) = 3` | `12` | `9` | `5` | no |
| `(3,3)` cost `4` (or any cost `≥ 3`) | `12` | `9` | `5` | no |

The three rows are one arrival table. The table is an exact illustration of
Theorems 1 and 2, not an adopted dynamics.

## Framework Boundary

Admissibility supplies one fixed nearest-neighbor rule, covariant under
lattice translations and proper cubic rotations, and says that the local
distribution varies with nearest-neighbor conditions. It does not supply a
numerical hop cost on occupancy pairs. This note therefore treats `rho` as a
displayed probe, not as an axiom clause.

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
| minkbest 8-tuple `(3, 1, 3, 1, 1, 3, 1, 1)` | displayed comparison target | mathematical input; not an axiom |
| `rho` on inward weights | named member clause | defined here; uniqueness not claimed |
| diamond order on `((3,0,0),(1,1,1))` | the B_3 test pair, scored on `B_4(0)` | declared |

There are no measured, fitted, literature, or observational inputs. A
continuum metric, a path-length axiom, and any cost written into
Admissibility remain outside the result.

## Mutations

1. Treat `rho` as a leftover table of the eight numbers: Theorem 1 evaluates
   a member clause on weights, including the new `(3,3)` pair the 8-tuple
   does not name.
2. Claim that `rho` is the unique extension of the 8-tuple: uniqueness of
   `rho` is not claimed.
3. Fold an unstated ninth cost into the 8-tuple and call that the named
   rule: Theorem 1 names `(3,3)` by the same clause, not by a leftover
   entry.
4. Treat omit-versus-`rho` as automatic leftover of a smaller-ball score:
   Theorem 2 recomputes the 129-site table and records the sharp bound
   `≥ 3`.
5. Write `rho` into Admissibility or attach a path-length law: the live
   axiom memo still states one fixed covariant nearest-neighbor rule and
   contains no two-end occupancy hop cost.
6. Attach ell^1 as a law because the diamond comparison uses axis and
   body-diagonal sites: the note does not attach ell^1.

## What This Does Not Claim

- No cost is written into Admissibility.
- No path-length law is attached.
- Uniqueness of `rho` is not claimed.
- The comparison is not scored outside `B_4(0)` except for rebuilding the
  eight `B_3` orbits.
- The named rule is not a leftover of a per-radius filling.
- The note does not attach ell^1 as a law.
- No continuum metric is derived.
- No privileged physical seed is added to the Lattice axiom.
- No Record readout is assigned to a site without a record.

## No-Go Discipline Gate

The negative claim is only this: the named equal-weight-or-seed-exit rule
reproducing the minkbest 8-tuple and naming the `B_4` `(3,3)` orbit is a
finite member clause, not a per-radius leftover, not an Admissibility
clause, and not a path-length law. It is not a claim that `rho` is unique
or that it belongs in the axiom.

### N1 — materially distinct routes

| Route | Exact attack | Result and authority | Marker |
|---|---|---|---|
| leftover of the 8-tuple | Argue that naming `(3,3)` is only a radius-4 patch of the same table. | Theorem 1: `rho` is a member clause on weights; `rho(3,3) = 3` is not a leftover entry. | **ATTEMPTED** |
| uniqueness of the clause | Treat any map reproducing `c` as this `rho`. | Theorem 3: uniqueness of `rho` is not claimed. | **ATTEMPTED** |
| attach ell^1 | Read the diamond comparison as a path-length law. | Theorem 3: ell^1 is not attached. | **ATTEMPTED** |
| invent a ninth leftover cost | Fold `(3,3)` into the 8-tuple without the clause. | Theorem 1: the new orbit is named by equal weight. | **ATTEMPTED** |
| cheaper unused orbit | Assign cost `1` or `2` to `(3,3)` and keep the named table. | Theorem 2: those costs change 24 times; the named table is the `≥ 3` table. | **ATTEMPTED** |
| adopt the rule | Write `rho` into Admissibility. | Theorem 3 and the live axiom memo: one fixed covariant nearest-neighbor rule, no hop cost. | **ATTEMPTED** |

### N2 — wall independence and collapse

There is one comparison and one adoption refusal, not a stack of independent
walls. Reproduction of the 8-tuple and the B_4 arrival-table identity are
two certificates of the same named-rule statement.

| Pair | First closes second? | Second closes first? | Disposition |
|---|---:|---:|---|
| 8-tuple reproduction / B_4 table | no: matching eight numbers does not fix unused-orbit arrivals | no: a shared table does not force the weight clause | independent conclusions on one rule |
| scoring statement / adoption refusal | no: a named probe can match `c` and still be refused as an axiom | no: refusing adoption does not decide the numbers | independent conclusions |

Path-length attachment is not counted as a third wall: Theorem 3 simply
does not attach one.

### N3 — hidden-condition scan

| Phrase or premise | Classification |
|---|---|
| “one-seed growth from `0`” | explicit theorem hypothesis; the Lattice axiom privileges no site |
| “inward occupation of the one-seed front” | defined from nearer neighbors; not an extra occupancy axiom |
| “named rule on inward weights” | displayed finite probe, not a derived scale |
| “minkbest 8-tuple” | displayed comparison target; not a load-bearing parent on this branch |
| “same arrival table for omit or cost `≥ 3`” | Theorem 2; exact Dijkstra on `B_4(0)` |
| “same axis/body-diagonal order as B_3” | the pair `((3,0,0),(1,1,1))` |
| “member clause, not a per-radius leftover” | Theorems 1 and 2 |
| “Uniqueness of `rho` is not claimed” | Theorem 3 |
| “Displayed, not adopted” | Theorem 3; no Admissibility edit |

### N4 — citation-to-residual matching

| Evidence path:line | Residual attacked | Residual claimed closed | Match? |
|---|---|---|---:|
| `docs/MINIMAL_AXIOMS_2026-06-29.md:37` | ambient lattice and proper cubic rotations | `Z^3` nearest-neighbor graph and `G+` | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:57` | Admissibility covariance | one fixed covariant nearest-neighbor rule; no hop cost supplied | yes; cost stays displayed |
| `scripts/named_equal_weight_hopcost_2026_08_15.py:293` | reproduction of the 8-tuple | `rho` equals `(3,1,3,1,1,3,1,1)` | yes |
| `scripts/named_equal_weight_hopcost_2026_08_15.py:298` | naming of the new orbit | `rho(3,3) = 3` on 48 edges | yes |
| `scripts/named_equal_weight_hopcost_2026_08_15.py:315` | axis arrival | `t(4,0,0) = 12` | yes |
| `scripts/named_equal_weight_hopcost_2026_08_15.py:320` | B_3 diamond order on this ball | `t(3,0,0) = 9`, `t(1,1,1) = 5`, still reverses | yes |
| `scripts/named_equal_weight_hopcost_2026_08_15.py:328` | omit versus named `(3,3)` | same 129-site table | yes |
| `scripts/named_equal_weight_hopcost_2026_08_15.py:333` | unused-orbit bound | any cost at least `3` shares the table | yes |
| `scripts/named_equal_weight_hopcost_2026_08_15.py:361` | adoption of a cost | note and axiom keep the cost out of Admissibility | yes |

No evidence citation is used to claim a path-length axiom, a continuum
metric, uniqueness of `rho`, or an Admissibility rewrite.

### N5 — rhetoric and resolution audit

| Resolution | Executed? | Narrow negative supported? |
|---|---:|---|
| per element | yes: each directed `B_4(0)` edge | eight B_3 orbits plus the named `(3,3)` orbit |
| per site | yes: inward occupancy at each site | no other occupancy dictionary is used |
| per mode | yes: the named weight rule | uniqueness of `rho` is not claimed |
| per block | yes: `t(4,0,0)` and diamond order on `B_4(0)` | no variance or larger ball is scored |
| lattice wide | no | no Admissibility cost and no path-length law are adopted |

The runner prints the same five resolution statements.

### N6 — partial closure and primitive scan

The only dependency used is the registered `minimal_axioms` node. No
approved primitive supplies a two-end occupancy hop cost, and none is
reclassified as an import or wall.

Two partial-closure mechanisms are recorded rather than suppressed. The
eight-number minkbest filling is a strictly smaller statement: it does not
name `(3,3)`. Existence of some reversing filling on `B_3(0)` is a strictly
weaker statement: it does not supply this member clause. The remaining
physical choice—whether any hop cost belongs in Admissibility—stays
explicit and does not require an axiom edit.

### N7 — hostile steelman

The strongest objection is that writing `cost 3` on equal weights is only
a slogan for the already-displayed 8-tuple, so naming `(3,3)` is leftover
bookkeeping once `B_4` grows that orbit. The objection correctly identifies
that the eight numbers match and that cost `3` on `(3,3)` does not change
times. It fails because the clause is local in the two weights, applies to
every inward-weight pair including the new orbit, and is not a radius-indexed
patch of leftover entries. Uniqueness of that clause is not claimed, and
the clause is not written into Admissibility.

### N8 — cross-cycle echo

The live axiom memo is the only load-bearing parent. Nearby covariance
language is context.

| Earlier surface | Similar issue | Mechanism considered here |
|---|---|---|
| `docs/MINIMAL_AXIOMS_2026-06-29.md` | proper cubic covariance of the nearest-neighbor rule | used as `G+` equivariance of the displayed cost; the rule itself is not replaced |
| displayed minkbest 8-tuple | same eight numbers on `B_3` orbits | scored as a comparison target; Theorem 1 is the member clause, not a leftover |
| unused `(3,3)` orbit on `B_4(0)` | ninth orbit omitted by the 8-tuple | named here by equal inward weight |

No earlier mechanism retires the named clause or the adoption refusal.

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
ball, and the eight B_3 occupancy-pair orbits; evaluates the named
equal-weight-or-seed-exit rule on those orbits and on `(3,3)`; reports
that the eight values are `(3, 1, 3, 1, 1, 3, 1, 1)` and `rho(3,3) = 3`;
reports that omit, the named assignment, and every `(3,3)` cost at least
`3` share the arrival table; reports `t(4,0,0) = 12` and that the B_3
axis/diagonal pair still reverses; rejects the mutation families, including
per-radius leftover and uniqueness; and verifies that the live axiom memo
does not host the displayed cost. Declared audit inputs are this note and
the axiom memo.
