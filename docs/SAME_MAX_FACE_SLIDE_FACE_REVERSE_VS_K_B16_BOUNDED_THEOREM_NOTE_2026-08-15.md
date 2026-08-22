---
claim_id: same_max_face_slide_face_reverse_vs_k_b16_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Face reverse under the named same-max face-slide hop-cost on B_16(0) at k=1..8 is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/same_max_face_slide_face_reverse_vs_k_b16_2026_08_15.py
---

# Named Same-Max Face-Slide Face Reverse Versus Integer Scale `k` On `B_16(0)`

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** one named nearest-neighbor hop-cost on the ℓ¹ ball `B_16(0)`,
scored only for the face-diagonal reverse comparison at every available
integer scale `k=1..8`.
**Audit-status authority:** independent audit lane only. This note authors
no audit verdict and predicts none.
**Primary runner:**
[`scripts/same_max_face_slide_face_reverse_vs_k_b16_2026_08_15.py`](../scripts/same_max_face_slide_face_reverse_vs_k_b16_2026_08_15.py)
**Cache:** none. `cache_write: false`.

## Result Up Front

Write `|σ_v|` for the number of nonzero coordinates of `v ∈ Z^3`. On a
directed nearest-neighbor hop `v → w` still inside `B_16(0)`, the stacked
rules `ν`, `μ`, `ρ3`, and `ω` are

`ν(v→w) = 3` if `|σ_v|=0` or `(|σ_v|=|σ_w|=1)` or `|σ_w| < |σ_v|`, else `1`;

`μ(v→w) = 3` if `ν` would be `3` or `(|σ_v|=|σ_w|=2` and the least nonzero
`|w_i|` equals `1)`, else `1`;

`ρ3(v→w) = 3` if `μ` would be `3` or `(|σ_v|=|σ_w|=3` and exactly two
`|w_i|` equal `1)`, else `1`;

`ω(v→w) = 3` if `ρ3` would be `3` or `(|σ_v|=|σ_w|=2` and
`max_i |w_i| > max_i |v_i|)`, else `1`.

The displayed same-max face-slide rule `ψ` is `ω` plus cost `3` on a
`2→2` hop whose destination has the same max absolute coordinate as the
source:

`ψ(v→w) = 3` if `ω` would be `3` or `(|σ_v|=|σ_w|=2` and
`max_i |w_i| = max_i |v_i|)`, else `1`.

Those clauses are the whole rule. Uniqueness is not claimed. This note is
the first display of face reverse under `ψ` at `k=1..8` on `B_16(0)`.

The parent out-face hop `(2,2,0) → (3,2,0)` still has `|σ|=2→2` and
`max |w_i|=3 > max |v_i|=2`, so `ω` already taxes it and `ψ=3`. The new
same-max clause is not leftover of `ω`: the interior face-slide hop
`(2,1,0) → (2,2,0)` has `|σ|=2→2` and `max |w_i|=2 = max |v_i|`, so
`ω = 1` while `ψ = 3`.

A pair `((2k,0,0),(k,k,0))` is available when both sites lie in `B_16(0)`.
That is `| (2k,0,0) |_1 = 2k ≤ 16` and `| (k,k,0) |_1 = 2k ≤ 16`, so every
`k=1..8` is available. No scale is omitted.

One Dijkstra from the origin on `B_16(0)` (6017 sites; 6016 nonzero) gives

`t(2,0,0) = 6`, `t(4,0,0) = 12`, `t(6,0,0) = 18`, `t(8,0,0) = 24`,
`t(10,0,0) = 26`, `t(12,0,0) = 28`, `t(14,0,0) = 32`, `t(16,0,0) = 38`,

`t(1,1,0) = 4`, `t(2,2,0) = 10`, `t(3,3,0) = 14`, `t(4,4,0) = 16`,
`t(5,5,0) = 18`, `t(6,6,0) = 20`, `t(7,7,0) = 22`, `t(8,8,0) = 26`.

For each available `k`, the displayed face-diagonal comparison is whether

`t(2k,0,0)^2 / (4k^2) > t(k,k,0)^2 / (2k^2)`,

equivalently `t(2k,0,0)^2 > 2 t(k,k,0)^2`. The bits are

| `k` | pair | axis `t^2/|v|_2^2` | face `t^2/|v|_2^2` | reverse |
|---|---|---|---|---|
| `1` | `((2,0,0),(1,1,0))` | `36/4=9` | `16/2=8` | yes |
| `2` | `((4,0,0),(2,2,0))` | `144/16=9` | `100/8=25/2` | no |
| `3` | `((6,0,0),(3,3,0))` | `324/36=9` | `196/18=98/9` | no |
| `4` | `((8,0,0),(4,4,0))` | `576/64=9` | `256/32=8` | yes |
| `5` | `((10,0,0),(5,5,0))` | `676/100=169/25` | `324/50=162/25` | yes |
| `6` | `((12,0,0),(6,6,0))` | `784/144=49/9` | `400/72=50/9` | no |
| `7` | `((14,0,0),(7,7,0))` | `1024/196=256/49` | `484/98=242/49` | yes |
| `8` | `((16,0,0),(8,8,0))` | `1444/256=361/64` | `676/128=169/32` | yes |

Exact integer comparisons `t(2k,0,0)^2 ? 2 t(k,k,0)^2`:

- `k=1`: `36 > 32` holds
- `k=2`: `144 > 200` fails
- `k=3`: `324 > 392` fails
- `k=4`: `576 > 512` holds
- `k=5`: `676 > 648` holds
- `k=6`: `784 > 800` fails
- `k=7`: `1024 > 968` holds
- `k=8`: `1444 > 1352` holds

The hold/fail pattern of the eight bits is yes, no, no, yes, yes, no, yes, yes.
Face reverse holds at `k=1`, `k=4`, `k=5`, `k=7`, and `k=8`, and fails at
`k=2`, `k=3`, and `k=6`.

A pure both-weights-`1` axis walk to `(2k,0,0)` costs `6k`. That walk
matches the Dijkstra arrival through `k=4`. From `k=5` the computed axis
arrival is strictly cheaper than `6k`. Those walks are witnesses, not a
uniqueness claim.

The sixteen arrivals are computed on `B_16(0)` under `ψ`, not copied from
a smaller-ball table and not copied from an `ω` pair table. The extra
same-max clause is live on this host: `(2,1,0) → (2,2,0)` lies in
`B_16(0)` and has `ψ = 3` while `ω = 1`. Under `ω` the face times on this
ball are `4,8,12,16,18,20,22,24` and reverse fails only at `k=6`. The
same-max addendum changes the face arrivals at `k=2`, `k=3`, and `k=8`.

The rule is displayed, not adopted. Do not write `ψ` into Admissibility.
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
none of the hop costs. The integers `3` and `1`, the support-size and
max-coordinate clauses, and the arrival function `t` are separately displayed
mathematical inputs. No axiom text is edited.

## Named Rule

Let `B_16(0) = { v ∈ Z^3 : |v|_1 ≤ 16 }`. Directed edges are the six
nearest-neighbor steps whose both ends lie in the ball. For `v ∈ B_16(0)`,
`t(v)` is the least sum of `ψ` along a directed path from `0` to `v` in
that graph.

The first `ν` clause is seed-exit. The second is both weights `1`. The third
is support drop. The `μ` addendum taxes a `2→2` hop whose destination still
touches a unit coordinate. The `ρ3` addendum taxes a `3→3` hop whose
destination has exactly two unit coordinates. The `ω` addendum taxes a
`2→2` hop that grows the coordinate box on a face. The `ψ` addendum taxes
a `2→2` hop that keeps the coordinate-box max (same-max face slide).

## Theorem 1 — Arrivals `t(2k,0,0)` And `t(k,k,0)` On `B_16(0)`

One origin Dijkstra on `B_16(0)` returns the integer arrivals

| site | `t_ψ` |
|---|---:|
| `(2,0,0)` | `6` |
| `(1,1,0)` | `4` |
| `(4,0,0)` | `12` |
| `(2,2,0)` | `10` |
| `(6,0,0)` | `18` |
| `(3,3,0)` | `14` |
| `(8,0,0)` | `24` |
| `(4,4,0)` | `16` |
| `(10,0,0)` | `26` |
| `(5,5,0)` | `18` |
| `(12,0,0)` | `28` |
| `(6,6,0)` | `20` |
| `(14,0,0)` | `32` |
| `(7,7,0)` | `22` |
| `(16,0,0)` | `38` |
| `(8,8,0)` | `26` |

Every listed site lies in `B_16(0)`. No `k=1..8` pair is omitted. The
sixteen values are computed on `B_16(0)`, not copied from a larger-ball
table and not copied from the `ω` pair table. These values are Dijkstra
outputs, not fitted scalars.

A witness walk to `(2,0,0)` is seed-exit `3` onto `(1,0,0)` and both-weights-`1`
axis hop `3` onto `(2,0,0)`, summing to `6`. A witness walk to `(1,1,0)` is
seed-exit `3` onto `(0,1,0)` and support-increase `1` onto `(1,1,0)`,
summing to `4`. A witness walk to `(2,2,0)` is seed-exit `3` onto
`(0,1,0)`, support-increase `1` onto `(1,1,0)`, hugging slide `3` onto
`(1,2,0)`, and same-max face slide `3` onto `(2,2,0)`, summing to `10`.
A witness walk to `(8,0,0)` is eight both-weights-`1` axis hops of cost
`3`, summing to `24`. Those walks are witnesses, not a uniqueness claim.

For each `k=1..8` the note also records whether

`t(2k,0,0)^2 / (4k^2) > t(k,k,0)^2 / (2k^2)`.

## Theorem 2 — Hold/Fail Pattern Of The Eight Bits

The Euclidean-normalized comparison at each available `k` is

`t(2k,0,0)^2 / (4k^2) > t(k,k,0)^2 / (2k^2)`,

equivalently `t(2k,0,0)^2 > 2 t(k,k,0)^2`. Substituting the computed times
gives the eight bits of Result Up Front. The hold/fail pattern is
yes, no, no, yes, yes, no, yes, yes. Reverse holds at `k=1`, `k=4`,
`k=5`, `k=7`, and `k=8`, and fails at `k=2`, `k=3`, and `k=6`. The
comparison is displayed, not adopted.

## Theorem 3 — Displayed, Not Adopted

The rule `ψ` is a displayed scoring device on `B_16(0)`. Do not write `ψ`
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
conditional_surface_status: "exact on B_16(0) for the displayed rule ψ at available k=1..8; no Admissibility edit; not attached to L1"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## What This Note Does Not Claim

- Uniqueness of `ψ` among hop-costs that score the face-versus-axis bits
  at any `k`.
- Any edit of Lattice, Qubit, Admissibility, or Record.
- Any attachment to L1.
- Any continuum potential, any inverse-power kernel, and any gravitational
  identification.
- Any statement off `B_16(0)`.
- Any score for a pair that is not an available face-versus-axis pair
  `((2k,0,0),(k,k,0))` at `k=1..8`.
- Any reuse of an `ω` arrival table as a substitute for the `ψ`
  Dijkstra.
- Any reuse of a larger-ball arrival table as a substitute for the
  radius-`16` Dijkstra.
- Any adoption of `ψ` as an admissibility rule. Face reverse versus `k`
  on this ball is a displayed comparison, not an adoption.
