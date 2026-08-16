---
claim_id: f_cut_mix1_first_fill_seed_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On the two-cube with off-patch o=0, the lex-first seed that F_cut (1,0,0,0,1) fills is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_mix1_first_fill_seed_2026_08_15.py
---

# Lex-First Two-Cube Seed That `F_cut` `(1,0,0,0,1)` Fills

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** displayed occupancy-to-lock dynamics of one cube-covariant
map on the twelve-vertex two-cube `{0,1,2}×{0,1}×{0,1}`, started from
seeds ordered by increasing size then lexicographic site order, with
off-patch occupancy identically `0`. The lex-first seed that fills is
displayed, not adopted.
**Audit-status authority:** independent audit lane only. This note authors no audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_mix1_first_fill_seed_2026_08_15.py`](../scripts/f_cut_mix1_first_fill_seed_2026_08_15.py)
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

Let `f_mix1` be the newly named `F_cut` remaining-bit map

```text
(wt1, opp2, adj2, vertex3, mixed3) = (1, 0, 0, 0, 1)
```

with complements forced. It fires on axis types `(1,0,2)`, `(1,2,0)`,
and mixed3 `(1,1,1)`. Selector `P` of `#6502` is
`P(f) := (wt1=1)` and `(adj2,vertex3,mixed3)≠(0,0,0)`;
`P(f_mix1)=1`. Those coverage and selector scores are leftover-character
of `#6510`/`#6502`. The object of this note is the first seed `f_mix1`
fills.

Enumerate seeds `S` by increasing `|S|`, then lexicographic site
order, starting at `|S|=1`.

**Theorem 1.** `cov2(f_mix1)=8`, `cov1=0`, and `cov3=0`. This
reconfirms the `#6510`/`#6502` scores.

**Theorem 2.** The lex-first seed that `f_mix1` fills is the size-`2`
edge

`S={(0,0,0),(0,0,1)}`.

So `|S|=2`. Eight of the `66` two-site seeds fill; the edge above is
the first in lex order. None of the `12` one-site seeds fill. None of
the `220` three-site seeds fill.

**Theorem 3.** From that `S`, the lock history is `(2, 6, 8, 10, 12)`
and the run fills. The seed, the history, and the remaining-bit tuple
are displayed only. Do not adopt a bit. Do not adopt a seed. Do not
write a seed or a remaining bit into Admissibility.

Displayed, not adopted.

Not leftover-character of #6510 (that scored `cov2=8`, `cov3=0`,
`cov1=0` only).
Not leftover-character of #6502 (that named `P`).
New first fill of a newly named map.

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
predicate. The map `f_mix1` is a supplied displayed member, not axiom
content. A seed is likewise displayed data, not an admissibility rule.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Finite exact first-fill seed search of one displayed F_cut map on a twelve-vertex two-cube."
trace_class: frontier_discovery
target_claim_id: f_cut_mix1_first_fill_seed
target_blocker_text: "lex-first two-cube seed that F_cut (1,0,0,0,1) fills"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the bounded first-fill claim; do not adopt the seed"
conditional_surface_status: "exact on the two-cube with off-patch o=0; the seed remains displayed data"
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
`f_mix1(c)=1` iff the axis type is `wt1=(1,0,2)`, `wt5=(1,2,0)`, or
`mixed3=(1,1,1)`. Its remaining-bit tuple is `(1,0,0,0,1)`.

On those representatives the bits are

| map | wt1 | opp2 | adj2 | type210 | vertex3 | mixed3 | empty | full |
|---|---|---|---|---|---|---|---|---|
| `f_L1` | 1 | 0 | 1 | 1 | 1 | 1 | 0 | 0 |
| `f_mix1` | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 |

Hamming parity of `|c|_1` is a different predicate: `opp2` is even and
`f_L1(opp2)=0`, while `adj2` is even and `f_L1(adj2)=1`.

One tick locks every currently unlocked on-patch site whose neighbor
tuple has `f=1`. The process starts with `locks_0=S` and halts at the
first fixed point, or at tick `12`. Lock history is the sequence of
cardinalities from `t=0` through halt. Fill means `|locks_halt|=12`.

Seeds are enumerated by increasing cardinality, then as combinations
of the lexicographic site list.

## Theorem 1 — `cov2=8`, `cov1=0`, `cov3=0`

Among the `C(12,1)=12` one-site seeds, `f_mix1` fills none:
`cov1=0`. Among the `C(12,2)=66` two-site seeds it fills eight:
`cov2=8`. Among the `C(12,3)=220` three-site seeds it fills none:
`cov3=0`. Those scores reconfirm `#6510`/`#6502`. They name when
`f_mix1` fills or fails; they do not name the lex-first seed that
succeeds.

## Theorem 2 — lex-first fill seed

Search the `12` one-site seeds in lex order. None fills.

Search the `66` two-site seeds in lex order. The first that fills is

`S={(0,0,0),(0,0,1)}`.

This is the `z`-edge of the `x=0` face at `y=0`. Its size is `|S|=2`.
Eight two-site seeds fill in all: the four edges of the `x=0` face and
the four edges of the `x=2` face. The other seven come later in lex
order. No three-site seed fills. The lex-first filler is therefore
this edge.

## Theorem 3 — history from `S`; display, not adoption

Start with that `S`, so `|locks_0|=2`.

At tick `1` four sites lock as type `wt1`: the remaining `x=0` face
`(0,1,0)`, `(0,1,1)` and the middle-slice `y=0` pair `(1,0,0)`,
`(1,0,1)`. After tick `1` one has `|locks_1|=6`.

At tick `2` the `x=2`, `y=0` edge `(2,0,0)`, `(2,0,1)` each see a
single occupied nearest neighbor along `-x` (type `wt1`) and lock.
After tick `2` one has `|locks_2|=8`.

At tick `3` the remaining `x=2` face `(2,1,0)`, `(2,1,1)` lock as type
`wt1`. After tick `3` one has `|locks_3|=10`.

At tick `4` the leftover middle-slice pair `(1,1,0)`, `(1,1,1)` each
see axis type `mixed3=(1,1,1)` and lock. The run fills:

`T=4`, `|locks_halt|=12`, history `(2, 6, 8, 10, 12)`, fill bit `1`.

The last wave uses the `mixed3` remaining bit. The seed and the
remaining-bit tuple are displayed data. Do not adopt a bit. Do not
adopt `f_mix1`. Do not adopt this seed. Do not write a seed or a
remaining bit into Admissibility. Admissibility is not a dynamics
axiom and does not supply this predicate or this seed. The seed is not
written into Admissibility.

A `cov2=8` score is not a first-fill seed. The first-fill seed is a
new finite object on this two-cube.

## Exact Target And Obligation Graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record wording | quoted; no edit |
| two-cube, off-patch `o=0`, lex seed order | declared finite data |
| `cov2=8`, `cov1=0`, `cov3=0` | recomputed |
| first fill | `{(0,0,0),(0,0,1)}` |
| `|S|` | `2` |
| history from that `S` | `(2, 6, 8, 10, 12)`; fills |
| adoption of a bit, the seed, or the map | refused |
| formation site / rate from the axioms | open |

## Boundary And Imports

No observation, fit, continuum limit, or Hamming-as-`f_L1`
identification is imported. The two-cube, the predicate `f_mix1`, and
the seed order are supplied mathematical data for this note. Record
lock language is quoted only as the existing lock/content/absence
boundary; it does not select this map or any seed.

## Promotion Value Gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers which first seed `f_mix1` fills. |
| V2 | Current main has the axiom memo and the `#6510`/`#6502` coverage scores, not this first-fill seed. |
| V3 | The twelve-vertex process through size `3` is independently finite and exact. |
| V4 | The theorem is more than restating Admissibility: it executes a supplied predicate the axiom does not name. |
| V5 | Neither the map nor the seed is an admissibility rule, and neither is adopted. |

## No-Go Discipline Gate

The negative content is narrow: a coverage score is not a first-fill
seed, and a displayed filler, remaining bit, or seed is not axiom
content.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| one-site census | all `12` sites | `cov1=0` |
| two-site census | all `66` pairs | `cov2=8` |
| lex two-site search | first of `66` | `S={(0,0,0),(0,0,1)}` fills |
| three-site census | all `220` triples | `cov3=0` |
| history from `S` | occupancy-to-lock under `f_mix1` | `(2, 6, 8, 10, 12)`; fills |
| Hamming parity | `|c|_1 mod 2` | different predicate; `adj2` even |
| write a bit, seed, or map into Admissibility | treat any as the local rule | refused; axiom is not a dynamics axiom |

### N2 — wall independence

The missing formation-site selector, the missing axiom-level
occupancy rule, and the choice among displayed members are distinct
open items. This note claims no complete wall and no compiler no-go.

### N3 — hidden-condition scan

The two-cube, off-patch `o=0`, lex site order, six-neighbor order, and
the remaining-bit tuple `(1,0,0,0,1)` are declared. Cube covariance is
used only as the axis-type reading of a six-tuple. No continuum,
Hamming, or admissibility rewrite is assumed.

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
| per site | every two-cube vertex against `f_mix1` | no derived kernel values |
| per mode | no mode calculation | no spectral exhaustion |
| per block | all seeds of size `1` through `3` | no physical compiler |
| lattice wide | checked and not executed | neither map nor the seed adopted as a rule |

### N6 — live partial-closure paths

Live routes include an independent reason to select or reject
`f_mix1`, a first-fill seed of another newly named `F_cut` map, and a
formation mechanism supplied by something other than a displayed
predicate.

### N7 — hostile steelman

**Steelman:** `cov2=8` already says this map fills eight pairs, so any
of those pairs may be treated as the formation seed and written as a
rule, and the `mixed3` bit may be adopted because the last wave uses
it.

**Answer:** The lex-first such seed is `{(0,0,0),(0,0,1)}`, with
history `(2, 6, 8, 10, 12)`. That is a displayed finite fact. Do not
adopt a bit. Admissibility does not name `f_mix1` or this seed.

### N8 — cross-cycle echo

A coverage ranking of the `32` maps (`#6510`) and the selector `P`
(`#6502`) are different claims. This note executes the lex-first seed
that `F_cut` `(1,0,0,0,1)` fills.

**Gate disposition:** PASS for the finite first-fill statement and the
displayed history. FAIL / DO NOT SHIP for “adopt `f_mix1`,” “adopt a
bit,” “write a seed into Admissibility,” or “`cov2=8` already is the
first-fill seed.”

## Primary Runner

The primary runner rebuilds the two-cube, the predicate `f_mix1`, the
`cov1`/`cov2`/`cov3` reconfirmation, the lex search, the first-fill
seed with its history and fill bit, the `wt1` then `mixed3` waves, the
current premise boundary, and the non-adoption wording. It authors no
audit verdict.
