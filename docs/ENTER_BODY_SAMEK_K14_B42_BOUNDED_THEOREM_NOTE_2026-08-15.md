---
claim_id: enter_body_samek_k14_b42_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Same-k reverse at k=14 under the named enter-body hop-cost on B_42(0) is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/enter_body_samek_k14_b42_2026_08_15.py
---

# Named Enter-Body Same-k Reverse At k=14 On B_42(0)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** one named nearest-neighbor hop-cost on the ℓ¹ ball `B_42(0)`,
scored only for the same-`k` axis versus body-diagonal arrival ratio at
`k=14`.
**Audit-status authority:** independent audit lane only. This note authors
no audit verdict and predicts none.
**Primary runner:**
[`scripts/enter_body_samek_k14_b42_2026_08_15.py`](../scripts/enter_body_samek_k14_b42_2026_08_15.py)
**Cache:** none. `cache_write: false`.

## Result Up Front

The named enter-body hop-cost `ε` is the already scored corridor-slide
rule `μ` plus cost `3` on a `2→3` hop. `ε` restores same-`k` reverse at
`k=13` (`25` versus `43`). The new residual is whether that reverse still
holds at `k=14` on `B_42(0)`. The ball is
not leftover of a smaller-ball table: one origin Dijkstra is run on this
ball.
Uniqueness is not claimed.

Write `|σ_v|` for the number of nonzero coordinates of `v ∈ Z^3`. On a
directed nearest-neighbor hop `v → w` still inside `B_42(0)`, the displayed
rule `ε` is

`ε(v→w) = 3` if `μ` would be `3` or `(|σ_v|=2` and `|σ_w|=3)`, else `1`,

where `μ(v→w) = 3` if `ν` would be `3` or `(|σ_v|=|σ_w|=2` and the least
nonzero `|w_i|` equals `1)`, else `1`,

and `ν(v→w) = 3` if `|σ_v|=0` or `(|σ_v|=|σ_w|=1)` or `|σ_w| < |σ_v|`,
else `1`.

The first three clauses are seed-exit, both weights `1`, and support drop.
The fourth clause is the corridor slide. The fifth clause is enter-body.
Those five clauses are the whole rule.

One Dijkstra from the origin on `B_42(0)` (102425 sites; 102424 nonzero) gives

`t(14,0,0) = 26`, `t(14,14,14) = 46`.

The displayed same-`k` comparison at `k=14` is

`t(14,0,0)^2 / 196  ?  t(14,14,14)^2 / 588`,

which is `676/196` versus `2116/588`, or equivalently `2028 > 2116`. The
inequality does not hold. Same-`k` reverse at `k=14` under `ε` is no. The
`k=13` restore does not continue at `k=14`. Independently, the new axis
site is `t(42,0,0) = 58`. The shared axis site `t(39,0,0) = 51` is an `ε`
score on this ball, not a leftover of the `B_39(0)` table.

The pair is not leftover of `μ`: on the enter-body hop
`(1,1,0) → (1,1,1)` one has `|σ| : 2 → 3`, so `μ = 1` while `ε = 3`.
Therefore `μ` cannot price enter body, and the `ε` scores below are not a
leftover of `μ`. The site `(14,14,14)` has ℓ¹ norm `42`, so it is absent
from `B_39(0)`. The `B_42(0)` table is therefore
not leftover of the `B_39(0)` times. On this same Dijkstra the restored
`k=13` pair remains
`t(13,0,0) = 25` and `t(13,13,13) = 43`; those are not the `k=14` pair.

The rule is displayed, not adopted. Do not write `ε` into Admissibility.
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
the least-nonzero-coordinate clause, and the arrival function `t` are
separately displayed mathematical inputs. No axiom text is edited.

## Named Rule

Let `B_42(0) = { v ∈ Z^3 : |v|_1 ≤ 42 }`. Directed edges are the six
nearest-neighbor steps whose both ends lie in the ball. For `v ∈ B_42(0)`,
`t(v)` is the least sum of `ε` along a directed path from `0` to `v` in
that graph.

The comparator `μ` uses only the first four clauses of `ε`. On the
enter-body hop `(1,1,0) → (1,1,1)` one has `|σ| : 2 → 3`, so `μ = 1`
while `ε = 3`. Therefore `μ` cannot price enter body, and the `ε` scores
below are not a leftover of `μ`.

## Theorem 1 — Arrivals `t(14,0,0)` And `t(14,14,14)` On `B_42(0)`

One origin Dijkstra on `B_42(0)` returns the integer arrivals

| site | `t_ε` |
|---|---:|
| `(14,0,0)` | `26` |
| `(14,14,14)` | `46` |

Every listed site lies in `B_42(0)`. The site `(14,14,14)` has ℓ¹ norm `42`,
so it is absent from `B_39(0)`. The pair is computed on `B_42(0)`, not
copied from a smaller-ball table and not copied from the restored `k=13`
pair `25` versus `43`. These values are Dijkstra outputs, not fitted scalars.

A witness axis walk of cost `26` is seed-exit `3` onto `(1,0,0)`,
support-increase `1` onto `(1,1,0)`, enter-body `3` onto `(1,1,1)`,
thirteen support-preserving cost-`1` body hops to `(14,1,1)`, and two
support-drops `3` then `3` onto `(14,0,0)`, summing to `26`. A witness
body walk of cost `46` is the same prefix onto `(1,1,1)`, then
thirty-nine support-preserving cost-`1` hops to `(14,14,14)`, summing to
`46`. Those walks are witnesses, not a uniqueness claim.

## Theorem 2 — Reverse At The Same-`k` Scale `k=14`

The Euclidean-normalized comparison at `k=14` is

`t(14,0,0)^2 / 196  ?  t(14,14,14)^2 / 588`,

equivalently `3 t(14,0,0)^2 ? t(14,14,14)^2`. Substituting the computed times
gives `3 · 26^2 = 2028` and `46^2 = 2116`, so

`2028 > 2116` is false; `2028 < 2116`.

Arrival per Euclidean length is smaller at `(14,0,0)` than at `(14,14,14)`.
Same-`k` reverse at `k=14` under `ε` is no. The inequality does not hold.
The comparison is displayed, not adopted.

## Theorem 3 — Displayed, Not Adopted

The rule `ε` is a displayed scoring device on `B_42(0)`. Do not write `ε`
into Admissibility. Do not attach L1. It is not a replacement for
unit-cost first arrival, and it is not offered as the unique hop-cost with
same-`k` reverse.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact integer same-k arrivals and reverse comparison on the finite ball B_42(0) for one named hop-cost at k=14. The rule is displayed, not adopted."
trace_class: frontier_discovery
artifact_role: theorem
conditional_surface_status: "exact on B_42(0) for the displayed rule ε at k=14; no Admissibility edit; not attached to L1"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## What This Note Does Not Claim

- Uniqueness of `ε` among hop-costs that score the same-`k` pair at `k=14`.
- Any edit of Lattice, Qubit, Admissibility, or Record.
- Any attachment to L1.
- Any continuum potential, any inverse-power kernel, and any gravitational
  identification.
- Any statement off `B_42(0)`.
- Any score for a pair that is not the same-`k` axis / body-diagonal pair
  at `k=14`.
- Any reuse of a smaller-ball arrival table, or of the `μ` table, as a
  substitute for the radius-`42` Dijkstra.
- Membership of `ε` as a physical hop-cost. The `k=13` restore does not
  continue at `k=14` on this ball; that is a displayed exclusion test, not
  an adoption.
