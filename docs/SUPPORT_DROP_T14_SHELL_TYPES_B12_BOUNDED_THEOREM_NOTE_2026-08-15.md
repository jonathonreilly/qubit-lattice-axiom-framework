---
claim_id: support_drop_t14_shell_types_b12_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "G+ types of the t=14 shell under the named support-drop hop-cost on B_12(0) are named. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/support_drop_t14_shell_types_b12_2026_08_15.py
---

# G+ Types Of The t=14 Shell On B_12(0)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** one named nearest-neighbor hop-cost on the ℓ¹ ball `B_12(0)`,
scored only by naming the G+ types of the arrival shell `t=14` and by
asking whether the doubled axis `(8,0,0)` shares that shell with `(4,4,4)`.
**Audit-status authority:** independent audit lane only. This note authors
no audit verdict and predicts none.
**Primary runner:**
[`scripts/support_drop_t14_shell_types_b12_2026_08_15.py`](../scripts/support_drop_t14_shell_types_b12_2026_08_15.py)
**Cache:** none. `cache_write: false`.

## Result Up Front

The isochrone type-count census on `B_12(0)` reported that the `t=14`
shell has 26 G+ types, 15 distinct `|v|_2^2`, and holds `(4,4,4)`. Those
26/15 counts are the investment, not the residual. The residual here is
the lex-sorted list of abs-sorted G+ representatives, each with its site
count, and the yes-or-no question of whether the doubled axis `(8,0,0)`
sits in the same shell.

Write `|σ_v|` for the number of nonzero coordinates of `v ∈ Z^3`. On a
directed nearest-neighbor hop `v → w` still inside `B_12(0)`, the displayed
rule `ν` is

`ν(v→w) = 3` if `|σ_v|=0` or `(|σ_v|=|σ_w|=1)` or `|σ_w| < |σ_v|`,
else `1`.

The first clause is seed-exit. The second is both weights `1`. The third is
support drop. Those three clauses are the whole rule. Uniqueness is not claimed.

The proper cubic group `G+` is the 24 signed-permutation rotations of
determinant `+1`. A G+ type is one `G+` orbit. The representative of an
orbit is its lexicographically maximal first-octant triple (the
lex-sorted list of those abs-sorted 3-tuples is the type list).

One Dijkstra from the origin on `B_12(0)` (2625 sites; 2624 nonzero) gives
a `t=14` shell of 578 sites. Those sites partition into the 26 G+ types
named in Theorem 1. The same arrival function gives `t(8,0,0) = 14` and
`t(4,4,4) = 14`, so the doubled axis and the doubled body diagonal sit
in the same shell.

These named types are not leftover of the 26/15 counts: a pair of
integers does not name the representatives or decide whether `(8,0,0)`
shares the shell.

The census is displayed, not adopted. Do not write `ν` into Admissibility.
Do not attach L1.

## Current Premise Boundary

The Lattice and Admissibility premises are quoted from
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md):

Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
adjacency, standard translations, and proper cubic rotations about each site.

There is one fixed nearest-neighbor admissibility rule, covariant under lattice
translations and proper cubic rotations.

For each site, the probability distribution over the possibilities is
determined by, and varies with, the nearest-neighbor conditions.

Lattice supplies the six-neighbor graph and the ball. Admissibility supplies
none of the hop costs. The integers `3` and `1`, the support-size clauses,
and the arrival function `t` are separately displayed mathematical inputs.
No axiom text is edited.

## Named Rule And Type Convention

Let `B_12(0) = { v ∈ Z^3 : |v|_1 ≤ 12 }`. Directed edges are the six
nearest-neighbor steps whose both ends lie in the ball. For `v ∈ B_12(0)`,
`t(v)` is the least sum of `ν` along a directed path from `0` to `v` in
that graph.

A G+ type is represented by the lexicographically maximal first-octant
member of its orbit. The type list of a shell is those representatives
sorted in lexicographic order. Absolute-coordinate first-octant form does
not merge chiral pairs: `(5,3,4)` and `(5,4,3)` remain distinct `G+`
orbits.

## Theorem 1 — Named G+ Types On The t=14 Shell

One origin Dijkstra on `B_12(0)` reaches every site. The `t=14` shell has
578 sites. The lex-sorted abs-sorted G+ representatives, each with site
count, are

| representative | site count |
|---|---:|
| `(4,4,4)` | 8 |
| `(5,3,4)` | 24 |
| `(5,4,3)` | 24 |
| `(5,5,2)` | 24 |
| `(6,1,5)` | 24 |
| `(6,2,4)` | 24 |
| `(6,3,3)` | 24 |
| `(6,4,2)` | 24 |
| `(6,5,1)` | 24 |
| `(6,6,0)` | 12 |
| `(7,1,4)` | 24 |
| `(7,2,3)` | 24 |
| `(7,3,2)` | 24 |
| `(7,4,1)` | 24 |
| `(7,5,0)` | 24 |
| `(8,0,0)` | 6 |
| `(8,1,3)` | 24 |
| `(8,2,2)` | 24 |
| `(8,3,1)` | 24 |
| `(8,4,0)` | 24 |
| `(9,1,2)` | 24 |
| `(9,2,1)` | 24 |
| `(9,3,0)` | 24 |
| `(10,1,1)` | 24 |
| `(10,2,0)` | 24 |
| `(11,1,0)` | 24 |

Those twenty-six orbits partition the 578 sites.

B_12(0) only. The named types are displayed, not adopted.

## Theorem 2 — Doubled Axis And Doubled Body Diagonal

The same Dijkstra gives `t(8,0,0) = 14` and `t(4,4,4) = 14`. So `(8,0,0)` and `(4,4,4)` both have `t=14`, and both appear in the type list of Theorem 1.

Both facts are displayed, not adopted.

## Theorem 3 — Displayed, Not Adopted

The rule `ν` is a displayed scoring device on `B_12(0)`. Do not write `ν`
into Admissibility. Do not attach L1. The named G+ types are not offered
as a unique hop-cost property and are not a replacement for unit-cost
first arrival.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The t=14 G+ types of B_12(0) are named for one displayed hop-cost, including the shared-shell fact for (8,0,0) and (4,4,4). The rule is displayed, not adopted."
trace_class: frontier_discovery
artifact_role: theorem
conditional_surface_status: "exact on B_12(0) for the displayed rule ν; no Admissibility edit; not attached to L1"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## What This Note Does Not Claim

- Uniqueness of `ν` among hop-costs with this type list.
- Any edit of Lattice, Qubit, Admissibility, or Record.
- Any attachment to L1.
- Any continuum potential, any inverse-power kernel, and any gravitational
  identification.
- Any statement off `B_12(0)`.
- Any reuse of the 26/15 counts as a substitute for the named type list.
