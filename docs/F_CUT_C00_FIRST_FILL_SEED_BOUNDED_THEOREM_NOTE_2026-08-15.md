---
claim_id: f_cut_c00_first_fill_seed_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On the two-cube with off-patch o=0, the lex-first seed that F_cut (1,0,0,0,0) fills is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_c00_first_fill_seed_2026_08_15.py
---

# Lex-First Two-Cube Seed That `F_cut` `(1,0,0,0,0)` Fills

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** displayed occupancy-to-lock dynamics of one cube-covariant
map on the twelve-vertex two-cube `{0,1,2}×{0,1}×{0,1}`, started from
seeds ordered by increasing size then lexicographic site order, from
size `3` through size `6`, with off-patch occupancy identically `0`.
The lex-first seed that fills is displayed, not adopted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_c00_first_fill_seed_2026_08_15.py`](../scripts/f_cut_c00_first_fill_seed_2026_08_15.py)
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
`(1,2,0)`. It is one of the two `#6490` maps with `wt1=1` and
`cov2=0`. That coverage score is leftover-character of `#6490`. The
object of this note is the first seed `f00` fills.

Enumerate seeds `S` by increasing `|S|`, then lexicographic site
order, starting at `|S|=3` and stopping at `|S|=6`.

**Theorem 1.** `cov2(f00)=0` among the `66` two-site seeds. This
reconfirms `#6490`.

**Theorem 2.** No seed of size `3` fills. The lex-first seed that
`f00` fills is the size-`4` face

`S={(0,0,0),(0,0,1),(0,1,0),(0,1,1)}`.

So `|S|=4`. Seven of the `495` four-site seeds fill; the face above is
the first in lex order. None of the `792` five-site seeds fill. Four
of the `924` six-site seeds fill.

**Theorem 3.** From that `S`, the lock history is `(4, 8, 12)` and the
run fills. The seed and the history are displayed only. Do not adopt a
seed. Do not write a seed into Admissibility.

Displayed, not adopted.

Not leftover-character of #6490 (that scored `cov2` only).
Not leftover-character of #6473 (that named `Max(1)`).

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
content. A seed is likewise displayed data, not an admissibility rule.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Finite exact first-fill seed search of one displayed F_cut map on a twelve-vertex two-cube from size 3 through size 6."
trace_class: frontier_discovery
target_claim_id: f_cut_c00_first_fill_seed
target_blocker_text: "lex-first two-cube seed of size at least 3 that F_cut (1,0,0,0,0) fills"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the bounded first-fill claim; do not adopt the seed"
conditional_surface_status: "exact on the two-cube with off-patch o=0 for |S|<=6; the seed remains displayed data"
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
remaining-bit tuple is `(1,0,0,0,0)`.

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

Seeds are enumerated by increasing cardinality, then as combinations
of the lexicographic site list. The search starts at size `3` because
`cov2(f00)=0`, so the first fill has `|S|≥3`. The cap is size `6`.

## Theorem 1 — `cov2(f00)=0`

Among the `C(12,2)=66` unordered two-site seeds, `f00` fills none.
That is `cov2(f00)=0`. It reconfirms the `#6490` exception score for
this remaining-bit tuple. The one-site coverage is likewise `0`.
Those scores name when `f00` fails to fill; they do not name a seed
that succeeds.

## Theorem 2 — lex-first fill seed

Search the `220` three-site seeds in lex order. None fills.

Search the `495` four-site seeds in lex order. The first that fills is

`S={(0,0,0),(0,0,1),(0,1,0),(0,1,1)}`.

This is the entire `x=0` face of the two-cube. Its size is `|S|=4`.
Seven four-site seeds fill in all; the other six come later in lex
order. No five-site seed fills. Four six-site seeds fill. The
lex-first filler through the size-`6` cap is therefore this face.

## Theorem 3 — history from `S`; display, not adoption

Start with that `S`, so `|locks_0|=4`.

At tick `1` the four middle-slice sites
`(1,0,0)`, `(1,0,1)`, `(1,1,0)`, `(1,1,1)`
each see a single occupied nearest neighbor along `-x` (type `wt1`),
so `f00` returns `1`. The four `x=2` sites see the empty tuple and
stay unlocked. After tick `1` one has `|locks_1|=8`.

At tick `2` the four `x=2` sites each see a single occupied nearest
neighbor along `-x` (type `wt1`) and lock. The run fills:

`T=2`, `|locks_halt|=12`, history `(4, 8, 12)`, fill bit `1`.

The executed firings are the `wt1` orbit only. The seed is displayed
data. Do not adopt `f00`. Do not adopt this seed. Do not write a seed
into Admissibility. Admissibility is not a dynamics axiom and does not
supply this predicate or this seed. The seed is not written into
Admissibility.

A `cov2=0` score is not a first-fill seed. The first-fill seed is a
new finite object on this two-cube.

## Exact Target And Obligation Graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record wording | quoted; no edit |
| two-cube, off-patch `o=0`, lex seed order from size `3` | declared finite data |
| `cov2(f00)=0` | recomputed; `0` of `66` |
| first fill through size `6` | `{(0,0,0),(0,0,1),(0,1,0),(0,1,1)}` |
| `|S|` | `4` |
| history from that `S` | `(4, 8, 12)`; fills |
| adoption of the seed or the map | refused |
| formation site / rate from the axioms | open |

## Boundary And Imports

No observation, fit, continuum limit, or Hamming-as-`f_L1`
identification is imported. The two-cube, the predicate `f00`, and the
seed order are supplied mathematical data for this note. Record lock
language is quoted only as the existing lock/content/absence boundary;
it does not select this map or any seed.

## Promotion Value Gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers which first seed of size at least `3`, if any through size `6`, `f00` fills. |
| V2 | Current main has the axiom memo and the `#6490` `cov2=0` score, not this first-fill seed. |
| V3 | The twelve-vertex process through size `6` is independently finite and exact. |
| V4 | The theorem is more than restating Admissibility: it executes a supplied predicate the axiom does not name. |
| V5 | Neither the map nor the seed is an admissibility rule, and neither is adopted. |

## No-Go Discipline Gate

The negative content is narrow: a `cov2=0` exception is not a first-fill
seed, and a displayed filler or seed is not axiom content.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| two-site census | all `66` pairs | `cov2(f00)=0` |
| three-site census | all `220` triples | none fills |
| lex four-site search | first of `495` | `S={(0,0,0),(0,0,1),(0,1,0),(0,1,1)}` fills |
| five-site census | all `792` | none fills |
| six-site census | all `924` | four fill; later than `S` |
| history from `S` | occupancy-to-lock under `f00` | `(4, 8, 12)`; fills |
| Hamming parity | `|c|_1 mod 2` | different predicate; `adj2` even |
| write a seed or map into Admissibility | treat either as the local rule | refused; axiom is not a dynamics axiom |

### N2 — wall independence

The missing formation-site selector, the missing axiom-level
occupancy rule, and the choice among displayed members are distinct
open items. This note claims no complete wall and no compiler no-go.

### N3 — hidden-condition scan

The two-cube, off-patch `o=0`, lex site order, size window `3` through
`6`, six-neighbor order, and the remaining-bit tuple `(1,0,0,0,0)` are
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
| per site | every two-cube vertex against `f00` | no derived kernel values |
| per mode | no mode calculation | no spectral exhaustion |
| per block | all seeds of size `2` through `6` | no physical compiler |
| lattice wide | checked and not executed | neither map nor the seed adopted as a rule |

### N6 — live partial-closure paths

Live routes include an independent reason to select or reject `f00`,
a first-fill seed of the other `#6490` exception `(1,1,0,0,0)`, and a
formation mechanism supplied by something other than a displayed
predicate.

### N7 — hostile steelman

**Steelman:** `cov2=0` already says this map never fills a small seed,
so either it never fills or any large enough face may be treated as
the formation seed and written as a rule.

**Answer:** A four-site face already fills, and the lex-first such
seed is `{(0,0,0),(0,0,1),(0,1,0),(0,1,1)}`. That is a displayed
finite fact. Admissibility does not name `f00` or this seed.

### N8 — cross-cycle echo

A `cov2` ranking of the `32` maps (`#6490`) and a one-site coverage
of this pair (`#6473`) are different claims. This note executes the
lex-first seed that `F_cut` `(1,0,0,0,0)` fills.

**Gate disposition:** PASS for the finite first-fill statement and the
displayed history. FAIL / DO NOT SHIP for “adopt `f00`,” “write a seed
into Admissibility,” or “`cov2=0` already is the first-fill seed.”

## Primary Runner

The primary runner rebuilds the two-cube, the predicate `f00`, the
two-site `cov2` reconfirmation, the lex search from size `3` through
size `6`, the first-fill seed with its history and fill bit, the
`wt1` face-to-face waves, the current premise boundary, and the
non-adoption wording. It authors no audit verdict.
