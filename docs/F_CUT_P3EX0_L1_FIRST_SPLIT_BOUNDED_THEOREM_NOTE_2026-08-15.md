---
claim_id: f_cut_p3ex0_l1_first_split_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On the two-cube with off-patch o=0, the lex-first seed of size at most 3 at which f_L1 and F_cut (0,0,1,1,0) disagree on fill is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_p3ex0_l1_first_split_2026_08_15.py
---

# First Two-Cube Seed Of Size At Most Three Where `f_L1` And `F_cut` `(0,0,1,1,0)` Disagree On Fill

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** displayed occupancy-to-lock dynamics of two cube-covariant
maps on the twelve-vertex two-cube `{0,1,2}×{0,1}×{0,1}`, started from
every nonempty seed of size at most three, with off-patch occupancy
identically `0`. The first seed at which `f_L1` and
`F_cut (0,0,1,1,0)` disagree on fill is displayed, not adopted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_p3ex0_l1_first_split_2026_08_15.py`](../scripts/f_cut_p3ex0_l1_first_split_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

Write the two-cube as the twelve sites `{0,1,2}×{0,1}×{0,1}`. A site
locks when a displayed predicate of its six-neighbor occupancy tuple
returns `1`. Off-patch neighbors contribute occupancy `0`. A
blank-block is a different rule; it is not used. A run is the tuple of lock-set
cardinalities from the seed through halt, together with the fill bit
`|locks_halt|=12`. Three-site coverage is

```text
cov3(f) = |{ S : |S|=3 and f fills from S }|.
```

The displayed selector on remaining bits
`(wt1, opp2, adj2, vertex3, mixed3)` is

```text
P(f) := (wt1=1) and (adj2, vertex3, mixed3) ≠ (0, 0, 0).
```

Let `f_L1(c)=1` if and only if some axis is unbalanced: `c_{+μ} ≠ c_{-μ}`
for at least one `μ ∈ {x,y,z}`. Equivalently, some discrete neighbor
contrast `n_μ = c_{+μ} − c_{-μ}` is nonzero. This is **not** Hamming parity
`|c|_1 mod 2`. `f_L1` is the 10-orbit reading `n ≠ 0`, not Hamming.
Its remaining-bit tuple is

```text
(wt1, opp2, adj2, vertex3, mixed3) = (1, 0, 1, 1, 1)
```

Let `f_ex0` be the `F_cut` remaining-bit map

```text
(wt1, opp2, adj2, vertex3, mixed3) = (0, 0, 1, 1, 0)
```

with complements forced. It fires on the `adj2`/`adj4` pair and on
`vertex3`, and nowhere else. It is the lex-first `#6502` map with
`P=0` and `cov3>0`.

New map versus `f_L1`, not leftover of `F_W0` remaining-bit splits.
`#6502` named this map by the selector-coverage pair `(P, cov3)`. The
present object is the first `|S|≤3` seed at which the two maps disagree
on fill.

Enumerate nonempty seeds `S` by increasing `|S|`, then lexicographic
site order, through `|S|≤3` (`12+66+220=298` seeds).

**Theorem 1.** `P(f_ex0)=0` and `cov3(f_ex0)=24`.

**Theorem 2.** The lex-first nonempty seed of size at most three at
which `f_L1` and `f_ex0` disagree on fill is `S={(0,0,0)}`.

**Theorem 3.** From that `S`, `f_L1` has lock history `(1, 4, 8, 11, 12)`
and fills. `f_ex0` has lock history `(1)` and does not fill.
The seed and both histories are displayed only. Do not adopt `f_ex0`.
Do not adopt `f_L1`. Do not write a seed into Admissibility.

Displayed, not adopted.

Not leftover of `F_W0` remaining-bit splits. Those splits stay inside
the `wt1=0` class. This note compares this `#6502` map to `f_L1`.

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
predicate. The maps `f_L1` and `f_ex0` are supplied displayed members,
not axiom content. A seed is likewise displayed data, not an
admissibility rule.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Finite exact seed census of two displayed occupancy-to-lock maps on a twelve-vertex two-cube through size 3."
trace_class: frontier_discovery
target_claim_id: f_cut_p3ex0_l1_first_split
target_blocker_text: "lex-first two-cube seed of size at most 3 at which f_L1 and F_cut (0,0,1,1,0) disagree on fill"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the bounded seed-census claim; do not adopt either map or the seed"
conditional_surface_status: "exact on the two-cube with off-patch o=0 for |S|<=3; both maps remain displayed members"
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
| full | `(0,3,0)` | `(1,1,1,1,1,1)` |

`F_cut` is the cube-covariant class with `f(empty)=f(full)=0` and
`f(c)=f(1-c)`. Five remaining bits stay free, so `|F_cut|=32`. Those
bits are ordered `(wt1, opp2, adj2, vertex3, mixed3)`.

`f_L1(c)=1` iff `n_unbalanced(c)≥1`. Its remaining-bit tuple is
`(1,0,1,1,1)`.
`f_ex0(c)=1` iff the axis type is `adj2=(2,0,1)`, its complement
`adj4`, or `vertex3=(3,0,0)`. Its remaining-bit tuple is `(0,0,1,1,0)`.

On those representatives the bits are

| map | wt1 | opp2 | adj2 | type210 | vertex3 | mixed3 | empty | full |
|---|---|---|---|---|---|---|---|---|
| `f_L1` | 1 | 0 | 1 | 1 | 1 | 1 | 0 | 0 |
| `f_ex0` | 0 | 0 | 1 | 1 | 1 | 0 | 0 | 0 |

The maps disagree on `wt1` and `mixed3`. Hamming parity of `|c|_1` is a
different predicate: `adj2` is even and `f_L1(adj2)=1`.

One tick locks every currently unlocked on-patch site whose neighbor
tuple has `f=1`. The process starts with `locks_0=S` and halts at the
first fixed point, or at tick `12`. Lock history is the sequence of
cardinalities from `t=0` through halt. Fill means `|locks_halt|=12`.

Seeds are enumerated by increasing cardinality, then as combinations
of the lexicographic site list. That census is `12+66+220=298` nonempty
seeds of size at most three. It is a seed census on this two-cube, not
an occupancy-step clone of a previously displayed single seed.

## Theorem 1 — selector and three-site coverage

Reconfirm the `#6502` pair for this map.

`P` reads the remaining bits only. `f_ex0` has `wt1=0`, so `P(f_ex0)=0`.
There are `C(12,3)=220` unordered three-site seeds. Independent
execution of every such seed gives `cov3(f_ex0)=24`. Equivalently,
`f_ex0` fills twenty-four of the two hundred twenty three-site seeds
and misses the rest.

`P=0` already forces `cov2(f_ex0)=0` by the `#6494` two-site selector,
which is leftover-character of that coverage score. It is not the
residual of this note. The residual is the first seed at which `f_L1`
and `f_ex0` disagree on fill.

## Theorem 2 — first seed where the maps disagree on fill

Among the 298 nonempty seeds of size at most three, ordered by
increasing `|S|` then lexicographic combination of the site list, the
first seed at which `f_L1` and `f_ex0` disagree on fill is the lex-first
one-site seed

`S={(0,0,0)}`.

On that seed `f_L1` fills and `f_ex0` does not. Every later one-site
seed is also an `f_L1` fill and an `f_ex0` miss, but those seeds are
later in the lex order. No smaller nonempty seed exists. So a
distinguishing fill-split exists inside the `|S|≤3` cap, and it already
occurs at `|S|=1`.

`f_ex0` fills none of the twelve one-site seeds, none of the sixty-six
two-site seeds, and twenty-four of the 220 three-site seeds. `f_L1`
fills all twelve one-site seeds, sixty-two of the sixty-six two-site
seeds, and all 220 three-site seeds.

## Theorem 3 — both histories from `S`, display not adoption

Start with `S={(0,0,0)}`, so `|locks_0|=1`.

The first wave is already a split. The three sites
`(0,0,1)`, `(0,1,0)`, `(1,0,0)`
each see a single occupied nearest neighbor (type `wt1`). Then
`f_L1=1` and `f_ex0=0`. Every other unlocked site sees the empty tuple
and stays unlocked.

Therefore `f_L1` locks those three `wt1` neighbors at tick `1`,
reaching four locks, and then continues:

`T=4`, `|locks_halt|=12`, history `(1, 4, 8, 11, 12)`, fill bit `1`.

`f_ex0` never fires on `wt1`, so it adds no site and halts at the seed:

`T=0`, `|locks_halt|=1`, history `(1)`, fill bit `0`.

The executed split is the `wt1` orbit on the first wave. `f_ex0` has
`wt1=0` and `mixed3=0`, so it cannot leave a one-site seed on this
patch.

The first distinguishing fill-split seed is displayed only. Do not
adopt `f_ex0`. Do not adopt `f_L1`. Do not write a seed into Admissibility.
Admissibility is not a dynamics axiom and does not supply this
predicate or this seed. The seed is not written into Admissibility.
Do not adopt a bit.

Agreement later, on some three-site seeds that `f_ex0` does fill, is
path coincidence on `adj2`/`vertex3`, not identity of maps.
Disagreement at the lex-first one-site seed is a displayed finite fact,
not a reason to treat either member as axiom content.

## Exact Target And Obligation Graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record wording | quoted; no edit |
| two-cube, off-patch `o=0`, lex seed order, `|S|≤3` | declared finite data |
| `P(f_ex0)=0` and `cov3(f_ex0)=24` | recomputed; #6502 scores |
| first fill-split seed | `{(0,0,0)}` |
| both histories | `(1, 4, 8, 11, 12)` and `(1)` |
| both fill bits | `f_L1` fills; `f_ex0` does not |
| identity of the two maps | refused; they disagree on `wt1` |
| adoption of either map or the seed | refused |
| formation site / rate from the axioms | open |

## Boundary And Imports

No observation, fit, continuum limit, or Hamming-as-`f_L1`
identification is imported. The two-cube, the two predicates, and the
seed order are supplied mathematical data for this note. Record lock
language is quoted only as the existing lock/content/absence boundary;
it does not select either map or any seed.

## Promotion Value Gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers which first `|S|≤3` seed, if any, is a fill disagreement of `f_L1` and `f_ex0`. |
| V2 | Current main has the axiom memo and no landed first-fill-split census of these two maps. |
| V3 | The 298-seed twelve-vertex process is independently finite and exact. |
| V4 | The theorem is more than restating Admissibility: it executes two supplied predicates the axiom does not name. |
| V5 | Neither map nor the seed is an admissibility rule, and none is adopted. |

## No-Go Discipline Gate

The negative content is narrow: a first fill-split seed is not
predicate identity, and a displayed filler or seed is not axiom
content.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| selector `P` | remaining bits of `f_ex0` | `P(f_ex0)=0` because `wt1=0` |
| 3-site coverage | all 220 triples | `cov3(f_ex0)=24` |
| lex census through size 3 | 298 seeds | first fill-split at `{(0,0,0)}` |
| `f_L1` from that `S` | some-axis-unbalanced predicate | fills; history `(1, 4, 8, 11, 12)` |
| `f_ex0` from that `S` | remaining bits `(0,0,1,1,0)` | does not fill; history `(1)` |
| `wt1` distinction | evaluate both maps on `(1,0,2)` | they disagree; maps stay distinct |
| Hamming parity | `|c|_1 mod 2` | different predicate; `adj2` even |
| write a seed or map into Admissibility | treat either as the local rule | refused; axiom is not a dynamics axiom |

### N2 — wall independence

The missing formation-site selector, the missing axiom-level
occupancy rule, and the choice among displayed members are distinct
open items. This note claims no complete wall and no compiler no-go.

### N3 — hidden-condition scan

The two-cube, off-patch `o=0`, lex site order, size cap 3,
six-neighbor order, and both predicates are declared. Cube covariance
is used only as the axis-type reading of a six-tuple. No continuum,
Hamming, or admissibility rewrite is assumed.

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
| per site | every two-cube vertex against both predicates | no derived kernel values |
| per mode | no mode calculation | no spectral exhaustion |
| per block | all 298 seeds of size at most 3 | no physical compiler |
| lattice wide | checked and not executed | neither map nor the seed adopted as a rule |

### N6 — live partial-closure paths

Live routes include an independent reason to select or reject either
map, a larger-seed census, and a formation mechanism supplied by
something other than a displayed predicate.

### N7 — hostile steelman

**Steelman:** `f_ex0` is only the lex-first `#6502` `P=0` `cov3>0`
tuple, so the fill-split versus `f_L1` may already be leftover of
`F_W0` remaining-bit splits inside the `wt1=0` class, or the maps may
still agree on every seed `f_L1` fills.

**Answer:** `F_W0` remaining-bit splits stay inside the `wt1=0` class.
This note compares the `#6502` map `(0,0,1,1,0)` to `f_L1`. The
lex-first size-at-most-three seed `{(0,0,0)}` already splits fill:
`f_L1` fills with history `(1, 4, 8, 11, 12)` and `f_ex0` halts at the
seed with history `(1)`. The maps also disagree on `wt1`. Admissibility
does not name either map or this seed.

### N8 — cross-cycle echo

A `F_W0` remaining-bit split and a raw `(P, cov3)` score (#6502) are
different claims. This note executes the first `|S|≤3` seed at which
`f_L1` and `F_cut (0,0,1,1,0)` disagree on fill.

**Gate disposition:** PASS for the finite first-seed statement and the
displayed histories. FAIL / DO NOT SHIP for “adopt `f_ex0`,” “adopt
`f_L1`,” “write a seed into Admissibility,” or “the maps are the same
dynamics on every two-cube seed `f_L1` fills.”

## Primary Runner

The primary runner rebuilds the two-cube, both predicates, the 298-seed
lex census, the selector bit and three-site coverage, the first
fill-split seed with both histories and both fill bits, the `wt1` split
on the first wave, the current premise boundary, and the non-adoption
wording. It authors no audit verdict.
