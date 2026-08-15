---
claim_id: f_cut_joint_two_three_site_maximizer_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Among the 32 F_cut maps on the two-cube with off-patch o=0, N_both maps attain both cov2=66 and cov3=220. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_joint_two_three_site_maximizer_2026_08_15.py
---

# Joint Two-Site And Three-Site Maximizer Inside The Three-Cut Class `F_cut`

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact occupancy-to-lock joint-coverage census of the 32
cube-covariant complement-even predicates that vanish on empty and full,
on the twelve-vertex two-cube, over all 66 unordered 2-site seeds and all
220 unordered 3-site seeds, with off-patch occupancy `0`. The selector is
joint coverage, not leftover of either separate ranking. The displayed
joint maximizer is not adopted as the physical Admissibility rule.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_joint_two_three_site_maximizer_2026_08_15.py`](../scripts/f_cut_joint_two_three_site_maximizer_2026_08_15.py)
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
class. The two-site coverage ranking of the same 32 maps is a different
leftover inventory: it named a two-map leftover. The three-site coverage
ranking is a different leftover inventory: it named a different leftover
pair. This note asks the new ranking object: among all 32 maps, which
maps attain both maxima at once.

On the two-cube `{0,1,2}×{0,1}×{0,1}`, each unordered pair of vertices is
a 2-site seed and each unordered triple is a 3-site seed. There are
`C(12,2)=66` two-site seeds and `C(12,3)=220` three-site seeds. Off-patch
neighbors have occupancy `0`. Each tick, every unlocked on-patch vertex
evaluates `f` on its six-neighbor occupancy tuple and locks if `f=1`. The
process is synchronous and stops at a fixed point in at most 12 ticks.
Fill means `|locks_halt|=12`. Coverage is

```text
cov2(f) = |{ S : |S|=2 and f fills from S }|,
cov3(f) = |{ S : |S|=3 and f fills from S }|.
```

Do not list the seeds.

`f_L1(c)=1` if and only if some axis is unbalanced: `c_{+μ} ≠ c_{-μ}` for
at least one `μ ∈ {x,y,z}`. Equivalently, some discrete neighbor contrast
`n_μ = c_{+μ} − c_{-μ}` is nonzero. This is **not** Hamming parity
`|c|_1 mod 2`.

The five remaining bits of an `F_cut` map, in the displayed order
`(wt1, opp2, adj2, vertex3, mixed3)`, are the values on the three
complement-pairs and two complement-fixed orbits after empty and full are
forced to `0`.

**Theorem 1.** Exhaustive ranking of the 32 maps reconfirms the two-site
and three-site leftover pairs. The two maps that attain `cov2=66` have
remaining-bit tuples

```text
(1, 1, 1, 1, 0), (1, 1, 1, 1, 1).
```

The two maps that attain `cov3=220` have remaining-bit tuples

```text
(1, 0, 1, 1, 1), (1, 1, 1, 1, 1).
```

The second of those three-site maximizers is `f_L1`.

**Theorem 2.** The joint-maximizer class is

```text
N_both = |{ f in F_cut : cov2(f)=66 and cov3(f)=220 }|.
```

Enumeration gives

```text
N_both = 1
```

and the remaining-bit tuple of that one map is `(1, 1, 1, 1, 1)`.

**Theorem 3.** So `N_both=1` and that map is remaining-bit
`(1, 1, 1, 1, 1)`. Displayed, not adopted.

Do not write the ranking into Admissibility.

Not leftover of #6430 (that was the 2-site ranking; it named a two-map leftover).
Not leftover of #6453 (that was the 3-site ranking; a different leftover pair).

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The ten-orbit reconstruction, the 32-element F_cut, the exact leftover pairs cov2=66 and cov3=220, and the joint-maximizer count N_both=1 with remaining-bit tuple (1,1,1,1,1) are enumerated. The displayed joint maximizer is not adopted. No physical law is selected."
trace_class: upstream_support
target_claim_id: f_cut_joint_two_three_site_maximizer
target_blocker_text: "whether a unique F_cut map attains both the 2-site and 3-site coverage maxima"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the F_cut joint coverage selector; any physical use must separately derive an Admissibility selector"
conditional_surface_status: "exact for F_cut on this twelve-vertex patch with off-patch o=0 and all 66 two-site plus 220 three-site seeds; no Z^3-wide law and no physical selector"
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
- the complete set of 66 unordered 2-site seeds;
- the complete set of 220 unordered 3-site seeds.

No observational comparator, literature constant, Wilson weight, rate, or
generator is imported. No Record scalar functional appears.

## Exact Target And Objects

**Target.** Reconfirm the `cov2=66` pair and the `cov3=220` pair among the
32 members of `F_cut` on the two-cube, then count how many maps attain
both maxima, and display the remaining-bit tuple of every such map.

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
```

so `f_L1` has remaining-bit tuple `(1, 0, 1, 1, 1)`. The displayed joint
maximizer has remaining-bit tuple `(1, 1, 1, 1, 1)`: it equals `f_L1`
except that `opp2` is on. Neither map is adopted.

A locked set `S` determines occupancies: a lattice neighbor in `S` has
occupancy `1`, and every other neighbor — including every off-patch
neighbor — has occupancy `0`. One synchronous tick replaces `S` by

```text
S ∪ { v in two-cube \ S : f(neighborhood_6(v; S)) = 1 }.
```

Then `cov2(f)` is the number of 2-site seeds whose halt set has cardinality
12, `cov3(f)` is the same count on 3-site seeds, and `N_both` is the number
of maps in `F_cut` that attain both `cov2=66` and `cov3=220`.

## Theorems

**Theorem 1.** There are exactly 24 proper cube rotations and exactly 10
orbits on `{0,1}^6`. The three cuts leave `|F_cut|=32`. The unbalanced-axis
map `f_L1` is one element of `F_cut`. It is not Hamming parity. On the
twelve-vertex two-cube with off-patch occupancy `0`, exhaustive ranking of
all 32 maps on all 66 two-site seeds and all 220 three-site seeds gives
the leftover pairs

```text
cov2=66 : (1, 1, 1, 1, 0), (1, 1, 1, 1, 1)
cov3=220 : (1, 0, 1, 1, 1), (1, 1, 1, 1, 1).
```

The remaining-bit tuple of `f_L1` is `(1, 0, 1, 1, 1)`, so `f_L1` is one
of the two 3-site maximizers and is not a 2-site maximizer.

**Theorem 2.** The joint coverage selector is the intersection of those
two leftover pairs. Exhaustive ranking gives

```text
N_both = 1
```

and the remaining-bit tuple of that one map is

```text
(1, 1, 1, 1, 1).
```

Equivalently, a map in `F_cut` attains both `cov2=66` and `cov3=220` if
and only if its remaining-bit tuple is `(1, 1, 1, 1, 1)`.

**Theorem 3.** So `N_both=1` and that map is remaining-bit
`(1, 1, 1, 1, 1)`. It is distinct from `f_L1` (they disagree on `opp2`).
It attains `cov2=66` and `cov3=220`. Displayed, not adopted.

## Proof-Obligation Graph

| obligation | exact disposition |
|---|---|
| 24 proper cube rotations | signed permutations of the three axes with determinant `+1` |
| 10 orbits on `{0,1}^6` | axis-type classes `(u,b,e)` partition the 64 cells with the listed sizes |
| `|F_cut|=32` | three complement-pairs and two complement-fixed orbits remain free after the vanish cuts |
| `f_L1` is in `F_cut` | `u` is rotation- and complement-invariant and `u(empty)=u(full)=0` |
| `f_L1` is not Hamming | the two-unbalanced-axis orbit has even weight and `f_L1=1` |
| two `cov2=66` maps | remaining-bit tuples `(1, 1, 1, 1, 0)` and `(1, 1, 1, 1, 1)` |
| two `cov3=220` maps | remaining-bit tuples `(1, 0, 1, 1, 1)` and `(1, 1, 1, 1, 1)` |
| two-cube has twelve vertices | `{0,1,2}×{0,1}×{0,1}` |
| 66 two-site seeds | `C(12,2)` unordered pairs |
| 220 three-site seeds | `C(12,3)` unordered triples |
| off-patch occupancy `0` | declared stencil default; not a blank-block |
| `N_both` and remaining-bit tuples | exhaustive 32-map ranking of the pair `(cov2, cov3)` |
| uniqueness of the joint maximizer | `N_both=1`; remaining-bit tuple `(1, 1, 1, 1, 1)` is the displayed map |

## Counterfactual And Mutation Table

1. Replace `f_L1` by Hamming parity `|c|_1 mod 2`: the maps disagree on the
   two-unbalanced-axis orbit, and Hamming is a different `F_cut` member.
2. Change the off-patch default away from `0`: the occupancy stencil
   changes and the coverage ranking is a different object.
3. Drop any of the three cuts: the class is no longer the 32-element
   `F_cut`.
4. Score only 2-site seeds: that leftover is #6430, a different leftover
   pair.
5. Score only 3-site seeds: that leftover is #6453, a different leftover
   pair.
6. Assert that `f_L1` is the joint maximizer: `f_L1` has `cov2=62`, so it
   is not in the joint class.

## What This Does Not Claim

- No physical Admissibility selector and no adopted occupancy law.
- No Qubit rewrite and no `M_2(C)`-valued conditional probability.
- No `Z^3`-wide formation, rate, or generator.
- No identification of `f_L1` with Hamming parity.
- No leftover-character restatement of the 2-site `F_cut` ranking, and no
  leftover-character restatement of the 3-site `F_cut` ranking, in place
  of this joint coverage selector.
- No list of the 66 two-site seeds or the 220 three-site seeds.
- No blank-block or 4-site variant.

## No-Go Discipline Gate

The only negative claim is adoption: the unique joint maximizer is
displayed and is not written into Admissibility. The positive count
`N_both=1` with remaining-bit tuple `(1, 1, 1, 1, 1)` is an exact
enumeration, not a wall.

### N1 — materially distinct routes

| Route | Exact attack | Result and authority | Marker |
|---|---|---|---|
| orbit reconstruction | Recompute the 24 rotations and the 10 axis-type orbits. | Theorem 1 and checks `thm1-twenty-four-rotations` / `thm1-ten-orbits`. | **ATTEMPTED** |
| three-cut class | Force vanish-on-empty, vanish-on-full, and `f(c)=f(1-c)`. | Theorem 1 and check `thm1-f-cut-cardinality` give `|F_cut|=32`. | **ATTEMPTED** |
| Hamming-as-`f_L1` | Test whether `|c|_1 mod 2` equals the unbalanced-axis predicate. | Theorem 1 and check `thm1-f-L1-not-hamming` separate the maps. | **ATTEMPTED** |
| `cov2` pair reconfirm | Run every `F_cut` map on all 66 two-site seeds. | Theorem 1 and check `thm1-cov2-max-pair` give the two `cov2=66` tuples. | **ATTEMPTED** |
| `cov3` pair reconfirm | Run every `F_cut` map on all 220 three-site seeds. | Theorem 1 and check `thm1-cov3-max-pair` give the two `cov3=220` tuples. | **ATTEMPTED** |
| joint coverage selector | Count maps that attain both maxima. | Theorem 2 / Theorem 3 and checks `thm2-n-both` / `thm3-unique-joint-maximizer`. | **ATTEMPTED** |

### N2 — wall independence and collapse

There is one negative conclusion: the displayed joint maximizer is not
adopted. The exact count `N_both=1` and the remaining-bit tuple
`(1, 1, 1, 1, 1)` are two certificates of the same joint class, so they
collapse rather than count as two walls.

| Pair | First closes second? | Second closes first? | Disposition |
|---|---:|---:|---|
| `N_both=1` / displayed `(1, 1, 1, 1, 1)` | yes: a singleton names that tuple | yes: that tuple is the singleton | collapse into the joint class |
| leftover of #6430 / this selector | no: that leftover scored only `cov2` | no: a joint class does not replace the 2-site ranking | different object |
| leftover of #6453 / this selector | no: that leftover scored only `cov3` | no: a joint class does not replace the 3-site ranking | different object |
| static `|F_cut|=32` / `N_both` | no: membership is not dynamics | no: a joint count does not replace the three-cut class | separate exact counts |
| `f_L1` membership / joint class | no: `f_L1` attains `cov3` only | no: the joint map is not `f_L1` | different remaining-bit tuples |

Physical law selection is not a wall: this note makes no negative theorem
about the existence of a selector and simply does not claim one.

### N3 — hidden-condition scan

| Phrase or premise | Classification |
|---|---|
| “work on the twelve-vertex two-cube” | explicit patch hypothesis; not a `Z^3` theorem |
| off-patch occupancy `0` | explicit default; blank-block is a different rule |
| `F_cut` | explicit three-cut class; the other 992 covariant maps are excluded |
| all 66 two-site and 220 three-site seeds | explicit seed classes; a single ranking is a different residual |
| “lock” | Record permanence on this Boolean occupancy model, not a possibility-valued law |
| “cube-covariant” | invariance under the 24 proper rotations, cited to Lattice/Admissibility |
| Hamming parity | displayed mutation only |
| remaining-bit tuple `(1, 1, 1, 1, 1)` | displayed joint maximizer, not a selected law |

### N4 — citation-to-residual matching

| Evidence path:line | Residual attacked | Residual claimed closed | Match? |
|---|---|---|---:|
| `docs/MINIMAL_AXIOMS_2026-06-29.md:37` | ambient lattice and cubic rotations | sites are `Z^3` with proper cubic rotations | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:57` | covariant nearest-neighbor rule | covariance is the class filter, not a selector | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:79` | lock permanence | a locked site stays locked | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:83` | unreadability of absence | unlocked and off-patch sites contribute occupancy `0`, not a readout | yes |
| `scripts/f_cut_joint_two_three_site_maximizer_2026_08_15.py:81` | 24 proper rotations | signed permutations with determinant `+1` | yes |
| `scripts/f_cut_joint_two_three_site_maximizer_2026_08_15.py:125` | `f_L1` definition | unbalanced-axis predicate, not Hamming | yes |
| `scripts/f_cut_joint_two_three_site_maximizer_2026_08_15.py:130` | Hamming mutation | `|c|_1 mod 2` is a different `F_cut` map | yes |
| `scripts/f_cut_joint_two_three_site_maximizer_2026_08_15.py:52` | 66 two-site seeds | `C(12,2)` unordered pairs on the two-cube | yes |
| `scripts/f_cut_joint_two_three_site_maximizer_2026_08_15.py:55` | 220 three-site seeds | `C(12,3)` unordered triples on the two-cube | yes |
| `scripts/f_cut_joint_two_three_site_maximizer_2026_08_15.py:198` | `cov2(f)` and `cov3(f)` | number of 2-site or 3-site seeds a map fills | yes |
| `scripts/f_cut_joint_two_three_site_maximizer_2026_08_15.py:375` | joint class | exact `N_both` on `F_cut` | yes |
| `scripts/f_cut_joint_two_three_site_maximizer_2026_08_15.py:69` | displayed map | remaining bits `(1, 1, 1, 1, 1)` | yes |

No evidence citation is used to claim that a physical occupancy law, a
formation rate, or a `Z^3`-wide selector has been closed.

### N5 — rhetoric and resolution audit

| Resolution | Executed? | Narrow negative supported? |
|---|---:|---|
| per element | yes: all 64 neighbor 6-tuples | each is assigned its axis-type orbit; no broader cell class is classified |
| per site | yes: the twelve two-cube vertices | each uses the same six-direction stencil with off-patch occupancy `0` |
| per mode | yes: every map in `F_cut` | the ranking is this class on both seed cardinalities; other classes are unclaimed |
| per block | yes: the count `N_both` | the joint class is a singleton with remaining bits `(1, 1, 1, 1, 1)` |
| lattice wide | no | no `Z^3`-wide formation or Admissibility selector is asserted |

The runner prints the same five resolution statements.

### N6 — partial closure and primitive scan

The primitive registry at `docs/audit/data/axiom_premise_nodes.json` was
checked. The only dependency used is the registered `minimal_axioms` node.
Approved primitives are `scale_reference_primitive`,
`kinetic_isotropy_primitive`, and `realized_state_primitive`. None of them
supplies a Boolean occupancy map, a seed-coverage ranking, or an
Admissibility selector, and none is reclassified as an import or wall.

One partial-closure mechanism is displayed rather than suppressed: one
`F_cut` map does attain both `cov2=66` and `cov3=220`. That positive
member does not select it as the physical rule. The remaining physical
choice — which, if any, `F_cut` map is the Admissibility occupancy
predicate — stays explicit.

The open derivation-obligation registry
(`docs/audit/data/derivation_obligations.json`) names no occupancy-to-lock
coverage target; those open gates are unused here.

### N7 — hostile steelman

The strongest objection is that the intersection of two already-named
leftover pairs is leftover-character of those rankings: once the
`cov2=66` pair and the `cov3=220` pair are listed, their set-theoretic
meet is a bookkeeping remainder. That objection is correctly about the
existence of the two leftover pairs. It does not overturn the stated
theorem: among all maps in `F_cut`, the new selector is the joint class
`{f : cov2(f)=66 and cov3(f)=220}`, and that class is a singleton whose
remaining-bit tuple is `(1, 1, 1, 1, 1)`. The displayed map differs from
`f_L1` on `opp2`. Joint coverage is a new selector, not leftover of
either ranking.

### N8 — cross-cycle echo

Repository search found nearby occupancy and covariance surfaces. They are
context, not load-bearing dependencies. The 24 rotations, 10 orbits,
`F_cut`, and 32-map joint ranking are recomputed here.

| Earlier surface | Similar issue | Mechanism considered here |
|---|---|---|
| `docs/ADMISSIBILITY_COVARIANT_Q8_CONDITIONAL_LAW_PAIR_BOUNDED_THEOREM_NOTE_2026-08-13.md` | proper-cubic covariance of a local rule | covariance is used only as the orbit filter for Boolean maps |
| `docs/PHYSICAL_SPATIAL_BLOCK_SEAM_DICHOTOMY_CYCLE728_NOTE_2026-08-04.md` | two-cell box `{0,1,2}×{0,1}×{0,1}` | the same twelve spatial vertices are the patch; the seam cost is unused |
| `docs/MINIMAL_AXIOMS_2026-06-29.md` | one covariant nearest-neighbor rule | the axiom names the contract; this note does not select the rule |

No earlier mechanism retires the `F_cut` joint coverage selector or
adopts remaining-bit tuple `(1, 1, 1, 1, 1)` as a physical law.

No-Go Discipline disposition: **PASS** for the displayed-not-adopted joint
maximizer and the exact count `N_both=1` stated above.

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
`F_cut`, evaluates all 32 maps on the two-cube from every 2-site seed and
every 3-site seed, reports the `cov2=66` pair and the `cov3=220` pair,
reports `N_both = 1` with remaining-bit tuple `(1, 1, 1, 1, 1)`, checks
that `f_L1` is not Hamming parity, and exhibits the displayed joint
maximizer without adopting it. Declared audit inputs are this note and
the axiom memo. No runner cache is written.
