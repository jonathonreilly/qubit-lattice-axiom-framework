---
claim_id: clause_011_face_reverse_vs_k_b16_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Face-diagonal reverse versus integer scale k under the named (0,1,1) hop-cost on B_16(0) is reported for k=1..8. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/clause_011_face_reverse_vs_k_b16_2026_08_15.py
---

# Named (0,1,1) Face Reverse Versus Scale k On B_16(0)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact arrival times under one named hop-cost on the finite
16-hop neighborhood of the origin in the cubic nearest-neighbor graph.
Face-diagonal reverse bits for integer scale `k=1..8` are displayed, not
adopted.
**Audit-status authority:** independent audit lane only. This note authors
no audit verdict and predicts none.
**Primary runner:**
[`scripts/clause_011_face_reverse_vs_k_b16_2026_08_15.py`](../scripts/clause_011_face_reverse_vs_k_b16_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.
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

One Dijkstra from the origin yields

```text
t(2,0,0)=4
t(4,0,0)=8
t(6,0,0)=10
t(8,0,0)=12
t(10,0,0)=14
t(12,0,0)=16
t(14,0,0)=18
t(16,0,0)=22
t(1,1,0)=2
t(2,2,0)=4
t(3,3,0)=6
t(4,4,0)=8
t(5,5,0)=10
t(6,6,0)=12
t(7,7,0)=14
t(8,8,0)=16
```

For each integer scale `k=1..8` the displayed reverse test is

```text
t(2k,0,0)^2 / (4k^2) > t(k,k,0)^2 / (2k^2).
```

That comparison is equivalent to the integer test
`t(2k,0,0)^2 > 2 t(k,k,0)^2`. The eight bits are

```text
k=1  16/4 = 4 > 2 = 4/2                 yes   16 > 8
k=2  64/16 = 4 > 2 = 16/8               yes   64 > 32
k=3  100/36 > 2 = 36/18                 yes   100 > 72
k=4  144/64 = 9/4 > 2 = 64/32           yes   144 > 128
k=5  196/100 > 2 = 100/50               no    196 > 200 is false
k=6  256/144 > 2 = 144/72               no    256 > 288 is false
k=7  324/196 > 2 = 196/98               no    324 > 392 is false
k=8  484/256 > 2 = 256/128              no    484 > 512 is false
```

Reverse holds at `k=1,2,3,4` and fails at `k=5,6,7,8`. The cheaper
rival still keeps `k=4`. Failure is not isolated at `k=5`. Uniqueness
is not required. Displayed, not adopted.

## Current Premise Boundary

The Lattice and Admissibility premises are quoted from
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md):

Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
adjacency, standard translations, and proper cubic rotations about each site.

There is one fixed nearest-neighbor admissibility rule, covariant under
lattice translations and proper cubic rotations.

The axiom set supplies the cubic nearest-neighbor graph. It does not
supply a hop-cost, a face-diagonal reverse test, an integer scale `k`,
or a preferred clause-toggle. This note therefore treats `(0,1,1)` as a
separately named finite scoring rule. The note does not write `(0,1,1)`
into Admissibility and does not enlarge the axiom set.

Record is not used. No readout, formation site, or scalar collection
functional enters the arrival times.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Sixteen arrival times and eight displayed reverse bits are exact outputs of one Dijkstra on B_16(0); the hop-cost is a disclosed scoring rule, not an axiom."
trace_class: compute
artifact_role: theorem
conditional_surface_status: "exact on B_16(0) under the named (0,1,1) hop-cost; displayed, not adopted"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

`B_16(0)` is the closed 16-hop neighborhood of the origin. Every hop
used below is a nearest-neighbor step whose endpoints both lie in that
set. One Dijkstra computes the named arrival time `t(v)` from the
origin to each site.

The displayed pairs are `(2k,0,0)` versus `(k,k,0)` for each
`k=1..8`. Each comparison is displayed only. It is not a derived
continuum law and is not attached as an L1 hop-cost.

## Theorem 1

On `B_16(0)` under the named `(0,1,1)` hop-cost, the axis arrivals are

`t(2,0,0)=4`, `t(4,0,0)=8`, `t(6,0,0)=10`, `t(8,0,0)=12`,
`t(10,0,0)=14`, `t(12,0,0)=16`, `t(14,0,0)=18`, `t(16,0,0)=22`,

and the face arrivals are

`t(1,1,0)=2`, `t(2,2,0)=4`, `t(3,3,0)=6`, `t(4,4,0)=8`,
`t(5,5,0)=10`, `t(6,6,0)=12`, `t(7,7,0)=14`, `t(8,8,0)=16`.

Each value is the Dijkstra arrival time. Face arrivals equal the
nearest-neighbor hop counts, because a monotone support-nondecreasing
path from the origin to `(k,k,0)` uses only cost-1 hops. Axis arrivals
are strictly larger than the corresponding hop counts, because the last
step onto a 1-support site costs 3 unless a support-raising detour is
cheaper.

## Theorem 2

For each `k=1..8` the displayed comparison is whether

`t(2k,0,0)^2 / (4k^2) > t(k,k,0)^2 / (2k^2)`.

The eight integer forms and bits are `16 > 8` yes, `64 > 32` yes,
`100 > 72` yes, `144 > 128` yes, `196 > 200` no, `256 > 288` no,
`324 > 392` no, and `484 > 512` no. Reverse therefore holds on
`k=1..4` and fails on `k=5..8`. Displayed, not adopted.

## Theorem 3

The note does not write `(0,1,1)` into Admissibility. Do not attach L1.
Uniqueness is not required. The current axiom memo is not edited.

## What This Does Not Claim

- It does not adopt the `(0,1,1)` hop-cost as framework content.
- It does not claim that reverse survives every listed scale.
- It does not claim that failure is isolated at `k=5`.
- It does not claim that the named rule is the only reverser.
- It does not identify `t` with nearest-neighbor hop count on the axis.
- It does not supply a physical clock, a continuum metric, or a Record
  readout of the arrival times.

## Reproducibility

```text
python3 scripts/clause_011_face_reverse_vs_k_b16_2026_08_15.py
```

The runner prints the sixteen times, the eight displayed comparisons, and
`TOTAL: PASS=<n> FAIL=<n>`.
