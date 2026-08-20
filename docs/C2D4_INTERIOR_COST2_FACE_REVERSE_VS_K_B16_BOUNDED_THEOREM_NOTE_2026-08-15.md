---
claim_id: c2d4_interior_cost2_face_reverse_vs_k_b16_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Face reverse under the named c2d4-plus-interior hop-cost on B_16(0) at k=1..8 is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/c2d4_interior_cost2_face_reverse_vs_k_b16_2026_08_15.py
---

# Named C2d4-Plus-Interior Cost-2 Face Reverse Versus Integer Scale `k` On `B_16(0)`

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** one named nearest-neighbor hop-cost on the ℓ¹ ball `B_16(0)`,
scored only for the face-diagonal reverse comparison at every available
integer scale `k=1..8`.
**Audit-status authority:** independent audit lane only. This note authors
no audit verdict and predicts none.
**Primary runner:**
[`scripts/c2d4_interior_cost2_face_reverse_vs_k_b16_2026_08_15.py`](../scripts/c2d4_interior_cost2_face_reverse_vs_k_b16_2026_08_15.py)
**Cache:** none. `cache_write: false`.

## Result Up Front

Write `|σ_v|` for the number of nonzero coordinates of `v ∈ Z^3`. On a
directed nearest-neighbor hop `v → w` still inside `B_16(0)`, the stacked
rules `ν`, `μ`, and `ρ3` are

`ν(v→w) = 3` if `|σ_v|=0` or `(|σ_v|=|σ_w|=1)` or `|σ_w| < |σ_v|`, else `1`;

`μ(v→w) = 3` if `ν` would be `3` or `(|σ_v|=|σ_w|=2` and the least nonzero
`|w_i|` equals `1)`, else `1`;

`ρ3(v→w) = 3` if `μ` would be `3` or `(|σ_v|=|σ_w|=3` and exactly two
`|w_i|` equal `1)`, else `1`.

The displayed cost-2 max≥4 out-face rule `c2d4` is `ρ3` plus cost `2` (not `3`)
on a `2→2` hop whose destination max grows and whose source max is already
at least `4`:

`c2d4(v→w) = 3` if `ρ3` would be `3`, else `2` if (`|σ_v|=|σ_w|=2` and
`max_i |w_i| > max_i |v_i|` and `max_i |v_i| ≥ 4`), else `1`.

The displayed c2d4-plus-interior rule `i2` is `c2d4` plus cost `2` (not `3`)
on a `3→3` hop whose destination minimum absolute coordinate is already at
least `2` (interior body hops):

`i2(v→w) = 3` if `ρ3` would be `3`, else `2` if `c2d4` would be `2` or
(`|σ_v|=|σ_w|=3` and `min_i |w_i| ≥ 2`), else `1`.

Those clauses are the whole rule. Uniqueness is not claimed. This note is
the first display of face reverse under `i2` at `k=1..8` on `B_16(0)`.

The interior extra fires on `(2,2,2) → (3,2,2)`: that hop has `|σ|=3→3` and
destination min abs `2`, so `i2 = 2` while `c2d4 = ρ3 = 1`. The interior
extra is idle on `(2,2,2) → (2,2,1)`: that hop has `|σ|=3→3` but destination
min abs `1`, so `i2 = ρ3 = 1`. The interior extra also skips
`(1,1,1) → (2,1,1)`: destination min abs is `1`, and corridor-slide `ρ3`
already prices that hop at `3` because the destination has exactly two unit
coordinates, so `i2 = ρ3 = 3` there. The interior extra is not leftover of
`ρ3`: the interior body-growth hop `(2,2,2) → (3,2,2)` has `ρ3=1` and
`i2=2`.

The inherited `c2d4` extra still fires on `(4,2,0) → (5,2,0)`: that hop has
`|σ|=2→2`, dest max `5` greater than source max `4`, and source max `4`, so
`i2 = c2d4 = 2` while `ρ3 = 1`. The inherited extra skips
`(3,2,0) → (4,2,0)` (source max `3`) and `(2,2,0) → (3,2,0)` (source max
`2`). The unit-out-face hop `(1,1,0) → (2,1,0)` has source max `1`, so the
inherited extra is idle; corridor-slide `μ` already prices that hop at `3`,
so `i2 = ρ3 = 3` there.

A pair `((2k,0,0),(k,k,0))` is available when both sites lie in `B_16(0)`.
That is `| (2k,0,0) |_1 = 2k ≤ 16` and `| (k,k,0) |_1 = 2k ≤ 16`, so every
`k=1..8` is available. No scale is omitted.

One Dijkstra from the origin on `B_16(0)` (6017 sites; 6016 nonzero) gives

`t(2,0,0) = 6`, `t(4,0,0) = 12`, `t(6,0,0) = 18`, `t(8,0,0) = 24`,
`t(10,0,0) = 26`, `t(12,0,0) = 28`, `t(14,0,0) = 31`, `t(16,0,0) = 37`,

`t(1,1,0) = 4`, `t(2,2,0) = 8`, `t(3,3,0) = 10`, `t(4,4,0) = 12`,
`t(5,5,0) = 15`, `t(6,6,0) = 18`, `t(7,7,0) = 21`, `t(8,8,0) = 24`.

For each available `k`, the displayed face-diagonal comparison is whether

`t(2k,0,0)^2 / (4k^2) > t(k,k,0)^2 / (2k^2)`,

equivalently `t(2k,0,0)^2 > 2 t(k,k,0)^2`. The bits are

| `k` | pair | axis `t^2/|v|_2^2` | face `t^2/|v|_2^2` | reverse |
|---|---|---|---|---|
| `1` | `((2,0,0),(1,1,0))` | `36/4=9` | `16/2=8` | yes |
| `2` | `((4,0,0),(2,2,0))` | `144/16=9` | `64/8=8` | yes |
| `3` | `((6,0,0),(3,3,0))` | `324/36=9` | `100/18=50/9` | yes |
| `4` | `((8,0,0),(4,4,0))` | `576/64=9` | `144/32=9/2` | yes |
| `5` | `((10,0,0),(5,5,0))` | `676/100=169/25` | `225/50=9/2` | yes |
| `6` | `((12,0,0),(6,6,0))` | `784/144=49/9` | `324/72=9/2` | yes |
| `7` | `((14,0,0),(7,7,0))` | `961/196` | `441/98=9/2` | yes |
| `8` | `((16,0,0),(8,8,0))` | `1369/256` | `576/128=9/2` | yes |

Exact integer comparisons `t(2k,0,0)^2 ? 2 t(k,k,0)^2`:

- `k=1`: `36 > 32` holds
- `k=2`: `144 > 128` holds
- `k=3`: `324 > 200` holds
- `k=4`: `576 > 288` holds
- `k=5`: `676 > 450` holds
- `k=6`: `784 > 648` holds
- `k=7`: `961 > 882` holds
- `k=8`: `1369 > 1152` holds

The hold/fail pattern of the eight bits is yes, yes, yes, yes, yes, yes, yes, yes.
Face reverse holds at `k=1..8`. There is no fail among the eight bits.

A pure both-weights-`1` axis walk to `(2k,0,0)` costs `6k`. That walk
matches the Dijkstra arrival through `k=4`. From `k=5` the computed axis
arrival is strictly cheaper than `6k`. Those walks are witnesses, not a
uniqueness claim.

The sixteen arrivals are computed on `B_16(0)` under `i2`, not copied from
a smaller-ball table and not copied from a `c2d4` or `ρ3` pair table. The
interior clause is live on this host: `(2,2,2) → (3,2,2)` lies in `B_16(0)`
and has `i2 = 2` while `c2d4 = ρ3 = 1`. On the sixteen displayed
face-versus-axis sites the `i2` arrivals equal the corresponding `c2d4`
arrivals; that coincidence is an output of the `i2` Dijkstra, not a
substitution of a `c2d4` table.

The rule is displayed, not adopted. Do not write `i2` into Admissibility.
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
none of the hop costs. The integers `3`, `2`, and `1`, the support-size,
max-coordinate, min-coordinate, and source-max clauses, and the arrival
function `t` are separately displayed mathematical inputs. No axiom text is
edited.

## Named Rule

Let `B_16(0) = { v ∈ Z^3 : |v|_1 ≤ 16 }`. Directed edges are the six
nearest-neighbor steps whose both ends lie in the ball. For `v ∈ B_16(0)`,
`t(v)` is the least sum of `i2` along a directed path from `0` to `v` in
that graph.

The first `ν` clause is seed-exit. The second is both weights `1`. The third
is support drop. The `μ` addendum taxes a `2→2` hop whose destination still
touches a unit coordinate. The `ρ3` addendum taxes a `3→3` hop whose
destination has exactly two unit coordinates. The `c2d4` addendum taxes a
`2→2` hop that grows the coordinate box on a face whose source max is
already at least `4`, at cost `2` rather than cost `3`. The `i2` addendum
taxes a `3→3` hop whose destination has already left every unit coordinate,
at cost `2` rather than cost `3`. It skips body hops whose destination still
has a unit coordinate.

## Theorem 1 — Arrivals `t(2k,0,0)` And `t(k,k,0)` On `B_16(0)`

One origin Dijkstra on `B_16(0)` returns the integer arrivals

| site | `t_{i2}` |
|---|---:|
| `(2,0,0)` | `6` |
| `(1,1,0)` | `4` |
| `(4,0,0)` | `12` |
| `(2,2,0)` | `8` |
| `(6,0,0)` | `18` |
| `(3,3,0)` | `10` |
| `(8,0,0)` | `24` |
| `(4,4,0)` | `12` |
| `(10,0,0)` | `26` |
| `(5,5,0)` | `15` |
| `(12,0,0)` | `28` |
| `(6,6,0)` | `18` |
| `(14,0,0)` | `31` |
| `(7,7,0)` | `21` |
| `(16,0,0)` | `37` |
| `(8,8,0)` | `24` |

Every listed site lies in `B_16(0)`. No `k=1..8` pair is omitted. The
sixteen values are computed on `B_16(0)`, not copied from a larger-ball
table. These values are Dijkstra outputs, not fitted scalars.

A witness walk to `(2,0,0)` is seed-exit `3` onto `(1,0,0)` and both-weights-`1`
axis hop `3` onto `(2,0,0)`, summing to `6`. A witness walk to `(1,1,0)` is
seed-exit `3` onto `(0,1,0)` and support-increase `1` onto `(1,1,0)`,
summing to `4`. A witness walk to `(8,0,0)` is eight both-weights-`1` axis
hops of cost `3`, summing to `24`. Those walks are witnesses, not a
uniqueness claim.

For each `k=1..8` the note also records whether

`t(2k,0,0)^2 / (4k^2) > t(k,k,0)^2 / (2k^2)`.

## Theorem 2 — Hold/Fail Pattern Of The Eight Bits

The Euclidean-normalized comparison at each available `k` is

`t(2k,0,0)^2 / (4k^2) > t(k,k,0)^2 / (2k^2)`,

equivalently `t(2k,0,0)^2 > 2 t(k,k,0)^2`. Substituting the computed times
gives the eight bits of Result Up Front. The hold/fail pattern is
yes, yes, yes, yes, yes, yes, yes, yes. Reverse holds at `k=1..8`. The
comparison is displayed, not adopted.

## Theorem 3 — Displayed, Not Adopted

The rule `i2` is a displayed scoring device on `B_16(0)`. Do not write
`i2` into Admissibility. Do not attach L1. It is not a replacement for
unit-cost first arrival, and it is not offered as the unique hop-cost with
face reverse at any `k`.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact integer face-versus-axis arrivals and reverse bits versus available integer scale k on the finite ball B_16(0) for one named hop-cost. The rule is displayed, not adopted."
trace_class: frontier_discovery
artifact_role: theorem
conditional_surface_status: "exact on B_16(0) for the displayed rule i2 at available k=1..8; no Admissibility edit; not attached to L1"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## What This Note Does Not Claim

- Uniqueness of `i2` among hop-costs that score the face-versus-axis bits
  at any `k`.
- Any edit of Lattice, Qubit, Admissibility, or Record.
- Any attachment to L1.
- Any continuum potential, any inverse-power kernel, and any gravitational
  identification.
- Any statement off `B_16(0)`.
- Any score for a pair that is not an available face-versus-axis pair
  `((2k,0,0),(k,k,0))` at `k=1..8`.
- Any reuse of a `c2d4` or `ρ3` arrival table as a substitute for the `i2`
  Dijkstra.
- Any reuse of a larger-ball arrival table as a substitute for the
  radius-`16` Dijkstra.
- Any adoption of `i2` as an admissibility rule. Face reverse versus `k`
  on this ball is a displayed comparison, not an adoption.
