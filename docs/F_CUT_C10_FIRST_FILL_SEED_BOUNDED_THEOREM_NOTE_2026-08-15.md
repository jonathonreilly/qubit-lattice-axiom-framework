---
claim_id: f_cut_c10_first_fill_seed_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On the two-cube with off-patch o=0, the lex-first seed that F_cut (1,1,0,0,0) fills is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_c10_first_fill_seed_2026_08_15.py
---

# Lex-First Two-Cube Seed That `F_cut` `(1,1,0,0,0)` Fills

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** displayed occupancy-to-lock dynamics of the cube-covariant
map `F_cut` remaining bits `(1,1,0,0,0)` on the twelve-vertex two-cube
`{0,1,2}×{0,1}×{0,1}`, started from seeds ordered by increasing size
then lexicographic site order, from `|S|=3` through `|S|=6`, with
off-patch occupancy identically `0`. The lex-first fill seed is
displayed, not adopted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_c10_first_fill_seed_2026_08_15.py`](../scripts/f_cut_c10_first_fill_seed_2026_08_15.py)
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
`f00=(1,0,0,0,0)`, which silences `opp2`.

Among the `66` two-site seeds, `cov2(f10)=0` (#6490). That scoring
does not name a first fill. Enumerate seeds `S` by increasing `|S|`,
then lexicographic site order, starting at `|S|=3` through `|S|=6`.

**Theorem 1.** `cov2(f10)=0` among the `66` two-site seeds. This
reconfirms the `#6490` exception for remaining bits `(1,1,0,0,0)`.

**Theorem 2.** The lex-first seed that `f10` fills is the size-`3`
seed `S={(0,0,0),(1,1,1),(2,0,0)}`. So `|S|=3`. Four of the `220`
three-site seeds fill; this is the first in lex order.

**Theorem 3.** From that `S` the lock history is `(3, 12)` and the run
fills. The seed and the history are displayed only. Do not adopt
`f10`. Do not adopt a seed. Do not write a seed into Admissibility.

Displayed, not adopted.

Not leftover-character of #6490 (that scored `cov2` only).
Not leftover-character of the `(1,0,0,0,0)` first-fill seed (that is a
different map; `f00` does not fill this `S`).
New finite object: the lex-first fill of remaining bits `(1,1,0,0,0)`.

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
content. A seed is likewise displayed data, not an admissibility rule.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Finite exact seed census of one displayed F_cut occupancy-to-lock map on a twelve-vertex two-cube from size 3 through size 6."
trace_class: frontier_discovery
target_claim_id: f_cut_c10_first_fill_seed
target_blocker_text: "lex-first two-cube seed from which F_cut remaining bits (1,1,0,0,0) fills"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the bounded first-fill-seed claim; do not adopt the map or the seed"
conditional_surface_status: "exact on the two-cube with off-patch o=0 for |S|<=6; the map and seed remain displayed"
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

Hamming parity of `|c|_1` is a different predicate: `opp2` is even and
`f_L1(opp2)=0`, while `f10(opp2)=1`.

One tick locks every currently unlocked on-patch site whose neighbor
tuple has `f=1`. The process starts with `locks_0=S` and halts at the
first fixed point, or at tick `12`. Lock history is the sequence of
cardinalities from `t=0` through halt. Fill means `|locks_halt|=12`.

Seeds are enumerated by increasing cardinality, then as combinations
of the lexicographic site list. The two-site census has `66` seeds.
The search for a first fill starts at size `3` (`220` seeds) and
continues through size `6` (`C(12,3)+…+C(12,6)=2431` seeds in the
search window). It is a seed census on this two-cube, not a clone of
the `(1,0,0,0,0)` first-fill map.

## Theorem 1 — `cov2(f10)=0`

Reconfirm the `#6490` exception for this remaining-bit tuple.

There are `C(12,2)=66` unordered two-site seeds. From each of them
`f10` fails to fill: `cov2(f10)=0`. No two-site seed is a filler.

That fact scores coverage only. It does not name a first fill, a
history, or a preferred seed.

## Theorem 2 — lex-first fill seed

Enumerate seeds by increasing `|S|`, then lex, starting at `3`.

No seed of size `2` fills, as Theorem 1 already recorded. At size
`3` four of the `220` seeds fill. The first in lex order is

`S={(0,0,0),(1,1,1),(2,0,0)}`.

So `|S|=3`. The later size-`3` fillers are the three remaining
`x`-aligned `opp2` pairs with the opposite middle-cube vertex. They
are not the lex-first seed.

The census through size `6` is

| `|S|` | `C(12,|S|)` | number that fill | lex-first filler |
|---|---|---|---|
| 2 | 66 | 0 | none |
| 3 | 220 | 4 | `{(0,0,0),(1,1,1),(2,0,0)}` |
| 4 | 495 | 7 | the `x=0` face (later than size 3) |
| 5 | 792 | 0 | none |
| 6 | 924 | 12 | later than size 3 |

A first fill therefore exists inside the `|S|≤6` cap, and it occurs
already at size `3`.

This is not the `(1,0,0,0,0)` first-fill seed. That map first fills
only at a size-`4` face and does not fill this size-`3` `S`.

## Theorem 3 — history from that `S`

Start with `S={(0,0,0),(1,1,1),(2,0,0)}`, so `|locks_0|=3`.

The nine unlocked sites at tick `1` split as follows.

- Eight sites see a single occupied nearest neighbor (type `wt1`):
  `(0,0,1)`, `(0,1,0)`, `(0,1,1)`, `(1,0,1)`, `(1,1,0)`, `(2,0,1)`,
  `(2,1,0)`, `(2,1,1)`. Both `f10` and `f00` return `1`.
- The remaining site `(1,0,0)` sees type `opp2=(0,1,2)`: its `+x` and
  `-x` neighbors `(2,0,0)` and `(0,0,0)` are both locked. Then
  `f10=1` and `f00=0`.

Therefore `f10` locks all nine unlocked sites in one tick:

`T=1`, `|locks_halt|=12`, history `(3, 12)`, fill bit `1`.

The executed new orbit is `opp2` at `(1,0,0)`. Silencing that bit
(`f00`) leaves `(1,0,0)` unlocked and halts at eleven locks, so the
two maps are dynamically distinct on this seed.

The seed `S` and the history `(3, 12)` are displayed data. Do not
adopt `f10`. Do not adopt a seed. Do not write a seed into
Admissibility. The seed is not written into Admissibility.

## Exact Target And Obligation Graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record wording | quoted; no edit |
| two-cube, off-patch `o=0`, lex seed order, sizes `3`–`6` | declared finite data |
| `cov2(f10)=0` | recomputed; `#6490` |
| lex-first fill seed | `{(0,0,0),(1,1,1),(2,0,0)}`, `|S|=3` |
| history from that `S` | `(3, 12)`; fills |
| identity with `f00` or `f_L1` | refused; different remaining bits |
| adoption of the map or the seed | refused |
| formation site / rate from the axioms | open |

## Boundary And Imports

No observation, fit, continuum limit, or Hamming-as-`f_L1`
identification is imported. The two-cube, the predicate `f10`, and the
seed order are supplied mathematical data for this note. Record lock
language is quoted only as the existing lock/content/absence boundary;
it does not select this map or any seed.

## Promotion Value Gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers which first `|S|≥3` seed, if any, `f10` fills. |
| V2 | Current main has the axiom memo and no landed first-fill-seed census of remaining bits `(1,1,0,0,0)`. |
| V3 | The twelve-vertex process through size `6` is independently finite and exact. |
| V4 | The theorem is more than restating Admissibility: it executes a supplied predicate the axiom does not name. |
| V5 | Neither the map nor the seed is an admissibility rule, and neither is adopted. |

## No-Go Discipline Gate

The negative content is narrow: a first fill is not an axiom-level
occupancy rule, and a displayed seed is not axiom content.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| two-site coverage | all `66` pairs | `cov2(f10)=0` |
| lex census from size `3` | `220` three-site seeds | first fill at `{(0,0,0),(1,1,1),(2,0,0)}` |
| `f10` from that `S` | remaining bits `(1,1,0,0,0)` | fills; history `(3, 12)` |
| `f00` from that `S` | remaining bits `(1,0,0,0,0)` | does not fill; different map |
| `opp2` distinction | evaluate `f10` on `(0,1,2)` | `f10=1`; `f_L1=0` |
| Hamming parity | `|c|_1 mod 2` | different predicate; `opp2` even |
| write a seed or map into Admissibility | treat either as the local rule | refused; axiom is not a dynamics axiom |

### N2 — wall independence

The missing formation-site selector, the missing axiom-level
occupancy rule, and the choice among displayed members are distinct
open items. This note claims no complete wall and no compiler no-go.

### N3 — hidden-condition scan

The two-cube, off-patch `o=0`, lex site order, size window `3`–`6`,
six-neighbor order, and the predicate `f10` are declared. Cube
covariance is used only as the axis-type reading of a six-tuple. No
continuum, Hamming, or admissibility rewrite is assumed.

### N4 — source residual matching

The axiom memo supplies the cubic nearest-neighbor graph and states
that Admissibility is not a dynamics axiom and does not supply the
formation site, probability, or rate. The residual therefore matches
those sources: a displayed lock predicate and a displayed seed are
extra data.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | axis-type representatives and off-patch `0` | no alphabet classification |
| per site | every two-cube vertex against the displayed lock predicate | no derived kernel values |
| per mode | no mode calculation | no spectral exhaustion |
| per block | all seeds of size `2` through `6` | no physical compiler |
| lattice wide | checked and not executed | neither the map nor the seed adopted as a rule |

### N6 — live partial-closure paths

Live routes include an independent reason to select or reject `f10`,
a first-fill census of the remaining `cov2=0` members, and a
formation mechanism supplied by something other than a displayed
predicate.

### N7 — hostile steelman

**Steelman:** `cov2=0` already said this map cannot start, so either
no fill exists or the first fill is the same size-`4` face that
`(1,0,0,0,0)` uses, and the two `#6490` exceptions are one object.

**Answer:** The lex-first fill of `f10` is already the size-`3` seed
`{(0,0,0),(1,1,1),(2,0,0)}`, with history `(3, 12)`. The map `f00`
does not fill that seed. The two remaining-bit tuples are different
maps and produce different first-fill seeds.

### N8 — cross-cycle echo

A two-site coverage score of `0` (#6490) and a first-fill seed of
remaining bits `(1,0,0,0,0)` are different claims. This note executes
the lex-first fill of remaining bits `(1,1,0,0,0)`.

**Gate disposition:** PASS for the finite first-fill statement and the
displayed history. FAIL / DO NOT SHIP for “adopt `f10`,” “adopt this
seed,” “write a seed into Admissibility,” or “`f10` is the same
first-fill object as `f00`.”

## Primary Runner

The primary runner rebuilds the two-cube, the predicate `f10`, the
two-site coverage `cov2(f10)=0`, the lex census from size `3` through
size `6`, the first-fill seed with its history and fill bit, the
`opp2` lock at `(1,0,0)`, the current premise boundary, and the
non-adoption wording. It authors no audit verdict.
