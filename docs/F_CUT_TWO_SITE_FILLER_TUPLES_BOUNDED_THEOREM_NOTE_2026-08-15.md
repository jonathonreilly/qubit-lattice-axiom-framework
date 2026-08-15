---
claim_id: f_cut_two_site_filler_tuples_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "The four F_cut maps that fill the two-cube from the face-diagonal 2-site seed with off-patch o=0 are classified by their (wt1, opp2, adj2, vertex3, mixed3) tuples. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_two_site_filler_tuples_2026_08_15.py
---

# Four `F_cut` 2-Site Filler Remaining-Bit Tuples

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact remaining-bit taxonomy of the four cube-covariant
complement-even maps that fill the twelve-vertex two-cube from the
face-diagonal 2-site seed `{(0,0,0),(1,1,0)}` with off-patch occupancy
`0`. Each filler is named once by its `(wt1, opp2, adj2, vertex3,
mixed3)` tuple. The four tuples are displayed rival members. None is
adopted as the physical Admissibility rule.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_two_site_filler_tuples_2026_08_15.py`](../scripts/f_cut_two_site_filler_tuples_2026_08_15.py)
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
`{0,1,2}×{0,1}×{0,1}`, seed `{(0,0,0),(1,1,0)}` starts locked. Off-patch
neighbors have occupancy `0`. Each tick, every unlocked on-patch vertex
evaluates `f` on its six-neighbor occupancy tuple and locks if `f=1`.
Fill means `|locks_halt|=12`. Reconstructing that dynamics on every map
in `F_cut` yields exactly four fillers.

Investment #6413 counted `N_cut2=4` and displayed one non-L1 tuple
`(1, 0, 1, 1, 0)`. That only counted 4. It did not name the four members.
Investment #6410 named eight remaining-bit tuples; those eight are 1-site
fillers. This note is the four-member 2-site taxonomy, not a second
count of four and not the 1-site eight.

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

**Theorem 1.** `f_L1` is one of the four and its tuple is
`(wt1, opp2, adj2, vertex3, mixed3) = (1, 0, 1, 1, 1)`. Another of the
four is `(1, 0, 1, 1, 0)`.

**Theorem 2.** The four remaining-bit tuples, listed once each in
lexicographic order, are

```text
(1, 0, 1, 1, 0)
(1, 0, 1, 1, 1)
(1, 1, 1, 1, 0)
(1, 1, 1, 1, 1)
```

```text
N_distinct = 4.
```

Exactly one row is `(1, 0, 1, 1, 1)`.

**Theorem 3.** The four tuples are the displayed 2-site `F_cut` rivals.
Do not adopt any. Do not write the table into Admissibility.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The ten-orbit reconstruction, the four F_cut 2-site fillers, membership of f_L1, the displayed other tuple (1, 0, 1, 1, 0), the four remaining-bit tuples, and N_distinct=4 are enumerated. The table is displayed, not written into Admissibility."
trace_class: upstream_support
target_claim_id: f_cut_two_site_filler_tuples
target_blocker_text: "the four F_cut 2-site fillers remain unnamed as remaining-bit tuples"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the four-tuple 2-site taxonomy; any physical use must separately derive an Admissibility selector"
conditional_surface_status: "exact for the four F_cut 2-site fillers on this twelve-vertex patch with off-patch o=0 and the face-diagonal seed; no Z^3-wide law and no physical selector"
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
- the face-diagonal 2-site seed `{(0,0,0),(1,1,0)}`;
- the named remaining bits `wt1`, `opp2`, `adj2`, `vertex3`, `mixed3`.

No observational comparator, literature constant, Wilson weight, rate, or
generator is imported. No Record scalar functional appears.

Not leftover-character of #6413. That only counted 4 and displayed one
non-L1 tuple. Not leftover-character of #6410: those eight are 1-site fillers.
This note lists each remaining 2-site filler once.

## Exact Target And Objects

**Target.** Name each of the four `F_cut` maps that fill from the
face-diagonal 2-site seed by its remaining-bit tuple, count the distinct
tuples, and record that `f_L1` is one named row.

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

The four fillers are the maps in `F_cut` whose halt set from this seed
has cardinality 12. Define

```text
f_L1(c) = 1  iff  u(c) ≥ 1.
```

The remaining-bit tuple of a filler is the assignment
`(wt1,opp2,adj2,vertex3,mixed3)`. Complements are forced, so the tuple
names the map inside `F_cut`. `N_distinct` is the number of distinct
tuples among the four fillers.

Do not write the table into Admissibility.

## Theorems

**Theorem 1.** There are exactly 24 proper cube rotations and exactly 10
orbits on `{0,1}^6`. The three cuts leave `|F_cut|=32`. Exactly four
members of `F_cut` fill the twelve-vertex two-cube from seed
`{(0,0,0),(1,1,0)}` with off-patch occupancy `0`. The unbalanced-axis
map `f_L1` is one of those four. It is not Hamming parity. Its
remaining-bit tuple is `(wt1,opp2,adj2,vertex3,mixed3)=(1, 0, 1, 1, 1)`,
and complement-even forces `wt5=1`, `adj4=1`, `opp4=0`. Its lock
cardinalities are `(2,7,11,12)` and its halt tick is `3`. Another of the
four is `(1, 0, 1, 1, 0)`.

**Theorem 2.** Exhaustive naming of the four reconstructed fillers
gives the four tuples listed above and

```text
N_distinct = 4.
```

Exactly one row is `(1, 0, 1, 1, 1)`.

**Theorem 3.** The four tuples are the displayed 2-site `F_cut` rivals.
None is adopted. The table is not an Admissibility clause.

## Proof-Obligation Graph

| obligation | exact disposition |
|---|---|
| 24 proper cube rotations | signed permutations of the three axes with determinant `+1` |
| 10 orbits on `{0,1}^6` | axis-type classes `(u,b,e)` partition the 64 cells with the listed sizes |
| `|F_cut|=32` | three complement-pairs and two complement-fixed orbits remain free after the vanish cuts |
| four fillers | exhaustive 32-run census of `F_cut` to a fixed point with `|locks|=12` from this seed |
| `f_L1` is in the four | halt set has cardinality 12 at tick 3 |
| `f_L1` is not Hamming | the two-unbalanced-axis orbit `adj2` has even weight and `f_L1=1` |
| L1 bit tuple | `(1, 0, 1, 1, 1)` |
| displayed other | remaining-bit tuple `(1, 0, 1, 1, 0)` is a second filler |
| four tuples | lexicographic list of the four remaining-bit assignments |
| `N_distinct` | four distinct tuples |
| unique L1 row | exactly one of the four equals `(1, 0, 1, 1, 1)` |
| no Admissibility rewrite | displayed rival members only |

## Mutations

1. Replace `f_L1` by Hamming `|c|_1 mod 2`: the maps disagree on the
   two-unbalanced-axis orbit, and Hamming does not fill from this seed.
2. Replace off-patch occupancy `0` by a blank-block: first-wave candidates
   become undefined; that is a different census.
3. Drop complement-even or the vanish-on-full cut: the class is no longer
   the 32-element `F_cut`.
4. Seed only `(0,0,0)`: the 1-site eight-tuple table is a different
   residual.
5. Collapse the four rows to the count `N_cut2=4`: that is leftover
   character of #6413, not this taxonomy.

## What This Does Not Claim

- No physical Admissibility selector and no adopted occupancy law.
- No Qubit rewrite and no `M_2(C)`-valued conditional probability.
- No `Z^3`-wide formation, rate, or generator.
- No identification of `f_L1` with Hamming parity.
- No leftover-character restatement of the `N_cut2=4` count, and no
  restatement of the eight 1-site filler tuples, in place of the
  four-tuple 2-site table.
- No blank-block or 3-site variant.
- No axiom edit: the table is displayed, not written into Admissibility.

## No-Go Discipline Gate

The only negative claim is that the four members are not a single
unnamed class: they are four named tuples, and only one of those
tuples is L1. The taxonomy is an exact enumeration, not a wall, and it
is not an Admissibility clause.

### N1 — materially distinct routes

| Route | Exact attack | Result and authority | Marker |
|---|---|---|---|
| orbit reconstruction | Recompute the 24 rotations and the 10 axis-type orbits. | Theorem 1 and checks `thm1-twenty-four-rotations` / `thm1-ten-orbits`. | **ATTEMPTED** |
| four-filler reconstruction | Run every map in `F_cut` to a fixed point from this seed and keep `|locks|=12`. | Theorem 1 and check `thm1-four-fillers` give four fillers. | **ATTEMPTED** |
| L1 membership and tuple | Evaluate `f_L1` on the named orbits and on the two-cube. | Theorem 1 and check `thm1-f-L1-in-four-and-tuple`. | **ATTEMPTED** |
| Hamming-as-`f_L1` | Test whether `|c|_1 mod 2` equals the unbalanced-axis predicate. | Theorem 1 and check `thm1-f-L1-not-hamming` separate the maps. | **ATTEMPTED** |
| four-tuple taxonomy | Name each filler by `(wt1,opp2,adj2,vertex3,mixed3)` and count distinct rows. | Theorem 2 and checks `thm2-four-tuples-listed` / `thm2-n-distinct`. | **ATTEMPTED** |
| unique L1 row and displayed other | Count L1 rows and exhibit `(1, 0, 1, 1, 0)`. | Theorem 1–2 and checks `thm1-displayed-other-tuple` / `thm2-exactly-one-l1-row`. | **ATTEMPTED** |

### N2 — wall independence and collapse

There is one negative conclusion: the four members are not anonymous,
and L1 is not the whole table. The distinct-tuple count and the unique
L1-row count are two certificates of the same table, so they collapse
rather than count as two walls.

| Pair | First closes second? | Second closes first? | Disposition |
|---|---:|---:|---|
| `N_distinct=4` / unique L1 row | no: four distinct rows do not name which row is L1 | no: a unique L1 row does not force four distinct rows | independent table properties |
| four-filler count / four-tuple table | no: membership in the four does not name the tuples | no: a tuple table does not replace the fill census | separate exact objects |
| displayed `(1, 0, 1, 1, 0)` / unique L1 row | yes: a second named row is non-uniqueness of L1 | yes: uniqueness of the L1 row plus four rows requires a non-L1 row | collapse into the named-table claim |
| 1-site eight / this four-tuple table | no: a different seed | no: this seed does not classify the 1-site eight | different seed, different residual |

Physical law selection is not a wall: this note makes no negative theorem
about the existence of a selector and simply does not claim one.

### N3 — hidden-condition scan

| Phrase or premise | Classification |
|---|---|
| “work on the twelve-vertex two-cube” | explicit patch hypothesis; not a `Z^3` theorem |
| off-patch occupancy `0` | explicit default; blank-block is a different rule |
| the four fillers | explicit `F_cut` 2-site fill set; the other 28 maps in `F_cut` are excluded |
| remaining-bit tuples | explicit orbit bits; not leftover-character of #6413 or #6410 |
| “lock” | Record permanence on this Boolean occupancy model, not a possibility-valued law |
| “cube-covariant” | invariance under the 24 proper rotations, cited to Lattice/Admissibility |
| Hamming parity | displayed mutation only |
| `N_distinct=4` | displayed taxonomy inside the four, not an Admissibility clause |
| face-diagonal 2-site seed | explicit seed; the 1-site eight is a different residual |

### N4 — citation-to-residual matching

| Evidence path:line | Residual attacked | Residual claimed closed | Match? |
|---|---|---|---:|
| `docs/MINIMAL_AXIOMS_2026-06-29.md:37` | ambient lattice and cubic rotations | sites are `Z^3` with proper cubic rotations | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:57` | covariant nearest-neighbor rule | covariance is the class filter, not a selector | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:79` | lock permanence | a locked site stays locked | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:83` | unreadability of absence | unlocked and off-patch sites contribute occupancy `0`, not a readout | yes |
| `scripts/f_cut_two_site_filler_tuples_2026_08_15.py:79` | 24 proper rotations | signed permutations with determinant `+1` | yes |
| `scripts/f_cut_two_site_filler_tuples_2026_08_15.py:124` | `f_L1` definition | unbalanced-axis predicate, not Hamming | yes |
| `scripts/f_cut_two_site_filler_tuples_2026_08_15.py:129` | Hamming mutation | `|c|_1 mod 2` is a different map | yes |
| `scripts/f_cut_two_site_filler_tuples_2026_08_15.py:54` | remaining bits | named tuple `(wt1,opp2,adj2,vertex3,mixed3)` | yes |
| `scripts/f_cut_two_site_filler_tuples_2026_08_15.py:267` | four-filler reconstruction | `F_cut` maps with `|locks|=12` from this seed | yes |
| `scripts/f_cut_two_site_filler_tuples_2026_08_15.py:350` | `N_distinct` | distinct remaining-bit tuples among the four | yes |

No evidence citation is used to claim that a physical occupancy law, a
formation rate, or a `Z^3`-wide selector has been closed.

### N5 — rhetoric and resolution audit

| Resolution | Executed? | Narrow negative supported? |
|---|---:|---|
| per element | yes: all 64 neighbor 6-tuples | each is assigned its axis-type orbit; no broader cell class is classified |
| per site | yes: the twelve two-cube vertices | each uses the same six-direction stencil with off-patch occupancy `0` |
| per mode | yes: every map in `F_cut`, then every 2-site filler | the taxonomy is this class on this seed; other seeds are unclaimed |
| per block | yes: the four-tuple table | `N_distinct` and the unique L1 row are table properties |
| lattice wide | no | no `Z^3`-wide formation or Admissibility selector is asserted |

The runner prints the same five resolution statements.

### N6 — partial closure and primitive scan

The primitive registry at `docs/audit/data/axiom_premise_nodes.json` was
checked. The only dependency used is the registered `minimal_axioms` node.
No approved primitive supplies the Boolean occupancy maps, and none is
reclassified as an import or wall.

One partial-closure mechanism is displayed rather than suppressed: the
four `F_cut` 2-site fillers are named by remaining-bit tuples, and L1
is exactly one of those four rows. That table does not write the tuples
into Admissibility and does not select `f_L1` as the physical rule. The
remaining physical choice — which, if any, occupancy predicate is the
Admissibility rule — stays explicit.

### N7 — hostile steelman

The strongest objection is that the five remaining bits *are* the free
data of `F_cut`, so listing four tuples is leftover-character of the
`N_cut2=4` count: among four maps that already vary on `(opp2,mixed3)`
with `wt1=adj2=vertex3=1` forced by fill, writing the four combinations
is tautological. That objection is correctly about the algebraic shape
of the four. It does not overturn the stated theorem. #6413 counted four
and displayed one non-L1 tuple; the members stayed unnamed. The object
here is the four-row table itself. A collision (`N_distinct<4`) would
have been displayed. It does not occur.

### N8 — cross-cycle echo

Repository search found nearby occupancy and covariance surfaces. They are
context, not load-bearing dependencies. The 24 rotations, 10 orbits,
four fillers, remaining-bit tuples, and `N_distinct` are recomputed here.

| Earlier surface | Similar issue | Mechanism considered here |
|---|---|---|
| [`docs/ADMISSIBILITY_COVARIANT_Q8_CONDITIONAL_LAW_PAIR_BOUNDED_THEOREM_NOTE_2026-08-13.md`](ADMISSIBILITY_COVARIANT_Q8_CONDITIONAL_LAW_PAIR_BOUNDED_THEOREM_NOTE_2026-08-13.md) | proper-cubic covariance of a local rule | covariance is used only as the orbit filter for Boolean maps |
| [`docs/PHYSICAL_SPATIAL_BLOCK_SEAM_DICHOTOMY_CYCLE728_NOTE_2026-08-04.md`](PHYSICAL_SPATIAL_BLOCK_SEAM_DICHOTOMY_CYCLE728_NOTE_2026-08-04.md) | two-cell box `{0,1,2}×{0,1}×{0,1}` | the same twelve spatial vertices are the patch; the seam cost is unused |
| [`docs/MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) | one covariant nearest-neighbor rule | the axiom names the contract; this note does not select the rule |

The `N_cut2=4` count #6413 and the 1-site eight-tuple table #6410 are
the leftover-character this note refuses to repeat. They are not parents
and do not close the four-tuple 2-site taxonomy.

No earlier mechanism names the four 2-site members or writes the table
into Admissibility.

No-Go Discipline disposition: **PASS** for the four-tuple taxonomy,
`N_distinct = 4`, and the unique L1 row stated above.

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
`F_cut`, reconstructs the four 2-site fillers, checks that `f_L1` is
among them with tuple `(1, 0, 1, 1, 1)`, checks that `(1, 0, 1, 1, 0)`
is another filler, lists the four remaining-bit tuples, and reports
`N_distinct = 4`. Declared audit inputs are this note and the axiom
memo. No runner cache is written.
