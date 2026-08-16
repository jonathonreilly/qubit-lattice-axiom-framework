---
claim_id: f_cut_cov8_positive_q4_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Among the 32 F_cut maps on the two-cube with off-patch o=0, whether positive 8-site coverage is equivalent to (wt1=1) or (adj2=1) is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_cov8_positive_q4_2026_08_15.py
---

# Whether `cov8>0` Is `Q4` Among The 32 `F_cut` Maps

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact occupancy-to-lock 8-site coverage of all 32 cube-covariant
complement-even maps in `F_cut`, on the twelve-vertex two-cube, over all
495 unordered 8-site seeds, with off-patch occupancy `0`. The scored
predicate is `Q4(f) := (wt1=1) or (adj2=1)`. Whether `cov8(f)>0` is
equivalent to `Q4(f)` is reported. `Q4` is displayed. It is not adopted
as the physical Admissibility rule.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_cov8_positive_q4_2026_08_15.py`](../scripts/f_cut_cov8_positive_q4_2026_08_15.py)
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

The five remaining bits, in the displayed order
`(wt1, opp2, adj2, vertex3, mixed3)`, are the values on the three
complement-pairs and two complement-fixed orbits after empty and full are
forced to `0`. Write

```text
Q4(f) := (wt1=1) or (adj2=1).
```

Investment #6518 asked the same predicate at seed size `k=4`. Dual `k=8`
is unique-max together with `k=4,6` (#6465). Not leftover-character of #6518:
that was cov4>0 iff Q4. New `|S|`. Not leftover-character of #6465: that
named the unique maximizer at those three sizes. The present object is
whether positive 8-site coverage is the same cut as `Q4`.

On the two-cube `{0,1,2}×{0,1}×{0,1}`, each unordered 8-set of vertices is
an 8-site seed. There are `C(12,8)=495` such seeds. Off-patch neighbors
have occupancy `0`. Each tick, every unlocked on-patch vertex evaluates
`f` on its six-neighbor occupancy tuple and locks if `f=1`. The process
is synchronous and stops at a fixed point in at most 12 ticks. Fill means
`|locks_halt|=12`. Coverage is

```text
cov8(f) = |{ S : |S|=8 and f fills from S }|.
```

Do not list the seeds.

`f_L1(c)=1` if and only if some axis is unbalanced: `c_{+μ} ≠ c_{-μ}` for
at least one `μ ∈ {x,y,z}`. Equivalently, some discrete neighbor contrast
`n_μ = c_{+μ} − c_{-μ}` is nonzero. This is **not** Hamming parity
`|c|_1 mod 2`. The remaining-bit tuple of `f_L1` is `(1, 0, 1, 1, 1)`.
That map is a control: it has `Q4=1` and `cov8>0`, so it is not a
counterexample.

**Theorem 1.** Among the 32 maps, cov8(f)>0 iff Q4(f) fails. The
lex-first counterexample remaining-bit tuple `(0, 0, 0, 1, 0)`
has

```text
Q4 = 0
cov8 = 44
```

so `cov8>0` holds while `Q4` fails. Remaining-bit order is
`(wt1, opp2, adj2, vertex3, mixed3)`.

**Theorem 2.** The three census counts are

```text
N_Q4 = 24
N_pos = 30
N_both = 24
```

Every `Q4` map has positive 8-site coverage. Six `Q4`-false maps still
fill at least one 8-site seed.

**Theorem 3.** The failed equivalence, the lex-first counterexample, and
the triple `(N_Q4, N_pos, N_both)` are displayed. Do not adopt Q4.

Do not write Q4 into Admissibility.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The ten-orbit reconstruction, the 32-element F_cut, the predicate Q4=(wt1=1) or (adj2=1), and the exact census of cov8>0 versus Q4 are enumerated. The iff fails. The lex-first counterexample is remaining bits (0,0,0,1,0) with cov8=44. No physical law is selected."
trace_class: upstream_support
target_claim_id: f_cut_cov8_positive_q4
target_blocker_text: "whether cov8>0 is the same cut as Q4=(wt1=1) or (adj2=1)"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the cov8>0 versus Q4 census; any physical use must separately derive an Admissibility selector"
conditional_surface_status: "exact for all 32 F_cut maps on this twelve-vertex patch with off-patch o=0 and all 495 eight-site seeds; no Z^3-wide law and no physical selector"
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
- the complete set of 495 unordered 8-site seeds;
- the remaining-bit predicate `Q4(f) := (wt1=1) or (adj2=1)`.

No observational comparator, literature constant, Wilson weight, rate, or
generator is imported. No Record scalar functional appears.

## Exact Target And Objects

**Target.** Decide whether `cov8(f)>0` if and only if `Q4(f)`, among the
32 members of `F_cut` on the two-cube. If the iff fails, name one lex-first
counterexample. Report `N_Q4`, `N_pos`, and `N_both`. Display. Do not
adopt Q4.

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
Q4(f)      = 1  iff  the remaining bit wt1 is 1 or the remaining bit adj2 is 1,
f_L1(c)    = 1  iff  u(c) ≥ 1.
```

So `f_L1` has remaining bits `(1, 0, 1, 1, 1)` and therefore `Q4(f_L1)=1`.
Neither `Q4` nor `f_L1` is adopted.

A locked set `S` determines occupancies: a lattice neighbor in `S` has
occupancy `1`, and every other neighbor — including every off-patch
neighbor — has occupancy `0`. One synchronous tick replaces `S` by

```text
S ∪ { v in two-cube \ S : f(neighborhood_6(v; S)) = 1 }.
```

Then `cov8(f)` is the number of 8-site seeds whose halt set has cardinality
12. Write `N_Q4` for the number of maps with `Q4=1`, `N_pos` for the
number with `cov8>0`, and `N_both` for the number with both. Lex order on
counterexamples is lexicographic order of remaining-bit tuples.

## Theorems

**Theorem 1.** There are exactly 24 proper cube rotations and exactly 10
orbits on `{0,1}^6`. The three cuts leave `|F_cut|=32`. The unbalanced-axis
map `f_L1` is one element of `F_cut` and is not Hamming parity. On the
twelve-vertex two-cube with off-patch occupancy `0`, exhaustive evaluation
of all 32 maps on all 495 eight-site seeds shows that `cov8(f)>0` is not
equivalent to `Q4(f)`. The lex-first counterexample remaining-bit tuple is
`(0, 0, 0, 1, 0)`: that map has `wt1=0` and `adj2=0`, so `Q4=0`, but it
fills 44 of the 495 seeds, so `cov8 = 44`.

**Theorem 2.** The census on the same 32 maps is

```text
N_Q4 = 24
N_pos = 30
N_both = 24.
```

The inclusion `Q4 ⇒ (cov8>0)` holds. The converse fails on six maps.

**Theorem 3.** The failed iff, the lex-first remaining-bit tuple
`(0, 0, 0, 1, 0)`, and the triple `(24, 30, 24)` are displayed. Do not
adopt Q4 as the physical Admissibility rule.

## Proof-Obligation Graph

| obligation | exact disposition |
|---|---|
| 24 proper cube rotations | signed permutations of the three axes with determinant `+1` |
| 10 orbits on `{0,1}^6` | axis-type classes `(u,b,e)` partition the 64 cells with the listed sizes |
| `|F_cut|=32` | three complement-pairs and two complement-fixed orbits remain free after empty/full are forced to `0` |
| `Q4` | remaining-bit predicate `(wt1=1) or (adj2=1)` |
| 495 eight-site seeds | `C(12,8)` unordered 8-sets on the two-cube |
| `f_L1` is not Hamming | unbalanced-axis predicate disagrees with `|c|_1 mod 2` and has remaining bits `(1, 0, 1, 1, 1)` |
| `cov8>0` iff `Q4` | fails; lex-first counterexample `(0, 0, 0, 1, 0)` has `Q4=0` and `cov8=44` |
| counts | `N_Q4=24`, `N_pos=30`, `N_both=24` |
| displayed predicate | `Q4`, not adopted |

## What This Does Not Claim

- No physical Admissibility selector.
- No `Z^3`-wide formation law.
- No unique-max ranking at `k=8`.
- No reopening of the `k=4` `#6518` census.
- No blank-block or other seed-size variant.

## No-Go Discipline Gate

The only negative claim is the failed equivalence: `cov8>0` is not the
same cut as `Q4` on this 32-map class. The three counts and the lex-first
counterexample are exact enumerations, not a wall against a later selector.

### N1 — materially distinct routes

| Route | Exact attack | Result and authority | Marker |
|---|---|---|---|
| orbit reconstruction | Recompute the 24 rotations and the 10 axis-type orbits. | Theorem 1 and checks `thm1-twenty-four-rotations` / `thm1-ten-orbits`. | **ATTEMPTED** |
| three-cut class | Force vanish-on-empty, vanish-on-full, and `f(c)=f(1-c)`. | Theorem 1 and check `thm1-f-cut-cardinality` give `|F_cut|=32`. | **ATTEMPTED** |
| Hamming-as-`f_L1` | Test whether `|c|_1 mod 2` equals the unbalanced-axis predicate. | Theorem 1 and check `thm1-f-L1-not-hamming` separate the maps. | **ATTEMPTED** |
| `cov8>0` iff `Q4` | Score every one of the 32 maps by `cov8` and by `Q4`. | Theorem 1 and check `thm1-not-equivalent` give a lex-first counterexample. | **ATTEMPTED** |
| three counts | Count `N_Q4`, `N_pos`, and `N_both`. | Theorem 2 and check `thm2-counts`. | **ATTEMPTED** |
| adopt `Q4` | Write `Q4` into Admissibility. | Theorem 3 and check `thm3-displayed-not-adopted`. | **ATTEMPTED** |

### N2 — wall independence and collapse

There is one negative conclusion: `cov8>0` is not equivalent to `Q4`. The
six `Q4`-false maps with `cov8>0` are six certificates of the same failed
converse, so they collapse rather than count as six walls.

| Pair | First closes second? | Second closes first? | Disposition |
|---|---:|---:|---|
| failed iff / lex-first `(0,0,0,1,0)` | no: failure does not name the first remaining-bit witness | yes: one counterexample closes the iff | witness versus the universal claim |
| `N_Q4=24` / `N_pos=30` | no: twenty-four Q4 maps do not name thirty positive maps | no: thirty positive maps do not name which twenty-four are Q4 | independent counts |
| `#6518` `cov4` iff / this `cov8` iff | no: a 4-site cut is not 8-site dynamics | no: an 8-site cut does not replace the 4-site census | different `|S|` |
| `#6465` unique-max / this positive cut | no: uniqueness of a maximizer is not `cov8>0` | no: a positive-coverage test does not name the unique maximizer | different ranking object |

Physical law selection is not a wall: this note makes no negative theorem
about the existence of a selector and simply does not claim one.

### N3 — hidden-condition scan

| Phrase or premise | Classification |
|---|---|
| “work on the twelve-vertex two-cube” | explicit patch hypothesis; not a `Z^3` theorem |
| off-patch occupancy `0` | explicit default; blank-block is a different rule |
| `F_cut` | explicit three-cut class; the other 992 covariant maps are excluded |
| remaining-bit order `(wt1, opp2, adj2, vertex3, mixed3)` | explicit coordinate system for `Q4` and lex order |
| all 495 eight-site seeds | explicit seed class; a 4-site ranking is a different residual |
| “lock” | Record permanence on this Boolean occupancy model, not a possibility-valued law |
| “cube-covariant” | invariance under the 24 proper rotations, cited to Lattice/Admissibility |
| Hamming parity | displayed mutation only |
| remaining-bit tuple `(0, 0, 0, 1, 0)` | displayed witness, not a selected law |

### N4 — citation-to-residual matching

| Evidence path:line | Residual attacked | Residual claimed closed | Match? |
|---|---|---|---:|
| `docs/MINIMAL_AXIOMS_2026-06-29.md:37` | ambient lattice and cubic rotations | sites are `Z^3` with proper cubic rotations | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:57` | covariant nearest-neighbor rule | covariance is the class filter, not a selector | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:79` | lock permanence | a locked site stays locked | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:83` | unreadability of absence | unlocked and off-patch sites contribute occupancy `0`, not a readout | yes |
| `scripts/f_cut_cov8_positive_q4_2026_08_15.py:79` | 24 proper rotations | signed permutations with determinant `+1` | yes |
| `scripts/f_cut_cov8_positive_q4_2026_08_15.py:123` | `f_L1` definition | unbalanced-axis predicate, not Hamming | yes |
| `scripts/f_cut_cov8_positive_q4_2026_08_15.py:128` | Hamming mutation | `|c|_1 mod 2` is a different map | yes |
| `scripts/f_cut_cov8_positive_q4_2026_08_15.py:50` | 495 eight-site seeds | `C(12,8)` unordered 8-sets on the two-cube | yes |
| `scripts/f_cut_cov8_positive_q4_2026_08_15.py:132` | `Q4` | `(wt1=1) or (adj2=1)` on remaining bits | yes |
| `scripts/f_cut_cov8_positive_q4_2026_08_15.py:63` | lex-first counterexample | remaining bits `(0, 0, 0, 1, 0)` | yes |
| `scripts/f_cut_cov8_positive_q4_2026_08_15.py:193` | `cov8(f)` | number of 8-site seeds a map fills | yes |
| `scripts/f_cut_cov8_positive_q4_2026_08_15.py:53` | `N8_SEEDS=495` | seed-count ceiling | yes |

No evidence citation is used to claim that a physical occupancy law, a
formation rate, or a `Z^3`-wide selector has been closed.

### N5 — rhetoric and resolution audit

| Resolution | Executed? | Narrow negative supported? |
|---|---:|---|
| per element | yes: all 64 neighbor 6-tuples | each is assigned its axis-type orbit; no broader cell class is classified |
| per site | yes: the twelve two-cube vertices | each uses the same six-direction stencil with off-patch occupancy `0` |
| per mode | yes: all 32 `F_cut` maps | the score is `cov8>0` versus `Q4` on this class |
| per block | yes: the failed iff and the triple `(24, 30, 24)` | `Q4` does not cut positive 8-site coverage |
| lattice wide | no | no `Z^3`-wide formation or Admissibility selector is asserted |

The runner prints the same five resolution statements.

### N6 — partial closure and primitive scan

The primitive registry at `docs/audit/data/axiom_premise_nodes.json` was
checked. The only dependency used is the registered `minimal_axioms` node.
Approved primitives are `scale_reference_primitive`,
`kinetic_isotropy_primitive`, and `realized_state_primitive`. None of them
supplies a Boolean occupancy map, a seed-coverage ranking, or an
Admissibility selector, and none is reclassified as an import or wall.

One partial-closure mechanism is displayed rather than suppressed: every
`Q4` map does have `cov8>0`, so the forward implication holds. That
inclusion does not restore the converse and does not select `Q4` as the
physical rule. The remaining physical choice — which, if any, `F_cut` map
is the Admissibility occupancy predicate — stays explicit.

The open derivation-obligation registry
(`docs/audit/data/derivation_obligations.json`) names no occupancy-to-lock
coverage target; those open gates are unused here.

### N7 — hostile steelman

The strongest objection is that `#6518` already tested `Q4` against
positive coverage, so an 8-site score might be called leftover decoration
of that cut, or that `#6465` already knew `k=8` is a unique-max size, so
the census might be called leftover ranking of that maximizer. Those
objections are correctly about `cov4>0` and about uniqueness of a
maximizer. They do not overturn the stated theorem: on the 495 eight-site
seeds, `Q4` still fails to cut `cov8>0`, and the lex-first witness is the
vertex3-only remaining-bit tuple `(0, 0, 0, 1, 0)`. A 4-site cut does not
name the 8-site cut. This is a new `|S|`.

### N8 — cross-cycle echo

Repository search found nearby occupancy and covariance surfaces. They are
context, not load-bearing dependencies. The 24 rotations, 10 orbits,
`F_cut`, `Q4`, and the 495-seed scores are recomputed here.

| Earlier surface | Similar issue | Mechanism considered here |
|---|---|---|
| `docs/ADMISSIBILITY_COVARIANT_Q8_CONDITIONAL_LAW_PAIR_BOUNDED_THEOREM_NOTE_2026-08-13.md` | proper-cubic covariance of a local rule | covariance is used only as the orbit filter for Boolean maps |
| `docs/PHYSICAL_SPATIAL_BLOCK_SEAM_DICHOTOMY_CYCLE728_NOTE_2026-08-04.md` | two-cell box `{0,1,2}×{0,1}×{0,1}` | the same twelve spatial vertices are the patch; the seam cost is unused |
| `docs/MINIMAL_AXIOMS_2026-06-29.md` | one covariant nearest-neighbor rule | the axiom names the contract; this note does not select the rule |

No earlier mechanism retires the `cov8>0` versus `Q4` census or restores
the failed iff.

No-Go Discipline disposition: **PASS** for the failed equivalence
`cov8(f)>0` iff `Q4(f)` and the exact triple `(N_Q4, N_pos, N_both)`
stated above.

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
`F_cut`, evaluates every remaining-bit map on the two-cube from every
8-site seed, reports that `cov8(f)>0` is not equivalent to `Q4(f)`, names
the lex-first counterexample remaining-bit tuple `(0, 0, 0, 1, 0)` with
`cov8 = 44`, reports `N_Q4 = 24`, `N_pos = 30`, and `N_both = 24`, checks
that `f_L1` is not Hamming parity, and exhibits `Q4` as displayed, not
adopted. Declared audit inputs are this note and the axiom memo. No runner
cache is written.
