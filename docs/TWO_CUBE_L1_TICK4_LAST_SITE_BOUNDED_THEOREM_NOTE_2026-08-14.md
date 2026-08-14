---
claim_id: two_cube_l1_tick4_last_site_bounded_theorem_note_2026-08-14
claim_type: bounded_theorem
claim_scope: "On the displayed two-cube L1 patch, the last unread vertex (2,1,1) stays unread through ticks 0,1,2,3 and locks at tick 4 with 3n=(-1,-1,-1) and k=3. This is the last formation event of displayed L1 on this complex."
upstream_dependencies:
  - minimal_axioms
runner: scripts/two_cube_l1_tick4_last_site_2026_08_14.py
---

# L1 Tick 4 Forms The Last Site

**Date:** 2026-08-14
**Type:** bounded_theorem
**Scope:** exact last-site formation of the displayed L1 occupancy kernel on one twelve-site two-cube carrier.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/two_cube_l1_tick4_last_site_2026_08_14.py`](../scripts/two_cube_l1_tick4_last_site_2026_08_14.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

After tick 3 the three distance-3 sites are locked. The remaining unread
vertex is `(2,1,1)`, at graph distance `4` from the seed.

**Theorem.** At the start of tick 4,

```text
(2,1,1):  3n = (-1,-1,-1),  k = 3,  forms.
```

The site is unread at `t = 0,1,2,3` and locked at `t = 4`. Tick 4 forms
exactly that one site.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact finite last-site formation time and k-value on one supplied two-cube carrier."
trace_class: frontier_discovery
target_claim_id: two_cube_l1_tick4_last_site
target_blocker_text: "whether the last two-cube vertex forms at tick 4 with k=3"
source_of_blocker_text: handoff
reachability_to_target: unknown_frontier
artifact_role: theorem
next_trace_action: "independent audit of the bounded last-site claim"
conditional_surface_status: "exact on the supplied two-cube L1 patch for tick 4; other complexes remain separate"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

`cache_write: false`

## Inputs And Import Boundary

- **Framework dependency:** live Lattice and Record sentences, quoted without rewrite.
- **Explicit theorem-domain condition:** the same reconstructed L1 kernel as the tick-3 table, continued one tick.
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

Unread through tick 3: `(2,1,1)` only. Tick 4 new locks:
`{(2,1,1)}`. Then `|locks_4|=12`.

## Exact Target And Proof Obligations

Check unreadness at `t<=3`, lock at `t=4`, singleton formation set, and
`k=3` from exact `3n`.

## Theorems

### Theorem 1 — last site waits for the distance-3 layer

`(2,1,1)` has no locked neighbor until the three distance-3 sites lock.
Hence it is unread at `t=0,1,2,3`.

### Theorem 2 — tick 4 is a singleton with `k=3`

After tick 3, `3n(2,1,1)=(-1,-1,-1)` and `k=3`. The site forms, and it is
the only unread site, so the formation set is a singleton.

## What Is Not Claimed

- No statement that every complex saturates at diameter.
- No physical clock identification.

- No axiom edit and no replacement of the live Record sentences.
- Qubit remains `M_2(C)`.
- No unique member of the axiom class.
- No inverse-square law and no Newtonian identification.

## Runner Contract

The companion runner reconstructs the occupancy kernel on the displayed
patch and checks the theorems with exact `Fraction` arithmetic. It prints
`TOTAL: PASS=... FAIL=...` and writes no cache. Declared review inputs are
this note and the axiom memo only.
