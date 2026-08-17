---
claim_id: support_drop_t8_paths_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "A shortest path under the named support-drop hop-cost is exhibited to each t=8 G+ representative on B_6(0). Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/support_drop_t8_paths_2026_08_15.py
---

# Lex-First Shortest Paths To The t=8 G+ Representatives

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** one named nearest-neighbor hop-cost on the closed taxicab ball
`B_6(0)`, and a lex-first shortest path from the origin to each of the
seven G+ representatives that share first-arrival `t=8`. Displayed, not
adopted. B_6(0) only.
**Audit-status authority:** independent audit lane only. This note authors
no audit verdict and predicts none.
**Primary runner:**
[`scripts/support_drop_t8_paths_2026_08_15.py`](../scripts/support_drop_t8_paths_2026_08_15.py)
**Cache:** none. `cache_write: false`.

## Result Up Front

A prior census on the same ball named seven proper-cubic site-types on
the reverse-critical shell `t=8`. That type list is the investment, not
the residual. The residual here is a lex-first shortest path from the
origin to each of those seven representatives, together with the hop-cost
list and hop-cost multiset along that path. The path exhibition is not
leftover of the type list: a type name does not supply a walk or a
hop-cost word.

Write `|σ_v|` for the number of nonzero coordinates of `v ∈ Z^3`. On a
directed nearest-neighbor hop `v → w` still inside `B_6(0)`, the displayed
rule `ν` is

`ν(v→w) = 3` if `|σ_v|=0` or `(|σ_v|=|σ_w|=1)` or `|σ_w| < |σ_v|`,
else `1`.

The first clause is seed-exit. The second is both weights `1`. The third
is support drop. Those three clauses are the whole rule. Uniqueness is
not claimed.

One Dijkstra from the origin on `B_6(0)` (377 sites; 376 nonzero), keeping
the lexicographically first site sequence among least-cost walks, returns
the seven paths below. Each hop-cost list is `3,1,1,1,1,1`. Each list
sums to `8`. Each hop-cost multiset is `{1,1,1,1,1,3}`.

The rule and the paths are displayed, not adopted. Do not write ν into
Admissibility. Do not attach L1.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "A lex-first shortest path and hop-cost list summing to 8 are exhibited to each of the seven t=8 G+ representatives on B_6(0). The hop-cost is a named displayed rule, not an axiom clause."
trace_class: frontier_discovery
artifact_role: theorem
conditional_surface_status: "exact on B_6(0) for the displayed rule ν; no Admissibility edit; not attached to L1"
hypothetical_axiom_status: no edit
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Current Premise Boundary

The Lattice and Admissibility premises are quoted from
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md):

Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
adjacency, standard translations, and proper cubic rotations about each site.

There is one fixed nearest-neighbor admissibility rule, covariant under lattice
translations and proper cubic rotations.

For each site, the probability distribution over the possibilities is
determined by, and varies with, the nearest-neighbor conditions.

When present, a record locks exactly one admissible local possibility.

Record is not used. Lattice supplies the six-neighbor graph and the ball.
Admissibility supplies none of the hop costs. The integers `3` and `1`,
the support-size clauses, first-arrival `t`, and the seven walks are
separately displayed mathematical inputs. No axiom text is edited.

## Named Rule And Lex Convention

Let `B_6(0) = { v ∈ Z^3 : |v|_1 ≤ 6 }`. Directed edges are the six
nearest-neighbor steps whose both ends lie in the ball. For `v ∈ B_6(0)`,
`t(v)` is the least sum of `ν` along a directed path from `0` to `v` in
that graph.

The proper cubic group `G+` is the 24 signed-permutation rotations of
determinant `+1`. A G+ site-type is one `G+` orbit. The representative of
an orbit is its lexicographically maximal first-octant member. The seven
representatives with `t=8` are

`(2,2,2)`, `(3,1,2)`, `(3,2,1)`, `(3,3,0)`, `(4,1,1)`, `(4,2,0)`, `(5,1,0)`.

A path is a finite sequence of sites. Among shortest `0 → v` paths, the
lex-first path is the least sequence in the dictionary order of integer
triples. That convention is displayed data for the theorems below.

## Theorem 1 — Lex-First Shortest Path And Hop-Cost List To Each Type

On `B_6(0)`, the lex-first shortest path from `0` to each `t=8`
representative, the hop-cost list along that path, and the hop-cost
multiset are:

| representative | lex-first path | hop-cost list | multiset | sum |
|---|---|---|---|---:|
| `(2,2,2)` | `(0,0,0) → (0,0,1) → (0,1,1) → (0,1,2) → (0,2,2) → (1,2,2) → (2,2,2)` | `3,1,1,1,1,1` | `{1,1,1,1,1,3}` | 8 |
| `(3,1,2)` | `(0,0,0) → (0,0,1) → (0,1,1) → (0,1,2) → (1,1,2) → (2,1,2) → (3,1,2)` | `3,1,1,1,1,1` | `{1,1,1,1,1,3}` | 8 |
| `(3,2,1)` | `(0,0,0) → (0,0,1) → (0,1,1) → (0,2,1) → (1,2,1) → (2,2,1) → (3,2,1)` | `3,1,1,1,1,1` | `{1,1,1,1,1,3}` | 8 |
| `(3,3,0)` | `(0,0,0) → (0,1,0) → (1,1,0) → (1,2,0) → (1,3,0) → (2,3,0) → (3,3,0)` | `3,1,1,1,1,1` | `{1,1,1,1,1,3}` | 8 |
| `(4,1,1)` | `(0,0,0) → (0,0,1) → (0,1,1) → (1,1,1) → (2,1,1) → (3,1,1) → (4,1,1)` | `3,1,1,1,1,1` | `{1,1,1,1,1,3}` | 8 |
| `(4,2,0)` | `(0,0,0) → (0,1,0) → (1,1,0) → (1,2,0) → (2,2,0) → (3,2,0) → (4,2,0)` | `3,1,1,1,1,1` | `{1,1,1,1,1,3}` | 8 |
| `(5,1,0)` | `(0,0,0) → (0,1,0) → (1,1,0) → (2,1,0) → (3,1,0) → (4,1,0) → (5,1,0)` | `3,1,1,1,1,1` | `{1,1,1,1,1,3}` | 8 |

Each walk uses six nearest-neighbor hops inside `B_6(0)`. Each hop-cost
list sums to `8`, which equals the Dijkstra arrival `t` of that
representative. The type list named the endpoints; it did not name these
walks. The residual is therefore not leftover of the type list.

## Theorem 2 — Every Exhibited Path Starts With A Cost-3 Seed-Exit

Every path in the Theorem 1 table starts with a seed-exit hop of cost
`3`. Explicitly, the first hop is one of `0 → (0,0,1)` or `0 → (0,1,0)`,
both of which have `|σ_0|=0` and therefore cost `3` under `ν`. The
remaining five hops on each exhibited path cost `1`. Displayed, not
adopted.

This is a statement about the seven lex-first shortest paths, not a
selection of `ν` as a physical law and not an attachment of L1.

## Theorem 3 — Displayed, Not Adopted

Do not write ν into Admissibility. The live Admissibility sentences remain
the quoted nearest-neighbor distribution rule. They do not name inward
weights, seed-exit, support drop, or a numerical hop-cost.

Do not attach L1. Arrival `t` is not taxicab length: the seed-exit already
costs `3`, and each exhibited sum is `8` while the taxicab lengths of the
seven representatives are `6,6,6,6,6,6,6`. The integer `8` is the
orbit-cost sum along each exhibited path, not an L1 length.

The rule and the seven paths are displayed, not adopted. Uniqueness of
`ν` among hop-costs is not claimed.

## Exact Target And Obligation Graph

| Obligation | Status |
|---|---|
| current Lattice, Admissibility, and Record wording | quoted; no edit |
| named support-drop hop-cost `ν` | reconstructed as the three-clause rule; displayed only |
| one Dijkstra on `B_6(0)` with lex-first paths | executed |
| lex-first shortest path to each of the seven types | executed |
| hop-cost list and multiset, each summing to `8` | executed |
| every exhibited path starts with a cost-3 seed-exit | executed |
| write `ν` into Admissibility | refused |
| attach L1 | refused |
| leftover of the type list | refused; the type list does not exhibit walks |
| law outside `B_6(0)` | not claimed |

## What This Note Does Not Claim

- Uniqueness of `ν` among hop-costs that reach these sites at arrival `8`.
- Any edit of Lattice, Qubit, Admissibility, or Record.
- Any attachment to L1.
- Any continuum potential, any inverse-power kernel, and any gravitational
  identification.
- Any statement off `B_6(0)`.
- That every shortest path, as opposed to the lex-first one, is exhibited.

## Live Parent Quotes

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

> There is one fixed nearest-neighbor admissibility rule, covariant under lattice
> translations and proper cubic rotations.

> For each site, the probability distribution over the possibilities is
> determined by, and varies with, the nearest-neighbor conditions.

Their dependency role is limited to the repository's lattice and
admissibility vocabulary. This theorem separately supplies the named
hop-cost and the seven walks as displayed data. No axiom sentence is
edited.

## Primary Runner

The primary runner rebuilds `B_6(0)`, applies one Dijkstra for `ν` that
retains the lex-first shortest path to every site, checks the seven
representatives, checks each hop-cost list and sum, checks the seed-exit
clause, and checks the axiom-boundary refusals and the dispatch-forbidden
phrases. It writes no cache and authors no audit verdict.
