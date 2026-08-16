---
claim_id: f_cut_wt1_zero_opp2_miss_mechanism_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On the two-cube with off-patch o=0, the first neighborhood at which F_cut (0,0,1,1,1) refuses and (0,1,1,1,1) fires, on seed {(0,0,0),(0,1,1),(2,0,0)}, is reported by tick, site, and axis type. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_wt1_zero_opp2_miss_mechanism_2026_08_15.py
---

# First Refused Neighborhood On The wt1=0 Opp2 Split Seed

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** independent occupancy-to-lock runs from the displayed 3-site
seed `S = {(0,0,0),(0,1,1),(2,0,0)}` on the twelve-vertex two-cube
`{0,1,2}×{0,1}×{0,1}` with off-patch occupancy `0`. The map `f00` with
remaining-bit tuple `(0, 0, 1, 1, 1)` does not fill `S`. The map `f10`
with remaining-bit tuple `(0, 1, 1, 1, 1)` fills `S`. On `S`, the first
neighborhood at which `f00=0` and `f10=1` is reported by tick, site, and
axis type. That type is `opp2`, the remaining bit that splits the pair.
Displayed, not adopted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_wt1_zero_opp2_miss_mechanism_2026_08_15.py`](../scripts/f_cut_wt1_zero_opp2_miss_mechanism_2026_08_15.py)
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

On the two-cube `{0,1,2}×{0,1}×{0,1}`, off-patch neighbors have occupancy
`0`. Each tick, every unlocked on-patch vertex evaluates `f` on its
six-neighbor occupancy tuple and locks if `f=1`. The process is
synchronous and stops at a fixed point in at most 12 ticks. Fill means
`|locks_halt|=12`. Tick `t = 1` is the first evaluation on the seed
occupancy.

`f_L1(c)=1` if and only if some axis is unbalanced: `c_{+μ} ≠ c_{-μ}` for
at least one `μ ∈ {x,y,z}`. Equivalently, some discrete neighbor contrast
`n_μ = c_{+μ} − c_{-μ}` is nonzero. This is **not** Hamming parity
`|c|_1 mod 2`. The remaining-bit tuple of `f_L1` is
`(wt1, opp2, adj2, vertex3, mixed3) = (1, 0, 1, 1, 1)`.

Write `f00` for the `F_cut` map with remaining-bit tuple `(0, 0, 1, 1, 1)`
and `f10` for `(0, 1, 1, 1, 1)`. Both maps have `wt1=0`. They differ only
on `opp2`. Neither map is adopted.

New mechanism. Not leftover of #6486 (fill-bit only): that leftover names
that `f10` fills `S` and `f00` misses, a pair of fill bits. This residual
is the first refused neighborhood on that same seed.

**Theorem 1.** Independent recomputation from

```text
S = {(0,0,0),(0,1,1),(2,0,0)}
```

gives lock-count history `(3, 5)` for `f00` (halt at five locks; does not
fill) and history `(3, 6, 8, 11, 12)` for `f10` (fills). The first wave of
`f00` is `{(0,0,1),(0,1,0)}`. The first wave of `f10` is
`{(0,0,1),(0,1,0),(1,0,0)}`.

**Theorem 2.** On that seed `S`, the first neighborhood at which `f00`
refuses and `f10` fires is

```text
t = 1
x = (1, 0, 0)
axis type = opp2 = (0, 1, 2)
```

The six-neighbor occupancy is `(1, 1, 0, 0, 0, 0)`: both ends of the `x`
axis occupied, the `y` and `z` axes empty. That is the `opp2` orbit. The
same first event is seen on the independent `f00` run and on the
independent `f10` run. There is one such event at that tick.

**Theorem 3.** That type is `opp2`, the remaining bit that splits `f00`
from `f10`. Display. Do not adopt opp2.
Do not write it into Admissibility.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The independent f00 miss and f10 fill of S, and the first refused neighborhood on that seed (tick, site, axis type), are enumerated. opp2 is displayed, not written into Admissibility."
trace_class: frontier_discovery
target_claim_id: f_cut_wt1_zero_opp2_miss_mechanism
target_blocker_text: "the first neighborhood at which f00 refuses and f10 fires, on the #6484/#6486 split seed, remains unnamed"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the displayed first refused neighborhood; any physical use must separately derive an Admissibility selector"
conditional_surface_status: "exact for f00 and f10 on this twelve-vertex patch with off-patch o=0 and the displayed 3-site seed; no Z^3-wide law and no physical selector"
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
- the displayed 3-site seed `{(0,0,0),(0,1,1),(2,0,0)}`;
- independent lock-step runs of `f00` and of `f10` from that seed.

No observational comparator, literature constant, Wilson weight, rate, or
generator is imported. No Record scalar functional appears.

New mechanism. Not leftover of #6486. That leftover is fill-bit only:
`f10` fills and `f00` misses. This residual is the first refused
neighborhood on the same seed. It is not an `N_orb` count. The first axis
type being `opp2` identifies the remaining bit that splits `f00` from
`f10` and does not adopt that bit.

## Exact Target And Objects

**Target.** Reconfirm that `f10` fills `S` and `f00` does not, with the
displayed lock-count histories. Name the first `(tick, site, axis type)`
at which `f00` refuses and `f10` fires on `S`. Display whether that type
is `opp2`.

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
f00(c)  = remaining-value of (0, 0, 1, 1, 1),
f10(c)  = remaining-value of (0, 1, 1, 1, 1),
f_L1(c) = 1  iff  u(c) ≥ 1.
```

So `f00` has remaining-bit tuple `(0, 0, 1, 1, 1)`, `f10` has
`(0, 1, 1, 1, 1)`, and `f_L1` has `(1, 0, 1, 1, 1)`. The maps `f00` and
`f10` differ only on `opp2`. Neither map is adopted.

A locked set `L` determines occupancies: a lattice neighbor in `L` has
occupancy `1`, and every other neighbor — including every off-patch
neighbor — has occupancy `0`. One synchronous tick replaces `L` by

```text
L ∪ { v in two-cube \ L : f(neighborhood_6(v; L)) = 1 }.
```

An independent run of `f` from a seed is that iteration started at the
seed and continued to a fixed point. The first refused neighborhood on a
run is the lexicographically first unlocked site, at the earliest tick,
whose neighborhood has `f00=0` and `f10=1`. Tick `t = 1` is the first
evaluation on the seed occupancy.

## Theorems

**Theorem 1.** There are exactly 24 proper cube rotations and exactly 10
orbits on `{0,1}^6`. The opp2-silent map `f00` is one element of
`F_cut`. The unbalanced-axis map `f_L1` is a different element; it is
not Hamming parity. On the twelve-vertex two-cube with off-patch
occupancy `0`, independent runs from
`S = {(0,0,0),(0,1,1),(2,0,0)}` give history `(3, 5)` for `f00` (does
not fill) and history `(3, 6, 8, 11, 12)` for `f10` (fills).

**Theorem 2.** On that seed, the first neighborhood with
`f00(nbhd)=0` and `f10(nbhd)=1` is tick `t = 1`, site `(1, 0, 0)`,
axis type `opp2` `= (0, 1, 2)`. The occupancy is
`(1, 1, 0, 0, 0, 0)`.

**Theorem 3.** That type is `opp2`, the bit that splits `f00` from
`f10`. Display. Do not adopt opp2. Do not write it into
Admissibility. The first refused neighborhood is a displayed census
output, not a selected occupancy law.

## Proof-Obligation Graph

| obligation | exact disposition |
|---|---|
| 24 proper cube rotations | signed permutations of the three axes with determinant `+1` |
| 10 orbits on `{0,1}^6` | axis-type classes `(u,b,e)` partition the 64 cells with the listed sizes |
| `f00` is in `F_cut` | remaining bits `(0, 0, 1, 1, 1)`; silent on `wt1` and `opp2` and their complements |
| `f_L1` is not Hamming | the two-unbalanced-axis orbit has even weight and `f_L1=1` |
| `f10` fills `S` | independent run from `S` fills with history `(3, 6, 8, 11, 12)` |
| `f00` misses `S` | independent run from `S` halts with history `(3, 5)` |
| two-cube has twelve vertices | `{0,1,2}×{0,1}×{0,1}` |
| off-patch occupancy `0` | declared stencil default; not a blank-block |
| first refused neighborhood | `t = 1`, site `(1, 0, 0)`, axis type `opp2` on `S` |
| type is opp2 | first axis type is `opp2`; displayed, not adopted |

## Counterfactual And Mutation Table

1. Replace `f_L1` by Hamming parity: Hamming is a different `F_cut` map
   (it disagrees on the two-unbalanced-axis orbit) and is not this
   miss-neighborhood residual.
2. Replace off-patch occupancy `0` by a blank-block: first-wave
   candidates become undefined; that is a different census.
3. Report only the fill bits of `f00` and `f10` on `S`: that leftover
   is #6486 (fill-bit only), not the first refused neighborhood.
4. Adopt `opp2` as the physical rule: the note displays the first axis
   type and writes nothing into Admissibility.
5. Score only the `f10` run: the theorem requires independent runs of
   both maps from `S`.
6. Treat a later tick as first: on `S` the first refusal is at `t = 1`
   on the seed occupancy itself.
7. Identify the extra with `mixed3`: both maps fire `mixed3`, so the
   first `f00=0` and `f10=1` neighborhood cannot be `mixed3`.

## What This Does Not Claim

- No physical Admissibility selector and no adopted occupancy law.
- No Qubit rewrite and no `M_2(C)`-valued conditional probability.
- No `Z^3`-wide formation, rate, or generator.
- No identification of `f_L1` with Hamming parity.
- No leftover restatement of the #6486 fill-bit pair.
- No `N_orb` count of missed seeds.
- No adoption of `opp2` or of `wt1`.
- No blank-block or 2-site variant as the claimed object.

## No-Go Discipline Gate

The only negative claim is that `f00` refuses an `opp2` neighborhood that
`f10` fires, on the displayed 3-site seed. The first refused neighborhood
is an exact enumeration, not a wall.

### N1 — materially distinct routes

| Route | Exact attack | Result and authority | Marker |
|---|---|---|---|
| orbit reconstruction | Recompute the 24 rotations and the 10 axis-type orbits. | Theorem 1 and checks `thm1-twenty-four-rotations` / `thm1-ten-orbits`. | **ATTEMPTED** |
| Hamming-as-`f_L1` | Test whether `|c|_1 mod 2` equals the unbalanced-axis predicate. | Theorem 1 and check `thm1-f-L1-not-hamming` separate the maps. | **ATTEMPTED** |
| fill reconfirm | Run `f00` and `f10` independently from `S`. | Theorem 1 and check `thm1-f10-fills-f00-misses`. | **ATTEMPTED** |
| first refusal | Name the first `(t, x, axis type)` on `{(0,0,0),(0,1,1),(2,0,0)}`. | Theorem 2 and check `thm2-first-refusal`. | **ATTEMPTED** |
| opp2 versus mixed3 | Ask whether that first type is opp2 or mixed3. | Theorem 3 and check `thm3-type-is-opp2`. | **ATTEMPTED** |
| display, do not adopt | Ask whether a remaining bit is written into Admissibility. | Theorem 3 and check `thm3-display-not-adopt-opp2`. | **ATTEMPTED** |

### N2 — wall independence and collapse

There is one negative conclusion: `f00` refuses `opp2` on `S` while
`f10` fires it. Naming the miss history and naming the first refused
neighborhood are two certificates of that opp2-silent refusal, so they
collapse rather than count as two walls.

| Pair | First closes second? | Second closes first? | Disposition |
|---|---:|---:|---|
| history `(3, 5)` / first `opp2` refusal | no: a miss history does not name a neighborhood | no: one neighborhood does not give the halt history | independent exact objects |
| first `(t,x,type)` / type-is-opp2 | yes: the type is `opp2` | no: naming the splitter bit does not name the site | collapse into the refused-axis type |
| `f10` fills `S` / first extra lock `(1,0,0)` | no: a fill does not name the first extra site | no: one extra lock does not fill the patch | independent exact objects |
| #6486 fill bits / this first refusal | no: fill bits do not name a tick or a type | no: this first type is `opp2` | different extras |

Physical law selection is not a wall: this note makes no negative theorem
about the existence of a selector and simply does not claim one.

### N3 — hidden-condition scan

| Phrase or premise | Classification |
|---|---|
| “work on the twelve-vertex two-cube” | explicit patch hypothesis; not a `Z^3` theorem |
| off-patch occupancy `0` | explicit default; blank-block is a different rule |
| `F_cut` | explicit three-cut class; the other 992 covariant maps are excluded |
| displayed 3-site seed | explicit seed; a two-site miss list is a different residual |
| “lock” | Record permanence on this Boolean occupancy model, not a possibility-valued law |
| “cube-covariant” | invariance under the 24 proper rotations, cited to Lattice/Admissibility |
| Hamming parity | displayed mutation only |
| first axis type `opp2` | displayed mechanism, not a selected law |

### N4 — citation-to-residual matching

| Evidence path:line | Residual attacked | Residual claimed closed | Match? |
|---|---|---|---:|
| `docs/MINIMAL_AXIOMS_2026-06-29.md:37` | ambient lattice and cubic rotations | sites are `Z^3` with proper cubic rotations | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:57` | covariant nearest-neighbor rule | covariance is the class filter, not a selector | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:79` | lock permanence | a locked site stays locked | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:83` | unreadability of absence | unlocked and off-patch sites contribute occupancy `0`, not a readout | yes |
| `scripts/f_cut_wt1_zero_opp2_miss_mechanism_2026_08_15.py:94` | 24 proper rotations | signed permutations with determinant `+1` | yes |
| `scripts/f_cut_wt1_zero_opp2_miss_mechanism_2026_08_15.py:138` | `f_L1` definition | unbalanced-axis predicate, not Hamming | yes |
| `scripts/f_cut_wt1_zero_opp2_miss_mechanism_2026_08_15.py:143` | Hamming mutation | `|c|_1 mod 2` is a different map | yes |
| `scripts/f_cut_wt1_zero_opp2_miss_mechanism_2026_08_15.py:157` | `f00` definition | remaining-bit tuple `(0, 0, 1, 1, 1)` | yes |
| `scripts/f_cut_wt1_zero_opp2_miss_mechanism_2026_08_15.py:162` | `f10` definition | remaining-bit tuple `(0, 1, 1, 1, 1)` | yes |
| `scripts/f_cut_wt1_zero_opp2_miss_mechanism_2026_08_15.py:53` | displayed seed | `{(0,0,0),(0,1,1),(2,0,0)}` | yes |
| `scripts/f_cut_wt1_zero_opp2_miss_mechanism_2026_08_15.py:213` | independent runs | lock-step evolution from the displayed seed | yes |
| `scripts/f_cut_wt1_zero_opp2_miss_mechanism_2026_08_15.py:256` | first refused neighborhood | earliest `(tick, site, axis type)` with `f00=0` and `f10=1` | yes |

No evidence citation is used to claim that a physical occupancy law, a
formation rate, or a `Z^3`-wide selector has been closed.

### N5 — rhetoric and resolution audit

| Resolution | Executed? | Narrow negative supported? |
|---|---:|---|
| per element | yes: all 64 neighbor 6-tuples | each is assigned its axis-type orbit; no broader cell class is classified |
| per site | yes: the twelve two-cube vertices | each uses the same six-direction stencil with off-patch occupancy `0` |
| per mode | yes: `f00` and `f10` from the displayed seed | independent runs; `f10` fills; `f00` misses |
| per block | yes: the first refused neighborhood | tick, site, and axis type on the displayed seed |
| lattice wide | no | no `Z^3`-wide formation or Admissibility selector is asserted |

The runner prints the same five resolution statements.

### N6 — partial closure and primitive scan

The primitive registry at `docs/audit/data/axiom_premise_nodes.json` was
checked. The only dependency used is the registered `minimal_axioms` node.
No approved primitive supplies the Boolean occupancy maps, and none is
reclassified as an import or wall. The scale-reference, kinetic-isotropy,
and realized-state primitives are unused.

One partial-closure mechanism is displayed rather than suppressed: `f00`
does lie in `F_cut` and does fire `adj2`, `vertex3`, and `mixed3`. That
positive member does not make `f00` fill `S` and does not write `opp2`
into Admissibility. The remaining physical choice — which, if any,
`F_cut` map is the Admissibility occupancy predicate — stays explicit.

### N7 — hostile steelman

The strongest objection is that `f00` and `f10` differ only on the
`opp2` remaining bit, so the first neighborhood with `f00=0` and
`f10=1` is forced to be `opp2` by the remaining-bit tuple, and naming
it might be called leftover-character of that tuple or of the #6486
fill-bit pair. That objection is correctly about the bit assignment
and the fill bits. It does not overturn the stated theorem: the new
object is the first `(tick, site, axis type)` on the displayed 3-site
seed `f00` does not fill. Displaying `opp2` names that mechanism. No
bit is adopted.

A second steelman is that history `(3, 5)` already encodes the miss, so
the first refused neighborhood is leftover of the miss history. The
miss history does not name a tick, a site, or an axis type. Those three
coordinates were unnamed.

### N8 — cross-cycle echo

Repository search found nearby occupancy and covariance surfaces. They are
context, not load-bearing dependencies. The 24 rotations, 10 orbits,
`f00`, `f10`, the two lock histories, and the first refused neighborhood
are recomputed here.

| Earlier surface | Similar issue | Mechanism considered here |
|---|---|---|
| `docs/ADMISSIBILITY_COVARIANT_Q8_CONDITIONAL_LAW_PAIR_BOUNDED_THEOREM_NOTE_2026-08-13.md` | proper-cubic covariance of a local rule | covariance is used only as the orbit filter for Boolean maps |
| `docs/PHYSICAL_SPATIAL_BLOCK_SEAM_DICHOTOMY_CYCLE728_NOTE_2026-08-04.md` | two-cell box `{0,1,2}×{0,1}×{0,1}` | the same twelve spatial vertices are the patch; the seam cost is unused |
| `docs/MINIMAL_AXIOMS_2026-06-29.md` | one covariant nearest-neighbor rule | the axiom names the contract; this note does not select the rule |

No earlier mechanism retires the first refused neighborhood of `f00` on
this seed or writes `opp2` into Admissibility.

No-Go Discipline disposition: **PASS** for the independent `f10` fill of
`S`, the independent `f00` miss, and the displayed first refused
neighborhood stated above.

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
`f00` and `f10` independently from the displayed 3-site seed, reports that
`f10` fills and `f00` misses with the displayed histories, names the first
refused neighborhood on that seed by tick, site, and axis type, checks that
the type is `opp2`, checks that `f_L1` is not Hamming parity, and
does not adopt a bit. Declared audit inputs are this note and the axiom
memo. No runner cache is written.
