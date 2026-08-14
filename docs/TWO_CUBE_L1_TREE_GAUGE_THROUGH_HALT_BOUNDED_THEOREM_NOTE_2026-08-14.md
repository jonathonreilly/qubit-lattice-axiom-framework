---
claim_id: two_cube_l1_tree_gauge_through_halt_bounded_theorem_note_2026-08-14
claim_type: bounded_theorem
claim_scope: "On the displayed two-face tree, the assignment phi(F*)=rho(A), phi(F_B)=rho(A)+rho(B) solves g=rho after ticks 3 and 4. After tick 3 the source is (8,7). After tick 4 it is (8,8). Static uniqueness of the two-face decoder is not restated; this is the update identity through halt."
upstream_dependencies:
  - minimal_axioms
runner: scripts/two_cube_l1_tree_gauge_through_halt_2026_08_14.py
---

# Tree Gauge Holds Through Saturation

**Date:** 2026-08-14
**Type:** bounded_theorem
**Scope:** exact two-face tree-gauge identities after ticks 3 and 4 of the displayed L1 occupancy kernel on one twelve-site two-cube carrier.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/two_cube_l1_tree_gauge_through_halt_2026_08_14.py`](../scripts/two_cube_l1_tree_gauge_through_halt_2026_08_14.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

The displayed two-face incidence is

```text
g_A := phi(F*),   g_B := -phi(F*) + phi(F_B).
```

The tree-gauge assignment is

```text
phi(F*) = rho(A),   phi(F_B) = rho(A) + rho(B).
```

**Theorem.** After tick 3 the occupancy source is `(rho(A), rho(B)) = (8,7)`
(B misses only `(2,1,1)`). After tick 4 it is `(8,8)`. In both cases
`g = rho`. This is the update identity at the halt, not a restatement of
static uniqueness.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact integer tree-gauge identities after ticks 3 and 4 of a reconstructed L1 kernel on one two-cube carrier."
trace_class: frontier_discovery
target_claim_id: two_cube_l1_tree_gauge_through_halt
target_blocker_text: "whether g=rho still holds after L1 ticks 3 and 4"
source_of_blocker_text: handoff
reachability_to_target: unknown_frontier
artifact_role: theorem
next_trace_action: "independent audit of the bounded halt tree-gauge claim"
conditional_surface_status: "exact on the supplied two-face tree and ticks 3 and 4; other complexes remain separate"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

`cache_write: false`

## Inputs And Import Boundary

- **Framework dependency:** none of the four axioms supplies a face incidence or a Gauss decoder.
- **Explicit theorem-domain condition:** two-face tree, reconstructed L1 source ticks, and the displayed decoder.
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

Tick 3: `rho=(8,7)`, `phi=(8,15)`, `g=(8,7)`.
Tick 4: `rho=(8,8)`, `phi=(8,16)`, `g=(8,8)`.

## Exact Target And Proof Obligations

Compute `rho` after ticks 3 and 4, apply the tree gauge, and check
`g=rho`.

## Theorems

### Theorem 1 — source values at the remaining ticks

After tick 3 cube A is full and cube B misses `(2,1,1)`, so `(8,7)`.
After tick 4 both cubes are full, so `(8,8)`.

### Theorem 2 — tree gauge still solves `g=rho`

Substituting `phi(F*)=rho(A)` and `phi(F_B)=rho(A)+rho(B)` into the
incidence returns `g=rho` at both ticks.

## What Is Not Claimed

- No third face and no minus-x ray.
- No static uniqueness restatement of the two-face decoder.

- No axiom edit and no replacement of the live Record sentences.
- Qubit remains `M_2(C)`.
- No unique member of the axiom class.
- No inverse-square law and no Newtonian identification.

## Runner Contract

The companion runner reconstructs the occupancy kernel on the displayed
patch and checks the theorems with exact `Fraction` arithmetic. It prints
`TOTAL: PASS=... FAIL=...` and writes no cache. Declared review inputs are
this note and the axiom memo only.
