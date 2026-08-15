---
claim_id: f_cut_four_site_coverage_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Among the 32 F_cut maps on the two-cube with off-patch o=0, the maximum number of 4-site seeds filled is 495, attained by 1 map. f_L1 is not the unique maximizer. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_four_site_coverage_2026_08_15.py
---

# Four-Site Fill Coverage Ranking Inside The Three-Cut Class `F_cut`

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact occupancy-to-lock coverage ranking of the 32 cube-covariant
complement-even predicates that vanish on empty and full, on the
twelve-vertex two-cube, over all 495 unordered 4-site seeds, with
off-patch occupancy `0`. The unbalanced-axis map `f_L1` and the remaining-bit
tuple `f1=(1,1,1,1,1)` are displayed as scored members. Neither is adopted
as the physical Admissibility rule.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_four_site_coverage_2026_08_15.py`](../scripts/f_cut_four_site_coverage_2026_08_15.py)
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
class. The 2-site coverage ranking of the same 32 maps (#6429) is a
different leftover inventory: it used a different seed cardinality `|S|`.
The 3-site coverage ranking (#6453) is again a different leftover: also a
different `|S|`, and it found two maximizers, `f_L1` and `f1`. The joint
2+3 maximizer identity (#6457) names a pair of coverage scores, not this
`|S|=4` ranking. This note is not a seed-table of two named maps. It asks
the new ranking object: among all 32 maps, how many of the 495 four-site
seeds does each fill, and is `f_L1` the unique maximizer.

On the two-cube `{0,1,2}×{0,1}×{0,1}`, each unordered 4-set of vertices is
a 4-site seed. There are `C(12,4)=495` such seeds. Off-patch neighbors
have occupancy `0`. Each tick, every unlocked on-patch vertex evaluates
`f` on its six-neighbor occupancy tuple and locks if `f=1`. The process
is synchronous and stops at a fixed point in at most 12 ticks. Fill means
`|locks_halt|=12`. Coverage is

```text
cov4(f) = |{ S : |S|=4 and f fills from S }|.
```

Do not list the seeds.

`f_L1(c)=1` if and only if some axis is unbalanced: `c_{+μ} ≠ c_{-μ}` for
at least one `μ ∈ {x,y,z}`. Equivalently, some discrete neighbor contrast
`n_μ = c_{+μ} − c_{-μ}` is nonzero. This is **not** Hamming parity
`|c|_1 mod 2`.

The five remaining bits of an `F_cut` map, in the displayed order
`(wt1, opp2, adj2, vertex3, mixed3)`, are the values on the three
complement-pairs and two complement-fixed orbits after empty and full are
forced to `0`. Write `f1` for the remaining-bit tuple `(1, 1, 1, 1, 1)`.

**Theorem 1.** `f_L1 ∈ F_cut`, `f1 ∈ F_cut`, and

```text
cov4(f_L1) = 489
cov4(f1) = 495.
```

The remaining-bit tuple of `f_L1` is `(1, 0, 1, 1, 1)`. The remaining-bit
tuple of `f1` is `(1, 1, 1, 1, 1)`.

**Theorem 2.** Exhaustive enumeration of the 32 maps gives

```text
m4 = 495
N_max4 = 1.
```

So the 4-site maximum is the full seed count, attained by one map.

**Theorem 3.** So `N_max4=1`, but that unique maximizer is not `f_L1`.
The displayed maximizer is the remaining-bit tuple `(1, 1, 1, 1, 1)`,
which is `f1`, with `cov4=495`. The map `f_L1` attains `489 < 495`.
Displayed, not adopted.

Do not write the ranking into Admissibility.

Not leftover-character of #6429 (that was the 2-site ranking; different |S|).
Not leftover-character of #6453 (that was the 3-site ranking; different |S|;
`f_L1` and `f1` both attained the 3-site maximum).
Not leftover-character of #6457 (that was the joint 2+3 maximizer identity,
not this `|S|=4` ranking). This note is not a seed-table of two named maps.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The ten-orbit reconstruction, the 32-element F_cut, membership of f_L1 and f1, the exact integers cov4(f_L1)=489 and cov4(f1)=495, and the 4-site coverage-ranking pair (m4,N_max4)=(495,1) are enumerated. Uniqueness of f_L1 as an F_cut 4-site coverage maximizer is false on this patch. No physical law is selected."
trace_class: upstream_support
target_claim_id: f_cut_four_site_coverage
target_blocker_text: "whether f_L1 uniquely maximizes 4-site fill coverage among the 32 F_cut maps"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the F_cut 4-site coverage ranking; any physical use must separately derive an Admissibility selector"
conditional_surface_status: "exact for F_cut on this twelve-vertex patch with off-patch o=0 and all 495 four-site seeds; no Z^3-wide law and no physical selector"
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
- the complete set of 495 unordered 4-site seeds.

No observational comparator, literature constant, Wilson weight, rate, or
generator is imported. No Record scalar functional appears.

## Exact Target And Objects

**Target.** Rank the 32 members of `F_cut` by four-site fill coverage on
the two-cube, report `cov4(f_L1)` and `cov4(f1)`, and decide uniqueness of
`f_L1` as a 4-site maximizer.

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
`f(c)=f(1-c)`. The empty/full pair is forced to `0`. The remaining free
data are three complement-pair bits and two complement-fixed orbit bits,
so `|F_cut|=32`. The remaining-bit tuple is those five bits in the order
`(wt1, opp2, adj2, vertex3, mixed3)`.

Define

```text
f_L1(c)     = 1  iff  u(c) ≥ 1,
f1(c)       = 1  iff  c is neither empty nor full,
```

so `f_L1` has remaining-bit tuple `(1, 0, 1, 1, 1)` and `f1` has
remaining-bit tuple `(1, 1, 1, 1, 1)`. The displayed maximizer is `f1`.
Neither map is adopted.

A locked set `S` determines occupancies: a lattice neighbor in `S` has
occupancy `1`, and every other neighbor — including every off-patch
neighbor — has occupancy `0`. One synchronous tick replaces `S` by

```text
S ∪ { v in two-cube \ S : f(neighborhood_6(v; S)) = 1 }.
```

Then `cov4(f)` is the number of 4-site seeds whose halt set has cardinality
12, `m4` is the maximum of `cov4` over `F_cut`, and `N_max4` is the number
of maps attaining `m4`.

## Theorems

**Theorem 1.** There are exactly 24 proper cube rotations and exactly 10
orbits on `{0,1}^6`. The three cuts leave `|F_cut|=32`. The unbalanced-axis
map `f_L1` is one element of `F_cut`. It is not Hamming parity. The map
`f1` is the complementary remaining-bit tuple with `opp2` on. On the
twelve-vertex two-cube with off-patch occupancy `0`, exhaustive run of all
495 four-site seeds gives

```text
cov4(f_L1) = 489
cov4(f1) = 495.
```

**Theorem 2.** Exhaustive ranking of the 32 maps on all 495 four-site
seeds gives

```text
m4 = 495
N_max4 = 1.
```

The unique remaining-bit tuple that attains `m4` is

```text
(1, 1, 1, 1, 1).
```

Equivalently, a map in `F_cut` fills every 4-site seed if and only if it
is `f1`.

**Theorem 3.** So `N_max4=1`, but that map is not `f_L1`. The map `f_L1`
fills 489 of the 495 four-site seeds, so it is not a maximizer. The
displayed maximizer is the remaining-bit tuple `(1, 1, 1, 1, 1)`. It is
distinct from `f_L1` (they disagree on `opp2`) and has `cov4=495`.
Displayed, not adopted.

## Proof-Obligation Graph

| obligation | exact disposition |
|---|---|
| 24 proper cube rotations | signed permutations of the three axes with determinant `+1` |
| 10 orbits on `{0,1}^6` | axis-type classes `(u,b,e)` partition the 64 cells with the listed sizes |
| `|F_cut|=32` | three complement-pairs and two complement-fixed orbits remain free after the vanish cuts |
| `f_L1` is in `F_cut` | `u` is rotation- and complement-invariant and `u(empty)=u(full)=0` |
| `f1` is in `F_cut` | vanish on empty and full, and complement-even on every remaining orbit |
| `f_L1` is not Hamming | the two-unbalanced-axis orbit has even weight and `f_L1=1` |
| `cov4(f_L1)=489` | exhaustive 495-seed fill census of `f_L1` |
| `cov4(f1)=495` | exhaustive 495-seed fill census of `f1` |
| two-cube has twelve vertices | `{0,1,2}×{0,1}×{0,1}` |
| 495 four-site seeds | `C(12,4)` unordered 4-sets |
| off-patch occupancy `0` | declared stencil default; not a blank-block |
| `m4`, `N_max4` | exhaustive 32-map ranking of `cov4` |
| uniqueness of `f_L1` as maximizer | false; remaining-bit tuple `(1, 1, 1, 1, 1)` is the unique maximizer with `cov4=495` |

## Counterfactual And Mutation Table

1. Replace `f_L1` by Hamming parity `|c|_1 mod 2`: the maps disagree on the
   two-unbalanced-axis orbit, and Hamming is a different `F_cut` member.
2. Change the off-patch default away from `0`: the occupancy stencil
   changes and the coverage ranking is a different object.
3. Drop any of the three cuts: the class is no longer the 32-element
   `F_cut`.
4. Score only 2-site seeds: that leftover is #6429, a different `|S|`.
5. Score only 3-site seeds: that leftover is #6453, a different `|S|`.
6. Identify the unique joint 2+3 maximizer and stop: that leftover is
   #6457, not the `|S|=4` ranking.
7. Assert that `f_L1` uniquely maximizes `cov4`: the explicit remaining-bit
   tuple `(1, 1, 1, 1, 1)` with `cov4=495` and `cov4(f_L1)=489` refute
   uniqueness of `f_L1`.

## What This Does Not Claim

- No physical Admissibility selector and no adopted occupancy law.
- No Qubit rewrite and no `M_2(C)`-valued conditional probability.
- No `Z^3`-wide formation, rate, or generator.
- No identification of `f_L1` with Hamming parity.
- No leftover-character restatement of the 2-site `F_cut` ranking, the
  3-site `F_cut` ranking, or the joint 2+3 maximizer identity, in place
  of this 32-map 4-site coverage ranking.
- No list of the 495 four-site seeds, and not a seed-table of two named
  maps.
- No blank-block or 5-site variant.

## No-Go Discipline Gate

The only negative claim is uniqueness of the maximizer: `f_L1` is not the
unique `F_cut` maximizer of four-site coverage on this patch. The positive
triple `(m4, N_max4, cov4(f_L1))=(495, 1, 489)` is an exact enumeration,
not a wall.

### N1 — materially distinct routes

| Route | Exact attack | Result and authority | Marker |
|---|---|---|---|
| orbit reconstruction | Recompute the 24 rotations and the 10 axis-type orbits. | Theorem 1 and checks `thm1-twenty-four-rotations` / `thm1-ten-orbits`. | **ATTEMPTED** |
| three-cut class | Force vanish-on-empty, vanish-on-full, and `f(c)=f(1-c)`. | Theorem 1 and check `thm1-f-cut-cardinality` give `|F_cut|=32`. | **ATTEMPTED** |
| Hamming-as-`f_L1` | Test whether `|c|_1 mod 2` equals the unbalanced-axis predicate. | Theorem 1 and check `thm1-f-L1-not-hamming` separate the maps. | **ATTEMPTED** |
| `cov4` of the two named maps | Run `f_L1` and `f1` on all 495 four-site seeds. | Theorem 1 and check `thm1-cov4-L1-and-f1` give `cov4(f_L1)=489` and `cov4(f1)=495`. | **ATTEMPTED** |
| `F_cut` 4-site coverage ranking | Score every map in `F_cut` by `cov4`. | Theorem 2 and check `thm2-m4-and-n-max4` give `m4 = 495` and `N_max4 = 1`. | **ATTEMPTED** |
| uniqueness of `f_L1` as maximizer | Ask whether the maximizer class is the singleton `{f_L1}`. | Theorem 3 and checks `thm3-not-unique-l1-maximizer` / `thm3-displayed-other-maximizer`. | **ATTEMPTED** |

### N2 — wall independence and collapse

There is one negative conclusion: uniqueness of `f_L1` as maximizer fails.
The unique maximizer being `f1` and the score `cov4(f_L1)=489 < m4` are
two certificates of the same non-uniqueness of `f_L1`, so they collapse
rather than count as two walls.

| Pair | First closes second? | Second closes first? | Disposition |
|---|---:|---:|---|
| `N_max4=1` with maximizer `f1` / `cov4(f_L1)=489` | yes: the unique maximizer is not `f_L1` | yes: a strictly smaller score is non-uniqueness of `f_L1` | collapse into the uniqueness failure |
| `cov4(f1)=495` / `m4=495` | no: a score does not name the multiplicity | no: the max does not name uniqueness of `f_L1` | independent positive integers versus uniqueness |
| static `|F_cut|=32` / ranking pair `(m4, N_max4)` | no: membership is not dynamics | no: a ranking does not replace the three-cut class | separate exact counts |
| leftover of #6429 / this ranking | no: that leftover scored `|S|=2` | no: a 4-site ranking does not replace the 2-site ranking | different object |
| leftover of #6453 / this ranking | no: that leftover scored `|S|=3` | no: a 4-site ranking does not replace the 3-site ranking | different object |
| leftover of #6457 / this ranking | no: that leftover named the joint 2+3 maximizer | no: a 4-site ranking does not replace a joint-score identity | different object |

Physical law selection is not a wall: this note makes no negative theorem
about the existence of a selector and simply does not claim one.

### N3 — hidden-condition scan

| Phrase or premise | Classification |
|---|---|
| “work on the twelve-vertex two-cube” | explicit patch hypothesis; not a `Z^3` theorem |
| off-patch occupancy `0` | explicit default; blank-block is a different rule |
| `F_cut` | explicit three-cut class; the other 992 covariant maps are excluded |
| all 495 four-site seeds | explicit seed class; a 2-site or 3-site ranking is a different residual |
| “lock” | Record permanence on this Boolean occupancy model, not a possibility-valued law |
| “cube-covariant” | invariance under the 24 proper rotations, cited to Lattice/Admissibility |
| Hamming parity | displayed mutation only |
| remaining-bit tuple `(1, 1, 1, 1, 1)` | displayed witness against uniqueness of `f_L1`, not a selected law |

### N4 — citation-to-residual matching

| Evidence path:line | Residual attacked | Residual claimed closed | Match? |
|---|---|---|---:|
| `docs/MINIMAL_AXIOMS_2026-06-29.md:37` | ambient lattice and cubic rotations | sites are `Z^3` with proper cubic rotations | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:57` | covariant nearest-neighbor rule | covariance is the class filter, not a selector | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:79` | lock permanence | a locked site stays locked | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:83` | unreadability of absence | unlocked and off-patch sites contribute occupancy `0`, not a readout | yes |
| `scripts/f_cut_four_site_coverage_2026_08_15.py:76` | 24 proper rotations | signed permutations with determinant `+1` | yes |
| `scripts/f_cut_four_site_coverage_2026_08_15.py:120` | `f_L1` definition | unbalanced-axis predicate, not Hamming | yes |
| `scripts/f_cut_four_site_coverage_2026_08_15.py:125` | Hamming mutation | `|c|_1 mod 2` is a different `F_cut` map | yes |
| `scripts/f_cut_four_site_coverage_2026_08_15.py:129` | `f1` definition | remaining bits `(1, 1, 1, 1, 1)` | yes |
| `scripts/f_cut_four_site_coverage_2026_08_15.py:49` | 495 four-site seeds | `C(12,4)` unordered 4-sets on the two-cube | yes |
| `scripts/f_cut_four_site_coverage_2026_08_15.py:193` | `cov4(f)` | number of 4-site seeds a map fills | yes |
| `scripts/f_cut_four_site_coverage_2026_08_15.py:296` | ranking | exact `(m4, N_max4)` on `F_cut` | yes |
| `scripts/f_cut_four_site_coverage_2026_08_15.py:62` | uniqueness | displayed maximizer, remaining bits `(1, 1, 1, 1, 1)` | yes |

No evidence citation is used to claim that a physical occupancy law, a
formation rate, or a `Z^3`-wide selector has been closed.

### N5 — rhetoric and resolution audit

| Resolution | Executed? | Narrow negative supported? |
|---|---:|---|
| per element | yes: all 64 neighbor 6-tuples | each is assigned its axis-type orbit; no broader cell class is classified |
| per site | yes: the twelve two-cube vertices | each uses the same six-direction stencil with off-patch occupancy `0` |
| per mode | yes: every map in `F_cut` | the ranking is this class on all 495 seeds; other classes are unclaimed |
| per block | yes: the pair `(m4, N_max4)` | uniqueness of `f_L1` fails because the unique maximizer is `f1` |
| lattice wide | no | no `Z^3`-wide formation or Admissibility selector is asserted |

The runner prints the same five resolution statements.

### N6 — partial closure and primitive scan

The primitive registry at `docs/audit/data/axiom_premise_nodes.json` was
checked. The only dependency used is the registered `minimal_axioms` node.
Approved primitives are `scale_reference_primitive`,
`kinetic_isotropy_primitive`, and `realized_state_primitive`. None of them
supplies a Boolean occupancy map, a seed-coverage ranking, or an
Admissibility selector, and none is reclassified as an import or wall.

One partial-closure mechanism is displayed rather than suppressed: `f_L1`
does lie in `F_cut` and does fill 489 of the 495 four-site seeds. That
positive member does not make `f_L1` a maximizer and does not select it
as the physical rule. The remaining physical choice — which, if any,
`F_cut` map is the Admissibility occupancy predicate — stays explicit.

The open derivation-obligation registry
(`docs/audit/data/derivation_obligations.json`) names no occupancy-to-lock
coverage target; those open gates are unused here.

### N7 — hostile steelman

The strongest objection is that `f1` was already the unique joint 2+3
maximizer (#6457) and already a 3-site maximizer (#6453), so four-site
coverage might be called a leftover decoration of those two named maps,
or a seed-table that only scores `f_L1` against `f1`. That objection is
correctly about the existence of a two-map comparison at other
cardinalities. It does not overturn the stated theorem: among all 32
maps in `F_cut`, four-site coverage selects the singleton `{f1}` and
excludes `f_L1` (`489 < 495`). That is a ranking failure for uniqueness
of `f_L1` at `|S|=4`, not leftover-character of #6429, #6453, or #6457,
and not a seed-table of two named maps.

### N8 — cross-cycle echo

Repository search found nearby occupancy and covariance surfaces. They are
context, not load-bearing dependencies. The 24 rotations, 10 orbits,
`F_cut`, and 32-map 495-seed ranking are recomputed here.

| Earlier surface | Similar issue | Mechanism considered here |
|---|---|---|
| `docs/ADMISSIBILITY_COVARIANT_Q8_CONDITIONAL_LAW_PAIR_BOUNDED_THEOREM_NOTE_2026-08-13.md` | proper-cubic covariance of a local rule | covariance is used only as the orbit filter for Boolean maps |
| `docs/PHYSICAL_SPATIAL_BLOCK_SEAM_DICHOTOMY_CYCLE728_NOTE_2026-08-04.md` | two-cell box `{0,1,2}×{0,1}×{0,1}` | the same twelve spatial vertices are the patch; the seam cost is unused |
| `docs/MINIMAL_AXIOMS_2026-06-29.md` | one covariant nearest-neighbor rule | the axiom names the contract; this note does not select the rule |

No earlier mechanism retires the `F_cut` 4-site coverage ranking or
restores uniqueness of `f_L1` as a maximizer inside the 32-map class.

No-Go Discipline disposition: **PASS** for the uniqueness failure and the
exact triple `(m4, N_max4, cov4(f_L1))` stated above.

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
`F_cut`, evaluates all 32 maps on the two-cube from every 4-site seed,
reports `cov4(f_L1) = 489` and `cov4(f1) = 495`, reports `m4 = 495` and
`N_max4 = 1`, checks that `f_L1` is not Hamming parity, and exhibits the
displayed maximizer by remaining-bit tuple `(1, 1, 1, 1, 1)` with
`cov4=495`. Declared audit inputs are this note and the axiom memo.
No runner cache is written.
