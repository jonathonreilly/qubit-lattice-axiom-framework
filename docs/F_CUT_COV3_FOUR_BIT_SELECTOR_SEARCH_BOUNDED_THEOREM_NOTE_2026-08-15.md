---
claim_id: f_cut_cov3_four_bit_selector_search_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Among the 32 F_cut maps on the two-cube with off-patch o=0, whether any displayed 4-bit remaining-bit AND or OR equals cov3>0 is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_cov3_four_bit_selector_search_2026_08_15.py
---

# Four-Bit Remaining-Bit Selector Search For Positive 3-Site Coverage

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact occupancy-to-lock 3-site fillability on the twelve-vertex
two-cube with off-patch occupancy `0`, for the thirty-two cube-covariant
cut maps `F_cut`, tested against every AND of four remaining bits and
every OR of four remaining bits.
**Audit-status authority:** independent audit lane only. This note writes no
audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_cov3_four_bit_selector_search_2026_08_15.py`](../scripts/f_cut_cov3_four_bit_selector_search_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result up front

Investment #6514 showed that no 1-bit remaining-bit predicate and no
`wt1`-AND-bit predicate equals `cov3>0`. Investment #6524 showed
no 3-bit AND/OR, and not P/Q4/Q1, equals `cov3>0`. Residual is the
4-bit menu: every AND of four remaining bits and every OR of four
remaining bits. New bit-width after the 3-bit menu failed. This note
completes that menu. It is not a Max(3) rename.

`F_cut` is the cube-covariant class of `{0,1}`-valued maps on the six
nearest-neighbor occupancy bits with `f(empty)=f(full)=0` and `f(c)=f(1-c)`.
It has five free remaining bits and size 32. Remaining bits are ordered as
`(wt1, opp2, adj2, vertex3, mixed3)`.

`f_L1(c)=1` if and only if some axis is unbalanced: the signed pair
`n_μ = c_{+μ} − c_{-μ}` is nonzero. This is **not** Hamming parity
`|c|_1 mod 2`. The remaining-bit tuple of `f_L1` is `(1, 0, 1, 1, 1)`.

On the two-cube with off-patch occupancy `0`, write
`cov3(f)` for the number of unordered 3-site seeds from which `f` fills.
There are ten displayed candidates: the five 4-bit ANDs and the five
4-bit ORs.

- Theorem 1. For each displayed 4-bit `Q`, `cov3>0` iff `Q` fails.
  None. Reconfirm #6524: no 3-bit AND/OR, and not P/Q4/Q1. `N_pos = 20`.
- Theorem 2. For each displayed `Q`, `N_Q`, `N_pos`, `N_both`. Every
  4-bit AND has `N_Q = 2`, `N_pos = 20`, `N_both = 2`. Every 4-bit OR
  has `N_Q = 30`, `N_pos = 20`, `N_both = 20`.
- Theorem 3. Display. Do not adopt a bit.

Do not write the search into Admissibility. Displayed, not adopted.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The 32 F_cut maps are enumerated by remaining bits and scored exactly by whether any of the 220 three-site seeds fills. Each displayed 4-bit remaining-bit Q is tested for cov3>0 iff Q. No physical Admissibility selector is claimed."
trace_class: frontier_discovery
target_claim_id: f_cut_cov3_four_bit_selector_search
target_blocker_text: "whether a displayed 4-bit remaining-bit AND or OR equals cov3>0 among the 32 F_cut maps"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the 4-bit remaining-bit selector search; do not adopt a displayed bit"
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
- the displayed 4-bit remaining-bit candidate list named in Theorem 1.

No observational comparator, literature constant, rate, or generator is
imported. Hamming parity is a contrast map only; it is not `f_L1`.

## Exact target and objects

**Target.** Among the 32 members of `F_cut`, decide whether any displayed
4-bit remaining-bit AND or OR `Q` equals the fillability predicate `cov3>0`.

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

The displayed candidates `Q` are:

1. every AND of four remaining bits, in remaining-bit order;
2. every OR of four remaining bits, in remaining-bit order.

This list is the new bit-width after the 3-bit menu failed. The 3-bit
AND/OR predicates and the named extras `P`, `Q4=(wt1 or adj2)`, and
`Q1=(wt1 and adj2)` are not re-adopted; they are only reconfirmed as
non-matches.

## Theorems

### Theorem 1 — each displayed 4-bit `Q` versus `cov3>0`

There are exactly 24 proper cube rotations and exactly 10 orbits on
`{0,1}^6`. The three cuts leave `|F_cut|=32`. The unbalanced-axis map
`f_L1` is one element of `F_cut` and is not Hamming parity.

Exhaustive evaluation of all 32 maps on all 220 three-site seeds gives
`N_pos = 20` maps with `cov3>0`. For each displayed 4-bit `Q`,
`cov3>0` iff `Q` fails. None.

Reconfirm #6524: no 3-bit AND/OR, and not P/Q4/Q1, equals `cov3>0`.
For the control `P`, `N_P = 14` and `N_both = 13`.

### Theorem 2 — `N_Q`, `N_pos`, `N_both` for each displayed `Q`

For each displayed `Q`, write `N_Q` for the number of maps with `Q` true
and `N_both` for the number with both `Q` and `cov3>0`. Then
`cov3>0` iff `Q` if and only if those three counts agree.

| `Q` | `N_Q` | `N_pos` | `N_both` | `cov3>0` iff `Q` |
|---|---:|---:|---:|---|
| `wt1 AND opp2 AND adj2 AND vertex3` | `N_Q = 2` | 20 | 2 | no |
| `wt1 AND opp2 AND adj2 AND mixed3` | `N_Q = 2` | 20 | 2 | no |
| `wt1 AND opp2 AND vertex3 AND mixed3` | `N_Q = 2` | 20 | 2 | no |
| `wt1 AND adj2 AND vertex3 AND mixed3` | `N_Q = 2` | 20 | 2 | no |
| `opp2 AND adj2 AND vertex3 AND mixed3` | `N_Q = 2` | 20 | 2 | no |
| `wt1 OR opp2 OR adj2 OR vertex3` | `N_Q = 30` | 20 | 20 | no |
| `wt1 OR opp2 OR adj2 OR mixed3` | `N_Q = 30` | 20 | 20 | no |
| `wt1 OR opp2 OR vertex3 OR mixed3` | `N_Q = 30` | 20 | 20 | no |
| `wt1 OR adj2 OR vertex3 OR mixed3` | `N_Q = 30` | 20 | 20 | no |
| `opp2 OR adj2 OR vertex3 OR mixed3` | `N_Q = 30` | 20 | 20 | no |

Every 4-bit AND has `N_Q = 2 ≠ 20` and `N_both = 2`. Every 4-bit OR has
`N_Q = 30 ≠ 20` and `N_both = 20`. No displayed count triple can be an iff.
There is therefore no displayed 4-bit remaining-bit AND or OR equals
`cov3>0`.

Witnesses include: remaining-bit `(0,0,1,1,0)` has `cov3=24>0` but every
4-bit AND is false; `(0,0,0,1,0)` has `cov3=0` but
`wt1 OR opp2 OR adj2 OR vertex3` is true; `(1,0,0,0,0)` has `cov3=0` but
is in every 4-bit OR that contains `wt1`.

### Theorem 3 — display; do not adopt a bit

The table is displayed. Do not adopt a bit. None of the ten predicates is
written into Admissibility. The search is a displayed census of named
Boolean combinations of remaining bits, not a selected physical rule and
not a Max(3) rename.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice and Admissibility premises | quoted; no edit |
| `F_cut` as the 32 cube-covariant cut maps | enumerated by remaining bits |
| `f_L1` as unbalanced-axis / `n_μ ≠ 0` | defined; Hamming rejected |
| two-cube, 220 three-site seeds, off-patch 0 | declared finite patch |
| `N_pos = 20` and #6524 3-bit leftover | proved by exhaustive `cov3` |
| each displayed 4-bit `Q` versus `cov3>0` | all ten fail iff; none |
| each displayed `Q` reports `N_Q`, `N_pos`, `N_both` | proved; displayed, not adopted |
| new bit-width after the 3-bit menu failed | completed; not a Max(3) rename |
| physical Admissibility selector | open |

## Boundary and imports

New bit-width after the 3-bit menu failed: #6524 showed no 3-bit AND/OR,
and not P/Q4/Q1, equals `cov3>0`, and left the 4-bit ANDs and 4-bit ORs
untested as a block. The present count tests that displayed list. The note
is not a Max(3) rename: no maximum of `cov3` is reported as a selector, and
`f_L1` is used only as the unbalanced-axis control.

Off-patch occupancy `0` is an explicit default on this patch. A blank-block
is a different rule and is not used.

No `Z^3`-wide formation law is claimed. Do not write the search into
Admissibility.

## Promotion value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers whether any displayed 4-bit remaining-bit AND or OR `Q` equals `cov3>0` inside `F_cut` on this patch. |
| V2 | Current main has the failed 3-bit search (#6524) but no landed 4-bit remaining-bit search for `cov3>0`. |
| V3 | The 32 maps, 220 seeds, and occupancy-to-lock evolution are independently finite and exact. |
| V4 | The theorem is more than a restatement of Admissibility: it scores a declared finite class. |
| V5 | It is not a physical selector: none match, and no bit is adopted. |

## No-Go Discipline gate

The negative content is narrow: none of the ten displayed 4-bit remaining-bit
AND or OR candidates equals `cov3>0` among the 32 `F_cut` maps on this
patch. No global compiler impossibility is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| Hamming parity | identify `f_L1` with `|c|_1 mod 2` | **ATTEMPTED** |
| leftover 3-bit menu | treat the search as a restatement of the failed 3-bit AND/OR and P/Q4/Q1 tests | **ATTEMPTED** |
| Max(3) rename | replace the fillability search by a maximum-`cov3` ranking | **ATTEMPTED** |
| adopt a bit | write a remaining bit into Admissibility | **ATTEMPTED** |
| blank-block off-patch | replace occupancy `0` by a blank-block | **ATTEMPTED** |
| lattice-wide formation | lift the patch census to a `Z^3` formation law | **ATTEMPTED** |

### N2 — wall independence

The failed 3-bit AND/OR and P/Q4/Q1 tests, the ten failed 4-bit tests, the
Hamming contrast, and the off-patch convention are distinct. This note claims
no complete wall collection.

### N3 — hidden-condition scan

The two-cube, the 220 triples, off-patch occupancy `0`, occupancy-to-lock
ticks, the `F_cut` remaining-bit order, and the displayed 4-bit candidate
list are declared. No silent extra bit combination is treated as matching.

### N4 — source residual matching

The live axiom memo supplies `Z^3`, proper cubic rotations, and one covariant
nearest-neighbor rule. The residual answered here is the 4-bit remaining-bit
selector search for `cov3>0` on the declared patch, a new bit-width after
the 3-bit menu failed, and not a Max(3) rename.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | 64 neighbor 6-tuples by axis-type orbit | no continuum occupancy |
| per site | twelve two-cube vertices, same stencil | no privileged site |
| per mode | all 32 `F_cut` maps scored on 220 seeds | no physical law selection |
| per block | each displayed 4-bit `Q` tested for `cov3>0` iff `Q` | no Admissibility write-in |
| lattice wide | checked and not executed | no `Z^3`-wide formation law |

### N6 — live partial-closure paths

Live routes include a different Boolean combination of remaining bits, a
different seed family, a different off-patch rule, and any independently
derived physical map from `F_cut` into Admissibility.

### N7 — hostile steelman

**Steelman:** #6524 already ruled out 3-bit AND/OR, `P`, `Q4`, and `Q1`, so
a 4-bit AND or a 4-bit OR must recover `cov3>0`.

**Answer:** Every 4-bit AND has `N_Q = 2 ≠ 20`. Every 4-bit OR has
`N_Q = 30 ≠ 20`. None.

### N8 — cross-cycle echo

Investment #6524 already showed no 3-bit AND/OR, and not P/Q4/Q1, equals
`cov3>0`. Echoing that failure is not a substitute for testing the 4-bit
menu that investment left open. The present search is a new bit-width after
the 3-bit menu failed.

No-Go Discipline disposition: **PASS** for the finite search and the
narrow none verdict. FAIL / DO NOT SHIP for “a 4-bit remaining-bit
AND or OR selects `cov3>0`” or “a displayed `Q` is the physical rule.”

## Live parent quotes

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

> There is one fixed nearest-neighbor admissibility rule, covariant under lattice
> translations and proper cubic rotations.

> A site with no record cannot be read.

## Runner contract

The companion runner enumerates the 32 `F_cut` maps, scores `cov3` on the
220 three-site seeds, tests each displayed 4-bit remaining-bit AND or OR
`Q` for `cov3>0` iff `Q`, reports `N_Q`, `N_pos`, and `N_both` for each
displayed `Q`, reconfirms `N_pos = 20` and the #6524 leftover that no
3-bit AND/OR and not P/Q4/Q1 equals `cov3>0`, and reports that none match.
Declared audit inputs are this note and the axiom memo; the runner writes
no cache and authors no audit verdict.
