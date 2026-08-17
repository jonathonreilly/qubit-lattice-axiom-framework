---
claim_id: unequal_radius_one_bit_tick_stab_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On the lex-first unequal-radius breaker, whether the single comparison t(−z)<t(+z) shrinks Stab is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/unequal_radius_one_bit_tick_stab_2026_08_15.py
---

# One Opposite-Pair Tick Bit Versus Occupancy Stab (Bounded Theorem)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** the uneqrad lex-first unequal-radius breaker
`U = B_2((−2,−2,−2)) ∪ B_1((−2,−2,−1)) ∪ B_3((−2,−2,1))` at
`v = (−3,−3,−1)`. Occupancy `σ` is the 6-NN indicator. The lock-tick
field is `t(w) = min_i ‖w − s_i‖_1` on occupied neighbors. The scored
datum is the single opposite-pair bit `b = [t(−z) < t(+z)]`. Score this
star only. Displayed, not adopted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/unequal_radius_one_bit_tick_stab_2026_08_15.py`](../scripts/unequal_radius_one_bit_tick_stab_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md).

## Result Up Front

Investment uneqord: the full older/newer order shrinks `Stab` to 1. That
extra is the full pairwise order. The residual here is not leftover of
uneqord (full order). New residual: the occupancy swapper only reverses
`−z ≺ +z`. Does the single bit `b = [t(−z) < t(+z)]` already give
`|Stab(σ,b)| = 1` and `N_bit_ok = 4`?

`U, v, σ, t` are the uneqrad lex-first breaker.

**Theorem 1.** `b = 1`. `|Stab(σ)| = 2`, `|Stab(σ,b)| = 1`. The
occupancy swapper is excluded.

**Theorem 2.** `N_bit_ok = 4`. The four July-3 pair members with this
support are all `Stab(σ,b)`-invariant because `|Stab(σ,b)| = 1`, so
`N_bit_ok = N_ord_ok = 4`.

**Theorem 3.** Displayed, not adopted. Do not write b into Admissibility. Do not attach L1. Qubit remains `M_2(C)`. No axiom edit.

## Current Premise Boundary

The Lattice, Admissibility, Record, and Qubit sentences used here are quoted
from [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md):

Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
adjacency, standard translations, and proper cubic rotations about each site.

There is one fixed nearest-neighbor admissibility rule, covariant under lattice
translations and proper cubic rotations.

For each site, the probability distribution over the possibilities is
determined by, and varies with, the nearest-neighbor conditions.

it does not supply the formation site, probability,
or rate.

The full one-site possibility domain has algebraic presentation `M_2(C)`.

When present, a record locks exactly one admissible local possibility.

A site never carries more than one record; records are permanent.

A readout value is determined by record content alone.

A site with no record cannot be read.

Admissibility names neither `Stab(σ,b)` nor the opposite-pair bit
`b = [t(−z) < t(+z)]`, nor the full pairwise order, as the framework's
fixed rule. The covariance clause is the reason a local labeling on the
orbit of `(σ, b)` must be stabilizer-invariant. Formation site and rate
remain outside the axiom memo. Qubit remains `M_2(C)`. No axiom edit.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Finite exact comparison on the uneqrad lex-first star: the opposite-pair bit b, |Stab(σ)|, |Stab(σ,b)|, swapper exclusion, and N_bit_ok versus N_ord_ok=4 are exact. Displayed counts only."
trace_class: frontier_discovery
target_claim_id: unequal_radius_one_bit_tick_stab
target_blocker_text: "on the lex-first unequal-radius breaker, whether the single comparison t(−z)<t(+z) shrinks Stab"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of b, |Stab(σ)|, |Stab(σ,b)|, swapper exclusion, and N_bit_ok; do not write b into Admissibility or attach L1"
conditional_surface_status: "exact on the uneqrad lex-first star; b=1; |Stab(σ)|=2; |Stab(σ,b)|=1; occupancy swapper excluded; N_bit_ok=4; displayed, not adopted"
hypothetical_axiom_status: "not proposed; no axiom or approved primitive is added"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

Write `B_r(c) = { x ∈ Z^3 : ‖x − c‖_1 ≤ r }`. The uneqrad lex-first
breaker is

`U = B_2((−2,−2,−2)) ∪ B_1((−2,−2,−1)) ∪ B_3((−2,−2,1))`,
radii `(2, 1, 3)`,
`v = (−3,−3,−1)`.

Occupancy `σ` is the 6-bit nearest-neighbor indicator of `U` at `v`, in
slot order

`(+x, −x, +y, −y, +z, −z)`.

On an occupied neighbor `w`,

`t(w) = min_i ‖w − s_i‖_1`.

Empty slots have no tick. Direct distances give `v ∉ U`,

`σ = (1, 0, 1, 0, 1, 1)`,
`t = (1, ·, 1, ·, 3, 2)`.

`G+` is the 24 proper cube rotations acting on the six slots.

`Stab(σ) = { g in G+ : g · σ = σ }`,

`b = 1` if `t(−z) < t(+z)`, else `0`.

`Stab(σ,b) = { g in G+ : g · σ = σ and b(g · t) = b(t) }`.

This keeps only the opposite-pair comparison `t(−z) < t(+z)`. It drops
the remaining older/newer pairs and the integer distances. Score the
uneqrad star only.

## Theorem 1 — report `b`, the two stabilizer orders, and the swapper

Occupied neighbors and ticks:

- `+x = (−2,−3,−1)` has `t = 1`,
- `+y = (−3,−2,−1)` has `t = 1`,
- `+z = (−3,−3,0)` has `t = 3`,
- `−z = (−3,−3,−2)` has `t = 2`.

Hence `t(−z) = 2 < 3 = t(+z)`, so `b = 1`.

The occupancy stabilizer is `{id, s}` with

`s : (x, y, z) ↦ (y, x, −z)`,

which swaps `+x ↔ +y` and `+z ↔ −z`. That map preserves `σ`. It sends
`t(+z) = 3` to `t(−z) = 2` and `t(−z) = 2` to `t(+z) = 3`, so the image
field has `t'(−z) = 3 > 2 = t'(+z)` and `b(s · t) = 0 ≠ b(t)`. The
occupancy swapper only reverses `−z ≺ +z`; the single bit already
detects that reversal. Therefore the occupancy swapper is excluded, and

`|Stab(σ)| = 2`, `|Stab(σ,b)| = 1`.

The single opposite-pair comparison, without the full order, already
shrinks occupancy `Stab` on this star.

## Theorem 2 — `N_bit_ok` versus `N_ord_ok = 4`

July-3 pair members are the 6-slot 3-letter colorings whose `G+` orbit
is sent to a different orbit by spatial inversion. Restricting to
support `σ` gives four members

`(1, 0, 2, 0, 1, 2)`, `(1, 0, 2, 0, 2, 1)`,
`(2, 0, 1, 0, 1, 2)`, `(2, 0, 1, 0, 2, 1)`,

so `N_pair_support = 4`. Because `|Stab(σ,b)| = 1`, every such member is
invariant under `Stab(σ,b)`. Hence

`N_bit_ok = 4`.

On this star `N_ord_ok = 4` for the same four members under
`Stab(σ,≺)`. The thinner extra still leaves `N_bit_ok = N_ord_ok = 4`.

## Theorem 3 — displayed, not adopted

The displayed bit, the two stabilizer orders, swapper exclusion,
`N_bit_ok = 4`, and `N_ord_ok = 4` are displayed member data. They are
not the framework's fixed Admissibility rule. This note does not write
b into Admissibility. Do not write b into Admissibility. Do not attach
L1. Occupancy-only formation is not attached. Qubit remains `M_2(C)`.
No approved primitive is added. No axiom edit.

## Honest-auditor / Boundary

- **What is proved.** On the uneqrad lex-first unequal-radius breaker,
  `b = 1`. `|Stab(σ)| = 2`, `|Stab(σ,b)| = 1`. The occupancy swapper is
  excluded. `N_bit_ok = 4`, equal to `N_ord_ok = 4`.
- **What is displayed only.** The opposite-pair bit and the two
  stabilizers are one rival table. They are not adopted.
- **What is not claimed.** No attachment of `b`, radii, integer `t`, or
  the full order to Admissibility; no attachment of occupancy-only
  formation; no axiom edit; no formation rate; no lattice-wide
  dynamics; no leftover of uneqord (full order); no compiler no-go.
- **Mutation controls.** A rebuilt `b ≠ 1` fails. A rebuilt
  `|Stab(σ)| ≠ 2` or `|Stab(σ,b)| ≠ 1` fails. A rebuilt occupancy
  swapper that preserves `b` fails. A rebuilt `N_bit_ok ≠ 4` fails. A
  note that writes b into Admissibility, attaches L1, or authors an
  audit verdict fails.

This note authors no audit verdict.

## Primary Runner

The primary runner rebuilds the uneqrad lex-first host, the occupancy,
the integer ticks, the opposite-pair bit, the 24 proper cube rotations,
`Stab(σ)`, `Stab(σ,b)`, occupancy-swapper exclusion, `N_bit_ok` against
`N_ord_ok = 4`, the current premise boundary, and the mutation
controls. It scores the uneqrad star only. It writes no cache and
authors no audit verdict.
