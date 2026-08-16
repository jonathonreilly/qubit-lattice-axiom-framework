---
claim_id: f_cut_c10_6492_seed_first_refuse_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On the two-cube with off-patch o=0, the first refused neighborhood of F_cut (1,1,0,0,0) on the #6492 seed {(0,0,0),(1,1,1),(2,0,0)} is reported, or the run refuses none. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_c10_6492_seed_first_refuse_2026_08_15.py
---

# First Refused Neighborhood Of F_cut (1,1,0,0,0) On The #6492 Seed

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact occupancy-to-lock dynamics on the displayed twelve-vertex
two-cube with off-patch occupancy 0. The F_cut map with remaining-bit
tuple `(1,1,0,0,0)` is run from the #6492 seed
`S = {(0,0,0),(1,1,1),(2,0,0)}`. The first remaining-bit neighborhood
that map refuses on that run is reported, or the run refuses none.
Displayed, not adopted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_c10_6492_seed_first_refuse_2026_08_15.py`](../scripts/f_cut_c10_6492_seed_first_refuse_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

Write the two-cube as the lex-ordered twelve-site patch
`{0,1,2} × {0,1} × {0,1}` of `Z^3`. Off-patch neighbors have occupancy 0.
A cube-covariant complement-even predicate that vanishes on the empty and
full six-neighbor cells is an F_cut map, coded by the five remaining bits
`(wt1, opp2, adj2, vertex3, mixed3)`.

The displayed map is

```text
f10 = (1,1,0,0,0).
```

From the #6492 seed

```text
S = {(0,0,0), (1,1,1), (2,0,0)}
```

the lock history is `(3, 12)` and `locks_halt=12`, so `f10` fills. The
remaining-bit orbits that appear as neighborhoods of unlocked sites on
that run are `wt1` and `opp2`. Both have remaining bit 1, so both are
accepted. No unlocked site sees a remaining-bit orbit that `f10` sends to
0. Therefore

```text
N_refuse = 0.
```

Every remaining-bit orbit that appears is accepted. The empty refuse list
is displayed. Do not adopt a bit.

The predicate `f_L1` used only as vocabulary is `n ≠ 0` (some axis
unbalanced). It is not Hamming parity.

New finite object. Not leftover-character of #6492: that leftover names
the fill bits of the pair `(1,0,0,0,0)` versus `(1,1,0,0,0)` on this same
seed. This residual is the first refused neighborhood of `f10` on the
filling run, not a second copy of the fill bit.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact two-cube occupancy ticks locate the first remaining-bit neighborhood that F_cut (1,1,0,0,0) refuses on the #6492 seed, or report N_refuse=0."
trace_class: frontier_discovery
target_claim_id: f_cut_c10_6492_seed_first_refuse
target_blocker_text: "first refused neighborhood of f10 on the #6492 filling run"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
conditional_surface_status: "exact on the supplied two-cube with off-patch o=0; no remaining bit is adopted"
hypothetical_axiom_status: "not proposed; no axiom or approved primitive is added"
admitted_observation_status: null
next_trace_action: "independent audit of the bounded algebraic claim"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Inputs And Import Boundary

- **Framework dependency:** the live Lattice, Admissibility, and Record
  sentences below supply the repository's site, nearest-neighbor, and lock
  vocabulary. They are quoted without rewrite.
- **Explicit theorem-domain condition:** the twelve-vertex two-cube, off-patch
  occupancy 0, the six-neighbor occupancy cell, the F_cut remaining-bit
  coding, the simultaneous lock tick, and the displayed seed are supplied
  mathematical data for this theorem. The axioms do not by themselves name
  this finite patch, the F_cut subclass, or the seed.
- **External empirical or literature inputs:** none.
- **Open physical bridge:** selection of a remaining bit by Record or
  Admissibility, and any physical reading of `wt1` or `opp2`, remain
  separate open obligations outside the target proved here.

## Exact Objects

Sites are the lex-ordered tuples

```text
(0,0,0), (0,0,1), (0,1,0), (0,1,1),
(1,0,0), (1,0,1), (1,1,0), (1,1,1),
(2,0,0), (2,0,1), (2,1,0), (2,1,1).
```

The six-neighbor cell of a site `v` relative to a lock set `L` is the
`{0,1}^6` occupancy of `v ± e_i`, with any off-patch neighbor scored 0.
The blank-block is a different rule and is not used. A tick locks every
unlocked site whose cell is sent to 1 by the predicate, all at once, and
halts at a fixed point. Fill means the halt lock set is the whole
twelve-site patch, equivalently `|locks_halt|=12`. The lock-history of a
run is the tuple of lock-set cardinalities, beginning with `|S|`.

The 24 proper cube rotations partition `{0,1}^6` into 10 orbits. The class
`F_cut` consists of the cube-covariant maps with `f(empty)=f(full)=0` and
`f(c)=f(1-c)`. Complement-evenness leaves five free bits on the remaining
orbit pairs, in the order `(wt1, opp2, adj2, vertex3, mixed3)`, so
`|F_cut|=32`.

`f_L1` is the map with remaining bits `(1,0,1,1,1)`. Equivalently,
`f_L1(c)=1` if and only if some axis is unbalanced (`n_μ = c_{+μ} − c_{-μ}`
is nonzero). This is **not** Hamming parity `|c|_1 mod 2`, which is the
different remaining-bit tuple `(1,0,0,1,1)`.

A remaining-bit neighborhood on a run is a six-neighbor cell of an
unlocked on-patch site whose orbit is one of the five remaining pairs
(or its complement). The map refuses that neighborhood when the
corresponding remaining bit is 0. `N_refuse` is the number of such
refused events on the run, scanned in lock-history order and, within a
tick, lex site order. If that list is empty, `N_refuse=0` and every
remaining-bit orbit that appears is accepted.

All runner quantities are exact integers. No float is used.

## Exact Target And Proof Obligations

The exact target is to reconfirm that `f10` fills from `S` with history
`(3, 12)` or the exact `locks_halt=12` run, and to name the lex-first
remaining-bit neighborhood that `f10` refuses on that run, or else to
report `N_refuse=0`.

The obligation graph is:

1. recompute the lock history of `f10` from `S` and confirm fill;
2. list every remaining-bit neighborhood of an unlocked site on that run
   and report the lex-first refused one, or `N_refuse=0`;
3. display the accepted appearing orbits without adopting a bit.

All three obligations are closed below and in the runner. Other seeds,
other remaining-bit maps, and any adoption of `wt1` or `opp2` are outside
this theorem. There is no missing lemma for the bounded target.

## Theorem 1 — `f10` fills from `S`

Recomputing occupancy-to-lock from

```text
S = {(0,0,0), (1,1,1), (2,0,0)}
```

with `f10=(1,1,0,0,0)` and off-patch occupancy `0` gives

```text
history = (3, 12),    locks_halt = 12,    fill = true.
```

The first wave locks all nine remaining sites in one tick. This is an
independent recomputation on the supplied patch. It is not imported as a
hypothesis.

## Theorem 2 — first refused neighborhood, or `N_refuse=0`

At tick 0 the nine unlocked sites and their six-neighbor cells are

```text
(0,0,1) : (0,0,0,0,0,1)  wt1=(1,0,2)     f10=1
(0,1,0) : (0,0,0,1,0,0)  wt1=(1,0,2)     f10=1
(0,1,1) : (1,0,0,0,0,0)  wt1=(1,0,2)     f10=1
(1,0,0) : (1,1,0,0,0,0)  opp2=(0,1,2)    f10=1
(1,0,1) : (0,0,1,0,0,0)  wt1=(1,0,2)     f10=1
(1,1,0) : (0,0,0,0,1,0)  wt1=(1,0,2)     f10=1
(2,0,1) : (0,0,0,0,0,1)  wt1=(1,0,2)     f10=1
(2,1,0) : (0,0,0,1,0,0)  wt1=(1,0,2)     f10=1
(2,1,1) : (0,1,0,0,0,0)  wt1=(1,0,2)     f10=1
```

The remaining-bit orbits that appear are `wt1` and `opp2`. Both remaining
bits of `f10` on those orbits are 1. The refuse list is empty, so

```text
N_refuse = 0.
```

After the first wave the lock set is the whole two-cube, so no later tick
presents an unlocked remaining-bit neighborhood. The abstract remaining
bits that `f10` sends to 0 (`adj2`, `vertex3`, `mixed3`) do not appear as
unlocked neighborhoods on this run.

## Theorem 3 — display, do not adopt a bit

The accepted appearing orbits `wt1` and `opp2` are displayed predicate
data of this one filling run. Do not adopt a bit. Do not write `wt1` or
`opp2` into Admissibility. The exhibition is not an adoption of either
remaining bit, and no Admissibility sentence is rewritten.

## Physical-Interpretation Boundary

The proved output is the fill of `f10` from `S` and the empty refuse
list `N_refuse=0`. This note neither installs a remaining bit as a
selected law nor changes the live Admissibility or Record sentences.
Remaining-bit tuples are displayed predicate data, not axiom content, and
no additional axiom is proposed.

## Mutation Checks

Three non-equivalences guard the load-bearing conclusions:

1. Hamming parity is not `f_L1` and is not `f10`;
2. the opp2-silent sibling `(1,0,0,0,0)` run from the same seed has a
   nonempty refuse list whose lex-first event is the `opp2` cell at
   `(1,0,0)`, so `N_refuse=0` is map-dependent;
3. the claim that `f10` refuses `opp2` on this run is false.

## What This Does Not Claim

- The two-cube is not claimed to be a physically derived finite world.
- No remaining bit is adopted, and `f10` is not selected as a physical law.
- No claim is made that Record locks on `wt1` or `opp2` cells, or that
  Admissibility prefers the displayed map.
- `N_refuse=0` on this filling run is not a claim that `f10` accepts every
  remaining-bit orbit in the abstract: it refuses `adj2`, `vertex3`, and
  `mixed3`, none of which appear here.
- Other seeds and other remaining-bit maps are not classified.
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
F_cut coding, and the displayed seed; physical interpretation of remaining
bits remains outside its target.

Admissibility is not a dynamics axiom. The live reading note that
Admissibility does not supply the formation site, probability, or rate is
quoted as a boundary, not as a dynamics replacement.

On the two-cube with off-patch o=0, the first refused neighborhood of F_cut
(1,1,0,0,0) on the #6492 seed {(0,0,0),(1,1,1),(2,0,0)} is reported, or
the run refuses none. Displayed, not adopted.

## Runner Contract

The companion runner checks Theorems 1–3 with exact integer occupancy
ticks. It recomputes the `f10` history from `S`, lists every remaining-bit
neighborhood on that run, and rejects the three mutations. It quotes the
live axiom sentences and records the import boundary. Declared review
inputs are this note and the axiom memo only.
