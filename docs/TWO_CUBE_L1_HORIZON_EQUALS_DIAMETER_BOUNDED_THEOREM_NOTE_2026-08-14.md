---
claim_id: two_cube_l1_horizon_equals_diameter_bounded_theorem_note_2026-08-14
claim_type: bounded_theorem
claim_scope: "On the displayed two-cube L1 patch with seed (0,0,0), the l1 diameter is 4, attained at (2,1,1). After tick 3 the lock set has 11 sites and is not full. After tick 4 it has 12 sites and is full. The first saturating tick therefore equals the diameter."
upstream_dependencies:
  - minimal_axioms
runner: scripts/two_cube_l1_horizon_equals_diameter_2026_08_14.py
---

# L1 Horizon Equals The Patch Diameter

**Date:** 2026-08-14
**Type:** bounded_theorem
**Scope:** exact comparison of first saturation tick with the l1 diameter of one twelve-site two-cube carrier.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/two_cube_l1_horizon_equals_diameter_2026_08_14.py`](../scripts/two_cube_l1_horizon_equals_diameter_2026_08_14.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

The seed is `(0,0,0)`. Graph distance on the patch is ordinary `l1`
distance restricted to `V`. The farthest vertex is `(2,1,1)`:

```text
diam = max_{v in V} d(v, seed) = 4.
```

**Theorem.** After tick 3, `|locks|=11 < 12`. After tick 4, `|locks|=12`.
The first saturating tick equals the diameter. The causal front therefore
travels at speed `1` through the whole displayed complex.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact finite comparison of first saturation tick with the l1 diameter on one supplied two-cube carrier."
trace_class: frontier_discovery
target_claim_id: two_cube_l1_horizon_equals_diameter
target_blocker_text: "whether the first saturating L1 tick equals the patch diameter"
source_of_blocker_text: handoff
reachability_to_target: unknown_frontier
artifact_role: theorem
next_trace_action: "independent audit of the bounded horizon claim"
conditional_surface_status: "exact on the supplied two-cube L1 patch from the origin seed; other seeds and complexes remain separate"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

`cache_write: false`

## Inputs And Import Boundary

- **Framework dependency:** live Lattice adjacency, quoted without rewrite.
- **Explicit theorem-domain condition:** reconstructed L1 kernel and the l1 metric on the twelve-site patch.
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

`d((2,1,1),(0,0,0))=4`. `|locks_3|=11`, `|locks_4|=12`.

## Exact Target And Proof Obligations

Compute the diameter, check non-saturation at tick 3, and saturation at
tick 4.

## Theorems

### Theorem 1 — diameter is four

Every vertex `v` satisfies `d(v,seed) <= 4`, and equality holds at
`(2,1,1)`.

### Theorem 2 — first saturation tick equals the diameter

Tick 3 leaves `(2,1,1)` unread, so the patch is not full. Tick 4 fills
it. The first saturating tick is `4`, equal to the diameter.

## What Is Not Claimed

- No continuum light cone.
- No statement for a different seed.

- No axiom edit and no replacement of the live Record sentences.
- Qubit remains `M_2(C)`.
- No unique member of the axiom class.
- No inverse-square law and no Newtonian identification.

## Runner Contract

The companion runner reconstructs the occupancy kernel on the displayed
patch and checks the theorems with exact `Fraction` arithmetic. It prints
`TOTAL: PASS=... FAIL=...` and writes no cache. Declared review inputs are
this note and the axiom memo only.
