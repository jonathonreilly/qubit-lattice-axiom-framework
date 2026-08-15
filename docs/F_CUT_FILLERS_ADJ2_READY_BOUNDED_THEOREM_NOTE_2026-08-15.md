---
claim_id: f_cut_fillers_adj2_ready_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Among the 8 F_cut 1-site fillers, N_adj1 = 8 have f(adj2)=1. f_L1 is not unique in that subset. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_fillers_adj2_ready_2026_08_15.py
---

# How Many Of The Eight `F_cut` Fillers Fire `adj2`

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact evaluation of the two-axis-contrast orbit `adj2` on the
eight cube-covariant complement-even predicates that vanish on empty and
full and that fill the twelve-vertex two-cube from a 1-site seed with
off-patch occupancy `0`. The unbalanced-axis map `f_L1` is displayed as
one filler that fires `adj2`. It is not adopted as the physical
Admissibility rule.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_fillers_adj2_ready_2026_08_15.py`](../scripts/f_cut_fillers_adj2_ready_2026_08_15.py)
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
`|locks_halt|=12`. Exactly eight members of `F_cut` fill. That
eight-count is leftover-character inventory of the three-cut fill census.
It is not the residual of this note.

The independently motivated extra asked here is the two-axis contrast
orbit. Write `adj2` for the cube orbit of weight-2 cells whose two `1`s
sit on different axes (one slot each). Equivalently, `adj2` is the
axis-type class `(u,b,e)=(2,0,1)`. It is not `opp2`, the three-cell orbit
of a fully occupied single axis with the other four slots empty. After
the 1-site first wave, the three face-diagonal sites of the first cube
see exactly an `adj2` neighborhood. So `f(adj2)=1` means two independent
nearest-neighbor contrasts form.

`f_L1(c)=1` if and only if some axis is unbalanced: `c_{+μ} ≠ c_{-μ}` for
at least one `μ ∈ {x,y,z}`. Equivalently, some discrete neighbor contrast
`n_μ = c_{+μ} − c_{-μ}` is nonzero. This is **not** Hamming parity
`|c|_1 mod 2`. Hamming is even on every weight-2 cell, so it kills
`adj2`. `f_L1` fires it.

**Theorem 1.** `f_L1(adj2)=1`. The map `f_L1` is one of the eight
`F_cut` 1-site fillers.

**Theorem 2.** Exactly `N_adj1 = 8` members of that eight-element set
have `f(adj2)=1`. Every filler fires `adj2`.

**Theorem 3.** So `N_adj1 > 1`: `f_L1` is not unique in that subset. A
displayed second filler `f_♦` is `1` exactly when the unbalanced-axis
count `u` satisfies `1 ≤ u ≤ 2`. It also fires `adj2` and also fills.
Displayed, not adopted.

Not leftover-character of the eight-count.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The ten-orbit reconstruction, the eight F_cut fillers, membership of f_L1, the adj2 orbit, and the exact firing count N_adj1=8 are enumerated. Uniqueness of f_L1 among adj2-firing fillers is false on this patch. No physical law is selected."
trace_class: upstream_support
target_claim_id: f_cut_fillers_adj2_ready
target_blocker_text: "how many of the eight F_cut 1-site fillers fire adj2, and whether f_L1 is unique in that subset"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the adj2-firing census among the eight fillers; any physical use must separately derive an Admissibility selector"
conditional_surface_status: "exact for F_cut fillers on this twelve-vertex patch with off-patch o=0; no Z^3-wide law and no physical selector"
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
- the `adj2` orbit of two-axis weight-2 cells.

No observational comparator, literature constant, Wilson weight, rate, or
generator is imported. No Record scalar functional appears.

## Exact Target And Objects

**Target.** Count how many of the eight `F_cut` 1-site fillers fire the
two-axis-contrast orbit `adj2`, and decide uniqueness of `f_L1` inside
that subset.

Write a neighbor configuration as `c ∈ {0,1}^6`. A proper cube rotation `R`
acts by `(R·c)(d) = c(R^{-1}d)` on the six face directions `d`. A map
`f:{0,1}^6 → {0,1}` is cube-covariant when `f(R·c)=f(c)` for every such `R`.
The axis type of `c` is the triple `(u,b,e)` with `u+b+e=3`, where `u` is
the number of axes with `c_{+} ≠ c_{-}`, `b` the number with
`(c_{+},c_{-})=(1,1)`, and `e` the number with `(c_{+},c_{-})=(0,0)`. These
ten types are exactly the ten orbits. Complement sends `(u,b,e)` to
`(u,e,b)`.

`F_cut` is the class of cube-covariant maps with `f(empty)=f(full)=0` and
`f(c)=f(1-c)`. The empty/full pair is forced to `0`. The remaining free
data are three complement-pair bits and two complement-fixed orbit bits,
so `|F_cut|=32`. The eight fillers are the members of `F_cut` whose halt
set on this patch has cardinality 12. They are recomputed here.

There are fifteen weight-2 cells. Three of them occupy both ends of one
axis; that is the `opp2` orbit `(0,1,2)`. The other twelve occupy one
slot on each of two different axes; that is `adj2`, the orbit `(2,0,1)`.
Complement sends `adj2` to `(2,1,0)`, so every map in `F_cut` assigns
those two orbits the same bit.

Define

```text
f_L1(c)     = 1  iff  u(c) ≥ 1,
f_♦(c)      = 1  iff  1 ≤ u(c) ≤ 2,
f_H(c)      = |c|_1 mod 2.
```

`f_L1` and `f_♦` lie in the eight-element filler set. `f_H` lies in
`F_cut` and is used only as a displayed mutation: it is even on every
weight-2 cell, so `f_H(adj2)=0`. It is not `f_L1`. `f_♦` is a displayed
second `adj2`-firing filler: it is not adopted.

A locked set `S` determines occupancies: a lattice neighbor in `S` has
occupancy `1`, and every other neighbor — including every off-patch
neighbor — has occupancy `0`. From the 1-site seed, the first wave locks
the three axis neighbors of the origin. Each of the three face-diagonal
sites `(1,1,0)`, `(1,0,1)`, `(0,1,1)` then sees two locked nearest
neighbors on different axes, which is an `adj2` 6-tuple.

`N_adj1` is the number of maps in the eight-element filler set with
`f(adj2)=1`.

## Theorems

**Theorem 1.** There are exactly 24 proper cube rotations and exactly 10
orbits on `{0,1}^6`. The orbit `adj2` is the 12-cell class `(2,0,1)` of
weight-2 two-axis cells. It is not `opp2`. The unbalanced-axis map
`f_L1` is one of the eight `F_cut` 1-site fillers. It is not Hamming
parity. On every cell of `adj2`, `f_L1=1`.

**Theorem 2.** Exhaustive evaluation of the eight fillers on `adj2` gives

```text
N_adj1 = 8.
```

Every `F_cut` 1-site filler fires the two-axis contrast.

**Theorem 3.** So `N_adj1 > 1`. The map `f_L1` fires `adj2`, but it is
not unique in that subset. The displayed second filler `f_♦` is distinct
from `f_L1` (they disagree on the three-unbalanced-axis orbit), also
fires `adj2`, and also fills, with lock cardinalities `(1,4,8,10,11,12)`
and halt tick `5`. Displayed, not adopted.

## Proof-Obligation Graph

| obligation | exact disposition |
|---|---|
| 24 proper cube rotations | signed permutations of the three axes with determinant `+1` |
| 10 orbits on `{0,1}^6` | axis-type classes `(u,b,e)` partition the 64 cells |
| `adj2` is the two-axis weight-2 orbit | 12 cells of type `(2,0,1)`; the other 3 weight-2 cells are `opp2` |
| face-diagonal first-wave neighborhoods | after the 1-site first wave, `(1,1,0)`, `(1,0,1)`, `(0,1,1)` see `adj2` |
| `f_L1` is unbalanced-axis, not Hamming | `u ≥ 1`; Hamming is even on `adj2` and disagrees |
| `f_L1(adj2)=1` | `u(adj2)=2` |
| `f_L1` is one of the eight fillers | halt set has cardinality 12 at tick 4 |
| eight fillers recomputed | exhaustive 32-run census of `F_cut` to a fixed point |
| `N_adj1` | all eight fillers assign `1` to `adj2` |
| uniqueness of `f_L1` among adj2-firing fillers | false; `f_♦` is an explicit second member |
| physical Admissibility selection | open and not claimed |

Every leaf needed for the stated census is discharged. No `Z^3`-wide
formation law is claimed.

## Mutations

1. Replace `f_L1` by Hamming `|c|_1 mod 2`: the maps disagree on `adj2`,
   and Hamming is even on every weight-2 cell.
2. Replace `adj2` by `opp2`: that is a different orbit (balanced axis),
   not the two-axis contrast.
3. Drop complement-even or the vanish-on-full cut: the class is no longer
   the 32-element `F_cut`, so the eight fillers are a different set.
4. Seed a second on-patch site: the first-wave face-diagonal neighborhoods
   change.
5. Assert `N_adj1=1`: the explicit second filler `f_♦` refutes uniqueness.

## What This Does Not Claim

- No physical Admissibility selector and no adopted occupancy law.
- No Qubit rewrite and no `M_2(C)`-valued conditional probability.
- No `Z^3`-wide formation, rate, or generator.
- No identification of `f_L1` with Hamming parity.
- No leftover-character reuse of the eight-count in place of this
  `adj2`-firing census.
- No claim that `adj2=1` selects `f_L1` among the eight fillers.
- No blank-block, 2-site, or 3-site variant.

## No-Go Discipline Gate

The only negative claim is uniqueness: `f_L1` is not the unique
`adj2`-firing `F_cut` filler of this patch. The positive count
`N_adj1=8` is an exact enumeration, not a wall.

### N1 — materially distinct routes

| Route | Exact attack | Result and authority | Marker |
|---|---|---|---|
| orbit reconstruction | Recompute the 24 rotations and the 10 axis-type orbits. | Theorem 1 and checks `thm1-twenty-four-rotations` / `thm1-ten-orbits`. | **ATTEMPTED** |
| `adj2` versus `opp2` | Split the 15 weight-2 cells into the 12-cell two-axis orbit and the 3-cell opposite-pair orbit. | Theorem 1 and check `thm1-adj2-orbit`. | **ATTEMPTED** |
| Hamming-as-`f_L1` | Test whether `|c|_1 mod 2` equals the unbalanced-axis predicate on `adj2`. | Theorem 1 and check `thm1-f-L1-not-hamming` separate the maps. | **ATTEMPTED** |
| `f_L1` on `adj2` | Evaluate `f_L1` on every cell of `adj2`. | Theorem 1 and check `thm1-f-L1-fires-adj2`. | **ATTEMPTED** |
| filler `adj2` census | Recompute the eight fillers and evaluate each on `adj2`. | Theorem 2 and check `thm2-n-adj1` give `N_adj1 = 8`. | **ATTEMPTED** |
| uniqueness of `f_L1` | Ask whether the adj2-firing filler class is a singleton. | Theorem 3 and checks `thm3-not-unique` / `thm3-displayed-other-filler`. | **ATTEMPTED** |

### N2 — wall independence and collapse

There is one negative conclusion: uniqueness fails. The explicit second
filler and the cardinality `N_adj1=8` are two certificates of the same
non-uniqueness, so they collapse rather than count as two walls.

| Pair | First closes second? | Second closes first? | Disposition |
|---|---:|---:|---|
| `N_adj1=8` / displayed `f_♦` | yes: a count larger than one is non-uniqueness | yes: one extra filler is non-uniqueness | collapse into the uniqueness failure |
| `f_L1` fires `adj2` / Hamming kills `adj2` | no: one map firing does not classify Hamming | no: Hamming killing `adj2` does not prove `f_L1` fires it | independent positive/negative members, not two walls |
| eight-count / `N_adj1` | no: membership in the filler set is not the adj2 bit | no: an adj2 count does not replace the fill census | separate exact counts |

Physical law selection is not a wall: this note makes no negative theorem
about the existence of a selector and simply does not claim one.

### N3 — hidden-condition scan

| Phrase or premise | Classification |
|---|---|
| “work on the twelve-vertex two-cube” | explicit patch hypothesis; not a `Z^3` theorem |
| off-patch occupancy `0` | explicit default; blank-block is a different rule |
| `F_cut` | explicit three-cut class; the other 992 covariant maps are excluded |
| “the eight fillers” | explicit fill subset of `F_cut`; recomputed, not imported as leftover |
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
| `scripts/f_cut_fillers_adj2_ready_2026_08_15.py:60` | 24 proper rotations | signed permutations with determinant `+1` | yes |
| `scripts/f_cut_fillers_adj2_ready_2026_08_15.py:104` | `f_L1` definition | unbalanced-axis predicate, not Hamming | yes |
| `scripts/f_cut_fillers_adj2_ready_2026_08_15.py:47` | `adj2` orbit | axis type `(2,0,1)`, not `opp2` | yes |
| `scripts/f_cut_fillers_adj2_ready_2026_08_15.py:248` | eight-filler census | exact fill subset of `F_cut` | yes |
| `scripts/f_cut_fillers_adj2_ready_2026_08_15.py:113` | uniqueness | displayed second filler `f_♦` | yes |

No evidence citation is used to claim that a physical occupancy law, a
formation rate, or a `Z^3`-wide selector has been closed.

### N5 — rhetoric and resolution audit

| Resolution | Executed? | Narrow negative supported? |
|---|---:|---|
| per element | yes: all 64 neighbor 6-tuples | each is assigned its axis-type orbit; no broader cell class is classified |
| per site | yes: the twelve two-cube vertices | each uses the same six-direction stencil with off-patch occupancy `0` |
| per mode | yes: every `F_cut` 1-site filler | the census is this class on this seed; other seeds are unclaimed |
| per block | yes: the pair `(8, N_adj1)` | uniqueness fails because `N_adj1=8` |
| lattice wide | no | no `Z^3`-wide formation or Admissibility selector is asserted |

The runner prints the same five resolution statements.

### N6 — partial closure and primitive scan

The primitive registry at `docs/audit/data/axiom_premise_nodes.json` was
checked. The only dependency used is the registered `minimal_axioms` node.
No approved primitive supplies the Boolean occupancy maps, and none is
reclassified as an import or wall.

One partial-closure mechanism is displayed rather than suppressed: `f_L1`
does fire `adj2` and does fill this patch from the 1-site seed. That
positive member does not make `f_L1` unique and does not select it as the
physical rule. The remaining physical choice — which, if any, `F_cut` map
is the Admissibility occupancy predicate — stays explicit. In particular,
`adj2=1` does not cut the eight-element set.

### N7 — hostile steelman

The strongest objection is that `adj2=1` is forced by the fill requirement
itself, so counting `N_adj1=8` is just restating that the eight maps fill.
The first-wave face-diagonal sites do see `adj2`, and every filler must
lock them to reach twelve vertices along the observed histories. That
objection correctly identifies a necessary condition for fill on this
patch. It does not retire the stated theorem: among the eight fillers, the
independently named two-axis bit is `1` on every member, so it does not
select `f_L1`. The displayed second filler `f_♦` already differs from
`f_L1` on the three-unbalanced-axis orbit and still fires `adj2`. That is
a class-level extra, not a tautology of the eight-count.

### N8 — cross-cycle echo

Repository search found nearby occupancy and covariance surfaces. They are
context, not load-bearing dependencies. The 24 rotations, 10 orbits,
`F_cut`, the eight fillers, and the `adj2` bit are recomputed here.

| Earlier surface | Similar issue | Mechanism considered here |
|---|---|---|
| `docs/ADMISSIBILITY_COVARIANT_Q8_CONDITIONAL_LAW_PAIR_BOUNDED_THEOREM_NOTE_2026-08-13.md` | proper-cubic covariance of a local rule | covariance is used only as the orbit filter for Boolean maps |
| `docs/CUBIC_NN_CONDITION_DOMAIN_SEPARATION_BOUNDED_THEOREM_NOTE_2026-08-13.md` | six-neighbor stencil of `Z^3` | the same six directions define occupancy 6-tuples; the product-kernel claim is unused |
| `docs/MINIMAL_AXIOMS_2026-06-29.md` | one covariant nearest-neighbor rule | the axiom names the contract; this note does not select the rule |

No earlier mechanism retires the `adj2`-firing census among the eight
fillers or restores uniqueness of `f_L1` inside that subset.

No-Go Discipline disposition: **PASS** for the uniqueness failure and the
exact pair `(8, N_adj1)` stated above.

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
`F_cut`, recomputes the eight 1-site fillers, identifies the `adj2` orbit,
reports `N_adj1 = 8`, checks that `f_L1` fires `adj2` and is not Hamming
parity, and exhibits the displayed second filler `f_♦`. Declared audit
inputs are this note and the axiom memo. No runner cache is written.
