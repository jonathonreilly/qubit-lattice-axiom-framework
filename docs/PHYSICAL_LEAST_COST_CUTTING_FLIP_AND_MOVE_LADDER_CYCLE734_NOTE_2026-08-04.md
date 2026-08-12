# Finite move structure at one supplied cell's four-column cost floor

Date: 2026-08-04

Claim type: bounded_theorem

Authority: none. Audit: unset. Constitutional effect: none. No axiom or
primitive is proposed or adopted. Cycle 734 of the emergent-geometry lane.

Primary runner:
[`scripts/physical_least_cost_cutting_flip_and_move_ladder_cycle734_2026_08_04.py`](../scripts/physical_least_cost_cutting_flip_and_move_ladder_cycle734_2026_08_04.py)
(31 PASS / 0 FAIL, fail-closed), with canonical cache
[`logs/runner-cache/physical_least_cost_cutting_flip_and_move_ladder_cycle734_2026_08_04.txt`](../logs/runner-cache/physical_least_cost_cutting_flip_and_move_ladder_cycle734_2026_08_04.txt)
and receipt
[`outputs/physical_least_cost_cutting_flip_and_move_ladder_cycle734_2026_08_04_receipt_2026-08-04.json`](../outputs/physical_least_cost_cutting_flip_and_move_ladder_cycle734_2026_08_04_receipt_2026-08-04.json).

Independent checker:
[`scripts/physical_least_cost_cutting_flip_and_move_ladder_cycle734_independent_check_2026_08_04.py`](../scripts/physical_least_cost_cutting_flip_and_move_ladder_cycle734_independent_check_2026_08_04.py)
(11 PASS / 0 FAIL, fail-closed), with canonical cache
[`logs/runner-cache/physical_least_cost_cutting_flip_and_move_ladder_cycle734_independent_check_2026_08_04.txt`](../logs/runner-cache/physical_least_cost_cutting_flip_and_move_ladder_cycle734_independent_check_2026_08_04.txt)
and receipt
[`outputs/physical_least_cost_cutting_flip_and_move_ladder_cycle734_independent_check_2026_08_04_receipt_2026-08-04.json`](../outputs/physical_least_cost_cutting_flip_and_move_ladder_cycle734_independent_check_2026_08_04_receipt_2026-08-04.json).

## Supplied model and premise boundary

Every result below is a theorem of a **supplied finite structural model**, not
of the framework axioms alone. The model chooses the unit four-cube, its
five-corner normalized-volume-one simplex pieces, exact interior-disjoint
24-piece dissections, and a four-coordinate pair charge.

- The **Lattice** axiom in
  [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies only
  spatial `Z^3` nearest-neighbour adjacency and the 24 proper cubic rotations.
- The registered
  [`KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md`](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md)
  supplies only equal tick/edge graining. It does not select a physical cell or
  provide a rule-to-tick correspondence.
- The four-cube, normalized-volume-one corner-simplex class, exact dissection
  rule, and charge counting corner pairs whose full four-coordinate `L1`
  separation exceeds one are declared inputs. This is **not** the spatial-only
  Cycle-725/Cycle-731 charge.
- The physical tick–Admissibility bridge and physical assembly-cell–simplex
  bridge remain open.

The landed
[`PHYSICAL_EXACT_ADJACENCY_DISSECTION_BRACKET_CYCLE725_NOTE_2026-08-03.md`](PHYSICAL_EXACT_ADJACENCY_DISSECTION_BRACKET_CYCLE725_NOTE_2026-08-03.md)
is prior authority for the supplied cell and minimal-piece convention. The
landed
[`PHYSICAL_COLUMN_FAMILY_PARITY_LAW_FORCED_ORBITS_CYCLE733_NOTE_2026-08-04.md`](PHYSICAL_COLUMN_FAMILY_PARITY_LAW_FORCED_ORBITS_CYCLE733_NOTE_2026-08-04.md)
is prior authority for the same four-column charge and its cost-144 floor. The
present runners independently reconstruct every object and count they use.
Cycles 731 and 732 are chronological context only; no certificate, support,
witness, or theorem from them is consumed.

## What this settles

In the declared model there are exactly 15,800 cost-144 dissections. Among all
`C(15800,2)=124,812,100` pairs of these minimizers, the number of replaced
pieces takes the exact values

```text
4, 6, 7, ..., 24
```

with 5 absent. The smallest cost-preserving change therefore replaces four
pieces, and there are 46,128 such unordered pairs. The absence of distances 1,
2, and 3 also proves that no cost-preserving re-cut of one, two, or three pieces
connects two floor dissections. This conclusion comes from the complete
minimizer-distance census, not from treating an incidence-compatible candidate
as automatically geometric.

Connect minimizers when they differ in at most `k` pieces. For cumulative
thresholds `k=4,...,10`, the exact component counts are

```text
349, 349, 157, 61, 61, 13, 1.
```

Thus the finite minimizer graph becomes connected at threshold ten. This is a
property of these 15,800 model dissections; it is not a mixing-time, dynamical,
or arbitrary-domain theorem.

Every four-piece edge replaces one of 120 eight-corner regions. Under the
carried order-48 action those regions form five families of sizes
`12,12,24,24,48`. Each region has either 2 or 24 genuine four-piece geometric
refills after adjoining the unchanged 20-piece complement, and exactly two of
those refills have local cost 24. Swapping these two floor refills is an
involution and accounts for all 46,128 four-piece minimizer edges.

## Exact finite objects

The unit four-cube has 16 corners and 4,368 five-corner subsets. Exact
determinants give normalized-volume spectrum
`0:1360, 1:2672, 2:320, 3:16`. The declared piece class contains the 2,672
volume-one simplices, so every dissection in that class has 24 pieces. Coarser
pieces exist and are excluded by the declared class; they are not impossible.

For a piece, the four-column charge counts corner pairs whose `L1` separation
across all four coordinates exceeds one. Its spectrum is
`6:400, 7:1216, 8:864, 9:192`. Every dissection has 24 pieces, so 144 is a lower
bound; the complete exact-cover search finds 15,800 attaining dissections and
therefore proves the floor. They use 192 of the 400 cost-six pieces, filling
four complete orbits of the carried action.

The carried action is 24 proper spatial cubic rotations times reversal of the
fourth coordinate. It has order 48 and partitions all pieces into 57 orbits of
sizes 16 and 48. It is not called the full four-cube symmetry group.

The generic sample chamber has 2,736 points, common integer denominator 12,810,
and zero piece-boundary incidences. Sample-point exact cover is used as a search
index, not as the final geometric predicate. Across the minimizer population,
15,168 piece pairs co-occur; every one is verified by an integer separating
hyperplane. Their unit volumes sum to the cell volume, so all 15,800 covers are
genuine dissections.

## Two- and three-piece candidate refills

Among the 15,168 co-occurring pairs, shared-corner counts are
`0:2976, 1:5280, 2:5376, 3:1248, 4:288`. Exactly the 288 pairs sharing four
corners have a second incidence-compatible two-piece refill. Their six-corner
Radon relation has two `+1`, two `-1`, and two zero coefficients. After the
unchanged 22-piece complement is adjoined, all 288 alternate refills pass the
full geometric dissection predicate. Their local costs rise by one in 192 cases
and by two in 96; none preserves the floor.

The submitted runner called 649,600 pairwise co-occurrence graph triangles
“triples sharing a cutting.” Review found that 13,568 are spurious cliques:
their three pairs occur in minimizers, but no single minimizer contains all
three. The repaired exact count is 636,032 genuine shared-cutting triples.

Of those genuine triples, 40,512 have an incidence-compatible second three-piece
refill candidate. Candidate local costs are `19:27264, 20:14592, 21:384`, above
the three-piece floor 18. These candidate counts are explicitly incidence
counts; the note does not promote all of them to geometric re-cuts. The exact
absence of a cost-preserving three-piece move is already independently closed by
the complete minimizer-distance census, which contains no distance three.

## Smallest regions and flip law

The 46,128 four-piece minimizer edges determine 120 distinct region corner
supports, each with eight corners and extent in all four coordinates. The five
carried region-family sizes are `12,12,24,24,48`. Depending on the family, a
region exposes 8 or 32 candidate pieces and has 2 or 24 genuine four-piece
geometric refills. Exactly two genuine refills attain local cost 24 in every
region.

Each four-piece edge removes one floor refill and inserts the other. Conversely,
whenever a minimizer contains one of the two floor refills, the swap returns
another minimizer, and swapping back restores the original. The 46,128 verified
applications equal the complete four-piece edge count. The note does not claim
that flips in overlapping regions are independent, commuting, or dynamically
available without a coordination rule.

## Independent reconstruction and hostile controls

The independent checker imports and executes no primary implementation. It
uses a separate Leibniz determinant expansion, pure coordinate action, exact
integer inverse acceptance, and the opposite (largest uncovered point) pivot in
its complete exact-cover search. That search visits 496,849 nodes rather than
the primary's 502,838 and returns the identical 15,800-dissection set.

Its 11 gates independently reconstruct all headline finite objects, including:

- 15,168 exactly separated co-occurring pairs;
- 649,600 pairwise graph triangles split into 636,032 genuine shared-cutting
  triples and 13,568 spurious cliques;
- the full 124,812,100-pair distance spectrum and component ladder;
- 120 regions in the five carried families; and
- genuine region refill counts 2/24 with exactly two floor refills each.

Hostile controls raise the charge of one cost-six piece, removing it from the
complete floor-search pool, and duplicate a simplex in a minimizer, destroying
the declared dissection cardinality. The primary separately rejects a
one-unit expected floor mutation and verifies all alternate two- and four-piece
geometric refills. Both runners fail closed.

## Boundary and honest read

- The theorem is only for normalized-volume-one corner simplices in one supplied
  cell with the declared four-column pair charge.
- The 15,800 minimizers, distance spectrum, component ladder, 120 regions, five
  region families, and flip count are exact only for this population.
- The two-piece alternatives and four-piece region refills pass genuine
  geometry. The three-piece refill spectrum is only an incidence-compatible
  candidate census; it is not called a geometric refill census.
- The no-one/two/three-piece cost-preserving statement quantifies over pairs of
  floor dissections in the complete census. It says nothing about nonminimum
  dissections or another cost.
- Connectivity at threshold ten is graph connectivity, not a local physical
  process, energy barrier, ergodicity rate, or independence of flips.
- No physical tick, framework Admissibility, physical assembly-cell selection,
  noncorner/coarser piece class, multi-cell domain, arbitrary extent, boundary,
  thermodynamic, or continuum claim is made.

## Dependencies

- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) — spatial adjacency and proper
  cubic rotations only.
- [Kinetic-isotropy primitive](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md) —
  equal tick/edge graining only.
- [Cycle 725 exact one-cell bracket](PHYSICAL_EXACT_ADJACENCY_DISSECTION_BRACKET_CYCLE725_NOTE_2026-08-03.md) —
  prior authority for the supplied cell and minimal-piece convention only.
- [Cycle 733 column-family parity law](PHYSICAL_COLUMN_FAMILY_PARITY_LAW_FORCED_ORBITS_CYCLE733_NOTE_2026-08-04.md) —
  prior authority for the four-column charge and cost-144 floor; all used
  objects are reconstructed locally.

## Proof-obligation disposition

CONDITIONAL. The finite census, distance graph, region classification, and flip
law are exact on the supplied model. Any physical reading is conditional on the
two open bridges above.

## Review record

The submitted branch passed its own 28 gates, but review found four material
evidence/scope defects: it treated 649,600 pairwise graph triangles as genuine
shared-cutting triples; it promoted sample-incidence refill candidates to
geometric re-cuts without adjoining the unchanged complement; it presented the
four-coordinate cost as if axioms supplied it; and it lacked fail-closed exit,
canonical caches, an independent checker, and a complete No-Go Discipline
packet. The repair separates the 13,568 spurious cliques, checks two- and
four-piece alternatives as complete geometric dissections, scopes the
three-piece spectrum to incidence candidates, declares the supplied-model
boundary, generates receipts, and adds independent reconstruction. No audit
verdict is authored or applied.

## No-Go Discipline Gate

This N1–N8 record covers two retained exact finite exclusions: (A) no pair of
floor dissections differs in one, two, or three pieces; and (B) the minimizer
graph is not connected below cumulative threshold ten. No universal `no_go`
claim ships. The primary cache contains the five required N5 resolution lines.

**N1 — Alternative route enumeration.** Every route is marked `ATTEMPTED` and
executed in the landed runners.

1. `ATTEMPTED` — complete minimizer-distance route: enumerate all 124,812,100
   pairs and observe minimum distance four, with no 1/2/3.
2. `ATTEMPTED` — exact two-piece geometry route: exhaust all co-occurring pairs,
   construct every alternative, adjoin 22 unchanged pieces, and show all 288
   genuine alternatives increase cost.
3. `ATTEMPTED` — genuine-triple route: intersect solution-membership bitsets to
   remove 13,568 spurious graph cliques before pricing candidate refills.
4. `ATTEMPTED` — opposite-pivot route: independently enumerate the identical
   15,800 minimizers with a search visiting a different node count.
5. `ATTEMPTED` — integer distance-matrix route: independently rebuild the full
   distance spectrum and cumulative component ladder.
6. `ATTEMPTED` — region-complement route: independently adjoin each unchanged
   20-piece complement and verify every 2/24 region refill geometrically.
7. `ATTEMPTED` — posting-list disjointness route: independently reproduce the
   29,069,284 distance-24 pairs from exact solution incidence.
8. `ATTEMPTED` — hostile mutation route: alter a minimum piece charge and
   duplicate a simplex; both cross their protected finite surfaces.

**N2 — Wall-independence audit.** The six open walls are NF (nonfloor
dissections), OC (other costs), PC (other piece classes), TR (physical
tick–Admissibility), SI (physical assembly-cell–simplex identification), and DE
(other domains or limits).

| pair | first→second | second→first | independent? | reason |
|---|---|---|---|---|
| NF–OC | no | no | yes | classifying nonminimizers for this cost does not classify another cost, or conversely |
| NF–PC | no | no | yes | nonminimum moves and changing the piece class are separate censuses |
| NF–TR | no | no | yes | finite graph structure does not realize a physical tick |
| NF–SI | no | no | yes | nonfloor classification does not identify framework cells |
| NF–DE | no | no | yes | one-cell nonminimum structure does not extend the domain |
| OC–PC | no | no | yes | changing the charge does not select the dissection class |
| OC–TR | no | no | yes | another finite cost does not supply a rule-to-tick bridge |
| OC–SI | no | no | yes | a cost convention and physical cell identification are distinct |
| OC–DE | no | no | yes | another one-cell cost does not imply multi-cell structure |
| PC–TR | no | no | yes | another piece class does not realize physical time |
| PC–SI | no | no | yes | choosing pieces does not identify physical assembly cells |
| PC–DE | no | no | yes | another one-cell class does not prove domain extension |
| TR–SI | no | no | yes | rule-to-tick and cell-shape bridges are distinct |
| TR–DE | no | no | yes | physical tick realization does not prove arbitrary-domain combinatorics |
| SI–DE | no | no | yes | identifying one cell does not extend the finite proof |

No wall automatically closes another; the collapsed set remains six.

**N3 — Hidden-wall scan.** The cell, volume normalization, piece class,
dissection predicate, four-coordinate charge, acting group, sample chamber,
floor population, move metric, and graph threshold convention are explicit.
“Local” means replacement cardinality inside this finite dissection population;
it is not framework locality. Sample cover is never promoted to geometry without
separator checks. No canonical, natural, obvious, or standard-physics premise
is hidden.

**N4 — Residual matching.** The no-small-move exclusion matches the complete
pair-distance residual: minimum four. The connectivity threshold matches the
exact cumulative component residual `349,349,157,61,61,13,1`. The two- and
four-piece geometric checks match their respective unchanged complements.
None of these residuals speaks about nonfloor states, other costs, other piece
classes, physical cells, or larger domains.

**N5 — Rhetoric audit.** Primary cached stdout records `per_element` for all
2,672 pieces, `per_site` for one supplied coordinate cell, `per_mode` not
executed because the model has no modes, `per_block` for the complete finite
minimizer/move/region censuses, and `lattice_wide` not executed with no
lattice-wide negative asserted.

**N6 — Partial-closure path scan.** NF closes by enumerating named higher-cost
levels; OC and PC close by rebuilding the exact proof for declared alternatives;
TR and SI may be imported by later bounded theorems and retired only by
theorem/audit; DE closes by an exact larger-domain reconstruction. Flip
independence can be studied through the overlap graph without any new axiom.

**N7 — Steelman.** A nonminimum dissection may admit a smaller preserving re-cut;
another charge or piece class may have distance-one moves; and a larger domain
may remain disconnected beyond ten. Those are concrete live routes. They do not
alter the complete finite distance or component census for this population.

**N8 — Cross-cycle echo.** Cycles 725 and 731 required the lane to distinguish
the supplied corner-simplex model from physical assembly and to avoid treating
sample-point cover as geometric dissection. This review applies both lessons:
the model boundary is explicit, graph cliques are separated from genuine
co-occurrence, and candidate refills are priced at their actual evidence level.

**Status: PASS.** All eight checks are answered; all eight N1 routes are
`ATTEMPTED`; the complete N2 pair table lands; N5 resolution lines land in the
canonical primary cache; and no universal negative remains.
