---
claim_id: unread_site_deletion_vs_c2d4_reverse_b6_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Same-k reverse and face at k=1 under named c2d4 on B_6(0) versus B_6(0) minus unread (2,0,0) is compared. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/unread_site_deletion_vs_c2d4_reverse_b6_2026_08_15.py
---

# Unread-Site Deletion Versus Named c2d4 Reverse And Face Bits At k=1 On B_6(0)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** two Dijkstra arrival comparisons at k=1 on the finite nearest-neighbor
graph `B_6(0)` and on `B_6(0)` minus one unread witness, under the named hop-cost
`c2d4`, displayed for this note only.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/unread_site_deletion_vs_c2d4_reverse_b6_2026_08_15.py`](../scripts/unread_site_deletion_vs_c2d4_reverse_b6_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.
**Cache:** none. `cache_write: false`.

## Result Up Front

Record supplies that a site with no record cannot be read. The displayed
recorded set on this host is

```text
R = { (0,0,0), (1,0,0), (1,1,0), (1,1,1) }.
```

The unread witness is `u = (2,0,0)`. It lies in `B_6(0)` and is not in `R`.
Uniqueness is not required.

Write `|σ_v|` for the number of nonzero coordinates of `v ∈ Z^3`. Named `c2d4`
is a separately displayed hop-cost. The parent clauses `ν`, `μ`, and `ρ3` are
those of the ridge-slide same-k scoring on this ball:

- `ν(v→w) = 3` if `|σ_v|=0` or `(|σ_v|=|σ_w|=1)` or `|σ_w| < |σ_v|`, else `1`;
- `μ(v→w) = 3` if `ν` would be `3` or `(|σ_v|=|σ_w|=2` and the least nonzero
  `|w_i|` equals `1)`, else `1`;
- `ρ3(v→w) = 3` if `μ` would be `3` or `(|σ_v|=|σ_w|=3` and exactly two
  `|w_i|` equal `1)`, else `1`;
- `c2d4(v→w) = 3` if `ρ3` would be `3`, else `2` if (`|σ_v|=|σ_w|=2` and
  `max_i |w_i| > max_i |v_i|` and `max_i |v_i| ≥ 4`), else `1`.

The extra `c2d4` clause is a max≥4 out-face hop priced at `2`. It is
displayed, not adopted.

The finite host is scored independently. Two Dijkstras from the origin are run:
first on `B_6(0)`, then on `B_6(0) \ {u}`. The ball is not leftover of a larger-ball table.

```text
B_6(0) := { v ∈ Z^3 : |v_1| + |v_2| + |v_3| ≤ 6 }.
```

It has 377 sites. The punctured host has 376 sites. Edges are the cubic
nearest-neighbor steps that remain inside the scored host.

On the full ball the four arrivals are

```text
t(1,0,0) = 3
t(1,1,1) = 5
t(2,0,0) = 6
t(1,1,0) = 4
```

The same-k reverse comparison at k=1 is

```text
t(1,0,0)^2 / 1 = 9 > 25/3 = t(1,1,1)^2 / 3.
```

Equivalently `27 > 25`. The reverse bit is true.

The same-k face comparison at k=1 is

```text
t(2,0,0)^2 / 4 = 9 > 8 = t(1,1,0)^2 / 2.
```

Equivalently `36 > 32`. The face bit is true.

On `B_6(0) \ {u}` the recorded arrivals are unchanged,

```text
t(1,0,0) = 3
t(1,1,1) = 5
t(1,1,0) = 4
```

and t(2,0,0) is absent. Reverse remains defined and true. The face bit is
undefined because its axis site is the deleted unread witness.

The reverse bit does not move. The face bit is undefined after deletion, so it
has no comparable value on the punctured host. No defined reverse or face bit moves.
Record set R is unchanged: `u` is not in `R`, and deleting `u` from the
host neither adds nor removes a recorded site. Displayed, not adopted.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Two Dijkstras, on B_6(0) then on B_6(0) minus unread (2,0,0), report the k=1 reverse and face bits under named c2d4. The comparison is displayed, not adopted."
trace_class: frontier_discovery
target_claim_id: unread_site_deletion_vs_c2d4_reverse_b6
target_blocker_text: "whether named c2d4 reverse or face bits at k=1 move after deleting one unread site while R is unchanged"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the bounded unread-site deletion comparison"
conditional_surface_status: "exact on B_6(0) versus B_6(0) minus unread (2,0,0) under named c2d4; displayed, not adopted"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Inputs And Import Boundary

- **Framework dependency:** the live Lattice sentence supplies nearest-neighbor
  adjacency on `Z^3`. It is quoted without rewrite. Named `c2d4` is not Lattice
  content. Record supplies that a site with no record cannot be read; it does
  not name a hop-cost.
- **Explicit theorem-domain condition:** the finite set `B_6(0)`, its
  nearest-neighbor edges, the displayed recorded set `R`, the unread witness
  `u = (2,0,0)`, and the named directed costs `ν`, `μ`, `ρ3`, and `c2d4` are
  supplied mathematical data for this theorem.
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

The live Record unreadability sentence, quoted and not rewritten:

> A site with no record cannot be read.

`c2d4` is a separately named hop-cost on directed nearest-neighbor hops. It is
not that admissibility rule.

Write `t(v)` for the Dijkstra arrival cost from the origin to `v` under `c2d4`.
Two Dijkstras are run: the full ball first, then the ball minus `u`.

An explicit axis witness is the single hop `(0,0,0) → (1,0,0)` of cost `3`.
An explicit face witness is `(0,0,0) → (1,0,0) → (1,1,0)` with costs `3+1=4`.
An explicit body witness is `(0,0,0) → (1,0,0) → (1,1,0) → (1,1,1)` with costs
`3+1+1=5`. An explicit unread-axis witness on the full ball is
`(0,0,0) → (1,0,0) → (2,0,0)` with costs `3+3=6`. Every `c2d4` path has first
hop cost `3`, and every hop costs at least `1`, so those witnesses are optimal
once Dijkstra matches them. They are witnesses, not a uniqueness claim.

The k=1 reverse bit uses only recorded sites `(1,0,0)` and `(1,1,1)`. The k=1
face bit uses `(2,0,0)` and `(1,1,0)`; the first of those is the unread
witness.

## Theorem 1 — Full-ball arrivals and k=1 reverse and face bits

Under `c2d4` on `B_6(0)`,

```text
t(1,0,0) = 3
t(1,1,1) = 5
t(2,0,0) = 6
t(1,1,0) = 4
```

The displayed reverse comparison is whether

```text
t(1,0,0)^2 / 1 > t(1,1,1)^2 / 3.
```

Substituting the computed times gives `9 > 25/3`, or equivalently `27 > 25`.
The reverse bit is true.

The displayed face comparison is whether

```text
t(2,0,0)^2 / 4 > t(1,1,0)^2 / 2.
```

Substituting the computed times gives `9 > 8`, or equivalently `36 > 32`.
The face bit is true.

## Theorem 2 — Punctured-ball arrivals and bits if defined

Under `c2d4` on `B_6(0) \ {u}`,

```text
t(1,0,0) = 3
t(1,1,1) = 5
t(1,1,0) = 4
```

and t(2,0,0) is absent. Reverse remains defined: `9 > 25/3` still holds, so
the reverse bit is true. The face bit is undefined.

## Theorem 3 — Bit motion after unread deletion; no axiom write and no L1 attachment

The reverse bit does not move. The face bit is undefined after deleting unread
`u`, because the face-axis site is that unread witness. No defined reverse or face bit moves.
Record set R is unchanged.

Do not write hop-costs into Admissibility. Do not attach L1.

The live Admissibility wording names one fixed nearest-neighbor
admissibility rule and does not name `c2d4`, `ρ3`, `μ`, or `ν`. This note
proposes no axiom edit. The comparison above is a score of one named hop-cost
on two hosts; it is not an attachment of a coordinate-sum hop-cost.

## What This Does Not Claim

- Uniqueness is not required.
- No physical identification of `t` as a clock, mass, or force law is made.
- No claim is made that Record locks these arrival times.
- Independent leftovers on larger balls are not used as parents.
- Undefined face after deleting the unread axis site is not a no-go against
  named hop-costs elsewhere.

These are scope boundaries, not impossibility or route-exhaustion claims.
Accordingly, no no-go verdict is authored here.

## Live Parent Quotes

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

> There is one fixed nearest-neighbor admissibility rule, covariant under lattice
> translations and proper cubic rotations.

> A site with no record cannot be read.

Their dependency role is limited to the repository's site graph, the
unreadability of a site with no record, and the refusal to treat a named
hop-cost as axiom content.

## Runner Contract

The companion runner builds `B_6(0)` and `B_6(0) \ {u}`, evaluates named
`c2d4`, and runs two Dijkstras from the origin, full ball then ball minus `u`.
It reports `t(1,0,0)`, `t(1,1,1)`, `t(2,0,0)`, and `t(1,1,0)` on the full
ball, the same four arrivals on the punctured ball with `t(2,0,0)` absent, the
k=1 reverse and face bits when defined, and whether any defined bit moves
while `R` is unchanged. It checks that the live Admissibility wording does not
name these hop-costs, refuses to attach L1, and records the import boundary.
Declared review inputs are this note and the axiom memo only.
