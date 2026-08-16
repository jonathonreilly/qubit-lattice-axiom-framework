---
claim_id: f_cut_cov8_positive_q8_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Among the 32 F_cut maps on the two-cube with off-patch o=0, whether positive 8-site coverage is equivalent to (wt1=1) or (adj2=1) or (opp2=1) or (vertex3=1) is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_cov8_positive_q8_2026_08_15.py
---

# Whether `cov8>0` Equals Displayed `Q8`

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact occupancy-to-lock fill positivity on the twelve-vertex two-cube
with off-patch occupancy `0`, scored on the 495 eight-site seeds, for the
thirty-two cube-covariant cut maps `F_cut`, against displayed `Q8`.
**Audit-status authority:** independent audit lane only. This note authors no audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_cov8_positive_q8_2026_08_15.py`](../scripts/f_cut_cov8_positive_q8_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result up front

Investment #6531 showed that `cov6>0` equals
`Q6 := (wt1=1) or (adj2=1) or (vertex3=1)`. Investment #6527 / the
`cov8=0` pair named the two maps with `cov8=0` as remaining-bit tuples
`(0, 0, 0, 0, 0)` and `(0, 0, 0, 0, 1)`. The 2-bit / `Q4 ∨ vertex3`
menu, which is `Q6` at `k=8`, failed to equal `cov8>0`. This note tests
the displayed remaining-bit predicate

```text
Q8(f) := (wt1 = 1) or (adj2 = 1) or (opp2 = 1) or (vertex3 = 1)
```

New k-selector after the 2-bit/Q4∨vertex3 menu failed, not
leftover-character of #6531, not leftover-character of #6527, and not a
rename of that failed menu.

`F_cut` is the cube-covariant class of `{0,1}`-valued maps on the six
nearest-neighbor occupancy bits with `f(empty)=f(full)=0` and `f(c)=f(1-c)`.
It has five free remaining bits and size 32. Remaining bits are ordered as
`(wt1, opp2, adj2, vertex3, mixed3)`. Thus `|F_cut| = 32`.

`f_L1(c)=1` if and only if some axis is unbalanced: the signed pair
`n_μ = c_{+μ} − c_{-μ}` is nonzero. This is **not** Hamming parity
`|c|_1 mod 2`. `f_L1` is the 10-orbit reading `n ≠ 0`, not Hamming. Its
remaining-bit tuple is `(1, 0, 1, 1, 1)`.

On the two-cube with off-patch occupancy `0`, write
`cov8(f) = |{S : |S|=8 and f fills from S}|`. Then:

- Theorem 1. `cov8(f) > 0` if and only if `Q8(f)` among the 32 maps.
  There is no counterexample.
- Theorem 2. `N_Q8 = 30`, `N_pos = 30`, `N_both = 30`.
- Theorem 3. `Q8` is displayed. Displayed, not adopted. Do not adopt a
  bit.

Do not adopt `Q8`. Do not write `Q8` into Admissibility.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The 32 F_cut maps are enumerated by remaining bits and scored exactly on the 495 eight-site seeds of the two-cube. Whether cov8>0 equals Q8, and the counts N_Q8, N_pos, N_both, are finite exact facts. No physical Admissibility selector is claimed."
trace_class: frontier_discovery
target_claim_id: f_cut_cov8_positive_q8
target_blocker_text: "whether cov8>0 equals Q8 among the 32 F_cut maps after the 2-bit/Q4∨vertex3 menu failed"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the bounded 8-site positivity-versus-Q8 comparison; do not adopt the displayed predicate Q8"
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
predicate. `Q8` is a displayed remaining-bit formula, not axiom content.

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

The eight-site seeds are the `C(12,8) = 495` subsets of size 8 in `T`. Then
`cov8(f)` is the number of those subsets from which `f` fills. The boolean
scored here is `cov8(f)>0`.

The displayed remaining-bit predicate is

```text
Q8(f) := (wt1 = 1) or (adj2 = 1) or (opp2 = 1) or (vertex3 = 1).
```

Mixed3 is free in `Q8`. Displayed, not adopted.

## Theorem 1 — `cov8>0` iff `Q8`

Enumerate all 32 remaining-bit tuples of `F_cut` and score `cov8` on the 495
eight-site seeds. Then `cov8(f) > 0` if and only if `Q8(f)`. There is no
lex-first counterexample.

The two maps with `cov8 = 0` are exactly the maps with `wt1 = 0`,
`opp2 = 0`, `adj2 = 0`, and `vertex3 = 0`:

- `(0, 0, 0, 0, 0)`
- `(0, 0, 0, 0, 1)`

Those two are exactly the `Q8`-false maps, and they are the #6527 /
`cov8=0` pair. The two maps that broke `Q6` / `Q4 ∨ vertex3` at `k=8`
are the `Q6`-false maps with `opp2 = 1`, and they are `Q8`-true with
positive coverage:

- `(0, 1, 0, 0, 0)` with `cov8 = 1`
- `(0, 1, 0, 0, 1)` with `cov8 = 1`

## Theorem 2 — `N_Q8`, `N_pos`, `N_both`

Among the 32 maps:

- `N_Q8 = 30` maps satisfy `Q8`;
- `N_pos = 30` maps have `cov8 > 0`;
- `N_both = 30` maps satisfy both.

Every `Q8`-true map has `cov8 > 0`, and every map with `cov8 > 0` is
`Q8`-true. `f_L1`, with remaining bits `(1, 0, 1, 1, 1)`, satisfies `Q8`
and has `cov8 = 494`.

## Theorem 3 — display; do not adopt a bit

`Q8` is the remaining-bit predicate obtained by adjoining `opp2` to the
`Q6` / `Q4 ∨ vertex3` menu that failed at `k=8`. On this patch it equals
8-site positivity. Displayed, not adopted. Do not adopt a bit. Do not
adopt `Q8`. Do not write `Q8` into Admissibility.

The identity `cov8>0 ⇔ Q8` is a finite fact about occupancy-to-lock on
this two-cube with off-patch `o=0`. It is not a physical formation-site
selector and not an axiom edit.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record wording | quoted; no edit |
| `F_cut` as the 32 cube-covariant cut maps | enumerated by remaining bits |
| `f_L1` as unbalanced-axis / `n ≠ 0` | defined; Hamming rejected |
| two-cube, 495 eight-site seeds, off-patch `o=0` | declared finite patch |
| `Q8` as `(wt1=1) or (adj2=1) or (opp2=1) or (vertex3=1)` | displayed, not adopted |
| `cov8>0` iff `Q8` | holds; no counterexample |
| `N_Q8 = 30`, `N_pos = 30`, `N_both = 30` | proved by exhaustive scoring |
| leftover-character of #6531 | refused; new k-selector after the 2-bit/Q4∨vertex3 menu failed |
| leftover-character of #6527 | refused; the zero pair is used only as the `Q8`-false class |
| adoption of a bit | refused |
| physical Admissibility selector | open |

## Boundary and imports

Not leftover-character of #6531: that closed `cov6>0` iff `Q6` at
`k=6`. Not leftover-character of #6527: that named the two `cov8=0`
maps. The present object is whether displayed four-disjunct `Q8` equals
8-site positivity after the 2-bit/Q4∨vertex3 menu failed.

The two #6527 zeros enter only as the `Q8`-false maps. They are not a
second seed-family ranking.

Off-patch occupancy `0` is an explicit default on this patch. A blank-block
is a different rule and is not used.

No observation, fit, continuum limit, or Hamming-as-`f_L1`
identification is imported. No `Z^3`-wide formation law is claimed.
Do not write `Q8` into Admissibility.

## Promotion value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers whether 8-site positivity equals displayed `Q8` inside `F_cut` on this patch. |
| V2 | Current main has the axiom memo, the #6531 `Q6` identity at `k=6`, and the #6527 `cov8=0` pair, but no landed 8-site positivity-versus-`Q8` comparison. |
| V3 | The 32 maps, 495 seeds, and displayed `Q8` are independently finite and exact. |
| V4 | The theorem is more than restating Admissibility: it scores a declared finite class against displayed `Q8`. |
| V5 | Equivalence with `Q8` holds on this patch, and displayed `Q8` is not adopted and is not written into Admissibility. |

## No-Go Discipline gate

The negative content is narrow: displayed `Q8` is not axiom content. No
global compiler impossibility is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| Hamming parity | identify `f_L1` with `|c|_1 mod 2` | **ATTEMPTED** |
| leftover of #6531 | treat the identity as leftover-character of `cov6>0` iff `Q6` | **ATTEMPTED** |
| leftover of #6527 | treat the identity as leftover-character of the `cov8=0` pair | **ATTEMPTED** |
| leftover of the failed menu | treat `Q8` as leftover-character of the 2-bit/Q4∨vertex3 menu | **ATTEMPTED** |
| adopt `Q8` | write `(wt1=1) or (adj2=1) or (opp2=1) or (vertex3=1)` into Admissibility | **ATTEMPTED** |
| blank-block off-patch | replace occupancy `0` by a blank-block | **ATTEMPTED** |

### N2 — wall independence

The Hamming contrast, the #6531 `Q6` identity, the #6527 zero pair, the
failed 2-bit / `Q4 ∨ vertex3` menu, and the off-patch convention are
distinct. This note claims no complete wall collection.

### N3 — hidden-condition scan

The two-cube, the 495 eight-site seeds, off-patch occupancy `0`,
occupancy-to-lock ticks, the `F_cut` remaining-bit order, and displayed
`Q8` are declared. Unique selection of `f_L1` is not silently assumed.

### N4 — source residual matching

The live axiom memo supplies `Z^3`, proper cubic rotations, and one covariant
nearest-neighbor rule. The residual answered here is whether 8-site
positivity equals `Q8` on the declared patch, not leftover-character of
#6531, not leftover-character of #6527, and not leftover-character of
the 2-bit/Q4∨vertex3 menu.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | 64 neighbor 6-tuples by axis-type orbit | no continuum occupancy |
| per site | twelve two-cube vertices, same stencil | no privileged site |
| per mode | all 32 `F_cut` maps scored on 495 seeds | no physical law selection |
| per block | `N_Q8`, `N_pos`, and `N_both` on this patch | no Admissibility write-in |
| lattice wide | checked and not executed | no `Z^3`-wide formation law |

### N6 — live partial-closure paths

Live routes include a different seed family, a different off-patch rule, a
selector other than `Q8` or `cov8>0`, and any independently derived physical
map from `F_cut` into Admissibility.

### N7 — hostile steelman

**Steelman:** #6527 already named the two `cov8=0` maps, so positivity at
`k=8` is just “not those two,” and adjoining `opp2` to failed `Q6` is a
rename, not a new selector.

**Answer:** The 2-bit / `Q4 ∨ vertex3` menu failed: `Q6` is true on
twenty-eight maps while thirty maps have `cov8>0`. The two extras are
exactly `opp2=1` with the other remaining bits zero. Displayed `Q8`
equals positivity on this patch, and it is not adopted.

### N8 — cross-cycle echo

Investment #6531 already showed that `cov6>0` iff `Q6`. Investment #6527
already named the `cov8=0` pair. Echoing either fact is not a substitute
for testing `Q8` against eight-site positivity after the
2-bit/Q4∨vertex3 menu failed.

No-Go Discipline disposition: **PASS** for the finite comparison.
FAIL / DO NOT SHIP for “adopt a bit” or “displayed `Q8` is the physical
rule.”

## Live parent quotes

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

> There is one fixed nearest-neighbor admissibility rule, covariant under lattice
> translations and proper cubic rotations.

> A site with no record cannot be read.

## Runner contract

The companion runner enumerates the 32 `F_cut` maps, scores `cov8` on the
495 eight-site seeds, compares positivity with displayed `Q8`, reports that
there is no counterexample, and reports `N_Q8 = 30`, `N_pos = 30`, and
`N_both = 30`. Declared audit inputs are this note and the axiom memo; the
runner writes no cache and authors no audit verdict.
