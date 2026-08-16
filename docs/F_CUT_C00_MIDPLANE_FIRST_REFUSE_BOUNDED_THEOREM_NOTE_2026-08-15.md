---
claim_id: f_cut_c00_midplane_first_refuse_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On the two-cube with off-patch o=0, the first refused neighborhood of F_cut (1,0,0,0,0) on the #6504 size-1 midplane four-site fill is reported, or the run refuses none. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_c00_midplane_first_refuse_2026_08_15.py
---

# First Refused Neighborhood On The `#6504` Size-1 Midplane Four-Site Fill Of `F_cut` `(1,0,0,0,0)`

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** displayed occupancy-to-lock dynamics of one cube-covariant
map on the twelve-vertex two-cube `{0,1,2}×{0,1}×{0,1}`, started from
the `#6504` size-1 midplane four-site seed
`S={(1,0,0),(1,0,1),(1,1,0),(1,1,1)}`, with off-patch occupancy
identically `0`. The first remaining-bit neighborhood that `f00`
refuses on that filling run is reported, or `N_refuse=0` if the run
refuses none. Displayed, not adopted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_c00_midplane_first_refuse_2026_08_15.py`](../scripts/f_cut_c00_midplane_first_refuse_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

Write the two-cube as the twelve sites `{0,1,2}×{0,1}×{0,1}`. A site
locks when a displayed predicate of its six-neighbor occupancy tuple
returns `1`. Off-patch neighbors contribute occupancy `0`. A
blank-block is a different rule; it is not used. A run is the tuple of lock-set
cardinalities from the seed through halt, together with the fill bit
`|locks_halt|=12`.

Let `f_L1(c)=1` if and only if some axis is unbalanced: `c_{+μ} ≠ c_{-μ}`
for at least one `μ ∈ {x,y,z}`. Equivalently, some discrete neighbor
contrast `n_μ = c_{+μ} − c_{-μ}` is nonzero. This is **not** Hamming parity
`|c|_1 mod 2`. `f_L1` is the 10-orbit reading `n ≠ 0`, not Hamming.

Let `f00` be the `F_cut` remaining-bit map

```text
(wt1, opp2, adj2, vertex3, mixed3) = (1, 0, 0, 0, 0)
```

with complements forced. It fires only on axis types `(1,0,2)` and
`(1,2,0)`. The seed

```text
S={(1,0,0),(1,0,1),(1,1,0),(1,1,1)}
```

is the `#6504` size-1 midplane four-site fill of this map: the unique
orbit of size `1` among the three orbits of the seven four-site fills.
That naming of the midplane is leftover-character of `#6504`. The
object of this note is the first remaining-bit neighborhood `f00`
refuses on the filling run from that midplane. This is a new seed, not
the `#6493` face.

A remaining-bit neighborhood is a six-tuple whose axis type is one of
`wt1`, `opp2`, `adj2`, `vertex3`, `mixed3`, or a complement of those.
Empty and full are the two `F_cut` cuts, not remaining bits. A refuse
is an unlocked on-patch site whose neighbor tuple has `f00=0` and
whose type is remaining-bit. `N_refuse` is the number of such events
on the run.

**Theorem 1.** `f00` fills from `S`. The lock history is `(4, 12)`
and `|locks_halt|=12`. This reconfirms the `#6504` midplane fill.

**Theorem 2.** Every remaining-bit orbit that appears on that run is
accepted. The only remaining-bit type that appears is `wt1`. So
`N_refuse=0`: the run refuses none. No unlocked site sees the empty
tuple: both end faces see a single occupied midplane neighbor.

**Theorem 3.** The refuse census is displayed only. Do not adopt a
bit. Do not write a remaining bit into Admissibility.

Displayed, not adopted.

Not leftover-character of #6504 (that named `N_orb=3` and the size-1
midplane).
Not leftover-character of #6493 (that named the lex-first face fill
and its refuse census).

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
predicate. The map `f00` is a supplied displayed member, not axiom
content. A remaining-bit assignment is likewise displayed data, not
an admissibility rule.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Finite exact remaining-bit refuse census of one displayed F_cut map on the #6504 size-1 midplane four-site fill of the twelve-vertex two-cube."
trace_class: frontier_discovery
target_claim_id: f_cut_c00_midplane_first_refuse
target_blocker_text: "first remaining-bit neighborhood that F_cut (1,0,0,0,0) refuses on the #6504 size-1 midplane four-site fill"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the bounded refuse census; do not adopt a remaining bit"
conditional_surface_status: "exact on the two-cube with off-patch o=0 for this displayed midplane; N_refuse remains displayed data"
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
| full | `(0,3,0)` | `(1,1,1,1,1,1)` |

`F_cut` is the cube-covariant class with `f(empty)=f(full)=0` and
`f(c)=f(1-c)`. Five remaining bits stay free, so `|F_cut|=32`. Those
bits are ordered `(wt1, opp2, adj2, vertex3, mixed3)`.

`f_L1(c)=1` iff `n_unbalanced(c)≥1`. Its remaining-bit tuple is
`(1,0,1,1,1)`.
`f00(c)=1` iff the axis type is `wt1=(1,0,2)` or `wt5=(1,2,0)`. Its
remaining-bit tuple is `(1, 0, 0, 0, 0)`.

On those representatives the bits are

| map | wt1 | opp2 | adj2 | type210 | vertex3 | mixed3 | empty | full |
|---|---|---|---|---|---|---|---|---|
| `f_L1` | 1 | 0 | 1 | 1 | 1 | 1 | 0 | 0 |
| `f00` | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

Hamming parity of `|c|_1` is a different predicate: `opp2` is even and
`f_L1(opp2)=0`, while `adj2` is even and `f_L1(adj2)=1`.

One tick locks every currently unlocked on-patch site whose neighbor
tuple has `f=1`. The process starts with `locks_0=S` and halts at the
first fixed point, or at tick `12`. Lock history is the sequence of
cardinalities from `t=0` through halt. Fill means `|locks_halt|=12`.

A remaining-bit refuse is recorded in lexicographic site order at each
tick, then by increasing tick. If the list is empty, report
`N_refuse=0`.

## Theorem 1 — `f00` fills from the `#6504` midplane

Start with

`S={(1,0,0),(1,0,1),(1,1,0),(1,1,1)}`,

so `|locks_0|=4`. This is the entire shared midplane `x=1`.

At tick `1` the four `x=0` sites each see a single occupied nearest
neighbor along `+x` (type `wt1`), and the four `x=2` sites each see a
single occupied nearest neighbor along `-x` (type `wt1`). Both end
faces lock in the same tick. The run fills:

`T=1`, `|locks_halt|=12`, history `(4, 12)`, fill bit `1`.

This reconfirms the `#6504` size-1 midplane fill. The seed is
displayed data, not a newly chosen first-fill object, and it is not
the `#6493` face.

## Theorem 2 — first remaining-bit refuse, or `N_refuse=0`

On the seed occupancy the unlocked sites evaluate as follows, in lex
order.

| site | type | `f00` |
|---|---|---|
| `(0,0,0)` | `wt1` | 1 |
| `(0,0,1)` | `wt1` | 1 |
| `(0,1,0)` | `wt1` | 1 |
| `(0,1,1)` | `wt1` | 1 |
| `(2,0,0)` | `wt1` | 1 |
| `(2,0,1)` | `wt1` | 1 |
| `(2,1,0)` | `wt1` | 1 |
| `(2,1,1)` | `wt1` | 1 |

Every unlocked neighborhood is remaining-bit type `wt1` and is
accepted. Empty does not appear on an unlocked site. After this tick
the two-cube is full, so no later unlocked neighborhood exists.

The remaining-bit orbits that appear are `{wt1}` only, and `f00`
accepts `wt1`. Therefore `N_refuse=0`: the run refuses none.

## Theorem 3 — display, not adoption

The executed firings are the `wt1` orbit only. No remaining bit other
than `wt1` is seen, and none is refused. Do not adopt `f00`.
Do not adopt `wt1`. Do not adopt `N_refuse=0` as a formation rule.
Do not write a remaining bit into Admissibility. Admissibility is not
a dynamics axiom and does not supply this predicate or this refuse
census. The census is not written into Admissibility.

A midplane orbit representative is not a refuse census. The refuse
census on that seed is a new finite object on this two-cube.

## Exact Target And Obligation Graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record wording | quoted; no edit |
| two-cube, off-patch `o=0`, `#6504` midplane `S` | declared finite data |
| `f00` fills from `S` | recomputed; history `(4, 12)` |
| remaining-bit refuse list | empty; `N_refuse=0` |
| empty evaluations on unlocked sites | none; both end faces are `wt1` |
| adoption of a remaining bit or the map | refused |
| formation site / rate from the axioms | open |

## Boundary And Imports

No observation, fit, continuum limit, or Hamming-as-`f_L1`
identification is imported. The two-cube, the predicate `f00`, and the
`#6504` midplane are supplied mathematical data for this note. Record lock
language is quoted only as the existing lock/content/absence boundary;
it does not select this map or any remaining bit.

## Promotion Value Gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers which first remaining-bit neighborhood, if any, `f00` refuses on the `#6504` midplane fill. |
| V2 | Current main has the axiom memo and the `#6504` orbit naming, not this refuse census. |
| V3 | The twelve-vertex process from this midplane is independently finite and exact. |
| V4 | The theorem is more than restating Admissibility: it executes a supplied predicate the axiom does not name. |
| V5 | Neither the map nor a remaining bit is an admissibility rule, and neither is adopted. |

## No-Go Discipline Gate

The negative content is narrow: a midplane orbit representative is not
a refuse census, and a displayed filler or remaining bit is not axiom
content.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| midplane fill | occupancy-to-lock from `S` | **ATTEMPTED**; history `(4, 12)`; fills |
| seed neighborhoods | eight unlocked sites at `t=0` | **ATTEMPTED**; eight `wt1`; all fire |
| remaining-bit refuses | remaining-bit types with `f00=0` | **ATTEMPTED**; `N_refuse=0` |
| empty cut on unlocked sites | empty tuple at `t=0` | **ATTEMPTED**; none; empty is not remaining-bit |
| Hamming parity | `|c|_1 mod 2` | **ATTEMPTED**; different predicate; `adj2` even |
| write a remaining bit into Admissibility | treat a bit as the local rule | **ATTEMPTED**; refused; axiom is not a dynamics axiom |

### N2 — wall independence

The missing formation-site selector, the missing axiom-level
occupancy rule, and the choice among displayed members are distinct
open items. This note claims no complete wall and no compiler no-go.

### N3 — hidden-condition scan

The two-cube, off-patch `o=0`, the `#6504` midplane, six-neighbor order,
remaining-bit versus empty/full, and the remaining-bit tuple
`(1,0,0,0,0)` are declared. Cube covariance is used only as the
axis-type reading of a six-tuple. No continuum, Hamming, or
admissibility rewrite is assumed.

### N4 — source residual matching

The axiom memo supplies the cubic nearest-neighbor graph and states
that Admissibility is not a dynamics axiom and does not supply the
formation site, probability, or rate. The extra therefore matches
those sources: a displayed lock predicate and a displayed refuse
census are extra data.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | axis-type representatives and off-patch `0` | no alphabet classification |
| per site | every two-cube vertex against `f00` | no derived kernel values |
| per mode | no mode calculation | no spectral exhaustion |
| per block | the `#6504` midplane run to a fixed point | no physical compiler |
| lattice wide | checked and not executed | neither map nor a remaining bit adopted as a rule |

### N6 — live partial-closure paths

Live routes include an independent reason to select or reject `f00`,
a refuse census of the remaining `#6504` orbits, and a formation
mechanism supplied by something other than a displayed predicate.

### N7 — hostile steelman

**Steelman:** the midplane already fills by one two-sided `wt1` wave,
so either there is nothing to report or the `#6493` face refuse census
already covers this seed.

**Answer:** this seed is the size-1 midplane, not the `#6493` face.
The remaining-bit refuse list is empty, so `N_refuse=0`. That is a
displayed finite fact on this seed. Admissibility does not name `f00`
or this census.

### N8 — cross-cycle echo

An orbit count (`#6504`) and a face refuse census (`#6493`) are
different claims. This note executes the remaining-bit refuse census
of `F_cut` `(1,0,0,0,0)` on the size-1 midplane.

**Gate disposition:** PASS for the finite refuse census and the
displayed history. FAIL / DO NOT SHIP for “adopt `f00`,” “write a
remaining bit into Admissibility,” or “`#6504` already is the refuse
census.”

## Primary Runner

The primary runner rebuilds the two-cube, the predicate `f00`, the
`#6504` midplane fill with its history and fill bit, the two-sided
`wt1` wave, the remaining-bit refuse list (empty; `N_refuse=0`), the
absence of empty unlocked evaluations, the current premise boundary,
and the non-adoption wording. It authors no audit verdict.
