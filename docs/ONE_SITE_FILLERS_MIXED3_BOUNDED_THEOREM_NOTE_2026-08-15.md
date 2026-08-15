---
claim_id: one_site_fillers_mixed3_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Among the 96 cube-covariant 1-site fillers on the two-cube with off-patch o=0, N_mix3 = 48 have f(mixed3)=1. f_L1 is not unique in that subset. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/one_site_fillers_mixed3_2026_08_15.py
---

# Mixed3 Among The Ninety-Six One-Site Fillers

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact count of how many of the 96 cube-covariant 1-site
fillers of the twelve-vertex two-cube fire the mixed-triple orbit
`mixed3`. The unbalanced-axis map `f_L1` is displayed as one such
filler. It is not adopted as the physical Admissibility rule.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/one_site_fillers_mixed3_2026_08_15.py`](../scripts/one_site_fillers_mixed3_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

The 24 proper cube rotations act on neighbor 6-tuples in `{0,1}^6` and
partition those 64 cells into 10 orbits. Cube-covariant predicates are the
`{0,1}`-assignments to those orbits. Restrict to `f(empty)=0`: there are
512 such maps. On the two-cube `{0,1,2}×{0,1}×{0,1}`, seed `(0,0,0)`
starts locked. Off-patch neighbors have occupancy `0`. Each tick, every
unlocked on-patch vertex evaluates `f` on its six-neighbor occupancy
tuple and locks if `f=1`. Fill means `|locks_halt|=12`. Reconstructing
that dynamics on every cube-covariant map with `f(empty)=0` yields
exactly 96 fillers.

That 96-element fill set is leftover-character inventory of the raw
1-site fill census (#6393). It is not the residual of this note. This
note asks an independently motivated extra on those 96: how many fire
`mixed3`. It is not a fifth bit-split of the eight `F_cut` fillers.

`mixed3` is the `G`-orbit of axis type `(1,1,1)`: one unbalanced axis,
one fully occupied axis, and one empty axis. A representative is
`(c_{+x},c_{-x},c_{+y},c_{-y},c_{+z},c_{-z})=(1,0,1,1,0,0)`. The orbit
has size `12`. `f(mixed3)=1` means a mixed-triple cell forms. L1 fires
`mixed3`.

The remaining named orbits used only to display a rival member are

| name | `(u,b,e)` | geometric reading | L1 value |
|---|---|---|---:|
| `wt1` | `(1,0,2)` | one-axis contrast; a 1-site wave | 1 |
| `opp2` | `(0,1,2)` | opposite pair; balanced axis silent | 0 |
| `adj2` | `(2,0,1)` | two-axis contrast forms | 1 |
| `vertex3` | `(3,0,0)` | three-axis contrast; cube-vertex type | 1 |
| `mixed3` | `(1,1,1)` | mixed triple | 1 |

`f_L1(c)=1` if and only if some axis is unbalanced: `c_{+μ} ≠ c_{-μ}` for
at least one `μ ∈ {x,y,z}`. Equivalently, some discrete neighbor contrast
`n_μ = c_{+μ} − c_{-μ}` is nonzero. This is **not** Hamming parity
`|c|_1 mod 2`.

**Theorem 1.** `f_L1` is one of the 96 fillers and `f_L1(mixed3)=1`.
Lock cardinalities `(1,4,8,11,12)` and halt tick `4`.

**Theorem 2.** Exactly

```text
N_mix3 = 48
```

members of the 96 fillers satisfy `f(mixed3)=1`.

**Theorem 3.** `N_mix3 > 1`, so `mixed3=1` does not select `f_L1` among
the 96. A displayed second filler `f_♦` is `1` exactly when the
unbalanced-axis count `u` satisfies `u ≥ 1` and the cell is not of
vertex type `(3,0,0)`. Its remaining-bit tuple is
`(wt1,opp2,adj2,vertex3,mixed3)=(1,0,1,0,1)`. It also has
`f(mixed3)=1` and fills, with lock cardinalities `(1,4,8,10,11,12)` and
halt tick `5`. Displayed, not adopted. Do not write mixed3 into
Admissibility.

Not leftover-character of #6404 (that AND-ed mixed3 on the 10→eight).
Not leftover-character of #6402. Not leftover-character of #6403.
Not leftover-character of #6405 (those split the eight). This is an
independently motivated extra on the 96.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The ten-orbit reconstruction, the 96 1-site fillers, membership of f_L1, f_L1(mixed3)=1, and the exact count N_mix3=48 are enumerated. Uniqueness of f_L1 among mixed3=1 fillers is false on this patch. mixed3 is displayed, not written into Admissibility."
trace_class: upstream_support
target_claim_id: one_site_fillers_mixed3
target_blocker_text: "how many of the 96 cube-covariant 1-site fillers fire mixed3, and whether f_L1 is unique in that subset"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the mixed3 filler count; any physical use must separately derive an Admissibility selector"
conditional_surface_status: "exact for the 96 1-site fillers on this twelve-vertex patch with off-patch o=0; no Z^3-wide law and no physical selector"
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
- the mixed-triple orbit `mixed3`.

No observational comparator, literature constant, Wilson weight, rate, or
generator is imported. No Record scalar functional appears.

Not leftover-character of #6393. That census only named the 96 maps. This
note evaluates them on `mixed3`. Not leftover-character of #6404. Not
leftover-character of the eight-filler bit splits #6402/#6403/#6405.

## Exact Target And Objects

**Target.** Count how many of the 96 cube-covariant 1-site fillers fire
`mixed3`, and decide uniqueness of `f_L1` inside that subset.

Write a neighbor configuration as `c ∈ {0,1}^6`. A proper cube rotation `R`
acts by `(R·c)(d) = c(R^{-1}d)` on the six face directions `d`. A map
`f:{0,1}^6 → {0,1}` is cube-covariant when `f(R·c)=f(c)` for every such `R`.
Equivalently, `f` is constant on each orbit.

The axis type of `c` is the triple `(u,b,e)` with `u+b+e=3`, where `u` is
the number of axes with `c_{+} ≠ c_{-}`, `b` the number with
`(c_{+},c_{-})=(1,1)`, and `e` the number with `(c_{+},c_{-})=(0,0)`. These
ten types are exactly the ten orbits. Complement sends `(u,b,e)` to
`(u,e,b)`.

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

`mixed3` is complement-fixed: it is the unique weight-3 orbit with one
axis of each kind. The class under study is every cube-covariant `f` with
`f(empty)=0`, not the three-cut subclass `F_cut`. There are `2^9=512`
such maps.

Define

```text
f_L1(c)     = 1  iff  u(c) ≥ 1,
f_♦(c)      = 1  iff  u(c) ≥ 1 and (u,b,e) ≠ (3,0,0),
f_H(c)      = |c|_1 mod 2.
```

All three are cube-covariant and vanish on empty. On `mixed3` one has
`u=1`, so `f_L1(mixed3)=f_♦(mixed3)=1`. Hamming parity also fires
`mixed3` because that orbit has odd weight `3`, but Hamming is not a
filler: it does not halt with twelve locks. Hamming is used only as a
displayed mutation: it is not `f_L1`. `f_♦` is a displayed second
`mixed3=1` filler: it is not adopted. Its remaining-bit tuple is
`(1,0,1,0,1)`, which differs from L1's tuple `(1,0,1,1,1)` on
`vertex3`.

A locked set `S` determines occupancies: a lattice neighbor in `S` has
occupancy `1`, and every other neighbor — including every off-patch
neighbor — has occupancy `0`. One synchronous tick replaces `S` by

```text
S ∪ { v in two-cube \ S : f(neighborhood_6(v; S)) = 1 }.
```

The 96 fillers are the cube-covariant maps with `f(empty)=0` whose halt
set has cardinality `12`. `N_mix3` is the number of those 96 maps with
`f(mixed3)=1`. Do not write mixed3 into Admissibility.

## Theorems

**Theorem 1.** There are exactly 24 proper cube rotations and exactly 10
orbits on `{0,1}^6`. Exactly 512 cube-covariant maps vanish on empty.
Exactly 96 of them fill the twelve-vertex two-cube from seed `(0,0,0)`
with off-patch occupancy `0`. The mixed-triple orbit `mixed3` is the
size-`12` class `(u,b,e)=(1,1,1)`. The unbalanced-axis map `f_L1` is one
of those 96 fillers, is not Hamming parity, and satisfies
`f_L1(mixed3)=1`. Its remaining-bit tuple is
`(wt1,opp2,adj2,vertex3,mixed3)=(1,0,1,1,1)`. Its lock cardinalities are
`(1,4,8,11,12)` and its halt tick is `4`.

**Theorem 2.** Exhaustive evaluation of the 96 fillers on `mixed3` gives

```text
N_mix3 = 48.
```

Equivalently, exactly half of the 96 fillers fire `mixed3`. Flipping the
`mixed3` bit of any filler yields another filler: the 1-site fill
dynamics on this patch with off-patch occupancy `0` never uses a
`mixed3` neighborhood as a lock predicate.

**Theorem 3.** So `N_mix3 > 1`. The map `f_L1` fires `mixed3` and fills,
but it is not unique in that subset. The displayed second filler `f_♦`
is distinct from `f_L1` (they disagree on the three-unbalanced-axis
orbit), also has `f(mixed3)=1`, has remaining-bit tuple `(1,0,1,0,1)`,
and fills with lock cardinalities `(1,4,8,10,11,12)` and halt tick `5`.
Displayed, not adopted. The predicate `f(mixed3)=1` therefore does not
select `f_L1` among the 96 fillers. Do not write mixed3 into
Admissibility.

## Proof-Obligation Graph

| obligation | exact disposition |
|---|---|
| 24 proper cube rotations | signed permutations of the three axes with determinant `+1` |
| 10 orbits on `{0,1}^6` | axis-type classes `(u,b,e)` partition the 64 cells with the listed sizes |
| 512 empty-vanishing maps | nine free orbit bits after `f(empty)=0` |
| 96 fillers | exhaustive 512-run census to a fixed point with `|locks|=12` |
| `mixed3` orbit | representative `(1,0,1,1,0,0)`; type `(1,1,1)`; size `12` |
| `f_L1` is in the 96 | halt set has cardinality 12 at tick 4 |
| `f_L1` is not Hamming | the two-unbalanced-axis orbit `adj2` has even weight and `f_L1=1` |
| `f_L1(mixed3)=1` | `u(mixed3)=1` so the unbalanced-axis predicate fires |
| `N_mix3` | count of the 96 whose `mixed3` bit equals 1 |
| uniqueness of mixed3-ready `f_L1` | false; `f_♦` is an explicit second mixed3-ready filler |
| Hamming on `mixed3` | also fires, but Hamming is not a filler |
| physical Admissibility selection | open and not claimed; mixed3 is not written in |

Every leaf needed for the stated mixed3 census is discharged. No
`Z^3`-wide formation law is claimed.

## Mutations

1. Replace `f_L1` by Hamming `|c|_1 mod 2`: both fire `mixed3`, but
   Hamming is not a filler and disagrees with `f_L1` on the
   two-unbalanced-axis orbit.
2. Replace off-patch occupancy `0` by a blank-block: first-wave candidates
   become undefined; that is a different census.
3. Restrict the class to `F_cut` and AND mixed3 with the other L1 bits:
   that is leftover-character of #6404, a different residual.
4. Split only the eight `F_cut` fillers on one remaining bit: that is
   leftover-character of #6402/#6403/#6405.
5. Assert `N_mix3=1`: the explicit second mixed3-ready filler `f_♦`
   refutes uniqueness.

## What This Does Not Claim

- No physical Admissibility selector and no adopted occupancy law.
- No Qubit rewrite and no `M_2(C)`-valued conditional probability.
- No `Z^3`-wide formation, rate, or generator.
- No identification of `f_L1` with Hamming parity.
- No leftover-character restatement of the 96-filler census (#6393), of
  the #6404 AND on the eight, or of the #6402/#6403/#6405 bit-splits of
  the eight, in place of this mixed3 count on the 96.
- No blank-block, 2-site, or 3-site variant.
- No axiom edit: mixed3 is displayed, not written into Admissibility.

## No-Go Discipline Gate

The only negative claim is uniqueness: `f_L1` is not the unique 1-site
filler with `f(mixed3)=1`. The positive count `N_mix3=48` is an exact
enumeration, not a wall.

### N1 — materially distinct routes

| Route | Exact attack | Result and authority | Marker |
|---|---|---|---|
| orbit reconstruction | Recompute the 24 rotations and the 10 axis-type orbits. | Theorem 1 and checks `thm1-twenty-four-rotations` / `thm1-ten-orbits`. | **ATTEMPTED** |
| 96-filler reconstruction | Run every empty-vanishing cube-covariant map to a fixed point and keep `|locks|=12`. | Theorem 1 and check `thm1-ninety-six-fillers` give 96 fillers. | **ATTEMPTED** |
| `mixed3` orbit | Identify the size-`12` one-unbalanced / one-both / one-empty orbit. | Theorem 1 and check `thm1-mixed3-orbit`. | **ATTEMPTED** |
| Hamming-as-`f_L1` | Test whether `|c|_1 mod 2` equals the unbalanced-axis predicate. | Theorem 1 and check `thm1-f-L1-not-hamming` separate the maps. | **ATTEMPTED** |
| `N_mix3` census | Filter the 96 fillers by `f(mixed3)=1`. | Theorem 2 and check `thm2-n-mix3` give `N_mix3 = 48`. | **ATTEMPTED** |
| uniqueness of mixed3-ready `f_L1` | Ask whether the mixed3-ready class is a singleton. | Theorem 3 and checks `thm3-not-unique` / `thm3-displayed-other`. | **ATTEMPTED** |

### N2 — wall independence and collapse

There is one negative conclusion: uniqueness of mixed3-ready `f_L1`
fails. The explicit second mixed3-ready filler and the cardinality
`N_mix3=48` are two certificates of the same non-uniqueness, so they
collapse rather than count as two walls.

| Pair | First closes second? | Second closes first? | Disposition |
|---|---:|---:|---|
| `N_mix3=48` / displayed `f_♦` | yes: a count larger than one is non-uniqueness | yes: one extra mixed3-ready filler is non-uniqueness | collapse into the uniqueness failure |
| `f_L1(mixed3)=1` / Hamming also fires | no: one map firing does not classify Hamming | no: Hamming firing does not prove `f_L1` fills | independent member facts, not two walls |
| 96-filler count / `N_mix3` | no: naming the 96 does not evaluate `mixed3` | no: a mixed3 count does not replace the fill census | separate exact counts |

Physical law selection is not a wall: this note makes no negative theorem
about the existence of a selector and simply does not claim one.

### N3 — hidden-condition scan

| Phrase or premise | Classification |
|---|---|
| “work on the twelve-vertex two-cube” | explicit patch hypothesis; not a `Z^3` theorem |
| off-patch occupancy `0` | explicit default; blank-block is a different rule |
| the 96 fillers | explicit empty-vanishing 1-site fill set; not leftover-character of #6393 |
| `mixed3` | explicit mixed-triple orbit; independently motivated extra on the 96 |
| remaining-bit tuple | display label for a rival member; not a #6404 AND |
| “lock” | Record permanence on this Boolean occupancy model, not a possibility-valued law |
| “cube-covariant” | invariance under the 24 proper rotations, cited to Lattice/Admissibility |
| Hamming parity | displayed mutation only |
| `f_♦` | displayed witness against uniqueness, not a selected law |
| `N_mix3=48` | displayed non-uniqueness inside the 96, not an Admissibility clause |

### N4 — citation-to-residual matching

| Evidence path:line | Residual attacked | Residual claimed closed | Match? |
|---|---|---|---:|
| `docs/MINIMAL_AXIOMS_2026-06-29.md:37` | ambient lattice and cubic rotations | sites are `Z^3` with proper cubic rotations | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:57` | covariant nearest-neighbor rule | covariance is the class filter, not a selector | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:79` | lock permanence | a locked site stays locked | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:83` | unreadability of absence | unlocked and off-patch sites contribute occupancy `0`, not a readout | yes |
| `scripts/one_site_fillers_mixed3_2026_08_15.py:72` | 24 proper rotations | signed permutations with determinant `+1` | yes |
| `scripts/one_site_fillers_mixed3_2026_08_15.py:111` | `f_L1` definition | unbalanced-axis predicate, not Hamming | yes |
| `scripts/one_site_fillers_mixed3_2026_08_15.py:116` | Hamming mutation | `|c|_1 mod 2` is a different map | yes |
| `scripts/one_site_fillers_mixed3_2026_08_15.py:49` | `mixed3` representative | one unbalanced, one both-occupied, one empty axis | yes |
| `scripts/one_site_fillers_mixed3_2026_08_15.py:221` | 96-filler reconstruction | empty-vanishing maps with `|locks|=12` | yes |
| `scripts/one_site_fillers_mixed3_2026_08_15.py:298` | `N_mix3` | mixed3=1 cardinality inside the 96 | yes |
| `scripts/one_site_fillers_mixed3_2026_08_15.py:120` | uniqueness | displayed second mixed3-ready filler `f_♦` | yes |

No evidence citation is used to claim that a physical occupancy law, a
formation rate, or a `Z^3`-wide selector has been closed.

### N5 — rhetoric and resolution audit

| Resolution | Executed? | Narrow negative supported? |
|---|---:|---|
| per element | yes: all 64 neighbor 6-tuples | each is assigned its axis-type orbit; no broader cell class is classified |
| per site | yes: the twelve two-cube vertices | each uses the same six-direction stencil with off-patch occupancy `0` |
| per mode | yes: every cube-covariant `f` with `f(empty)=0` | the census is this class on this seed; other seeds are unclaimed |
| per block | yes: the pair `(96, N_mix3)` | uniqueness fails because `N_mix3=48` |
| lattice wide | no | no `Z^3`-wide formation or Admissibility selector is asserted |

The runner prints the same five resolution statements.

### N6 — partial closure and primitive scan

The primitive registry at `docs/audit/data/axiom_premise_nodes.json` was
checked. The only dependency used is the registered `minimal_axioms` node.
No approved primitive supplies the Boolean occupancy maps, and none is
reclassified as an import or wall.

One partial-closure mechanism is displayed rather than suppressed: `f_L1`
does fill this patch from the 1-site seed and does fire `mixed3`. That
positive member does not make `f_L1` unique among mixed3-ready fillers
and does not select it as the physical rule. The remaining physical
choice — which, if any, occupancy predicate is the Admissibility rule —
stays explicit. Do not write mixed3 into Admissibility.

### N7 — hostile steelman

The strongest objection is that `f(mixed3)=1` is independently motivated
— a mixed-triple cell should form — so it should be enough to pick
`f_L1` among the 96 fillers. That motivation is correctly about a
further cut. It does not overturn the stated theorem: among the 96
fillers, 48 already fire `mixed3`. The displayed second filler `f_♦`
already differs from `f_L1` on the three-unbalanced-axis orbit, fires
`mixed3`, and fills by a different lock history. Hamming also fires
`mixed3` and is not even a filler, so readiness on `mixed3` is not a
stand-in for the unbalanced-axis predicate. A second objection is that
this note is leftover-character of #6404, which already used `mixed3=1`
inside an AND on the eight `F_cut` fillers. That is a different class
and a different residual: the present count is `N_mix3` among the 96,
with no AND and no `F_cut` restriction.

### N8 — cross-cycle echo

Repository search found nearby occupancy and covariance surfaces. They are
context, not load-bearing dependencies. The 24 rotations, 10 orbits,
96 fillers, `mixed3` evaluation, and `N_mix3` are recomputed here.

| Earlier surface | Similar issue | Mechanism considered here |
|---|---|---|
| `docs/ADMISSIBILITY_COVARIANT_Q8_CONDITIONAL_LAW_PAIR_BOUNDED_THEOREM_NOTE_2026-08-13.md` | proper-cubic covariance of a local rule | covariance is used only as the orbit filter for Boolean maps |
| `docs/PHYSICAL_SPATIAL_BLOCK_SEAM_DICHOTOMY_CYCLE728_NOTE_2026-08-04.md` | two-cell box `{0,1,2}×{0,1}×{0,1}` | the same twelve spatial vertices are the patch; the seam cost is unused |
| `docs/MINIMAL_AXIOMS_2026-06-29.md` | one covariant nearest-neighbor rule | the axiom names the contract; this note does not select the rule |

The 96-filler census (#6393) is the class this note filters. It is not a
parent and does not close `N_mix3`. The eight-filler AND (#6404) and the
eight-filler bit splits (#6402/#6403/#6405) are different residuals.

No earlier mechanism retires the mixed3 count on the 96 or writes mixed3
into Admissibility.

No-Go Discipline disposition: **PASS** for the uniqueness failure and the
exact pair `(96, N_mix3)` stated above.

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

The companion runner reconstructs the 24 rotations and 10 orbits,
reconstructs the 96 1-site fillers, evaluates them on `mixed3`, reports
`N_mix3 = 48`, checks that `f_L1` is one of the 96 and fires `mixed3`
and is not Hamming parity, and exhibits the displayed second
mixed3-ready filler `f_♦` by its remaining-bit tuple `(1,0,1,0,1)`.
Declared audit inputs are this note and the axiom memo. No runner cache is
written.
