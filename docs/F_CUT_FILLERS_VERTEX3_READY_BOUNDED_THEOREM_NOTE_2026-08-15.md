---
claim_id: f_cut_fillers_vertex3_ready_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Among the 8 F_cut 1-site fillers, N_v31 = 4 have f(vertex3)=1. f_L1 is not unique in that subset. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_fillers_vertex3_ready_2026_08_15.py
---

# How Many Of The Eight `F_cut` Fillers Fire `vertex3`

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact bit-count of the eight `F_cut` 1-site fillers on the
complement-fixed `vertex3` orbit. The unbalanced-axis map `f_L1` is
displayed as one member of that subset. It is not adopted as the
physical Admissibility rule.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_fillers_vertex3_ready_2026_08_15.py`](../scripts/f_cut_fillers_vertex3_ready_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

The 24 proper cube rotations partition the 64 neighbor 6-tuples into 10
orbits. Cube-covariant predicates are `{0,1}`-assignments to those orbits.
The three displayed cuts `f(empty)=0`, `f(full)=0`, and `f(c)=f(1-c)`
leave five free bits, so `|F_cut|=32`. On the twelve-vertex two-cube
`{0,1,2}×{0,1}×{0,1}` from seed `(0,0,0)` with off-patch occupancy `0`,
exactly eight of those 32 maps fill (`|locks_halt|=12`). That eight-map
list is recomputed here; it is not leftover-character of a prior static
count.

`vertex3` is the complement-fixed orbit of one-from-each-axis cells: the
`+++` / cube-vertex type. Equivalently, it is the axis-type class
`(u,b,e)=(3,0,0)` of size 8. A three-axis contrast forms when `f` is `1`
on that orbit. This note does **not** run the `vertex3`-orbit *indicator*
as a member: that indicator is a different map, used only as a contrast
in a different residual.

`f_L1(c)=1` if and only if some axis is unbalanced: `c_{+μ} ≠ c_{-μ}` for
at least one `μ ∈ {x,y,z}`. Equivalently, some discrete neighbor contrast
`n_μ = c_{+μ} − c_{-μ}` is nonzero. This is **not** Hamming parity
`|c|_1 mod 2`.

**Theorem 1.** `f_L1(vertex3)=1`.

**Theorem 2.** Exactly `N_v31 = 4` of the eight `F_cut` 1-site fillers
satisfy `f(vertex3)=1`.

**Theorem 3.** So `N_v31 > 1`: `f_L1` is not unique in that subset. A
displayed second filler `f_♯` agrees with `f_L1` except that it is silent
on the mixed-triple orbit `(1,1,1)`. Displayed, not adopted.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The eight F_cut fillers are recomputed and evaluated on the vertex3 orbit. Exactly four fire vertex3. Uniqueness of f_L1 in that subset is false on this patch. No physical law is selected."
trace_class: upstream_support
target_claim_id: f_cut_fillers_vertex3_ready
target_blocker_text: "how many of the eight F_cut 1-site fillers have f(vertex3)=1, and whether f_L1 is unique in that subset"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the vertex3-ready filler count; any physical use must separately derive an Admissibility selector"
conditional_surface_status: "exact for the eight F_cut fillers on this twelve-vertex patch with off-patch o=0; no Z^3-wide law and no physical selector"
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
- the 1-site seed `(0,0,0)`.

No observational comparator, literature constant, Wilson weight, rate, or
generator is imported. No Record scalar functional appears.

Not leftover-character of the vertex3-orbit-indicator member. That residual
asks whether the indicator of `vertex3` itself fills. This residual asks how
many of the eight fillers assign `1` to that orbit.

## Exact Target And Objects

**Target.** Among the eight `F_cut` maps that fill the two-cube from a
1-site seed, count those with `f(vertex3)=1`, and decide uniqueness of
`f_L1` inside that subset.

Write a neighbor configuration as `c ∈ {0,1}^6`. A proper cube rotation `R`
acts by `(R·c)(d) = c(R^{-1}d)` on the six face directions `d`. A map
`f:{0,1}^6 → {0,1}` is cube-covariant when `f(R·c)=f(c)` for every such `R`.

The axis type of `c` is the triple `(u,b,e)` with `u+b+e=3`, where `u` is
the number of axes with `c_{+} ≠ c_{-}`, `b` the number with
`(c_{+},c_{-})=(1,1)`, and `e` the number with `(c_{+},c_{-})=(0,0)`. These
ten types are exactly the ten orbits. Complement sends `(u,b,e)` to
`(u,e,b)`.

`vertex3` is the orbit of the cell with occupied slots `+x,+y,+z` and of
every proper-rotation image of that cell. That orbit is exactly the class
`(3,0,0)`, of size 8. It is complement-fixed: complement of a
one-from-each-axis cell is again one-from-each-axis.

`F_cut` is the class of cube-covariant maps with `f(empty)=f(full)=0` and
`f(c)=f(1-c)`. The empty/full pair is forced to `0`. The remaining free
data are three complement-pair bits and two complement-fixed orbit bits
(mixed triple `(1,1,1)` and `vertex3`), so `|F_cut|=32`.

On the two-cube, seed `(0,0,0)` starts locked. Off-patch neighbors have
occupancy `0`. Each tick, every unlocked on-patch vertex evaluates `f` on
its six-neighbor occupancy tuple and locks if `f=1`. Fill means
`|locks_halt|=12`. The eight fillers are the members of `F_cut` that fill.

Define

```text
f_L1(c)     = 1  iff  u(c) ≥ 1,
f_♯(c)      = 1  iff  u(c) ≥ 1 and (u,b,e) ≠ (1,1,1),
f_H(c)      = |c|_1 mod 2.
```

`f_L1` and `f_♯` both lie in `F_cut` and both fill. `f_H` is a displayed
mutation only: it is not `f_L1`. `f_♯` is a displayed second
`vertex3`-ready filler: it is not adopted.

`N_v31` is the number of the eight fillers with `f(vertex3)=1`.

## Theorems

**Theorem 1.** The unbalanced-axis map `f_L1` is one of the eight `F_cut`
1-site fillers. It is not Hamming parity. Every `vertex3` cell has three
unbalanced axes, so `f_L1(vertex3)=1`. Lock cardinalities of `f_L1` on
this patch are `(1,4,8,11,12)` and the halt tick is `4`.

**Theorem 2.** Exhaustive evaluation of the eight fillers on the `vertex3`
orbit gives

```text
N_v31 = 4.
```

**Theorem 3.** So `N_v31 > 1`. The map `f_L1` fires `vertex3`, but it is
not unique in that subset. The displayed second filler `f_♯` is distinct
from `f_L1` (they disagree on the mixed-triple orbit) and also fires
`vertex3` and fills, with the same lock cardinalities `(1,4,8,11,12)` and
halt tick `4`. Displayed, not adopted.

## Proof-Obligation Graph

| obligation | exact disposition |
|---|---|
| 24 proper cube rotations | signed permutations of the three axes with determinant `+1` |
| 10 orbits on `{0,1}^6` | axis-type classes `(u,b,e)` partition the 64 cells |
| `|F_cut|=32` | three complement-pairs and two complement-fixed orbits remain free |
| eight fillers | exhaustive 32-run census of `F_cut` to a twelve-lock halt |
| `vertex3` orbit | complement-fixed class `(3,0,0)` of the `+++` cell; size 8 |
| `f_L1` is unbalanced-axis | `u ≥ 1`, not Hamming `|c|_1 mod 2` |
| `f_L1(vertex3)=1` | `u=3` on every `vertex3` cell |
| `N_v31` | four of the eight fillers assign `1` to `vertex3` |
| uniqueness of `f_L1` in that subset | false; `f_♯` is an explicit second `vertex3`-ready filler |
| physical Admissibility selection | open and not claimed |

Every leaf needed for the stated bit-count is discharged. No `Z^3`-wide
formation law is claimed.

## Mutations

1. Replace `f_L1` by Hamming `|c|_1 mod 2`: the maps disagree on the
   two-unbalanced-axis orbit, and Hamming is not a filler.
2. Replace the bit `f(vertex3)` by the `vertex3`-orbit *indicator* as a
   member: that is a different residual (one map's dynamics, not a count
   among the eight fillers).
3. Drop complement-even or the vanish cuts: the class is no longer
   `F_cut` and the eight-map list changes.
4. Seed a second on-patch site: the filler list can change.
5. Assert `N_v31=1`: the explicit second filler `f_♯` refutes uniqueness.

## What This Does Not Claim

- No physical Admissibility selector and no adopted occupancy law.
- No Qubit rewrite and no `M_2(C)`-valued conditional probability.
- No `Z^3`-wide formation, rate, or generator.
- No identification of `f_L1` with Hamming parity.
- No leftover-character of the vertex3-orbit-indicator member in place of
  this filler-bit count.
- No blank-block, 2-site, or 3-site variant.

## No-Go Discipline Gate

The only negative claim is uniqueness: `f_L1` is not the unique `F_cut`
filler with `f(vertex3)=1`. The positive count `N_v31=4` is an exact
enumeration, not a wall.

### N1 — materially distinct routes

| Route | Exact attack | Result and authority | Marker |
|---|---|---|---|
| orbit reconstruction | Recompute the 24 rotations and identify `vertex3` as `(3,0,0)`. | Theorem 1 and check `thm1-vertex3-orbit`. | **ATTEMPTED** |
| `f_L1` on `vertex3` | Evaluate the unbalanced-axis predicate on every `vertex3` cell. | Theorem 1 and check `thm1-f-L1-fires-vertex3`. | **ATTEMPTED** |
| Hamming-as-`f_L1` | Test whether `|c|_1 mod 2` equals the unbalanced-axis predicate. | Theorem 1 and check `thm1-f-L1-not-hamming` separate the maps. | **ATTEMPTED** |
| eight-filler census | Rebuild `F_cut` and retain the maps that fill. | Theorem 1 and check `thm1-f-L1-is-filler` give eight fillers. | **ATTEMPTED** |
| `vertex3`-ready count | Evaluate each filler on the `vertex3` orbit. | Theorem 2 and check `thm2-n-v31` give `N_v31 = 4`. | **ATTEMPTED** |
| uniqueness of `f_L1` | Ask whether the `vertex3`-ready filler class is a singleton. | Theorem 3 and checks `thm3-not-unique` / `thm3-displayed-other-filler`. | **ATTEMPTED** |

### N2 — wall independence and collapse

There is one negative conclusion: uniqueness fails. The explicit second
filler and the cardinality `N_v31=4` are two certificates of the same
non-uniqueness, so they collapse rather than count as two walls.

| Pair | First closes second? | Second closes first? | Disposition |
|---|---:|---:|---|
| `N_v31=4` / displayed `f_♯` | yes: a count larger than one is non-uniqueness | yes: one extra filler is non-uniqueness | collapse into the uniqueness failure |
| `f_L1(vertex3)=1` / Hamming differs | no: firing `vertex3` does not classify Hamming | no: Hamming differing does not evaluate `f_L1` on `vertex3` | independent positive/negative members, not two walls |
| eight-filler list / `N_v31` | no: filling is not the `vertex3` bit | no: a bit-count does not replace the fill census | separate exact counts |

Physical law selection is not a wall: this note makes no negative theorem
about the existence of a selector and simply does not claim one.

### N3 — hidden-condition scan

| Phrase or premise | Classification |
|---|---|
| “work on the twelve-vertex two-cube” | explicit patch hypothesis; not a `Z^3` theorem |
| off-patch occupancy `0` | explicit default; blank-block is a different rule |
| `F_cut` | explicit three-cut class; the other 992 covariant maps are excluded |
| eight fillers | explicit fill-halt subclass of `F_cut` |
| `vertex3` | explicit complement-fixed orbit `(3,0,0)`, not the indicator member |
| “lock” | Record permanence on this Boolean occupancy model, not a possibility-valued law |
| “cube-covariant” | invariance under the 24 proper rotations, cited to Lattice/Admissibility |
| Hamming parity | displayed mutation only |
| `f_♯` | displayed witness against uniqueness, not a selected law |

### N4 — citation-to-residual matching

| Evidence path:line | Residual attacked | Residual claimed closed | Match? |
|---|---|---|---:|
| `docs/MINIMAL_AXIOMS_2026-06-29.md:37` | ambient lattice and cubic rotations | sites are `Z^3` with proper cubic rotations | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:57` | covariant nearest-neighbor rule | covariance is the class filter, not a selector | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:79` | lock permanence | a locked site stays locked | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:83` | unreadability of absence | unlocked and off-patch sites contribute occupancy `0`, not a readout | yes |
| `scripts/f_cut_fillers_vertex3_ready_2026_08_15.py:61` | 24 proper rotations | signed permutations with determinant `+1` | yes |
| `scripts/f_cut_fillers_vertex3_ready_2026_08_15.py:105` | `f_L1` definition | unbalanced-axis predicate, not Hamming | yes |
| `scripts/f_cut_fillers_vertex3_ready_2026_08_15.py:110` | Hamming mutation | `|c|_1 mod 2` is a different map | yes |
| `scripts/f_cut_fillers_vertex3_ready_2026_08_15.py:114` | uniqueness | displayed second filler `f_♯` | yes |
| `scripts/f_cut_fillers_vertex3_ready_2026_08_15.py:249` | class census | exact `N_v31` on the eight fillers | yes |

No evidence citation is used to claim that a physical occupancy law, a
formation rate, or a `Z^3`-wide selector has been closed.

### N5 — rhetoric and resolution audit

| Resolution | Executed? | Narrow negative supported? |
|---|---:|---|
| per element | yes: all 64 neighbor 6-tuples | each is assigned its axis-type orbit; no broader cell class is classified |
| per site | yes: the twelve two-cube vertices | each uses the same six-direction stencil with off-patch occupancy `0` |
| per mode | yes: every `F_cut` filler | the census is this class on this seed; other seeds are unclaimed |
| per block | yes: the pair `(8, N_v31)` | uniqueness fails because `N_v31=4` |
| lattice wide | no | no `Z^3`-wide formation or Admissibility selector is asserted |

The runner prints the same five resolution statements.

### N6 — partial closure and primitive scan

The primitive registry at `docs/audit/data/axiom_premise_nodes.json` was
checked. The only dependency used is the registered `minimal_axioms` node.
No approved primitive supplies the Boolean occupancy maps, and none is
reclassified as an import or wall.

One partial-closure mechanism is displayed rather than suppressed: `f_L1`
does fire `vertex3` and does fill this patch from the 1-site seed. That
positive member does not make `f_L1` unique among `vertex3`-ready fillers
and does not select it as the physical rule. The remaining physical
choice — which, if any, `F_cut` map is the Admissibility occupancy
predicate — stays explicit.

### N7 — hostile steelman

The strongest objection is that `vertex3` cells need not appear on every
1-site filling trajectory, so uniqueness of `f_L1` might be restored by
restricting to “dynamically occurring” cells. That objection is correctly
about a smaller class. It does not overturn the stated theorem: among the
eight maps in `F_cut` that fill, four assign `1` to the `vertex3` orbit.
The displayed second filler `f_♯` already differs from `f_L1` on the
mixed-triple orbit, fires `vertex3`, and fills. That is a class-level
extra filler, not a trajectory-level identity.

### N8 — cross-cycle echo

Repository search found nearby occupancy and covariance surfaces. They are
context, not load-bearing dependencies. The 24 rotations, 10 orbits,
`F_cut`, the eight fillers, and the `vertex3` bit are recomputed here.

| Earlier surface | Similar issue | Mechanism considered here |
|---|---|---|
| `docs/ADMISSIBILITY_COVARIANT_Q8_CONDITIONAL_LAW_PAIR_BOUNDED_THEOREM_NOTE_2026-08-13.md` | proper-cubic covariance of a local rule | covariance is used only as the orbit filter for Boolean maps |
| `docs/PHYSICAL_SPATIAL_BLOCK_SEAM_DICHOTOMY_CYCLE728_NOTE_2026-08-04.md` | two-cell box `{0,1,2}×{0,1}×{0,1}` | the same twelve spatial vertices are the patch; the seam cost is unused |
| `docs/MINIMAL_AXIOMS_2026-06-29.md` | one covariant nearest-neighbor rule | the axiom names the contract; this note does not select the rule |

No earlier mechanism retires the `vertex3`-ready filler count or restores
uniqueness of `f_L1` inside that four-map subset.

No-Go Discipline disposition: **PASS** for the uniqueness failure and the
exact count `N_v31` stated above.

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
`F_cut`, identifies the eight 1-site fillers, evaluates `f(vertex3)` on
each, reports `N_v31 = 4`, checks that `f_L1` fires `vertex3` and is not
Hamming parity, and exhibits the displayed second filler `f_♯`. Declared
audit inputs are this note and the axiom memo. No runner cache is written.
