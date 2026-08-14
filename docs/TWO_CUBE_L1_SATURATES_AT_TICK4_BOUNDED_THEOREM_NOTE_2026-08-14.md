---
claim_id: two_cube_l1_saturates_at_tick4_bounded_theorem_note_2026-08-14
claim_type: bounded_theorem
claim_scope: "On the displayed two-cube L1 patch, after tick 4 every one of the 12 vertices is locked. Then rho(A)=8, rho(B)=8, F=11, tree-gauge phi(F*)=8 and phi(F_B)=16. This is a finite horizon of the displayed member, not a 4x4x4 occupancy step."
upstream_dependencies:
  - minimal_axioms
runner: scripts/two_cube_l1_saturates_at_tick4_2026_08_14.py
---

# L1 Saturates The Two-Cube At Tick 4

**Date:** 2026-08-14
**Type:** bounded_theorem
**Scope:** exact saturation census of the displayed L1 occupancy kernel on one twelve-site two-cube carrier.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/two_cube_l1_saturates_at_tick4_2026_08_14.py`](../scripts/two_cube_l1_saturates_at_tick4_2026_08_14.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

The patch has twelve vertices. After tick 4 the lock set equals the
patch.

```text
|locks_4| = 12,   F = 11,   rho(A) = 8,   rho(B) = 8.
```

Shared-face vertices are occupied and counted in both cubes. The
tree-gauge assignment of the two-face decoder is then

```text
phi(F*) = rho(A) = 8,   phi(F_B) = rho(A)+rho(B) = 16.
```

This is a finite horizon on the displayed complex.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact finite saturation census and tree-gauge integers on one supplied two-cube carrier after four L1 ticks."
trace_class: frontier_discovery
target_claim_id: two_cube_l1_saturates_at_tick4
target_blocker_text: "whether displayed L1 saturates the twelve-site two-cube at tick 4"
source_of_blocker_text: handoff
reachability_to_target: unknown_frontier
artifact_role: theorem
next_trace_action: "independent audit of the bounded saturation census"
conditional_surface_status: "exact on the supplied two-cube L1 patch at tick 4; other complexes remain separate"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

`cache_write: false`

## Inputs And Import Boundary

- **Framework dependency:** live Lattice and Record sentences, quoted without rewrite.
- **Explicit theorem-domain condition:** reconstructed L1 kernel, two-cube patch, formation count `F = |locks|-1`, and two-face tree gauge.
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

Twelve patch vertices. After tick 4: `|locks|=12`, `F=11`,
`rho(A)=rho(B)=8`, `phi(F*)=8`, `phi(F_B)=16`.

## Exact Target And Proof Obligations

Check the lock set equals the patch, the two cube occupancies, the
formation count, and the tree-gauge integers.

## Theorems

### Theorem 1 — every vertex is locked

`locks_4 = V`, so `|locks_4|=12`.

### Theorem 2 — census and tree gauge

`F = 12-1 = 11`. Both cubes are full, so `rho(A)=rho(B)=8`. The tree
gauge `phi(F*)=rho(A)`, `phi(F_B)=rho(A)+rho(B)` returns `(8,16)`.

## What Is Not Claimed

- No 4x4x4, torus, or line complex.
- No claim that every finite patch saturates at its diameter.

- No axiom edit and no replacement of the live Record sentences.
- Qubit remains `M_2(C)`.
- No unique member of the axiom class.
- No inverse-square law and no Newtonian identification.

## Runner Contract

The companion runner reconstructs the occupancy kernel on the displayed
patch and checks the theorems with exact `Fraction` arithmetic. It prints
`TOTAL: PASS=... FAIL=...` and writes no cache. Declared review inputs are
this note and the axiom memo only.
