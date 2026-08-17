---
claim_id: clause_011_body_reverse_vs_k_b16_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Body-diagonal reverse versus integer scale k under the named (0,1,1) hop-cost on B_16(0) is reported for k=1..5. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/clause_011_body_reverse_vs_k_b16_2026_08_15.py
---

# Named (0,1,1) Body-Diagonal Reverse Versus Scale k On B_16(0)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact arrival times under one named hop-cost on the finite
16-hop neighborhood of the origin in the cubic nearest-neighbor graph,
scored only for the face-orthogonal body census pairing
`((2k,0,0),(k,k,k))` at every integer `k=1,2,3,4,5`. The rule is
displayed, not adopted.
**Primary runner:**
[`scripts/clause_011_body_reverse_vs_k_b16_2026_08_15.py`](../scripts/clause_011_body_reverse_vs_k_b16_2026_08_15.py)
**Cache:** none. `cache_write: false`.

## Result Up Front

Let `B_16(0)` be the set of sites of `Z^3` whose nearest-neighbor graph
distance from the origin is at most 16. That set has 6017 sites and is
used only as a finite domain bound. It is not a hop-cost.

Hops are the six nearest-neighbor steps that remain inside `B_16(0)`.
Write `σ_v` for the support of a site (the set of nonzero coordinates).
The named clause-toggle `(0,1,1)` assigns

```text
cost(v→w) = 3  if |σ_v|=|σ_w|=1 or |σ_w|<|σ_v|,
          = 1  otherwise.
```

Seed-exit therefore costs 1. Axis 1-skeleton hops and support-drop hops
cost 3. Every other admitted hop costs 1. The rule is not written into
Admissibility: do not write (0,1,1) into Admissibility. Do not attach L1.

One Dijkstra from the origin yields the body-census arrivals

| `k` | site axis | `t(2k,0,0)` | site body | `t(k,k,k)` | `12 t(2k,0,0)^2` | `16 t(k,k,k)^2` | reverse |
|---|---|---:|---|---:|---:|---:|---|
| `1` | `(2,0,0)` | `4` | `(1,1,1)` | `3` | `192` | `144` | yes |
| `2` | `(4,0,0)` | `8` | `(2,2,2)` | `6` | `768` | `576` | yes |
| `3` | `(6,0,0)` | `10` | `(3,3,3)` | `9` | `1200` | `1296` | no |
| `4` | `(8,0,0)` | `12` | `(4,4,4)` | `12` | `1728` | `2304` | no |
| `5` | `(10,0,0)` | `14` | `(5,5,5)` | `15` | `2352` | `3600` | no |

```text
t(2,0,0)=4
t(1,1,1)=3
t(4,0,0)=8
t(2,2,2)=6
t(6,0,0)=10
t(3,3,3)=9
t(8,0,0)=12
t(4,4,4)=12
t(10,0,0)=14
t(5,5,5)=15
```

The displayed reverse tests are

```text
12 t(2,0,0)^2 = 192 > 144 = 16 t(1,1,1)^2     yes
12 t(4,0,0)^2 = 768 > 576 = 16 t(2,2,2)^2     yes
12 t(6,0,0)^2 = 1200 > 1296 = 16 t(3,3,3)^2   no
12 t(8,0,0)^2 = 1728 > 2304 = 16 t(4,4,4)^2   no
12 t(10,0,0)^2 = 2352 > 3600 = 16 t(5,5,5)^2  no
```

Body-diagonal reverse holds at `k=1,2` and fails at `k=3,4,5`. The
`k=5` row is an additional scale on `B_16(0)`, not leftover of the
smaller pairings. Uniqueness is not required. Displayed, not adopted.

## Current Premise Boundary

The Lattice and Admissibility premises are quoted from
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md):

Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
adjacency, standard translations, and proper cubic rotations about each site.

There is one fixed nearest-neighbor admissibility rule, covariant under
lattice translations and proper cubic rotations.

The axiom set supplies the cubic nearest-neighbor graph. It does not
supply a hop-cost, a body-diagonal reverse test, or a preferred
clause-toggle. This note therefore treats `(0,1,1)` as a separately
named finite scoring rule. The note does not write `(0,1,1)` into
Admissibility and does not enlarge the axiom set.

Record is not used. No readout, formation site, or scalar collection
functional enters the arrival times.

## Exact Objects

`B_16(0)` is the closed 16-hop neighborhood of the origin. Every hop
used below is a nearest-neighbor step whose endpoints both lie in that
set. One Dijkstra computes the named arrival time `t(v)` from the
origin to each site.

The pairing is not the same-`k` axis / body pair `(k,0,0)` versus
`(k,k,k)`. It is the face-orthogonal body census
`((2k,0,0),(k,k,k))`. The comparison is displayed only. It is not a
derived continuum law and is not attached as an L1 hop-cost.

## Theorem 1

On `B_16(0)` under the named `(0,1,1)` hop-cost, one origin Dijkstra
returns

`t(2,0,0)=4`, `t(1,1,1)=3`, `t(4,0,0)=8`, `t(2,2,2)=6`,
`t(6,0,0)=10`, `t(3,3,3)=9`, `t(8,0,0)=12`, `t(4,4,4)=12`,
`t(10,0,0)=14`, and `t(5,5,5)=15`.

Each value is the Dijkstra arrival time. Witnessing paths of those
costs exist. The walk

`0 → (1,0,0) → (2,0,0)`

has hop-costs `1,3` and sum `4`. The walk

`0 → (1,0,0) → (1,1,0) → (1,1,1)`

has hop-costs `1,1,1` and sum `3`. The walk

`0 → (1,0,0) → (1,1,0) → (2,1,0) → (3,1,0) → (4,1,0) → (4,0,0)`

has hop-costs `1,1,1,1,1,3` and sum `8`. The walk

`0 → (1,0,0) → (1,1,0) → (1,1,1) → (2,1,1) → (2,2,1) → (2,2,2)`

has hop-costs `1,1,1,1,1,1` and sum `6`. The walk

`0 → (1,0,0) → (1,1,0) → (2,1,0) → (3,1,0) → (4,1,0) → (5,1,0) → (6,1,0) → (6,0,0)`

has hop-costs `1,1,1,1,1,1,1,3` and sum `10`. The walk

`0 → (1,0,0) → (1,1,0) → (1,1,1) → (2,1,1) → (2,2,1) → (2,2,2) → (3,2,2) → (3,3,2) → (3,3,3)`

has hop-costs `1,1,1,1,1,1,1,1,1` and sum `9`. The walk

`0 → (1,0,0) → (1,1,0) → (2,1,0) → (3,1,0) → (4,1,0) → (5,1,0) → (6,1,0) → (7,1,0) → (8,1,0) → (8,0,0)`

has hop-costs `1,1,1,1,1,1,1,1,1,3` and sum `12`. The walk

`0 → (1,0,0) → (1,1,0) → (1,1,1) → (2,1,1) → (2,2,1) → (2,2,2) → (3,2,2) → (3,3,2) → (3,3,3) → (4,3,3) → (4,4,3) → (4,4,4)`

has hop-costs `1,1,1,1,1,1,1,1,1,1,1,1` and sum `12`. The walk

`0 → (1,0,0) → (1,1,0) → (2,1,0) → (3,1,0) → (4,1,0) → (5,1,0) → (6,1,0) → (7,1,0) → (8,1,0) → (9,1,0) → (10,1,0) → (10,0,0)`

has hop-costs `1,1,1,1,1,1,1,1,1,1,1,3` and sum `14`. The walk

`0 → (1,0,0) → (1,1,0) → (1,1,1) → (2,1,1) → (2,2,1) → (2,2,2) → (3,2,2) → (3,3,2) → (3,3,3) → (4,3,3) → (4,4,3) → (4,4,4) → (5,4,4) → (5,5,4) → (5,5,5)`

has hop-costs `1,1,1,1,1,1,1,1,1,1,1,1,1,1,1` and sum `15`.

The table is computed on `B_16(0)`, not copied from four named pairs.

## Theorem 2

For each `k=1,2,3,4,5` the displayed comparison is whether

`12 t(2k,0,0)^2 > 16 t(k,k,k)^2`.

Substituting the computed times gives

`12 t(2,0,0)^2 = 192 > 144 = 16 t(1,1,1)^2`,

`12 t(4,0,0)^2 = 768 > 576 = 16 t(2,2,2)^2`,

`12 t(6,0,0)^2 = 1200 > 1296` is false, since `16 t(3,3,3)^2 = 1296`,

`12 t(8,0,0)^2 = 1728 > 2304` is false, since `16 t(4,4,4)^2 = 2304`,

and

`12 t(10,0,0)^2 = 2352 > 3600` is false, since `16 t(5,5,5)^2 = 3600`.

Body-diagonal reverse therefore holds at the small scales `k=1,2` and
fails at `k=3,4,5` on this same finite domain. Fail is already present
at `k=3`; it is not isolated at the doubled diamond. Displayed, not
adopted.

## Theorem 3

The note does not write `(0,1,1)` into Admissibility. Do not attach L1.
Uniqueness is not required. The current axiom memo is not edited.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Ten arrival times and five displayed reverse inequalities are exact outputs of one Dijkstra on the named finite graph; the hop-cost is a disclosed scoring rule, not an axiom, and reverse holds at k=1,2 and fails at k=3,4,5."
trace_class: compute
artifact_role: theorem
conditional_surface_status: "exact on B_16(0) under the named (0,1,1) hop-cost at k=1..5 on ((2k,0,0),(k,k,k)); displayed, not adopted"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## What This Does Not Claim

- It does not adopt the `(0,1,1)` hop-cost as framework content.
- It does not claim that reverse survives every integer scale.
- It does not claim that the named rule is the only reverser.
- It does not identify `t` with nearest-neighbor hop count.
- It does not supply a physical clock, a continuum metric, or a Record
  readout of the arrival times.
- It does not score any pair other than `((2k,0,0),(k,k,k))`.
- It does not substitute four named pairs for the five-scale census.

## Reproducibility

```text
python3 scripts/clause_011_body_reverse_vs_k_b16_2026_08_15.py
```

The runner prints the ten times, the five displayed comparisons, and
`TOTAL: PASS=<n> FAIL=<n>`.
