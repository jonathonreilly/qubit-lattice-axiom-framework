---
claim_id: f_cut_qstar_cov8_max_selector_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Among the 8 F_cut maps with wt1=1 and adj2=1 on the two-cube with off-patch o=0, whether maximal cov8 equals vertex3=mixed3=1 is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_qstar_cov8_max_selector_2026_08_15.py
---

# Maximal Eight-Site Coverage Versus `vertex3` And `mixed3` Inside `Q_*`

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact occupancy-to-lock 8-site coverage of the eight
cube-covariant cut maps in `Q_*` — the `F_cut` subclass with `wt1=1`
and `adj2=1` — on the twelve-vertex two-cube with off-patch occupancy
`0`, over all 495 unordered 8-site seeds, in remaining-bit lex order,
together with whether maximal `cov8` among those eight equals the
displayed conjunction `vertex3=1` and `mixed3=1`. Displayed, not adopted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_qstar_cov8_max_selector_2026_08_15.py`](../scripts/f_cut_qstar_cov8_max_selector_2026_08_15.py)
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
forced to `0`. Write `Q_*` for the eight maps with `wt1=1` and `adj2=1`.
Those eight remaining-bit tuples, in remaining-bit lex order, are

```text
(1, 0, 1, 0, 0), (1, 0, 1, 0, 1), (1, 0, 1, 1, 0), (1, 0, 1, 1, 1),
(1, 1, 1, 0, 0), (1, 1, 1, 0, 1), (1, 1, 1, 1, 0), (1, 1, 1, 1, 1).
```

Investment among `Q_*` scored tot3/tot5/tot7/tot10 and found each of
those totalities iff `vertex3=1` and `mixed3=1`. That is a family of
totality residuals at other seed sizes. The present object is maximal
`cov8` among those same eight maps, and whether Max(8) equals the
displayed conjunction `Q := (vertex3=1 and mixed3=1)`. New k inside Q_*,
not leftover tot3/tot5/tot7/tot10.

On the two-cube `{0,1,2}×{0,1}×{0,1}`, each unordered 8-set of vertices is
an 8-site seed. There are `C(12,8)=495` such seeds. Off-patch neighbors
have occupancy `0`. Each tick, every unlocked on-patch vertex evaluates
`f` on its six-neighbor occupancy tuple and locks if `f=1`. The process
is synchronous and stops at a fixed point in at most 13 ticks. Fill means
`|locks_halt|=12`. Coverage is

```text
cov8(f) = |{ S : |S|=8 and f fills from S }|.
```

Write `m8` for the maximum of `cov8` among the eight. Max(8) is the set
of `Q_*` maps attaining `m8`. The seed-count ceiling is 495: a map
attains that ceiling exactly when it fills every 8-site seed. Do not
list the seeds.

`f_L1(c)=1` if and only if some axis is unbalanced: the signed pair
`n_μ = c_{+μ} − c_{-μ}` is nonzero. This is **not** Hamming parity
`|c|_1 mod 2`. The remaining-bit tuple of `f_L1` is `(1, 0, 1, 1, 1)`,
which sits in `Q_*`.

**Theorem 1.** Exhaustive evaluation of each of the eight `Q_*` maps on
all 495 eight-site seeds, in remaining-bit lex order, gives

```text
cov8((1, 0, 1, 0, 0)) = 158
cov8((1, 0, 1, 0, 1)) = 182
cov8((1, 0, 1, 1, 0)) = 446
cov8((1, 0, 1, 1, 1)) = 494
cov8((1, 1, 1, 0, 0)) = 175
cov8((1, 1, 1, 0, 1)) = 183
cov8((1, 1, 1, 1, 0)) = 471
cov8((1, 1, 1, 1, 1)) = 495
```

Thus `m8 = 495`, attained only by `(1, 1, 1, 1, 1)`. The displayed `Q`
holds on `(1, 0, 1, 1, 1)` and `(1, 1, 1, 1, 1)`. Maximal `cov8` among
the eight is not equivalent to `vertex3=1` and `mixed3=1`.

**Theorem 2.** Write `N_max` for the number of `Q_*` maps attaining
`m8`, `N_Q` for the number with `Q=1`, and `N_both` for the number
with both. Then

```text
N_max = 1
N_Q = 2
N_both = 1
```

The unique maximizer is `(1, 1, 1, 1, 1)`. The two `Q` maps are
`(1, 0, 1, 1, 1)` and `(1, 1, 1, 1, 1)`. The lex-first miss is
`(1, 0, 1, 1, 1)` — which is `f_L1` — with `Q=1` and `cov8=494`.

**Theorem 3.** The eight-line census and the Max(8) iff `Q` test
are displayed. Do not adopt a bit.

Do not write the ranking into Admissibility. Displayed, not adopted.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The ten-orbit reconstruction, the 32-element F_cut, the eight-element Q_* subclass, the exact cov8 census in remaining-bit lex order, and the Max(8)-iff-Q test are enumerated. No physical law is selected."
trace_class: frontier_discovery
target_claim_id: f_cut_qstar_cov8_max_selector
target_blocker_text: "whether maximal cov8 among the eight Q_* maps equals vertex3=mixed3=1"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the Q_* cov8 census and the Max(8)-iff-Q test; do not adopt a displayed bit"
conditional_surface_status: "exact for the eight Q_* maps on this twelve-vertex patch with off-patch occupancy 0; no Z^3-wide formation law"
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
- the complete set of 495 unordered 8-site seeds;
- the eight remaining-bit tuples of `Q_*`;
- the displayed conjunction `Q := (vertex3=1 and mixed3=1)`.

No observational comparator, literature constant, Wilson weight, rate, or
generator is imported. No Record scalar functional appears.

## Exact Target And Objects

**Target.** Report `cov8` of each of the eight `Q_*` maps on the two-cube,
in remaining-bit lex order, and decide whether maximal `cov8` is equivalent
to `vertex3=1` and `mixed3=1` among those eight. Display the census and the
verdict. Do not adopt a bit.

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

`Q_*` is the subclass with `wt1=1` and `adj2=1`. It has three free bits
(`opp2`, `vertex3`, `mixed3`) and size 8. Define

```text
f_L1(c)     = 1  iff  u(c) ≥ 1,
Q(f)        = 1  iff  vertex3(f)=1 and mixed3(f)=1.
```

So `f_L1` has remaining bits `(1, 0, 1, 1, 1)` and is one of the eight
`Q_*` maps. The displayed `Q` holds on exactly two of those eight:
`(1, 0, 1, 1, 1)` and `(1, 1, 1, 1, 1)`. Neither map is adopted.

A locked set `S` determines occupancies: a lattice neighbor in `S` has
occupancy `1`, and every other neighbor — including every off-patch
neighbor — has occupancy `0`. One synchronous tick replaces `S` by

```text
S ∪ { v in two-cube \ S : f(neighborhood_6(v; S)) = 1 }.
```

Then `cov8(f)` is the number of 8-site seeds whose halt set has cardinality
12. Write `m8` for the maximum of those eight integers. A map is in Max(8)
if and only if it attains `m8`. Off-patch occupancy `0` is an explicit
default; a blank-block is a different rule.

## Theorems

**Theorem 1.** There are exactly 24 proper cube rotations and exactly 10
orbits on `{0,1}^6`. The three cuts leave `|F_cut|=32`. The subclass
`Q_*` is the eight members with `wt1=1` and `adj2=1`, listed in
remaining-bit lex order in the Result Up Front. The unbalanced-axis map
`f_L1` is one element of `Q_*` and is not Hamming parity. On the
twelve-vertex two-cube with off-patch occupancy `0`, exhaustive evaluation
of each of the eight on all 495 eight-site seeds gives the census

```text
cov8((1, 0, 1, 0, 0)) = 158
cov8((1, 0, 1, 0, 1)) = 182
cov8((1, 0, 1, 1, 0)) = 446
cov8((1, 0, 1, 1, 1)) = 494
cov8((1, 1, 1, 0, 0)) = 175
cov8((1, 1, 1, 0, 1)) = 183
cov8((1, 1, 1, 1, 0)) = 471
cov8((1, 1, 1, 1, 1)) = 495
```

Maximal `cov8` among the eight is `m8 = 495`, attained only by
`(1, 1, 1, 1, 1)`. That is not equivalent to `vertex3=1` and `mixed3=1`.

**Theorem 2.** Write `N_max` for the number of `Q_*` maps with
`cov8=m8`, `N_Q` for the number with `Q=1`, and `N_both` for the
number with both. Then `N_max = 1`, `N_Q = 2`, and `N_both = 1`.
The lex-first miss is `(1, 0, 1, 1, 1)`: it has `Q=1` and
`cov8=494 < m8`.

**Theorem 3.** The eight-line census and the failed equivalence are
displayed. Do not adopt a bit. Do not write the ranking into
Admissibility.

## Proof-Obligation Graph

| obligation | exact disposition |
|---|---|
| 24 proper cube rotations | signed permutations of the three axes with determinant `+1` |
| 10 orbits on `{0,1}^6` | axis-type classes `(u,b,e)` partition the 64 cells with the listed sizes |
| `|F_cut|=32` | three complement-pairs and two complement-fixed orbits remain free after empty/full are forced to `0` |
| `|Q_*|=8` | remaining bits with `wt1=1` and `adj2=1`, lex-ordered |
| 495 eight-site seeds | `C(12,8)` unordered 8-sets on the two-cube |
| `f_L1` is not Hamming | unbalanced-axis predicate disagrees with `|c|_1 mod 2` and has remaining bits `(1, 0, 1, 1, 1)` |
| eight-line `cov8` census | exhaustive `cov8` on `Q_*` yields `(158, 182, 446, 494, 175, 183, 471, 495)` |
| Max(8) iff `Q` | fails: `N_max = 1`, `N_Q = 2`, `N_both = 1`; lex-first miss `(1, 0, 1, 1, 1)` |
| displayed tuples | the eight `Q_*` remaining-bit tuples and `Q`, not adopted |

## What This Does Not Claim

- No physical Admissibility selector.
- No `Z^3`-wide formation law.
- No ranking of the other 24 maps in `F_cut`.
- No reopening of tot3/tot5/tot7/tot10 as a selector.
- No adoption of `Q`, of `f_L1`, or of any remaining bit.
- No blank-block or other-`k` variant.

## No-Go Discipline Gate

The census is an exact enumeration, not a wall. The Max(8)-iff-`Q` test
fails among `Q_*` and is not an Admissibility selector.

### N1 — materially distinct routes

| Route | Exact attack | Result and authority | Marker |
|---|---|---|---|
| orbit reconstruction | Recompute the 24 rotations and the 10 axis-type orbits. | Theorem 1 and checks `thm1-twenty-four-rotations` / `thm1-ten-orbits`. | **ATTEMPTED** |
| three-cut class and `Q_*` | Force vanish-on-empty, vanish-on-full, `f(c)=f(1-c)`, then `wt1=adj2=1`. | Theorem 1 and checks `thm1-f-cut-cardinality` / `thm1-qstar-eight-lex` give `|F_cut|=32` and `|Q_*|=8`. | **ATTEMPTED** |
| Hamming-as-`f_L1` | Test whether `|c|_1 mod 2` equals the unbalanced-axis predicate. | Theorem 1 and check `thm1-f-L1-not-hamming` separate the maps. | **ATTEMPTED** |
| eight-map 8-site score | Score each `Q_*` map by `cov8` on all 495 seeds in lex order. | Theorem 1 and check `thm1-max-not-iff-q`. | **ATTEMPTED** |
| Max(8) iff `Q` | Ask whether maximal `cov8` equals `vertex3=mixed3=1` among the eight. | Theorem 2 and check `thm2-counts-and-lex-first-miss`. | **ATTEMPTED** |
| adopt a bit | Write `Q` or any remaining bit into Admissibility. | Theorem 3 and check `thm3-displayed-not-adopted`. | **ATTEMPTED** |

### N2 — wall independence and collapse

There is no wall. The eight `cov8` integers are an exact enumeration.
The failing Max(8)-iff-`Q` test is one displayed conjunction on this
eight-map list, not a physical selector.

| Pair | First closes second? | Second closes first? | Disposition |
|---|---:|---:|---|
| eight `cov8` integers / Max(8)-iff-`Q` | yes: the census names who attains `m8` | no: the failed equivalence does not name the six non-maximal scores | independent census versus the iff test |
| maximizer `(1, 1, 1, 1, 1)` / miss `(1, 0, 1, 1, 1)` | no: tot8 with `opp2` does not force the `opp2=0` `Q` map to attain `m8` | no: the miss does not forbid the `opp2=1` maximizer | independent remaining-bit witnesses of the same `Q` |
| leftover tot3/tot5/tot7/tot10 / this Max(8) test | no: totality at other seed sizes does not name Max(8) | no: an eight-site maximizer test does not replace those totalities | New k inside `Q_*` |
| tot8 ceiling / Max(8) | yes here: `m8` happens to equal the seed count | no in general: a unique maximizer need not fill every seed | reported fact, not a new law |

Physical law selection is not a wall: this note makes no negative theorem
about the existence of a selector and simply does not claim one.

### N3 — hidden-condition scan

| Phrase or premise | Classification |
|---|---|
| “work on the twelve-vertex two-cube” | explicit patch hypothesis; not a `Z^3` theorem |
| off-patch occupancy `0` | explicit default; blank-block is a different rule |
| `F_cut` | explicit three-cut class; the other 992 covariant maps are excluded |
| `Q_*` | explicit `wt1=1` and `adj2=1` subclass; the other 24 maps are unclaimed |
| all 495 eight-site seeds | explicit seed class; tot3/tot5/tot7/tot10 are different residuals |
| displayed `Q` | explicit conjunction of two remaining bits; not a derived law |
| “lock” | Record permanence on this Boolean occupancy model, not a possibility-valued law |
| “cube-covariant” | invariance under the 24 proper rotations, cited to Lattice/Admissibility |
| Hamming parity | displayed mutation only |
| remaining-bit tuples of `Q_*` | displayed witnesses, not selected laws |

### N4 — citation-to-residual matching

| Evidence path:line | Residual attacked | Residual claimed closed | Match? |
|---|---|---|---:|
| `docs/MINIMAL_AXIOMS_2026-06-29.md:37` | ambient lattice and cubic rotations | sites are `Z^3` with proper cubic rotations | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:57` | covariant nearest-neighbor rule | covariance is the class filter, not a selector | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:79` | lock permanence | a locked site stays locked | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:83` | unreadability of absence | unlocked and off-patch sites contribute occupancy `0`, not a readout | yes |
| `scripts/f_cut_qstar_cov8_max_selector_2026_08_15.py:80` | 24 proper rotations | signed permutations with determinant `+1` | yes |
| `scripts/f_cut_qstar_cov8_max_selector_2026_08_15.py:124` | `f_L1` definition | unbalanced-axis predicate, not Hamming | yes |
| `scripts/f_cut_qstar_cov8_max_selector_2026_08_15.py:129` | Hamming mutation | `|c|_1 mod 2` is a different map | yes |
| `scripts/f_cut_qstar_cov8_max_selector_2026_08_15.py:55` | 495 eight-site seeds | `C(12,8)` unordered 8-sets on the two-cube | yes |
| `scripts/f_cut_qstar_cov8_max_selector_2026_08_15.py:143` | `Q_*` membership | `wt1=1` and `adj2=1` | yes |
| `scripts/f_cut_qstar_cov8_max_selector_2026_08_15.py:148` | displayed `Q` | `vertex3=1` and `mixed3=1` | yes |
| `scripts/f_cut_qstar_cov8_max_selector_2026_08_15.py:245` | `cov8(f)` | number of 8-site seeds a map fills | yes |
| `scripts/f_cut_qstar_cov8_max_selector_2026_08_15.py:67` | seed-count 495 | `C(12,8)` ceiling used as the comparison scale | yes |

No evidence citation is used to claim that a physical occupancy law, a
formation rate, or a `Z^3`-wide selector has been closed.

### N5 — rhetoric and resolution audit

| Resolution | Executed? | Narrow negative supported? |
|---|---:|---|
| per element | yes: all 64 neighbor 6-tuples | each is assigned its axis-type orbit; no broader cell class is classified |
| per site | yes: the twelve two-cube vertices | each uses the same six-direction stencil with off-patch occupancy `0` |
| per mode | yes: the eight `Q_*` maps | the score is these eight maps on all 495 seeds; other classes are unclaimed |
| per block | yes: the census against Max(8) iff `Q` | maximal `cov8` is not the displayed conjunction among the eight |
| lattice wide | no | no `Z^3`-wide formation or Admissibility selector is asserted |

The runner prints the same five resolution statements.

### N6 — partial closure and primitive scan

The primitive registry at `docs/audit/data/axiom_premise_nodes.json` was
checked. The only dependency used is the registered `minimal_axioms` node.
Approved primitives are `scale_reference_primitive`,
`kinetic_isotropy_primitive`, and `realized_state_primitive`. None of them
supplies a Boolean occupancy map, a seed-coverage ranking, or an
Admissibility selector, and none is reclassified as an import or wall.

One partial-closure mechanism is displayed rather than suppressed: one of
the eight maps fills every 8-site seed, one `Q` map misses a single seed,
and six maps miss more. That split makes Max(8) strictly smaller than `Q`
among `Q_*` on this patch and does not select the maximizer as the
physical rule. The remaining physical choice — which, if any, `F_cut` map
is the Admissibility occupancy predicate — stays explicit.

The open derivation-obligation registry
(`docs/audit/data/derivation_obligations.json`) names no occupancy-to-lock
coverage target; those open gates are unused here.

### N7 — hostile steelman

The strongest objection is that tot3/tot5/tot7/tot10 already asked
whether those totalities equal `vertex3=1` and `mixed3=1` among `Q_*`,
so an eight-line 8-site census plus the same two-bit conjunction might
be called leftover decoration of those totality tests. That objection
is correctly about different seed classes, or about totality rather than
the maximizer set. It does not overturn the stated theorem: on the 495
eight-site seeds the eight `cov8` values are the integers above, `m8=495`
is attained only by `(1, 1, 1, 1, 1)`, and `Q` also holds on
`(1, 0, 1, 1, 1)` with `cov8=494`. A tot7 census does not name the
8-site maximizer set. This is a new `k` inside `Q_*`, not leftover
tot3/tot5/tot7/tot10.

### N8 — cross-cycle echo

Repository search found nearby occupancy and covariance surfaces. They are
context, not load-bearing dependencies. The 24 rotations, 10 orbits,
`F_cut`, the eight `Q_*` maps, and the 495-seed scores are recomputed
here.

| Earlier surface | Similar issue | Mechanism considered here |
|---|---|---|
| `docs/ADMISSIBILITY_COVARIANT_Q8_CONDITIONAL_LAW_PAIR_BOUNDED_THEOREM_NOTE_2026-08-13.md` | proper-cubic covariance of a local rule | covariance is used only as the orbit filter for Boolean maps |
| `docs/PHYSICAL_SPATIAL_BLOCK_SEAM_DICHOTOMY_CYCLE728_NOTE_2026-08-04.md` | two-cell box `{0,1,2}×{0,1}×{0,1}` | the same twelve spatial vertices are the patch; the seam cost is unused |
| `docs/MINIMAL_AXIOMS_2026-06-29.md` | one covariant nearest-neighbor rule | the axiom names the contract; this note does not select the rule |

No earlier mechanism retires the eight-map `cov8` census or replaces
Max(8) iff `Q` among `Q_*`.

No-Go Discipline disposition: **PASS** for the Max(8)-iff-`Q` test
and the exact eight-line `cov8` census stated above.

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
`F_cut` and the eight-element `Q_*` subclass, evaluates each remaining-bit
tuple in lex order on the two-cube from every 8-site seed, reports the
eight `cov8` values, checks that maximal `cov8` is not equivalent to
`vertex3=1` and `mixed3=1`, reports `N_max`, `N_Q`, `N_both` and the
lex-first miss, checks that `f_L1` is not Hamming parity, and exhibits
the census and `Q` as displayed, not adopted. Declared audit inputs are
this note and the axiom memo. No runner cache is written.
