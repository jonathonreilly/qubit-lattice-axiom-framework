---
claim_id: l1_locksupport_vs_c2d4_face_k1_b6_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Face reverse at k=1 under unit ℓ¹ versus named c2d4 on B_6(0) is compared. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/l1_locksupport_vs_c2d4_face_k1_b6_2026_08_15.py
---

# Unit ℓ¹ Lock-Support Versus Named c2d4 Face Reverse Bits At k=1 On B_6(0)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** two Dijkstra arrival comparisons at k=1 on the finite nearest-neighbor
graph `B_6(0)`, under native unit ℓ¹ and the named hop-cost `c2d4`, displayed
for this note only.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/l1_locksupport_vs_c2d4_face_k1_b6_2026_08_15.py`](../scripts/l1_locksupport_vs_c2d4_face_k1_b6_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.
**Cache:** none. `cache_write: false`.

## Result Up Front

Write `|σ_v|` for the number of nonzero coordinates of `v ∈ Z^3`. Native unit
ℓ¹ on the cubic 6-NN graph prices every remaining hop at cost `1`. That unit
graph is the lock-support cone of the origin: Record locks at a site, and the
native nearest-neighbor support spreads at unit hop cost. Named `c2d4` is a
separately displayed hop-cost. The parent clauses `ν`, `μ`, and `ρ3` are those
of the ridge-slide same-k scoring on this ball:

- `ν(v→w) = 3` if `|σ_v|=0` or `(|σ_v|=|σ_w|=1)` or `|σ_w| < |σ_v|`, else `1`;
- `μ(v→w) = 3` if `ν` would be `3` or `(|σ_v|=|σ_w|=2` and the least nonzero
  `|w_i|` equals `1)`, else `1`;
- `ρ3(v→w) = 3` if `μ` would be `3` or `(|σ_v|=|σ_w|=3` and exactly two
  `|w_i|` equal `1)`, else `1`;
- `c2d4(v→w) = 3` if `ρ3` would be `3`, else `2` if (`|σ_v|=|σ_w|=2` and
  `max_i |w_i| > max_i |v_i|` and `max_i |v_i| ≥ 4`), else `1`.

The extra `c2d4` clause is a max≥4 out-face hop priced at `2`: support stays
`2`, the destination max absolute coordinate grows, and the source max is
already at least `4`. It is displayed, not adopted. Uniqueness is not required.

Face reverse at k=1 is the integer comparison

```text
t(2,0,0)^2 > 2 t(1,1,0)^2.
```

The finite host is scored independently. Two Dijkstras from the origin are run
on this ball, unit ℓ¹ first, then `c2d4`. The ball is not leftover of a larger-ball table.

```text
B_6(0) := { v ∈ Z^3 : |v_1| + |v_2| + |v_3| ≤ 6 }.
```

It has 377 sites. Edges are the cubic nearest-neighbor steps that remain
inside `B_6(0)`.

Under unit ℓ¹ the two arrivals are

```text
t(2,0,0) = 2
t(1,1,0) = 2
```

The face reverse comparison at k=1 is

```text
t(2,0,0)^2 = 4 > 8 = 2 t(1,1,0)^2.
```

The inequality fails. The ℓ¹ face bit is false.

Under `c2d4` the two arrivals are

```text
t(2,0,0) = 6
t(1,1,0) = 4
```

The face reverse comparison at k=1 is

```text
t(2,0,0)^2 = 36 > 32 = 2 t(1,1,0)^2.
```

The inequality holds. The `c2d4` face bit is true.

The two face bits disagree. Displayed, not adopted.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Two Dijkstras on B_6(0) report t(2,0,0) and t(1,1,0) under unit ℓ¹ and named c2d4 and compare the k=1 face reverse bits. The comparison is displayed, not adopted."
trace_class: frontier_discovery
target_claim_id: l1_locksupport_vs_c2d4_face_k1_b6
target_blocker_text: "whether native 6-NN ℓ¹ lock-support face reverse bits agree with c2d4 Dijkstra face reverse bits at k=1"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the bounded face-bit comparison"
conditional_surface_status: "exact on B_6(0) under unit ℓ¹ versus named c2d4; displayed, not adopted"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Inputs And Import Boundary

- **Framework dependency:** the live Lattice sentence supplies nearest-neighbor
  adjacency on `Z^3`. It is quoted without rewrite. Unit ℓ¹ and named `c2d4`
  are not Lattice content. Record supplies lock of one admissible local
  possibility; it does not name a hop-cost.
- **Explicit theorem-domain condition:** the finite set `B_6(0)`, its
  nearest-neighbor edges, unit ℓ¹ cost `1` on every remaining hop, and the
  named directed costs `ν`, `μ`, `ρ3`, and `c2d4` are supplied mathematical
  data for this theorem.
- **External empirical or literature inputs:** none.
- **Open physical bridge:** writing hop-costs into Admissibility, attaching
  L1, selecting `c2d4` as a physical cost, or lifting the comparison off
  `B_6(0)` remain separate obligations. This note does not close them.

## Exact Objects

All runner values are integers. No float is used in the comparison.

The live Lattice sentence, quoted and not rewritten:

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

The live Admissibility sentence, quoted and not rewritten:

> There is one fixed nearest-neighbor admissibility rule, covariant under lattice
> translations and proper cubic rotations.

The live Record lock sentence, quoted and not rewritten:

> When present, a record locks exactly one admissible local possibility.

Unit ℓ¹ and `c2d4` are separately named hop-costs on directed nearest-neighbor
hops. Neither is that admissibility rule.

Write `t(v)` for a Dijkstra arrival cost from the origin to `v` on `B_6(0)`,
with the cost named in each theorem. Two Dijkstras are run: unit ℓ¹ first,
then `c2d4`.

An explicit axis witness under unit ℓ¹ is two unit hops
`(0,0,0) → (1,0,0) → (2,0,0)` of total cost `2`. An explicit face witness is
two unit hops `(0,0,0) → (1,0,0) → (1,1,0)` of total cost `2`. Under `c2d4`
the corresponding axis witness has costs `3+3=6` and the face witness has
costs `3+1=4`. Every `c2d4` path has first hop cost `3`, and every hop costs
at least `1`, so those witnesses are optimal once Dijkstra matches them.
Under unit ℓ¹ every hop costs `1`, so graph distance is the arrival.

## Theorem 1 — Unit ℓ¹ arrivals and face reverse bit at k=1

Under unit ℓ¹ on `B_6(0)`,

```text
t(2,0,0) = 2
t(1,1,0) = 2
```

The displayed comparison is whether

```text
t(2,0,0)^2 > 2 t(1,1,0)^2.
```

Substituting the computed times gives `4 > 8`. The inequality fails. The ℓ¹
face bit is false.

## Theorem 2 — Named c2d4 arrivals and face reverse bit at k=1

Under `c2d4` on `B_6(0)`,

```text
t(2,0,0) = 6
t(1,1,0) = 4
```

The displayed comparison is whether

```text
t(2,0,0)^2 > 2 t(1,1,0)^2.
```

Substituting the computed times gives `36 > 32`. The inequality holds. The
`c2d4` face bit is true.

## Theorem 3 — Face-bit comparison; no axiom write and no L1 attachment

The two face bits disagree.

Do not write hop-costs into Admissibility. Do not attach L1.

The live Admissibility wording names one fixed nearest-neighbor
admissibility rule and does not name unit ℓ¹, `c2d4`, `ρ3`, `μ`, or `ν`.
This note proposes no axiom edit. The comparison above is a score of two
named hop-costs at two sites; it is not an attachment of a coordinate-sum
hop-cost.

## What This Does Not Claim

- Uniqueness is not required.
- No physical identification of `t` as a clock, mass, or force law is made.
- No claim is made that Record locks these arrival times.
- Independent leftovers on larger balls are not used as parents.
- Disagreement on this ball is not a no-go against named hop-costs elsewhere.

These are scope boundaries, not impossibility or route-exhaustion claims.
Accordingly, no no-go verdict is authored here.

## Live Parent Quotes

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

> There is one fixed nearest-neighbor admissibility rule, covariant under lattice
> translations and proper cubic rotations.

> A site with no record cannot be read.

Their dependency role is limited to the repository's site graph and the
refusal to treat a named hop-cost as axiom content.

## Runner Contract

The companion runner builds `B_6(0)`, evaluates unit ℓ¹ and named `c2d4`, and
runs two Dijkstras from the origin, unit ℓ¹ then `c2d4`. It reports
`t(2,0,0)` and `t(1,1,0)` under each cost, checks the integer form of each
k=1 face reverse comparison, and checks that the face bits disagree. It
checks that the live Admissibility wording does not name these hop-costs,
refuses to attach L1, and records the import boundary. Declared review
inputs are this note and the axiom memo only.
