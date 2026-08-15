---
claim_id: f_min_l1_first_distinguishing_seed_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On the two-cube with off-patch o=0, the first nonempty seed of size at most 3 at which f_min and f_L1 disagree in halt history or fill is S={(0,0,0),(2,1,1)}. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_min_l1_first_distinguishing_seed_2026_08_15.py
---

# First Two-Cube Seed Of Size At Most Three Where `f_min` And `f_L1` Disagree

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** displayed occupancy-to-lock dynamics of two cube-covariant
maps on the twelve-vertex two-cube `{0,1,2}×{0,1}×{0,1}`, started from
every nonempty seed of size at most three, with off-patch occupancy
identically `0`. The first distinguishing seed is displayed, not adopted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/f_min_l1_first_distinguishing_seed_2026_08_15.py`](../scripts/f_min_l1_first_distinguishing_seed_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

Write the two-cube as the twelve sites `{0,1,2}×{0,1}×{0,1}`. A site
locks when a displayed predicate of its six-neighbor occupancy tuple
returns `1`. Off-patch neighbors contribute occupancy `0`. A run is the
tuple of lock-set cardinalities from the seed through halt, together
with the fill bit `|locks_halt|=12`.

Let `f_L1(c)=1` if and only if some axis is unbalanced (`n≠0`,
not Hamming parity). Let `f_min(c)=1` if and only if `n_both(c)=0` and
some axis is unbalanced. These remain distinct maps: they disagree on
the `mixed3=(1,1,1)` orbit.

Enumerate nonempty seeds `S` by increasing `|S|`, then lexicographic
site order, through `|S|≤3` (`12+66+220=298` seeds).

**Theorem 1.** Every 1-site seed has identical halt history and fill
for the two maps. The long-axis seed `{(0,0,0),(1,0,0),(2,0,0)}` also
agrees, with history `(3, 9, 12)` and fill. The first nonempty seed of
size at most three at which the runs differ is
`S={(0, 0, 0), (2, 1, 1)}`.

**Theorem 2.** From that `S`, `f_L1` has lock history `(2, 8, 12)` and
fills. `f_min` has lock history `(2, 8, 10)` and does not fill.

**Theorem 3.** The first distinguishing seed is displayed only. Do not
adopt either map. Do not write a seed into Admissibility.

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
not axiom content. A seed is likewise displayed data, not an
admissibility rule.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Finite exact seed census of two displayed occupancy-to-lock maps on a twelve-vertex two-cube through size 3."
trace_class: frontier_discovery
target_claim_id: f_min_l1_first_distinguishing_seed
target_blocker_text: "first nonempty two-cube seed of size at most 3 at which f_min and f_L1 disagree in halt history or fill"
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
| type210 | `(2,1,0)` | `(1,1,1,0,0,1)` |
| vertex3 | `(3,0,0)` | `(1,0,1,0,1,0)` |
| mixed3 | `(1,1,1)` | `(1,0,1,1,0,0)` |
| full | `(0,3,0)` | `(1,1,1,1,1,1)` |

`f_L1(c)=1` iff `n_unbalanced(c)≥1`.
`f_min(c)=1` iff `n_both(c)=0` and `n_unbalanced(c)≥1`.

On those representatives the bits are

| map | wt1 | opp2 | adj2 | type210 | vertex3 | mixed3 | empty | full |
|---|---|---|---|---|---|---|---|---|
| `f_L1` | 1 | 0 | 1 | 1 | 1 | 1 | 0 | 0 |
| `f_min` | 1 | 0 | 1 | 0 | 1 | 0 | 0 | 0 |

The maps disagree on `mixed3` and on type `(2,1,0)`. Hamming parity of
`|c|_1` is a different predicate: `opp2` is even and `f_L1(opp2)=0`.

One tick locks every currently unlocked on-patch site whose neighbor
tuple has `f=1`. The process starts with `locks_0=S` and halts at the
first fixed point, or at tick `12`. Lock history is the sequence of
cardinalities from `t=0` through halt. Fill means `|locks_halt|=12`.

Seeds are enumerated by increasing cardinality, then as combinations
of the lexicographic site list. That census is `12+66+220=298` nonempty
seeds of size at most three. It is a seed census on this two-cube, not
an occupancy-step clone of a previously displayed single seed.

## Theorem 1 — first distinguishing seed

Reconfirm the two already-run seeds.

Every singleton `S={p}` with `p` on the two-cube has the same run for
`f_min` and `f_L1`. In particular the corner seed `{(0,0,0)}` has
history `(1, 4, 8, 11, 12)` and fills under both maps.

The long-axis seed `{(0,0,0),(1,0,0),(2,0,0)}` has history `(3, 9, 12)`
and fills under both maps. Mixed3 is unvisited on that path, so the
predicate difference is not executed.

Among the remaining seeds of size at most three, ordered as above, the
first seed at which halt history or fill differs is the first nonempty seed

`S={(0, 0, 0), (2, 1, 1)}`.

It is the last 2-site combination that begins with `(0,0,0)`. The ten
earlier pairs that begin with `(0,0,0)` agree, as do all twelve
singletons. So a distinguishing seed exists inside the `|S|≤3` cap.

Not leftover-character of #6411 (that 1-site history agreement).
Not leftover-character of #6412 (that long-axis history agreement).
Not an occupancy-step clone: same two-cube, seed census.

## Theorem 2 — both histories and both fill bits

Start with `S={(0,0,0),(2,1,1)}`, so `|locks_0|=2`.

The first wave is the same for both maps. The six sites
`(0,0,1)`, `(0,1,0)`, `(1,0,0)`, `(1,1,1)`, `(2,0,1)`, `(2,1,0)`
each see a single occupied nearest neighbor (type `wt1`), so both
predicates return `1`. The four remaining sites see the empty tuple.

After tick `1` one has `|locks_1|=8`. The four unlocked sites then
split:

- `(0,1,1)` and `(2,0,0)` see type `vertex3=(3,0,0)`. Both predicates
  return `1`.
- `(1,0,1)` and `(1,1,0)` see type `(2,1,0)`. Then `f_L1=1` and
  `f_min=0`, because `n_both=1`.

Therefore `f_L1` locks all four remaining sites at tick `2` and fills:

`T=2`, `|locks_halt|=12`, history `(2, 8, 12)`, fill bit `1`.

`f_min` locks only the two `vertex3` sites. The pair
`(1,0,1)`, `(1,1,0)` remains type `(2,1,0)` and never unlocks:

`T=2`, `|locks_halt|=10`, history `(2, 8, 10)`, fill bit `0`.

The executed split is the type-`(2,1,0)` orbit, not the unvisited
`mixed3` representative. The maps were already distinct as predicates;
this seed is the first size-at-most-three place where that distinction
changes the halt history or the fill bit.

## Theorem 3 — display, not adoption

The first distinguishing seed is `S={(0, 0, 0), (2, 1, 1)}`. It is
displayed data. Do not adopt `f_min`. Do not adopt `f_L1`. Do not
write a seed into Admissibility. Admissibility is not a dynamics axiom
and does not supply this predicate or this seed. The seed is not
written into Admissibility.

Agreement on every 1-site seed and on the long-axis 3-site seed is
path coincidence on those seeds, not identity of maps. Disagreement
on this 2-site seed is likewise a displayed finite fact, not a reason
to treat either member as axiom content.

## Exact Target And Obligation Graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record wording | quoted; no edit |
| two-cube, off-patch `o=0`, lex seed order, `|S|≤3` | declared finite data |
| 1-site and long-axis agreement | recomputed |
| first distinguishing seed | `{(0, 0, 0), (2, 1, 1)}` |
| both histories | `(2, 8, 12)` and `(2, 8, 10)` |
| both fill bits | `f_L1` fills; `f_min` does not |
| identity of the two maps | refused; they disagree on `mixed3` |
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
| V1 | It answers which first `|S|≤3` seed, if any, separates `f_min` from `f_L1` in halt history or fill. |
| V2 | Current main has the axiom memo and no landed first-distinguishing-seed census of these two maps. |
| V3 | The 298-seed twelve-vertex process is independently finite and exact. |
| V4 | The theorem is more than restating Admissibility: it executes two supplied predicates the axiom does not name. |
| V5 | Neither map nor the seed is an admissibility rule, and none is adopted. |

## No-Go Discipline Gate

The negative content is narrow: a first distinguishing seed is not
predicate identity, and a displayed filler or seed is not axiom
content.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| 1-site census | every singleton seed | histories and fill agree |
| long-axis seed | `{(0,0,0),(1,0,0),(2,0,0)}` | both fill; history `(3, 9, 12)` |
| lex census through size 3 | 298 seeds | first split at `{(0,0,0),(2,1,1)}` |
| `f_L1` from that `S` | some-axis-unbalanced predicate | fills; history `(2, 8, 12)` |
| `f_min` from that `S` | nonempty `n_both=0` predicate | does not fill; history `(2, 8, 10)` |
| `mixed3` distinction | evaluate both maps on `(1,1,1)` | they disagree; maps stay distinct |
| Hamming parity | `|c|_1 mod 2` | different predicate; `opp2` even |
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

**Steelman:** Same histories on every 1-site seed and on the long-axis
seed mean the maps are dynamically the same, so the rival may be
dropped or adopted as `f_L1`.

**Answer:** The first size-at-most-three seed
`{(0, 0, 0), (2, 1, 1)}` already splits both history and fill. The
maps also disagree on `mixed3`. Admissibility does not name either
map or this seed.

### N8 — cross-cycle echo

A 1-site identity of `f_min` and a long-axis fill of `f_min` are
different claims. This note executes the first distinguishing seed in
the size-at-most-three lex census.

**Gate disposition:** PASS for the finite first-seed statement and the
displayed histories. FAIL / DO NOT SHIP for “adopt `f_min`,” “adopt
`f_L1`,” “write a seed into Admissibility,” or “the maps are the same
dynamics on every two-cube seed.”

## Primary Runner

The primary runner rebuilds the two-cube, both predicates, the 298-seed
lex census, the 1-site and long-axis reconfirmations, the first
distinguishing seed with both histories and both fill bits, the
type-`(2,1,0)` split, the current premise boundary, and the
non-adoption wording. It authors no audit verdict.
