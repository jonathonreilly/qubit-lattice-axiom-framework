---
claim_id: cost3_reversal_minkowski_fit_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Among the 405 diamond-reversing {1,2,3} two-end occupancy costs on B_3(0), the lex-first minimizer of var(|v|_2/t(v)) is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/cost3_reversal_minkowski_fit_2026_08_15.py
---

# Lex-First Diamond-Reversing Cost Minimizing `var(|v|_2/t(v))` On `B_3(0)`

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact orbit census and exact integer path costs on the radius-3
nearest-neighbor ball of one seed; population variance of `|v|_2/t(v)` on
the 62 nonzero sites. Displayed, not adopted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/cost3_reversal_minkowski_fit_2026_08_15.py`](../scripts/cost3_reversal_minkowski_fit_2026_08_15.py)
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

The eight `G+` orbits of inward occupancy pairs on this ball, in the order
used below, are the inward-weight pairs

```text
(0,1), (1,0), (1,1), (1,2), (2,1), (2,2), (2,3), (3,2).
```

A filling reverses the diamond axis/diagonal order when it violates

```text
t(3,0,0)^2 / 9  <=  t(1,1,1)^2 / 3,
```

equivalently when `3 t(3,0,0)^2 > 9 t(1,1,1)^2`. Exactly 405 of the
`3^8 = 6561` fillings reverse that order.

On the 62 sites of `B_3(0) \ {0}`, write `r(v) = |v|_2 / t(v)` and let
`var` be the population variance

```text
var(r) = (1/62) sum_v (r(v) - mean(r))^2.
```

The ell^1 filling `t(v) = |v|_1` has

```text
var_ell1 = 0.02073945514155.
```

The lex-first reversing filling `c = (1, 1, 3, 1, 1, 1, 1, 1)` has

```text
var_lex = 0.02227566969848
```

and is not the closest reversing filling to `t ∝ |v|_2`. Among the 405
reversing fillings, the lex-first minimizer of `var(r)` is

```text
c = (3, 1, 3, 1, 1, 3, 1, 1),
```

realizing `t(3,0,0) = 9`, `t(1,1,1) = 5`, and

```text
var_best = 0.00017588571746.
```

That comparison is reported on `B_3(0)` only. It is not a leftover of the
existence of 405 reversals, and it is not a leftover of scoring one map.
Displayed, not adopted.

## Exact Theorems

### Theorem 1

The directed nearest-neighbor edges of `B_3(0)` carry exactly eight `G+`
orbits of endpoint occupancy pairs, with inward-weight representatives as
above. Exactly 405 of the 6561 `{1,2,3}` fillings reverse
`3 t(3,0,0)^2 <= 9 t(1,1,1)^2`.

On the 62 nonzero sites the population variance of `|v|_2 / t(v)` for the
ell^1 filling `t = |·|_1` is `0.02073945514155`. For the lex-first reversing
filling `(1, 1, 3, 1, 1, 1, 1, 1)`, which realizes `t(3,0,0) = 7` and
`t(1,1,1) = 3`, the same variance is `0.02227566969848`. The lex-first
reversal is therefore farther from a constant ratio `|v|_2 / t(v)` than
ell^1 is.

### Theorem 2

Among those 405 reversing fillings, ordered lexicographically as 8-tuples in
`{1,2,3}^8` in the Theorem 1 orbit order, the first minimizer of
`var(|v|_2/t(v))` is

```text
c = (3, 1, 3, 1, 1, 3, 1, 1).
```

Seed-exit cost `3`, inbound `(1,0)` cost `1`, axis-extension cost `3`,
`(1,2)` cost `1`, `(2,1)` cost `1`, `(2,2)` cost `3`, `(2,3)` cost `1`, and
`(3,2)` cost `1`. It realizes `t(3,0,0) = 9` and `t(1,1,1) = 5`, hence
`3·81 = 243 > 9·25 = 225`, so it remains reversing. Its population variance
is `0.00017588571746`, strictly below both baselines of Theorem 1.

The six `G+` site-types in `B_3(0) \ {0}` arrive at

```text
t(1,0,0) = 3,  t(2,0,0) = 6,  t(1,1,0) = 4,
t(3,0,0) = 9,  t(2,1,0) = 7,  t(1,1,1) = 5.
```

Exactly 27 reversing fillings share this arrival table: the three inbound
orbits `(1,0)`, `(2,1)`, and `(3,2)` may each be set to any value in
`{1,2,3}` without changing any shortest-path time on `B_3(0)`. The
lex-first representative sets those three unused orbits to `1`.

The axis path `0 → (1,0,0) → (2,0,0) → (3,0,0)` costs `3+3+3 = 9`. The
body-diagonal path `0 → (1,0,0) → (1,1,0) → (1,1,1)` costs `3+1+1 = 5`.
The three axis types then satisfy `t = 3 |v|_2` exactly. The remaining
types sit near that same ratio, which is why the variance drops by two
orders of magnitude relative to ell^1.

### Theorem 3

The minimizing filling is displayed as a finite probe on `B_3(0)`. It is
not written into Admissibility. No path-length law is attached. The note
does not attach ell^1, the lex-first reversal, or the variance minimizer as
a law. The live axiom memo continues to state that there is one fixed
nearest-neighbor admissibility rule, covariant under translations and
proper cubic rotations; that rule is not replaced by `c(σ_v, σ_w)`.
Displayed, not adopted.

## Proof-Obligation Graph

| Obligation | Disposition |
|---|---|
| name `B_3(0)` and the six direction bits | closed by the nearest-neighbor graph of `Z^3` |
| define inward occupancy of the one-seed front | closed: a bit is set exactly on a strictly nearer neighbor |
| count `G+` | closed: 24 proper cubic rotations |
| count reversing fillings | closed by Theorem 1; 405 of 6561 |
| score `var(|v|_2/t(v))` for ell^1 and for the lex-first reversal | closed by Theorem 1 |
| exhibit the lex-first variance minimizer among the 405 | closed by Theorem 2; `(3, 1, 3, 1, 1, 3, 1, 1)` |
| treat existence of a reversal as the fit | refused; existence does not select a variance minimizer |
| treat one reversing map as the fit | refused; the lex-first reversal is not the minimizer |
| write a cost into Admissibility | refused; Theorem 3 |
| attach a path-length law | refused; Theorem 3 |

The obligation graph is acyclic. Every leaf of the bounded comparison is
closed. Adoption of a cost or of a path-length law is not a proof leaf.

## Representative Values

| filling | `t(3,0,0)` | `t(1,1,1)` | `var(|v|_2/t)` | diamond? |
|---|---:|---:|---:|---|
| ell^1, `t = \|·\|_1` | `3` | `3` | `0.02073945514155` | yes |
| lex-first reversal `(1, 1, 3, 1, 1, 1, 1, 1)` | `7` | `3` | `0.02227566969848` | no |
| lex-first variance minimizer `(3, 1, 3, 1, 1, 3, 1, 1)` | `9` | `5` | `0.00017588571746` | no |

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
| `c(σ_v, σ_w) ∈ {1,2,3}` | displayed `G+`-equivariant hop cost | mathematical input; not an axiom |
| diamond reversal on `(3,0,0)` and `(1,1,1)` | filter defining the 405-map family | declared test pair |
| `var(\|v\|_2/t(v))` on `B_3(0) \ {0}` | displayed closeness to `t ∝ \|v\|_2` | computed; not a continuum metric |
| existence of 405 reversals | context, not a load-bearing parent | rebuilt here; does not select a minimizer |
| one lex-first reversing map | context, not a load-bearing parent | scored in Theorem 1 and beaten in Theorem 2 |

There are no measured, fitted, literature, or observational inputs. A
continuum metric, a path-length axiom, and any cost written into
Admissibility remain outside the result.

## Mutations

1. Score all 6561 maps, not only the 405 reversals: the residual asked
   only which reversing cost is closest to `t ∝ |v|_2`.
2. Replace population variance by a sample factor `1/61`: the scored set
   is the finite list of 62 sites, so the mean-square deviation uses `1/62`.
3. Treat the lex-first reversal as the fit: Theorem 1 gives it a larger
   variance than ell^1, and Theorem 2 exhibits a strictly smaller reversing
   variance.
4. Treat existence of 405 reversals as the fit: existence does not name a
   minimizer of `var(|v|_2/t(v))`.
5. Collapse the 27-fold degeneracy to a unique 8-tuple without a lex rule:
   three inbound orbits are unused on `B_3(0)`; lex-first sets them to `1`.
6. Write `c` into Admissibility or attach a path-length law: the live axiom
   memo still states one fixed covariant nearest-neighbor rule and contains
   no two-end occupancy hop cost.

## What This Does Not Claim

- No cost is written into Admissibility.
- No path-length law is attached.
- The comparison is not scored outside `B_3(0)`.
- The variance minimizer is not a leftover of the existence of 405 reversals.
- The variance minimizer is not a leftover of scoring one reversing map.
- No continuum metric is derived.
- No privileged physical seed is added to the Lattice axiom.
- No Record readout is assigned to a site without a record.

## No-Go Discipline Gate

The negative claim is only this: on `B_3(0)`, the report of the lex-first
minimizer of `var(|v|_2/t(v))` among the 405 diamond-reversing `{1,2,3}`
two-end occupancy costs is not a leftover of existence, is not a leftover
of one reversing map, is not an Admissibility clause, and does not attach
a path-length law. It is not a claim that the minimizer belongs in the
axiom, nor that the same 8-tuple minimizes any other closeness score.

### N1 — materially distinct routes

| Route | Exact attack | Result and authority | Marker |
|---|---|---|---|
| existence leftover | Argue that naming 405 reversals already selects a Euclidean fit. | Theorem 2: the 405 maps take 15 distinct variances; existence does not pick the minimum. | **ATTEMPTED** |
| one-map leftover | Score only the lex-first reversal `(1, 1, 3, 1, 1, 1, 1, 1)`. | Theorem 1: that map has `var = 0.02227566969848`, worse than ell^1. | **ATTEMPTED** |
| attach ell^1 | Read the smaller ell^1 variance as a path-length law. | Theorem 3: ell^1 is a displayed baseline, not attached. | **ATTEMPTED** |
| unused inbound orbits | Claim a unique 8-tuple without lex order. | Theorem 2: 27 fillings share the arrival table; lex-first is `(3, 1, 3, 1, 1, 3, 1, 1)`. | **ATTEMPTED** |
| sample variance | Replace `1/62` by `1/61`. | The scored object is the finite 62-site list; the ranking of the 405 is unchanged. | **ATTEMPTED** |
| adopt the minimizer | Write `c` into Admissibility. | Theorem 3 and the live axiom memo: one fixed covariant nearest-neighbor rule, no hop cost. | **ATTEMPTED** |

### N2 — wall independence and collapse

There is one comparison and one adoption refusal, not a stack of independent
walls. The 405-map census and the lex-first variance witness are two
certificates of the same minimizer statement.

| Pair | First closes second? | Second closes first? | Disposition |
|---|---:|---:|---|
| 405-map census / lex-first minimizer | yes, as an exhaustive minimum that includes the witness | yes, as an explicit minimizing filling | collapse into Theorem 2 |
| minimizer statement / adoption refusal | no: a probe can minimize variance and still be refused as an axiom | no: refusing adoption does not decide the minimum | independent conclusions |

Path-length attachment is not counted as a third wall: Theorem 3 simply
does not attach one.

### N3 — hidden-condition scan

| Phrase or premise | Classification |
|---|---|
| “one-seed growth from `0`” | explicit theorem hypothesis; the Lattice axiom privileges no site |
| “inward occupation of the one-seed front” | defined from nearer neighbors; not an extra occupancy axiom |
| “`c ∈ {1,2,3}`” | displayed finite probe, not a derived scale |
| “`G+`-equivariant” | covariance under the axiom's proper cubic rotations |
| “diamond-reversing” | the displayed axis/diagonal inequality on `B_3(0)` only |
| “population variance on 62 sites” | the finite list `B_3(0) \ {0}` |
| “not a leftover” of existence or of one map | Theorems 1 and 2 |
| “Displayed, not adopted” | Theorem 3; no Admissibility edit |

### N4 — citation-to-residual matching

| Evidence path:line | Residual attacked | Residual claimed closed | Match? |
|---|---|---|---:|
| `docs/MINIMAL_AXIOMS_2026-06-29.md:37` | ambient lattice and proper cubic rotations | `Z^3` nearest-neighbor graph and `G+` | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:57` | Admissibility covariance | one fixed covariant nearest-neighbor rule; no hop cost supplied | yes; cost stays displayed |
| `scripts/cost3_reversal_minkowski_fit_2026_08_15.py:319` | size of the reversing family | exactly 405 reversals | yes |
| `scripts/cost3_reversal_minkowski_fit_2026_08_15.py:329` | ell^1 and lex-first-reversal variances | displayed digits of Theorem 1 | yes |
| `scripts/cost3_reversal_minkowski_fit_2026_08_15.py:349` | lex-first variance minimizer | `(3, 1, 3, 1, 1, 3, 1, 1)` | yes |
| `scripts/cost3_reversal_minkowski_fit_2026_08_15.py:354` | arrival times of that filling | `t(3,0,0) = 9`, `t(1,1,1) = 5` | yes |
| `scripts/cost3_reversal_minkowski_fit_2026_08_15.py:396` | adoption of a cost | note and axiom keep the cost out of Admissibility | yes |

No evidence citation is used to claim a path-length axiom, a continuum
metric, or an Admissibility rewrite.

### N5 — rhetoric and resolution audit

| Resolution | Executed? | Narrow negative supported? |
|---|---:|---|
| per element | yes: each directed `B_3(0)` edge | one inward occupancy pair; no other edge family is classified |
| per site | yes: `|v|_2/t(v)` on each nonzero site | no other occupancy dictionary is used |
| per mode | yes: all 405 reversing fillings | non-reversing fillings and larger balls are untested and unclaimed |
| per block | yes: population variance on `B_3(0) \ {0}` | closeness is the stated variance only |
| lattice wide | no | no Admissibility cost and no path-length law are adopted |

The runner prints the same five resolution statements.

### N6 — partial closure and primitive scan

The only dependency used is the registered `minimal_axioms` node. No
approved primitive supplies a two-end occupancy hop cost, and none is
reclassified as an import or wall.

Two partial-closure mechanisms are recorded rather than suppressed. The
existence of 405 reversals is a strictly weaker statement: it does not
select a variance minimizer. Scoring the single lex-first reversing map is
a strictly smaller census: that map is not the minimizer. The remaining
physical choice—whether any hop cost belongs in Admissibility—stays
explicit and does not require an axiom edit.

### N7 — hostile steelman

The strongest objection is that the lex-first reversing filling should
already be the Euclidean-closest reversing cost, because it is the first
map that delays the axis while leaving the body diagonal cheap. The
objection correctly identifies a reversing mechanism. It fails because
cheap seed-exit and expensive axis-extension make `|v|_2/t(v)` vary from
`1` at `(1,0,0)` down to `3/7` at `(3,0,0)`. Raising the seed-exit cost to
`3` and the `(2,2)` cost to `3` keeps reversal (`243 > 225`) while pinning
the three axis types to the common ratio `1/3`. The 405-map census is the
hostile check of that larger menu, and the lex-first minimizer is the
explicit witness.

### N8 — cross-cycle echo

The live axiom memo is the only load-bearing parent. Nearby covariance
language is context.

| Earlier surface | Similar issue | Mechanism considered here |
|---|---|---|
| `docs/MINIMAL_AXIOMS_2026-06-29.md` | proper cubic covariance of the nearest-neighbor rule | used as `G+` equivariance of the displayed cost; the rule itself is not replaced |
| existence of 405 reversing `{1,2,3}` fillings | same eight orbits, existence only | counted as a strictly weaker probe; Theorem 2 is not a leftover of existence |
| one lex-first reversing map | same family, one filling | scored in Theorem 1; Theorem 2 is not a leftover of that one map |

No earlier mechanism retires the variance census or the adoption refusal.

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
and the 228 directed edges; counts the eight `G+` orbits of inward occupancy
pairs; exhausts the 405 reversing `{1,2,3}` fillings; reports the ell^1 and
lex-first-reversal variances; exhibits the lex-first variance minimizer;
rejects the mutation families, including existence leftover and one-map
leftover; and verifies that the live axiom memo does not host the displayed
cost. Declared audit inputs are this note and the axiom memo.
