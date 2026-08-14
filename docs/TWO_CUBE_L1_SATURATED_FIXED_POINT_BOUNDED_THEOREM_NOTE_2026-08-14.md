---
claim_id: two_cube_l1_saturated_fixed_point_bounded_theorem_note_2026-08-14
claim_type: bounded_theorem
claim_scope: "On the displayed two-cube L1 patch, the full lock set is a fixed point: one further L1 step adds no locks and leaves F, rho(A), rho(B), and phi unchanged. The empty configuration is also a fixed point. That is the halt of the displayed member, not another step on a new patch."
upstream_dependencies:
  - minimal_axioms
runner: scripts/two_cube_l1_saturated_fixed_point_2026_08_14.py
---

# After Saturation L1 Is The Identity

**Date:** 2026-08-14
**Type:** bounded_theorem
**Scope:** exact fixed-point identities of the displayed L1 occupancy kernel on one twelve-site two-cube carrier.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/two_cube_l1_saturated_fixed_point_2026_08_14.py`](../scripts/two_cube_l1_saturated_fixed_point_2026_08_14.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

Start from the full lock set `locks = V`. One further `L1` step produces

```text
new locks = empty,   F unchanged,   rho(A), rho(B), phi unchanged.
```

The empty configuration is the other fixed point: with no locked neighbor,
every unread site has `n=0` and stays unread.

Those two endpoints are the halt of the displayed member.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact fixed-point identities of a reconstructed L1 kernel at the full and empty endpoints of one two-cube carrier."
trace_class: frontier_discovery
target_claim_id: two_cube_l1_saturated_fixed_point
target_blocker_text: "whether displayed L1 is the identity on the saturated two-cube and on the empty configuration"
source_of_blocker_text: handoff
reachability_to_target: unknown_frontier
artifact_role: theorem
next_trace_action: "independent audit of the bounded fixed-point claim"
conditional_surface_status: "exact on the supplied two-cube L1 patch at the two endpoints; other complexes remain separate"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

`cache_write: false`

## Inputs And Import Boundary

- **Framework dependency:** live Record permanence, quoted without rewrite.
- **Explicit theorem-domain condition:** reconstructed L1 kernel on the twelve-site patch.
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

Full lock set: `V`. Empty lock set: `empty`. One step of `L1` on each.

## Exact Target And Proof Obligations

Check that the full set and the empty set are fixed, and that evolving
five ticks from the seed agrees with four ticks.

## Theorems

### Theorem 1 — full set is a fixed point

Every site is already locked, so the unread-and-`n != 0` set is empty.

### Theorem 2 — empty set is a fixed point

Off-patch occupancy is `0`, so `n=0` everywhere and nothing forms.

### Theorem 3 — halt after saturation

`locks_5 = locks_4` when grown from the seed, so a fifth tick does not
change `F`, `rho`, or `phi`.

## What Is Not Claimed

- No uniqueness of this halt among other kernels.
- No physical stopping-time identification.

- No axiom edit and no replacement of the live Record sentences.
- Qubit remains `M_2(C)`.
- No unique member of the axiom class.
- No inverse-square law and no Newtonian identification.

## Runner Contract

The companion runner reconstructs the occupancy kernel on the displayed
patch and checks the theorems with exact `Fraction` arithmetic. It prints
`TOTAL: PASS=... FAIL=...` and writes no cache. Declared review inputs are
this note and the axiom memo only.
