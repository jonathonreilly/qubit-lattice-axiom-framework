# S^3 General-R — Finite-Radius Cap Certificate

**Date:** 2026-04-13; narrowed 2026-05-28
**Claim type:** bounded_theorem
**Status:** bounded support theorem. This row is narrowed to the finite-radius
PL cap construction and boundary-link certificate scope that its retained
one-hop dependencies actually establish. It does not claim unrestricted all-R
PL cap closure, global uniqueness, physical closure, or `PL S^3`
identification.
**Status authority:** independent audit lane only
**Primary runner:** [`scripts/frontier_s3_cap_uniqueness.py`](../scripts/frontier_s3_cap_uniqueness.py) (finite cone-cap construction certificate, PASS=52 FAIL=0)

---

## Status

This row is narrowed to a bounded finite-radius certificate. It previously
claimed the S^3 lane was CLOSED for all `R >= 2` via the PL Poincare
conjecture, with compactification uniqueness and framework-level physical
selection both RESOLVED. The audit lane correctly treated those broader
statements as exceeding the support actually carried by the retained one-hop
dependencies.

The retained one-hop dependencies are `retained_bounded` only for
finite-radius certificates. This repair keeps exactly the finite mathematics
those dependencies establish and removes the unrestricted all-R closure,
global uniqueness, physical closure, and `PL S^3` identification claims.

## Setup

Let `B_R` be the cubical ball of radius `R` in `Z^3` (the union of all unit
cubes whose 8 corners lie within Euclidean distance `R` of the origin), and let

    M_R = B_R  cup  cone(partial B_R)

be the cone-capped closure. The bounded certificate below concerns the explicit
cubical-ball boundary family at the finite radii checked by the runners.

## Bounded Claim

For the explicit cubical-ball family at the finite radii checked by the runners,
the following finite combinatorial facts are established by direct computation.

### Part A. Boundary-vertex link disk certificate

From the retained boundary-link dependency
([S3_BOUNDARY_LINK_THEOREM_NOTE.md](S3_BOUNDARY_LINK_THEOREM_NOTE.md),
runner `scripts/frontier_s3_boundary_link_theorem.py`):

1. For every checked `R = 2..10` and every boundary vertex `v` of `B_R`, the
   vertex link `link(v, B_R)` is a PL 2-disk, verified by direct finite
   computation on the actual cubical-ball links (5,778 boundary vertices,
   0 failures).
2. For every nonempty proper subset `P` of `{0, -1}^3` whose `P` side and
   complement are both connected in `Q_3`, the simplicial closure `K_simp(P)`
   inside the standard octahedral `S^2` is a PL 2-disk, by exhaustive
   126-subset enumeration.

The disk-capping consequence `link(v, M_R) = link(v, B_R) cup_{boundary}
cone(boundary)` is a PL 2-sphere wherever the boundary-link disk property is
established, by the constructive disk-capping lemma. Interior-vertex links are
the octahedral boundary `S^2` by the local 3x3x3 argument, and the cone-point
link is `partial B_R`.

### Part B. Finite cone-cap construction certificate

From the retained cap-construction dependency
([S3_CAP_UNIQUENESS_NOTE.md](S3_CAP_UNIQUENESS_NOTE.md),
runner `scripts/frontier_s3_cap_uniqueness.py`), for the cubical-ball family at
radii `R = 2, 3, 4, 5`:

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
families. They can be cited as a concrete finite-radius cone-cap construction,
boundary-link disk, and boundary-matching certificate.

## Out Of Scope / Open

The retained one-hop dependencies are `retained_bounded` for finite-radius
certificates only. They explicitly do NOT supply the following, and this note
does NOT claim any of them. Each is framed as an open follow-on, not a
foreclosure.

1. **Unrestricted all-R PL cap closure.** The finite cone-cap construction is
   checked at the explicit radii `R = 2, 3, 4, 5` (Part B) and the boundary-link
   disk property at `R = 2..10` (Part A); the unrestricted all-R PL cap closure
   is not established here. The boundary-link dependency leaves the
   large-coordinate (`v_i <= -2`) bridge-lemma analytic closure open, so the
   all-R disk theorem itself is not closed. Closing the bridge lemma and the
   all-R cap construction is an open follow-on.
2. **Global uniqueness.** No proof that every admissible cap is
   PL-homeomorphic to the cone cap. The retained cap dependency supplies a
   construction certificate, not a global cap-map uniqueness theorem
   (no PL Schoenflies, Alexander cone uniqueness, Alexander trick, or
   mapping-class-group classification is derived). Establishing global cap
   uniqueness is an open follow-on.
3. **Physical closure.** No proof that closure of the open cubical ball is
   physically mandatory, and no derivation of the Kawamoto-Smit homogeneity
   premise. Whether the framework Hamiltonian forces closure is an open
   follow-on.
4. **PL S^3 identification.** No proof that the compactified lattice `M_R` is
   `PL S^3`. The PL Poincare conjecture (Perelman 2003) and the TOP/PL
   equivalence in dimension 3 (Moise) are not discharged on the framework
   surface here; van Kampen `pi_1 = 0` for `M_R` is likewise not carried as a
   retained handle by these dependencies. Identifying `M_R` with `PL S^3` is an
   open follow-on.

## What This Note Does Not Claim

- No unrestricted all-R PL cap closure.
- No global cap-map uniqueness; no proof that every admissible cap is
  PL-homeomorphic to the cone cap.
- No proof that closure is physically mandatory; no derivation of the
  Kawamoto-Smit homogeneity premise.
- No proof that the compactified lattice is `PL S^3`.
- No proof of PL Schoenflies, Alexander cone uniqueness, the Alexander trick,
  mapping-class-group classification, van Kampen, Perelman, or Moise.
- No retained verdict, no direct ledger retag, and no downstream status
  propagation without independent audit.

## Relation To The Prior Broad-Closure Attempt

The previous version of this row asserted:

> The cone-capped cubical ball `M_R = B_R cup cone(partial B_R)` is PL
> homeomorphic to `S^3` for every `R >= 2`, with compactification uniqueness
> and framework-level physical selection both resolved; the lane is CLOSED.

That stronger statement depended on the PL Poincare conjecture (Perelman),
TOP/PL equivalence (Moise), van Kampen `pi_1` closure, global cap-map
uniqueness, and a physical-closure premise. The audit correctly treated those
as unclosed on the framework surface, because the retained one-hop
dependencies do not derive those external authorities or carry retained
handles for them.

This repair does not attempt to smuggle those authorities into the row.
Instead it keeps the part that is finite over the declared runner families:
the boundary-link disk certificate (Part A) and the cone-cap construction
certificate (Part B). Any downstream argument that still needs the all-R cap
closure, global cap uniqueness, physical closure, or `PL S^3` identification
must cite or derive those separately.

## Relationship To The Companion Finite Certificates

This note is parallel to two independently narrowed finite certificates over
the same cubical-ball boundary family:

- [`S3_CAP_UNIQUENESS_NOTE.md`](S3_CAP_UNIQUENESS_NOTE.md) — finite cone-cap
  construction certificate (`R = 2, 3, 4, 5`), the direct executable artifact
  for Part B.
- [`PL_TOPOLOGY_INFRASTRUCTURE_TEXTBOOK_IMPORT_NOTE_2026-05-17.md`](PL_TOPOLOGY_INFRASTRUCTURE_TEXTBOOK_IMPORT_NOTE_2026-05-17.md)
  — finite cone-cap construction certificate (`R = 2, 3, 4`), parallel
  cross-support.

The boundary-link disk certificate (Part A) is supplied by
[`S3_BOUNDARY_LINK_THEOREM_NOTE.md`](S3_BOUNDARY_LINK_THEOREM_NOTE.md).

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

The boundary-link disk certificate (Part A) is verified by the dependency
runner:

```bash
python3 scripts/frontier_s3_boundary_link_theorem.py
```

## Citations

This section registers explicit dependency edges for the retained one-hop
authorities supporting each part of the bounded claim above; the markdown links
register them as one-hop dependency edges in the citation graph.

- [S3_CAP_UNIQUENESS_NOTE.md](S3_CAP_UNIQUENESS_NOTE.md) — supplies the finite
  cone-cap construction certificate (Part B), corroborated by the runner
  `scripts/frontier_s3_cap_uniqueness.py` (PASS=52 FAIL=0).
- [S3_BOUNDARY_LINK_THEOREM_NOTE.md](S3_BOUNDARY_LINK_THEOREM_NOTE.md) —
  supplies the boundary-vertex link disk certificate (Part A); runner
  `scripts/frontier_s3_boundary_link_theorem.py`.

The runner-side artifacts are:

- `scripts/frontier_s3_cap_uniqueness.py` — finite cone-cap construction
  certificate at `R = 2, 3, 4, 5` (PASS=52 FAIL=0); the direct executable
  artifact for this row.
- `scripts/frontier_s3_boundary_link_theorem.py` — boundary-vertex link disk
  verification at `R = 2..10` plus the exhaustive 126-subset combinatorial
  certificate.

## Audit Request

Please re-audit this row at the narrowed scope above. The intended safe scope
is the finite-radius PL cap construction and boundary-link disk certificate
(Parts A and B) if the auditor agrees that the retained one-hop dependencies
close those finite statements. The unrestricted all-R PL cap closure, global
uniqueness, physical closure, and `PL S^3` identification claims are out of
scope and should not be propagated from this row. Any effective status is
assigned only by the independent audit lane.
