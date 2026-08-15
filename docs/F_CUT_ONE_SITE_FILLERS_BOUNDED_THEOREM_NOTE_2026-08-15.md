---
claim_id: f_cut_one_site_fillers_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Among the 32 cube-covariant complement-even predicates that vanish on empty and full, N = 8 fill the twelve-vertex two-cube from a 1-site seed with off-patch o=0. f_L1 is not unique in that set. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_one_site_fillers_2026_08_15.py
---

# One-Site Fillers Inside The Three-Cut Class `F_cut`

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact occupancy-to-lock census of the 32 cube-covariant
complement-even predicates that vanish on empty and full, on the
twelve-vertex two-cube from a 1-site seed with off-patch occupancy `0`.
The unbalanced-axis map `f_L1` is displayed as one filler. It is not
adopted as the physical Admissibility rule.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_one_site_fillers_2026_08_15.py`](../scripts/f_cut_one_site_fillers_2026_08_15.py)
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
class. It is not the residual of this note. The 512-map fill census of
every cube-covariant `f` with only `f(empty)=0` is a different leftover
inventory. This note asks the intersection question: how many members of
`F_cut` fill.

On the two-cube `{0,1,2}×{0,1}×{0,1}`, seed `(0,0,0)` starts locked.
Off-patch neighbors have occupancy `0`. Each tick, every unlocked on-patch
vertex evaluates `f` on its six-neighbor occupancy tuple and locks if
`f=1`. The process is synchronous and stops at a fixed point in at most
12 ticks. Fill means `|locks_halt|=12`.

`f_L1(c)=1` if and only if some axis is unbalanced: `c_{+μ} ≠ c_{-μ}` for
at least one `μ ∈ {x,y,z}`. Equivalently, some discrete neighbor contrast
`n_μ = c_{+μ} − c_{-μ}` is nonzero. This is **not** Hamming parity
`|c|_1 mod 2`.

**Theorem 1.** `f_L1 ∈ F_cut` and `f_L1` fills: lock cardinalities
`(1,4,8,11,12)` and halt tick `4`.

**Theorem 2.** Hamming parity `|c|_1 mod 2` lies in `F_cut` and does not
fill: lock cardinalities `(1,4,5,7,9)` and halt tick `4`, so
`|locks_halt|=9`.

**Theorem 3.** Exactly `N = 8` members of `F_cut` fill. So `N > 1`:
`f_L1` is not unique in that set. A displayed second filler `f_♦` is `1`
exactly when the unbalanced-axis count `u` satisfies `1 ≤ u ≤ 2`.
Displayed, not adopted.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The ten-orbit reconstruction, the 32-element F_cut, membership of f_L1 and Hamming parity, and the exact fill count N=8 are enumerated. Uniqueness of f_L1 as an F_cut filler is false on this patch. No physical law is selected."
trace_class: upstream_support
target_claim_id: f_cut_one_site_fillers
target_blocker_text: "how many of the 32 F_cut predicates fill the two-cube from a 1-site seed, and whether f_L1 is the unique filler in that set"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the F_cut fill census; any physical use must separately derive an Admissibility selector"
conditional_surface_status: "exact for F_cut on this twelve-vertex patch with off-patch o=0; no Z^3-wide law and no physical selector"
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

Not leftover-character of the static 32-count of `F_cut`. Not leftover-character of the 512-map fill census.

## Exact Target And Objects

**Target.** Count the members of `F_cut` that fill the two-cube from the
1-site seed, and decide uniqueness of `f_L1` inside that set.

Write a neighbor configuration as `c ∈ {0,1}^6`. A proper cube rotation `R`
acts by `(R·c)(d) = c(R^{-1}d)` on the six face directions `d`. A map
`f:{0,1}^6 → {0,1}` is cube-covariant when `f(R·c)=f(c)` for every such `R`.
Equivalently, `f` is constant on each orbit.

The axis type of `c` is the triple `(u,b,e)` with `u+b+e=3`, where `u` is
the number of axes with `c_{+} ≠ c_{-}`, `b` the number with
`(c_{+},c_{-})=(1,1)`, and `e` the number with `(c_{+},c_{-})=(0,0)`. These
ten types are exactly the ten orbits. Complement sends `(u,b,e)` to
`(u,e,b)`.

| `(u,b,e)` | orbit size | complement image |
|---|---:|---|
| `(0,0,3)` empty | 1 | `(0,3,0)` full |
| `(0,3,0)` full | 1 | `(0,0,3)` empty |
| `(0,1,2)` opposite pair | 3 | `(0,2,1)` |
| `(0,2,1)` | 3 | `(0,1,2)` |
| `(1,0,2)` one unbalanced axis | 6 | `(1,2,0)` |
| `(1,2,0)` | 6 | `(1,0,2)` |
| `(2,0,1)` two unbalanced axes | 12 | `(2,1,0)` |
| `(2,1,0)` | 12 | `(2,0,1)` |
| `(1,1,1)` mixed triple | 12 | `(1,1,1)` |
| `(3,0,0)` three unbalanced axes | 8 | `(3,0,0)` |

`F_cut` is the class of cube-covariant maps with `f(empty)=f(full)=0` and
`f(c)=f(1-c)`. The empty/full pair is forced to `0`. The remaining free
data are three complement-pair bits and two complement-fixed orbit bits,
so `|F_cut|=32`.

Define

```text
f_L1(c)     = 1  iff  u(c) ≥ 1,
f_♦(c)      = 1  iff  1 ≤ u(c) ≤ 2,
f_H(c)      = |c|_1 mod 2.
```

All three are cube-covariant, vanish on empty and full, and are
complement-even, hence lie in `F_cut`. `f_H` is used only as a displayed
mutation: it is not `f_L1`. `f_♦` is a displayed second filler: it is not
adopted.

A locked set `S` determines occupancies: a lattice neighbor in `S` has
occupancy `1`, and every other neighbor — including every off-patch
neighbor — has occupancy `0`. One synchronous tick replaces `S` by

```text
S ∪ { v in two-cube \ S : f(neighborhood_6(v; S)) = 1 }.
```

`N` is the number of maps in `F_cut` whose halt set has cardinality 12.

## Theorems

**Theorem 1.** There are exactly 24 proper cube rotations and exactly 10
orbits on `{0,1}^6`. The three cuts leave `|F_cut|=32`. The unbalanced-axis
map `f_L1` is one element of `F_cut`. It is not Hamming parity. On the
twelve-vertex two-cube from seed `(0,0,0)` with off-patch occupancy `0`,
`f_L1` fills: lock cardinalities `(1,4,8,11,12)` and halt tick `4`.

**Theorem 2.** Hamming parity `|c|_1 mod 2` is a different element of
`F_cut`. It does not fill. Its lock cardinalities are `(1,4,5,7,9)` and
its halt tick is `4`, so `|locks_halt|=9`.

**Theorem 3.** Exhaustive enumeration of the 32 maps gives

```text
N = 8.
```

So `N > 1`. The map `f_L1` fills, but it is not unique in `F_cut`. The
displayed second filler `f_♦` is distinct from `f_L1` (they disagree on
the three-unbalanced-axis orbit) and also fills, with lock cardinalities
`(1,4,8,10,11,12)` and halt tick `5`. Displayed, not adopted.

## Proof-Obligation Graph

| obligation | exact disposition |
|---|---|
| 24 proper cube rotations | signed permutations of the three axes with determinant `+1` |
| 10 orbits on `{0,1}^6` | axis-type classes `(u,b,e)` partition the 64 cells with the listed sizes |
| `|F_cut|=32` | three complement-pairs and two complement-fixed orbits remain free after the vanish cuts |
| `f_L1` is in `F_cut` | `u` is rotation- and complement-invariant and `u(empty)=u(full)=0` |
| `f_L1` is not Hamming | the two-unbalanced-axis orbit has even weight and `f_L1=1` |
| `f_L1` fills | halt set has cardinality 12 at tick 4 |
| Hamming is in `F_cut` and does not fill | halt set has cardinality 9 |
| two-cube has twelve vertices | `{0,1,2}×{0,1}×{0,1}` |
| off-patch occupancy `0` | declared stencil default; not a blank-block |
| `N` | exhaustive 32-run census of `F_cut` to a fixed point |
| uniqueness of `f_L1` in `F_cut` | false; `f_♦` is an explicit second filler |
| physical Admissibility selection | open and not claimed |

Every leaf needed for the stated census is discharged. No `Z^3`-wide
formation law is claimed.

## Mutations

1. Replace `f_L1` by Hamming `|c|_1 mod 2`: the maps disagree on the
   two-unbalanced-axis orbit, and Hamming does not fill.
2. Replace off-patch occupancy `0` by a blank-block: first-wave candidates
   become undefined; that is a different census.
3. Drop complement-even or the vanish-on-full cut: the class is no longer
   the 32-element `F_cut`.
4. Seed a second on-patch site: the 1-site first-wave and fill counts change.
5. Assert `N=1`: the explicit second filler `f_♦` refutes uniqueness.

## What This Does Not Claim

- No physical Admissibility selector and no adopted occupancy law.
- No Qubit rewrite and no `M_2(C)`-valued conditional probability.
- No `Z^3`-wide formation, rate, or generator.
- No identification of `f_L1` with Hamming parity.
- No leftover-character count of the static 32 or of the 512-map census
  in place of this `F_cut` dynamics census.
- No blank-block, 2-site, or 3-site variant.

## No-Go Discipline Gate

The only negative claim is uniqueness: `f_L1` is not the unique `F_cut`
filler of this patch. The positive count `N=8` is an exact enumeration,
not a wall.

### N1 — materially distinct routes

| Route | Exact attack | Result and authority | Marker |
|---|---|---|---|
| orbit reconstruction | Recompute the 24 rotations and the 10 axis-type orbits. | Theorem 1 and checks `thm1-twenty-four-rotations` / `thm1-ten-orbits`. | **ATTEMPTED** |
| three-cut class | Force vanish-on-empty, vanish-on-full, and `f(c)=f(1-c)`. | Theorem 1 and check `thm1-f-cut-cardinality` give `|F_cut|=32`. | **ATTEMPTED** |
| Hamming-as-`f_L1` | Test whether `|c|_1 mod 2` equals the unbalanced-axis predicate. | Theorem 1 and check `thm1-f-L1-not-hamming` separate the maps. | **ATTEMPTED** |
| Hamming fill | Run Hamming parity on the same patch. | Theorem 2 and check `thm2-hamming-does-not-fill` give nine locks. | **ATTEMPTED** |
| `F_cut` fill census | Run every map in `F_cut` to a fixed point. | Theorem 3 and check `thm3-n-fill` give `N = 8`. | **ATTEMPTED** |
| uniqueness of `f_L1` | Ask whether the `F_cut` filler class is a singleton. | Theorem 3 and checks `thm3-not-unique` / `thm3-displayed-other-filler`. | **ATTEMPTED** |

### N2 — wall independence and collapse

There is one negative conclusion: uniqueness fails. The explicit second
filler and the cardinality `N=8` are two certificates of the same
non-uniqueness, so they collapse rather than count as two walls.

| Pair | First closes second? | Second closes first? | Disposition |
|---|---:|---:|---|
| `N=8` / displayed `f_♦` | yes: a count larger than one is non-uniqueness | yes: one extra filler is non-uniqueness | collapse into the uniqueness failure |
| `f_L1` fills / Hamming does not | no: one map filling does not classify Hamming | no: Hamming failing does not prove `f_L1` fills | independent positive/negative members, not two walls |
| static `|F_cut|=32` / fill count `N` | no: membership is not dynamics | no: a fill count does not replace the three-cut class | separate exact counts |

Physical law selection is not a wall: this note makes no negative theorem
about the existence of a selector and simply does not claim one.

### N3 — hidden-condition scan

| Phrase or premise | Classification |
|---|---|
| “work on the twelve-vertex two-cube” | explicit patch hypothesis; not a `Z^3` theorem |
| off-patch occupancy `0` | explicit default; blank-block is a different rule |
| `F_cut` | explicit three-cut class; the other 992 covariant maps are excluded |
| “lock” | Record permanence on this Boolean occupancy model, not a possibility-valued law |
| “cube-covariant” | invariance under the 24 proper rotations, cited to Lattice/Admissibility |
| Hamming parity | displayed mutation only |
| `f_♦` | displayed witness against uniqueness, not a selected law |

### N4 — citation-to-residual matching

| Evidence path:line | Residual attacked | Residual claimed closed | Match? |
|---|---|---|---:|
| `docs/MINIMAL_AXIOMS_2026-06-29.md:37` | ambient lattice and cubic rotations | sites are `Z^3` with proper cubic rotations | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:57` | covariant nearest-neighbor rule | covariance is the class filter, not a selector | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:79` | lock permanence | a locked site stays locked | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:83` | unreadability of absence | unlocked and off-patch sites contribute occupancy `0`, not a readout | yes |
| `scripts/f_cut_one_site_fillers_2026_08_15.py:59` | 24 proper rotations | signed permutations with determinant `+1` | yes |
| `scripts/f_cut_one_site_fillers_2026_08_15.py:103` | `f_L1` definition | unbalanced-axis predicate, not Hamming | yes |
| `scripts/f_cut_one_site_fillers_2026_08_15.py:108` | Hamming mutation | `|c|_1 mod 2` is a different `F_cut` map | yes |
| `scripts/f_cut_one_site_fillers_2026_08_15.py:247` | class census | exact `N` on `F_cut` | yes |
| `scripts/f_cut_one_site_fillers_2026_08_15.py:112` | uniqueness | displayed second filler `f_♦` | yes |

No evidence citation is used to claim that a physical occupancy law, a
formation rate, or a `Z^3`-wide selector has been closed.

### N5 — rhetoric and resolution audit

| Resolution | Executed? | Narrow negative supported? |
|---|---:|---|
| per element | yes: all 64 neighbor 6-tuples | each is assigned its axis-type orbit; no broader cell class is classified |
| per site | yes: the twelve two-cube vertices | each uses the same six-direction stencil with off-patch occupancy `0` |
| per mode | yes: every map in `F_cut` | the census is this class on this seed; other seeds are unclaimed |
| per block | yes: the pair `(|F_cut|, N)` | uniqueness fails because `N=8` |
| lattice wide | no | no `Z^3`-wide formation or Admissibility selector is asserted |

The runner prints the same five resolution statements.

### N6 — partial closure and primitive scan

The primitive registry at `docs/audit/data/axiom_premise_nodes.json` was
checked. The only dependency used is the registered `minimal_axioms` node.
No approved primitive supplies the Boolean occupancy maps, and none is
reclassified as an import or wall.

One partial-closure mechanism is displayed rather than suppressed: `f_L1`
does fill this patch from the 1-site seed and does lie in `F_cut`. That
positive member does not make `f_L1` unique and does not select it as the
physical rule. The remaining physical choice — which, if any, `F_cut` map
is the Admissibility occupancy predicate — stays explicit.

### N7 — hostile steelman

The strongest objection is that several of the eight fillers agree with
`f_L1` on every 6-tuple that actually occurs along the 1-site filling
trajectory of `f_L1`, so uniqueness might be restored by restricting to
“dynamically occurring” cells. That objection is correctly about a smaller
class. It does not overturn the stated theorem: among all maps in `F_cut`,
eight fill. The displayed second filler `f_♦` already differs from `f_L1`
on the three-unbalanced-axis orbit, and it fills by a different lock
history. That is a class-level extra filler, not a trajectory-level
identity.

### N8 — cross-cycle echo

Repository search found nearby occupancy and covariance surfaces. They are
context, not load-bearing dependencies. The 24 rotations, 10 orbits,
`F_cut`, and 32-map dynamics are recomputed here.

| Earlier surface | Similar issue | Mechanism considered here |
|---|---|---|
| `docs/ADMISSIBILITY_COVARIANT_Q8_CONDITIONAL_LAW_PAIR_BOUNDED_THEOREM_NOTE_2026-08-13.md` | proper-cubic covariance of a local rule | covariance is used only as the orbit filter for Boolean maps |
| `docs/PHYSICAL_SPATIAL_BLOCK_SEAM_DICHOTOMY_CYCLE728_NOTE_2026-08-04.md` | two-cell box `{0,1,2}×{0,1}×{0,1}` | the same twelve spatial vertices are the patch; the seam cost is unused |
| `docs/MINIMAL_AXIOMS_2026-06-29.md` | one covariant nearest-neighbor rule | the axiom names the contract; this note does not select the rule |

No earlier mechanism retires the `F_cut` fill census or restores uniqueness
of `f_L1` inside the 32-map class.

No-Go Discipline disposition: **PASS** for the uniqueness failure and the
exact pair `(|F_cut|, N)` stated above.

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
`F_cut`, evaluates all 32 maps on the two-cube, reports `N = 8`, checks
that `f_L1` fills and is not Hamming parity, checks that Hamming parity
halts at nine locks, and exhibits the displayed second filler `f_♦`.
Declared audit inputs are this note and the axiom memo. No runner cache is
written.
