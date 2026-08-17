---
claim_id: support_drop_t8_mixed_shell_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "The G+ site-types that share arrival t=8 under the named support-drop hop-cost on B_6(0) are named. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/support_drop_t8_mixed_shell_2026_08_15.py
---

# G+ Types Sharing Arrival t=8 Under The Named Support-Drop Hop-Cost

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** the lex-sorted G+ representatives that share first-arrival `t=8`
on the closed taxicab ball `B_6(0)` under the named support-drop hop-cost
`ν`. Displayed, not adopted. B_6(0) only.
**Audit-status authority:** independent audit lane only. This note writes no
audit verdict and predicts none.
**Primary runner:**
[`scripts/support_drop_t8_mixed_shell_2026_08_15.py`](../scripts/support_drop_t8_mixed_shell_2026_08_15.py)

## Result up front

A prior isochrone census on the same ball showed that the constant-`t` shells
at `t=5,6,7,8` each mix more than one Euclidean radius. That mixed-shell bit
is the investment, not the residual. The residual here is to *name* the
proper-cubic site-types that occupy the reverse-critical shell containing
`(2,2,2)`.

On `B_6(0)={v∈Z^3:|v|_1≤6}`, six-neighbor hops are assigned the named cost

```text
ν(v→w) = 3  if |σ_v|=0 or (|σ_v|=|σ_w|=1) or |σ_w|<|σ_v|,
         1  otherwise,
```

where `σ_v={i:v_i≠0}` and `|σ_v|` is the number of nonzero coordinates.
One Dijkstra from the origin gives first-arrival `t`. In particular
`t(2,2,2)=8` and `t(4,0,0)=10`, so `t=8` is the reverse-critical shell.

The proper cubic group `G+` is the 24 signed-permutation rotations of
determinant `+1`. A G+ site-type is one `G+` orbit. The representative of an
orbit is its lexicographically maximal triple. The lex-sorted list of G+
representatives with `t=8`, each with `|v|_2^2` and orbit size, is

| representative | `|v|_2^2` | orbit size |
|---|---:|---:|
| `(2,2,2)` | 12 | 8 |
| `(3,1,2)` | 14 | 24 |
| `(3,2,1)` | 14 | 24 |
| `(3,3,0)` | 18 | 12 |
| `(4,1,1)` | 18 | 24 |
| `(4,2,0)` | 20 | 24 |
| `(5,1,0)` | 26 | 24 |

Those seven orbits partition the 140 sites with `t=8`. The list uses five
distinct Euclidean squared radii `{12,14,18,20,26}`. Displayed, not adopted.
Do not write ν into Admissibility. Do not attach L1.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The t=8 G+ representatives, Euclidean squared radii, and orbit sizes are a finite first-arrival census on B_6(0). The hop-cost is a named displayed rule, not an axiom clause."
trace_class: upstream_support
target_claim_id: cube_covariant_hop_cost_physical_selection
target_blocker_text: "select a physical hop-cost from Admissibility rather than display a named finite rule"
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "keep ν outside Admissibility; do not promote the mixed t=8 shell to a physical isochrone law"
conditional_surface_status: "exact for one Dijkstra of the named support-drop hop-cost on B_6(0); no law selection, no L1 attachment, no axiom edit"
hypothetical_axiom_status: no edit
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Premises and declared objects

The only scientific dependency is the current four-axiom authority
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md).

Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
adjacency, standard translations, and proper cubic rotations about each site.

There is one fixed nearest-neighbor admissibility rule, covariant under lattice
translations and proper cubic rotations.

For each site, the probability distribution over the possibilities is
determined by, and varies with, the nearest-neighbor conditions.

When present, a record locks exactly one admissible local possibility.

Record is not used. The hop-cost `ν` is not that Admissibility rule. It is a
separately named integer weight on already-present six-neighbor edges. The
axioms do not select `ν`, do not select first-arrival `t`, and do not select
an Euclidean radius as a physical clock.

Declared mathematical scaffolding, not measured physics:

- the closed taxicab ball `B_6(0)` of 377 integer sites;
- the induced six-neighbor graph of that ball;
- the 24-element proper cubic group `G+`;
- the named three-clause cost `ν` written above;
- one Dijkstra first-arrival `t` from the origin.

No observational comparator, continuum limit, or Record readout is imported.

## Theorem 1 — Lex-sorted t=8 G+ representatives

Run one Dijkstra for `ν` on the induced six-neighbor graph of `B_6(0)`.
Every site is reachable. The body-diagonal type has `t(2,2,2)=8`. Every
other site of that `G+` orbit has the same arrival, so the whole
eight-point type sits on the reverse-critical shell.

Grouping the 140 sites with `t=8` by `G+` orbits yields exactly the seven
representatives in the table above, already written in lexicographic order.
Each listed orbit lies entirely inside `B_6(0)`, and `t` is constant on
each orbit. The two chiral types `(3,1,2)` and `(3,2,1)` are distinct
`G+` orbits of size 24; a determinant-`+1` signed permutation cannot send
one to the other.

The table reports `|v|_2^2` rather than a floating Euclidean length. The
five exact squared lengths are `12,14,18,20,26`.

## Theorem 2 — More than one Euclidean radius, displayed not adopted

The seven-type list is not a single Euclidean sphere. The squared radii
`{12,14,18,20,26}` are five distinct values, so the `t=8` shell mixes
Euclidean radii. In particular `(2,2,2)` has squared radius `12` while
`(5,1,0)` has squared radius `26`. The pair `(3,3,0)` and `(4,1,1)`
share squared radius `18` but remain distinct `G+` types, with orbit
sizes `12` and `24`.

This is the named content of the residual: the mixed-shell bit is refined
to an explicit type list. The list is displayed, not adopted. It is not a
physical isochrone law, not a selection of `ν` as the Admissibility
rule, and not a continuum radius coordinate.

## Theorem 3 — ν stays outside Admissibility; L1 is not attached

Do not write ν into Admissibility. The Admissibility axiom determines a
local probability distribution from nearest-neighbor *conditions on the
possibility domain*. It does not assign integer hop costs, first-arrival
times, or Euclidean radii.

Do not attach L1. Arrival `t` is not taxicab length: the seed exit
`0→(1,0,0)` already costs `3`, and `t(2,2,2)=8` is not `|v|_1=6`. The
present census does not identify `ν` with unit-cost nearest-neighbor
length, does not replace Lattice adjacency by a different stencil, and
does not promote `t` to a physical clock.

Displayed, not adopted.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice, Admissibility, and Record wording | quoted; no edit |
| named support-drop hop-cost `ν` | reconstructed as the three-clause rule; displayed only |
| one Dijkstra on `B_6(0)` | executed |
| `t(2,2,2)=8` reverse-critical shell | executed |
| lex-sorted G+ representatives at `t=8` | executed; seven types |
| `|v|_2^2` and orbit size for each type | executed |
| more than one Euclidean radius | executed; five squared radii |
| write `ν` into Admissibility | refused |
| attach L1 | refused |
| law outside `B_6(0)` | not claimed |

## Boundary and imports

The theorem uses only the current Lattice graph, the named displayed
hop-cost, and the 24 proper cubic rotations. It does not import a
physical Admissibility kernel, a Record content map, a continuum radius,
or any hop-cost other than `ν`. Uniqueness of `ν` is not claimed.

## Promotion value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It names the G+ types on the reverse-critical `t=8` shell, which the mixed-shell census left unnamed. |
| V2 | Current main has the four axioms and no landed type list for this hop-cost on `B_6(0)`. |
| V3 | The census is finite and exact: one Dijkstra on 377 sites. |
| V4 | Naming the seven types is not a restatement of Admissibility and not a restatement of the mixed-shell bit. |
| V5 | The hop-cost remains displayed. It is not a physical compiler and is not written into any axiom. |

## No-Go Discipline Gate

The negative content is narrow: the named `t=8` shell is not a single
Euclidean sphere, and the displayed hop-cost is not an axiom clause.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| unit-cost six-neighbor length | attach L1 as the arrival | **RULED OUT BY EXECUTION**: `t≠|v|_1` already at `(1,0,0)` and `(2,2,2)` |
| write `ν` into Admissibility | treat hop-cost as the local possibility law | **ATTEMPTED** and refused; different object |
| unsigned coordinate type | merge `(3,1,2)` with `(3,2,1)` | **ATTEMPTED**; those are two G+ orbits |
| single Euclidean sphere at `t=8` | claim one radius | **RULED OUT BY EXECUTION**; five squared radii |
| leave the ball | Dijkstra on a larger patch | different domain; B_6(0) only |
| adopt `ν` as physical law | uniqueness or axiom edit | **ATTEMPTED** and refused |

### N2 — wall independence

The missing physical hop-cost selector, the missing Admissibility-to-cost
bridge, and the missing clock identification are distinct open premises.
This note claims no complete wall and no compiler impossibility.

### N3 — hidden-condition scan

The ball, the six-neighbor stencil, the three-clause cost, the 24-element
group, the lex-max representative convention, and the single Dijkstra are
declared. No continuum radius, no L1 identification, and no axiom edit
are assumed.

### N4 — source residual matching

The current axiom memo supplies the cubic graph and proper cubic
rotations used here. It does not supply `ν`. The residual is therefore a
displayed census on that graph, not an axiom consequence.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | each t=8 G+ representative | no classification of other shells |
| per site | first-arrival on `B_6(0)` | no law outside the ball |
| per mode | not used | no spectral claim |
| per block | seven-orbit partition of the 140-site shell | no physical isochrone law |
| lattice wide | checked and not executed | no `Z^3`-wide adoption of `ν` |

### N6 — live partial-closure paths

Live routes are an independently derived physical hop-cost, a derived
bridge from Admissibility conditions to integer edge weights, and a
derived clock identification. None of those is closed here.

### N7 — hostile steelman

**Steelman:** Once the mixed-shell bit is known, naming the `t=8` types
is leftover bookkeeping.

**Answer:** The mixed-shell bit says only that several radii occur. It
does not name the G+ types, does not split the chiral pair, and does not
report orbit sizes. Those are the residual.

### N8 — cross-cycle echo

The investment that `t=5,6,7,8` mix Euclidean radii is used only as
motivation. This note does not re-score those other shells and does not
adopt their mixing as a physical law.

**Gate disposition:** PASS for the finite `t=8` type list and the two
refusals above. FAIL / DO NOT SHIP for “`ν` is the Admissibility rule,”
“attach L1,” or “the `t=8` shell is a single Euclidean sphere.”

## Primary runner

The primary runner rebuilds `B_6(0)`, applies one Dijkstra for `ν`,
groups the `t=8` sites by `G+` orbits, and checks the lex-sorted table,
the mixed-radius statement, the axiom-boundary refusals, and the
dispatch-forbidden phrases. It writes no cache and authors no audit
verdict.
