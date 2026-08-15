---
claim_id: f_cut_filler_bit_tuples_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "The eight F_cut 1-site fillers are classified by their (wt1, opp2, adj2, vertex3, mixed3) tuples. N_distinct distinct tuples. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_filler_bit_tuples_2026_08_15.py
---

# Eight `F_cut` 1-Site Filler Remaining-Bit Tuples

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact remaining-bit taxonomy of the eight cube-covariant
complement-even 1-site fillers of the twelve-vertex two-cube with
off-patch occupancy `0`. Each filler is named once by its
`(wt1, opp2, adj2, vertex3, mixed3)` tuple. The eight tuples are
displayed rival members. None is adopted as the physical Admissibility
rule.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_filler_bit_tuples_2026_08_15.py`](../scripts/f_cut_filler_bit_tuples_2026_08_15.py)
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
`{0,1,2}×{0,1}×{0,1}`, seed `(0,0,0)` starts locked. Off-patch neighbors
have occupancy `0`. Each tick, every unlocked on-patch vertex evaluates
`f` on its six-neighbor occupancy tuple and locks if `f=1`. Fill means
`|locks_halt|=12`. Reconstructing that dynamics on every map in `F_cut`
yields exactly eight fillers.

Investment #6402–#6405 reported four separate counts on those eight
(`N_opp0=4`, `N_v31=4`, `N_and=1`, `N_adj1=8`). Those are one-bit or
AND counts. They do not name the eight members. This note is the
eight-member taxonomy, not a second count of one bit, not another AND
table.

The axis type of a 6-tuple `c` is the triple `(u,b,e)` with `u+b+e=3`,
where `u` is the number of axes with `c_{+} ≠ c_{-}`, `b` the number with
`(c_{+},c_{-})=(1,1)`, and `e` the number with `(c_{+},c_{-})=(0,0)`.
The remaining free orbits after the vanish cuts, and the names used here,
are

| name | `(u,b,e)` | geometric reading |
|---|---|---|
| `wt1` | `(1,0,2)` | one-axis contrast; a 1-site wave |
| `opp2` | `(0,1,2)` | opposite pair; balanced axis |
| `adj2` | `(2,0,1)` | two-axis contrast |
| `vertex3` | `(3,0,0)` | three-axis contrast; cube-vertex type |
| `mixed3` | `(1,1,1)` | mixed triple |

Complement-even forces `wt5=wt1`, `adj4=adj2`, and `opp4=opp2`.

`f_L1(c)=1` if and only if some axis is unbalanced: `c_{+μ} ≠ c_{-μ}` for
at least one `μ ∈ {x,y,z}`. Equivalently, some discrete neighbor contrast
`n_μ = c_{+μ} − c_{-μ}` is nonzero. This is **not** Hamming parity
`|c|_1 mod 2`.

**Theorem 1.** `f_L1` is one of the eight and its tuple is
`(wt1, opp2, adj2, vertex3, mixed3) = (1, 0, 1, 1, 1)`.

**Theorem 2.** The eight remaining-bit tuples, listed once each in
lexicographic order, are

```text
(1, 0, 1, 0, 0)
(1, 0, 1, 0, 1)
(1, 0, 1, 1, 0)
(1, 0, 1, 1, 1)
(1, 1, 1, 0, 0)
(1, 1, 1, 0, 1)
(1, 1, 1, 1, 0)
(1, 1, 1, 1, 1)
```

```text
N_distinct = 8.
```

adj2=1 for all eight. Exactly one row is `(1, 0, 1, 1, 1)`.

**Theorem 3.** The eight tuples are the displayed rival members of
`F_cut` that fill from 1-site. Do not adopt any. Do not write the table
into Admissibility.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The ten-orbit reconstruction, the eight F_cut 1-site fillers, membership of f_L1, the eight remaining-bit tuples, N_distinct=8, adj2-universality, and the unique L1 row are enumerated. The table is displayed, not written into Admissibility."
trace_class: upstream_support
target_claim_id: f_cut_filler_bit_tuples
target_blocker_text: "the eight F_cut 1-site fillers remain unnamed as remaining-bit tuples"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the eight-tuple taxonomy; any physical use must separately derive an Admissibility selector"
conditional_surface_status: "exact for the eight F_cut 1-site fillers on this twelve-vertex patch with off-patch o=0; no Z^3-wide law and no physical selector"
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
- the 1-site seed `(0,0,0)`;
- the named remaining bits `wt1`, `opp2`, `adj2`, `vertex3`, `mixed3`.

No observational comparator, literature constant, Wilson weight, rate, or
generator is imported. No Record scalar functional appears.

Not leftover-character of #6402. Not leftover-character of #6403.
Not leftover-character of #6404. Not leftover-character of #6405.
Those notes count one bit or an AND of bits. This note lists each filler
once.

## Exact Target And Objects

**Target.** Name each of the eight `F_cut` 1-site fillers by its
remaining-bit tuple, count the distinct tuples, and record whether
`adj2=1` for all eight and whether exactly one row is the L1 tuple.

Write a neighbor configuration as `c ∈ {0,1}^6`. A proper cube rotation `R`
acts by `(R·c)(d) = c(R^{-1}d)` on the six face directions `d`. A map
`f:{0,1}^6 → {0,1}` is cube-covariant when `f(R·c)=f(c)` for every such `R`.
Equivalently, `f` is constant on each orbit.

The ten axis-type classes `(u,b,e)` are exactly the ten orbits. Complement
sends `(u,b,e)` to `(u,e,b)`.

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

A locked set `S` determines occupancies: a lattice neighbor in `S` has
occupancy `1`, and every other neighbor — including every off-patch
neighbor — has occupancy `0`. One synchronous tick replaces `S` by

```text
S ∪ { v in two-cube \ S : f(neighborhood_6(v; S)) = 1 }.
```

The eight fillers are the maps in `F_cut` whose halt set has cardinality
12. Define

```text
f_L1(c) = 1  iff  u(c) ≥ 1.
```

The remaining-bit tuple of a filler is the assignment
`(wt1,opp2,adj2,vertex3,mixed3)`. Complements are forced, so the tuple
names the map inside `F_cut`. `N_distinct` is the number of distinct
tuples among the eight fillers.

Do not write the table into Admissibility.

## Theorems

**Theorem 1.** There are exactly 24 proper cube rotations and exactly 10
orbits on `{0,1}^6`. The three cuts leave `|F_cut|=32`. Exactly eight
members of `F_cut` fill the twelve-vertex two-cube from seed `(0,0,0)`
with off-patch occupancy `0`. The unbalanced-axis map `f_L1` is one of
those eight. It is not Hamming parity. Its remaining-bit tuple is
`(wt1,opp2,adj2,vertex3,mixed3)=(1, 0, 1, 1, 1)`, and complement-even
forces `wt5=1`, `adj4=1`, `opp4=0`. Its lock cardinalities are
`(1,4,8,11,12)` and its halt tick is `4`.

**Theorem 2.** Exhaustive naming of the eight reconstructed fillers
gives the eight tuples listed above and

```text
N_distinct = 8.
```

adj2=1 for all eight. Exactly one row is `(1, 0, 1, 1, 1)`.

**Theorem 3.** The eight tuples are the displayed rival members of
`F_cut` that fill from 1-site. None is adopted. The table is not an
Admissibility clause.

## Proof-Obligation Graph

| obligation | exact disposition |
|---|---|
| 24 proper cube rotations | signed permutations of the three axes with determinant `+1` |
| 10 orbits on `{0,1}^6` | axis-type classes `(u,b,e)` partition the 64 cells with the listed sizes |
| `|F_cut|=32` | three complement-pairs and two complement-fixed orbits remain free after the vanish cuts |
| eight fillers | exhaustive 32-run census of `F_cut` to a fixed point with `|locks|=12` |
| `f_L1` is in the eight | halt set has cardinality 12 at tick 4 |
| `f_L1` is not Hamming | the two-unbalanced-axis orbit `adj2` has even weight and `f_L1=1` |
| L1 bit tuple | `(1, 0, 1, 1, 1)` |
| eight tuples | lexicographic list of the eight remaining-bit assignments |
| `N_distinct` | eight distinct tuples |
| `adj2` universality | every filler has `adj2=1` |
| unique L1 row | exactly one of the eight equals `(1, 0, 1, 1, 1)` |
| no Admissibility rewrite | displayed rival members only |

## Mutations

1. Replace `f_L1` by Hamming `|c|_1 mod 2`: the maps disagree on `adj2`,
   and Hamming is not a filler.
2. Drop `adj2=1`: the resulting `F_cut` maps with `wt1=1` and `adj2=0`
   do not fill, so they are not rows of the table.
3. Drop complement-even or the vanish-on-full cut: the class is no longer
   the 32-element `F_cut`, and the eight-filler set is a different census.
4. Replace off-patch occupancy `0` by a blank-block: first-wave candidates
   become undefined; that is a different census.
5. Collapse the eight rows to a single-bit count: that is leftover
   character of #6402/#6403/#6405, not this taxonomy.

## What This Does Not Claim

- No physical Admissibility selector and no adopted occupancy law.
- No Qubit rewrite and no `M_2(C)`-valued conditional probability.
- No `Z^3`-wide formation, rate, or generator.
- No identification of `f_L1` with Hamming parity.
- No leftover-character restatement of `N_opp0`, `N_v31`, `N_and`, or
  `N_adj1` in place of the eight-tuple table.
- No blank-block, 2-site, or 3-site variant.
- No axiom edit: the table is displayed, not written into Admissibility.

## No-Go Discipline Gate

The only negative claim is that the eight members are not a single
unnamed class: they are eight named tuples, and only one of those
tuples is L1. The taxonomy is an exact enumeration, not a wall, and it
is not an Admissibility clause.

### N1 — materially distinct routes

| Route | Exact attack | Result and authority | Marker |
|---|---|---|---|
| orbit reconstruction | Recompute the 24 rotations and the 10 axis-type orbits. | Theorem 1 and checks `thm1-twenty-four-rotations` / `thm1-ten-orbits`. | **ATTEMPTED** |
| eight-filler reconstruction | Run every map in `F_cut` to a fixed point and keep `|locks|=12`. | Theorem 1 and check `thm1-eight-fillers` give eight fillers. | **ATTEMPTED** |
| L1 membership and tuple | Evaluate `f_L1` on the named orbits and on the two-cube. | Theorem 1 and check `thm1-f-L1-in-eight-and-tuple`. | **ATTEMPTED** |
| Hamming-as-`f_L1` | Test whether `|c|_1 mod 2` equals the unbalanced-axis predicate. | Theorem 1 and check `thm1-f-L1-not-hamming` separate the maps. | **ATTEMPTED** |
| eight-tuple taxonomy | Name each filler by `(wt1,opp2,adj2,vertex3,mixed3)` and count distinct rows. | Theorem 2 and checks `thm2-eight-tuples-listed` / `thm2-n-distinct`. | **ATTEMPTED** |
| adj2-universality and unique L1 row | Test `adj2` on all eight and count L1 rows. | Theorem 2 and checks `thm2-adj2-all-one` / `thm2-exactly-one-l1-row`. | **ATTEMPTED** |

### N2 — wall independence and collapse

There is one negative conclusion: the eight members are not anonymous,
and L1 is not the whole table. The distinct-tuple count and the unique
L1-row count are two certificates of the same table, so they collapse
rather than count as two walls.

| Pair | First closes second? | Second closes first? | Disposition |
|---|---:|---:|---|
| `N_distinct=8` / unique L1 row | no: eight distinct rows do not name which row is L1 | no: a unique L1 row does not force eight distinct rows | independent table properties |
| `adj2=1` for all eight / unique L1 row | no: a shared `adj2` bit is not uniqueness of the full tuple | no: uniqueness of L1 does not force `adj2=1` on the other seven | independent bits |
| eight-filler count / eight-tuple table | no: membership in the eight does not name the tuples | no: a tuple table does not replace the fill census | separate exact objects |

Physical law selection is not a wall: this note makes no negative theorem
about the existence of a selector and simply does not claim one.

### N3 — hidden-condition scan

| Phrase or premise | Classification |
|---|---|
| “work on the twelve-vertex two-cube” | explicit patch hypothesis; not a `Z^3` theorem |
| off-patch occupancy `0` | explicit default; blank-block is a different rule |
| the eight fillers | explicit `F_cut` 1-site fill set; the other 24 maps in `F_cut` are excluded |
| remaining-bit tuples | explicit orbit bits; not a leftover-character of #6402–#6405 |
| “lock” | Record permanence on this Boolean occupancy model, not a possibility-valued law |
| “cube-covariant” | invariance under the 24 proper rotations, cited to Lattice/Admissibility |
| Hamming parity | displayed mutation only |
| `N_distinct=8` | displayed taxonomy inside the eight, not an Admissibility clause |

### N4 — citation-to-residual matching

| Evidence path:line | Residual attacked | Residual claimed closed | Match? |
|---|---|---|---:|
| `docs/MINIMAL_AXIOMS_2026-06-29.md:37` | ambient lattice and cubic rotations | sites are `Z^3` with proper cubic rotations | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:57` | covariant nearest-neighbor rule | covariance is the class filter, not a selector | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:79` | lock permanence | a locked site stays locked | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:83` | unreadability of absence | unlocked and off-patch sites contribute occupancy `0`, not a readout | yes |
| `scripts/f_cut_filler_bit_tuples_2026_08_15.py:78` | 24 proper rotations | signed permutations with determinant `+1` | yes |
| `scripts/f_cut_filler_bit_tuples_2026_08_15.py:123` | `f_L1` definition | unbalanced-axis predicate, not Hamming | yes |
| `scripts/f_cut_filler_bit_tuples_2026_08_15.py:128` | Hamming mutation | `|c|_1 mod 2` is a different map | yes |
| `scripts/f_cut_filler_bit_tuples_2026_08_15.py:53` | remaining bits | named tuple `(wt1,opp2,adj2,vertex3,mixed3)` | yes |
| `scripts/f_cut_filler_bit_tuples_2026_08_15.py:266` | eight-filler reconstruction | `F_cut` maps with `|locks|=12` | yes |
| `scripts/f_cut_filler_bit_tuples_2026_08_15.py:349` | `N_distinct` | distinct remaining-bit tuples among the eight | yes |

No evidence citation is used to claim that a physical occupancy law, a
formation rate, or a `Z^3`-wide selector has been closed.

### N5 — rhetoric and resolution audit

| Resolution | Executed? | Narrow negative supported? |
|---|---:|---|
| per element | yes: all 64 neighbor 6-tuples | each is assigned its axis-type orbit; no broader cell class is classified |
| per site | yes: the twelve two-cube vertices | each uses the same six-direction stencil with off-patch occupancy `0` |
| per mode | yes: every map in `F_cut`, then every filler | the taxonomy is this class on this seed; other seeds are unclaimed |
| per block | yes: the eight-tuple table | `N_distinct`, `adj2` universality, and the unique L1 row are table properties |
| lattice wide | no | no `Z^3`-wide formation or Admissibility selector is asserted |

The runner prints the same five resolution statements.

### N6 — partial closure and primitive scan

The primitive registry at `docs/audit/data/axiom_premise_nodes.json` was
checked. The only dependency used is the registered `minimal_axioms` node.
No approved primitive supplies the Boolean occupancy maps, and none is
reclassified as an import or wall.

One partial-closure mechanism is displayed rather than suppressed: the
eight `F_cut` 1-site fillers are named by remaining-bit tuples, and L1
is exactly one of those eight rows. That table does not write the tuples
into Admissibility and does not select `f_L1` as the physical rule. The
remaining physical choice — which, if any, occupancy predicate is the
Admissibility rule — stays explicit.

### N7 — hostile steelman

The strongest objection is that the five remaining bits *are* the free
data of `F_cut`, so listing eight tuples is leftover-character of the
eight-filler census: among eight maps that already vary on
`(opp2,vertex3,mixed3)` with `wt1=adj2=1` forced by fill, writing the
eight combinations is tautological. That objection is correctly about
the algebraic shape of the eight. It does not overturn the stated
theorem. #6402–#6405 counted one bit or an AND of bits and left the
members unnamed. The object here is the eight-row table itself. A
collision (`N_distinct<8`) or an `adj2=0` row would have been displayed.
Neither occurs.

### N8 — cross-cycle echo

Repository search found nearby occupancy and covariance surfaces. They are
context, not load-bearing dependencies. The 24 rotations, 10 orbits,
eight fillers, remaining-bit tuples, and `N_distinct` are recomputed here.

| Earlier surface | Similar issue | Mechanism considered here |
|---|---|---|
| [`docs/ADMISSIBILITY_COVARIANT_Q8_CONDITIONAL_LAW_PAIR_BOUNDED_THEOREM_NOTE_2026-08-13.md`](ADMISSIBILITY_COVARIANT_Q8_CONDITIONAL_LAW_PAIR_BOUNDED_THEOREM_NOTE_2026-08-13.md) | proper-cubic covariance of a local rule | covariance is used only as the orbit filter for Boolean maps |
| [`docs/PHYSICAL_SPATIAL_BLOCK_SEAM_DICHOTOMY_CYCLE728_NOTE_2026-08-04.md`](PHYSICAL_SPATIAL_BLOCK_SEAM_DICHOTOMY_CYCLE728_NOTE_2026-08-04.md) | two-cell box `{0,1,2}×{0,1}×{0,1}` | the same twelve spatial vertices are the patch; the seam cost is unused |
| [`docs/MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) | one covariant nearest-neighbor rule | the axiom names the contract; this note does not select the rule |

The one-bit counts #6402–#6405 are the leftover-character this note
refuses to repeat. They are not parents and do not close the eight-tuple
taxonomy.

No earlier mechanism names the eight members or writes the table into
Admissibility.

No-Go Discipline disposition: **PASS** for the eight-tuple taxonomy,
`N_distinct = 8`, `adj2=1` for all eight, and the unique L1 row stated
above.

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
`F_cut`, reconstructs the eight 1-site fillers, checks that `f_L1` is
among them with tuple `(1, 0, 1, 1, 1)`, lists the eight remaining-bit
tuples, reports `N_distinct = 8`, checks that `adj2=1` for all eight,
and checks that exactly one row is `(1, 0, 1, 1, 1)`. Declared audit
inputs are this note and the axiom memo. No runner cache is written.
