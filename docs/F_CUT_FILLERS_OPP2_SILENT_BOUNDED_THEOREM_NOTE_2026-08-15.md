---
claim_id: f_cut_fillers_opp2_silent_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Among the 8 F_cut 1-site fillers, N_opp0 = 4 have f(opp2)=0. f_L1 is not unique in that subset. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_fillers_opp2_silent_2026_08_15.py
---

# Opp2 Silence Among The Eight `F_cut` One-Site Fillers

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact count of how many of the eight `F_cut` 1-site fillers of
the twelve-vertex two-cube vanish on the opposite-pair orbit `opp2`.
The unbalanced-axis map `f_L1` is displayed as one such filler. It is
not adopted as the physical Admissibility rule.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_fillers_opp2_silent_2026_08_15.py`](../scripts/f_cut_fillers_opp2_silent_2026_08_15.py)
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
`|locks_halt|=12`. Exactly eight members of `F_cut` fill from this 1-site
seed. That eight-count is leftover-character inventory of the fill census.
It is not the residual of this note.

`opp2` is the orbit of a cell with exactly one axis fully occupied and the
other four slots `0`. A representative is `(c_{+x},c_{-x},c_{+y},c_{-y},c_{+z},c_{-z})=(1,1,0,0,0,0)`.
The axis type is `(u,b,e)=(0,1,2)`: no unbalanced axis, one both-occupied
axis, two empty axes. The orbit has size `3`. Equivalently, `opp2` is the
orbit of a cell with both ends of one axis occupied and the remaining four
slots empty. `f(opp2)=0` means a filled axis does not form.

`f_L1(c)=1` if and only if some axis is unbalanced: `c_{+μ} ≠ c_{-μ}` for
at least one `μ ∈ {x,y,z}`. Equivalently, some discrete neighbor contrast
`n_μ = c_{+μ} − c_{-μ}` is nonzero. This is **not** Hamming parity
`|c|_1 mod 2`.

**Theorem 1.** `f_L1(opp2)=0` and `f_L1` is one of the eight `F_cut`
1-site fillers. Lock cardinalities `(1,4,8,11,12)` and halt tick `4`.

**Theorem 2.** Exactly

```text
N_opp0 = 4
```

members of the eight fillers satisfy `f(opp2)=0`.

**Theorem 3.** `N_opp0 > 1`, so `f_L1` is not unique in that subset. A
displayed second filler `f_♦` is `1` exactly when the unbalanced-axis
count `u` satisfies `1 ≤ u ≤ 2`. It also has `f(opp2)=0` and fills, with
lock cardinalities `(1,4,8,10,11,12)` and halt tick `5`. Displayed, not
adopted.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The F_cut reconstruction, the eight 1-site fillers, the opp2 orbit, f_L1(opp2)=0, and the exact silent count N_opp0=4 are enumerated. Uniqueness of f_L1 among opp2-silent fillers is false on this patch. No physical law is selected."
trace_class: upstream_support
target_claim_id: f_cut_fillers_opp2_silent
target_blocker_text: "how many of the eight F_cut 1-site fillers vanish on opp2, and whether f_L1 is unique in that subset"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the opp2-silent filler count; any physical use must separately derive an Admissibility selector"
conditional_surface_status: "exact for F_cut 1-site fillers on this twelve-vertex patch with off-patch o=0; no Z^3-wide law and no physical selector"
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
- the opposite-pair orbit `opp2`.

No observational comparator, literature constant, Wilson weight, rate, or
generator is imported. No Record scalar functional appears.

Not leftover-character of the eight-filler count. That count only named the
eight maps. This note evaluates them on `opp2`.

## Exact Target And Objects

**Target.** Count how many of the eight `F_cut` 1-site fillers vanish on
`opp2`, and decide uniqueness of `f_L1` inside that subset.

Write a neighbor configuration as `c ∈ {0,1}^6`. A proper cube rotation `R`
acts by `(R·c)(d) = c(R^{-1}d)` on the six face directions `d`. A map
`f:{0,1}^6 → {0,1}` is cube-covariant when `f(R·c)=f(c)` for every such `R`.

The axis type of `c` is the triple `(u,b,e)` with `u+b+e=3`, where `u` is
the number of axes with `c_{+} ≠ c_{-}`, `b` the number with
`(c_{+},c_{-})=(1,1)`, and `e` the number with `(c_{+},c_{-})=(0,0)`. These
ten types are exactly the ten orbits. Complement sends `(u,b,e)` to
`(u,e,b)`.

`opp2` is the orbit `(0,1,2)`: exactly one both-occupied axis and two empty
axes. Complement sends it to `opp4=(0,2,1)`. Complement-even maps therefore
have `f(opp2)=f(opp4)`.

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
complement-even, hence lie in `F_cut`. On `opp2` one has `u=0`, so
`f_L1(opp2)=f_♦(opp2)=0`. Hamming parity also vanishes on `opp2` because
that orbit has weight `2`, but Hamming is not a filler: it halts with nine
locks. Hamming is used only as a displayed mutation: it is not `f_L1`.
`f_♦` is a displayed second silent filler: it is not adopted.

A locked set `S` determines occupancies: a lattice neighbor in `S` has
occupancy `1`, and every other neighbor — including every off-patch
neighbor — has occupancy `0`. One synchronous tick replaces `S` by

```text
S ∪ { v in two-cube \ S : f(neighborhood_6(v; S)) = 1 }.
```

The eight fillers are the members of `F_cut` whose halt set has cardinality
`12`. `N_opp0` is the number of those eight maps with `f(opp2)=0`.

## Theorems

**Theorem 1.** There are exactly 24 proper cube rotations and exactly 10
orbits on `{0,1}^6`. The three cuts leave `|F_cut|=32`. Exactly eight
members fill the twelve-vertex two-cube from seed `(0,0,0)` with off-patch
occupancy `0`. The opposite-pair orbit `opp2` is the size-`3` class
`(u,b,e)=(0,1,2)`. The unbalanced-axis map `f_L1` is one of those eight
fillers, is not Hamming parity, and satisfies `f_L1(opp2)=0`. Its lock
cardinalities are `(1,4,8,11,12)` and its halt tick is `4`.

**Theorem 2.** Exhaustive evaluation of the eight fillers on `opp2` gives

```text
N_opp0 = 4.
```

**Theorem 3.** So `N_opp0 > 1`. The map `f_L1` is silent on `opp2` and
fills, but it is not unique in that subset. The displayed second filler
`f_♦` is distinct from `f_L1` (they disagree on the three-unbalanced-axis
orbit), also has `f(opp2)=0`, and fills with lock cardinalities
`(1,4,8,10,11,12)` and halt tick `5`. Displayed, not adopted. The
predicate `f(opp2)=0` therefore does not select `f_L1` among the eight
fillers.

## Proof-Obligation Graph

| obligation | exact disposition |
|---|---|
| 24 proper cube rotations | signed permutations of the three axes with determinant `+1` |
| 10 orbits on `{0,1}^6` | axis-type classes `(u,b,e)` partition the 64 cells |
| `|F_cut|=32` | three complement-pairs and two complement-fixed orbits remain free after the vanish cuts |
| eight 1-site fillers | exhaustive 32-run census of `F_cut` to a fixed point with halt cardinality `12` |
| `opp2` orbit | representative `(1,1,0,0,0,0)`; type `(0,1,2)`; size `3` |
| `f_L1` is in `F_cut` and fills | `u` is rotation- and complement-invariant; halt set has cardinality `12` |
| `f_L1` is not Hamming | the two-unbalanced-axis orbit has even weight and `f_L1=1` |
| `f_L1(opp2)=0` | `u(opp2)=0` so the unbalanced-axis predicate vanishes |
| `N_opp0` | four of the eight fillers assign `0` to the `opp2`/`opp4` pair |
| uniqueness of silent `f_L1` | false; `f_♦` is an explicit second silent filler |
| Hamming on `opp2` | also silent, but Hamming is not a filler |
| physical Admissibility selection | open and not claimed |

Every leaf needed for the stated silent-count is discharged. No `Z^3`-wide
formation law is claimed.

## Mutations

1. Replace `f_L1` by Hamming `|c|_1 mod 2`: both vanish on `opp2`, but
   Hamming is not a filler and disagrees with `f_L1` on the
   two-unbalanced-axis orbit.
2. Replace off-patch occupancy `0` by a blank-block: first-wave candidates
   become undefined; that is a different census.
3. Drop complement-even or the vanish-on-full cut: the class is no longer
   the 32-element `F_cut`.
4. Treat the leftover eight-count as the residual: that count does not
   evaluate `opp2`.
5. Assert `N_opp0=1`: the explicit second silent filler `f_♦` refutes
   uniqueness.

## What This Does Not Claim

- No physical Admissibility selector and no adopted occupancy law.
- No Qubit rewrite and no `M_2(C)`-valued conditional probability.
- No `Z^3`-wide formation, rate, or generator.
- No identification of `f_L1` with Hamming parity.
- No leftover-character count of the eight fillers in place of this
  `opp2` evaluation.
- No blank-block, 2-site, or 3-site variant.

## No-Go Discipline Gate

The only negative claim is uniqueness: `f_L1` is not the unique `F_cut`
1-site filler with `f(opp2)=0`. The positive count `N_opp0=4` is an exact
enumeration, not a wall.

### N1 — materially distinct routes

| Route | Exact attack | Result and authority | Marker |
|---|---|---|---|
| class reconstruction | Recompute the 24 rotations, 10 orbits, `F_cut`, and the eight fillers. | Theorem 1 and check `thm1-class-reconstruction`. | **ATTEMPTED** |
| `opp2` orbit | Identify the size-`3` both-ends-of-one-axis orbit. | Theorem 1 and check `thm1-opp2-orbit`. | **ATTEMPTED** |
| Hamming-as-`f_L1` | Test whether `|c|_1 mod 2` equals the unbalanced-axis predicate. | Theorem 1 and check `thm1-f-L1-not-hamming`. | **ATTEMPTED** |
| `f_L1` on `opp2` | Evaluate `f_L1` on `opp2` and confirm it fills. | Theorem 1 and check `thm1-f-L1-opp2-silent-and-fills`. | **ATTEMPTED** |
| silent-filler census | Count fillers with `f(opp2)=0`. | Theorem 2 and check `thm2-n-opp0` give `N_opp0 = 4`. | **ATTEMPTED** |
| uniqueness of silent `f_L1` | Ask whether the silent-filler class is a singleton. | Theorem 3 and checks `thm3-not-unique` / `thm3-displayed-other`. | **ATTEMPTED** |

### N2 — wall independence and collapse

There is one negative conclusion: uniqueness of silent `f_L1` fails. The
explicit second silent filler and the cardinality `N_opp0=4` are two
certificates of the same non-uniqueness, so they collapse rather than
count as two walls.

| Pair | First closes second? | Second closes first? | Disposition |
|---|---:|---:|---|
| `N_opp0=4` / displayed `f_♦` | yes: a count larger than one is non-uniqueness | yes: one extra silent filler is non-uniqueness | collapse into the uniqueness failure |
| `f_L1(opp2)=0` / Hamming also silent | no: one map vanishing does not classify Hamming | no: Hamming vanishing does not prove `f_L1` fills | independent member facts, not two walls |
| eight-filler count / `N_opp0` | no: naming the eight does not evaluate `opp2` | no: a silent count does not replace the fill census | separate exact counts |

Physical law selection is not a wall: this note makes no negative theorem
about the existence of a selector and simply does not claim one.

### N3 — hidden-condition scan

| Phrase or premise | Classification |
|---|---|
| “work on the twelve-vertex two-cube” | explicit patch hypothesis; not a `Z^3` theorem |
| off-patch occupancy `0` | explicit default; blank-block is a different rule |
| `F_cut` | explicit three-cut class; the other 992 covariant maps are excluded |
| the eight 1-site fillers | explicit fill subclass; not leftover-character of that count |
| `opp2` | explicit opposite-pair orbit; not Hamming weight parity |
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
| `scripts/f_cut_fillers_opp2_silent_2026_08_15.py:60` | 24 proper rotations | signed permutations with determinant `+1` | yes |
| `scripts/f_cut_fillers_opp2_silent_2026_08_15.py:104` | `f_L1` definition | unbalanced-axis predicate, not Hamming | yes |
| `scripts/f_cut_fillers_opp2_silent_2026_08_15.py:44` | `opp2` representative | one fully occupied axis and four empty slots | yes |
| `scripts/f_cut_fillers_opp2_silent_2026_08_15.py:248` | silent-filler census | exact `N_opp0` among the eight fillers | yes |
| `scripts/f_cut_fillers_opp2_silent_2026_08_15.py:113` | uniqueness | displayed second silent filler `f_♦` | yes |

No evidence citation is used to claim that a physical occupancy law, a
formation rate, or a `Z^3`-wide selector has been closed.

### N5 — rhetoric and resolution audit

| Resolution | Executed? | Narrow negative supported? |
|---|---:|---|
| per element | yes: all 64 neighbor 6-tuples | each is assigned its axis-type orbit; no broader cell class is classified |
| per site | yes: the twelve two-cube vertices | each uses the same six-direction stencil with off-patch occupancy `0` |
| per mode | yes: every map in `F_cut` | the census is this class on this seed; other seeds are unclaimed |
| per block | yes: the pair `(8, N_opp0)` | uniqueness fails because `N_opp0=4` |
| lattice wide | no | no `Z^3`-wide formation or Admissibility selector is asserted |

The runner prints the same five resolution statements.

### N6 — partial closure and primitive scan

The primitive registry at `docs/audit/data/axiom_premise_nodes.json` was
checked. The only dependency used is the registered `minimal_axioms` node.
No approved primitive supplies the Boolean occupancy maps, and none is
reclassified as an import or wall.

One partial-closure mechanism is displayed rather than suppressed: `f_L1`
does fill this patch from the 1-site seed, does lie in `F_cut`, and does
vanish on `opp2`. That positive member does not make `f_L1` unique among
silent fillers and does not select it as the physical rule. The remaining
physical choice — which, if any, `F_cut` map is the Admissibility occupancy
predicate — stays explicit.

### N7 — hostile steelman

The strongest objection is that `f(opp2)=0` is independently motivated —
a filled axis should not form — so it should be enough to pick `f_L1`
among the eight fillers. That motivation is correctly about a further
cut. It does not overturn the stated theorem: among the eight fillers,
four already vanish on `opp2`. The displayed second filler `f_♦` already
differs from `f_L1` on the three-unbalanced-axis orbit, vanishes on
`opp2`, and fills by a different lock history. Hamming also vanishes on
`opp2` and is not even a filler, so silence on `opp2` is not a stand-in
for the unbalanced-axis predicate.

### N8 — cross-cycle echo

Repository search found nearby occupancy and covariance surfaces. They are
context, not load-bearing dependencies. The 24 rotations, 10 orbits,
`F_cut`, the eight fillers, and the `opp2` evaluation are recomputed here.

| Earlier surface | Similar issue | Mechanism considered here |
|---|---|---|
| `docs/ADMISSIBILITY_COVARIANT_Q8_CONDITIONAL_LAW_PAIR_BOUNDED_THEOREM_NOTE_2026-08-13.md` | proper-cubic covariance of a local rule | covariance is used only as the orbit filter for Boolean maps |
| `docs/PHYSICAL_SPATIAL_BLOCK_SEAM_DICHOTOMY_CYCLE728_NOTE_2026-08-04.md` | two-cell box `{0,1,2}×{0,1}×{0,1}` | the same twelve spatial vertices are the patch; the seam cost is unused |
| `docs/MINIMAL_AXIOMS_2026-06-29.md` | one covariant nearest-neighbor rule | the axiom names the contract; this note does not select the rule |

No earlier mechanism retires the silent-`opp2` count or restores uniqueness
of `f_L1` inside the eight-filler class.

No-Go Discipline disposition: **PASS** for the uniqueness failure and the
exact pair `(8, N_opp0)` stated above.

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
`F_cut`, identifies the eight 1-site fillers, evaluates them on `opp2`,
reports `N_opp0 = 4`, checks that `f_L1` is silent on `opp2` and is not
Hamming parity, and exhibits the displayed second silent filler `f_♦`.
Declared audit inputs are this note and the axiom memo. No runner cache is
written.
