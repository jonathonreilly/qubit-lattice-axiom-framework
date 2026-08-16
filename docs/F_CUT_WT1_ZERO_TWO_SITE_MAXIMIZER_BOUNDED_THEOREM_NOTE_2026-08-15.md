---
claim_id: f_cut_wt1_zero_two_site_maximizer_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Among the 16 F_cut maps with remaining bit wt1=0 on the two-cube with off-patch o=0, the maximum 2-site coverage is 0, attained by 16 maps. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_wt1_zero_two_site_maximizer_2026_08_15.py
---

# Wt1-Silent Two-Site Coverage Ranking Inside The Three-Cut Class `F_cut`

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact occupancy-to-lock coverage ranking of those cube-covariant
complement-even predicates that vanish on empty and full *and* vanish on
the weight-one orbit `wt1`, on the twelve-vertex two-cube, over all
66 unordered 2-site seeds, with off-patch occupancy `0`. The
unbalanced-axis map `f_L1` is displayed only as a contrast: it has
`wt1=1` and is not a member of the subclass. No map is adopted as the
physical Admissibility rule.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_wt1_zero_two_site_maximizer_2026_08_15.py`](../scripts/f_cut_wt1_zero_two_site_maximizer_2026_08_15.py)
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
inventory (#6429). This note asks a new ranking object on a new subclass:
among the maps in `F_cut` that already vanish on `wt1`, how many of the
66 two-site seeds does each fill, and is the maximizer unique.

`wt1` is the orbit of a cell with exactly one unbalanced axis and two
empty axes. A representative is
`(c_{+x},c_{-x},c_{+y},c_{-y},c_{+z},c_{-z})=(1,0,0,0,0,0)`. The axis type
is `(u,b,e)=(1,0,2)`. The orbit has size `6`. Equivalently, `wt1` is the
orbit of a cell with exactly one occupied neighbor. `f(wt1)=0` means a
single occupied neighbor does not form.

Write

```text
F_W0 = { f ∈ F_cut : f(wt1) = 0 }.
```

The `wt1` bit is one of the five free remaining bits, so

```text
|F_W0| = 16.
```

On the two-cube `{0,1,2}×{0,1}×{0,1}`, each unordered pair of vertices is
a 2-site seed. There are `C(12,2)=66` such seeds. Off-patch neighbors
have occupancy `0`. Each tick, every unlocked on-patch vertex evaluates
`f` on its six-neighbor occupancy tuple and locks if `f=1`. The process
is synchronous and stops at a fixed point in at most 12 ticks. Fill means
`|locks_halt|=12`. Coverage is

```text
cov2(f) = |{ S : |S|=2 and f fills from S }|.
```

`f_L1(c)=1` if and only if some axis is unbalanced: `c_{+μ} ≠ c_{-μ}` for
at least one `μ ∈ {x,y,z}`. Equivalently, some discrete neighbor contrast
`n_μ = c_{+μ} − c_{-μ}` is nonzero. This is **not** Hamming parity
`|c|_1 mod 2`. f_L1 has remaining-bit tuple `(1, 0, 1, 1, 1)`, so
`wt1=1` and `f_L1 ∉ F_W0`.

The five remaining bits of an `F_cut` map, in the displayed order
`(wt1, opp2, adj2, vertex3, mixed3)`, are the values on the three
complement-pairs and two complement-fixed orbits after empty and full are
forced to `0`. Membership in `F_W0` is exactly the remaining-bit condition
`wt1=0`.

**Theorem 1.** Exhaustive ranking of the 16 maps in `F_W0` gives

```text
|F_W0| = 16
m2 = 0
N_max = 16.
```

Every map in `F_W0` fills none of the 66 two-site seeds. The maximum
halt size on this subclass, even for the remaining-bit tuple
`(0, 1, 1, 1, 1)` that turns every other free bit on, is `4`.

**Theorem 2.** So N_max is not 1. There is no unique maximizer tuple.
Two-site coverage does not select a unique member inside `F_W0`.
The same fact in the claim voice: two-site coverage does not select a unique member.

**Theorem 3.** Display the pair `(m2, N_max)=(0, 16)` and the
classification: every remaining-bit tuple with `wt1=0` attains `m2`.
Displayed, not adopted. Do not re-list Max(2) of the full 32.

Do not write the ranking into Admissibility.

Not leftover-character of #6429 (that ranked all 32). This is a new
selector question on a new subclass.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The ten-orbit reconstruction, the 32-element F_cut, the 16-element F_W0, the exact integer pair (m2,N_max)=(0,16), and the uniqueness failure N_max≠1 are enumerated. No physical law is selected."
trace_class: upstream_support
target_claim_id: f_cut_wt1_zero_two_site_maximizer
target_blocker_text: "whether 2-site coverage selects a unique member inside the unnamed wt1=0 half of F_cut"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the F_W0 2-site coverage ranking; any physical use must separately derive an Admissibility selector"
conditional_surface_status: "exact for F_W0 on this twelve-vertex patch with off-patch o=0 and all 66 two-site seeds; no Z^3-wide law and no physical selector"
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
- the weight-one orbit `wt1` and the subclass `F_W0`.

No observational comparator, literature constant, Wilson weight, rate, or
generator is imported. No Record scalar functional appears.

Not leftover-character of #6429 (that ranked all 32). Do not re-list Max(2)
of the full 32.

## Exact Target And Objects

**Target.** Restrict the 32-member class `F_cut` to the independently
motivated extra `f(wt1)=0`, rank that new subclass `F_W0` by two-site fill
coverage on the two-cube, report the pair `(m2, N_max)`, and decide
whether `N_max=1`.

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
`(wt1, opp2, adj2, vertex3, mixed3)`. The subclass `F_W0` freezes the
`wt1` bit at `0` and leaves the other four bits free, so `|F_W0|=16`.

Define

```text
f_L1(c)     = 1  iff  u(c) ≥ 1,
```

so `f_L1` has remaining-bit tuple `(1, 0, 1, 1, 1)` and does not lie in
`F_W0`. It is displayed only as the contrast that the unbalanced-axis
predicate uses `wt1=1`. It is not adopted.

A locked set `S` determines occupancies: a lattice neighbor in `S` has
occupancy `1`, and every other neighbor — including every off-patch
neighbor — has occupancy `0`. One synchronous tick replaces `S` by

```text
S ∪ { v in two-cube \ S : f(neighborhood_6(v; S)) = 1 }.
```

Then `cov2(f)` is the number of 2-site seeds whose halt set has
cardinality 12, `m2` is the maximum of `cov2` over `F_W0`, and `N_max`
is the number of maps in `F_W0` attaining `m2`.

From a 2-site seed, a third vertex is adjacent to at most two locked
sites. The first wave can therefore use only `empty` (never forms),
`wt1` (one locked neighbor), `opp2` (opposite pair; long-axis seeds),
or `adj2` (two non-opposite neighbors; face-diagonal seeds). With
`f(wt1)=0`, long-axis seeds halt at size `3` when `opp2=1` and
face-diagonal seeds halt at size `4` when `adj2=1`. Neither is a fill.

## Theorems

**Theorem 1.** There are exactly 24 proper cube rotations and exactly 10
orbits on `{0,1}^6`. The three cuts leave `|F_cut|=32`. The unbalanced-axis
map `f_L1` is one element of `F_cut` and is not Hamming parity. It is not
an element of `F_W0`. On the twelve-vertex two-cube with off-patch
occupancy `0`, exhaustive ranking of all 16 maps in `F_W0` on all 66
two-site seeds gives

```text
|F_W0| = 16
m2 = 0
N_max = 16.
```

**Theorem 2.** So N_max is not 1. There is no unique remaining-bit
tuple attaining `m2`. Two-site coverage does not select a unique member
inside the unnamed `wt1=0` half.

**Theorem 3.** Display: every remaining-bit tuple with `wt1=0` attains
`m2 = 0`. A displayed certificate is that the generous tuple
`(0, 1, 1, 1, 1)` has maximum halt size `4` on the 66 seeds. Displayed,
not adopted. Do not re-list Max(2) of the full 32.

## Proof-Obligation Graph

| obligation | exact disposition |
|---|---|
| 24 proper cube rotations | signed permutations of the three axes with determinant `+1` |
| 10 orbits on `{0,1}^6` | axis-type classes `(u,b,e)` partition the 64 cells with the listed sizes |
| `|F_cut|=32` | three complement-pairs and two complement-fixed orbits remain free after the vanish cuts |
| `|F_W0|=16` | the `wt1` remaining bit is frozen at `0`; four free bits remain |
| `f_L1` is not in `F_W0` | remaining-bit tuple `(1, 0, 1, 1, 1)` has `wt1=1` |
| `f_L1` is not Hamming | the two-unbalanced-axis orbit has even weight and `f_L1=1` |
| two-cube has twelve vertices | `{0,1,2}×{0,1}×{0,1}` |
| 66 two-site seeds | `C(12,2)` unordered pairs |
| off-patch occupancy `0` | declared stencil default; not a blank-block |
| `m2` and `N_max` | exhaustive 16-map ranking of `cov2` on `F_W0` |
| uniqueness of a maximizer | false; `N_max = 16` and every `wt1=0` tuple attains `m2 = 0` |
| no 2-site fill without `wt1` | even `(0, 1, 1, 1, 1)` has maximum halt size `4` |

## Counterfactual And Mutation Table

1. Replace `f_L1` by Hamming parity: Hamming is a different `F_cut` map
   (it disagrees on the two-unbalanced-axis orbit). Hamming is not used
   as a member of `F_W0`.
2. Replace off-patch occupancy `0` by a blank-block: first-wave candidates
   become undefined; that is a different census.
3. Drop complement-even or the vanish-on-full cut: the class is no longer
   the 32-element `F_cut`, so `F_W0` is no longer this 16-element subclass.
4. Rank all 32 maps of `F_cut` by `cov2`: that leftover is #6429, not the
   `F_W0` restriction. Do not re-list Max(2) of the full 32.
5. Unfreeze `wt1`: the 16 maps with `wt1=1` are a different subclass and
   are the only maps that can fire a one-neighbor first wave.
6. Assert that two-site coverage selects a unique member of `F_W0`: the
   exact count `N_max = 16` refutes uniqueness.

## What This Does Not Claim

- No physical Admissibility selector and no adopted occupancy law.
- No Qubit rewrite and no `M_2(C)`-valued conditional probability.
- No `Z^3`-wide formation, rate, or generator.
- No identification of `f_L1` with Hamming parity.
- No leftover-character restatement of the 32-map coverage ranking
  (#6429) in place of this `F_W0` coverage ranking.
- No re-list of Max(2) of the full 32.
- No blank-block or 3-site variant.

## No-Go Discipline Gate

The only negative claim is uniqueness of the maximizer: two-site
coverage does not select a unique member of `F_W0`. The positive
triple `(|F_W0|, m2, N_max)=(16, 0, 16)` is an exact enumeration, not
a wall.

### N1 — materially distinct routes

| Route | Exact attack | Result and authority | Marker |
|---|---|---|---|
| orbit reconstruction | Recompute the 24 rotations and the 10 axis-type orbits. | Theorem 1 and checks `thm1-twenty-four-rotations` / `thm1-ten-orbits`. | **ATTEMPTED** |
| three-cut class and `F_W0` | Force vanish-on-empty, vanish-on-full, `f(c)=f(1-c)`, and `f(wt1)=0`. | Theorem 1 and check `thm1-f-cut-cardinality` give `|F_cut|=32`; Theorem 1 gives `|F_W0|=16`. | **ATTEMPTED** |
| Hamming-as-`f_L1` | Test whether `|c|_1 mod 2` equals the unbalanced-axis predicate. | Theorem 1 and check `thm1-f-L1-not-hamming` separate the maps. | **ATTEMPTED** |
| `f_L1` outside `F_W0` | Read the `wt1` remaining bit of `f_L1`. | Remaining-bit tuple `(1, 0, 1, 1, 1)` has `wt1=1`. | **ATTEMPTED** |
| `F_W0` coverage ranking | Score every map in `F_W0` by `cov2`. | Theorem 1 and check `thm1-m2-n-max` give `m2 = 0` and `N_max = 16`. | **ATTEMPTED** |
| uniqueness of a maximizer | Ask whether `N_max=1`. | Theorem 2 and checks `thm2-not-unique` / `thm3-all-sixteen-attain-m2`. | **ATTEMPTED** |

### N2 — wall independence and collapse

There is one negative conclusion: uniqueness of the maximizer fails. The
count `N_max=16` and the statement that every `wt1=0` tuple attains
`m2` are two certificates of the same non-uniqueness, so they collapse
rather than count as two walls.

| Pair | First closes second? | Second closes first? | Disposition |
|---|---:|---:|---|
| `N_max=16` / all sixteen attain `m2` | yes: a count larger than one is non-uniqueness | yes: a full-class tie is non-uniqueness | collapse into the uniqueness failure |
| `m2=0` / max halt size `4` | no: a coverage score does not name the halt histogram | no: a halt bound does not name uniqueness | independent of uniqueness |
| static `|F_W0|=16` / ranking pair `(m2, N_max)` | no: membership is not dynamics | no: a ranking does not replace the `wt1=0` cut | separate exact counts |
| leftover of #6429 / this ranking | no: that leftover ranked all 32 maps | no: an `F_W0` ranking does not replace the 32-map ranking | different object |

Physical law selection is not a wall: this note makes no negative theorem
about the existence of a selector and simply does not claim one.

### N3 — hidden-condition scan

| Phrase or premise | Classification |
|---|---|
| “work on the twelve-vertex two-cube” | explicit patch hypothesis; not a `Z^3` theorem |
| off-patch occupancy `0` | explicit default; blank-block is a different rule |
| `F_cut` | explicit three-cut class; the other 992 covariant maps are excluded |
| `F_W0` | explicit `wt1=0` subclass of `F_cut` |
| all 66 two-site seeds | explicit seed class; a one-seed fill is a different residual |
| “lock” | Record permanence on this Boolean occupancy model, not a possibility-valued law |
| “cube-covariant” | invariance under the 24 proper rotations, cited to Lattice/Admissibility |
| Hamming parity | displayed mutation only |
| remaining-bit tuple `(0, 1, 1, 1, 1)` | displayed halt-size certificate, not a selected law |

### N4 — citation-to-residual matching

| Evidence path:line | Residual attacked | Residual claimed closed | Match? |
|---|---|---|---:|
| `docs/MINIMAL_AXIOMS_2026-06-29.md:37` | ambient lattice and cubic rotations | sites are `Z^3` with proper cubic rotations | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:57` | covariant nearest-neighbor rule | covariance is the class filter, not a selector | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:79` | lock permanence | a locked site stays locked | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:83` | unreadability of absence | unlocked and off-patch sites contribute occupancy `0`, not a readout | yes |
| `scripts/f_cut_wt1_zero_two_site_maximizer_2026_08_15.py:74` | 24 proper rotations | signed permutations with determinant `+1` | yes |
| `scripts/f_cut_wt1_zero_two_site_maximizer_2026_08_15.py:118` | `f_L1` definition | unbalanced-axis predicate, not Hamming | yes |
| `scripts/f_cut_wt1_zero_two_site_maximizer_2026_08_15.py:123` | Hamming mutation | `|c|_1 mod 2` is a different `F_cut` map | yes |
| `scripts/f_cut_wt1_zero_two_site_maximizer_2026_08_15.py:49` | 66 two-site seeds | `C(12,2)` unordered pairs on the two-cube | yes |
| `scripts/f_cut_wt1_zero_two_site_maximizer_2026_08_15.py:187` | `cov2(f)` | number of 2-site seeds a map fills | yes |
| `scripts/f_cut_wt1_zero_two_site_maximizer_2026_08_15.py:351` | ranking | exact `(m2, N_max)` on `F_W0` | yes |
| `scripts/f_cut_wt1_zero_two_site_maximizer_2026_08_15.py:60` | `wt1` orbit | axis type `(1,0,2)` | yes |
| `scripts/f_cut_wt1_zero_two_site_maximizer_2026_08_15.py:173` | halt size | no `F_W0` 2-site seed fills | yes |

No evidence citation is used to claim that a physical occupancy law, a
formation rate, or a `Z^3`-wide selector has been closed.

### N5 — rhetoric and resolution audit

| Resolution | Executed? | Narrow negative supported? |
|---|---:|---|
| per element | yes: all 64 neighbor 6-tuples | each is assigned its axis-type orbit; no broader cell class is classified |
| per site | yes: the twelve two-cube vertices | each uses the same six-direction stencil with off-patch occupancy `0` |
| per mode | yes: every map in `F_W0` | the ranking is this subclass on all 66 seeds; other classes are unclaimed |
| per block | yes: the pair `(m2, N_max)` | uniqueness fails because `N_max=16` and every `wt1=0` map attains `m2` |
| lattice wide | no | no `Z^3`-wide formation or Admissibility selector is asserted |

The runner prints the same five resolution statements.

### N6 — partial closure and primitive scan

The primitive registry at `docs/audit/data/axiom_premise_nodes.json` was
checked. The only dependency used is the registered `minimal_axioms` node.
No approved primitive supplies the Boolean occupancy maps, and none is
reclassified as an import or wall.

One partial-closure mechanism is displayed rather than suppressed:
`wt1=0` is an independently named remaining bit, and the 16-map subclass
it cuts out is closed under the three displayed cuts. That static cut
does not make two-site coverage a selector inside the subclass. The
remaining physical choice — which, if any, `F_cut` map is the
Admissibility occupancy predicate — stays explicit.

### N7 — hostile steelman

The strongest objection is that `m2=0` for every `wt1=0` map is “obvious”
once one-neighbor formation is silenced, so the ranking might be called
a leftover decoration of the already-known 32-map ranking, or a restatement
of #6476 that no `wt1=0` map lies in Max(2) of all 32. That objection is
correctly about first-wave local types. It does not overturn the stated
theorem: among maps in `F_cut` that already silence `wt1`, two-site
coverage selects the entire 16-element class equally at `cov2=0`. Coverage
therefore does not select a member inside the unnamed `wt1=0` half. The
32-map maximizer set is a different object and is not re-listed here.

### N8 — cross-cycle echo

Repository search found nearby occupancy and covariance surfaces. They are
context, not load-bearing dependencies. The 24 rotations, 10 orbits,
`F_cut`, `F_W0`, and 16-map 66-seed ranking are recomputed here.

| Earlier surface | Similar issue | Mechanism considered here |
|---|---|---|
| `docs/ADMISSIBILITY_COVARIANT_Q8_CONDITIONAL_LAW_PAIR_BOUNDED_THEOREM_NOTE_2026-08-13.md` | proper-cubic covariance of a local rule | covariance is used only as the orbit filter for Boolean maps |
| `docs/PHYSICAL_SPATIAL_BLOCK_SEAM_DICHOTOMY_CYCLE728_NOTE_2026-08-04.md` | two-cell box `{0,1,2}×{0,1}×{0,1}` | the same twelve spatial vertices are the patch; the seam cost is unused |
| `docs/MINIMAL_AXIOMS_2026-06-29.md` | one covariant nearest-neighbor rule | the axiom names the contract; this note does not select the rule |

No earlier mechanism retires the `F_W0` 2-site coverage ranking or
restores uniqueness of a maximizer inside the 16-map subclass.

No-Go Discipline disposition: **PASS** for the uniqueness failure and the
exact triple `(|F_W0|, m2, N_max)` stated above.

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
`F_cut`, restricts to `F_W0`, evaluates all 16 maps on the two-cube from
every 2-site seed, reports `|F_W0| = 16`, `m2 = 0` and `N_max = 16`,
checks that `f_L1` is not Hamming parity and is not in `F_W0`, and
exhibits that every `wt1=0` remaining-bit tuple attains `m2`. Declared
audit inputs are this note and the axiom memo. No runner cache is written.
