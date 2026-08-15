---
claim_id: f_mix0_l1_first_distinguishing_seed_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On the two-cube with off-patch o=0, the first nonempty seed of size at most 3 at which f_mix0 and f_L1 disagree in halt history or fill is S={(0,0,0),(0,0,1),(2,0,0)}. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_mix0_l1_first_distinguishing_seed_2026_08_15.py
---

# First Two-Cube Seed Of Size At Most Three Where `f_mix0` And `f_L1` Disagree

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** displayed occupancy-to-lock dynamics of two cube-covariant
maps on the twelve-vertex two-cube `{0,1,2}×{0,1}×{0,1}`, started from
every nonempty seed of size at most three, with off-patch occupancy
identically `0`. The first distinguishing seed is displayed, not adopted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/f_mix0_l1_first_distinguishing_seed_2026_08_15.py`](../scripts/f_mix0_l1_first_distinguishing_seed_2026_08_15.py)
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

Let `f_mix0` be the `F_cut` remaining-bit map

```text
(wt1, opp2, adj2, vertex3, mixed3) = (1, 0, 1, 1, 0)
```

with complements forced. It is L1 with `mixed3=0`. The maps remain
distinct: they disagree on the `mixed3=(1,1,1)` orbit.

Among `opp2=0` maps they tie on 2-site coverage (#6434) and on 1-site
coverage (#6435). They agree on `{(0,0,0)}`, the face-diagonal
`{(0,0,0),(1,1,0)}`, and opposite-corner `S*={(0,0,0),(2,1,1)}` (both
fill). Those agreements are leftover-character of those coverage and
named-seed surfaces. They are not the residual of this note.

Enumerate nonempty seeds `S` by increasing `|S|`, then lexicographic
site order, through `|S|≤3` (`12+66+220=298` seeds).

**Theorem 1.** The two maps agree on `{(0,0,0)}`, on the face-diagonal
`{(0,0,0),(1,1,0)}`, and on opposite-corner `S*={(0,0,0),(2,1,1)}`.
All three seeds fill under both maps.

**Theorem 2.** The first nonempty seed of size at most three at which
fill or lock history differs is `S={(0,0,0),(0,0,1),(2,0,0)}`. From
that `S`, `f_L1` has lock history `(3, 8, 11, 12)` and fills. `f_mix0`
has lock history `(3, 8, 10)` and does not fill. This is the first
10-lock disagreement seed in the lex census.

**Theorem 3.** The first distinguishing seed is displayed only. Do not
adopt either map. Do not write a seed into Admissibility.

Displayed, not adopted.

Not leftover-character of #6417 (that was `f_min`).
Not leftover-character of #6431 (that was the cov=66 pair).

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
predicate. The maps `f_L1` and `f_mix0` are supplied displayed members,
not axiom content. A seed is likewise displayed data, not an
admissibility rule.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Finite exact seed census of two displayed occupancy-to-lock maps on a twelve-vertex two-cube through size 3."
trace_class: frontier_discovery
target_claim_id: f_mix0_l1_first_distinguishing_seed
target_blocker_text: "first nonempty two-cube seed of size at most 3 at which f_mix0 and f_L1 disagree in halt history or fill"
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
`f_mix0(c)=1` iff `n_unbalanced(c)≥1` and the axis type is not
`mixed3=(1,1,1)`. Its remaining-bit tuple is `(1,0,1,1,0)`.

On those representatives the bits are

| map | wt1 | opp2 | adj2 | type210 | vertex3 | mixed3 | empty | full |
|---|---|---|---|---|---|---|---|---|
| `f_L1` | 1 | 0 | 1 | 1 | 1 | 1 | 0 | 0 |
| `f_mix0` | 1 | 0 | 1 | 1 | 1 | 0 | 0 | 0 |

The maps disagree only on `mixed3` among these remaining bits. Hamming
parity of `|c|_1` is a different predicate: `opp2` is even and
`f_L1(opp2)=0`.

One tick locks every currently unlocked on-patch site whose neighbor
tuple has `f=1`. The process starts with `locks_0=S` and halts at the
first fixed point, or at tick `12`. Lock history is the sequence of
cardinalities from `t=0` through halt. Fill means `|locks_halt|=12`.

Seeds are enumerated by increasing cardinality, then as combinations
of the lexicographic site list. That census is `12+66+220=298` nonempty
seeds of size at most three. It is a seed census on this two-cube, not
an occupancy-step clone of a previously displayed single seed.

## Theorem 1 — named seeds agree

Reconfirm the three already-run seeds that both maps fill.

The corner seed `{(0,0,0)}` has history `(1, 4, 8, 11, 12)` and fills
under both maps.

The face-diagonal seed `{(0,0,0),(1,1,0)}` has history `(2, 7, 11, 12)`
and fills under both maps.

The opposite-corner seed `S*={(0,0,0),(2,1,1)}` has history
`(2, 8, 12)` and fills under both maps.

Every nonempty seed of size at most two agrees (all `12+66=78` of
them). Mixed3 is unvisited on those paths, so the remaining-bit
difference is not executed.

## Theorem 2 — first distinguishing seed, both histories, both fill bits

Among the remaining seeds of size at most three, ordered as above, the
first nonempty seed at which halt history or fill differs is

`S={(0,0,0),(0,0,1),(2,0,0)}`.

It is the first 3-site combination that begins
`(0,0,0),(0,0,1),(2,0,0)`. The earlier size-1 and size-2 seeds agree,
as do the size-3 combinations that precede it. So a distinguishing seed
exists inside the `|S|≤3` cap.

Start with that `S`, so `|locks_0|=3`.

The first wave is the same for both maps. The five sites
`(0,1,0)`, `(0,1,1)`, `(1,0,1)`, `(2,0,1)`, `(2,1,0)`
each see a single occupied nearest neighbor (type `wt1`), so both
predicates return `1`. The site `(1,0,0)` sees type `opp2` and stays
unlocked. The remaining three sites see the empty tuple or an empty
pair and stay unlocked.

After tick `1` one has `|locks_1|=8`. The four unlocked sites then
split:

- `(1,1,1)` and `(2,1,1)` see type `adj2=(2,0,1)`. Both predicates
  return `1`.
- `(1,1,0)` sees type `opp2=(0,1,2)`. Both predicates return `0`.
- `(1,0,0)` sees type `mixed3=(1,1,1)`. Then `f_L1=1` and `f_mix0=0`.

Therefore `f_L1` locks three of those four sites at tick `2`, reaching
eleven locks, and then locks the last site `(1,1,0)` (now type
`(2,1,0)`) at tick `3` and fills:

`T=3`, `|locks_halt|=12`, history `(3, 8, 11, 12)`, fill bit `1`.

`f_mix0` locks only the two `adj2` sites. The pair
`(1,0,0)`, `(1,1,0)` remains type `mixed3` after that wave and never
unlocks:

`T=2`, `|locks_halt|=10`, history `(3, 8, 10)`, fill bit `0`.

The executed split is the `mixed3` orbit at `(1,0,0)`. This is the
first 10-lock disagreement seed in the lex census: `f_mix0` halts at
ten locks while `f_L1` fills. The maps were already distinct as
predicates; this seed is the first size-at-most-three place where that
distinction changes the halt history or the fill bit.

## Theorem 3 — display, not adoption

The first distinguishing seed is `S={(0,0,0),(0,0,1),(2,0,0)}`. It is
displayed data. Do not adopt `f_mix0`. Do not adopt `f_L1`. Do not
write a seed into Admissibility. Admissibility is not a dynamics axiom
and does not supply this predicate or this seed. The seed is not
written into Admissibility.

Agreement on the 1-site seed, the face-diagonal, and `S*` is path
coincidence on those seeds, not identity of maps. Disagreement on this
3-site seed is likewise a displayed finite fact, not a reason to treat
either member as axiom content.

## Exact Target And Obligation Graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record wording | quoted; no edit |
| two-cube, off-patch `o=0`, lex seed order, `|S|≤3` | declared finite data |
| named-seed agreement | recomputed; all three fill |
| first distinguishing seed | `{(0,0,0),(0,0,1),(2,0,0)}` |
| both histories | `(3, 8, 11, 12)` and `(3, 8, 10)` |
| both fill bits | `f_L1` fills; `f_mix0` does not |
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
| V1 | It answers which first `|S|≤3` seed, if any, separates `f_mix0` from `f_L1` in halt history or fill. |
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
| 1-site seed | `{(0,0,0)}` | both fill; history `(1, 4, 8, 11, 12)` |
| face-diagonal | `{(0,0,0),(1,1,0)}` | both fill; history `(2, 7, 11, 12)` |
| opposite-corner `S*` | `{(0,0,0),(2,1,1)}` | both fill; history `(2, 8, 12)` |
| lex census through size 3 | 298 seeds | first split at `{(0,0,0),(0,0,1),(2,0,0)}` |
| `f_L1` from that `S` | some-axis-unbalanced predicate | fills; history `(3, 8, 11, 12)` |
| `f_mix0` from that `S` | remaining bits `(1,0,1,1,0)` | does not fill; history `(3, 8, 10)` |
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

**Steelman:** Same coverage on the `opp2=0` slice, same 1-site coverage,
and the same fill of `(0,0,0)`, the face-diagonal, and `S*` mean the
maps are dynamically the same, so the rival may be dropped or adopted
as `f_L1`.

**Answer:** The first size-at-most-three seed
`{(0,0,0),(0,0,1),(2,0,0)}` already splits both history and fill.
`f_mix0` halts at ten locks; `f_L1` fills. The maps also disagree on
`mixed3`. Admissibility does not name either map or this seed.

### N8 — cross-cycle echo

A first-distinguishing-seed census of `f_min` (#6417) and a cov=66
pair (#6431) are different claims. This note executes the first
distinguishing seed of `f_mix0` versus `f_L1` in the size-at-most-three
lex census.

**Gate disposition:** PASS for the finite first-seed statement and the
displayed histories. FAIL / DO NOT SHIP for “adopt `f_mix0`,” “adopt
`f_L1`,” “write a seed into Admissibility,” or “the maps are the same
dynamics on every two-cube seed.”

## Primary Runner

The primary runner rebuilds the two-cube, both predicates, the 298-seed
lex census, the three named-seed reconfirmations, the first
distinguishing seed with both histories and both fill bits, the
`mixed3` split at `(1,0,0)`, the current premise boundary, and the
non-adoption wording. It authors no audit verdict.
