---
claim_id: clause_011_reverse_paths_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Shortest paths under the named (0,1,1) clause-toggle that reverse diamond on B_6(0) are exhibited. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/clause_011_reverse_paths_2026_08_15.py
---

# Clause `(0,1,1)` Reverse Paths On The Radius-Six Ball

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** lex-first minimum-cost walks from the origin to `(4,0,0)` and to
`(2,2,2)` on the closed radius-six nearest-neighbor ball, under the named
clause-toggle with cheap seed-exit and expensive axis-one and support-drop
hops. The rule is displayed, not adopted. The walks are not leftover of the
two arrival numbers.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/clause_011_reverse_paths_2026_08_15.py`](../scripts/clause_011_reverse_paths_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

Work on the cubic lattice `Z^3` with nearest-neighbor adjacency. Write
`B_6(0)` for the closed ball `{v ∈ Z^3 : |v|_1 ≤ 6}`. Hops that would leave
the ball are absent. For a site `v`, write `σ_v` for the set of nonzero
coordinates and write the inward weight `w(v) = |σ_v|`.

A directed nearest-neighbor hop `v → u` is classified by three named clauses:

- seed-exit when `w(v) = 0`,
- both-weights-one (axis-one) when `w(v) = w(u) = 1`,
- support-drop when `w(u) < w(v)`.

The displayed clause-toggle `(s,a,d) = (0,1,1)` charges cost `3` if
both-weights-one holds or support-drop holds, and charges cost `1` otherwise.
Seed-exit is therefore cheap. This is a finite named hop-cost on `B_6(0)`. It
is not written into Admissibility, and it is not the uniform graph-length
rule that charges `1` on every nearest-neighbor hop.

Three exact statements survive review.

1. The lex-first shortest walk `0 → (4,0,0)` is
   `(0,0,0) → (0,-1,0) → (1,-1,0) → (2,-1,0) → (3,-1,0) → (4,-1,0) → (4,0,0)`
   with hop-cost list `(1,1,1,1,1,3)` summing to `8`. The lex-first shortest
   walk `0 → (2,2,2)` is
   `(0,0,0) → (0,0,1) → (0,1,1) → (0,1,2) → (0,2,2) → (1,2,2) → (2,2,2)`
   with hop-cost list `(1,1,1,1,1,1)` summing to `6`. Those arrival numbers
   reverse the two-point comparison `(4,0,0)` versus `(2,2,2)`.
2. Both displayed walks begin with a cost-`1` seed-exit. The first hop is
   not an axis-one hop and is not a support-drop.
3. The clause-toggle is displayed, not adopted. It is not written into
   Admissibility. The uniform graph-length comparator is not attached as a
   physical time.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact Dijkstra reconstruction exhibits the lex-first minimum-cost walks to the two reverse-diamond sites under the named (0,1,1) clause-toggle on B_6(0). The rule and the walks are displayed, not adopted."
trace_class: frontier_discovery
target_claim_id: clause_011_reverse_paths
target_blocker_text: "exhibit lex-first shortest paths that reverse diamond under the cheap-seed (0,1,1) clause-toggle"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the exhibited walks; do not write the clause-toggle into Admissibility and do not attach uniform graph-length as physical time"
conditional_surface_status: "exact for the named (0,1,1) hop-cost on B_6(0); other clause triples, other radii, and any physical selector remain unclaimed"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Target And Proof Obligations

**Exact target.** On `B_6(0)` under the named `(0,1,1)` hop-cost, exhibit the
lex-first shortest walks from the origin to `(4,0,0)` and to `(2,2,2)`, record
the hop-cost lists, confirm the lists sum to the arrival numbers `8` and `6`,
and confirm that both walks start with a cost-`1` seed-exit. Do not treat the
two arrival numbers as a substitute for the walks. Do not write the
clause-toggle into Admissibility. Do not attach the uniform graph-length
comparator.

| Obligation | Disposition |
|---|---|
| named `(0,1,1)` hop-cost on `B_6(0)` | defined here; executed in Theorem 1 |
| lex-first shortest walk `0 → (4,0,0)` with costs summing to `8` | proved here in Theorem 1 |
| lex-first shortest walk `0 → (2,2,2)` with costs summing to `6` | proved here in Theorem 1 |
| both walks start with a cost-`1` seed-exit | proved here in Theorem 2 |
| walks are not leftover of the two-point times | proved here in Theorem 1 by exhibiting the hops |
| clause-toggle not written into Admissibility | Theorem 3 |
| uniform graph-length not attached | Theorem 3 |

Boundary cases are not hidden. The axis-only walk
`(0,0,0) → (1,0,0) → (2,0,0) → (3,0,0) → (4,0,0)` has hop-cost list
`(1,3,3,3)` and sums to `10`, so it is not shortest. Charging seed-exit `3`
as well recovers a different named triple and different arrivals. Other
radii, other destinations, and any selector that would adopt the
clause-toggle as the framework's nearest-neighbor rule are outside the
target.

## Inputs And Support Inventory

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies the
  cubic nearest-neighbor substrate and the one-fixed-rule Admissibility
  sentence. As the registered `minimal_axioms` premise, it is not a
  bounded-status source.
- The three clause names (seed-exit, both-weights-one, support-drop) and the
  toggle `(s,a,d) = (0,1,1)` are displayed mathematical hypotheses, not
  framework-derived physical selectors.
- No approved primitive is used. Scale reference, kinetic isotropy, and
  realized-state evaluation are not inputs.
- The uniform graph-length comparator that charges `1` on every
  nearest-neighbor hop is a disclosed contrast only. It is not attached.

## Current Premise Boundary

The Lattice and Admissibility premises are quoted from
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md):

Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
adjacency, standard translations, and proper cubic rotations about each site.

There is one fixed nearest-neighbor admissibility rule, covariant under lattice
translations and proper cubic rotations.

For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.

Record is quoted only to keep formation and readout outside the hop-cost:

When present, a record locks exactly one admissible local possibility.

A readout value is determined by record content alone.

A site with no record cannot be read.

Admissibility does not supply the formation site, probability, or rate. It
also does not name a hop-cost, a two-point arrival table, or a preferred
clause-toggle.

## Objects

Let `e_1 = (1,0,0)`, `e_2 = (0,1,0)`, `e_3 = (0,0,1)`. The six nearest-neighbor
shifts are `±e_1`, `±e_2`, `±e_3`. The closed ball is

```text
B_6(0) = { v ∈ Z^3 : |v|_1 ≤ 6 }.
```

It contains exactly `377` sites. The directed graph used here has an edge
`v → u` precisely when `u − v` is one of the six shifts and both endpoints
lie in `B_6(0)`.

Inward weight: `w(v) = |σ_v|`, the number of nonzero coordinates of `v`.
Then `w(0) = 0`, `w(±e_i) = 1`, and `w((2,2,2)) = 3`.

Named hop-cost for the displayed triple `(s,a,d) = (0,1,1)`:

```text
c(v → u) = 3  if  (w(v) = w(u) = 1)  or  (w(u) < w(v)),
c(v → u) = 1  otherwise.
```

Seed-exit hops have `w(v) = 0` and therefore cost `1` under this triple.
Axis-one hops and support-drop hops cost `3`.

Arrival time `t(v)` is the minimum sum of hop-costs over directed walks from
`0` to `v` that remain in `B_6(0)`.

A walk from `0` to a target is a **shortest path** when its hop-cost sum
equals `t(target)`. Among shortest paths, the **lex-first** walk is the one
obtained by the following local rule, which is the ordinary lexicographic
minimum on the sequence of sites: starting at `0`, if the walk so far ends
at `v ≠ target`, the next site is the lexicographically smallest neighbor
`u` for which some shortest `0 → target` walk continues `v → u`. Site order
is the ordinary tuple order on `Z^3`.

## Theorem 1 — Lex-first shortest paths

**Statement.** Under the named `(0,1,1)` hop-cost on `B_6(0)`,

- `t(4,0,0) = 8` and `t(2,2,2) = 6`,
- the lex-first shortest path `0 → (4,0,0)` is the six-hop walk
  `(0,0,0) → (0,-1,0) → (1,-1,0) → (2,-1,0) → (3,-1,0) → (4,-1,0) → (4,0,0)`
  with hop-cost list `(1,1,1,1,1,3)`,
- the lex-first shortest path `0 → (2,2,2)` is the six-hop walk
  `(0,0,0) → (0,0,1) → (0,1,1) → (0,1,2) → (0,2,2) → (1,2,2) → (2,2,2)`
  with hop-cost list `(1,1,1,1,1,1)`.

In particular `t(4,0,0) > t(2,2,2)`, so the two-point comparison on these
sites reverses relative to uniform graph-length (where the same sites have
arrivals `4` and `6`). The hop-cost lists are part of the claim: the result
is not leftover of the two arrival numbers.

**Proof.** The directed graph is finite. Dijkstra's algorithm from the origin
computes every arrival. The same algorithm run backward from each target,
using the original directed costs on reversed edges, computes remaining
cost-to-target. A neighbor `u` of `v` lies on some shortest `0 → target`
walk if and only if

```text
t(v) + c(v → u) = t(u)    and    t(u) + t_to_target(u) = t(target).
```

The lex-first reconstruction then always takes the lexicographically
smallest such `u`. The runner executes both reconstructions.

Direct inspection of the first walk: `w(0) = 0`, so the opening hop is a
seed-exit of cost `1`. Each of the next four hops stays at inward weight
`2` and is neither axis-one nor a support-drop, hence costs `1`. The last
hop `(4,-1,0) → (4,0,0)` drops weight `2 → 1` and therefore costs `3`. The
list sums to `8`, matching `t(4,0,0)`.

Direct inspection of the second walk: the opening hop is again a seed-exit
of cost `1`. The remaining five hops have weight pairs
`(1,2)`, `(2,2)`, `(2,2)`, `(2,3)`, `(3,3)` and are therefore all cost `1`.
The list sums to `6`, matching `t(2,2,2)`.

The axis-only competitor to `(4,0,0)` is not shortest: after the cheap
seed-exit, the three remaining hops are axis-one and cost `3` each, for
total `10`. A first hop into the negative first-coordinate half-space cannot
reach `(4,0,0)` at cost `8`, because returning across the plane `x = 0` and
then advancing to `x = 4` plus a final axis-one or support-drop hop already
overshoots. The reconstruction therefore begins at `(0,-1,0)`, the
lexicographically smallest first site that still lies on a shortest walk.

On the body-diagonal target, every first hop that decreases a coordinate
forces a later compensating support-drop or a longer walk, and the
remaining-cost test excludes those neighbors. The lexicographically
smallest surviving first site is `(0,0,1)`.

Thus the two walks, the two hop-cost lists, and the two arrival numbers are
exhibited together.

## Theorem 2 — Cheap seed-exit, displayed not adopted

**Statement.** Both lex-first shortest paths of Theorem 1 start with a
cost-`1` seed-exit. That opening hop is displayed as a feature of the named
toggle. It is not adopted as a physical selector.

**Proof.** Both walks begin `0 → u` with `w(0) = 0` and `w(u) = 1`. Seed-exit
holds. Axis-one fails because the destination weight is `1` but the source
weight is `0`, not `1`. Support-drop fails because the weight rises. Under
`(s,a,d) = (0,1,1)` the hop therefore costs `1`. The hop-cost lists of
Theorem 1 begin with that `1`.

If seed-exit were charged `3` as well, the same opening hops would cost `3`
and the displayed lists would no longer be the lists of Theorem 1. That is
a different named triple. This note does not run that triple as a claim.

## Theorem 3 — Not written into Admissibility; uniform graph-length not attached

**Statement.** The named clause-toggle `(0,1,1)` is not written into
Admissibility. The uniform graph-length comparator is not attached as a
physical time, a hop-cost, or a two-point law. Uniqueness of the toggle
among reversing rules is not claimed.

**Proof.** Admissibility, as quoted above, supplies one fixed nearest-neighbor
rule that determines a local possibility distribution from nearest-neighbor
conditions. It does not name inward weights, seed-exit, axis-one hops,
support-drop, or a numerical hop-cost. Inserting `(s,a,d) = (0,1,1)` into
that sentence would be an axiom edit. This note proposes none.

Uniform graph-length charges `1` on every nearest-neighbor hop and therefore
gives arrivals `|v|_1`. On the two displayed sites those arrivals are `4`
and `6`, which do not reverse. Using that comparator as a parent of the
walks, or rewriting the walks as leftover of those two integers, would
attach a different rule. The walks of Theorem 1 use the named toggle and
are longer than graph-length on the axis site precisely because the last
hop is a charged support-drop.

No later selector is forbidden. The claim is only that the present
exhibition does not perform the selection.

## Boundary And Non-Claims

- The note does not claim that `(0,1,1)` is the unique reversing
  clause-toggle, nor that it minimizes any variance.
- The note does not extend the ball past radius six, and it does not score
  other destinations except as Dijkstra scaffolding for the two targets.
- The note does not identify hop-cost with a Record readout, a formation
  rate, or a nearest-neighbor possibility law.
- The note does not attach uniform graph-length, and it does not treat the
  two arrival numbers as a substitute for the exhibited walks.
- The note does not propose axiom text.

## Imports Table

| Input | Role | Status language |
|---|---|---|
| live axiom memo | cubic nearest-neighbor substrate; Admissibility does not name a hop-cost | registered `minimal_axioms` premise |
| displayed `(0,1,1)` toggle | finite hop-cost hypothesis | displayed, not adopted |
| uniform graph-length | disclosed contrast only | not attached |

No approved primitive is consumed.

## Promotion Value Gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the path-exhibition residual for the cheap-seed reversing toggle: the walks and hop-cost lists are produced, not only the two arrival numbers. |
| V2 | Current `origin/main` has no landed source note exhibiting these two lex-first walks under the named `(0,1,1)` clause-toggle on `B_6(0)`. |
| V3 | The graph, costs, and reconstructions are finite and exact. No observational input is used. |
| V4 | The hop-cost lists distinguish the claim from a restatement of `t(4,0,0)=8` and `t(2,2,2)=6`. The axis-only competitor summing to `10` is an explicit contrast. |
| V5 | The toggle is displayed, not adopted. It is not a physical time, not an Admissibility edit, and not a uniqueness theorem. |

## No-Go Discipline Gate

The negative content is narrow: this exhibition does not write `(0,1,1)`
into Admissibility and does not attach uniform graph-length. No global
impossibility for a later hop-cost selector is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| named `(0,1,1)` Dijkstra | charge axis-one and support-drop only | executed; yields the displayed walks |
| axis-only competitor | stay on the first-coordinate axis | sums to `10`; not shortest |
| charge seed-exit as well | use the triple `(1,1,1)` | different arrivals; not this claim |
| uniform graph-length | charge `1` on every hop | arrivals `4` and `6`; no reverse; not attached |
| write the toggle into Admissibility | treat hop-cost as the axiom's nearest-neighbor rule | axiom edit; not derived |
| other radii or destinations | leave `B_6(0)` or change the two sites | different object |
| later selector among reversing triples | uniqueness or variance ranking | live route; not claimed here |

### N2 — wall independence

The missing physical selector, the missing identification of hop-cost with
Admissibility, and the missing uniqueness statement are distinct residuals.
This note claims no complete wall collection.

### N3 — hidden-condition scan

The ball radius, the three clause names, the toggle `(0,1,1)`, the
lex-first reconstruction rule, and the two targets are declared. Uniform
graph-length is used only as a disclosed contrast.

### N4 — source residual matching

The current axiom memo supplies the cubic nearest-neighbor substrate and
does not name a hop-cost. The residual is therefore an exhibition under a
displayed hypothesis, matching those sources.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | named hops and inward-weight clauses | no continuum interpolation |
| per site | arrivals at `(4,0,0)` and `(2,2,2)` | no lattice-wide time law |
| per mode | no mode calculation | no spectral claim |
| per block | one Dijkstra family and two lex-first reconstructions | no selector among all reversing triples |
| lattice wide | checked and not executed | no Admissibility edit; no attached uniform graph-length |

### N6 — live partial-closure paths

Live routes include a later derivation that would select a hop-cost from
Admissibility, a comparison among several reversing triples, a different
radius, and a Record-typed reading of arrival. None is closed here.

### N7 — hostile steelman

**Steelman:** Once the two arrivals `8` and `6` are known, the paths are
leftover and need not be exhibited.

**Answer:** Several walks can share an arrival. The axis-only walk to
`(4,0,0)` has a different hop-cost list and is not shortest. The lex-first
rule plus the hop-cost lists are the content that the two integers do not
record. Theorem 1 therefore exhibits the walks.

### N8 — cross-cycle echo

A full three-clause scan and a seed-exit-expensive support-drop rule are
different objects. This note does not import their arrivals as premises. It
recomputes the `(0,1,1)` walks on `B_6(0)` from the named cost.

**Gate disposition:** PASS for the exhibited lex-first walks, the hop-cost
lists, the cheap seed-exit opening, and the narrow non-adoption statements.
FAIL / DO NOT SHIP for “Admissibility is `(0,1,1)`,” “uniform graph-length
is the physical time,” or “no other reversing rule exists.”

## Primary Runner

The primary runner builds `B_6(0)`, evaluates the named hop-cost, computes
arrivals by Dijkstra, reconstructs both lex-first shortest paths, checks the
hop-cost lists and the cheap seed-exit openings, pins the current axiom
wording, and runs mutation controls that replace the named toggle by uniform
graph-length or by an expensive seed-exit. It authors no audit verdict.
