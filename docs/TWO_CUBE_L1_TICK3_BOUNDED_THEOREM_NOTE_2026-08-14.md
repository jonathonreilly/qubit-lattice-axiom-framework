---
claim_id: two_cube_l1_tick3_bounded_theorem_note_2026-08-14
claim_type: bounded_theorem
claim_scope: "On the displayed two-cube L1 patch with seed (0,0,0), after two ticks the lock set is the seed together with the graph-distance 1 and 2 layers (8 sites). Tick 3 forms exactly the three distance-3 sites (1,1,1) with k=|3n|^2=3 and (2,1,0),(2,0,1) with k=2. The distance-4 site (2,1,1) has n=0 and stays unread. This is a later tick of the displayed member, not a new patch."
upstream_dependencies:
  - minimal_axioms
runner: scripts/two_cube_l1_tick3_2026_08_14.py
---

# L1 Tick 3 Forms The Three Distance-Three Sites

**Date:** 2026-08-14
**Type:** bounded_theorem
**Scope:** exact tick-3 formation table of the displayed L1 occupancy kernel on one twelve-site two-cube carrier.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/two_cube_l1_tick3_2026_08_14.py`](../scripts/two_cube_l1_tick3_2026_08_14.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

Write two adjacent unit cubes

```text
A = {0,1} x {0,1} x {0,1},   B = {1,2} x {0,1} x {0,1}.
```

The displayed patch is `V = A union B` (twelve vertices). Occupancy off the
patch is `0`. A locked site has occupancy `1` and stays locked. An unread
site has occupancy `0`. The neighbor imbalance is

```text
n_mu(v) = (o(v+e_mu) - o(v-e_mu)) / 3,   mu in {x,y,z},
k(v) = |3n(v)|^2.
```

An unread patch site forms if and only if `n(v) != 0`. The seed is
`{(0,0,0)}`. After two ticks the lock set is the seed together with the
graph-distance `1` and `2` layers (eight sites). The unread remainder is

```text
{(1,1,1), (2,1,0), (2,0,1)}   (distance 3)
and   (2,1,1)   (distance 4).
```

**Theorem.** At the start of tick 3 the kernel table is

```text
(1,1,1):  3n = (-1,-1,-1),  k = 3,  forms
(2,1,0):  3n = (-1,-1, 0),  k = 2,  forms
(2,0,1):  3n = (-1, 0,-1),  k = 2,  forms
(2,1,1):  n  = (0,0,0),     stays unread.
```

Tick 3 therefore locks exactly the three distance-3 sites.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact finite k-table and formation set on one supplied two-cube carrier at tick 3 of a reconstructed L1 kernel."
trace_class: frontier_discovery
target_claim_id: two_cube_l1_tick3
target_blocker_text: "whether tick 3 of displayed L1 locks the three distance-3 sites with the stated k table"
source_of_blocker_text: handoff
reachability_to_target: unknown_frontier
artifact_role: theorem
next_trace_action: "independent audit of the bounded tick-3 table"
conditional_surface_status: "exact on the supplied two-cube L1 patch for tick 3; later ticks and other complexes remain separate"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

`cache_write: false`

## Inputs And Import Boundary

- **Framework dependency:** the live Lattice and Record sentences quoted
  below supply the cubic site set, lock permanence, and unreadability of
  absence. They are quoted without rewrite.
- **Explicit theorem-domain condition:** the twelve-site two-cube patch, the
  seed, the occupancy kernel `n_mu = (o_{+mu}-o_{-mu})/3`, and the integer
  `k = |3n|^2` are supplied mathematical data for this note.
- **External empirical or literature inputs:** none.

## Live Parent Quotes

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

> Records form.

> When present, a record locks exactly one admissible local possibility. A
> site never carries more than one record; records are permanent.

> Only records are readable. A readout value is determined by record content
> alone.

Their dependency role is limited to the cubic site set, lock permanence, and
the unreadability of absence. The occupancy kernel, the two-cube patch, and
the tick index are separately supplied.

## Exact Objects

All runner values are exact integers or rationals in `Q`. No float is used.

After tick 2 the eight locked sites are

```text
(0,0,0), (1,0,0), (0,1,0), (0,0,1), (1,1,0), (1,0,1), (0,1,1), (2,0,0).
```

Tick 3 new locks: `(1,1,1)`, `(2,1,0)`, `(2,0,1)`. Then `|locks_3|=11`
and `(2,1,1)` remains unread.

## Exact Target And Proof Obligations

The exact target is the tick-3 formation set together with the four
`k`-values. The runner reconstructs `L1` locally, evaluates `n` and
`k` on the four unread sites after tick 2, and checks the formation set.

## Theorems

### Theorem 1 — three distance-3 sites form

The unread sites with `n != 0` after tick 2 are exactly
`{(1,1,1),(2,1,0),(2,0,1)}`. Those three lock. The site `(2,1,1)` has
`n=0` and stays unread.

### Theorem 2 — exact integer `k` table

`k = |3n|^2` is an integer. The four unread sites give `k=3,2,2,0`
respectively. No float is used.

## What Is Not Claimed

- No fourth tick, no saturation statement, and no full `Z^3` history.
- No identification of `k` with a physical spin or a spectral measure.

- No axiom edit and no replacement of the live Record sentences.
- Qubit remains `M_2(C)`.
- No unique member of the axiom class.
- No inverse-square law and no Newtonian identification.

## Runner Contract

The companion runner reconstructs the occupancy kernel on the displayed
patch and checks the theorems with exact `Fraction` arithmetic. It prints
`TOTAL: PASS=... FAIL=...` and writes no cache. Declared review inputs are
this note and the axiom memo only.
