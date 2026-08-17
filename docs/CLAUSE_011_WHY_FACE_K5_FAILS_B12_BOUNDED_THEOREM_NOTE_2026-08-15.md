---
claim_id: clause_011_why_face_k5_fails_b12_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Lex-first shortest paths to (10,0,0) and (5,5,0) under the named (0,1,1) hop-cost on B_12(0) are named. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/clause_011_why_face_k5_fails_b12_2026_08_15.py
---

# Clause `(0,1,1)` Lex-First Walks At The Face Scale Where Reverse Fails

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** one directed Dijkstra on the nearest-neighbor graph of the closed
radius-twelve ball under the named clause-toggle with cheap seed-exit and
expensive axis-one and support-drop hops. The lex-first shortest walks from
the origin to `(10,0,0)` and to `(5,5,0)` are named. Displayed, not adopted.
The walks are not leftover of the no bit.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/clause_011_why_face_k5_fails_b12_2026_08_15.py`](../scripts/clause_011_why_face_k5_fails_b12_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.
**Cache:** none. `cache_write: false`.

## Result Up Front

Work on the cubic lattice `Z^3` with nearest-neighbor adjacency. Write
`B_12(0)` for the closed ball `{v ∈ Z^3 : |v|_1 ≤ 12}`. This set has exactly
`2625` sites. Hops that would leave the ball are absent. For a site `v`, write
`σ_v` for the set of nonzero coordinates and write the inward weight
`w(v) = |σ_v|`.

A directed nearest-neighbor hop `v → u` is classified by three named clauses:

- seed-exit when `w(v) = 0`,
- both-weights-one (axis-one) when `w(v) = w(u) = 1`,
- support-drop when `w(u) < w(v)`.

The displayed clause-toggle `(s,a,d) = (0,1,1)` charges cost `3` if
both-weights-one holds or support-drop holds, and charges cost `1` otherwise.
Seed-exit is therefore cheap. This is a finite named hop-cost on `B_12(0)`. It
is not written into Admissibility, and it is not attached to L1.

One origin Dijkstra returns the in-ball arrivals

```text
t(10,0,0)=14
t(5,5,0)=10
```

The lex-first shortest walk `0 → (10,0,0)` is

`(0,0,0) → (0,-1,0) → (1,-1,0) → (2,-1,0) → (3,-1,0) → (4,-1,0) → (5,-1,0) → (6,-1,0) → (7,-1,0) → (8,-1,0) → (9,-1,0) → (10,-1,0) → (10,0,0)`

with hop-cost list `(1,1,1,1,1,1,1,1,1,1,1,3)` summing to `14`.

The lex-first shortest walk `0 → (5,5,0)` is

`(0,0,0) → (0,1,0) → (1,1,0) → (1,2,0) → (1,3,0) → (1,4,0) → (1,5,0) → (2,5,0) → (3,5,0) → (4,5,0) → (5,5,0)`

with hop-cost list `(1,1,1,1,1,1,1,1,1,1)` summing to `10`.

The displayed comparison

$$
\frac{t(10,0,0)^2}{100}>\frac{t(5,5,0)^2}{50}
$$

fails: `196/100 = 49/25` is not greater than `100/50 = 2`. Equivalently
`50 t(10,0,0)^2 = 9800 < 10000 = 100 t(5,5,0)^2`. That no bit is displayed,
not adopted. Naming the two walks is not leftover of the no bit. Uniqueness
is not claimed among shortest walks of those costs. Do not attach L1.
Do not write (0,1,1) into Admissibility.

Literal score lines used by the runner:

- t(10,0,0)=14
- t(5,5,0)=10
- 50 t(10,0,0)^2 = 9800 < 10000 = 100 t(5,5,0)^2
- not leftover of the no bit
- Uniqueness is not claimed
- Do not write (0,1,1) into Admissibility
- Do not attach L1

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "One Dijkstra on B_12(0) names the lex-first shortest walks to (10,0,0) and (5,5,0) under the named (0,1,1) hop-cost and displays that the k=5 face reverse comparison fails. The rule is displayed, not adopted."
trace_class: frontier_discovery
target_claim_id: clause_011_why_face_k5_fails_b12
target_blocker_text: "name lex-first shortest paths to (10,0,0) and (5,5,0) under (0,1,1) on B_12(0); the k=5 reverse comparison fails"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the named lex-first walks; do not write the clause-toggle into Admissibility and do not attach L1"
conditional_surface_status: "exact for the named (0,1,1) hop-cost on B_12(0); other clause triples, other radii, and any physical selector remain unclaimed"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Target And Proof Obligations

**Exact target.** On `B_12(0)` under the named `(0,1,1)` hop-cost, report
`t(10,0,0)` and `t(5,5,0)`, and name a lex-first shortest path to each.
Score whether `t(10,0,0)^2/100 > t(5,5,0)^2/50`. Do not write `(0,1,1)` into
Admissibility. Do not attach L1. Uniqueness is not required.

| Obligation | Disposition |
|---|---|
| named `(0,1,1)` hop-cost on `B_12(0)` | defined here; executed in Theorem 1 |
| arrivals `t(10,0,0)` and `t(5,5,0)` | proved here in Theorem 1 |
| lex-first shortest walk to each site | proved here in Theorem 1 |
| displayed reverse comparison fails | Theorem 2 |
| walks are not leftover of the no bit | Theorem 1 by exhibiting the hops |
| clause-toggle not written into Admissibility | Theorem 3 |
| L1 not attached | Theorem 3 |

## Inputs And Import Boundary

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies the
  cubic nearest-neighbor substrate and the one-fixed-rule Admissibility
  sentence. As the registered `minimal_axioms` premise, it is not a
  bounded-status source.
- The three clause names (seed-exit, both-weights-one, support-drop) and the
  toggle `(s,a,d) = (0,1,1)` are displayed mathematical hypotheses, not
  framework-derived physical selectors.
- No approved primitive is used. Scale reference, kinetic isotropy, and
  realized-state evaluation are not inputs.
- External empirical or literature inputs:** none.
- Uniform graph-length, which charges `1` on every nearest-neighbor hop, is a
  disclosed contrast only. It is not attached.

## Current Premise Boundary

The Lattice and Admissibility premises are quoted from
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md):

Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
adjacency, standard translations, and proper cubic rotations about each site.

There is one fixed nearest-neighbor admissibility rule, covariant under lattice
translations and proper cubic rotations.

For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.

Admissibility is not a dynamics axiom. It does not choose a Hamiltonian or
transfer operator, supply transition-probability or weight values, select a
scalar or nonzero kinetic branch, assert a Dirac-square carrier, define a time
metric, or provide a record-production process or physical persistence
dynamics.

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
B_12(0) = { v ∈ Z^3 : |v|_1 ≤ 12 }.
```

It contains exactly `2625` sites. The directed graph used here has an edge
`v → u` precisely when `u − v` is one of the six shifts and both endpoints
lie in `B_12(0)`.

Inward weight: `w(v) = |σ_v|`, the number of nonzero coordinates of `v`.
Then `w(0) = 0`, `w(±e_i) = 1`, `w((10,-1,0)) = 2`, and `w((5,5,0)) = 2`.

Named hop-cost for the displayed triple `(s,a,d) = (0,1,1)`:

```text
c(v → u) = 3  if  (w(v) = w(u) = 1)  or  (w(u) < w(v)),
c(v → u) = 1  otherwise.
```

Seed-exit hops have `w(v) = 0` and therefore cost `1` under this triple.
Axis-one hops and support-drop hops cost `3`.

Arrival time `t(v)` is the minimum sum of hop-costs over directed walks from
`0` to `v` that remain in `B_12(0)`. One Dijkstra computation from the origin
produces every in-ball `t(v)` used below.

A walk from `0` to a target is a **shortest path** when its hop-cost sum
equals `t(target)`. Among shortest paths, the **lex-first** walk is the one
obtained by the following local rule, which is the ordinary lexicographic
minimum on the sequence of sites: starting at `0`, if the walk so far ends
at `v ≠ target`, the next site is the lexicographically smallest neighbor
`u` for which some shortest `0 → target` walk continues `v → u`. Site order
is the ordinary tuple order on `Z^3`. Uniqueness of the shortest walk is
not required and is not claimed.

The Euclidean squared lengths used in the displayed comparison are
`|(10,0,0)|_2^2 = 100` and `|(5,5,0)|_2^2 = 50`. Face reverse on this ordered
pair means `t(10,0,0)^2 / 100 > t(5,5,0)^2 / 50`. That comparison is
displayed, not adopted.

## Theorem 1 — Arrivals and lex-first shortest paths

**Statement.** Under the named `(0,1,1)` hop-cost on `B_12(0)`,

- `t(10,0,0) = 14` and `t(5,5,0) = 10`,
- the lex-first shortest path `0 → (10,0,0)` is the twelve-hop walk
  `(0,0,0) → (0,-1,0) → (1,-1,0) → (2,-1,0) → (3,-1,0) → (4,-1,0) → (5,-1,0) → (6,-1,0) → (7,-1,0) → (8,-1,0) → (9,-1,0) → (10,-1,0) → (10,0,0)`
  with hop-cost list `(1,1,1,1,1,1,1,1,1,1,1,3)`,
- the lex-first shortest path `0 → (5,5,0)` is the ten-hop walk
  `(0,0,0) → (0,1,0) → (1,1,0) → (1,2,0) → (1,3,0) → (1,4,0) → (1,5,0) → (2,5,0) → (3,5,0) → (4,5,0) → (5,5,0)`
  with hop-cost list `(1,1,1,1,1,1,1,1,1,1)`.

These two values are Dijkstra outputs, not fitted scalars. The hop-cost
lists are part of the claim: the result is not leftover of the no bit.

**Proof.** The directed graph is finite. Dijkstra's algorithm from the origin
computes every in-ball arrival. A directed edge `v → u` lies on the
shortest-path dag when `t(v) + c(v → u) = t(u)`. A neighbor `u` of `v` lies
on some shortest `0 → target` walk if and only if that edge is a
shortest-path edge and `u` can reach the target along the dag. The
lex-first reconstruction then always takes the lexicographically smallest
such `u`. The runner executes one origin Dijkstra and both reconstructions.

Direct inspection of the first walk: `w(0) = 0`, so the opening hop is a
seed-exit of cost `1`. Each of the next ten hops stays at inward weight
`2` and is neither axis-one nor a support-drop, hence costs `1`. The last
hop `(10,-1,0) → (10,0,0)` drops weight `2 → 1` and therefore costs `3`.
The list sums to `14`, matching `t(10,0,0)`. Every site on the walk has
`|v|_1 ≤ 11` except the terminal axis site, so the walk remains in
`B_12(0)`.

Direct inspection of the second walk: the opening hop is again a seed-exit
of cost `1`. The remaining nine hops have weight pairs that never stay at
inward weight `1` and never drop support, and therefore all cost `1`. The
list sums to `10`, matching `t(5,5,0)`.

The axis-only competitor
`(0,0,0) → (1,0,0) → (2,0,0) → (3,0,0) → (4,0,0) → (5,0,0) → (6,0,0) → (7,0,0) → (8,0,0) → (9,0,0) → (10,0,0)`
has hop-cost list `(1,3,3,3,3,3,3,3,3,3)` and sums to `28`, so it is not
shortest. A first hop into the negative first-coordinate half-space cannot
reach `(10,0,0)` at cost `14`: after that seed-exit the remaining
first-coordinate gap is eleven, and a later support-drop of cost `3` already
forces the total above `14` unless the walk never spends an extra hop. The
reconstruction therefore begins at `(0,-1,0)`, the lexicographically
smallest first site that still lies on a shortest walk.

On the face target, every first hop that decreases a coordinate or opens
the unused third coordinate forces a later compensating hop, and the
shortest-path dag excludes those neighbors. The lexicographically smallest
surviving first site is `(0,1,0)`. The continuation then prefers the
negative-to-positive tuple order, so it fills the second coordinate to `5`
before advancing the first coordinate.

Another shortest walk to `(10,0,0)` exists, namely the sign-flipped corridor
through `(10,1,0)`. Another shortest walk to `(5,5,0)` exists, namely the
corridor that advances the first coordinate first. Those competitors have
the same costs but are lexicographically later. Uniqueness is not claimed.

Thus the two walks, the two hop-cost lists, and the two arrival numbers are
exhibited together. Knowing only that the Theorem 2 comparison fails does
not name either walk.

## Theorem 2 — The displayed reverse comparison fails

**Statement.** Whether `t(10,0,0)^2 / 100 > t(5,5,0)^2 / 50` fails. That
comparison is displayed, not adopted.

**Proof.** Substitute the Theorem 1 arrivals:

```text
t(10,0,0)^2 / 100 = 196 / 100 = 49/25,
t(5,5,0)^2 / 50 = 100 / 50 = 2.
```

Then `49/25 < 2`, so the strict inequality fails. The integer form used by
the runner is `50 t(10,0,0)^2 = 9800 < 10000 = 100 t(5,5,0)^2`.

Uniform graph-length on the same pair gives arrivals `|v|_1`, hence `10`
and `10`, and also fails the same comparison: `100/100 = 1` is not greater
than `100/50 = 2`. That shared no bit does not identify the named walks or
the named arrivals `14` and `10`. The comparison is therefore not leftover
of those two integers, and the walks are not leftover of the no bit. The
graph-length comparator is not attached.

## Theorem 3 — Not written into Admissibility; L1 not attached

**Statement.** Do not write `(0,1,1)` into Admissibility. Do not attach L1.
Uniqueness is not claimed among hop-costs.

**Proof.** Admissibility, as quoted above, supplies one fixed nearest-neighbor
rule that determines a local possibility distribution from nearest-neighbor
conditions. It does not name inward weights, seed-exit, axis-one hops,
support-drop, or a numerical hop-cost. Inserting `(s,a,d) = (0,1,1)` into
that sentence would be an axiom edit. This note proposes none.

L1 here means the uniform graph-length comparator that charges `1` on every
nearest-neighbor hop and therefore gives arrivals `|v|_1`. Attaching that
comparator as a parent of the named walks, or rewriting the walks as leftover
of those integers, would attach a different rule. The pair
`((10,0,0),(5,5,0))` has named arrivals `14` and `10`, not `10` and `10`.

No later selector is forbidden. The claim is only that the present score does
not perform the selection.

## Boundary And Non-Claims

- The note does not claim that `(0,1,1)` is the unique reversing
  clause-toggle, nor that the exhibited walks are the unique shortest walks.
- The note does not extend the ball past radius twelve.
- The note does not identify hop-cost with a Record readout, a formation
  rate, or a nearest-neighbor possibility law.
- The note does not attach L1, and it does not treat the no bit as a
  substitute for the named walks.
- The note does not propose axiom text.
- The lex-first walks and the failed comparison are not claimed outside
  `B_12(0)` and are not claimed for any hop-cost other than the named
  `(0,1,1)`.

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
| V1 | It names the lex-first walks to `(10,0,0)` and `(5,5,0)` and displays that the k=5 reverse comparison fails. |
| V2 | Current `origin/main` has no landed source note naming these `(0,1,1)` lex-first walks on `B_12(0)`. |
| V3 | The graph, costs, and one Dijkstra are finite and exact. No observational input is used. |
| V4 | The hop sequences are new relative to the two arrival numbers and relative to the no bit. |
| V5 | The toggle is displayed, not adopted. It is not a physical time, not an Admissibility edit, and not a uniqueness theorem. |

## No-Go Discipline Gate

The negative content is narrow: this score does not write `(0,1,1)` into
Admissibility and does not attach L1. No global impossibility for a later
hop-cost selector is claimed. These are scope boundaries, not impossibility.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| named `(0,1,1)` Dijkstra on `B_12(0)` | charge axis-one and support-drop only | executed; yields the displayed arrivals and walks |
| reuse the no bit alone | copy “reverse fails” as a substitute for the walks | false; the hops are not leftover of the no bit |
| charge seed-exit as well | use the triple `(1,1,1)` | different opening hop; not this claim |
| uniform graph-length | charge `1` on every hop | arrivals `10` and `10`; not attached |
| write the toggle into Admissibility | treat hop-cost as the axiom's nearest-neighbor rule | axiom edit; not derived |
| later selector among reversing triples | uniqueness or variance ranking | live route; not claimed here |

### N2 — wall independence

The missing physical selector, the missing identification of hop-cost with
Admissibility, and the missing uniqueness statement are distinct residuals.
This note claims no complete wall collection.

### N3 — hidden-condition scan

The ball radius, the three clause names, the toggle `(0,1,1)`, the reverse
predicate, the two sites, and the lex-first reconstruction rule are
declared. Uniform graph-length is used only as a disclosed contrast.

### N4 — source residual matching

The current axiom memo supplies the cubic nearest-neighbor substrate and
does not name a hop-cost. The residual is therefore a score under a
displayed hypothesis, matching those sources.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | named hops and inward-weight clauses | no continuum interpolation |
| per site | arrivals and lex-first walks at the two in-ball targets | no lattice-wide time law |
| per mode | exact integer reverse test at this pair | no spectral claim |
| per block | one Dijkstra on `B_12(0)` | no selector among all reversing triples |
| lattice wide | checked and not executed | no Admissibility edit; L1 not attached |

### N6 — live partial-closure paths

Live routes include a later derivation that would select a hop-cost from
Admissibility, a comparison among several reversing triples, and a
Record-typed reading of arrival. None is closed here.

### N7 — hostile steelman

**Steelman:** Once the no bit `t(10,0,0)^2/100 > t(5,5,0)^2/50` is known to
fail, the two walks are leftover.

**Answer:** The no bit is a comparison of two integers. It does not name the
twelve-hop corridor through `(10,-1,0)` or the ten-hop corridor through
`(1,5,0)`. Those sequences, and the fact that they are the lex-first
shortest walks, are additional data. The result is not leftover of the no
bit.

### N8 — cross-cycle echo

A six-scale reverse census and a two-point no bit are different objects.
This note does not import those bits as premises. It recomputes the
`(0,1,1)` arrivals on `B_12(0)` from the named cost and reconstructs the
lex-first walks to `(10,0,0)` and `(5,5,0)`.

**Gate disposition:** PASS for the two in-ball arrivals, the two lex-first
walks, the failed reverse comparison, and the narrow non-adoption
statements. FAIL / DO NOT SHIP for “Admissibility is `(0,1,1)`,” “L1 is the
physical time,” or “no other reversing rule exists.”

## Primary Runner

The primary runner builds `B_12(0)`, evaluates the named hop-cost, computes
arrivals by one Dijkstra, reconstructs the lex-first walks to `(10,0,0)`
and `(5,5,0)` on the shortest-path dag, checks the two in-ball times and
the failed reverse comparison, pins the current axiom wording, and runs
mutation controls that replace the named toggle by uniform graph-length or
by an expensive seed-exit on a witnessing walk. It authors no audit verdict.

## claim_scope

Lex-first shortest paths to (10,0,0) and (5,5,0) under the named (0,1,1) hop-cost on B_12(0) are named. Displayed, not adopted.
