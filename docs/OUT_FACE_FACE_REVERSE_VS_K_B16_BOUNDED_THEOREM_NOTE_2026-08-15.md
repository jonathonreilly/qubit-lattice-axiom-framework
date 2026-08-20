---
claim_id: out_face_face_reverse_vs_k_b16_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Face-diagonal reverse versus integer scale k under the named out-face hop-cost on B_16(0) is reported for available k=1..8. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/out_face_face_reverse_vs_k_b16_2026_08_15.py
---

# Named Out-Face Face Reverse Versus Integer Scale k On B_16(0)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** one named nearest-neighbor hop-cost on the ℓ¹ ball `B_16(0)`,
scored only for the face-diagonal reverse comparison at every available
integer scale `k=1..8`.
**Audit-status authority:** independent audit lane only. This note authors
no audit verdict and predicts none.
**Primary runner:**
[`scripts/out_face_face_reverse_vs_k_b16_2026_08_15.py`](../scripts/out_face_face_reverse_vs_k_b16_2026_08_15.py)
**Cache:** none. `cache_write: false`.

## Result Up Front

The named out-face hop-cost `ω` is the already scored ridge-slide rule
`ρ3` plus cost `3` on a `2→2` hop whose destination has strictly larger
max absolute coordinate than the source (growing the coordinate box on a
face). The residual scored here is the face-versus-axis bit at each
available integer scale `k=1..8` on `B_16(0)`. Uniqueness is not claimed.

Write `|σ_v|` for the number of nonzero coordinates of `v ∈ Z^3`. On a
directed nearest-neighbor hop `v → w` still inside `B_16(0)`, the displayed
comparator `ν` is

`ν(v→w) = 3` if `|σ_v|=0` or `(|σ_v|=|σ_w|=1)` or `|σ_w| < |σ_v|`,
else `1`.

The displayed corridor-slide rule `μ` is

`μ(v→w) = 3` if `ν(v→w)` would be `3` or `(|σ_v|=|σ_w|=2` and the least
nonzero `|w_i|` equals `1)`, else `1`.

The displayed ridge-slide rule `ρ3` is

`ρ3(v→w) = 3` if `μ(v→w)` would be `3` or `(|σ_v|=|σ_w|=3` and exactly
two `|w_i|` equal `1)`, else `1`.

The displayed rule `ω` is

`ω(v→w) = 3` if `ρ3(v→w)` would be `3` or `(|σ_v|=|σ_w|=2` and
`max_i |w_i| > max_i |v_i|)`, else `1`.

The first three clauses are those of `ν`: seed-exit, both weights `1`, and
support drop. The fourth is the axis-hugging `2→2` slide of `μ`. The fifth
is the ridge `3→3` slide of `ρ3`. The sixth is the growing-box face slide.
Those six clauses are the whole rule.

A pair `((2k,0,0),(k,k,0))` is available when both sites lie in `B_16(0)`.
That is `| (2k,0,0) |_1 = 2k ≤ 16` and `| (k,k,0) |_1 = 2k ≤ 16`, so every
`k=1..8` is available. No scale is omitted.

One Dijkstra from the origin on `B_16(0)` (6017 sites; 6016 nonzero) gives

`t(2,0,0) = 6`, `t(4,0,0) = 12`, `t(6,0,0) = 18`, `t(8,0,0) = 24`,
`t(10,0,0) = 26`, `t(12,0,0) = 28`, `t(14,0,0) = 32`, `t(16,0,0) = 38`,

`t(1,1,0) = 4`, `t(2,2,0) = 8`, `t(3,3,0) = 12`, `t(4,4,0) = 16`,
`t(5,5,0) = 18`, `t(6,6,0) = 20`, `t(7,7,0) = 22`, `t(8,8,0) = 24`.

For each available `k`, the displayed face-diagonal comparison is whether

`t(2k,0,0)^2 / (4k^2) > t(k,k,0)^2 / (2k^2)`,

equivalently `t(2k,0,0)^2 > 2 t(k,k,0)^2`. The bits are

| `k` | pair | axis `t^2/|v|_2^2` | face `t^2/|v|_2^2` | reverse |
|---|---|---|---|---|
| `1` | `((2,0,0),(1,1,0))` | `36/4=9` | `16/2=8` | yes |
| `2` | `((4,0,0),(2,2,0))` | `144/16=9` | `64/8=8` | yes |
| `3` | `((6,0,0),(3,3,0))` | `324/36=9` | `144/18=8` | yes |
| `4` | `((8,0,0),(4,4,0))` | `576/64=9` | `256/32=8` | yes |
| `5` | `((10,0,0),(5,5,0))` | `676/100=169/25` | `324/50=162/25` | yes |
| `6` | `((12,0,0),(6,6,0))` | `784/144=49/9` | `400/72=50/9` | no |
| `7` | `((14,0,0),(7,7,0))` | `1024/196=256/49` | `484/98=242/49` | yes |
| `8` | `((16,0,0),(8,8,0))` | `1444/256=361/64` | `576/128=9/2` | yes |

Exact integer comparisons `t(2k,0,0)^2 ? 2 t(k,k,0)^2`:

- `k=1`: `36 > 32` holds
- `k=2`: `144 > 128` holds
- `k=3`: `324 > 288` holds
- `k=4`: `576 > 512` holds
- `k=5`: `676 > 648` holds
- `k=6`: `784 > 800` fails
- `k=7`: `1024 > 968` holds
- `k=8`: `1444 > 1152` holds

Reverse holds at `k=1,2,3,4,5,7,8` and fails at `k=6`. The `k=6` is the
only fail. The score is not leftover of the `μ` face-versus-`k` table on
the same ball: under `μ` the axis times are `6,12,16,18,20,22,24,30` and
the face times are `4,8,10,12,14,16,18,20`, so `μ` fails at `k=6` and at
`k=7`. Nor is it leftover of `ρ3`: under `ρ3` the axis times are
`6,12,18,20,22,24,26,32` and the face times are `4,8,10,12,14,16,18,20`,
so every `ρ3` bit on this ball holds, including `k=6`. The extra out-face
clause is what changes the arrivals. On the growing-box hop
`(2,2,0) → (2,3,0)` one has `|σ| : 2 → 2` and `max |w_i|=3 > max |v_i|=2`,
while the least nonzero `|w_i|` is `2`, so `ν = μ = ρ3 = 1` while `ω = 3`.
Therefore `ρ3` cannot price the growing-box face slide. Independently, the
axis endpoint of this ball is `t(16,0,0) = 38`. The only in-ball neighbor
of `(16,0,0)` is `(15,0,0)`, so the last hop is the both-weights-`1` axis
step of cost `3`.

The rule is displayed, not adopted. Do not write `ω` into Admissibility.
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
the max-absolute-coordinate test, and the arrival function `t` are
separately displayed mathematical inputs. No axiom text is edited.

## Named Rule

Let `B_16(0) = { v ∈ Z^3 : |v|_1 ≤ 16 }`. Directed edges are the six
nearest-neighbor steps whose both ends lie in the ball. For `v ∈ B_16(0)`,
`t(v)` is the least sum of `ω` along a directed path from `0` to `v` in
that graph.

The comparator `ρ3` uses only the first five clauses of `ω`. On the
growing-box slide `(2,2,0) → (2,3,0)` one has `|σ| : 2 → 2` and
`max |w_i| > max |v_i|`, with least nonzero `|w_i| = 2`, so `ρ3 = 1`
while `ω = 3`. Therefore `ρ3` cannot price the growing-box face slide,
and the `ω` scores below are not a leftover of `ρ3`.

## Theorem 1 — Arrivals `t(2k,0,0)` And `t(k,k,0)` On `B_16(0)`

One origin Dijkstra on `B_16(0)` returns the integer arrivals

| site | `t_ω` |
|---|---:|
| `(2,0,0)` | `6` |
| `(1,1,0)` | `4` |
| `(4,0,0)` | `12` |
| `(2,2,0)` | `8` |
| `(6,0,0)` | `18` |
| `(3,3,0)` | `12` |
| `(8,0,0)` | `24` |
| `(4,4,0)` | `16` |
| `(10,0,0)` | `26` |
| `(5,5,0)` | `18` |
| `(12,0,0)` | `28` |
| `(6,6,0)` | `20` |
| `(14,0,0)` | `32` |
| `(7,7,0)` | `22` |
| `(16,0,0)` | `38` |
| `(8,8,0)` | `24` |

Every listed site lies in `B_16(0)`. No `k=1..8` pair is omitted. The
sixteen values are computed on `B_16(0)`, not copied from a larger-ball
table and not copied from the `μ` or `ρ3` pair tables. These values are
Dijkstra outputs, not fitted scalars.

A witness walk to `(2,0,0)` is seed-exit `3` onto `(1,0,0)` and
both-weights-`1` axis hop `3` onto `(2,0,0)`, summing to `6`. A witness
walk to `(1,1,0)` is seed-exit `3` onto `(0,1,0)` and body `1→2` of cost
`1` onto `(1,1,0)`, summing to `4`. A witness walk to `(6,0,0)` is six
axis hops of cost `3` from the origin through `(1,0,0)` to `(6,0,0)`,
summing to `18`. A witness walk to `(3,3,0)` is seed-exit `3` onto
`(0,1,0)`, body `1` onto `(1,1,0)`, hugging or out-face slide `3` onto
`(1,2,0)`, face hop `1` onto `(2,2,0)`, growing-box out-face slide `3`
onto `(2,3,0)`, and face hop `1` onto `(3,3,0)`, summing to `12`. Those
walks are witnesses, not a uniqueness claim.

## Theorem 2 — Face Reverse Versus Available Integer Scale `k`

The Euclidean-normalized comparison at each available `k` is

`t(2k,0,0)^2 / (4k^2) > t(k,k,0)^2 / (2k^2)`,

equivalently `t(2k,0,0)^2 > 2 t(k,k,0)^2`. Substituting the computed times
gives the eight bits of Result Up Front. In particular the `k=6`
comparison is `784/144` versus `400/72`, or `784 > 800`, so `k=6` fails,
and `k=6` is the only fail.

Arrival per Euclidean length is larger at `(2k,0,0)` than at `(k,k,0)` for
`k=1,2,3,4,5,7,8` and is not larger for `k=6`. The comparison is
displayed, not adopted.

## Theorem 3 — Displayed, Not Adopted

The rule `ω` is a displayed scoring device on `B_16(0)`. Do not write `ω`
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
conditional_surface_status: "exact on B_16(0) for the displayed rule ω at available k=1..8; no Admissibility edit; not attached to L1"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## What This Note Does Not Claim

- Uniqueness of `ω` among hop-costs that score the face-versus-axis bits
  at any `k`.
- Any edit of Lattice, Qubit, Admissibility, or Record.
- Any attachment to L1.
- Any continuum potential, any inverse-power kernel, and any gravitational
  identification.
- Any statement off `B_16(0)`.
- Any score for a pair that is not an available face-versus-axis pair
  `((2k,0,0),(k,k,0))` at `k=1..8`.
- Any reuse of a `μ` or `ρ3` arrival table as a substitute for the `ω`
  Dijkstra.
- Any adoption of the displayed reverse bits as a physical law.
