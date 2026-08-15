---
claim_id: f_cut_k4_v30_shared_face_miss_mechanism_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On the two-cube with off-patch o=0 and 1-site seed (1,0,0), the first neighborhood at which F_cut (1,1,1,0,0) refuses and (1,1,1,1,1) fires is reported by tick, site, and axis type. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_k4_v30_shared_face_miss_mechanism_2026_08_15.py
---

# First Refused Neighborhood On The Shared-Face One-Site Miss Seeds

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** independent occupancy-to-lock runs from each of the four
shared-face one-site seeds that the `vertex3=0` k=4 map `f00=(1,1,1,0,0)`
does not fill, on the twelve-vertex two-cube `{0,1,2}×{0,1}×{0,1}` with
off-patch occupancy `0`. The `F_cut` map `f11` with remaining-bit tuple
`(1, 1, 1, 1, 1)` fills each of those four seeds. On seed `(1,0,0)`, the
first neighborhood at which `f00=0` and `f11=1` is reported by tick,
site, and axis type. The other three shared-face seeds share that first
axis type. Displayed, not adopted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_k4_v30_shared_face_miss_mechanism_2026_08_15.py`](../scripts/f_cut_k4_v30_shared_face_miss_mechanism_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

The 24 proper cube rotations act on neighbor 6-tuples in `{0,1}^6` and
partition those 64 cells into 10 orbits. Cube-covariant predicates are the
`{0,1}`-assignments to those orbits. The three displayed cuts

1. vanish on empty: `f(empty)=0`,
2. vanish on full: `f(full)=0`,
3. complement-even: `f(c)=f(1-c)`

leave five free bits, so `|F_cut| = 32`. Remaining bits are ordered as
`(wt1, opp2, adj2, vertex3, mixed3)`.

On the two-cube `{0,1,2}×{0,1}×{0,1}`, each vertex is a 1-site seed.
There are 12 such seeds. Off-patch neighbors have occupancy `0`. Each
tick, every unlocked on-patch vertex evaluates `f` on its six-neighbor
occupancy tuple and locks if `f=1`. The process is synchronous and stops
at a fixed point in at most 12 ticks. Fill means `|locks_halt|=12`.

`f_L1(c)=1` if and only if some axis is unbalanced: `c_{+μ} ≠ c_{-μ}` for
at least one `μ ∈ {x,y,z}`. Equivalently, some discrete neighbor contrast
`n_μ = c_{+μ} − c_{-μ}` is nonzero. This is **not** Hamming parity
`|c|_1 mod 2`. The remaining-bit tuple of `f_L1` is
`(wt1, opp2, adj2, vertex3, mixed3) = (1, 0, 1, 1, 1)`.

Write `f00` for remaining bits `(1, 1, 1, 0, 0)` and `f11` for
`(1, 1, 1, 1, 1)`. The map `f00` is one of the two `vertex3=0` k=4 maps.
The map `f11` is a `vertex3=1` member of the same remaining-bit class.
Neither map is adopted.

New mechanism. Not leftover of #6448: that only listed sites. Investment
#6448 reported that both `vertex3=0` k=4 maps miss the shared-face
corners `{(1,0,0),(1,0,1),(1,1,0),(1,1,1)}`. The present object is the
first refused neighborhood on those seeds, not the miss list itself.

**Theorem 1.** Independent recomputation from seed `(1,0,0)` reconfirms
that f11 fills from (1,0,0); f00 does not. The lock-count history of
`f00` is `(1, 5, 10)` and the history of `f11` is `(1, 5, 10, 12)`. The
same pair of histories holds on the other three shared-face seeds. Those
four sites are exactly `Miss(f00)`.

**Theorem 2.** On seed `(1,0,0)`, the first neighborhood at which `f00`
refuses and `f11` fires is

```text
t = 3
x = (0, 1, 1)
axis type = vertex3 = (3, 0, 0)
```

The six-neighbor occupancy is `(1, 0, 0, 1, 0, 1)`: all three axes are
unbalanced. That is a 3-axis contrast. An extra `f00` refuses. The same
first event is seen on the independent `f00` run and on the independent
`f11` run. Because the type is `vertex3`, the miss is refusing a 3-axis
contrast.

**Theorem 3.** The other three shared-face seeds have the same first
axis type `vertex3`. Their first refused sites are `(0, 1, 0)`,
`(0, 0, 1)`, and `(0, 0, 0)` respectively, each at `t = 3`. Display. Do
not adopt vertex3. Do not write it into Admissibility.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The four shared-face 1-site misses of f00, the independent f11 fills, and the first refused neighborhood on seed (1,0,0) (tick, site, axis type) are enumerated. vertex3 is displayed, not written into Admissibility."
trace_class: frontier_discovery
target_claim_id: f_cut_k4_v30_shared_face_miss_mechanism
target_blocker_text: "the first neighborhood at which f00 refuses and f11 fires, on the shared-face 1-site miss (1,0,0), remains unnamed"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the displayed first refused neighborhood; any physical use must separately derive an Admissibility selector"
conditional_surface_status: "exact for f00 and f11 on this twelve-vertex patch with off-patch o=0 and the four shared-face 1-site misses; no Z^3-wide law and no physical selector"
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
laws. Admissibility does not supply the formation site, probability, or rate.

The following are declared mathematical scaffolding, not measured or fitted
physics inputs:

- the 24 proper signed-permutation rotations of the three axes
  (`det = +1`);
- occupancy 6-tuples on the ordered neighbor stencil
  `(+x,-x,+y,-y,+z,-z)`;
- the two-cube vertex set `{0,1,2}×{0,1}×{0,1}`;
- the off-patch occupancy default `0`;
- the complete set of 12 one-site seeds;
- independent lock-step runs of `f00` and of `f11` from each shared-face
  miss.

No observational comparator, literature constant, Wilson weight, rate, or
generator is imported. No Record scalar functional appears.

Not leftover of #6448. That leftover listed the four missed shared-face
sites. This residual is the first refused neighborhood on those seeds.

## Exact Target And Objects

**Target.** Reconfirm that `f11` fills from `(1,0,0)` and `f00` does not,
then name the first `(tick, site, axis type)` at which `f00` refuses and
`f11` fires on that seed, and state whether the other three shared-face
seeds have the same first axis type.

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
order `(wt1, opp2, adj2, vertex3, mixed3)`.

Define

```text
f_L1(c) = 1  iff  u(c) ≥ 1,
f00(c)  = remaining-value of (1, 1, 1, 0, 0),
f11(c)  = remaining-value of (1, 1, 1, 1, 1).
```

So `f00` has remaining-bit tuple `(1, 1, 1, 0, 0)` and `f11` has
`(1, 1, 1, 1, 1)`. They differ on `vertex3` and on `mixed3`. Neither map
is adopted.

A locked set `S` determines occupancies: a lattice neighbor in `S` has
occupancy `1`, and every other neighbor — including every off-patch
neighbor — has occupancy `0`. One synchronous tick replaces `S` by

```text
S ∪ { v in two-cube \ S : f(neighborhood_6(v; S)) = 1 }.
```

An independent run of `f` from a seed is that iteration started at the
seed and continued to a fixed point. A miss is a 1-site seed whose
`f00` halt set has cardinality strictly less than 12. The first refused
neighborhood on a run is the lexicographically first unlocked site, at
the earliest tick, whose neighborhood has `f00=0` and `f11=1`. Tick
`t = 1` is the first evaluation on the seed occupancy.

## Theorems

**Theorem 1.** There are exactly 24 proper cube rotations and exactly 10
orbits on `{0,1}^6`. The unbalanced-axis map `f_L1` is one element of
`F_cut`. It is not Hamming parity. On the twelve-vertex two-cube with
off-patch occupancy `0`, independent runs from seed `(1,0,0)` reconfirm
that `f11` fills and `f00` does not, with lock-count histories
`(1, 5, 10, 12)` and `(1, 5, 10)` respectively. The four shared-face
sites are exactly the one-site misses of `f00`.

**Theorem 2.** On seed `(1,0,0)`, the first neighborhood with
`f00(nbhd)=0` and `f11(nbhd)=1` is tick `t = 3`, site `(0, 1, 1)`,
axis type `vertex3` `= (3, 0, 0)`. The occupancy is
`(1, 0, 0, 1, 0, 1)`. Coverage of a 3-axis contrast is what `f11`
adds and `f00` refuses.

**Theorem 3.** The other three shared-face seeds have the same first
axis type. Display. Do not adopt vertex3. Do not write it into
Admissibility. The first refused neighborhood is a displayed census
output, not a selected occupancy law.

## Proof-Obligation Graph

| obligation | exact disposition |
|---|---|
| 24 proper cube rotations | signed permutations of the three axes with determinant `+1` |
| 10 orbits on `{0,1}^6` | axis-type classes `(u,b,e)` partition the 64 cells with the listed sizes |
| `f_L1` is in `F_cut` | `u` is rotation- and complement-invariant and `u(empty)=u(full)=0` |
| `f_L1` is not Hamming | the two-unbalanced-axis orbit has even weight and `f_L1=1` |
| `f00` misses `(1,0,0)` | independent run halts at lock-count history `(1, 5, 10)` |
| `f11` fills `(1,0,0)` | independent run fills with history `(1, 5, 10, 12)` |
| four shared-face misses of `f00` | exhaustive 12-seed fill census; lex list as above |
| two-cube has twelve vertices | `{0,1,2}×{0,1}×{0,1}` |
| off-patch occupancy `0` | declared stencil default; not a blank-block |
| first refused neighborhood | `t = 3`, site `(0, 1, 1)`, axis type `vertex3` on seed `(1,0,0)` |
| same first axis type on the other three | each first refusal is `vertex3` at `t = 3` |

## Counterfactual And Mutation Table

1. Replace `f_L1` by Hamming parity: Hamming is a different `F_cut` map
   (it disagrees on the two-unbalanced-axis orbit) and is not this
   miss-neighborhood residual.
2. Replace off-patch occupancy `0` by a blank-block: first-wave
   candidates become undefined; that is a different census.
3. Start from a non-shared-face seed such as `(0,0,0)`: `f00` fills that
   seed; that leftover of #6448 is not a miss.
4. Report only the four missed sites: that leftover of #6448 names the
   miss list, not the first refused neighborhood.
5. Adopt `vertex3` as the physical rule: the note displays the first axis
   type and writes nothing into Admissibility.
6. Score only the `f11` run: the theorem requires independent runs of
   both maps from each shared-face miss.

## What This Does Not Claim

- No physical Admissibility selector and no adopted occupancy law.
- No Qubit rewrite and no `M_2(C)`-valued conditional probability.
- No `Z^3`-wide formation, rate, or generator.
- No identification of `f_L1` with Hamming parity.
- No leftover restatement of the four-site miss list of #6448.
- No adoption of `vertex3`.
- No blank-block or 2-site variant.

## No-Go Discipline Gate

The only negative claim is that `f00` refuses a 3-axis-contrast
neighborhood that `f11` fires, on each of the four shared-face 1-site
misses. The first refused neighborhood is an exact enumeration, not a
wall.

### N1 — materially distinct routes

| Route | Exact attack | Result and authority | Marker |
|---|---|---|---|
| orbit reconstruction | Recompute the 24 rotations and the 10 axis-type orbits. | Theorem 1 and checks `thm1-twenty-four-rotations` / `thm1-ten-orbits`. | **ATTEMPTED** |
| Hamming-as-`f_L1` | Test whether `|c|_1 mod 2` equals the unbalanced-axis predicate. | Theorem 1 and check `thm1-f-L1-not-hamming` separate the maps. | **ATTEMPTED** |
| fill versus miss | Score seed `(1,0,0)` under `f00` and under `f11`. | Theorem 1 and check `thm1-f00-miss-f11-fill`. | **ATTEMPTED** |
| lex-first refusal | Name the first `(t, x, axis type)` on seed `(1,0,0)`. | Theorem 2 and check `thm2-first-refusal`. | **ATTEMPTED** |
| other-three type | Compare first axis types on the remaining three shared-face misses. | Theorem 3 and check `thm3-other-three-same-axis-type`. | **ATTEMPTED** |
| display, do not adopt | Ask whether `vertex3` is written into Admissibility. | Theorem 3 and check `thm3-display-not-adopt-vertex3`. | **ATTEMPTED** |

### N2 — wall independence and collapse

There is one negative conclusion: `f00` refuses `vertex3` on these four
misses while `f11` fires it. Naming the first refused neighborhood and
stating that the other three share the same first axis type are two
certificates of the same 3-axis-contrast refusal, so they collapse rather
than count as two walls.

| Pair | First closes second? | Second closes first? | Disposition |
|---|---:|---:|---|
| four misses / first `vertex3` refusal | no: a miss list does not name a neighborhood | no: one neighborhood does not list the four seeds | independent exact objects |
| lex-first `(t,x,type)` / other-three type | yes: the type is the shared mechanism | no: a shared type does not name the lex-first site | collapse into the refused-axis type |
| `cov1(f00)=8` / four named misses | yes: four misses give the count | yes: the count is the size of the four-set | collapse into the miss set |
| leftover of #6448 / this first refusal | no: that leftover is the miss list | no: a miss neighborhood does not replace that list | different object |

Physical law selection is not a wall: this note makes no negative theorem
about the existence of a selector and simply does not claim one.

### N3 — hidden-condition scan

| Phrase or premise | Classification |
|---|---|
| “work on the twelve-vertex two-cube” | explicit patch hypothesis; not a `Z^3` theorem |
| off-patch occupancy `0` | explicit default; blank-block is a different rule |
| `F_cut` | explicit three-cut class; the other 992 covariant maps are excluded |
| four shared-face 1-site misses | explicit seed class; a two-site leftover is a different residual |
| “lock” | Record permanence on this Boolean occupancy model, not a possibility-valued law |
| “cube-covariant” | invariance under the 24 proper rotations, cited to Lattice/Admissibility |
| Hamming parity | displayed mutation only |
| first axis type `vertex3` | displayed mechanism, not a selected law |

### N4 — citation-to-residual matching

| Evidence path:line | Residual attacked | Residual claimed closed | Match? |
|---|---|---|---:|
| `docs/MINIMAL_AXIOMS_2026-06-29.md:37` | ambient lattice and cubic rotations | sites are `Z^3` with proper cubic rotations | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:57` | covariant nearest-neighbor rule | covariance is the class filter, not a selector | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:79` | lock permanence | a locked site stays locked | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:83` | unreadability of absence | unlocked and off-patch sites contribute occupancy `0`, not a readout | yes |
| `scripts/f_cut_k4_v30_shared_face_miss_mechanism_2026_08_15.py:95` | 24 proper rotations | signed permutations with determinant `+1` | yes |
| `scripts/f_cut_k4_v30_shared_face_miss_mechanism_2026_08_15.py:139` | `f_L1` definition | unbalanced-axis predicate, not Hamming | yes |
| `scripts/f_cut_k4_v30_shared_face_miss_mechanism_2026_08_15.py:144` | Hamming mutation | `|c|_1 mod 2` is a different map | yes |
| `scripts/f_cut_k4_v30_shared_face_miss_mechanism_2026_08_15.py:158` | `f00` definition | remaining-bit tuple `(1, 1, 1, 0, 0)` | yes |
| `scripts/f_cut_k4_v30_shared_face_miss_mechanism_2026_08_15.py:163` | `f11` definition | remaining-bit tuple `(1, 1, 1, 1, 1)` | yes |
| `scripts/f_cut_k4_v30_shared_face_miss_mechanism_2026_08_15.py:53` | 12 one-site seeds | the twelve two-cube vertices | yes |
| `scripts/f_cut_k4_v30_shared_face_miss_mechanism_2026_08_15.py:214` | independent runs | lock-step evolution from each shared-face seed | yes |
| `scripts/f_cut_k4_v30_shared_face_miss_mechanism_2026_08_15.py:266` | first refused neighborhood | earliest `(tick, site, axis type)` with `f00=0` and `f11=1` | yes |

No evidence citation is used to claim that a physical occupancy law, a
formation rate, or a `Z^3`-wide selector has been closed.

### N5 — rhetoric and resolution audit

| Resolution | Executed? | Narrow negative supported? |
|---|---:|---|
| per element | yes: all 64 neighbor 6-tuples | each is assigned its axis-type orbit; no broader cell class is classified |
| per site | yes: the twelve two-cube vertices | each uses the same six-direction stencil with off-patch occupancy `0` |
| per mode | yes: `f00` and `f11` from each shared-face miss | independent runs; `f11` fills; `f00` misses |
| per block | yes: the first refused neighborhood | tick, site, and axis type on seed `(1,0,0)`; same type on the other three |
| lattice wide | no | no `Z^3`-wide formation or Admissibility selector is asserted |

The runner prints the same five resolution statements.

### N6 — partial closure and primitive scan

The primitive registry at `docs/audit/data/axiom_premise_nodes.json` was
checked. The only dependency used is the registered `minimal_axioms` node.
Approved primitives (`scale_reference_primitive`,
`kinetic_isotropy_primitive`, `realized_state_primitive`) are unused and
are not reclassified as imports or walls. No approved primitive supplies
the Boolean occupancy maps.

One partial-closure mechanism is displayed rather than suppressed: `f00`
does lie in `F_cut` and does fill 8 of the 12 one-site seeds. That
positive member does not write `vertex3` into Admissibility. The remaining
physical choice — which, if any, `F_cut` map is the Admissibility occupancy
predicate — stays explicit.

### N7 — hostile steelman

The strongest objection is that `f00` is already known to miss four
1-site seeds because its remaining bit `vertex3` is `0`, so naming the
first refused neighborhood might be called leftover of the miss-set list
in #6448. That objection is correctly about the miss list and the
remaining-bit tuple. It does not overturn the stated theorem: the new
object is the first `(tick, site, axis type)` on seed `(1,0,0)`, together
with the statement that the other three misses share that first axis
type. Displaying `vertex3` names that mechanism. `vertex3` is not adopted.

A second steelman is that `f00` also has `mixed3=0`, so the first refusal
might have been `mixed3` rather than `vertex3`. Direct evolution on the
independent runs shows the first refused neighborhoods are `vertex3`
occupancies, not `mixed3`. Different object.

### N8 — cross-cycle echo

Repository search found nearby occupancy and covariance surfaces. They are
context, not load-bearing dependencies. The 24 rotations, 10 orbits,
`f00`, `f11`, the four shared-face misses, and the first refused
neighborhood are recomputed here.

| Earlier surface | Similar issue | Mechanism considered here |
|---|---|---|
| `docs/ADMISSIBILITY_COVARIANT_Q8_CONDITIONAL_LAW_PAIR_BOUNDED_THEOREM_NOTE_2026-08-13.md` | proper-cubic covariance of a local rule | covariance is used only as the orbit filter for Boolean maps |
| `docs/PHYSICAL_SPATIAL_BLOCK_SEAM_DICHOTOMY_CYCLE728_NOTE_2026-08-04.md` | two-cell box `{0,1,2}×{0,1}×{0,1}` | the same twelve spatial vertices are the patch; the seam cost is unused |
| `docs/MINIMAL_AXIOMS_2026-06-29.md` | one covariant nearest-neighbor rule | the axiom names the contract; this note does not select the rule |

No earlier mechanism retires the first refused neighborhood or writes
`vertex3` into Admissibility.

No-Go Discipline disposition: **PASS** for the `f00` miss / `f11` fill
reconfirm, the independent runs, and the displayed first refused
neighborhood stated above.

## Promotion value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It names the first refused neighborhood of `f00` versus `f11` on seed `(1,0,0)` by tick, site, and axis type. |
| V2 | Current main and #6448 list the four missed sites; they do not name the first refused neighborhood. |
| V3 | The two maps, four seeds, and occupancy-to-lock evolution are independently finite and exact. |
| V4 | The theorem is more than a restatement of Admissibility: it reports a displayed first refusal. |
| V5 | It is not a physical selector: `vertex3` is displayed, not adopted. |

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

The companion runner reconstructs the 24 rotations and 10 orbits, evaluates
`f00` and `f11` independently from every shared-face 1-site seed,
reconfirms that `f11` fills and `f00` misses, names the first refused
neighborhood on seed `(1,0,0)` by tick, site, and axis type, checks that
the other three misses share that first axis type, checks that `f_L1` is
not Hamming parity, and does not adopt `vertex3`. Declared audit inputs
are this note and the axiom memo. No runner cache is written.
