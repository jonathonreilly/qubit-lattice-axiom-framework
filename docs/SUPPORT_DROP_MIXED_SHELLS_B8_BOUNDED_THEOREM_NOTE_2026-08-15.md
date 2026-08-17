---
claim_id: support_drop_mixed_shells_b8_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Mixed t=const shells under the named support-drop hop-cost on B_8(0) are named. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/support_drop_mixed_shells_b8_2026_08_15.py
---

# Mixed t=const Shells Of The Named Support-Drop Hop-Cost On B_8(0)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** one Dijkstra arrival field for a named six-neighbor hop-cost on the
closed ℓ¹ ball of radius 8 in `Z^3`. The mixed `t`-constant shells are named
by arrival value, site count, and number of distinct Euclidean radii. The
cost and the census are displayed, not adopted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/support_drop_mixed_shells_b8_2026_08_15.py`](../scripts/support_drop_mixed_shells_b8_2026_08_15.py)

## Result Up Front

On `B_8(0)={v in Z^3 : |v|_1 <= 8}` (833 sites), let `σ_v` be the set of
nonzero coordinates of `v`, and write `|σ_v|` for its cardinality. On the
six-neighbor graph restricted to this ball, the named support-drop hop-cost is

```text
ν(v → w) = 3  if |σ_v|=0 or (|σ_v|=|σ_w|=1) or |σ_w| < |σ_v|,
         = 1  otherwise.
```

Let `t` be first-arrival time from the origin under one Dijkstra with this
cost. The 832 nonzero sites carry exactly twelve distinct arrival values

```text
{3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 16}.
```

Six of those twelve values are single Euclidean radii. The other six mix
more than one `|v|_2^2`. Those mixed arrivals, named rather than left as a
six-of-twelve bit, are:

| `t` | sites | distinct `|v|_2^2` | the set of `|v|_2^2` |
|---|---:|---:|---|
| `t=5` | 32 | 2 | `{3, 5}` |
| `t=6` | 66 | 4 | `{4, 6, 8, 10}` |
| `t=7` | 96 | 4 | `{9, 11, 13, 17}` |
| `t=8` | 140 | 5 | `{12, 14, 18, 20, 26}` |
| `t=9` | 198 | 8 | `{9, 17, 19, 21, 25, 27, 29, 37}` |
| `t=10` | 258 | 10 | `{16, 22, 24, 26, 30, 32, 34, 38, 40, 50}` |

The reverse-critical shell `t=8` is present and is among the mixed shells:
it holds 140 sites and five distinct radii, and it contains the body-diagonal
type `(2,2,2)` with `|v|_2^2=12`. Displayed, not adopted.

Do not write `ν` into Admissibility. Do not attach L1. The named cost is
not attached as a hop-cost law.

## Named Objects

`B_8(0)` is the closed ℓ¹ ball of radius 8. Lattice supplies nearest-neighbor
adjacency and the proper cubic rotations about each site. The hop-cost `ν` is
not Admissibility content: Admissibility supplies one fixed nearest-neighbor
probability rule and does not name a path metric, a seed-exit penalty, an
axis-skeleton penalty, or a support-drop penalty.

The three clauses of `ν` are:

1. seed-exit: `|σ_v|=0`, the unique hop leaving the origin;
2. both-weights-1: `|σ_v|=|σ_w|=1`, a hop along the coordinate-axis 1-skeleton;
3. support drop: `|σ_w| < |σ_v|`, a hop that strictly decreases the number of
   occupied axes.

Each expensive clause costs 3; every other six-neighbor hop that stays in the
ball costs 1. Uniqueness of this cost among all integer hop-costs is not
claimed.

A `t`-constant shell is the set of nonzero sites with a fixed arrival. It is
mixed when that set contains more than one value of `|v|_2^2`. Euclidean
radius enters only as that diagnostic. No inverse-power radial law is used.

The phrase reverse-critical `t=8` names the unique shell that contains the
body-diagonal type `(2,2,2)` under this displayed cost. This note does not
re-score the diamond comparison and does not adopt that shell as a physical
clock.

## Theorem 1 — Named Mixed Arrival Values

One Dijkstra on the 833-site graph produces a unique finite arrival `t(v)` at
every site. Restricting to `B_8(0)\{0}` yields twelve arrival values. The
six mixed values, with site counts and distinct-radius counts computed on
this ball, are exactly the table above.

The same census written as named rows:

- `t=5`: 32 sites, 2 distinct `|v|_2^2`, set `{3, 5}`.
- `t=6`: 66 sites, 4 distinct `|v|_2^2`, set `{4, 6, 8, 10}`.
- `t=7`: 96 sites, 4 distinct `|v|_2^2`, set `{9, 11, 13, 17}`.
- `t=8`: 140 sites, 5 distinct `|v|_2^2`, set `{12, 14, 18, 20, 26}`.
- `t=9`: 198 sites, 8 distinct `|v|_2^2`, set `{9, 17, 19, 21, 25, 27, 29, 37}`.
- `t=10`: 258 sites, 10 distinct `|v|_2^2`, set `{16, 22, 24, 26, 30, 32, 34, 38, 40, 50}`.

Site counts sum to 790. The remaining 42 nonzero sites occupy the six
single-radius arrivals `t in {3, 4, 11, 12, 13, 16}` and are not the target
of this note.

The first mixed shell is already `t=5`, which joins the body-diagonal type
`(1,1,1)` (`|v|_2^2=3`) to the type `(2,1,0)` (`|v|_2^2=5`). The largest
mixed shell is `t=10`, which joins ten radii including the axis type
`(4,0,0)` (`|v|_2^2=16`). These identities are computed on `B_8(0)` itself.
They are not leftovers of a mixed-shell bit that only said six of twelve mix.

## Theorem 2 — Reverse-Critical `t=8` Is Mixed

The shell `t=8` is present on this ball. It is not single-radius: it
contains five distinct `|v|_2^2` values `{12, 14, 18, 20, 26}` on 140 sites.
The body-diagonal type `(2,2,2)` arrives at `t=8` with `|v|_2^2=12`, so this
is the reverse-critical shell of the named cost.

That shell is among the six mixed arrivals of Theorem 1. The statement is
displayed, not adopted: naming the shell and recording that it mixes five
radii does not select a physical time metric, a diamond law, or a Record
readout.

## Theorem 3 — Boundary

Do not write `ν` into Admissibility. The current axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) names one
fixed nearest-neighbor admissibility rule by which, for each site, the
probability distribution over local possibilities is determined by, and varies
with, the nearest-neighbor conditions. That clause does not supply hop-costs,
arrival times, mixed shells, or a preferred path metric. This note does not
amend the axiom memo.

Do not attach L1. The mixed-shell census is a property of the named cost
alone. An ℓ¹ arrival is not used, not scored, and not attached.

The named cost is a displayed scoring rule on `B_8(0)`. It is not adopted as
a dynamics, a time metric, a clock, or a Record readout.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "One Dijkstra on B_8(0) names the six mixed t-constant shells by arrival, site count, and distinct |v|_2^2. The named cost remains displayed, not adopted."
trace_class: bounded_positive
artifact_role: theorem
conditional_surface_status: "exact on the named hop-cost restricted to B_8(0); no axiom or time-metric closure"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Proof-Obligation Graph

| Obligation | Disposition |
|---|---|
| name `B_8(0)` and the six-neighbor graph | closed: ℓ¹ ball of radius 8, 833 sites |
| name `ν` by the three support-weight clauses | closed: seed-exit, both-weights-1, support drop |
| compute one Dijkstra arrival field | closed by the primary runner |
| list every mixed `t` on `B_8(0)\{0}` | closed: `{5, 6, 7, 8, 9, 10}` |
| report distinct `|v|_2^2` count and site count for each mixed `t` | closed: table above |
| decide whether reverse-critical `t=8` is mixed | closed: mixed, five radii, 140 sites |
| write `ν` into Admissibility | refused |
| attach L1 | refused |
| adopt `ν` as a physical time metric | outside the claim |

The obligation graph is acyclic. Every leaf of the bounded report is closed
on `B_8(0)`. Axiom edits, adoption, and any statement outside this ball are
not proof leaves.

## Imports And Claim Boundary

| Item | Role | Provenance / status |
|---|---|---|
| Lattice nearest-neighbor adjacency | graph of the ball | current minimal axiom memo |
| Admissibility | negative boundary only | current minimal axiom memo; not a hop-cost |
| `ν` | named displayed hop-cost | declared in this note |
| `B_8(0)` | declared finite domain | 833 integer sites |
| ℓ¹ arrival | not used | not attached |

There are no measured, fitted, literature, or observational inputs. The
result does not select a physical clock, a Lorentzian reconstruction, or a
Record-to-time bridge.

## Review Record

The residual asked for the mixed arrival values of the named support-drop
hop-cost on `B_8(0)`, together with the number of distinct `|v|_2^2` in each
shell, not for a leftover mixed-shell bit and not for an adopted law. The
durable content is the six-row census and the display that `t=8` is mixed.
No axiom sentence is added.
