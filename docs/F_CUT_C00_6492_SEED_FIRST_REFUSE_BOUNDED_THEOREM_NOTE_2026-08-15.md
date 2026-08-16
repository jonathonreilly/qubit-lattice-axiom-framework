---
claim_id: f_cut_c00_6492_seed_first_refuse_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On the two-cube with off-patch o=0, the first refused neighborhood of F_cut (1,0,0,0,0) on the #6492 seed {(0,0,0),(1,1,1),(2,0,0)} is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_c00_6492_seed_first_refuse_2026_08_15.py
---

# First Refused Neighborhood Of `F_cut` `(1,0,0,0,0)` On The `#6492` Seed

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** displayed occupancy-to-lock dynamics of one cube-covariant
map on the twelve-vertex two-cube `{0,1,2}×{0,1}×{0,1}`, started from
the displayed three-site seed `S={(0,0,0),(1,1,1),(2,0,0)}`, with
off-patch occupancy identically `0`. The first neighborhood that
`F_cut (1,0,0,0,0)` refuses on that run is displayed, not adopted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_c00_6492_seed_first_refuse_2026_08_15.py`](../scripts/f_cut_c00_6492_seed_first_refuse_2026_08_15.py)
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
`(1,2,0)`. The displayed seed is the `#6492` first split of the two
`wt1=1`, `cov2=0` maps:

```text
S = {(0,0,0), (1,1,1), (2,0,0)}.
```

This is a new seed object: not L1-miss-why and not a second named-pair fill.
`#6492` reported the fill bits of `f00` versus `f10=(1,1,0,0,0)`.
The object of this note is the first neighborhood `f00` refuses on the
run from that displayed seed.

**Theorem 1.** From `S`, `f00` has lock history `(3, 11)` and does not
fill. The history ends before `12`.

**Theorem 2.** The run does fire a remaining-bit orbit after the seed:
eight unlocked sites present a `wt1` cell and lock. The lex-first
refused neighborhood, ordered by tick then site, is the `opp2` cell at
tick `0` on site `(1,0,0)`:

```text
cell = (1,1,0,0,0,0),    axis type (0,1,2),    remaining bit opp2.
```

After that wave the leftover site sees an `adj4` cell of type `(2,1,0)`,
the `adj2` remaining bit, which `f00` also refuses. That later refuse
is not first.

**Theorem 3.** Display. Do not adopt a bit. Do not adopt `opp2`. Do not
write a remaining bit into Admissibility.

Displayed, not adopted.

Not leftover-character of L1-miss-why (that asked why `f_L1` misses four
two-site seeds).
Not leftover-character of `#6492` as a named-pair fill (that scored the
fill bits of `f00` versus `f10`).
New finite object: the first refused neighborhood of `f00` on this seed.

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
claim_type_reason: "Finite exact first-refuse neighborhood of one displayed F_cut map on a twelve-vertex two-cube from the #6492 seed."
trace_class: frontier_discovery
target_claim_id: f_cut_c00_6492_seed_first_refuse
target_blocker_text: "lex-first neighborhood that F_cut (1,0,0,0,0) refuses on the #6492 seed"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the bounded first-refuse claim; do not adopt a bit"
conditional_surface_status: "exact on the two-cube with off-patch o=0 from the displayed seed; the refused bit remains displayed data"
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

`adj4` is the complement of `adj2`: axis type `(2,1,0)`, the same
remaining bit as `adj2`. `opp4` is the complement of `opp2`: axis type
`(0,2,1)`, the same remaining bit as `opp2`. Empty and full are not
remaining-bit orbits.

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

A refused neighborhood on the run is an unlocked site at some tick
whose six-neighbor cell has `f00=0`. Events are ordered by increasing
tick, then lexicographic site. The first such event is the first
refused neighborhood. Remaining-bit labels, axis types, and orbit
names are the three equivalent readings of that cell.

## Theorem 1 — `f00` does not fill from `S`

Start with `S={(0,0,0),(1,1,1),(2,0,0)}`, so `|locks_0|=3`. One tick
locks eight sites and leaves `(1,0,0)` unlocked. The process then
halts: history `(3, 11)`, fill bit `0`. The history ends before `12`.
This reconfirms the `#6492` `f00` miss on this seed.

## Theorem 2 — first refused neighborhood

At tick `0` the nine unlocked sites present two orbit types:

- eight sites see a `wt1` cell of type `(1,0,2)` and lock, because
  `f00` has remaining bit `wt1=1`;
- the leftover site `(1,0,0)` sees the cell `(1,1,0,0,0,0)`, the
  `opp2` representative of type `(0,1,2)`, and stays unlocked,
  because `f00` has remaining bit `opp2=0`.

The run therefore does fire a remaining-bit orbit after the seed
(`wt1`). The report is not “never fires a remaining-bit orbit after
the seed.”

The unique refuse at tick `0` is already first in tick-then-site
order: site `(1,0,0)`, orbit `opp2`, type `(0,1,2)`, remaining bit
`opp2`.

After the wave, `|locks_1|=11` and the leftover site sees

```text
(1,1,1,0,1,0),    axis type (2,1,0),    orbit adj4,    remaining bit adj2.
```

`f00` refuses that cell as well, so the process halts unfilled. The
`adj2` refuse is later than the `opp2` refuse.

## Theorem 3 — display, not adoption

The first refuse is displayed data. Do not adopt a bit. Do not adopt
`opp2`. Do not adopt `adj2`. Do not write a remaining bit into
Admissibility. Admissibility is not a dynamics axiom and does not
supply this predicate, this seed, or this refuse. The refused
neighborhood is not written into Admissibility.

A named-pair fill bit is not a first refused neighborhood. The first
refuse is a new finite object on this two-cube.

## Exact Target And Obligation Graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record wording | quoted; no edit |
| two-cube, off-patch `o=0`, seed `S` | declared finite data |
| `f00` history from `S` | `(3, 11)`; no fill |
| first refuse, or “never fires a remaining-bit orbit after the seed” | `opp2` at tick `0` on `(1,0,0)` |
| later refuse on the leftover site | `adj4` / `adj2`; not first |
| adoption of a remaining bit | refused |
| formation site / rate from the axioms | open |

## Boundary And Imports

No observation, fit, continuum limit, or Hamming-as-`f_L1`
identification is imported. The two-cube, the predicate `f00`, and the
seed `S` are supplied mathematical data for this note. Record lock
language is quoted only as the existing lock/content/absence boundary;
it does not select this map or any remaining bit.

## Promotion Value Gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers which first neighborhood, if any, `f00` refuses on the `#6492` seed. |
| V2 | Current main has the axiom memo and the `#6492` fill-bit split, not this first refuse. |
| V3 | The twelve-vertex process from one displayed seed is independently finite and exact. |
| V4 | The theorem is more than restating Admissibility: it executes a supplied predicate the axiom does not name. |
| V5 | Neither the map nor a remaining bit is an admissibility rule, and neither is adopted. |

## No-Go Discipline Gate

The negative content is narrow: a named-pair fill bit is not a first
refuse, and a displayed refuse or remaining bit is not axiom content.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| history from `S` | occupancy-to-lock under `f00` | `(3, 11)`; no fill |
| remaining-bit fire after the seed | unlocked cells at tick `0` | eight `wt1` cells fire |
| first refuse, tick then site | unlocked cells with `f00=0` | `opp2` at `(1,0,0)` |
| later leftover cell | tick `1` on `(1,0,0)` | `adj4` / `adj2`; not first |
| Hamming parity | `|c|_1 mod 2` | different predicate; `adj2` even |
| write a bit into Admissibility | treat `opp2` as the local rule | refused; axiom is not a dynamics axiom |

### N2 — wall independence

The missing formation-site selector, the missing axiom-level
occupancy rule, and the choice among displayed remaining bits are
distinct open items. This note claims no complete wall and no compiler
no-go.

### N3 — hidden-condition scan

The two-cube, off-patch `o=0`, the displayed seed
`S={(0,0,0),(1,1,1),(2,0,0)}`, six-neighbor order, and the
remaining-bit tuple `(1,0,0,0,0)` are declared. Cube covariance is
used only as the axis-type reading of a six-tuple. No continuum,
Hamming, or admissibility rewrite is assumed.

### N4 — source residual matching

The axiom memo supplies the cubic nearest-neighbor graph and states
that Admissibility is not a dynamics axiom and does not supply the
formation site, probability, or rate. The extra therefore matches
those sources: a displayed lock predicate and a displayed refuse are
extra data.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | axis-type representatives and off-patch `0` | no alphabet classification |
| per site | every two-cube vertex against `f00` | no derived kernel values |
| per mode | no mode calculation | no spectral exhaustion |
| per block | the displayed seed through halt | no physical compiler |
| lattice wide | checked and not executed | neither map nor a bit adopted as a rule |

### N6 — live partial-closure paths

Live routes include an independent reason to select or reject `f00`,
the first refuse of the sibling map `f10` on the same seed, and a
formation mechanism supplied by something other than a displayed
predicate.

### N7 — hostile steelman

**Steelman:** `#6492` already said `f00` misses this seed because it
lacks the `opp2` bit, so the first refuse is just that fill-bit score
and may be written as a rule.

**Answer:** The fill bit is a halt cardinality. The first refuse is a
tick, a site, an orbit, an axis type, and a remaining-bit label on a
concrete six-neighbor cell. That is a displayed finite fact.
Admissibility does not name `f00` or `opp2`.

### N8 — cross-cycle echo

A two-site miss mechanism for `f_L1` (L1-miss-why) and a named-pair
fill split of `f00` versus `f10` (`#6492`) are different claims. This
note executes the first refused neighborhood of `F_cut` `(1,0,0,0,0)`
on the displayed `#6492` seed.

**Gate disposition:** PASS for the finite first-refuse statement and the
displayed history. FAIL / DO NOT SHIP for “adopt `opp2`,” “write a bit
into Admissibility,” or “the `#6492` fill bit already is the first
refuse.”

## Primary Runner

The primary runner rebuilds the two-cube, the predicate `f00`, the
history from `S`, the first-refuse event, the later `adj4` leftover
cell, the current premise boundary, and the non-adoption wording. It
authors no audit verdict.

## What This Does Not Claim

- The two-cube is not claimed to be a physically derived finite world.
- The `opp2` bit is not adopted, and `f00` is not selected as a physical law.
- No claim is made that Record locks, or refuses, on `opp2` cells.
- The later `adj4` refuse is not the first refuse.
- Independent class leftovers are not used as parents.

These are scope boundaries, not impossibility or route-exhaustion claims.
Accordingly, no no-go verdict is authored here.

## Live Parent Quotes

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

> There is one fixed nearest-neighbor admissibility rule, covariant under lattice
> translations and proper cubic rotations.

> For each site, the probability distribution over the possibilities is
> determined by, and varies with, the nearest-neighbor conditions.

> The full one-site possibility domain has algebraic presentation `M_2(C)`.

> When present, a record locks exactly one admissible local possibility.

> A site with no record cannot be read.

Their dependency role is limited to the repository's site, nearest-neighbor,
and lock vocabulary. This theorem separately supplies the two-cube, the
`F_cut` coding, and the refuse census; physical interpretation of `opp2`
remains outside its target.

On the two-cube with off-patch o=0, the first refused neighborhood of F_cut (1,0,0,0,0) on the #6492 seed {(0,0,0),(1,1,1),(2,0,0)} is reported. Displayed, not adopted.
