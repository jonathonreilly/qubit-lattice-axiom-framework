---
claim_id: f_cut_opp2_silent_long_axis_miss_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Among F_cut maps with f(opp2)=0 on the two-cube with off-patch o=0, every map misses all four long-axis 2-site seeds. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_opp2_silent_long_axis_miss_2026_08_15.py
---

# Silent-Opp2 Implies The Four Long-Axis Two-Site Misses

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact occupancy-to-lock census of every cube-covariant
complement-even predicate that vanishes on empty, full, *and* the
opposite-pair orbit `opp2`, on the twelve-vertex two-cube, from each of
the four long-axis 2-site endpairs, with off-patch occupancy `0`. The
unbalanced-axis map `f_L1` is displayed as one member of that subclass.
It is not adopted as the physical Admissibility rule.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_opp2_silent_long_axis_miss_2026_08_15.py`](../scripts/f_cut_opp2_silent_long_axis_miss_2026_08_15.py)
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

`opp2` is the orbit of a cell with exactly one axis fully occupied and the
other four slots `0`. A representative is
`(c_{+x},c_{-x},c_{+y},c_{-y},c_{+z},c_{-z})=(1,1,0,0,0,0)`. The axis type
is `(u,b,e)=(0,1,2)`: no unbalanced axis, one both-occupied axis, two
empty axes. The orbit has size `3`. `f(opp2)=0` means a filled axis does
not form.

Write

```text
F0 = { f ∈ F_cut : f(opp2) = 0 }.
```

The `opp2` bit is one of the five free remaining bits, so `|F0| = 16`.

On the two-cube `{0,1,2}×{0,1}×{0,1}`, each unordered pair of vertices is
a 2-site seed. Off-patch neighbors have occupancy `0`. Each tick, every
unlocked on-patch vertex evaluates `f` on its six-neighbor occupancy
tuple and locks if `f=1`. The process is synchronous and stops at a
fixed point in at most 12 ticks. Fill means `|locks_halt|=12`.

`f_L1(c)=1` if and only if some axis is unbalanced: `c_{+μ} ≠ c_{-μ}` for
at least one `μ ∈ {x,y,z}`. Equivalently, some discrete neighbor contrast
`n_μ = c_{+μ} − c_{-μ}` is nonzero. This is **not** Hamming parity
`|c|_1 mod 2`. The remaining-bit tuple of `f_L1` is
`(wt1, opp2, adj2, vertex3, mixed3) = (1, 0, 1, 1, 1)`, so `f_L1 ∈ F0`.

Write `M` for the four long-axis 2-site endpairs of the two-cube, in
lexicographic order of sorted site pairs:

```text
{(0,0,0),(2,0,0)}
{(0,0,1),(2,0,1)}
{(0,1,0),(2,1,0)}
{(0,1,1),(2,1,1)}
```

These are exactly the four 2-site seeds listed as `f_L1` misses. New
object. Not leftover-character of #6438 (that was listing L1's four).
This note is the class statement: whether every map in `F0` misses every
seed in `M`.

**Theorem 1.** `f_L1 ∈ F0` and misses every seed in `M`. On each seed the
independent `f_L1` run halts unfilled with lock-count history `(2, 6, 8)`.

**Theorem 2.** Every `f` in `F0` misses every seed in `M`. Exhaustive
enumeration of the 16 maps against the four seeds gives 64 misses and
zero fills. Silent-opp2 therefore implies the long-axis misses. There is
no counterexample remaining-bit tuple and no filled seed in `M`.

**Theorem 3.** Display. Do not adopt opp2. Do not write it into Admissibility.

`claim_scope`: Among F_cut maps with f(opp2)=0 on the two-cube with
off-patch o=0, every map misses all four long-axis 2-site seeds.
Displayed, not adopted.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The ten-orbit reconstruction, the 32-element F_cut, the 16-element F0, membership of f_L1, the four long-axis seeds M, and the exact 16-by-4 miss table are enumerated. Silent-opp2 implies the long-axis misses on this patch. No physical law is selected."
trace_class: frontier_discovery
target_claim_id: f_cut_opp2_silent_long_axis_miss
target_blocker_text: "whether every F_cut map with f(opp2)=0 misses the four long-axis 2-site seeds"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the F0 x M miss table; any physical use must separately derive an Admissibility selector"
conditional_surface_status: "exact for F0 on this twelve-vertex patch with off-patch o=0 and the four long-axis 2-site seeds; no Z^3-wide law and no physical selector"
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
laws. Admissibility
does not supply the formation site, probability, or rate.

The following are declared mathematical scaffolding, not measured or fitted
physics inputs:

- the 24 proper signed-permutation rotations of the three axes
  (`det = +1`);
- occupancy 6-tuples on the ordered neighbor stencil
  `(+x,-x,+y,-y,+z,-z)`;
- the two-cube vertex set `{0,1,2}×{0,1}×{0,1}`;
- the off-patch occupancy default `0`;
- the four long-axis 2-site seeds `M`;
- the opposite-pair orbit `opp2` and the subclass `F0`.

No observational comparator, literature constant, Wilson weight, rate, or
generator is imported. No Record scalar functional appears.

Not leftover-character of #6438 (that was listing L1's four). New object:
the class miss of every `F0` map on `M`.

## Exact Target And Objects

**Target.** Restrict the 32-member class `F_cut` to the independently
motivated extra `f(opp2)=0`, reconfirm that `f_L1` lies in that subclass
and misses every seed in `M`, and decide whether every other map in `F0`
misses every seed in `M`.

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
`f(c)=f(1-c)`. The remaining-bit tuple is those five free bits in the
order `(wt1, opp2, adj2, vertex3, mixed3)`. The subclass `F0` freezes the
`opp2` bit at `0` and leaves the other four bits free, so `|F0|=16`.

Define

```text
f_L1(c) = 1  iff  u(c) ≥ 1,
```

so `f_L1` has remaining-bit tuple `(1, 0, 1, 1, 1)` and lies in `F0`.
Neither `f_L1` nor silent-opp2 is adopted.

A locked set `S` determines occupancies: a lattice neighbor in `S` has
occupancy `1`, and every other neighbor — including every off-patch
neighbor — has occupancy `0`. One synchronous tick replaces `S` by

```text
S ∪ { v in two-cube \ S : f(neighborhood_6(v; S)) = 1 }.
```

An independent run of `f` from a seed is that iteration started at the
seed and continued to a fixed point. A miss is a 2-site seed whose halt
set has cardinality strictly less than 12.

`M` is the four long-axis displacement-`(2,0,0)` pairs. `|M| = 4`.

## Theorems

**Theorem 1.** There are exactly 24 proper cube rotations and exactly 10
orbits on `{0,1}^6`. The three cuts leave `|F_cut|=32`. The unbalanced-axis
map `f_L1` is one element of `F_cut` and of `F0`: it vanishes on `opp2`.
It is not Hamming parity. On the twelve-vertex two-cube with off-patch
occupancy `0`, each of the four seeds in `M` is a miss for `f_L1`, with
history `(2, 6, 8)`.

**Theorem 2.** Exhaustive run of every map in `F0` from every seed in `M`
gives

```text
|F0| = 16
|M| = 4
miss events = 64
fill events = 0.
```

Every `f` in `F0` misses every seed in `M`. Silent-opp2 implies the
long-axis misses. No remaining-bit tuple in `F0` fills any seed of `M`.

**Theorem 3.** Display. Do not adopt opp2. Do not write it into Admissibility.
The class miss is displayed census output. It is not a physical selector.

## Proof-Obligation Graph

| obligation | exact disposition |
|---|---|
| 24 proper cube rotations | signed permutations of the three axes with determinant `+1` |
| 10 orbits on `{0,1}^6` | axis-type classes `(u,b,e)` partition the 64 cells with the listed sizes |
| `|F_cut|=32` | three complement-pairs and two complement-fixed orbits remain free after the vanish cuts |
| `|F0|=16` | the `opp2` remaining bit is frozen at `0`; four free bits remain |
| `f_L1` is in `F0` | `u` is rotation- and complement-invariant, `u(empty)=u(full)=0`, and `u(opp2)=0` |
| `f_L1` is not Hamming | the two-unbalanced-axis orbit has even weight and `f_L1=1` |
| `M` is the four long-axis endpairs | lex list of displacement-`(2,0,0)` pairs on the two-cube |
| `f_L1` misses every seed in `M` | four independent runs halt unfilled at history `(2, 6, 8)` |
| every `F0` map misses every seed in `M` | exhaustive 16-by-4 lock-step table; 64 misses, 0 fills |
| off-patch occupancy `0` | declared stencil default; not a blank-block |
| no adoption of `opp2` | displayed class condition, not an Admissibility clause |

## Counterfactual And Mutation Table

1. Replace `f_L1` by Hamming parity: Hamming is a different `F_cut` map
   (it disagrees on the two-unbalanced-axis orbit) and is not the
   unbalanced-axis predicate.
2. Replace off-patch occupancy `0` by a blank-block: first-wave candidates
   become undefined; that is a different census.
3. Drop complement-even or the vanish-on-full cut: the class is no longer
   the 32-element `F_cut`, so `F0` is no longer this 16-element subclass.
4. List only `f_L1`'s four misses: that leftover is #6438, not the class
   statement on `F0`.
5. Turn `opp2` on: maps with `f(opp2)=1` are outside `F0` and are a
   different residual; this note does not adopt that bit.
6. Assert that some `F0` map fills a long-axis seed: the 16-by-4 table
   is empty of fills and refutes the assertion.

## What This Does Not Claim

- No physical Admissibility selector and no adopted occupancy law.
- No Qubit rewrite and no `M_2(C)`-valued conditional probability.
- No `Z^3`-wide formation, rate, or generator.
- No identification of `f_L1` with Hamming parity.
- No leftover-character restatement of listing L1's four (#6438) in
  place of this `F0` class miss.
- No adoption of `opp2` and no write of silent-opp2 into Admissibility.
- No blank-block or 3-site variant.

## No-Go Discipline Gate

The negative content is narrow: silent-opp2 is not hereby adopted. The
positive class miss is an exact enumeration, not a wall.

### N1 — materially distinct routes

| Route | Exact attack | Result and authority | Marker |
|---|---|---|---|
| orbit reconstruction | Recompute the 24 rotations and the 10 axis-type orbits. | Theorem 1 and checks `thm1-twenty-four-rotations` / `thm1-ten-orbits`. | **ATTEMPTED** |
| three-cut class and `F0` | Force vanish-on-empty, vanish-on-full, `f(c)=f(1-c)`, and `f(opp2)=0`. | Theorem 1 and check `thm1-f-cut-cardinality` give `|F_cut|=32` and `|F0|=16`. | **ATTEMPTED** |
| Hamming-as-`f_L1` | Test whether `|c|_1 mod 2` equals the unbalanced-axis predicate. | Theorem 1 and check `thm1-f-L1-not-hamming` separate the maps. | **ATTEMPTED** |
| `f_L1` membership and `M` | Read the `opp2` bit of `f_L1` and run it from each seed in `M`. | Theorem 1 and check `thm1-f-L1-in-F0-misses-M`. | **ATTEMPTED** |
| `F0` class miss | Run every map in `F0` from every seed in `M`. | Theorem 2 and check `thm2-every-F0-misses-every-M` give 64 misses. | **ATTEMPTED** |
| adopt `opp2` | Write silent-opp2 into Admissibility. | Theorem 3 and check `thm3-display-not-adopt`; refused. | **ATTEMPTED** |

### N2 — wall independence and collapse

There is one negative conclusion: `opp2` is not adopted. The 16-map miss
table and the four `f_L1` histories are certificates of the same class
miss, so they collapse rather than count as two walls.

| Pair | First closes second? | Second closes first? | Disposition |
|---|---:|---:|---|
| `f_L1` misses `M` / every `F0` map misses `M` | no: one member is not the class | yes: the class includes `f_L1` | class statement strictly stronger |
| leftover of #6438 / this class miss | no: listing L1's four is not a class theorem | no: a class miss does not replace the L1 list | different object |
| static `|F0|=16` / 16-by-4 table | no: membership is not dynamics | no: a miss table does not replace the `opp2=0` cut | separate exact counts |

Physical law selection is not a wall: this note makes no negative theorem
about the existence of a selector and simply does not claim one.

### N3 — hidden-condition scan

| Phrase or premise | Classification |
|---|---|
| “work on the twelve-vertex two-cube” | explicit patch hypothesis; not a `Z^3` theorem |
| off-patch occupancy `0` | explicit default; blank-block is a different rule |
| `F_cut` | explicit three-cut class; the other 992 covariant maps are excluded |
| `F0` | explicit `opp2=0` subclass of `F_cut` |
| four long-axis 2-site seeds `M` | explicit seed class; a one-seed fill is a different residual |
| “lock” | Record permanence on this Boolean occupancy model, not a possibility-valued law |
| “cube-covariant” | invariance under the 24 proper rotations, cited to Lattice/Admissibility |
| Hamming parity | displayed mutation only |
| silent-opp2 | displayed class condition, not a selected law |

### N4 — citation-to-residual matching

| Evidence path:line | Residual attacked | Residual claimed closed | Match? |
|---|---|---|---:|
| `docs/MINIMAL_AXIOMS_2026-06-29.md:37` | ambient lattice and cubic rotations | sites are `Z^3` with proper cubic rotations | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:57` | covariant nearest-neighbor rule | covariance is the class filter, not a selector | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:79` | lock permanence | a locked site stays locked | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:83` | unreadability of absence | unlocked and off-patch sites contribute occupancy `0`, not a readout | yes |
| `scripts/f_cut_opp2_silent_long_axis_miss_2026_08_15.py:80` | 24 proper rotations | signed permutations with determinant `+1` | yes |
| `scripts/f_cut_opp2_silent_long_axis_miss_2026_08_15.py:124` | `f_L1` definition | unbalanced-axis predicate, not Hamming | yes |
| `scripts/f_cut_opp2_silent_long_axis_miss_2026_08_15.py:129` | Hamming mutation | `|c|_1 mod 2` is a different map | yes |
| `scripts/f_cut_opp2_silent_long_axis_miss_2026_08_15.py:52` | four long-axis seeds | lex endpairs of displacement `(2,0,0)` | yes |
| `scripts/f_cut_opp2_silent_long_axis_miss_2026_08_15.py:179` | lock-step run | independent occupancy-to-lock from a seed | yes |
| `scripts/f_cut_opp2_silent_long_axis_miss_2026_08_15.py:272` | `F_cut` census | 32 remaining-bit assignments | yes |
| `scripts/f_cut_opp2_silent_long_axis_miss_2026_08_15.py:66` | `opp2` orbit | axis type `(0,1,2)` | yes |

No evidence citation is used to claim that a physical occupancy law, a
formation rate, or a `Z^3`-wide selector has been closed.

### N5 — rhetoric and resolution audit

| Resolution | Executed? | Narrow negative supported? |
|---|---:|---|
| per element | yes: all 64 neighbor 6-tuples | each is assigned its axis-type orbit; no broader cell class is classified |
| per site | yes: the twelve two-cube vertices | each uses the same six-direction stencil with off-patch occupancy `0` |
| per mode | yes: every map in `F0` | the miss table is this subclass on the four long-axis seeds |
| per block | yes: the `F0 × M` fill table | every silent-opp2 map misses every seed in `M` |
| lattice wide | no | no `Z^3`-wide formation or Admissibility selector is asserted |

The runner prints the same five resolution statements.

### N6 — partial closure and primitive scan

The primitive registry at `docs/audit/data/axiom_premise_nodes.json` was
checked. The only dependency used is the registered `minimal_axioms` node.
No approved primitive supplies the Boolean occupancy maps, and none is
reclassified as an import or wall.

One partial-closure mechanism is displayed rather than suppressed: `f_L1`
does lie in `F0` and does miss every seed in `M`. That positive member
does not select silent-opp2 as the physical rule. The remaining physical
choice — which, if any, `F0` map is the Admissibility occupancy
predicate — stays explicit.

### N7 — hostile steelman

The strongest objection is that because `f_L1` already misses these four
seeds, and because `f_L1` is the most permissive remaining-bit pattern
inside `F0` except that `mixed3` may be turned off, the class miss is a
leftover of listing L1's four. That objection is correctly about the
static remaining-bit table and about the earlier four-seed list. It does
not overturn the stated theorem: among maps in `F_cut` that already
silence `opp2`, no map fills any long-axis 2-site seed. The 16-by-4
table is a class object, not a restatement of one map's miss set.
Predicate support is not monotone for fill — a weaker map can in
principle occupy a different neighborhood and fire where a stronger map
sees `opp2` — so the class statement is not a corollary of the `f_L1`
list. It is recomputed.

### N8 — cross-cycle echo

Repository search found nearby occupancy and covariance surfaces. They are
context, not load-bearing dependencies. The 24 rotations, 10 orbits,
`F_cut`, `F0`, `M`, and 16-by-4 miss table are recomputed here.

| Earlier surface | Similar issue | Mechanism considered here |
|---|---|---|
| `docs/ADMISSIBILITY_COVARIANT_Q8_CONDITIONAL_LAW_PAIR_BOUNDED_THEOREM_NOTE_2026-08-13.md` | proper-cubic covariance of a local rule | covariance is used only as the orbit filter for Boolean maps |
| `docs/PHYSICAL_SPATIAL_BLOCK_SEAM_DICHOTOMY_CYCLE728_NOTE_2026-08-04.md` | two-cell box `{0,1,2}×{0,1}×{0,1}` | the same twelve spatial vertices are the patch; the seam cost is unused |
| `docs/MINIMAL_AXIOMS_2026-06-29.md` | one covariant nearest-neighbor rule | the axiom names the contract; this note does not select the rule |

No earlier mechanism retires the `F0` long-axis class miss or adopts
`opp2` as Admissibility content.

No-Go Discipline disposition: **PASS** for the class miss and the
displayed, not adopted, silent-opp2 condition stated above.

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
`F_cut`, restricts to `F0`, evaluates all 16 maps on the two-cube from
each of the four long-axis seeds, reports that `f_L1 ∈ F0` misses every
seed in `M` with history `(2, 6, 8)`, reports `|F0| = 16`, `|M| = 4`,
and 64 miss events, checks that `f_L1` is not Hamming parity, and
checks that this note displays the class miss without adopting `opp2`.
Declared audit inputs are this note and the axiom memo. No runner cache
is written.
