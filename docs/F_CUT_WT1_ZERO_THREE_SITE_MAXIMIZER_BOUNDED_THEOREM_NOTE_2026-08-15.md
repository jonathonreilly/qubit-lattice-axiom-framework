---
claim_id: f_cut_wt1_zero_three_site_maximizer_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Among the 16 F_cut maps with remaining bit wt1=0 on the two-cube with off-patch o=0, the maximum 3-site coverage is 44, attained by 2 maps. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_wt1_zero_three_site_maximizer_2026_08_15.py
---

# Three-Site Fill-Coverage Maximizer Among The Sixteen `wt1=0` Maps In `F_cut`

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact occupancy-to-lock coverage ranking of the 16 cube-covariant
complement-even predicates that vanish on empty and full and have remaining
bit `wt1=0`, on the twelve-vertex two-cube, over all 220 unordered 3-site
seeds, with off-patch occupancy `0`. The attaining remaining-bit tuples are
displayed. No map is adopted as the physical Admissibility rule.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_wt1_zero_three_site_maximizer_2026_08_15.py`](../scripts/f_cut_wt1_zero_three_site_maximizer_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

The 24 proper cube rotations act on neighbor 6-tuples in `{0,1}^6` and
partition those 64 cells into 10 orbits. Cube-covariant predicates are the
`{0,1}`-assignments to those orbits. The three displayed cuts

1. vanish on empty: `f(empty)=0`,
2. vanish on full: `f(full)=0`,
3. complement-even: `f(c)=f(1-c)`

leave five free bits, so

```text
|F_cut| = 32.
```

The five remaining bits, in the displayed order
`(wt1, opp2, adj2, vertex3, mixed3)`, are the values on the three
complement-pairs and two complement-fixed orbits after empty and full are
forced to `0`. Exactly one of those bits is `wt1`. The subclass scored here
is the 16 maps with remaining bit `wt1=0`.

That static split of `F_cut` is leftover-character inventory. The 32-map
3-site ranking of the same two-cube is a different leftover inventory: it
asked which maps attain the global `Max(3)` of all 32, and both of those
global maximizers have `wt1=1`. This note asks the new coverage object on the subclass:
among the 16 maps with `wt1=0`, what is the maximum number of
the 220 three-site seeds each fills, and is that maximum attained uniquely.

On the two-cube `{0,1,2}×{0,1}×{0,1}`, each unordered triple of vertices is
a 3-site seed. There are `C(12,3)=220` such seeds. Off-patch neighbors
have occupancy `0`. Each tick, every unlocked on-patch vertex evaluates
`f` on its six-neighbor occupancy tuple and locks if `f=1`. The process
is synchronous and stops at a fixed point in at most 12 ticks. Fill means
`|locks_halt|=12`. Coverage is

```text
cov3(f) = |{ S : |S|=3 and f fills from S }|.
```

Do not list the seeds.

`f_L1(c)=1` if and only if some axis is unbalanced: `c_{+μ} ≠ c_{-μ}` for
at least one `μ ∈ {x,y,z}`. Equivalently, some discrete neighbor contrast
`n_μ = c_{+μ} − c_{-μ}` is nonzero. This is **not** Hamming parity
`|c|_1 mod 2`. The unbalanced-axis map has remaining-bit tuple
`(1, 0, 1, 1, 1)`, so remaining bit `wt1=1`. It is outside the scored
subclass and is not a candidate for the subclass maximizer.

**Theorem 1.** Exhaustive enumeration of the 16 maps with remaining bit
`wt1=0` on all 220 three-site seeds gives

```text
m3 = 44
N_max = 2
```

so the subclass maximum 3-site coverage is 44, attained by 2 maps.

**Theorem 2.** So `N_max > 1`: the `wt1=0` subclass does not have a
unique 3-site maximizer. There is no single remaining-bit tuple that
alone attains `m3`.

**Theorem 3.** The two attaining remaining-bit tuples, displayed and not
adopted, are

```text
(0, 1, 1, 1, 0), (0, 1, 1, 1, 1).
```

Do not write the ranking into Admissibility.

Not leftover-character of the 32-map 3-site ranking (that leftover named
the global `Max(3)` pair, both with `wt1=1`). The present object is a new
coverage object on the subclass.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The ten-orbit reconstruction, the 32-element F_cut, the 16-element wt1=0 subclass, and the 3-site coverage-ranking pair (m3,N_max)=(44,2) with displayed remaining-bit tuples (0,1,1,1,0) and (0,1,1,1,1) are enumerated. Uniqueness of a 3-site maximizer inside the subclass is false on this patch. No physical law is selected."
trace_class: upstream_support
target_claim_id: f_cut_wt1_zero_three_site_maximizer
target_blocker_text: "whether 3-site coverage selects a unique member inside the wt1=0 half of F_cut"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the wt1=0 3-site coverage ranking; any physical use must separately derive an Admissibility selector"
conditional_surface_status: "exact for the wt1=0 half of F_cut on this twelve-vertex patch with off-patch o=0 and all 220 three-site seeds; no Z^3-wide law and no physical selector"
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
- the complete set of 220 unordered 3-site seeds;
- the remaining-bit filter `wt1=0`.

No observational comparator, literature constant, Wilson weight, rate, or
generator is imported. No Record scalar functional appears.

## Exact Target And Objects

**Target.** Rank the 16 members of `F_cut` with remaining bit `wt1=0` by
three-site fill coverage on the two-cube, report the pair `(m3, N_max)`,
decide whether `N_max` equals one, and display the attaining remaining-bit
tuples without adopting a map.

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
`f(c)=f(1-c)`. The empty/full pair is forced to `0`. The remaining free
data are three complement-pair bits and two complement-fixed orbit bits,
so `|F_cut|=32`. The remaining-bit tuple is those five bits in the order
`(wt1, opp2, adj2, vertex3, mixed3)`. The scored subclass is the 16
tuples whose first coordinate is `0`.

Define

```text
f_L1(c)     = 1  iff  u(c) ≥ 1,
```

so `f_L1` has remaining-bit tuple `(1, 0, 1, 1, 1)` and lies outside the
subclass. Neither `f_L1` nor either displayed maximizer is adopted.

A locked set `S` determines occupancies: a lattice neighbor in `S` has
occupancy `1`, and every other neighbor — including every off-patch
neighbor — has occupancy `0`. One synchronous tick replaces `S` by

```text
S ∪ { v in two-cube \ S : f(neighborhood_6(v; S)) = 1 }.
```

Then `cov3(f)` is the number of 3-site seeds whose halt set has cardinality
12, `m3` is the maximum of `cov3` over the 16 maps with `wt1=0`, and
`N_max` is the number of those maps attaining `m3`.

## Theorems

**Theorem 1.** There are exactly 24 proper cube rotations and exactly 10
orbits on `{0,1}^6`. The three cuts leave `|F_cut|=32`. Exactly 16 of
those maps have remaining bit `wt1=0`. The unbalanced-axis map `f_L1` is
one element of `F_cut` and is not Hamming parity; its remaining bit
`wt1` is `1`, so it is not among the 16. On the twelve-vertex two-cube
with off-patch occupancy `0`, exhaustive ranking of the 16 maps on all
220 three-site seeds gives

```text
m3 = 44
N_max = 2
```

**Theorem 2.** Because `N_max > 1`, 3-site coverage does not select a
unique member inside the `wt1=0` half. There is not a unique 3-site
maximizer on this subclass, and there is no single remaining-bit tuple
to report as the unique maximizer.

**Theorem 3.** The two maps that attain `m3` have remaining-bit tuples

```text
(0, 1, 1, 1, 0), (0, 1, 1, 1, 1).
```

They differ only on the complement-fixed orbit `mixed3`. Both are
displayed. Neither is adopted as the physical Admissibility rule.

## Proof-Obligation Graph

| obligation | exact disposition |
|---|---|
| 24 proper cube rotations | signed permutations of the three axes with determinant `+1` |
| 10 orbits on `{0,1}^6` | axis-type classes `(u,b,e)` partition the 64 cells with the listed sizes |
| `|F_cut|=32` | three complement-pairs and two complement-fixed orbits remain free after empty/full are forced to `0` |
| 16 maps with `wt1=0` | the remaining bit on orbit `(1,0,2)` and its complement `(1,2,0)` is fixed to `0`; the other four free bits vary |
| 220 three-site seeds | `C(12,3)` unordered triples on the two-cube |
| `f_L1` is not Hamming | unbalanced-axis predicate disagrees with `|c|_1 mod 2` and has remaining bits `(1, 0, 1, 1, 1)` |
| pair `(m3, N_max)` | exhaustive `cov3` on the 16 maps yields `(44, 2)` |
| uniqueness | fails: `N_max > 1` |
| displayed tuples | `(0, 1, 1, 1, 0)` and `(0, 1, 1, 1, 1)`, not adopted |

## What This Does Not Claim

- No physical Admissibility selector.
- No `Z^3`-wide formation law.
- No ranking of the complementary 16 maps with `wt1=1`.
- No reopening of the 32-map global `Max(3)` pair.
- No blank-block or 4-site variant.

## No-Go Discipline Gate

The only negative claim is uniqueness of the maximizer: the `wt1=0`
subclass of `F_cut` does not have a unique 3-site coverage maximizer on
this patch. The positive pair `(m3, N_max)=(44, 2)` is an exact
enumeration, not a wall.

### N1 — materially distinct routes

| Route | Exact attack | Result and authority | Marker |
|---|---|---|---|
| orbit reconstruction | Recompute the 24 rotations and the 10 axis-type orbits. | Theorem 1 and checks `thm1-twenty-four-rotations` / `thm1-ten-orbits`. | **ATTEMPTED** |
| three-cut class | Force vanish-on-empty, vanish-on-full, and `f(c)=f(1-c)`. | Theorem 1 and check `thm1-f-cut-and-wt1-zero-cardinality` give `|F_cut|=32`. | **ATTEMPTED** |
| `wt1=0` subclass | Fix remaining bit `wt1` to `0` and count the remaining 16 maps. | Theorem 1 and the same cardinality check. | **ATTEMPTED** |
| Hamming-as-`f_L1` | Test whether `|c|_1 mod 2` equals the unbalanced-axis predicate. | Theorem 1 and check `thm1-f-L1-not-hamming` separate the maps. | **ATTEMPTED** |
| subclass 3-site ranking | Score every `wt1=0` map by `cov3`. | Theorem 1 and check `thm1-m3-and-n-max` give `m3 = 44` and `N_max = 2`. | **ATTEMPTED** |
| uniqueness of a maximizer | Ask whether the maximizer class is a singleton. | Theorem 2 and checks `thm2-not-unique-maximizer` / `thm3-displayed-maximizers`. | **ATTEMPTED** |

### N2 — wall independence and collapse

There is one negative conclusion: uniqueness of the maximizer fails. The
explicit two-tuple display and the cardinality `N_max=2` are two
certificates of the same non-uniqueness, so they collapse rather than
count as two walls.

| Pair | First closes second? | Second closes first? | Disposition |
|---|---:|---:|---|
| `N_max=2` / displayed pair | yes: a count larger than one is non-uniqueness | yes: two displayed maximizers are non-uniqueness | collapse into the uniqueness failure |
| `m3=44` / uniqueness failure | no: a score does not name the multiplicity | no: non-uniqueness does not name the score | independent positive integer versus uniqueness |
| static 16-map subclass / ranking pair `(m3, N_max)` | no: membership is not dynamics | no: a ranking does not replace the remaining-bit filter | separate exact counts |
| leftover 32-map `Max(3)` / this ranking | no: that leftover scored all 32 maps | no: a subclass ranking does not replace the global pair | different object |

Physical law selection is not a wall: this note makes no negative theorem
about the existence of a selector and simply does not claim one.

### N3 — hidden-condition scan

| Phrase or premise | Classification |
|---|---|
| “work on the twelve-vertex two-cube” | explicit patch hypothesis; not a `Z^3` theorem |
| off-patch occupancy `0` | explicit default; blank-block is a different rule |
| `F_cut` | explicit three-cut class; the other 992 covariant maps are excluded |
| remaining bit `wt1=0` | explicit subclass filter; the complementary 16 maps are excluded |
| all 220 three-site seeds | explicit seed class; a 2-site ranking is a different residual |
| “lock” | Record permanence on this Boolean occupancy model, not a possibility-valued law |
| “cube-covariant” | invariance under the 24 proper rotations, cited to Lattice/Admissibility |
| Hamming parity | displayed mutation only |
| remaining-bit tuples `(0, 1, 1, 1, 0)` and `(0, 1, 1, 1, 1)` | displayed witnesses against uniqueness, not selected laws |

### N4 — citation-to-residual matching

| Evidence path:line | Residual attacked | Residual claimed closed | Match? |
|---|---|---|---:|
| `docs/MINIMAL_AXIOMS_2026-06-29.md:37` | ambient lattice and cubic rotations | sites are `Z^3` with proper cubic rotations | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:57` | covariant nearest-neighbor rule | covariance is the class filter, not a selector | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:79` | lock permanence | a locked site stays locked | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:83` | unreadability of absence | unlocked and off-patch sites contribute occupancy `0`, not a readout | yes |
| `scripts/f_cut_wt1_zero_three_site_maximizer_2026_08_15.py:74` | 24 proper rotations | signed permutations with determinant `+1` | yes |
| `scripts/f_cut_wt1_zero_three_site_maximizer_2026_08_15.py:118` | `f_L1` definition | unbalanced-axis predicate, not Hamming | yes |
| `scripts/f_cut_wt1_zero_three_site_maximizer_2026_08_15.py:123` | Hamming mutation | `|c|_1 mod 2` is a different `F_cut` map | yes |
| `scripts/f_cut_wt1_zero_three_site_maximizer_2026_08_15.py:49` | 220 three-site seeds | `C(12,3)` unordered triples on the two-cube | yes |
| `scripts/f_cut_wt1_zero_three_site_maximizer_2026_08_15.py:183` | `cov3(f)` | number of 3-site seeds a map fills | yes |
| `scripts/f_cut_wt1_zero_three_site_maximizer_2026_08_15.py:285` | subclass ranking | `wt1=0` filter and `cov3` on those 16 maps | yes |
| `scripts/f_cut_wt1_zero_three_site_maximizer_2026_08_15.py:347` | pair `(m3, N_max)` | exact maximum and multiplicity on the subclass | yes |
| `scripts/f_cut_wt1_zero_three_site_maximizer_2026_08_15.py:60` | `f_L1` remaining bits | `(1, 0, 1, 1, 1)` lies outside `wt1=0` | yes |

No evidence citation is used to claim that a physical occupancy law, a
formation rate, or a `Z^3`-wide selector has been closed.

### N5 — rhetoric and resolution audit

| Resolution | Executed? | Narrow negative supported? |
|---|---:|---|
| per element | yes: all 64 neighbor 6-tuples | each is assigned its axis-type orbit; no broader cell class is classified |
| per site | yes: the twelve two-cube vertices | each uses the same six-direction stencil with off-patch occupancy `0` |
| per mode | yes: every map in the `wt1=0` half of `F_cut` | the ranking is this subclass on all 220 seeds; other classes are unclaimed |
| per block | yes: the pair `(m3, N_max)` | uniqueness fails because `N_max=2` |
| lattice wide | no | no `Z^3`-wide formation or Admissibility selector is asserted |

The runner prints the same five resolution statements.

### N6 — partial closure and primitive scan

The primitive registry at `docs/audit/data/axiom_premise_nodes.json` was
checked. The only dependency used is the registered `minimal_axioms` node.
Approved primitives are `scale_reference_primitive`,
`kinetic_isotropy_primitive`, and `realized_state_primitive`. None of them
supplies a Boolean occupancy map, a seed-coverage ranking, or an
Admissibility selector, and none is reclassified as an import or wall.

One partial-closure mechanism is displayed rather than suppressed: the
subclass does have a well-defined 3-site maximum `m3=44`, attained by two
explicit remaining-bit tuples. That positive pair does not make either
tuple the unique maximizer and does not select either as the physical
rule. The remaining physical choice — which, if any, `F_cut` map is the
Admissibility occupancy predicate — stays explicit.

The open derivation-obligation registry
(`docs/audit/data/derivation_obligations.json`) names no occupancy-to-lock
coverage target; those open gates are unused here.

### N7 — hostile steelman

The strongest objection is that the 32-map 3-site ranking already showed
no `wt1=0` map lies in the global maximizer pair, so a ranking inside the
16 might be called leftover decoration of that split. That objection is
correctly about exclusion from the global `Max(3)`. It does not overturn
the stated theorem: among the 16 maps with `wt1=0`, three-site coverage
selects a two-element class `{(0, 1, 1, 1, 0), (0, 1, 1, 1, 1)}` with
score `44`, not a singleton. Exclusion from the global pair does not name
the subclass maximum or its multiplicity. This is a new coverage object on the subclass.

### N8 — cross-cycle echo

Repository search found nearby occupancy and covariance surfaces. They are
context, not load-bearing dependencies. The 24 rotations, 10 orbits,
`F_cut`, the `wt1=0` filter, and the 16-map 220-seed ranking are
recomputed here.

| Earlier surface | Similar issue | Mechanism considered here |
|---|---|---|
| `docs/ADMISSIBILITY_COVARIANT_Q8_CONDITIONAL_LAW_PAIR_BOUNDED_THEOREM_NOTE_2026-08-13.md` | proper-cubic covariance of a local rule | covariance is used only as the orbit filter for Boolean maps |
| `docs/PHYSICAL_SPATIAL_BLOCK_SEAM_DICHOTOMY_CYCLE728_NOTE_2026-08-04.md` | two-cell box `{0,1,2}×{0,1}×{0,1}` | the same twelve spatial vertices are the patch; the seam cost is unused |
| `docs/MINIMAL_AXIOMS_2026-06-29.md` | one covariant nearest-neighbor rule | the axiom names the contract; this note does not select the rule |

No earlier mechanism retires the `wt1=0` 3-site coverage ranking or
restores uniqueness of a maximizer inside the 16-map subclass.

No-Go Discipline disposition: **PASS** for the uniqueness failure and the
exact pair `(m3, N_max)` stated above.

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
`F_cut`, restricts to the 16 maps with remaining bit `wt1=0`, evaluates
those maps on the two-cube from every 3-site seed, reports `m3 = 44` and
`N_max = 2`, checks that `f_L1` is not Hamming parity and lies outside
the subclass, and exhibits the displayed maximizers by remaining-bit
tuples `(0, 1, 1, 1, 0)` and `(0, 1, 1, 1, 1)`. Declared audit inputs are
this note and the axiom memo. No runner cache is written.
