---
claim_id: f_cut_c00_four_site_fill_orbit_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On the two-cube with off-patch o=0, the seven 4-site seeds that F_cut (1,0,0,0,0) fills form N_orb orbits under two-cube-preserving rotations. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_c00_four_site_fill_orbit_2026_08_15.py
---

# Orbit Type Of The Seven Four-Site Seeds `F_cut` `(1,0,0,0,0)` Fills

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** orbit count of the seven four-site seeds on the twelve-vertex
two-cube `{0,1,2}×{0,1}×{0,1}` that the displayed `F_cut` remaining-bit
map `(1,0,0,0,0)` fills, under the proper cube rotations about the box
center `(1, 1/2, 1/2)` that permute those twelve sites, with off-patch
occupancy identically `0`. The integer `N_orb` and one lexicographic
representative per orbit are displayed, not adopted. The seven seeds
are not listed.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_c00_four_site_fill_orbit_2026_08_15.py`](../scripts/f_cut_c00_four_site_fill_orbit_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

Write the two-cube as the twelve sites `{0,1,2}×{0,1}×{0,1}`. A site
locks when a displayed predicate of its six-neighbor occupancy tuple
returns `1`. Off-patch neighbors contribute occupancy `0`. A
blank-block is a different rule; it is not used. A run is the tuple of
lock-set cardinalities from the seed through halt. Fill means
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
`(1,2,0)`.

Let `M` be the set of unordered four-site seeds that `f00` fills on
this two-cube. Let `G` be the group of two-cube-preserving rotations:
those proper cube rotations about `(1, 1/2, 1/2)` that permute the
twelve sites. Sixteen of the twenty-four ambient proper cubic matrices
send at least one site off the two-cube and are not used. The remaining
eight induce `G`. `N_orb` is the number of `G`-orbits in `M`. One lex
representative is kept per orbit.

**Theorem 1.** `|M|=7` among the `495` four-site seeds. The `#6493`
face

`S={(0,0,0),(0,0,1),(0,1,0),(0,1,1)}`

is in `M`.

**Theorem 2.** `N_orb = 3`. The three orbits have sizes `2`, `4`, and
`1`. One lex representative per orbit is

- size `2`: `{(0,0,0),(0,0,1),(0,1,0),(0,1,1)}` (the `#6493` face);
- size `4`: `{(0,0,0),(0,0,1),(2,1,0),(2,1,1)}`;
- size `1`: `{(1,0,0),(1,0,1),(1,1,0),(1,1,1)}`.

**Theorem 3.** Display `N_orb = 3`. Do not list all seven. Do not adopt
an orbit. Do not write an orbit into Admissibility.

Displayed, not adopted.

This is new geometry of the fill set `M`. It is not leftover-character
of `#6493` (that named the lex-first face and the fill count `7`). It
is not `N_orb` of a miss set.

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
content. A seed, an orbit, and the integer `N_orb` are likewise
displayed data, not an admissibility rule. The seed is not written into
Admissibility.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Finite exact orbit count of the seven four-site seeds that one displayed F_cut map fills on a twelve-vertex two-cube under two-cube-preserving rotations."
trace_class: frontier_discovery
target_claim_id: f_cut_c00_four_site_fill_orbit
target_blocker_text: "N_orb of the seven four-site seeds that F_cut (1,0,0,0,0) fills under two-cube-preserving rotations"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the bounded fill-set orbit count; do not adopt an orbit"
conditional_surface_status: "exact on the two-cube with off-patch o=0; N_orb remains displayed data"
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
first fixed point, or at tick `12`. Fill means `|locks_halt|=12`.

`M` is the set of four-site combinations that fill under `f00`. Seeds
in `M` are compared as unordered four-sets. The ambient proper cubic
group about the box center `(1, 1/2, 1/2)` is the `24` signed
permutations of the three axes with determinant `+1`. A matrix is kept
in `G` only when it permutes the twelve sites. If a rotation does not
preserve the twelve-set, it is not used.

An orbit representative is the lexicographically least four-tuple in
that orbit, using the lexicographic site order above.

## Theorem 1 — `|M|=7` and the `#6493` face

Among the `C(12,4)=495` unordered four-site seeds, `f00` fills exactly
seven. That reconfirms the `#6493` fill count.

The `#6493` face `S={(0,0,0),(0,0,1),(0,1,0),(0,1,1)}` is one of those
seven. From that seed the lock history is `(4, 8, 12)` and the run
fills. The face is therefore in `M`.

## Theorem 2 — `N_orb` and one lex representative per orbit

Act with `G` on `M`. The action partitions `M` into three orbits:

`N_orb = 3`

The orbit of the `#6493` face has size `2`. Its lex representative is
that face itself. The second orbit has size `4`; its lex representative
is `{(0,0,0),(0,0,1),(2,1,0),(2,1,1)}`. The third orbit is a singleton;
its lex representative is the middle slice
`{(1,0,0),(1,0,1),(1,1,0),(1,1,1)}`.

Those three representatives are the displayed orbit type of the fill
set. They are not a listing of `M`.

## Theorem 3 — display `N_orb`; do not list the seven

The integer to report is `N_orb = 3`. The seven members of `M` are not
listed. The three lex representatives name orbit type, not a census of
every filler.

Do not adopt `f00`. Do not adopt an orbit. Do not write an orbit into
Admissibility. Admissibility is not a dynamics axiom and does not
supply this predicate, this fill set, or this orbit count.

A fill count of `7` is not an orbit type. The orbit type of `M` is a
new finite object on this two-cube. It is not `N_orb` of a miss set.

## Exact Target And Obligation Graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record wording | quoted; no edit |
| two-cube, off-patch `o=0`, four-site seeds | declared finite data |
| `|M|=7` and `#6493` face in `M` | recomputed |
| `N_orb` under two-cube-preserving rotations | `3` |
| one lex representative per orbit | three displayed |
| listing of all seven members of `M` | refused |
| adoption of the orbit or the map | refused |
| formation site / rate from the axioms | open |

## Boundary And Imports

No observation, fit, continuum limit, or Hamming-as-`f_L1`
identification is imported. The two-cube, the predicate `f00`, the
fill-set `M`, and the two-cube-preserving rotation group are supplied
mathematical data for this note. Record lock language is quoted only
as the existing lock/content/absence boundary; it does not select this
map or any orbit.

## Promotion Value Gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers how many `G`-orbits the seven four-site `f00` fillers form. |
| V2 | Current main has the axiom memo and the `#6493` face/count, not this fill-set orbit type. |
| V3 | The twelve-vertex fill census and the eight-element group action are independently finite and exact. |
| V4 | The theorem is more than restating Admissibility: it executes a supplied predicate and a supplied group the axiom does not name. |
| V5 | Neither the map nor the orbit is an admissibility rule, and neither is adopted. |

## No-Go Discipline Gate

The negative content is narrow: a fill count of `7` is not an orbit
type, an orbit type of a fill set is not an orbit type of a miss set,
and a displayed orbit is not axiom content.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| four-site census | all `495` seeds | `|M|=7` |
| `#6493` face membership | run from `{(0,0,0),(0,0,1),(0,1,0),(0,1,1)}` | fills; in `M` |
| ambient proper cubes | `24` signed permutations, `det=+1` | sixteen discarded |
| two-cube-preserving `G` | keep only twelve-set permutations | `|G|=8` |
| orbit partition of `M` | `G` acting on the seven fillers | `N_orb = 3` |
| lex representatives | least four-tuple per orbit | three displayed |
| list all seven | write every member of `M` | refused |
| Hamming parity | `|c|_1 mod 2` | different predicate; `adj2` even |
| write an orbit into Admissibility | treat `N_orb` as the local rule | refused; axiom is not a dynamics axiom |

### N2 — wall independence

The missing formation-site selector, the missing axiom-level
occupancy rule, and the choice among displayed members are distinct
open items. This note claims no complete wall and no compiler no-go.

### N3 — hidden-condition scan

The two-cube, off-patch `o=0`, six-neighbor order, the remaining-bit
tuple `(1,0,0,0,0)`, and the restriction to two-cube-preserving
rotations are declared. Cube covariance is used only as the axis-type
reading of a six-tuple and as the ambient cubic group. No continuum,
Hamming, miss-set orbit, or admissibility rewrite is assumed.

### N4 — source residual matching

The axiom memo supplies the cubic nearest-neighbor graph and states
that Admissibility is not a dynamics axiom and does not supply the
formation site, probability, or rate. The extra therefore matches
those sources: a displayed lock predicate, a displayed fill set, and a
displayed orbit count are extra data.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | axis-type representatives and off-patch `0` | no alphabet classification |
| per site | every two-cube vertex against `f00` | no derived kernel values |
| per mode | no mode calculation | no spectral exhaustion |
| per block | all `495` four-site seeds and the `G`-action on `M` | no physical compiler |
| lattice wide | checked and not executed | neither map nor orbit adopted as a rule |

### N6 — live partial-closure paths

Live routes include an independent reason to select or reject `f00`,
the orbit type of the other `#6490` exception `(1,1,0,0,0)`, and a
formation mechanism supplied by something other than a displayed
predicate.

### N7 — hostile steelman

**Steelman:** `#6493` already counted seven four-site fillers and named
the lex-first face, so either those seven are one face-type orbit or
the miss-set orbit count of a different map already names the geometry.

**Answer:** The seven fillers form `N_orb = 3` orbits under
two-cube-preserving rotations, with lex representatives the `#6493`
face, a size-`4` mixed pair, and the middle slice. That is a displayed
finite fact about the fill set `M`, not about a miss set.
Admissibility does not name `f00` or this orbit type.

### N8 — cross-cycle echo

A lex-first four-site face (`#6493`) and a fill count of `7` are
different claims from the orbit type of that fill set. This note
executes `N_orb` of the seven four-site seeds that `F_cut` `(1,0,0,0,0)`
fills. It is not leftover-character of `#6493`. New finite object: the
fill-set orbit type.

**Gate disposition:** PASS for the finite fill-set orbit statement and
the displayed `N_orb`. FAIL / DO NOT SHIP for “adopt `f00`,” “write an
orbit into Admissibility,” “list all seven,” or “this is `N_orb` of a
miss set.”

## Primary Runner

The primary runner rebuilds the two-cube, the predicate `f00`, the
four-site fill set `M`, membership of the `#6493` face, the
two-cube-preserving rotation group, the orbit count `N_orb`, one lex
representative per orbit, the current premise boundary, and the
non-adoption wording. It does not list all seven in the note contract.
It authors no audit verdict.
