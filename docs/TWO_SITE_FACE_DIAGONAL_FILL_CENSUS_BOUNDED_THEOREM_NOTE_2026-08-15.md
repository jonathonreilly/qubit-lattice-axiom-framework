---
claim_id: two_site_face_diagonal_fill_census_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Among cube-covariant f with f(empty)=0, N_fill_2 = 64 fill the twelve-vertex two-cube from the face-diagonal 2-site seed with off-patch o=0. f_L1 is not unique in that set. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/two_site_face_diagonal_fill_census_2026_08_15.py
---

# Two-Site Face-Diagonal Fill Census Of The 512 Cube-Covariant Maps

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact occupancy-to-lock census of the 512 cube-covariant
predicates that vanish on empty, on the twelve-vertex two-cube from the
face-diagonal 2-site seed `{(0,0,0),(1,1,0)}` with off-patch occupancy `0`.
The unbalanced-axis map `f_L1` is displayed as one filler. The two-axis
map `f_two` is displayed as a non-filler. Neither is adopted as the
physical Admissibility rule.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/two_site_face_diagonal_fill_census_2026_08_15.py`](../scripts/two_site_face_diagonal_fill_census_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

The 24 proper cube rotations act on neighbor 6-tuples in `{0,1}^6` and
partition those 64 cells into 10 orbits. Cube-covariant predicates are the
`{0,1}`-assignments to those orbits. Restricting to `f(empty)=0` leaves
nine free bits, so there are exactly 512 such maps.

That 512-count is leftover-character inventory of the covariance class.
The 1-site fill census of the same 512 maps is a different leftover
inventory: it used seed `(0,0,0)` alone. A separate halt run of the single
map `f_two` from this same 2-site seed is also a different residual. This
note asks how many of the 512 maps fill from the face-diagonal pair.

On the two-cube `{0,1,2}×{0,1}×{0,1}`, seed `{(0,0,0),(1,1,0)}` starts
locked. Off-patch neighbors have occupancy `0`. Each tick, every unlocked
on-patch vertex evaluates `f` on its six-neighbor occupancy tuple and
locks if `f=1`. The process is synchronous and stops at a fixed point in
at most 12 ticks. Fill means `|locks_halt|=12`.

`f_L1(c)=1` if and only if some axis is unbalanced: `c_{+μ} ≠ c_{-μ}` for
at least one `μ ∈ {x,y,z}`. Equivalently, some discrete neighbor contrast
`n_μ = c_{+μ} − c_{-μ}` is nonzero. This is **not** Hamming parity
`|c|_1 mod 2`.

`f_two(c)=1` if and only if at least two axes are unbalanced. This is
**not** `f_L1`.

**Theorem 1.** `f_L1` is one of the 512 maps and fills from this seed:
lock cardinalities `(2,7,11,12)` and halt tick `3`.

**Theorem 2.** `f_two` is a different one of the 512 maps and does not
fill: first wave `{(1,0,0),(0,1,0)}`, lock cardinalities `(2,4)`, halt
tick `1`, so `|locks_halt|=4`.

**Theorem 3.** Exactly `N_fill_2 = 64` of the 512 maps fill. So
`N_fill_2 > 1`: `f_L1` is not unique. A displayed second filler `f_any`
is `1` on every nonempty 6-tuple. Displayed, not adopted.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The ten-orbit reconstruction, the 512-map class, membership of f_L1 and f_two, the f_L1 fill, the f_two four-lock halt, and the exact fill count N_fill_2=64 are enumerated. Uniqueness of f_L1 as a 2-site filler is false on this patch. No physical law is selected."
trace_class: upstream_support
target_claim_id: two_site_face_diagonal_fill_census
target_blocker_text: "how many cube-covariant f with f(empty)=0 fill the two-cube from the face-diagonal 2-site seed, and whether f_L1 is the unique filler"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the 2-site fill census; any physical use must separately derive an Admissibility selector"
conditional_surface_status: "exact for the 512 maps on this twelve-vertex patch with off-patch o=0 and the displayed 2-site seed; no Z^3-wide law and no physical selector"
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
- the face-diagonal 2-site seed `{(0,0,0),(1,1,0)}`.

No observational comparator, literature constant, Wilson weight, rate, or
generator is imported. No Record scalar functional appears.

Not leftover-character of the 1-site fill census. Not a second f_two face-diagonal halt run.

## Exact Target And Objects

**Target.** Count the cube-covariant maps with `f(empty)=0` that fill the
two-cube from the face-diagonal 2-site seed, and decide uniqueness of
`f_L1` inside that set.

Write a neighbor configuration as `c ∈ {0,1}^6`. A proper cube rotation `R`
acts by `(R·c)(d) = c(R^{-1}d)` on the six face directions `d`. A map
`f:{0,1}^6 → {0,1}` is cube-covariant when `f(R·c)=f(c)` for every such `R`.
Equivalently, `f` is constant on each orbit.

The axis type of `c` is the triple `(u,b,e)` with `u+b+e=3`, where `u` is
the number of axes with `c_{+} ≠ c_{-}`, `b` the number with
`(c_{+},c_{-})=(1,1)`, and `e` the number with `(c_{+},c_{-})=(0,0)`. These
ten types are exactly the ten orbits.

| `(u,b,e)` | orbit size | role in this census |
|---|---:|---|
| `(0,0,3)` empty | 1 | forced `f=0` by the class |
| `(0,3,0)` full | 1 | free bit |
| `(0,1,2)` opposite pair | 3 | free bit |
| `(0,2,1)` | 3 | free bit |
| `(1,0,2)` one unbalanced axis | 6 | forced `f=1` on every filler |
| `(1,2,0)` | 6 | free bit |
| `(2,0,1)` two unbalanced axes | 12 | forced `f=1` on every filler |
| `(2,1,0)` | 12 | free bit |
| `(1,1,1)` mixed triple | 12 | free bit |
| `(3,0,0)` three unbalanced axes | 8 | forced `f=1` on every filler |

Define

```text
f_L1(c)   = 1  iff  u(c) ≥ 1,
f_two(c)  = 1  iff  u(c) ≥ 2,
f_any(c)  = 1  iff  c ≠ empty,
f_H(c)    = |c|_1 mod 2.
```

All four are cube-covariant. `f_L1`, `f_two`, and `f_any` vanish on empty
and are therefore among the 512 maps. `f_H` is used only as a displayed
mutation: it is not `f_L1`. `f_any` is a displayed second filler: it is
not adopted. `f_two` is a displayed non-filler: it is not adopted.

A locked set `S` determines occupancies: a lattice neighbor in `S` has
occupancy `1`, and every other neighbor — including every off-patch
neighbor — has occupancy `0`. One synchronous tick replaces `S` by

```text
S ∪ { v in two-cube \ S : f(neighborhood_6(v; S)) = 1 }.
```

`N_fill_2` is the number of the 512 maps whose halt set has cardinality 12.

The three orbits that actually fire along the common filling trajectory
are `(1,0,2)`, `(2,0,1)`, and `(3,0,0)`. Every filler is `1` on those
three orbits and `0` on empty; the other six orbit bits remain free, so
the filler class has size `2^6 = 64`. That characterization is a
post-census identity, not an input.

## Theorems

**Theorem 1.** There are exactly 24 proper cube rotations and exactly 10
orbits on `{0,1}^6`. The vanish-on-empty cut leaves 512 cube-covariant
maps. The unbalanced-axis map `f_L1` is one of them. It is not Hamming
parity. On the twelve-vertex two-cube from seed `{(0,0,0),(1,1,0)}` with
off-patch occupancy `0`, `f_L1` fills: lock cardinalities `(2,7,11,12)`
and halt tick `3`.

**Theorem 2.** The two-axis map `f_two` is a different one of the 512
maps. It does not fill. Its first wave is exactly `{(1,0,0),(0,1,0)}`.
Its lock cardinalities are `(2,4)` and its halt tick is `1`, so
`|locks_halt|=4`.

**Theorem 3.** Exhaustive enumeration of the 512 maps gives

```text
N_fill_2 = 64.
```

So `N_fill_2 > 1`. The map `f_L1` fills, but it is not unique. The
displayed second filler `f_any` is distinct from `f_L1` (they disagree on
every balanced nonempty orbit) and also fills, with the same lock
cardinalities `(2,7,11,12)` and halt tick `3`. Displayed, not adopted.

## Proof-Obligation Graph

| obligation | exact disposition |
|---|---|
| 24 proper cube rotations | signed permutations of the three axes with determinant `+1` |
| 10 orbits on `{0,1}^6` | axis-type classes `(u,b,e)` partition the 64 cells with the listed sizes |
| 512 maps | nine free orbit bits after `f(empty)=0` |
| `f_L1` is in the 512 | `u` is rotation-invariant and `u(empty)=0` |
| `f_L1` is not Hamming | the two-unbalanced-axis orbit has even weight and `f_L1=1` |
| `f_L1` fills | halt set has cardinality 12 at tick 3 |
| `f_two` is `u≥2` and does not fill | halt set has cardinality 4 at tick 1 |
| two-cube has twelve vertices | `{0,1,2}×{0,1}×{0,1}` |
| seed is the displayed face-diagonal pair | `{(0,0,0),(1,1,0)}` |
| off-patch occupancy `0` | declared stencil default; not a blank-block |
| `N_fill_2` | exhaustive 512-run census to a fixed point |
| uniqueness of `f_L1` | false; `f_any` is an explicit second filler |
| physical Admissibility selection | open and not claimed |

Every leaf needed for the stated census is discharged. No `Z^3`-wide
formation law is claimed.

## Mutations

1. Replace `f_L1` by Hamming `|c|_1 mod 2`: the maps disagree on the
   two-unbalanced-axis orbit. Hamming is not the unbalanced-axis rule.
2. Replace `f_L1` by `f_two`: first wave still locks `(1,0,0)` and
   `(0,1,0)`, but sites with a single unbalanced axis never lock, and
   the process halts at four sites.
3. Replace off-patch occupancy `0` by a blank-block: first-wave candidates
   become undefined; that is a different census.
4. Seed only `(0,0,0)`: the 1-site fill count is a different residual.
5. Assert `N_fill_2=1`: the explicit second filler `f_any` refutes
   uniqueness.

## What This Does Not Claim

- No physical Admissibility selector and no adopted occupancy law.
- No Qubit rewrite and no `M_2(C)`-valued conditional probability.
- No `Z^3`-wide formation, rate, or generator.
- No identification of `f_L1` with Hamming parity.
- No leftover-character count of the 1-site fill census in place of this
  2-site dynamics census.
- No second halt-only run of `f_two` in place of the 512-map census.
- No blank-block, 1-site, or 3-site variant as the stated residual.

## No-Go Discipline Gate

The only negative claim is uniqueness: `f_L1` is not the unique 2-site
filler of this patch. The positive count `N_fill_2 = 64` is an exact
enumeration, not a wall. The four-lock halt of `f_two` is a displayed
member contrast, not a compiler impossibility.

### N1 — materially distinct routes

| Route | Exact attack | Result and authority | Marker |
|---|---|---|---|
| orbit reconstruction | Recompute the 24 rotations and the 10 axis-type orbits. | Theorem 1 and checks `thm1-twenty-four-rotations` / `thm1-ten-orbits`. | **ATTEMPTED** |
| vanish-on-empty class | Force `f(empty)=0` on cube-covariant maps. | Theorem 1 and check `thm1-five-twelve-maps` give 512 maps. | **ATTEMPTED** |
| Hamming-as-`f_L1` | Test whether `|c|_1 mod 2` equals the unbalanced-axis predicate. | Theorem 1 and check `thm1-f-L1-not-hamming` separate the maps. | **ATTEMPTED** |
| `f_L1` fill | Run `f_L1` from the face-diagonal 2-site seed. | Theorem 1 and check `thm1-f-L1-fills` give twelve locks at tick 3. | **ATTEMPTED** |
| `f_two` halt | Run `f_two` (`u≥2`) from the same seed. | Theorem 2 and check `thm2-f-two-does-not-fill` give four locks. | **ATTEMPTED** |
| 2-site fill census | Run every vanish-on-empty cube-covariant map to a fixed point. | Theorem 3 and checks `thm3-n-fill-2` / `thm3-not-unique`. | **ATTEMPTED** |

### N2 — wall independence and collapse

There is one negative conclusion: uniqueness fails. The explicit second
filler and the cardinality `N_fill_2 = 64` are two certificates of the
same non-uniqueness, so they collapse rather than count as two walls.

| Pair | First closes second? | Second closes first? | Disposition |
|---|---:|---:|---|
| `N_fill_2=64` / displayed `f_any` | yes: a count larger than one is non-uniqueness | yes: one extra filler is non-uniqueness | collapse into the uniqueness failure |
| `f_L1` fills / `f_two` does not | no: one map filling does not classify `f_two` | no: `f_two` failing does not prove `f_L1` fills | independent positive/negative members, not two walls |
| 1-site fill count / `N_fill_2` | no: a different seed is a different census | no: a 2-site count does not replace the 1-site count | separate exact counts |

Physical law selection is not a wall: this note makes no negative theorem
about the existence of a selector and simply does not claim one.

### N3 — hidden-condition scan

| Phrase or premise | Classification |
|---|---|
| “work on the twelve-vertex two-cube” | explicit patch hypothesis; not a `Z^3` theorem |
| off-patch occupancy `0` | explicit default; blank-block is a different rule |
| vanish-on-empty | explicit class filter; maps with `f(empty)=1` are excluded |
| “lock” | Record permanence on this Boolean occupancy model, not a possibility-valued law |
| “cube-covariant” | invariance under the 24 proper rotations, cited to Lattice/Admissibility |
| Hamming parity | displayed mutation only |
| `f_two` | displayed non-filler, not a selected law |
| `f_any` | displayed witness against uniqueness, not a selected law |

### N4 — citation-to-residual matching

| Evidence path:line | Residual attacked | Residual claimed closed | Match? |
|---|---|---|---:|
| `docs/MINIMAL_AXIOMS_2026-06-29.md:37` | ambient lattice and cubic rotations | sites are `Z^3` with proper cubic rotations | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:57` | covariant nearest-neighbor rule | covariance is the class filter, not a selector | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:79` | lock permanence | a locked site stays locked | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:83` | unreadability of absence | unlocked and off-patch sites contribute occupancy `0`, not a readout | yes |
| `scripts/two_site_face_diagonal_fill_census_2026_08_15.py:64` | 24 proper rotations | signed permutations with determinant `+1` | yes |
| `scripts/two_site_face_diagonal_fill_census_2026_08_15.py:103` | `f_L1` definition | unbalanced-axis predicate, not Hamming | yes |
| `scripts/two_site_face_diagonal_fill_census_2026_08_15.py:108` | `f_two` definition | two-unbalanced-axis predicate, not `f_L1` | yes |
| `scripts/two_site_face_diagonal_fill_census_2026_08_15.py:212` | class census | exact `N_fill_2` on the 512 maps | yes |
| `scripts/two_site_face_diagonal_fill_census_2026_08_15.py:117` | uniqueness | displayed second filler `f_any` | yes |

No evidence citation is used to claim that a physical occupancy law, a
formation rate, or a `Z^3`-wide selector has been closed.

### N5 — rhetoric and resolution audit

| Resolution | Executed? | Narrow negative supported? |
|---|---:|---|
| per element | yes: all 64 neighbor 6-tuples | each is assigned its axis-type orbit; no broader cell class is classified |
| per site | yes: the twelve two-cube vertices | each uses the same six-direction stencil with off-patch occupancy `0` |
| per mode | yes: every vanish-on-empty cube-covariant map | the census is this class on this seed; other seeds are unclaimed |
| per block | yes: the pair `(512, N_fill_2)` | uniqueness fails because `N_fill_2=64` |
| lattice wide | no | no `Z^3`-wide formation or Admissibility selector is asserted |

The runner prints the same five resolution statements.

### N6 — partial closure and primitive scan

The primitive registry at `docs/audit/data/axiom_premise_nodes.json` was
checked. The only dependency used is the registered `minimal_axioms` node.
No approved primitive supplies the Boolean occupancy maps, and none is
reclassified as an import or wall.

One partial-closure mechanism is displayed rather than suppressed: `f_L1`
does fill this patch from the face-diagonal 2-site seed. That positive
member does not make `f_L1` unique and does not select it as the physical
rule. The remaining physical choice — which, if any, of the 64 fillers is
the Admissibility occupancy predicate — stays explicit.

### N7 — hostile steelman

The strongest objection is that all 64 fillers share the same lock history
`(2,7,11,12)`, so uniqueness might be restored by identifying maps that
agree on every 6-tuple that occurs along that trajectory. That objection
is correctly about a smaller, trajectory-level quotient. It does not
overturn the stated theorem: among all 512 cube-covariant maps with
`f(empty)=0`, sixty-four fill. The displayed second filler `f_any`
already differs from `f_L1` on every balanced nonempty orbit. Those
orbits are idle on this seed, but they remain distinct class-level maps.

### N8 — cross-cycle echo

Repository search found nearby occupancy and covariance surfaces. They are
context, not load-bearing dependencies. The 24 rotations, 10 orbits, 512
maps, and 2-site dynamics are recomputed here.

| Earlier surface | Similar issue | Mechanism considered here |
|---|---|---|
| `docs/ADMISSIBILITY_COVARIANT_Q8_CONDITIONAL_LAW_PAIR_BOUNDED_THEOREM_NOTE_2026-08-13.md` | proper-cubic covariance of a local rule | covariance is used only as the orbit filter for Boolean maps |
| `docs/PHYSICAL_SPATIAL_BLOCK_SEAM_DICHOTOMY_CYCLE728_NOTE_2026-08-04.md` | two-cell box `{0,1,2}×{0,1}×{0,1}` | the same twelve spatial vertices are the patch; the seam cost is unused |
| `docs/MINIMAL_AXIOMS_2026-06-29.md` | one covariant nearest-neighbor rule | the axiom names the contract; this note does not select the rule |
| `docs/INFORMATIVE_FRACTION_COVARIANT_RULE_QUANTIZATION_OCCUPANCY_RESIDUAL_THEOREM_NOTE_2026-07-02.md` | the same 10 orbits on `{0,1}^6` | orbit sizes are recomputed; the informative-fraction residual is unused |

No earlier mechanism retires the 2-site fill census or restores uniqueness
of `f_L1` inside the 512-map class.

No-Go Discipline disposition: **PASS** for the uniqueness failure and the
exact pair `(512, N_fill_2)` stated above.

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
the 512 vanish-on-empty cube-covariant maps, evaluates all 512 maps on the
two-cube from the face-diagonal 2-site seed, reports `N_fill_2 = 64`,
checks that `f_L1` fills and is not Hamming parity, checks that `f_two`
halts at four locks, and exhibits the displayed second filler `f_any`.
Declared audit inputs are this note and the axiom memo. No runner cache is
written.
