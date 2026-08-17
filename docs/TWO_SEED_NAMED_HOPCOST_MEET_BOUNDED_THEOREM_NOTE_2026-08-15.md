---
claim_id: two_seed_named_hopcost_meet_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Two-seed meetings under the named equal-weight hop-cost on B_4(0)∪B_4((2,0,0)) are scored vs ℓ¹. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/two_seed_named_hopcost_meet_2026_08_15.py
---

# Two-Seed Meetings Under The Named Equal-Weight Hop-Cost On `B_4(0)∪B_4((2,0,0))`

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact integer path costs of two one-seed fronts on the union of
two radius-4 nearest-neighbor balls; first-meeting sites and the
population variance of `|v-s0|_2 / t0(v)` versus ell^1. Displayed, not
adopted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/two_seed_named_hopcost_meet_2026_08_15.py`](../scripts/two_seed_named_hopcost_meet_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

Let `s0 = (0,0,0)` and `s1 = (2,0,0)`. Write `B_4(c)` for the set of
sites of `Z^3` reachable from `c` by at most four nearest-neighbor steps,
and write

```text
U = B_4(s0) ∪ B_4(s1).
```

`U` has 195 sites. One-seed growth from each seed is confined to this
union. Inward weight at a site relative to the seed being grown is the
number of six-neighbors strictly nearer that seed. The named hop-cost
`ρ` on a directed nearest-neighbor edge is `3` if the edge is a seed-exit
or if the two endpoints have equal inward weight relative to that seed,
and is `1` otherwise. Arrival times `t0` and `t1` are the minimum path
costs from `s0` and from `s1` under `ρ` grown from that seed. They are
produced by one pair of Dijkstras on `U`.

The simultaneous-arrival set is

```text
E = { v ∈ U : t0(v) = t1(v) }.
```

The first-meeting set is

```text
M = { v ∈ E : no neighbor w of v has t0(w) < t0(v) and t1(w) < t1(v) }.
```

Uniqueness not required. On this union, `M` happens to be a singleton.

**Theorem 1.** The lex-first first-meeting site under `ρ` is `(1, 0, 0)`
with `t = 3`, and `|M| = 1`. The same site is the unique first-meeting
site under ell^1, with arrival `t = 1`.

**Theorem 2.** On `M`, the population variance of `|v-s0|_2 / t0(v)` is
`0` under `ρ` and `0` under ell^1, so neither figure is smaller. That
zero comparison is the uniqueness of first contact, not a leftover of
one-seed variance. The residual's common-ratio question is therefore also
scored on the 25-site midplane `E`, which is the same set under `ρ` and
under ell^1. On `E`,

```text
var_ρ = 0.00033709642621
var_ell1 = 0.00995038158264
```

so `var_ρ` is strictly below the ell^1 figure. This is not leftover of
one-seed variance: the scored list is the two-seed midplane of `U`, not
the 128 nonzero sites of `B_4(0)`.

**Theorem 3.** Displayed, not adopted. Do not write `ρ` into
Admissibility. Do not attach L1. No path-length law is attached.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "One pair of Dijkstras on the 195-site union computes the first-meeting set, its lex-first site and time, and the population variances on M and on the 25-site midplane versus ell^1."
trace_class: frontier_discovery
target_claim_id: two_seed_named_hopcost_meet
target_blocker_text: "whether first-meeting sites under the named hop-cost have |x-s|_2/t closer to a common ratio than under ell^1"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the displayed two-seed meeting score; do not adopt the named hop-cost or attach L1"
conditional_surface_status: "exact for U = B_4(0) ∪ B_4((2,0,0)), the named hop-cost, and one pair of Dijkstras; displayed, not adopted"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

Physical sites are the points of the cubic lattice `Z^3`, with
nearest-neighbor adjacency. `G+` is the 24-element group of proper cubic
rotations; it is used only to name the ambient lattice, not to reduce the
two-seed pair. The seeds are a theorem hypothesis. No site is privileged
in the Lattice axiom.

Inward weight of `v` relative to seed `s` is

```text
w_s(v) = |{ u ∈ N(v) : |u-s|_1 < |v-s|_1 }|.
```

A directed edge `v → w` inside `U` has named cost

```text
ρ_s(v → w) = 3  if v = s or w_s(v) = w_s(w),
ρ_s(v → w) = 1  otherwise.
```

This is the equal-weight hop-cost of the one-seed `B_3`/`B_4` isochrone
investment, including the `(3,3)` pair that appears on radius 4, together
with seed-exit. It is not rewritten into Admissibility.

`t0` is Dijkstra from `s0` with costs `ρ_{s0}`. `t1` is Dijkstra from
`s1` with costs `ρ_{s1}`. The ell^1 comparator uses the closed forms
`t0^{ℓ¹}(v) = |v-s0|_1` and `t1^{ℓ¹}(v) = |v-s1|_1`. The runner does
not run a third Dijkstra.

## Exact Theorems

### Theorem 1

`B_4(s0)` and `B_4(s1)` each have 129 sites. Their union `U` has 195
sites and 828 directed nearest-neighbor edges. One pair of Dijkstras on
`U` yields `t0` and `t1` under `ρ`.

The simultaneous-arrival set `E` is the midplane `x = 1` inside `U`, with
25 sites. The first-meeting set is the subset of `E` with no neighbor
strictly earlier for both fronts. That subset is

```text
M = { (1, 0, 0) }.
```

The lex-first meeting site is therefore `(1, 0, 0)`, and `|M| = 1`. Its
arrival under `ρ` is `t = 3`: the two seed-exit edges
`s0 → (1, 0, 0)` and `s1 → (1, 0, 0)` each cost `3`. Under ell^1 the
same site is the unique first-meeting site, with `t = 1`. Uniqueness is
reported, not required.

The later midplane sites remain simultaneous arrivals. Each has a
midplane neighbor nearer `(1, 0, 0)` at which both fronts are strictly
earlier, so those sites are in `E` and not in `M`.

### Theorem 2

Population variance on a finite list `S` is

```text
var(a) = (1/|S|) Σ_{v in S} (a(v) - mean(a))^2.
```

On `M`, both lists are singletons, so

```text
var_ρ(M) = 0,    var_ell1(M) = 0.
```

Neither is smaller. That identity is uniqueness of first contact. It is
not leftover of one-seed variance: the one-seed `B_3`/`B_4` scores were
population variances on 62 or 128 nonzero sites of a single ball, not a
two-seed first-meeting set.

The residual asks whether first-meeting sites have `|x-s|_2 / t` closer
to a common ratio than under ell^1. With `|M| = 1` that comparison is
vacuous, so the same variance is also scored on the 25-site
simultaneous-arrival midplane `E`, which is the set of two-seed meetings
in the weaker sense that neither front is strictly earlier at the site.
On `E`,

```text
var_ρ(E)     = 0.00033709642621
var_ell1(E)  = 0.00995038158264
```

and `var_ρ(E)` is strictly below `var_ell1(E)`. The midplane ratios under
`ρ` cluster near `1/3`; the ell^1 ratios range from `1` at `(1, 0, 0)`
to `√10 / 4` at the far axis sites. The comparison is displayed, not
adopted. The note does not attach ell^1, and it does not attach `ρ`, as
a path-length law.

### Theorem 3

The named hop-cost and the two-seed meeting score are displayed as a
finite probe on `U`. They are not written into Admissibility. Do not
write `ρ` into Admissibility. Do not attach L1. No path-length law is
attached. The live axiom memo continues to state that there is one fixed
nearest-neighbor admissibility rule, covariant under translations and
proper cubic rotations; that rule is not replaced by `ρ`. Displayed, not
adopted.

## Proof-Obligation Graph

| Obligation | Disposition |
|---|---|
| name `U = B_4(0) ∪ B_4((2,0,0))` | closed: 129 + 129 sites, union 195 |
| define inward weight relative to the seed being grown | closed: count of strictly nearer six-neighbors |
| name `ρ` as seed-exit or equal inward weight cost 3, else 1 | closed; displayed, not adopted |
| produce `t0` and `t1` by one pair of Dijkstras | closed by Theorem 1 |
| form `M` as equal times with no neighbor earlier for both | closed by Theorem 1; `|M| = 1` |
| report the lex-first meeting site and its `t` | closed: `(1, 0, 0)` at `t = 3` |
| score `var(\|v-s0\|_2/t0)` on `M` versus ell^1 | closed by Theorem 2; both zero |
| score the same variance on the 25-site midplane | closed by Theorem 2; `ρ` strictly below |
| treat the score as leftover of one-seed variance | refused; different list |
| require uniqueness of a meeting site | refused; uniqueness not required |
| write `ρ` into Admissibility | refused; Theorem 3 |
| attach a path-length law or L1 | refused; Theorem 3 |

The obligation graph is acyclic. Every leaf of the bounded comparison is
closed. Adoption of a cost or of a path-length law is not a proof leaf.

## Representative Values

| object | `ρ` | ell^1 |
|---|---|---|
| lex-first meeting site | `(1, 0, 0)` | `(1, 0, 0)` |
| meeting time `t` | `3` | `1` |
| `|M|` | `1` | `1` |
| `|E|` | `25` | `25` |
| `var(\|v-s0\|_2/t0)` on `M` | `0` | `0` |
| `var(\|v-s0\|_2/t0)` on `E` | `0.00033709642621` | `0.00995038158264` |

The table is an exact illustration of Theorems 1 and 2, not an adopted
dynamics.

## Framework Boundary

Admissibility supplies one fixed nearest-neighbor rule, covariant under
lattice translations and proper cubic rotations, and says that the local
distribution varies with nearest-neighbor conditions. It does not supply
a numerical hop cost, a seed pair, or a meeting set. This note therefore
treats `ρ` as a displayed probe, not as an axiom clause.

Record is not used. No formation site, formation rate, or readout value is
assigned to an unoccupied site. The two seeds are a theorem hypothesis
for the two fronts, not privileged physical sites.

## Imports And Claim Boundary

| Item | Role | Provenance / status |
|---|---|---|
| `Z^3` nearest-neighbor adjacency and proper cubic rotations | ambient lattice | live axiom memo |
| two seeds at `(0,0,0)` and `(2,0,0)` | theorem hypothesis | declared; no site is privileged in the axiom |
| `U = B_4(0) ∪ B_4((2,0,0))` | finite domain | declared |
| named hop-cost `ρ` | displayed two-end cost | mathematical input; not an axiom |
| one pair of Dijkstras | `t0`, `t1` | computed; Theorem 1 |
| first-meeting set `M` | equal times, no neighbor earlier for both | computed; Theorem 1 |
| `var(\|v-s0\|_2/t0)` on `M` and on `E` versus ell^1 | displayed common-ratio test | computed; Theorem 2 |
| one-seed `B_3`/`B_4` isochrone variance | context, not a load-bearing parent | different list; not leftover |

There are no measured, fitted, literature, or observational inputs. A
path-length axiom and any cost written into Admissibility remain outside
the result.

## Mutations

1. Grow each front on the infinite lattice: the residual asks for fronts
   on `B_4` about each seed, or on the union inside
   `B_4(0) ∪ B_4((2,0,0))`.
2. Treat the one-seed `B_3`/`B_4` variance as already the two-seed
   meeting score: the lists are different; Theorem 2 recomputes variance
   on `M` and on `E`.
3. Require a unique meeting site: uniqueness is not required; this union
   happens to have `|M| = 1`.
4. Replace population variance by a sample factor: `M` and `E` are finite
   lists, so the mean-square deviation uses `1/|S|`.
5. Run more than one pair of Dijkstras, or grow a third cost by search:
   the residual asks for one pair under the named hop-cost.
6. Write `ρ` into Admissibility or attach L1: the live axiom memo still
   states one fixed covariant nearest-neighbor rule and contains no
   named hop-cost.

## What This Does Not Claim

- No cost is written into Admissibility.
- No path-length law is attached.
- The comparison is not scored outside `U`.
- The two-seed score is not leftover of one-seed variance.
- The note does not attach L1 as a law.
- Uniqueness of a meeting site is not required.
- No continuum metric is derived.
- No privileged physical seed is added to the Lattice axiom.
- No Record readout is assigned to a site without a record.

## No-Go Discipline Gate

The negative claim is only this: on `U = B_4(0) ∪ B_4((2,0,0))`, scoring
two-seed first meetings under the named equal-weight hop-cost versus
ell^1 is not leftover of one-seed variance, is not an Admissibility
clause, and does not attach a path-length law. It is not a claim that
`ρ` belongs in the axiom.

### N1 — materially distinct routes

| Route | Exact attack | Result and authority | Marker |
|---|---|---|---|
| leftover of one-seed variance | Argue that the `B_3`/`B_4` isochrone variance is already the two-seed meeting score. | Theorem 2: different list; `M` and `E` are two-seed sets. | **ATTEMPTED** |
| require uniqueness | Treat a non-unique `M` as a failed theorem. | Uniqueness not required; this union has `|M| = 1` as a report, not a demand. | **ATTEMPTED** |
| attach L1 | Read the smaller midplane variance as a path-length law. | Theorem 3: ell^1 is a displayed baseline, not attached. | **ATTEMPTED** |
| extra Dijkstras | Grow more than one pair, or scan other costs. | One pair of Dijkstras under the named hop-cost. | **ATTEMPTED** |
| leave the union | Score meetings on the infinite lattice. | Domain is `U`; fronts stay inside the two radius-4 balls. | **ATTEMPTED** |
| adopt the hop-cost | Write `ρ` into Admissibility. | Theorem 3 and the live axiom memo: one fixed covariant nearest-neighbor rule, no hop cost. | **ATTEMPTED** |

### N2 — wall independence and collapse

There is one comparison and one adoption refusal, not a stack of independent
walls. The lex-first meeting report and the variance comparison are two
certificates of the same two-seed scoring statement.

| Pair | First closes second? | Second closes first? | Disposition |
|---|---:|---:|---|
| first-meeting census / variance comparison | no: `|M| = 1` does not fix the 25-site midplane variance | no: a smaller midplane variance does not name the lex-first site | independent conclusions on one pair of fronts |
| scoring statement / adoption refusal | no: a probe can beat ell^1 on `E` and still be refused as an axiom | no: refusing adoption does not decide the numbers | independent conclusions |

Path-length attachment is not counted as a third wall: Theorem 3 simply
does not attach one.

### N3 — hidden-condition scan

| Phrase or premise | Classification |
|---|---|
| “two seeds at `(0,0,0)` and `(2,0,0)`” | explicit theorem hypothesis; the Lattice axiom privileges no site |
| “inward weight relative to the seed being grown” | defined from nearer neighbors; not an extra occupancy axiom |
| “named hop-cost, seed-exit or equal inward weight” | displayed finite probe, not a derived scale |
| “one pair of Dijkstras on `U`” | the definition of `t0` and `t1` |
| “no neighbor strictly earlier for both” | the definition of `M` inside `E` |
| “population variance on `M` and on `E`” | the finite lists of first-meeting and simultaneous-arrival sites |
| “not leftover” of one-seed variance | Theorem 2; different list |
| “Displayed, not adopted” | Theorem 3; no Admissibility edit |

### N4 — citation-to-residual matching

| Evidence path:line | Residual attacked | Residual claimed closed | Match? |
|---|---|---|---:|
| `docs/MINIMAL_AXIOMS_2026-06-29.md:37` | ambient lattice | `Z^3` nearest-neighbor graph | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:57` | Admissibility covariance | one fixed covariant nearest-neighbor rule; no hop cost supplied | yes; cost stays displayed |
| `scripts/two_seed_named_hopcost_meet_2026_08_15.py:290` | two-seed domain and named hop-cost | union of two `B_4` balls; cost 3 on seed-exit or equal inward weight | yes |
| `scripts/two_seed_named_hopcost_meet_2026_08_15.py:295` | one pair of Dijkstras | two `shortest_all` calls | yes |
| `scripts/two_seed_named_hopcost_meet_2026_08_15.py:305` | lex-first meeting site and `t` | `(1, 0, 0)` at `t = 3`, `|M| = 1` | yes |
| `scripts/two_seed_named_hopcost_meet_2026_08_15.py:338` | variance versus ell^1 | zero on `M`; `ρ` strictly below on `E` | yes |
| `scripts/two_seed_named_hopcost_meet_2026_08_15.py:353` | leftover of one-seed variance | note states different list | yes |
| `scripts/two_seed_named_hopcost_meet_2026_08_15.py:358` | adoption of a cost | note and axiom keep the cost out of Admissibility | yes |

No evidence citation is used to claim a path-length axiom or an
Admissibility rewrite.

### N5 — rhetoric and resolution audit

| Resolution | Executed? | Narrow negative supported? |
|---|---:|---|
| per element | yes: each directed union edge | named hop-cost relative to the seed being grown |
| per site | yes: first-meeting and simultaneous-arrival sets on `U` | no other occupancy dictionary is used |
| per mode | yes: one pair of Dijkstras | no other hop-cost is scanned |
| per block | yes: lex-first meeting and variance versus ell^1 | closeness is the stated variance only |
| lattice wide | no | no Admissibility cost and no path-length law are adopted |

The runner prints the same five resolution statements.

### N6 — partial closure and primitive scan

The only dependency used is the registered `minimal_axioms` node. No
approved primitive supplies a named hop-cost or a two-seed meeting law,
and none is reclassified as an import or wall.

Two partial-closure mechanisms are recorded rather than suppressed. The
one-seed `B_3`/`B_4` isochrone variance is a strictly one-center
statement: it does not score two-seed meetings. Uniqueness of first
contact on this union is a strictly weaker statement than a common-ratio
comparison on `E`. The remaining physical choice—whether any hop cost
belongs in Admissibility—stays explicit and does not require an axiom
edit.

### N7 — hostile steelman

The strongest objection is that two radius-4 fronts from seeds two steps
apart must meet only at `(1, 0, 0)`, so the two-seed score is leftover
of the one-seed seed-exit cost `3` and of the one-seed midplane times.
The objection correctly identifies the unique first-contact site and the
seed-exit cost. It fails because `M` is defined from both fronts, `|M|`
is a two-seed report, the midplane list `E` is not the one-seed ball,
and the two variances on `E` are new numbers. Uniqueness is not
required; it is an output.

### N8 — cross-cycle echo

The live axiom memo is the only load-bearing parent. Nearby one-seed
isochrone language is context.

| Earlier surface | Similar issue | Mechanism considered here |
|---|---|---|
| `docs/MINIMAL_AXIOMS_2026-06-29.md` | proper cubic covariance of the nearest-neighbor rule | used only as ambient lattice; the rule itself is not replaced |
| one-seed `B_3`/`B_4` isochrones of `ρ` | same hop-cost, one center | scored as a strictly one-center parent; Theorem 2 is not leftover |
| ell^1 two-ball occupancy census | same seeds, different question | occupied-NN counts are not arrival times |

No earlier mechanism retires the two-seed meeting score or the adoption
refusal.

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

The companion runner builds the two radius-4 balls and their union;
assigns the named hop-cost relative to each seed; runs one pair of
Dijkstras; reports the lex-first first-meeting site `(1, 0, 0)` at
`t = 3` and `|M| = 1`; reports that both population variances on `M`
are zero; reports that on the 25-site midplane `var_ρ` is strictly
below ell^1; rejects the mutation families, including leftover of
one-seed variance; and verifies that the live axiom memo does not host
the named hop-cost. Declared audit inputs are this note and the axiom
memo.
