---
claim_id: f_cut_cov4_positive_selector_search_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Among the 32 F_cut maps on the two-cube with off-patch o=0, whether any displayed remaining-bit candidate equals cov4>0 is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_cov4_positive_selector_search_2026_08_15.py
---

# Remaining-Bit Search For A Selector Equal To `cov4>0`

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact occupancy-to-lock 4-site fill positivity on the
twelve-vertex two-cube with off-patch occupancy `0`, scored for the
thirty-two cube-covariant cut maps `F_cut`, against a displayed menu of
remaining-bit candidates.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_cov4_positive_selector_search_2026_08_15.py`](../scripts/f_cut_cov4_positive_selector_search_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result up front

Investment #6509 showed that `cov4>0` is not `P`. Every `P`-true map has
`cov4>0` (`N_both = 14`), but positivity is larger (`N_pos = 24`). The ten
extras are the two `#6490` exceptions together with the eight maps that have
`wt1 = 0` and `adj2 = 1`. This note searches a displayed remaining-bit
predicate `Q` such that `cov4>0` if and only if `Q`, on the same 32 maps.

`F_cut` is the cube-covariant class of `{0,1}`-valued maps on the six
nearest-neighbor occupancy bits with `f(empty)=f(full)=0` and `f(c)=f(1-c)`.
It has five free remaining bits and size 32. Remaining bits are ordered as
`(wt1, opp2, adj2, vertex3, mixed3)`.

`f_L1(c)=1` if and only if some axis is unbalanced: the signed pair
`n_μ = c_{+μ} − c_{-μ}` is nonzero. This is **not** Hamming parity
`|c|_1 mod 2`. `f_L1` is the 10-orbit reading `n ≠ 0`, not Hamming. Its
remaining-bit tuple is `(1, 0, 1, 1, 1)`.

The selector `P` is the remaining-bit predicate

```text
P := (wt1 = 1) and (adj2, vertex3, mixed3) ≠ (0, 0, 0).
```

The displayed candidate menu is:

- each remaining bit, as a standalone `{0,1}` predicate;
- `wt1` AND each other remaining bit;
- `P` itself;
- `adj2` alone;
- `wt1` OR `adj2`.

**Theorem 1.** For each candidate `Q` in that menu, whether
`cov4(f)>0` if and only if `Q(f)` holds on all 32 maps is decided by
exhaustive scoring. Exactly one candidate succeeds.

**Theorem 2.** The unique matching candidate is

```text
Q_* := (wt1 = 1) or (adj2 = 1).
```

No other menu entry equals `cov4>0`. In particular `P` fails: ten
`P`-false maps have `cov4>0`.

**Theorem 3.** The matching bit formula is displayed only. Do not adopt a
bit. Do not write `Q_*` into Admissibility.

Displayed, not adopted.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The 32 F_cut maps are enumerated by remaining bits and scored exactly on the 495 four-site seeds. Each displayed remaining-bit candidate is compared to cov4>0. The unique match is a finite Boolean identity on this patch, not a physical Admissibility selector."
trace_class: frontier_discovery
target_claim_id: f_cut_cov4_positive_selector_search
target_blocker_text: "whether any displayed remaining-bit candidate equals cov4>0 among the 32 F_cut maps"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the bounded selector search; do not adopt the matching bit formula"
conditional_surface_status: "exact for occupancy-to-lock on the twelve-vertex two-cube with off-patch occupancy 0; no Z^3-wide formation law"
hypothetical_axiom_status: "not proposed; no axiom or approved primitive is added"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Current premise boundary

The only scientific dependency is the current four-axiom authority linked
above. The Lattice and Admissibility premises are quoted from
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md):

Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
adjacency, standard translations, and proper cubic rotations about each site.

There is one fixed nearest-neighbor admissibility rule, covariant under lattice
translations and proper cubic rotations.

For each site, the probability distribution over the possibilities is
determined by, and varies with, the nearest-neighbor conditions.

The axiom memo says the distribution concerns which possibility a forming
record locks, conditional on formation at that site; it does not supply the
formation site, probability, or rate.

The current Record boundary is:

Records form.

When present, a record locks exactly one admissible local possibility.

A readout value is determined by record content alone.

A site with no record cannot be read.

Record supplies no formation-site selector and no occupancy-to-lock
predicate. The candidates below are displayed remaining-bit formulas, not
axiom content.

## Exact objects

The two-cube is `T = {0,1,2} × {0,1} × {0,1}` (twelve vertices). Off-patch
occupancy `0` is the explicit default: a neighbor of a site in `T` that is
not itself in `T` is treated as unoccupied. A blank-block is a different
rule and is not used.

A configuration `c ∈ {0,1}^6` is a six-tuple of neighbor occupancies in
direction order `(+x,-x,+y,-y,+z,-z)`. Axis type is
`(n_unbalanced, n_both, n_empty)`, where an axis is unbalanced if its two
bits differ, both if both bits are 1, and empty if both bits are 0.
Complement swaps `n_both` with `n_empty`. The five remaining bits of
`F_cut`, in the order `(wt1, opp2, adj2, vertex3, mixed3)`, are the values
on orbit types `(1,0,2)`, `(0,1,2)`, `(2,0,1)`, `(3,0,0)`, `(1,1,1)`.
Complement partners are forced equal; empty and full are fixed at 0. Thus
`N_free = 5` and `|F_cut| = 32`.

Occupancy-to-lock: from a locked set `L ⊂ T`, a site `x ∈ T \ L` locks at
the next tick if and only if `f` of its six-neighbor occupancy (off-patch
entries 0) equals 1. The map `f` fills from a seed `S` if iterating this
rule from `L_0 = S` reaches `L = T` in at most 13 ticks.

The four-site seeds are the `C(12,4) = 495` subsets of size 4 in `T`. Then
`cov4(f)` is the number of those subsets from which `f` fills. The boolean
scored here is `cov4(f)>0`.

`P` and the menu candidates are functions of the remaining-bit tuple only.

## Theorem 1 — each candidate versus `cov4>0`

Direct evolution on the 495 four-site seeds scores every `F_cut` map.
`N_pos = 24`, `N_P = 14`, and `N_both = 14`. Every `P`-true map has
`cov4>0`. The eight maps with `wt1 = 0` and `adj2 = 0` are exactly the
maps with `cov4 = 0`. The ten extras (`P` false, `cov4>0`) are:

- the two `#6490` exceptions `(1, 0, 0, 0, 0)` and `(1, 1, 0, 0, 0)`,
  each with `cov4 = 7`;
- the eight maps with `wt1 = 0` and `adj2 = 1`.

Thus `cov4>0` properly contains `P`. `f_L1` itself has `cov4 = 489`.

For each displayed candidate `Q`, the identity `cov4>0 ⇔ Q` on all 32
maps is:

| candidate `Q` | `cov4>0` iff `Q` | mismatch |
|---|---|---|
| `wt1` | no | eight `wt1=0`, `adj2=1` maps have `cov4>0` |
| `opp2` | no | both false positives and false negatives |
| `adj2` | no | eight `adj2=0` maps with `wt1=1` have `cov4>0` |
| `vertex3` | no | both false positives and false negatives |
| `mixed3` | no | both false positives and false negatives |
| `wt1` AND `opp2` | no | sixteen false negatives |
| `wt1` AND `adj2` | no | sixteen false negatives |
| `wt1` AND `vertex3` | no | sixteen false negatives |
| `wt1` AND `mixed3` | no | sixteen false negatives |
| `P` | no | ten extras; `P` fails |
| `adj2` alone | no | same eight `adj2=0`, `wt1=1` extras as standalone `adj2` |
| `wt1` OR `adj2` | yes | none; twenty-four true, eight false |

`P` fails. Standalone bits fail. Every `wt1` AND other-bit product fails.
`adj2` alone fails.

## Theorem 2 — the unique matching candidate

Exactly one menu entry works. Name it:

```text
Q_* = (wt1 = 1) ∨ (adj2 = 1).
```

It holds on precisely the twenty-four maps with `cov4>0` and on no other
`F_cut` map. Equivalently, on this patch a four-site seed can fill only
when the displayed remaining bits turn on the weight-1 orbit or the
adjacent-pair orbit (or both).

If the menu had contained no match, the report would have been that no
candidate matches. That counterfactual is false: one candidate matches,
and it is `wt1` OR `adj2`.

## Theorem 3 — display, not adoption

`Q_*` is displayed data. Do not adopt a bit. Do not adopt `P`. Do not
adopt `f_L1`. Do not write `Q_*` into Admissibility. Admissibility does
not name this remaining-bit formula.

The identity `cov4>0 ⇔ (wt1 ∨ adj2)` is a finite fact about occupancy-to-lock
on this two-cube with off-patch `o=0`. It is not a physical formation-site
selector and not an axiom edit.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record wording | quoted; no edit |
| `F_cut` as the 32 cube-covariant cut maps | enumerated by remaining bits |
| `f_L1` as unbalanced-axis / `n ≠ 0` | defined; Hamming rejected |
| two-cube, 495 four-site seeds, off-patch `o=0` | declared finite patch |
| each remaining bit versus `cov4>0` | none matches |
| `wt1` AND each other bit versus `cov4>0` | none matches |
| `P` versus `cov4>0` | fails; ten extras |
| `adj2` alone | does not match |
| unique matching name | `Q_* = wt1 ∨ adj2` |
| leftover-character of #6509 | refused; that was `cov4>0` is not `P` |
| adoption of a bit | refused |
| physical Admissibility selector | open |

## Boundary and imports

Not leftover-character of #6509: that note showed `cov4>0` is not `P`.
The present object is a search among remaining-bit formulas for a
replacement that *does* equal positivity.

The two `#6490` exceptions enter only as two of the ten extras already
counted by that positivity census. They are not a second seed-family
ranking.

Off-patch occupancy `0` is an explicit default on this patch. A
blank-block is a different rule and is not used.

No observation, fit, continuum limit, or Hamming-as-`f_L1`
identification is imported. No `Z^3`-wide formation law is claimed.

## Promotion value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers whether any displayed remaining-bit candidate equals `cov4>0` on the 32 `F_cut` maps. |
| V2 | Current main has the axiom memo and the #6509 fact that positivity is not `P`, but no landed remaining-bit search for a matching `Q`. |
| V3 | The 32 maps, 495 seeds, and Boolean candidates are independently finite and exact. |
| V4 | The theorem is more than restating Admissibility: it scores a declared finite class against a declared candidate menu. |
| V5 | The matching formula is displayed, not adopted, and is not written into Admissibility. |

## No-Go Discipline gate

The negative content is narrow: `P` is not `cov4>0`, standalone remaining
bits are not `cov4>0`, and a displayed match is not axiom content. No
global compiler impossibility is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| Hamming parity | identify `f_L1` with `|c|_1 mod 2` | **ATTEMPTED** |
| leftover of #6509 | treat the search as restating that `cov4>0` is not `P` | **ATTEMPTED** |
| rename `P` | identify `Q_*` with `P` | **ATTEMPTED** |
| adopt the matching bit | write `wt1 ∨ adj2` into Admissibility | **ATTEMPTED** |
| blank-block off-patch | replace occupancy `0` by a blank-block | **ATTEMPTED** |
| lattice-wide formation | lift the patch identity to a `Z^3` formation law | **ATTEMPTED** |

### N2 — wall independence

The failed `P` extra, the Hamming contrast, the `#6490` pair, and the
off-patch convention are distinct. This note claims no complete wall
collection.

### N3 — hidden-condition scan

The two-cube, the 495 four-site seeds, off-patch occupancy `0`,
occupancy-to-lock ticks, the `F_cut` remaining-bit order, and the
candidate menu are declared. Unique selection of `f_L1` is not silently
assumed.

### N4 — source residual matching

The live axiom memo supplies `Z^3`, proper cubic rotations, and one
covariant nearest-neighbor rule. The residual answered here is whether any
displayed remaining-bit candidate equals `cov4>0` on this patch, not
leftover-character of #6509.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | 64 neighbor 6-tuples by axis-type orbit | no continuum occupancy |
| per site | twelve two-cube vertices, same stencil | no privileged site |
| per mode | all 32 `F_cut` maps scored on 495 seeds and the displayed menu | no physical law selection |
| per block | the unique matching formula on this patch | no Admissibility write-in |
| lattice wide | checked and not executed | no `Z^3`-wide formation law |

### N6 — live partial-closure paths

Live routes include a different seed family, a different off-patch rule,
a selector outside the displayed remaining-bit menu, and any
independently derived physical map from `F_cut` into Admissibility.

### N7 — hostile steelman

**Steelman:** Every `P`-true map already has `cov4>0`, so positivity is
just `P`, or else just `adj2`, and no new selector exists.

**Answer:** Ten `P`-false maps have `cov4>0`, so positivity is not `P`.
Eight maps have `adj2 = 0` and still `cov4>0`, so positivity is not
`adj2` alone. The remaining-bit formula `wt1 ∨ adj2` equals positivity
exactly, and it is displayed, not adopted.

### N8 — cross-cycle echo

Investment #6509 already showed that `cov4>0` is not `P`. Investment
#6490 named the two `wt1=1`, `cov2=0` exceptions. Echoing either fact is
not a substitute for testing the remaining-bit menu against 4-site
positivity.

No-Go Discipline disposition: **PASS** for the finite candidate census
and the unique matching name. FAIL / DO NOT SHIP for “adopt a bit,”
“`P` equals `cov4>0`,” or “`Q_*` is the physical rule.”

## Live parent quotes

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

> There is one fixed nearest-neighbor admissibility rule, covariant under lattice
> translations and proper cubic rotations.

> A site with no record cannot be read.

## Runner contract

The companion runner enumerates the 32 `F_cut` maps, scores `cov4` on the
495 four-site seeds, tests every displayed remaining-bit candidate
against `cov4>0`, reconfirms that `P` fails, names `wt1` OR `adj2` as the
unique match, and checks that no bit is adopted. Declared
audit inputs are this note and the axiom memo; the runner writes no cache
and authors no audit verdict.
