---
claim_id: cost2_max4_out_face_doubled_pairing_b12_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Doubled-axis versus body-diagonal reverse under the named cost-2 max≥4 out-face hop-cost on B_12(0) is reported for available k=1..4. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/cost2_max4_out_face_doubled_pairing_b12_2026_08_15.py
---

# Named Cost-2 Max≥4 Out-Face Doubled Pairing On B_12(0)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** one named nearest-neighbor hop-cost on the finite ball `B_12(0)`,
scored only for the doubled pairing `((2k,0,0),(k,k,k))` at each
available integer `k=1,2,3,4`.
**Audit-status authority:** independent audit lane only. This note authors
no audit verdict and predicts none.
**Primary runner:**
[`scripts/cost2_max4_out_face_doubled_pairing_b12_2026_08_15.py`](../scripts/cost2_max4_out_face_doubled_pairing_b12_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.
**Cache:** none. `cache_write: false`.

## Result Up Front

Write `|σ_v|` for the number of nonzero coordinates of `v ∈ Z^3`. On a
nearest-neighbor hop `v → w` the named cost-2 max≥4 out-face hop-cost
`c2d4` is the first display of doubled pairing under `c2d4`. The parent
clauses `ν`, `μ`, and `ρ3` are those of the ridge-slide same-k scoring on
this ball:

- `ν(v→w) = 3` if `|σ_v|=0` or `(|σ_v|=|σ_w|=1)` or `|σ_w| < |σ_v|`, else `1`;
- `μ(v→w) = 3` if `ν` would be `3` or `(|σ_v|=|σ_w|=2` and the least nonzero
  `|w_i|` equals `1)`, else `1`;
- `ρ3(v→w) = 3` if `μ` would be `3` or `(|σ_v|=|σ_w|=3` and exactly two
  `|w_i|` equal `1)`, else `1`;
- `c2d4(v→w) = 3` if `ρ3` would be `3`, else `2` if (`|σ_v|=|σ_w|=2` and
  `max_i |w_i| > max_i |v_i|` and `max_i |v_i| ≥ 4`), else `1`.

The extra clause is a max≥4 out-face hop priced at `2`: support stays `2`,
the destination max absolute coordinate grows, and the source max is already
at least `4`. It fires on `(4,2,0) → (5,2,0)` at cost `2`. It does not fire
on the max≥3 out hop `(3,2,0) → (4,2,0)`, whose source max is `3`, nor on the
deep-out hop `(2,2,0) → (3,2,0)`, whose source max is `2`, nor on the
unit-out-face hop `(1,1,0) → (2,1,0)`, whose source max is `1`. That unit-out
hop remains priced at `3` by corridor-slide `μ`, which is already inside
`ρ3`. The skipped max≥3 out hop stays at `ρ3 = 1`, so `c2d4 = 1` there. The
skipped deep-out hop likewise stays at `ρ3 = 1`, so `c2d4 = 1` there. The
parent `d4` uses the same extra hop at cost `3`. The cost-2 max≥3 out-face
rule that prices growing-max `2→2` hops already at source max `3` is not the
displayed rule. Uniqueness is not claimed.

The finite host is scored independently: one origin Dijkstra is run on this
ball. The ball is not leftover of a larger-ball table.

```text
B_12(0) := { v ∈ Z^3 : |v_1| + |v_2| + |v_3| ≤ 12 }.
```

It has 2625 sites (2624 nonzero). Edges are the cubic nearest-neighbor steps
that remain inside `B_12(0)`. For each `k=1,2,3,4` both `(2k,0,0)` and
`(k,k,k)` lie in `B_12(0)`, so no pair is omitted. One Dijkstra from the
origin yields

| `k` | site axis | `t(2k,0,0)` | site body | `t(k,k,k)` | `t(2k,0,0)^2/(4k^2)` | `t(k,k,k)^2/(3k^2)` | reverse |
|---|---|---:|---|---:|---|---|---|
| `1` | `(2,0,0)` | `6` | `(1,1,1)` | `5` | `36/4` | `25/3` | yes |
| `2` | `(4,0,0)` | `12` | `(2,2,2)` | `10` | `144/16` | `100/12` | yes |
| `3` | `(6,0,0)` | `18` | `(3,3,3)` | `13` | `324/36` | `169/27` | yes |
| `4` | `(8,0,0)` | `24` | `(4,4,4)` | `16` | `576/64` | `256/48` | yes |

Equivalently, `3 t(2k,0,0)^2 ? 4 t(k,k,k)^2` is `108 > 100`, `432 > 400`,
`972 > 676`, and `1728 > 1024`. The inequality holds at every available
`k=1..4`. Independently, the new axis site is `t(12,0,0) = 33`.

The extra `2→2` clause is live on this host. The hop `(4,2,0) → (5,2,0)` has
`c2d4=2` and `ρ3=1`, and both ends lie in `B_12(0)`. Therefore `ρ3` cannot price the max≥4 out-face hop, and `d4` cannot cheapen it to `2`. The same
Dijkstra gives `t(3,2,0) = 9` and `t(4,2,0) = 10`, matching the skipped extra
hop of cost `1`, and `t(5,2,0) = 12`, matching the extra hop of cost `2`.
The displayed body last hop `(1,1,0) → (1,1,1)` keeps cost `1`. The skipped
hops `(2,2,0) → (3,2,0)` and `(3,2,0) → (4,2,0)` have `c2d4=1`. The new clause is live.

The pair is not leftover of `ρ3` as a rule: at `k=4` the axis arrivals under
`c2d4` and a cheapest `ρ3` height-two face-growth witness are `24` versus `20`.
The same walk that scores `20` under `ρ3` — seed-exit onto
`(0,-1,0)`, unit-cube leave, corridor-slide to height two, six height-two
slides to `(8,-2,0)`, corridor return, and support-drop — scores `24`
under `c2d4`, because four of those height-two slides grow a source max
already at least `4` and therefore cost `2`. Independently, `t(12,0,0) = 33`
is cheaper than the twelve-hop axis walk of cost `36`, because that far-axis
witness uses one live extra hop `(9,-2,0) → (10,-2,0)` of cost `2`. The
site `(4,4,4)` has coordinate-sum `12`, so it is absent from `B_11(0)`.
The `B_12(0)` table is therefore not leftover of a smaller-ball table.

The rule is displayed, not adopted. Do not write `c2d4` into Admissibility.
Do not write c2d4 into Admissibility. Do not attach L1.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "One Dijkstra on B_12(0) reports t(2k,0,0) and t(k,k,k) under the named cost-2 max≥4 out-face hop-cost at available k=1..4 and scores the doubled pairing comparison. The hop-cost is displayed, not adopted."
trace_class: frontier_discovery
target_claim_id: cost2_max4_out_face_doubled_pairing_b12
target_blocker_text: "whether doubled-axis versus body-diagonal reverse at available k=1..4 holds after max≥4 out-face 2-to-2 hops are priced at 2"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the bounded arrival comparison"
conditional_surface_status: "exact on B_12(0) under the named hop-cost at available k=1..4 on ((2k,0,0),(k,k,k)); displayed, not adopted"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Inputs And Import Boundary

- **Framework dependency:** the live Lattice sentence supplies nearest-neighbor
  adjacency on `Z^3`. It is quoted without rewrite. The hop-cost `c2d4` is not
  Lattice content.
- **Explicit theorem-domain condition:** the finite set `B_12(0)`, its
  nearest-neighbor edges, and the named directed costs `ν`, `μ`, `ρ3`, and
  `c2d4` are supplied mathematical data for this theorem.
- **External empirical or literature inputs:** none.
- **Open physical bridge:** writing `c2d4` into Admissibility, selecting it as
  a physical cost, or lifting the comparison off `B_12(0)` remain separate
  obligations. This note does not close them.

## Exact Objects

All runner values are integers. No float is used in the comparison.

The live Lattice sentence, quoted and not rewritten:

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

The live Admissibility sentence, quoted and not rewritten:

> There is one fixed nearest-neighbor admissibility rule, covariant under lattice
> translations and proper cubic rotations.

`c2d4` is a separately named hop-cost on directed nearest-neighbor hops. It is
not that admissibility rule.

Write `t(v)` for the Dijkstra arrival cost from the origin to `v` under
`c2d4`, using one Dijkstra on `B_12(0)`.

The pairing is not the same-`k` axis / body pair `(k,0,0)` versus
`(k,k,k)`. It is the doubled pairing `((2k,0,0),(k,k,k))`.

On the max≥4 out hop `(4,2,0) → (5,2,0)` one has `|σ_v|=|σ_w|=2`, dest max
`5` greater than source max `4`, and source max already `4`, so `ρ3 = 1`
while `c2d4 = 2` and the parent `d4` would be `3`. Therefore `ρ3` cannot
price the max≥4 out-face hop. On the in-ball hop `(4,1,0) → (5,1,0)` the extra
clause fires, but the destination least nonzero absolute coordinate is `1`,
so both `ρ3` and `c2d4` cost `3`. On the max≥3 out hop `(3,2,0) → (4,2,0)`
the extra clause is idle because the source max is `3`; both `ρ3` and `c2d4`
cost `1`, while the cost-2 max≥3 parent would be `2`. On the deep-out hop
`(2,2,0) → (3,2,0)` the extra clause is idle because the source max is `2`;
both `ρ3` and `c2d4` cost `1`. On the unit-out hop `(1,1,0) → (2,1,0)` the
extra clause is idle because the source max is `1`; corridor-slide already
prices that hop at `3`. On the body hop `(1,0,0) → (1,1,0)` both `ρ3` and
`c2d4` cost `1`. On the interior `3→3` hop `(2,2,2) → (3,2,2)` the
destination has no unit coordinate, so both `ρ3` and `c2d4` cost `1`.

## Theorem 1 — Arrivals For Each Available `k=1..4`

Under `c2d4` on `B_12(0)`, one origin Dijkstra returns the integer arrivals

| site | `t` |
|---|---:|
| `(2,0,0)` | `6` |
| `(1,1,1)` | `5` |
| `(4,0,0)` | `12` |
| `(2,2,2)` | `10` |
| `(6,0,0)` | `18` |
| `(3,3,3)` | `13` |
| `(8,0,0)` | `24` |
| `(4,4,4)` | `16` |

Every listed site lies in `B_12(0)`. The site `(4,4,4)` has coordinate-sum
`12`, so it is absent from `B_11(0)`. The pair is computed on `B_12(0)`, not
copied from a smaller-ball table and not copied from a `ρ3` table. These
values are Dijkstra outputs, not fitted scalars.

A witness walk of cost `6` from `0` to `(2,0,0)` is seed-exit `3` onto
`(1,0,0)` and both-weights-`1` cost `3` onto `(2,0,0)`, summing to `6`.
A witness walk of cost `5` from `0` to `(1,1,1)` is seed-exit `3` onto
`(0,0,1)`, leave-axis `1` onto `(0,1,1)`, and enter-body `1` onto
`(1,1,1)`, summing to `5`. A witness walk of cost `12` from `0` to
`(4,0,0)` is four both-weights-`1` axis hops
`0 → (1,0,0) → (2,0,0) → (3,0,0) → (4,0,0)` of costs `3,3,3,3`, summing
to `12`. A witness walk of cost `10` from `0` to `(2,2,2)` is seed-exit
`3` onto `(0,0,1)`, leave-axis `1` onto `(0,1,1)`, corridor-slide `3` onto
`(0,1,2)`, non-growing `2→2` of cost `1` onto `(0,2,2)`, enter-body `1`
onto `(1,2,2)`, and support-preserving cost-`1` body hop onto `(2,2,2)`,
summing to `10`. A witness walk of cost `18` from `0` to `(6,0,0)` is
six both-weights-`1` axis hops
`0 → (1,0,0) → (2,0,0) → (3,0,0) → (4,0,0) → (5,0,0) → (6,0,0)` of
costs `3,3,3,3,3,3`, summing to `18`. A witness walk of cost `13` from
`0` to `(3,3,3)` is seed-exit `3` onto `(0,0,1)`, leave-axis `1` onto
`(0,1,1)`, corridor-slide `3` onto `(0,1,2)`, non-growing `2→2` of cost
`1` onto `(0,2,2)`, support-preserving cost-`1` onto `(0,2,3)`,
non-growing `2→2` of cost `1` onto `(0,3,3)`, enter-body `1` onto
`(1,3,3)`, and two support-preserving cost-`1` body hops to `(3,3,3)`,
summing to `13`. A witness walk of cost `24` from `0` to `(8,0,0)` is
eight both-weights-`1` axis hops `0 → (1,0,0) → (2,0,0) → (3,0,0) →
(4,0,0) → (5,0,0) → (6,0,0) → (7,0,0) → (8,0,0)` of costs
`3,3,3,3,3,3,3,3`, summing to `24`. A witness walk of cost `16` from `0`
to `(4,4,4)` is seed-exit `3` onto `(0,0,1)`, leave-axis `1` onto
`(0,1,1)`, corridor-slide `3` onto `(0,1,2)`, non-growing `2→2` of cost
`1` onto `(0,2,2)`, support-preserving cost-`1` onto `(0,2,3)`,
enter-body `1` onto `(1,2,3)`, support-preserving cost-`1` onto
`(1,2,4)`, two cost-`1` hops onto `(1,4,4)`, and three
support-preserving cost-`1` body hops to `(4,4,4)`, summing to `16`.
Those walks are witnesses of the listed costs, not uniqueness claims.

A witness that the extra clause is live is the walk seed-exit `3` onto
`(0,1,0)`, unit-cube leave `1` onto `(1,1,0)`, corridor-slide `3` onto
`(1,2,0)`, support-preserving `1` onto `(2,2,0)`, deep-out `1` onto
`(3,2,0)`, skipped max≥3 out-face `1` onto `(4,2,0)`, and max≥4 out-face
`2` onto `(5,2,0)`, summing to `12`. Stopping before the last hop yields
`10`. Stopping at `(3,2,0)` yields `9`. Independently, `t(3,2,0) = 9`,
`t(4,2,0) = 10`, and `t(5,2,0) = 12`. A far-axis witness of cost `33` to
`(12,0,0)` uses one live extra hop `(9,-2,0) → (10,-2,0)` of cost `2`
after a body-side climb to height two; the twelve-hop axis walk would
cost `36`.

## Theorem 2 — Reverse At Each Available Doubled Pair

For each available `k=1,2,3,4` the Euclidean-normalized comparison is
whether

```text
t(2k,0,0)^2 / (4k^2) > t(k,k,k)^2 / (3k^2).
```

Equivalently `3 t(2k,0,0)^2 ? 4 t(k,k,k)^2`. Substituting the computed
times gives

| `k` | `3 t(2k,0,0)^2` | `4 t(k,k,k)^2` | reverse |
|---|---:|---:|---|
| `1` | `108` | `100` | `108 > 100` |
| `2` | `432` | `400` | `432 > 400` |
| `3` | `972` | `676` | `972 > 676` |
| `4` | `1728` | `1024` | `1728 > 1024` |

Arrival per Euclidean length is larger at `(2k,0,0)` than at `(k,k,k)` for
every available `k=1..4`. Doubled pairing reverse under `c2d4` is yes at
each of those four scales. The comparison is displayed, not adopted. The
inequality holds.

## Theorem 3 — No axiom write and no L1 attachment

Do not write c2d4 into Admissibility. Do not attach L1.

Do not write `c2d4` into Admissibility.

The live Admissibility wording names one fixed nearest-neighbor
admissibility rule and does not name `c2d4`, `d4`, `ρ3`, `μ`, or `ν`. This
note proposes no axiom edit. The comparison above is a score of the named
hop-cost against itself at two sites; it is not an attachment of a
coordinate-sum hop-cost. It is not a replacement for first arrival under
a constant hop-cost. Uniqueness is not claimed.

## What This Does Not Claim

- No uniqueness claim is made for this named hop-cost at any available `k`.
- The live `2→2` clause on `B_12(0)` is not a statement about larger hosts.
- No physical identification of `t` as a clock, mass, or force law is made.
- No claim is made that Record locks these arrival times.
- Independent leftovers on larger balls are not used as parents.
- Any statement off `B_12(0)`.
- Any score for a pair that is not `((2k,0,0),(k,k,k))`.
- Any omitted pair among `k=1..4`: both sites of each pair lie in `B_12(0)`.
- Any reuse of the `ρ3` arrival table as a substitute for the `c2d4` Dijkstra.

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

The companion runner builds `B_12(0)`, evaluates the named hop-cost, and
runs one Dijkstra from the origin. It reports `t(2k,0,0)` and `t(k,k,k)`
for each available `k=1..4`, checks the integer form of Theorem 2, checks
that the extra `2→2` clause is live on in-host hops at cost `2`, skips
`(2,2,0) → (3,2,0)` and `(3,2,0) → (4,2,0)` as a new tax, and fires
`(4,2,0) → (5,2,0)` at cost `2`, checks that the live Admissibility wording
does not name `c2d4`, and records the import boundary. Declared review
inputs are this note and the axiom memo only.
