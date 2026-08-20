---
claim_id: cost2_ridge_enter_face_reverse_vs_k_b16_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Face-diagonal reverse versus integer scale k under the named cost-2 ridge-enter hop-cost on B_16(0) is reported for available k=1..8. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/cost2_ridge_enter_face_reverse_vs_k_b16_2026_08_15.py
---

# Named Cost-2 Ridge-Enter Face Reverse Versus Integer Scale k On B_16(0)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** one named nearest-neighbor hop-cost on the ℓ¹ ball `B_16(0)`,
scored only for the face-diagonal reverse comparison at every available
integer scale `k=1..8`.
**Audit-status authority:** independent audit lane only. This note authors
no audit verdict and predicts none.
**Primary runner:**
[`scripts/cost2_ridge_enter_face_reverse_vs_k_b16_2026_08_15.py`](../scripts/cost2_ridge_enter_face_reverse_vs_k_b16_2026_08_15.py)
**Cache:** none. `cache_write: false`.

## Result Up Front

The named cost-2 ridge-enter hop-cost `c2` is the already scored ridge-slide
rule `ρ3` except that a `2→3` hop whose destination has exactly two
absolute coordinates equal to `1` costs `2`, not `1`. Same-`k` reverse
under `c2` holds at `k=1` on `B_6(0)`. This is the first display of the
face-versus-axis bits versus integer scale `k=1..8` for `c2` on
`B_16(0)`. Uniqueness is not claimed.

Write `|σ_v|` for the number of nonzero coordinates of `v ∈ Z^3`. On a
directed nearest-neighbor hop `v → w` still inside `B_16(0)`, the displayed
comparators are

`ν(v→w) = 3` if `|σ_v|=0` or `(|σ_v|=|σ_w|=1)` or `|σ_w| < |σ_v|`,
else `1`;

`μ(v→w) = 3` if `ν` would be `3` or `(|σ_v|=|σ_w|=2` and the least
nonzero `|w_i|` equals `1)`, else `1`;

`ρ3(v→w) = 3` if `μ` would be `3` or `(|σ_v|=|σ_w|=3` and exactly two
`|w_i|` equal `1)`, else `1`;

`κ(v→w) = 3` if `ρ3` would be `3` or `(|σ_v|=2` and `|σ_w|=3` and exactly
two `|w_i|` equal `1)`, else `1`;

`c2(v→w) = 3` if `ρ3` would be `3`, else `2` if `(|σ_v|=2` and `|σ_w|=3`
and exactly two `|w_i|` equal `1)`, else `1`.

Those stacked clauses are the whole rule. The extra `c2` clause is a
ridge-enter: support rises `2→3` and the destination has exactly two unit
coordinates. It is not the all-`2→3` tax, and it is not the cost-`3`
ridge-enter `κ`.

A pair `((2k,0,0),(k,k,0))` is available when both sites lie in `B_16(0)`.
That is `| (2k,0,0) |_1 = 2k ≤ 16` and `| (k,k,0) |_1 = 2k ≤ 16`, so every
`k=1..8` is available. No scale is omitted.

One Dijkstra from the origin on `B_16(0)` (6017 sites; 6016 nonzero) gives

`t(2,0,0) = 6`, `t(4,0,0) = 12`, `t(6,0,0) = 18`, `t(8,0,0) = 20`,
`t(10,0,0) = 22`, `t(12,0,0) = 24`, `t(14,0,0) = 26`, `t(16,0,0) = 32`,

`t(1,1,0) = 4`, `t(2,2,0) = 8`, `t(3,3,0) = 10`, `t(4,4,0) = 12`,
`t(5,5,0) = 14`, `t(6,6,0) = 16`, `t(7,7,0) = 18`, `t(8,8,0) = 20`.

For each available `k`, the displayed face-diagonal comparison is whether

`t(2k,0,0)^2 / (4k^2) > t(k,k,0)^2 / (2k^2)`,

equivalently `t(2k,0,0)^2 > 2 t(k,k,0)^2`. The bits are

| `k` | pair | axis `t^2/|v|_2^2` | face `t^2/|v|_2^2` | reverse |
|---|---|---|---|---|
| `1` | `((2,0,0),(1,1,0))` | `36/4=9` | `16/2=8` | yes |
| `2` | `((4,0,0),(2,2,0))` | `144/16=9` | `64/8=8` | yes |
| `3` | `((6,0,0),(3,3,0))` | `324/36=9` | `100/18=50/9` | yes |
| `4` | `((8,0,0),(4,4,0))` | `400/64=25/4` | `144/32=9/2` | yes |
| `5` | `((10,0,0),(5,5,0))` | `484/100=121/25` | `196/50=98/25` | yes |
| `6` | `((12,0,0),(6,6,0))` | `576/144=4` | `256/72=32/9` | yes |
| `7` | `((14,0,0),(7,7,0))` | `676/196=169/49` | `324/98=162/49` | yes |
| `8` | `((16,0,0),(8,8,0))` | `1024/256=4` | `400/128=25/8` | yes |

Exact integer comparisons `t(2k,0,0)^2 ? 2 t(k,k,0)^2`:

- `k=1`: `36 > 32` holds
- `k=2`: `144 > 128` holds
- `k=3`: `324 > 200` holds
- `k=4`: `400 > 288` holds
- `k=5`: `484 > 392` holds
- `k=6`: `576 > 512` holds
- `k=7`: `676 > 648` holds
- `k=8`: `1024 > 800` holds

Reverse holds at every available `k=1..8`. The extra ridge-enter clause
is live on this host: the hop `(2,1,0) → (2,1,1)` lies in `B_16(0)` and
has `c2 = 2` while `ρ3 = 1` and `κ = 3`, so `ρ3` cannot price the
ridge-enter and `κ` cannot price it at cost `2`. Independently,
`t(14,1,1) = 25`. The displayed body last hop `(1,1,0) → (1,1,1)` has
three unit coordinates, so the extra clause does not fire and that hop
keeps cost `1`.

The sixteen arrivals are computed on `B_16(0)` under `c2`, not copied from
a smaller-ball table and not copied from a `ρ3` or `κ` pair table. The
axis endpoint of this ball is `t(16,0,0) = 32`. The only in-ball neighbor
of `(16,0,0)` is `(15,0,0)`, so the last hop is the both-weights-`1` axis
step of cost `3`. The site `(16,-1,-1)` lies outside `B_16(0)`.

The rule is displayed, not adopted. Do not write c2 into Admissibility.
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
none of the hop costs. The integers `3`, `2`, and `1`, the support-size
clauses, the two-unit-destination test, and the arrival function `t` are
separately displayed mathematical inputs. No axiom text is edited.

## Named Rule

Let `B_16(0) = { v ∈ Z^3 : |v|_1 ≤ 16 }`. Directed edges are the six
nearest-neighbor steps whose both ends lie in the ball. For `v ∈ B_16(0)`,
`t(v)` is the least sum of `c2` along a directed path from `0` to `v` in
that graph.

The comparator `ρ3` uses only the first three stacked clauses of `c2`. On
the ridge-enter hop `(2,1,0) → (2,1,1)` one has `|σ| : 2 → 3` and exactly
two `|w_i| = 1`, so `ρ3 = 1` while `c2 = 2` and `κ = 3`. Therefore `ρ3`
cannot price the ridge-enter, `κ` cannot price it at cost `2`, and the
`c2` scores below are not a leftover of a `ρ3`-only or `κ`-only walk
inventory. On the interior `3→3` hop `(2,2,2) → (3,2,2)` the destination
has no unit coordinate, so `c2` costs `1`.

## Theorem 1 — Arrivals `t(2k,0,0)` And `t(k,k,0)` On `B_16(0)`

One origin Dijkstra on `B_16(0)` returns the integer arrivals

| site | `t_c2` |
|---|---:|
| `(2,0,0)` | `6` |
| `(1,1,0)` | `4` |
| `(4,0,0)` | `12` |
| `(2,2,0)` | `8` |
| `(6,0,0)` | `18` |
| `(3,3,0)` | `10` |
| `(8,0,0)` | `20` |
| `(4,4,0)` | `12` |
| `(10,0,0)` | `22` |
| `(5,5,0)` | `14` |
| `(12,0,0)` | `24` |
| `(6,6,0)` | `16` |
| `(14,0,0)` | `26` |
| `(7,7,0)` | `18` |
| `(16,0,0)` | `32` |
| `(8,8,0)` | `20` |

Every listed site lies in `B_16(0)`. No `k=1..8` pair is omitted. The
sixteen values are computed on `B_16(0)`, not copied from a larger-ball
table. These values are Dijkstra outputs, not fitted scalars.

A witness walk to `(2,0,0)` is seed-exit `3` onto `(1,0,0)` and both-weights-`1`
axis hop `3` onto `(2,0,0)`, summing to `6`. A witness walk to `(1,1,0)` is
seed-exit `3` onto `(0,1,0)` and body `1→2` of cost `1` onto `(1,1,0)`,
summing to `4`. A witness walk to `(6,0,0)` is six both-weights-`1` axis
hops of cost `3`, summing to `18`. A witness walk to `(3,3,0)` is seed-exit
`3` onto `(0,1,0)`, body `1` onto `(1,1,0)`, hugging slide `3` onto
`(1,2,0)`, then three cost-`1` face hops onto `(3,3,0)`, summing to `10`.
Those walks are witnesses, not a uniqueness claim.

## Theorem 2 — Face Reverse Versus Available Integer Scale `k`

The Euclidean-normalized comparison at each available `k` is

`t(2k,0,0)^2 / (4k^2) > t(k,k,0)^2 / (2k^2)`,

equivalently `t(2k,0,0)^2 > 2 t(k,k,0)^2`. Substituting the computed times
gives the eight bits of Result Up Front. In particular the `k=3`
comparison is `324/36` versus `100/18`, or `324 > 200`, so `k=3` still
holds, and the `k=7` comparison is `676/196` versus `324/98`, or
`676 > 648`, so `k=7` still holds.

Arrival per Euclidean length is larger at `(2k,0,0)` than at `(k,k,0)` for
every available `k=1..8`. The comparison is displayed, not adopted. The
inequality holds at each available scale.

## Theorem 3 — Displayed, Not Adopted

The rule `c2` is a displayed scoring device on `B_16(0)`. Do not write c2
into Admissibility. Do not attach L1. It is not a replacement for
unit-cost first arrival, and it is not offered as the unique hop-cost with
face reverse at any `k`.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact integer face-versus-axis arrivals and reverse bits versus available integer scale k on the finite ball B_16(0) for one named hop-cost. The rule is displayed, not adopted."
trace_class: frontier_discovery
artifact_role: theorem
conditional_surface_status: "exact on B_16(0) for the displayed rule c2 at available k=1..8; no Admissibility edit; not attached to L1"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## What This Note Does Not Claim

- Uniqueness of `c2` among hop-costs that score the face-versus-axis bits
  at any `k`.
- Any edit of Lattice, Qubit, Admissibility, or Record.
- Any attachment to L1.
- Any continuum potential, any inverse-power kernel, and any gravitational
  identification.
- Any statement off `B_16(0)`.
- Any score for a pair that is not an available face-versus-axis pair
  `((2k,0,0),(k,k,0))` at `k=1..8`.
- Any reuse of a `ρ3` or `κ` arrival table as a substitute for the `c2`
  Dijkstra.
- Any reuse of a larger-ball arrival table as a substitute for the
  radius-`16` Dijkstra.
- Membership of `c2` as a physical hop-cost. Face reverse versus `k` on
  this ball is a displayed comparison, not an adoption.
