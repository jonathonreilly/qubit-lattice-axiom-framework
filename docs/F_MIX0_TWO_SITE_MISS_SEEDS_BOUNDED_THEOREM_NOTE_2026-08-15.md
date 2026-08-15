---
claim_id: f_mix0_two_site_miss_seeds_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "The four two-site seeds from which the F_cut map (1,0,1,1,0) does not fill are listed, and they are the same four that f_L1 misses. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_mix0_two_site_miss_seeds_2026_08_15.py
---

# The Four Two-Site Seeds `f_mix0` Does Not Fill

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact two-site fill coverage of the `F_cut` rival `f_mix0` with
remaining bits `(1,0,1,1,0)` on the twelve-vertex two-cube with off-patch
occupancy `0`. The four miss seeds and their halt histories are listed
and compared to the four seeds `f_L1` misses. The map is displayed, not
adopted as the physical Admissibility rule.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/f_mix0_two_site_miss_seeds_2026_08_15.py`](../scripts/f_mix0_two_site_miss_seeds_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

The 24 proper cube rotations act on neighbor 6-tuples in `{0,1}^6` and
partition those 64 cells into 10 orbits. Cube-covariant predicates are the
`{0,1}`-assignments to those orbits. The three displayed cuts

1. vanish on empty: `f(empty)=0`,
2. vanish on full: `f(full)=0`,
3. complement-even: `f(c)=f(1-c)`

leave five free bits, so `|F_cut|=32`. On the two-cube
`{0,1,2}×{0,1}×{0,1}`, a locked seed starts the dynamics. Off-patch neighbors
have occupancy `0`. Each tick, every unlocked on-patch vertex evaluates
`f` on its six-neighbor occupancy tuple and locks if `f=1`. Fill means
`|locks_halt|=12`. There are `C(12,2)=66` two-site seeds. Coverage
`cov(f)` is the number of those seeds from which `f` fills.

The displayed `F_cut` rival is the remaining-bit tuple

```text
(wt1, opp2, adj2, vertex3, mixed3) = (1, 0, 1, 1, 0)
```

with complements forced. Call that map `f_mix0`. It is L1 with
`mixed3=0`. It fills from 1-site, from the face-diagonal 2-site
`{(0,0,0),(1,1,0)}`, and from opposite-corner `S*={(0,0,0),(2,1,1)}`
like L1 (#6415/#6424). Those fills are leftover-character of
#6415/#6424. They are not the residual of this note.

Among `F_cut` maps with `opp2=0`, both `f_mix0` and `f_L1` attain
`cov=62` (#6433/#6434). #6434 only named that pair. This note asks
whether they miss the *same* four two-site seeds. If they do, `mixed3`
does not change the 2-site fill set inside that pair. If they do not,
`mixed3` is a 2-site selector between the two `opp2=0` maximizers.
Not leftover-character of #6434. Not leftover-character of the
`l1miss2` surface: that surface listed L1's four misses on a different
map.

`f_L1(c)=1` if and only if some axis is unbalanced: `c_{+μ} ≠ c_{-μ}` for
at least one `μ ∈ {x,y,z}`. Equivalently, some discrete neighbor contrast
`n_μ = c_{+μ} − c_{-μ}` is nonzero. This is **not** Hamming parity
`|c|_1 mod 2`. `f_L1` is the 10-orbit reading `n ≠ 0`, not Hamming.

**Theorem 1.** `cov(f_mix0)=62`. `f_mix0` fills the face-diagonal seed
and opposite-corner `S*`.

**Theorem 2.** The four miss seeds, in lex order, with halt lock-count
and lock history, are

```text
((0, 0, 0), (2, 0, 0))  |locks_halt|=8  T=2  history=(2, 6, 8)
((0, 0, 1), (2, 0, 1))  |locks_halt|=8  T=2  history=(2, 6, 8)
((0, 1, 0), (2, 1, 0))  |locks_halt|=8  T=2  history=(2, 6, 8)
((0, 1, 1), (2, 1, 1))  |locks_halt|=8  T=2  history=(2, 6, 8)
```

**Theorem 3.** These are the same four two-site seeds that `f_L1`
misses, recomputed in the same run, each with the same history
`(2, 6, 8)`. Displayed, not adopted. `mixed3` does not change the
2-site fill set between these two `opp2=0` maximizers.

Do not write f_mix0 into Admissibility.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "On the twelve-vertex two-cube with off-patch o=0, the F_cut rival f_mix0 with remaining bits (1,0,1,1,0) is reconstructed and run from all 66 two-site seeds. The four misses and their halt histories are listed and compared to f_L1. The map is displayed, not written into Admissibility."
trace_class: upstream_support
target_claim_id: f_mix0_two_site_miss_seeds
target_blocker_text: "whether f_mix0 and f_L1 miss the same four two-site seeds"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the two-site miss-set comparison; any physical use must separately derive an Admissibility selector"
conditional_surface_status: "exact for f_mix0 and f_L1 on this twelve-vertex patch with off-patch o=0 and the 66 two-site seeds; no Z^3-wide law and no physical selector"
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
- the 66 two-site seeds, listed in lex order of sorted site pairs;
- the face-diagonal seed `{(0,0,0),(1,1,0)}` and opposite-corner
  `S*={(0,0,0),(2,1,1)}`;
- the named remaining bits `wt1`, `opp2`, `adj2`, `vertex3`, `mixed3`;
- the displayed map `f_mix0` with tuple `(1,0,1,1,0)`.

No observational comparator, literature constant, Wilson weight, rate, or
generator is imported. No Record scalar functional appears.

Not leftover-character of #6434 (that only named the `cov=62` pair).
Not leftover-character of the `l1miss2` surface (that listed L1's four
misses on a different map). This note is the four-set of `f_mix0` and
the same-four comparison.

## Exact Target And Objects

**Target.** Run `f_mix0` from every two-site seed on the two-cube with
off-patch occupancy `0`. Reconfirm `cov=62` and the face-diagonal /
`S*` fills. List the four miss seeds in lex order with halt histories.
Recompute L1's four misses in the same run and state whether the
four-sets are equal.

Write a neighbor configuration as `c ∈ {0,1}^6`. A proper cube rotation `R`
acts by `(R·c)(d) = c(R^{-1}d)` on the six face directions `d`. A map
`f:{0,1}^6 → {0,1}` is cube-covariant when `f(R·c)=f(c)` for every such `R`.
Equivalently, `f` is constant on each orbit.

The axis type of a 6-tuple `c` is the triple `(u,b,e)` with `u+b+e=3`,
where `u` is the number of axes with `c_{+} ≠ c_{-}`, `b` the number with
`(c_{+},c_{-})=(1,1)`, and `e` the number with `(c_{+},c_{-})=(0,0)`. The
ten axis-type classes are exactly the ten orbits. Complement sends
`(u,b,e)` to `(u,e,b)`.

| `(u,b,e)` | name | orbit size | complement image |
|---|---|---:|---|
| `(0,0,3)` | empty | 1 | `(0,3,0)` full |
| `(0,3,0)` | full | 1 | `(0,0,3)` empty |
| `(0,1,2)` | `opp2` | 3 | `(0,2,1)` `opp4` |
| `(0,2,1)` | `opp4` | 3 | `(0,1,2)` `opp2` |
| `(1,0,2)` | `wt1` | 6 | `(1,2,0)` `wt5` |
| `(1,2,0)` | `wt5` | 6 | `(1,0,2)` `wt1` |
| `(2,0,1)` | `adj2` | 12 | `(2,1,0)` `adj4` |
| `(2,1,0)` | `adj4` | 12 | `(2,0,1)` `adj2` |
| `(1,1,1)` | `mixed3` | 12 | `(1,1,1)` |
| `(3,0,0)` | `vertex3` | 8 | `(3,0,0)` |

`F_cut` is the class of cube-covariant maps with `f(empty)=f(full)=0` and
`f(c)=f(1-c)`. The empty/full pair is forced to `0`. The remaining free
data are three complement-pair bits and two complement-fixed orbit bits,
so `|F_cut|=32`.

A locked set `L` determines occupancies: a lattice neighbor in `L` has
occupancy `1`, and every other neighbor — including every off-patch
neighbor — has occupancy `0`. One synchronous tick replaces `L` by

```text
L ∪ { v in two-cube \ L : f(neighborhood_6(v; L)) = 1 }.
```

The eight 1-site fillers are the maps in `F_cut` whose halt set from seed
`(0,0,0)` has cardinality 12. One of those eight is the remaining-bit
tuple `(1,0,1,1,0)`. Complements are `wt5=1`, `adj4=1`, `opp4=0`, and
`vertex3=1` is already listed. Support of that map is 44.

Define

```text
f_L1(c) = 1  iff  u(c) ≥ 1.
```

Its remaining-bit tuple is `(1,0,1,1,1)` and its support is 56. It is not
`f_mix0`: the maps differ only on the complement-fixed orbit `mixed3`.

A two-site seed is any unordered pair of distinct two-cube vertices.
Lex order is the dictionary order of the sorted pair of site triples.

Do not write `f_mix0` into Admissibility.

## Theorems

**Theorem 1.** There are exactly 24 proper cube rotations and exactly 10
orbits on `{0,1}^6`. The three cuts leave `|F_cut|=32`. The unbalanced-axis
map `f_L1` is not Hamming parity. The remaining-bit map `f_mix0` with
tuple `(1,0,1,1,0)` lies in `F_cut`. On the twelve-vertex two-cube with
off-patch occupancy `0` it fills 62 of the 66 two-site seeds. It fills
the face-diagonal seed `{(0,0,0),(1,1,0)}` with history `(2, 7, 11, 12)`
and opposite-corner `S*={(0,0,0),(2,1,1)}` with history `(2, 8, 12)`.

**Theorem 2.** The four two-site seeds from which `f_mix0` does not fill,
listed in lex order, each halt at eight locks:

```text
((0, 0, 0), (2, 0, 0))  |locks_halt|=8  T=2  history=(2, 6, 8)
((0, 0, 1), (2, 0, 1))  |locks_halt|=8  T=2  history=(2, 6, 8)
((0, 1, 0), (2, 1, 0))  |locks_halt|=8  T=2  history=(2, 6, 8)
((0, 1, 1), (2, 1, 1))  |locks_halt|=8  T=2  history=(2, 6, 8)
```

Each seed is a long-axis pair at fixed `(y,z)`: the two sites differ
only by `Δx=2`.

**Theorem 3.** Recomputing `f_L1` on the same 66 seeds yields the same
four misses, in the same lex order, each with history `(2, 6, 8)`. The
four-sets are equal. Displayed, not adopted. `f_mix0` is not an
Admissibility clause.

## Proof-Obligation Graph

| obligation | exact disposition |
|---|---|
| 24 proper cube rotations | signed permutations of the three axes with determinant `+1` |
| 10 orbits on `{0,1}^6` | axis-type classes `(u,b,e)` partition the 64 cells with the listed sizes |
| `|F_cut|=32` | three complement-pairs and two complement-fixed orbits remain free after the vanish cuts |
| `f_L1` is not Hamming | the two-unbalanced-axis orbit `adj2` has even weight and `f_L1=1` |
| `f_mix0` membership | remaining-bit tuple `(1,0,1,1,0)` is cube-covariant, complement-even, and vanishes on empty/full |
| `cov(f_mix0)=62` | 62 of 66 two-site seeds halt at 12 locks |
| face-diagonal and `S*` fills | histories `(2, 7, 11, 12)` and `(2, 8, 12)` |
| four miss seeds | lex list above, each history `(2, 6, 8)` |
| same four as `f_L1` | L1's recomputed miss set equals the `f_mix0` four-set |
| physical Admissibility selection | open and not claimed; `f_mix0` is not written in |

Every leaf needed for the stated miss-set comparison is discharged. No
`Z^3`-wide formation law is claimed.

## Mutations

1. Replace `f_L1` by Hamming `|c|_1 mod 2`: the remaining-bit tuple changes
   and Hamming does not fill from the face-diagonal seed.
2. Flip `mixed3` from `0` to `1`: the map becomes `f_L1`, not `f_mix0`;
   the two-site miss set happens to stay the same.
3. Replace the census by the single seeds of #6415/#6424: those are the
   face-diagonal and `S*` fills, leftover-character of those surfaces.
4. Replace off-patch occupancy `0` by a blank-block: first-wave candidates
   become undefined; that is a different census.
5. Assert that `f_mix0` misses a different four than `f_L1`: the
   recomputed sets are equal.
6. Treat #6434 as already listing the four seeds: that surface named the
   `cov=62` pair and did not list the misses.

## What This Does Not Claim

- No physical Admissibility selector and no adopted occupancy law.
- No Qubit rewrite and no `M_2(C)`-valued conditional probability.
- No `Z^3`-wide formation, rate, or generator.
- No identification of `f_L1` with Hamming parity.
- No leftover-character restatement of the 1-site / face-diagonal / `S*`
  fills of `f_mix0` (#6415/#6424) in place of this miss-set list.
- No leftover-character restatement of #6434 (the `cov=62` pair) in
  place of the four seeds.
- No leftover-character restatement of the `l1miss2` L1 miss list in
  place of the `f_mix0` census.
- No blank-block variant and no adoption of a miss seed as canonical.
- No axiom edit: `f_mix0` is displayed, not written into Admissibility.

## No-Go Discipline Gate

The only negative claim is that Hamming is not `f_L1`. The four-set
equality is an exact pair of censuses, not a wall, and it is not an
Admissibility clause.

### N1 — materially distinct routes

| Route | Exact attack | Result and authority | Marker |
|---|---|---|---|
| orbit reconstruction | Recompute the 24 rotations and the 10 axis-type orbits. | Theorem 1 and checks `thm1-twenty-four-rotations` / `thm1-ten-orbits`. | **ATTEMPTED** |
| `f_mix0` coverage | Run `f_mix0` from all 66 two-site seeds. | Theorem 1 and check `thm1-mix0-in-f-cut-cov-62` give `cov=62`. | **ATTEMPTED** |
| face-diagonal and `S*` | Run `f_mix0` from those two displayed seeds. | Theorem 1 and check `thm1-face-diagonal-and-sstar-fill`. | **ATTEMPTED** |
| Hamming-as-`f_L1` | Test whether `|c|_1 mod 2` equals the unbalanced-axis predicate. | Theorem 1 and check `thm1-f-L1-not-hamming` separate the maps. | **ATTEMPTED** |
| four miss seeds | Collect the seeds with `|locks_halt|≠12` in lex order. | Theorem 2 and checks `thm2-four-miss-seeds-lex` / `thm2-halt-histories`. | **ATTEMPTED** |
| same-four comparison | Recompute L1's four misses in the same run. | Theorem 3 and check `thm3-same-four-as-l1`. | **ATTEMPTED** |

### N2 — wall independence and collapse

There is one negative conclusion: Hamming is not `f_L1`. The four-set
equality is a positive exact comparison.

| Pair | First closes second? | Second closes first? | Disposition |
|---|---:|---:|---|
| `cov(f_mix0)=62` / four miss seeds | no: a count does not name the seeds | no: naming four misses does not prove the coverage of the other 62 | independent positive runs |
| `f_mix0` misses / `f_L1` misses | no: one map's miss set does not classify the other | no: L1's four do not prove `f_mix0` misses those same four | independent censuses, compared after both run |
| face-diagonal fill / four misses | no: filling one seed does not list the misses | no: the miss list does not prove the face-diagonal fill | separate seeds |

Physical law selection is not a wall: this note makes no negative theorem
about the existence of a selector and simply does not claim one.

### N3 — hidden-condition scan

| Phrase or premise | Classification |
|---|---|
| “work on the twelve-vertex two-cube” | explicit patch hypothesis; not a `Z^3` theorem |
| off-patch occupancy `0` | explicit default; blank-block is a different rule |
| 66 two-site seeds | explicit domain; not the 1-site or 3-site censuses |
| remaining bits `(1,0,1,1,0)` | explicit `F_cut` rival; L1 is a different tuple |
| “lock” | Record permanence on this Boolean occupancy model, not a possibility-valued law |
| “cube-covariant” | invariance under the 24 proper rotations, cited to Lattice/Admissibility |
| Hamming parity | displayed mutation only |
| same four as `f_L1` | displayed comparison, not an Admissibility clause |

### N4 — citation-to-residual matching

| Evidence path:line | Residual attacked | Residual claimed closed | Match? |
|---|---|---|---:|
| `docs/MINIMAL_AXIOMS_2026-06-29.md:37` | ambient lattice and cubic rotations | sites are `Z^3` with proper cubic rotations | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:57` | covariant nearest-neighbor rule | covariance is the class filter, not a selector | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:79` | lock permanence | a locked site stays locked | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:83` | unreadability of absence | unlocked and off-patch sites contribute occupancy `0`, not a readout | yes |
| `scripts/f_mix0_two_site_miss_seeds_2026_08_15.py:76` | 24 proper rotations | signed permutations with determinant `+1` | yes |
| `scripts/f_mix0_two_site_miss_seeds_2026_08_15.py:120` | `f_L1` definition | unbalanced-axis predicate, not Hamming | yes |
| `scripts/f_mix0_two_site_miss_seeds_2026_08_15.py:125` | Hamming mutation | `|c|_1 mod 2` is a different map | yes |
| `scripts/f_mix0_two_site_miss_seeds_2026_08_15.py:64` | `f_mix0` tuple | remaining bits `(1,0,1,1,0)` | yes |
| `scripts/f_mix0_two_site_miss_seeds_2026_08_15.py:279` | 66 two-site seeds | combinations of the twelve vertices, lex-sorted | yes |
| `scripts/f_mix0_two_site_miss_seeds_2026_08_15.py:288` | miss census | seeds whose halt set is not the full two-cube | yes |
| `scripts/f_mix0_two_site_miss_seeds_2026_08_15.py:52` | face-diagonal seed | `{(0,0,0),(1,1,0)}` | yes |
| `scripts/f_mix0_two_site_miss_seeds_2026_08_15.py:53` | opposite-corner `S*` | `{(0,0,0),(2,1,1)}` | yes |
| `scripts/f_mix0_two_site_miss_seeds_2026_08_15.py:175` | lock dynamics | synchronous ticks from a supplied seed to a fixed point | yes |

No evidence citation is used to claim that a physical occupancy law, a
formation rate, or a `Z^3`-wide selector has been closed.

### N5 — rhetoric and resolution audit

| Resolution | Executed? | Narrow negative supported? |
|---|---:|---|
| per element | yes: all 64 neighbor 6-tuples | each is assigned its axis-type orbit; no broader cell class is classified |
| per site | yes: the twelve two-cube vertices | each uses the same six-direction stencil with off-patch occupancy `0` |
| per mode | yes: `f_mix0` and `f_L1` from every two-site seed | the miss sets are this pair of maps on this seed domain |
| per block | yes: the pair `(miss four-set, history)` | each miss has `|locks_halt|=8` with history `(2, 6, 8)` |
| lattice wide | no | no `Z^3`-wide formation or Admissibility selector is asserted |

The runner prints the same five resolution statements.

### N6 — partial closure and primitive scan

The primitive registry at `docs/audit/data/axiom_premise_nodes.json` was
checked. The only dependency used is the registered `minimal_axioms` node.
No approved primitive supplies the Boolean occupancy maps, and none is
reclassified as an import or wall.

One partial-closure mechanism is displayed rather than suppressed: the
`F_cut` map with remaining bits `(1,0,1,1,0)` misses the same four
two-site seeds as `f_L1`. That shared miss set does not write `f_mix0`
into Admissibility and does not select either map as the physical rule.
The remaining physical choice — which, if any, occupancy predicate is
the Admissibility rule — stays explicit.

### N7 — hostile steelman

The strongest objection is that `f_mix0` differs from L1 only on
`mixed3`, so any two-site seed whose first two waves never present a
`mixed3` neighborhood must share L1's fill bit, making the same four
misses leftover-character of the `l1miss2` list or of #6434. That
objection is correctly about the `mixed3` orbit not being queried on
these four long-axis pairs. It does not overturn the stated theorem.
Whether `mixed3=0` changes the 2-site fill set is a new census: every
two-site seed is run under both maps. The four misses happen to
coincide. A split would have been displayed. None occurs. #6434 named
the pair and did not list the seeds. The `l1miss2` surface is L1
alone.

### N8 — cross-cycle echo

Repository search found nearby occupancy and covariance surfaces. They are
context, not load-bearing dependencies. The 24 rotations, 10 orbits,
`f_mix0` tuple, the 66-seed census, and the L1 comparison are recomputed
here.

| Earlier surface | Similar issue | Mechanism considered here |
|---|---|---|
| `docs/ADMISSIBILITY_COVARIANT_Q8_CONDITIONAL_LAW_PAIR_BOUNDED_THEOREM_NOTE_2026-08-13.md` | proper-cubic covariance of a local rule | covariance is used only as the orbit filter for Boolean maps |
| `docs/PHYSICAL_SPATIAL_BLOCK_SEAM_DICHOTOMY_CYCLE728_NOTE_2026-08-04.md` | two-cell box `{0,1,2}×{0,1}×{0,1}` | the same twelve spatial vertices are the patch; the seam cost is unused |
| `docs/MINIMAL_AXIOMS_2026-06-29.md` | one covariant nearest-neighbor rule | the axiom names the contract; this note does not select the rule |

The 1-site / face-diagonal / `S*` fills of `f_mix0` (#6415/#6424) are
reconfirmed and are not the residual. The `cov=62` pair (#6433/#6434)
is the class this note splits into named miss seeds. The `l1miss2`
surface lists L1's four misses on a different map.

No earlier mechanism retires the `f_mix0` miss-set list or writes
`f_mix0` into Admissibility.

No-Go Discipline disposition: **PASS** for the Hamming distinction and
the exact four-set equality of `f_mix0` and `f_L1` stated above.

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
`F_cut`, isolates the remaining-bit map `f_mix0`, checks that
`cov(f_mix0)=62`, confirms the face-diagonal and `S*` fills, lists the
four miss seeds in lex order with halt histories, recomputes L1's four
misses, and reports that the four-sets are equal. Declared audit inputs
are this note and the axiom memo. No runner cache is written.
