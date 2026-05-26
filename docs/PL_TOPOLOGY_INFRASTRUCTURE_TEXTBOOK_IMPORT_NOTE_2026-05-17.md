# PL-Topology Infrastructure — Finite Cone-Cap Boundary Certificate

**Date:** 2026-05-17; narrowed 2026-05-26
**Claim type:** bounded_theorem
**Status:** bounded support theorem. This row is narrowed to an executable
finite cone-cap construction certificate for the explicit cubical-ball
boundary family used by the compactification lane.
**Runner:** [`scripts/frontier_pl_topology_finite_cone_cap_certificate.py`](../scripts/frontier_pl_topology_finite_cone_cap_certificate.py)
**Status authority:** independent audit lane only.

## Purpose

This row no longer claims to establish the previous five named external
imports. It supplies a finite, auditable construction that downstream topology
work can cite only for the explicit cone-cap boundary facts below.

The checker constructs cubical balls at radii `R = 2, 3, 4`, extracts their
boundary squares, triangulates those squares by a fixed diagonal convention,
and cones the resulting boundary triangulation to one apex. It then verifies
integer combinatorial identities for the resulting finite complexes.

## Bounded Claim

For each checked radius `R = 2, 3, 4`:

1. The cubical boundary is connected and closed after the fixed
   triangulation: every boundary edge is incident to exactly two boundary
   triangles.
2. The boundary triangulation has Euler characteristic `chi = 2`.
3. The cone-cap tetrahedral complex has the boundary triangulation as exactly
   its boundary: each base triangle occurs once, and every apex-side face is
   paired by two tetrahedra.
4. The link of the cone apex is exactly the original boundary triangulation.
5. The cone-cap complex has Euler characteristic `chi = 1`.

These are finite construction facts about the declared runner family. They do
not classify arbitrary PL caps and do not identify any physical compactified
space.

## What This Note Does Not Claim

- No derivation of PL Schoenflies, Alexander's cone theorem, the Alexander
  trick, any mapping-class-group theorem, Perelman, Moise, or van Kampen.
- No derivation of the Kawamoto-Smit homogeneity premise.
- No proof that every admissible cap is PL-homeomorphic to the cone cap.
- No proof that the compactified lattice is `S^3`.
- No physical closure theorem, no staggered-fermion realization theorem, and no
  new axiom.
- No audit verdict and no direct ledger retag. Independent audit must decide
  whether this bounded finite certificate can be retained as
  `retained_bounded`.

## Relationship To The Older Import Wrapper

The earlier version of this row bundled four PL-topology / geometric-topology
theorems and one lattice-QFT homogeneity premise as named non-derivation
imports. That scope did not close under audit because the row did not derive
those external authorities or provide retained one-hop handles for them.

This repair deliberately abandons that broader wrapper scope. Any downstream
argument that still needs global Schoenflies-style exhaustiveness,
Perelman/Moise identification, mapping-class gluing uniqueness, or the
Kawamoto-Smit physical-closure premise must cite or derive those authorities
separately. This row contributes only the finite cone-cap construction
certificate above.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_pl_topology_finite_cone_cap_certificate.py
```

Expected result:

```text
PL finite cone-cap certificate: PASS
PASS=36 FAIL=0
```
