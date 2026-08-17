---
claim_id: clause_011_samek_k6_b18_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Same-k reverse at k=6 under the named (0,1,1) hop-cost on B_18(0) is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/clause_011_samek_k6_b18_2026_08_15.py
---

# Named (0,1,1) Same-k Reverse At k=6 On B_18(0)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact same-`k` axis versus body-diagonal arrival comparison at
`k=6` under one named hop-cost on the finite 18-hop neighborhood of the
origin in the cubic nearest-neighbor graph. The rule is displayed, not
adopted.
**Audit-status authority:** independent audit lane only. This note authors
no audit verdict and predicts none.
**Primary runner:**
[`scripts/clause_011_samek_k6_b18_2026_08_15.py`](../scripts/clause_011_samek_k6_b18_2026_08_15.py)
**Cache:** none. `cache_write: false`.

## Result Up Front

Let `B_18(0)` be the set of sites of `Z^3` whose nearest-neighbor graph
distance from the origin is at most 18. That set has 8473 sites and is
used only as a finite domain bound. It is not a hop-cost. The body-
diagonal site `(6,6,6)` has nearest-neighbor graph distance 18, so it is
absent from `B_16(0)` and sits on the boundary of `B_18(0)`.

Hops are the six nearest-neighbor steps that remain inside `B_18(0)`.
Write `|σ_v|` for the support of a site (the number of nonzero
coordinates). The named clause-toggle `(0,1,1)` assigns

```text
cost(v→w) = 3  if |σ_v|=|σ_w|=1 or |σ_w|<|σ_v|,
          = 1  otherwise.
```

Seed-exit therefore costs 1. Axis 1-skeleton hops and support-drop hops
cost 3. Every other admitted hop costs 1. The rule is cheaper at
seed-exit than a rule that prices seed-exit at 3. The rule is not
written into Admissibility: do not write (0,1,1) into Admissibility.
Do not attach L1. Uniqueness is not required.

One Dijkstra from the origin yields the same-`k` arrivals at `k=6`

| `k` | `t(k,0,0)` | `t(k,k,k)` | `t(k,0,0)^2 / k^2` | `t(k,k,k)^2 / (3k^2)` | reverse |
|---|---:|---:|---:|---:|---|
| `6` | `10` | `18` | `100/36` | `324/108` | no |

The displayed test

`t(6,0,0)^2 / 36 > t(6,6,6)^2 / 108`

fails. Equivalently `3 t(6,0,0)^2 > t(6,6,6)^2` is `300 > 324`, which
is false. Same-`k` reverse therefore does not hold at `k=6` under the
named cheaper rival on `B_18(0)`. The earlier same-`k` table on
`B_16(0)` already failed at `k=1` and held at `k=2..5`; enlarging the
domain to include `(6,6,6)` does not restore reverse at this next
scale. The table is same-`k`; it is not the doubled pairing
`(4,0,0)` versus `(2,2,2)` and `(8,0,0)` versus `(4,4,4)`. Displayed,
not adopted.

## Current Premise Boundary

The Lattice and Admissibility premises are quoted from
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md):

Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
adjacency, standard translations, and proper cubic rotations about each site.

There is one fixed nearest-neighbor admissibility rule, covariant under
lattice translations and proper cubic rotations.

The axiom set supplies the cubic nearest-neighbor graph. It does not
supply a hop-cost, a same-`k` reverse test, or a preferred
clause-toggle. This note therefore treats `(0,1,1)` as a separately
named finite scoring rule. The note does not write `(0,1,1)` into
Admissibility and does not enlarge the axiom set.

Record is not used. No readout, formation site, or scalar collection
functional enters the arrival times.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Two same-k arrival times and one displayed reverse inequality are exact outputs of one Dijkstra on the named finite graph; the hop-cost is a disclosed scoring rule, not an axiom, and same-k reverse fails at k=6."
trace_class: compute
artifact_role: theorem
conditional_surface_status: "exact on B_18(0) under the named (0,1,1) hop-cost at k=6; displayed, not adopted"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

`B_18(0)` is the closed 18-hop neighborhood of the origin. Every hop
used below is a nearest-neighbor step whose endpoints both lie in that
set. The site `(6,6,6)` has nearest-neighbor graph distance 18, so it
lies on the ball. One Dijkstra computes the named arrival time `t(v)`
from the origin to each site.

The displayed inequality compares the axis and body-diagonal sites that
share the scale `k=6`, after Euclidean length `6` on the axis and
`6√3` on the body diagonal. The comparison is displayed only. It is
not a derived continuum law and is not attached as an L1 hop-cost.

## Theorem 1

On `B_18(0)` under the named `(0,1,1)` hop-cost,

`t(6,0,0)=10` and `t(6,6,6)=18`.

Each value is the Dijkstra arrival time. The axis value `10` is
strictly smaller than the axis-skeleton sum `1+3+3+3+3+3=16`, so a
support-raising detour is cheaper than staying on the axis. The body-
diagonal value equals the nearest-neighbor hop count `18`, because a
monotone support-nondecreasing path from the origin uses only cost-1
hops and remains inside `B_18(0)`.

## Theorem 2

The displayed same-`k` test at `k=6` is

`t(6,0,0)^2 / 36  ?  t(6,6,6)^2 / 108`,

equivalently `3 t(6,0,0)^2 ? t(6,6,6)^2`. Substituting the computed
times gives `100/36` versus `324/108`, or `300 > 324`, which is false.

Same-`k` reverse therefore fails at `k=6` on this finite domain. The
cheaper rival does not keep same-`k` reverse at this scale. Displayed,
not adopted.

## Theorem 3

The note does not write `(0,1,1)` into Admissibility. Do not attach L1.
Uniqueness is not required. The current axiom memo is not edited.

## What This Does Not Claim

- It does not adopt the `(0,1,1)` hop-cost as framework content.
- It does not claim that same-`k` reverse holds at `k=6`.
- It does not claim that the named rule is the only reverser.
- It does not identify `t` with nearest-neighbor hop count on the axis.
- It does not replace the doubled pairing
  `(4,0,0)`/`(2,2,2)` and `(8,0,0)`/`(4,4,4)` by this same-`k` pair.
- It does not score the separately named support-drop rule.
- It does not supply a physical clock, a continuum metric, or a Record
  readout of the arrival times.

## Reproducibility

```text
python3 scripts/clause_011_samek_k6_b18_2026_08_15.py
```

The runner prints the two times, the displayed comparison, and
`TOTAL: PASS=<n> FAIL=<n>`.
