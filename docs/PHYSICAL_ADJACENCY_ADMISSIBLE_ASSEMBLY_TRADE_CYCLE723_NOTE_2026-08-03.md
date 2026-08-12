# Adjacency-admissible assembly and the excess-slot trade — Cycle 723

Date: 2026-08-03

Claim type: bounded_theorem

Status: proposed_retained

Authority: none. Audit status is set only by the independent audit lane.
Constitutional effect: none. This cycle edits no axiom, foundation,
Qualification, primitive, registry, policy, queue, audit-status, or PR-control
surface. No new axiom or primitive is proposed or adopted.

The exact result is conditional on a supplied combinatorial model: one
tick-extended unit cell, its sixteen `0/1` corners, and a complete dissection
into nondegenerate five-corner 4-simplices, with all ten vertex pairs counted as
slot-uses. The Lattice axiom supplies only the spatial `Z^3` nearest-neighbour
grading. It does not select simplicial assembly cells, the corner-only model, or
a physical rule-to-tick realization. Those bridges remain open.

**Primary runner:**
[`scripts/physical_adjacency_admissible_assembly_trade_cycle723_2026_08_03.py`](../scripts/physical_adjacency_admissible_assembly_trade_cycle723_2026_08_03.py);
cached stdout
[`logs/runner-cache/physical_adjacency_admissible_assembly_trade_cycle723_2026_08_03.txt`](../logs/runner-cache/physical_adjacency_admissible_assembly_trade_cycle723_2026_08_03.txt);
paired receipt
[`outputs/physical_adjacency_admissible_assembly_trade_cycle723_2026_08_03_receipt_2026-08-03.json`](../outputs/physical_adjacency_admissible_assembly_trade_cycle723_2026_08_03_receipt_2026-08-03.json).

**Independent checker:**
[`scripts/physical_adjacency_admissible_assembly_trade_cycle723_independent_check_2026_08_03.py`](../scripts/physical_adjacency_admissible_assembly_trade_cycle723_independent_check_2026_08_03.py);
cached stdout
[`logs/runner-cache/physical_adjacency_admissible_assembly_trade_cycle723_independent_check_2026_08_03.txt`](../logs/runner-cache/physical_adjacency_admissible_assembly_trade_cycle723_independent_check_2026_08_03.txt).
It does not import the primary. It re-enumerates the 4-simplex spectrum, the
tick-split floors, the Kuhn-path costs, all facet tetrahedra, and all 182 facet
covers with its own exact determinant and separating-axis code. It pins the
primary source and checks only the numerical receipt's schema; it does not call
the finite Cycle-696 matrix rows an independent exact result.

```yaml
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "separate the exact one-cell corner-dissection adjacency floor from the finite supplied-compiler deletion and cutoff-reduction measurements"
source_of_blocker_text: frontier_question
reachability_to_target: supports
artifact_role: runner_certificate
next_trace_action: "test nonsimplicial and refined-vertex constructions, and derive or reject an analytic compiler-level nullspace before extending the finite cutoff reduction"
```

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
reachability_to_target: supports
conditional_surface_status: "exact exhaustive one-unit-cell corner-simplex lower bound in a supplied dissection model; numerical Cycle-696 open-box rows at L=3,4 and supplied tolerances"
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "the corner enumeration and lower bound are exact finite arithmetic, while deletion, cutoff reduction, range, and frame partitions are bounded numerical compiler evaluations"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact target and obligation graph

**Exact target.** In the supplied one-cell corner-simplex dissection model,
establish a positive lower bound on spatial-footprint-exceeding slot-uses. For
the supplied Cycle-696 compiler only, measure deletion and cutoff-pseudoinverse
reduction at the explicitly named finite boxes, including the exact identities
of the tolerance-resolved stabilizers and proper-frame partitions.

**Obligation graph.** A performs the exact Kuhn slot census. B exhausts every
five-corner piece and rejects the affine-dependent high-adjacency control. C
exhausts the two forced boundary-facet covers and combines their exact floor
with conservative middle-volume bookkeeping. D assembles the supplied
Cycle-696 matrices. E reports the finite spectral cutoff, mixed coupling, and
nonzero stationarity residual. F compares exact frame-member signatures and
proper-frame equivalence partitions. R1–R4 are the dependent-quadruple,
48/48-distinctness, shifted-quadratic, and nonzero-residual controls. The
independent checker reconstructs A–C without importing the primary.

**Strongest missing lemma.** No framework principle selects this corner-simplex
model, and no exact analytic nullspace/decoupling theorem is proved for the
Cycle-696 matrix. Therefore the packet proves no physical all-construction
obstruction, no exact stationary Schur elimination, and no arbitrary-`L`,
boundary-free, or continuum law.

## Why this exists

The assembly stencil of this lane — the Kuhn path stencil on the tick-extended
unit cell — carries 240 edge slots, of which 120 are purely spatial. Of those
120, 72 lie along the six nearest-neighbour axis directions named by the Lattice
axiom and 48 do not. The 48 are the slots at which the construction reaches past
the axiom's own adjacency, and the natural question is whether some other
construction could be assembled from axiom-adjacency slots alone. If one could,
the finite proper-frame partition measured in the preceding cycles would become entirely
axiom-internal.

This cycle answers in two bounded halves. First, the excess is **forced inside the
supplied corner-simplex dissection model**: over a complete enumeration of its
corner pieces, none is adjacency-only, and a positive floor holds simplex by
simplex and for one full unit-cell dissection. Second, removing the exceeding slots from
the assembled second-variation form does not remove their content — it either
discards more than half of the form or trades cell-locality for range — and in
the scanned rows the finite stabilizer members and proper-frame partition agree.

## The seam is larger than 48

Give each edge slot its **spatial footprint weight**: the L1 weight of the spatial
part of its direction. Weight 0 is a same-site slot, weight 1 is a nearest-neighbour
slot of the axiom's 6-NN adjacency, and weight 2 or more exceeds that adjacency.
A tick-crossing slot still has a spatial part, so the correct count of "exceeds
adjacency" is by footprint, not by "purely spatial".

| spatial footprint weight | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| slot-uses in the stencil | 24 | 108 | 72 | 36 |
| distinct slot variables per cell | 8 | 36 | 18 | 3 |

So **108 of the 240 slot-uses, and 21 of the 65 distinct slot variables per cell,
exceed the axiom's 6-NN adjacency** — more than twice what the purely spatial
reading names. The 48 purely spatial exceeding slot-uses (36 face-diagonal and 12
body-diagonal) are one part of that seam, not the whole of it.

## No five-corner simplex in the supplied model is adjacency-only

The obstruction is affine independence, and it is visible already at small size.
Among three cell corners spanning a nondegenerate triangle, at most 2 of the 3
slots are 6-NN. Among four affinely independent corners, at most 3 of the 6 slots
are 6-NN; reaching 4 requires an affinely **dependent** quadruple, which cannot be
a simplex. The runner carries that dependent quadruple as an explicit rejector, so
the bound is a measurement and not an assertion.

Over the complete enumeration of corner 5-subsets of the tick-extended cell —
4368 subsets, of which **3008 are nondegenerate** — every nondegenerate corner
4-simplex carries **at least 3 footprint-exceeding slots**, at each of the four
tick splits (1, 2, 3 or 4 of its corners at tick 0). The floor is positive at every
split, so no five-corner simplex in this model is adjacency-only. The Kuhn path stencil
carries 5/4/4/5 by tick split against that floor of 3/3/3/3, and attains the
purely spatial floor 3/1/1/3 exactly.

## The one-unit-cell floor, and a coincidence that carries no content

The per-simplex floor does not by itself bound a whole cell. The facet structure
supplies the rest.

**Facet forcing.** A nondegenerate corner 4-simplex meets the tick-0 hyperplane in
a 3-face exactly when 4 of its corners lie there, and then in exactly one such face.
So the tick-0 facet of the cell is dissected by the 4-corner family and the tick-1
facet by the 1-corner family, and no other simplex contributes to either facet.

**Cone relation.** For those two extreme families, and over the complete
enumeration, 24 times the simplex volume equals 6 times the volume of its base
facet tetrahedron. Each extreme family therefore consumes exactly the facet's own
6 volume units of the cell's 24.

**Facet census.** The 3-cube facet admits 58 nondegenerate corner tetrahedra, of
6-fold volume 1 and 2, and **182 corner dissections**, of sizes 5 and 6. Interior
disjointness is decided by an exact integer separating-axis test — face normals of
both tetrahedra and all edge-pair cross products — so the census is exact, not
sampled. Pairwise interior disjointness plus total normalized volume 6 covers the
convex facet up to shared boundaries. Every one of the 182 covers carries at
least **18** exceeding slots.

**Bookkeeping.** Of the cell's 24 volume units, the two extreme families take 6
each, leaving 12 for middle-split simplices. A middle-split corner simplex has
24-fold volume at most 3, so at least 4 of them are needed, each carrying at least
3 exceeding slots. Thus every complete corner-simplex dissection of this one
tick-extended unit cell has the conservative floor

> 18 + 18 + 3 x 4 = **48 footprint-exceeding slot-uses**, against the Kuhn path
> stencil's 108.

**Caution, stated plainly.** This floor of 48 and the Kuhn stencil's purely spatial
excess of 48 are counts of two different things — a lower bound over complete
corner-simplex dissections on the full footprint-exceeding count, versus one particular stencil's
purely spatial count, whose own full count is 108. Their numerical agreement carries
no content and is gated in the runner as a distinctness check so that it cannot be
read as one.

## What removing the exceeding slots costs

Assemble the tick-resolved second-variation form Q on a spatially open box at tick
length 2, and split the slot variables by footprint weight into the
adjacency-admissible set A (weight at most 1) and the exceeding set D (weight at
least 2). At box size 3 this is 446 slot variables = 270 + 176.

Two properties of Q come first.

- **Q is cell-local.** Every nonzero coupling of Q joins two slots whose site
  supports fit in one unit cell; the largest entry at spatial extent 2 or more is
  exactly 0.000000e+00.
- **Q_DD has a tolerance-resolved near-flat block in the scanned rows.** At the
  supplied `1e-5` cutoff it has 16, 24 and 54 discarded directions at box size and tick length
  (3, 2), (3, 3) and (4, 2), matching the count of cells times ticks in each case.
  Their coupling through the mixed block Q_AD is below 1.0e-04, but is nonzero;
  and the live part is well conditioned: softest live eigenvalue 1.5900e-01 at box
  size 3 and 4.8367e-02 at box size 4, condition numbers 1.83e+02 and 6.00e+02.
  the cutoff-pseudoinverse reduction is numerically well conditioned on the
  retained complement. The discarded count is unchanged for cutoffs from
  `1e-6` through `1e-4` on these three rows.

**The deletion horn.** Restricting to Q_AA — simply dropping the exceeding
variables — discards 0.529 of the form's squared Frobenius weight at box size 3 and
0.547 at box size 4. More than half the assembled form lives in or across the
exceeding slots.

**The cutoff-reduction horn.** Applying the supplied cutoff pseudoinverse to D
preserves its constructed quadratic identity to below 1.0e-12, while a uniformly
shifted reduced form breaks that identity at 8.608e-04. This is **not** an exact
stationary elimination: the constructed vector has D-gradient norm
`3.147189e-06` and maximum component `1.333344e-06`. What the reduction does not keep is
locality. Writing the cutoff-reduced form's Frobenius weight as shares by spatial extent
(squares summing to one), box size 3 gives 0.400 on-site, 0.886 at range 1 and 0.235
beyond one cell; box size 4 gives 0.428, 0.836, 0.160 at range 2 and 0.304 at range
3 — the full box diameter. The largest entry beyond one cell is 6.318 in the
cutoff-reduced form against exactly 0.000000e+00 in the assembled form, so this range is
**generated by this cutoff reduction, not inherited from the assembly**, on the scanned rows.

On these finite rows, deletion pays in Frobenius weight and this supplied
cutoff-pseudoinverse construction pays in range. Other reductions are untested.

## The finite frame partition survives both operations

The tolerance-resolved signed/tick stabilizer and proper-frame equivalence
partition are read off three different matrices — the full assembled form,
the deleted form Q_AA, and the cutoff-reduced form — at box sizes 3 and 4. All six
rows have the identical twelve `(signed spatial map, tick shift)` stabilizer
members — six spatial maps at both tick shifts — and the identical eight-block
partition of the 24 proper-frame transforms. This is a finite identity-level
comparison, not merely equality of counts and not an arbitrary-box law.

## Boundary

- The exact theorem is conditional on a complete dissection of one tick-extended
  unit cell into nondegenerate 4-simplices chosen from its sixteen `0/1` corners,
  with every vertex pair counted as a slot-use. Nonsimplicial cells, incomplete
  families, refined/non-corner vertices, alternative slot conventions, and
  coarser cells are outside the theorem. The framework does not select this model.
- The unit-cell floor of 48 uses the facet census of one cell facet together with the
  volume bookkeeping; it is a floor on footprint-exceeding **slot-uses** of a corner
  stencil, not on distinct variables, and not on any quantity of a non-corner
  construction.
- The deletion and cutoff-reduction measurements are at box sizes 3 and 4 only.
  The reported nonzero far-range entries are finite observations; no decay or
  asymptotic claim is made, and the box is
  spatially open, so boundary effects are present at both sizes.
- The Frobenius shares are bookkeeping on the assembled matrix. They are not
  identified with any continuum quantity, and no continuum limit is taken.
- The comparison tolerance used for the symmetry identities and frame partitions, the cutoff
  threshold, and the compiler's finite-difference step are supplied constants of the
  runner, not measured quantities.
- Q is indefinite; nothing here is a positivity or stability statement about it.

## Honest auditor read

The strongest part is the conditional combinatorial half: exact integer arithmetic, complete
enumerations at every stage, an explicit rejector for the affine-independence bound,
and a cone relation that is verified rather than asserted. The weakest part is the
step from the per-simplex floor to the one-cell floor of 48, which chains the facet
census, the cone relation and the volume bookkeeping; each link is gated, but the
chain is the place to attack. The model-selection bridge is open. The 48/48 agreement is flagged in the runner precisely
because it would otherwise invite a reading it does not support. The assembly half is
two box sizes, and the claim that the cutoff reduction generates range rather than
inheriting it rests on the assembled form's beyond-cell entries being exactly zero,
which is measured and not tolerance-limited.

Current-main integration context, non-load-bearing: the later unaudited
`PHYSICAL_EXACT_ADJACENCY_DISSECTION_BRACKET_CYCLE725_NOTE_2026-08-03.md`
independently strengthens the supplied-model census to an exact floor of 68
when all corner-piece volumes are allowed, and to 108 for minimal-volume
pieces. Therefore this packet's 48 is a conservative intermediate lower bound,
not the strongest bound currently recorded. No Cycle725 certificate is used by
the proof here, so this provenance notice deliberately creates no dependency
edge.

## Dependencies

- [Tick-extension second variation](CUBIC_COXETER_REGGE_3PLUS1_TICK_EXTENSION_SECOND_VARIATION_NARROW_THEOREM_NOTE_2026-06-09.md) — landed, unaudited: the tick-extended second-variation object assembled here.
- [Proper-cubic covariance ceiling](PHYSICAL_PROPER_CUBIC_COVARIANCE_CEILING_CYCLE690_NOTE_2026-07-24.md) — landed, unaudited: the covariance ceiling of unit-cell triangulations.
- [Direction set versus triangulation covariance](PHYSICAL_DIRECTION_SET_VS_TRIANGULATION_COVARIANCE_CYCLE695_NOTE_2026-07-25.md) — landed, unaudited: the direction-set reading of covariance, and the Kuhn edge-direction census.
- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) — the Lattice axiom's 6-NN adjacency and proper cubic rotations, which define the admissible set here.
- [Cycle-696 open-coframe endpoint compiler](../scripts/physical_open_coframe_k_endpoint_compiler_cycle696_2026_07_25.py) — landed, audit-excluded support: the complete numerical assembly contract used verbatim, including its Cycle-576 and Regge support closure. It supplies the finite matrix; it is not audit authority.
- [Stencil-derived centrality](PHYSICAL_STENCIL_DERIVED_CENTRALITY_CYCLE721_NOTE_2026-08-02.md) — landed, unaudited: the finite tick-fixed/folded frame interpretation. Its exact determinant split is retained; no improper map is promoted to a framework symmetry here.
- [Oriented diagonal stencil orbit](PHYSICAL_ORIENTED_DIAGONAL_STENCIL_ORBIT_CYCLE722_NOTE_2026-08-02.md) — landed, unaudited: the finite proper-frame orientation and line-subgroup convention used to name the proper-frame partition. No all-stencil or arbitrary-parameter selection is imported.

## No-Go Discipline Gate

This packet contains a bounded wall (“no adjacency-only corner-simplex
dissection” in the supplied model) and therefore records the mandatory N1–N8
stress test. It does not ship a `no_go` claim.

**N1 — alternative-route enumeration.** The exhaustive piece census attempts
every nondegenerate five-corner 4-simplex, including normalized volumes 1, 2,
and 3, and the facet search attempts every exact corner-tetrahedron cover. The
Kuhn route is retained as a nonoptimal upper witness at cost 108. Refined or
non-corner vertices, nonsimplicial cell complexes, different slot accounting,
coarser cells, and non-pseudoinverse reductions are explicit OPEN routes because
they are outside the enumeration.

**N2 — wall-independence audit.** The remaining walls are pairwise distinct:
corner-only vertex choice; simplicial complete-dissection choice; one-cell and
one-tick extent; all-pairs slot-use accounting; supplied Cycle-696 compiler;
finite open boxes; and supplied spectral/tolerance cutoffs. Removing any one
does not logically remove the others. The exact lower bound uses only the first
four; the numerical horns use the latter three and do not strengthen the exact
model boundary.

**N3 — hidden-wall scan.** Hidden assumptions made explicit are normalized
4-volume 24 for the cell; coverage inferred from interior disjointness plus full
volume; multiplicity counting of slot-uses rather than distinct variables;
periodic tick and spatially open compiler boxes; finite-difference Hessians; an
indefinite matrix; and tolerance-resolved, not exact, spectral/frame identities.

**N4 — residual matching.** Exact integer anchors are `4368`, `3008`, the
tick-split floor `3/3/3/3`, `58` facet tetrahedra, `182` covers, facet floor `18`,
and conservative unit-cell floor `48`. Numerical residuals are reported rather
than hidden: maximum discarded eigenvalue below `1e-5`, mixed coupling below
`1e-4`, nonzero D-gradient norm `3.147189e-06`, quadratic-identity deviation
below `1e-12`, and the stated frame tolerance. The primary cache carries the
five-line N5 resolution certificate.

**N5 — resolved granularity.** The canonical primary stdout states exactly what
is resolved at `per_element`, `per_site`, `per_mode`, `per_block`, and
`lattice_wide` resolution. The last is explicitly unresolved.

**N6 — rhetoric audit.** “Forced”, “floor”, and “no adjacency-only” always refer
to the supplied one-cell corner-simplex dissection model. The numerical branch
uses “cutoff reduction”, never exact stationary elimination. No wording promotes
the result to all framework constructions, arbitrary lattice size, or continuum.

**N7 — strongest surviving steelman.** A nonsimplicial nearest-neighbour cell
complex does not require every pair of its vertices to be an edge, and a refined
or rational-vertex triangulation can leave the enumerated corner universe. Either
could realize an adjacency-only assembly without contradicting any gate here.
This is the preferred escape route, not a footnote.

**N8 — cross-cycle echo.** Cycle696 supplies only the finite compiler. Cycle721
distinguishes tick-fixed and folded determinant gradings; Cycle722 distinguishes
determinant from diagonal orientation. This note preserves both distinctions and
uses their names only for its finite proper-frame partition. It neither imports
an improper framework symmetry nor echoes an all-stencil selection claim.

## Review record

Iteration 1 of adversarial science review (Codex, 2026-08-12) returned
FIX_THEN_PROCEED. The submitted exact-stationarity claim was refuted directly:
the cutoff-constructed vector has nonzero D-gradient norm `3.147189e-06`.
The packet now calls it a cutoff-pseudoinverse quadratic reduction and gates the
residual. Floating determinant/rank paths were replaced by exact arithmetic;
the negative theorem was narrowed to a supplied one-cell corner-simplex
dissection model and given a complete N1–N8 record plus cached N5 certificate;
finite flat counts and range observations were de-lawed. Load-bearing Cycle696,
Cycle721, and Cycle722 dependencies are now real graph edges. The evidence
surface now has declared transitive inputs, deterministic receipt generation,
canonical caches, and a source-pinned independent exact checker. Finally,
frame-survival gates compare exact stabilizer-member signatures and exact
proper-frame partitions rather than cardinalities alone. Audit remains unset;
this review applies no audit verdict.

## What this opens

1. **Non-corner constructions.** The floor proved here is over corner vertex sets.
   A construction on a refined cell, or with vertices at other rational positions,
   is untouched by this enumeration and is the natural next place to look for an
   adjacency-only assembly.
2. **The generated range.** The cutoff-reduced form has nonzero entries at the
   full box diameter in these two rows. Measuring how that range behaves as the box grows would
   turn a two-size observation into a law.
3. **The 18 of the facet census.** Every facet dissection carries at least 18
   exceeding slots, and the two facet families are forced. Whether that 18 is itself
   forced by the facet's own adjacency graph, independently of the volume argument,
   is a self-contained question.
4. **Finite partition insensitivity.** The tolerance-resolved stabilizer members
   and proper-frame partition are identical across all three forms on both rows.
   Identifying the smallest sub-block of the admissible variables that still carries
   the 8-valued label would sharpen what the label actually depends on.
