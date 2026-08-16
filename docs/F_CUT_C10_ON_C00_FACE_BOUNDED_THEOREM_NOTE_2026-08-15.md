---
claim_id: f_cut_c10_on_c00_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On the two-cube with off-patch o=0, whether F_cut (1,1,0,0,0) fills the #6493 four-site face of (1,0,0,0,0) is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_c10_on_c00_face_2026_08_15.py
---

# Whether `F_cut` `(1,1,0,0,0)` Fills The `#6493` Four-Site Face

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** displayed occupancy-to-lock dynamics on the twelve-vertex two-cube
`{0,1,2}×{0,1}×{0,1}` with off-patch occupancy identically `0`, started
from the `#6493` four-site face
`S={(0,0,0),(0,0,1),(0,1,0),(0,1,1)}`. Whether the cube-covariant map
`F_cut` remaining bits `(1,1,0,0,0)` fills that face is reported.
Displayed, not adopted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_c10_on_c00_face_2026_08_15.py`](../scripts/f_cut_c10_on_c00_face_2026_08_15.py)
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

Let `f00` and `f10` be the `F_cut` remaining-bit maps

```text
f00 = (wt1, opp2, adj2, vertex3, mixed3) = (1, 0, 0, 0, 0)
f10 = (wt1, opp2, adj2, vertex3, mixed3) = (1, 1, 0, 0, 0)
```

with complements forced. The seed

```text
S = {(0,0,0), (0,0,1), (0,1,0), (0,1,1)}
```

is the `#6493` lex-first four-site face that `f00` fills. Naming that
face as leftover-character of `#6493` does not adopt it. The map `f10`
first fills a different size-`3` seed (leftover-character of `#6496`).
The object of this note is whether `f10` fills this same four-site face.

This is a new pair on a displayed seed. It is not a second named-pair
fill of `#6492`.

**Theorem 1.** `f00` fills `S`. The lock history is `(4, 8, 12)` and
`|locks_halt|=12`. This reconfirms the `#6493` face fill.

**Theorem 2.** `f10` also fills `S`. The lock history is `(4, 8, 12)`
and `|locks_halt|=12`. On this face the executed remaining-bit orbit is
only `wt1`; the `opp2` bit that separates the maps is not seen.

**Theorem 3.** The fill bits and both histories are displayed only. Do
not adopt a bit. Do not adopt a seed. Do not write a remaining bit into
Admissibility. The seed is not written into Admissibility.

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
predicate. The maps `f00` and `f10` are supplied displayed members, not
axiom content. The face `S` is likewise displayed data, not an
admissibility rule.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Finite exact occupancy ticks of two displayed F_cut maps on one four-site face of the twelve-vertex two-cube."
trace_class: frontier_discovery
target_claim_id: f_cut_c10_on_c00_face
target_blocker_text: "whether F_cut remaining bits (1,1,0,0,0) fills the #6493 four-site face of (1,0,0,0,0)"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the bounded face-fill report; do not adopt a bit"
conditional_surface_status: "exact on the two-cube with off-patch o=0 for this displayed face; the maps remain displayed"
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
`f00(c)=1` iff the axis type is `wt1=(1,0,2)` or `wt5=(1,2,0)`. Its
remaining-bit tuple is `(1,0,0,0,0)`.
`f10(c)=1` iff the axis type is `wt1=(1,0,2)`, `opp2=(0,1,2)`,
`wt5=(1,2,0)`, or `opp2c=(0,2,1)`. Its remaining-bit tuple is
`(1,1,0,0,0)`.

On those representatives the bits are

| map | wt1 | opp2 | adj2 | type210 | vertex3 | mixed3 | empty | full | wt5 | opp2c |
|---|---|---|---|---|---|---|---|---|---|---|
| `f_L1` | 1 | 0 | 1 | 1 | 1 | 1 | 0 | 0 | 1 | 0 |
| `f00` | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 |
| `f10` | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 |

Hamming parity of `|c|_1` is a different predicate: `opp2` is even and
`f_L1(opp2)=0`, while `f10(opp2)=1`.

One tick locks every currently unlocked on-patch site whose neighbor
tuple has `f=1`. The process starts with `locks_0=S` and halts at the
first fixed point, or at tick `12`. Lock history is the sequence of
cardinalities from `t=0` through halt. Fill means `|locks_halt|=12`.

The displayed seed is the entire `x=0` face of the two-cube. It is
not the `#6496` size-`3` first-fill seed of `f10`, and it is not the
`#6492` size-`3` named pair.

## Theorem 1 — `f00` fills `S`

Start with `S={(0,0,0),(0,0,1),(0,1,0),(0,1,1)}`, so `|locks_0|=4`.

At tick `1` the four middle-slice sites
`(1,0,0)`, `(1,0,1)`, `(1,1,0)`, `(1,1,1)`
each see a single occupied nearest neighbor along `-x` (type `wt1`),
so `f00` returns `1`. The four `x=2` sites see the empty tuple and
stay unlocked. After tick `1` one has `|locks_1|=8`.

At tick `2` the four `x=2` sites each see a single occupied nearest
neighbor along `-x` (type `wt1`) and lock. The run fills:

`T=2`, `|locks_halt|=12`, history `(4, 8, 12)`, fill bit `1`.

This reconfirms the `#6493` face fill of remaining bits `(1,0,0,0,0)`.

## Theorem 2 — whether `f10` fills `S`

From the same `S`, the first wave of `f10` is identical. The four
middle-slice sites again see type `wt1`, which `f10` accepts. The four
`x=2` sites again see the empty cut, which `F_cut` rejects. After tick
`1` one has `|locks_1|=8`.

At tick `2` the four `x=2` sites again see type `wt1` and lock. The
run fills:

`T=2`, `|locks_halt|=12`, history `(4, 8, 12)`, fill bit `1`.

So `f10` fills this same four-site face. The executed remaining-bit
orbit on the run is only `wt1`. The `opp2` cell that separates `f10`
from `f00` does not appear. Empty is the `F_cut` empty cut, not a
remaining-bit refuse.

The lock history is recorded either way: here both maps fill, and both
histories are `(4, 8, 12)`.

This is not the `#6496` first fill of `f10`. That first fill is the
different size-`3` seed `{(0,0,0),(1,1,1),(2,0,0)}`, on which `f00`
does not fill. Agreement on this face is therefore not identity of
the two maps.

## Theorem 3 — display; do not adopt a bit

The fill bits, the common history `(4, 8, 12)`, and the face `S` are
displayed data. Do not adopt a bit. Do not adopt `f10`. Do not adopt
`opp2`. Do not adopt a seed. Do not write a remaining bit into
Admissibility. The seed is not written into Admissibility.

Displayed, not adopted.

## Exact Target And Obligation Graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record wording | quoted; no edit |
| two-cube, off-patch `o=0`, displayed face `S` | declared finite data |
| `f00` fills `S` | recomputed; history `(4, 8, 12)` |
| whether `f10` fills `S` | yes; history `(4, 8, 12)` |
| identity with the `#6496` first fill | refused; different seed |
| second named-pair fill of `#6492` | refused; different seed |
| adoption of a bit, a map, or the seed | refused |
| formation site / rate from the axioms | open |

## Boundary And Imports

No observation, fit, continuum limit, or Hamming-as-`f_L1`
identification is imported. The two-cube, the predicates `f00` and
`f10`, and the face `S` are supplied mathematical data for this note.
Record lock language is quoted only as the existing lock/content/absence
boundary; it does not select either map or any seed.

## Promotion Value Gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers whether `f10` fills the `#6493` four-site face of `f00`. |
| V2 | Current main has the axiom memo and no landed report of this pair on this face. |
| V3 | The twelve-vertex process from this face is independently finite and exact. |
| V4 | The theorem is more than restating Admissibility: it executes two supplied predicates the axiom does not name. |
| V5 | Neither map, nor the `opp2` bit, nor the face is an admissibility rule, and none is adopted. |

## No-Go Discipline Gate

The negative content is narrow: a displayed fill on a displayed face is
not an axiom-level occupancy rule, and a remaining bit is not axiom
content.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| `f00` from `S` | remaining bits `(1,0,0,0,0)` | fills; history `(4, 8, 12)` |
| `f10` from `S` | remaining bits `(1,1,0,0,0)` | fills; history `(4, 8, 12)` |
| `opp2` on this run | evaluate cells on `S` | only `wt1` and empty appear |
| `#6496` first fill | size-`3` seed `{(0,0,0),(1,1,1),(2,0,0)}` | `f10` fills; `f00` does not |
| `#6492` named pair | that same size-`3` seed | a different seed; not this face |
| Hamming parity | `|c|_1 mod 2` | different predicate; `opp2` even |
| write a bit or seed into Admissibility | treat either as the local rule | refused; axiom is not a dynamics axiom |

### N2 — wall independence

The missing formation-site selector, the missing axiom-level
occupancy rule, and the choice among displayed members are distinct
open items. This note claims no complete wall and no compiler no-go.

### N3 — hidden-condition scan

The two-cube, off-patch `o=0`, the face `S`, six-neighbor order, and
the predicates `f00` and `f10` are declared. Cube covariance is used
only as the axis-type reading of a six-tuple. No continuum, Hamming,
or admissibility rewrite is assumed.

### N4 — source residual matching

The axiom memo supplies the cubic nearest-neighbor graph and states
that Admissibility is not a dynamics axiom and does not supply the
formation site, probability, or rate. The residual therefore matches
those sources: displayed lock predicates and a displayed face are
extra data.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | axis-type representatives and off-patch `0` | no alphabet classification |
| per site | every two-cube vertex against both displayed lock predicates | no derived kernel values |
| per mode | no mode calculation | no spectral exhaustion |
| per block | the displayed four-site face to a fixed point | no physical compiler |
| lattice wide | checked and not executed | neither map nor bit adopted as a rule |

### N6 — live partial-closure paths

Live routes include an independent reason to select or reject `f10`,
a census of other faces, and a formation mechanism supplied by
something other than a displayed predicate.

### N7 — hostile steelman

**Steelman:** `#6496` already said `f10` first fills at size `3`, so
asking whether it fills the later `#6493` face is either automatic or
a second named-pair fill of the `#6492` seed.

**Answer:** First fill at a different size-`3` seed does not decide
this face. The `#6492` seed is `{(0,0,0),(1,1,1),(2,0,0)}`, on which
the two maps disagree. This note executes the different displayed
face `S` and reports that both maps fill it, with common history
`(4, 8, 12)`.

### N8 — cross-cycle echo

A first-fill seed of remaining bits `(1,0,0,0,0)` (#6493), a first-fill
seed of remaining bits `(1,1,0,0,0)` (#6496), and a named-pair fill
on the `#6492` seed are different claims. This note reports whether
`f10` fills the `#6493` face.

**Gate disposition:** PASS for the finite face-fill report and the
displayed histories. FAIL / DO NOT SHIP for “adopt `f10`,” “adopt a
bit,” “write a remaining bit into Admissibility,” or “this is a second
named-pair fill of `#6492`.”

## Primary Runner

The primary runner rebuilds the two-cube, the predicates `f00` and
`f10`, the `#6493` face fill of `f00`, the fill bit and lock history
of `f10` on that face, the `wt1`-only wave, the distinction from the
`#6496` and `#6492` seeds, the current premise boundary, and the
non-adoption wording. It authors no audit verdict.
