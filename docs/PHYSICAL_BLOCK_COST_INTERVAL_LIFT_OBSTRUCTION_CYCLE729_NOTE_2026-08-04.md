# An exact `[216,320]` supplied-block cost interval with a non-regular maximizer — Cycle 729

Date: 2026-08-04

Claim type: bounded_theorem

Authority: none. Audit: unset. Constitutional effect: none. This cycle edits no
axiom, approved primitive, premise registry, audit verdict, queue, or PR-control
surface. No new axiom or primitive is proposed or adopted.

Status: **unaudited source note**. This is an exact finite theorem of a supplied
corner-simplex model, not a derivation of that model from the framework axioms.

## Result

In the supplied model below, every 48-piece dissection of the two-cell,
one-tick box has declared adjacency cost in

\[
216 \leq C \leq 320,
\]

and both endpoints are attained. The lower endpoint is reached by the stacked
monotone-path dissection. A second carried dissection reaches `320`.

The carried cost-`320` maximizer is not face-to-face and therefore is not the
lower hull of any assignment of heights to the box's 24 corners. This is a
statement about that exhibited maximizer in this finite model. It does not say
that every maximizing dissection is non-regular, that lifting cannot find some
other maximizer, or that a physical construction must optimize this charge.

## Supplied model and premise boundary

The finite domain is supplied rather than selected by the framework:

- spatial corners are `{0,1,2} x {0,1} x {0,1}`;
- the tick coordinate is `{0,1}` at the same regulator graining;
- a piece is a five-corner 4-simplex of normalized volume one;
- a dissection is an interior-disjoint exact cover by 48 such pieces; and
- a piece's declared charge is the number of its ten vertex pairs whose
  spatial L1 separation is greater than one.

There are 24 corners and `42504` five-corner subsets. Exact determinant
enumeration gives `17280` normalized-volume-one pieces, with charge spectrum

```
3:128, 4:768, 5:2816, 6:4928, 7:5760, 8:2608, 9:272.
```

The Lattice axiom supplies only the spatial `Z^3` nearest-neighbour grading and
proper cubic rotations. The registered kinetic-isotropy primitive supplies
only equal tick/edge graining. Neither source selects corner simplices,
minimal-volume dissections, this all-pairs charge, a physical block, or a
tick--Admissibility realization. Those are open physical bridges, not hidden
consequences of the exact finite calculation.

## Exact certificate proof

The proper-spatial stabilizer of the elongated box, together with tick
reversal, has order `16`. Its action partitions the `17280` pieces into `1080`
orbits of size `16`.

For each piece orbit, the runner constructs a generic point orbit. The point
coordinates are superincreasing integer barycentric combinations of the
piece's corners. Exact barycentric tests gate all `17280` points against all
`17280` pieces and find zero boundary incidences. Consequently, every point is
interior to exactly one piece of any supplied dissection.

Let `M[p,o]` count points of orbit `o` interior to piece `p`. If integer data
`u_o`, `Z`, and positive denominator `D` satisfy

\[
\sum_o M[p,o]u_o + Z \leq D c(p)
\]

for every minimal piece, summing over a 48-piece dissection gives

\[
16\sum_o u_o + 48Z \leq DC.
\]

Reversing the inequality gives an upper certificate. Symmetry compresses the
verification but is not assumed of the dissection: both certificates are
checked on all `1080` representative rows and again on all `17280` pieces.

The carried floor certificate has denominator `512`, numerator `110144`, least
slack zero, and `30` tight orbit rows. Thus

\[
C \geq \left\lceil 110144/512 \right\rceil = 216.
\]

The carried ceiling certificate has denominator `49`, numerator `15728`, least
slack zero, and `53` tight orbit rows. Thus

\[
C \leq \left\lfloor 15728/49 \right\rfloor = 320.
\]

The certificate vectors are supplied integer data verified by the runners;
the artifact does not derive or optimize them. No minimal-denominator claim is
made.

## Endpoint witnesses

The primary and independent runners certify each witness by exact normalized
volume, total volume `48`, and a separating integer normal for all `1128`
piece pairs. Since every piece lies in the box, pairwise interior-disjointness
and the full volume establish exact cover.

- The two stacked monotone-path stencils contain 48 pieces and cost `216`.
- The Cycle 728 carried witness contains 48 pieces and costs `318`.
- The new carried witness contains 48 pieces and costs `320`.

The independent checker does not import or execute the primary. It parses the
carried literals, reconstructs the `42504`-subset census with a recursive exact
determinant, builds exact unimodular inverses by cofactors, and searches a
broader set of `2928` primitive integer normals in `[-4,4]^4` for every witness
pair. It independently obtains costs `216`, `318`, and `320` and all `1128`
separations for each witness.

## What the lower-hull obstruction proves

A regular corner triangulation is the lower-face complex of lifted corners.
Faces of a polytope meet face-to-face. Therefore a supplied dissection with an
unpaired tetrahedral facet strictly inside the box cannot be such a lower hull.

Exact tetrahedral-facet counting finds:

- no unpaired internal facets for the stacked `216` witness;
- no unpaired internal facets for the Cycle 728 cost-`318` witness; and
- `16` unpaired internal facets for the cost-`320` witness.

The first two comparisons are also positive, not merely absence-of-obstruction
checks. Supplied integer height vectors clear all `912` outside-corner lower
face inequalities with exact minimum margins `16` and `32`, respectively.
Thus these two witnesses are regular, while the exhibited cost-`320` witness
is not.

This proves that the finite configuration space has a non-regular maximizer.
It does not prove that the regular subspace has maximum `318`: the runners do
not enumerate every regular dissection, and another regular cost-`320` witness
is not excluded.

## Relation to Cycle 728

[Cycle 728](PHYSICAL_SPATIAL_BLOCK_SEAM_DICHOTOMY_CYCLE728_NOTE_2026-08-04.md)
is a direct but unaudited dependency. It supplies the exact cost-`318` witness,
the seam-respecting bracket `[216,256]`, and the earlier global maximum window
`[318,324]`. The primary runner reads Cycle 728's receipt, parses its
`BLOCK_HI` literal without executing the dependency, and gates entrywise
identity with the local `PRIOR` data.

Cycle 729 sharpens the earlier global window to `[216,320]` by new certificates
and a new witness. It does **not** claim that Cycle 728 used a lift-only search,
that `318` was the maximum among regular triangulations, or that Cycle 728
proved a different certificate shape was necessary. Those statements appeared
in the submitted Cycle 729 prose but are not carried by the reviewed Cycle 728
package and have been removed.

Cycle 727 is ordering and affine-comparison context only. Its long direction is
the tick coordinate, while the charge here reads the long spatial coordinate;
no Cycle 727 theorem bears load here. Cycle 725 is model lineage only: this
runner reconstructs its own finite census, certificates, and endpoint witnesses
rather than importing the one-cell bracket.

## Honest boundary

- The exact interval quantifies only over supplied normalized-volume-one
  corner-simplex dissections of this one `2 x 1 x 1` spatial block through one
  equal-grained tick.
- The cost is the declared spatial-L1 vertex-pair charge. The framework does
  not require a physical construction to pay it.
- The cost-`320` witness is non-face-to-face but remains a valid dissection:
  exact pair separation and total volume certify the cover without assuming a
  conforming complex.
- Only this carried maximizer is proved non-regular. No classification of all
  maximizers or exact maximum over regular triangulations is carried.
- No result is claimed for coarser or non-corner pieces, nonsimplicial cells,
  other charges, larger blocks, longer tick runs, alternative boundaries,
  thermodynamic or continuum limits, curvature, a metric, an action, or a
  field equation.

## Evidence package

- Primary runner:
  `scripts/physical_block_cost_interval_lift_obstruction_cycle729_2026_08_04.py`
- Independent checker:
  `scripts/physical_block_cost_interval_lift_obstruction_cycle729_independent_check_2026_08_04.py`
- Primary cache:
  `logs/runner-cache/physical_block_cost_interval_lift_obstruction_cycle729_2026_08_04.txt`
- Independent cache:
  `logs/runner-cache/physical_block_cost_interval_lift_obstruction_cycle729_independent_check_2026_08_04.txt`
- Generated receipt:
  `outputs/physical_block_cost_interval_lift_obstruction_cycle729_2026_08_04_receipt_2026-08-04.json`

The primary contains no solver and exits nonzero on any failed gate. The
independent checker uses different exact determinant, inverse, orbit,
membership-load, separator, and lower-hull implementations. It also damages
both certificates and one witness and requires every mutation to fail its
target gate.

## Dependencies

- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) — supply only the spatial
  lattice grading and proper cubic rotations.
- [Kinetic-isotropy primitive](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md)
  — supplies only equal regulator graining of the tick and spatial axes.
- [Cycle 728 spatial-block seam theorem](PHYSICAL_SPATIAL_BLOCK_SEAM_DICHOTOMY_CYCLE728_NOTE_2026-08-04.md)
  — landed but unaudited; supplies the exact cost-`318` witness and the
  `[318,324]` window under the same supplied-model boundary.

## No-Go Discipline Gate

This packet covers only the finite negative statement that the one carried
cost-`320` maximizer is not the lower hull of any height assignment to these 24
corners. It does not ship a physical, all-maximizer, all-model, arbitrary-block,
or continuum no-go.

**N1 — Alternative route enumeration.** The route families are normalized by
mathematical mechanism and terminal obligation.

1. `ATTEMPTED` — face-complex route: exact facet multiplicities identify `16`
   tetrahedral facets carried once and off every box boundary face. Since the
   separately certified witness covers the box, these are nonconforming
   internal facets; lower faces of a polytope form a face-to-face complex.
2. `ATTEMPTED` — positive comparator route: all `912` strict lower-face
   inequalities are reconstructed for the `216` and `318` witnesses, and
   carried integer heights clear them with margins `16` and `32`. This shows
   the implementation can certify regular objects and is not a blanket
   rejection.
3. `NOT ATTEMPTED` — a Farkas dual certificate for infeasibility of all `912`
   cost-`320` lift inequalities could give a second algebraic obstruction. It
   is not needed for the exact facet proof and is not claimed as landed
   evidence.
4. `NOT ATTEMPTED` — exhaustive enumeration of all regular dissections could
   determine the regular-subspace maximum. The present result deliberately
   does not make that stronger claim.

**N2 — Open-condition independence.** These are walls only to broader physical
interpretations, not missing assumptions in the finite theorem.

| pair | first closes second? | second closes first? | independent? |
|---|---:|---:|---:|
| physical model selection / tick--Admissibility realization | no | no | yes |
| physical model selection / larger-block composition | no | no | yes |
| tick--Admissibility realization / larger-block composition | no | no | yes |

**N3 — Hidden-condition scan.** “Supplied” is explicit at the title, opening,
runner docstring, receipt, and boundary. “Regular” means only the lower hull of
corner heights. “Maximizer” means the exhibited cost-`320` witness attains the
independently certified finite ceiling. No “natural,” “standard,” or
framework-selected language supplies a missing physical bridge.

**N4 — Residual matching.** Cycle 728 supplies exactly the carried cost-`318`
witness and `[318,324]` window in the same spatial-block model; the runner binds
both through its receipt and literal. Cycle 728 does not supply lift-search
provenance or certificate-shape necessity, so neither is imported. The minimal
axioms and kinetic-isotropy note are premise sources, not no-go witnesses.

**N5 — Rhetoric audit.** The primary cached stdout carries substantive
`per_element:`, `per_site:`, `per_mode:`, `per_block:`, and `lattice_wide:`
execution-certificate lines. Only per-element and per-block finite checks are
executed. Per-mode and lattice-wide conclusions are explicitly not executed and
are not asserted.

**N6 — Partial-closure paths.** A physical cell/charge-selection result could
retire the supplied-model condition. A tick-realization bridge could retire the
tick condition. A separate composition theorem could extend the box domain. An
exhaustive regular-triangulation theorem could settle the regular-subspace
maximum. None is renamed as a required new axiom, and none is treated as closed.

**N7 — Steelman.** The strongest surviving objection is concrete: there may be
another cost-`320` dissection that is face-to-face and regular, and non-corner,
coarser, or nonsimplicial constructions need not obey this interval at all. That
objection defeats an all-maximizer or physical no-go. It does not defeat the
bounded statement about the one carried witness, whose exact cover, cost,
internal facets, and ceiling attainment are independently checked.

**N8 — Cross-cycle echo.** Reviews of Cycles 724--728 repeatedly found that
exact corner-simplex arithmetic does not select a physical assembly model.
Cycle 729 carries that supplied-model boundary forward. The submitted Cycle 729
also echoed two historical statements that did not survive Cycle 728 review;
they were removed rather than laundered into a new dependency claim.

Status: **PASS** for the finite obstruction above. The N5 lines land in the
primary cache with this packet.

## Review record

Review-loop iteration 1 (Codex, 2026-08-12) returned `FIX_THEN_PROCEED`. The
submitted interval and witness survived independent exact reconstruction. The
review demoted the physical framing to a supplied-model theorem, added the
kinetic-isotropy and direct Cycle 728 dependencies, removed unsupported Cycle
728 lift-search and certificate-shape history, narrowed the non-regularity
claim to the carried maximizer, tightened exact gates, made the runner
fail-closed, added a fully independent exact checker and hostile controls,
replaced the cold output with canonical content-pinned caches, generated the
receipt from the run, and landed the N1--N8/N5 packet. No audit verdict was
applied.
