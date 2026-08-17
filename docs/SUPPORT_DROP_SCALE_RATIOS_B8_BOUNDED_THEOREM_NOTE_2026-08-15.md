---
claim_id: support_drop_scale_ratios_b8_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Axis and body-diagonal arrival ratios under the named support-drop hop-cost on B_8(0) are reported for k=1..4. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/support_drop_scale_ratios_b8_2026_08_15.py
---

# Axis And Body-Diagonal Arrival Ratios Under Support-Drop On B_8(0)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** one named nearest-neighbor hop-cost on the ℓ¹ ball `B_8(0)`,
scored only for axis arrivals `t(k,0,0)` and body-diagonal arrivals
`t(k,k,k)` at `k=1,2,3,4` on sites that exist, and for the displayed
scale-ratio reverse test at each available `k`.
**Audit-status authority:** independent audit lane only. This note authors
no audit verdict and predicts none.
**Primary runner:**
[`scripts/support_drop_scale_ratios_b8_2026_08_15.py`](../scripts/support_drop_scale_ratios_b8_2026_08_15.py)
**Cache:** none. `cache_write: false`.

## Result Up Front

Axis and body-diagonal arrival ratios under the named support-drop hop-cost on B_8(0) are reported for k=1..4. Displayed, not adopted.

The same named support-drop hop-cost `ν` already scored for the single
pair `(4,0,0)` versus `(2,2,2)` is scored independently at every integer
scale `k=1,2,3,4` whose sites lie in `B_8(0)`. The table is not leftover of that one pair:
both available same-`k` pairs reverse, and the
body-diagonal sites at `k=3,4` are omitted because they lie outside the
ball.

Write `|σ_v|` for the number of nonzero coordinates of `v ∈ Z^3`. On a
directed nearest-neighbor hop `v → w` still inside `B_8(0)`, the displayed
rule `ν` is

`ν(v→w) = 3` if `|σ_v|=0` or `(|σ_v|=|σ_w|=1)` or `|σ_w| < |σ_v|`,
else `1`.

The first clause is seed-exit. The second is both weights `1`. The third is
support drop. Those three clauses are the whole rule. Uniqueness is not claimed.

One Dijkstra from the origin on `B_8(0)` (833 sites; 832 nonzero) gives

`t(1,0,0) = 3`, `t(1,1,1) = 5`,
`t(2,0,0) = 6`, `t(2,2,2) = 8`,
`t(3,0,0) = 9`, `t(4,0,0) = 10`.

The sites `(3,3,3)` and `(4,4,4)` have ℓ¹ norms `9` and `12`, so they are
outside `B_8(0)` and are omitted.

The Euclidean-normalized axis and body-diagonal ratios are

`t(k,0,0)/k` and `t(k,k,k)/(k√3)`

for those sites that exist. Their squares are `t(k,0,0)^2 / k^2` and
`t(k,k,k)^2 / (3k^2)`. Reverse at scale `k` means the first square is
strictly larger. That holds at both available scales:

`9 > 25/3` at `k=1`, and `9 > 16/3` at `k=2`.

The ratio gap stays open. It is not the leftover of one pair.

The rule is displayed, not adopted. Do not write `ν` into Admissibility.
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

Let `B_8(0) = { v ∈ Z^3 : |v|_1 ≤ 8 }`. Directed edges are the six
nearest-neighbor steps whose both ends lie in the ball. For `v ∈ B_8(0)`,
`t(v)` is the least sum of `ν` along a directed path from `0` to `v` in
that graph.

A site `(k,0,0)` lies in the ball for every `k=1,2,3,4`. A site `(k,k,k)`
lies in the ball if and only if `3k ≤ 8`, so only `k=1` and `k=2`.

## Theorem 1 — Arrival Table At Scales `k=1,2,3,4`

One origin Dijkstra on `B_8(0)` returns the integer arrivals below. A
blank cell means the site is outside the ball and is omitted.

| `k` | `t(k,0,0)` | `t(k,0,0)/k` | `t(k,k,k)` | `t(k,k,k)/(k√3)` |
|---|---:|---:|---:|---:|
| `1` | `3` | `3` | `5` | `5/√3` |
| `2` | `6` | `3` | `8` | `4/√3` |
| `3` | `9` | `3` | omitted | omitted |
| `4` | `10` | `5/2` | omitted | omitted |

Witnessing paths of those `ν`-costs exist. The walk `0 → (1,0,0)` has hop
cost `3`. The walk

`0 → (1,0,0) → (1,1,0) → (1,1,1)`

has hop-costs `3,1,1` and sum `5`. The walk

`0 → (1,0,0) → (2,0,0)`

has hop-costs `3,3` and sum `6`. The walk

`0 → (1,0,0) → (1,1,0) → (1,1,1) → (2,1,1) → (2,2,1) → (2,2,2)`

has hop-costs `3,1,1,1,1,1` and sum `8`. The walk

`0 → (1,0,0) → (2,0,0) → (3,0,0)`

has hop-costs `3,3,3` and sum `9`. The walk

`0 → (1,0,0) → (1,1,0) → (2,1,0) → (3,1,0) → (4,1,0) → (4,0,0)`

has hop-costs `3,1,1,1,1,3` and sum `10`.

## Theorem 2 — Reverse At Each Available Scale

For each available `k`, reverse means

`t(k,0,0)^2 / k^2 > t(k,k,k)^2 / (3k^2)`,

equivalently `3 t(k,0,0)^2 > t(k,k,k)^2`. Displayed, not adopted.

| `k` | `t(k,0,0)^2 / k^2` | `t(k,k,k)^2 / (3k^2)` | reverse |
|---|---:|---:|---|
| `1` | `9` | `25/3` | yes (`27 > 25`) |
| `2` | `9` | `16/3` | yes (`108 > 64`) |
| `3` | `9` | omitted | omitted |
| `4` | `25/4` | omitted | omitted |

Both available same-`k` comparisons reverse. The ratio gap stays open
across the two scales that exist on `B_8(0)`. The `(4,0,0)` versus
`(2,2,2)` diamond is a mixed-scale pair; it is not a substitute for this
same-`k` table.

## Theorem 3 — Displayed, Not Adopted

The rule `ν` is a displayed scoring device on `B_8(0)`. Do not write `ν`
into Admissibility. Do not attach L1. It is not a replacement for
unit-cost first arrival, and it is not offered as the unique hop-cost with
a same-`k` ratio gap.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact integer arrivals and same-k axis versus body-diagonal ratio reverse on the finite ball B_8(0) for one named hop-cost. The rule is displayed, not adopted."
trace_class: frontier_discovery
artifact_role: theorem
conditional_surface_status: "exact on B_8(0) for the displayed rule ν; no Admissibility edit; not attached to L1"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## What This Note Does Not Claim

- Uniqueness of `ν` among hop-costs that reverse same-`k` ratios.
- Any edit of Lattice, Qubit, Admissibility, or Record.
- Any attachment to L1.
- Any continuum potential, any inverse-power kernel, and any gravitational
  identification.
- Any statement off `B_8(0)`.
- Any reuse of a single mixed-scale pair as a substitute for the
  `k=1..4` table.
- Any write of `ν` into Admissibility.
