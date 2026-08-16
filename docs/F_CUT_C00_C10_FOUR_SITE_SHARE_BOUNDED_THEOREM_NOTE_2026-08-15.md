---
claim_id: f_cut_c00_c10_four_site_share_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On the two-cube with off-patch o=0, whether the 7 four-site fills of F_cut (1,0,0,0,0) and (1,1,0,0,0) are the same set is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_c00_c10_four_site_share_2026_08_15.py
---

# Four-Site Fill Sets Of `F_cut` `(1,0,0,0,0)` And `(1,1,0,0,0)` Are Equal

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** displayed occupancy-to-lock dynamics of the cube-covariant
maps `F_cut` remaining bits `(1, 0, 0, 0, 0)` and `(1, 1, 0, 0, 0)` on
the twelve-vertex two-cube `{0,1,2}×{0,1}×{0,1}`, scored on all `495`
four-site seeds, with off-patch occupancy identically `0`. Whether the
two 7-sets of four-site fills are the same set is reported. Displayed,
not adopted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_c00_c10_four_site_share_2026_08_15.py`](../scripts/f_cut_c00_c10_four_site_share_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

Write the two-cube as the twelve sites `{0,1,2}×{0,1}×{0,1}`. A site
locks when a displayed predicate of its six-neighbor occupancy tuple
returns `1`. Off-patch neighbors contribute occupancy `0`. A
blank-block is a different rule; it is not used. A run is the tuple of
lock-set cardinalities from the seed through halt, together with the
fill bit `|locks_halt|=12`.

Let `f_L1(c)=1` if and only if some axis is unbalanced: `c_{+μ} ≠ c_{-μ}`
for at least one `μ ∈ {x,y,z}`. Equivalently, some discrete neighbor
contrast `n_μ = c_{+μ} − c_{-μ}` is nonzero. This is **not** Hamming parity
`|c|_1 mod 2`. `f_L1` is the 10-orbit reading `n ≠ 0`, not Hamming.

Let `f00` and `f10` be the `F_cut` remaining-bit maps

```text
f00 = (wt1, opp2, adj2, vertex3, mixed3) = (1, 0, 0, 0, 0)
f10 = (wt1, opp2, adj2, vertex3, mixed3) = (1, 1, 0, 0, 0)
```

with complements forced. They disagree on `opp2`. `#6493` scored
`cov4(f00) = 7`. `#6506` scored `cov4(f10) = 7`. `#6507` reported that
both maps fill the `#6493` face. The object of this note is whether the
two 7-sets are the same set.

This is the first share-test of the exception pair at `k=4`. It is not
leftover of L1/f0 share. Not leftover-character of the L1/f0 share
(that compared miss sets of `f_L1` and `f0=(1,1,1,1,0)`).

Write `M00` (resp. `M10`) for the set of unordered 4-site seeds from
which `f00` (resp. `f10`) fills.

**Theorem 1.** `|M00| = 7` and `|M10| = 7` among the `495` four-site
seeds. This reconfirms `#6493` and `#6506`. The `#6493` face is in both
sets.

**Theorem 2.** `|M00 ∩ M10| = 7`. Therefore `M00 = M10`. The equality
bit is `1`.

**Theorem 3.** The cardinals, the intersection, and the equality bit are
displayed only. Do not adopt a bit. Do not adopt either map. Do not
write a remaining bit into Admissibility. Do not list all seven.

Displayed, not adopted.

## Current Premise Boundary

The Lattice and Admissibility premises are quoted from
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md):

Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
adjacency, standard translations, and proper cubic rotations about each site.

For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.

Admissibility is not a dynamics axiom.

The only use of those sentences is to name the cubic nearest-neighbor
graph and to keep formation outside the axiom. The axiom memo says the
distribution concerns which possibility a forming record locks,
conditional on formation; it does not supply the formation site, probability, or rate.

The current Record boundary is:

When present, a record locks exactly one admissible local possibility.

A readout value is determined by record content alone.

A site with no record cannot be read.

Record supplies no formation-site selector and no occupancy-to-lock
predicate. The maps `f00` and `f10` are supplied displayed members, not
axiom content. A remaining-bit tuple is likewise displayed data, not an
admissibility rule.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Finite exact 4-site fill-set share of two displayed F_cut occupancy-to-lock maps on a twelve-vertex two-cube."
trace_class: frontier_discovery
target_claim_id: f_cut_c00_c10_four_site_share
target_blocker_text: "whether the 7 four-site fills of F_cut (1,0,0,0,0) and (1,1,0,0,0) are the same set"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the bounded 4-site fill-set share; do not adopt either map or a remaining bit"
conditional_surface_status: "exact on the two-cube with off-patch o=0 for |S|=4; the maps and bits remain displayed"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

Sites of the two-cube, in lexicographic order:

`(0,0,0)`, `(0,0,1)`, `(0,1,0)`, `(0,1,1)`,
`(1,0,0)`, `(1,0,1)`, `(1,1,0)`, `(1,1,1)`,
`(2,0,0)`, `(2,0,1)`, `(2,1,0)`, `(2,1,1)`.

The six-neighbor tuple at a site is ordered
`(+x,-x,+y,-y,+z,-z)`. Each coordinate is the occupancy of that
neighbor: `1` if the neighbor is an on-patch lock, else `0`. Every
off-patch neighbor is `0`. The off-patch occupancy `0` is the explicit
default.

For each axis, the pair of opposite bits is

- unbalanced if the bits are `{0,1}`,
- both if the bits are `{1,1}`,
- empty if the bits are `{0,0}`.

Write `(n_unbalanced, n_both, n_empty)` with sum `3`. Representative
orbits used below:

| name | type | representative |
|---|---|---|
| empty | `(0,0,3)` | `(0,0,0,0,0,0)` |
| wt1 | `(1,0,2)` | `(1,0,0,0,0,0)` |
| opp2 | `(0,1,2)` | `(1,1,0,0,0,0)` |
| adj2 | `(2,0,1)` | `(1,0,1,0,0,0)` |
| type210 | `(2,1,0)` | `(1,1,1,0,0,1)` |
| vertex3 | `(3,0,0)` | `(1,0,1,0,1,0)` |
| mixed3 | `(1,1,1)` | `(1,0,1,1,0,0)` |
| wt5 | `(1,2,0)` | `(1,1,1,1,1,0)` |
| opp2c | `(0,2,1)` | `(1,1,1,1,0,0)` |
| full | `(0,3,0)` | `(1,1,1,1,1,1)` |

`F_cut` is the cube-covariant class with `f(empty)=f(full)=0` and
`f(c)=f(1-c)`. Five remaining bits stay free, so `|F_cut|=32`. Those
bits are ordered `(wt1, opp2, adj2, vertex3, mixed3)`.

`f_L1(c)=1` iff `n_unbalanced(c)≥1`. Its remaining-bit tuple is
`(1,0,1,1,1)`.
`f00(c)=1` iff the axis type is `wt1=(1,0,2)` or `wt5=(1,2,0)`. Its
remaining-bit tuple is `(1, 0, 0, 0, 0)`.
`f10(c)=1` iff the axis type is `wt1=(1,0,2)`, `opp2=(0,1,2)`,
`wt5=(1,2,0)`, or `opp2c=(0,2,1)`. Its remaining-bit tuple is
`(1, 1, 0, 0, 0)`.

On those representatives the bits are

| map | wt1 | opp2 | adj2 | type210 | vertex3 | mixed3 | empty | full | wt5 | opp2c |
|---|---|---|---|---|---|---|---|---|---|---|
| `f_L1` | 1 | 0 | 1 | 1 | 1 | 1 | 0 | 0 | 1 | 0 |
| `f00` | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 |
| `f10` | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 |

Hamming parity of `|c|_1` is a different predicate: `opp2` is even and
`f_L1(opp2)=0`, while `f10(opp2)=1`.

One tick locks every currently unlocked on-patch site whose neighbor
tuple has `f=1`. The process starts with `locks_0=S` and halts at the
first fixed point, or at tick `12`. Lock history is the sequence of
cardinalities from `t=0` through halt. Fill means `|locks_halt|=12`.

Seeds of size `4` are the `C(12,4)=495` unordered 4-subsets of the
two-cube. `M00` is the set of those seeds from which `f00` fills.
`M10` is the set of those seeds from which `f10` fills. The `#6493`
face is the entire `x=0` slice
`{(0,0,0),(0,0,1),(0,1,0),(0,1,1)}`. Do not list all seven.

## Theorem 1 — `|M00| = 7` and `|M10| = 7`

Among the `495` four-site seeds, exactly seven fill under `f00` and
exactly seven fill under `f10`.

So `|M00| = 7` and `|M10| = 7`. This reconfirms the coverage scores of
`#6493` and `#6506`. The `#6493` face is a member of both sets; from
that face both maps have history `(4, 8, 12)` and fill, which
reconfirms `#6507`.

The coincidence of scores is not yet an identification of the two
fill sets. The maps disagree on `opp2`. The new object is the share
of the two 7-sets.

## Theorem 2 — `|M00 ∩ M10| = 7` and `M00 = M10`

The intersection of the two fill sets has seven members. Combined with
Theorem 1 this is `M00 = M10`. The equality bit is `1`.

Set equality of the four-site fillers is not map identity. `f10` fires
on `opp2` and `f00` does not. On this two-cube at seed size `4`, that
remaining-bit difference does not produce a four-site fill that one
map has and the other lacks.

## Theorem 3 — display; do not adopt a bit

The integers `|M00| = 7`, `|M10| = 7`, `|M00 ∩ M10| = 7`, and the
equality bit `1` are displayed data. Do not adopt a bit. Do not adopt
`f00`. Do not adopt `f10`. Do not write a remaining bit into
Admissibility. The remaining-bit tuples `(1, 0, 0, 0, 0)` and
`(1, 1, 0, 0, 0)` are not written into Admissibility. Do not list all
seven.

## Exact Target And Obligation Graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record wording | quoted; no edit |
| two-cube, off-patch `o=0`, all `495` four-site seeds | declared finite data |
| `|M00|` and `|M10|` | both `7` |
| `|M00 ∩ M10|` and set equality | `7`; `M00 = M10` |
| identity of the two maps | refused; they disagree on `opp2` |
| leftover of the L1/f0 share | refused; different maps and fill vs miss |
| adoption of either map or a remaining bit | refused |
| formation site / rate from the axioms | open |

## Boundary And Imports

No observation, fit, continuum limit, or Hamming-as-`f_L1`
identification is imported. The two-cube, the predicates `f00` and
`f10`, and the four-site seed list are supplied mathematical data for
this note. Record lock language is quoted only as the existing
lock/content/absence boundary; it does not select either map or any
remaining bit.

## Promotion Value Gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers whether the 7 four-site fills of remaining bits `(1,0,0,0,0)` and `(1,1,0,0,0)` are the same set. |
| V2 | Current main has the axiom memo and no landed 4-site fill-set share of this exception pair. |
| V3 | The twelve-vertex process on `495` seeds under both maps is independently finite and exact. |
| V4 | The theorem is more than restating Admissibility: it executes two supplied predicates the axiom does not name. |
| V5 | Neither map nor a remaining bit is an admissibility rule, and neither is adopted. |

## No-Go Discipline Gate

The negative content is narrow: a 4-site fill-set share is not an
axiom-level occupancy rule, and a displayed remaining bit is not axiom
content.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| four-site fill of `f00` | all `495` 4-subsets | `|M00| = 7` |
| four-site fill of `f10` | all `495` 4-subsets | `|M10| = 7` |
| share | set intersection | `|M00 ∩ M10| = 7`; `M00 = M10` |
| `#6493` face | both maps on that face | in the intersection; history `(4, 8, 12)` |
| `opp2` distinction | evaluate both maps on `(0,1,2)` | `f10=1`; `f00=0`; sets still equal |
| Hamming parity | `|c|_1 mod 2` | different predicate; `opp2` even |
| L1/f0 miss share | miss sets of `f_L1` and `f0` | different objects; not this share |
| write a bit or map into Admissibility | treat either as the local rule | refused; axiom is not a dynamics axiom |

### N2 — wall independence

The missing formation-site selector, the missing axiom-level
occupancy rule, and the choice among displayed members are distinct
open items. This note claims no complete wall and no compiler no-go.

### N3 — hidden-condition scan

The two-cube, off-patch `o=0`, six-neighbor order, the predicates
`f00` and `f10`, and the `#6493` face are declared. Cube covariance is
used only as the axis-type reading of a six-tuple. No continuum,
Hamming, or admissibility rewrite is assumed.

### N4 — source residual matching

The axiom memo supplies the cubic nearest-neighbor graph and states
that Admissibility is not a dynamics axiom and does not supply the
formation site, probability, or rate. The residual therefore matches
those sources: two displayed lock predicates and two displayed remaining
bits are extra data.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | axis-type representatives and off-patch `0` | no alphabet classification |
| per site | every two-cube vertex against both displayed lock predicates | no derived kernel values |
| per mode | no mode calculation | no spectral exhaustion |
| per block | all `495` four-site seeds under both maps | no physical compiler |
| lattice wide | checked and not executed | neither map nor a remaining bit adopted as a rule |

### N6 — live partial-closure paths

Live routes include an independent reason to select or reject either
map, a ranking of the remaining `F_cut` members at seed size `4`, and
a formation mechanism supplied by something other than a displayed
predicate.

### N7 — hostile steelman

**Steelman:** `#6493` and `#6506` already said both coverages equal
`7`, and `#6507` already said both fill the same face, so either the
sets are leftover of those notes or this is the L1/f0 miss share again
and should be adopted.

**Answer:** `#6493` and `#6506` scored cardinals. `#6507` tested one
named face. This note compares the two 7-sets: `|M00 ∩ M10| = 7` and
`M00 = M10`. It is the first share-test of the exception pair at
`k=4`. It is not leftover of L1/f0 share. The equality bit is
displayed. Do not adopt a bit.

### N8 — cross-cycle echo

A coverage score (`#6493`, `#6506`), a one-face fill (`#6507`), and a
miss-set share of a different pair (`f_L1` vs `f0`) are different
claims. This note executes the 4-site fill-set share of remaining bits
`(1, 0, 0, 0, 0)` and `(1, 1, 0, 0, 0)`.

**Gate disposition:** PASS for the finite share statement and the
equality bit. FAIL / DO NOT SHIP for “adopt `f00` or `f10`,” “adopt a
remaining bit,” “write a bit into Admissibility,” or “this is leftover
of L1/f0 share.”

## Primary Runner

The primary runner rebuilds the two-cube, the predicates `f00` and
`f10`, the fill sets `|M00| = 7` and `|M10| = 7`, the intersection
`|M00 ∩ M10| = 7`, the equality `M00 = M10`, membership of the
`#6493` face, the current premise boundary, and the non-adoption
wording. It authors no audit verdict.
