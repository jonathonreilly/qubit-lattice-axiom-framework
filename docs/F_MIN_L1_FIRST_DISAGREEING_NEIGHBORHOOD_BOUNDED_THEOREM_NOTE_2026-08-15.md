---
claim_id: f_min_l1_first_disagreeing_neighborhood_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On the two-cube with off-patch o=0 and seed {(0,0,0),(2,1,1)}, the first neighborhood at which f_min and f_L1 disagree is reported by tick, site, and axis type. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_min_l1_first_disagreeing_neighborhood_2026_08_15.py
---

# First Neighborhood Where `f_min` And `f_L1` Disagree From The Displayed Seed

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** displayed occupancy-to-lock dynamics of two cube-covariant
maps on the twelve-vertex two-cube `{0,1,2}×{0,1}×{0,1}`, started from
the displayed seed `S*={(0,0,0),(2,1,1)}`, with off-patch occupancy
identically `0`. The first disagreeing neighborhood is displayed, not
adopted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/f_min_l1_first_disagreeing_neighborhood_2026_08_15.py`](../scripts/f_min_l1_first_disagreeing_neighborhood_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

Write the two-cube as the twelve sites `{0,1,2}×{0,1}×{0,1}`. A site
locks when a displayed predicate of its six-neighbor occupancy tuple
returns `1`. Off-patch neighbors contribute occupancy `0`. Two
independent runs start from the same seed and update on their own
locked sets.

Let `f_L1(c)=1` if and only if some axis is unbalanced (`n≠0`,
not Hamming parity). Let `f_min(c)=1` if and only if `n_both(c)=0` and
some axis is unbalanced. These remain distinct maps: they disagree on
the `mixed3=(1,1,1)` orbit and on any occupancy that is still
unbalanced with `n_both≥1`.

**Theorem 1.** From `S*={(0,0,0),(2,1,1)}`, `f_L1` fills with lock
history `(2, 8, 12)`. `f_min` does not fill.

**Theorem 2.** The first tick and unlocked site at which the two
predicates differ, on either run's locked set, is `t=2`,
`x=(1, 0, 1)`, axis type `(2, 1, 0)`, with `f_L1=1` and `f_min=0`.

**Theorem 3.** That neighborhood stencil is the six-tuple
`(1, 1, 1, 0, 0, 1)` in order `(+x,-x,+y,-y,+z,-z)`. It is displayed
only. Do not adopt a selector. Do not adopt either map. Do not write
the stencil into Admissibility.

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
not axiom content. A neighborhood stencil is likewise displayed data,
not an admissibility rule.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Finite exact tick-by-tick neighborhood census of two displayed occupancy-to-lock maps from one two-cube seed."
trace_class: frontier_discovery
target_claim_id: f_min_l1_first_disagreeing_neighborhood
target_blocker_text: "first neighborhood at which f_min and f_L1 disagree from S*={(0,0,0),(2,1,1)}"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the bounded neighborhood claim; do not adopt either map or the stencil"
conditional_surface_status: "exact on the two-cube with off-patch o=0 from the displayed seed; both maps remain displayed members"
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

The displayed seed is `S*={(0,0,0),(2,1,1)}`.

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

The maps disagree exactly on mixed3 and on any `n_both≥1` occupancy
that is still unbalanced, including type `(2,1,0)`. They agree on
`opp2`, which has `n_both=1` but no unbalanced axis. Hamming parity of
`|c|_1` is a different predicate: `opp2` is even and `f_L1(opp2)=0`.

One tick locks every currently unlocked on-patch site whose neighbor
tuple has `f=1` for that run's predicate. The process starts with
`locks_0=S*` and evaluates both predicates at every unlocked site
against that run's locked set before locking. Sites are read in the
lexicographic order above, so the first disagreeing site at a tick is
the lexicographically first unlocked site whose two predicate values
differ.

Not leftover-character of #6417: that only named `S*` as the first
`|S|≤3` seed at which halt history or fill differs. The object here is
the first disagreeing stencil along the two independent runs from that
seed.

## Theorem 1 — reconfirm fill from `S*`

Start with `S*={(0,0,0),(2,1,1)}`, so `|locks_0|=2`.

`f_L1` has lock history `(2, 8, 12)` and fills: after two ticks every
on-patch site is locked.

`f_min` shares the first wave and then stops short of the full
twelve-site set. It does not fill.

This reconfirms the fill split already named with `S*`. It does not
yet name the neighborhood at which the predicates first differ.

## Theorem 2 — first disagreeing tick, site, and axis type

At tick `1` the locked set of each run is still `S*`. Every unlocked
site that sees a single occupied nearest neighbor is type `wt1`; both
predicates return `1`. The remaining unlocked sites see the empty
tuple; both predicates return `0`. No unlocked site disagrees. The
shared first wave locks the six sites

`(0,0,1)`, `(0,1,0)`, `(1,0,0)`, `(1,1,1)`, `(2,0,1)`, `(2,1,0)`.

After tick `1` one has `|locks_1|=8` on both runs. At tick `2` the
four unlocked sites split:

- `(0,1,1)` and `(2,0,0)` see type `vertex3=(3,0,0)`. Both predicates
  return `1`.
- `(1, 0, 1)` and `(1,1,0)` see type `(2, 1, 0)`. Then `f_L1=1` and
  `f_min=0`, because `n_both=1` and two axes are unbalanced.

The lexicographically first such site is `x=(1, 0, 1)`. That is the
first disagreeing neighborhood: tick `t=2`, site `(1, 0, 1)`, axis
type `(2, 1, 0)`, predicate values `f_L1=1` and `f_min=0`. The same
`(t,x,type)` is obtained on the `f_L1` run and on the `f_min` run,
because the locked sets still coincide at the evaluation of tick `2`.

The same-tick companion site `(1,1,0)` is also type `(2,1,0)`, but it
is later in lexicographic order.

## Theorem 3 — display the stencil

At `x=(1, 0, 1)` and the shared eight-site locked set of tick `2`, the
six-neighbor tuple in order `(+x,-x,+y,-y,+z,-z)` is

`(1, 1, 1, 0, 0, 1)`.

That is: `(2,0,1)` and `(0,0,1)` occupied, `(1,1,1)` occupied,
`(1,-1,1)` off-patch empty, `(1,0,2)` off-patch empty, and `(1,0,0)`
occupied. The axis type is `(2, 1, 0)`. This is the displayed
disagreeing stencil.

Do not adopt a selector. Do not adopt `f_min`. Do not adopt `f_L1`.
Do not write the stencil into Admissibility. Admissibility is not a
dynamics axiom and does not supply this predicate or this
neighborhood. The stencil is not written into Admissibility.

The executed split is the type-`(2,1,0)` orbit. Mixed3 remains a
predicate-level distinction; it is not the first executed neighborhood
on these two runs.

## Exact Target And Obligation Graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record wording | quoted; no edit |
| two-cube, off-patch `o=0`, seed `S*` | declared finite data |
| `f_L1` fill from `S*` | recomputed; history `(2, 8, 12)` |
| `f_min` fill from `S*` | recomputed; does not fill |
| first disagreeing `(t,x,axis-type)` | `t=2`, `(1, 0, 1)`, `(2, 1, 0)` |
| first disagreeing stencil | `(1, 1, 1, 0, 0, 1)` |
| both predicate values | `f_L1=1`, `f_min=0` |
| identity of the two maps | refused; they disagree on mixed3 and type `(2,1,0)` |
| adoption of either map or the stencil | refused |
| formation site / rate from the axioms | open |

## Boundary And Imports

No observation, fit, continuum limit, or Hamming-as-`f_L1`
identification is imported. The two-cube, the two predicates, and the
seed are supplied mathematical data for this note. Record lock
language is quoted only as the existing lock/content/absence boundary;
it does not select either map or any neighborhood.

## Promotion Value Gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the first neighborhood, by tick, site, and axis type, at which `f_min` and `f_L1` disagree from `S*`. |
| V2 | Current main has the axiom memo and no landed first-disagreeing-neighborhood census of these two maps from this seed. |
| V3 | The twelve-vertex two-run process is independently finite and exact. |
| V4 | The theorem is more than restating Admissibility: it executes two supplied predicates the axiom does not name. |
| V5 | Neither map nor the stencil is an admissibility rule, and none is adopted. |

## No-Go Discipline Gate

The negative content is narrow: a first disagreeing neighborhood is
not a selector, and a displayed stencil is not axiom content.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| `f_L1` from `S*` | some-axis-unbalanced predicate | fills; history `(2, 8, 12)` |
| `f_min` from `S*` | nonempty `n_both=0` predicate | does not fill |
| tick-1 neighborhoods | both predicates on `locks=S*` | no unlocked disagreement |
| tick-2 neighborhoods | both predicates on the shared eight-site set | first split at `(1, 0, 1)` |
| axis type of that 6-tuple | opposite-pair census | `(2, 1, 0)` |
| displayed stencil | six-neighbor order `(+x,-x,+y,-y,+z,-z)` | `(1, 1, 1, 0, 0, 1)` |
| Hamming parity | `|c|_1 mod 2` | different predicate; `opp2` even |
| write a stencil or map into Admissibility | treat either as the local rule | refused; axiom is not a dynamics axiom |

### N2 — wall independence

The missing formation-site selector, the missing axiom-level
occupancy rule, and the choice among displayed members are distinct
open items. This note claims no complete wall and no compiler no-go.

### N3 — hidden-condition scan

The two-cube, off-patch `o=0`, seed `S*`, six-neighbor order,
lexicographic site order, and both predicates are declared. Cube
covariance is used only as the axis-type reading of a six-tuple. No
continuum, Hamming, or admissibility rewrite is assumed.

### N4 — source residual matching

The axiom memo supplies the cubic nearest-neighbor graph and states
that Admissibility is not a dynamics axiom and does not supply the
formation site, probability, or rate. The residual therefore matches
those sources: a displayed lock predicate and a displayed stencil are
extra data.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | axis-type representatives and off-patch `0` | no alphabet classification |
| per site | every unlocked two-cube vertex against both predicates | no derived kernel values |
| per mode | no mode calculation | no spectral exhaustion |
| per block | both independent runs from `S*` to a fixed point | no physical compiler |
| lattice wide | checked and not executed | neither map nor the stencil adopted as a rule |

### N6 — live partial-closure paths

Live routes include an independent reason to select or reject either
map, a larger-complex census, and a formation mechanism supplied by
something other than a displayed predicate.

### N7 — hostile steelman

**Steelman:** The seed `S*` already names the split, so the first
disagreeing neighborhood is leftover character and may be treated as
a selector.

**Answer:** Naming `S*` reports only that halt history or fill
differs. The first executed neighborhood is a different object: tick
`2`, site `(1, 0, 1)`, type `(2, 1, 0)`, stencil
`(1, 1, 1, 0, 0, 1)`. Admissibility does not name either map or this
stencil. Do not adopt a selector.

### N8 — cross-cycle echo

A seed that distinguishes fill is a different claim from the first
neighborhood at which the two predicates return different bits.
This note executes that neighborhood on the two independent runs.

**Gate disposition:** PASS for the finite first-neighborhood statement
and the displayed stencil. FAIL / DO NOT SHIP for “adopt `f_min`,”
“adopt `f_L1`,” “adopt a selector,” “write the stencil into
Admissibility,” or “the maps are the same dynamics on this seed.”

## Primary Runner

The primary runner rebuilds the two-cube, both predicates, the two
independent runs from `S*`, the fill reconfirmation, the first
disagreeing tick, site, axis type, and stencil, the current premise
boundary, and the non-adoption wording. It authors no audit verdict.
