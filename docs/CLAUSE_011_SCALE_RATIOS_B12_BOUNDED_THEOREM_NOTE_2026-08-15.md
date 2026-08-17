---
claim_id: clause_011_scale_ratios_b12_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Axis and body-diagonal arrival ratios under the named (0,1,1) hop-cost on B_12(0) are reported for k=1..4. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/clause_011_scale_ratios_b12_2026_08_15.py
---

# Named (0,1,1) Same-k Axis And Body Ratios On B_12(0)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact same-`k` axis versus body-diagonal arrival ratios under
one named hop-cost on the finite 12-hop neighborhood of the origin in
the cubic nearest-neighbor graph. The rule is displayed, not adopted.
**Audit-status authority:** independent audit lane only. This note authors
no audit verdict and predicts none.
**Primary runner:**
[`scripts/clause_011_scale_ratios_b12_2026_08_15.py`](../scripts/clause_011_scale_ratios_b12_2026_08_15.py)
**Cache:** none. `cache_write: false`.

## Result Up Front

Let `B_12(0)` be the set of sites of `Z^3` whose nearest-neighbor graph
distance from the origin is at most 12. That set has 2625 sites and is
used only as a finite domain bound. It is not a hop-cost.

Hops are the six nearest-neighbor steps that remain inside `B_12(0)`.
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

One Dijkstra from the origin yields the same-`k` arrivals

| `k` | `t(k,0,0)` | `t(k,k,k)` | `t(k,0,0)^2 / k^2` | `t(k,k,k)^2 / (3k^2)` | reverse |
|---|---:|---:|---:|---:|---|
| `1` | `1` | `3` | `1` | `3` | no |
| `2` | `4` | `6` | `4` | `3` | yes |
| `3` | `7` | `9` | `49/9` | `3` | yes |
| `4` | `8` | `12` | `4` | `3` | yes |

For `k=1` the displayed test

`t(1,0,0)^2 / 1^2 > t(1,1,1)^2 / (3·1^2)`

fails. For each of `k=2,3,4` the same-`k` reverse holds. The cheaper
rival therefore does not keep same-`k` reverse at every listed scale.
The table is same-`k`; it is not the doubled pairing
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
claim_type_reason: "Eight same-k arrival times and four displayed reverse inequalities are exact outputs of one Dijkstra on the named finite graph; the hop-cost is a disclosed scoring rule, not an axiom, and same-k reverse fails at k=1."
trace_class: compute
artifact_role: theorem
conditional_surface_status: "exact on B_12(0) under the named (0,1,1) hop-cost at k=1..4; displayed, not adopted"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

`B_12(0)` is the closed 12-hop neighborhood of the origin. Every hop
used below is a nearest-neighbor step whose endpoints both lie in that
set. One Dijkstra computes the named arrival time `t(v)` from the
origin to each site.

The four displayed inequalities compare axis and body-diagonal sites
that share the same scale `k`, after Euclidean length `k` on the axis
and `k√3` on the body diagonal. The comparison is displayed only. It is
not a derived continuum law and is not attached as an L1 hop-cost.

## Theorem 1

On `B_12(0)` under the named `(0,1,1)` hop-cost,

`t(1,0,0)=1`, `t(1,1,1)=3`,
`t(2,0,0)=4`, `t(2,2,2)=6`,
`t(3,0,0)=7`, `t(3,3,3)=9`,
`t(4,0,0)=8`, and `t(4,4,4)=12`.

Each value is the Dijkstra arrival time. The `k=1` axis value equals
the seed-exit cost 1. The `k=2` and `k=3` axis values equal the
axis-skeleton sums `1+3` and `1+3+3`. The `k=4` axis value `8` is
strictly smaller than the axis-skeleton sum `1+3+3+3=10`, so a
support-raising detour is cheaper than staying on the axis. Each
body-diagonal value equals the nearest-neighbor hop count `3k`, because
a monotone support-nondecreasing path from the origin uses only cost-1
hops.

## Theorem 2

The displayed same-`k` test is

`t(k,0,0)^2 / k^2  ?  t(k,k,k)^2 / (3k^2)`,

equivalently `3 t(k,0,0)^2 ? t(k,k,k)^2`. Substituting the computed
times gives

| `k` | `3 t(k,0,0)^2` | `t(k,k,k)^2` | reverse |
|---|---:|---:|---|
| `1` | `3` | `9` | `3 > 9` is false |
| `2` | `48` | `36` | `48 > 36` |
| `3` | `147` | `81` | `147 > 81` |
| `4` | `192` | `144` | `192 > 144` |

Same-`k` reverse therefore fails at `k=1` and holds at `k=2,3,4` on
this same finite domain. The cheaper rival does not keep same-`k`
reverse at every `k=1..4`. Displayed, not adopted.

## Theorem 3

The note does not write `(0,1,1)` into Admissibility. Do not attach L1.
Uniqueness is not required. The current axiom memo is not edited.

## What This Does Not Claim

- It does not adopt the `(0,1,1)` hop-cost as framework content.
- It does not claim that same-`k` reverse holds at every listed scale.
- It does not claim that the named rule is the only reverser.
- It does not identify `t` with nearest-neighbor hop count on the axis.
- It does not replace the doubled pairing
  `(4,0,0)`/`(2,2,2)` and `(8,0,0)`/`(4,4,4)` by this same-`k` table.
- It does not supply a physical clock, a continuum metric, or a Record
  readout of the arrival times.

## Reproducibility

```text
python3 scripts/clause_011_scale_ratios_b12_2026_08_15.py
```

The runner prints the eight times, the four displayed comparisons, and
`TOTAL: PASS=<n> FAIL=<n>`.
