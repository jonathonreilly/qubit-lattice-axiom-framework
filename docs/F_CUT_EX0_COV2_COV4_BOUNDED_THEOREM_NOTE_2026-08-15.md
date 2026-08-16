---
claim_id: f_cut_ex0_cov2_cov4_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On the two-cube with off-patch o=0, the 2-site and 4-site coverage of F_cut (0,0,1,1,0) are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_ex0_cov2_cov4_2026_08_15.py
---

# Two-Site And Four-Site Fill Coverage Of `F_cut` `(0,0,1,1,0)`

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact occupancy-to-lock coverage of one cube-covariant
complement-even predicate that vanishes on empty and full, on the
twelve-vertex two-cube, over all 66 unordered 2-site seeds and all
495 unordered 4-site seeds, with off-patch occupancy `0`. The
remaining-bit map `f_ex0=(0,0,1,1,0)` is displayed as a scored member.
It is not adopted as the physical Admissibility rule.
**Audit-status authority:** independent audit lane only. This note authors no audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_ex0_cov2_cov4_2026_08_15.py`](../scripts/f_cut_ex0_cov2_cov4_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

The 24 proper cube rotations act on neighbor 6-tuples in `{0,1}^6` and
partition those 64 cells into 10 orbits. Cube-covariant predicates are the
`{0,1}`-assignments to those orbits. The three displayed cuts

1. vanish on empty: `f(empty)=0`,
2. vanish on full: `f(full)=0`,
3. complement-even: `f(c)=f(1-c)`

leave five free bits, so `|F_cut|=32`. The five remaining bits, in the
displayed order `(wt1, opp2, adj2, vertex3, mixed3)`, are the values on
the three complement-pairs and two complement-fixed orbits after empty
and full are forced to `0`.

Write `f_ex0` for the remaining-bit tuple

```text
(wt1, opp2, adj2, vertex3, mixed3) = (0, 0, 1, 1, 0).
```

It fires on the `adj2`/`adj4` pair and on `vertex3`, and nowhere else.
The displayed selector on remaining bits is

```text
P(f) := (wt1=1) and (adj2, vertex3, mixed3) ≠ (0, 0, 0).
```

On the two-cube `{0,1,2}×{0,1}×{0,1}`, each unordered `k`-set of vertices
is a `k`-site seed. There are `C(12,2)=66` two-site seeds and
`C(12,4)=495` four-site seeds. Off-patch neighbors have occupancy `0`.
A blank-block is a different rule; it is not used. Each tick, every
unlocked on-patch vertex evaluates `f` on its six-neighbor occupancy
tuple and locks if `f=1`. The process is synchronous and stops at a
fixed point in at most 12 ticks. Fill means `|locks_halt|=12`. Coverage
is

```text
covk(f) = |{ S : |S|=k and f fills from S }|.
```

Do not list the seeds.

`f_L1(c)=1` if and only if some axis is unbalanced: `c_{+μ} ≠ c_{-μ}` for
at least one `μ ∈ {x,y,z}`. Equivalently, some discrete neighbor contrast
`n_μ = c_{+μ} − c_{-μ}` is nonzero. This is **not** Hamming parity
`|c|_1 mod 2`. `f_L1` is the 10-orbit reading `n ≠ 0`, not Hamming. Its
remaining-bit tuple is `(1, 0, 1, 1, 1)`.

Investment `#6511` named `f_ex0` by the pair `P=0` and `cov3(f_ex0)=24`.
Investment `#6509` named a class of `P`-false extras with `cov4>0`,
including maps with `wt1=0` and `adj2=1`. Those leftovers are a
selector-coverage pair and a class statement. This note is new scores
of a newly named map: the pair `(cov2, cov4)` of this remaining-bit
tuple.

**Theorem 1.** `P(f_ex0)=0` and

```text
cov2(f_ex0) = 0.
```

This matches the implication `P=0` ⇒ `cov2=0`. The implication holds
for every `P`-false member of `F_cut` on this patch; `f_ex0` is the
named control.

**Theorem 2.** Exhaustive run of all 495 four-site seeds gives

```text
cov4(f_ex0) = 232.
```

**Theorem 3.** The pair `(cov2, cov4)=(0, 232)` is displayed only.
Do not adopt a bit. Do not adopt `f_ex0`. Do not write the scores into Admissibility. The scores are not written into Admissibility. Hence no axiom or approved primitive is added.

Displayed, not adopted.

Not leftover-character of #6511 (that was `P=0` and `cov3=24`).
Not leftover-character of #6509 (that was the class of `P`-false extras with `cov4>0`, including `wt1=0` `adj2=1` maps). New scores of a newly named map.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The remaining-bit identity of f_ex0, the selector bit P(f_ex0)=0, and the exact integers cov2(f_ex0)=0 and cov4(f_ex0)=232 are enumerated on the two-cube. No physical law is selected."
trace_class: upstream_support
target_claim_id: f_cut_ex0_cov2_cov4
target_blocker_text: "2-site and 4-site fill coverage of F_cut remaining bits (0,0,1,1,0)"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the displayed (cov2,cov4) pair; any physical use must separately derive an Admissibility selector"
conditional_surface_status: "exact for f_ex0 on this twelve-vertex patch with off-patch o=0; no Z^3-wide law and no physical selector"
hypothetical_axiom_status: "no edit"
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
- the complete sets of 66 two-site seeds and 495 four-site seeds;
- the displayed remaining-bit tuple `(0, 0, 1, 1, 0)`.

No observational comparator, literature constant, Wilson weight, rate, or
generator is imported. No Record scalar functional appears.

## Exact Target And Objects

**Target.** Report `cov2(f_ex0)` as a control of `P=0` ⇒ `cov2=0`, and
report `cov4(f_ex0)`, on the two-cube with off-patch occupancy `0`.

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
so `|F_cut|=32`.

Define

```text
f_ex0(c) = 1  iff  c is of type adj2, adj4, or vertex3,
f_L1(c)  = 1  iff  u(c) ≥ 1.
```

A locked set `S` determines occupancies: a lattice neighbor in `S` has
occupancy `1`, and every other neighbor — including every off-patch
neighbor — has occupancy `0`. One synchronous tick replaces `S` by

```text
S ∪ { v in two-cube \ S : f(neighborhood_6(v; S)) = 1 }.
```

Then `cov2(f)` and `cov4(f)` are the numbers of 2-site and 4-site seeds
whose halt set has cardinality 12.

## Theorems

**Theorem 1.** There are exactly 24 proper cube rotations and exactly 10
orbits on `{0,1}^6`. The three cuts leave `|F_cut|=32`. The map `f_ex0`
is one element of `F_cut`, with remaining bits `(0, 0, 1, 1, 0)`. The
selector bit is `P(f_ex0)=0` because `wt1=0`. The unbalanced-axis map
`f_L1` is a different element of `F_cut`. It is not Hamming parity.
On the twelve-vertex two-cube with off-patch occupancy `0`, exhaustive
run of all 66 two-site seeds gives

```text
cov2(f_ex0) = 0.
```

This matches `P=0` ⇒ `cov2=0`. Every `P`-false map in `F_cut` has
`cov2=0` on this patch. The `#6511` three-site score is reconfirmed:
`cov3(f_ex0)=24`.

**Theorem 2.** Exhaustive run of all 495 four-site seeds gives

```text
cov4(f_ex0) = 232.
```

The map has `wt1=0` and `adj2=1`, so it sits in the `#6509` extras
class, but that class statement does not name this integer.

**Theorem 3.** The pair `(cov2, cov4)=(0, 232)` is displayed only.
Do not adopt a bit. Do not adopt `f_ex0`. Do not write the scores into Admissibility. Displayed, not adopted.

## Proof-Obligation Graph

| obligation | exact disposition |
|---|---|
| 24 proper cube rotations | signed permutations of the three axes with determinant `+1` |
| 10 orbits on `{0,1}^6` | axis-type classes `(u,b,e)` partition the 64 cells with the listed sizes |
| `|F_cut|=32` | three complement-pairs and two complement-fixed orbits remain free after the vanish cuts |
| `f_ex0` is in `F_cut` | remaining bits `(0,0,1,1,0)` with complements forced and empty/full at `0` |
| `P(f_ex0)=0` | `wt1=0` |
| `f_L1` is not Hamming | the two-unbalanced-axis orbit has even weight and `f_L1=1` |
| `cov2(f_ex0)=0` | exhaustive 66-seed fill census of `f_ex0` |
| `P=0` ⇒ `cov2=0` | no `P`-false member of `F_cut` fills a two-site seed on this patch |
| `cov3(f_ex0)=24` | reconfirmed `#6511` three-site census |
| `cov4(f_ex0)=232` | exhaustive 495-seed fill census of `f_ex0` |
| two-cube has twelve vertices | `{0,1,2}×{0,1}×{0,1}` |
| 66 two-site seeds | `C(12,2)` unordered 2-sets |
| 495 four-site seeds | `C(12,4)` unordered 4-sets |
| off-patch occupancy `0` | declared stencil default; not a blank-block |
| adoption of a bit | refused |

## Counterfactual And Mutation Table

1. Replace `f_L1` by Hamming parity `|c|_1 mod 2`: the maps disagree on the
   two-unbalanced-axis orbit, and Hamming is a different `F_cut` member.
2. Change the off-patch default away from `0`: the occupancy stencil
   changes and both coverage integers are a different object.
3. Drop any of the three cuts: the class is no longer the 32-element
   `F_cut`.
4. Stop at `P=0` and `cov3=24`: that leftover is `#6511`, not the pair
   `(cov2, cov4)`.
5. Stop at the class of `P`-false extras with `cov4>0`: that leftover is
   `#6509`, not this named map's scores.
6. Adopt `adj2=1` or `vertex3=1` as the physical rule: the scores are
   displayed members, not an Admissibility selector.

## What This Does Not Claim

- No physical Admissibility selector and no adopted occupancy law.
- No Qubit rewrite and no `M_2(C)`-valued conditional probability.
- No `Z^3`-wide formation, rate, or generator.
- No identification of `f_L1` with Hamming parity.
- No leftover-character restatement of `#6511` or `#6509` in place of
  this named map's `(cov2, cov4)` pair.
- No list of the 66 two-site seeds or the 495 four-site seeds.
- No blank-block or 5-site variant.

## No-Go Discipline Gate

The only negative claim is non-adoption: the displayed pair is not an
Admissibility selector. The positive pair `(cov2, cov4)=(0, 232)` is an
exact enumeration, not a wall.

### N1 — materially distinct routes

| Route | Exact attack | Result and authority | Marker |
|---|---|---|---|
| orbit reconstruction | Recompute the 24 rotations and the 10 axis-type orbits. | Theorem 1 and checks `thm1-twenty-four-rotations` / `thm1-f-cut-and-two-cube`. | **ATTEMPTED** |
| remaining-bit identity | Evaluate `f_ex0` on the five remaining orbits. | Theorem 1 and check `thm1-f-ex0-remaining-bits` give `(0,0,1,1,0)`. | **ATTEMPTED** |
| selector `P` | Apply `P` to those remaining bits. | Theorem 1 and check `thm1-p-false` give `P(f_ex0)=0`. | **ATTEMPTED** |
| two-site coverage | Run `f_ex0` on all 66 two-site seeds. | Theorem 1 and check `thm1-cov2-zero` give `cov2(f_ex0)=0`. | **ATTEMPTED** |
| `P=0` ⇒ `cov2=0` | Score every `P`-false map on two-site seeds. | Theorem 1 and check `thm1-p-implies-cov2-zero`. | **ATTEMPTED** |
| four-site coverage | Run `f_ex0` on all 495 four-site seeds. | Theorem 2 and check `thm2-cov4` give `cov4(f_ex0)=232`. | **ATTEMPTED** |

### N2 — wall independence and collapse

There is one negative conclusion: the displayed pair is not a selected
law. The two coverage integers are independent positive enumerations of
different seed cardinalities; they collapse only as the displayed pair
of this map, not as two walls.

| Pair | First closes second? | Second closes first? | Disposition |
|---|---:|---:|---|
| `cov2=0` / `P=0` | no: a coverage integer does not name the remaining-bit selector | no: the selector does not compute the census | implication plus control, not two walls |
| `cov2=0` / `cov4=232` | no: two-site miss does not name four-site coverage | no: a four-site integer does not force two-site miss | independent `|S|` |
| leftover of `#6511` / this pair | no: that leftover scored `(P, cov3)` | no: a `(cov2, cov4)` pair does not replace `cov3` | different object |
| leftover of `#6509` / this pair | no: that leftover named a class of extras | no: a named-map pair does not replace a class statement | different object |

Physical law selection is not a wall: this note makes no negative theorem
about the existence of a selector and simply does not claim one.

### N3 — hidden-condition scan

| Phrase or premise | Classification |
|---|---|
| “work on the twelve-vertex two-cube” | explicit patch hypothesis; not a `Z^3` theorem |
| off-patch occupancy `0` | explicit default; blank-block is a different rule |
| `F_cut` | explicit three-cut class; the other 992 covariant maps are excluded |
| remaining bits `(0,0,1,1,0)` | explicit displayed member |
| all 66 two-site seeds | explicit seed class |
| all 495 four-site seeds | explicit seed class |
| “lock” | Record permanence on this Boolean occupancy model, not a possibility-valued law |
| “cube-covariant” | invariance under the 24 proper rotations, cited to Lattice/Admissibility |
| Hamming parity | displayed mutation only |

### N4 — citation-to-residual matching

| Evidence path:line | Residual attacked | Residual claimed closed | Match? |
|---|---|---|---:|
| `docs/MINIMAL_AXIOMS_2026-06-29.md:37` | ambient lattice and cubic rotations | sites are `Z^3` with proper cubic rotations | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:57` | covariant nearest-neighbor rule | covariance is the class filter, not a selector | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:79` | lock permanence | a locked site stays locked | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:83` | unreadability of absence | unlocked and off-patch sites contribute occupancy `0`, not a readout | yes |
| `scripts/f_cut_ex0_cov2_cov4_2026_08_15.py:85` | 24 proper rotations | signed permutations with determinant `+1` | yes |
| `scripts/f_cut_ex0_cov2_cov4_2026_08_15.py:149` | `f_L1` definition | unbalanced-axis predicate, not Hamming | yes |
| `scripts/f_cut_ex0_cov2_cov4_2026_08_15.py:154` | Hamming mutation | `|c|_1 mod 2` is a different `F_cut` map | yes |
| `scripts/f_cut_ex0_cov2_cov4_2026_08_15.py:158` | `f_ex0` definition | remaining bits `(0, 0, 1, 1, 0)` | yes |
| `scripts/f_cut_ex0_cov2_cov4_2026_08_15.py:163` | selector `P` | `wt1=1` and not all of `adj2,vertex3,mixed3` zero | yes |
| `scripts/f_cut_ex0_cov2_cov4_2026_08_15.py:53` | 66 two-site seeds | `C(12,2)` unordered 2-sets on the two-cube | yes |
| `scripts/f_cut_ex0_cov2_cov4_2026_08_15.py:59` | 495 four-site seeds | `C(12,4)` unordered 4-sets on the two-cube | yes |
| `scripts/f_cut_ex0_cov2_cov4_2026_08_15.py:224` | coverage | number of `k`-site seeds a map fills | yes |

No evidence citation is used to claim that a physical occupancy law, a
formation rate, or a `Z^3`-wide selector has been closed.

### N5 — rhetoric and resolution audit

| Resolution | Executed? | Narrow negative supported? |
|---|---:|---|
| per element | yes: all 64 neighbor 6-tuples | each is assigned its axis-type orbit; no broader cell class is classified |
| per site | yes: the twelve two-cube vertices | each uses the same six-direction stencil with off-patch occupancy `0` |
| per mode | yes: `f_ex0` scored at `|S|=2` and `|S|=4` | the pair is this map on those seed classes; other maps are unclaimed except the `P=0` ⇒ `cov2=0` control |
| per block | yes: the pair `(cov2, cov4)=(0, 232)` | the pair is displayed, not adopted |
| lattice wide | no | no `Z^3`-wide formation or Admissibility selector is asserted |

The runner prints the same five resolution statements.

### N6 — partial closure and primitive scan

The primitive registry at `docs/audit/data/axiom_premise_nodes.json` was
checked. The only dependency used is the registered `minimal_axioms` node.
Approved primitives are `scale_reference_primitive`,
`kinetic_isotropy_primitive`, and `realized_state_primitive`. None of them
supplies a Boolean occupancy map, a seed-coverage pair, or an
Admissibility selector, and none is reclassified as an import or wall.

One partial-closure mechanism is displayed rather than suppressed:
`f_ex0` does lie in `F_cut`, does match `P=0` ⇒ `cov2=0`, and does fill
232 of the 495 four-site seeds. Those positive integers do not select
the map as the physical rule. The remaining physical choice — which, if
any, `F_cut` map is the Admissibility occupancy predicate — stays
explicit.

The open derivation-obligation registry
(`docs/audit/data/derivation_obligations.json`) names no occupancy-to-lock
coverage target; those open gates are unused here.

### N7 — hostile steelman

The strongest objection is that `#6511` already named `f_ex0` by
`P=0` and `cov3=24`, and that `#6509` already placed `wt1=0` `adj2=1`
maps among the `P`-false extras with `cov4>0`, so the pair
`(cov2, cov4)` might be called leftover decoration of those two
investments. That objection is correctly about the existence of a
selector-coverage pair and a class statement. It does not overturn the
stated theorem: the named map has `cov2=0` and `cov4=232`, a new pair
of integers that neither leftover computed.

### N8 — cross-cycle echo

A raw `(P, cov3)` score (`#6511`) and a class of `P`-false `cov4>0`
extras (`#6509`) are different claims. This note executes the 2-site
and 4-site coverage of the remaining-bit tuple `(0,0,1,1,0)`.

**Gate disposition:** PASS for the finite pair `(cov2, cov4)=(0, 232)`
and the `P=0` ⇒ `cov2=0` control. FAIL / DO NOT SHIP for “adopt
`f_ex0`,” “adopt a remaining bit,” or “write the scores into
Admissibility.”

No-Go Discipline disposition: **PASS**

## Primary Runner

The primary runner rebuilds the two-cube, the ten-orbit `F_cut` class,
the remaining-bit map `(0,0,1,1,0)`, the selector bit `P`, the 66-seed
two-site census, the 495-seed four-site census, the `P=0` ⇒ `cov2=0`
control, the current premise boundary, and the non-adoption wording.
It authors no audit verdict.
