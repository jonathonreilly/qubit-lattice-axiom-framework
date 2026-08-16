---
claim_id: f_cut_qstar_cov11_census_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Among the 8 F_cut maps with wt1=1 and adj2=1 on the two-cube with off-patch o=0, the cov11 values and whether cov11>0 is constant or restricted are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_qstar_cov11_census_2026_08_15.py
---

# Eleven-Site Coverage Census Of The Eight `Q_*` Maps

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact occupancy-to-lock 11-site coverage of the eight
cube-covariant cut maps in `Q_*` — the `F_cut` subclass with `wt1=1`
and `adj2=1` — on the twelve-vertex two-cube with off-patch occupancy
`0`, over all 12 unordered 11-site seeds, in remaining-bit lex order,
together with whether `cov11>0` is constant on those eight or equals a
displayed remaining-bit restriction. Displayed, not adopted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_qstar_cov11_census_2026_08_15.py`](../scripts/f_cut_qstar_cov11_census_2026_08_15.py)
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

Investment #6516 identified `Q_*` with `cov1>0`. Investment #6476
recorded Max duality only for k=4,5. The present object is the 11-site
coverage of each of those eight maps, and whether `cov11>0` is constant
on `Q_*` or equals a displayed remaining-bit restriction. New k inside
Q_*: the scored predicate is `cov11>0` on this seed class, not leftover
`cov1>0` as a rename of `Q_*`, and not a Max-duality rename.

On the two-cube `{0,1,2}×{0,1}×{0,1}`, each unordered 11-set of vertices is
an 11-site seed. There are `C(12,11)=12` such seeds. Off-patch neighbors
have occupancy `0`. Each tick, every unlocked on-patch vertex evaluates
`f` on its six-neighbor occupancy tuple and locks if `f=1`. The process
is synchronous and stops at a fixed point in at most 13 ticks. Fill means
`|locks_halt|=12`. Coverage is

```text
cov11(f) = |{ S : |S|=11 and f fills from S }|.
```

The comparison ceiling `m11=12` is that seed count: a map attains `m11`
exactly when it fills every 11-site seed. Do not list the seeds.

`f_L1(c)=1` if and only if some axis is unbalanced: the signed pair
`n_μ = c_{+μ} − c_{-μ}` is nonzero. This is **not** Hamming parity
`|c|_1 mod 2`. The remaining-bit tuple of `f_L1` is `(1, 0, 1, 1, 1)`,
which sits in `Q_*`.

**Theorem 1.** Exhaustive evaluation of each of the eight `Q_*` maps on
all 12 eleven-site seeds, in remaining-bit lex order, gives

```text
cov11((1, 0, 1, 0, 0)) = 4
cov11((1, 0, 1, 0, 1)) = 4
cov11((1, 0, 1, 1, 0)) = 12
cov11((1, 0, 1, 1, 1)) = 12
cov11((1, 1, 1, 0, 0)) = 4
cov11((1, 1, 1, 0, 1)) = 4
cov11((1, 1, 1, 1, 0)) = 12
cov11((1, 1, 1, 1, 1)) = 12
```

Each 11-site seed omits exactly one two-cube vertex. The eight end
vertices (`x ∈ {0,2}`) present neighborhood type `(3,0,0)` (`vertex3`).
The four mid vertices (`x=1`) present neighborhood type `(2,1,0)`, the
complement of `adj2`. Because `F_cut` is complement-even, fill of a
mid-omitting seed is exactly `adj2=1`, and fill of an end-omitting seed
is exactly `vertex3=1`. Hence on `Q_*` one has the displayed identity
`cov11 = 4 + 8·vertex3`.

**Theorem 2.** Among those eight, `cov11>0` holds for all eight. It is
constant, not a remaining-bit restriction. The count is

```text
N_pos11 = 8
```

Every `Q_*` map already has `adj2=1`, so the four mid-omitting seeds
always fill. No extra remaining bit is required for positivity. The
map `(1, 0, 1, 1, 1)` — which is `f_L1` — has `cov11=12`.

**Theorem 3.** The eight-line census and the constant `cov11>0` verdict
are displayed. Do not adopt a bit.

Do not write the ranking into Admissibility. Displayed, not adopted.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The ten-orbit reconstruction, the 32-element F_cut, the eight-element Q_* subclass, the exact cov11 census in remaining-bit lex order, and the constant cov11>0 verdict are enumerated. No physical law is selected."
trace_class: frontier_discovery
target_claim_id: f_cut_qstar_cov11_census
target_blocker_text: "cov11 of each of the eight Q_* maps, and whether cov11>0 is constant or a remaining-bit restriction"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the Q_* cov11 census and the constant positivity verdict; do not adopt a displayed bit"
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
- the complete set of 12 unordered 11-site seeds;
- the eight remaining-bit tuples of `Q_*`;
- the displayed positivity test `cov11>0`.

No observational comparator, literature constant, Wilson weight, rate, or
generator is imported. No Record scalar functional appears.

## Exact Target And Objects

**Target.** Report `cov11` of each of the eight `Q_*` maps on the two-cube,
in remaining-bit lex order, and decide whether `cov11>0` holds for all
eight or equals a displayed remaining-bit restriction. Display the census
and the verdict. Do not adopt a bit.

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
f_L1(c)     = 1  iff  u(c) ≥ 1.
```

So `f_L1` has remaining bits `(1, 0, 1, 1, 1)` and is one of the eight
`Q_*` maps. Neither `f_L1` nor any remaining bit is adopted.

A locked set `S` determines occupancies: a lattice neighbor in `S` has
occupancy `1`, and every other neighbor — including every off-patch
neighbor — has occupancy `0`. One synchronous tick replaces `S` by

```text
S ∪ { v in two-cube \ S : f(neighborhood_6(v; S)) = 1 }.
```

Then `cov11(f)` is the number of 11-site seeds whose halt set has
cardinality 12. Write `m11=12` for the number of 11-site seeds. A map
attains `m11` if and only if it fills every such seed. Off-patch occupancy
`0` is an explicit default; a blank-block is a different rule.

Because an 11-site seed leaves exactly one unlocked vertex, fill is
decided on the first tick by whether `f` fires on that vertex's
all-others-locked neighborhood.

## Theorems

**Theorem 1.** There are exactly 24 proper cube rotations and exactly 10
orbits on `{0,1}^6`. The three cuts leave `|F_cut|=32`. The subclass
`Q_*` is the eight members with `wt1=1` and `adj2=1`, listed in
remaining-bit lex order in the Result Up Front. The unbalanced-axis map
`f_L1` is one element of `Q_*` and is not Hamming parity. On the
twelve-vertex two-cube with off-patch occupancy `0`, exhaustive evaluation
of each of the eight on all 12 eleven-site seeds gives the census

```text
cov11((1, 0, 1, 0, 0)) = 4
cov11((1, 0, 1, 0, 1)) = 4
cov11((1, 0, 1, 1, 0)) = 12
cov11((1, 0, 1, 1, 1)) = 12
cov11((1, 1, 1, 0, 0)) = 4
cov11((1, 1, 1, 0, 1)) = 4
cov11((1, 1, 1, 1, 0)) = 12
cov11((1, 1, 1, 1, 1)) = 12
```

The eight end-omitting seeds fire iff `vertex3=1`. The four mid-omitting
seeds fire iff `adj2=1`. On `Q_*` this is `cov11 = 4 + 8·vertex3`.

**Theorem 2.** Write `N_pos11` for the number of `Q_*` maps with
`cov11>0`. Then `N_pos11 = 8`. So `cov11>0` holds for all eight: it
is constant, not a remaining-bit restriction. The four mid-omitting
seeds already fire from `adj2=1`, which is part of the definition of
`Q_*`.

**Theorem 3.** The eight-line census and the constant positivity verdict
are displayed. Do not adopt a bit. Do not write the ranking into
Admissibility.

## Proof-Obligation Graph

| obligation | exact disposition |
|---|---|
| 24 proper cube rotations | signed permutations of the three axes with determinant `+1` |
| 10 orbits on `{0,1}^6` | axis-type classes `(u,b,e)` partition the 64 cells with the listed sizes |
| `|F_cut|=32` | three complement-pairs and two complement-fixed orbits remain free after empty/full are forced to `0` |
| `|Q_*|=8` | remaining bits with `wt1=1` and `adj2=1`, lex-ordered |
| 12 eleven-site seeds | `C(12,11)` unordered 11-sets on the two-cube; `m11=12` |
| `f_L1` is not Hamming | unbalanced-axis predicate disagrees with `|c|_1 mod 2` and has remaining bits `(1, 0, 1, 1, 1)` |
| eight-line `cov11` census | exhaustive `cov11` on `Q_*` yields `(4, 4, 12, 12, 4, 4, 12, 12)` |
| `cov11>0` constant | holds: `N_pos11 = 8`; not a remaining-bit restriction |
| displayed tuples | the eight `Q_*` remaining-bit tuples, not adopted |

## What This Does Not Claim

- No physical Admissibility selector.
- No `Z^3`-wide formation law.
- No ranking of the other 24 maps in `F_cut`.
- No reopening of a 1-site or `cov1>0` residual as a rename of `Q_*`.
- No Max-duality claim for `k=11`; Max duality only for k=4,5 is prior context.
- No adoption of `f_L1`, of `vertex3`, or of any remaining bit.
- No blank-block or other seed-size variant.

## No-Go Discipline Gate

The census is an exact enumeration, not a wall. The constant `cov11>0`
verdict is the eight-map positivity count on this seed class, not an
Admissibility selector.

### N1 — materially distinct routes

| Route | Exact attack | Result and authority | Marker |
|---|---|---|---|
| orbit reconstruction | Recompute the 24 rotations and the 10 axis-type orbits. | Theorem 1 and checks `thm1-twenty-four-rotations` / `thm1-ten-orbits`. | **ATTEMPTED** |
| three-cut class and `Q_*` | Force vanish-on-empty, vanish-on-full, `f(c)=f(1-c)`, then `wt1=adj2=1`. | Theorem 1 and checks `thm1-f-cut-cardinality` / `thm1-qstar-eight-lex` give `|F_cut|=32` and `|Q_*|=8`. | **ATTEMPTED** |
| Hamming-as-`f_L1` | Test whether `|c|_1 mod 2` equals the unbalanced-axis predicate. | Theorem 1 and check `thm1-f-L1-not-hamming` separate the maps. | **ATTEMPTED** |
| eight-map 11-site score | Score each `Q_*` map by `cov11` on all 12 seeds in lex order. | Theorem 1 and check `thm1-cov11-census-lex`. | **ATTEMPTED** |
| `cov11>0` constant or restricted | Ask whether positivity holds for all eight or iff a remaining-bit restriction. | Theorem 2 and check `thm2-pos11-constant-all-eight`. | **ATTEMPTED** |
| adopt a bit | Write any remaining bit into Admissibility. | Theorem 3 and check `thm3-displayed-not-adopted`. | **ATTEMPTED** |

### N2 — wall independence and collapse

There is no wall. The eight `cov11` integers are an exact enumeration.
The passing constant-positivity test is the eight-map count on this
seed class, not a physical selector.

| Pair | First closes second? | Second closes first? | Disposition |
|---|---:|---:|---|
| eight `cov11` integers / `cov11>0` constant | yes: every listed integer is positive | no: positivity does not name the 4-versus-12 split | independent census versus the positivity test |
| mid-omitting 4 / end-omitting 8 | no: `adj2=1` does not force `vertex3` | no: `vertex3` does not replace `adj2` | independent seed classes; positivity uses only the mid class |
| leftover `cov1>0` / this census | no: #6516 already named `Q_*` by `cov1>0` | no: an eight-line 11-site score does not rename that 1-site residual | New k inside `Q_*` |
| Max duality for `k=4,5` / this `cov11` census | no: #6476 is a different seed-size pairing | no: eleven-site scores do not restore that pairing | Max duality only for k=4,5 |

Physical law selection is not a wall: this note makes no negative theorem
about the existence of a selector and simply does not claim one.

### N3 — hidden-condition scan

| Phrase or premise | Classification |
|---|---|
| “work on the twelve-vertex two-cube” | explicit patch hypothesis; not a `Z^3` theorem |
| off-patch occupancy `0` | explicit default; blank-block is a different rule |
| `F_cut` | explicit three-cut class; the other 992 covariant maps are excluded |
| `Q_*` | explicit `wt1=1` and `adj2=1` subclass; the other 24 maps are unclaimed |
| all 12 eleven-site seeds | explicit seed class; a 1-site or 5-site ranking is a different residual |
| displayed `cov11>0` | explicit positivity test; not a derived law |
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
| `scripts/f_cut_qstar_cov11_census_2026_08_15.py:89` | 24 proper rotations | signed permutations with determinant `+1` | yes |
| `scripts/f_cut_qstar_cov11_census_2026_08_15.py:133` | `f_L1` definition | unbalanced-axis predicate, not Hamming | yes |
| `scripts/f_cut_qstar_cov11_census_2026_08_15.py:138` | Hamming mutation | `|c|_1 mod 2` is a different map | yes |
| `scripts/f_cut_qstar_cov11_census_2026_08_15.py:53` | 12 eleven-site seeds | `C(12,11)` unordered 11-sets on the two-cube | yes |
| `scripts/f_cut_qstar_cov11_census_2026_08_15.py:152` | `Q_*` membership | `wt1=1` and `adj2=1` | yes |
| `scripts/f_cut_qstar_cov11_census_2026_08_15.py:248` | `cov11(f)` | number of 11-site seeds a map fills | yes |
| `scripts/f_cut_qstar_cov11_census_2026_08_15.py:65` | `m11=12` | seed-count ceiling | yes |
| `scripts/f_cut_qstar_cov11_census_2026_08_15.py:76` | end-omitting type | missing end vertex presents `(3,0,0)` | yes |
| `scripts/f_cut_qstar_cov11_census_2026_08_15.py:264` | mid-omitting neighborhood | missing mid vertex presents complement of `adj2` | yes |

No evidence citation is used to claim that a physical occupancy law, a
formation rate, or a `Z^3`-wide selector has been closed.

### N5 — rhetoric and resolution audit

| Resolution | Executed? | Narrow negative supported? |
|---|---:|---|
| per element | yes: all 64 neighbor 6-tuples | each is assigned its axis-type orbit; no broader cell class is classified |
| per site | yes: the twelve two-cube vertices | each uses the same six-direction stencil with off-patch occupancy `0` |
| per mode | yes: the eight `Q_*` maps | the score is these eight maps on all 12 seeds; other classes are unclaimed |
| per block | yes: the census against `cov11>0` | positivity holds for all eight and is not a remaining-bit restriction |
| lattice wide | no | no `Z^3`-wide formation or Admissibility selector is asserted |

The runner prints the same five resolution statements.

### N6 — partial closure and primitive scan

The primitive registry at `docs/audit/data/axiom_premise_nodes.json` was
checked. The only dependency used is the registered `minimal_axioms` node.
Approved primitives are `scale_reference_primitive`,
`kinetic_isotropy_primitive`, and `realized_state_primitive`. None of them
supplies a Boolean occupancy map, a seed-coverage ranking, or an
Admissibility selector, and none is reclassified as an import or wall.

One partial-closure mechanism is displayed rather than suppressed: four of
the eight maps fill every 11-site seed (`cov11=12`) and four fill only the
four mid-omitting seeds (`cov11=4`). That split is exactly `vertex3` on
this patch and is not adopted as a physical rule. Positivity itself does
not see the split: `cov11>0` is already guaranteed by `adj2=1`. The
remaining physical choice — which, if any, `F_cut` map is the
Admissibility occupancy predicate — stays explicit.

The open derivation-obligation registry
(`docs/audit/data/derivation_obligations.json`) names no occupancy-to-lock
coverage target; those open gates are unused here.

### N7 — hostile steelman

The strongest objection is that #6516 already read `Q_*` as `cov1>0`, so
an eight-line 11-site census on which every `Q_*` map has `cov11>0` might
be called leftover decoration of that 1-site residual, or a Max-duality
echo of #6476. That objection is correctly about a positive-coverage
threshold at a different seed size. It does not overturn the stated
theorem: on the 12 eleven-site seeds the eight `cov11` values are the
integers above, `cov11>0` holds for all eight, and the positivity test is
constant rather than a remaining-bit restriction. A `cov1>0` threshold
does not name the 11-site census. New k inside Q_*.

### N8 — cross-cycle echo

Repository search found nearby occupancy and covariance surfaces. They are
context, not load-bearing dependencies. The 24 rotations, 10 orbits,
`F_cut`, the eight `Q_*` maps, and the 12-seed scores are recomputed
here.

| Earlier surface | Similar issue | Mechanism considered here |
|---|---|---|
| `docs/ADMISSIBILITY_COVARIANT_Q8_CONDITIONAL_LAW_PAIR_BOUNDED_THEOREM_NOTE_2026-08-13.md` | proper-cubic covariance of a local rule | covariance is used only as the orbit filter for Boolean maps |
| `docs/PHYSICAL_SPATIAL_BLOCK_SEAM_DICHOTOMY_CYCLE728_NOTE_2026-08-04.md` | two-cell box `{0,1,2}×{0,1}×{0,1}` | the same twelve spatial vertices are the patch; the seam cost is unused |
| `docs/MINIMAL_AXIOMS_2026-06-29.md` | one covariant nearest-neighbor rule | the axiom names the contract; this note does not select the rule |

No earlier mechanism retires the eight-map `cov11` census or replaces
the constant `cov11>0` verdict among `Q_*`.

No-Go Discipline disposition: **PASS** for the constant `cov11>0`
verdict and the exact eight-line `cov11` census stated above.

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
tuple in lex order on the two-cube from every 11-site seed, reports the
eight `cov11` values, checks that `cov11>0` holds for all eight and is
not a remaining-bit restriction, checks that `f_L1` is not Hamming
parity, and exhibits the census as displayed, not adopted. Declared
audit inputs are this note and the axiom memo. No runner cache is
written.
