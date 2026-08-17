---
claim_id: axis_skeleton_hopcost_b4_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On B_4(0), the named axis-skeleton hop-cost is scored for the small-ball reverse and for variance vs ρ and ℓ¹. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/axis_skeleton_hopcost_b4_2026_08_15.py
---

# Named Axis-Skeleton Hop-Cost Scored On `B_4(0)`

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact integer path costs of one displayed named rule on the
radius-4 nearest-neighbor ball of one seed; small-ball order at `(3,0,0)`
versus `(1,1,1)` and population variance of `|v|_2/t(v)` versus `ρ` and
ell^1 on the 128 nonzero sites. Displayed, not adopted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/axis_skeleton_hopcost_b4_2026_08_15.py`](../scripts/axis_skeleton_hopcost_b4_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

Let `B_4(0)` be the set of sites of `Z^3` reachable from the origin by at
most four nearest-neighbor steps. This is the 129-site ball. One-seed growth
starts at `0`. The occupancy `σ_n` at a site `n` is the 6-bit string whose
direction-`d` bit is set exactly when the neighbor of `n` in direction `d` is
strictly nearer the seed. This is the inward occupation of the one-seed
front.

`G+` is the 24-element group of proper cubic rotations about the seed.
Arrival time `t(n)` is the minimum path cost from `0` to `n` through
`B_4(0)`.

The named axis-skeleton rule `α` assigns a hop cost on every inward
occupancy pair that appears in `B_4`:

```text
α(σ_v, σ_w) = 3  if |σ_v| = 0 or (|σ_v| = |σ_w| = 1),
α(σ_v, σ_w) = 1  otherwise.
```

Seed-exit or both inward weights equal to `1` costs `3`; every other inward
pair costs `1`. This is the same named rule scored on `B_6(0)`. The nine
inward-weight pairs realized on `B_4(0)` are

```text
(0,1), (1,0), (1,1), (1,2), (2,1), (2,2), (2,3), (3,2), (3,3).
```

On the same sites the note also scores the named equal-weight rule `ρ`,

```text
ρ(σ_v, σ_w) = 3  if |σ_v| = |σ_w| or |σ_v| = 0,
ρ(σ_v, σ_w) = 1  otherwise,
```

and the ell^1 filling `t(v) = |v|_1`. The comparison is not a leftover of
B_6 times: the balls are a different ball, and the B_6 detour site
`(4,1,0)` is not a site of `B_4(0)`.

Two Dijkstras capped at the 129-site ball give

```text
t_α(3,0,0) = 7,  t_α(1,1,1) = 5,  t_α(4,0,0) = 10.
```

The B_3 small-ball reverse test is `3 t(3,0,0)^2 > 9 t(1,1,1)^2`. Under
`α` this fails: `3·49 = 147` is not greater than `9·25 = 225`. The B_3
pair does not reverse.

On the 128 sites of `B_4(0) \ {0}`, write `s(v) = |v|_2 / t(v)` and let
`var` be the population variance

```text
var(s) = (1/128) sum_v (s(v) - mean(s))^2.
```

The three fillings have

```text
var_alpha = 0.00397088249988,
var_rho   = 0.00035024862901,
var_ell1  = 0.01771035124177.
```

The order is `var_rho < var_alpha < var_ell1`. So `var_α` is strictly
below ell^1 and strictly above `ρ`. Displayed, not adopted. The note does
not attach ell^1, does not attach `ρ`, and does not attach `α`, as a
path-length law.

## Exact Theorems

### Theorem 1

The directed nearest-neighbor edges of `B_4(0)` carry nine inward-weight
pairs of occupancies. The named axis-skeleton rule assigns every pair:
seed-exit `(0,1)` costs `3`, the axis pair `(1,1)` costs `3`, and every
other pair — including the equal-weight pairs `(2,2)` and `(3,3)` —
costs `1`. By contrast `ρ` costs `3` on those equal-weight pairs.

Two Dijkstras on the 129-site ball yield

```text
t(3,0,0) = 7,  t(1,1,1) = 5,  t(4,0,0) = 10
```

under `α`, and

```text
t_ρ(3,0,0) = 9,  t_ρ(1,1,1) = 5,  t_ρ(4,0,0) = 12
```

under `ρ`. The B_3 pair is `((3,0,0),(1,1,1))`. The reverse test
`3 t(3,0,0)^2 > 9 t(1,1,1)^2` does not reverse under `α`.

The axis-only path `0 → (1,0,0) → (2,0,0) → (3,0,0) → (4,0,0)` still
costs `3+3+3+3 = 12`. It is not shortest. The cheaper `α` path
`0 → (1,0,0) → (1,1,0) → (2,1,0) → (3,1,0) → (3,0,0)` costs
`3+1+1+1+1 = 7`, and one further axis hop `(3,0,0) → (4,0,0)` of cost
`3` gives `t(4,0,0) = 10`. The body-diagonal path
`0 → (1,0,0) → (1,1,0) → (1,1,1)` costs `3+1+1 = 5`.

The site `(4,1,0)` has ell^1 radius `5` and is not a site of `B_4(0)`.
A leftover of B_6 times would use that site as a cheap return to
`(4,0,0)`. The B_4 arrival `t(4,0,0) = 10` is therefore not a leftover
of B_6 times.

### Theorem 2

On the 128 nonzero sites of `B_4(0)`, the population variance of
`|v|_2/t(v)` is `0.00397088249988` for `α`, `0.00035024862901` for `ρ`,
and `0.01771035124177` for the ell^1 filling `t = |·|_1`. The order is
`var_rho < var_alpha < var_ell1`. The named axis-skeleton rule is
therefore strictly below ell^1 and strictly above `ρ` on this ball.

The `G+` site-types in `B_4(0)` arrive under `α` at

```text
t(1,0,0) = 3,  t(1,1,0) = 4,  t(1,1,1) = 5,
t(2,0,0) = 6,  t(2,1,0) = 5,  t(2,1,1) = 6,
t(2,2,0) = 6,  t(3,0,0) = 7,  t(3,1,0) = 6,
t(4,0,0) = 10.
```

Axis types are no longer pinned to `t = 3 |v|_2`: the off-axis return
cheapens `(3,0,0)` to `7` and `(4,0,0)` to `10`. That is why `var_α`
sits between `ρ` and ell^1. The comparison is scored on `B_4(0)` only.
It is not a leftover of B_6 times: the balls are a different ball, the
128-site list is not the 376-site list, and `(4,1,0)` is absent.

### Theorem 3

The named rule `α` is displayed as a finite probe on `B_4(0)`. It is
not written into Admissibility. No path-length law is attached. The note
does not attach ell^1, `ρ`, or the displayed rule as a law. The live axiom
memo continues to state that there is one fixed nearest-neighbor
admissibility rule, covariant under translations and proper cubic
rotations; that rule is not replaced by `c(σ_v, σ_w)`. Displayed, not
adopted.

## Proof-Obligation Graph

| Obligation | Disposition |
|---|---|
| name `B_4(0)` as the 129-site ball | closed by the nearest-neighbor graph of `Z^3` |
| define inward occupancy of the one-seed front | closed: a bit is set exactly on a strictly nearer neighbor |
| count `G+` | closed: 24 proper cubic rotations |
| name `α` on every inward occupancy pair in `B_4` | closed: cost `3` iff seed-exit or both weights `1`, else `1` |
| score `ρ` and ell^1 on the same sites | closed by Theorems 1 and 2 |
| report `t_α(3,0,0)`, `t_α(1,1,1)`, and `t_α(4,0,0)` | closed by Theorem 1 |
| report whether the B_3 pair still reverses | closed by Theorem 1; it does not reverse |
| score `var(\|v\|_2/t(v))` for `α`, `ρ`, and ell^1 | closed by Theorem 2; `var_rho < var_alpha < var_ell1` |
| treat B_6 times as the B_4 score | refused; different ball, `(4,1,0)` absent |
| write a cost into Admissibility | refused; Theorem 3 |
| attach a path-length law | refused; Theorem 3 |

The obligation graph is acyclic. Every leaf of the bounded comparison is
closed. Adoption of a cost or of a path-length law is not a proof leaf.

## Representative Values

| filling | `t(3,0,0)` | `t(1,1,1)` | `t(4,0,0)` | `var(\|v\|_2/t)` | B_3 reverse? |
|---|---:|---:|---:|---:|---|
| ell^1, `t = \|·\|_1` | `3` | `3` | `4` | `0.01771035124177` | no |
| named `ρ` | `9` | `5` | `12` | `0.00035024862901` | yes |
| named `α` | `7` | `5` | `10` | `0.00397088249988` | no |

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
| named rule `α` | displayed hop cost on inward weights | mathematical input; not an axiom |
| named rule `ρ` | displayed equal-weight comparison on the same sites | mathematical input; not an axiom |
| small-ball pair `((3,0,0),(1,1,1))` | the B_3 reverse test on `B_4(0)` | declared |
| `var(\|v\|_2/t(v))` on `B_4(0) \ {0}` | displayed closeness of the three fillings | computed; not a continuum metric |
| B_6 score of the same `α` | context, not a load-bearing parent | different ball; `(4,1,0)` is absent |

There are no measured, fitted, literature, or observational inputs. A
continuum metric, a path-length axiom, and any cost written into
Admissibility remain outside the result.

## Mutations

1. Treat B_6 times as already the B_4 score: the balls are a different
   ball; `(4,1,0)` is not a site of `B_4(0)`; Theorem 1 recomputes
   `t(4,0,0) = 10`.
2. Treat the axis-only path as shortest: that path still costs `12`, but
   the off-axis return through `(3,1,0)` is cheaper under `α` and is why
   the B_3 pair does not reverse.
3. Replace population variance by a sample factor `1/127`: the scored set
   is the finite list of 128 sites, so the mean-square deviation uses
   `1/128`.
4. Enlarge the graph past `B_4(0)`: the residual scores the 129-site
   ball only.
5. Write `α` into Admissibility or attach a path-length law: the live
   axiom memo still states one fixed covariant nearest-neighbor rule and
   contains no two-end occupancy hop cost.
6. Attach ell^1 or `ρ` because one variance is smaller: Theorem 3 does
   not attach either.

## What This Does Not Claim

- No cost is written into Admissibility.
- No path-length law is attached.
- The comparison is not scored outside `B_4(0)`.
- The B_4 score is not a leftover of B_6 times (different ball).
- The note does not attach ell^1 as a law.
- The note does not attach `ρ` as a law.
- No continuum metric is derived.
- No privileged physical seed is added to the Lattice axiom.
- No Record readout is assigned to a site without a record.

## No-Go Discipline Gate

The negative claim is only this: on `B_4(0)`, scoring the named
axis-skeleton hop-cost for the small-ball reverse and for
`var(|v|_2/t)` versus `ρ` and ell^1 is not a leftover of B_6 times, is
not an Admissibility clause, and does not attach a path-length law. It
is not a claim that the named rule belongs in the axiom, nor that it
minimizes any score on `B_4(0)`.

### N1 — materially distinct routes

| Route | Exact attack | Result and authority | Marker |
|---|---|---|---|
| leftover of B_6 times | Argue that the B_6 arrival table of `α` is already the B_4 table. | Theorem 1: different ball; `(4,1,0)` is absent; `t(4,0,0) = 10` is a new number. | **ATTEMPTED** |
| keep the axis-only path | Treat `t(3,0,0)` as the four-hop axis cost `9`. | Theorem 1: the off-axis return through `(3,1,0)` gives `7`; the pair does not reverse. | **ATTEMPTED** |
| attach ell^1 | Read the smaller-than-ell^1 variance as a path-length law. | Theorem 3: ell^1 is a displayed baseline, not attached. | **ATTEMPTED** |
| attach `ρ` | Read `var_ρ < var_α` as selecting `ρ`. | Theorem 3: `ρ` is a displayed comparison, not attached. | **ATTEMPTED** |
| invent a tenth cost | Fold a pair that does not appear on `B_4(0)` into `α`. | Theorem 1: the nine realized weight pairs are all named by `α`. | **ATTEMPTED** |
| adopt the named rule | Write `α` into Admissibility. | Theorem 3 and the live axiom memo: one fixed covariant nearest-neighbor rule, no hop cost. | **ATTEMPTED** |

### N2 — wall independence and collapse

There is one comparison and one adoption refusal, not a stack of independent
walls. The small-ball witness and the three-way variance comparison are two
certificates of the same B_4 scoring statement.

| Pair | First closes second? | Second closes first? | Disposition |
|---|---:|---:|---|
| small-ball order / variance comparison | no: failure to reverse does not fix the 128-site variances | no: the order `var_rho < var_alpha < var_ell1` does not decide the B_3 pair | independent conclusions on one named rule |
| scoring statement / adoption refusal | no: a probe can fail to reverse, sit between `ρ` and ell^1, and still be refused as an axiom | no: refusing adoption does not decide the numbers | independent conclusions |

Path-length attachment is not counted as a third wall: Theorem 3 simply
does not attach one.

### N3 — hidden-condition scan

| Phrase or premise | Classification |
|---|---|
| “one-seed growth from `0`” | explicit theorem hypothesis; the Lattice axiom privileges no site |
| “inward occupation of the one-seed front” | defined from nearer neighbors; not an extra occupancy axiom |
| “named axis-skeleton hop-cost” | displayed finite probe, not a derived scale |
| “two Dijkstras capped at the 129-site ball” | the definition of `t_α` and `t_ρ` through `B_4(0)` |
| “`(4,1,0)` is not a site” | exact ell^1 radius `5` versus ball radius `4` |
| “same B_3 pair `((3,0,0),(1,1,1))`” | the small-ball reverse test |
| “population variance on 128 sites” | the finite list `B_4(0) \ {0}` |
| “not a leftover” of B_6 times | Theorems 1 and 2; different ball |
| “Displayed, not adopted” | Theorem 3; no Admissibility edit |

### N4 — citation-to-residual matching

| Evidence path:line | Residual attacked | Residual claimed closed | Match? |
|---|---|---|---:|
| `docs/MINIMAL_AXIOMS_2026-06-29.md:37` | ambient lattice and proper cubic rotations | `Z^3` nearest-neighbor graph and `G+` | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:57` | Admissibility covariance | one fixed covariant nearest-neighbor rule; no hop cost supplied | yes; cost stays displayed |
| `scripts/axis_skeleton_hopcost_b4_2026_08_15.py:303` | size of the scored ball | `B_4(0)` has 129 sites | yes |
| `scripts/axis_skeleton_hopcost_b4_2026_08_15.py:327` | arrival times of the B_3 pair and `(4,0,0)` | `t(3,0,0) = 7`, `t(1,1,1) = 5`, `t(4,0,0) = 10` | yes |
| `scripts/axis_skeleton_hopcost_b4_2026_08_15.py:332` | small-ball reverse test | `3 t(3,0,0)^2 > 9 t(1,1,1)^2` fails | yes |
| `scripts/axis_skeleton_hopcost_b4_2026_08_15.py:357` | three-way variance order | `var_rho < var_alpha < var_ell1` | yes |
| `scripts/axis_skeleton_hopcost_b4_2026_08_15.py:370` | leftover of B_6 times | note states different ball and absent `(4,1,0)` | yes |
| `scripts/axis_skeleton_hopcost_b4_2026_08_15.py:379` | adoption of a cost | note and axiom keep the cost out of Admissibility | yes |

No evidence citation is used to claim a path-length axiom, a continuum
metric, or an Admissibility rewrite.

### N5 — rhetoric and resolution audit

| Resolution | Executed? | Narrow negative supported? |
|---|---:|---|
| per element | yes: each directed `B_4(0)` edge | nine named inward-weight pairs |
| per site | yes: `|v|_2/t(v)` on each nonzero site | no other occupancy dictionary is used |
| per mode | yes: `α`, `ρ`, and ell^1 on the same ball | no other named rule is scored |
| per block | yes: small-ball order and variance on `B_4(0) \ {0}` | closeness is the stated variance only |
| lattice wide | no | no Admissibility cost and no path-length law are adopted |

The runner prints the same five resolution statements.

### N6 — partial closure and primitive scan

The only dependency used is the registered `minimal_axioms` node. No
approved primitive supplies a two-end occupancy hop cost, and none is
reclassified as an import or wall.

Two partial-closure mechanisms are recorded rather than suppressed. The
B_6 score of the same `α` is a strictly larger-ball statement: it uses
sites such as `(4,1,0)` that `B_4(0)` does not contain. Naming `α` on
the finite weight pairs is a strictly weaker statement: it does not
decide small-ball order or the 128-site variances. The remaining
physical choice—whether any hop cost belongs in Admissibility—stays
explicit and does not require an axiom edit.

### N7 — hostile steelman

The strongest objection is that transporting `α` from `B_6(0)` to
`B_4(0)` is automatic leftover: the same seed-exit cost, the same axis
pair cost, and the same cheap off-axis hops should make the smaller-ball
score a corollary of the B_6 table, including a continuing small-ball
reverse. The objection correctly identifies that the cost rule is the
same named rule. It fails because `B_4(0)` is a different finite list,
does not contain `(4,1,0)`, and the cheapest `α` return to `(4,0,0)`
through that site is unavailable. The B_4 arrival `t(4,0,0) = 10` and
the failure of `3·49 > 225` are new certificates, not leftovers.

### N8 — cross-cycle echo

The live axiom memo is the only load-bearing parent. Nearby covariance
language is context.

| Earlier surface | Similar issue | Mechanism considered here |
|---|---|---|
| `docs/MINIMAL_AXIOMS_2026-06-29.md` | proper cubic covariance of the nearest-neighbor rule | used as `G+` equivariance of the displayed cost; the rule itself is not replaced |
| B_6 score of the same `α` | same named costs, larger ball, site `(4,1,0)` present | scored as a strictly larger-ball parent; Theorems 1 and 2 are not leftovers |
| named equal-weight rule `ρ` | cost `3` on every equal-weight pair | scored as a displayed comparison on the same 128 sites; not attached |

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

The companion runner builds the 24 proper cubic rotations and the 129-site
ball; assigns the named axis-skeleton hop-cost on every inward occupancy
pair in `B_4`; scores `ρ` and ell^1 on the same sites; runs two Dijkstras
capped at `B_4(0)`; reports `t(3,0,0) = 7`, `t(1,1,1) = 5`, and
`t(4,0,0) = 10`; reports that the B_3 pair does not reverse; compares
`var(|v|_2/t)` for `α`, `ρ`, and ell^1 on the 128 nonzero sites; rejects
the mutation families, including leftover of B_6 times; and verifies that
the live axiom memo does not host the displayed cost. Declared audit
inputs are this note and the axiom memo.
