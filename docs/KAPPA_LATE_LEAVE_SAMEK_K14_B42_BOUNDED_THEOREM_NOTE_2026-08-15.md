---
claim_id: kappa_late_leave_samek_k14_b42_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Same-k reverse at k=14 under the named kappa-plus-late-leave hop-cost on B_42(0) is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/kappa_late_leave_samek_k14_b42_2026_08_15.py
---

# Named Kappa-Plus-Late-Leave Same-k Reverse At k=14 On B_42(0)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** one named nearest-neighbor hop-cost on the ℓ¹ ball `B_42(0)`,
scored only for the same-`k` axis versus body-diagonal arrival ratio at
`k=14`. First display of the named kappa-plus-late-leave hop-cost at the
wall.
**Audit-status authority:** independent audit lane only. This note authors
no audit verdict and predicts none.
**Primary runner:**
[`scripts/kappa_late_leave_samek_k14_b42_2026_08_15.py`](../scripts/kappa_late_leave_samek_k14_b42_2026_08_15.py)
**Cache:** none. `cache_write: false`.

## Result Up Front

The named kappa-plus-late-leave hop-cost `κλ` stacks both extras on the
ridge-slide rule `ρ3`: ridge-enter from `κ` and late-leave from `λ2`.
The ball is not leftover of a smaller-ball table: one origin Dijkstra is
run on `B_42(0)`, and the site `(14,14,14)` is absent from `B_39(0)`.
Uniqueness is not claimed.

Write `|σ_v|` for the number of nonzero coordinates of `v ∈ Z^3`. On a
directed nearest-neighbor hop `v → w` still inside `B_42(0)`, the displayed
ancestors of `κλ` are

`ν(v→w) = 3` if `|σ_v|=0` or `(|σ_v|=|σ_w|=1)` or `|σ_w| < |σ_v|`,
else `1`;

`μ(v→w) = 3` if `ν` would be `3` or `(|σ_v|=|σ_w|=2` and the least
nonzero `|w_i|` equals `1)`, else `1`;

`ρ3(v→w) = 3` if `μ` would be `3` or `(|σ_v|=|σ_w|=3` and exactly two
`|w_i|` equal `1)`, else `1`.

The displayed extras are

`κ(v→w) = 3` if `ρ3` would be `3` or `(|σ_v|=2` and `|σ_w|=3` and
exactly two `|w_i|` equal `1)`, else `1`;

`λ2(v→w) = 3` if `ρ3` would be `3` or `(|σ_v|=1` and `|σ_w|=2` and
`max_i |w_i| ≥ 2)`, else `1`.

The displayed rule `κλ` is

`κλ(v→w) = 3` if `ρ3` would be `3` or `(|σ_v|=2` and `|σ_w|=3` and
exactly two `|w_i|` equal `1)` or `(|σ_v|=1` and `|σ_w|=2` and
`max_i |w_i| ≥ 2)`, else `1`.

The first extra is ridge-enter. The second extra is late-leave: a
leave-axis hop whose destination has some absolute coordinate at least
`2`. The unit-cube leave `(1,0,0) → (1,1,0)` stays cost `1`. The body
last hop `(1,1,0) → (1,1,1)` stays cost `1`.

One Dijkstra from the origin on `B_42(0)` (102425 sites; 102424 nonzero)
gives the first display of `κλ` at the wall

`t(14,0,0) = 26`, `t(14,14,14) = 46`.

The displayed same-`k` comparison at `k=14` is

`t(14,0,0)^2 / 196  ?  t(14,14,14)^2 / 588`,

which is `676/196` versus `2116/588`, or equivalently `2028 > 2116`. The
inequality does not hold. Same-`k` reverse does not restore at `k=14`.
Independently, the new axis site is `t(42,0,0) = 58`. The shared axis site
`t(39,0,0) = 51` is an independent readout on this ball.

The integers `26` and `46` coincide with the named `ρ3` wall pair. They
are not leftover of `ρ3`. They are not leftover of `κ`. They are not leftover of `λ2`.
On `(2,1,0) → (2,1,1)` one has `|σ| : 2 → 3` and exactly two `|w_i|`
equal `1`, so `κλ = 3` while `ρ3 = 1` and `λ2 = 1`. On
`(2,0,0) → (2,1,0)` one has `|σ| : 1 → 2` and `max |w_i| = 2`, so
`κλ = 3` while `ρ3 = 1` and `κ = 1`. Stacking both extras therefore
prices hops that neither ancestor prices alone.

The rule is displayed, not adopted. Do not write κλ into Admissibility.
Do not attach L1.

## Current Premise Boundary

The Lattice and Admissibility premises are quoted from
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md):

Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
adjacency, standard translations, and proper cubic rotations about each site.

There is one fixed nearest-neighbor admissibility rule, covariant under lattice
translations and proper cubic rotations.

For each site, the probability distribution over the possibilities is
determined by, and varies with, the nearest-neighbor conditions.

Lattice supplies the six-neighbor graph and the ball. Admissibility supplies
none of the hop costs. The integers `3` and `1`, the support-size clauses,
and the arrival function `t` are separately displayed mathematical inputs.
No axiom text is edited.

## Named Rule

Let `B_42(0) = { v ∈ Z^3 : |v|_1 ≤ 42 }`. Directed edges are the six
nearest-neighbor steps whose both ends lie in the ball. For `v ∈ B_42(0)`,
`t(v)` is the least sum of `κλ` along a directed path from `0` to `v` in
that graph.

The site `(14,0,0)` has ℓ¹ norm `14` and therefore also lies in `B_39(0)`.
The site `(14,14,14)` has ℓ¹ norm `42`, so it is absent from `B_39(0)`. The
`B_42(0)` table is therefore not leftover of the `B_39(0)` times.

The ridge-slide comparator `ρ3` uses every clause of `κλ` except the two
stacked extras. The ridge-enter comparator `κ` omits late-leave. The
late-leave comparator `λ2` omits ridge-enter. Therefore none of those
three comparators can price both extras, and the `κλ` scores below are
not a leftover of `ρ3`, of `κ`, or of `λ2`.

## Theorem 1 — Arrivals `t(14,0,0)` And `t(14,14,14)` On `B_42(0)`

One origin Dijkstra on `B_42(0)` returns the integer arrivals

| site | `t_κλ` |
|---|---:|
| `(14,0,0)` | `26` |
| `(14,14,14)` | `46` |

Every listed site lies in `B_42(0)`. The site `(14,14,14)` has ℓ¹ norm `42`,
so it is absent from `B_39(0)`. The pair is computed on `B_42(0)`, not
copied from a smaller-ball table. These values are Dijkstra outputs, not
fitted scalars.

## Theorem 2 — Reverse At The Same-`k` Scale `k=14`

The Euclidean-normalized comparison at `k=14` is

`t(14,0,0)^2 / 196  ?  t(14,14,14)^2 / 588`,

equivalently `3 t(14,0,0)^2 ? t(14,14,14)^2`. Substituting the computed times
gives `3 · 26^2 = 2028` and `46^2 = 2116`, so

`2028 > 2116` is false; `2028 < 2116`.

Arrival per Euclidean length is smaller at `(14,0,0)` than at `(14,14,14)`.
Same-`k` reverse at `k=14` is no. Reverse does not restore at the wall. The
comparison is displayed, not adopted.

## Theorem 3 — Displayed, Not Adopted

The rule `κλ` is a displayed scoring device on `B_42(0)`. Do not write κλ
into Admissibility. Do not attach L1. It is not a replacement for
unit-cost first arrival, and it is not offered as the unique hop-cost with
same-`k` reverse.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact integer same-k arrivals and reverse comparison on the finite ball B_42(0) for one named hop-cost at k=14. The hop-cost is displayed, not adopted."
trace_class: frontier_discovery
artifact_role: theorem
conditional_surface_status: "exact on B_42(0) for the displayed rule κλ at k=14; no Admissibility edit; not attached to L1"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## What This Note Does Not Claim

- Uniqueness of `κλ` among hop-costs that score the same-`k` pair at `k=14`.
- Any edit of Lattice, Qubit, Admissibility, or Record.
- Any attachment to L1.
- Any continuum potential, any inverse-power kernel, and any gravitational
  identification.
- Any statement off `B_42(0)`.
- Any score for a pair that is not the same-`k` axis / body-diagonal pair
  at `k=14`.
- Any reuse of a smaller-ball arrival table as a substitute for the
  radius-`42` Dijkstra.
- Membership of `κλ` as a physical hop-cost. Reverse at `k=14` on this ball
  is a displayed comparison, not an adoption.
