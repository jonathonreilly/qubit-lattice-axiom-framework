---
claim_id: f_cut_q8_mixed3_cov8_freedom_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Among the 30 Q8-true F_cut maps on the two-cube with off-patch o=0, whether mixed3-pairs have equal cov8 is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_q8_mixed3_cov8_freedom_2026_08_15.py
---

# Mixed3 Is Not Free For Integer Cov8 Inside Q8

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact 8-site occupancy-to-lock coverage of the 30 Q8-true
cube-covariant complement-even maps in `F_cut`, on the twelve-vertex
two-cube, with off-patch occupancy `0`. Those 30 maps form 15 pairs that
differ only by the remaining bit `mixed3`. Whether those pairs have equal
`cov8` is reported. `mixed3` is displayed, not adopted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_q8_mixed3_cov8_freedom_2026_08_15.py`](../scripts/f_cut_q8_mixed3_cov8_freedom_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result up front

Investment #6539: the remaining-bit predicate
`Q8 = wt1 ∨ opp2 ∨ adj2 ∨ vertex3` equals `cov8>0` on the 32-element class
`F_cut`. That predicate ignores `mixed3`. The two maps with `cov8=0` are
the Q8-false mixed3-pair `(0, 0, 0, 0, 0)` and `(0, 0, 0, 0, 1)`. This
note asks the integer residual inside the 30 Q8-true maps: of the 15 pairs
that differ only by `mixed3`, how many have equal `cov8`.

Not leftover-character of #6539: that was a positivity selector. The
present object is the integer `cov8` of each Q8-true mixed3-pair.

`F_cut` is the cube-covariant class of `{0,1}`-valued maps on the six
nearest-neighbor occupancy bits with `f(empty)=f(full)=0` and `f(c)=f(1-c)`.
It has five free remaining bits and size 32. Remaining bits are ordered as
`(wt1, opp2, adj2, vertex3, mixed3)`.

`f_L1(c)=1` if and only if some axis is unbalanced: the signed pair
`n_μ = c_{+μ} − c_{-μ}` is nonzero. This is **not** Hamming parity
`|c|_1 mod 2`. The remaining-bit tuple of `f_L1` is `(1, 0, 1, 1, 1)`.

On the two-cube `{0,1,2}×{0,1}×{0,1}`, each unordered 8-subset of vertices
is an 8-site seed. There are `C(12,8)=495` such seeds. Off-patch neighbors
have occupancy `0`. Each tick, every unlocked on-patch vertex evaluates
`f` on its six-neighbor occupancy tuple and locks if `f=1`. Fill means
the halt set has cardinality 12. Coverage is

```text
cov8(f) = |{ S : |S|=8 and f fills from S }|.
```

A blank-block is a different rule and is not used.

Independent coverage of all 32 maps, then restriction to the 30 Q8-true
maps as 15 mixed3-pairs:

- Theorem 1. Exactly one of those 15 pairs has equal `cov8`.
  `N_equal = 1` and `N_diff = 14`. The equal pair is
  `(0, 1, 0, 0, 0)` and `(0, 1, 0, 0, 1)`, both with `cov8 = 1`.
- Theorem 2. The lex-first pair that differs is
  `(0, 0, 0, 1, 0)` versus `(0, 0, 0, 1, 1)`, with
  `cov8((0, 0, 0, 1, 0)) = 44` and
  `cov8((0, 0, 0, 1, 1)) = 132`.
- Theorem 3. The equality count and the differing pair are displayed.
  Do not adopt mixed3.

Q8-positivity is free of `mixed3`. Integer `cov8` inside Q8 is not.
Displayed, not adopted.

Do not write mixed3 into Admissibility. Displayed, not adopted.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Independent 8-site coverage of the 30 Q8-true F_cut maps, grouped as 15 mixed3-pairs, yields an exact equality count and a named lex-first differing pair. mixed3 is displayed, not adopted."
trace_class: frontier_discovery
target_claim_id: f_cut_q8_mixed3_cov8_freedom
target_blocker_text: "among Q8-true maps, whether mixed3-pairs have equal cov8"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the mixed3-pair cov8 equality count; do not adopt mixed3"
conditional_surface_status: "exact for occupancy-to-lock on the twelve-vertex two-cube with off-patch occupancy 0; no Z^3-wide formation law"
hypothetical_axiom_status: "not proposed; no axiom or approved primitive is added"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Premises and declared mathematical objects

The only scientific dependency is the current four-axiom authority linked
above. Lattice supplies `Z^3` with nearest-neighbor adjacency and proper cubic
rotations. Admissibility supplies one fixed nearest-neighbor rule, covariant
under those motions. Record is not used as a formation-site selector: the
dynamics here are a declared occupancy-to-lock predicate on a finite patch.

The following are declared mathematical scaffolding, not measured or fitted
physics inputs:

- the two-cube `T = {0,1,2} × {0,1} × {0,1}` (twelve vertices of two unit
  cubes sharing the face `x=1`);
- the complete set of 495 unordered 8-site seeds;
- off-patch occupancy `0` (a neighbor of a site in `T` that is not itself in
  `T` is treated as unoccupied; a blank-block is a different rule);
- the six-direction stencil `{±e_x, ±e_y, ±e_z}` at every site;
- the 24 proper cube rotations;
- the ten axis-type orbits of `{0,1}^6` under those rotations;
- the class `F_cut` of cube-covariant maps with `f(empty)=f(full)=0` and
  complement symmetry `f(c)=f(1-c)`;
- the remaining-bit predicate
  `Q8 = wt1 ∨ opp2 ∨ adj2 ∨ vertex3`.

No observational comparator, literature constant, rate, or generator is
imported. Hamming parity is a contrast map only; it is not `f_L1`.

## Exact target and objects

**Target.** Among the 30 Q8-true `F_cut` maps on the two-cube with
off-patch occupancy `0`, report how many of the 15 mixed3-pairs have
equal `cov8`. If not all, name the lex-first pair that differs and both
`cov8` values. Display the count. Do not adopt `mixed3`.

A configuration `c ∈ {0,1}^6` is a six-tuple of neighbor occupancies in
direction order `(+x,-x,+y,-y,+z,-z)`. Axis type is
`(n_unbalanced, n_both, n_empty)`, where an axis is unbalanced if its two
bits differ, both if both bits are 1, and empty if both bits are 0. Complement
swaps `n_both` with `n_empty`. The five remaining bits of `F_cut`, in the
order `(wt1, opp2, adj2, vertex3, mixed3)`, are the values on orbit types
`(1,0,2)`, `(0,1,2)`, `(2,0,1)`, `(3,0,0)`, `(1,1,1)`. Complement partners
are forced equal; empty and full are fixed at 0.

`Q8` is true exactly when at least one of `wt1`, `opp2`, `adj2`, `vertex3`
is 1. It does not read `mixed3`. The two Q8-false maps are
`(0, 0, 0, 0, 0)` and `(0, 0, 0, 0, 1)`. The other 30 maps form 15 pairs
that share the first four remaining bits and differ only in `mixed3`.
Pairs are ordered by that four-bit prefix in lex order.

Occupancy-to-lock: from a locked set `L ⊂ T`, a site `x ∈ T \ L` locks at
the next tick if and only if `f` of its six-neighbor occupancy (off-patch
entries 0) equals 1. The map `f` fills from a seed if iterating this rule
from the seed reaches `L = T` in at most 13 ticks. Runs of distinct maps
are independent.

## Theorems

### Theorem 1 — one of the fifteen Q8-true mixed3-pairs has equal `cov8`

There are exactly 24 proper cube rotations and exactly 10 orbits on
`{0,1}^6`. The three cuts leave `|F_cut|=32`. The unbalanced-axis map
`f_L1` is one element of `F_cut` and is not Hamming parity. Its remaining
bits are `(1, 0, 1, 1, 1)`, so it is Q8-true.

`Q8` holds on exactly 30 of the 32 maps. Those 30 maps are 15 pairs
differing only by `mixed3`. Exhaustive `cov8` on all 495 eight-site seeds
gives `N_equal = 1` and `N_diff = 14`.

The one equal pair is the `opp2`-only pair

```text
(0, 1, 0, 0, 0)  cov8 = 1
(0, 1, 0, 0, 1)  cov8 = 1
```

The two Q8-false maps both have `cov8 = 0`. That pair is outside the
scored class.

### Theorem 2 — lex-first unequal pair

The 15 prefixes in lex order begin at `(0, 0, 0, 1)`. That first pair
already differs:

```text
cov8((0, 0, 0, 1, 0)) = 44
cov8((0, 0, 0, 1, 1)) = 132
```

So the lex-first pair that differs is the `vertex3`-only pair
`(0, 0, 0, 1, 0)` versus `(0, 0, 0, 1, 1)`.

### Theorem 3 — display; do not adopt mixed3

The equality count `N_equal = 1` and the lex-first differing pair with
coverages `44` and `132` are displayed. Mixed3-freedom of Q8 as a
positivity selector does not extend to freedom of the integer `cov8`
inside Q8.

Do not adopt mixed3. Do not write mixed3 into Admissibility. `f_L1`
remains the unbalanced-axis predicate `n≠0` rather than Hamming parity.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice and Admissibility premises | quoted; no edit |
| `F_cut` remaining-bit order | enumerated |
| `Q8 = wt1 ∨ opp2 ∨ adj2 ∨ vertex3` | defined; ignores `mixed3` |
| `f_L1` as unbalanced-axis / `n_μ ≠ 0` | defined; Hamming rejected |
| two-cube, 495 eight-site seeds, off-patch 0 | declared finite patch |
| 30 Q8-true maps as 15 mixed3-pairs | enumerated |
| `N_equal = 1`, `N_diff = 14` | proved by coverage |
| lex-first differing pair and both `cov8` | `(0, 0, 0, 1, 0)` / `44` and `(0, 0, 0, 1, 1)` / `132` |
| leftover-character of #6539 | refused; positivity is not the integer |
| physical Admissibility selector | open |

## Current premise boundary

The Lattice and Admissibility premises are quoted from
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md):

Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
adjacency, standard translations, and proper cubic rotations about each site.

There is one fixed nearest-neighbor admissibility rule, covariant under lattice
translations and proper cubic rotations.

For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.

Admissibility identifies the six-neighbor condition domain and covariance
under proper cubic rotations; it does not supply the formation site, probability, or rate.
The boolean occupancy predicates and the lock-update rule are explicit
bounded mathematical input, not axiom text.

The current Record boundary is:

Records form.

When present, a record locks exactly one admissible local possibility.

A readout value is determined by record content alone.

A site with no record cannot be read.

Permanence of a lock once formed is used only as the declared update rule on
this finite patch. No physical readout, content map, or formation rate is
identified.

## Boundary and imports

Not leftover-character of #6539: that displayed Q8 as a positivity selector
equal to `cov8>0` and therefore independent of `mixed3`. The present object
is whether each Q8-true mixed3-pair has the same integer cov8.

Off-patch occupancy `0` is an explicit default on this patch. A blank-block
is a different rule and is not used.

No `Z^3`-wide formation law is claimed. Do not write mixed3 into
Admissibility.

## Promotion value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers how many of the 15 Q8-true mixed3-pairs have equal `cov8`. |
| V2 | Current main has the positivity fact #6539 (`Q8` iff `cov8>0`, ignoring `mixed3`), but no landed integer-`cov8` mixed3-freedom test inside Q8. |
| V3 | The 30 maps, 495 seeds, and occupancy-to-lock evolution are independently finite and exact. |
| V4 | The theorem is more than a restatement of Admissibility: Q8-positivity freedom of `mixed3` is not integer-`cov8` freedom. |
| V5 | It is not a physical selector: the equality count is displayed, and `mixed3` is not adopted. |

## No-Go Discipline gate

The negative content is narrow: on this patch, integer `cov8` is not
constant on Q8-true mixed3-pairs. No global compiler impossibility is
claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| Hamming parity | identify `f_L1` with `|c|_1 mod 2` | **ATTEMPTED** |
| leftover #6539 | treat integer-`cov8` equality as leftover-character of the positivity selector | **ATTEMPTED** |
| Q8-false pair | treat the scored class as the two `cov8=0` maps | **ATTEMPTED** |
| all pairs equal | claim mixed3 is free for integer `cov8` inside Q8 | **ATTEMPTED** |
| adopt `mixed3` | write the bit into Admissibility | **ATTEMPTED** |
| lattice-wide formation | lift the patch coverages to a `Z^3` formation law | **ATTEMPTED** |

### N2 — wall independence

The Hamming contrast, the leftover-#6539 extra, and the off-patch
convention are distinct. This note claims no complete wall collection.

### N3 — hidden-condition scan

The two-cube, the 495 eight-site seeds, off-patch occupancy `0`,
occupancy-to-lock ticks, the `F_cut` remaining-bit order, and the
predicate `Q8` are declared. Equality of mixed3-pair `cov8` values is
not silently assumed.

### N4 — source residual matching

The live axiom memo supplies `Z^3`, proper cubic rotations, and one covariant
nearest-neighbor rule. The residual answered here is integer-`cov8`
mixed3-freedom inside Q8, not leftover-character of #6539.

| Evidence path:line | Residual attacked | Residual claimed closed | Match? |
|---|---|---|---:|
| `docs/MINIMAL_AXIOMS_2026-06-29.md:37` | ambient lattice and cubic rotations | sites are `Z^3` with proper cubic rotations | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:57` | covariant nearest-neighbor rule | covariance is the class filter, not a selector | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:79` | lock permanence | a locked site stays locked | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:83` | unreadability of absence | unlocked and off-patch sites contribute occupancy `0`, not a readout | yes |
| `scripts/f_cut_q8_mixed3_cov8_freedom_2026_08_15.py:87` | 24 proper rotations | signed permutations with determinant `+1` | yes |
| `scripts/f_cut_q8_mixed3_cov8_freedom_2026_08_15.py:131` | `f_L1` definition | unbalanced-axis predicate, not Hamming | yes |
| `scripts/f_cut_q8_mixed3_cov8_freedom_2026_08_15.py:136` | Hamming mutation | `|c|_1 mod 2` is a different map | yes |
| `scripts/f_cut_q8_mixed3_cov8_freedom_2026_08_15.py:150` | `Q8` predicate | `wt1 ∨ opp2 ∨ adj2 ∨ vertex3`; ignores `mixed3` | yes |
| `scripts/f_cut_q8_mixed3_cov8_freedom_2026_08_15.py:52` | 495 eight-site seeds | `C(12,8)` unordered 8-subsets on the two-cube | yes |
| `scripts/f_cut_q8_mixed3_cov8_freedom_2026_08_15.py:181` | `cov8(f)` | number of 8-site seeds a map fills | yes |

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | 64 neighbor 6-tuples by axis-type orbit | no continuum occupancy |
| per site | twelve two-cube vertices, same stencil | no privileged site |
| per mode | all 30 Q8-true maps on all 495 eight-site seeds | no physical law selection |
| per block | mixed3-pair `cov8` equality count on this patch | no Admissibility write-in |
| lattice wide | checked and not executed | no `Z^3`-wide formation law |

The runner prints the same five resolution statements.

### N6 — live partial-closure paths

The primitive registry at `docs/audit/data/axiom_premise_nodes.json` was
checked. The only dependency used is the registered `minimal_axioms` node.
None of the approved primitives supplies a Boolean occupancy map, a
seed-coverage ranking, or an Admissibility selector.

Live routes include a different seed cardinality, a different off-patch
rule, a selector other than this equality count, and any independently
derived physical map from `F_cut` into Admissibility. One partial-closure
mechanism is displayed rather than suppressed: the `opp2`-only pair is
the unique Q8-true mixed3-pair with equal `cov8`. That pair does not
select `mixed3` or `opp2`.

### N7 — hostile steelman

**Steelman:** Because Q8 ignores `mixed3` and equals `cov8>0`, mixed3 is
dynamically free on every Q8-true pair, so the two maps in each pair must
fill the same number of 8-site seeds.

**Answer:** Positivity of `cov8` is not the integer `cov8`. Fourteen of
the fifteen Q8-true mixed3-pairs have unequal coverage. The lex-first
counterexample is `(0, 0, 0, 1, 0)` with `cov8 = 44` versus
`(0, 0, 0, 1, 1)` with `cov8 = 132`. That is a new uniqueness inside Q8,
not leftover-character of the positivity selector.

### N8 — cross-cycle echo

Investment #6539 already displayed that Q8 equals `cov8>0` and therefore
ignores `mixed3`. Echoing that positivity fact is not a substitute for
the 15-pair integer comparison.

| Earlier surface | Similar issue | Mechanism considered here |
|---|---|---|
| `docs/ADMISSIBILITY_COVARIANT_Q8_CONDITIONAL_LAW_PAIR_BOUNDED_THEOREM_NOTE_2026-08-13.md` | proper-cubic covariance of a local rule | covariance is used only as the orbit filter for Boolean maps; that note's quaternion-axis pair is unused |
| `docs/PHYSICAL_SPATIAL_BLOCK_SEAM_DICHOTOMY_CYCLE728_NOTE_2026-08-04.md` | two-cell box `{0,1,2}×{0,1}×{0,1}` | the same twelve spatial vertices are the patch; the seam cost is unused |
| `docs/MINIMAL_AXIOMS_2026-06-29.md` | one covariant nearest-neighbor rule | the axiom names the contract; this note does not select the rule |

No-Go Discipline disposition: **PASS** for the finite equality count and
the displayed lex-first differing pair. FAIL / DO NOT SHIP for
“`mixed3` is free for integer `cov8` inside Q8” or “`mixed3` is the
physical rule.”

## Live parent quotes

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

> There is one fixed nearest-neighbor admissibility rule, covariant under lattice
> translations and proper cubic rotations.

> A site with no record cannot be read.

## Runner contract

The companion runner reconstructs the 24 rotations and 10 orbits, rebuilds
`F_cut`, evaluates `cov8` of all 32 maps, restricts to the 30 Q8-true maps
as 15 mixed3-pairs, reports `N_equal = 1` and `N_diff = 14`, names the
lex-first differing pair `(0, 0, 0, 1, 0)` / `(0, 0, 0, 1, 1)` with
coverages `44` and `132`, checks that `f_L1` is not Hamming parity, and
exhibits the equality count as displayed, not adopted. Declared audit
inputs are this note and the axiom memo; the runner writes no cache and
authors no audit verdict.
