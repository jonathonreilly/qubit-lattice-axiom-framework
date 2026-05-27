# S^3 Cap Finite Cone-Cap Construction Certificate

**Date:** 2026-04-12; narrowed 2026-05-27
**Script:** `scripts/frontier_s3_cap_uniqueness.py`
**Lane:** S^3 / compactification
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only

---

## Status

This row is a bounded finite construction certificate. It no longer claims
that the framework forces a unique cap among all possible PL closures, and it
does not identify the resulting compactification with `PL S^3`.

The legacy row name contains "uniqueness" because this note originally tried
to close the global cap-map uniqueness step. The current audited repair keeps
the useful finite mathematics and removes the imported global topology.

## Bounded Claim

For the explicit cubical-ball family constructed by the runner at radii
`R = 2, 3, 4, 5`, the checker proves these finite combinatorial facts:

1. The cubical ball is nonempty and has a nonempty cubical boundary.
2. The boundary quads, after a fixed diagonal triangulation, form a connected
   closed triangulated 2-manifold: every boundary edge has degree two and every
   boundary-vertex link is a cycle.
3. The boundary triangulation has Euler characteristic `chi = 2`.
4. Coning the boundary triangulation to one apex gives a finite tetrahedral
   cone-cap complex whose boundary is exactly the original boundary
   triangulation.
5. Every non-base cone face is paired by exactly two tetrahedra.
6. The link of the cone apex is exactly the original boundary triangulation.
7. The cone-cap complex has Euler characteristic `chi = 1`.

These statements are internal finite mathematics over the declared runner
family. They can be cited as a concrete cone-cap construction and boundary
matching certificate.

## What This Note Does Not Claim

- No proof that closure is physically mandatory.
- No derivation of the Kawamoto-Smit homogeneity premise.
- No proof that every admissible cap is PL-homeomorphic to the cone cap.
- No proof of PL Schoenflies, Alexander cone uniqueness, Alexander trick,
  mapping-class-group classification, van Kampen, Perelman, or Moise.
- No proof that the compactified lattice is `PL S^3`.
- No retained verdict, no direct ledger retag, and no downstream status
  propagation without independent audit.

## Relation To The Prior Textbook-Import Attempt

The previous version attempted to use standard global topology to prove:

> Any PL 3-complex cap that closes the cubical ball to a closed simply
> connected PL 3-manifold is PL-homeomorphic to the cone cap, hence the result
> is `PL S^3`.

That stronger statement depended on external PL Schoenflies/Alexander,
Perelman/Moise, mapping-class, van Kampen, and physical-closure premises. The
audit correctly treated those as unclosed imports. This repair does not
attempt to smuggle those authorities into the row.

Instead, it proves the part that is actually finite on the framework surface:
given the explicit cubical boundary produced by the runner, the cone-cap
construction is an exact finite tetrahedral construction whose boundary and
apex-link data match the source boundary.

## Relationship To The PL-Topology Finite Certificate

This note is parallel to
[`PL_TOPOLOGY_INFRASTRUCTURE_TEXTBOOK_IMPORT_NOTE_2026-05-17.md`](PL_TOPOLOGY_INFRASTRUCTURE_TEXTBOOK_IMPORT_NOTE_2026-05-17.md),
which was independently narrowed to a finite cone-cap construction certificate
for `R = 2, 3, 4`.

The present runner repeats the finite construction locally for this legacy S3
row and extends the checked radius set to `R = 5`. The dependency may be useful
cross-support, but this note's runner is the direct executable artifact for the
row being re-audited.

## Verification

Run:

```bash
python3 scripts/frontier_s3_cap_uniqueness.py
```

Expected result:

```text
S3 finite cone-cap construction certificate: PASS
PASS=52 FAIL=0
```

## Audit Request

Please re-audit this row at the narrowed scope above. The intended safe
scope is the bounded finite construction certificate above if the auditor
agrees that the runner closes the finite statements. The old global uniqueness
and `PL S^3` compactification claims are out of scope and should not be
propagated from this row. Any effective status is assigned only by the
independent audit lane.
