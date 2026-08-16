---
claim_id: f_cut_cov3_positive_bit_support_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Among the 20 F_cut maps with cov3>0 on the two-cube with off-patch o=0, whether any remaining bit is constant is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_cov3_positive_bit_support_2026_08_15.py
---

# Remaining-Bit Support On The Twenty Positive-Coverage Maps

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact occupancy-to-lock 3-site fillability on the twelve-vertex
two-cube with off-patch occupancy `0`, for the thirty-two cube-covariant
cut maps `F_cut`, restricted to the twenty maps with `cov3>0`, reporting
for each remaining bit the pair
`(n_bit=0 among the 20, n_bit=1 among the 20)` and whether any remaining
bit is constant on those twenty maps.
**Audit-status authority:** independent audit lane only. This note writes no
audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_cov3_positive_bit_support_2026_08_15.py`](../scripts/f_cut_cov3_positive_bit_support_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result up front

Investment p3bit5 closed the remaining-bit selector menu: no 1-bit, 2-bit,
3-bit, 4-bit, or 5-bit remaining-bit AND or OR equals `cov3>0`.
`N_pos = 20`. Remaining-bit search is exhausted. This note asks a
different object: for each of the five remaining bits, whether it is
constant on the 20 maps with `cov3>0`. The output is a new support
description, not a selector.

`F_cut` is the cube-covariant class of `{0,1}`-valued maps on the six
nearest-neighbor occupancy bits with `f(empty)=f(full)=0` and `f(c)=f(1-c)`.
It has five free remaining bits and size 32. Remaining bits are ordered as
`(wt1, opp2, adj2, vertex3, mixed3)`.

`f_L1(c)=1` if and only if some axis is unbalanced: the signed pair
`n_μ = c_{+μ} − c_{-μ}` is nonzero. This is **not** Hamming parity
`|c|_1 mod 2`. The remaining-bit tuple of `f_L1` is `(1, 0, 1, 1, 1)`.

On the two-cube with off-patch occupancy `0`, write
`cov3(f)` for the number of unordered 3-site seeds from which `f` fills.

- Theorem 1. For each remaining bit, the pair
  `(n_bit=0 among the 20, n_bit=1 among the 20)`.
- Theorem 2. Whether any remaining bit is constant on the 20. None.
- Theorem 3. Display. Do not adopt a bit.

Do not write the pairs into Admissibility. Displayed, not adopted.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The 32 F_cut maps are enumerated by remaining bits and scored exactly by whether any of the 220 three-site seeds fills. On the 20 maps with cov3>0, each remaining bit is counted as (n=0, n=1). No physical Admissibility selector is claimed."
trace_class: frontier_discovery
target_claim_id: f_cut_cov3_positive_bit_support
target_blocker_text: "whether any remaining bit is constant on the 20 F_cut maps with cov3>0"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the remaining-bit support pairs on the twenty maps; do not adopt a displayed bit"
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
  complement symmetry `f(c)=f(1-c)`;
- the five remaining bits in the order `(wt1, opp2, adj2, vertex3, mixed3)`.

No observational comparator, literature constant, rate, or generator is
imported. Hamming parity is a contrast map only; it is not `f_L1`.

## Exact target and objects

**Target.** Among the 20 members of `F_cut` with `cov3>0` on the two-cube
with off-patch occupancy `0`, report for each remaining bit the pair
`(n_bit=0 among the 20, n_bit=1 among the 20)`, and decide whether any
remaining bit is constant on those twenty maps.

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

The three-site seeds are the `C(12,3)=220` unordered triples of vertices of
`T`. Then `cov3(f)` is the number of those triples from which `f` fills, and
`cov3>0` is the Boolean fillability predicate.

A remaining bit `b` is constant on the 20 if one of `n_{b=0}` or `n_{b=1}`
is zero. That is a support description of the positive-coverage set, not a
selector `Q` tested for `cov3>0` iff `Q`.

## Theorems

### Theorem 1 — remaining-bit pairs on the twenty maps

There are exactly 24 proper cube rotations and exactly 10 orbits on
`{0,1}^6`. The three cuts leave `|F_cut|=32`. The unbalanced-axis map
`f_L1` is one element of `F_cut` and is not Hamming parity.

Exhaustive evaluation of all 32 maps on all 220 three-site seeds gives
`N_pos = 20` maps with `cov3>0`. For each remaining bit, the pair
`(n_bit=0 among the 20, n_bit=1 among the 20)` is:

| remaining bit | `(n_bit=0, n_bit=1)` among the 20 |
|---|---|
| `wt1` | `(n_{wt1=0}, n_{wt1=1}) = (6, 14)` |
| `opp2` | `(n_{opp2=0}, n_{opp2=1}) = (8, 12)` |
| `adj2` | `(n_{adj2=0}, n_{adj2=1}) = (6, 14)` |
| `vertex3` | `(n_{vertex3=0}, n_{vertex3=1}) = (8, 12)` |
| `mixed3` | `(n_{mixed3=0}, n_{mixed3=1}) = (10, 10)` |

Each pair sums to `N_pos = 20`. `f_L1` itself is among the 20.

### Theorem 2 — no remaining bit is constant on the 20

A remaining bit is constant on the 20 if and only if one entry of its
Theorem 1 pair is `0`. None of the five pairs has a zero entry.

`wt1` splits `6` versus `14`. `opp2` splits `8` versus `12`. `adj2`
splits `6` versus `14`. `vertex3` splits `8` versus `12`. `mixed3`
splits `10` versus `10`. No remaining bit is constant on the 20.

### Theorem 3 — display; do not adopt a bit

The pairs are displayed. Do not adopt a bit. The support description is
not written into Admissibility. It is not a remaining-bit selector and
not a Max(3) rename.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice and Admissibility premises | quoted; no edit |
| `F_cut` as the 32 cube-covariant cut maps | enumerated by remaining bits |
| `f_L1` as unbalanced-axis / `n_μ ≠ 0` | defined; Hamming rejected |
| two-cube, 220 three-site seeds, off-patch 0 | declared finite patch |
| `N_pos = 20` after p3bit5 selector exhaustion | proved by exhaustive `cov3` |
| each remaining-bit pair on the 20 | proved |
| any remaining bit constant on the 20 | none |
| display; do not adopt a bit | displayed, not adopted |
| physical Admissibility selector | open |

## Boundary and imports

Remaining-bit search is exhausted: p3bit5 showed no 1–5 bit remaining-bit
AND or OR equals `cov3>0`. The present count does not reopen that menu.
It reports a support description of the already enumerated 20 maps.

The note is not a Max(3) rename: no maximum of `cov3` is reported as a
selector, and `f_L1` is used only as the unbalanced-axis control.

Off-patch occupancy `0` is an explicit default on this patch. A blank-block
is a different rule and is not used.

No `Z^3`-wide formation law is claimed. Do not write the pairs into
Admissibility.

## Promotion value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers, for each remaining bit, the pair `(n=0, n=1)` on the 20 maps with `cov3>0`, and whether any remaining bit is constant. |
| V2 | Current main has the exhausted 1–5 bit remaining-bit AND/OR search (p3bit5) but no landed support census of the 20. |
| V3 | The 32 maps, 220 seeds, and occupancy-to-lock evolution are independently finite and exact. |
| V4 | The theorem is more than a restatement of Admissibility: it scores a declared finite class. |
| V5 | It is not a physical selector: no remaining bit is constant, and no bit is adopted. |

## No-Go Discipline gate

The negative content is narrow: no remaining bit is constant on the 20
`F_cut` maps with `cov3>0` on this patch. No global compiler impossibility
is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| Hamming parity | identify `f_L1` with `|c|_1 mod 2` | **ATTEMPTED** |
| leftover 1–5 bit menu | treat the pairs as a restatement of the failed AND/OR tests | **ATTEMPTED** |
| Max(3) rename | replace the support pairs by a maximum-`cov3` ranking | **ATTEMPTED** |
| adopt a bit | write a remaining bit into Admissibility | **ATTEMPTED** |
| blank-block off-patch | replace occupancy `0` by a blank-block | **ATTEMPTED** |
| lattice-wide formation | lift the patch census to a `Z^3` formation law | **ATTEMPTED** |

### N2 — wall independence

The exhausted 1–5 bit AND/OR tests, the five support pairs, the Hamming
contrast, and the off-patch convention are distinct. This note claims
no complete wall collection.

### N3 — hidden-condition scan

The two-cube, the 220 triples, off-patch occupancy `0`, occupancy-to-lock
ticks, the `F_cut` remaining-bit order, and the restriction to the 20
maps with `cov3>0` are declared. No silent extra bit is treated as
constant.

### N4 — source residual matching

The live axiom memo supplies `Z^3`, proper cubic rotations, and one covariant
nearest-neighbor rule. The residual answered here is the remaining-bit
support of `cov3>0` on the declared patch after remaining-bit search is
exhausted, and not a Max(3) rename.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | 64 neighbor 6-tuples by axis-type orbit | no continuum occupancy |
| per site | twelve two-cube vertices, same stencil | no privileged site |
| per mode | all 32 `F_cut` maps scored on 220 seeds | no physical law selection |
| per block | each remaining bit counted on the 20 | no Admissibility write-in |
| lattice wide | checked and not executed | no `Z^3`-wide formation law |

### N6 — live partial-closure paths

Live routes include a different seed family, a different off-patch rule,
a different finite patch, and any independently derived physical map from
`F_cut` into Admissibility.

### N7 — hostile steelman

**Steelman:** p3bit5 already ruled out every remaining-bit AND and OR of
width 1 through 5, so one remaining bit must be constant on the 20 and
recover a support-side selector.

**Answer:** `wt1` is `(6, 14)`. `opp2` is `(8, 12)`. `adj2` is
`(6, 14)`. `vertex3` is `(8, 12)`. `mixed3` is `(10, 10)`. None.

### N8 — cross-cycle echo

Investment p3bit5 already showed no 1–5 bit AND/OR equals `cov3>0`. Echoing
that failure is not a substitute for counting the five remaining bits on
the 20. The present object is a support description, not a selector.

No-Go Discipline disposition: **PASS** for the finite support census and the
narrow none-constant verdict. FAIL / DO NOT SHIP for “a remaining bit is
constant on the 20” or “a displayed pair is the physical rule.”

## Live parent quotes

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

> There is one fixed nearest-neighbor admissibility rule, covariant under lattice
> translations and proper cubic rotations.

> A site with no record cannot be read.

## Runner contract

The companion runner enumerates the 32 `F_cut` maps, scores `cov3` on the
220 three-site seeds, restricts to the 20 maps with `cov3>0`, reports for
each remaining bit the pair `(n_bit=0 among the 20, n_bit=1 among the 20)`,
decides whether any remaining bit is constant on the 20, and reports that
none is constant.
Declared audit inputs are this note and the axiom memo; the runner writes
no cache and authors no audit verdict.
