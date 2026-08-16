---
claim_id: f_cut_c10_four_site_coverage_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On the two-cube with off-patch o=0, the 4-site coverage of F_cut (1,1,0,0,0) is reported, and whether it fills the #6493 face. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_c10_four_site_coverage_2026_08_15.py
---

# Four-Site Coverage Of `F_cut` `(1,1,0,0,0)` On The Two-Cube

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** displayed occupancy-to-lock dynamics of the cube-covariant
map `F_cut` remaining bits `(1,1,0,0,0)` on the twelve-vertex two-cube
`{0,1,2}×{0,1}×{0,1}`, scored on all `495` four-site seeds, with
off-patch occupancy identically `0`. The 4-site coverage and whether
the `#6493` face fills are displayed, not adopted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_c10_four_site_coverage_2026_08_15.py`](../scripts/f_cut_c10_four_site_coverage_2026_08_15.py)
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

Let `f10` be the `F_cut` remaining-bit map

```text
(wt1, opp2, adj2, vertex3, mixed3) = (1, 1, 0, 0, 0)
```

with complements forced. It fires on `wt1` and `opp2` and on their
complements `wt5` and `(0,2,1)`. It is a different map from
`f00=(1,0,0,0,0)`, which silences `opp2`, and from `f_L1=(1,0,1,1,1)`.

`#6496` already named the first fill of `f10`: four of the `220`
three-site seeds fill. `#6493` named the first fill of `f00`: seven of
the `495` four-site seeds fill, and the lex-first of those is the
`x=0` face. The object of this note is the 4-site score of the second
`#6490` exception `f10`, and whether that `#6493` face is among the
fillers.

**Theorem 1.** `cov4(f10) = 7` among the `495` four-site seeds.

**Theorem 2.** The `#6493` face

`S={(0,0,0),(0,0,1),(0,1,0),(0,1,1)}`

is among the fillers. From that `S` the lock history is `(4, 8, 12)`
and the run fills.

**Theorem 3.** The score `7` and the face-membership bit are displayed
only. Do not adopt a bit. Do not adopt `f10`. Do not write a remaining
bit into Admissibility.

Displayed, not adopted.

Not leftover-character of #6496 (that named a size-`3` first fill).
Not leftover-character of #6493 (that scored `f00` and named its
lex-first face).
New score of the second exception: `cov4` of remaining bits
`(1,1,0,0,0)`.

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
predicate. The map `f10` is a supplied displayed member, not axiom
content. A remaining-bit tuple is likewise displayed data, not an
admissibility rule.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Finite exact 4-site fill census of one displayed F_cut occupancy-to-lock map on a twelve-vertex two-cube."
trace_class: frontier_discovery
target_claim_id: f_cut_c10_four_site_coverage
target_blocker_text: "4-site coverage of F_cut remaining bits (1,1,0,0,0) and whether the #6493 face fills"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the bounded 4-site coverage claim; do not adopt the map or a remaining bit"
conditional_surface_status: "exact on the two-cube with off-patch o=0 for |S|=4; the map and bits remain displayed"
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
`f10(c)=1` iff the axis type is `wt1=(1,0,2)`, `opp2=(0,1,2)`,
`wt5=(1,2,0)`, or `opp2c=(0,2,1)`. Its remaining-bit tuple is
`(1,1,0,0,0)`.

On those representatives the bits are

| map | wt1 | opp2 | adj2 | type210 | vertex3 | mixed3 | empty | full | wt5 | opp2c |
|---|---|---|---|---|---|---|---|---|---|---|
| `f_L1` | 1 | 0 | 1 | 1 | 1 | 1 | 0 | 0 | 1 | 0 |
| `f10` | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 |
| `f00` | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 |

Hamming parity of `|c|_1` is a different predicate: `opp2` is even and
`f_L1(opp2)=0`, while `f10(opp2)=1`.

One tick locks every currently unlocked on-patch site whose neighbor
tuple has `f=1`. The process starts with `locks_0=S` and halts at the
first fixed point, or at tick `12`. Lock history is the sequence of
cardinalities from `t=0` through halt. Fill means `|locks_halt|=12`.

Seeds of size `4` are the `C(12,4)=495` unordered 4-subsets of the
two-cube. Coverage `cov4(f)` is the number of those seeds from which
`f` fills. The `#6493` face is the entire `x=0` slice
`{(0,0,0),(0,0,1),(0,1,0),(0,1,1)}`. The seven fillers are not listed.

## Theorem 1 — `cov4(f10) = 7`

Among the `495` four-site seeds, exactly seven fill under `f10`.

So `cov4(f10) = 7`. This is a coverage score of one displayed map. It
does not rank the other thirty-one `F_cut` members and does not adopt
any remaining bit.

The same integer `7` already appears as `cov4(f00)` in `#6493`. That
coincidence of scores is not an identification of the two maps:
`f10` and `f00` disagree on `opp2`. The new object is the score of
the second exception, not a reuse of the `f00` first-fill census.

## Theorem 2 — the `#6493` face is among the fillers

The face

`S={(0,0,0),(0,0,1),(0,1,0),(0,1,1)}`

is one of the seven four-site seeds that `f10` fills.

Start with that `S`, so `|locks_0|=4`. At tick `1` the four
middle-slice sites `(1,0,0)`, `(1,0,1)`, `(1,1,0)`, `(1,1,1)` each see
a single occupied nearest neighbor along `-x` (type `wt1`), so `f10`
returns `1`. The four `x=2` sites see the empty tuple and stay
unlocked. After tick `1` one has `|locks_1|=8`. At tick `2` the four
`x=2` sites each see a single occupied nearest neighbor along `-x`
(type `wt1`) and lock.

`T=2`, `|locks_halt|=12`, history `(4, 8, 12)`, fill bit `1`.

The executed firings on this face are the `wt1` orbit only, so the
`opp2` bit that distinguishes `f10` from `f00` is not needed on this
particular seed. Face membership is therefore not a new named-pair
fill; it is a yes/no against a previously displayed face.

## Theorem 3 — display; do not adopt a bit

The integers `cov4(f10) = 7` and the yes-bit that the `#6493` face
fills are displayed data. Do not adopt a bit. Do not adopt `f10`. Do
not write a remaining bit into Admissibility. The remaining-bit tuple
`(1, 1, 0, 0, 0)` is not written into Admissibility.

## Exact Target And Obligation Graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record wording | quoted; no edit |
| two-cube, off-patch `o=0`, all `495` four-site seeds | declared finite data |
| `cov4(f10)` | `7` |
| `#6493` face among the fillers | yes; history `(4, 8, 12)` |
| identity with `f00` or `f_L1` | refused; different remaining bits |
| adoption of the map or a remaining bit | refused |
| formation site / rate from the axioms | open |

## Boundary And Imports

No observation, fit, continuum limit, or Hamming-as-`f_L1`
identification is imported. The two-cube, the predicate `f10`, and the
four-site seed list are supplied mathematical data for this note.
Record lock language is quoted only as the existing lock/content/absence
boundary; it does not select this map or any remaining bit.

## Promotion Value Gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers `cov4` of remaining bits `(1,1,0,0,0)` and whether the `#6493` face fills. |
| V2 | Current main has the axiom memo and no landed 4-site coverage score of this map. |
| V3 | The twelve-vertex process on `495` seeds is independently finite and exact. |
| V4 | The theorem is more than restating Admissibility: it executes a supplied predicate the axiom does not name. |
| V5 | Neither the map nor a remaining bit is an admissibility rule, and neither is adopted. |

## No-Go Discipline Gate

The negative content is narrow: a 4-site coverage score is not an
axiom-level occupancy rule, and a displayed remaining bit is not axiom
content.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| four-site coverage | all `495` 4-subsets | `cov4(f10) = 7` |
| `#6493` face | `{(0,0,0),(0,0,1),(0,1,0),(0,1,1)}` | among the fillers; history `(4, 8, 12)` |
| `f00` on that face | remaining bits `(1,0,0,0,0)` | also fills; different map |
| `opp2` distinction | evaluate `f10` on `(0,1,2)` | `f10=1`; `f_L1=0` |
| Hamming parity | `|c|_1 mod 2` | different predicate; `opp2` even |
| write a bit or map into Admissibility | treat either as the local rule | refused; axiom is not a dynamics axiom |

### N2 — wall independence

The missing formation-site selector, the missing axiom-level
occupancy rule, and the choice among displayed members are distinct
open items. This note claims no complete wall and no compiler no-go.

### N3 — hidden-condition scan

The two-cube, off-patch `o=0`, six-neighbor order, the predicate
`f10`, and the `#6493` face are declared. Cube covariance is used only
as the axis-type reading of a six-tuple. No continuum, Hamming, or
admissibility rewrite is assumed.

### N4 — source residual matching

The axiom memo supplies the cubic nearest-neighbor graph and states
that Admissibility is not a dynamics axiom and does not supply the
formation site, probability, or rate. The residual therefore matches
those sources: a displayed lock predicate and a displayed remaining
bit are extra data.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | axis-type representatives and off-patch `0` | no alphabet classification |
| per site | every two-cube vertex against the displayed lock predicate | no derived kernel values |
| per mode | no mode calculation | no spectral exhaustion |
| per block | all `495` four-site seeds | no physical compiler |
| lattice wide | checked and not executed | neither the map nor a remaining bit adopted as a rule |

### N6 — live partial-closure paths

Live routes include an independent reason to select or reject `f10`,
a 4-site ranking of the remaining `F_cut` members, and a formation
mechanism supplied by something other than a displayed predicate.

### N7 — hostile steelman

**Steelman:** `#6496` already said `f10` fills at size `3`, and
`#6493` already said seven 4-site seeds fill for `f00`, so either
`cov4(f10)` is leftover of those notes or the `#6493` face is a new
named-pair fill that should be adopted.

**Answer:** `#6496` scored three-site first-fill (`4` of `220`). This
note scores four-site coverage of the same map: `cov4(f10) = 7`. The
`#6493` face is among those seven fillers, with history `(4, 8, 12)`.
The score and the membership bit are displayed. Do not adopt a bit.

### N8 — cross-cycle echo

A size-`3` first-fill seed (#6496) and a size-`4` first-fill face of
a different map (#6493) are different claims. This note executes the
4-site coverage of remaining bits `(1,1,0,0,0)` and tests that
previously displayed face.

**Gate disposition:** PASS for the finite coverage statement and the
face-membership bit. FAIL / DO NOT SHIP for “adopt `f10`,” “adopt a
remaining bit,” “write a bit into Admissibility,” or “this is leftover
character of #6496 or #6493.”

## Primary Runner

The primary runner rebuilds the two-cube, the predicate `f10`, the
4-site coverage `cov4(f10) = 7`, membership of the `#6493` face, the
face history `(4, 8, 12)`, the current premise boundary, and the
non-adoption wording. It authors no audit verdict.
