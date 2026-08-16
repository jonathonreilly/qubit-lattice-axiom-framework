---
claim_id: f_cut_wt1_zero_l1_first_split_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On the two-cube with off-patch o=0, the lex-first seed of size at most 3 at which f_L1 fills and F_cut (0,0,1,1,1) does not is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_wt1_zero_l1_first_split_2026_08_15.py
---

# First |S|≤3 Seed Splitting f_L1 From Its wt1=0 Sibling

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact occupancy dynamics on the twelve-vertex two-cube with
off-patch occupancy `o=0`. The lex-first seed of size at most 3 at which
`f_L1` fills and `F_cut` `(0,0,1,1,1)` does not is reported. Displayed, not
adopted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_wt1_zero_l1_first_split_2026_08_15.py`](../scripts/f_cut_wt1_zero_l1_first_split_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

On the two-cube with off-patch `o=0`, the lex-first seed of size at most 3
at which `f_L1` fills and `F_cut` `(0,0,1,1,1)` does not is the one-site
seed `S={(0,0,0)}`. Independent runs from that seed give lock histories
`(1, 4, 8, 11, 12)` for `f_L1` and the halting lock history `(1)` for the
sibling. The first split is tick 1: `f_L1` locks the three on-patch axis
neighbors `{(1,0,0), (0,1,0), (0,0,1)}` while the sibling stays at the seed.

`f_L1` is the remaining-bit tuple `(1,0,1,1,1)` in the order
`(wt1, opp2, adj2, vertex3, mixed3)`, equivalently `n≠0` (some axis
unbalanced). It is not Hamming parity. The sibling is that tuple with `wt1`
flipped to `0`. Neither the seed nor the `wt1` bit is adopted.

## Current Premise Boundary

The Lattice and Record premises are quoted from
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md):

Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
adjacency, standard translations, and proper cubic rotations about each site.

When present, a record locks exactly one admissible local possibility.

Records are permanent. The occupancy predicate used here is a separately
supplied finite map on six-neighbor cells. It is not Admissibility content
and is not written into the axiom memo.

The two-cube, the off-patch default `o=0`, the 32 complement-even `F_cut`
maps, and the lex order on seeds are explicit theorem-domain data. This note
does not claim that the axioms select `wt1`, `f_L1`, or the sibling.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact finite lock histories on the twelve-vertex two-cube identify the lex-first |S|<=3 seed at which f_L1 fills and F_cut (0,0,1,1,1) does not."
trace_class: frontier_discovery
target_claim_id: f_cut_wt1_zero_l1_first_split
target_blocker_text: "is wt1 dynamically free on the two-cube"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
conditional_surface_status: "exact on the supplied two-cube with off-patch o=0; the sibling map and the split seed are displayed and not adopted"
hypothetical_axiom_status: "none; wt1 is displayed remaining-bit data and is not proposed as axiom content"
admitted_observation_status: null
next_trace_action: "independent audit of the bounded occupancy claim"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

The two-cube is the twelve-site patch

`V = {0,1,2} × {0,1} × {0,1} ⊂ Z^3`.

Cube `A` is `x∈{0,1}`; cube `B` is `x∈{1,2}`; they share the face `x=1`.
The six-neighbor tuple at `v` is the occupancy of `v±e_1,v±e_2,v±e_3`, with
off-patch occupancy `0`. A seed `S⊂V` starts locked. Each tick every
unlocked site evaluates a supplied `{0,1}`-valued map `f` on its current
six-tuple and locks if `f=1`. Halt is the first fixed point. Fill means the
halt set is all of `V`.

The 24 proper cube rotations partition `{0,1}^6` into 10 orbits. The class
`F_cut` consists of the cube-covariant maps with `f(empty)=f(full)=0` and
`f(c)=f(1-c)`. Complement-evenness leaves five free bits on the remaining
orbit pairs, in the order `(wt1, opp2, adj2, vertex3, mixed3)`, so
`|F_cut|=32`.

`f_L1` is the map with remaining bits `(1,0,1,1,1)`. Equivalently,
`f_L1(c)=1` if and only if some axis is unbalanced (`n≠0`). Hamming parity
`|c|_1 mod 2` is a different `F_cut` map: it differs from `f_L1` on 24 of
the 64 cells. The sibling studied here is `F_cut` `(0,0,1,1,1)`, i.e. `f_L1`
with `wt1` set to `0`. The two maps are run independently.

Seeds of size at most 3 are listed by increasing size, and within each size
by lexicographic order of sorted site tuples in the coordinate order of `V`.

## Theorem 1 — Three-Site Coverages

`f_L1` fills every one of the `C(12,3)=220` three-site seeds. The all-ones
remaining-bit map `f1=(1,1,1,1,1)` also fills all 220. The sibling
`(0,0,1,1,1)` fills 24 of the 220 and therefore is not a 3-site maximizer.
In particular it is not a member of `Max(3)={f_L1,f1}`.

These are independent recomputations on the supplied patch. They do not
import a prior census as a hypothesis.

## Theorem 2 — Lex-First Split Seed

Search every seed of size at most 3 in the lex order of the previous
section. The first seed at which `f_L1` fills and `(0,0,1,1,1)` does not is

`S={(0,0,0)}`, `|S|=1`.

No smaller nonempty seed exists. Among one-site seeds this is the first in
coordinate lex order.

## Theorem 3 — Independent Histories And The First Split

From `S={(0,0,0)}` the independent lock-count histories are

- `f_L1`: `(1, 4, 8, 11, 12)`, saturating at tick 4;
- `F_cut` `(0,0,1,1,1)`: the halting lock history `(1)`.

At tick 0 both maps hold only the seed. At tick 1 the three on-patch
neighbors of the seed each see a `wt1` cell. `f_L1` has `wt1=1`, so those
three sites lock and the locked set becomes
`{(0,0,0),(1,0,0),(0,1,0),(0,0,1)}`. The sibling has `wt1=0`, so its first
wave is empty and it remains at the seed. That tick-1 disagreement is the
first split. Later L1 ticks are not needed to witness the split and are
recorded only as the completing history of the filling map.

Do not adopt wt1. The bit, the sibling map, and the seed `S` are displayed
finite data. They are not proposed as axiom content and are not written
into Admissibility.

## Negative Scope

This note does not select a preferred `F_cut` map, does not lift the
two-cube to a larger patch, and does not assert a physical formation law.
Coverage counts other than the 220-versus-24 three-site comparison and the
lex-first split are outside the target. Hamming parity is used only as a
negative control that `f_L1` is `n≠0`.

## Inputs And Import Boundary

- **Framework dependency:** the quoted Lattice and Record sentences above.
  They supply adjacency and permanence of a formed lock. They do not supply
  `f_L1` or `wt1`.
- **Explicit theorem-domain condition:** the twelve-vertex two-cube, off-patch
  occupancy `0`, simultaneous lock ticks, and the 32 `F_cut` maps.
- **External empirical or literature inputs:** none.
- **Open physical bridge:** any Admissibility identification of a remaining
  bit, and any Record-formation reading of a lock tick, remain separate
  obligations.

On the two-cube with off-patch o=0, the lex-first seed of size at most 3 at
which f_L1 fills and F_cut (0,0,1,1,1) does not is reported. Displayed, not
adopted.
