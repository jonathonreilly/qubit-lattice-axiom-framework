# Exact adjacency-cost bracket for dissections of one tick-box — Cycle 725

Date: 2026-08-03

Claim type: bounded_theorem

Authority: none. Audit: unset. Constitutional effect: none. No new axiom or
primitive is proposed or adopted.

Runner: `scripts/physical_exact_adjacency_dissection_bracket_cycle725_2026_08_03.py`
(30 PASS / 0 FAIL, exit 0, about 3 seconds; the runner fails closed — any failed
gate makes the process exit nonzero). Every number below is exact integer or exact
rational arithmetic over carried certificates and witness lists; no optimiser and
no floating point enters any gate.

## Supplied model, and what stays open

Everything in this note is a theorem of a **supplied** structural model, not of the
framework axioms alone. The model: the box is one lattice cell carried through one
tick — three spatial coordinates and a tick coordinate, sixteen corners; a piece is
the convex hull of five corners with nonzero volume, with all ten vertex pairs
graded by their spatial separation; a dissection is a family of pieces with disjoint
interiors whose volumes fill the box. What each premise actually supplies:

- the **Lattice** axiom of [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)
  supplies the spatial `Z^3` nearest-neighbour adjacency that grades the vertex
  pairs, and the 24 proper cubic rotations acting here — nothing else;
- the registered **kinetic-isotropy primitive** supplies the equal tick/edge
  graining under which the tick coordinate enters the model — no cell selection and
  no rule-to-tick correspondence;
- the corner-simplex/dissection structure itself — the choice of five-corner
  4-simplex pieces, the grading of all ten vertex pairs, and the dissection
  definition — is supplied here as the declared domain of the theorem.

Two identifications stay **open**, exactly as the landed cycle 724 note records for
this same model: the physical tick–Admissibility realization bridge (which rule
variation corresponds to which tick), and the identification of physical assembly
cells with pairwise-adjacency simplices. A nonsimplicial cell complex whose actual
1-skeleton edges are nearest-neighbour does not require every vertex pair to be
adjacent, and nothing in the framework selects simplicial cells. Nothing in this
note obliges any physical construction to pay the costs computed here; that reading
is available only if the open bridges close.

## What this settles, within the supplied model

Within the model, every vertex pair inside a piece whose spatial separation is more
than one step is a slot-use the Lattice axiom's adjacency does not supply. Counting
those uses over a dissection gives its **adjacency cost**. The landed cycle 724
note bracketed the cost of minimal-volume corner dissections between 96 and 108 by
counting arguments, exhibiting the monotone-path stencil at 108; the natural worry
is that 108 is a property of favoured stencils rather than of the box.

**Over all dissections of the tick-box into minimal-volume corner pieces, the
adjacency cost is bracketed exactly by 108 and 128, and both ends are attained.**
The lower end is not a stencil property: three structurally unlike dissections
reach 108. Cost parity is forced, so the attainable set is exactly the eleven even
values from 108 to 128.

**The bracket has an honest scope.** Admitting coarser corner pieces — pieces of
volume 2 and 3 alongside the minimal ones — drops the floor to 68, attained by a
genuine sixteen-piece dissection. Minimality of the pieces is precisely what pins
108.

## Objects

Volume throughout is the **normalized lattice 4-volume**
`|det(v_1 - v_0, ..., v_4 - v_0)|`, which is `4! = 24` times the Euclidean volume;
the whole box has normalized volume 24. This normalization is a declared convention
of the runner, load-bearing in the 24-piece count and in every volume-sum check
below.

Of the five-corner subsets, 1360 are degenerate and the remaining 3008 have
normalized volume 1, 2 or 3 with multiplicities 2672, 320 and 16. The 2672 volume-1
pieces are the **minimal** ones; a minimal-volume dissection therefore uses exactly
24 pieces. Adjacency cost runs from 3 to 7 over minimal pieces and from 3 to 9 over
all pieces.

The symmetry acting here is the axiom's 24 proper cubic rotations of the spatial
coordinates, with the tick fixed. They permute the minimal pieces in 114 orbits of
sizes 8 and 24.

## Method: certificates and witnesses, no solver in the artifact

Bounds are carried as integer multiplier vectors and checked directly; attaining
families are carried as piece lists and checked to be genuine dissections. Nothing
in the runner calls an optimiser.

The bounds are proved through **sample points**. A dissection covers every interior
point of the box exactly once, so a bound proved for every family that covers a
fixed set of sample points exactly once holds for every dissection. Three sample
families are built from pinned recipes: a fixed-weight family with one point per
minimal piece, an invariant family of 2736 points carried by the 24 rotations
into 114 point-orbits all of size 24, and a second invariant family on different
prime weights with the same construction, carried for the discipline gate's
chamber probe. All have zero boundary incidences against all 3008 pieces, which
is what makes the device sound; every piece contains between 6 and 1041 of the
primary invariant points, and every point of every family lies in some piece.
These carried families are the ones this note's orbit-level statements quantify
over; they are pinned recipes, not an enumeration of all possible sample
families.

Disjointness of the attaining families is **decided**, not sampled. Two convex
bodies have disjoint interiors exactly when a direction separates them; all
vertices here are zero-one corners, so differences lie in the ternary cube and a
supporting direction may be taken orthogonal to three ternary vectors — a
three-by-three ternary determinant, hence entries bounded by 4. Sweeping every
direction in that range decides the question.

## Results

**The floor is 108 and it is exact.** A fixed-weight integer certificate with
support 211 is tight at 2093 points and totals 108. An invariant certificate over
the rotation orbits reaches the same value using eight orbits at denominator 2,
tight at 2224 points. Three structurally unlike dissections attain it, with cost
profiles `{4: 12, 5: 12}`, `{3: 1, 4: 11, 5: 11, 6: 1}` and
`{3: 1, 4: 13, 5: 7, 6: 3}`; no two share a profile. Each attaining family is
carried as an explicit piece list and verified only by its own checks — no
identification of any carried family with a previously named stencil is claimed.
108 is a property of the box, not of a stencil.

**The ceiling is 128.** An invariant certificate at denominator 3 is tight at 1136
points and totals 128, and dissections attain it.

**Parity is forced over the minimal pieces.** The cost vector lies in the span of
the point-incidence columns together with the all-ones column over the two-element
field — rank 465 on both sample families — so every minimal-volume dissection has
even cost, and each of seven single-piece perturbations of the cost vector leaves
that span. Combined with the bracket, the attainable costs are exactly 108, 110,
112, 114, 116, 118, 120, 122, 124, 126, 128, every one realised by a checked
dissection.

**The carried parity certificate stops at the minimal pieces.** Over all pieces the
rank is again 465 but the cost vector is **not** in the span of the sampled
incidence columns plus the volume column, and the same elimination on the
fixed-weight sample family repeats the non-membership at rank 465, so the gap is
not an artifact of one sample recipe. That is a statement about this certificate
family, not about coarse dissections: it shows this incidence-plus-volume device
cannot certify parity past the minimal pieces. No odd-cost coarse dissection is
exhibited, and none is excluded; whether all-piece dissections share a parity is
open.

**The scope boundary: 68.** Admitting every corner piece, an invariant certificate
at denominator 6 is tight at 296 points and totals exactly 68, and a sixteen-piece
dissection with volume profile `{1: 8, 2: 8}` attains it. The bracket over all
corner pieces is 68 to 128.

**A denominator law governs invariant certificates built on the carried sample
family.** Every carried sample point-orbit has size 24, so a covariant certificate
at denominator D on this family produces a bound that is a multiple of 24/D —
computable in advance with no optimiser. Sixteen rungs were predicted this way and
every one is attained exactly by a carried certificate:

| bracket | D = 1 | D = 2 | D = 3 | D = 6 |
|---|---|---|---|---|
| minimal pieces, floor | 96 | 108 | 104 | 108 |
| minimal pieces, ceiling | 144 | 132 | 128 | 128 |
| all pieces, floor | 48 | 60 | 64 | 68 |
| all pieces, ceiling | 144 | 132 | 128 | 128 |

The endpoint fixes the denominator: 108 needs halves, 128 needs thirds, 68 needs
sixths. A single covariant scheme reaching all three needs sixths. Note the dip at
D = 3 in the first row — sharper denominators are not monotonically better.

**A remark on the landed cycle 724 floor of 96.** 96 is the largest multiple of 24
at or below 108, so within this certificate device — covariant over the carried
orbits, integer multipliers, denominator 1 — integral covariant bounds cap at
exactly 96, the same value the cycle 724 note reached by a different counting
route. Integrality alone is not the obstruction here: the fixed-weight family
carries an integral certificate reaching 108. It is covariance over these orbits
together with integrality that caps at 96. This names a mechanism inside the
carried device; it is not a statement about the cycle 724 argument itself.

**No single carried orbit certifies the floor.** Over the 114 point-orbits of the
carried invariant sample family, the best bound obtainable from any one orbit is
84, below 108; the carried halves certificate reaches 108 only by combining eight
orbits, and no single one of those eight yields more than 84 on its own. A second
pinned invariant sample family on different prime weights — carried with the same
soundness checks (2736 points, 114 orbits of size 24, zero boundary incidences,
every point used) — gives the same answer: its best single-orbit bound is also
84. Additionally, all 96 box symmetries (the improper half and tick reversal
included) permute the 3008 pieces preserving volume and cost, so conjugating any
sample family or certificate by a box symmetry preserves every bound total and
cannot manufacture a stronger single-orbit certificate. Whether a sample family
beyond the carried ones admits a stronger single-orbit certificate is untested —
the carried families are pinned recipes, and sample chambers are not enumerated.

**Every carried certificate is coordinatewise locally maximal.** For all nineteen
carried certificates — the eighteen invariant multiplier vectors and the
fixed-weight one — every unit strengthening breaks feasibility: all 114
single-orbit bumps and the uniform bump for each invariant certificate, and all
2672 per-piece bumps and the uniform bump for the fixed-weight certificate. None
of the carried bounds is a slack bound dressed up as a sharp one. Certificates
outside the carried set are not addressed.

**A discriminating negative control.** A cost-72 family of pieces whose volumes sum
to 24 is rejected: it has 86 overlapping interior pairs and fails to cover the
sample points exactly once on both families. Volume bookkeeping alone does not make
a dissection, and the certificates correctly do not apply to it.

## Author-side cross-checks: provenance only, not landed evidence

Before this note was written, headline numbers were re-derived by separate
machinery — a third sample family, linear-programming re-decisions of pairwise
intersection, simplex recomputation of the four bracket endpoints, and corruption
controls on the load-bearing gates. The scratch script that ran those checks is
**not carried** in this change, so none of that is reproducible from the landing
set and none of it is landed evidence; it must not be cited as such. The
audit-facing evidence for every claim above is the carried runner, its committed
cold transcript, and its pinned runner cache, and nothing in this note depends on
the uncarried checks.

## Boundary and honest read

- Every claim here is a theorem of the supplied tick-extended corner-simplex
  dissection model. The physical tick–Admissibility realization bridge and the
  identification of physical assembly cells with pairwise-adjacency simplices are
  open; nonsimplicial cell complexes are untested and are not excluded.
- 108 is exact **for minimal-volume corner pieces**. It is not a bound on
  dissections in general: coarser corner pieces reach 68. Any downstream use must
  carry the piece class with it.
- The bracket is a statement about one lattice cell carried through one tick.
  Extending it to longer tick runs or larger spatial blocks is open work, not a
  corollary.
- The sample-point device bounds a **larger** family than the dissections
  (everything covering the points exactly once). Both ends are attained by
  exhibited dissections, so no gap remains here, but the device on its own gives
  one-sided information.
- The single-orbit statement quantifies over the 114 point-orbits of each of the
  two carried invariant sample families only; the local-maximality statement
  covers the nineteen carried certificates only; the coarse-parity statement
  covers this incidence-plus-volume certificate family only, on both carried
  sample families. None of the three is a universal negative and no `no_go`
  claim ships; their committed N1–N8 record is the No-Go Discipline Gate section
  below, and the five-line N5 execution certificate is in the primary runner's
  cached stdout.
- The rotation group acting is the axiom's proper spatial rotations with the tick
  fixed. All 96 box symmetries — the improper half and tick reversal included —
  permute the pieces preserving volume and cost, so the census and the brackets
  are unchanged under them; orbit-level statements under a larger acting group
  (merged orbits, invariant chambers) remain open.
- Volume is the normalized lattice 4-volume, a declared convention (whole box 24).
- Nothing here derives a metric, a curvature, or a field equation. It fixes an
  exact combinatorial cost inside the supplied model; whether the geometry lane's
  physical constructions are subject to that cost depends on the open bridges
  above.

## Artifacts

- Runner: `scripts/physical_exact_adjacency_dissection_bracket_cycle725_2026_08_03.py`
- Cold output: `outputs/physical_exact_adjacency_dissection_bracket_cycle725_2026_08_03_cold_2026-08-03.txt`
- Receipt: `outputs/physical_exact_adjacency_dissection_bracket_cycle725_2026_08_03_receipt_2026-08-03.json`
  (the pretty-printed form of the RECEIPT line the runner prints)
- Runner cache: `logs/runner-cache/physical_exact_adjacency_dissection_bracket_cycle725_2026_08_03.txt`

## Dependencies

- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) — the Lattice axiom's spatial
  `Z^3` nearest-neighbour adjacency, which grades the vertex pairs, and its 24
  proper cubic rotations. That is all the axiom supplies here; it does not select
  the piece model.
- [Kinetic-isotropy primitive](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md) — the
  registered primitive supplying the equal tick/edge graining under which the tick
  coordinate enters the supplied model. It supplies no cell selection and no
  rule-to-tick correspondence.

Context, cited without a dependency edge — not load-bearing. Landed:
`PHYSICAL_SCALE_FREE_ADJACENCY_DISSECTION_BRACKET_CYCLE724_NOTE_2026-08-03.md`
(the same supplied-model boundary, the unimodular counting bracket 96 to 108, and
the monotone-path stencil verified at 108). Provenance only, absent from `main` at
the time of writing: the in-flight cycle 722 and cycle 723 measurements
`physical_oriented_diagonal_stencil_orbit_cycle722_2026_08_02` and
`physical_adjacency_admissible_assembly_trade_cycle723_2026_08_03`. The results
here are independent of all of them: every certificate and witness is carried in
this delta and re-verified locally by the runner.

## Review record

Iteration 1 of the combined adversarial science review (Sol, 2026-08-08) returned
FIX_THEN_PROCEED. The note was typed `bounded_theorem` and demoted from a
Lattice-only physical framing to a theorem of the supplied tick-extended
corner-simplex dissection model, adopting the landed cycle 724 boundary: the
tick–Admissibility realization bridge and the simplex identification are open, and
the "must pay" physical reading was removed. Three overbroad negatives were
narrowed to their computed scopes — "a single orbit cannot carry the floor" to the
114 carried point-orbits, "every carried bound is locally maximal" to the five
tested certificates, and "the parity relation does not extend" to this
incidence-plus-volume certificate family — and the earlier universal wording must
not be cited as a passed gate. The claimed identification of the first cost-108
witness with the cycle 723 monotone stencil was found false (the carried family
shares only the cost profile) and was removed. The runner was made fail-closed, the
normalized 4-volume convention was declared, the uncarried scratch cross-checks
were demoted to author provenance, the receipt is now generated by the runner with
full gate names, and the canonical pinned runner cache was added. The stale
branch-generated citation-graph manifest was reverted; the manifest acknowledgement
for this note is regenerated at landing from the integrated tree, as with the
sibling cycle 724 landing.

Iteration 2 (confirmation round, 2026-08-08): the confirmation seat verified the
iteration-1 science repairs but found the narrowed negative boundaries still owed
the mandatory landed no-go-discipline artifacts. Both land in this revision: the
committed N1–N8 gate record below, and the five-line N5 resolution certificate
(per_element / per_site / per_mode / per_block / lattice_wide) emitted by the
primary runner into its stdout and pinned cache. No `no_go` claim ships; the
claims stay bounded facts about carried objects.

Iteration 3 (second confirmation round, 2026-08-08): the iteration-2 checklist
used untested route markers, summarized wall independence in prose, and left the
84-versus-108 wording ambiguous. All three are repaired. Every N1 route is now
ATTEMPTED through a bounded in-runner computation: a second pinned sample family
(sound, best single-orbit cap 84 again), a 96-map box-symmetry volume-and-cost
preservation sweep, the strengthening test extended from five to all nineteen
carried certificates — which retires the iteration-2 untested-certificate wall
by computation — and a fixed-weight-family all-piece parity elimination
repeating the non-membership. N2 is now the full 15-row pairwise independence
table over the six remaining walls. Every surface states that 84 is the best
single-orbit bound and that 108 is reached only by the eight-orbit joint
certificate. The runner grew from 26 to 30 gates, all passing.

## No-Go Discipline Gate

This section is the committed N1–N8 record for the negative content that survives
the narrowing: three bounded, carried-object facts — (a) no single one of the 114
point-orbits of either carried invariant sample family yields a bound above 84,
and the carried halves certificate reaches 108 only by combining eight orbits;
(b) each of the nineteen carried certificates refuses every unit and uniform
strengthening; (c) the carried incidence-plus-volume certificate family over the
two-element field does not extend past the minimal pieces, on both carried sample
families. No `no_go` claim ships; every negative is priced to its exact carried
object. The N5 execution certificate (one line per resolution class) is in the
primary runner's cached stdout,
`logs/runner-cache/physical_exact_adjacency_dissection_bracket_cycle725_2026_08_03.txt`.

**N1 — Alternative route enumeration.** Marker contract: every enumerated route
is ATTEMPTED or RULED OUT BY PRIOR. All six routes here are ATTEMPTED; none uses
any other disposition.

1. Per-orbit envelope route (claim a): ATTEMPTED — each of the 114 carried
   point-orbits of the primary invariant family is optimized exactly by the
   two-variable lower-envelope argument, best value 84; within the carried
   affine-in-membership certificate device this optimization is complete for a
   single orbit.
2. Chamber probe route (claim a): ATTEMPTED — a second pinned invariant sample
   family on different prime weights is carried, passes the full soundness
   checks (2736 points, 114 orbits of size 24, zero boundary incidences, every
   point used), and its per-orbit optima are computed the same way: best value
   84 again. The attempt is bounded — two chambers are tested, not all; full
   chamber enumeration is the sample-family closure wall in the N2 table.
3. Symmetry route (claim a): ATTEMPTED — all 96 box symmetries (48 signed
   spatial permutations, tick fixed or reversed) are verified to permute the
   3008 pieces preserving volume and cost, so conjugating any sample family or
   certificate by a box symmetry preserves every bound total and cannot
   manufacture a stronger single-orbit certificate. Orbit-level statements
   under a larger acting group are the symmetry-enlargement wall in the N2
   table.
4. Certificate-completion route (claim b): ATTEMPTED — all nineteen carried
   certificates refuse every strengthening: 114 orbit bumps plus the uniform
   bump for each of the eighteen invariant certificates, 2672 per-piece bumps
   plus the uniform bump for the fixed-weight certificate. This computation
   retires the iteration-2 untested-certificate wall.
5. Parity elimination route (claim c): ATTEMPTED — two-element-field
   elimination on the primary invariant family, minimal and all-piece variants,
   rank 465, membership for minimal pieces and non-membership for all pieces,
   with seven unit-cut discrimination controls.
6. Parity second-family route (claim c): ATTEMPTED — the same all-piece
   elimination on the fixed-weight family repeats the result: rank 465,
   non-membership, seven unit cuts refuted.

No route beyond the claims' scopes is enumerated, because no negative is
asserted at those scopes: universal one-orbit impossibility, actual-dissection
coarse parity, and physical cost obligations are not claimed, and their attack
surfaces are carried as the open walls of the N2 table and the N7 steelman.

**N2 — Wall-independence audit.** The six open walls, with short labels declared
for the table:

- SF — sample-family closure wall: enumerate all boundary-free invariant sample
  families (chambers) and their single-orbit caps.
- OD — odd-coarse-dissection wall: exhibit an odd-cost coarse dissection, or
  prove a complete parity theorem for all-piece dissections.
- TR — tick-realization bridge: the physical tick–Admissibility realization
  (which rule variation corresponds to which tick).
- SI — simplex-identification bridge: identification of physical assembly cells
  with pairwise-adjacency simplices.
- SE — symmetry-enlargement wall: orbit-level statements under a larger acting
  group (improper half, tick reversal; merged orbits, invariant chambers).
- SC — scale-extension wall: longer tick runs and larger spatial blocks.

All 15 unordered pairs, both closure directions each:

| pair | closing the first closes the second? | closing the second closes the first? | independent? | why |
|---|---|---|---|---|
| SF–OD | no | no | yes | chamber enumeration produces certificates, not dissections or parity theorems; an odd dissection decides parity but names no chamber |
| SF–TR | no | no | yes | combinatorial closure inside the model versus a physical realization theorem |
| SF–SI | no | no | yes | chambers are model-internal; the cell-identification bridge is physical |
| SF–SE | no | no | yes | chambers are enumerated under the acting 24-element group; a larger group regroups orbits, which the smaller-group enumeration does not decide, and vice versa |
| SF–SC | no | no | yes | one-box chambers say nothing about longer runs or larger blocks, and conversely |
| OD–TR | no | no | yes | model parity versus physical tick realization |
| OD–SI | no | no | yes | model parity versus physical cell identification |
| OD–SE | no | no | yes | the group choice does not decide parity; parity does not decide the group |
| OD–SC | no | no | yes | one-box parity versus extended domains |
| TR–SI | no | no | yes | distinct bridges — rule-to-tick correspondence versus cell shape; the landed cycle 724 note records them separately |
| TR–SE | no | no | yes | physical bridge versus model symmetry choice |
| TR–SC | no | no | yes | physical bridge versus model domain size |
| SI–SE | no | no | yes | cell identification versus symmetry choice |
| SI–SC | no | no | yes | cell identification versus domain size |
| SE–SC | no | no | yes | group enlargement on one box versus domain extension |

All 15 pairs are independent in both directions; no row is double-counted. One
one-way pricing dependency is declared rather than collapsed: closing SF by full
chamber enumeration would re-price claim (a) from carried-family scope to a
genuine one-orbit impossibility. That is a claim-level re-pricing, not a
wall-closure implication, and it is exactly why claim (a) ships at carried-family
scope. The iteration-2 wall list had a seventh row, the untested-certificate
wall; it was closed in iteration 3 by running the strengthening test on all
nineteen carried certificates, and it no longer appears.

**N3 — Hidden-wall scan.** Iteration-1 review found the hidden scopes: "any one
point-orbit" hid "one of the 114 carried orbits"; "the parity relation does not
extend" hid "is not certified by the carried incidence-plus-volume columns";
"every carried bound" hid "the five tested certificates". All three are promoted
into the claim statements, the gate names, and the receipt — and the third was
then discharged outright in iteration 3 by testing all nineteen certificates.
Two hidden premises were promoted with them: the supplied corner-simplex model
(now the first section) and the normalized 4-volume convention (now declared).
Iteration 3 also promoted two previously implicit scopes into tested statements
plus explicit walls: "one pinned sample recipe" (now two carried families tested;
SF carries the remainder) and "proper rotations only" (now a 96-map preservation
sweep; SE carries the remainder).

**N4 — Residual matching.** Witness dispositions: claim (a) rests on the
per-orbit envelope computations on both carried invariant families — the
residual, "best certificate from one carried orbit within the carried device",
matches (a) exactly; the eight-orbit halves certificate supplies the positive
complement, and its 108 total is a joint eight-orbit bound, never a single-orbit
value. Claim (b) rests on the 115 strengthening refutations per invariant
certificate and the 2673 per fixed-weight certificate — the residual matches the
all-nineteen statement exactly. Claim (c) rests on the rank-465 eliminations and
non-membership on both carried sample families — the residual "cost vector
outside this span" matches (c), and the even cost-108 witness fixes minimal-piece
parity on the positive side. The uncarried author-side scratch checks are dropped
as negative witnesses (provenance only, per the cross-checks section).

**N5 — Rhetoric audit.** All three claims were checked across per-element /
per-site / per-mode / per-block / lattice-wide resolutions; the tested and
untested resolutions are stated line-by-line in the N5 resolution certificate in
the primary's cached stdout (per_element: exact recounted slacks and refusals
only, including all 96 symmetry images; per_site: the three carried pinned
sample recipes only; per_mode: 114 carried orbits per invariant family and all
nineteen carried certificates, none outside the carried set; per_block: minimal
versus all-corner piece classes, with no coarse dissection-parity negative;
lattice_wide: checked and not executed — no lattice-wide negative exists in this
package). Every phrase wider than these resolutions was narrowed in iterations
1–3; the note carries no universal negative.

**N6 — Partial-closure path scan.** The one partial-closure path found in
iteration 2 — running the strengthening test on the remaining fourteen
certificates — WAS executed in iteration 3 (N1 route 4), closing that wall by
pure computation. Of the remaining walls: SF closes by finite chamber
enumeration (unexecuted); OD closes by exhibiting an odd-cost coarse dissection
or proving a complete parity theorem; SE closes by recomputing the orbit-level
statements under the enlarged groups (the census and brackets are already shown
invariant); SC closes by extending the domain. No registered primitive supplies
the two physical bridges — kinetic-isotropy supplies the equal tick/edge
graining only — and no convention or labeling reframe closes them; both need
theorems. The legitimate import-bearing path is named: a consuming theorem may
take the simplex identification as an explicit import, bound it, and retire it
by audit. Nothing here forecloses that.

**N7 — Steelman.** Strongest counter-argument: "A chamber beyond the two carried
families may furnish a single-orbit dual reaching 108 — two chambers are tested,
not all; a single merged orbit under the enlarged 96-element group is the union
of up to two proper-rotation orbits and was never tested as a joint two-orbit
certificate; and coarse dissections may all share even parity under an invariant
invisible to both carried sample families — no odd dissection is exhibited." The
steelman is concrete and correct, and it is why nothing here ships as a no-go:
its three routes are exactly SF, SE, and OD, all carried OPEN in the N2 table,
and the claims as narrowed are facts about carried objects the steelman does not
touch.

**N8 — Cross-cycle echo.** The landed cycle 724 review demoted this same lane to
the supplied tick-extended simplex model and preserved the untested construction
escapes; this note carries that boundary forward as its first section instead of
repeating the broader physical tendency the iteration-1 review flagged here. The
repo's earlier falsification of a comparator slogan that generalized beyond its
comparator is echoed by pricing every negative to its exact carried family,
orbit set, and certificate list.

**Status: PASS** — narrow by construction: all eight checks answered, every N1
route ATTEMPTED under the marker contract, no failure condition hit, no `no_go`
claim ships, and both required artifacts land in this PR (this section, and the
N5 certificate in the primary's cached stdout).
