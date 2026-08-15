---
claim_id: f_cut_f0_three_site_miss_orbit_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On the two-cube with off-patch o=0, the eight 3-site seeds that F_cut (1,1,1,1,0) does not fill form N_orb=1 orbit under two-cube-preserving rotations. One lex representative is {(0,0,0),(1,0,1),(2,0,0)}. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_f0_three_site_miss_orbit_2026_08_15.py
---

# The Eight Three-Site Misses Of F_cut (1,1,1,1,0) Are One Orbit

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact lock-evolution coverage and orbit count on the supplied
twelve-site two-cube `{0,1,2} × {0,1} × {0,1}` with off-patch occupancy
`o = 0`. The map `f0` with remaining bits `(1,1,1,1,0)` is displayed
cut-map data, not axiom content and not a selector.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_f0_three_site_miss_orbit_2026_08_15.py`](../scripts/f_cut_f0_three_site_miss_orbit_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

Work on the two-cube of twelve lattice sites
`{0,1,2} × {0,1} × {0,1}`. Off-patch occupancy is `0`. A seed locks its
sites. At each tick, every unlocked site whose six-neighbor axis type is
fired by the displayed map locks. The process fills when all twelve sites
are locked at halt.

`F_cut` is the family of cube-covariant `{0,1}`-maps on six-neighbor
occupancy with `f(empty) = f(full) = 0` and `f(c) = f(1-c)`. After those
constraints the remaining bits are
`(wt1, opp2, adj2, vertex3, mixed3)`. The displayed member is

```text
f0 = (1, 1, 1, 1, 0).
```

This is not `f_L1`. The L1 map is `n ≠ 0` (some axis unbalanced), with
bits `(1,0,1,1,1)`. It is not Hamming parity of the six neighbor bits,
which has bits `(1,0,0,1,1)`.

There are `C(12,3) = 220` three-site seeds. The map `f0` fills `212` of
them, so the missed set `M` has eight seeds. Let `G` be the
two-cube-preserving proper cube rotations: the `24` proper cubic
rotations, applied about the box center `(1, 1/2, 1/2)`, that permute
the twelve sites. Then

```text
N_orb = 1.
```

One lex representative of the unique orbit is

```text
{(0,0,0), (1,0,1), (2,0,0)}.
```

The geometric type is therefore a single `G`-orbit. The claim is that
orbit count and that one representative. An eight-row leftover table of
`M` is not the claim. Displayed, not adopted.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact lock evolution on the twelve-site two-cube enumerates the eight missed 3-site seeds of displayed f0 and proves they form one orbit under two-cube-preserving proper cube rotations."
trace_class: frontier_discovery
target_claim_id: f_cut_f0_three_site_miss_orbit
target_blocker_text: "geometric type of the eight three-site seeds that F_cut (1,1,1,1,0) misses"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
conditional_surface_status: "exact on the supplied two-cube with off-patch o=0 and displayed f0; no selector or Admissibility edit is asserted"
hypothetical_axiom_status: "not proposed; no axiom or approved primitive is added"
admitted_observation_status: null
next_trace_action: "independent audit of the bounded orbit-count claim"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Inputs And Import Boundary

- **Framework dependency:** the live Lattice, Admissibility, and Record
  sentences below supply site language, nearest-neighbor covariance, and
  the lock/unread rule. They are quoted without rewrite.
- **Explicit theorem-domain condition:** the twelve-site two-cube, off-patch
  occupancy `0`, the displayed `F_cut` bit tuple `f0 = (1,1,1,1,0)`,
  simultaneous ready-lock evolution, and the two-cube-preserving subset of
  the `24` proper cube rotations about the box center are supplied
  mathematical data for this theorem.
- **External empirical or literature inputs:** none.
- **Open physical bridge:** selection of `f0` by Admissibility or Record,
  and any physical naming of the missed orbit, remain separate open
  obligations outside the target proved here. Do not adopt f0.

## Exact Objects

Sites are the twelve points of `{0,1,2} × {0,1} × {0,1}`. A site outside
this set has occupancy `0`. For an unlocked site `v` the six neighbors
`v ± e_μ`, `μ ∈ {x,y,z}`, determine an axis type
`(n_unbalanced, n_both, n_empty)` with those three integers summing to
`3`. The named remaining types are

```text
wt1 = (1,0,2), opp2 = (0,1,2), adj2 = (2,0,1),
vertex3 = (3,0,0), mixed3 = (1,1,1).
```

Complement swaps empty with both and leaves unbalanced fixed, so
`mixed3` and `vertex3` are self-complementary. `F_cut` forces
`f(empty) = f(full) = 0` and equal values on each complementary pair.
The five remaining bits therefore label the `32` cut maps. The displayed
map `f0` fires every remaining type except `mixed3`.

`f_L1` fires iff `n_unbalanced ≥ 1`. Hamming parity of the six neighbor
occupancy bits equals the parity of `n_unbalanced`. Both differ from
`f0` on at least one remaining bit.

A seed `S` starts locked. Each tick locks every currently unlocked site
whose axis type is fired. Halt is the first tick with no new lock. Fill
means the halt lock set is the whole two-cube.

`G` is computed, not postulated: among the `24` proper cube rotations
(signed permutation matrices of determinant `1`), keep those whose
action about `(1, 1/2, 1/2)` permutes the twelve sites. That subset has
eight elements and includes the identity. Only those site permutations
are used.

## Exact Target And Proof Obligations

The exact target is the pair `(|M|, N_orb)` together with one lex
representative per `G`-orbit in `M`.

The obligation graph is:

1. enumerate all `220` three-site subsets of the two-cube;
2. run the lock evolution of displayed `f0` from each subset and collect
   the unfilled set `M`;
3. generate `G` as the two-cube-preserving proper cube rotations;
4. partition `M` into `G`-orbits and report `N_orb` with one lex
   representative per orbit.

All four obligations are closed below and in the runner. The two-cube,
off-patch default, and displayed bit tuple are theorem hypotheses.
Other patches, other maps, and any selector among `F_cut` are outside
this theorem.

## Theorem 1 — `|M| = 8`

Direct enumeration gives `C(12,3) = 220` three-site seeds. The lock
evolution of `f0` fills `212` of them and misses `8`. Thus `|M| = 8`.
The same evolution fills all `220` seeds for both `f_L1` and the
remaining-bit tuple `(1,1,1,1,1)`, so the eight misses are specific to
displayed `f0`, not to every cut map.

## Theorem 2 — `N_orb = 1` with one lex representative

Let `G` act on three-site subsets by applying each two-cube-preserving
proper cube rotation to the three sites. The eight members of `M` form a
single `G`-orbit. Therefore `N_orb = 1`. The lexicographically first
representative, with sites ordered as `(x,y,z)` and each seed written
in sorted site order, is

```text
{(0,0,0), (1,0,1), (2,0,0)}.
```

On that representative the `f0` lock history is `(3, 8, 10)`: the seed
locks three sites, two further waves lock five then two, and halt occurs
with ten locks, so the representative is unfilled. Because the eight
misses are one orbit, that one unfilled representative is the geometric
type. The other seven images are not independent extras and are not
listed as the claim.

## Theorem 3 — display `N_orb`; do not adopt `f0`

The displayed output is `N_orb = 1` and the representative
`{(0,0,0), (1,0,1), (2,0,0)}`. The map `f0` is theorem-domain data. This
note does not write `f0` into Admissibility, does not select it among
the `32` cut maps, and does not name the missed orbit as a physical
sector. Displayed, not adopted.

## Physical-Interpretation Boundary

The proved output is an orbit count on a supplied finite patch for a
displayed cut map. This note neither assigns the orbit a physical label
nor changes Lattice, Admissibility, or Record. No additional axiom is
proposed.

## Mutation Checks

Three non-equivalences guard the load-bearing conclusions:

1. `N_orb` is `1`, not `8`; treating the eight seeds as eight geometric
   types fails;
2. `f0` is not `f_L1` and is not Hamming parity;
3. the representative is unfilled, so the orbit is a genuine miss of
   `f0` rather than a filled seed mislabeled.

## What This Does Not Claim

- `f0` is not adopted as the physical nearest-neighbor rule.
- The eight missed seeds are not eight independent extras.
- No claim is made that Record locks the representative or that
  Admissibility selects mixed3-silence.
- Other `F_cut` tuples, other seed cardinalities, and the infinite
  lattice outside the two-cube are not classified.
- Independent class-`C` leftovers are not used as parents.

These are scope boundaries, not impossibility or route-exhaustion claims.
Accordingly, no no-go verdict is authored here.

## Live Parent Quotes

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

> There is one fixed nearest-neighbor admissibility rule, covariant under
> lattice translations and proper cubic rotations.

> When present, a record locks exactly one admissible local possibility.

> A site with no record cannot be read.

Their dependency role is limited to site language, covariance of a
nearest-neighbor rule, and the lock/unread vocabulary. This theorem
separately supplies the two-cube, the displayed cut map, and the orbit
count; physical selection of `f0` remains outside its target.

## Runner Contract

The companion runner checks Theorems 1–3 by enumerating the `220`
three-site seeds, evolving displayed `f0`, constructing `G` from the
`24` proper cube rotations, and computing `N_orb` with one lex
representative. It also checks the mutations, quotes the live axiom
sentences, prints substantive N5 scope certificates, and records the
import boundary. Declared review inputs are this note and the axiom
memo only.
