---
claim_id: f_cut_mix0_line_seed_fill_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On the two-cube with off-patch o=0, the F_cut map with remaining bits (1,0,1,1,0) does fill from the 3-site long-axis seed. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_mix0_line_seed_fill_2026_08_15.py
---

# Does `f_mix0` Fill From The 3-Site Long-Axis Seed

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact fill of the `F_cut` rival `f_mix0` with remaining bits
`(1,0,1,1,0)` from the displayed 3-site long-axis seed on the
twelve-vertex two-cube with off-patch occupancy `0`. The map is
displayed, not adopted as the physical Admissibility rule.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_mix0_line_seed_fill_2026_08_15.py`](../scripts/f_cut_mix0_line_seed_fill_2026_08_15.py)
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
`|locks_halt|=12`.

The displayed `F_cut` rival is the remaining-bit tuple

```text
(wt1, opp2, adj2, vertex3, mixed3) = (1, 0, 1, 1, 0)
```

with complements forced. Call that map `f_mix0`. It is L1 with
`mixed3=0`. It fills from 1-site, from the face-diagonal 2-site, and from
`S*` like L1 (#6415/#6424). Its 1-site history from `(0,0,0)` is
`(1, 4, 8, 11, 12)`, the same tuple as L1. Those 1-site, face-diagonal,
and `S*` fills are leftover-character of #6415/#6424. They are not the
residual of this note.

This note asks a new map question on the remaining displayed seed: whether
`f_mix0` fills from the 3-site long-axis seed

```text
S = {(0,0,0), (1,0,0), (2,0,0)}.
```

Not leftover-character of #6419. That surface was the line-seed fill of
`f_cutmin` (tuple `(1,0,1,0,0)`). This note is the same seed on a
different remaining-bit map.

`f_L1(c)=1` if and only if some axis is unbalanced: `c_{+μ} ≠ c_{-μ}` for
at least one `μ ∈ {x,y,z}`. Equivalently, some discrete neighbor contrast
`n_μ = c_{+μ} − c_{-μ}` is nonzero. This is **not** Hamming parity
`|c|_1 mod 2`. On this same seed, `f_L1` fills with lock history
`(3, 9, 12)` (#6408). `f_L1` is the 10-orbit reading `n ≠ 0`, not Hamming.

**Theorem 1.** `f_L1` fills from `S` with lock history `(3, 9, 12)`.

**Theorem 2.** `f_mix0` fills from `S`. Halt locks, halt tick, and lock
history are

```text
|locks_halt| = 12
T = 2
history = (3, 9, 12)
```

**Theorem 3.** On this seed the two maps share the lock-history tuple
`(3, 9, 12)`. They differ on the remaining bit `mixed3`: L1 has
`mixed3=1` and `f_mix0` has `mixed3=0`. Displayed, not adopted.
Do not write `f_mix0` into Admissibility.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "On the twelve-vertex two-cube with off-patch o=0, the F_cut rival f_mix0 with remaining bits (1,0,1,1,0) is reconstructed and run from the 3-site long-axis seed. Halt locks, T, and lock history are enumerated. The map is displayed, not written into Admissibility."
trace_class: upstream_support
target_claim_id: f_cut_mix0_line_seed_fill
target_blocker_text: "whether the F_cut map with remaining bits (1,0,1,1,0) fills from the 3-site long-axis seed"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the line-seed fill; any physical use must separately derive an Admissibility selector"
conditional_surface_status: "exact for f_mix0 and f_L1 on this twelve-vertex patch with off-patch o=0 and seed S; no Z^3-wide law and no physical selector"
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
- the 3-site long-axis seed `S = {(0,0,0),(1,0,0),(2,0,0)}`;
- the named remaining bits `wt1`, `opp2`, `adj2`, `vertex3`, `mixed3`;
- the displayed map `f_mix0` with tuple `(1,0,1,1,0)`.

No observational comparator, literature constant, Wilson weight, rate, or
generator is imported. No Record scalar functional appears.

Not leftover-character of #6419 (`f_cutmin` on this same seed). That
surface is the line-seed fill of the unique support-36 1-site filler.
This note is the fill of `f_mix0` from the remaining displayed seed.

## Exact Target And Objects

**Target.** Run `f_mix0` from `S` on the two-cube with off-patch occupancy
`0`. Report halt locks, halt tick `T`, and the lock-history tuple. State
whether the run fills. Compare the history to `f_L1` on the same seed.

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

Start locked equals `S`, not a 1-site seed. Fill from `S` means the halt
set has cardinality 12.

Do not write f_mix0 into Admissibility.
Do not write `f_mix0` into Admissibility.

## Theorems

**Theorem 1.** There are exactly 24 proper cube rotations and exactly 10
orbits on `{0,1}^6`. The three cuts leave `|F_cut|=32`. The unbalanced-axis
map `f_L1` is not Hamming parity. Started from `S` with off-patch occupancy
`0`, `f_L1` fills the twelve-vertex two-cube. Its lock cardinalities are
`(3, 9, 12)` and its halt tick is `2`.

**Theorem 2.** Reconstructing the eight `F_cut` 1-site fillers isolates
the remaining-bit member `f_mix0` with tuple `(1,0,1,1,0)`. Its 1-site
history is `(1, 4, 8, 11, 12)`. Started from `S` with off-patch occupancy
`0`, the same map fills:

```text
|locks_halt| = 12
T = 2
history = (3, 9, 12)
```

**Theorem 3.** The line-seed histories of `f_mix0` and `f_L1` are equal.
The remaining bits are not: `mixed3` is `0` on `f_mix0` and `1` on L1.
The common line-seed history is displayed, not adopted. `f_mix0` is not
an Admissibility clause.

## Proof-Obligation Graph

| obligation | exact disposition |
|---|---|
| 24 proper cube rotations | signed permutations of the three axes with determinant `+1` |
| 10 orbits on `{0,1}^6` | axis-type classes `(u,b,e)` partition the 64 cells with the listed sizes |
| `|F_cut|=32` | three complement-pairs and two complement-fixed orbits remain free after the vanish cuts |
| `f_L1` is not Hamming | the two-unbalanced-axis orbit `adj2` has even weight and `f_L1=1` |
| `f_L1` fills from `S` | halt set has cardinality 12 at tick 2 with history `(3, 9, 12)` |
| `f_mix0` is an `F_cut` 1-site filler | the remaining-bit tuple `(1,0,1,1,0)` is one of the eight 1-site fillers, support 44 |
| `f_mix0` 1-site history | `(1, 4, 8, 11, 12)`, the same tuple as L1 |
| `f_mix0` fills from `S` | `|locks_halt|=12`, `T=2`, history `(3, 9, 12)` |
| comparison | the two maps share the line-seed history and differ on `mixed3` |
| physical Admissibility selection | open and not claimed; `f_mix0` is not written in |

Every leaf needed for the stated line-seed fill is discharged. No `Z^3`-wide
formation law is claimed.

## Mutations

1. Replace `f_L1` by Hamming `|c|_1 mod 2`: the remaining-bit tuple changes
   and Hamming does not fill from `S`.
2. Flip `mixed3` from `0` to `1`: the map becomes `f_L1`, not `f_mix0`.
3. Replace the seed by the 1-site seed `(0,0,0)`: the history becomes
   `(1, 4, 8, 11, 12)`, which is leftover-character of #6415, not this residual.
4. Replace off-patch occupancy `0` by a blank-block: first-wave candidates
   become undefined; that is a different census.
5. Assert that `f_mix0` fails to fill from `S`: the reconstructed run
   reaches all twelve vertices at tick 2.
6. Replace `f_mix0` by `f_cutmin` `(1,0,1,0,0)`: that is #6419, a different
   remaining-bit map on the same seed.

## What This Does Not Claim

- No physical Admissibility selector and no adopted occupancy law.
- No Qubit rewrite and no `M_2(C)`-valued conditional probability.
- No `Z^3`-wide formation, rate, or generator.
- No identification of `f_L1` with Hamming parity.
- No leftover-character restatement of the 1-site / face-diagonal / `S*`
  fills of `f_mix0` (#6415/#6424) in place of this 3-site fill.
- No leftover-character restatement of the line-seed fill of `f_cutmin`
  (#6419) in place of this different remaining-bit map.
- No blank-block variant and no adoption of a second seed as canonical.
- No axiom edit: `f_mix0` is displayed, not written into Admissibility.

## No-Go Discipline Gate

The only negative claim is that Hamming is not `f_L1` and does not fill
from `S`. The positive fill of `f_mix0` from `S` is an exact run, not a
wall, and it is not an Admissibility clause.

### N1 — materially distinct routes

| Route | Exact attack | Result and authority | Marker |
|---|---|---|---|
| orbit reconstruction | Recompute the 24 rotations and the 10 axis-type orbits. | Theorem 1 and checks `thm1-twenty-four-rotations` / `thm1-ten-orbits`. | **ATTEMPTED** |
| L1 line-seed fill | Run `f_L1` from `S` to a fixed point. | Theorem 1 and check `thm1-f-L1-fills-line` give history `(3, 9, 12)`. | **ATTEMPTED** |
| Hamming-as-`f_L1` | Test whether `|c|_1 mod 2` equals the unbalanced-axis predicate. | Theorem 1 and check `thm1-f-L1-not-hamming` separate the maps. | **ATTEMPTED** |
| `f_mix0` membership | Reconstruct the eight 1-site fillers and isolate tuple `(1,0,1,1,0)`. | Theorem 2 and check `thm1-mix0-tuple-and-one-site-filler`. | **ATTEMPTED** |
| `f_mix0` from `S` | Run the remaining-bit map from the long-axis seed. | Theorem 2 and check `thm2-mix0-line-fill` give fill at `T=2`. | **ATTEMPTED** |
| history comparison | Compare line-seed histories and the `mixed3` bit of the two maps. | Theorem 3 and check `thm3-comparison-same-line-history`. | **ATTEMPTED** |

### N2 — wall independence and collapse

There is one negative conclusion: Hamming is not `f_L1`. The fill of
`f_mix0` from `S` is a positive exact run.

| Pair | First closes second? | Second closes first? | Disposition |
|---|---:|---:|---|
| `f_mix0` fills from `S` / `f_L1` fills from `S` | no: one map filling does not classify the other | no: L1 filling does not prove `f_mix0` fills | independent positive runs, not two walls |
| `f_L1` fills / Hamming does not | no: one map filling does not classify Hamming | no: Hamming failing does not prove `f_L1` fills | independent positive/negative members, not two walls |
| 1-site history / line-seed history | no: the 1-site run does not fix the 3-site run | no: a shared line-seed history does not restore `mixed3` | separate exact runs |

Physical law selection is not a wall: this note makes no negative theorem
about the existence of a selector and simply does not claim one.

### N3 — hidden-condition scan

| Phrase or premise | Classification |
|---|---|
| “work on the twelve-vertex two-cube” | explicit patch hypothesis; not a `Z^3` theorem |
| off-patch occupancy `0` | explicit default; blank-block is a different rule |
| 3-site long-axis seed `S` | explicit remaining displayed seed; not the 1-site seed of #6415 |
| remaining bits `(1,0,1,1,0)` | explicit `F_cut` rival; L1 and `f_cutmin` are different tuples |
| “lock” | Record permanence on this Boolean occupancy model, not a possibility-valued law |
| “cube-covariant” | invariance under the 24 proper rotations, cited to Lattice/Admissibility |
| Hamming parity | displayed mutation only |
| shared history `(3, 9, 12)` | displayed comparison, not an Admissibility clause |

### N4 — citation-to-residual matching

| Evidence path:line | Residual attacked | Residual claimed closed | Match? |
|---|---|---|---:|
| `docs/MINIMAL_AXIOMS_2026-06-29.md:37` | ambient lattice and cubic rotations | sites are `Z^3` with proper cubic rotations | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:57` | covariant nearest-neighbor rule | covariance is the class filter, not a selector | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:79` | lock permanence | a locked site stays locked | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:83` | unreadability of absence | unlocked and off-patch sites contribute occupancy `0`, not a readout | yes |
| `scripts/f_cut_mix0_line_seed_fill_2026_08_15.py:81` | 24 proper rotations | signed permutations with determinant `+1` | yes |
| `scripts/f_cut_mix0_line_seed_fill_2026_08_15.py:125` | `f_L1` definition | unbalanced-axis predicate, not Hamming | yes |
| `scripts/f_cut_mix0_line_seed_fill_2026_08_15.py:130` | Hamming mutation | `|c|_1 mod 2` is a different map | yes |
| `scripts/f_cut_mix0_line_seed_fill_2026_08_15.py:50` | long-axis seed | `S = {(0,0,0),(1,0,0),(2,0,0)}` | yes |
| `scripts/f_cut_mix0_line_seed_fill_2026_08_15.py:66` | `f_mix0` tuple | remaining bits `(1,0,1,1,0)` | yes |
| `scripts/f_cut_mix0_line_seed_fill_2026_08_15.py:180` | lock dynamics | synchronous ticks from a supplied seed to a fixed point | yes |

No evidence citation is used to claim that a physical occupancy law, a
formation rate, or a `Z^3`-wide selector has been closed.

### N5 — rhetoric and resolution audit

| Resolution | Executed? | Narrow negative supported? |
|---|---:|---|
| per element | yes: all 64 neighbor 6-tuples | each is assigned its axis-type orbit; no broader cell class is classified |
| per site | yes: the twelve two-cube vertices | each uses the same six-direction stencil with off-patch occupancy `0` |
| per mode | yes: `f_mix0` and `f_L1` from `S` | the fill is this pair of maps on this seed; other seeds are unclaimed except as 1-site context |
| per block | yes: the pair `(halt locks, history)` | fill from `S` is `|locks_halt|=12` with history `(3, 9, 12)` |
| lattice wide | no | no `Z^3`-wide formation or Admissibility selector is asserted |

The runner prints the same five resolution statements.

### N6 — partial closure and primitive scan

The primitive registry at `docs/audit/data/axiom_premise_nodes.json` was
checked. The only dependency used is the registered `minimal_axioms` node.
No approved primitive supplies the Boolean occupancy maps, and none is
reclassified as an import or wall.

One partial-closure mechanism is displayed rather than suppressed: the
`F_cut` 1-site filler with remaining bits `(1,0,1,1,0)` also fills from
the 3-site long-axis seed, and on that seed it shares L1's lock history.
That shared history does not write `f_mix0` into Admissibility and does
not select either map as the physical rule. The remaining physical
choice — which, if any, occupancy predicate is the Admissibility rule —
stays explicit.

### N7 — hostile steelman

The strongest objection is that a 3-site long-axis seed already occupies
an entire long edge, so any 1-site filler with `wt1=adj2=1` will flood
the two remaining long edges in one tick and close the last three
opposite-corner sites in the next, making the shared history `(3, 9, 12)`
leftover-character of #6415 or of #6419. That objection is correctly
about the first two waves on this particular seed. It does not overturn
the stated theorem. `f_mix0` and L1 already differ on `mixed3`, so
`mixed3=0` is not inert in general. Whether that difference survives on
`S` is a new run. It happens not to change the history: `f_mix0` still
fills, with the same history as `f_L1`. A failure to fill would have
been displayed. None occurs. The #6419 residual was `f_cutmin`, a
different remaining-bit map.

### N8 — cross-cycle echo

Repository search found nearby occupancy and covariance surfaces. They are
context, not load-bearing dependencies. The 24 rotations, 10 orbits,
`f_mix0` tuple, and the line-seed run are recomputed here.

| Earlier surface | Similar issue | Mechanism considered here |
|---|---|---|
| `docs/ADMISSIBILITY_COVARIANT_Q8_CONDITIONAL_LAW_PAIR_BOUNDED_THEOREM_NOTE_2026-08-13.md` | proper-cubic covariance of a local rule | covariance is used only as the orbit filter for Boolean maps |
| `docs/PHYSICAL_SPATIAL_BLOCK_SEAM_DICHOTOMY_CYCLE728_NOTE_2026-08-04.md` | two-cell box `{0,1,2}×{0,1}×{0,1}` | the same twelve spatial vertices are the patch; the seam cost is unused |
| `docs/MINIMAL_AXIOMS_2026-06-29.md` | one covariant nearest-neighbor rule | the axiom names the contract; this note does not select the rule |

The 1-site / face-diagonal / `S*` fills of `f_mix0` (#6415/#6424) are
the class this note re-runs from the remaining displayed seed. They are
not parents and do not close the line-seed fill. The line-seed fill of
`f_cutmin` (#6419) is a different remaining-bit map on the same seed.

No earlier mechanism retires the line-seed fill or writes `f_mix0`
into Admissibility.

No-Go Discipline disposition: **PASS** for the Hamming distinction and
the exact fill of `f_mix0` from `S` stated above.

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
`F_cut`, isolates the remaining-bit 1-site filler `f_mix0`, checks that
`f_L1` fills from `S` with history `(3, 9, 12)`, runs `f_mix0` from `S`,
and reports `|locks_halt|=12`, `T=2`, and history `(3, 9, 12)`.
Declared audit inputs are this note and the axiom memo. No runner cache is
written.
