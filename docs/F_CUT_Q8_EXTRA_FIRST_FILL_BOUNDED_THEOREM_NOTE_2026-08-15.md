---
claim_id: f_cut_q8_extra_first_fill_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On the two-cube with off-patch o=0, the lex-first seed that F_cut (0,1,0,0,0) fills is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_q8_extra_first_fill_2026_08_15.py
---

# Lex-First Two-Cube Seed That The Q8 Extra `F_cut` `(0,1,0,0,0)` Fills

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** displayed occupancy-to-lock dynamics of one cube-covariant
map on the twelve-vertex two-cube `{0,1,2}×{0,1}×{0,1}`, started from
seeds ordered by increasing size then lexicographic site order, from
size `1` through size `8`, with off-patch occupancy identically `0`.
The lex-first seed that fills is displayed, not adopted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_q8_extra_first_fill_2026_08_15.py`](../scripts/f_cut_q8_extra_first_fill_2026_08_15.py)
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

Let `f_e` be the newly named Q8 extra `F_cut` remaining-bit map

```text
(wt1, opp2, adj2, vertex3, mixed3) = (0, 1, 0, 0, 0)
```

with complements forced. It fires only on axis types `(0,1,2)` and
`(0,2,1)`. Investment `#6555` scored `cov6(f_e)=0` and `cov8(f_e)>0`.
Those scores are leftover-character of `#6555`. The object of this
note is the first seed `f_e` fills. This is a new first-fill of a
newly named extra. It is not the first-fill object of the sixteen
`wt1=0` maps.

Enumerate seeds `S` by increasing `|S|`, then lexicographic site
order, starting at `|S|=1` and stopping at `|S|=8`.

**Theorem 1.** The lex-first seed that `f_e` fills is the size-`8`
pair of opposite faces

`S={(0,0,0),(0,0,1),(0,1,0),(0,1,1),(2,0,0),(2,0,1),(2,1,0),(2,1,1)}`.

So `|S|=8`. From that `S` the lock history is `(8, 12)` and the run
fills.

**Theorem 2.** At that cardinality, `cov8(f_e)=1` among the `495`
eight-site seeds. Every smaller cardinality is empty:
`covk(f_e)=0` for `k=1,…,7`.

**Theorem 3.** The seed, the coverage count, and the history are
displayed only. Do not adopt a seed. Do not write a seed into
Admissibility.

Displayed, not adopted.

Not leftover-character of #6555 (that scored `cov6=0` and `cov8>0` only).
Not leftover-character of the `wt1=0` first-fill seed.

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
predicate. The map `f_e` is a supplied displayed member, not axiom
content. A seed is likewise displayed data, not an admissibility rule.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Finite exact first-fill seed search of one displayed Q8 extra F_cut map on a twelve-vertex two-cube from size 1 through size 8."
trace_class: frontier_discovery
target_claim_id: f_cut_q8_extra_first_fill
target_blocker_text: "lex-first two-cube seed that F_cut (0,1,0,0,0) fills"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the bounded first-fill claim; do not adopt the seed"
conditional_surface_status: "exact on the two-cube with off-patch o=0 for |S|<=8; the seed remains displayed data"
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
| type021 | `(0,2,1)` | `(1,1,1,1,0,0)` |
| wt5 | `(1,2,0)` | `(1,1,1,1,1,0)` |
| full | `(0,3,0)` | `(1,1,1,1,1,1)` |

`F_cut` is the cube-covariant class with `f(empty)=f(full)=0` and
`f(c)=f(1-c)`. Five remaining bits stay free, so `|F_cut|=32`. Those
bits are ordered `(wt1, opp2, adj2, vertex3, mixed3)`.

`f_L1(c)=1` iff `n_unbalanced(c)≥1`. Its remaining-bit tuple is
`(1,0,1,1,1)`.
`f_e(c)=1` iff the axis type is `opp2=(0,1,2)` or `type021=(0,2,1)`.
Its remaining-bit tuple is `(0,1,0,0,0)`.

On those representatives the bits are

| map | wt1 | opp2 | adj2 | type210 | vertex3 | mixed3 | type021 | empty | full |
|---|---|---|---|---|---|---|---|---|---|
| `f_L1` | 1 | 0 | 1 | 1 | 1 | 1 | 0 | 0 | 0 |
| `f_e` | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 |

Hamming parity of `|c|_1` is a different predicate: `opp2` is even and
`f_L1(opp2)=0`, while `adj2` is even and `f_L1(adj2)=1`.

One tick locks every currently unlocked on-patch site whose neighbor
tuple has `f=1`. The process starts with `locks_0=S` and halts at the
first fixed point, or at tick `12`. Lock history is the sequence of
cardinalities from `t=0` through halt. Fill means `|locks_halt|=12`.

Seeds are enumerated by increasing cardinality, then as combinations
of the lexicographic site list. The search starts at size `1`. The
cap is size `8` because `#6555` already scored `cov6=0` and `cov8>0`.

## Theorem 1 — lex-first fill seed and lock history

Search seeds of size `1` through `7` in lex order. None fills.

Search the `495` eight-site seeds in lex order. The first that fills is

`S={(0,0,0),(0,0,1),(0,1,0),(0,1,1),(2,0,0),(2,0,1),(2,1,0),(2,1,1)}`.

This is the pair of opposite faces `x=0` and `x=2`. Its size is `|S|=8`.

Start with that `S`, so `|locks_0|=8`. At tick `1` the four middle-slice
sites `(1,0,0)`, `(1,0,1)`, `(1,1,0)`, `(1,1,1)` each see both `+x` and
`-x` occupied and the four transverse neighbors empty (type `opp2`),
so `f_e` returns `1`. The run fills:

`T=1`, `|locks_halt|=12`, history `(8, 12)`, fill bit `1`.

The executed firings are the `opp2` orbit only.

## Theorem 2 — `cov8(f_e)` at that cardinality

Among the `C(12,8)=495` unordered eight-site seeds, `f_e` fills exactly
one. That is `cov8(f_e)=1`. The unique filler is the lex-first seed of
Theorem 1.

The smaller scores are

| `k` | `C(12,k)` | `covk(f_e)` |
|---|---|---|
| 1 | 12 | 0 |
| 2 | 66 | 0 |
| 3 | 220 | 0 |
| 4 | 495 | 0 |
| 5 | 792 | 0 |
| 6 | 924 | 0 |
| 7 | 792 | 0 |
| 8 | 495 | 1 |

In particular `cov6(f_e)=0` and `cov8(f_e)=1>0`, which reconfirms the
`#6555` scores and names the unique eight-site filler those scores did
not name.

## Theorem 3 — display, not adoption

The seed is displayed data. Do not adopt `f_e`. Do not adopt this seed.
Do not write a seed into Admissibility. Admissibility is not a dynamics
axiom and does not supply this predicate or this seed. The seed is not
written into Admissibility.

A `cov6=0` and `cov8>0` pair of scores is not a first-fill seed. The
first-fill seed is a new finite object on this two-cube.

## Exact Target And Obligation Graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record wording | quoted; no edit |
| two-cube, off-patch `o=0`, lex seed order from size `1` | declared finite data |
| `covk(f_e)=0` for `k=1,…,7` | recomputed |
| first fill through size `8` | `{(0,0,0),(0,0,1),(0,1,0),(0,1,1),(2,0,0),(2,0,1),(2,1,0),(2,1,1)}` |
| `|S|` | `8` |
| `cov8(f_e)` | `1` of `495` |
| history from that `S` | `(8, 12)`; fills |
| adoption of the seed or the map | refused |
| formation site / rate from the axioms | open |

## Boundary And Imports

No observation, fit, continuum limit, or Hamming-as-`f_L1`
identification is imported. The two-cube, the predicate `f_e`, and the
seed order are supplied mathematical data for this note. Record lock
language is quoted only as the existing lock/content/absence boundary;
it does not select this map or any seed.

## Promotion Value Gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers which first seed, if any through size `8`, the Q8 extra `f_e` fills. |
| V2 | Current main has the axiom memo and the `#6555` `cov6=0`, `cov8>0` scores, not this first-fill seed. |
| V3 | The twelve-vertex process through size `8` is independently finite and exact. |
| V4 | The theorem is more than restating Admissibility: it executes a supplied predicate the axiom does not name. |
| V5 | Neither the map nor the seed is an admissibility rule, and neither is adopted. |

## No-Go Discipline Gate

The negative content is narrow: a `cov6=0` score is not a first-fill
seed, and a displayed filler or seed is not axiom content.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| sizes `1` through `7` | all `C(12,k)` seeds | `covk(f_e)=0` |
| lex eight-site search | first of `495` | `S` the opposite `x` faces; fills |
| eight-site census | all `495` | `cov8(f_e)=1` |
| history from `S` | occupancy-to-lock under `f_e` | `(8, 12)`; fills |
| Hamming parity | `|c|_1 mod 2` | different predicate; `adj2` even |
| write a seed or map into Admissibility | treat either as the local rule | refused; axiom is not a dynamics axiom |

### N2 — wall independence

The missing formation-site selector, the missing axiom-level
occupancy rule, and the choice among displayed members are distinct
open items. This note claims no complete wall and no compiler no-go.

### N3 — hidden-condition scan

The two-cube, off-patch `o=0`, lex site order, size window `1` through
`8`, six-neighbor order, and the remaining-bit tuple `(0,1,0,0,0)` are
declared. Cube covariance is used only as the axis-type reading of a
six-tuple. No continuum, Hamming, or admissibility rewrite is assumed.

### N4 — source residual matching

The axiom memo supplies the cubic nearest-neighbor graph and states
that Admissibility is not a dynamics axiom and does not supply the
formation site, probability, or rate. The extra therefore matches
those sources: a displayed lock predicate and a displayed seed are
extra data.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | axis-type representatives and off-patch `0` | no alphabet classification |
| per site | every two-cube vertex against `f_e` | no derived kernel values |
| per mode | no mode calculation | no spectral exhaustion |
| per block | all seeds of size `1` through `8` | no physical compiler |
| lattice wide | checked and not executed | neither map nor the seed adopted as a rule |

### N6 — live partial-closure paths

Live routes include an independent reason to select or reject `f_e`,
a first-fill seed of the other Q8 extra `(0,1,0,0,1)`, and a
formation mechanism supplied by something other than a displayed
predicate.

### N7 — hostile steelman

**Steelman:** `cov6=0` and `cov8>0` already say this extra first fills
at size `8`, so any eight-site pair of faces may be treated as the
formation seed and written as a rule.

**Answer:** Exactly one eight-site seed fills, and the lex-first such
seed is the opposite `x` faces named above. That is a displayed
finite fact. Admissibility does not name `f_e` or this seed.

### N8 — cross-cycle echo

A `cov6=0`/`cov8>0` score pair (`#6555`) and a first-fill of the
sixteen `wt1=0` maps are different claims. This note executes the
lex-first seed that the newly named extra `F_cut` `(0,1,0,0,0)` fills.

**Gate disposition:** PASS for the finite first-fill statement and the
displayed history. FAIL / DO NOT SHIP for “adopt `f_e`,” “write a seed
into Admissibility,” or “`cov8>0` already is the first-fill seed.”

## Primary Runner

The primary runner rebuilds the two-cube, the predicate `f_e`, the
lex search from size `1` through size `8`, the first-fill seed with
its history and fill bit, the `cov8` count, the `opp2` middle-slice
wave, the current premise boundary, and the non-adoption wording. It
authors no audit verdict.
