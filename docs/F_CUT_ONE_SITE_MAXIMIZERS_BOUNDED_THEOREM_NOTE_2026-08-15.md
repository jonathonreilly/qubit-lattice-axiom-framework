---
claim_id: f_cut_one_site_maximizers_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Among the 32 F_cut maps on the two-cube with off-patch o=0, the four maps that fill every 1-site seed are named by remaining-bit tuple. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_one_site_maximizers_2026_08_15.py
---

# Four `F_cut` 1-Site Coverage Maximizers Named By Remaining-Bit Tuple

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact naming of the four cube-covariant complement-even predicates
that fill every 1-site seed on the twelve-vertex two-cube with off-patch
occupancy `0`. Each maximizer is identified once by its
`(wt1, opp2, adj2, vertex3, mixed3)` remaining-bit tuple. The four-map
set is displayed. No tuple is adopted as the physical Admissibility
rule.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_one_site_maximizers_2026_08_15.py`](../scripts/f_cut_one_site_maximizers_2026_08_15.py)
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

On the two-cube `{0,1,2}×{0,1}×{0,1}`, each vertex is a 1-site seed.
There are twelve such seeds. Off-patch neighbors have occupancy `0`. Each
tick, every unlocked on-patch vertex evaluates `f` on its six-neighbor
occupancy tuple and locks if `f=1`. The process is synchronous and stops
at a fixed point in at most 12 ticks. Fill means `|locks_halt|=12`.
Coverage is

```text
cov1(f) = |{ S : |S|=1 and f fills from S }|.
```

#6399 is eight maps that fill from one given 1-site seed, not four maps
that fill all twelve. Not leftover-character of #6399. Do not re-list the
eight 1-site fillers. The new object here is the four-map set: the four
remaining-bit tuples that attain the maximum on every 1-site seed.

`f_L1(c)=1` if and only if some axis is unbalanced: `c_{+μ} ≠ c_{-μ}` for
at least one `μ ∈ {x,y,z}`. Equivalently, some discrete neighbor contrast
`n_μ = c_{+μ} − c_{-μ}` is nonzero. This is **not** Hamming parity
`|c|_1 mod 2`.

The five remaining bits of an `F_cut` map, in the displayed order
`(wt1, opp2, adj2, vertex3, mixed3)`, are the values on the three
complement-pairs and two complement-fixed orbits after empty and full are
forced to `0`. Write `f1` for the remaining-bit tuple `(1, 1, 1, 1, 1)`.

**Theorem 1.** Exhaustive recomputation of `cov1` on all 32 maps and all
12 one-site seeds reconfirms

```text
m_1 = 12
N_max_1 = 4.
```

The four maximizers, named by remaining-bit tuple, are

```text
(1, 0, 1, 1, 0)
(1, 0, 1, 1, 1)
(1, 1, 1, 1, 0)
(1, 1, 1, 1, 1)
```

Equivalently, a map in `F_cut` fills every 1-site seed if and only if
`wt1=adj2=vertex3=1`, with `opp2` and `mixed3` free.

**Theorem 2.** Both `f_L1` and `f1` are among them. The map `f_L1` has
remaining-bit tuple `(1, 0, 1, 1, 1)`. The map `f1` has remaining-bit
tuple `(1, 1, 1, 1, 1)`. Each attains `cov1=12`.

**Theorem 3.** Display all four. Do not adopt a tuple. Do not write them into Admissibility. Do not re-list the eight 1-site fillers of #6399.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The ten-orbit reconstruction, the 32-element F_cut, the ranking pair (m_1,N_max_1)=(12,4), and the four remaining-bit tuples that fill every 1-site seed are enumerated. The four-map set is displayed, not written into Admissibility."
trace_class: upstream_support
target_claim_id: f_cut_one_site_maximizers
target_blocker_text: "the four F_cut maps that fill every 1-site seed remain unnamed as remaining-bit tuples"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the named four-map set; any physical use must separately derive an Admissibility selector"
conditional_surface_status: "exact for the four F_cut maximizers on this twelve-vertex patch with off-patch o=0 and all twelve 1-site seeds; no Z^3-wide law and no physical selector"
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
- the complete set of twelve 1-site seeds.

No observational comparator, literature constant, Wilson weight, rate, or
generator is imported. No Record scalar functional appears.

Not leftover-character of #6399 (that named eight maps that fill from one
given 1-site seed, not four maps that fill all twelve). The ranking pair
`(m_1, N_max_1)` is recomputed only so the four attaining maps can be
named.

## Exact Target And Objects

**Target.** Reconfirm the 1-site coverage ranking pair on `F_cut`, then
name the four maps that fill every 1-site seed by remaining-bit tuple.

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
remaining-bit tuple `(1, 1, 1, 1, 1)`. The four displayed maximizers have
remaining-bit tuples `(1, 0, 1, 1, 0)`, `(1, 0, 1, 1, 1)`,
`(1, 1, 1, 1, 0)`, and `(1, 1, 1, 1, 1)`. No tuple is adopted.

A locked set `S` determines occupancies: a lattice neighbor in `S` has
occupancy `1`, and every other neighbor — including every off-patch
neighbor — has occupancy `0`. One synchronous tick replaces `S` by

```text
S ∪ { v in two-cube \ S : f(neighborhood_6(v; S)) = 1 }.
```

Then `cov1(f)` is the number of 1-site seeds whose halt set has cardinality
12, `m_1` is the maximum of `cov1` over `F_cut`, and `N_max_1` is the
number of maps attaining `m_1`. The four-map set is the remaining-bit
tuples with `cov1=m_1`.

## Theorems

**Theorem 1.** There are exactly 24 proper cube rotations and exactly 10
orbits on `{0,1}^6`. The three cuts leave `|F_cut|=32`. The unbalanced-axis
map `f_L1` is one element of `F_cut`. It is not Hamming parity. The map
`f1` is the remaining-bit tuple with every free bit on. On the
twelve-vertex two-cube with off-patch occupancy `0`, exhaustive ranking of
all 32 maps on all twelve 1-site seeds reconfirms

```text
m_1 = 12
N_max_1 = 4.
```

The four remaining-bit tuples that attain `m_1` are

```text
(1, 0, 1, 1, 0)
(1, 0, 1, 1, 1)
(1, 1, 1, 1, 0)
(1, 1, 1, 1, 1)
```

Equivalently, a map in `F_cut` fills every 1-site seed if and only if
`wt1=adj2=vertex3=1`. The bits `opp2` and `mixed3` remain free.

**Theorem 2.** Both `f_L1` and `f1` are among them. Their remaining-bit
tuples are `(1, 0, 1, 1, 1)` and `(1, 1, 1, 1, 1)`, and each has
`cov1=12`.

**Theorem 3.** Display all four. Do not adopt a tuple. Do not write them into Admissibility. The four-map set is a displayed rival class, not a
selected occupancy law. Do not re-list the eight 1-site fillers of #6399.

## Proof-Obligation Graph

| obligation | exact disposition |
|---|---|
| 24 proper cube rotations | signed permutations of the three axes with determinant `+1` |
| 10 orbits on `{0,1}^6` | axis-type classes `(u,b,e)` partition the 64 cells with the listed sizes |
| `|F_cut|=32` | three complement-pairs and two complement-fixed orbits remain free after the vanish cuts |
| `f_L1` is in `F_cut` | `u` is rotation- and complement-invariant and `u(empty)=u(full)=0` |
| `f1` is in `F_cut` | vanish on empty and full, and complement-even on every remaining orbit |
| `f_L1` is not Hamming | the two-unbalanced-axis orbit has even weight and `f_L1=1` |
| two-cube has twelve vertices | `{0,1,2}×{0,1}×{0,1}` |
| twelve 1-site seeds | one singleton per vertex |
| off-patch occupancy `0` | declared stencil default; not a blank-block |
| `m_1` and `N_max_1` | exhaustive 32-map ranking of `cov1`; recomputed, then used only to name the attaining four |
| four-map set | remaining-bit tuples `(1, 0, 1, 1, 0)`, `(1, 0, 1, 1, 1)`, `(1, 1, 1, 1, 0)`, `(1, 1, 1, 1, 1)` |
| `f_L1` and `f1` among them | both remaining-bit tuples occur in the four-map set |

## Counterfactual And Mutation Table

1. Replace `f_L1` by Hamming parity: Hamming is a different `F_cut` map
   (it disagrees on the two-unbalanced-axis orbit) and is not a 1-site
   coverage maximizer.
2. Replace off-patch occupancy `0` by a blank-block: first-wave candidates
   become undefined; that is a different census.
3. Drop complement-even or the vanish-on-full cut: the class is no longer
   the 32-element `F_cut`.
4. Score only one given 1-site seed and list every filler: that leftover
   is #6399, eight maps from one seed, not four maps that fill all twelve.
5. Report only `m_1` and `N_max_1`: that leftover is a coverage count,
   not the named four-map set.
6. Adopt any remaining-bit tuple as the physical rule: the note displays
   all four and writes none into Admissibility.

## What This Does Not Claim

- No physical Admissibility selector and no adopted occupancy law.
- No Qubit rewrite and no `M_2(C)`-valued conditional probability.
- No `Z^3`-wide formation, rate, or generator.
- No identification of `f_L1` with Hamming parity.
- No leftover-character restatement of #6399 in place of the named
  four-map set.
- No re-list of the eight 1-site fillers of one given seed.
- No blank-block or multi-site variant.

## No-Go Discipline Gate

The only negative claim is that the 1-site coverage maximizer inside
`F_cut` is not a singleton and is not `{f_L1}` alone. The named four-map
set is an exact enumeration, not a wall.

### N1 — materially distinct routes

| Route | Exact attack | Result and authority | Marker |
|---|---|---|---|
| orbit reconstruction | Recompute the 24 rotations and the 10 axis-type orbits. | Theorem 1 and checks `thm1-twenty-four-rotations` / `thm1-ten-orbits`. | **ATTEMPTED** |
| three-cut class | Force vanish-on-empty, vanish-on-full, and `f(c)=f(1-c)`. | Theorem 1 and check `thm1-f-cut-cardinality` give `|F_cut|=32`. | **ATTEMPTED** |
| Hamming-as-`f_L1` | Test whether `|c|_1 mod 2` equals the unbalanced-axis predicate. | Theorem 1 and check `thm1-f-L1-not-hamming` separate the maps. | **ATTEMPTED** |
| ranking reconfirm | Score every map in `F_cut` by `cov1`. | Theorem 1 and check `thm1-reconfirm-ranking` give `m_1 = 12` and `N_max_1 = 4`. | **ATTEMPTED** |
| name the four maximizers | List remaining-bit tuples with `cov1=m_1`. | Theorem 1 and check `thm1-named-four-map-set`. | **ATTEMPTED** |
| membership and display | Ask whether `f_L1` and `f1` are among them, and whether any tuple is adopted. | Theorem 2, Theorem 3, and checks `thm2-f-L1-and-f1-among-them` / `thm3-display-not-adopted`. | **ATTEMPTED** |

### N2 — wall independence and collapse

There is one negative conclusion: the maximizer class is not a singleton
and is not `{f_L1}` alone. Naming the four remaining-bit tuples and the
cardinality `N_max_1=4` are two certificates of the same four-map set, so
they collapse rather than count as two walls.

| Pair | First closes second? | Second closes first? | Disposition |
|---|---:|---:|---|
| `N_max_1=4` / named four | yes: a count of four is the set's size | yes: four named tuples give the count | collapse into the four-map set |
| `f_L1` among them / `f1` among them | no: one membership is not the other | no: one membership is not the other | independent positive memberships |
| static `|F_cut|=32` / four-map set | no: membership is not dynamics | no: naming maximizers does not replace the three-cut class | separate exact counts |
| leftover of #6399 / this four-map set | no: that leftover named eight one-seed fillers | no: naming the four does not replace the one-seed census | different object |

Physical law selection is not a wall: this note makes no negative theorem
about the existence of a selector and simply does not claim one.

### N3 — hidden-condition scan

| Phrase or premise | Classification |
|---|---|
| “work on the twelve-vertex two-cube” | explicit patch hypothesis; not a `Z^3` theorem |
| off-patch occupancy `0` | explicit default; blank-block is a different rule |
| `F_cut` | explicit three-cut class; the other 992 covariant maps are excluded |
| all twelve 1-site seeds | explicit seed class; a one-seed fill is a different residual |
| “lock” | Record permanence on this Boolean occupancy model, not a possibility-valued law |
| “cube-covariant” | invariance under the 24 proper rotations, cited to Lattice/Admissibility |
| Hamming parity | displayed mutation only |
| remaining-bit tuples of the four-map set | displayed, not a selected law |

### N4 — citation-to-residual matching

| Evidence path:line | Residual attacked | Residual claimed closed | Match? |
|---|---|---|---:|
| `docs/MINIMAL_AXIOMS_2026-06-29.md:37` | ambient lattice and cubic rotations | sites are `Z^3` with proper cubic rotations | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:57` | covariant nearest-neighbor rule | covariance is the class filter, not a selector | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:79` | lock permanence | a locked site stays locked | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:83` | unreadability of absence | unlocked and off-patch sites contribute occupancy `0`, not a readout | yes |
| `scripts/f_cut_one_site_maximizers_2026_08_15.py:84` | 24 proper rotations | signed permutations with determinant `+1` | yes |
| `scripts/f_cut_one_site_maximizers_2026_08_15.py:128` | `f_L1` definition | unbalanced-axis predicate, not Hamming | yes |
| `scripts/f_cut_one_site_maximizers_2026_08_15.py:133` | Hamming mutation | `|c|_1 mod 2` is a different `F_cut` map | yes |
| `scripts/f_cut_one_site_maximizers_2026_08_15.py:52` | twelve 1-site seeds | one singleton per two-cube vertex | yes |
| `scripts/f_cut_one_site_maximizers_2026_08_15.py:208` | `cov1(f)` | number of 1-site seeds a map fills | yes |
| `scripts/f_cut_one_site_maximizers_2026_08_15.py:311` | ranking | exact `(m_1, N_max_1)` used to name the attaining four | yes |
| `scripts/f_cut_one_site_maximizers_2026_08_15.py:65` | four-map set | displayed remaining-bit tuples that fill every 1-site seed | yes |
| `scripts/f_cut_one_site_maximizers_2026_08_15.py:147` | `f1` | remaining-bit tuple `(1, 1, 1, 1, 1)`, displayed not adopted | yes |

No evidence citation is used to claim that a physical occupancy law, a
formation rate, or a `Z^3`-wide selector has been closed.

### N5 — rhetoric and resolution audit

| Resolution | Executed? | Narrow negative supported? |
|---|---:|---|
| per element | yes: all 64 neighbor 6-tuples | each is assigned its axis-type orbit; no broader cell class is classified |
| per site | yes: the twelve two-cube vertices | each uses the same six-direction stencil with off-patch occupancy `0` |
| per mode | yes: every map in `F_cut` | the four maximizers are named inside this class on all twelve seeds |
| per block | yes: the four-map set | all four remaining-bit tuples attain `m_1`; `f_L1` and `f1` are among them |
| lattice wide | no | no `Z^3`-wide formation or Admissibility selector is asserted |

The runner prints the same five resolution statements.

### N6 — partial closure and primitive scan

The primitive registry at `docs/audit/data/axiom_premise_nodes.json` was
checked. The only dependency used is the registered `minimal_axioms` node.
No approved primitive supplies the Boolean occupancy maps, and none is
reclassified as an import or wall.

One partial-closure mechanism is displayed rather than suppressed: `f_L1`
and `f1` both lie in `F_cut` and both fill every 1-site seed. That
positive membership does not select either named tuple as the physical
rule. The remaining physical choice — which, if any, `F_cut` map is the
Admissibility occupancy predicate — stays explicit.

### N7 — hostile steelman

The strongest objection is that the four maximizers include `f_L1` and
`f1` and therefore might be called leftover-character of #6399, which
already exhibited eight maps that fill from one given 1-site seed. That
objection is correctly about the one-seed fill census. It does not
overturn the stated theorem: #6399 asked which maps fill from one given
seed; this residual asks which maps fill every 1-site seed, and names
those four by remaining-bit tuple. Displaying the four tuples names that
set. No tuple is adopted. Do not re-list the eight 1-site fillers.

### N8 — cross-cycle echo

Repository search found nearby occupancy and covariance surfaces. They are
context, not load-bearing dependencies. The 24 rotations, 10 orbits,
`F_cut`, the 32-map 12-seed ranking, and the four remaining-bit tuples are
recomputed here.

| Earlier surface | Similar issue | Mechanism considered here |
|---|---|---|
| `docs/ADMISSIBILITY_COVARIANT_Q8_CONDITIONAL_LAW_PAIR_BOUNDED_THEOREM_NOTE_2026-08-13.md` | proper-cubic covariance of a local rule | covariance is used only as the orbit filter for Boolean maps |
| `docs/PHYSICAL_SPATIAL_BLOCK_SEAM_DICHOTOMY_CYCLE728_NOTE_2026-08-04.md` | two-cell box `{0,1,2}×{0,1}×{0,1}` | the same twelve spatial vertices are the patch; the seam cost is unused |
| `docs/MINIMAL_AXIOMS_2026-06-29.md` | one covariant nearest-neighbor rule | the axiom names the contract; this note does not select the rule |

No earlier mechanism retires the named four-map set or writes any
remaining-bit tuple into Admissibility.

No-Go Discipline disposition: **PASS** for the named four-map set and the
reconfirmed ranking pair `(m_1, N_max_1)` stated above.

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
`F_cut`, evaluates all 32 maps on the two-cube from every 1-site seed,
reconfirms `m_1 = 12` and `N_max_1 = 4`, names the four maximizers by
remaining-bit tuple `(1, 0, 1, 1, 0)`, `(1, 0, 1, 1, 1)`,
`(1, 1, 1, 1, 0)`, and `(1, 1, 1, 1, 1)`, records that `f_L1` and `f1`
are among them, checks that `f_L1` is not Hamming parity, and does not
adopt a tuple. Declared audit inputs are this note and the axiom memo.
No runner cache is written.
