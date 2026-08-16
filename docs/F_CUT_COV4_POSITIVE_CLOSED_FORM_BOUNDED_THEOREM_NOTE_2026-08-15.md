---
claim_id: f_cut_cov4_positive_closed_form_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Among the 32 F_cut maps on the two-cube with off-patch o=0, whether positive 4-site coverage is equivalent to P is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_cov4_positive_closed_form_2026_08_15.py
---

# Whether Positive 4-Site Coverage Equals P Among the 32 F_cut Maps

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact occupancy-to-lock fill positivity on the twelve-vertex two-cube
with off-patch occupancy `0`, scored on the 495 four-site seeds, for the
thirty-two cube-covariant cut maps `F_cut`.
**Audit-status authority:** independent audit lane only. This note writes no
audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_cov4_positive_closed_form_2026_08_15.py`](../scripts/f_cut_cov4_positive_closed_form_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result up front

Investment #6494 closed the 2-site positivity question: `cov2(f) > 0` if and
only if the remaining-bit predicate
`P(f) := (wt1=1) and (adj2,vertex3,mixed3)≠(0,0,0)`.
Investment #6502 showed that `cov3>0` is not `P`. Investment #6503 showed
that `cov1>0` is not `P`. This note repeats the same displayed predicate on a
new seed cardinality: four-site seeds. New k, not leftover-character of those
three investments and not a Max(4) rename.

`F_cut` is the cube-covariant class of `{0,1}`-valued maps on the six
nearest-neighbor occupancy bits with `f(empty)=f(full)=0` and `f(c)=f(1-c)`.
It has five free remaining bits and size 32. Remaining bits are ordered as
`(wt1, opp2, adj2, vertex3, mixed3)`.

`f_L1(c)=1` if and only if some axis is unbalanced: the signed pair
`n_μ = c_{+μ} − c_{-μ}` is nonzero. This is **not** Hamming parity
`|c|_1 mod 2`. The remaining-bit tuple of `f_L1` is `(1, 0, 1, 1, 1)`.

On the two-cube with off-patch occupancy `0`, write
`cov4(f) = |{S : |S|=4 and f fills from S}|`. Then:

- Theorem 1. cov4(f) > 0 is not equivalent to P(f) among the 32 maps.
  The lex-first remaining-bit counterexample is `(0, 0, 1, 0, 0)`, which has
  `P = 0` and `cov4 = 52`.
- Theorem 2. `N_P = 14`, `N_pos = 24`, `N_both = 14`.
- Theorem 3. `P` is displayed. Displayed, not adopted.

Do not write P into Admissibility. The extra that would have made 4-site
positivity the same selector as 2-site positivity is not present.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The 32 F_cut maps are enumerated by remaining bits and scored exactly on the 495 four-site seeds of the two-cube. Whether cov4>0 equals P, and the counts N_P, N_pos, N_both, are finite exact facts. No physical Admissibility selector is claimed."
trace_class: frontier_discovery
target_claim_id: f_cut_cov4_positive_closed_form
target_blocker_text: "whether cov4>0 is the same selector P among the 32 F_cut maps"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the bounded 4-site positivity-versus-P comparison; do not adopt the displayed predicate P"
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

**Target.** Decide whether `cov4(f) > 0` if and only if `P(f)`, for every
member of `F_cut` on `T`.

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

The four-site seeds are the `C(12,4) = 495` unordered 4-subsets of `T`. Then
`cov4(f)` is the number of those subsets from which `f` fills.

The displayed remaining-bit predicate is

`P(f) := (wt1=1) and (adj2,vertex3,mixed3)≠(0,0,0)`.

Opp2 is free in `P`. The two remaining-bit tuples with `wt1=1` and
`(adj2, vertex3, mixed3) = (0, 0, 0)` are `(1, 0, 0, 0, 0)` and
`(1, 1, 0, 0, 0)`; both have `P` false. Displayed, not adopted.

## Theorems

### Theorem 1 — `cov4>0` is not `P`; lex-first witness

Enumerate all 32 remaining-bit tuples of `F_cut` and score `cov4` on the 495
four-site seeds. Then `cov4(f) > 0` is not equivalent to `P(f)`.

The lex-first remaining-bit counterexample, in the order
`(wt1, opp2, adj2, vertex3, mixed3)`, is `(0, 0, 1, 0, 0)`. That map has
`wt1 = 0`, so `P` is false, and `cov4 = 52 > 0`.

### Theorem 2 — `N_P`, `N_pos`, `N_both`

Among the 32 maps:

- `N_P = 14` maps satisfy `P`;
- `N_pos = 24` maps have `cov4 > 0`;
- `N_both = 14` maps satisfy both.

Every `P`-true map has `cov4 > 0`. Equivalence fails only in the other
direction: ten `P`-false maps still have positive 4-site coverage. Those ten
are the eight maps with `wt1 = 0` and `adj2 = 1`, together with the two
tuples `(1, 0, 0, 0, 0)` and `(1, 1, 0, 0, 0)`.

### Theorem 3 — display; do not adopt `P`

`P` is the same remaining-bit predicate that #6494 found equivalent to
`cov2>0`. On four-site seeds it is not the positivity selector. Displayed,
not adopted. Do not write P into Admissibility.

`f_L1`, with remaining bits `(1, 0, 1, 1, 1)`, satisfies `P` and has
positive `cov4`. That is consistent with Theorem 2 and does not restore
equivalence.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice and Admissibility premises | quoted; no edit |
| `F_cut` as the 32 cube-covariant cut maps | enumerated by remaining bits |
| `f_L1` as unbalanced-axis / `n_μ ≠ 0` | defined; Hamming rejected |
| two-cube, 495 four-site seeds, off-patch 0 | declared finite patch |
| `P` as `(wt1=1)` and `(adj2,vertex3,mixed3)≠(0,0,0)` | displayed, not adopted |
| `cov4>0` iff `P` | fails; lex-first witness `(0, 0, 1, 0, 0)` |
| `N_P = 14`, `N_pos = 24`, `N_both = 14` | proved by exhaustive scoring |
| leftover-character of #6494, #6502, #6503 | refused; new k |
| physical Admissibility selector | open |

## Boundary and imports

Not leftover-character of #6494: that closed `cov2>0` iff `P` on two-site
seeds. The present count is `cov4` on 495 four-site seeds, a different seed
family.

Not leftover-character of #6502: that showed `cov3>0` is not `P` on
three-site seeds. New k.

Not leftover-character of #6503: that showed `cov1>0` is not `P` on
one-site seeds. New k.

The note is not a Max(4) ranking and not a seed-table: maximizers of `cov4`
are not selected, and no seed census of a named map is compiled.

Off-patch occupancy `0` is an explicit default on this patch. A blank-block
is a different rule and is not used.

No `Z^3`-wide formation law is claimed. Do not write P into Admissibility.

## Promotion value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers whether 4-site positivity is the same selector as `P` inside `F_cut` on this patch. |
| V2 | Current main has no landed 4-site positivity-versus-`P` comparison for `F_cut`. |
| V3 | The 32 maps, 495 seeds, and occupancy-to-lock evolution are independently finite and exact. |
| V4 | The theorem is more than a restatement of Admissibility: it scores a declared finite class. |
| V5 | It is not a physical selector: equivalence fails, and displayed `P` is not adopted. |

## No-Go Discipline gate

The negative content is narrow: `cov4>0` is not equivalent to `P` among the
32 `F_cut` maps on this patch. No global compiler impossibility is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| Hamming parity | identify `f_L1` with `|c|_1 mod 2` | **ATTEMPTED** |
| leftover 2-site closed form | treat the 4-site comparison as leftover-character of #6494 | **ATTEMPTED** |
| leftover 3-site or 1-site | treat the count as leftover-character of #6502 or #6503 | **ATTEMPTED** |
| Max(4) rename | replace positivity-versus-`P` by a 4-site maximizer ranking | **ATTEMPTED** |
| adopt `P` | write `P` into Admissibility | **ATTEMPTED** |
| blank-block off-patch | replace occupancy `0` by a blank-block | **ATTEMPTED** |

### N2 — wall independence

The failed equivalence, the Hamming contrast, and the off-patch convention
are distinct. This note claims no complete wall collection.

### N3 — hidden-condition scan

The two-cube, the 495 four-site seeds, off-patch occupancy `0`,
occupancy-to-lock ticks, the `F_cut` remaining-bit order, and the displayed
predicate `P` are declared. Equivalence of `cov4>0` with `P` is not silently
assumed.

### N4 — source residual matching

The live axiom memo supplies `Z^3`, proper cubic rotations, and one covariant
nearest-neighbor rule. The residual answered here is whether 4-site
positivity equals `P` on the declared patch, not leftover-character of
#6494, #6502, or #6503, and not a Max(4) ranking.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | 64 neighbor 6-tuples by axis-type orbit | no continuum occupancy |
| per site | twelve two-cube vertices, same stencil | no privileged site |
| per mode | all 32 `F_cut` maps scored on 495 seeds | no physical law selection |
| per block | `N_P`, `N_pos`, `N_both` on this patch | no Admissibility write-in |
| lattice wide | checked and not executed | no `Z^3`-wide formation law |

### N6 — live partial-closure paths

Live routes include a different seed family, a different off-patch rule, a
selector other than `P` or `cov4>0`, and any independently derived physical
map from `F_cut` into Admissibility.

### N7 — hostile steelman

**Steelman:** #6494 already showed that positivity is `P`, so every later
`k` inherits the same selector.

**Answer:** Inheritance fails at `k=4`. Fourteen maps satisfy `P` and all
of them have `cov4>0`, but twenty-four maps have `cov4>0`. The lex-first
witness `(0, 0, 1, 0, 0)` has `P` false and `cov4 = 52`. Displayed `P` is
not adopted.

### N8 — cross-cycle echo

Investments #6502 and #6503 already showed that `cov3>0` and `cov1>0` are
not `P`. Echoing those failures is not a substitute for the four-site count:
`k=4` is a new seed family, and the lex-first witness and the triple
`(N_P, N_pos, N_both)` are four-site facts.

No-Go Discipline disposition: **PASS** for the finite comparison and the
narrow equivalence failure. FAIL / DO NOT SHIP for “`cov4>0` is `P`” or
“displayed `P` is the physical rule.”

## Live parent quotes

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

> There is one fixed nearest-neighbor admissibility rule, covariant under lattice
> translations and proper cubic rotations.

> A site with no record cannot be read.

## Runner contract

The companion runner enumerates the 32 `F_cut` maps, scores `cov4` on the
495 four-site seeds, compares positivity with displayed `P`, reports the
lex-first remaining-bit counterexample `(0, 0, 1, 0, 0)`, and reports
`N_P = 14`, `N_pos = 24`, and `N_both = 14`. Declared audit inputs are this
note and the axiom memo; the runner writes no cache and authors no audit
verdict.
