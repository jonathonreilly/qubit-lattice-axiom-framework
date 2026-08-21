---
claim_id: seedo_four_event_minkowski_gram_signature_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: Minkowski Gram signature of the three seedo displacements from origin of axis, face, and body events is reported versus gram4 (1,2,0). Displayed, not adopted.
upstream_dependencies:
  - minimal_axioms
runner: scripts/seedo_four_event_minkowski_gram_signature_2026_08_15.py
---

# Seedo Four-Event Minkowski Gram Signature Versus gram4

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact 3×3 Minkowski Gram of three displayed seedo displacements
on four cube events. Signature is reported versus gram4 `(1,2,0)`. Displayed,
not adopted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/seedo_four_event_minkowski_gram_signature_2026_08_15.py`](../scripts/seedo_four_event_minkowski_gram_signature_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

Four events only. No Dijkstra. Ticks are the displayed seedo values, not
recomputed by path dump. Do not attach L1. Do not write a metric into
Admissibility. Uniqueness is not required.

## Result Up Front

The four events, as in gram4, are

```text
O=(0,0,0), A=(1,0,0), D=(1,1,0), B=(1,1,1).
```

`A` is the axis event, `D` the face event, and `B` the body event. Displayed
seedo ticks, not recomputed by path dump, are

```text
t(O)=0, t(A)=1, t(D)=2, t(B)=3.
```

Four-vectors and the Minkowski product are the displayed comparison data

```text
u(x)=(t(x), x_1, x_2, x_3),
u·v = t_u t_v − x_u·x_v.
```

Let `G` be the 3×3 Gram of `u(A)`, `u(D)`, `u(B)`. Then the nine exact
entries are

```text
G = [[0, 1, 2], [1, 2, 4], [2, 4, 6]].
```

Exact rational LDL with diagonal pivoting, and independently the exact
characteristic polynomial, both give signature `(n+, n−, n0) = (1, 2, 0)`.
That signature equals gram4's `(1,2,0)`. Displayed, not adopted.

The equality does not attach a Lorentzian 3-plane to reverse HOLD, does not
select a spacetime metric, and does not close L1.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The nine Gram entries and the inertia (1,2,0) close by exact rational algebra on four displayed events; the comparison to gram4 is a report, not an adopted metric."
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "whether the Lorentzian 3-plane of three cube displacements is coupled to reverse HOLD"
source_of_blocker_text: handoff
reachability_to_target: reports
artifact_role: theorem
next_trace_action: "independent audit of the displayed Gram and signature; do not attach L1"
conditional_surface_status: "exact for the four displayed events and displayed seedo ticks; metric not adopted"
hypothetical_axiom_status: no edit
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Inputs And Import Boundary

- **Framework dependency:** Lattice supplies the cubic lattice `Z^3` as the
  site set. The live sentence is quoted without rewrite.
- **Displayed comparison data:** the four events, the seedo ticks, the
  4-vector map, and the Minkowski product are inputs of this note. They are
  not derived here and are not written into Admissibility.
- **gram4 comparison target:** signature `(1,2,0)` is the displayed gram4
  value being compared against. It is not recomputed from HOLD paths.
- **External empirical or literature inputs:** none.
- **Open physical bridge:** a spacetime metric, a Lorentz-restoration claim,
  and L1 remain outside the target.

Live Lattice sentence, quoted and not rewritten:

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

## Exact Objects

All coefficients are exact rationals. Signature is not read from floats.

The four events are only

```text
O=(0,0,0), A=(1,0,0), D=(1,1,0), B=(1,1,1).
```

Displayed ticks:

```text
t(O)=0, t(A)=1, t(D)=2, t(B)=3.
```

The corresponding 4-vectors are

```text
u(O)=(0,0,0,0),
u(A)=(1,1,0,0),
u(D)=(2,1,1,0),
u(B)=(3,1,1,1).
```

`G` is the Gram of the three displacements from the origin. `u(O)` is the
zero vector and does not enter `G`.

## Theorem 1 — Nine Exact Gram Entries

Direct evaluation of `u·v = t_u t_v − x_u·x_v` gives

```text
u(A)·u(A) = 1-1 = 0,
u(A)·u(D) = 2-1 = 1,
u(A)·u(B) = 3-1 = 2,
u(D)·u(D) = 4-2 = 2,
u(D)·u(B) = 6-2 = 4,
u(B)·u(B) = 9-3 = 6.
```

Hence

```text
G = [[0, 1, 2], [1, 2, 4], [2, 4, 6]].
```

`G` is symmetric. The unpivoted leading principal minors are `0`, `-1`, and
`2`. In particular `det G = 2`, so `G` is nondegenerate, while the vanishing
leading minor blocks unpivoted Sylvester counting.

## Theorem 2 — Signature `(n+, n−, n0) = (1, 2, 0)`

Congruence to a diagonal form is obtained by exact rational LDL after
largest-absolute-diagonal pivoting. One such diagonal is
`diag(6, -2/3, -1/2)`. The signs are one positive and two negative, with no
zero. Sylvester's law therefore gives

```text
(n+, n−, n0) = (1, 2, 0).
```

Independently, the characteristic polynomial is the exact cubic

```text
det(λI − G) = λ^3 − 8λ^2 − 9λ − 2.
```

The constant term is `-det G = -2 ≠ 0`, so `n0 = 0`. The exact Sturm chain
of this cubic has two sign changes on `(-∞,0)` and one on `(0,+∞)`, hence
the same inertia `(1, 2, 0)`.

## Theorem 3 — Comparison To gram4 `(1,2,0)`

The displayed seedo signature equals gram4's (1,2,0). Displayed, not
adopted.

The report is a numerical equality of two inertias on the same three
displacements under two separately named tick displays. Uniqueness is not
required: this note does not claim that reverse HOLD is the unique source of
a Lorentzian 3-plane, nor that seedo ticks are the unique source. Do not
attach L1. Do not write a metric into Admissibility.

A Euclidean spatial Gram of the same three vectors `(A,D,B)` is positive
definite of inertia `(3,0,0)`. Erasing the displayed ticks (setting every
`t=0`) likewise changes the Minkowski signature. Those mutations show that
the Minkowski product and the displayed ticks are load-bearing for Theorem 2.
They are not a physical metric selection.

## Exact Target And Obligation Graph

| Obligation | Disposition |
|---|---|
| fix four events only | declared: `O,A,D,B` |
| use displayed seedo ticks | declared: `0,1,2,3`; No Dijkstra |
| form 4-vectors and Minkowski products | Theorem 1 |
| report the nine exact `G` entries | Theorem 1 |
| compute inertia by exact rational LDL | Theorem 2 |
| confirm inertia by characteristic polynomial | Theorem 2 |
| compare to gram4 `(1,2,0)` | Theorem 3: equal; Displayed, not adopted |
| attach L1 or a metric to Admissibility | outside the claim |

The obligation graph is acyclic. Physical Lorentz restoration is not a proof
leaf because it is expressly not part of the target.

## What This Does Not Claim

- It does not recompute ticks by a shortest-path dump.
- It does not introduce a fifth event.
- It does not adopt a Minkowski metric as framework structure.
- It does not write a metric into Admissibility.
- It does not attach L1.
- It does not claim uniqueness of the Lorentzian 3-plane or of the tick
  display.
- It does not edit Lattice, Qubit, Admissibility, Record, or any primitive.
- It does not use observational, fitted, or literature values.

## Runner Contract

The companion runner checks Theorems 1–3 with exact `Fraction` arithmetic,
pivoted LDL inertia, characteristic-polynomial inertia, the Euclidean and
zero-tick mutations, the gram4 comparison, the live Lattice quote, and the
claim bounds (four events, No Dijkstra, no L1, no metric written into
Admissibility, no runner cache). Declared review inputs are this note and
the axiom memo only.
