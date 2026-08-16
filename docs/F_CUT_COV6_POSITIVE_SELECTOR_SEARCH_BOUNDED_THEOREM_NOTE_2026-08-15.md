---
claim_id: f_cut_cov6_positive_selector_search_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Among the 32 F_cut maps on the two-cube with off-patch o=0, whether positive 6-site coverage is equivalent to (wt1=1) or (adj2=1) or (vertex3=1) is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_cov6_positive_selector_search_2026_08_15.py
---

# Remaining-Bit Search For A Selector Equal To `cov6>0`

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact occupancy-to-lock fill positivity on the twelve-vertex two-cube
with off-patch occupancy `0`, scored on the 924 six-site seeds, for the
thirty-two cube-covariant cut maps `F_cut`, against displayed `Q6` and a
menu of one-bit and `wt1`-AND remaining-bit candidates.
**Audit-status authority:** independent audit lane only. This note authors no audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_cov6_positive_selector_search_2026_08_15.py`](../scripts/f_cut_cov6_positive_selector_search_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result up front

Investment #6526 showed that `cov6>0` is not `Q4`. That census had
`N_Q4 = 24`, `N_pos = 28`, `N_both = 24`. Every `Q4`-true map has
`cov6>0`, and the four extras are exactly the `Q4`-false maps with
`vertex3 = 1`. This note tests the displayed remaining-bit predicate

```text
Q6(f) := (wt1 = 1) or (adj2 = 1) or (vertex3 = 1)
```

and searches every standalone remaining bit and every `wt1` AND other
remaining bit. New k-selector after `Q4` failed at `k=6`, not
leftover-character of #6526 and not a rename of that mismatch.

`F_cut` is the cube-covariant class of `{0,1}`-valued maps on the six
nearest-neighbor occupancy bits with `f(empty)=f(full)=0` and `f(c)=f(1-c)`.
It has five free remaining bits and size 32. Remaining bits are ordered as
`(wt1, opp2, adj2, vertex3, mixed3)`. Thus `|F_cut| = 32`.

`f_L1(c)=1` if and only if some axis is unbalanced: the signed pair
`n_μ = c_{+μ} − c_{-μ}` is nonzero. This is **not** Hamming parity
`|c|_1 mod 2`. `f_L1` is the 10-orbit reading `n ≠ 0`, not Hamming. Its
remaining-bit tuple is `(1, 0, 1, 1, 1)`.

On the two-cube with off-patch occupancy `0`, write
`cov6(f) = |{S : |S|=6 and f fills from S}|`. Then:

- Theorem 1. `cov6(f) > 0` if and only if `Q6(f)` among the 32 maps.
  There is no counterexample. No standalone remaining bit equals
  `cov6>0`. No `wt1` AND other remaining bit equals `cov6>0`.
- Theorem 2. `N_Q6 = 28`, `N_pos = 28`, `N_both = 28`.
- Theorem 3. `Q6` is displayed. Displayed, not adopted. Do not adopt a
  bit.

Do not adopt `Q6`. Do not write `Q6` into Admissibility.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The 32 F_cut maps are enumerated by remaining bits and scored exactly on the 924 six-site seeds of the two-cube. Whether cov6>0 equals Q6, and whether any 1-bit or wt1-AND-bit equals cov6>0, are finite exact facts. No physical Admissibility selector is claimed."
trace_class: frontier_discovery
target_claim_id: f_cut_cov6_positive_selector_search
target_blocker_text: "whether cov6>0 equals Q6, or any 1-bit or wt1-AND remaining-bit formula, among the 32 F_cut maps"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the bounded 6-site positivity-versus-Q6 comparison; do not adopt the displayed predicate Q6"
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
predicate. `Q6` is a displayed remaining-bit formula, not axiom content.

## Exact objects

The two-cube is `T = {0,1,2} × {0,1} × {0,1}` (twelve vertices). Off-patch
occupancy `0` is the explicit default: a neighbor of a site in `T` that is
not itself in `T` is treated as unoccupied. A blank-block is a different rule and is not used.

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

The six-site seeds are the `C(12,6) = 924` subsets of size 6 in `T`. Then
`cov6(f)` is the number of those subsets from which `f` fills. The boolean
scored here is `cov6(f)>0`.

The displayed remaining-bit predicate is

```text
Q6(f) := (wt1 = 1) or (adj2 = 1) or (vertex3 = 1).
```

Opp2 and mixed3 are free in `Q6`. The displayed one-bit menu is each
remaining bit as a standalone `{0,1}` predicate. The displayed
`wt1`-AND menu is `wt1` AND each other remaining bit. Displayed, not
adopted.

## Theorem 1 — `cov6>0` iff `Q6`; no 1-bit or `wt1`-AND match

Enumerate all 32 remaining-bit tuples of `F_cut` and score `cov6` on the 924
six-site seeds. Then `cov6(f) > 0` if and only if `Q6(f)`. There is no
lex-first counterexample.

The four maps with `cov6 = 0` are exactly the maps with `wt1 = 0`,
`adj2 = 0`, and `vertex3 = 0`:

- `(0, 0, 0, 0, 0)`
- `(0, 0, 0, 0, 1)`
- `(0, 1, 0, 0, 0)`
- `(0, 1, 0, 0, 1)`

Those four are exactly the `Q6`-false maps. The four #6526 extras that
broke `Q4` at `k=6` are the `Q4`-false maps with `vertex3 = 1`, and they
are `Q6`-true with positive coverage:

- `(0, 0, 0, 1, 0)` with `cov6 = 4`
- `(0, 0, 0, 1, 1)` with `cov6 = 12`
- `(0, 1, 0, 1, 0)` with `cov6 = 20`
- `(0, 1, 0, 1, 1)` with `cov6 = 28`

No standalone remaining bit equals `cov6>0`. No `wt1` AND other remaining
bit equals `cov6>0`.

| candidate `Q` | `cov6>0` iff `Q` | mismatch |
|---|---|---|
| `Q6` | yes | none |
| `wt1` | no | twelve `wt1=0` maps still have `cov6>0` |
| `opp2` | no | both false positives and false negatives |
| `adj2` | no | twelve `adj2=0` maps still have `cov6>0` |
| `vertex3` | no | twelve `vertex3=0` maps still have `cov6>0` |
| `mixed3` | no | both false positives and false negatives |
| `wt1` AND `opp2` | no | twenty false negatives |
| `wt1` AND `adj2` | no | twenty false negatives |
| `wt1` AND `vertex3` | no | twenty false negatives |
| `wt1` AND `mixed3` | no | twenty false negatives |

## Theorem 2 — `N_Q6`, `N_pos`, `N_both`

Among the 32 maps:

- `N_Q6 = 28` maps satisfy `Q6`;
- `N_pos = 28` maps have `cov6 > 0`;
- `N_both = 28` maps satisfy both.

Every `Q6`-true map has `cov6 > 0`, and every map with `cov6 > 0` is
`Q6`-true. `f_L1`, with remaining bits `(1, 0, 1, 1, 1)`, satisfies `Q6`
and has `cov6 = 920`.

## Theorem 3 — display; do not adopt a bit

`Q6` is the remaining-bit predicate obtained by adjoining `vertex3` to
the `Q4` that failed at `k=6`. On this patch it equals 6-site positivity.
Displayed, not adopted. Do not adopt a bit. Do not adopt `Q6`. Do not
write `Q6` into Admissibility.

The identity `cov6>0 ⇔ Q6` is a finite fact about occupancy-to-lock on
this two-cube with off-patch `o=0`. It is not a physical formation-site
selector and not an axiom edit.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record wording | quoted; no edit |
| `F_cut` as the 32 cube-covariant cut maps | enumerated by remaining bits |
| `f_L1` as unbalanced-axis / `n ≠ 0` | defined; Hamming rejected |
| two-cube, 924 six-site seeds, off-patch `o=0` | declared finite patch |
| `Q6` as `(wt1=1) or (adj2=1) or (vertex3=1)` | displayed, not adopted |
| `cov6>0` iff `Q6` | holds; no counterexample |
| each remaining bit versus `cov6>0` | none matches |
| `wt1` AND each other bit versus `cov6>0` | none matches |
| `N_Q6 = 28`, `N_pos = 28`, `N_both = 28` | proved by exhaustive scoring |
| leftover-character of #6526 | refused; new k-selector after `Q4` failed at `k=6` |
| adoption of a bit | refused |
| physical Admissibility selector | open |

## Boundary and imports

Not leftover-character of #6526: that closed `cov6>0` is not `Q4`, with
`N_Q4 = 24`, `N_pos = 28`, `N_both = 24`. The present object is whether
the displayed three-disjunct `Q6`, or any 1-bit or `wt1`-AND formula,
equals that same positivity.

The four #6526 extras enter only as the `vertex3 = 1` maps that `Q4`
missed. They are not a second seed-family ranking.

Off-patch occupancy `0` is an explicit default on this patch. A blank-block
is a different rule and is not used.

No observation, fit, continuum limit, or Hamming-as-`f_L1`
identification is imported. No `Z^3`-wide formation law is claimed.
Do not write `Q6` into Admissibility.

## Promotion value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers whether 6-site positivity equals displayed `Q6`, and whether any 1-bit or `wt1`-AND formula does, inside `F_cut` on this patch. |
| V2 | Current main has the axiom memo and the #6526 fact that `cov6>0` is not `Q4`, but no landed 6-site positivity-versus-`Q6` search. |
| V3 | The 32 maps, 924 seeds, and remaining-bit candidates are independently finite and exact. |
| V4 | The theorem is more than restating Admissibility: it scores a declared finite class against displayed `Q6` and the 1-bit / `wt1`-AND menu. |
| V5 | Equivalence with `Q6` holds on this patch, and displayed `Q6` is not adopted and is not written into Admissibility. |

## No-Go Discipline gate

The negative content is narrow: no 1-bit or `wt1`-AND remaining-bit
formula equals `cov6>0`, and displayed `Q6` is not axiom content. No
global compiler impossibility is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| Hamming parity | identify `f_L1` with `|c|_1 mod 2` | **ATTEMPTED** |
| leftover of #6526 | treat the search as leftover-character of `cov6>0` is not `Q4` | **ATTEMPTED** |
| standalone remaining bit | identify `cov6>0` with one remaining bit | **ATTEMPTED** |
| `wt1` AND other bit | identify `cov6>0` with a `wt1` product | **ATTEMPTED** |
| adopt `Q6` | write `(wt1=1) or (adj2=1) or (vertex3=1)` into Admissibility | **ATTEMPTED** |
| blank-block off-patch | replace occupancy `0` by a blank-block | **ATTEMPTED** |

### N2 — wall independence

The failed 1-bit identities, the Hamming contrast, the #6526 `Q4`
mismatch, and the off-patch convention are distinct. This note claims no
complete wall collection.

### N3 — hidden-condition scan

The two-cube, the 924 six-site seeds, off-patch occupancy `0`,
occupancy-to-lock ticks, the `F_cut` remaining-bit order, displayed
`Q6`, and the 1-bit / `wt1`-AND menu are declared. Unique selection of
`f_L1` is not silently assumed.

### N4 — source residual matching

The live axiom memo supplies `Z^3`, proper cubic rotations, and one covariant
nearest-neighbor rule. The residual answered here is whether 6-site
positivity equals `Q6` or any 1-bit / `wt1`-AND formula on the declared
patch, not leftover-character of #6526.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | 64 neighbor 6-tuples by axis-type orbit | no continuum occupancy |
| per site | twelve two-cube vertices, same stencil | no privileged site |
| per mode | all 32 `F_cut` maps scored on 924 seeds | no physical law selection |
| per block | `N_Q6`, `N_pos`, and `N_both` on this patch | no Admissibility write-in |
| lattice wide | checked and not executed | no `Z^3`-wide formation law |

### N6 — live partial-closure paths

Live routes include a different seed family, a different off-patch rule, a
selector other than `Q6` or `cov6>0`, and any independently derived physical
map from `F_cut` into Admissibility.

### N7 — hostile steelman

**Steelman:** #6526 already showed that positivity at `k=6` is just
`Q4` plus the four `vertex3=1` extras, so either a 1-bit or `Q4` itself
already selects, and no new formula is needed.

**Answer:** `Q4` fails: twenty-four maps satisfy `Q4` while twenty-eight
have `cov6>0`. No standalone remaining bit and no `wt1` AND other bit
equals positivity. The displayed three-disjunct `Q6` does equal
positivity on this patch, and it is not adopted.

### N8 — cross-cycle echo

Investment #6526 already showed that `cov6>0` is not `Q4`. Echoing that
mismatch is not a substitute for testing `Q6` and the 1-bit / `wt1`-AND
menu against the same six-site positivity.

No-Go Discipline disposition: **PASS** for the finite comparison and the
narrow 1-bit / `wt1`-AND failure. FAIL / DO NOT SHIP for “adopt a bit”
or “displayed `Q6` is the physical rule.”

## Live parent quotes

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

> There is one fixed nearest-neighbor admissibility rule, covariant under lattice
> translations and proper cubic rotations.

> A site with no record cannot be read.

## Runner contract

The companion runner enumerates the 32 `F_cut` maps, scores `cov6` on the
924 six-site seeds, compares positivity with displayed `Q6`, reports that
there is no counterexample, reports that no 1-bit or `wt1`-AND formula
equals `cov6>0`, and reports `N_Q6 = 28`, `N_pos = 28`, and
`N_both = 28`. Declared audit inputs are this note and the axiom memo; the
runner writes no cache and authors no audit verdict.
