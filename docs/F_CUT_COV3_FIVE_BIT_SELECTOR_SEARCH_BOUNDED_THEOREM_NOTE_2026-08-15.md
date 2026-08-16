---
claim_id: f_cut_cov3_five_bit_selector_search_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Among the 32 F_cut maps on the two-cube with off-patch o=0, whether the 5-bit remaining-bit AND or the 5-bit OR equals cov3>0 is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_cov3_five_bit_selector_search_2026_08_15.py
---

# Five-Bit Remaining-Bit Selector Search For Positive 3-Site Coverage

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact occupancy-to-lock 3-site fillability on the twelve-vertex
two-cube with off-patch occupancy `0`, for the thirty-two cube-covariant
cut maps `F_cut`, tested against the AND of all five remaining bits and
the OR of all five remaining bits.
**Audit-status authority:** independent audit lane only. This note writes no
audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_cov3_five_bit_selector_search_2026_08_15.py`](../scripts/f_cut_cov3_five_bit_selector_search_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result up front

Investment #6514 showed that no 1-bit remaining-bit predicate and no
`wt1`-AND-bit predicate equals `cov3>0`. Investment #6524 showed
no 3-bit AND/OR, and not P/Q4/Q1, equals `cov3>0`. Investment p3bit4:
no 4-bit AND/OR equals `cov3>0`. Residual is the 5-bit menu: the AND
of all five remaining bits and the OR of all five remaining bits.
Last remaining-bit width for cov3>0. This note completes that menu.
It is not a Max(3) rename.

`F_cut` is the cube-covariant class of `{0,1}`-valued maps on the six
nearest-neighbor occupancy bits with `f(empty)=f(full)=0` and `f(c)=f(1-c)`.
It has five free remaining bits and size 32. Remaining bits are ordered as
`(wt1, opp2, adj2, vertex3, mixed3)`.

`f_L1(c)=1` if and only if some axis is unbalanced: the signed pair
`n_μ = c_{+μ} − c_{-μ}` is nonzero. This is **not** Hamming parity
`|c|_1 mod 2`. The remaining-bit tuple of `f_L1` is `(1, 0, 1, 1, 1)`.

On the two-cube with off-patch occupancy `0`, write
`cov3(f)` for the number of unordered 3-site seeds from which `f` fills.
There are two displayed candidates:

- `Q_and5 := wt1∧opp2∧adj2∧vertex3∧mixed3`
  (`wt1 AND opp2 AND adj2 AND vertex3 AND mixed3`);
- `Q_or5 := wt1∨opp2∨adj2∨vertex3∨mixed3`
  (`wt1 OR opp2 OR adj2 OR vertex3 OR mixed3`).

- Theorem 1. Whether `cov3>0` iff `Q_and5`, and whether `cov3>0` iff
  `Q_or5`. Both fail. None. Reconfirm p3bit4: no 4-bit AND/OR equals
  `cov3>0`. `N_pos = 20`.
- Theorem 2. For each, `N_Q`, `N_pos`, `N_both`. `Q_and5` has
  `N_Q = 1`, `N_pos = 20`, `N_both = 1`. `Q_or5` has `N_Q = 31`,
  `N_pos = 20`, `N_both = 20`.
- Theorem 3. Display. Do not adopt a bit.

Do not write the search into Admissibility. Displayed, not adopted.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The 32 F_cut maps are enumerated by remaining bits and scored exactly by whether any of the 220 three-site seeds fills. Q_and5 and Q_or5 are each tested for cov3>0 iff Q. No physical Admissibility selector is claimed."
trace_class: frontier_discovery
target_claim_id: f_cut_cov3_five_bit_selector_search
target_blocker_text: "whether the 5-bit remaining-bit AND or the 5-bit OR equals cov3>0 among the 32 F_cut maps"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the 5-bit remaining-bit selector search; do not adopt a displayed bit"
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
- the displayed 5-bit remaining-bit candidates `Q_and5` and `Q_or5` named
  in Theorem 1.

No observational comparator, literature constant, rate, or generator is
imported. Hamming parity is a contrast map only; it is not `f_L1`.

## Exact target and objects

**Target.** Among the 32 members of `F_cut`, decide whether the displayed
5-bit remaining-bit AND `Q_and5` or the displayed 5-bit remaining-bit OR
`Q_or5` equals the fillability predicate `cov3>0`.

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

1. `Q_and5`, the AND of all five remaining bits;
2. `Q_or5`, the OR of all five remaining bits.

This list is the last remaining-bit width for cov3>0 after the 4-bit menu
failed. The 4-bit AND/OR predicates are not re-adopted; they are only
reconfirmed as non-matches.

## Theorems

### Theorem 1 — `Q_and5` and `Q_or5` versus `cov3>0`

There are exactly 24 proper cube rotations and exactly 10 orbits on
`{0,1}^6`. The three cuts leave `|F_cut|=32`. The unbalanced-axis map
`f_L1` is one element of `F_cut` and is not Hamming parity.

Exhaustive evaluation of all 32 maps on all 220 three-site seeds gives
`N_pos = 20` maps with `cov3>0`. For `Q_and5`, `cov3>0` iff `Q` fails.
For `Q_or5`, `cov3>0` iff `Q` fails. None.

Reconfirm p3bit4: no 4-bit AND/OR equals `cov3>0`.
For the control `P`, `N_P = 14` and `N_both = 13`.

### Theorem 2 — `N_Q`, `N_pos`, `N_both` for each displayed `Q`

For each displayed `Q`, write `N_Q` for the number of maps with `Q` true
and `N_both` for the number with both `Q` and `cov3>0`. Then
`cov3>0` iff `Q` if and only if those three counts agree.

| `Q` | `N_Q` | `N_pos` | `N_both` | `cov3>0` iff `Q` |
|---|---:|---:|---:|---|
| `Q_and5` = `wt1 AND opp2 AND adj2 AND vertex3 AND mixed3` | `N_Q = 1` | 20 | 1 | no |
| `Q_or5` = `wt1 OR opp2 OR adj2 OR vertex3 OR mixed3` | `N_Q = 31` | 20 | 20 | no |

`Q_and5` has `N_Q = 1 ≠ 20` and `N_both = 1`. `Q_or5` has
`N_Q = 31 ≠ 20` and `N_both = 20`. No displayed count triple can be an iff.
There is therefore no displayed 5-bit remaining-bit AND or OR equals
`cov3>0`.

Witnesses include: remaining-bit `(0,0,1,1,0)` has `cov3=24>0` but
`Q_and5` is false; `(0,0,0,0,0)` has `cov3=0` and is the unique map with
`Q_or5` false; `(1,0,0,0,0)` has `cov3=0` but `Q_or5` is true.

### Theorem 3 — display; do not adopt a bit

The table is displayed. Do not adopt a bit. Neither predicate is
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
| `N_pos = 20` and p3bit4 4-bit leftover | proved by exhaustive `cov3` |
| `Q_and5` and `Q_or5` versus `cov3>0` | both fail iff; none |
| each displayed `Q` reports `N_Q`, `N_pos`, `N_both` | proved; displayed, not adopted |
| last remaining-bit width for cov3>0 | completed; not a Max(3) rename |
| physical Admissibility selector | open |

## Boundary and imports

Last remaining-bit width for cov3>0: p3bit4 showed no 4-bit AND/OR
equals `cov3>0`, and left the AND of all five remaining bits and the OR
of all five remaining bits untested as a block. The present count tests
that displayed list. The note is not a Max(3) rename: no maximum of
`cov3` is reported as a selector, and `f_L1` is used only as the
unbalanced-axis control.

Off-patch occupancy `0` is an explicit default on this patch. A blank-block
is a different rule and is not used.

No `Z^3`-wide formation law is claimed. Do not write the search into
Admissibility.

## Promotion value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers whether the displayed 5-bit remaining-bit AND `Q_and5` or OR `Q_or5` equals `cov3>0` inside `F_cut` on this patch. |
| V2 | Current main has the failed 4-bit search (p3bit4) but no landed 5-bit remaining-bit search for `cov3>0`. |
| V3 | The 32 maps, 220 seeds, and occupancy-to-lock evolution are independently finite and exact. |
| V4 | The theorem is more than a restatement of Admissibility: it scores a declared finite class. |
| V5 | It is not a physical selector: none match, and no bit is adopted. |

## No-Go Discipline gate

The negative content is narrow: neither of the two displayed 5-bit remaining-bit
AND or OR candidates equals `cov3>0` among the 32 `F_cut` maps on this
patch. No global compiler impossibility is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| Hamming parity | identify `f_L1` with `|c|_1 mod 2` | **ATTEMPTED** |
| leftover 4-bit menu | treat the search as a restatement of the failed 4-bit AND/OR tests | **ATTEMPTED** |
| Max(3) rename | replace the fillability search by a maximum-`cov3` ranking | **ATTEMPTED** |
| adopt a bit | write a remaining bit into Admissibility | **ATTEMPTED** |
| blank-block off-patch | replace occupancy `0` by a blank-block | **ATTEMPTED** |
| lattice-wide formation | lift the patch census to a `Z^3` formation law | **ATTEMPTED** |

### N2 — wall independence

The failed 4-bit AND/OR tests, the two failed 5-bit tests, the
Hamming contrast, and the off-patch convention are distinct. This note claims
no complete wall collection.

### N3 — hidden-condition scan

The two-cube, the 220 triples, off-patch occupancy `0`, occupancy-to-lock
ticks, the `F_cut` remaining-bit order, and the displayed 5-bit candidates
`Q_and5` and `Q_or5` are declared. No silent extra bit combination is treated
as matching.

### N4 — source residual matching

The live axiom memo supplies `Z^3`, proper cubic rotations, and one covariant
nearest-neighbor rule. The residual answered here is the 5-bit remaining-bit
selector search for `cov3>0` on the declared patch, the last remaining-bit
width for cov3>0 after the 4-bit menu failed, and not a Max(3) rename.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | 64 neighbor 6-tuples by axis-type orbit | no continuum occupancy |
| per site | twelve two-cube vertices, same stencil | no privileged site |
| per mode | all 32 `F_cut` maps scored on 220 seeds | no physical law selection |
| per block | `Q_and5` and `Q_or5` tested for `cov3>0` iff `Q` | no Admissibility write-in |
| lattice wide | checked and not executed | no `Z^3`-wide formation law |

### N6 — live partial-closure paths

Live routes include a different Boolean combination of remaining bits, a
different seed family, a different off-patch rule, and any independently
derived physical map from `F_cut` into Admissibility.

### N7 — hostile steelman

**Steelman:** p3bit4 already ruled out every 4-bit AND and every 4-bit OR,
so the 5-bit AND or the 5-bit OR must recover `cov3>0`.

**Answer:** `Q_and5` has `N_Q = 1 ≠ 20`. `Q_or5` has
`N_Q = 31 ≠ 20`. None.

### N8 — cross-cycle echo

Investment p3bit4 already showed no 4-bit AND/OR equals `cov3>0`. Echoing
that failure is not a substitute for testing the 5-bit menu that investment
left open. The present search is the last remaining-bit width for cov3>0.

No-Go Discipline disposition: **PASS** for the finite search and the
narrow none verdict. FAIL / DO NOT SHIP for “a 5-bit remaining-bit
AND or OR selects `cov3>0`” or “a displayed `Q` is the physical rule.”

## Live parent quotes

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

> There is one fixed nearest-neighbor admissibility rule, covariant under lattice
> translations and proper cubic rotations.

> A site with no record cannot be read.

## Runner contract

The companion runner enumerates the 32 `F_cut` maps, scores `cov3` on the
220 three-site seeds, tests `Q_and5` and `Q_or5` for `cov3>0` iff `Q`,
reports `N_Q`, `N_pos`, and `N_both` for each displayed `Q`, reconfirms
`N_pos = 20` and the p3bit4 leftover that no 4-bit AND/OR equals
`cov3>0`, and reports that none match.
Declared audit inputs are this note and the axiom memo; the runner writes
no cache and authors no audit verdict.
