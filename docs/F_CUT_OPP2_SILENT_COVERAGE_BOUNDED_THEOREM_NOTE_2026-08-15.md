---
claim_id: f_cut_opp2_silent_coverage_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Among F_cut maps with f(opp2)=0 on the two-cube with off-patch o=0, the maximum 2-site fill coverage is 62, attained by 2 maps. f_L1 is not the unique maximizer. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_opp2_silent_coverage_2026_08_15.py
---

# Opp2-Silent Two-Site Coverage Ranking Inside The Three-Cut Class `F_cut`

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact occupancy-to-lock coverage ranking of those cube-covariant
complement-even predicates that vanish on empty and full *and* vanish on
the opposite-pair orbit `opp2`, on the twelve-vertex two-cube, over all
66 unordered 2-site seeds, with off-patch occupancy `0`. The
unbalanced-axis map `f_L1` is displayed as one scored member. It is not
adopted as the physical Admissibility rule.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_opp2_silent_coverage_2026_08_15.py`](../scripts/f_cut_opp2_silent_coverage_2026_08_15.py)
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
class. The 32-map two-site coverage ranking is a different leftover
inventory. The eight-filler `opp2`-silence count is a different leftover
inventory. This note asks the new restricted ranking object: among the
maps in `F_cut` that already vanish on `opp2`, how many of the 66
two-site seeds does each fill, and is `f_L1` the unique maximizer.

`opp2` is the orbit of a cell with exactly one axis fully occupied and the
other four slots `0`. A representative is
`(c_{+x},c_{-x},c_{+y},c_{-y},c_{+z},c_{-z})=(1,1,0,0,0,0)`. The axis type
is `(u,b,e)=(0,1,2)`: no unbalanced axis, one both-occupied axis, two
empty axes. The orbit has size `3`. Equivalently, `opp2` is the orbit of a
cell with both ends of one axis occupied and the remaining four slots
empty. `f(opp2)=0` means a filled axis does not form. That silent
balanced-axis extra is independently motivated: it is `f_L1`'s remaining
bit on this orbit.

Write

```text
F0 = { f ∈ F_cut : f(opp2) = 0 }.
```

The `opp2` bit is one of the five free remaining bits, so

```text
|F0| = 16.
```

On the two-cube `{0,1,2}×{0,1}×{0,1}`, each unordered pair of vertices is
a 2-site seed. There are `C(12,2)=66` such seeds. Off-patch neighbors
have occupancy `0`. Each tick, every unlocked on-patch vertex evaluates
`f` on its six-neighbor occupancy tuple and locks if `f=1`. The process
is synchronous and stops at a fixed point in at most 12 ticks. Fill means
`|locks_halt|=12`. Coverage is

```text
cov(f) = |{ S : |S|=2 and f fills from S }|.
```

`f_L1(c)=1` if and only if some axis is unbalanced: `c_{+μ} ≠ c_{-μ}` for
at least one `μ ∈ {x,y,z}`. Equivalently, some discrete neighbor contrast
`n_μ = c_{+μ} − c_{-μ}` is nonzero. This is **not** Hamming parity
`|c|_1 mod 2`.

The five remaining bits of an `F_cut` map, in the displayed order
`(wt1, opp2, adj2, vertex3, mixed3)`, are the values on the three
complement-pairs and two complement-fixed orbits after empty and full are
forced to `0`. Membership in `F0` is exactly the remaining-bit condition
`opp2=0`.

**Theorem 1.** `f_L1 ∈ F0` and

```text
cov(f_L1) = 62.
```

Its remaining-bit tuple is `(1, 0, 1, 1, 1)`.

**Theorem 2.** Exhaustive enumeration of the 16 maps in `F0` gives

```text
|F0| = 16
m0 = 62
N0 = 2.
```

The two maximizers are exactly the remaining-bit tuples with
`wt1=adj2=vertex3=1`, `opp2=0`, and `mixed3` free.

**Theorem 3.** So `N0 > 1`, and that pair is not `{f_L1}`:
`f_L1` is not the unique maximizer. A displayed maximizer has
remaining-bit tuple `(1, 0, 1, 1, 0)` and `cov=62`. Displayed, not
adopted.

Do not write the ranking into Admissibility.

Not leftover-character of #6429 (that ranked all 32). Not leftover-character of #6402 (that counted 10→opp2=0 among eight fillers).

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The ten-orbit reconstruction, the 32-element F_cut, the 16-element F0, membership of f_L1, the exact integer cov(f_L1)=62, and the F0 coverage-ranking pair (m0,N0)=(62,2) are enumerated. Uniqueness of f_L1 as an F0 2-site coverage maximizer is false on this patch. No physical law is selected."
trace_class: upstream_support
target_claim_id: f_cut_opp2_silent_coverage
target_blocker_text: "whether f_L1 uniquely maximizes 2-site fill coverage among F_cut maps with f(opp2)=0"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the F0 2-site coverage ranking; any physical use must separately derive an Admissibility selector"
conditional_surface_status: "exact for F0 on this twelve-vertex patch with off-patch o=0 and all 66 two-site seeds; no Z^3-wide law and no physical selector"
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
- the complete set of 66 unordered 2-site seeds;
- the opposite-pair orbit `opp2` and the subclass `F0`.

No observational comparator, literature constant, Wilson weight, rate, or
generator is imported. No Record scalar functional appears.

Not leftover-character of #6429 (that ranked all 32). Not leftover-character of #6402 (that counted 10→opp2=0 among eight fillers).

## Exact Target And Objects

**Target.** Restrict the 32-member class `F_cut` to the independently
motivated extra `f(opp2)=0`, rank that subclass `F0` by two-site fill
coverage on the two-cube, reconfirm `f_L1 ∈ F0` with `cov(f_L1)=62`, and
decide uniqueness of `f_L1` as a maximizer inside `F0`.

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
`(wt1, opp2, adj2, vertex3, mixed3)`. The subclass `F0` freezes the
`opp2` bit at `0` and leaves the other four bits free, so `|F0|=16`.

Define

```text
f_L1(c)     = 1  iff  u(c) ≥ 1,
```

so `f_L1` has remaining-bit tuple `(1, 0, 1, 1, 1)` and lies in `F0`. The
displayed maximizer has remaining-bit tuple `(1, 0, 1, 1, 0)`: it equals
`f_L1` except that `mixed3` is off. Neither map is adopted.

A locked set `S` determines occupancies: a lattice neighbor in `S` has
occupancy `1`, and every other neighbor — including every off-patch
neighbor — has occupancy `0`. One synchronous tick replaces `S` by

```text
S ∪ { v in two-cube \ S : f(neighborhood_6(v; S)) = 1 }.
```

Then `cov(f)` is the number of 2-site seeds whose halt set has cardinality
12, `m0` is the maximum of `cov` over `F0`, and `N0` is the number of
maps in `F0` attaining `m0`.

## Theorems

**Theorem 1.** There are exactly 24 proper cube rotations and exactly 10
orbits on `{0,1}^6`. The three cuts leave `|F_cut|=32`. The unbalanced-axis
map `f_L1` is one element of `F_cut` and of `F0`: it vanishes on `opp2`.
It is not Hamming parity. On the twelve-vertex two-cube with off-patch
occupancy `0`, exhaustive run of all 66 two-site seeds gives

```text
cov(f_L1) = 62.
```

Its remaining-bit tuple is `(1, 0, 1, 1, 1)`.

**Theorem 2.** Exhaustive ranking of the 16 maps in `F0` gives

```text
|F0| = 16
m0 = 62
N0 = 2.
```

The two remaining-bit tuples that attain `m0` are

```text
(1, 0, 1, 1, 0), (1, 0, 1, 1, 1).
```

Equivalently, a map in `F0` attains `m0` if and only if
`wt1=adj2=vertex3=1`. The bit `mixed3` remains free.

**Theorem 3.** So `N0 > 1`. The map `f_L1` fills 62 of the 66 seeds and
does attain `m0`, but it is not unique as a maximizer. The displayed
second maximizer is the remaining-bit tuple `(1, 0, 1, 1, 0)`. It is
distinct from `f_L1` (they disagree on `mixed3`) and has `cov=62`.
Displayed, not adopted.

## Proof-Obligation Graph

| obligation | exact disposition |
|---|---|
| 24 proper cube rotations | signed permutations of the three axes with determinant `+1` |
| 10 orbits on `{0,1}^6` | axis-type classes `(u,b,e)` partition the 64 cells with the listed sizes |
| `|F_cut|=32` | three complement-pairs and two complement-fixed orbits remain free after the vanish cuts |
| `|F0|=16` | the `opp2` remaining bit is frozen at `0`; four free bits remain |
| `f_L1` is in `F0` | `u` is rotation- and complement-invariant, `u(empty)=u(full)=0`, and `u(opp2)=0` |
| `f_L1` is not Hamming | the two-unbalanced-axis orbit has even weight and `f_L1=1` |
| `cov(f_L1)=62` | exhaustive 66-seed fill census of `f_L1` |
| two-cube has twelve vertices | `{0,1,2}×{0,1}×{0,1}` |
| 66 two-site seeds | `C(12,2)` unordered pairs |
| off-patch occupancy `0` | declared stencil default; not a blank-block |
| `m0` and `N0` | exhaustive 16-map ranking of `cov` on `F0` |
| uniqueness of `f_L1` as maximizer | false; remaining-bit tuple `(1, 0, 1, 1, 0)` is an explicit maximizer with `cov=62` |

## Counterfactual And Mutation Table

1. Replace `f_L1` by Hamming parity: Hamming is a different `F_cut` map
   (it disagrees on the two-unbalanced-axis orbit) and is not an `F0`
   coverage maximizer.
2. Replace off-patch occupancy `0` by a blank-block: first-wave candidates
   become undefined; that is a different census.
3. Drop complement-even or the vanish-on-full cut: the class is no longer
   the 32-element `F_cut`, so `F0` is no longer this 16-element subclass.
4. Rank all 32 maps of `F_cut` by `cov`: that leftover is #6429, not the
   `F0` restriction. Global maximizers there have `opp2=1` and `cov=66`.
5. Count how many of the eight 1-site fillers vanish on `opp2`: that
   leftover is #6402, not a coverage ranking.
6. Assert that `f_L1` uniquely maximizes `cov` on `F0`: the explicit
   remaining-bit tuple `(1, 0, 1, 1, 0)` with `cov=62` refutes uniqueness.

## What This Does Not Claim

- No physical Admissibility selector and no adopted occupancy law.
- No Qubit rewrite and no `M_2(C)`-valued conditional probability.
- No `Z^3`-wide formation, rate, or generator.
- No identification of `f_L1` with Hamming parity.
- No leftover-character restatement of the 32-map coverage ranking
  (#6429), and no leftover-character restatement of the eight-filler
  `opp2`-silence count (#6402), in place of this `F0` coverage ranking.
- No blank-block or 3-site variant.

## No-Go Discipline Gate

The only negative claim is uniqueness of the maximizer: `f_L1` is not the
unique `F0` maximizer of two-site coverage on this patch. The positive
triple `(|F0|, m0, N0)=(16, 62, 2)` is an exact enumeration, not a wall.

### N1 — materially distinct routes

| Route | Exact attack | Result and authority | Marker |
|---|---|---|---|
| orbit reconstruction | Recompute the 24 rotations and the 10 axis-type orbits. | Theorem 1 and checks `thm1-twenty-four-rotations` / `thm1-ten-orbits`. | **ATTEMPTED** |
| three-cut class and `F0` | Force vanish-on-empty, vanish-on-full, `f(c)=f(1-c)`, and `f(opp2)=0`. | Theorem 1 and check `thm1-f-cut-cardinality` give `|F_cut|=32`; Theorem 2 gives `|F0|=16`. | **ATTEMPTED** |
| Hamming-as-`f_L1` | Test whether `|c|_1 mod 2` equals the unbalanced-axis predicate. | Theorem 1 and check `thm1-f-L1-not-hamming` separate the maps. | **ATTEMPTED** |
| `cov(f_L1)` and `F0` membership | Run `f_L1` from every 2-site seed and read its `opp2` bit. | Theorem 1 and check `thm1-f-L1-in-F0-cov-sixty-two` give `f_L1 ∈ F0` and `cov(f_L1) = 62`. | **ATTEMPTED** |
| `F0` coverage ranking | Score every map in `F0` by `cov`. | Theorem 2 and check `thm2-m0-n0-f0` give `m0 = 62` and `N0 = 2`. | **ATTEMPTED** |
| uniqueness of `f_L1` as maximizer | Ask whether the maximizer class is the singleton `{f_L1}`. | Theorem 3 and checks `thm3-not-unique-maximizer` / `thm3-displayed-other-maximizer`. | **ATTEMPTED** |

### N2 — wall independence and collapse

There is one negative conclusion: uniqueness of the maximizer fails. The
explicit second maximizer and the cardinality `N0=2` are two
certificates of the same non-uniqueness, so they collapse rather than
count as two walls.

| Pair | First closes second? | Second closes first? | Disposition |
|---|---:|---:|---|
| `N0=2` / displayed `(1, 0, 1, 1, 0)` | yes: a count larger than one is non-uniqueness | yes: one extra maximizer is non-uniqueness | collapse into the uniqueness failure |
| `cov(f_L1)=62` / `m0=62` | no: a score does not name the max class | no: the max does not name uniqueness | independent of uniqueness |
| static `|F0|=16` / ranking pair `(m0, N0)` | no: membership is not dynamics | no: a ranking does not replace the `opp2=0` cut | separate exact counts |
| leftover of #6429 / this ranking | no: that leftover ranked all 32 maps | no: an `F0` ranking does not replace the 32-map ranking | different object |
| leftover of #6402 / this ranking | no: that leftover counted `opp2=0` among eight fillers | no: a 16-map ranking does not replace an eight-filler silence count | different object |

Physical law selection is not a wall: this note makes no negative theorem
about the existence of a selector and simply does not claim one.

### N3 — hidden-condition scan

| Phrase or premise | Classification |
|---|---|
| “work on the twelve-vertex two-cube” | explicit patch hypothesis; not a `Z^3` theorem |
| off-patch occupancy `0` | explicit default; blank-block is a different rule |
| `F_cut` | explicit three-cut class; the other 992 covariant maps are excluded |
| `F0` | explicit `opp2=0` subclass of `F_cut` |
| all 66 two-site seeds | explicit seed class; a one-seed fill is a different residual |
| “lock” | Record permanence on this Boolean occupancy model, not a possibility-valued law |
| “cube-covariant” | invariance under the 24 proper rotations, cited to Lattice/Admissibility |
| Hamming parity | displayed mutation only |
| remaining-bit tuple `(1, 0, 1, 1, 0)` | displayed witness against uniqueness, not a selected law |

### N4 — citation-to-residual matching

| Evidence path:line | Residual attacked | Residual claimed closed | Match? |
|---|---|---|---:|
| `docs/MINIMAL_AXIOMS_2026-06-29.md:37` | ambient lattice and cubic rotations | sites are `Z^3` with proper cubic rotations | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:57` | covariant nearest-neighbor rule | covariance is the class filter, not a selector | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:79` | lock permanence | a locked site stays locked | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:83` | unreadability of absence | unlocked and off-patch sites contribute occupancy `0`, not a readout | yes |
| `scripts/f_cut_opp2_silent_coverage_2026_08_15.py:74` | 24 proper rotations | signed permutations with determinant `+1` | yes |
| `scripts/f_cut_opp2_silent_coverage_2026_08_15.py:118` | `f_L1` definition | unbalanced-axis predicate, not Hamming | yes |
| `scripts/f_cut_opp2_silent_coverage_2026_08_15.py:123` | Hamming mutation | `|c|_1 mod 2` is a different `F_cut` map | yes |
| `scripts/f_cut_opp2_silent_coverage_2026_08_15.py:49` | 66 two-site seeds | `C(12,2)` unordered pairs on the two-cube | yes |
| `scripts/f_cut_opp2_silent_coverage_2026_08_15.py:193` | `cov(f)` | number of 2-site seeds a map fills | yes |
| `scripts/f_cut_opp2_silent_coverage_2026_08_15.py:296` | ranking | exact `(m0, N0)` on `F0` | yes |
| `scripts/f_cut_opp2_silent_coverage_2026_08_15.py:127` | uniqueness | displayed maximizer, remaining bits `(1, 0, 1, 1, 0)` | yes |
| `scripts/f_cut_opp2_silent_coverage_2026_08_15.py:60` | `opp2` orbit | axis type `(0,1,2)` | yes |

No evidence citation is used to claim that a physical occupancy law, a
formation rate, or a `Z^3`-wide selector has been closed.

### N5 — rhetoric and resolution audit

| Resolution | Executed? | Narrow negative supported? |
|---|---:|---|
| per element | yes: all 64 neighbor 6-tuples | each is assigned its axis-type orbit; no broader cell class is classified |
| per site | yes: the twelve two-cube vertices | each uses the same six-direction stencil with off-patch occupancy `0` |
| per mode | yes: every map in `F0` | the ranking is this subclass on all 66 seeds; other classes are unclaimed |
| per block | yes: the pair `(m0, N0)` | uniqueness fails because `N0=2` and `f_L1` is one of two maximizers |
| lattice wide | no | no `Z^3`-wide formation or Admissibility selector is asserted |

The runner prints the same five resolution statements.

### N6 — partial closure and primitive scan

The primitive registry at `docs/audit/data/axiom_premise_nodes.json` was
checked. The only dependency used is the registered `minimal_axioms` node.
No approved primitive supplies the Boolean occupancy maps, and none is
reclassified as an import or wall.

One partial-closure mechanism is displayed rather than suppressed: `f_L1`
does lie in `F0` and does fill 62 of the 66 two-site seeds, which is the
`F0` maximum. That positive member does not make `f_L1` unique as a
maximizer and does not select it as the physical rule. The remaining
physical choice — which, if any, `F0` map is the Admissibility occupancy
predicate — stays explicit.

### N7 — hostile steelman

The strongest objection is that the two `F0` maximizers differ only on
`mixed3`, so the restricted ranking might be called a leftover decoration
of the already-known `f_L1` bit pattern, or a leftover of the 32-map
ranking that already scored `f_L1` at 62. That objection is correctly
about the static remaining-bit table and about the earlier global
ranking. It does not overturn the stated theorem: among maps in `F_cut`
that already silence `opp2`, two-site coverage selects a two-element
class that contains `f_L1` but is not the singleton `{f_L1}`. Coverage
plus silent-balanced-axis therefore does not select `f_L1` inside
`F_cut`. The displayed second maximizer already differs from `f_L1` on
`mixed3`, and that is a ranking failure for uniqueness of `f_L1` inside
`F0`, not a leftover of the 32-map ranking or of an eight-filler silence
count.

### N8 — cross-cycle echo

Repository search found nearby occupancy and covariance surfaces. They are
context, not load-bearing dependencies. The 24 rotations, 10 orbits,
`F_cut`, `F0`, and 16-map 66-seed ranking are recomputed here.

| Earlier surface | Similar issue | Mechanism considered here |
|---|---|---|
| `docs/ADMISSIBILITY_COVARIANT_Q8_CONDITIONAL_LAW_PAIR_BOUNDED_THEOREM_NOTE_2026-08-13.md` | proper-cubic covariance of a local rule | covariance is used only as the orbit filter for Boolean maps |
| `docs/PHYSICAL_SPATIAL_BLOCK_SEAM_DICHOTOMY_CYCLE728_NOTE_2026-08-04.md` | two-cell box `{0,1,2}×{0,1}×{0,1}` | the same twelve spatial vertices are the patch; the seam cost is unused |
| `docs/MINIMAL_AXIOMS_2026-06-29.md` | one covariant nearest-neighbor rule | the axiom names the contract; this note does not select the rule |

No earlier mechanism retires the `F0` 2-site coverage ranking or
restores uniqueness of `f_L1` as a maximizer inside the 16-map subclass.

No-Go Discipline disposition: **PASS** for the uniqueness failure and the
exact triple `(|F0|, m0, N0)` stated above.

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
every 2-site seed, reports `cov(f_L1) = 62`, reports `|F0| = 16`,
`m0 = 62` and `N0 = 2`, checks that `f_L1` is not Hamming parity, and
exhibits the displayed maximizer by remaining-bit tuple `(1, 0, 1, 1, 0)`
with `cov=62`. Declared audit inputs are this note and the axiom memo. No
runner cache is written.
