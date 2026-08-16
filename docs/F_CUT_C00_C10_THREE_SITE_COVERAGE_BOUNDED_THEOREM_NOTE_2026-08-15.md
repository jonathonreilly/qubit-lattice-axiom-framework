---
claim_id: f_cut_c00_c10_three_site_coverage_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On the two-cube with off-patch o=0, the 3-site coverage of F_cut (1,0,0,0,0) and (1,1,0,0,0) is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_c00_c10_three_site_coverage_2026_08_15.py
---

# Three-Site Coverage Of The Two `#6490` `F_cut` Exceptions

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact occupancy-to-lock 3-site coverage of the two cube-covariant
complement-even maps in `F_cut` with remaining-bit tuples
`(1, 0, 0, 0, 0)` and `(1, 1, 0, 0, 0)`, on the twelve-vertex two-cube,
over all 220 unordered 3-site seeds, with off-patch occupancy `0`. Those
two maps are the `#6490` exceptions (`wt1=1` and `cov2=0`). The pair of
coverages is displayed. Neither map is adopted as the physical
Admissibility rule.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_c00_c10_three_site_coverage_2026_08_15.py`](../scripts/f_cut_c00_c10_three_site_coverage_2026_08_15.py)
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
forced to `0`. Write `f00` for remaining bits `(1, 0, 0, 0, 0)` and `f10`
for remaining bits `(1, 1, 0, 0, 0)`. Both have `wt1=1`. Both have
`cov2=0`. They are the two `#6490` exceptions to the failed equivalence
`cov2>0` iff `wt1=1`.

Not leftover-character of #6490: that scored only cov2. The present object
is three-site coverage of the same two maps. New |S|.

On the two-cube `{0,1,2}×{0,1}×{0,1}`, each unordered triple of vertices is
a 3-site seed. There are `C(12,3)=220` such seeds. Off-patch neighbors
have occupancy `0`. Each tick, every unlocked on-patch vertex evaluates
`f` on its six-neighbor occupancy tuple and locks if `f=1`. The process
is synchronous and stops at a fixed point in at most 12 ticks. Fill means
`|locks_halt|=12`. Coverage is

```text
cov3(f) = |{ S : |S|=3 and f fills from S }|.
```

The comparison ceiling `m3=220` is that seed count: a map attains `m3`
exactly when it fills every 3-site seed. Do not list the seeds.

`f_L1(c)=1` if and only if some axis is unbalanced: `c_{+μ} ≠ c_{-μ}` for
at least one `μ ∈ {x,y,z}`. Equivalently, some discrete neighbor contrast
`n_μ = c_{+μ} − c_{-μ}` is nonzero. This is **not** Hamming parity
`|c|_1 mod 2`. The remaining-bit tuple of `f_L1` is `(1, 0, 1, 1, 1)`.
That map is a control, not a scored exception.

**Theorem 1.** Exhaustive evaluation of the two exception maps on all 220
three-site seeds gives

```text
cov3(f00) = 0
cov3(f10) = 4.
```

**Theorem 2.** Neither attains m3=220.

**Theorem 3.** The pair `(cov3(f00), cov3(f10)) = (0, 4)` is displayed.
Neither `f00` nor `f10` is adopted as the physical Admissibility rule.

Do not write the ranking into Admissibility.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The ten-orbit reconstruction, the 32-element F_cut, membership of f00=(1,0,0,0,0) and f10=(1,1,0,0,0), and the exact pair cov3(f00)=0, cov3(f10)=4 against m3=220 are enumerated. Neither exception fills every 3-site seed. No physical law is selected."
trace_class: upstream_support
target_claim_id: f_cut_c00_c10_three_site_coverage
target_blocker_text: "do the cov2=0 wt1=1 maps fill any 3-site seed"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the two-exception 3-site coverage pair; any physical use must separately derive an Admissibility selector"
conditional_surface_status: "exact for f00 and f10 on this twelve-vertex patch with off-patch o=0 and all 220 three-site seeds; no Z^3-wide law and no physical selector"
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
- the two remaining-bit tuples `(1, 0, 0, 0, 0)` and `(1, 1, 0, 0, 0)`.

No observational comparator, literature constant, Wilson weight, rate, or
generator is imported. No Record scalar functional appears.

## Exact Target And Objects

**Target.** Report `cov3` of the two `#6490` exception maps `f00` and `f10`
on the two-cube, and decide whether either attains `m3=220`. Display the
pair. Do not adopt a map.

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
f00(c)      = 1  iff  the remaining-bit assignment is (1, 0, 0, 0, 0),
f10(c)      = 1  iff  the remaining-bit assignment is (1, 1, 0, 0, 0),
f_L1(c)     = 1  iff  u(c) ≥ 1.
```

So `f00` fires only on the `wt1` orbit and its complement, `f10` fires on
`wt1` and `opp2` (and their complements), and `f_L1` has remaining bits
`(1, 0, 1, 1, 1)`. None of these maps is adopted.

A locked set `S` determines occupancies: a lattice neighbor in `S` has
occupancy `1`, and every other neighbor — including every off-patch
neighbor — has occupancy `0`. One synchronous tick replaces `S` by

```text
S ∪ { v in two-cube \ S : f(neighborhood_6(v; S)) = 1 }.
```

Then `cov3(f)` is the number of 3-site seeds whose halt set has cardinality
12. Write `m3=220` for the number of 3-site seeds. A map attains `m3` if
and only if it fills every such seed.

## Theorems

**Theorem 1.** There are exactly 24 proper cube rotations and exactly 10
orbits on `{0,1}^6`. The three cuts leave `|F_cut|=32`. The maps `f00` and
`f10` are two of those 32 members. Both have remaining bit `wt1=1`. Both
have `cov2=0`, which is the `#6490` exception pair. The unbalanced-axis
map `f_L1` is one element of `F_cut` and is not Hamming parity. On the
twelve-vertex two-cube with off-patch occupancy `0`, exhaustive evaluation
of the two exception maps on all 220 three-site seeds gives

```text
cov3(f00) = 0
cov3(f10) = 4.
```

So `f00` fills no 3-site seed, and `f10` fills four of the 220.

**Theorem 2.** Because `cov3(f00)=0 < 220` and `cov3(f10)=4 < 220`,
neither attains `m3=220`. The `#6490` exceptions do not fill the 3-site
seed class. Neither attains m3=220.

**Theorem 3.** The pair

```text
(cov3(f00), cov3(f10)) = (0, 4)
```

is displayed. Neither remaining-bit tuple is adopted as the physical
Admissibility rule.

## Proof-Obligation Graph

| obligation | exact disposition |
|---|---|
| 24 proper cube rotations | signed permutations of the three axes with determinant `+1` |
| 10 orbits on `{0,1}^6` | axis-type classes `(u,b,e)` partition the 64 cells with the listed sizes |
| `|F_cut|=32` | three complement-pairs and two complement-fixed orbits remain free after empty/full are forced to `0` |
| `f00` and `f10` in `F_cut` | remaining-bit tuples `(1, 0, 0, 0, 0)` and `(1, 1, 0, 0, 0)` |
| 220 three-site seeds | `C(12,3)` unordered triples on the two-cube; `m3=220` |
| `f_L1` is not Hamming | unbalanced-axis predicate disagrees with `|c|_1 mod 2` and has remaining bits `(1, 0, 1, 1, 1)` |
| pair `(cov3(f00), cov3(f10))` | exhaustive `cov3` yields `(0, 4)` |
| attain `m3` | fails for both maps |
| displayed tuples | `(1, 0, 0, 0, 0)` and `(1, 1, 0, 0, 0)`, not adopted |

## What This Does Not Claim

- No physical Admissibility selector.
- No `Z^3`-wide formation law.
- No ranking of the other 30 maps in `F_cut`.
- No reopening of the 32-map global `Max(3)` pair.
- No blank-block or 4-site variant.

## No-Go Discipline Gate

The only negative claim is attainment of `m3`: neither `#6490` exception
fills every 3-site seed on this patch. The positive pair
`(cov3(f00), cov3(f10))=(0, 4)` is an exact enumeration, not a wall.

### N1 — materially distinct routes

| Route | Exact attack | Result and authority | Marker |
|---|---|---|---|
| orbit reconstruction | Recompute the 24 rotations and the 10 axis-type orbits. | Theorem 1 and checks `thm1-twenty-four-rotations` / `thm1-ten-orbits`. | **ATTEMPTED** |
| three-cut class | Force vanish-on-empty, vanish-on-full, and `f(c)=f(1-c)`. | Theorem 1 and check `thm1-f-cut-cardinality` give `|F_cut|=32`. | **ATTEMPTED** |
| Hamming-as-`f_L1` | Test whether `|c|_1 mod 2` equals the unbalanced-axis predicate. | Theorem 1 and check `thm1-f-L1-not-hamming` separate the maps. | **ATTEMPTED** |
| two-exception 3-site score | Score `f00` and `f10` by `cov3` on all 220 seeds. | Theorem 1 and check `thm1-cov3-f00-and-f10` give `0` and `4`. | **ATTEMPTED** |
| attain `m3=220` | Ask whether either exception fills every 3-site seed. | Theorem 2 and check `thm2-neither-attains-m3`. | **ATTEMPTED** |
| adopt a map | Write `f00` or `f10` into Admissibility. | Theorem 3 and check `thm3-displayed-not-adopted`. | **ATTEMPTED** |

### N2 — wall independence and collapse

There is one negative conclusion: neither exception attains `m3=220`. The
two separate inequalities `0<220` and `4<220` are two certificates of the
same non-attainment, so they collapse rather than count as two walls.

| Pair | First closes second? | Second closes first? | Disposition |
|---|---:|---:|---|
| `cov3(f00)=0` / `cov3(f10)=4` | no: one map's score does not name the other | no: four fills do not force zero fills | independent positive integers |
| pair `(0, 4)` / non-attainment of `m3` | yes: both scores are below 220 | no: non-attainment does not name the scores | independent scores versus the ceiling test |
| static `#6490` pair / this `cov3` pair | no: `cov2=0` is not 3-site dynamics | no: a 3-site score does not replace the 2-site exception | different `|S|` |
| leftover `#6490` / this ranking | no: that leftover scored only `cov2` | no: a 3-site pair does not replace the 2-site census | New \|S\| |

Physical law selection is not a wall: this note makes no negative theorem
about the existence of a selector and simply does not claim one.

### N3 — hidden-condition scan

| Phrase or premise | Classification |
|---|---|
| “work on the twelve-vertex two-cube” | explicit patch hypothesis; not a `Z^3` theorem |
| off-patch occupancy `0` | explicit default; blank-block is a different rule |
| `F_cut` | explicit three-cut class; the other 992 covariant maps are excluded |
| remaining bits `(1, 0, 0, 0, 0)` and `(1, 1, 0, 0, 0)` | explicit scored pair; the other 30 maps are unclaimed |
| all 220 three-site seeds | explicit seed class; a 2-site ranking is a different residual |
| “lock” | Record permanence on this Boolean occupancy model, not a possibility-valued law |
| “cube-covariant” | invariance under the 24 proper rotations, cited to Lattice/Admissibility |
| Hamming parity | displayed mutation only |
| remaining-bit tuples `(1, 0, 0, 0, 0)` and `(1, 1, 0, 0, 0)` | displayed witnesses, not selected laws |

### N4 — citation-to-residual matching

| Evidence path:line | Residual attacked | Residual claimed closed | Match? |
|---|---|---|---:|
| `docs/MINIMAL_AXIOMS_2026-06-29.md:37` | ambient lattice and cubic rotations | sites are `Z^3` with proper cubic rotations | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:57` | covariant nearest-neighbor rule | covariance is the class filter, not a selector | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:79` | lock permanence | a locked site stays locked | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:83` | unreadability of absence | unlocked and off-patch sites contribute occupancy `0`, not a readout | yes |
| `scripts/f_cut_c00_c10_three_site_coverage_2026_08_15.py:81` | 24 proper rotations | signed permutations with determinant `+1` | yes |
| `scripts/f_cut_c00_c10_three_site_coverage_2026_08_15.py:125` | `f_L1` definition | unbalanced-axis predicate, not Hamming | yes |
| `scripts/f_cut_c00_c10_three_site_coverage_2026_08_15.py:130` | Hamming mutation | `|c|_1 mod 2` is a different `F_cut` map | yes |
| `scripts/f_cut_c00_c10_three_site_coverage_2026_08_15.py:53` | 220 three-site seeds | `C(12,3)` unordered triples on the two-cube | yes |
| `scripts/f_cut_c00_c10_three_site_coverage_2026_08_15.py:144` | `f00` remaining bits | `(1, 0, 0, 0, 0)` | yes |
| `scripts/f_cut_c00_c10_three_site_coverage_2026_08_15.py:149` | `f10` remaining bits | `(1, 1, 0, 0, 0)` | yes |
| `scripts/f_cut_c00_c10_three_site_coverage_2026_08_15.py:210` | `cov3(f)` | number of 3-site seeds a map fills | yes |
| `scripts/f_cut_c00_c10_three_site_coverage_2026_08_15.py:67` | `m3=220` | seed-count ceiling | yes |

No evidence citation is used to claim that a physical occupancy law, a
formation rate, or a `Z^3`-wide selector has been closed.

### N5 — rhetoric and resolution audit

| Resolution | Executed? | Narrow negative supported? |
|---|---:|---|
| per element | yes: all 64 neighbor 6-tuples | each is assigned its axis-type orbit; no broader cell class is classified |
| per site | yes: the twelve two-cube vertices | each uses the same six-direction stencil with off-patch occupancy `0` |
| per mode | yes: `f00` and `f10` | the score is these two maps on all 220 seeds; other classes are unclaimed |
| per block | yes: the pair `(0, 4)` against `m3=220` | neither exception attains the ceiling |
| lattice wide | no | no `Z^3`-wide formation or Admissibility selector is asserted |

The runner prints the same five resolution statements.

### N6 — partial closure and primitive scan

The primitive registry at `docs/audit/data/axiom_premise_nodes.json` was
checked. The only dependency used is the registered `minimal_axioms` node.
Approved primitives are `scale_reference_primitive`,
`kinetic_isotropy_primitive`, and `realized_state_primitive`. None of them
supplies a Boolean occupancy map, a seed-coverage ranking, or an
Admissibility selector, and none is reclassified as an import or wall.

One partial-closure mechanism is displayed rather than suppressed: `f10`
does fill four of the 220 three-site seeds, while `f00` fills none. That
positive pair does not make either tuple a unique maximizer and does not
select either as the physical rule. The remaining physical choice —
which, if any, `F_cut` map is the Admissibility occupancy predicate —
stays explicit.

The open derivation-obligation registry
(`docs/audit/data/derivation_obligations.json`) names no occupancy-to-lock
coverage target; those open gates are unused here.

### N7 — hostile steelman

The strongest objection is that `#6490` already showed these two maps
never fill a 2-site seed, so a 3-site score might be called leftover
decoration of that silence. That objection is correctly about `cov2=0`.
It does not overturn the stated theorem: on the 220 three-site seeds,
`f00` still fills none, while `f10` fills four. Two-site silence does
not name the 3-site pair. This is a new `|S|`.

### N8 — cross-cycle echo

Repository search found nearby occupancy and covariance surfaces. They are
context, not load-bearing dependencies. The 24 rotations, 10 orbits,
`F_cut`, the two exception maps, and the 220-seed scores are recomputed
here.

| Earlier surface | Similar issue | Mechanism considered here |
|---|---|---|
| `docs/ADMISSIBILITY_COVARIANT_Q8_CONDITIONAL_LAW_PAIR_BOUNDED_THEOREM_NOTE_2026-08-13.md` | proper-cubic covariance of a local rule | covariance is used only as the orbit filter for Boolean maps |
| `docs/PHYSICAL_SPATIAL_BLOCK_SEAM_DICHOTOMY_CYCLE728_NOTE_2026-08-04.md` | two-cell box `{0,1,2}×{0,1}×{0,1}` | the same twelve spatial vertices are the patch; the seam cost is unused |
| `docs/MINIMAL_AXIOMS_2026-06-29.md` | one covariant nearest-neighbor rule | the axiom names the contract; this note does not select the rule |

No earlier mechanism retires the two-exception 3-site coverage pair or
restores attainment of `m3=220` for `f00` or `f10`.

No-Go Discipline disposition: **PASS** for the non-attainment of `m3` and
the exact pair `(cov3(f00), cov3(f10))` stated above.

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
`F_cut`, evaluates `f00=(1,0,0,0,0)` and `f10=(1,1,0,0,0)` on the
two-cube from every 3-site seed, reports `cov3(f00) = 0` and
`cov3(f10) = 4`, checks that neither attains `m3=220`, checks that
`f_L1` is not Hamming parity, and exhibits the two remaining-bit tuples
as displayed, not adopted. Declared audit inputs are this note and the
axiom memo. No runner cache is written.
