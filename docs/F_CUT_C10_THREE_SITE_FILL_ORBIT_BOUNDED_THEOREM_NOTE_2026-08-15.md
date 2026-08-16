---
claim_id: f_cut_c10_three_site_fill_orbit_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On the two-cube with off-patch o=0, the four 3-site seeds that F_cut (1,1,0,0,0) fills form N_orb=1 orbits under two-cube-preserving rotations. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_c10_three_site_fill_orbit_2026_08_15.py
---

# Orbit Type Of The Four Three-Site Fills Of `F_cut` `(1,1,0,0,0)`

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact occupancy-to-lock 3-site fill set of the cube-covariant
complement-even map in `F_cut` with remaining-bit tuple `(1, 1, 0, 0, 0)`,
on the twelve-vertex two-cube, with off-patch occupancy `0`, together with
the number of orbits of that fill set under two-cube-preserving proper
cube rotations about the box center. The orbit count and one lex
representative are displayed. The map is not adopted as the physical
Admissibility rule. Do not list all four.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_c10_three_site_fill_orbit_2026_08_15.py`](../scripts/f_cut_c10_three_site_fill_orbit_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

The 24 proper cube rotations act on neighbor 6-tuples in `{0,1}^6` and
partition those 64 cells into 10 orbits. Cube-covariant predicates are the
`{0,1}`-assignments to those orbits. The three displayed cuts

1. vanish on empty: `f(empty)=0`,
2. vanish on full: `f(full)=0`,
3. complement-even: `f(c)=f(1-c)`

leave five free bits, so

```text
|F_cut| = 32.
```

The five remaining bits, in the displayed order
`(wt1, opp2, adj2, vertex3, mixed3)`, are the values on the three
complement-pairs and two complement-fixed orbits after empty and full are
forced to `0`. Write `f10` for remaining bits `(1, 1, 0, 0, 0)`. This map
has `wt1=1` and is the second `#6490` exception (`cov2=0` with `wt1=1`).

Not leftover-character of #6496: that counted `|M|=4`. The present object
is the orbit type of that already-counted fill set under two-cube
rotations. New geometry of a counted fill set of the second exception.

On the two-cube `{0,1,2}×{0,1}×{0,1}`, each unordered triple of vertices is
a 3-site seed. There are `C(12,3)=220` such seeds. Off-patch neighbors
have occupancy `0`. Each tick, every unlocked on-patch vertex evaluates
`f` on its six-neighbor occupancy tuple and locks if `f=1`. The process
is synchronous and stops at a fixed point in at most 12 ticks. Fill means
`|locks_halt|=12`. Write `M` for the set of 3-site seeds that `f10` fills.

`f_L1(c)=1` if and only if some axis is unbalanced: `c_{+μ} ≠ c_{-μ}` for
at least one `μ ∈ {x,y,z}`. Equivalently, some discrete neighbor contrast
`n_μ = c_{+μ} − c_{-μ}` is nonzero. This is **not** Hamming parity
`|c|_1 mod 2`. The remaining-bit tuple of `f_L1` is `(1, 0, 1, 1, 1)`.
That map is a control, not a scored exception.

The group `G` is the set of proper cube rotations about the box center
`(1, 1/2, 1/2)` that permute the twelve vertices. Rotations that do not
preserve the 12-set are discarded. That group has order 8: it is the
square-prism rotation group that keeps the long axis of the two-cube.

**Theorem 1.** Exhaustive evaluation of `f10` on all 220 three-site seeds
gives

```text
|M| = 4.
```

The `#6492` seed `{(0,0,0),(1,1,1),(2,0,0)}` is an element of `M`.

**Theorem 2.** The fill set `M` is a single `G`-orbit. There is one lex
representative:

```text
N_orb = 1
lex representative = {(0,0,0),(1,1,1),(2,0,0)}.
```

That representative is the `#6492` seed. Do not list all four.

**Theorem 3.** The integer `N_orb = 1` is displayed. The orbit is not
adopted as the physical Admissibility rule.

Do not write the orbit into Admissibility.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The ten-orbit reconstruction, the 32-element F_cut, membership of f10=(1,1,0,0,0), the exact fill count |M|=4, membership of the #6492 seed, and the orbit count N_orb=1 under the order-8 two-cube-preserving rotation group are enumerated. No physical law is selected."
trace_class: upstream_support
target_claim_id: f_cut_c10_three_site_fill_orbit
target_blocker_text: "what is the orbit type of the four 3-site seeds that f10 fills"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the f10 3-site fill-orbit count; any physical use must separately derive an Admissibility selector"
conditional_surface_status: "exact for f10 on this twelve-vertex patch with off-patch o=0 and the order-8 two-cube-preserving rotation group; no Z^3-wide law and no physical selector"
hypothetical_axiom_status: "not proposed; no axiom or approved primitive is added"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Premises And Declared Mathematical Objects

The only scientific dependency is the current four-axiom authority linked
above. Lattice supplies `Z^3`, nearest-neighbor adjacency, and proper cubic
rotations. Admissibility supplies one fixed nearest-neighbor rule covariant
under those rotations. Record supplies permanence of a lock and unreadability
of an absent record. Qubit is unused beyond the ambient one-site algebra
boundary: the maps here are Boolean occupancy predicates, not `M_2(C)`-valued
laws.

The following are declared mathematical scaffolding, not measured or fitted
physics inputs:

- the 24 proper signed-permutation rotations of the three axes
  (`det = +1`);
- occupancy 6-tuples on the ordered neighbor stencil
  `(+x,-x,+y,-y,+z,-z)`;
- the two-cube vertex set `{0,1,2}×{0,1}×{0,1}`;
- the off-patch occupancy default `0`;
- the complete set of 220 unordered 3-site seeds;
- the remaining-bit tuple `(1, 1, 0, 0, 0)`;
- the `#6492` seed `{(0,0,0),(1,1,1),(2,0,0)}`;
- proper cube rotations about the box center that preserve the 12-set.

No observational comparator, literature constant, Wilson weight, rate, or
generator is imported. No Record scalar functional appears.

## Exact Target And Objects

**Target.** Reconfirm that `f10` fills exactly four 3-site seeds and that
the `#6492` seed is among them. Report `N_orb` of that fill set under
two-cube-preserving rotations, with one lex representative per orbit.
Display `N_orb`. Do not list all four. Do not adopt a seed.

Write a neighbor configuration as `c ∈ {0,1}^6`. A proper cube rotation `R`
acts by `(R·c)(d) = c(R^{-1}d)` on the six face directions `d`. A map
`f:{0,1}^6 → {0,1}` is cube-covariant when `f(R·c)=f(c)` for every such `R`.
Equivalently, `f` is constant on each orbit.

The axis type of `c` is the triple `(u,b,e)` with `u+b+e=3`, where `u` is
the number of axes with `c_{+} ≠ c_{-}`, `b` the number with
`(c_{+},c_{-})=(1,1)`, and `e` the number with `(c_{+},c_{-})=(0,0)`. These
ten types are exactly the ten orbits. Complement sends `(u,b,e)` to
`(u,e,b)`.

| remaining name | `(u,b,e)` | orbit size | complement image |
|---|---|---:|---|
| empty | `(0,0,3)` | 1 | full |
| full | `(0,3,0)` | 1 | empty |
| `opp2` | `(0,1,2)` | 3 | `(0,2,1)` |
| `wt1` | `(1,0,2)` | 6 | `(1,2,0)` |
| `adj2` | `(2,0,1)` | 12 | `(2,1,0)` |
| `mixed3` | `(1,1,1)` | 12 | itself |
| `vertex3` | `(3,0,0)` | 8 | itself |

`F_cut` is the class of cube-covariant maps with `f(empty)=f(full)=0` and
`f(c)=f(1-c)`. The empty/full pair is forced to `0`. The remaining free
data are three complement-pair bits and two complement-fixed orbit bits,
so `|F_cut|=32`. The remaining-bit tuple is those five bits in the order
`(wt1, opp2, adj2, vertex3, mixed3)`.

Define

```text
f10(c)      = 1  iff  the remaining-bit assignment is (1, 1, 0, 0, 0),
f_L1(c)     = 1  iff  u(c) ≥ 1.
```

So `f10` fires on `wt1` and `opp2` (and their complements), and `f_L1`
has remaining bits `(1, 0, 1, 1, 1)`. Neither map is adopted.

A locked set `S` determines occupancies: a lattice neighbor in `S` has
occupancy `1`, and every other neighbor — including every off-patch
neighbor — has occupancy `0`. One synchronous tick replaces `S` by

```text
S ∪ { v in two-cube \ S : f(neighborhood_6(v; S)) = 1 }.
```

Then `M` is the set of 3-site seeds whose halt set has cardinality 12.

The group `G` is obtained from the 24 proper cube rotations by acting
about the box center `(1, 1/2, 1/2)` and retaining only those maps that
permute the twelve vertices. If a rotation does not preserve the 12-set,
it is not used. The surviving group has order 8. Two seeds lie in the
same `G`-orbit when a surviving rotation carries one unordered triple
onto the other. `N_orb` is the number of such orbits in `M`. The lex
representative of an orbit is the unique seed whose sorted triple of
sites is minimal in dictionary order.

## Theorems

**Theorem 1.** There are exactly 24 proper cube rotations and exactly 10
orbits on `{0,1}^6`. The three cuts leave `|F_cut|=32`. The map `f10` is
one of those 32 members. The unbalanced-axis map `f_L1` is one element of
`F_cut` and is not Hamming parity. On the twelve-vertex two-cube with
off-patch occupancy `0`, exhaustive evaluation of `f10` on all 220
three-site seeds gives

```text
|M| = 4.
```

The `#6492` seed `{(0,0,0),(1,1,1),(2,0,0)}` belongs to `M`.

**Theorem 2.** Exactly eight of the 24 proper cube rotations about the
box center permute the twelve vertices. The fill set `M` is closed under
that group and forms a single orbit:

```text
N_orb = 1.
```

The unique lex representative is the `#6492` seed
`{(0,0,0),(1,1,1),(2,0,0)}`. Do not list all four.

**Theorem 3.** The integer

```text
N_orb = 1
```

is displayed. The orbit is not adopted as the physical Admissibility
rule.

## Proof-Obligation Graph

| obligation | exact disposition |
|---|---|
| 24 proper cube rotations | signed permutations of the three axes with determinant `+1` |
| 10 orbits on `{0,1}^6` | axis-type classes `(u,b,e)` partition the 64 cells with the listed sizes |
| `|F_cut|=32` | three complement-pairs and two complement-fixed orbits remain free after empty/full are forced to `0` |
| `f10` in `F_cut` | remaining-bit tuple `(1, 1, 0, 0, 0)` |
| 220 three-site seeds | `C(12,3)` unordered triples on the two-cube |
| `f_L1` is not Hamming | unbalanced-axis predicate disagrees with `|c|_1 mod 2` and has remaining bits `(1, 0, 1, 1, 1)` |
| `|M|=4` with `#6492` in `M` | exhaustive fill census; the displayed seed fills |
| `|G|=8` | two-cube-preserving proper rotations about the box center |
| `N_orb=1` | `M` is one `G`-orbit; lex representative is the `#6492` seed |
| displayed integer | `N_orb=1`, not adopted |

## What This Does Not Claim

- No physical Admissibility selector.
- No `Z^3`-wide formation law.
- No listing of the four seeds as independent extras.
- No ranking of the other 31 maps in `F_cut`.
- No blank-block or 4-site variant.

## No-Go Discipline Gate

The only negative claim is adoption: the orbit of the four fills is not
written into Admissibility. The positive pair `|M|=4` and `N_orb=1` is
an exact enumeration, not a wall.

### N1 — materially distinct routes

| Route | Exact attack | Result and authority | Marker |
|---|---|---|---|
| orbit reconstruction | Recompute the 24 rotations and the 10 axis-type orbits. | Theorem 1 and checks `thm1-twenty-four-rotations` / `thm1-ten-orbits`. | **ATTEMPTED** |
| three-cut class | Force vanish-on-empty, vanish-on-full, and `f(c)=f(1-c)`. | Theorem 1 and check `thm1-f-cut-and-f10` place `f10` in `|F_cut|=32`. | **ATTEMPTED** |
| Hamming-as-`f_L1` | Test whether `|c|_1 mod 2` equals the unbalanced-axis predicate. | Theorem 1 and check `thm1-f-L1-not-hamming` separate the maps. | **ATTEMPTED** |
| fill census | Score `f10` on all 220 three-site seeds and test the `#6492` seed. | Theorem 1 and check `thm1-fill-count-and-6492` give `|M|=4` with that seed in `M`. | **ATTEMPTED** |
| two-cube group and `N_orb` | Restrict to rotations that preserve the 12-set and orbit `M`. | Theorem 2 and checks `thm2-preserving-group` / `thm2-n-orb-and-lex-rep` give `|G|=8` and `N_orb=1`. | **ATTEMPTED** |
| adopt an orbit | Write the orbit or the `#6492` seed into Admissibility. | Theorem 3 and check `thm3-display-not-list-four`. | **ATTEMPTED** |

### N2 — wall independence and collapse

There is one negative conclusion: the displayed orbit is not adopted.
The count `|M|=4` and the orbit type `N_orb=1` are two certificates of
the same fill set, not two walls.

| Pair | First closes second? | Second closes first? | Disposition |
|---|---:|---:|---|
| `|M|=4` / `N_orb=1` | no: a raw count does not name the group action | no: one orbit does not name the seed cardinality without `|G|` | independent positive integers |
| `#6492` membership / `N_orb=1` | no: one seed in `M` does not force a single orbit | no: a single orbit does not name which seed is lex-first without the order | membership versus orbit type |
| leftover `#6496` count / this `N_orb` | no: `|M|=4` is not an orbit type | no: `N_orb=1` does not replace the seed count | New geometry |
| static `#6490` pair / this fill orbit | no: `cov2=0` is not 3-site dynamics | no: a 3-site orbit does not replace the 2-site exception | different `|S|` |

Physical law selection is not a wall: this note makes no negative theorem
about the existence of a selector and simply does not claim one.

### N3 — hidden-condition scan

| Phrase or premise | Classification |
|---|---|
| “work on the twelve-vertex two-cube” | explicit patch hypothesis; not a `Z^3` theorem |
| off-patch occupancy `0` | explicit default; blank-block is a different rule |
| `F_cut` | explicit three-cut class; the other 992 covariant maps are excluded |
| remaining bits `(1, 1, 0, 0, 0)` | explicit scored map; the other 31 maps are unclaimed |
| all 220 three-site seeds | explicit seed class; a 2-site ranking is a different residual |
| two-cube-preserving rotations | explicit restriction of the 24 cube rotations to the 12-set |
| “lock” | Record permanence on this Boolean occupancy model, not a possibility-valued law |
| “cube-covariant” | invariance under the 24 proper rotations, cited to Lattice/Admissibility |
| Hamming parity | displayed mutation only |
| remaining-bit tuple `(1, 1, 0, 0, 0)` and the `#6492` seed | displayed witnesses, not selected laws |

### N4 — citation-to-residual matching

| Evidence path:line | Residual attacked | Residual claimed closed | Match? |
|---|---|---|---:|
| `docs/MINIMAL_AXIOMS_2026-06-29.md:37` | ambient lattice and cubic rotations | sites are `Z^3` with proper cubic rotations | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:57` | covariant nearest-neighbor rule | covariance is the class filter, not a selector | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:79` | lock permanence | a locked site stays locked | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:83` | unreadability of absence | unlocked and off-patch sites contribute occupancy `0`, not a readout | yes |
| `scripts/f_cut_c10_three_site_fill_orbit_2026_08_15.py:75` | 24 proper rotations | signed permutations with determinant `+1` | yes |
| `scripts/f_cut_c10_three_site_fill_orbit_2026_08_15.py:122` | `f_L1` definition | unbalanced-axis predicate, not Hamming | yes |
| `scripts/f_cut_c10_three_site_fill_orbit_2026_08_15.py:127` | Hamming mutation | `|c|_1 mod 2` is a different map | yes |
| `scripts/f_cut_c10_three_site_fill_orbit_2026_08_15.py:50` | 220 three-site seeds | `C(12,3)` unordered triples on the two-cube | yes |
| `scripts/f_cut_c10_three_site_fill_orbit_2026_08_15.py:60` | `f10` remaining bits | `(1, 1, 0, 0, 0)` | yes |
| `scripts/f_cut_c10_three_site_fill_orbit_2026_08_15.py:62` | `#6492` seed | `{(0,0,0),(1,1,1),(2,0,0)}` | yes |
| `scripts/f_cut_c10_three_site_fill_orbit_2026_08_15.py:231` | fill predicate | halt set of cardinality 12 | yes |
| `scripts/f_cut_c10_three_site_fill_orbit_2026_08_15.py:263` | two-cube-preserving group | proper rotations about the box center that permute the 12-set | yes |
| `scripts/f_cut_c10_three_site_fill_orbit_2026_08_15.py:294` | orbit of a seed | `G`-images of an unordered triple | yes |

No evidence citation is used to claim that a physical occupancy law, a
formation rate, or a `Z^3`-wide selector has been closed.

### N5 — rhetoric and resolution audit

| Resolution | Executed? | Narrow negative supported? |
|---|---:|---|
| per element | yes: all 64 neighbor 6-tuples | each is assigned its axis-type orbit; no broader cell class is classified |
| per site | yes: the twelve two-cube vertices | each uses the same six-direction stencil with off-patch occupancy `0` |
| per mode | yes: `f10` on all 220 seeds | the score is this one map; other classes are unclaimed |
| per block | yes: `N_orb=1` of the four-element fill set | the four fills are one geometric type, not adopted |
| lattice wide | no | no `Z^3`-wide formation or Admissibility selector is asserted |

The runner prints the same five resolution statements.

### N6 — partial closure and primitive scan

The primitive registry at `docs/audit/data/axiom_premise_nodes.json` was
checked. The only dependency used is the registered `minimal_axioms` node.
Approved primitives are `scale_reference_primitive`,
`kinetic_isotropy_primitive`, and `realized_state_primitive`. None of them
supplies a Boolean occupancy map, a seed-orbit count, or an Admissibility
selector, and none is reclassified as an import or wall.

One partial-closure mechanism is displayed rather than suppressed: the
four 3-site fills of `f10` are a single geometric type under two-cube
rotations, with lex representative the `#6492` seed. That orbit type
does not make `f10` a unique maximizer and does not select it as the
physical rule. The remaining physical choice — which, if any, `F_cut`
map is the Admissibility occupancy predicate — stays explicit.

The open derivation-obligation registry
(`docs/audit/data/derivation_obligations.json`) names no occupancy-to-lock
coverage or fill-orbit target; those open gates are unused here.

### N7 — hostile steelman

The strongest objection is that `#6496` already counted four 3-site
fills of `f10`, so an orbit type of that same set might be called leftover
decoration of a known cardinality. That objection is correctly about
`|M|=4`. It does not overturn the stated theorem: the four fills are one
orbit under the order-8 two-cube-preserving rotation group, not four
independent extras. A raw count does not name `N_orb`. This is new
geometry of a counted fill set of the second exception.

### N8 — cross-cycle echo

Repository search found nearby occupancy and covariance surfaces. They are
context, not load-bearing dependencies. The 24 rotations, 10 orbits,
`F_cut`, the map `f10`, the fill set `M`, and `N_orb` are recomputed
here.

| Earlier surface | Similar issue | Mechanism considered here |
|---|---|---|
| `docs/ADMISSIBILITY_COVARIANT_Q8_CONDITIONAL_LAW_PAIR_BOUNDED_THEOREM_NOTE_2026-08-13.md` | proper-cubic covariance of a local rule | covariance is used only as the orbit filter for Boolean maps |
| `docs/PHYSICAL_SPATIAL_BLOCK_SEAM_DICHOTOMY_CYCLE728_NOTE_2026-08-04.md` | two-cell box `{0,1,2}×{0,1}×{0,1}` | the same twelve spatial vertices are the patch; the seam cost is unused |
| `docs/MINIMAL_AXIOMS_2026-06-29.md` | one covariant nearest-neighbor rule | the axiom names the contract; this note does not select the rule |

No earlier mechanism retires the orbit type of the four 3-site fills of
`f10` or writes that orbit into Admissibility.

No-Go Discipline disposition: **PASS** for the displayed `N_orb=1` of
the four 3-site fills of `f10` stated above.

## Live Parent Quotes

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

> There is one fixed nearest-neighbor admissibility rule, covariant under lattice
> translations and proper cubic rotations.

> When present, a record locks exactly one admissible local possibility. A
> site never carries more than one record; records are permanent.

> Only records are readable. A readout value is determined by record content
> alone. A site with no record cannot be read.

## Runner Contract

The companion runner reconstructs the 24 rotations and 10 orbits, rebuilds
`F_cut`, evaluates `f10=(1,1,0,0,0)` on the two-cube from every 3-site
seed, reports `|M| = 4` with the `#6492` seed in `M`, restricts to the
eight two-cube-preserving proper rotations about the box center, reports
`N_orb = 1` with that seed as the unique lex representative, checks that
`f_L1` is not Hamming parity, and exhibits `N_orb` as displayed, not
adopted. Declared audit inputs are this note and the axiom memo. No
runner cache is written.
