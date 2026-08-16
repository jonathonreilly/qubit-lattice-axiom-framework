---
claim_id: f_cut_wt1_zero_f1_first_split_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On the two-cube with off-patch o=0, the lex-first seed of size at most 3 at which F_cut (1,1,1,1,1) fills and (0,1,1,1,1) does not is S={(0,0,0)}. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_wt1_zero_f1_first_split_2026_08_15.py
---

# First Seed Of Size At Most Three Where `f1` Fills And Its `wt1=0` Sibling Does Not

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** displayed occupancy-to-lock dynamics of two cube-covariant
`F_cut` maps on the twelve-vertex two-cube `{0,1,2}×{0,1}×{0,1}`,
started from every nonempty seed of size at most three, with off-patch
occupancy identically `0`. The lex-first seed at which `f1` fills and
the `wt1=0` sibling does not is displayed, not adopted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_wt1_zero_f1_first_split_2026_08_15.py`](../scripts/f_cut_wt1_zero_f1_first_split_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

Write the two-cube as the twelve sites `{0,1,2}×{0,1}×{0,1}`. A site
locks when a displayed predicate of its six-neighbor occupancy tuple
returns `1`. Off-patch neighbors contribute occupancy `0`. A run is the
tuple of lock-set cardinalities from the seed through halt, together
with the fill bit `|locks_halt|=12`.

`F_cut` is the cube-covariant class with `f(empty)=f(full)=0` and
`f(c)=f(1-c)`. Remaining bits are ordered
`(wt1, opp2, adj2, vertex3, mixed3)`. Write

- `f1 = (1,1,1,1,1)`,
- `fwt = (0,1,1,1,1)`.

`f_L1(c)=1` if and only if some axis is unbalanced (`n≠0`,
not Hamming parity). That map has remaining bits `(1,0,1,1,1)` and is
not this pair.

Enumerate nonempty seeds `S` by increasing `|S|`, then lexicographic
site order, through `|S|≤3` (`12+66+220=298` seeds).

**Theorem 1.** `f1` fills every 2-site seed (`cov2(f1)=66`). `fwt` is
not in `Max(2)`: `cov2(fwt)=0`, while `Max(2)` is the class attaining
`66`.

**Theorem 2.** The lex-first seed of size at most 3 at which `f1`
fills and `fwt` does not is `S={(0,0,0)}`, so `|S|=1`.

**Theorem 3.** From that `S`, `f1` has lock history `(1, 4, 8, 11, 12)`
and fills. `fwt` has lock history `(1,)` and does not fill. Display
the first split. Do not adopt `wt1`.

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
predicate. The maps `f1` and `fwt` are supplied displayed members, not
axiom content. A seed is likewise displayed data, not an admissibility
rule: no axiom or approved primitive is added.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Finite exact seed census of two displayed F_cut occupancy-to-lock maps on a twelve-vertex two-cube through size 3."
trace_class: frontier_discovery
target_claim_id: f_cut_wt1_zero_f1_first_split
target_blocker_text: "lex-first two-cube seed of size at most 3 at which F_cut (1,1,1,1,1) fills and (0,1,1,1,1) does not"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the bounded first-split claim; do not adopt wt1 or the seed"
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
off-patch neighbor is `0`. Off-patch occupancy `0` is the explicit
default; a blank-block is a different rule.

For each axis, the pair of opposite bits is

- unbalanced if the bits are `{0,1}`,
- both if the bits are `{1,1}`,
- empty if the bits are `{0,0}`.

Write `(n_unbalanced, n_both, n_empty)` with sum `3`. Remaining-bit
orbits used below:

| name | type | representative |
|---|---|---|
| empty | `(0,0,3)` | `(0,0,0,0,0,0)` |
| wt1 | `(1,0,2)` | `(1,0,0,0,0,0)` |
| opp2 | `(0,1,2)` | `(1,1,0,0,0,0)` |
| adj2 | `(2,0,1)` | `(1,0,1,0,0,0)` |
| type120 | `(1,2,0)` | `(1,0,1,1,1,1)` |
| vertex3 | `(3,0,0)` | `(1,0,1,0,1,0)` |
| mixed3 | `(1,1,1)` | `(1,0,1,1,0,0)` |
| full | `(0,3,0)` | `(1,1,1,1,1,1)` |

`f_L1(c)=1` if and only if some axis is unbalanced. Hamming parity of
`|c|_1` is a different predicate: `adj2` is even and `f_L1(adj2)=1`.

On those representatives the remaining bits are

| map | wt1 | opp2 | adj2 | vertex3 | mixed3 |
|---|---|---|---|---|---|
| `f1` | 1 | 1 | 1 | 1 | 1 |
| `fwt` | 0 | 1 | 1 | 1 | 1 |
| `f_L1` | 1 | 0 | 1 | 1 | 1 |

Complement-even assignment sends type `(1,2,0)` with `wt1`. So `f1`
fires on every nonempty nonfull six-tuple, and `fwt` is silent on
`wt1` and on its complement.

One tick locks every currently unlocked on-patch site whose neighbor
tuple has `f=1`. The process starts with `locks_0=S` and halts at the
first fixed point, or at tick `12`. Lock history is the sequence of
cardinalities from `t=0` through halt. Fill means `|locks_halt|=12`.
`Max(k)` is the set of `F_cut` maps attaining the maximum number of
filling `k`-site seeds.

Seeds are enumerated by increasing cardinality, then as combinations
of the lexicographic site list. That census is `12+66+220=298` nonempty
seeds of size at most three.

## Theorem 1 — `f1` fills every 2-site seed; `fwt` is not in `Max(2)`

There are `C(12,2)=66` two-site seeds. Independent runs from each seed
give `cov2(f1)=66`: `f1` fills every 2-site seed. The same census gives
`cov2(fwt)=0`. Therefore `fwt` does not attain the two-site maximum
and is not in `Max(2)`. The two-site maximum `66` is attained (in
particular) by `f1` and by `f0=(1,1,1,1,0)`.

This is the 2-site coverage comparison of the pair, not a recensus of
`Max(11)`.

## Theorem 2 — lex-first seed of size at most 3

The lex-first seed of size at most 3 at which `f1` fills and `fwt`
does not is

`S={(0, 0, 0)}`.

It is the first 1-site seed in lexicographic site order. Every later
1-site seed is likewise a fill for `f1` and a miss for `fwt`, but the
lex-first witness is the corner singleton. So a distinguishing seed
exists inside the `|S|≤3` cap, and it has `|S|=1`.

Not leftover of the `opp2=0` first-split pair (that pair is `f_L1`
versus `(0,0,1,1,1)`). The present pair differs only in the `wt1` bit
of `f1`.

## Theorem 3 — histories from `S`; display, not adoption

Start with `S={(0,0,0)}`, so `|locks_0|=1`.

The three on-patch nearest neighbors `(1,0,0)`, `(0,1,0)`, `(0,0,1)`
each see a single occupied nearest neighbor, type `wt1`. Then `f1=1`
and `fwt=0`. Every other unlocked site sees the empty tuple.

Therefore `f1` locks those three sites at tick `1` and continues:

`T=4`, `|locks_halt|=12`, history `(1, 4, 8, 11, 12)`, fill bit `1`.

`fwt` locks nothing further. The first wave is empty:

`T=0`, `|locks_halt|=1`, history `(1,)`, fill bit `0`.

The executed split is the `wt1` orbit. Display the first split. Do not
adopt `wt1`. Do not adopt `f1`. Do not adopt `fwt`. Do not write a
seed into Admissibility. The seed is not written into Admissibility.

A displayed filler or seed is not axiom content. Admissibility is not
a dynamics axiom and does not supply this predicate or this seed.

## Exact Target And Obligation Graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record wording | quoted; no edit |
| two-cube, off-patch `o=0`, lex seed order, `|S|≤3` | declared finite data |
| `f1` fills every 2-site seed | recomputed; `cov2=66` |
| `fwt` not in `Max(2)` | recomputed; `cov2=0` |
| lex-first seed | `{(0, 0, 0)}` |
| both histories | `(1, 4, 8, 11, 12)` and `(1,)` |
| both fill bits | `f1` fills; `fwt` does not |
| adoption of `wt1` or either map | refused |
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
| V1 | It answers which first `|S|≤3` seed, if any, is a fill for `f1` and a miss for `fwt`. |
| V2 | Current main has the axiom memo and no landed first-split census of this `wt1` pair. |
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
| 2-site census | every pair seed | `f1` fills all `66`; `fwt` fills none |
| `Max(2)` membership | compare `cov2` to `66` | `fwt` is not in `Max(2)` |
| lex census through size 3 | 298 seeds | first split at `{(0,0,0)}` |
| `f1` from that `S` | remaining bits `(1,1,1,1,1)` | fills; history `(1, 4, 8, 11, 12)` |
| `fwt` from that `S` | remaining bits `(0,1,1,1,1)` | does not fill; history `(1,)` |
| `wt1` distinction | evaluate both maps on `(1,0,2)` | they disagree; first wave splits |
| Hamming parity | `|c|_1 mod 2` | different predicate; `adj2` even |
| write a seed or `wt1` into Admissibility | treat either as the local rule | refused; axiom is not a dynamics axiom |

### N2 — wall independence

The missing formation-site selector, the missing axiom-level
occupancy rule, and the choice among displayed members are distinct
open items. This note claims no complete wall and no compiler no-go.

### N3 — hidden-condition scan

The two-cube, off-patch `o=0`, lex site order, size cap 3,
six-neighbor order, and both remaining-bit tuples are declared. Cube
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
| per element | remaining-bit representatives and off-patch `0` | no alphabet classification |
| per site | every two-cube vertex against both predicates | no derived kernel values |
| per mode | no mode calculation | no spectral exhaustion |
| per block | all 66 two-site seeds and the lex `|S|≤3` search | no physical compiler |
| lattice wide | checked and not executed | neither map nor the seed adopted as a rule |

### N6 — live partial-closure paths

Live routes include an independent reason to select or reject either
map, a larger-`k` coverage comparison, and a formation mechanism
supplied by something other than a displayed predicate.

### N7 — hostile steelman

**Steelman:** `fwt` sits in `Max(11)`, so the `wt1` bit is dynamically
free on small seeds and the pair may be treated as one object.

**Answer:** The lex-first seed `{(0, 0, 0)}` already splits fill.
`f1` fills every 2-site seed and `fwt` fills none of them. `Max(11)`
membership is a different ranking. Admissibility does not name either
map or this seed.

### N8 — cross-cycle echo

A 2-site fill census of `f1` and a `Max(11)` listing of `fwt` are
different claims. This note executes the first seed of size at most 3
at which the pair disagrees on fill.

No-Go Discipline disposition: **PASS**

**Gate disposition:** PASS for the finite first-seed statement and the
displayed histories. FAIL / DO NOT SHIP for “adopt `wt1`,” “adopt
`f1`,” “write a seed into Admissibility,” or “the maps are the same
dynamics on every two-cube seed.”

## Primary Runner

The primary runner rebuilds the two-cube, both remaining-bit
predicates, the 66-seed two-site coverage comparison, the lex
`|S|≤3` first-split search, both histories and both fill bits from
`{(0,0,0)}`, the `wt1` first-wave mechanism, the current premise
boundary, and the non-adoption wording. It authors no audit verdict.
