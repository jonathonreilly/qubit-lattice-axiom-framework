---
claim_id: f_min_line_seed_fill_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On the two-cube with off-patch o=0, the nonempty n_both=0 map f_min does fill from the 3-site long-axis seed. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_min_line_seed_fill_2026_08_15.py
---

# Line-Seed Fill Of The Named Nonempty `n_both=0` Map

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** displayed occupancy-to-lock dynamics of two cube-covariant
maps on the twelve-vertex two-cube `{0,1,2}×{0,1}×{0,1}`, started from
the 3-site long-axis seed, with off-patch occupancy identically `0`.
`f_min` is displayed, not adopted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/f_min_line_seed_fill_2026_08_15.py`](../scripts/f_min_line_seed_fill_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

Write the two-cube as the twelve sites `{0,1,2}×{0,1}×{0,1}`. A site
locks when a displayed predicate of its six-neighbor occupancy tuple
returns `1`. Off-patch neighbors contribute occupancy `0`. Fill means
the halt lock set has cardinality `12`.

Let `f_L1(c)=1` if and only if some axis of `c` is unbalanced (`n≠0`,
not Hamming parity). Let `f_min(c)=1` if and only if `n_both(c)=0` and
some axis is unbalanced. These are distinct maps: they disagree on the
`mixed3=(1,1,1)` orbit.

**Theorem 1.** From `S={(0,0,0),(1,0,0),(2,0,0)}`, `f_L1` fills with
lock history `(3, 9, 12)`.

**Theorem 2.** From the same seed, `f_min` reaches a fixed point at
tick `T=2` with `|locks_halt|=12` and lock history `(3, 9, 12)`. It
does fill.

**Theorem 3.** On this seed the executed unlocking configurations never
include `mixed3`, so the two maps produce the same lock history. The
comparison is displayed only. Do not adopt `f_min`. `f_min` is
not written into Admissibility.

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
predicate. The maps `f_L1` and `f_min` are supplied displayed members,
not axiom content.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Finite exact lock histories of two displayed occupancy-to-lock maps on a twelve-vertex two-cube from one named seed."
trace_class: frontier_discovery
target_claim_id: f_min_line_seed_fill
target_blocker_text: "whether the named nonempty n_both=0 rival fills the two-cube from the 3-site long-axis seed"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the bounded fill claim; do not adopt f_min"
conditional_surface_status: "exact on the two-cube with off-patch o=0 from S; f_min remains a displayed member"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

Sites of the two-cube:

`(x,y,z)` with `x∈{0,1,2}` and `y,z∈{0,1}`.

The six-neighbor tuple at a site is ordered
`(+x,-x,+y,-y,+z,-z)`. Each coordinate is the occupancy of that
neighbor: `1` if the neighbor is an on-patch lock, else `0`. Every
off-patch neighbor is `0`.

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
| vertex3 | `(3,0,0)` | `(1,0,1,0,1,0)` |
| mixed3 | `(1,1,1)` | `(1,0,1,1,0,0)` |
| full | `(0,3,0)` | `(1,1,1,1,1,1)` |

`f_L1(c)=1` iff `n_unbalanced(c)≥1`.
`f_min(c)=1` iff `n_both(c)=0` and `n_unbalanced(c)≥1`.

On those representatives the bits are

| map | wt1 | opp2 | adj2 | vertex3 | mixed3 | empty | full |
|---|---|---|---|---|---|---|---|
| `f_L1` | 1 | 0 | 1 | 1 | 1 | 0 | 0 |
| `f_min` | 1 | 0 | 1 | 1 | 0 | 0 | 0 |

`f_min` therefore has support `26` on `{0,1}^6`. The maps disagree on
`mixed3`. Hamming parity of `|c|_1` is a different predicate: `opp2`
is even and `f_L1(opp2)=0`.

One tick locks every currently unlocked on-patch site whose neighbor
tuple has `f=1`. The process starts with `locks_0=S` and halts at the
first fixed point, or at tick `12`. Lock history is the sequence of
cardinalities from `t=0` through halt.

## Theorem 1 — `f_L1` fills from the line seed

Start with `S={(0,0,0),(1,0,0),(2,0,0)}`, so `|locks_0|=3`.

The six sites `(0,1,0)`, `(0,0,1)`, `(1,1,0)`, `(1,0,1)`, `(2,1,0)`,
`(2,0,1)` each see exactly one occupied nearest neighbor along `y` or
`z`. That tuple is type `wt1`, so `f_L1=1`. The three remaining
sites `(0,1,1)`, `(1,1,1)`, `(2,1,1)` see the empty tuple.

After tick `1` one has `|locks_1|=9`. Each of the three remaining
sites then sees two unbalanced axes (`adj2`), so they lock at tick
`2`. The halt set is the whole two-cube:

`T=2`, `|locks_halt|=12`, history `(3, 9, 12)`.

This is the displayed `f_L1` line-seed fill, recomputed here.

## Theorem 2 — `f_min` from the same seed

The same first-wave sites are type `wt1`, and `f_min(wt1)=1`. The
same second-wave sites are type `adj2`, and `f_min(adj2)=1`. No
unlocking configuration from `S` is type `mixed3` or `opp2`.

Therefore `f_min` produces the same updates. It reaches a fixed point
at `T=2` with `|locks_halt|=12` and lock history `(3, 9, 12)`. Fill
holds: `f_min` does fill from the 3-site long-axis seed.

The first wave is exactly the six long-axis `y`/`z` neighbors listed
in Theorem 1.

## Theorem 3 — comparison, not adoption

On this seed the two maps agree on every executed unlocking tuple, so
they have the same lock history. They remain distinct maps: `mixed3`
is live as a predicate difference and is simply unvisited from `S`.

The 1-site `f_L1` history from `{(0,0,0)}` is `(1, 4, 8, 11, 12)`.
That is a different seed and a different history. The present claim
is not that leftover, and it is not an `F_cut` AND count.

`f_min` is a displayed rival member. Do not adopt `f_min`. It is
not written into Admissibility. Admissibility is not a dynamics axiom and
does not supply this predicate.

## Exact Target And Obligation Graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record wording | quoted; no edit |
| two-cube, seed `S`, off-patch `o=0` | declared finite data |
| `f_L1` line-seed history `(3, 9, 12)` | recomputed |
| `f_min` halt locks, `T`, history | `12`, `2`, `(3, 9, 12)` |
| fill boolean | does fill |
| identity of `f_min` with `f_L1` | refused; they disagree on `mixed3` |
| adoption into Admissibility | refused |
| formation site / rate from the axioms | open |

## Boundary And Imports

No observation, fit, continuum limit, or Hamming-as-`f_L1`
identification is imported. The two-cube and the two predicates are
supplied mathematical data for this note. Record lock language is
quoted only as the existing lock/content/absence boundary; it does
not select `f_min`.

## Promotion Value Gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers whether the named nonempty `n_both=0` rival fills from the second displayed seed. |
| V2 | Current main has the axiom memo and no landed line-seed `f_min` fill. |
| V3 | The twelve-vertex process is independently finite and exact. |
| V4 | The theorem is more than restating Admissibility: it executes a supplied predicate the axiom does not name. |
| V5 | It is not an admissibility rule and is not adopted. |

## No-Go Discipline Gate

The negative content is narrow: agreement of histories on this seed is
not identity of maps, and a displayed filler is not axiom content.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| `f_L1` from `S` | some-axis-unbalanced predicate | fills; history `(3, 9, 12)` |
| `f_min` from `S` | nonempty `n_both=0` predicate | fills; same history |
| `mixed3` distinction | evaluate both maps on `(1,1,1)` | they disagree; maps stay distinct |
| 1-site seed | start at `(0,0,0)` only | `f_L1` history `(1, 4, 8, 11, 12)`; different claim |
| Hamming parity | `|c|_1 mod 2` | different predicate; `opp2` even |
| write into Admissibility | treat `f_min` as the local rule | refused; axiom is not a dynamics axiom |

### N2 — wall independence

The missing formation-site selector, the missing axiom-level
occupancy rule, and the unvisited `mixed3` distinction are distinct
open items. This note claims no complete wall and no compiler no-go.

### N3 — hidden-condition scan

The two-cube, off-patch `o=0`, seed `S`, six-neighbor order, and both
predicates are declared. Cube covariance is used only as the
axis-type reading of a six-tuple. No continuum, Hamming, or
admissibility rewrite is assumed.

### N4 — source residual matching

The axiom memo supplies the cubic nearest-neighbor graph and states
that Admissibility is not a dynamics axiom and does not supply the
formation site, probability, or rate. The residual therefore matches
those sources: a displayed lock predicate is extra data.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | axis-type representatives and off-patch `0` | no alphabet classification |
| per site | every two-cube vertex against the predicate | no derived kernel values |
| per mode | no mode calculation | no spectral exhaustion |
| per block | the twelve-vertex two-cube from `S` | no physical compiler |
| lattice wide | checked and not executed | `f_min` not adopted as a rule |

### N6 — live partial-closure paths

Live routes include an independent reason to select or reject
`f_min`, a seed family on which `mixed3` is visited, and a formation
mechanism supplied by something other than a displayed predicate.

### N7 — hostile steelman

**Steelman:** Same history from `S` means `f_min` is `f_L1`, so the
rival may be adopted.

**Answer:** The maps disagree on `mixed3`. History agreement on one
seed is path coincidence, not predicate identity. Admissibility does
not name either map.

### N8 — cross-cycle echo

A 1-site identity of `f_min` and an `F_cut` AND count on this seed
are different claims. This note executes only the fill boolean and
the lock history of the named rival from `S`.

**Gate disposition:** PASS for the finite fill statement and the
displayed comparison. FAIL / DO NOT SHIP for “adopt `f_min`,” “write
`f_min` into Admissibility,” or “`f_min` is `f_L1`.”

## Primary Runner

The primary runner rebuilds the two-cube, the seed, both predicates,
the line-seed histories, the `mixed3` distinction, the 1-site
mutation, the current premise boundary, and the non-adoption wording.
It authors no audit verdict.
