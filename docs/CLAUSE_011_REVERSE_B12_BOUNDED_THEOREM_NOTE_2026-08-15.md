---
claim_id: clause_011_reverse_b12_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Body-diagonal reverse under the named (0,1,1) hop-cost on B_12(0) is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/clause_011_reverse_b12_2026_08_15.py
---

# Named (0,1,1) Hop-Cost Body-Diagonal Reverse On B_12(0)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact arrival times under one named hop-cost on the finite
12-hop neighborhood of the origin in the cubic nearest-neighbor graph.
The rule is displayed, not adopted.
**Primary runner:**
[`scripts/clause_011_reverse_b12_2026_08_15.py`](../scripts/clause_011_reverse_b12_2026_08_15.py)

## Result Up Front

Let `B_12(0)` be the set of sites of `Z^3` whose nearest-neighbor graph
distance from the origin is at most 12. That set has 2625 sites and is
used only as a finite domain bound. It is not a hop-cost.

Hops are the six nearest-neighbor steps that remain inside `B_12(0)`.
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
t(4,0,0)=8
t(8,0,0)=12
t(12,0,0)=18
t(2,2,2)=6
t(4,4,4)=12
```

The displayed reverse tests are

```text
12 t(4,0,0)^2 = 768 > 576 = 16 t(2,2,2)^2     yes
12 t(8,0,0)^2 = 1728 > 2304 = 16 t(4,4,4)^2   no
```

The small body-diagonal pair still reverses. The doubled pair does not.
A rival member of this family is only live if reverse survives scale, so
the named rule is not live on that score. Uniqueness is not required.
Displayed, not adopted.

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

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Five arrival times and two displayed reverse inequalities are exact outputs of one Dijkstra on the named finite graph; the hop-cost is a disclosed scoring rule, not an axiom, and the doubled pair fails reverse."
trace_class: compute
artifact_role: theorem
conditional_surface_status: "exact on B_12(0) under the named (0,1,1) hop-cost; displayed, not adopted"
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

The two reverse inequalities compare axis and body-diagonal sites that
share the same Euclidean squared length pair `(16,12)` after scaling:
`(4,0,0)` with `(2,2,2)`, and `(8,0,0)` with `(4,4,4)`. The comparison
is displayed only. It is not a derived continuum law and is not attached
as an L1 hop-cost.

## Theorem 1

On `B_12(0)` under the named `(0,1,1)` hop-cost,

`t(4,0,0)=8`, `t(8,0,0)=12`, `t(12,0,0)=18`, `t(2,2,2)=6`, and
`t(4,4,4)=12`.

Each value is the Dijkstra arrival time. The axis values are strictly
larger than the corresponding nearest-neighbor hop counts, because the
last step onto a 1-support site costs 3. The body-diagonal values equal
the hop counts, because a monotone support-nondecreasing path from the
origin uses only cost-1 hops.

## Theorem 2

The displayed inequalities are

`12 t(4,0,0)^2 = 768 > 576 = 16 t(2,2,2)^2`,

and

`12 t(8,0,0)^2 = 1728 > 2304` is false, since `16 t(4,4,4)^2 = 2304`.

Body-diagonal reverse therefore holds for the small pair and fails for
the doubled pair on this same finite domain. Displayed, not adopted.

## Theorem 3

The note does not write `(0,1,1)` into Admissibility. Do not attach L1.
Uniqueness is not required. The current axiom memo is not edited.

## What This Does Not Claim

- It does not adopt the `(0,1,1)` hop-cost as framework content.
- It does not claim that reverse survives scale.
- It does not claim that the named rule is the only reverser.
- It does not identify `t` with nearest-neighbor hop count.
- It does not supply a physical clock, a continuum metric, or a Record
  readout of the arrival times.

## Reproducibility

```text
python3 scripts/clause_011_reverse_b12_2026_08_15.py
```

The runner prints the five times, both displayed comparisons, and
`TOTAL: PASS=<n> FAIL=<n>`.
