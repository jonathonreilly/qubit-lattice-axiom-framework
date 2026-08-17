---
claim_id: clause_011_reverse_b8_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Body and face reverse under the named (0,1,1) hop-cost on B_8(0) are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/clause_011_reverse_b8_2026_08_15.py
---

# Clause `(0,1,1)` Body And Face Reverse On The Radius-Eight Ball

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** one directed Dijkstra on the nearest-neighbor graph of the closed
radius-eight ball under the named clause-toggle with cheap seed-exit and
expensive axis-one and support-drop hops. Body and face reverse bits that
live on this ball are reported. Displayed, not adopted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/clause_011_reverse_b8_2026_08_15.py`](../scripts/clause_011_reverse_b8_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.
**Cache:** none. `cache_write: false`.

## Result Up Front

Work on the cubic lattice `Z^3` with nearest-neighbor adjacency. Write
`B_8(0)` for the closed ball `{v ∈ Z^3 : |v|_1 ≤ 8}`. This set has exactly
`833` sites. Hops that would leave the ball are absent. For a site `v`, write
`σ_v` for the set of nonzero coordinates and write the inward weight
`w(v) = |σ_v|`.

A directed nearest-neighbor hop `v → u` is classified by three named clauses:

- seed-exit when `w(v) = 0`,
- both-weights-one (axis-one) when `w(v) = w(u) = 1`,
- support-drop when `w(u) < w(v)`.

The displayed clause-toggle `(s,a,d) = (0,1,1)` charges cost `3` if
both-weights-one holds or support-drop holds, and charges cost `1` otherwise.
Seed-exit is therefore cheap. This is a finite named hop-cost on `B_8(0)`. It
is not written into Admissibility, and it is not attached to L1.

One origin Dijkstra returns the in-ball arrivals

```text
t(4,0,0)=8,  t(6,0,0)=10,  t(8,0,0)=14,
t(2,2,2)=6,  t(3,3,0)=6,   t(4,4,0)=8.
```

The listed body-diagonal partner `(4,4,4)` has `|v|_1 = 12`, so it is not a
site of `B_8(0)`. Therefore `t(4,4,4)` is not a `B_8(0)` arrival, and
`12 t(8,0,0)^2 > 16 t(4,4,4)^2` is not a `B_8(0)` comparison.

The reverse bits that do live on this ball are:

- body pair `((4,0,0),(2,2,2))`: `12 t(4,0,0)^2 = 768 > 576 = 16 t(2,2,2)^2` holds;
- face pair `((4,0,0),(3,3,0))`: more-diagonal site `(3,3,0)` has the smaller
  `t^2/|v|_2^2`, since `16 t(3,3,0)^2 = 576 < 1152 = 18 t(4,0,0)^2`;
- face pair `((8,0,0),(4,4,0))`: more-diagonal site `(4,4,0)` has the smaller
  `t^2/|v|_2^2`, since `64 t(4,4,0)^2 = 4096 < 6272 = 32 t(8,0,0)^2`.

These values are not leftover of the B_6(0) cheap-seed table: on that smaller
ball `t(6,0,0)` is `12` because `(6,1,0)` is absent, while here `t(6,0,0)=10`.
The sites `(8,0,0)` and `(4,4,0)` are themselves outside B_6(0). Uniqueness
is not claimed among hop-costs.

Literal score lines used by the runner:

- t(4,4,4) is not a B_8(0) arrival
- 12 t(8,0,0)^2 > 16 t(4,4,4)^2 is not a B_8(0) comparison
- (8,1,0) is outside B_8(0)
- Do not write (0,1,1) into Admissibility

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "One Dijkstra on B_8(0) reports the named (0,1,1) arrivals and the body/face reverse bits that live on this ball. The large body partner (4,4,4) is outside the ball. The rule is displayed, not adopted."
trace_class: frontier_discovery
target_claim_id: clause_011_reverse_b8
target_blocker_text: "does reverse survive for body and face pairs under cheap-seed (0,1,1) on B_8(0)"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the B_8(0) reverse bits; do not write the clause-toggle into Admissibility and do not attach L1"
conditional_surface_status: "exact for the named (0,1,1) hop-cost on B_8(0); other clause triples, other radii, and any physical selector remain unclaimed"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Target And Proof Obligations

**Exact target.** On `B_8(0)` under the named `(0,1,1)` hop-cost, report
`t(4,0,0)`, `t(6,0,0)`, `t(8,0,0)`, `t(2,2,2)`, `t(4,4,4)`, `t(3,3,0)`, and
`t(4,4,0)`. Score whether `12 t(4,0,0)^2 > 16 t(2,2,2)^2` and whether
`12 t(8,0,0)^2 > 16 t(4,4,4)^2`. Score whether each face pair
`((4,0,0),(3,3,0))` and `((8,0,0),(4,4,0))` has smaller `t^2/|v|_2^2` on the
more-diagonal site. Do not write `(0,1,1)` into Admissibility. Do not attach
L1.

| Obligation | Disposition |
|---|---|
| named `(0,1,1)` hop-cost on `B_8(0)` | defined here; executed in Theorem 1 |
| six in-ball arrivals | proved here in Theorem 1 |
| `t(4,4,4)` on this ball | Theorem 1: not a site of `B_8(0)` |
| body reverse at `((4,0,0),(2,2,2))` | Theorem 2: holds |
| body reverse at `((8,0,0),(4,4,4))` | Theorem 2: not a `B_8(0)` comparison |
| face reverse at the two named pairs | Theorem 2: both hold |
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
B_8(0) = { v ∈ Z^3 : |v|_1 ≤ 8 }.
```

It contains exactly `833` sites. The directed graph used here has an edge
`v → u` precisely when `u − v` is one of the six shifts and both endpoints
lie in `B_8(0)`.

Inward weight: `w(v) = |σ_v|`, the number of nonzero coordinates of `v`.
Then `w(0) = 0`, `w(±e_i) = 1`, `w((3,3,0)) = 2`, and `w((2,2,2)) = 3`.

Named hop-cost for the displayed triple `(s,a,d) = (0,1,1)`:

```text
c(v → u) = 3  if  (w(v) = w(u) = 1)  or  (w(u) < w(v)),
c(v → u) = 1  otherwise.
```

Seed-exit hops have `w(v) = 0` and therefore cost `1` under this triple.
Axis-one hops and support-drop hops cost `3`.

Arrival time `t(v)` is the minimum sum of hop-costs over directed walks from
`0` to `v` that remain in `B_8(0)`. One Dijkstra computation from the origin
produces every in-ball `t(v)` used below.

The Euclidean squared length is `|v|_2^2 = v_1^2 + v_2^2 + v_3^2`. Body reverse
on an axis/body pair is the exact integer test `12 t_axis^2 > 16 t_diag^2`,
which is `t^2/|v|_2^2` larger on the axis site for the pair
`((4,0,0),(2,2,2))`. Face reverse on an ordered pair `(a,b)` in which `b` has
strictly more nonzero coordinates than `a` means

```text
t(b)^2 |a|_2^2 < t(a)^2 |b|_2^2.
```

## Theorem 1 — Named arrivals on B_8(0)

**Statement.** Under the named `(0,1,1)` hop-cost on `B_8(0)`,

```text
t(4,0,0)=8,  t(6,0,0)=10,  t(8,0,0)=14,
t(2,2,2)=6,  t(3,3,0)=6,   t(4,4,0)=8.
```

The site `(4,4,4)` satisfies `|v|_1 = 12 > 8`, so it is outside `B_8(0)` and
`t(4,4,4)` is not a `B_8(0)` arrival.

**Proof.** The directed graph is finite. Dijkstra's algorithm from the origin
computes every in-ball arrival. The runner executes that single computation
and reads the six listed sites.

Witnessing walks of those costs exist inside the ball. The walk

`(0,0,0) → (1,0,0) → (1,1,0) → (2,1,0) → (3,1,0) → (4,1,0) → (4,0,0)`

has hop-costs `(1,1,1,1,1,3)` and sum `8`. The walk

`(0,0,0) → (1,0,0) → (1,1,0) → (1,1,1) → (2,1,1) → (2,2,1) → (2,2,2)`

has hop-costs `(1,1,1,1,1,1)` and sum `6`. The walk

`(0,0,0) → (1,0,0) → (1,1,0) → (2,1,0) → (3,1,0) → (3,2,0) → (3,3,0)`

has hop-costs `(1,1,1,1,1,1)` and sum `6`. The walk

`(0,0,0) → (1,0,0) → (1,1,0) → (2,1,0) → (3,1,0) → (4,1,0) → (4,2,0) → (4,3,0) → (4,4,0)`

has hop-costs `(1,1,1,1,1,1,1,1)` and sum `8`. The walk

`(0,0,0) → (1,0,0) → (1,1,0) → (2,1,0) → (3,1,0) → (4,1,0) → (5,1,0) → (6,1,0) → (6,0,0)`

has hop-costs `(1,1,1,1,1,1,1,3)` and sum `10`. The walk

`(0,0,0) → (1,0,0) → (1,1,0) → (2,1,0) → (3,1,0) → (4,1,0) → (5,1,0) → (6,1,0) → (7,1,0) → (7,0,0) → (8,0,0)`

has hop-costs `(1,1,1,1,1,1,1,1,3,3)` and sum `14`. The last two hops are forced
by the ball: `(8,1,0)` has `|v|_1 = 9` and is therefore outside `B_8(0)`, so
the axis site `(8,0,0)` cannot be entered by a single support-drop from
`(8,1,0)`.

On `B_6(0)` the same local rule gives `t(6,0,0) = 12`, because `(6,1,0)` lies
outside that ball. The present table is therefore not leftover of the `B_6(0)`
cheap-seed arrivals.

## Theorem 2 — Body and face reverse bits

**Statement.** On `B_8(0)` under the named `(0,1,1)` hop-cost:

1. `12 t(4,0,0)^2 = 768 > 576 = 16 t(2,2,2)^2`.
2. `12 t(8,0,0)^2 > 16 t(4,4,4)^2` is not a `B_8(0)` comparison, because
   `t(4,4,4)` is not a `B_8(0)` arrival.
3. Each face pair `((4,0,0),(3,3,0))` and `((8,0,0),(4,4,0))` has smaller
   `t^2/|v|_2^2` on the more-diagonal site:
   `16 t(3,3,0)^2 = 576 < 1152 = 18 t(4,0,0)^2` and
   `64 t(4,4,0)^2 = 4096 < 6272 = 32 t(8,0,0)^2`.

These bits are displayed, not adopted.

**Proof.** Substitute the Theorem 1 arrivals. For the first body pair,
`| (4,0,0) |_2^2 = 16` and `| (2,2,2) |_2^2 = 12`, so the displayed integer
test is exactly `t^2/|v|_2^2` larger on the axis site: `64/16 = 4 > 3 = 36/12`.

The large body partner `(4,4,4)` is not a vertex of the graph, so no arrival
exists to insert into `12 t(8,0,0)^2 > 16 t(4,4,4)^2`. Enlarging the ball to
include that site would be a different object.

For the face pairs the more-diagonal site is the one with strictly more
nonzero coordinates: `w(3,3,0) = 2 > 1 = w(4,0,0)` and
`w(4,4,0) = 2 > 1 = w(8,0,0)`. The integer comparisons above are exactly
`t(b)^2 |a|_2^2 < t(a)^2 |b|_2^2`. The densities are `36/18 = 2 < 4 = 64/16`
and `64/32 = 2 < 49/16 = 196/64`.

Uniform graph-length on the same in-ball body pair gives arrivals `4` and `6`
and does not reverse. That comparator is not attached.

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
comparator as a parent of the reverse bits, or rewriting the bits as leftover
of those integers, would attach a different rule. The in-ball body pair
reverses under the named toggle and does not reverse under graph-length.

No later selector is forbidden. The claim is only that the present score does
not perform the selection.

## Boundary And Non-Claims

- The note does not claim that `(0,1,1)` is the unique reversing
  clause-toggle, nor that it minimizes any variance.
- The note does not extend the ball past radius eight. In particular it does
  not invent an arrival at `(4,4,4)`.
- The note does not identify hop-cost with a Record readout, a formation
  rate, or a nearest-neighbor possibility law.
- The note does not attach L1, and it does not treat the `B_6(0)` cheap-seed
  table as a substitute for the radius-eight Dijkstra.
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
| V1 | It answers the B_8 residual for the cheap-seed reversing toggle: the in-ball arrivals and the live body/face reverse bits are produced, and the missing large body partner is named as absent. |
| V2 | Current `origin/main` has no landed source note scoring these `(0,1,1)` reverse bits on `B_8(0)`. |
| V3 | The graph, costs, and one Dijkstra are finite and exact. No observational input is used. |
| V4 | `t(6,0,0)=10` distinguishes the table from the `B_6(0)` leftover `12`. The absence of `(4,4,4)` distinguishes the large body question from a B_12 score. |
| V5 | The toggle is displayed, not adopted. It is not a physical time, not an Admissibility edit, and not a uniqueness theorem. |

## No-Go Discipline Gate

The negative content is narrow: this score does not write `(0,1,1)` into
Admissibility and does not attach L1. No global impossibility for a later
hop-cost selector is claimed. These are scope boundaries, not impossibility.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| named `(0,1,1)` Dijkstra on `B_8(0)` | charge axis-one and support-drop only | executed; yields the displayed arrivals |
| enlarge the ball to include `(4,4,4)` | score `12 t(8,0,0)^2 > 16 t(4,4,4)^2` | different object; not this claim |
| reuse `B_6(0)` times | copy `t(6,0,0)=12` | false on this ball; `t(6,0,0)=10` |
| charge seed-exit as well | use the triple `(1,1,1)` | different arrivals; not this claim |
| uniform graph-length | charge `1` on every hop | no body reverse on `((4,0,0),(2,2,2))`; not attached |
| write the toggle into Admissibility | treat hop-cost as the axiom's nearest-neighbor rule | axiom edit; not derived |
| later selector among reversing triples | uniqueness or variance ranking | live route; not claimed here |

### N2 — wall independence

The missing physical selector, the missing identification of hop-cost with
Admissibility, the missing uniqueness statement, and the missing `(4,4,4)`
vertex are distinct residuals. This note claims no complete wall collection.

### N3 — hidden-condition scan

The ball radius, the three clause names, the toggle `(0,1,1)`, the reverse
predicates, and the listed sites are declared. Uniform graph-length is used
only as a disclosed contrast.

### N4 — source residual matching

The current axiom memo supplies the cubic nearest-neighbor substrate and
does not name a hop-cost. The residual is therefore a score under a
displayed hypothesis, matching those sources.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | named hops and inward-weight clauses | no continuum interpolation |
| per site | arrivals at the six in-ball targets | no lattice-wide time law |
| per mode | exact integer reverse tests | no spectral claim |
| per block | one Dijkstra on `B_8(0)` | no selector among all reversing triples |
| lattice wide | checked and not executed | no Admissibility edit; L1 not attached |

### N6 — live partial-closure paths

Live routes include a later derivation that would select a hop-cost from
Admissibility, a comparison among several reversing triples, a larger ball
that contains `(4,4,4)`, and a Record-typed reading of arrival. None is
closed here.

### N7 — hostile steelman

**Steelman:** Once the `B_6(0)` arrivals `t(4,0,0)=8` and `t(2,2,2)=6` are
known, the `B_8(0)` reverse bits are leftover.

**Answer:** On this ball `t(6,0,0)` drops from `12` to `10`, `t(8,0,0)=14`
and `t(4,4,0)=8` are new, and `(4,4,4)` is simply not present. Those facts
are not determined by the two-point `B_6(0)` times.

### N8 — cross-cycle echo

A full three-clause scan, a seed-exit-expensive support-drop rule, and a
radius-twelve ball that contains `(4,4,4)` are different objects. This note
does not import their arrivals as premises. It recomputes the `(0,1,1)`
arrivals on `B_8(0)` from the named cost.

**Gate disposition:** PASS for the six in-ball arrivals, the live body and
face reverse bits, the named absence of `(4,4,4)`, and the narrow
non-adoption statements. FAIL / DO NOT SHIP for “Admissibility is
`(0,1,1)`,” “L1 is the physical time,” or “no other reversing rule exists.”

## Primary Runner

The primary runner builds `B_8(0)`, evaluates the named hop-cost, computes
arrivals by one Dijkstra, checks the six in-ball times and the reverse bits
that live on this ball, records that `(4,4,4)` is outside the ball, pins the
current axiom wording, and runs mutation controls that replace the named
toggle by uniform graph-length or by an expensive seed-exit on a witnessing
walk. It authors no audit verdict.
