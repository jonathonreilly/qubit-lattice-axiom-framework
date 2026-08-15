---
claim_id: f_cut_three_site_coverage_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Among the 32 F_cut maps on the two-cube with off-patch o=0, the maximum number of 3-site seeds filled is 220, attained by 2 maps. f_L1 is not the unique maximizer. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_three_site_coverage_2026_08_15.py
---

# Three-Site Fill Coverage Ranking Inside The Three-Cut Class `F_cut`

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact occupancy-to-lock coverage ranking of the 32 cube-covariant
complement-even predicates that vanish on empty and full, on the
twelve-vertex two-cube, over all 220 unordered 3-site seeds, with
off-patch occupancy `0`. The unbalanced-axis map `f_L1` is displayed as
one scored member. It is not adopted as the physical Admissibility rule.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_three_site_coverage_2026_08_15.py`](../scripts/f_cut_three_site_coverage_2026_08_15.py)
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

That static cardinality is leftover-character inventory of the three-cut
class. The two-site coverage ranking of the same 32 maps is a different
leftover inventory: it used a different seed cardinality `|S|`. The
two-map leftover that compared two named 10-orbit maps on all 3-site
seeds is a different leftover inventory. This note asks the new ranking
object: among all 32 maps, how many of the 220 three-site seeds does
each fill, and is `f_L1` the unique maximizer.

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
`|c|_1 mod 2`.

The five remaining bits of an `F_cut` map, in the displayed order
`(wt1, opp2, adj2, vertex3, mixed3)`, are the values on the three
complement-pairs and two complement-fixed orbits after empty and full are
forced to `0`.

**Theorem 1.** `f_L1 ∈ F_cut` and

```text
cov2(f_L1) = 62.
```

Its remaining-bit tuple is `(1, 0, 1, 1, 1)`. The two maps that attain
two-site coverage `66` have remaining-bit tuples

```text
(1, 1, 1, 1, 0), (1, 1, 1, 1, 1).
```

**Theorem 2.** Exhaustive enumeration of the 32 maps gives

```text
m3 = 220
N_max3 = 2
cov3(f_L1) = 220.
```

So `f_L1` attains the 3-site maximum. The two maximizers are exactly the
remaining-bit tuples `(1, 0, 1, 1, 1)` and `(1, 1, 1, 1, 1)`.

**Theorem 3.** So `N_max3 > 1`: `f_L1` is a maximizer but not the unique
maximizer. A displayed other maximizer has remaining-bit tuple
`(1, 1, 1, 1, 1)` and `cov3=220`. Displayed, not adopted.

Do not write the ranking into Admissibility.

Not leftover-character of #6429 (that was the 2-site ranking; different |S|).
Not leftover-character of #6427 (that was an |S|=3 census of two named
10-orbit maps).

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The ten-orbit reconstruction, the 32-element F_cut, membership of f_L1, the exact integer cov2(f_L1)=62, the two cov2=66 remaining-bit tuples, and the 3-site coverage-ranking pair (m3,N_max3)=(220,2) with cov3(f_L1)=220 are enumerated. Uniqueness of f_L1 as an F_cut 3-site coverage maximizer is false on this patch. No physical law is selected."
trace_class: upstream_support
target_claim_id: f_cut_three_site_coverage
target_blocker_text: "whether f_L1 uniquely maximizes 3-site fill coverage among the 32 F_cut maps"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the F_cut 3-site coverage ranking; any physical use must separately derive an Admissibility selector"
conditional_surface_status: "exact for F_cut on this twelve-vertex patch with off-patch o=0 and all 220 three-site seeds; no Z^3-wide law and no physical selector"
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
- the complete set of 66 unordered 2-site seeds (Theorem 1 reconfirm);
- the complete set of 220 unordered 3-site seeds.

No observational comparator, literature constant, Wilson weight, rate, or
generator is imported. No Record scalar functional appears.

## Exact Target And Objects

**Target.** Rank the 32 members of `F_cut` by three-site fill coverage on
the two-cube, reconfirm `cov2(f_L1)=62` and the two `cov2=66` maps, and
decide uniqueness of `f_L1` as a 3-site maximizer.

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
`(wt1, opp2, adj2, vertex3, mixed3)`.

Define

```text
f_L1(c)     = 1  iff  u(c) ≥ 1,
```

so `f_L1` has remaining-bit tuple `(1, 0, 1, 1, 1)`. The displayed other
maximizer has remaining-bit tuple `(1, 1, 1, 1, 1)`: it equals `f_L1`
except that `opp2` is on. Neither map is adopted.

A locked set `S` determines occupancies: a lattice neighbor in `S` has
occupancy `1`, and every other neighbor — including every off-patch
neighbor — has occupancy `0`. One synchronous tick replaces `S` by

```text
S ∪ { v in two-cube \ S : f(neighborhood_6(v; S)) = 1 }.
```

Then `cov2(f)` is the number of 2-site seeds whose halt set has cardinality
12, `cov3(f)` is the same count on 3-site seeds, `m3` is the maximum of
`cov3` over `F_cut`, and `N_max3` is the number of maps attaining `m3`.

## Theorems

**Theorem 1.** There are exactly 24 proper cube rotations and exactly 10
orbits on `{0,1}^6`. The three cuts leave `|F_cut|=32`. The unbalanced-axis
map `f_L1` is one element of `F_cut`. It is not Hamming parity. On the
twelve-vertex two-cube with off-patch occupancy `0`, exhaustive run of all
66 two-site seeds gives

```text
cov2(f_L1) = 62.
```

Its remaining-bit tuple is `(1, 0, 1, 1, 1)`. The two maps that attain
two-site coverage `66` are the remaining-bit tuples `(1, 1, 1, 1, 0)` and
`(1, 1, 1, 1, 1)`.

**Theorem 2.** Exhaustive ranking of the 32 maps on all 220 three-site
seeds gives

```text
m3 = 220
N_max3 = 2
cov3(f_L1) = 220.
```

The two remaining-bit tuples that attain `m3` are

```text
(1, 0, 1, 1, 1), (1, 1, 1, 1, 1).
```

Equivalently, a map in `F_cut` fills every 3-site seed if and only if it
is one of those two tuples. The two-site maximizer `(1, 1, 1, 1, 0)` does
not attain `m3`.

**Theorem 3.** So `N_max3 > 1`. The map `f_L1` fills all 220 of the 220
three-site seeds, so it is a maximizer, but it is not unique as a
maximizer. The displayed other maximizer is the remaining-bit tuple
`(1, 1, 1, 1, 1)`. It is distinct from `f_L1` (they disagree on `opp2`)
and has `cov3=220`. Displayed, not adopted.

## Proof-Obligation Graph

| obligation | exact disposition |
|---|---|
| 24 proper cube rotations | signed permutations of the three axes with determinant `+1` |
| 10 orbits on `{0,1}^6` | axis-type classes `(u,b,e)` partition the 64 cells with the listed sizes |
| `|F_cut|=32` | three complement-pairs and two complement-fixed orbits remain free after the vanish cuts |
| `f_L1` is in `F_cut` | `u` is rotation- and complement-invariant and `u(empty)=u(full)=0` |
| `f_L1` is not Hamming | the two-unbalanced-axis orbit has even weight and `f_L1=1` |
| `cov2(f_L1)=62` | exhaustive 66-seed fill census of `f_L1` |
| two `cov2=66` maps | remaining-bit tuples `(1, 1, 1, 1, 0)` and `(1, 1, 1, 1, 1)` |
| two-cube has twelve vertices | `{0,1,2}×{0,1}×{0,1}` |
| 220 three-site seeds | `C(12,3)` unordered triples |
| off-patch occupancy `0` | declared stencil default; not a blank-block |
| `m3`, `N_max3`, `cov3(f_L1)` | exhaustive 32-map ranking of `cov3` |
| uniqueness of `f_L1` as maximizer | false; remaining-bit tuple `(1, 1, 1, 1, 1)` is an explicit second maximizer with `cov3=220` |

## Counterfactual And Mutation Table

1. Replace `f_L1` by Hamming parity `|c|_1 mod 2`: the maps disagree on the
   two-unbalanced-axis orbit, and Hamming is a different `F_cut` member.
2. Change the off-patch default away from `0`: the occupancy stencil
   changes and the coverage ranking is a different object.
3. Drop any of the three cuts: the class is no longer the 32-element
   `F_cut`.
4. Score only 2-site seeds: that leftover is #6429, a different `|S|`.
5. Score only two named 10-orbit maps on 3-site seeds: that leftover is
   #6427, not the 32-map ranking.
6. Assert that `f_L1` uniquely maximizes `cov3`: the explicit remaining-bit
   tuple `(1, 1, 1, 1, 1)` with `cov3=220` refutes uniqueness.

## What This Does Not Claim

- No physical Admissibility selector and no adopted occupancy law.
- No Qubit rewrite and no `M_2(C)`-valued conditional probability.
- No `Z^3`-wide formation, rate, or generator.
- No identification of `f_L1` with Hamming parity.
- No leftover-character restatement of the 2-site `F_cut` ranking
  (different `|S|`), and no leftover-character restatement of a two-map
  3-site census, in place of this 32-map 3-site coverage ranking.
- No list of the 220 three-site seeds.
- No blank-block or 4-site variant.

## No-Go Discipline Gate

The only negative claim is uniqueness of the maximizer: `f_L1` is not the
unique `F_cut` maximizer of three-site coverage on this patch. The positive
triple `(m3, N_max3, cov3(f_L1))=(220, 2, 220)` is an exact enumeration,
not a wall.

### N1 — materially distinct routes

| Route | Exact attack | Result and authority | Marker |
|---|---|---|---|
| orbit reconstruction | Recompute the 24 rotations and the 10 axis-type orbits. | Theorem 1 and checks `thm1-twenty-four-rotations` / `thm1-ten-orbits`. | **ATTEMPTED** |
| three-cut class | Force vanish-on-empty, vanish-on-full, and `f(c)=f(1-c)`. | Theorem 1 and check `thm1-f-cut-cardinality` give `|F_cut|=32`. | **ATTEMPTED** |
| Hamming-as-`f_L1` | Test whether `|c|_1 mod 2` equals the unbalanced-axis predicate. | Theorem 1 and check `thm1-f-L1-not-hamming` separate the maps. | **ATTEMPTED** |
| `cov2` reconfirm | Run every `F_cut` map on all 66 two-site seeds. | Theorem 1 and checks `thm1-cov2-L1-sixty-two` / `thm1-cov2-max-pair` give `cov2(f_L1)=62` and the two `cov2=66` tuples. | **ATTEMPTED** |
| `F_cut` 3-site coverage ranking | Score every map in `F_cut` by `cov3`. | Theorem 2 and checks `thm2-m3-and-n-max3` / `thm2-cov3-L1` give `m3 = 220`, `N_max3 = 2`, and `cov3(f_L1) = 220`. | **ATTEMPTED** |
| uniqueness of `f_L1` as maximizer | Ask whether the maximizer class is the singleton `{f_L1}`. | Theorem 3 and checks `thm3-not-unique-maximizer` / `thm3-displayed-other-maximizer`. | **ATTEMPTED** |

### N2 — wall independence and collapse

There is one negative conclusion: uniqueness of the maximizer fails. The
explicit second maximizer and the cardinality `N_max3=2` are two
certificates of the same non-uniqueness, so they collapse rather than
count as two walls.

| Pair | First closes second? | Second closes first? | Disposition |
|---|---:|---:|---|
| `N_max3=2` / displayed `(1, 1, 1, 1, 1)` | yes: a count larger than one is non-uniqueness | yes: one extra maximizer is non-uniqueness | collapse into the uniqueness failure |
| `cov3(f_L1)=220` / `m3=220` | no: a score does not name the multiplicity | no: the max does not name uniqueness | independent positive integers versus uniqueness |
| static `|F_cut|=32` / ranking pair `(m3, N_max3)` | no: membership is not dynamics | no: a ranking does not replace the three-cut class | separate exact counts |
| leftover of #6429 / this ranking | no: that leftover scored `|S|=2` | no: a 3-site ranking does not replace the 2-site ranking | different object |
| leftover of #6427 / this ranking | no: that leftover scored two named maps | no: a 32-map ranking does not replace a two-map census | different object |

Physical law selection is not a wall: this note makes no negative theorem
about the existence of a selector and simply does not claim one.

### N3 — hidden-condition scan

| Phrase or premise | Classification |
|---|---|
| “work on the twelve-vertex two-cube” | explicit patch hypothesis; not a `Z^3` theorem |
| off-patch occupancy `0` | explicit default; blank-block is a different rule |
| `F_cut` | explicit three-cut class; the other 992 covariant maps are excluded |
| all 220 three-site seeds | explicit seed class; a 2-site ranking is a different residual |
| “lock” | Record permanence on this Boolean occupancy model, not a possibility-valued law |
| “cube-covariant” | invariance under the 24 proper rotations, cited to Lattice/Admissibility |
| Hamming parity | displayed mutation only |
| remaining-bit tuple `(1, 1, 1, 1, 1)` | displayed witness against uniqueness, not a selected law |

### N4 — citation-to-residual matching

| Evidence path:line | Residual attacked | Residual claimed closed | Match? |
|---|---|---|---:|
| `docs/MINIMAL_AXIOMS_2026-06-29.md:37` | ambient lattice and cubic rotations | sites are `Z^3` with proper cubic rotations | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:57` | covariant nearest-neighbor rule | covariance is the class filter, not a selector | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:79` | lock permanence | a locked site stays locked | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:83` | unreadability of absence | unlocked and off-patch sites contribute occupancy `0`, not a readout | yes |
| `scripts/f_cut_three_site_coverage_2026_08_15.py:77` | 24 proper rotations | signed permutations with determinant `+1` | yes |
| `scripts/f_cut_three_site_coverage_2026_08_15.py:121` | `f_L1` definition | unbalanced-axis predicate, not Hamming | yes |
| `scripts/f_cut_three_site_coverage_2026_08_15.py:126` | Hamming mutation | `|c|_1 mod 2` is a different `F_cut` map | yes |
| `scripts/f_cut_three_site_coverage_2026_08_15.py:52` | 220 three-site seeds | `C(12,3)` unordered triples on the two-cube | yes |
| `scripts/f_cut_three_site_coverage_2026_08_15.py:198` | `cov3(f)` | number of 3-site seeds a map fills | yes |
| `scripts/f_cut_three_site_coverage_2026_08_15.py:301` | ranking | exact `(m3, N_max3)` on `F_cut` | yes |
| `scripts/f_cut_three_site_coverage_2026_08_15.py:65` | uniqueness | displayed maximizer, remaining bits `(1, 1, 1, 1, 1)` | yes |

No evidence citation is used to claim that a physical occupancy law, a
formation rate, or a `Z^3`-wide selector has been closed.

### N5 — rhetoric and resolution audit

| Resolution | Executed? | Narrow negative supported? |
|---|---:|---|
| per element | yes: all 64 neighbor 6-tuples | each is assigned its axis-type orbit; no broader cell class is classified |
| per site | yes: the twelve two-cube vertices | each uses the same six-direction stencil with off-patch occupancy `0` |
| per mode | yes: every map in `F_cut` | the ranking is this class on all 220 seeds; other classes are unclaimed |
| per block | yes: the pair `(m3, N_max3)` | uniqueness fails because `N_max3=2` even though `f_L1` attains `m3` |
| lattice wide | no | no `Z^3`-wide formation or Admissibility selector is asserted |

The runner prints the same five resolution statements.

### N6 — partial closure and primitive scan

The primitive registry at `docs/audit/data/axiom_premise_nodes.json` was
checked. The only dependency used is the registered `minimal_axioms` node.
Approved primitives are `scale_reference_primitive`,
`kinetic_isotropy_primitive`, and `realized_state_primitive`. None of them
supplies a Boolean occupancy map, a seed-coverage ranking, or an
Admissibility selector, and none is reclassified as an import or wall.

One partial-closure mechanism is displayed rather than suppressed: `f_L1`
does lie in `F_cut` and does fill all 220 of the 220 three-site seeds.
That positive member does not make `f_L1` the unique maximizer and does
not select it as the physical rule. The remaining physical choice — which,
if any, `F_cut` map is the Admissibility occupancy predicate — stays
explicit.

The open derivation-obligation registry
(`docs/audit/data/derivation_obligations.json`) names no occupancy-to-lock
coverage target; those open gates are unused here.

### N7 — hostile steelman

The strongest objection is that `f_L1` already fills every 3-site seed, so
three-site coverage might be called a leftover decoration of the already
known 1-site and 2-site fill tables, or of the two-map 3-site census
that first split `mix0` from `f_L1`. That objection is correctly about the
existence of some 3-site split between two named maps. It does not
overturn the stated theorem: among all maps in `F_cut`, three-site
coverage selects a two-element class that contains `f_L1` and also
contains the remaining-bit tuple `(1, 1, 1, 1, 1)`. The displayed
maximizer differs from `f_L1` on `opp2`, and that is a ranking failure
for uniqueness of `f_L1`, not a leftover of a two-map comparison or of
the 2-site ranking (different `|S|`).

### N8 — cross-cycle echo

Repository search found nearby occupancy and covariance surfaces. They are
context, not load-bearing dependencies. The 24 rotations, 10 orbits,
`F_cut`, and 32-map 220-seed ranking are recomputed here.

| Earlier surface | Similar issue | Mechanism considered here |
|---|---|---|
| `docs/ADMISSIBILITY_COVARIANT_Q8_CONDITIONAL_LAW_PAIR_BOUNDED_THEOREM_NOTE_2026-08-13.md` | proper-cubic covariance of a local rule | covariance is used only as the orbit filter for Boolean maps |
| `docs/PHYSICAL_SPATIAL_BLOCK_SEAM_DICHOTOMY_CYCLE728_NOTE_2026-08-04.md` | two-cell box `{0,1,2}×{0,1}×{0,1}` | the same twelve spatial vertices are the patch; the seam cost is unused |
| `docs/MINIMAL_AXIOMS_2026-06-29.md` | one covariant nearest-neighbor rule | the axiom names the contract; this note does not select the rule |

No earlier mechanism retires the `F_cut` 3-site coverage ranking or
restores uniqueness of `f_L1` as a maximizer inside the 32-map class.

No-Go Discipline disposition: **PASS** for the uniqueness failure and the
exact triple `(m3, N_max3, cov3(f_L1))` stated above.

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
`F_cut`, evaluates all 32 maps on the two-cube from every 2-site seed and
every 3-site seed, reports `cov2(f_L1) = 62` and the two `cov2=66`
remaining-bit tuples, reports `m3 = 220`, `N_max3 = 2`, and
`cov3(f_L1) = 220`, checks that `f_L1` is not Hamming parity, and exhibits
the displayed other maximizer by remaining-bit tuple `(1, 1, 1, 1, 1)`
with `cov3=220`. Declared audit inputs are this note and the axiom memo.
No runner cache is written.
