---
claim_id: f_cut_cov2_positive_closed_form_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Among the 32 F_cut maps on the two-cube with off-patch o=0, positive 2-site coverage is equivalent to remaining bits satisfying wt1=1 and (adj2,vertex3,mixed3) not all zero. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_cov2_positive_closed_form_2026_08_15.py
---

# Closed Form of Positive 2-Site Coverage Among the 32 F_cut Maps

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact occupancy-to-lock fill counts on the twelve-vertex two-cube
with off-patch occupancy `0`, scored on the sixty-six two-site seeds, for the
thirty-two cube-covariant cut maps `F_cut`.
**Audit-status authority:** independent audit lane only. This note writes no
audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_cov2_positive_closed_form_2026_08_15.py`](../scripts/f_cut_cov2_positive_closed_form_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result up front

Investment #6490 showed that cov2>0 is not wt1=1: the two exceptions are
remaining-bit tuples `(1, 0, 0, 0, 0)` and `(1, 1, 0, 0, 0)`. This note
tests a new selector on the same 32 maps, not leftover of naming those two.

`F_cut` is the cube-covariant class of `{0,1}`-valued maps on the six
nearest-neighbor occupancy bits with `f(empty)=f(full)=0` and `f(c)=f(1-c)`.
It has five free remaining bits and size 32. Remaining bits are ordered as
`(wt1, opp2, adj2, vertex3, mixed3)`.

`f_L1(c)=1` if and only if some axis is unbalanced: the signed pair
`n_μ = c_{+μ} − c_{-μ}` is nonzero. This is **not** Hamming parity
`|c|_1 mod 2`. The remaining-bit tuple of `f_L1` is `(1, 0, 1, 1, 1)`.

On the two-cube with off-patch occupancy `0`, write
`cov2(f) = |{S : |S|=2 and f fills from S}|`. Define

`P(f) := (wt1=1) and (adj2,vertex3,mixed3)≠(0,0,0)`.

Then:

- Theorem 1. The two #6490 exceptions have P=false and cov2=0.
- Theorem 2. `cov2(f)>0 iff P(f)` for all 32 maps. The counts are
  `N_pos = 14`, `N_P = 14`, `N_both = 14`.
- Theorem 3. The selector `P` is displayed. Do not adopt a bit.

Displayed, not adopted.

Do not write the selector into Admissibility. The closed form is a
remaining-bit predicate on this patch, not a physical law.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The 32 F_cut maps are enumerated by remaining bits and scored exactly on the sixty-six two-site seeds of the two-cube. P(f) and cov2(f)>0 are finite exact predicates. No physical Admissibility selector is claimed."
trace_class: frontier_discovery
target_claim_id: f_cut_cov2_positive_closed_form
target_blocker_text: "which remaining bits make cov2>0 among the 32 F_cut maps"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the bounded closed form; do not adopt P as a bit"
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
- off-patch occupancy `0` (a neighbor of a site in `T` that is not itself in
  `T` is treated as unoccupied; a blank-block is a different rule);
- the six-direction stencil
  `{±e_x, ±e_y, ±e_z}` at every site;
- the 24 proper cube rotations;
- the ten axis-type orbits of `{0,1}^6` under those rotations;
- the class `F_cut` of cube-covariant maps with `f(empty)=f(full)=0` and
  complement symmetry `f(c)=f(1-c)`.

No observational comparator, literature constant, rate, or generator is
imported. Hamming parity is a contrast map only; it is not `f_L1`.

## Exact target and objects

**Target.** Test whether positive 2-site coverage on `T` is equivalent to
the remaining-bit selector `P` on `F_cut`.

A configuration `c ∈ {0,1}^6` is a six-tuple of neighbor occupancies in
direction order `(+x,-x,+y,-y,+z,-z)`. Axis type is
`(n_unbalanced, n_both, n_empty)`, where an axis is unbalanced if its two
bits differ, both if both bits are 1, and empty if both bits are 0. Complement
swaps `n_both` with `n_empty`. The five remaining bits of `F_cut`, in the
order `(wt1, opp2, adj2, vertex3, mixed3)`, are the values on orbit types
`(1,0,2)`, `(0,1,2)`, `(2,0,1)`, `(3,0,0)`, `(1,1,1)`. Complement partners
are forced equal; empty and full are fixed at 0.

Occupancy-to-lock: from a locked set `L ⊂ T`, a site `x ∈ T \ L` locks at
the next tick if and only if `f` of its six-neighbor occupancy (off-patch
entries 0) equals 1. The map `f` fills from a seed `S` if iterating this
rule from `L_0 = S` reaches `L = T` in at most 13 ticks.

The two-site seeds are the sixty-six unordered pairs of distinct sites in
`T`. Then `cov2(f)` is the number of those pairs from which `f` fills.

The selector is `P(f) := (wt1=1) and (adj2,vertex3,mixed3)≠(0,0,0)`. The
`opp2` bit is free in `P`. New selector, not leftover of naming the two
#6490 exceptions.

## Theorems

### Theorem 1 — the two #6490 exceptions have P=false and cov2=0

The remaining-bit tuples `(1, 0, 0, 0, 0)` and `(1, 1, 0, 0, 0)` are the
two maps with `wt1=1` and `(adj2,vertex3,mixed3)=(0,0,0)`. For both,
`P` is false because the last three remaining bits are all zero. Direct
evolution on all 66 two-site seeds gives `cov2=0` for both. This reconfirms
#6490: cov2>0 is not wt1=1.

### Theorem 2 — `cov2(f)>0 iff P(f)` on all 32 maps

Enumerate the 32 members of `F_cut` by remaining bits. For each map compute
`cov2(f)` by occupancy-to-lock from every two-site seed, and evaluate `P`
from the remaining bits. Then `P(f)` equals the Boolean `cov2(f)>0` on
every map. The counts are `N_pos = 14`, `N_P = 14`, `N_both = 14`. There
is no counterexample tuple.

The fourteen maps with `P` true are exactly the maps with `wt1=1` and at
least one of `adj2`, `vertex3`, `mixed3` equal to 1.

### Theorem 3 — display; do not adopt a bit

`P` is a remaining-bit closed form of the predicate `cov2>0` on this
patch. Displayed, not adopted. Do not adopt a bit: neither `wt1` alone,
nor `opp2`, nor any one of `adj2`, `vertex3`, `mixed3`, nor the compound
`P`, is written into Admissibility.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice and Admissibility premises | quoted; no edit |
| `F_cut` as the 32 cube-covariant cut maps | enumerated by remaining bits |
| `f_L1` as unbalanced-axis / `n_μ ≠ 0` | defined; Hamming rejected |
| two-cube, sixty-six two-site seeds, off-patch 0 | declared finite patch |
| two #6490 exceptions have P=false and cov2=0 | proved by evolution |
| `cov2(f)>0 iff P(f)` on all 32 maps | proved by exhaustive scoring |
| adopt `P` or a remaining bit | refused; displayed, not adopted |
| leftover of naming the two #6490 exceptions | refused; new selector |
| physical Admissibility selector | open |

## Boundary and imports

Not leftover of naming those two: #6490 only exhibited the two `wt1=1`
maps with `cov2=0`. The present object is the selector `P` on all 32 maps,
which excludes those two by the three-bit remainder rather than by a
two-name leftover list.

Off-patch occupancy `0` is an explicit default on this patch. A blank-block
is a different rule and is not used.

No `Z^3`-wide formation law is claimed. Do not write the selector into
Admissibility.

## Promotion value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers whether `cov2>0` has a remaining-bit closed form inside `F_cut` on this patch. |
| V2 | Current main has the #6490 exceptions but no landed closed form of `cov2>0`. |
| V3 | The 32 maps, 66 seeds, and occupancy-to-lock evolution are independently finite and exact. |
| V4 | The theorem is more than a restatement of Admissibility: it scores a declared finite class. |
| V5 | It is not a physical selector: `P` is displayed and no bit is adopted. |

## No-Go Discipline gate

The negative content is narrow: `wt1=1` alone does not select positive
2-site coverage, and the closed form `P` is not adopted as a bit. No
global compiler impossibility is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| Hamming parity | identify `f_L1` with `|c|_1 mod 2` | **ATTEMPTED** |
| leftover of two names | replace `P` by the two-name leftover list from #6490 | **ATTEMPTED** |
| leftover of `wt1=1` | treat the closed form as leftover-character of #6490 | **ATTEMPTED** |
| adopt a bit | write `P` or one remaining bit into Admissibility | **ATTEMPTED** |
| blank-block off-patch | replace occupancy `0` by a blank-block | **ATTEMPTED** |
| lattice-wide formation | lift the patch count to a `Z^3` formation law | **ATTEMPTED** |

### N2 — wall independence

The failed `wt1=1` identification, the Hamming contrast, and the off-patch
convention are distinct. This note claims no complete wall collection.

### N3 — hidden-condition scan

The two-cube, the sixty-six pairs, off-patch occupancy `0`, occupancy-to-lock
ticks, and the `F_cut` remaining-bit order are declared. Adoption of `P` as
a physical bit is not silently assumed.

### N4 — source residual matching

The live axiom memo supplies `Z^3`, proper cubic rotations, and one covariant
nearest-neighbor rule. The residual answered here is the remaining-bit
closed form of `cov2>0` on the declared patch, not leftover of naming the
two #6490 exceptions.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | 64 neighbor 6-tuples by axis-type orbit | no continuum occupancy |
| per site | twelve two-cube vertices, same stencil | no privileged site |
| per mode | all 32 `F_cut` maps scored on 66 seeds | no physical law selection |
| per block | `P` versus `cov2>0` on this patch | no Admissibility write-in |
| lattice wide | checked and not executed | no `Z^3`-wide formation law |

### N6 — live partial-closure paths

Live routes include a different seed family, a different off-patch rule, a
selector other than `P`, and any independently derived physical map from
`F_cut` into Admissibility.

### N7 — hostile steelman

**Steelman:** the two #6490 exceptions already name the leftover, so a
closed form is only a two-name list.

**Answer:** `P` is a three-bit remainder on `wt1=1`, not a leftover list of
two tuples. It is checked against all 32 maps. Displayed, not adopted.
Do not adopt a bit.

### N8 — cross-cycle echo

Investment #6490 already showed that cov2>0 is not wt1=1. Echoing those two
exceptions is not a substitute for testing `P` on the whole class.

No-Go Discipline disposition: **PASS** for the finite closed form and the
refusal to adopt a bit. FAIL / DO NOT SHIP for “`P` is the physical rule”
or “`wt1` alone selects 2-site fillability.”

## Live parent quotes

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

> There is one fixed nearest-neighbor admissibility rule, covariant under lattice
> translations and proper cubic rotations.

> A site with no record cannot be read.

## Runner contract

The companion runner enumerates the 32 `F_cut` maps, scores `cov2` on the
sixty-six two-site seeds, reconfirms that the two #6490 exceptions have
P=false and cov2=0, and checks that `cov2(f)>0 iff P(f)` on the whole
class. Declared audit inputs are this note and the axiom memo; the runner
writes no cache and authors no audit verdict.
