---
claim_id: f_cut_cov3_max_selector_search_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Among the 32 F_cut maps on the two-cube with off-patch o=0, whether a displayed remaining-bit predicate equals cov3=220 is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_cov3_max_selector_search_2026_08_15.py
---

# Remaining-Bit Selector Search For Max(3) Coverage `cov3=220`

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact occupancy-to-lock 3-site fillability on the twelve-vertex
two-cube with off-patch occupancy `0`, for the thirty-two cube-covariant
cut maps `F_cut`, tested against a displayed list of remaining-bit
predicates `Q` for equality with `cov3=220`.
**Audit-status authority:** independent audit lane only. This note writes no
audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_cov3_max_selector_search_2026_08_15.py`](../scripts/f_cut_cov3_max_selector_search_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result up front

Investment #6473/#6457 named Max(3) as the pair `{L1, f1}` with
`cov3=220`. Investment #6551 showed that no remaining bit is constant on the 20
maps with `cov3>0`. That residual asked a support question on the
positive set. New Max(3) selector: this note is a remaining-bit search
for whether any displayed `Q` equals the Max(3) predicate `cov3=220`
among the 32 maps. Not leftover-character of #6551: that was whether a
remaining bit is constant on the 20.

`F_cut` is the cube-covariant class of `{0,1}`-valued maps on the six
nearest-neighbor occupancy bits with `f(empty)=f(full)=0` and `f(c)=f(1-c)`.
It has five free remaining bits and size 32. Remaining bits are ordered as
`(wt1, opp2, adj2, vertex3, mixed3)`.

`f_L1(c)=1` if and only if some axis is unbalanced: the signed pair
`n_μ = c_{+μ} − c_{-μ}` is nonzero. This is **not** Hamming parity
`|c|_1 mod 2`. The remaining-bit tuple of `f_L1` is `(1, 0, 1, 1, 1)`.
The remaining-bit tuple of `f1` is `(1, 1, 1, 1, 1)`.

On the two-cube with off-patch occupancy `0`, write
`cov3(f)` for the number of unordered 3-site seeds from which `f` fills.
The displayed candidates are: each remaining bit; every 2-bit AND; every
2-bit OR; `Q_*=(wt1 and adj2)`; `Q4=(wt1 or adj2)`;
`Q6=(wt1 or adj2 or vertex3)`; and `Q8=(wt1 or adj2 or opp2 or vertex3)`.

- Theorem 1. None. No displayed remaining-bit `Q` equals `cov3=220`.
- Theorem 2. `N_max = 2`. For each displayed `Q`, `N_Q` and `N_both`
  are reported in the table.
- Theorem 3. Display. Do not adopt a bit.

Do not write the search into Admissibility. Displayed, not adopted.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The 32 F_cut maps are enumerated by remaining bits and scored exactly by whether all 220 three-site seeds fill. Each displayed remaining-bit Q is tested for cov3=220 iff Q. No physical Admissibility selector is claimed."
trace_class: frontier_discovery
target_claim_id: f_cut_cov3_max_selector_search
target_blocker_text: "whether a displayed remaining-bit predicate equals cov3=220 among the 32 F_cut maps"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the remaining-bit Max(3) selector search; do not adopt a displayed bit"
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
- the displayed remaining-bit candidate list named in Theorem 1.

No observational comparator, literature constant, rate, or generator is
imported. Hamming parity is a contrast map only; it is not `f_L1`.

## Exact target and objects

**Target.** Among the 32 members of `F_cut`, decide whether any displayed
remaining-bit predicate `Q` equals the Max(3) predicate `cov3=220`.

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
`cov3=220` is the Boolean Max(3) predicate.

The displayed candidates `Q` are:

1. each remaining bit: `wt1`, `opp2`, `adj2`, `vertex3`, `mixed3`;
2. every 2-bit AND of remaining bits, in remaining-bit order;
3. every 2-bit OR of remaining bits, in remaining-bit order;
4. `Q_*=(wt1 and adj2)`;
5. `Q4=(wt1 or adj2)`;
6. `Q6=(wt1 or adj2 or vertex3)`;
7. `Q8=(wt1 or adj2 or opp2 or vertex3)`.

`Q_*` coincides with the 2-bit AND `wt1 AND adj2`. `Q4` coincides with
the 2-bit OR `wt1 OR adj2`. Both are displayed as named extras because
the search menu names them.

## Theorems

### Theorem 1 — whether any displayed `Q` equals `cov3=220`

There are exactly 24 proper cube rotations and exactly 10 orbits on
`{0,1}^6`. The three cuts leave `|F_cut|=32`. The unbalanced-axis map
`f_L1` is one element of `F_cut` and is not Hamming parity.

Exhaustive evaluation of all 32 maps on all 220 three-site seeds gives
`N_max = 2` maps with `cov3=220`. Those maps are `f_L1` with remaining
bits `(1, 0, 1, 1, 1)` and `f1` with remaining bits `(1, 1, 1, 1, 1)`.

For each displayed `Q`, write `N_Q` for the number of maps with `Q` true
and `N_both` for the number with both `Q` and `cov3=220`. Then
`cov3=220` iff `Q` if and only if those three counts agree.

None of the displayed predicates satisfies `cov3=220` iff `Q`. There is
therefore no displayed remaining-bit candidate equal to `cov3=220`.

### Theorem 2 — `N_max` and the counts `N_Q`, `N_both`

`N_max = 2`. The table reports `N_Q` and `N_both` for each displayed `Q`.

| `Q` | `N_Q` | `N_max` | `N_both` | `cov3=220` iff `Q` |
|---|---:|---:|---:|---|
| `wt1` | `N_Q = 16` | 2 | 2 | no |
| `opp2` | `N_Q = 16` | 2 | 1 | no |
| `adj2` | `N_Q = 16` | 2 | 2 | no |
| `vertex3` | `N_Q = 16` | 2 | 2 | no |
| `mixed3` | `N_Q = 16` | 2 | 2 | no |
| `wt1 AND opp2` | `N_Q = 8` | 2 | 1 | no |
| `wt1 AND adj2` | `N_Q = 8` | 2 | 2 | no |
| `wt1 AND vertex3` | `N_Q = 8` | 2 | 2 | no |
| `wt1 AND mixed3` | `N_Q = 8` | 2 | 2 | no |
| `opp2 AND adj2` | `N_Q = 8` | 2 | 1 | no |
| `opp2 AND vertex3` | `N_Q = 8` | 2 | 1 | no |
| `opp2 AND mixed3` | `N_Q = 8` | 2 | 1 | no |
| `adj2 AND vertex3` | `N_Q = 8` | 2 | 2 | no |
| `adj2 AND mixed3` | `N_Q = 8` | 2 | 2 | no |
| `vertex3 AND mixed3` | `N_Q = 8` | 2 | 2 | no |
| `wt1 OR opp2` | `N_Q = 24` | 2 | 2 | no |
| `wt1 OR adj2` | `N_Q = 24` | 2 | 2 | no |
| `wt1 OR vertex3` | `N_Q = 24` | 2 | 2 | no |
| `wt1 OR mixed3` | `N_Q = 24` | 2 | 2 | no |
| `opp2 OR adj2` | `N_Q = 24` | 2 | 2 | no |
| `opp2 OR vertex3` | `N_Q = 24` | 2 | 2 | no |
| `opp2 OR mixed3` | `N_Q = 24` | 2 | 2 | no |
| `adj2 OR vertex3` | `N_Q = 24` | 2 | 2 | no |
| `adj2 OR mixed3` | `N_Q = 24` | 2 | 2 | no |
| `vertex3 OR mixed3` | `N_Q = 24` | 2 | 2 | no |
| `Q_*=(wt1 and adj2)` | `N_Q = 8` | 2 | 2 | no |
| `Q4=(wt1 or adj2)` | `N_Q = 24` | 2 | 2 | no |
| `Q6=(wt1 or adj2 or vertex3)` | `N_Q = 28` | 2 | 2 | no |
| `Q8=(wt1 or adj2 or opp2 or vertex3)` | `N_Q = 30` | 2 | 2 | no |

Every 1-bit predicate has `N_Q = 16 ≠ 2`. Every 2-bit AND has
`N_Q = 8 ≠ 2`. Every 2-bit OR has `N_Q = 24 ≠ 2`. `Q_*` has
`N_Q = 8 ≠ 2`. `Q4` has `N_Q = 24 ≠ 2`. `Q6` has `N_Q = 28 ≠ 2`.
`Q8` has `N_Q = 30 ≠ 2`. No displayed count triple can be an iff.

Witnesses include: remaining-bit `(1, 0, 1, 1, 1)` has `cov3=220` but
`opp2=0`, so every `opp2`-AND misses a maximizer; remaining-bit
`(0, 0, 0, 0, 0)` has `cov3=0` but is missed only after the named extras
still include many non-max maps. The two maximizers differ only in
`opp2`, so no 1-bit, no 2-bit AND/OR, and none of `Q_*`, `Q4`, `Q6`,
`Q8` can isolate exactly that pair.

### Theorem 3 — display; do not adopt a bit

The table is displayed. Do not adopt a bit. None of the displayed
predicates is written into Admissibility. The search is a displayed
census of named Boolean combinations of remaining bits, not a selected
physical rule.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice and Admissibility premises | quoted; no edit |
| `F_cut` as the 32 cube-covariant cut maps | enumerated by remaining bits |
| `f_L1` as unbalanced-axis / `n_μ ≠ 0` | defined; Hamming rejected |
| two-cube, 220 three-site seeds, off-patch 0 | declared finite patch |
| `N_max = 2` as `{L1, f1}` with `cov3=220` | proved by exhaustive `cov3` |
| each displayed `Q` versus `cov3=220` | all fail iff; verdict is none |
| 1-bit, 2-bit AND/OR, `Q_*`, `Q4`, `Q6`, `Q8` | displayed, not adopted |
| leftover-character of #6551 | refused; new Max(3) selector |
| physical Admissibility selector | open |

## Boundary and imports

This is a New Max(3) selector search. Investment #6473/#6457 named
Max(3) as `{L1, f1}` with `cov3=220`. Investment #6551 showed that no
remaining bit is constant on the 20 maps with `cov3>0`. The present
count tests a displayed remaining-bit menu against `cov3=220`. Not
leftover-character of #6551: that was a support description of the
positive set, not a Max(3) iff.

Off-patch occupancy `0` is an explicit default on this patch. A blank-block
is a different rule and is not used.

No `Z^3`-wide formation law is claimed. Do not write the search into
Admissibility.

## Promotion value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers whether a displayed remaining-bit `Q` equals `cov3=220` inside `F_cut` on this patch. |
| V2 | Current main has the Max(3) pair and the #6551 support description, but no landed remaining-bit iff search for `cov3=220`. |
| V3 | The 32 maps, 220 seeds, and occupancy-to-lock evolution are independently finite and exact. |
| V4 | The theorem is more than a restatement of Admissibility: it scores a declared finite class. |
| V5 | It is not a physical selector: none, and no bit is adopted. |

## No-Go Discipline gate

The negative content is narrow: none of the displayed remaining-bit
candidates equals `cov3=220` among the 32 `F_cut` maps on this patch.
No global compiler impossibility is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| Hamming parity | identify `f_L1` with `|c|_1 mod 2` | **ATTEMPTED** |
| leftover #6551 support | treat the search as a restatement of bit-constancy on the 20 | **ATTEMPTED** |
| adopt a bit | write a remaining bit into Admissibility | **ATTEMPTED** |
| blank-block off-patch | replace occupancy `0` by a blank-block | **ATTEMPTED** |
| lattice-wide formation | lift the patch census to a `Z^3` formation law | **ATTEMPTED** |
| rename without search | quote `{L1, f1}` without testing the displayed `Q` menu | **ATTEMPTED** |

### N2 — wall independence

The failed 1-bit tests, the failed 2-bit AND/OR tests, the named extras
`Q_*`, `Q4`, `Q6`, `Q8`, the Hamming contrast, and the off-patch
convention are distinct. This note claims no complete wall collection.

### N3 — hidden-condition scan

The two-cube, the 220 triples, off-patch occupancy `0`, occupancy-to-lock
ticks, the `F_cut` remaining-bit order, and the displayed candidate list
are declared. No silent extra bit combination is treated as matching.

### N4 — source residual matching

The live axiom memo supplies `Z^3`, proper cubic rotations, and one covariant
nearest-neighbor rule. The residual answered here is the remaining-bit
selector search for `cov3=220` on the declared patch, a New Max(3)
selector, and not leftover-character of #6551.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | 64 neighbor 6-tuples by axis-type orbit | no continuum occupancy |
| per site | twelve two-cube vertices, same stencil | no privileged site |
| per mode | all 32 `F_cut` maps scored on 220 seeds | no physical law selection |
| per block | each displayed `Q` tested for `cov3=220` iff `Q` | no Admissibility write-in |
| lattice wide | checked and not executed | no `Z^3`-wide formation law |

### N6 — live partial-closure paths

Live routes include a different Boolean combination of remaining bits, a
different seed family, a different off-patch rule, and any independently
derived physical map from `F_cut` into Admissibility.

### N7 — hostile steelman

**Steelman:** Max(3) is already `{L1, f1}`, so a 1-bit, a 2-bit AND/OR,
`Q_*`, `Q4`, `Q6`, or `Q8` must recover `cov3=220`.

**Answer:** Every 1-bit has `N_Q = 16 ≠ 2`. Every 2-bit AND has
`N_Q = 8 ≠ 2`. Every 2-bit OR has `N_Q = 24 ≠ 2`. `Q_*` has `N_Q = 8`,
`Q4` has `N_Q = 24`, `Q6` has `N_Q = 28`, and `Q8` has `N_Q = 30`.
None.

### N8 — cross-cycle echo

Investment #6551 already showed that no remaining bit is constant on the
20 maps with `cov3>0`. Echoing that support description is not a
substitute for testing the displayed menu against `cov3=220`. The
present search is a New Max(3) selector.

No-Go Discipline disposition: **PASS** for the finite search and the
narrow none verdict. FAIL / DO NOT SHIP for “a displayed remaining-bit
candidate selects `cov3=220`” or “a displayed `Q` is the physical rule.”

## Live parent quotes

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

> There is one fixed nearest-neighbor admissibility rule, covariant under lattice
> translations and proper cubic rotations.

> A site with no record cannot be read.

## Runner contract

The companion runner enumerates the 32 `F_cut` maps, scores `cov3` on the
220 three-site seeds, tests each displayed remaining-bit `Q` for
`cov3=220` iff `Q`, reports `N_max = 2` and the pair `{L1, f1}`, and
reports that the verdict is none. Declared audit inputs are this note
and the axiom memo; the runner writes no cache and authors no audit
verdict.
