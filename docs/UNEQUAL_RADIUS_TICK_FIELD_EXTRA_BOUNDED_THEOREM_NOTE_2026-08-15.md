---
claim_id: unequal_radius_tick_field_extra_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Whether the unequal-radius lock-tick field is determined by 6-NN occupancy, or is an extra, is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/unequal_radius_tick_field_extra_2026_08_15.py
---

# Unequal-Radius Tick Field Is An Extra Relative To NN Occupancy (Bounded Theorem)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** the uneqrad lex-first unequal-radius breaker
`U_uneq = B_2((−2,−2,−2)) ∪ B_1((−2,−2,−1)) ∪ B_3((−2,−2,1))` at
`v = (−3,−3,−1)`, scored against one equal-radius control. Occupancy
`σ` is the 6-NN indicator. The lock-tick field is
`t(w) = min_i ‖w − s_i‖_1` on occupied neighbors. Displayed, not adopted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/unequal_radius_tick_field_extra_2026_08_15.py`](../scripts/unequal_radius_tick_field_extra_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md).

## Result Up Front

Investment uneqlaw reports `N_commute = 24` on the `G+` orbit of this
host. Investment uneqrun reports `N_fire = 4`: a `G+`-equivariant
tick-ok pair fires. Those are orbit-count and fire-count residuals. The
residual here is not leftover of uneqlaw (orbit count). New residual:
`t` is not a function of occupancy `σ`. ticklip: equal `r` gives
constant `t = r` on occupied neighbors. uneqrad: mixed `t`.

`U_uneq` and `v` are the uneqrad lex-first breaker (mixed `t`). The
same-center equal-radius union
`B_2(s1) ∪ B_2(s2) ∪ B_2(s3)` occupies this `v`, so the equal-radius
control is the displayed equal-`r` star of ticklab.

**Theorem 1.** `σ(U_uneq, v)` does not determine `t(U_uneq, v)`. The
lex-first uneqrad weight-4 star has the same `σ` and a different `t`.
The equal-radius control has constant occupied ticks.

**Theorem 2.** The tick field (or the three radii) is a newly named
extra relative to NN occupancy. Admissibility still requires an
NN-determined `μ`. Do not adopt the extra.

**Theorem 3.** Displayed, not adopted. Do not write radii or t into Admissibility. Do not write radii into Admissibility. Do not attach L1.
Qubit remains `M_2(C)`. No axiom edit.

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

Admissibility names neither the lock-tick field `t` nor any
unequal-radius 3-ball union, nor any three radii, as the framework's
fixed rule. The nearest-neighbor clause is the reason a local law `μ`
must be determined by the six-neighbor conditions. Formation site and
rate remain outside the axiom memo. Qubit remains `M_2(C)`. No axiom
edit.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Finite exact comparison of occupancy σ versus lock-tick field t on the uneqrad lex-first breaker, the lex-first same-σ uneqrad star, and one equal-radius control: σ does not determine t, so the tick field (or the three radii) is a displayed extra. Displayed only."
trace_class: frontier_discovery
target_claim_id: unequal_radius_tick_field_extra
target_blocker_text: "whether the unequal-radius lock-tick field is determined by 6-NN occupancy, or is an extra"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the same-σ different-t pair and the equal-radius control; do not write radii or t into Admissibility or attach L1"
conditional_surface_status: "exact on the scored breaker, the lex-first same-σ star, and the ticklab equal-radius control; t is not a function of σ; extra displayed, not adopted"
hypothetical_axiom_status: "not proposed; no axiom or approved primitive is added"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

Write `B_r(c) = { x ∈ Z^3 : ‖x − c‖_1 ≤ r }`. The uneqrad lex-first
breaker is

`U_uneq = B_2((−2,−2,−2)) ∪ B_1((−2,−2,−1)) ∪ B_3((−2,−2,1))`,
radii `(2, 1, 3)`,
`v = (−3,−3,−1)`.

Occupancy `σ` is the 6-bit nearest-neighbor indicator of a union at an
unread site, in slot order

`(+x, −x, +y, −y, +z, −z)`.

On an occupied neighbor `w`,

`t(w) = min_i ‖w − s_i‖_1`.

Empty slots have no tick. Direct distances give `v ∉ U_uneq`,

`σ = (1, 0, 1, 0, 1, 1)`,
`t = (1, ·, 1, ·, 3, 2)`.

The same-center equal-radius union is

`U_same = B_2((−2,−2,−2)) ∪ B_2((−2,−2,−1)) ∪ B_2((−2,−2,1))`.

Then `‖v − s2‖_1 = 2`, so `v ∈ U_same` and this `v` is not unread. The
equal-radius control is therefore the displayed equal-`r` star of
ticklab:

`U_eq = B_2(0) ∪ B_2((2,0,0)) ∪ B_2((1,2,1))`,
`v_eq = (−1,1,1)`,

`σ_eq = (1, 0, 1, 1, 0, 1)`,
`t_eq = (2, ·, 2, 2, ·, 2)`.

The lex-first uneqrad weight-4 star (not a breaker) is

`(s1,s2,s3) = ((−2,−2,−2), (−2,−2,−1), (−2,−2,0))`, radii `(2, 1, 2)`,
same unread site `v = (−3,−3,−1)`, with the same occupancy
`σ = (1, 0, 1, 0, 1, 1)` and a different tick field
`t = (1, ·, 1, ·, 2, 2)`.

Score the lex-first breaker and this one equal-radius control. The
same-`σ` first star is the variation witness inside the uneqrad box.

## Theorem 1 — `σ` does not determine `t`

On `U_uneq` at `v`, the occupied neighbors and ticks are

- `+x = (−2,−3,−1)` has `t = 1`,
- `+y = (−3,−2,−1)` has `t = 1`,
- `+z = (−3,−3,0)` has `t = 3`,
- `−z = (−3,−3,−2)` has `t = 2`.

Hence mixed `t = (1, ·, 1, ·, 3, 2)` at `σ = (1, 0, 1, 0, 1, 1)`.

On the lex-first uneqrad weight-4 star the same unread site has the
same occupancy and

- `+x` has `t = 1`,
- `+y` has `t = 1`,
- `+z` has `t = 2`,
- `−z` has `t = 2`.

So `t` varies at fixed `σ` in the uneqrad box:
`(1, ·, 1, ·, 3, 2) ≠ (1, ·, 1, ·, 2, 2)`. Occupancy does not select
the tick field.

On the equal-radius control, ticklip applies: one common radius `r = 2`
forces `t = r` on every occupied neighbor. The displayed ticks are
constant `2`. That constant field is a different `t` from the mixed
uneqrad breaker field. The two scored hosts need not share `σ`; the
same-`σ` variation already lives inside the uneqrad box.

If `t` were a function of `σ`, the two uneqrad stars would carry the
same occupied ticks. They do not.

## Theorem 2 — newly named extra; do not adopt

A 6-NN occupancy is the nearest-neighbor condition at an unread site.
Admissibility still requires an NN-determined `μ`: the probability
distribution over the possibilities is determined by, and varies with,
the nearest-neighbor conditions. The lock-tick field (or the three
radii that produce it) is not a function of that occupancy. It is a
newly named extra relative to NN occupancy.

The extra is reported. Do not adopt the extra. Admissibility is not
enlarged by radii or by `t`. This is not leftover of uneqlaw (orbit
count): `N_commute = 24` is an orbit-membership count, not a test of
whether `t` is determined by `σ`.

## Theorem 3 — displayed, not adopted

The mixed breaker ticks, the same-`σ` first-star ticks, and the
constant equal-radius control ticks are displayed member data. They
are not the framework's fixed Admissibility rule. This note does not
write radii or t into Admissibility. Do not write radii or t into Admissibility. Do not write radii into Admissibility. Do not attach
L1. Occupancy-only formation is not attached. Qubit remains `M_2(C)`.
No approved primitive is added. No axiom edit.

## Honest-auditor / Boundary

- **What is proved.** On the uneqrad lex-first breaker, `σ` and mixed
  `t` are as displayed. The same-center equal-radius union occupies
  that `v`, so the equal-radius control is the ticklab star, with
  constant occupied `t = 2`. In the uneqrad box the lex-first
  weight-4 star has the same `σ` and a different `t`. Therefore `σ`
  does not determine `t`.
- **What is displayed only.** The three radii and the tick field are
  one rival extra table. They are not adopted.
- **What is not claimed.** No attachment of radii or `t` to
  Admissibility; no attachment of occupancy-only formation; no axiom
  edit; no formation rate; no lattice-wide dynamics; no leftover of
  uneqlaw (orbit count); no compiler no-go.
- **Mutation controls.** A rebuilt breaker `t` other than
  `(1, ·, 1, ·, 3, 2)` fails. A rebuilt first-star pair with a
  different `σ` or the same `t` fails. A note that writes radii or
  `t` into Admissibility, attaches L1, or authors an audit verdict
  fails.

This note authors no audit verdict.

## Primary Runner

The primary runner rebuilds `U_uneq` and `v`, the mixed lock-ticks,
the same-center equal-radius occupancy of `v`, the ticklab
equal-radius control, the lex-first same-`σ` uneqrad star, the
comparison that `σ` does not determine `t`, the current premise
boundary, and the mutation controls. It writes no cache and authors
no audit verdict.
