---
claim_id: clause_011_face_reverse_vs_k_b12_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Face-diagonal reverse versus integer scale k under the named (0,1,1) hop-cost on B_12(0) is reported for k=1..6. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/clause_011_face_reverse_vs_k_b12_2026_08_15.py
---

# Clause `(0,1,1)` Face Reverse Versus Integer Scale k On The Radius-Twelve Ball

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** one directed Dijkstra on the nearest-neighbor graph of the closed
radius-twelve ball under the named clause-toggle with cheap seed-exit and
expensive axis-one and support-drop hops. Face reverse versus integer scale
$k$ is reported for $k=1,\ldots,6$. Displayed, not adopted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/clause_011_face_reverse_vs_k_b12_2026_08_15.py`](../scripts/clause_011_face_reverse_vs_k_b12_2026_08_15.py)
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
t(2,0,0)=4,    t(4,0,0)=8,    t(6,0,0)=10,
t(8,0,0)=12,   t(10,0,0)=14,  t(12,0,0)=18,
t(1,1,0)=2,    t(2,2,0)=4,    t(3,3,0)=6,
t(4,4,0)=8,    t(5,5,0)=10,   t(6,6,0)=12.
```

For each $k=1,\ldots,6$, reverse means the displayed comparison

$$
\frac{t(2k,0,0)^2}{4k^2}>\frac{t(k,k,0)^2}{2k^2}
$$

holds, equivalently $t(k,k,0)^2\cdot 4k^2<t(2k,0,0)^2\cdot 2k^2$. The bit is
displayed, not adopted.

| $k$ | pair | axis $t^2/|v|_2^2$ | face $t^2/|v|_2^2$ | reverse |
|---|---|---|---|---|
| $1$ | $((2,0,0),(1,1,0))$ | $16/4=4$ | $4/2=2$ | yes |
| $2$ | $((4,0,0),(2,2,0))$ | $64/16=4$ | $16/8=2$ | yes |
| $3$ | $((6,0,0),(3,3,0))$ | $100/36=25/9$ | $36/18=2$ | yes |
| $4$ | $((8,0,0),(4,4,0))$ | $144/64=9/4$ | $64/32=2$ | yes |
| $5$ | $((10,0,0),(5,5,0))$ | $196/100=49/25$ | $100/50=2$ | no |
| $6$ | $((12,0,0),(6,6,0))$ | $324/144=9/4$ | $144/72=2$ | yes |

Exact integer comparisons:

- 4 t(1,1,0)^2 = 16 < 32 = 2 t(2,0,0)^2
- 16 t(2,2,0)^2 = 256 < 512 = 8 t(4,0,0)^2
- 36 t(3,3,0)^2 = 1296 < 1800 = 18 t(6,0,0)^2
- 64 t(4,4,0)^2 = 4096 < 4608 = 32 t(8,0,0)^2
- 100 t(5,5,0)^2 = 10000 > 9800 = 50 t(10,0,0)^2
- 144 t(6,6,0)^2 = 20736 < 23328 = 72 t(12,0,0)^2

The reverse bit is therefore not the same for every $k=1,\ldots,6$. Reverse
holds at $k=1,2,3,4,6$ and fails at $k=5$. The cheaper rival does not stay
reversed at $k=5$. The three even-$k$ face pairs already scored on this ball
under this toggle do not determine $t(2,0,0)$, $t(1,1,0)$, $t(6,0,0)$,
$t(3,3,0)$, $t(10,0,0)$, or $t(5,5,0)$. The $k=1,3,5$ times are
independent Dijkstra outputs on $B_{12}(0)$. Uniqueness is not claimed among hop-costs.
Displayed, not adopted. Do not attach L1.

Literal score lines used by the runner:

- t(2,0,0)=4
- t(4,0,0)=8
- t(6,0,0)=10
- t(8,0,0)=12
- t(10,0,0)=14
- t(12,0,0)=18
- t(1,1,0)=2
- t(2,2,0)=4
- t(3,3,0)=6
- t(4,4,0)=8
- t(5,5,0)=10
- t(6,6,0)=12
- (12,1,0) is outside B_12(0)
- Do not write (0,1,1) into Admissibility

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "One Dijkstra on B_12(0) reports the named (0,1,1) arrivals and the six face-versus-axis reverse bits versus integer scale k. The rule is displayed, not adopted."
trace_class: frontier_discovery
target_claim_id: clause_011_face_reverse_vs_k_b12
target_blocker_text: "does (0,1,1) keep the same face reverse bit for every k=1..6 on B_12(0), including k=5"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the B_12(0) face reverse bits versus k; do not write the clause-toggle into Admissibility and do not attach L1"
conditional_surface_status: "exact for the named (0,1,1) hop-cost on B_12(0); other clause triples, other radii, and any physical selector remain unclaimed"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Target And Proof Obligations

**Exact target.** On `B_12(0)` under the named `(0,1,1)` hop-cost, report
$t(2k,0,0)$ and $t(k,k,0)$ for each $k=1,\ldots,6$. Score whether
$t(2k,0,0)^2/(4k^2)>t(k,k,0)^2/(2k^2)$. Do not write `(0,1,1)` into
Admissibility. Do not attach L1.

| Obligation | Disposition |
|---|---|
| named `(0,1,1)` hop-cost on `B_12(0)` | defined here; executed in Theorem 1 |
| twelve in-ball arrivals at the six scales | proved here in Theorem 1 |
| face reverse versus integer scale $k$ | Theorem 2: yes/yes/yes/yes/no/yes |
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
Then `w(0) = 0`, `w(±e_i) = 1`, `w((2,2,0)) = 2`, and `w((5,5,0)) = 2`.

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

The Euclidean squared length is `|v|_2^2 = v_1^2 + v_2^2 + v_3^2`. Face reverse
on an ordered pair `(a,b)` in which `b` has strictly more nonzero coordinates
than `a` means

```text
t(b)^2 |a|_2^2 < t(a)^2 |b|_2^2.
```

For each integer $k=1,\ldots,6$ the ordered pair is $((2k,0,0),(k,k,0))$. The
second site is the more-diagonal site. The pair is reverse when
$t(2k,0,0)^2/(4k^2)>t(k,k,0)^2/(2k^2)$.

The three even-$k$ face pairs $((4,0,0),(2,2,0))$, $((8,0,0),(4,4,0))$, and
$((12,0,0),(6,6,0))$ cover only $k=2,4,6$. They do not determine the $k=1,3,5$
times. The $k=1,\ldots,6$ table is therefore not leftover of those three pairs.

## Theorem 1 — Named arrivals at each scale

**Statement.** Under the named `(0,1,1)` hop-cost on `B_12(0)`, for each
$k=1,\ldots,6$,

```text
t(2,0,0)=4,    t(1,1,0)=2,
t(4,0,0)=8,    t(2,2,0)=4,
t(6,0,0)=10,   t(3,3,0)=6,
t(8,0,0)=12,   t(4,4,0)=8,
t(10,0,0)=14,  t(5,5,0)=10,
t(12,0,0)=18,  t(6,6,0)=12.
```

These twelve values are Dijkstra outputs, not fitted scalars.

**Proof.** The directed graph is finite. Dijkstra's algorithm from the origin
computes every in-ball arrival. The runner executes that single computation
and reads the twelve listed sites.

Witnessing walks of those costs exist inside the ball. The walk

`(0,0,0) → (1,0,0) → (2,0,0)`

has hop-costs `(1,3)` and sum `4`. The walk

`(0,0,0) → (1,0,0) → (1,1,0)`

has hop-costs `(1,1)` and sum `2`. The walk

`(0,0,0) → (1,0,0) → (1,1,0) → (2,1,0) → (3,1,0) → (4,1,0) → (4,0,0)`

has hop-costs `(1,1,1,1,1,3)` and sum `8`. The walk

`(0,0,0) → (1,0,0) → (1,1,0) → (2,1,0) → (2,2,0)`

has hop-costs `(1,1,1,1)` and sum `4`. The walk

`(0,0,0) → (1,0,0) → (1,1,0) → (2,1,0) → (3,1,0) → (4,1,0) → (5,1,0) → (6,1,0) → (6,0,0)`

has hop-costs `(1,1,1,1,1,1,1,3)` and sum `10`. The walk

`(0,0,0) → (1,0,0) → (1,1,0) → (2,1,0) → (3,1,0) → (3,2,0) → (3,3,0)`

has hop-costs `(1,1,1,1,1,1)` and sum `6`. The walk

`(0,0,0) → (1,0,0) → (1,1,0) → (2,1,0) → (3,1,0) → (4,1,0) → (5,1,0) → (6,1,0) → (7,1,0) → (8,1,0) → (8,0,0)`

has hop-costs `(1,1,1,1,1,1,1,1,1,3)` and sum `12`. The site `(8,1,0)` has
`|v|_1 = 9` and therefore lies in `B_12(0)`. The walk

`(0,0,0) → (1,0,0) → (1,1,0) → (2,1,0) → (3,1,0) → (4,1,0) → (4,2,0) → (4,3,0) → (4,4,0)`

has hop-costs `(1,1,1,1,1,1,1,1)` and sum `8`. The walk

`(0,0,0) → (1,0,0) → (1,1,0) → (2,1,0) → (3,1,0) → (4,1,0) → (5,1,0) → (6,1,0) → (7,1,0) → (8,1,0) → (9,1,0) → (10,1,0) → (10,0,0)`

has hop-costs `(1,1,1,1,1,1,1,1,1,1,1,3)` and sum `14`. The site `(10,1,0)`
has `|v|_1 = 11` and therefore lies in `B_12(0)`. The walk

`(0,0,0) → (1,0,0) → (1,1,0) → (2,1,0) → (3,1,0) → (4,1,0) → (5,1,0) → (5,2,0) → (5,3,0) → (5,4,0) → (5,5,0)`

has hop-costs `(1,1,1,1,1,1,1,1,1,1)` and sum `10`. The walk

`(0,0,0) → (1,0,0) → (1,1,0) → (2,1,0) → (3,1,0) → (4,1,0) → (5,1,0) → (6,1,0) → (7,1,0) → (8,1,0) → (9,1,0) → (10,1,0) → (11,1,0) → (11,0,0) → (12,0,0)`

has hop-costs `(1,1,1,1,1,1,1,1,1,1,1,1,3,3)` and sum `18`. The last two hops
are forced by the ball: `(12,1,0)` has `|v|_1 = 13` and is therefore outside
`B_12(0)`, so the axis site `(12,0,0)` cannot be entered by a single
support-drop from `(12,1,0)`. The walk

`(0,0,0) → (1,0,0) → (1,1,0) → (2,1,0) → (3,1,0) → (4,1,0) → (5,1,0) → (6,1,0) → (6,2,0) → (6,3,0) → (6,4,0) → (6,5,0) → (6,6,0)`

has hop-costs `(1,1,1,1,1,1,1,1,1,1,1,1)` and sum `12`.

## Theorem 2 — Reverse bit versus integer scale k

**Statement.** For each $k=1,\ldots,6$ the displayed comparison is whether
$t(2k,0,0)^2/(4k^2)>t(k,k,0)^2/(2k^2)$. The six bits are:

- $k=1$: $t(1,1,0)^2/|(1,1,0)|_2^2=2<4=t(2,0,0)^2/|(2,0,0)|_2^2$ (yes)
- $k=2$: $t(2,2,0)^2/|(2,2,0)|_2^2=2<4=t(4,0,0)^2/|(4,0,0)|_2^2$ (yes)
- $k=3$: $t(3,3,0)^2/|(3,3,0)|_2^2=2<25/9=t(6,0,0)^2/|(6,0,0)|_2^2$ (yes)
- $k=4$: $t(4,4,0)^2/|(4,4,0)|_2^2=2<9/4=t(8,0,0)^2/|(8,0,0)|_2^2$ (yes)
- $k=5$: $t(5,5,0)^2/|(5,5,0)|_2^2=2\not<49/25=t(10,0,0)^2/|(10,0,0)|_2^2$ (no)
- $k=6$: $t(6,6,0)^2/|(6,6,0)|_2^2=2<9/4=t(12,0,0)^2/|(12,0,0)|_2^2$ (yes)

The bit is not the same for every $k$. Reverse holds at $k=4$ and fails at
$k=5$. The cheaper rival does not stay reversed at $k=5$. The three even-$k$
pairs do not determine the $k=1,3,5$ times or the $k=5$ fail.

These reverse bits are displayed, not adopted.

**Proof.** Substitute the Theorem 1 arrivals. The more-diagonal site is the
one with strictly more nonzero coordinates. The integer comparisons in
Result Up Front are exactly $t(b)^2 |a|_2^2 < t(a)^2 |b|_2^2$ when reverse
holds, and the opposite inequality at $k=5$:
$100\,t(5,5,0)^2=10000>9800=50\,t(10,0,0)^2$.

Uniform graph-length on the same six pairs gives arrivals equal to `|v|_1`
and does not reverse: the more-diagonal site then has the larger density
after cancelling the common hop count against `|v|_2^2`. That comparator is
not attached.

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
of those integers, would attach a different rule. The six face pairs reverse
under the named toggle at five scales and do not reverse under graph-length.

No later selector is forbidden. The claim is only that the present score does
not perform the selection.

## Boundary And Non-Claims

- The note does not claim that `(0,1,1)` is the unique reversing
  clause-toggle, nor that it minimizes any variance.
- The note does not extend the ball past radius twelve.
- The note does not identify hop-cost with a Record readout, a formation
  rate, or a nearest-neighbor possibility law.
- The note does not attach L1, and it does not treat the three even-$k$ face
  pairs as a substitute for the six-scale Dijkstra table.
- The note does not propose axiom text.
- Face-diagonal reverse versus $k$ is not claimed outside $B_{12}(0)$ and is
  not claimed for any hop-cost other than the named `(0,1,1)`.

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
| V1 | It answers the $k$-scale residual for the cheap-seed face pairs: the twelve arrivals and the six reverse bits are produced. |
| V2 | Current `origin/main` has no landed source note scoring these `(0,1,1)` reverse bits versus $k=1,\ldots,6$ on `B_12(0)`. |
| V3 | The graph, costs, and one Dijkstra are finite and exact. No observational input is used. |
| V4 | The $k=1,3,5$ times are new relative to the three even-$k$ face pairs. Reverse fails at $k=5$. |
| V5 | The toggle is displayed, not adopted. It is not a physical time, not an Admissibility edit, and not a uniqueness theorem. |

## No-Go Discipline Gate

The negative content is narrow: this score does not write `(0,1,1)` into
Admissibility and does not attach L1. No global impossibility for a later
hop-cost selector is claimed. These are scope boundaries, not impossibility.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| named `(0,1,1)` Dijkstra on `B_12(0)` | charge axis-one and support-drop only | executed; yields the displayed arrivals |
| reuse the three even-$k$ pairs | copy $k=2,4,6$ as a six-scale table | false; $k=1,3,5$ times are new |
| charge seed-exit as well | use the triple `(1,1,1)` | different arrivals; not this claim |
| uniform graph-length | charge `1` on every hop | no face reverse on the six pairs; not attached |
| write the toggle into Admissibility | treat hop-cost as the axiom's nearest-neighbor rule | axiom edit; not derived |
| later selector among reversing triples | uniqueness or variance ranking | live route; not claimed here |

### N2 — wall independence

The missing physical selector, the missing identification of hop-cost with
Admissibility, and the missing uniqueness statement are distinct residuals.
This note claims no complete wall collection.

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
| per site | arrivals at the twelve in-ball targets | no lattice-wide time law |
| per mode | exact integer reverse tests versus $k$ | no spectral claim |
| per block | one Dijkstra on `B_12(0)` | no selector among all reversing triples |
| lattice wide | checked and not executed | no Admissibility edit; L1 not attached |

### N6 — live partial-closure paths

Live routes include a later derivation that would select a hop-cost from
Admissibility, a comparison among several reversing triples, and a
Record-typed reading of arrival. None is closed here.

### N7 — hostile steelman

**Steelman:** Once the even-$k$ arrivals $t(4,0,0)=8$, $t(8,0,0)=12$,
$t(12,0,0)=18$, $t(2,2,0)=4$, $t(4,4,0)=8$, and $t(6,6,0)=12$ are known,
the six-scale reverse bits are leftover.

**Answer:** The $k=1,3,5$ times are not among those six values. In particular
$t(10,0,0)=14$ and $t(5,5,0)=10$ are new, and they are the pair that fails
reverse. Those facts are not determined by the even-$k$ face times.

### N8 — cross-cycle echo

A seed-exit-expensive support-drop rule and a three-pair even-$k$ census are
different objects. This note does not import their arrivals as premises. It
recomputes the `(0,1,1)` arrivals on `B_12(0)` from the named cost at every
integer scale $k=1,\ldots,6$.

**Gate disposition:** PASS for the twelve in-ball arrivals, the six reverse
bits versus $k$, and the narrow non-adoption statements. FAIL / DO NOT SHIP
for “Admissibility is `(0,1,1)`,” “L1 is the physical time,” or “no other
reversing rule exists.”

## Primary Runner

The primary runner builds `B_12(0)`, evaluates the named hop-cost, computes
arrivals by one Dijkstra, checks the twelve in-ball times and the six reverse
bits versus $k$, pins the current axiom wording, and runs mutation controls
that replace the named toggle by uniform graph-length or by an expensive
seed-exit on a witnessing walk. It authors no audit verdict.

## claim_scope

Face-diagonal reverse versus integer scale k under the named (0,1,1) hop-cost on B_12(0) is reported for k=1..6. Displayed, not adopted.
