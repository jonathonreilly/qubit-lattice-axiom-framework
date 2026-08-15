---
claim_id: f_cut_five_site_maximizers_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Among the 32 F_cut maps on the two-cube with off-patch o=0, the two maps that attain maximum 5-site coverage are named by remaining-bit tuple. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_five_site_maximizers_2026_08_15.py
---

# Two `F_cut` 5-Site Coverage Maximizers Named By Remaining-Bit Tuple

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact naming of the two cube-covariant complement-even predicates
that attain maximum 5-site fill coverage on the twelve-vertex two-cube with
off-patch occupancy `0`. Each maximizer is identified once by its
`(wt1, opp2, adj2, vertex3, mixed3)` remaining-bit tuple. The two-map
set is displayed. Neither map is adopted as the physical Admissibility
rule. Do not list the 792 seeds.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_five_site_maximizers_2026_08_15.py`](../scripts/f_cut_five_site_maximizers_2026_08_15.py)
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

On the two-cube `{0,1,2}×{0,1}×{0,1}`, each unordered 5-set of vertices is
a 5-site seed. There are `C(12,5)=792` such seeds. Do not list the 792
seeds. Off-patch neighbors have occupancy `0`. Each tick, every unlocked
on-patch vertex evaluates `f` on its six-neighbor occupancy tuple and
locks if `f=1`. The process is synchronous and stops at a fixed point in
at most 12 ticks. Fill means `|locks_halt|=12`. Coverage is

```text
cov5(f) = |{ S : |S|=5 and f fills from S }|.
```

Investment #6465 ranked that coverage: it proved `m_5=792` and
`N_max_5=2`. That leftover only reported `m_5` and `N_max_5`. Not leftover-character of #6465
(that only reported m_5 and N_max_5). The new object here is the two-map
set: the two remaining-bit tuples that attain the maximum. Same move as
coverival #6430 after `N_max_2=2`.

`f_L1(c)=1` if and only if some axis is unbalanced: `c_{+μ} ≠ c_{-μ}` for
at least one `μ ∈ {x,y,z}`. Equivalently, some discrete neighbor contrast
`n_μ = c_{+μ} − c_{-μ}` is nonzero. This is **not** Hamming parity
`|c|_1 mod 2`.

The five remaining bits of an `F_cut` map, in the displayed order
`(wt1, opp2, adj2, vertex3, mixed3)`, are the values on the three
complement-pairs and two complement-fixed orbits after empty and full are
forced to `0`. Write `f1` for the remaining-bit tuple `(1, 1, 1, 1, 1)`.
The remaining-bit tuple of `f_L1` is `(1, 0, 1, 1, 1)`.

**Theorem 1.** Exhaustive recomputation of `cov5` on all 32 maps and all
792 five-site seeds reconfirms

```text
m_5 = 792
N_max_5 = 2
```

The two maximizer remaining-bit tuples are

```text
(1, 0, 1, 1, 1)
(1, 1, 1, 1, 1)
```

Equivalently, a map in `F_cut` fills every 5-site seed if and only if
`wt1=adj2=vertex3=mixed3=1`, with `opp2` free.

**Theorem 2.** Both named maps sit in that two-map set: f_L1 is among them
and f1 is among them. Their 5-site scores are

```text
cov5(f_L1) = 792
cov5(f1) = 792.
```

**Theorem 3.** Display both. Do not adopt a tuple. Do not write them into Admissibility.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The ten-orbit reconstruction, the 32-element F_cut, the ranking pair (m_5,N_max_5)=(792,2), and the two remaining-bit tuples that attain m_5 are enumerated. Both f1 and f_L1 are among them. The two-map set is displayed, not written into Admissibility."
trace_class: upstream_support
target_claim_id: f_cut_five_site_maximizers
target_blocker_text: "who ties at k=5; the two F_cut 5-site coverage maximizers remain unnamed as remaining-bit tuples"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the named two-map set; any physical use must separately derive an Admissibility selector"
conditional_surface_status: "exact for the two F_cut maximizers on this twelve-vertex patch with off-patch o=0 and all 792 five-site seeds; no Z^3-wide law and no physical selector"
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
- the complete set of 792 unordered 5-site seeds, not listed.

No observational comparator, literature constant, Wilson weight, rate, or
generator is imported. No Record scalar functional appears.

Not leftover-character of #6465 (that only reported m_5 and N_max_5). The
ranking pair is recomputed only so the two attaining maps can be named.

## Exact Target And Objects

**Target.** Reconfirm the 5-site coverage ranking pair on `F_cut`, then
name the two maps that attain the maximum by remaining-bit tuple, and
state whether `f1` or `f_L1` is among them.

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
f1(c)       = 1  iff  c is neither empty nor full,
```

so `f_L1` has remaining-bit tuple `(1, 0, 1, 1, 1)` and `f1` has
remaining-bit tuple `(1, 1, 1, 1, 1)`. Neither map is adopted.

A locked set `S` determines occupancies: a lattice neighbor in `S` has
occupancy `1`, and every other neighbor — including every off-patch
neighbor — has occupancy `0`. One synchronous tick replaces `S` by

```text
S ∪ { v in two-cube \ S : f(neighborhood_6(v; S)) = 1 }.
```

Then `cov5(f)` is the number of 5-site seeds whose halt set has cardinality
12, `m_5` is the maximum of `cov5` over `F_cut`, and `N_max_5` is the
number of maps attaining `m_5`. The two-map set is the pair of
remaining-bit tuples with `cov5=m_5`.

## Theorems

**Theorem 1.** There are exactly 24 proper cube rotations and exactly 10
orbits on `{0,1}^6`. The three cuts leave `|F_cut|=32`. The unbalanced-axis
map `f_L1` is one element of `F_cut`. It is not Hamming parity. On the
twelve-vertex two-cube with off-patch occupancy `0`, exhaustive ranking of
all 32 maps on all 792 five-site seeds reconfirms

```text
m_5 = 792
N_max_5 = 2
```

The two remaining-bit tuples that attain `m_5` are

```text
(1, 0, 1, 1, 1)
(1, 1, 1, 1, 1)
```

Equivalently, a map in `F_cut` fills every 5-site seed if and only if
`wt1=adj2=vertex3=mixed3=1`. The bit `opp2` remains free.

**Theorem 2.** Both `f1` and `f_L1` are among the two maximizers:
`f_L1` is among them with remaining-bit tuple `(1, 0, 1, 1, 1)`, and
`f1` is among them with remaining-bit tuple `(1, 1, 1, 1, 1)`. Each
attains `cov5=792`.

**Theorem 3.** Display both. Do not adopt a tuple. Do not write them into Admissibility. The two-map set is a displayed rival pair, not a selected
occupancy law.

## Proof-Obligation Graph

| obligation | exact disposition |
|---|---|
| 24 proper cube rotations | signed permutations of the three axes with determinant `+1` |
| 10 orbits on `{0,1}^6` | axis-type classes `(u,b,e)` partition the 64 cells with the listed sizes |
| `|F_cut|=32` | three complement-pairs and two complement-fixed orbits remain free after the vanish cuts |
| `f_L1` is in `F_cut` | `u` is rotation- and complement-invariant and `u(empty)=u(full)=0` |
| `f_L1` is not Hamming | the two-unbalanced-axis orbit has even weight and `f_L1=1` |
| two-cube has twelve vertices | `{0,1,2}×{0,1}×{0,1}` |
| 792 five-site seeds | `C(12,5)` unordered 5-sets; not listed |
| off-patch occupancy `0` | declared stencil default; not a blank-block |
| `m_5` and `N_max_5` | exhaustive 32-map ranking of `cov5`; recomputed, then used only to name the attaining pair |
| two-map set | remaining-bit tuples `(1, 0, 1, 1, 1)` and `(1, 1, 1, 1, 1)` |
| `f1` and `f_L1` among them | both named tuples attain `m_5` |

## Counterfactual And Mutation Table

1. Replace `f_L1` by Hamming parity: Hamming is a different `F_cut` map
   (it disagrees on the two-unbalanced-axis orbit) and is not this
   coverage maximizer pair.
2. Replace off-patch occupancy `0` by a blank-block: first-wave candidates
   become undefined; that is a different census.
3. Drop complement-even or the vanish-on-full cut: the class is no longer
   the 32-element `F_cut`.
4. Report only `m_5` and `N_max_5`: that leftover is #6465, not the named
   two-map set.
5. List the 792 seeds: that seed table is a different residual; this note
   names maps, not seeds.
6. Adopt either remaining-bit tuple as the physical rule: the note
   displays both and writes neither into Admissibility.

## What This Does Not Claim

- No physical Admissibility selector and no adopted occupancy law.
- No Qubit rewrite and no `M_2(C)`-valued conditional probability.
- No `Z^3`-wide formation, rate, or generator.
- No identification of `f_L1` with Hamming parity.
- No leftover-character restatement of the #6465 ranking pair
  `(m_5, N_max_5)` in place of the named two-map set.
- No listed 792-seed table and no 2-site or 4-site variant.

## No-Go Discipline Gate

The only negative claim is that the 5-site coverage maximizer inside
`F_cut` is not a singleton. The named two-map set is an exact
enumeration, not a wall. Both `f1` and `f_L1` sit in that set.

### N1 — materially distinct routes

| Route | Exact attack | Result and authority | Marker |
|---|---|---|---|
| orbit reconstruction | Recompute the 24 rotations and the 10 axis-type orbits. | Theorem 1 and checks `thm1-twenty-four-rotations` / `thm1-ten-orbits`. | **ATTEMPTED** |
| three-cut class | Force vanish-on-empty, vanish-on-full, and `f(c)=f(1-c)`. | Theorem 1 and check `thm1-f-cut-cardinality` give `|F_cut|=32`. | **ATTEMPTED** |
| Hamming-as-`f_L1` | Test whether `|c|_1 mod 2` equals the unbalanced-axis predicate. | Theorem 1 and check `thm1-f-L1-not-hamming` separate the maps. | **ATTEMPTED** |
| ranking reconfirm | Score every map in `F_cut` by `cov5`. | Theorem 1 and check `thm1-reconfirm-ranking` give `m_5 = 792`, `N_max_5 = 2`. | **ATTEMPTED** |
| name both maximizers | List remaining-bit tuples with `cov5=m_5`. | Theorem 1 and check `thm1-named-two-map-set`. | **ATTEMPTED** |
| display, do not adopt | Ask whether `f1` or `f_L1` is among them, then whether either tuple is written into Admissibility. | Theorem 2, Theorem 3, and checks `thm2-f1-and-f-L1-among-them` / `thm3-display-both-not-adopted`. | **ATTEMPTED** |

### N2 — wall independence and collapse

There is one negative conclusion: the maximizer class is not a singleton.
Naming both remaining-bit tuples and the cardinality `N_max_5=2` are two
certificates of the same two-map set, so they collapse rather than count
as two walls.

| Pair | First closes second? | Second closes first? | Disposition |
|---|---:|---:|---|
| `N_max_5=2` / named pair | yes: a count of two is the pair's size | yes: two named tuples give the count | collapse into the two-map set |
| `cov5(f_L1)=792` / `m_5=792` | no: a score does not name the partner | no: the max does not name `f_L1` | independent positive integers until Theorem 2 names membership |
| static `|F_cut|=32` / two-map set | no: membership is not dynamics | no: naming maximizers does not replace the three-cut class | separate exact counts |
| leftover of #6465 / this two-map set | no: that leftover reported only `m_5` and `N_max_5` | no: naming the pair does not replace the ranking residual | different object |

Physical law selection is not a wall: this note makes no negative theorem
about the existence of a selector and simply does not claim one.

### N3 — hidden-condition scan

| Phrase or premise | Classification |
|---|---|
| “work on the twelve-vertex two-cube” | explicit patch hypothesis; not a `Z^3` theorem |
| off-patch occupancy `0` | explicit default; blank-block is a different rule |
| `F_cut` | explicit three-cut class; the other 992 covariant maps are excluded |
| all 792 five-site seeds | explicit seed class; seeds are not listed |
| “lock” | Record permanence on this Boolean occupancy model, not a possibility-valued law |
| “cube-covariant” | invariance under the 24 proper rotations, cited to Lattice/Admissibility |
| Hamming parity | displayed mutation only |
| remaining-bit tuples `(1, 0, 1, 1, 1)` and `(1, 1, 1, 1, 1)` | displayed two-map set, not a selected law |

### N4 — citation-to-residual matching

| Evidence path:line | Residual attacked | Residual claimed closed | Match? |
|---|---|---|---:|
| `docs/MINIMAL_AXIOMS_2026-06-29.md:37` | ambient lattice and cubic rotations | sites are `Z^3` with proper cubic rotations | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:57` | covariant nearest-neighbor rule | covariance is the class filter, not a selector | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:79` | lock permanence | a locked site stays locked | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:83` | unreadability of absence | unlocked and off-patch sites contribute occupancy `0`, not a readout | yes |
| `scripts/f_cut_five_site_maximizers_2026_08_15.py:79` | 24 proper rotations | signed permutations with determinant `+1` | yes |
| `scripts/f_cut_five_site_maximizers_2026_08_15.py:123` | `f_L1` definition | unbalanced-axis predicate, not Hamming | yes |
| `scripts/f_cut_five_site_maximizers_2026_08_15.py:128` | Hamming mutation | `|c|_1 mod 2` is a different `F_cut` map | yes |
| `scripts/f_cut_five_site_maximizers_2026_08_15.py:51` | 792 five-site seeds | `C(12,5)` unordered 5-sets on the two-cube | yes |
| `scripts/f_cut_five_site_maximizers_2026_08_15.py:362` | `cov5(f)` | number of 5-site seeds a map fills | yes |
| `scripts/f_cut_five_site_maximizers_2026_08_15.py:370` | ranking | exact `(m_5, N_max_5)` used to name the attaining pair | yes |
| `scripts/f_cut_five_site_maximizers_2026_08_15.py:142` | two-map set | displayed maximizer `f1=(1, 1, 1, 1, 1)` and partner `f_L1=(1, 0, 1, 1, 1)` | yes |

No evidence citation is used to claim that a physical occupancy law, a
formation rate, or a `Z^3`-wide selector has been closed.

### N5 — rhetoric and resolution audit

| Resolution | Executed? | Narrow negative supported? |
|---|---:|---|
| per element | yes: all 64 neighbor 6-tuples | each is assigned its axis-type orbit; no broader cell class is classified |
| per site | yes: the twelve two-cube vertices | each uses the same six-direction stencil with off-patch occupancy `0` |
| per mode | yes: every map in `F_cut` | the two maximizers are named inside this class on all 792 seeds |
| per block | yes: the two-map set | both remaining-bit tuples attain `m_5`; `f1` and `f_L1` are among them |
| lattice wide | no | no `Z^3`-wide formation or Admissibility selector is asserted |

The runner prints the same five resolution statements.

### N6 — partial closure and primitive scan

The primitive registry at `docs/audit/data/axiom_premise_nodes.json` was
checked. The only dependency used is the registered `minimal_axioms` node.
No approved primitive supplies the Boolean occupancy maps, and none is
reclassified as an import or wall.

One partial-closure mechanism is displayed rather than suppressed: `f_L1`
and `f1` both lie in `F_cut` and both fill all 792 five-site seeds. That
positive pair does not select either named tuple as the physical rule.
The remaining physical choice — which, if any, `F_cut` map is the
Admissibility occupancy predicate — stays explicit.

### N7 — hostile steelman

The strongest objection is that the two maximizers are the already-named
maps `f_L1` and `f1`, so naming them might be called leftover-character of
#6465 that already reported `m_5=792` and `N_max_5=2`. That objection is
correctly about the ranking pair. It does not overturn the stated theorem:
the #6465 residual stopped at the pair of integers; the two-map set
residual is the pair of remaining-bit tuples. Displaying both tuples names
that set. Neither tuple is adopted.

### N8 — cross-cycle echo

Repository search found nearby occupancy and covariance surfaces. They are
context, not load-bearing dependencies. The 24 rotations, 10 orbits,
`F_cut`, the 32-map 792-seed ranking, and the two remaining-bit tuples are
recomputed here.

| Earlier surface | Similar issue | Mechanism considered here |
|---|---|---|
| `docs/ADMISSIBILITY_COVARIANT_Q8_CONDITIONAL_LAW_PAIR_BOUNDED_THEOREM_NOTE_2026-08-13.md` | proper-cubic covariance of a local rule | covariance is used only as the orbit filter for Boolean maps |
| `docs/PHYSICAL_SPATIAL_BLOCK_SEAM_DICHOTOMY_CYCLE728_NOTE_2026-08-04.md` | two-cell box `{0,1,2}×{0,1}×{0,1}` | the same twelve spatial vertices are the patch; the seam cost is unused |
| `docs/MINIMAL_AXIOMS_2026-06-29.md` | one covariant nearest-neighbor rule | the axiom names the contract; this note does not select the rule |

No earlier mechanism retires the named two-map set or writes either
remaining-bit tuple into Admissibility.

No-Go Discipline disposition: **PASS** for the named two-map set and the
reconfirmed ranking pair `(m_5, N_max_5)` stated above.

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
`F_cut`, evaluates all 32 maps on the two-cube from every 5-site seed,
reconfirms `m_5 = 792` and `N_max_5 = 2`, names both maximizers by
remaining-bit tuple `(1, 0, 1, 1, 1)` and `(1, 1, 1, 1, 1)`, checks that
`f_L1` is among them and `f1` is among them, checks that `f_L1` is not
Hamming parity, and does not adopt either map. Declared audit inputs are
this note and the axiom memo. No runner cache is written.
