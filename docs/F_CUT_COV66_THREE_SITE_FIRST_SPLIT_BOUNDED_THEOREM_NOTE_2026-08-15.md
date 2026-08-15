---
claim_id: f_cut_cov66_three_site_first_split_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On the two-cube with off-patch o=0, the first 3-site seed at which the two F_cut cov=66 maximizers disagree is {(0,0,0),(1,0,1),(2,0,0)}: remaining-bit (1,1,1,1,0) does not fill and (1,1,1,1,1) does. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_cov66_three_site_first_split_2026_08_15.py
---

# First 3-Site Seed Where The Two `F_cut` `cov=66` Maximizers Disagree

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact naming of the first unordered 3-site seed, in
`combinations` order on the twelve-vertex two-cube
`{0,1,2}×{0,1}×{0,1}` with off-patch occupancy `0`, at which the two
`F_cut` maps that fill every 2-site seed disagree by fill. Remaining-bit
`(1,1,1,1,0)` does not fill that seed. Remaining-bit `(1,1,1,1,1)` does.
The seed and both lock histories are displayed. Neither map is adopted
as the physical Admissibility rule.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_cov66_three_site_first_split_2026_08_15.py`](../scripts/f_cut_cov66_three_site_first_split_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

The 24 proper cube rotations act on neighbor 6-tuples in `{0,1}^6` and
partition those 64 cells into 10 orbits. Cube-covariant predicates are the
`{0,1}`-assignments to those orbits. The three displayed cuts

1. vanish on empty: `f(empty)=0`,
2. vanish on full: `f(full)=0`,
3. complement-even: `f(c)=f(1-c)`

leave five free bits, so `|F_cut| = 32`.

On the two-cube `{0,1,2}×{0,1}×{0,1}`, each unordered pair of vertices is
a 2-site seed. There are `C(12,2)=66` such seeds. Off-patch neighbors
have occupancy `0`. Each tick, every unlocked on-patch vertex evaluates
`f` on its six-neighbor occupancy tuple and locks if `f=1`. The process
is synchronous and stops at a fixed point in at most 12 ticks. Fill means
`|locks_halt|=12`. Coverage is

```text
cov(f) = |{ S : |S|=2 and f fills from S }|.
```

The two maps that attain `cov=66` have remaining-bit tuples
`(wt1, opp2, adj2, vertex3, mixed3) = (1, 1, 1, 1, 0)` and
`(1, 1, 1, 1, 1)`. Write `f0` for the first and `f1` for the second.
They agree on every 2-site fill. This note does not rerun the 32-map
ranking as its residual. Not leftover-character of that ranking. Not an
`|S|` census. Not leftover-character of #6427 of the `f_min` versus `f_L1` three-site
split. The new object is the first 3-site seed, in
`combinations(TWO_CUBE, 3)` order with

```text
TWO_CUBE = ((x, y, z) : x ∈ {0,1,2}, y ∈ {0,1}, z ∈ {0,1}),
```

at which `fill(f0) ≠ fill(f1)`.

`f_L1(c)=1` if and only if some axis is unbalanced: `c_{+μ} ≠ c_{-μ}` for
at least one `μ ∈ {x,y,z}`. Equivalently, some discrete neighbor contrast
`n_μ = c_{+μ} − c_{-μ}` is nonzero. This is **not** Hamming parity
`|c|_1 mod 2`. The 1-site halt of either maximizer from `{(0,0,0)}`
agrees with `f_L1`: history `(1, 4, 8, 11, 12)` and fill. That failed-bar
is not the residual here.

**Theorem 1.** Both maps have two-site `cov=66` and agree on every 2-site
fill. The first 3-site seed where `fill(f0) ≠ fill(f1)` is

```text
S* = {(0,0,0), (1,0,1), (2,0,0)}.
```

`f0` does not fill. `f1` fills.

**Theorem 2.** On `S*`, the lock-count histories are `f0: (3, 8, 10)`
(halts unfilled) and `f1: (3, 9, 12)` (fills). Do not adopt either map.
Do not write them into Admissibility.

**Theorem 3.** Display. The first-wave neighborhood of `(1, 0, 0)` on
`S*` is `mixed3`. `f0` has `mixed3=0` and does not lock that site. `f1`
has `mixed3=1` and locks it. This is why they split. Do not list the
other 3-site seeds on which the two maps later disagree.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The two cov=66 maps, their 2-site agreement, the first combinations-order 3-site fill disagreement, the two lock histories, and the mixed3 neighborhood of (1,0,0) are enumerated. The seed is displayed, not written into Admissibility."
trace_class: frontier_discovery
target_claim_id: f_cut_cov66_three_site_first_split
target_blocker_text: "the first 3-site seed at which the two F_cut cov=66 maximizers disagree remains unnamed"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the displayed first-split seed; any physical use must separately derive an Admissibility selector"
conditional_surface_status: "exact for these two F_cut maps on this twelve-vertex patch with off-patch o=0 and combinations order on 3-site seeds; no Z^3-wide law and no physical selector"
hypothetical_axiom_status: "not proposed; no axiom or approved primitive is added"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Premises And Declared Mathematical Objects

The only scientific dependency is the current four-axiom authority linked
above. Lattice supplies `Z^3`, nearest-neighbor adjacency, and proper cubic
rotations. Admissibility supplies one fixed nearest-neighbor rule covariant
under those rotations. Record supplies permanence of a lock and unreadability
of an absent record. Qubit is unused beyond the ambient one-site algebra
boundary: the maps here are Boolean occupancy predicates, not `M_2(C)`-valued
laws.

The following are declared mathematical scaffolding, not measured or fitted
physics inputs:

- the 24 proper signed-permutation rotations of the three axes
  (`det = +1`);
- occupancy 6-tuples on the ordered neighbor stencil
  `(+x,-x,+y,-y,+z,-z)`;
- the two-cube vertex set `{0,1,2}×{0,1}×{0,1}`;
- the off-patch occupancy default `0`;
- `combinations` order on that vertex tuple for unordered 3-site seeds.

No observational comparator, literature constant, Wilson weight, rate, or
generator is imported. No Record scalar functional appears.

Not leftover-character of the two-site coverage ranking. Not leftover-character of #6427
of the `f_min` versus `f_L1` three-site split. Not an `|S|` census.

## Exact Target And Objects

**Target.** Reconfirm that the two named `cov=66` maximizers agree on
every 2-site fill, then name the first 3-site seed in combinations order
at which their fill bits differ, together with the two lock histories and
the first-wave neighborhood that causes the split.

Write a neighbor configuration as `c ∈ {0,1}^6`. A proper cube rotation `R`
acts by `(R·c)(d) = c(R^{-1}d)` on the six face directions `d`. A map
`f:{0,1}^6 → {0,1}` is cube-covariant when `f(R·c)=f(c)` for every such `R`.
Equivalently, `f` is constant on each orbit.

The axis type of `c` is the triple `(u,b,e)` with `u+b+e=3`, where `u` is
the number of axes with `c_{+} ≠ c_{-}`, `b` the number with
`(c_{+},c_{-})=(1,1)`, and `e` the number with `(c_{+},c_{-})=(0,0)`. These
ten types are exactly the ten orbits. Complement sends `(u,b,e)` to
`(u,e,b)`.

| remaining name | `(u,b,e)` | orbit size | complement image |
|---|---|---:|---|
| empty | `(0,0,3)` | 1 | full |
| full | `(0,3,0)` | 1 | empty |
| `opp2` | `(0,1,2)` | 3 | `(0,2,1)` |
| `wt1` | `(1,0,2)` | 6 | `(1,2,0)` |
| `adj2` | `(2,0,1)` | 12 | `(2,1,0)` |
| `mixed3` | `(1,1,1)` | 12 | itself |
| `vertex3` | `(3,0,0)` | 8 | itself |

`F_cut` is the class of cube-covariant maps with `f(empty)=f(full)=0` and
`f(c)=f(1-c)`. The remaining-bit tuple is the five free bits in the order
`(wt1, opp2, adj2, vertex3, mixed3)`. The two displayed maximizers are

```text
f0 : (1, 1, 1, 1, 0)
f1 : (1, 1, 1, 1, 1)
```

Neither map is adopted. They differ only on the complement-fixed orbit
`mixed3`.

Define

```text
f_L1(c)     = 1  iff  u(c) ≥ 1,
```

so `f_L1` has remaining-bit tuple `(1, 0, 1, 1, 1)`. It is displayed only
as the 1-site failed-bar that both maximizers share.

A locked set `S` determines occupancies: a lattice neighbor in `S` has
occupancy `1`, and every other neighbor — including every off-patch
neighbor — has occupancy `0`. One synchronous tick replaces `S` by

```text
S ∪ { v in two-cube \ S : f(neighborhood_6(v; S)) = 1 }.
```

The lock history is the sequence of lock cardinalities after the seed and
after each nonempty wave, until halt. Fill is `|locks_halt|=12`.

## Theorems

**Theorem 1.** There are exactly 24 proper cube rotations and exactly 10
orbits on `{0,1}^6`. The three cuts leave `|F_cut|=32`. Both remaining-bit
tuples `(1, 1, 1, 1, 0)` and `(1, 1, 1, 1, 1)` lie in `F_cut`. Exhaustive
scoring of all 66 two-site seeds reconfirms `cov(f0)=cov(f1)=66` and that
the two maps agree on every 2-site fill. Walking
`combinations(TWO_CUBE, 3)` in the declared vertex order, the first 3-site
seed at which the fill bits differ is

```text
S* = {(0,0,0), (1,0,1), (2,0,0)}.
```

`f0` does not fill. `f1` fills. `f_L1` is not Hamming parity.

**Theorem 2.** On `S*`, lock histories are `f0: (3, 8, 10)` (halts
unfilled) and `f1: (3, 9, 12)` (fills). Do not adopt either map. Do not
write them into Admissibility. The 1-site halt of either map from
`{(0,0,0)}` is `(1, 4, 8, 11, 12)`, the same as `f_L1`; that agreement
is not a 3-site selector.

**Theorem 3.** Display. The first-wave neighborhood of `(1, 0, 0)` on
`S*` has occupancy `(+x,-x,+y,-y,+z,-z) = (1, 1, 0, 0, 1, 0)`, which is
axis type `(1, 1, 1)` and therefore `mixed3`. `f0` has `mixed3=0` and
does not lock `(1, 0, 0)`. `f1` has `mixed3=1` and locks it. The first
wave of `f0` therefore reaches eight locks and the first wave of `f1`
reaches nine. That single site is why they split. Do not adopt the seed.
Do not list the other later 3-site fill disagreements.

## Proof-Obligation Graph

| obligation | exact disposition |
|---|---|
| 24 proper cube rotations | signed permutations of the three axes with determinant `+1` |
| 10 orbits on `{0,1}^6` | axis-type classes `(u,b,e)` partition the 64 cells with the listed sizes |
| `|F_cut|=32` | three complement-pairs and two complement-fixed orbits remain free after the vanish cuts |
| two named maximizers in `F_cut` | remaining-bit tuples `(1, 1, 1, 1, 0)` and `(1, 1, 1, 1, 1)` |
| `cov=66` for both | exhaustive 66-seed fill census of each map |
| agree on every 2-site fill | pairwise comparison of the 66 fill bits |
| first 3-site split | first `combinations(TWO_CUBE, 3)` seed with unequal fill bits is `S*` |
| `f0` does not fill `S*` | halt history `(3, 8, 10)` with ten locks |
| `f1` fills `S*` | halt history `(3, 9, 12)` with twelve locks |
| mixed3 display | neighborhood of `(1, 0, 0)` on `S*` is `(1,1,1)`; `f0` refuses it and `f1` locks it |
| `f_L1` is not Hamming | the two-unbalanced-axis orbit has even weight and `f_L1=1` |
| off-patch occupancy `0` | declared stencil default; not a blank-block |
| not written into Admissibility | both maps and `S*` are displayed only |

## Counterfactual And Mutation Table

1. Replace `f_L1` by Hamming parity: Hamming is a different `F_cut` map
   and is not a coverage maximizer.
2. Replace off-patch occupancy `0` by a blank-block: first-wave candidates
   become undefined; that is a different census.
3. Walk a different vertex order: the first disagreeing seed may change;
   the residual here is combinations order on the declared `TWO_CUBE`.
4. Report an `|S|` count of all 3-site disagreements: that leftover is a
   census, not the first-split seed.
5. Recycle leftover-character of #6427 of `f_min` versus `f_L1`: those maps are not the
   two `cov=66` maximizers; `f_min` is not in `F_cut`.
6. Adopt either remaining-bit tuple, or adopt `S*`, as the physical rule:
   the note displays both maps and the seed and writes none of them into
   Admissibility.

## What This Does Not Claim

- No physical Admissibility selector and no adopted occupancy law.
- No Qubit rewrite and no `M_2(C)`-valued conditional probability.
- No `Z^3`-wide formation, rate, or generator.
- No identification of `f_L1` with Hamming parity.
- No `|S|` census and no count of later 3-site disagreements.
- No leftover-character restatement of leftover-character of #6427 (`f_min` versus `f_L1`).
- No blank-block variant.

## No-Go Discipline Gate

The only negative claim is that the two `cov=66` maximizers, which agree
on every 2-site fill and on the 1-site halt, are not the same 3-site fill
map. The first combinations-order disagreement is an exact seed, not a
wall.

### N1 — materially distinct routes

| Route | Exact attack | Result and authority | Marker |
|---|---|---|---|
| orbit reconstruction | Recompute the 24 rotations and the 10 axis-type orbits. | Theorem 1 and checks `thm1-twenty-four-rotations` / `thm1-ten-orbits`. | **ATTEMPTED** |
| two-site agreement | Score both maps on all 66 two-site seeds. | Theorem 1 and check `thm1-cov66-and-two-site-agreement` give `cov=66` and pairwise fill agreement. | **ATTEMPTED** |
| Hamming-as-`f_L1` | Test whether `|c|_1 mod 2` equals the unbalanced-axis predicate. | Theorem 1 and check `thm1-f-L1-not-hamming` separate the maps. | **ATTEMPTED** |
| combinations walk | Walk every 3-site seed in declared order until fill bits differ. | Theorem 1 and check `thm1-first-three-site-split` name `S*`. | **ATTEMPTED** |
| lock histories | Record lock counts on `S*` for both maps. | Theorem 2 and check `thm2-lock-histories` give `(3, 8, 10)` and `(3, 9, 12)`. | **ATTEMPTED** |
| display, do not adopt | Ask whether either map or `S*` is written into Admissibility. | Theorem 3 and check `thm3-display-not-adopted`. | **ATTEMPTED** |

### N2 — wall independence and collapse

There is one negative conclusion: the two maximizers are not the same
3-site fill map. Naming `S*` and displaying the mixed3 neighborhood are
two certificates of the same first-split, so they collapse rather than
count as two walls.

| Pair | First closes second? | Second closes first? | Disposition |
|---|---:|---:|---|
| first-split seed / mixed3 display | yes: the seed is the site where mixed3 is first asked | yes: mixed3 on `(1, 0, 0)` is why that seed splits | collapse into the first-split |
| 2-site agreement / 3-site first split | no: pairwise 2-site equality does not name a 3-site seed | no: one 3-site split does not replace 2-site agreement | independent exact statements |
| leftover-character of #6427 `f_min`/`f_L1` / this first-split | no: those maps are a different pair | no: naming `S*` does not recast leftover-character of #6427 | different object |
| `|S|` census / first-split seed | no: a count does not name the first seed | no: one seed does not replace a census | different object |

Physical law selection is not a wall: this note makes no negative theorem
about the existence of a selector and simply does not claim one.

### N3 — hidden-condition scan

| Phrase or premise | Classification |
|---|---|
| “work on the twelve-vertex two-cube” | explicit patch hypothesis; not a `Z^3` theorem |
| off-patch occupancy `0` | explicit default; blank-block is a different rule |
| `F_cut` | explicit three-cut class; the other 992 covariant maps are excluded |
| combinations order on `TWO_CUBE` | explicit seed order; a different order is a different first seed |
| “lock” | Record permanence on this Boolean occupancy model, not a possibility-valued law |
| “cube-covariant” | invariance under the 24 proper rotations, cited to Lattice/Admissibility |
| Hamming parity | displayed mutation only |
| remaining-bit tuples `(1, 1, 1, 1, 0)` and `(1, 1, 1, 1, 1)` | displayed rival pair, not a selected law |
| `S* = {(0,0,0),(1,0,1),(2,0,0)}` | displayed first-split seed, not a selected law |

### N4 — citation-to-residual matching

| Evidence path:line | Residual attacked | Residual claimed closed | Match? |
|---|---|---|---:|
| `docs/MINIMAL_AXIOMS_2026-06-29.md:37` | ambient lattice and cubic rotations | sites are `Z^3` with proper cubic rotations | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:57` | covariant nearest-neighbor rule | covariance is the class filter, not a selector | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:79` | lock permanence | a locked site stays locked | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:83` | unreadability of absence | unlocked and off-patch sites contribute occupancy `0`, not a readout | yes |
| `scripts/f_cut_cov66_three_site_first_split_2026_08_15.py:85` | 24 proper rotations | signed permutations with determinant `+1` | yes |
| `scripts/f_cut_cov66_three_site_first_split_2026_08_15.py:129` | `f_L1` definition | unbalanced-axis predicate, not Hamming | yes |
| `scripts/f_cut_cov66_three_site_first_split_2026_08_15.py:134` | Hamming mutation | `|c|_1 mod 2` is a different `F_cut` map | yes |
| `scripts/f_cut_cov66_three_site_first_split_2026_08_15.py:52` | 66 two-site seeds | `C(12,2)` unordered pairs on the two-cube | yes |
| `scripts/f_cut_cov66_three_site_first_split_2026_08_15.py:55` | 3-site combinations order | `combinations(TWO_CUBE, 3)` | yes |
| `scripts/f_cut_cov66_three_site_first_split_2026_08_15.py:220` | `cov(f)` | number of 2-site seeds a map fills | yes |
| `scripts/f_cut_cov66_three_site_first_split_2026_08_15.py:231` | first 3-site fill split | first combinations-order seed with unequal fill bits | yes |
| `scripts/f_cut_cov66_three_site_first_split_2026_08_15.py:204` | lock histories | lock-count sequence until halt | yes |
| `scripts/f_cut_cov66_three_site_first_split_2026_08_15.py:182` | mixed3 neighborhood | six-neighbor occupancy of `(1, 0, 0)` on `S*` | yes |

No evidence citation is used to claim that a physical occupancy law, a
formation rate, or a `Z^3`-wide selector has been closed.

### N5 — rhetoric and resolution audit

| Resolution | Executed? | Narrow negative supported? |
|---|---:|---|
| per element | yes: all 64 neighbor 6-tuples | each is assigned its axis-type orbit; no broader cell class is classified |
| per site | yes: the twelve two-cube vertices | each uses the same six-direction stencil with off-patch occupancy `0` |
| per mode | yes: both `cov=66` maximizers | 2-site agreement and the first 3-site fill disagreement are named |
| per block | yes: the first-split seed | `S*` is displayed; later 3-site disagreements are not listed |
| lattice wide | no | no `Z^3`-wide formation or Admissibility selector is asserted |

The runner prints the same five resolution statements.

### N6 — partial closure and primitive scan

The primitive registry at `docs/audit/data/axiom_premise_nodes.json` was
checked. The only dependency used is the registered `minimal_axioms` node.
No approved primitive supplies the Boolean occupancy maps, and none is
reclassified as an import or wall.

One partial-closure mechanism is displayed rather than suppressed: both
maximizers agree with `f_L1` on the 1-site halt and agree with each other
on every 2-site fill. That positive agreement does not make them the same
3-site fill map and does not select either tuple as the physical rule.
The remaining physical choice — which, if any, `F_cut` map is the
Admissibility occupancy predicate — stays explicit.

### N7 — hostile steelman

The strongest objection is that because the two maximizers differ only on
`mixed3`, any 3-site seed that first asks a mixed3 neighborhood is a
leftover-character of the two-map naming, or a leftover-character of #6427 restatement of
the `f_min` versus `f_L1` split (those maps also disagree on mixed3). That
objection is correctly about the bit that distinguishes the maps. It does
not overturn the stated theorem: leftover-character of #6427 named a different pair and
reported an `|S|` count; the two-map naming stopped at the remaining-bit
tuples. The residual here is the first combinations-order 3-site seed at
which those two maps disagree by fill, together with the two lock
histories. Displaying `S*` names that seed. Neither map is adopted.

### N8 — cross-cycle echo

Repository search found nearby occupancy and covariance surfaces. They are
context, not load-bearing dependencies. The 24 rotations, 10 orbits, the
two remaining-bit tuples, the 66-seed 2-site agreement, and the first
3-site fill split are recomputed here.

| Earlier surface | Similar issue | Mechanism considered here |
|---|---|---|
| `docs/ADMISSIBILITY_COVARIANT_Q8_CONDITIONAL_LAW_PAIR_BOUNDED_THEOREM_NOTE_2026-08-13.md` | proper-cubic covariance of a local rule | covariance is used only as the orbit filter for Boolean maps |
| `docs/PHYSICAL_SPATIAL_BLOCK_SEAM_DICHOTOMY_CYCLE728_NOTE_2026-08-04.md` | two-cell box `{0,1,2}×{0,1}×{0,1}` | the same twelve spatial vertices are the patch; the seam cost is unused |
| `docs/MINIMAL_AXIOMS_2026-06-29.md` | one covariant nearest-neighbor rule | the axiom names the contract; this note does not select the rule |

No earlier mechanism retires the first-split seed or writes either
remaining-bit tuple into Admissibility.

No-Go Discipline disposition: **PASS** for the named first 3-site fill
split and the two displayed lock histories stated above.

## Live Parent Quotes

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

> There is one fixed nearest-neighbor admissibility rule, covariant under lattice
> translations and proper cubic rotations.

> When present, a record locks exactly one admissible local possibility. A
> site never carries more than one record; records are permanent.

> Only records are readable. A readout value is determined by record content
> alone. A site with no record cannot be read.

## Runner Contract

The companion runner reconstructs the 24 rotations and 10 orbits, rebuilds
the two `F_cut` maximizers from remaining-bit tuples `(1, 1, 1, 1, 0)` and
`(1, 1, 1, 1, 1)`, evaluates both maps on every 2-site seed, reconfirms
`cov=66` and pairwise fill agreement, walks `combinations(TWO_CUBE, 3)`
until the first fill disagreement, reports `S* = {(0,0,0),(1,0,1),(2,0,0)}`
with histories `(3, 8, 10)` and `(3, 9, 12)`, displays the mixed3
neighborhood of `(1, 0, 0)`, checks that `f_L1` is not Hamming parity, and
does not adopt either map. Declared audit inputs are this note and the
axiom memo. No runner cache is written.
