---
claim_id: support_drop_axis_path_b6_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "A shortest 0→(4,0,0) path under the named support-drop hop-cost is exhibited and sums to 10. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/support_drop_axis_path_b6_2026_08_15.py
---

# Support-Drop Axis Path On `B_6(0)`

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** one finite directed hop-cost on the six-neighbor graph of the
radius-6 ball `B_6(0)`, the lex-first cheapest walk from the origin to
`(4,0,0)`, and the on-axis-only comparison walk. No Admissibility rewrite,
no adopted hop-cost, no coordinate-sum law.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/support_drop_axis_path_b6_2026_08_15.py`](../scripts/support_drop_axis_path_b6_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

Work on the finite ball

```text
B_6(0) = { v ∈ Z^3 : |v_1| + |v_2| + |v_3| ≤ 6 }
```

of 377 sites, with the six-neighbor adjacency of the Lattice axiom, restricted
so that every hop stays inside the ball. For a site `v` write `σ(v)` for the
set of nonzero coordinates of `v` and `w(v) = |σ(v)|` for that set's
cardinality. The named support-drop hop-cost on a directed nearest-neighbor
edge `v → w` is

```text
ν(v → w) = 3  if w(v) = 0 or (w(v) = w(w) = 1) or w(w) < w(v),
          1  otherwise.
```

The three cost-3 clauses are seed-exit, both-weight-1 (axis 1-skeleton)
continuation, and a drop in coordinate-support cardinality. This is a
displayed finite scoring rule. Do not write ν into Admissibility.

The residual is the path type, not leftover of the arrival number. The
lex-first cheapest walk `0 → (4,0,0)` is

```text
(0,0,0) → (0,-1,0) → (1,-1,0) → (2,-1,0) → (3,-1,0) → (4,-1,0) → (4,0,0)
```

with hop costs `3, 1, 1, 1, 1, 3`, which sum to 10. The on-axis-only path
costs 12 and is displayed, not adopted. Do not attach L1.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "A finite Dijkstra on B_6(0) exhibits one lex-first cheapest walk 0 → (4,0,0) under the named support-drop hop-cost and shows that the on-axis-only walk costs 12. The rule is displayed, not adopted."
trace_class: negative_route_pruning
target_claim_id: support_drop_axis_path_b6
target_blocker_text: "why t(4,0,0)=10 under the named support-drop hop-cost, not 12"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the exhibited walk; any physical use must separately derive an Admissibility rule"
conditional_surface_status: "exact for the named hop-cost on B_6(0); no lattice-wide law or adopted cost"
hypothetical_axiom_status: "not proposed; no axiom or approved primitive is added"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Target And Proof Obligations

**Exact target.** On `B_6(0)`, under the named support-drop hop-cost `ν`,
exhibit the lexicographically first cheapest walk from the origin to
`(4,0,0)` as a list of sites and as a list of hop costs, and confirm that
those costs sum to 10. Display the on-axis-only walk and its cost 12 without
adopting it. Do not write `ν` into Admissibility. Do not attach L1.

| Obligation | Disposition |
|---|---|
| named hop-cost on directed six-neighbor edges in `B_6(0)` | defined above; checked by the companion runner |
| lex-first cheapest `0 → (4,0,0)` walk and hop costs | proved here in Theorem 1 |
| on-axis-only comparison walk of cost 12 | displayed in Theorem 2; not adopted |
| Admissibility and coordinate-sum non-identification | Theorem 3; no axiom edit |
| arrival number without a path | refused; the residual is the path type |

Boundary cases are not hidden. The destination `(4,0,0)` is an axis site of
weight 1, so every walk from the origin must pay a seed-exit 3 and later a
coordinate-support drop 3 if it ever leaves the axis. Walks that remain on
the positive first axis pay four cost-3 hops. Other radii, other destinations,
other hop-costs, and any physical reading of `ν` as the Admissibility rule
are outside the target.

## Inputs And Support Inventory

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies the
  cubic lattice `Z^3` with nearest-neighbor adjacency, the one fixed
  Admissibility rule as an unedited premise, and the Record lock sentence
  used only as a non-use boundary. As the registered `minimal_axioms`
  premise, it is not a bounded-status source.
- `B_6(0)`, the named rule `ν`, the destination `(4,0,0)`, and the
  lex-first convention are displayed mathematical hypotheses.
- No measured, fitted, observational, literature, or phenomenological value
  is used.
- Coordinate-support cardinality `w(v)` is not Admissibility support. The
  latter remains the set of local possibilities of nonzero probability.

## Exact Objects

Sites are integer triples. Two sites are adjacent when they differ by one
standard basis step. A walk is a finite sequence of adjacent sites remaining
in `B_6(0)`. The cost of a walk is the sum of `ν` on its directed hops.
A cheapest walk is a walk of minimal cost. Among cheapest walks from the
origin to `(4,0,0)`, the lex-first walk is the unique sequence that is
smallest in the lexicographic order of coordinate triples.

The companion runner implements one Dijkstra on the 377-site directed graph
and reconstructs the lex-first cheapest walk by a greedy choice, at each
site, of the least next site that continues some cheapest walk.

## Theorem 1 — lex-first cheapest walk sums to 10

The unique lex-first cheapest walk is

```text
(0,0,0) → (0,-1,0) → (1,-1,0) → (2,-1,0) → (3,-1,0) → (4,-1,0) → (4,0,0)
```

with hop costs

```text
3, 1, 1, 1, 1, 3
```

which sum to 10.

The first hop is a seed-exit: `w(0,0,0) = 0`, so the cost is 3. The next
four hops stay in the weight-2 face `y = -1` with nonnegative first
coordinate; each is neither seed-exit, nor both-weight-1, nor a support
drop, so each costs 1. The last hop `(4,-1,0) → (4,0,0)` drops coordinate
support from 2 to 1 and costs 3.

No cheaper walk exists. Every walk from the origin pays seed-exit 3. The
destination has weight 1, so a walk that leaves the axis must later pay at
least one support-drop 3. Two cost-3 hops plus any number of cost-1 hops
cannot sum below 6; the remaining net displacement from `(0,-1,0)` to
`(4,0,0)` after the seed-exit is five nearest-neighbor steps, so a
six-hop walk with exactly those two cost-3 payments is minimal and totals
10. The companion runner's Dijkstra returns arrival 10 at `(4,0,0)` and
finds exactly eight cheapest walks, all of cost 10. The lex-first member
is the walk displayed above.

## Theorem 2 — the on-axis-only path costs 12

The on-axis-only walk

```text
(0,0,0) → (1,0,0) → (2,0,0) → (3,0,0) → (4,0,0)
```

has hop costs `3, 3, 3, 3` and therefore costs 12. Each hop is seed-exit
or both-weight-1. Displayed, not adopted. The walk is a legal walk in
`B_6(0)` and is the unique four-hop walk from the origin to `(4,0,0)`,
but it is not cheapest.

## Theorem 3 — not an Admissibility clause and not L1

Do not write ν into Admissibility. The live axiom still says that there is
one fixed nearest-neighbor admissibility rule, covariant under lattice
translations and proper cubic rotations, determining a probability
distribution over local possibilities. The named hop-cost `ν` is a
finite scoring rule on directed lattice edges. It is not that rule, does
not select a support of possibilities, and is not proposed as an axiom or
approved primitive.

Do not attach L1. The set `B_6(0)` is only the finite domain. Graph
distance from the origin to `(4,0,0)` is 4, and the on-axis-only walk has
length 4, but those counts are not the hop-cost. The exhibited cheapest
walk has six hops and cost 10. The residual is the path type under `ν`,
not leftover of the arrival number 10 and not a coordinate-sum law.

## Mutations

1. Treat the on-axis-only walk as cheapest: its cost is 12, not 10.
2. Replace the exhibited sum 10 by 12: Dijkstra still returns 10.
3. Write `ν` into Admissibility: the axiom memo is unedited and contains
   no support-drop hop-cost.
4. Identify `ν` with unit graph-distance: the on-axis-only walk would then
   cost 4, contradicting both displayed sums.
5. Replace the lex-first walk by a later cheapest walk: the other seven
   cheapest walks also sum to 10, but they are lexicographically larger.

## What This Does Not Claim

- No Admissibility rewrite and no adopted hop-cost.
- No Qubit rewrite.
- No Record readout, formation site, or formation rate.
- No diamond-comparison or variance claim; those are outside this path
  exhibit.
- No uniqueness of `ν` among hop-costs with arrival 10.
- No continuum limit, no Newtonian kernel, and no observational input.

## No-Go Discipline Gate

The negative content is only this: the on-axis-only walk is not cheapest
under the named rule, the named rule is not written into Admissibility,
and the exhibit is not a coordinate-sum law. It is not a claim that
axis walks are impossible, or that a physical hop-cost has been selected.

### N1 — materially distinct routes

| Route | Exact attack | Result and authority | Marker |
|---|---|---|---|
| on-axis-only cheapest | Score the unique four-hop axis walk. | Theorem 2 and runner check `thm2-axis-costs-12` give cost 12, strictly above 10. | **ATTEMPTED** |
| arrival number without a path | Report only `t(4,0,0)=10`. | Theorem 1 exhibits sites and hop costs; the residual is the path type, not leftover of the arrival number. | **ATTEMPTED** |
| write `ν` into Admissibility | Treat the scoring rule as the axiom's local constraint. | Theorem 3 and check `thm3-not-written-into-admissibility` keep the axiom unedited. | **ATTEMPTED** |
| attach a coordinate-sum law | Identify cost with hop count or with `|v_1|+|v_2|+|v_3|`. | Theorem 3 and check `thm3-do-not-attach-l1`; graph length 4 is not cost 10. | **ATTEMPTED** |
| later cheapest walk as the exhibit | Pick any of the other seven cost-10 walks. | Theorem 1 and check `thm1-lex-path` select the unique lex-first member. | **ATTEMPTED** |
| leave the ball | Allow sites with coordinate-sum of absolute values greater than 6. | The construction is `B_6(0)` only; check `ball-is-b6` keeps every displayed site inside the ball. | **ATTEMPTED** |

### N2 — wall independence and collapse

There is one positive exhibit and two refusal sentences, not a three-wall
headline. The cost-12 axis comparison and the “not leftover of the arrival
number” sentence certify the same path-type residual. The Admissibility and
coordinate-sum refusals are scope boundaries, not independent impossibility
walls.

| Pair | First closes second? | Second closes first? | Disposition |
|---|---:|---:|---|
| axis cost 12 / lex-first cost 10 | no: a worse walk does not name the lex-first walk | no: a cheapest walk does not by itself display the axis walk | one comparison, not two walls |
| Admissibility refusal / coordinate-sum refusal | no | no | independent scope boundaries, not walls |
| eight cheapest walks / lex-first selection | yes, once lex order is fixed | no: uniqueness of the lex-first member uses the order | collapse into Theorem 1 |

### N3 — hidden-condition scan

| Phrase or premise | Classification |
|---|---|
| six-neighbor cubic lattice | cited registered Lattice premise |
| `B_6(0)` and destination `(4,0,0)` | explicit finite hypotheses |
| named rule `ν` | explicit displayed scoring rule, not an axiom |
| coordinate-support cardinality | site-coordinate datum; not Admissibility support |
| lex-first among cheapest walks | explicit tie-break; all eight cheapest walks are enumerated |
| “Displayed, not adopted.” | scope marker, not a hidden existence claim |
| Record lock sentence | quoted as a non-use boundary |

### N4 — citation-to-residual matching

| Evidence path:line | Residual attacked | Residual claimed closed | Match? |
|---|---|---|---:|
| `docs/MINIMAL_AXIOMS_2026-06-29.md:37` | ambient lattice adjacency | six-neighbor `Z^3` only | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:57` | Admissibility as a probability rule | `ν` is not that rule | yes; boundary stays open |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:70` | meaning of Admissibility support | coordinate-support is a different object | yes; boundary stays open |
| `scripts/support_drop_axis_path_b6_2026_08_15.py:80` | named hop-cost clauses | seed-exit, both-weight-1, support-drop | yes |
| `scripts/support_drop_axis_path_b6_2026_08_15.py:131` | lex-first reconstruction | greedy least next site on a cheapest walk | yes |
| `scripts/support_drop_axis_path_b6_2026_08_15.py:260` | exhibited path | computed lex-first walk sums to 10 | yes |
| `scripts/support_drop_axis_path_b6_2026_08_15.py:287` | on-axis comparison | axis-only cost is 12 | yes |

No evidence citation is used to claim that Admissibility has been rewritten,
that a physical hop-cost has been selected, or that a coordinate-sum law
has been attached.

### N5 — rhetoric and resolution audit

| Resolution | Executed? | Narrow negative supported? |
|---|---:|---|
| per element | yes: each displayed hop | each cost is the named rule; no other edge family is classified |
| per site | yes: every site of the exhibited walks | all lie in `B_6(0)`; other balls are unclaimed |
| per mode | yes: lex-first among eight cheapest walks | this destination and this rule only |
| per block | yes: axis-only cost 12 versus cheapest cost 10 | the axis walk is displayed and not adopted |
| lattice wide | no | no Admissibility rewrite or lattice-wide hop-cost is asserted |

The runner prints the same five resolution statements.

### N6 — partial closure and primitive scan

The primitive registry at `docs/audit/data/axiom_premise_nodes.json` was
checked. The only dependency used is the registered `minimal_axioms` node.
No approved primitive supplies the named hop-cost. None is reclassified as
an import or wall.

A partial-closure mechanism is displayed rather than suppressed: the
on-axis-only walk is a legal walk of cost 12. It closes the question “is
there an axis walk at all?” and does not close cheapest-arrival. The
remaining physical choice—whether any hop-cost is the Admissibility rule—
stays explicit and does not require an axiom edit to state honestly.

### N7 — hostile steelman

The strongest objection is that arrival 10 is already known, so exhibiting
a walk is bookkeeping rather than a residual. That objection would be
correct if the claim were only the number. The claim is the path type:
seed-exit onto the face `y = -1`, four cheap face hops, and one support-drop
return at `x = 4`. Replacing that exhibit by the number 10, or by the
on-axis-only walk of cost 12, loses the residual. To overturn the exhibit
one must produce a cheaper walk in `B_6(0)` or a lexicographically smaller
walk of cost 10. The Dijkstra and the eight-walk enumeration close those
terminal obligations.

### N8 — cross-cycle echo

Repository search found nearby landed six-neighbor geometry. It is context,
not a load-bearing dependency; the hop-cost and the walk are recomputed
here.

| Earlier surface | Similar issue | Mechanism considered here |
|---|---|---|
| `docs/CUBIC_NN_CONDITION_DOMAIN_SEPARATION_BOUNDED_THEOREM_NOTE_2026-08-13.md` | six-neighbor adjacency of `Z^3` | the same adjacency is the edge set of `B_6(0)`; no condition-domain claim is reused |
| `docs/MINIMAL_AXIOMS_2026-06-29.md` | one fixed Admissibility rule | quoted and left unedited; `ν` is not written into it |

No earlier mechanism exhibits the lex-first cheapest `0 → (4,0,0)` walk
under this named hop-cost.

No-Go Discipline disposition: **PASS** for the path-type exhibit and the
two refusal sentences stated at the start of this section.

## Live Parent Quotes

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

> There is one fixed nearest-neighbor admissibility rule, covariant under lattice
> translations and proper cubic rotations.

> When present, a record locks exactly one admissible local possibility.

> "available"/"admissible" denotes its support -- on finite menus,
> exactly the possibilities of nonzero probability.

## Runner Contract

The companion runner rebuilds `B_6(0)`, evaluates the named hop-cost,
runs one Dijkstra, reconstructs the lex-first cheapest walk, scores the
on-axis-only walk, enumerates all cheapest walks, and checks the
Admissibility and coordinate-sum refusals. Declared audit inputs are this
note and the axiom memo. The runner writes no cache and authors no audit
verdict.
